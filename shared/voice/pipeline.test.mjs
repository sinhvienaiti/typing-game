import test from "node:test";
import assert from "node:assert/strict";
import { StreamingResampler } from "./audio-resampler.mjs";
import { matchFinalWords } from "./final-matcher.mjs";
import { VoiceHost } from "./host.mjs";
import { parseVoiceMessage } from "./protocol.mjs";
import { loadOfflineVoskWorker } from "../../scripts/offline-vosk-plugin.mjs";
const target = (unitId, form, more = {}) => ({
  unitId,
  unitVersion: 1,
  eligibilityVersion: 1,
  capability: "word",
  forms: [form],
  eligible: true,
  eligibleFromSample: 0,
  ...more,
});
const snapshot = (more = {}) => ({
  sessionId: "s",
  inputEpoch: 1,
  audioEpoch: 0,
  sampleRate: 16000,
  snapshotId: "one",
  registryRevision: 1,
  publishedAtSample: 0,
  targets: [target("a", "one"), target("b", "planet")],
  ...more,
});
const word = (word, start, end, conf = 1) => ({ word, start, end, conf });
test("final lexical spans match their capture snapshot across target churn", () => {
  const old = snapshot(),
    newer = snapshot({
      snapshotId: "two",
      publishedAtSample: 2000,
      registryRevision: 2,
      targets: [target("new", "one")],
    });
  const result = matchFinalWords(
    [word("one", 0.05, 0.1), word("planet", 0.2, 0.4)],
    [old, newer],
    0,
    16000,
  );
  assert.equal(result[0].target.unitId, "a");
  assert.equal(result[0].snapshotId, "one");
  assert.equal(result.length, 1); // planet no longer existed when its own audio started
});
test("low confidence, overlapping or malformed timing, partial words and unsupported targets cannot commit", () => {
  const s = snapshot();
  for (const words of [
    [word("one", 0, 0.1, 0.84)],
    [word("on", 0, 0.1)],
    [null],
    [word("one", 1, 0.5)],
    [{ word: "one", end: 0.5, conf: 1 }],
  ])
    assert.deepEqual(matchFinalWords(words, [s], 0, 16000), []);
  assert.deepEqual(
    matchFinalWords(
      [word("one", 0, 0.1)],
      [snapshot({ targets: [target("a", "one", { eligible: false })] })],
      0,
      16000,
    ),
    [],
  );
  assert.deepEqual(
    matchFinalWords(
      [word("one", 0, 0.1)],
      [snapshot({ targets: [target("a", "one"), target("b", "one")] })],
      0,
      16000,
    ),
    [],
  );
});
test("longest phrase wins and a keyboard-owned spoken form never retargets", () => {
  const s = snapshot({
    targets: [
      target("a", "one"),
      target("phrase", "one planet", { capability: "phrase" }),
    ],
  });
  assert.equal(
    matchFinalWords(
      [word("one", 0.1, 0.2), word("planet", 0.2, 0.4)],
      [s],
      0,
      16000,
    )[0].target.unitId,
    "phrase",
  );
  s.targets.push(target("owned", "one planet", { eligible: false }));
  assert.notEqual(
    matchFinalWords(
      [word("one", 0.1, 0.2), word("planet", 0.2, 0.4)],
      [s],
      0,
      16000,
    )[0]?.target.unitId,
    "phrase",
  );
});
for (const rate of [16000, 44100, 48000])
  test(`streaming ${rate} Hz resampling preserves chunk boundaries and bounded state`, () => {
    const input = Float32Array.from({ length: rate }, (_, i) =>
      Math.sin((2 * Math.PI * 1000 * i) / rate),
    );
    const whole = new StreamingResampler(rate).push(input),
      streaming = new StreamingResampler(rate),
      out = [];
    for (let offset = 0; offset < input.length; offset += 128)
      out.push(...streaming.push(input.subarray(offset, offset + 128)));
    assert.ok(whole.length >= 15980 && whole.length <= 16000);
    assert.equal(out.length, whole.length);
    assert.ok(out.every((value, i) => Math.abs(value - whole[i]) < 1e-6));
    assert.ok(streaming.input.length <= 40);
  });
test("downsampling rejects high-frequency aliasing rather than skipping every third sample", () => {
  const amplitude = (freq) => {
    const out = new StreamingResampler(48000).push(
      Float32Array.from({ length: 48000 }, (_, i) =>
        Math.sin((2 * Math.PI * freq * i) / 48000),
      ),
    );
    return Math.sqrt(
      out.slice(128).reduce((sum, x) => sum + x * x, 0) / (out.length - 128),
    );
  };
  assert.ok(amplitude(1000) > 0.65);
  assert.ok(amplitude(12000) < 0.025);
});
test("vocabulary preflight messages are bounded and cannot carry audio", () => {
  const message = {
    type: "typing-game:voice:v1:vocabulary-check",
    version: 1,
    gameId: "space-typing",
    gameInstanceId: "i",
    sessionId: "s",
    inputEpoch: 1,
    audioEpoch: 0,
    requestId: "v",
    forms: [" Planet "],
  };
  assert.deepEqual(parseVoiceMessage(message).forms, ["planet"]);
  assert.throws(() =>
    parseVoiceMessage({ ...message, forms: Array(257).fill("word") }),
  );
  assert.throws(() => parseVoiceMessage({ ...message, pcm: [] }));
});
test("target backpressure rejects excess work and fresh capability checks stay session-bound", async () => {
  let release;
  const events = [],
    pending = new Promise((resolve) => {
      release = resolve;
    });
  const runtime = {
    sampleRate: 16000,
    engineId: "test",
    modelId: "test",
    nowSample: () => 1000,
    suspend: async () => {},
    resume: async () => {},
    flush: async () => {},
    close: async () => {},
    unsupportedForms: (forms) => forms.filter((form) => form === "unknown"),
    applyTargets: async (s) => {
      await pending;
      return { ready: s.targets.map((t) => t.unitId), unsupported: [] };
    },
  };
  const host = new VoiceHost({
    requestMicrophone: async () => ({ getTracks: () => [] }),
    createRuntime: async () => runtime,
    createSessionId: () => "s",
    onEvent: (event) => events.push(event),
  });
  await host.start(1);
  assert.equal(
    host.checkVocabulary({
      sessionId: "old",
      inputEpoch: 1,
      audioEpoch: 0,
      forms: ["unknown"],
    }),
    false,
  );
  assert.equal(
    host.checkVocabulary({
      sessionId: "s",
      inputEpoch: 1,
      audioEpoch: 0,
      requestId: "v",
      forms: ["one", "unknown"],
    }),
    true,
  );
  assert.deepEqual(events.at(-1).unsupported, ["unknown"]);
  const updates = Array.from({ length: 4 }, (_, i) =>
    host.applyTargets(snapshot({ snapshotId: "pending:" + i })),
  );
  await assert.rejects(host.applyTargets(snapshot()), /backpressure/);
  release();
  await Promise.all(updates);
  await host.stop();
});
test("pinned production Worker uses MEMFS and explicit recognizer readiness", () => {
  const { source } = loadOfflineVoskWorker();
  assert.ok(!source.includes("this.Vosk.FS.mount(this.Vosk.IDBFS"));
  assert.ok(!source.includes("this.Vosk.syncFilesystem("));
  assert.ok(source.includes('event: "recognizer-ready"'));
});
