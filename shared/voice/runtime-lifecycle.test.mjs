import test from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { stripTypeScriptTypes } from "node:module";
import { runInNewContext } from "node:vm";
import { matchFinalWords } from "./final-matcher.mjs";
import { snapshot } from "./fixtures.mjs";

// Exercise the production class with fake devices; no browser/model/mic required.
function setup() {
  const preparations = [], recognizers = [], gates = [], errors = [], detections = [], feedback = [];
  const source = readFileSync(new URL("../../portal/src/voice/runtime.ts", import.meta.url), "utf8")
    .replace(/^import[\s\S]*?;\n/gm, "")
    .replace("export class BrowserVoiceRuntime", "class BrowserVoiceRuntime");
  const Runtime = runInNewContext(stripTypeScriptTypes(source, { mode: "transform" }) + "\nBrowserVoiceRuntime", {
    AbortController, performance, matchFinalWords, WARMUP_SAMPLES: 16000, CAPTURE_MAX_PENDING: 10,
    primeRecognizer: (_recognizer, signal) => new Promise((resolve, reject) => {
      preparations.push({ resolve, reject, signal });
      signal.addEventListener("abort", () => reject(signal.reason), { once: true });
    }),
  });
  const model = { terminate() {}, createRecognizer(_rate, grammar) {
    const rec = { grammar, removed: 0, handlers: {}, on(name, cb) { this.handlers[name] = cb; }, setWords() {}, remove() { this.removed++; } };
    recognizers.push(rec); return rec;
  } };
  const audio = { close: async () => {} }, node = { disconnect() {} };
  const capture = { ...node, port: { postMessage: value => gates.push(value), close() {} } };
  const runtime = new Runtime(model, audio, capture, node, node, { sessionId:"session", onError: message => errors.push(message), onClock() {},
    onDetection: value => detections.push(value), onFeedback: value => feedback.push(value) });
  return { runtime, preparations, recognizers, gates, errors, detections, feedback };
}
test("concurrent resume shares the same recognizer preparation", async () => {
  const s = setup(), first = s.runtime.resume(), second = s.runtime.resume();
  assert.equal(first, second);
  assert.equal(s.recognizers.length, 1);
  s.preparations[0].resolve(); await first;
  assert.equal(s.gates.filter(g => g.enabled).length, 1);
  await s.runtime.close();
});
test("suspend cancels old warmup without clearing a newer resume", async () => {
  const s = setup(), old = s.runtime.resume();
  await s.runtime.suspend();
  const fresh = s.runtime.resume();
  await old;
  assert.equal(s.runtime.resume(), fresh);
  assert.equal(s.recognizers[0].removed, 1);
  s.preparations[1].resolve(); await fresh;
  assert.equal(s.gates.filter(g => g.enabled).length, 1);
  await s.runtime.close();
});
test("close prevents a simultaneous resume from resurrecting the decoder", async () => {
  const s = setup(), preparing = s.runtime.resume();
  const closing = s.runtime.close();
  await s.runtime.resume();
  await Promise.all([preparing, closing]);
  assert.equal(s.recognizers.length, 1);
  assert.equal(s.recognizers[0].removed, 1);
  assert.equal(s.gates.some(g => g.enabled), false);
});
test("paused runtime errors are reported once; removed recognizer errors are ignored", async () => {
  const s = setup(), preparing = s.runtime.resume();
  s.preparations[0].resolve(); await preparing;
  await s.runtime.suspend();
  s.recognizers[0].handlers.error({ error: "late old recognizer" });
  assert.equal(s.errors.length, 0);
  s.runtime.fail("microphone disconnected while paused");
  s.runtime.fail("duplicate worker event");
  await s.runtime.resume();
  assert.deepEqual(s.errors, ["microphone disconnected while paused"]);
  assert.equal(s.recognizers.length, 1);
  await s.runtime.close();
});
test("negative warmup origin accepts live words but never exports synthetic warmup evidence", async () => {
  const s = setup(), preparing = s.runtime.resume();
  s.preparations[0].resolve(); await preparing;
  await s.runtime.applyTargets(snapshot());
  s.runtime.baseSample = -8000;
  s.runtime.clock = 40000;
  const warming = { word:"red", start:0.2, end:0.4, conf:1 };
  const live = { word:"red", start:1.1, end:1.3, conf:1 };
  s.runtime.final({ text:"red", result:[warming] }, s.runtime.generation);
  assert.equal(s.feedback.length, 0);
  s.runtime.final({ text:"red red", result:[warming,live] }, s.runtime.generation);
  assert.equal(s.detections.length, 1);
  assert.equal(s.detections[0].audioStartSample, 9600);
  assert.equal(s.feedback.length, 1);
  assert.equal(s.feedback[0].transcript, "red");
  await s.runtime.close();
});

const flushTurns = async () => { for (let i = 0; i < 6; i++) await Promise.resolve(); };

test("recognizer listens only to the checked vocabulary and target words (grammar)", async () => {
  const s = setup();
  s.runtime.vocabulary = new Set(["red", "blue", "green"]);
  s.runtime.addGrammarForms(["red", "blue", "purple"]);
  const preparing = s.runtime.resume();
  s.preparations[0].resolve(); await preparing;
  assert.deepEqual([...s.recognizers[0].grammar], ["red", "blue"]);
  await s.runtime.close();
});

test("a new word while listening rebuilds the recognizer, but never mid-utterance", async () => {
  const s = setup();
  s.runtime.vocabulary = new Set(["red", "blue", "green"]);
  s.runtime.addGrammarForms(["red"]);
  const preparing = s.runtime.resume();
  s.preparations[0].resolve(); await preparing;
  // The player is saying something: the rebuild waits.
  s.recognizers[0].handlers.partialresult({ result: { partial: "re" } });
  s.runtime.addGrammarForms(["green"]);
  await flushTurns();
  assert.equal(s.recognizers.length, 1);
  // Utterance ends: now the recognizer is rebuilt with the new word.
  s.recognizers[0].handlers.result({ result: { text: "", result: [] } });
  await flushTurns();
  assert.equal(s.recognizers.length, 2);
  assert.equal(s.recognizers[0].removed, 1);
  assert.deepEqual([...s.recognizers[1].grammar], ["red", "green"]);
  s.preparations[1].resolve(); await flushTurns();
  assert.equal(s.gates.at(-1).enabled, true);
  await s.runtime.close();
});

test("an overload drops that utterance and restarts; only repeated overloads end the session", async () => {
  const s = setup();
  const preparing = s.runtime.resume();
  s.preparations[0].resolve(); await preparing;
  for (let i = 1; i <= 3; i++) {
    s.runtime.captureMessage({ type: "overflow", generation: s.runtime.generation, sample: 1600 * i });
    await flushTurns();
    assert.equal(s.errors.length, 0, "overload " + i + " recovers");
    assert.equal(s.recognizers.length, i + 1);
    s.preparations[i].resolve(); await flushTurns();
  }
  s.runtime.captureMessage({ type: "overflow", generation: s.runtime.generation, sample: 99999 });
  assert.equal(s.errors.length, 1);
  assert.match(s.errors[0], /overloaded/);
  await s.runtime.close();
});

test("overflow while paused is ignored", async () => {
  const s = setup();
  const preparing = s.runtime.resume();
  s.preparations[0].resolve(); await preparing;
  await s.runtime.suspend();
  s.runtime.captureMessage({ type: "overflow", generation: s.runtime.generation, sample: 1600 });
  await flushTurns();
  assert.equal(s.errors.length, 0);
  assert.equal(s.recognizers.length, 1);
  await s.runtime.close();
});

test("grammar catch-all [unk] is never reported as a heard word", async () => {
  const s = setup(), preparing = s.runtime.resume();
  s.preparations[0].resolve(); await preparing;
  await s.runtime.applyTargets(snapshot());
  s.runtime.baseSample = 0;
  s.runtime.clock = 40000;
  s.runtime.final({ text: "[unk]", result: [{ word: "[unk]", start: 1.1, end: 1.3, conf: 1 }] }, s.runtime.generation);
  assert.equal(s.feedback.length, 0);
  assert.equal(s.detections.length, 0);
  await s.runtime.close();
});
