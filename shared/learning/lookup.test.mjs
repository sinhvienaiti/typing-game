import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import * as contract from "./message-contract.mjs";
import * as query from "./query.mjs";
import {
  applyLearningEvent, applyLearningEvents, calculateMastery,
  calculateReviewPriority, createEmptyLearningProfile,
} from "./core.mjs";
import { parseLearningProfileBackup } from "./profile-backup.mjs";

const NOW = "2026-10-30T06:00:00.000Z";
const LOOKUP = "typing-game:learning:v1:lookup";
function event(entityId = "lantern", extra = {}) {
  return {
    version: 1, entityType: "vocabulary", entityId, gameId: "recall-typing",
    activityType: "meaning-recall", result: "correct", occurredAt: NOW,
    ...extra,
  };
}
function lookup(entityIds, entityType = "vocabulary") { return { entityType, entityIds }; }

test("lookup contract constants match the kit text and parse the nested query", async () => {
  const kit = await readFile(new URL("../game-kit/learning/contract.ts", import.meta.url), "utf8");
  assert.equal(contract.LEARNING_LOOKUP_MESSAGE, kit.match(/LEARNING_LOOKUP_MESSAGE = "([^"]+)"/)[1]);
  assert.equal(contract.LOOKUP_MAX_IDS, Number(kit.match(/LOOKUP_MAX_IDS = (\d+)/)[1]));
  assert.deepEqual(contract.parseLearningMessage({ type: LOOKUP, requestId: "lookup-1", query: lookup([" Lantern "]) }), {
    type: LOOKUP, requestId: "lookup-1", lookup: lookup(["lantern"]),
  });
});

test("lookup parser normalizes vocabulary, deduplicates and preserves first order", () => {
  assert.deepEqual(query.parseLearningLookup({ ...lookup([" River  bank ", "ＬＡＮＴＥＲＮ", "river bank", " ", "lantern"]), ignored: true }), lookup(["river bank", "lantern"]));
  for (const type of ["grammar", "sentence"]) {
    assert.deepEqual(query.parseLearningLookup(lookup([" A  B ", "a  b", "A  B", "e\u0301"], type)), lookup(["A  B", "a  b", "e\u0301"], type));
  }
  assert.equal(query.parseLearningLookup(lookup(Array(200).fill("lantern"))).entityIds.length, 1);
  assert.equal(query.parseLearningLookup(lookup([" " + "a".repeat(200) + " "])).entityIds[0].length, 200);
  assert.deepEqual(query.parseLearningLookup(Object.assign(Object.create(null), lookup([" Lantern "]))), lookup(["lantern"]));
});

const invalid = [
  ["null", null], ["array", []], ["string", "lookup"], ["date", new Date()],
  ["custom prototype", Object.assign(Object.create({ custom: true }), lookup(["a"]))],
  ["missing type", { entityIds: ["a"] }], ["unknown type", lookup(["a"], "word")],
  ["ids not array", lookup("a")], ["non-string id", lookup([1])],
  ["long id", lookup(["a".repeat(201)])], ["empty array", lookup([])],
  ["empty ids", lookup([" ", "\t"])], ["201 repeated ids", lookup(Array(201).fill("a"))],
];
for (const [name, value] of invalid) {
  test(`lookup parser rejects ${name}`, () => {
    assert.equal(typeof query.parseLearningLookup, "function");
    assert.throws(() => query.parseLearningLookup(value), TypeError);
  });
}

test("lookup directly reads requested records in order, recalculating query item metrics", () => {
  const profile = applyLearningEvents(null, [event("lantern"), event("river")]);
  const before = structuredClone(profile);
  const later = "2026-12-30T06:00:00.000Z";
  const result = query.lookupLearningRecords(profile, lookup(["River", "missing", "lantern", "river"]), later);
  assert.equal(result.entityType, "vocabulary");
  assert.deepEqual(result.items.map((item) => item.entityId), ["river", "lantern"]);
  const regular = query.queryLearningProfile(profile, { entityType: "vocabulary" }, later);
  for (const item of result.items) {
    assert.deepEqual(item, regular.items.find((row) => row.entityId === item.entityId));
    assert.equal(item.mastery, calculateMastery(profile.vocabulary[item.entityId], later));
    assert.equal(item.reviewPriority, calculateReviewPriority(profile.vocabulary[item.entityId], later));
  }
  assert.deepEqual(profile, before);
  Object.defineProperty(profile.vocabulary, "unrequested", { enumerable: true, get() { throw new Error("scanned profile"); } });
  assert.equal(query.lookupLearningRecords(profile, lookup(["lantern"]), later).items.length, 1);
});

for (const [entityType, collection] of [["vocabulary", "vocabulary"], ["grammar", "grammar"], ["sentence", "sentences"]]) {
  test(`lookup ${entityType} excludes prototype keys, including own records, and supports legacy samples`, () => {
    const profile = applyLearningEvents(null, [event("known", { entityType })]);
    delete profile[collection].known.recentSamples;
    for (const id of ["constructor", "__proto__", "toString", "tostring"]) {
      Object.defineProperty(profile[collection], id, { value: profile[collection].known, enumerable: true });
    }
    const result = query.lookupLearningRecords(profile, lookup(["constructor", "__proto__", "toString", "known"], entityType), NOW);
    assert.deepEqual(result.items.map((item) => item.entityId), ["known"]);
    assert.deepEqual(result.items[0].recentSamples, []);
    assert.equal(Object.hasOwn(profile[collection].known, "recentSamples"), false);
    const legacy = applyLearningEvents(null, [event("legacy", { entityType })]);
    delete legacy[collection].legacy.recentSamples;
    assert.equal(Object.hasOwn(query.queryLearningProfile(legacy, { entityType }, NOW).items[0], "recentSamples"), false);
  });
}

for (const entityType of ["vocabulary", "grammar", "sentence"]) {
  test(`core ${entityType} keeps eight chronological samples with five fields, including a late event`, () => {
    const offsets = [1, 2, 3, 4, 5, 6, 7, 8, 10, 9, 0];
    const events = offsets.map((minute, index) => event("known", {
      entityType, occurredAt: new Date(Date.parse(NOW) + minute * 60000).toISOString(),
      activityType: ["typing-attack", "meaning-recall", "listening", "review-card"][index % 4],
      result: index % 3 === 0 ? "wrong" : "correct",
      ...(index % 2 === 0 ? { hintUsed: true } : {}),
      userAnswer: "private answer", expectedAnswer: "private expected",
    }));
    let profile = createEmptyLearningProfile();
    for (const item of events) profile = applyLearningEvent(profile, item);
    const collection = entityType === "sentence" ? "sentences" : entityType;
    const expected = [...events].sort((a, b) => Date.parse(a.occurredAt) - Date.parse(b.occurredAt)).slice(-8).map((item) => ({
      occurredAt: item.occurredAt, gameId: item.gameId, activityType: item.activityType,
      result: item.result, hintUsed: item.hintUsed === true,
    }));
    assert.deepEqual(profile[collection].known.recentSamples, expected);
    assert.deepEqual(applyLearningEvents(null, events)[collection].known.recentSamples, expected);
    delete profile[collection].known.recentSamples;
    assert.equal(applyLearningEvent(profile, events[0])[collection].known.recentSamples.length, 1);
  });
}

test("backup accepts eight samples and a legacy record without samples", () => {
  const profile = applyLearningEvents(null, [event()]);
  profile.vocabulary.lantern.recentSamples = Array.from({ length: 8 }, () => ({
    occurredAt: NOW, gameId: "recall-typing", activityType: "meaning-recall", result: "correct", hintUsed: false,
  }));
  assert.deepEqual(parseLearningProfileBackup(JSON.stringify(profile)), profile);
  delete profile.vocabulary.lantern.recentSamples;
  assert.deepEqual(parseLearningProfileBackup(profile), profile);
});
for (const [name, samples] of [["nine samples", Array(9).fill({})], ["null sample", [null]], ["array sample", [[]]], ["string sample", ["bad"]], ["non-array", {}], ["null list", null]]) {
  test(`backup rejects ${name}`, () => {
    const profile = applyLearningEvents(null, [event()]);
    profile.vocabulary.lantern.recentSamples = samples;
    assert.throws(() => parseLearningProfileBackup(profile), /recentSamples/);
  });
}

for (const [entityType, collection] of [["vocabulary", "vocabulary"], ["grammar", "grammar"], ["sentence", "sentences"]]) {
  test(`F2 ${entityType} lookup projects sample fields from an existing stored profile`, () => {
    const profile = applyLearningEvents(null, [event("lantern", { entityType })]);
    const expected = structuredClone(profile[collection].lantern.recentSamples);
    Object.assign(profile[collection].lantern.recentSamples[0], {
      userAnswer: "PRIVATE_USER_ANSWER", expectedAnswer: "PRIVATE_EXPECTED_ANSWER", extra: "PRIVATE_EXTRA",
    });
    const before = structuredClone(profile);
    assert.deepEqual(query.lookupLearningRecords(profile, lookup(["lantern"], entityType), NOW).items[0].recentSamples, expected);
    assert.deepEqual(profile, before);
  });
}

// 233 P1-233-01: a contract field holding an object or array must not reach a game.
const SAMPLE_FIELDS = ["occurredAt", "gameId", "activityType", "result", "hintUsed"];
const NESTED = {
  object: () => ({ userAnswer: "PRIVATE_NESTED_USER_ANSWER", expectedAnswer: "PRIVATE_NESTED_EXPECTED_ANSWER" }),
  array: () => [{ userAnswer: "PRIVATE_NESTED_USER_ANSWER", expectedAnswer: "PRIVATE_NESTED_EXPECTED_ANSWER" }],
};
const COLLECTIONS = [["vocabulary", "vocabulary"], ["grammar", "grammar"], ["sentence", "sentences"]];
// Two samples: tests corrupt the first; the second must come back unchanged.
function twoSampleProfile(entityType = "vocabulary") {
  return applyLearningEvents(null, [
    event("lantern", { entityType }),
    event("lantern", { entityType, occurredAt: "2026-10-30T06:01:00.000Z", activityType: "listening", hintUsed: true }),
  ]);
}
function bothRoutes(profile, entityType = "vocabulary") {
  return [
    query.lookupLearningRecords(profile, lookup(["lantern"], entityType), NOW).items[0],
    query.queryLearningProfile(profile, { entityType }, NOW).items[0],
  ];
}

for (const field of SAMPLE_FIELDS) {
  for (const [kind, nested] of Object.entries(NESTED)) {
    test(`F2 types stored profile drops a sample whose ${field} holds an ${kind}, lookup and query`, () => {
      for (const [entityType, collection] of COLLECTIONS) {
        const profile = twoSampleProfile(entityType);
        const kept = structuredClone(profile[collection].lantern.recentSamples[1]);
        profile[collection].lantern.recentSamples[0][field] = nested();
        const before = structuredClone(profile);
        for (const item of bothRoutes(profile, entityType)) {
          assert.deepEqual(item.recentSamples, [kept], entityType);
          assert.doesNotMatch(JSON.stringify(item), /PRIVATE_NESTED_/);
        }
        assert.deepEqual(profile, before);
      }
    });

    test(`F2 types backup import drops a sample whose ${field} holds an ${kind}`, () => {
      for (const [entityType, collection] of COLLECTIONS) {
        const profile = twoSampleProfile(entityType);
        const kept = structuredClone(profile[collection].lantern.recentSamples[1]);
        profile[collection].lantern.recentSamples[0][field] = nested();
        const before = structuredClone(profile);
        for (const input of [JSON.stringify(profile), profile]) {
          const imported = parseLearningProfileBackup(input);
          assert.deepEqual(imported[collection].lantern.recentSamples, [kept], entityType);
          assert.doesNotMatch(JSON.stringify(imported), /PRIVATE_NESTED_/);
          for (const item of bothRoutes(imported, entityType)) assert.deepEqual(item.recentSamples, [kept]);
        }
        assert.deepEqual(profile, before);
      }
    });
  }
}

const MISSING = Symbol("missing");
const WRONG_PRIMITIVES = [
  ["occurredAt", 1793340000000], ["occurredAt", null], ["gameId", 7], ["gameId", true],
  ["activityType", false], ["result", "maybe"], ["result", 1], ["hintUsed", "true"], ["hintUsed", 0], ["hintUsed", null],
  ...SAMPLE_FIELDS.map((field) => [field, MISSING]),
];
function corruptFirstSample(field, value) {
  const profile = twoSampleProfile();
  const kept = structuredClone(profile.vocabulary.lantern.recentSamples[1]);
  if (value === MISSING) delete profile.vocabulary.lantern.recentSamples[0][field];
  else profile.vocabulary.lantern.recentSamples[0][field] = value;
  return { profile, kept };
}

test("F2 types stored profile drops samples with a wrong primitive or a missing field", () => {
  for (const [field, value] of WRONG_PRIMITIVES) {
    const { profile, kept } = corruptFirstSample(field, value);
    for (const item of bothRoutes(profile)) assert.deepEqual(item.recentSamples, [kept], `${field}=${String(value)}`);
  }
});

test("F2 types backup import drops samples with a wrong primitive or a missing field", () => {
  for (const [field, value] of WRONG_PRIMITIVES) {
    const { profile, kept } = corruptFirstSample(field, value);
    const imported = parseLearningProfileBackup(JSON.stringify(profile));
    assert.deepEqual(imported.vocabulary.lantern.recentSamples, [kept], `${field}=${String(value)}`);
  }
});

test("F2 types stored profile drops non-object samples and reads a non-list as no samples", () => {
  for (const bad of [null, "PRIVATE_NESTED_STRING", 5, ["PRIVATE_NESTED_ARRAY"]]) {
    const profile = twoSampleProfile();
    const kept = structuredClone(profile.vocabulary.lantern.recentSamples[1]);
    profile.vocabulary.lantern.recentSamples[0] = bad;
    for (const item of bothRoutes(profile)) {
      assert.deepEqual(item.recentSamples, [kept], String(bad));
      assert.doesNotMatch(JSON.stringify(item), /PRIVATE_NESTED_/);
    }
  }
  for (const list of [{ 0: { userAnswer: "PRIVATE_NESTED_LIST" } }, "PRIVATE_NESTED_LIST", null]) {
    const profile = twoSampleProfile();
    profile.vocabulary.lantern.recentSamples = list;
    for (const item of bothRoutes(profile)) {
      assert.deepEqual(item.recentSamples, [], String(list));
      assert.doesNotMatch(JSON.stringify(item), /PRIVATE_NESTED_/);
    }
  }
});

test("F3 error contract supports code-only replies and preserves explicit public messages", () => {
  assert.deepEqual(contract.makeLearningError("lookup-1", "query-failed"), {
    type: contract.LEARNING_ERROR_MESSAGE, requestId: "lookup-1", error: { code: "query-failed" },
  });
  assert.equal(contract.makeLearningError("lookup-1", "invalid-request", "Invalid lookup").error.message, "Invalid lookup");
});

test("F4 parsed lookup accepts an NFKC-expanded id while raw lookup retains validation", () => {
  const id = "ﬃ".repeat(99) + "e\u0301";
  const profile = applyLearningEvents(null, [event(id)]);
  const raw = lookup([id]);
  const parsed = query.parseLearningLookup(raw);
  assert.ok(parsed.entityIds[0].length > 200);
  assert.deepEqual(query.lookupParsedLearningRecords(profile, parsed, NOW), query.lookupLearningRecords(profile, raw, NOW));
  assert.throws(() => query.lookupLearningRecords(profile, lookup(["a".repeat(201)]), NOW), /too long/);
});
