import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import { parseLearningProfileBackup } from "../../shared/learning/profile-backup.mjs";
import { applyLearningEvents, calculateMastery, normalizeVocabularyKey } from "../../shared/learning/core.mjs";

globalThis.window ??= globalThis;
const { ParentLearningBridge } = await import("../src/learning/bridge.ts");
const registry = JSON.parse(await readFile(new URL("../public/games.json", import.meta.url), "utf8"));
const PREFIX = "typing-game:learning:v1:";
const NOW = "2026-10-30T06:00:00.000Z";
function attempt(extra = {}) {
  return { version: 1, entityType: "vocabulary", entityId: "lantern", gameId: "recall-typing", activityType: "meaning-recall", result: "correct", occurredAt: NOW, ...extra };
}
function setup(id = "dragon-hold", events = [attempt()]) {
  const game = registry.games.find((entry) => entry.id === id);
  assert.ok(game);
  const origin = new URL(game.appUrl).origin;
  const posted = [], callbacks = [];
  const frame = { contentWindow: { postMessage(message, targetOrigin) { posted.push({ message, targetOrigin }); } } };
  const store = {
    profile: applyLearningEvents(null, events), loads: 0, writes: 0,
    async applyMany(batch) { this.writes++; this.profile = applyLearningEvents(this.profile, batch); },
    async load() { this.loads++; return this.profile; },
  };
  const bridge = new ParentLearningBridge(store, (event) => callbacks.push(event));
  function send(data, extra = {}, activeFrame = frame, activeGame = game) {
    return bridge.handleMessage({ data, source: frame.contentWindow, origin, ...extra }, activeFrame, activeGame);
  }
  return { game, origin, frame, store, posted, callbacks, bridge, send };
}
function request(query = { entityType: "vocabulary", entityIds: ["lantern"] }, requestId = "lookup-1") {
  return { type: PREFIX + "lookup", requestId, query };
}
// Async handlers are fire-and-forget; a turn drains their promise continuations.
async function settle() { await new Promise((resolve) => setImmediate(resolve)); }
function expectResult(s, requestId = "lookup-1") {
  assert.equal(s.posted.length, 1);
  assert.equal(s.posted[0].message.type, PREFIX + "query-result");
  assert.equal(s.posted[0].message.requestId, requestId);
  assert.equal(s.posted[0].targetOrigin, s.origin);
  return s.posted[0].message.result;
}
function expectError(s, code = "invalid-request") {
  assert.equal(s.posted.length, 1);
  assert.equal(s.posted[0].message.type, PREFIX + "error");
  assert.equal(s.posted[0].message.requestId, "lookup-1");
  assert.equal(s.posted[0].message.error.code, code);
  assert.equal(s.posted[0].targetOrigin, s.origin);
}
for (const id of ["dragon-hold", "typing-defense", "typing-survival"]) {
  test(`lookup replies once to registered ${id}`, async () => {
    const s = setup(id);
    assert.equal(s.send(request()), true);
    await settle();
    assert.equal(expectResult(s).items[0].entityId, "lantern");
    assert.equal(s.store.loads, 1);
  });
}
for (const source of ["space origin", "hostile origin", "http origin", "stranger", "no frame", "no game"]) {
  test(`lookup silently ignores ${source} without loading`, async () => {
    const s = setup();
    const extra = source === "stranger" ? { source: {} } : source === "space origin" ? { origin: "https://space.typing-game.local" } : source === "hostile origin" ? { origin: "https://evil.example" } : source === "http origin" ? { origin: "http://" + new URL(s.game.appUrl).host } : {};
    assert.equal(s.send(request(), extra, source === "no frame" ? null : s.frame, source === "no game" ? null : s.game), true);
    await settle();
    assert.equal(s.store.loads, 0);
    assert.deepEqual(s.posted, []);
  });
}
test("lookup accepts 200 ids", async () => {
  const ids = Array.from({ length: 200 }, (_, i) => "word" + i);
  const s = setup("dragon-hold", ids.map((entityId) => attempt({ entityId })));
  s.send(request({ entityType: "vocabulary", entityIds: ids }));
  await settle();
  assert.equal(expectResult(s).items.length, 200);
});
test("lookup rejects 201 ids before loading, even duplicates", async () => {
  const s = setup();
  s.send(request({ entityType: "vocabulary", entityIds: Array(201).fill("lantern") }));
  await settle();
  expectError(s);
  assert.equal(s.store.loads, 0);
});
test("lookup omits new words and constructor, normalizing known words", async () => {
  const s = setup();
  s.send(request({ entityType: "vocabulary", entityIds: ["Lantern ", "dragon", "constructor"] }));
  await settle();
  assert.deepEqual(expectResult(s).items.map((item) => item.entityId), ["lantern"]);
});
for (const [name, query] of [
  ["not object", null], ["array query", []], ["ids not array", { entityType: "vocabulary", entityIds: "a" }],
  ["non-string id", { entityType: "vocabulary", entityIds: [1] }],
  ["long id", { entityType: "vocabulary", entityIds: ["a".repeat(201)] }],
  ["unknown type", { entityType: "word", entityIds: ["a"] }],
  ["empty array", { entityType: "vocabulary", entityIds: [] }],
  ["empty ids", { entityType: "vocabulary", entityIds: [" ", "\t"] }],
]) {
  test(`lookup rejects ${name} with matching requestId`, async () => {
    const s = setup();
    s.send(request(query));
    await settle();
    expectError(s);
    assert.equal(s.store.loads, 0);
  });
}
test("lookup does not reply to invalid requestId", async () => {
  const s = setup();
  s.send(request(undefined, "bad request id"));
  await settle();
  assert.equal(s.store.loads, 0);
  assert.deepEqual(s.posted, []);
});
test("lookup flushes an attempt from the same turn before reading", async () => {
  const s = setup("dragon-hold", []);
  s.send({ type: PREFIX + "attempt", requestId: "attempt-1", event: attempt({ gameId: s.game.id }) });
  s.send(request());
  await settle();
  assert.equal(s.posted.length, 2);
  assert.equal(s.posted[0].message.type, PREFIX + "ack");
  assert.equal(s.posted[1].message.type, PREFIX + "query-result");
  assert.equal(s.posted[1].message.result.items[0].attempts, 1);
  assert.equal(s.store.writes, 1);
  assert.equal(s.store.loads, 1);
});
test("lookup returns query-failed when the store cannot load", async () => {
  const s = setup();
  s.store.load = async () => { throw new Error("read failed"); };
  s.send(request());
  await settle();
  expectError(s, "query-failed");
});
test("lookup leaves the profile intact and never calls onApplied", async () => {
  const s = setup();
  const before = structuredClone(s.store.profile);
  s.send(request());
  await settle();
  expectResult(s);
  assert.deepEqual(s.store.profile, before);
  assert.equal(s.store.writes, 0);
  assert.deepEqual(s.callbacks, []);
});

// Dragonhold HEAD 1f1de484afd5092f5967454fab5f4e6edd3189c9:
// src/app/learning.ts RECALLS/isRightRecall and parseLookup rules (20-30, 170-194).
// LEARNING.weakMastery is 40 (src/content/rules.ts:622); normalization matches kit/events.ts:90-92.
const RECALLS = new Set(["meaning-recall", "listening", "review-card"]);
const isRightRecall = (activityType, result, hintUsed) => RECALLS.has(String(activityType)) && result === "correct" && hintUsed !== true;
function parseLookup(value, now) {
  const out = new Map();
  const object = value !== null && typeof value === "object" ? value : null;
  let rows = [];
  if (Array.isArray(value)) rows = value;
  else if (object && Array.isArray(object["items"])) rows = object["items"];
  else if (object && object["records"] !== null && typeof object["records"] === "object") {
    rows = Object.entries(object["records"]).map(([entityId, record]) => ({ entityId, ...record }));
  }
  for (const row of rows) {
    if (row === null || typeof row !== "object") continue;
    const record = row;
    const id = record["entityId"] ?? record["wordKey"];
    if (typeof id !== "string") continue;
    const mastery = typeof record["mastery"] === "number" ? Math.max(0, Math.min(100, record["mastery"])) : 0;
    const next = typeof record["nextReviewAt"] === "string" ? Date.parse(record["nextReviewAt"]) : Number.NaN;
    const samples = [record["recentAnswers"], record["recentSamples"]].flatMap((list) => (Array.isArray(list) ? list : []));
    const recalls = samples.filter((s) => s !== null && typeof s === "object" && isRightRecall(s["activityType"], s["result"], s["hintUsed"])).length;
    out.set(normalizeVocabularyKey(id), { mastery, due: (Number.isFinite(next) && next <= now) || mastery < 40, recalls });
  }
  return out;
}
test("lookup matches Dragonhold recall reader with two independent right recalls", async () => {
  const activities = [
    ["typing-attack", "correct", false], ["meaning-recall", "correct", false],
    ["review-card", "correct", true], ["listening", "correct", false], ["meaning-recall", "wrong", false],
  ];
  const s = setup("dragon-hold", activities.map(([activityType, result, hintUsed]) => attempt({ activityType, result, hintUsed })));
  s.send(request());
  await settle();
  const result = expectResult(s);
  const now = new Date().toISOString();
  const parsed = parseLookup(result, Date.parse(now)).get("lantern");
  assert.equal(parsed.recalls, 2);
  assert.equal(parsed.mastery, calculateMastery(s.store.profile.vocabulary.lantern, now));
  assert.equal(typeof result.items[0].nextReviewAt, "string");
  assert.ok(Number.isFinite(Date.parse(result.items[0].nextReviewAt)));
});
test("existing query dispatch still flushes and returns paginated records", async () => {
  const s = setup();
  s.send({ type: PREFIX + "query", requestId: "query-1", query: { entityType: "vocabulary" } });
  await settle();
  assert.equal(expectResult(s, "query-1").totalItems, 1);
});

for (const [entityType, collection] of [["vocabulary", "vocabulary"], ["grammar", "grammar"], ["sentence", "sentences"]]) {
  for (const type of ["lookup", "query"]) {
    test(`F2 ${type} sends only contracted sample fields from a ${entityType} backup`, async () => {
      const s = setup("dragon-hold", [attempt({ entityType })]);
      const expected = structuredClone(s.store.profile[collection].lantern.recentSamples);
      Object.assign(s.store.profile[collection].lantern.recentSamples[0], {
        userAnswer: "PRIVATE_USER_ANSWER", expectedAnswer: "PRIVATE_EXPECTED_ANSWER",
        extra: { answer: "PRIVATE_EXTRA" },
      });
      s.store.profile = parseLearningProfileBackup(JSON.stringify(s.store.profile));
      const before = structuredClone(s.store.profile);
      s.send({ ...request({ entityType, entityIds: ["lantern"] }), type: PREFIX + type });
      await settle();
      assert.deepEqual(expectResult(s).items[0].recentSamples, expected);
      assert.doesNotMatch(JSON.stringify(s.posted), /PRIVATE_/);
      assert.deepEqual(s.store.profile, before);
    });
  }
}

for (const type of ["lookup", "query"]) {
  for (const failure of ["load", "profile version"]) {
    test(`F3 ${type} returns only query-failed for a private ${failure} error`, async () => {
      const s = setup();
      if (failure === "load") {
        s.store.load = async () => { throw new Error("PROFILE_SECRET: unrequested-word / private answer"); };
      } else {
        s.store.profile.version = "PRIVATE_PROFILE_VALUE";
      }
      s.send({ ...request(), type: PREFIX + type });
      await settle();
      expectError(s, "query-failed");
      assert.deepEqual(s.posted[0].message, {
        type: PREFIX + "error", requestId: "lookup-1", error: { code: "query-failed" },
      });
      assert.doesNotMatch(JSON.stringify(s.posted), /PROFILE_SECRET|PRIVATE_PROFILE_VALUE|private answer|unrequested-word/);
    });
  }
}

for (const [label, id] of [
  ["100 ligatures", "ﬃ".repeat(100)],
  ["ligatures and a combining accent", "ﬃ".repeat(99) + "e\u0301"],
  ["a combining accent", "Cafe\u0301"],
]) {
  test(`F4 lookup accepts ${label} after one normalization`, async () => {
    const s = setup("dragon-hold", [attempt({ entityId: id })]);
    const normalized = normalizeVocabularyKey(id);
    assert.ok(s.store.profile.vocabulary[normalized]);
    s.send(request({ entityType: "vocabulary", entityIds: [id] }));
    await settle();
    assert.deepEqual(expectResult(s).items.map((item) => item.entityId), [normalized]);
    assert.equal(s.store.loads, 1);
  });
}
