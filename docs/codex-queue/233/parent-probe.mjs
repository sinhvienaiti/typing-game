import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { resolve } from "node:path";
import { pathToFileURL } from "node:url";
import test from "node:test";

const load = (path) => import(pathToFileURL(resolve(path)));
const { applyLearningEvents, normalizeVocabularyKey } = await load("shared/learning/core.mjs");
const { parseLearningProfileBackup } = await load("shared/learning/profile-backup.mjs");
const { resolveGameArt } = await load("portal/src/game-card.ts");
globalThis.window ??= globalThis;
const { ParentLearningBridge } = await load("portal/src/learning/bridge.ts");
const game = JSON.parse(readFileSync("portal/public/games.json", "utf8")).games.find((g) => g.id === "dragon-hold");
const namespace = "typing-game:learning:v1:";
const event = (entityType = "vocabulary", entityId = "lantern") => ({
  version: 1, entityType, entityId, gameId: "dragon-hold", activityType: "meaning-recall",
  occurredAt: "2026-10-30T06:00:00.000Z", result: "correct", hintUsed: false,
});
const collection = { vocabulary: "vocabulary", grammar: "grammar", sentence: "sentences" };
function setup(events = [event()]) {
  const posted = [];
  const frame = { contentWindow: { postMessage(message, origin) { posted.push({ message, origin }); } } };
  const store = { profile: applyLearningEvents(null, events), loads: 0,
    async load() { this.loads++; return this.profile; }, async applyMany() { throw new Error("unexpected write"); } };
  const bridge = new ParentLearningBridge(store);
  return { store, posted, async send(type, entityType = "vocabulary", ids = ["lantern"]) {
    bridge.handleMessage({ source: frame.contentWindow, origin: new URL(game.appUrl).origin,
      data: { type: namespace + type, requestId: "233-probe", query: { entityType, entityIds: ids } } }, frame, game);
    await new Promise((done) => setImmediate(done));
    assert.equal(posted.length, 1);
    assert.equal(posted[0].origin, new URL(game.appUrl).origin);
    return posted[0].message;
  } };
}

for (const entityType of Object.keys(collection)) for (const route of ["lookup", "query"]) {
  test(`F2 original and eight-sample nested-extra variant ${entityType}/${route}`, async () => {
    const s = setup(Array.from({ length: 8 }, () => event(entityType)));
    const samples = s.store.profile[collection[entityType]].lantern.recentSamples;
    for (const sample of samples) Object.assign(sample, { userAnswer: "PRIVATE_USER_ANSWER",
      expectedAnswer: "PRIVATE_EXPECTED_ANSWER", extra: [{ nested: { userAnswer: "PRIVATE_NESTED" } }] });
    s.store.profile = parseLearningProfileBackup(JSON.stringify(s.store.profile));
    const before = structuredClone(s.store.profile);
    const reply = await s.send(route, entityType);
    assert.equal(reply.type, namespace + "query-result");
    assert.equal(reply.result.items[0].recentSamples.length, 8);
    for (const sample of reply.result.items[0].recentSamples)
      assert.deepEqual(Object.keys(sample).sort(), ["occurredAt", "gameId", "activityType", "result", "hintUsed"].sort());
    assert.doesNotMatch(JSON.stringify(reply.result.items[0].recentSamples), /PRIVATE_/);
    assert.deepEqual(s.store.profile, before);
  });
}

for (const field of ["occurredAt", "gameId", "activityType", "result", "hintUsed"]) for (const route of ["lookup", "query"]) {
  test(`F2 allowed field with nested answer ${field}/${route}`, async () => {
    const s = setup();
    s.store.profile.vocabulary.lantern.recentSamples[0][field] = {
      userAnswer: "PRIVATE_NESTED_USER_ANSWER", expectedAnswer: "PRIVATE_NESTED_EXPECTED_ANSWER",
    };
    try { s.store.profile = parseLearningProfileBackup(JSON.stringify(s.store.profile)); }
    catch (error) { assert.ok(error instanceof TypeError); return; }
    const reply = await s.send(route);
    assert.doesNotMatch(JSON.stringify(reply), /PRIVATE_NESTED_/);
  });
}

for (const route of ["lookup", "query"]) for (const failure of ["non-Error", "cause", "oversized"]) {
  test(`F3 additional thrown value ${route}/${failure}`, async () => {
    const s = setup();
    const value = failure === "non-Error" ? { message: "PRIVATE_OBJECT", userAnswer: "PRIVATE_ANSWER" }
      : failure === "cause" ? new Error("PRIVATE_OUTER", { cause: new Error("PRIVATE_CAUSE") })
      : new Error("PRIVATE_LONG".repeat(1000));
    s.store.load = async () => { throw value; };
    assert.deepEqual(await s.send(route), { type: namespace + "error", requestId: "233-probe", error: { code: "query-failed" } });
  });
}

for (const raw of ["ﬃ".repeat(200), "  " + "ﬃ".repeat(198) + "e\u0301  ", "  Cafe\u0301  "]) {
  test(`F4 boundary/trim/dedup ${raw.trim().length}`, async () => {
    const s = setup([event("vocabulary", raw)]);
    const reply = await s.send("lookup", "vocabulary", [raw, raw + " "]);
    assert.equal(reply.type, namespace + "query-result");
    assert.deepEqual(reply.result.items.map((r) => r.entityId), [normalizeVocabularyKey(raw)]);
    assert.equal(s.store.loads, 1);
  });
}
test("F4 rejects 201 raw characters before reading storage", async () => {
  const s = setup();
  const reply = await s.send("lookup", "vocabulary", ["ﬃ".repeat(201)]);
  assert.equal(reply.error.code, "invalid-request");
  assert.equal(s.store.loads, 0);
});

const prefix = "/assets/dragon-hold/portal/";
const suffixes = ["..\\outside.png", "folder\\icon.png", "folder/\\icon.png"];
for (const separator of ["%2f", "%2F", "%5c", "%5C"]) {
  let suffix = "%2e%2e" + separator + "%2e%2e" + separator + "space-typing/portal/icon.png";
  for (let depth = 1; depth <= 6; depth++) {
    suffixes.push(suffix);
    suffix = suffix.replaceAll("%", "%25");
  }
}
for (const suffix of suffixes) test(`F5 independent separator/depth ${suffix}`, () => {
  for (const appUrl of [game.appUrl, game.appUrl + "/play/session/", game.appUrl.toUpperCase()]) {
    const art = { icon: prefix + suffix, cover: prefix + suffix };
    assert.deepEqual(resolveGameArt({ ...game, appUrl, art }), { icon: null, cover: null });
  }
});
