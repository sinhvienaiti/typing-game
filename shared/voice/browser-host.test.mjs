import test from "node:test";
import assert from "node:assert/strict";
import { createBrowserVoiceHost } from "../../portal/src/voice/host-factory.mjs";
const deferred = () => {
  let resolve;
  const promise = new Promise((r) => {
    resolve = r;
  });
  return { promise, resolve };
};
const tick = () => new Promise((r) => setImmediate(r));
function stream() {
  const track = {
    stops: 0,
    stop() {
      this.stops++;
    },
  };
  return { track, getTracks: () => [track] };
}
function runtime() {
  return {
    engineId: "test",
    modelId: "test",
    sampleRate: 16000,
    nowSample: () => 0,
    closed: 0,
    async close() {
      this.closed++;
    },
    async suspend() {},
    async resume() {},
    async flush() {},
    async applyTargets(s) {
      return { ready: s.targets.map((t) => t.unitId), unsupported: [] };
    },
  };
}
function environment(getUserMedia, locks) {
  const descriptors = new Map(
    ["window", "navigator"].map((key) => [
      key,
      Object.getOwnPropertyDescriptor(globalThis, key),
    ]),
  );
  Object.defineProperty(globalThis, "window", {
    value: { isSecureContext: true },
    configurable: true,
  });
  Object.defineProperty(globalThis, "navigator", {
    value: { locks, mediaDevices: { getUserMedia } },
    configurable: true,
  });
  return () => {
    for (const [key, descriptor] of descriptors) {
      if (descriptor) Object.defineProperty(globalThis, key, descriptor);
      else delete globalThis[key];
    }
  };
}
class Locks {
  held = false;
  async request(_name, _options, callback) {
    if (this.held) return callback(null);
    this.held = true;
    try {
      await callback({});
    } finally {
      this.held = false;
    }
  }
}
test("cancel before a Web Lock callback cannot request permission or retain ownership later", async () => {
  const gate = deferred();
  let requested = 0,
    released = false;
  const restore = environment(
    async () => {
      requested++;
      return stream();
    },
    {
      async request(_n, _o, cb) {
        await gate.promise;
        await cb({});
        released = true;
      },
    },
  );
  const host = createBrowserVoiceHost(
    () => {},
    async () => ({ BrowserVoiceRuntime: { create: async () => runtime() } }),
  );
  try {
    const start = host.start(0);
    await tick();
    await host.stop();
    gate.resolve();
    assert.equal(await start, false);
    await tick();
    assert.equal(requested, 0);
    assert.equal(released, true);
  } finally {
    await host.stop();
    restore();
  }
});
test("stop during native permission releases the lock immediately; a late stream is stopped before decoding", async () => {
  const gate = deferred(),
    locks = new Locks(),
    capture = stream();
  let decoded = 0;
  const restore = environment(() => gate.promise, locks);
  const host = createBrowserVoiceHost(
    () => {},
    async () => ({
      BrowserVoiceRuntime: {
        create: async () => {
          decoded++;
          return runtime();
        },
      },
    }),
  );
  try {
    const start = host.start(0);
    await tick();
    assert.equal(locks.held, true);
    await host.stop();
    await tick();
    assert.equal(locks.held, false);
    gate.resolve(capture);
    assert.equal(await start, false);
    assert.equal(capture.track.stops, 1);
    assert.equal(decoded, 0);
  } finally {
    await host.stop();
    restore();
  }
});
test("disposal of a late old decoder cannot release the new session's microphone lock", async () => {
  const gate = deferred(),
    locks = new Locks(),
    oldRuntime = runtime(),
    newRuntime = runtime();
  let decodes = 0;
  const restore = environment(async () => stream(), locks);
  const host = createBrowserVoiceHost(
    () => {},
    async () => ({
      BrowserVoiceRuntime: {
        create: async () => (++decodes === 1 ? gate.promise : newRuntime),
      },
    }),
  );
  try {
    const first = host.start(0);
    await tick();
    assert.equal(host.state, "PREPARING");
    assert.equal(await host.start(1), true);
    assert.equal(locks.held, true);
    gate.resolve(oldRuntime);
    assert.equal(await first, false);
    assert.equal(oldRuntime.closed, 1);
    assert.equal(locks.held, true);
    assert.equal(newRuntime.closed, 0);
    await host.stop();
    await tick();
    assert.equal(locks.held, false);
  } finally {
    await host.stop();
    restore();
  }
});

test("stop aborts model/decoder preparation without retaining the device or awaiting its normal timeout", async () => {
  const locks = new Locks();
  let aborted = 0;
  const restore = environment(async () => stream(), locks);
  const host = createBrowserVoiceHost(
    () => {},
    async () => ({
      BrowserVoiceRuntime: {
        create: (_stream, _callbacks, signal) =>
          new Promise((_resolve, reject) => {
            signal.addEventListener(
              "abort",
              () => {
                aborted++;
                reject(signal.reason);
              },
              { once: true },
            );
          }),
      },
    }),
  );
  try {
    const start = host.start(0);
    await tick();
    assert.equal(host.state, "PREPARING");
    await host.stop();
    assert.equal(await start, false);
    await tick();
    assert.equal(aborted, 1);
    assert.equal(locks.held, false);
  } finally {
    await host.stop();
    restore();
  }
});

test("the production factory reports permission and model/audio progress instead of silently discarding it", async () => {
  const restore = environment(async () => stream(), new Locks());
  const events = [];
  const host = createBrowserVoiceHost(event => events.push(event), async () => ({ BrowserVoiceRuntime: { create: async (_stream, callbacks) => {
    callbacks.onStatus("audio", "Starting audio capture…");
    return runtime();
  } } }));
  try {
    assert.equal(await host.start(4), true);
    assert.deepEqual(events.filter(e => e.type === "preparing").map(e => [e.inputEpoch, e.stage]), [[4, "permission"], [4, "model"], [4, "audio"]]);
    assert.equal(events.at(-1).type, "ready");
  } finally { await host.stop(); restore(); }
});
