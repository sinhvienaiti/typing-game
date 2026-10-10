import { test } from "node:test";
import assert from "node:assert/strict";
import { VoiceResultPolicy } from "./result-policy.mjs";
import { target, snapshot, detection } from "./fixtures.mjs";
const barrier = (changes = {}) => ({ sessionId: "session", inputEpoch: 0, audioEpoch: 0, sampleRate: 16000, fromSample: 0, engineId: "test-engine", modelId: "test-model", ...changes });
const live = (targets = snapshot().targets) => targets.map((t) => ({ ...t, keyboardOwned: false }));
function policy(options) { const p = new VoiceResultPolicy(options); p.barrier(barrier()); p.publish(snapshot()); p.acknowledge("snapshot-1", ["a", "b"], 200); return p; }

test("keyboard A suppresses A while voice B remains accepted, independent of a newer registry revision", () => {
  const p = policy(), current = live(); current[0].keyboardOwned = true; current[0].eligibilityVersion++;
  p.publish(snapshot({ snapshotId: "snapshot-2", registryRevision: 200, publishedAtSample: 250, targets: [target("b", "robot"), target("c", "orbit")] }));
  assert.equal(p.resolve(detection({ unitId: "b", form: "robot" }), current, 3200).accepted, true);
  assert.equal(p.resolve(detection({ detectionId: "a-after-key" }), current, 3200).accepted, false);
});
test("receipt is terminal before gameplay and duplicate delivery cannot authorize a second mutation", () => {
  const p = policy(); const d = detection(); assert.equal(p.resolve(d, live(), 3200).accepted, true);
  const duplicate = p.resolve(d, [], 3300); assert.equal(duplicate.accepted, true); assert.equal(duplicate.duplicate, true);
  const q = policy(), targets = live(); targets[0].eligible = false;
  assert.equal(q.resolve(d, targets, 3200).accepted, false);
  targets[0].eligible = true;
  const rejectedReplay = q.resolve(d, targets, 3300); assert.equal(rejectedReplay.accepted, false); assert.equal(rejectedReplay.duplicate, true);
});
test("overlapping audio for the same form cannot hit a later unit after decoder reset; separate readings can", () => {
  const p = policy(); p.resolve(detection(), live(), 3200);
  const next = target("new-a", "red"); p.publish(snapshot({ snapshotId: "snapshot-2", publishedAtSample: 200, targets: [next] })); p.acknowledge("snapshot-2", [next.unitId], 250);
  const d = detection({ snapshotId: "snapshot-2", detectionId: "new-detection", unitId: next.unitId, streamEpoch: 2 });
  assert.equal(p.resolve(d, live([next]), 3200).reason, "replayed-audio");
  assert.equal(p.resolve({ ...d, detectionId: "real-second-reading", audioStartSample: 3200, audioEndSample: 5000 }, live([next]), 5100).accepted, true);
});
test("old audio never rematches to a new same-word unit or eligibility window", () => {
  assert.equal(policy().resolve(detection(), live([target("new-a", "red")]), 3200).reason, "unit-terminal");
  assert.equal(policy().resolve(detection(), live([target("a", "red", { unitVersion: 2 })]), 3200).reason, "eligibility-changed");
  assert.equal(policy().resolve(detection(), live([target("a", "red", { eligibilityVersion: 2 })]), 3200).reason, "eligibility-changed");
  assert.equal(policy().resolve(detection(), live([target("a", "red", { eligibleFromSample: 500 })]), 3200).reason, "audio-before-ready");
});
test("sample freshness, engine identity, pause and TTS epochs are hard barriers", () => {
  for (const [changes, now, reason] of [[{ audioEndSample: 3300 }, 3200, "invalid-audio-window"], [{ audioStartSample: 150 }, 3200, "audio-before-ready"], [{}, 16001, "expired-result"], [{ modelId: "other" }, 3200, "engine-mismatch"], [{ sessionId: "old" }, 3200, "stale-session"]]) assert.equal(policy().resolve(detection(changes), live(), now).reason, reason);
  const p = policy(); p.barrier(barrier({ inputEpoch: 1, audioEpoch: 1, fromSample: 3200 }));
  assert.equal(p.resolve(detection(), live(), 3300).reason, "stale-input-epoch");
  assert.equal(p.resolve(detection({ detectionId: "tts", inputEpoch: 1 }), live(), 3300).reason, "stale-audio-epoch");
  assert.throws(() => p.barrier(barrier()));
  assert.throws(() => p.barrier(barrier({ inputEpoch: 1, audioEpoch: 1, fromSample: 3200, sampleRate: 48000 })));
});
test("unacknowledged, unsupported, ambiguous and resolving targets fail closed", () => {
  const p = new VoiceResultPolicy(); p.barrier(barrier()); p.publish(snapshot());
  assert.equal(p.resolve(detection(), live(), 3200).reason, "targets-not-ready");
  p.acknowledge("snapshot-1", ["b"], 200);
  assert.equal(p.resolve(detection({ detectionId: "unsupported" }), live(), 3200).reason, "targets-not-ready");
  assert.throws(() => p.acknowledge("snapshot-1", ["a"], 200));
  assert.equal(policy().resolve(detection(), live([target(), target("c", "red")]), 3200).reason, "ambiguous");
  assert.equal(policy().resolve(detection(), [{ ...live()[0], resolving: true }], 3200).reason, "unit-terminal");
});
test("ten seconds of histories are bounded and overflow does not evict needed proofs", () => {
  assert.throws(() => new VoiceResultPolicy({ retentionSeconds: 9 }));
  const p = policy({ maxSnapshots: 1 }); assert.throws(() => p.publish(snapshot({ snapshotId: "too-many" })), /capacity/);
  assert.equal(p.resolve(detection(), live(), 3200).accepted, false);
  const q = policy({ maxReceipts: 1 }); q.resolve(detection(), live(), 3200);
  assert.equal(q.resolve(detection({ detectionId: "second" }), live(), 3300).reason, "receipt-capacity");
});
test("a stable live snapshot survives long waits and gets ten seconds of history after replacement", () => {
  const p = policy();
  assert.equal(p.resolve(detection({ audioStartSample: 320000, audioEndSample: 321000 }), live(), 321500).accepted, true);
  p.publish(snapshot({ snapshotId: "snapshot-2", publishedAtSample: 322000, registryRevision: 2 }));
  p.acknowledge("snapshot-2", ["a", "b"], 322000);
  assert.equal(p.resolve(detection({ detectionId: "late-b", unitId: "b", form: "robot", audioStartSample: 321000, audioEndSample: 322500 }), live(), 323000).accepted, true);
  assert.throws(() => p.publish(snapshot({ snapshotId: "reverse-time", publishedAtSample: 100 })));
});
