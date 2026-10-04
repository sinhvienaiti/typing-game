import { test } from "node:test";
import assert from "node:assert/strict";
import { VoiceHost } from "./host.mjs";
import { snapshot, detection, feedback } from "./fixtures.mjs";
const deferred = () => { let resolve; const promise = new Promise((r) => { resolve = r; }); return { promise, resolve }; };
const tick = () => new Promise((r) => setImmediate(r));
function setup(changes = {}) {
  const events = [], counts = { stopped: 0, closed: 0, resumed: 0, flushed: 0, suspended: 0 }; let now = 200;
  const stream = { getTracks: () => [{ stop: () => counts.stopped++ }] };
  const runtime = { engineId: "test-engine", modelId: "test-model", sampleRate: 16000, nowSample: () => now,
    close: async () => { counts.closed++; }, suspend: async () => { counts.suspended++; }, resume: async () => { counts.resumed++; }, flush: async () => { counts.flushed++; },
    applyTargets: async (s) => ({ ready: s.targets.map((t) => t.unitId), unsupported: [] }) };
  const h = new VoiceHost({ requestMicrophone: async () => stream, createRuntime: async () => runtime, createSessionId: () => "session", onEvent: (e) => events.push(e), waitTail: async () => {}, ...changes });
  return { h, events, counts, stream, runtime, setNow: (n) => { now = n; } };
}
test("permission/model readiness alone cannot start recognition before target ACK", async () => {
  const { h, events, counts, setNow, runtime } = setup(); assert.equal(await h.start(0), true);
  assert.equal(h.state, "READY"); assert.equal(counts.resumed, 0);
  assert.equal(h.receiveDetection(detection(), h.generation), false);
  assert.equal(await h.applyTargets(snapshot()), true); assert.equal(h.state, "LISTENING");
  assert.deepEqual(events.map((e) => e.type), ["ready", "targets-applied", "listening"]);
  setNow(3200); assert.equal(h.receiveDetection(detection(), h.generation), true);
  const closing = deferred(); runtime.close = async () => { counts.closed++; await closing.promise; };
  const stop = h.stop(); assert.equal(counts.stopped, 1); assert.equal(counts.closed, 1);
  assert.equal(h.receiveDetection(detection(), h.generation - 1), false);
  closing.resolve(); await stop;
});
test("decoder feedback is gated, current-session metadata and never a combat detection", async () => {
  let onFeedback; const s = setup({ createRuntime: async (_stream, options) => { onFeedback = options.onFeedback; return s.runtime; } });
  await s.h.start(0); assert.equal(onFeedback(feedback()), false);
  await s.h.applyTargets(snapshot()); s.setNow(3200);
  for (const changes of [{ sessionId: "old" }, { inputEpoch: 1 }, { audioEpoch: 1 }, { engineId: "other" }, { modelId: "other" }, { audioEndSample: 3300 }, { evidence: "partial" }]) assert.equal(onFeedback(feedback(changes)), false);
  assert.equal(onFeedback(feedback()), true);
  assert.equal(s.events.at(-1).type, "feedback"); assert.equal(s.events.some((e) => e.type === "detection"), false);
  await s.h.suspend(1); assert.equal(onFeedback(feedback()), false);
  await s.h.resume(1); await s.h.applyTargets(snapshot({ inputEpoch: 1, audioEpoch: 1, snapshotId: "resume" }));
  assert.equal(onFeedback(feedback()), false);
  assert.equal(onFeedback(feedback({ inputEpoch: 1, audioEpoch: 1, result: "unrecognized", transcript: null })), true);
  await s.h.stop(); assert.equal(onFeedback(feedback()), false);
});
test("stop while permission is pending disposes a late stream without preparing a decoder", async () => {
  const permission = deferred(); let prepared = 0;
  const { h, stream, counts, events } = setup({ requestMicrophone: () => permission.promise, createRuntime: async () => { prepared++; throw new Error("should never prepare"); } });
  const start = h.start(0); await tick(); assert.equal(h.state, "REQUESTING_PERMISSION");
  await h.stop(); permission.resolve(stream); assert.equal(await start, false);
  assert.equal(h.state, "IDLE"); assert.equal(prepared, 0); assert.equal(counts.stopped, 1);
  assert.equal(events.some((e) => e.type === "ready"), false);
});
test("stop during preparation disposes a late worker and cannot resurrect the session", async () => {
  const preparation = deferred(); const { h, runtime, counts } = setup({ createRuntime: () => preparation.promise });
  const start = h.start(0); await tick(); assert.equal(h.state, "PREPARING");
  await h.stop(); preparation.resolve(runtime); assert.equal(await start, false);
  assert.equal(h.state, "IDLE"); assert.equal(counts.closed, 1);
});
test("latest start wins before either permission request can race", async () => {
  let sessions = 0; const { h } = setup({ createSessionId: () => `session-${++sessions}` });
  const a = h.start(0), b = h.start(1); assert.deepEqual(await Promise.all([a, b]), [false, true]);
  assert.equal(h.session.inputEpoch, 1); await h.stop();
});
test("late target compilation after pause is not an ACK and does not resume capture", async () => {
  const compile = deferred(), { h, runtime, events, counts } = setup(); runtime.applyTargets = () => compile.promise;
  await h.start(0); const apply = h.applyTargets(snapshot()); await tick();
  await h.suspend(1); compile.resolve({ ready: ["a", "b"], unsupported: [] });
  assert.equal(await apply, false); assert.equal(h.state, "SUSPENDED"); assert.equal(counts.resumed, 0);
  assert.equal(events.some((e) => e.type === "targets-applied"), false);
  await h.resume(1); assert.equal(h.session.audioEpoch, 1); assert.equal(h.state, "READY"); await h.stop();
});
test("invalid capability classification cannot make the host LISTENING", async () => {
  const { h, runtime } = setup(); runtime.applyTargets = async () => ({ ready: ["a"], unsupported: [] });
  await h.start(0); await assert.rejects(h.applyTargets(snapshot()), /ACK/); assert.equal(h.state, "READY"); await h.stop();
});
test("empty snapshots are valid and resume requires fresh epochs and target ACK", async () => {
  const { h } = setup(); await h.start(0); await h.applyTargets(snapshot({ targets: [] })); assert.equal(h.state, "LISTENING");
  await h.suspend(1); assert.equal(h.receiveDetection(detection(), h.generation), false);
  await h.resume(1); assert.equal(await h.applyTargets(snapshot()), false);
  assert.equal(await h.applyTargets(snapshot({ inputEpoch: 1, audioEpoch: 1, snapshotId: "resume", targets: [] })), true); await h.stop();
});
test("TTS gate ACK precedes playback; a stale ended callback cannot reopen a newer gate", async () => {
  const tail = deferred(); const { h, events, counts } = setup({ waitTail: () => tail.promise });
  await h.start(0); await h.applyTargets(snapshot());
  assert.equal(await h.audioOutputIntent(1), true); assert.equal(h.state, "SUSPENDED"); assert.equal(events.at(-1).type, "gate-closed");
  const ended = h.audioOutputEnded(1); await h.audioOutputIntent(2); tail.resolve(); assert.equal(await ended, false);
  assert.equal(h.state, "SUSPENDED"); assert.equal(counts.flushed, 0);
  assert.equal(await h.audioOutputEnded(2), true); assert.equal(h.session.audioEpoch, 1); assert.equal(h.state, "READY");
  assert.equal(h.receiveDetection(detection(), h.generation), false); await h.stop();
});
test("permission denial leaves an explicit error and no live microphone", async () => {
  const { h, counts, events } = setup({ requestMicrophone: async () => { throw new Error("denied"); } });
  assert.equal(await h.start(0), false); assert.equal(h.state, "ERROR"); assert.equal(h.session, null); assert.equal(counts.resumed, 0); assert.equal(events.at(-1).code, "local-runtime-failed");
});
test("audio ended cannot reopen a gate before capture has acknowledged closure", async () => {
  const suspended = deferred(); const { h, runtime } = setup(); await h.start(0); await h.applyTargets(snapshot());
  runtime.suspend = () => suspended.promise;
  const intent = h.audioOutputIntent(1); assert.equal(await h.audioOutputEnded(1), false);
  assert.equal(await h.resume(0), false); suspended.resolve(); assert.equal(await intent, true);
  assert.equal(await h.audioOutputEnded(1), true); await h.stop();
});
test("a duplicate TTS ended event cannot resume a subsequent gameplay pause", async () => {
  const { h } = setup(); await h.start(0); await h.applyTargets(snapshot());
  await h.audioOutputIntent(1); await h.audioOutputEnded(1); await h.suspend(1);
  assert.equal(await h.audioOutputEnded(1), false); assert.equal(h.state, "SUSPENDED"); await h.stop();
});
