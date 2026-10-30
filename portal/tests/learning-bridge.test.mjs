import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import { applyLearningEvents } from "../../shared/learning/core.mjs";
import { parseLearningProfileBackup } from "../../shared/learning/profile-backup.mjs";

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

// 233 P1-233-01: an answer nested inside a sample field must not reach the game frame.
const PREFIX = "typing-game:learning:v1:";
const SAMPLE_FIELDS = ["occurredAt", "gameId", "activityType", "result", "hintUsed"];
const NESTED = {
  object: () => ({ userAnswer: "PRIVATE_NESTED_USER_ANSWER", expectedAnswer: "PRIVATE_NESTED_EXPECTED_ANSWER" }),
  array: () => [{ userAnswer: "PRIVATE_NESTED_USER_ANSWER", expectedAnswer: "PRIVATE_NESTED_EXPECTED_ANSWER" }],
};

function twoSampleProfile() {
  const sample = { version: 1, entityType: "vocabulary", entityId: "lantern", gameId: "dragon-hold" };
  return applyLearningEvents(null, [
    { ...sample, activityType: "meaning-recall", result: "correct", occurredAt: "2026-10-30T06:00:00.000Z" },
    { ...sample, activityType: "listening", result: "correct", occurredAt: "2026-10-30T06:01:00.000Z", hintUsed: true },
  ]);
}

async function askFromFrame(profile, type) {
  const game = registeredGame("dragon-hold");
  const origin = new URL(game.appUrl).origin;
  const frame = makeFrame();
  const store = {
    profile, loads: 0,
    async load() { this.loads++; return this.profile; },
    async applyMany() { throw new Error("unexpected write"); },
  };
  const query = type === "lookup" ? { entityType: "vocabulary", entityIds: ["lantern"] } : { entityType: "vocabulary" };
  new ParentLearningBridge(store).handleMessage(
    { data: { type: PREFIX + type, requestId: "f2-types", query }, origin, source: frame.contentWindow },
    frame,
    game,
  );
  // Query handlers are fire-and-forget; one turn drains them.
  await new Promise((resolve) => setImmediate(resolve));
  assert.equal(frame.posted.length, 1);
  assert.equal(frame.posted[0].targetOrigin, origin);
  assert.equal(frame.posted[0].message.type, PREFIX + "query-result");
  assert.equal(frame.posted[0].message.requestId, "f2-types");
  assert.equal(store.loads, 1);
  return frame.posted;
}

for (const source of ["stored", "backup"]) {
  for (const field of SAMPLE_FIELDS) {
    for (const type of ["lookup", "query"]) {
      test(`F2 types ${type} from a ${source} profile drops a sample whose ${field} nests an answer`, async () => {
        for (const [kind, nested] of Object.entries(NESTED)) {
          let profile = twoSampleProfile();
          const kept = structuredClone(profile.vocabulary.lantern.recentSamples[1]);
          profile.vocabulary.lantern.recentSamples[0][field] = nested();
          if (source === "backup") {
            profile = parseLearningProfileBackup(JSON.stringify(profile));
            assert.deepEqual(profile.vocabulary.lantern.recentSamples, [kept], kind);
          }
          const before = structuredClone(profile);
          const posted = await askFromFrame(profile, type);
          const samples = posted[0].message.result.items[0].recentSamples;
          assert.deepEqual(samples, [kept], kind);
          assert.deepEqual(Object.keys(samples[0]).sort(), [...SAMPLE_FIELDS].sort());
          assert.doesNotMatch(JSON.stringify(posted), /PRIVATE_NESTED_/, kind);
          assert.deepEqual(profile, before, kind);
        }
      });
    }
  }
}
