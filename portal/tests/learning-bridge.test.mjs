import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

// The bridge schedules flushes through window timers.
globalThis.window ??= globalThis;

const { ParentLearningBridge } = await import("../src/learning/bridge.ts");

const registry = JSON.parse(
  await readFile(new URL("../public/games.json", import.meta.url), "utf8"),
);

const NEW_GAMES = [
  { id: "dragon-hold", appUrl: "https://dragon.typing-game.local", path: "/dragon-hold" },
  { id: "typing-defense", appUrl: "https://td.typing-game.local", path: "/typing-defense" },
  { id: "typing-survival", appUrl: "https://survival.typing-game.local", path: "/typing-survival" },
  { id: "immortality-cultivation", appUrl: "https://tutien.typing-game.local", path: "/immortality-cultivation" },
];

const EXPECTED_GROUPS = {
  monkeytype: "practice",
  "recall-typing": "practice",
  "karaoke-typing": "practice",
  "vocab-shooter": "battle",
  "space-typing": "battle",
  "dragon-hold": "battle",
  "typing-defense": "battle",
  "typing-survival": "battle",
  "immortality-cultivation": "battle",
};

function registeredGame(id) {
  const game = registry.games.find((entry) => entry.id === id);
  assert.ok(game, `${id} is registered in games.json`);
  return game;
}

function makeStore() {
  return {
    applied: [],
    async applyMany(events) {
      this.applied.push(...events);
    },
    async load() {
      throw new Error("not used");
    },
  };
}

function makeFrame() {
  const posted = [];
  return {
    posted,
    contentWindow: {
      postMessage(message, targetOrigin) {
        posted.push({ message, targetOrigin });
      },
    },
  };
}

function attempt(gameId, requestId) {
  return {
    type: "typing-game:learning:v1:attempt",
    requestId,
    event: {
      version: 1,
      entityType: "vocabulary",
      entityId: "lantern",
      gameId,
      activityType: "typing-attack",
      result: "correct",
      occurredAt: "2026-10-23T08:00:00.000Z",
      responseMs: 900,
    },
  };
}

test("registry groups every game and lists the new games", () => {
  assert.deepEqual(
    Object.fromEntries(registry.games.map((game) => [game.id, game.group])),
    EXPECTED_GROUPS,
  );
  for (const expected of NEW_GAMES) {
    const game = registeredGame(expected.id);
    assert.equal(game.appUrl, expected.appUrl);
    assert.equal(game.path, expected.path);
  }
});

for (const expected of NEW_GAMES) {
  test(`bridge accepts ${expected.id} events from its registered origin`, async () => {
    const game = registeredGame(expected.id);
    const store = makeStore();
    const applied = [];
    const bridge = new ParentLearningBridge(store, (event) => applied.push(event));
    const frame = makeFrame();

    const handled = bridge.handleMessage(
      {
        data: attempt(game.id, `req-${game.id}`),
        origin: new URL(game.appUrl).origin,
        source: frame.contentWindow,
      },
      frame,
      game,
    );
    await bridge.flush();

    assert.equal(handled, true);
    assert.equal(store.applied.length, 1);
    assert.equal(store.applied[0].gameId, game.id);
    assert.equal(applied.length, 1);
    assert.deepEqual(frame.posted, [
      {
        message: { type: "typing-game:learning:v1:ack", requestId: `req-${game.id}` },
        targetOrigin: expected.appUrl,
      },
    ]);
  });

  test(`bridge rejects ${expected.id} events from a wrong origin`, async () => {
    const game = registeredGame(expected.id);
    const store = makeStore();
    const bridge = new ParentLearningBridge(store);
    const frame = makeFrame();

    for (const origin of [
      "https://space.typing-game.local",
      "https://evil.example",
      `http://${new URL(game.appUrl).host}`,
    ]) {
      const handled = bridge.handleMessage(
        { data: attempt(game.id, "req-wrong-origin"), origin, source: frame.contentWindow },
        frame,
        game,
      );
      assert.equal(handled, true, "learning messages are consumed, not forwarded");
    }
    await bridge.flush();

    assert.equal(store.applied.length, 0);
    assert.equal(frame.posted.length, 0);
  });
}

test("bridge rejects a gameId that does not match the active game", async () => {
  const game = registeredGame("dragon-hold");
  const store = makeStore();
  const bridge = new ParentLearningBridge(store);
  const frame = makeFrame();

  bridge.handleMessage(
    {
      data: attempt("typing-survival", "req-wrong-game"),
      origin: new URL(game.appUrl).origin,
      source: frame.contentWindow,
    },
    frame,
    game,
  );
  await bridge.flush();

  assert.equal(store.applied.length, 0);
  assert.equal(frame.posted.length, 1);
  assert.equal(frame.posted[0].message.type, "typing-game:learning:v1:error");
  assert.equal(frame.posted[0].message.error.code, "invalid-request");
  assert.equal(frame.posted[0].targetOrigin, game.appUrl);
});

test("bridge ignores messages from a window other than the game frame", async () => {
  const game = registeredGame("typing-defense");
  const store = makeStore();
  const bridge = new ParentLearningBridge(store);
  const frame = makeFrame();
  const stranger = makeFrame();

  bridge.handleMessage(
    {
      data: attempt(game.id, "req-other-window"),
      origin: new URL(game.appUrl).origin,
      source: stranger.contentWindow,
    },
    frame,
    game,
  );
  await bridge.flush();

  assert.equal(store.applied.length, 0);
  assert.equal(frame.posted.length, 0);
  assert.equal(stranger.posted.length, 0);
});
