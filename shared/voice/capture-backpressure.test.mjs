import test from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { stripTypeScriptTypes } from "node:module";
import { runInNewContext } from "node:vm";
import { StreamingResampler } from "./audio-resampler.mjs";
import { CAPTURE_MAX_PENDING, CAPTURE_BLOCK_SAMPLES } from "../../portal/src/voice/capture-policy.ts";

function capture() {
  const messages = [];
  let Processor;
  const source = stripTypeScriptTypes(readFileSync(new URL("../../portal/src/voice/capture.worklet.ts", import.meta.url), "utf8").replace(/^import .*;\n/gm, ""));
  runInNewContext(source, {
    StreamingResampler, CAPTURE_MAX_PENDING, CAPTURE_BLOCK_SAMPLES, sampleRate: 16000,
    AudioWorkletProcessor: class { port = { postMessage: value => messages.push(value) }; },
    registerProcessor: (_name, Class) => Processor = Class,
  });
  const node = new Processor();
  const send = data => node.port.onmessage({ data });
  const audio = blocks => { for (let i = 0; i < blocks; i++) node.process([[new Float32Array(CAPTURE_BLOCK_SAMPLES)]]); };
  return { messages, send, audio };
}
test("capture tolerates bursty decode but has a hard one-second outstanding audio cap", () => {
  const c = capture();
  c.send({ type: "gate", generation: 1, enabled: true });
  c.audio(CAPTURE_MAX_PENDING + 1);
  assert.equal(c.messages.filter(m => m.type === "pcm").length, CAPTURE_MAX_PENDING);
  assert.equal(c.messages.some(m => m.type === "overflow"), false);
  c.audio(1);
  assert.equal(c.messages.filter(m => m.type === "overflow").length, 1);
  c.audio(20);
  assert.equal(c.messages.filter(m => m.type === "pcm").length, CAPTURE_MAX_PENDING);
});
test("fresh decoder credit replenishes capture; old-session credits cannot extend the cap", () => {
  const c = capture();
  c.send({ type: "gate", generation: 2, enabled: true });
  c.audio(CAPTURE_MAX_PENDING + 1);
  c.send({ type: "credit", generation: 2 });
  c.audio(1);
  assert.equal(c.messages.filter(m => m.type === "pcm").length, CAPTURE_MAX_PENDING + 1);
  c.send({ type: "credit", generation: 1 });
  c.audio(1);
  assert.equal(c.messages.filter(m => m.type === "overflow").length, 1);
});
