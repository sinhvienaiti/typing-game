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

const emitMessage = (data) => {
  const event = { origin, source: frameWindow, data };
  for (const listener of [...messageListeners]) listener(event);
};

const frameWindow = {
  postMessage(message, targetOrigin) {
    assert.equal(targetOrigin, origin);
    postedMessages.push(message);
    queueMicrotask(() => {
      emitMessage({
        protocolVersion: message.protocolVersion,
        previewSessionId: message.previewSessionId,
        nonce: message.nonce,
        requestId: message.requestId,
        type: message.type === "DISPOSE" ? "DISPOSED" : "APPLIED",
        payload: message.payload,
      });
    });
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

globalThis.window = fakeWindow;
globalThis.document = fakeDocument;

try {
  const adapter = Object.freeze({
    domain: "test",
    defaultScenario: "idle",
    candidatePayload: (candidate) => candidate,
    scenarioPayload: (scenario) => ({ scenario }),
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

  bridge.disposeImmediately();
  assert.equal(iframeRemoved, true, "bridge teardown should remove its iframe");
  assert.equal(messageListeners.size, 0, "bridge teardown should remove its message listener");

  console.log("Production Preview bridge same-frame coalescing test passed: superseded waiter rejects stale and latest candidate resolves.");
} finally {
  if (originalWindow === undefined) delete globalThis.window;
  else globalThis.window = originalWindow;
  if (originalDocument === undefined) delete globalThis.document;
  else globalThis.document = originalDocument;
}
