import { describe, expect, it } from "vitest";
import {
  LearningBridge,
  LearningBridgeError,
  buildCombatLearningEvent,
  type BridgeHost,
  type QueueStorage,
} from "./index";

const GAME = "dragon-hold";
const ORIGIN = "https://typing-game.local";

function memoryStorage(): QueueStorage & { data: Map<string, unknown> } {
  const data = new Map<string, unknown>();
  return {
    data,
    readJson: (key) => (data.has(key) ? JSON.parse(JSON.stringify(data.get(key))) : null),
    writeJson: (key, value) => {
      data.set(key, value);
      return true;
    },
  };
}

function fakeHost(framed: boolean) {
  const posted: Array<{ message: Record<string, unknown>; origin: string }> = [];
  const listeners = new Set<(event: MessageEvent<unknown>) => void>();
  const timers = new Map<number, () => void>();
  let nextTimer = 0;
  const parent = { postMessage: (message: unknown, origin: string) => posted.push({ message: message as Record<string, unknown>, origin }) };
  const host: BridgeHost = {
    parent: framed ? parent : null,
    addEventListener: (_type, listener) => listeners.add(listener),
    removeEventListener: (_type, listener) => listeners.delete(listener),
    setTimeout: (callback) => {
      nextTimer += 1;
      timers.set(nextTimer, callback);
      return nextTimer;
    },
    clearTimeout: (handle) => timers.delete(handle as number),
    now: () => 1_000,
  };
  return {
    host,
    posted,
    timers,
    deliver(data: unknown, options: { origin?: string; source?: unknown } = {}) {
      const event = { data, origin: options.origin ?? ORIGIN, source: options.source ?? parent } as MessageEvent<unknown>;
      for (const listener of listeners) listener(event);
    },
    fireTimers() {
      for (const [id, callback] of [...timers]) {
        timers.delete(id);
        callback();
      }
    },
  };
}

const entry = { id: "fire", en: "fire", vi: "lửa", ipa: "" };

describe("learning bridge", () => {
  it("refuses to start without a gameId", () => {
    expect(() => new LearningBridge({ gameId: "", host: fakeHost(true).host, storage: memoryStorage() })).toThrow("gameId is required");
  });

  it("posts attempts to the portal origin with this game's id", () => {
    const fake = fakeHost(true);
    const bridge = new LearningBridge({ gameId: GAME, host: fake.host, storage: memoryStorage() });
    bridge.sendAttempt(buildCombatLearningEvent({ gameId: GAME, entry, perfect: true }));
    expect(fake.posted).toHaveLength(1);
    expect(fake.posted[0]!.origin).toBe(ORIGIN);
    expect(fake.posted[0]!.message).toMatchObject({ type: "typing-game:learning:v1:attempt", event: { gameId: GAME } });
    expect(String(fake.posted[0]!.message["requestId"])).toMatch(/^dragon-hold-[a-z0-9]+-1$/);
    expect(() => bridge.sendAttempt(buildCombatLearningEvent({ gameId: "space-typing", entry, perfect: true }))).toThrow("is not dragon-hold");
  });

  it("queues attempts without a portal and sends them once inside one", () => {
    const storage = memoryStorage();
    const alone = new LearningBridge({ gameId: GAME, host: fakeHost(false).host, storage, maxQueue: 2 });
    expect(alone.embedded).toBe(false);
    for (const perfect of [true, false, true]) alone.sendAttempt(buildCombatLearningEvent({ gameId: GAME, entry, perfect }));
    expect(alone.queued().map((event) => event.result)).toEqual(["wrong", "correct"]);

    const fake = fakeHost(true);
    const framed = new LearningBridge({ gameId: GAME, host: fake.host, storage });
    expect(fake.posted.map((post) => post.message["type"])).toEqual([
      "typing-game:learning:v1:attempt",
      "typing-game:learning:v1:attempt",
    ]);
    expect(framed.queued()).toEqual([]);
  });

  it("resolves a query with the portal's result and ignores other origins", async () => {
    const fake = fakeHost(true);
    const bridge = new LearningBridge({ gameId: GAME, host: fake.host, storage: memoryStorage() });
    const answer = bridge.query({ entityType: "vocabulary", pageSize: 25 });
    const sent = fake.posted[0]!.message;
    expect(sent["type"]).toBe("typing-game:learning:v1:query");
    fake.deliver({ type: "typing-game:learning:v1:query-result", requestId: sent["requestId"], result: { total: 9 } }, { origin: "https://evil.local" });
    fake.deliver({ type: "typing-game:learning:v1:query-result", requestId: sent["requestId"], result: { total: 3 } });
    await expect(answer).resolves.toEqual({ total: 3 });
    expect(fake.timers.size).toBe(0);
  });

  it("rejects a lookup the portal refuses, one that times out, and one without a portal", async () => {
    const fake = fakeHost(true);
    const bridge = new LearningBridge({ gameId: GAME, host: fake.host, storage: memoryStorage() });
    const refused = bridge.lookup([" Fire ", "fire", "river"]);
    const sent = fake.posted[0]!.message;
    expect(sent).toMatchObject({ type: "typing-game:learning:v1:lookup", query: { entityType: "vocabulary", entityIds: ["fire", "river"] } });
    fake.deliver({ type: "typing-game:learning:v1:error", requestId: sent["requestId"], error: { code: "invalid-request", message: "not supported" } });
    await expect(refused).rejects.toMatchObject({ code: "portal-error", message: "not supported" });

    const slow = bridge.lookup(["fire"]);
    fake.fireTimers();
    await expect(slow).rejects.toBeInstanceOf(LearningBridgeError);

    await expect(bridge.lookup(Array.from({ length: 201 }, (_, index) => "w" + String(index)))).rejects.toThrow("1 to 200");
    const alone = new LearningBridge({ gameId: GAME, host: fakeHost(false).host, storage: memoryStorage() });
    await expect(alone.query({ entityType: "vocabulary" })).rejects.toMatchObject({ code: "no-portal" });
  });

  it("asks the portal for focus, reports speech and hands portal messages to listeners", () => {
    const fake = fakeHost(true);
    const bridge = new LearningBridge({ gameId: GAME, host: fake.host, storage: memoryStorage() });
    expect(bridge.requestFocus()).toBe(true);
    bridge.speechActive(true);
    expect(fake.posted.map((post) => post.message)).toEqual([
      { type: "typing-game:request-focus", gameId: GAME },
      { type: "typing-game:speech", active: true },
    ]);

    const music: boolean[] = [];
    const stop = bridge.onSharedMusic((playing) => music.push(playing));
    fake.deliver({ type: "typing-game:shared-music", playing: true });
    fake.deliver({ type: "typing-game:shared-music", playing: false }, { source: {} });
    stop();
    fake.deliver({ type: "typing-game:shared-music", playing: false });
    expect(music).toEqual([true]);

    const datasets: unknown[] = [];
    bridge.onMessage("typing-game:learning:v1:review-dataset", (data) => datasets.push(data["requestId"]));
    fake.deliver({ type: "typing-game:learning:v1:review-dataset", requestId: "r1" });
    expect(datasets).toEqual(["r1"]);

    bridge.dispose();
    expect(bridge.requestFocus()).toBe(false);
  });
});
