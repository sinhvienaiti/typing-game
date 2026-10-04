import { test } from "node:test";
import assert from "node:assert/strict";
import { ParentVoiceBridge } from "./bridge.mjs";
import { envelope, feedback } from "./fixtures.mjs";
function setup(options) {
  const posted = [], source = { postMessage: (data, origin) => posted.push({ data, origin }) };
  const frame = { contentWindow: source }, game = { id: "space-typing", appUrl: "https://space.typing-game.local/game" };
  const bridge = new ParentVoiceBridge(options);
  const send = (op, fields = {}, overrides = {}) => bridge.handleMessage({ data: envelope(op, fields), source, origin: "https://space.typing-game.local", ...overrides }, frame, game);
  return { bridge, send, posted, source, frame, game };
}
test("source, exact origin, game, version and instance are fenced before host creation", () => {
  let factories = 0; const s = setup({ createHost: () => { factories++; } });
  for (const overrides of [{ source: {} }, { origin: "https://evil.example" }]) s.send("hello", { versions: [1] }, overrides);
  s.send("hello", { versions: [1], gameId: "other" }); s.send("hello", { versions: [1], version: 2 });
  assert.equal(s.posted.length, 0); assert.equal(factories, 0);
  s.send("hello", { versions: [1] }); assert.equal(s.posted[0].origin, "https://space.typing-game.local");
  s.send("configure", { mode: "voice", language: "en", policyVersion: "v2", inputEpoch: 0, gameInstanceId: "old-instance" });
  s.send("start", { inputEpoch: 0 }); assert.equal(factories, 0);
});
test("production default honestly blocks Voice without any microphone or remote fallback", () => {
  const { send, posted } = setup(); send("hello", { versions: [1] }); assert.equal(posted[0].data.offlineEngineAvailable, false);
  send("configure", { mode: "voice", language: "en", policyVersion: "v2", inputEpoch: 0 }); send("start", { inputEpoch: 0 });
  assert.equal(posted.at(-1).data.code, "offline-engine-not-validated");
});
test("feedback forwards to the bound iframe only and dies with the host binding", () => {
  let callback;
  const s = setup({ createHost: (cb) => { callback = cb; return { session: { sessionId: "session", inputEpoch: 0 }, start: async () => {}, stop: async () => {} }; } });
  s.send("hello", { versions: [1] }); s.send("configure", { mode: "voice", language: "en", policyVersion: "v2", inputEpoch: 0 }); s.send("start", { inputEpoch: 0 });
  callback({ type: "feedback", ...feedback() });
  assert.deepEqual(s.posted.at(-1), { data: envelope("feedback", feedback()), origin: "https://space.typing-game.local" });
  s.bridge.reset(); const count = s.posted.length;
  callback({ type: "feedback", ...feedback({ transcript: "late" }) }); assert.equal(s.posted.length, count);
});
test("Typing/start and unrelated messages cannot create a host", () => {
  let created = 0; const s = setup({ createHost: () => { created++; } }); s.send("hello", { versions: [1] }); s.send("start", { inputEpoch: 0 });
  assert.equal(created, 0); assert.equal(s.bridge.handleMessage({ data: { type: "typing-game:learning:v1:query" } }, s.frame, s.game), false);
});
test("route reset and iframe reload invalidate old host callbacks immediately", () => {
  let callback, stopped = 0; const s = setup({ createHost: (cb) => { callback = cb; return { session: { sessionId: "session", inputEpoch: 1 }, start: async () => {}, stop: async () => { stopped++; } }; } });
  s.send("hello", { versions: [1] }); s.send("configure", { mode: "hybrid", language: "en", policyVersion: "v2", inputEpoch: 1 }); s.send("start", { inputEpoch: 1 });
  s.bridge.reset(); const length = s.posted.length; callback({ type: "error", code: "late", message: "late result" });
  assert.equal(s.posted.length, length); assert.equal(stopped, 1);
  s.send("hello", { versions: [1], gameInstanceId: "new-instance" }); s.send("start", { inputEpoch: 1 }); assert.equal(s.posted.at(-1).data.type, "typing-game:voice:v1:capabilities");
});
test("stop replies with the old session ACK and old-session messages cannot operate a new host", async () => {
  let stops = 0; const s = setup({ createHost: () => ({ session: { sessionId: "session", inputEpoch: 1 }, start: async () => {}, stop: async () => { stops++; } }) });
  s.send("hello", { versions: [1] }); s.send("configure", { mode: "hybrid", language: "en", policyVersion: "v2", inputEpoch: 1 }); s.send("start", { inputEpoch: 1 });
  s.send("stop", { sessionId: "wrong-session", inputEpoch: 1 }); assert.equal(stops, 0);
  s.send("stop", { sessionId: "session", inputEpoch: 1 }); await new Promise((r) => setImmediate(r));
  assert.equal(s.posted.at(-1).data.type, "typing-game:voice:v1:stopped"); assert.equal(stops, 1);
});
