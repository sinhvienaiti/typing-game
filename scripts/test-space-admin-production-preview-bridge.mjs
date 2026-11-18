import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { createRequire } from "node:module";

const requireFromPortal = createRequire(new URL("../portal/package.json", import.meta.url));
const ts = requireFromPortal("typescript");
const bridgeSource = await readFile(
  new URL("../portal/src/admin/v2/preview/production-preview-bridge.ts", import.meta.url),
  "utf8",
);
const transpiled = ts.transpileModule(bridgeSource, {
  compilerOptions: {
    module: ts.ModuleKind.ES2022,
    target: ts.ScriptTarget.ES2022,
    useDefineForClassFields: true,
  },
  fileName: "production-preview-bridge.ts",
}).outputText;
const bridgeModule = await import(`data:text/javascript;base64,${Buffer.from(transpiled).toString("base64")}`);
const { ProductionPreviewBridge, ProductionPreviewStaleError } = bridgeModule;

const originalWindow = globalThis.window;
const originalDocument = globalThis.document;
const origin = "https://space-typing.example";
const messageListeners = new Set();
const animationFrames = new Map();
const postedMessages = [];
let nextAnimationFrame = 1;
let iframeRemoved = false;
let deferNextType = null;
let deferredCommand = null;

const emitMessage = (data) => {
  const event = { origin, source: frameWindow, data };
  for (const listener of [...messageListeners]) listener(event);
};

const appliedResponse = (message) => ({
  protocolVersion: message.protocolVersion,
  previewSessionId: message.previewSessionId,
  nonce: message.nonce,
  requestId: message.requestId,
  type: message.type === "DISPOSE" ? "DISPOSED" : "APPLIED",
  payload: message.payload,
});

const frameWindow = {
  postMessage(message, targetOrigin) {
    assert.equal(targetOrigin, origin);
    postedMessages.push(message);
    if (message.type === deferNextType) {
      deferNextType = null;
      deferredCommand = message;
      return;
    }
    queueMicrotask(() => emitMessage(appliedResponse(message)));
  },
};

const iframe = {
  className: "",
  title: "",
  referrerPolicy: "",
  loading: "",
  allow: "",
  src: "",
  contentWindow: frameWindow,
  setAttribute() {},
  remove() { iframeRemoved = true; },
};

const fakeWindow = {
  setTimeout: globalThis.setTimeout.bind(globalThis),
  clearTimeout: globalThis.clearTimeout.bind(globalThis),
  requestAnimationFrame(callback) {
    const id = nextAnimationFrame++;
    animationFrames.set(id, callback);
    return id;
  },
  cancelAnimationFrame(id) {
    animationFrames.delete(id);
  },
  addEventListener(type, listener) {
    if (type === "message") messageListeners.add(listener);
  },
  removeEventListener(type, listener) {
    if (type === "message") messageListeners.delete(listener);
  },
};

const fakeDocument = {
  createElement(tag) {
    assert.equal(tag, "iframe");
    return iframe;
  },
};

const flushAnimationFrames = () => {
  const callbacks = [...animationFrames.values()];
  animationFrames.clear();
  for (const callback of callbacks) callback(16);
};

const flushMicrotasks = async () => {
  await Promise.resolve();
};

globalThis.window = fakeWindow;
globalThis.document = fakeDocument;

try {
  const adapter = Object.freeze({
    domain: "test",
    defaultScenario: "idle",
    candidatePayload: (candidate) => candidate,
    scenarioPayload: (scenario) => ({ scenario }),
    tuningPayload: (tuning) => ({ visual: tuning }),
  });
  const bridge = new ProductionPreviewBridge(
    Object.freeze({ origin, url: new URL(`${origin}/admin-preview.html`) }),
    adapter,
  );

  const iframeUrl = new URL(iframe.src);
  emitMessage({
    protocolVersion: 1,
    previewSessionId: iframeUrl.searchParams.get("previewSession"),
    nonce: iframeUrl.searchParams.get("nonce"),
    requestId: 0,
    type: "READY",
  });
  await bridge.waitUntilReady();

  const first = bridge.loadCandidate(Object.freeze({ id: "candidate-a" }));
  const second = bridge.loadCandidate(Object.freeze({ id: "candidate-b" }));
  const settled = Promise.allSettled([first, second]);

  assert.equal(animationFrames.size, 1, "same-frame candidates should share one render-frame flush");
  flushAnimationFrames();
  const [firstResult, secondResult] = await settled;

  assert.equal(firstResult.status, "rejected", "superseded same-frame candidate must reject");
  assert.ok(
    firstResult.reason instanceof ProductionPreviewStaleError,
    "superseded candidate must reject with ProductionPreviewStaleError",
  );
  assert.equal(secondResult.status, "fulfilled", "latest same-frame candidate should resolve");
  assert.deepEqual(secondResult.value, { id: "candidate-b" });

  const loads = postedMessages.filter((message) => message.type === "LOAD_CANDIDATE");
  assert.equal(loads.length, 1, "coalescing should send only the latest same-frame candidate");
  assert.deepEqual(loads[0].payload, { id: "candidate-b" });

  postedMessages.length = 0;
  deferNextType = "LOAD_CANDIDATE";
  const inFlightOld = bridge.loadCandidate(Object.freeze({ id: "candidate-in-flight-old" }));
  flushAnimationFrames();
  await flushMicrotasks();
  assert.ok(deferredCommand, "older candidate should be in flight before the newer candidate is queued");

  const inFlightLatest = bridge.loadCandidate(Object.freeze({ id: "candidate-in-flight-latest" }));
  flushAnimationFrames();
  const oldMessage = deferredCommand;
  deferredCommand = null;
  emitMessage({
    protocolVersion: oldMessage.protocolVersion,
    previewSessionId: oldMessage.previewSessionId,
    nonce: oldMessage.nonce,
    requestId: oldMessage.requestId,
    type: "ERROR",
    payload: { message: "Ship preview candidate was superseded by a newer request." },
  });
  const [oldInFlightResult, latestInFlightResult] = await Promise.allSettled([inFlightOld, inFlightLatest]);
  assert.equal(oldInFlightResult.status, "rejected", "older in-flight candidate must reject");
  assert.ok(
    oldInFlightResult.reason instanceof ProductionPreviewStaleError,
    "older in-flight child rejection must be normalized to ProductionPreviewStaleError",
  );
  assert.equal(latestInFlightResult.status, "fulfilled", "latest in-flight candidate should remain authoritative");

  deferNextType = "SET_TUNING";
  const staleTuning = bridge.setTuning(Object.freeze({ glow: 1.25 }));
  await flushMicrotasks();
  assert.ok(deferredCommand, "tuning command should be in flight before stale response");
  const tuningMessage = deferredCommand;
  deferredCommand = null;
  emitMessage({
    protocolVersion: tuningMessage.protocolVersion,
    previewSessionId: tuningMessage.previewSessionId,
    nonce: tuningMessage.nonce,
    requestId: tuningMessage.requestId,
    type: "ERROR",
    payload: { message: "Ship preview tuning was superseded.", code: "STALE_PREVIEW_COMMAND" },
  });
  await assert.rejects(staleTuning, ProductionPreviewStaleError);

  postedMessages.length = 0;
  const queuedBeforeReset = bridge.loadCandidate(Object.freeze({ id: "candidate-before-reset" }));
  const resetSettled = Promise.allSettled([queuedBeforeReset]);
  assert.equal(animationFrames.size, 1, "candidate should be queued before reset");

  const reset = bridge.reset();
  assert.equal(animationFrames.size, 0, "reset must cancel an unflushed candidate frame");
  const [queuedBeforeResetResult] = await resetSettled;
  await reset;

  assert.equal(queuedBeforeResetResult.status, "rejected", "reset must reject an unflushed candidate");
  assert.ok(
    queuedBeforeResetResult.reason instanceof ProductionPreviewStaleError,
    "reset must reject queued candidate with ProductionPreviewStaleError",
  );
  assert.equal(
    postedMessages.filter((message) => message.type === "LOAD_CANDIDATE").length,
    0,
    "reset must not let a stale queued candidate load after RESET",
  );
  assert.equal(
    postedMessages.filter((message) => message.type === "RESET").length,
    1,
    "reset should issue exactly one RESET command",
  );

  bridge.disposeImmediately();
  assert.equal(iframeRemoved, true, "bridge teardown should remove its iframe");
  assert.equal(messageListeners.size, 0, "bridge teardown should remove its message listener");

  console.log("Production Preview bridge coalescing/reset test passed: stale waiters, in-flight supersession, child stale codes, and reset invalidation are normalized.");
} finally {
  if (originalWindow === undefined) delete globalThis.window;
  else globalThis.window = originalWindow;
  if (originalDocument === undefined) delete globalThis.document;
  else globalThis.document = originalDocument;
}
