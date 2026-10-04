import { test } from "node:test";
import assert from "node:assert/strict";
import { parseDetection, parseSnapshot, parseVoiceMessage, normalizeSpokenForm } from "./protocol.mjs";
import { matchSnapshot } from "./target-snapshot.mjs";
import { target, snapshot, detection, envelope } from "./fixtures.mjs";

test("spoken forms preserve words, punctuation and non-ASCII rather than the keyboard key", () => {
  assert.equal(normalizeSpokenForm(" STAR   SHIP "), "star ship");
  assert.equal(normalizeSpokenForm("résumé"), "résumé");
  assert.equal(matchSnapshot(snapshot(), "r").status, "no-match");
  assert.equal(matchSnapshot(snapshot(), "RED").targets[0].unitId, "a");
  assert.equal(matchSnapshot(snapshot({ targets: [target(), target("b", "red")] }), "red").status, "ambiguous");
  assert.equal(matchSnapshot(snapshot(), "red", ["RED"]).status, "suppressed");
});
test("bounds and unique normalized forms/identities are enforced", () => {
  for (const s of [snapshot({ targets: Array.from({ length: 65 }, (_, i) => target(String(i))) }), snapshot({ targets: [target(), target()] }), snapshot({ targets: [target("a", "red", { forms: ["red", " RED "] })] }), snapshot({ targets: [target("a", "x", { forms: ["x".repeat(201)] })] }), snapshot({ targets: [target("a", "x", { forms: ["a", "b", "c", "d", "e", "f"] })] })]) assert.throws(() => parseSnapshot(s));
  assert.equal(parseSnapshot(snapshot({ targets: [] })).targets.length, 0);
  assert.throws(() => parseSnapshot(snapshot({ targets: [target("a", "x", { forms: ["ﬃ".repeat(100)] })] })));
  assert.throws(() => parseDetection(detection({ form: "ﬃ".repeat(100) })));
});
test("detection requires genuine evidence, ordered sample times and explicit score semantics", () => {
  assert.equal(parseDetection(detection()).emittedAtMs, 13.25);
  for (const d of [detection({ evidence: "partial" }), detection({ audioEndSample: 300 }), detection({ audioStartSample: -1 }), detection({ emittedAtMs: NaN }), detection({ score: 0.9 }), detection({ score: Infinity, scoreKind: "raw" })]) assert.throws(() => parseDetection(d));
  assert.equal(parseDetection(detection({ score: -2.3, scoreKind: "log-score" })).score, -2.3);
});
test("namespace/version and raw-audio boundaries reject invalid iframe messages", () => {
  for (const v of [envelope("hello", { versions: [] }), envelope("hello", { versions: [1, 1] }), envelope("hello", { versions: [1], pcm: new Float32Array(3) }), envelope("hello", { versions: [1], version: 2 }), envelope("unknown"), envelope("start", { inputEpoch: Infinity })]) assert.throws(() => parseVoiceMessage(v));
  assert.deepEqual(parseVoiceMessage(envelope("hello", { versions: [1] })).versions, [1]);
});
