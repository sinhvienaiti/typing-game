import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { createRequire } from "node:module";

const requireFromPortal = createRequire(new URL("../portal/package.json", import.meta.url));
const ts = requireFromPortal("typescript");
const studioSource = (await readFile(
  new URL("../portal/src/admin/v2/preview/production-preview-studio.ts", import.meta.url),
  "utf8",
)).replace(/^import "\.\/production-preview-a16\.css";\n/, "");
const transpiled = ts.transpileModule(studioSource, {
  compilerOptions: {
    module: ts.ModuleKind.ES2022,
    target: ts.ScriptTarget.ES2022,
    useDefineForClassFields: true,
  },
  fileName: "production-preview-studio.ts",
}).outputText;
const { createProductionPreviewStudio } = await import(
  `data:text/javascript;base64,${Buffer.from(transpiled).toString("base64")}`
);

class FakeElement {
  constructor(tagName) {
    this.tagName = tagName;
    this.className = "";
    this.textContent = "";
    this.children = [];
    this.attributes = new Map();
    this.listeners = new Map();
    this.tabIndex = -1;
    this.disabled = false;
    this.type = "";
    this.title = "";
    this.removed = false;
  }

  setAttribute(name, value) {
    this.attributes.set(name, String(value));
  }

  getAttribute(name) {
    return this.attributes.get(name) ?? null;
  }

  append(...nodes) {
    this.children.push(...nodes);
  }

  replaceChildren(...nodes) {
    this.children = [...nodes];
  }

  addEventListener(type, listener) {
    const listeners = this.listeners.get(type) ?? new Set();
    listeners.add(listener);
    this.listeners.set(type, listeners);
  }

  removeEventListener(type, listener) {
    this.listeners.get(type)?.delete(listener);
  }

  dispatch(type, event) {
    for (const listener of [...(this.listeners.get(type) ?? [])]) listener(event);
  }

  remove() {
    this.removed = true;
  }
}

const originalDocument = globalThis.document;
const documentListeners = new Map();
const fakeDocument = {
  fullscreenElement: null,
  createElement(tag) {
    return new FakeElement(tag);
  },
  addEventListener(type, listener) {
    const listeners = documentListeners.get(type) ?? new Set();
    listeners.add(listener);
    documentListeners.set(type, listeners);
  },
  removeEventListener(type, listener) {
    documentListeners.get(type)?.delete(listener);
  },
  async exitFullscreen() {},
};
globalThis.document = fakeDocument;

const keyEvent = (target, key) => {
  let prevented = false;
  return {
    target,
    key,
    altKey: false,
    ctrlKey: false,
    metaKey: false,
    preventDefault() { prevented = true; },
    get prevented() { return prevented; },
  };
};

const flushMicrotasks = async () => {
  for (let index = 0; index < 6; index += 1) await Promise.resolve();
};

try {
  const host = new FakeElement("section");
  const statusHost = new FakeElement("div");
  const studio = createProductionPreviewStudio(host, statusHost);
  const root = host.children[0];
  const actionsHost = root.children[1];
  const [resetButton, replayButton] = actionsHost.children;

  assert.equal(resetButton.disabled, true, "Reset must stay disabled until actions are bound");
  assert.equal(replayButton.disabled, true, "Replay must stay disabled until actions are bound");

  let resetCalls = 0;
  let replayCalls = 0;
  let resolveReset;
  const resetPending = new Promise((resolve) => { resolveReset = resolve; });
  studio.bindActions({
    reset: () => {
      resetCalls += 1;
      return resetPending;
    },
    replay: () => {
      replayCalls += 1;
    },
  });
  assert.equal(resetButton.disabled, false);
  assert.equal(replayButton.disabled, false);

  const resetShortcut = keyEvent(root, "r");
  root.dispatch("keydown", resetShortcut);
  assert.equal(resetShortcut.prevented, true);
  assert.equal(resetButton.disabled, true, "Reset should lock both actions immediately");
  assert.equal(replayButton.disabled, true, "Reset should lock Replay immediately");

  const overlappingReplay = keyEvent(root, " ");
  root.dispatch("keydown", overlappingReplay);
  await flushMicrotasks();
  assert.equal(resetCalls, 1, "Reset should run exactly once");
  assert.equal(replayCalls, 0, "keyboard Replay must not overlap an in-flight Reset");

  resolveReset();
  await flushMicrotasks();
  assert.equal(resetButton.disabled, false, "actions should unlock after Reset settles");
  assert.equal(replayButton.disabled, false, "actions should unlock after Reset settles");

  const replayShortcut = keyEvent(root, " ");
  root.dispatch("keydown", replayShortcut);
  await flushMicrotasks();
  assert.equal(replayCalls, 1, "Replay should run after the previous action settles");

  studio.bindActions({
    reset: () => {
      throw new Error("synchronous reset failure");
    },
    replay: () => {},
  });
  root.dispatch("keydown", keyEvent(root, "r"));
  await flushMicrotasks();
  assert.equal(statusHost.className, "st-admin-asset-preview-status bad");
  assert.equal(statusHost.textContent, "synchronous reset failure");
  assert.equal(resetButton.disabled, false, "sync throw must still unlock Reset through finally");
  assert.equal(replayButton.disabled, false, "sync throw must still unlock Replay through finally");

  studio.dispose();
  assert.equal(root.removed, true, "Studio dispose should remove its root");
  assert.equal(documentListeners.get("fullscreenchange")?.size ?? 0, 0, "Studio dispose should remove fullscreen listener");

  console.log("Production Preview Studio action serialization test passed: shortcuts cannot overlap actions and synchronous failures recover cleanly.");
} finally {
  if (originalDocument === undefined) delete globalThis.document;
  else globalThis.document = originalDocument;
}
