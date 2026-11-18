import test from "node:test";
import assert from "node:assert/strict";
import { primeRecognizer } from "../../portal/src/voice/decoder-warmup.mjs";

function fake({ ready = Promise.resolve(), send } = {}) {
  const listeners = new Map();
  let removed = 0, sent = 0;
  const recognizer = {
    ready: () => ready,
    on: (event, fn) => listeners.set(event, fn),
    acceptWaveformFloat(data, rate) {
      sent++;
      assert.equal(rate, 16000);
      assert.equal(data.length, 16000);
      assert.ok(data.every(x => x === 0));
      send?.(listeners);
    },
    remove: () => removed++,
  };
  return { recognizer, get removed() { return removed; }, get sent() { return sent; } };
}
test("warmup primes the retained recognizer with silence only after readiness", async () => {
  const f = fake({ send: listeners => listeners.get("partialresult")({}) });
  await primeRecognizer(f.recognizer);
  assert.equal(f.sent, 1);
  assert.equal(f.removed, 0);
});
test("warmup abort during readiness never admits late synthetic audio", async () => {
  const controller = new AbortController();
  let resolve;
  const f = fake({ ready: new Promise(r => resolve = r) });
  const outcome = assert.rejects(primeRecognizer(f.recognizer, controller.signal), { name: "AbortError" });
  controller.abort();
  await outcome;
  resolve();
  await Promise.resolve();
  assert.equal(f.sent, 0);
  assert.equal(f.removed, 0);
});
test("warmup fails closed on worker error; runtime owns recognizer disposal", async () => {
  const f = fake({ send: listeners => listeners.get("error")({ error: "broken" }) });
  await assert.rejects(primeRecognizer(f.recognizer), /broken/);
  assert.equal(f.removed, 0);
});
test("warmup timeout is bounded and late readiness cannot send to removed recognizer", async t => {
  t.mock.timers.enable({ apis: ["setTimeout"] });
  let resolve;
  const f = fake({ ready: new Promise(r => resolve = r) });
  const outcome = assert.rejects(primeRecognizer(f.recognizer), /timed out/);
  t.mock.timers.tick(15000);
  await outcome;
  resolve();
  await Promise.resolve();
  assert.equal(f.sent, 0);
  assert.equal(f.removed, 0);
});
