import test from "node:test";
import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { loadVerifiedAsset } from "./verified-asset.mjs";

const data = new TextEncoder().encode("verified model fixture");
const pin = { url: "/model.tar.gz", bytes: data.length, sha256: createHash("sha256").update(data).digest("hex"), label: "Offline model" };
test("verified cache works offline without fetching", async (t) => {
  t.mock.method(globalThis, "fetch", async () => { throw Error("Must not fetch"); });
  const cache = { match: async () => new Response(data) };
  assert.deepEqual(new Uint8Array(await loadVerifiedAsset({ ...pin, cache })), data);
});
test("bad cache is removed and retried once; only verified network bytes cached", async (t) => {
  let fetches = 0, deleted = 0, written = 0, status = 0;
  t.mock.method(globalThis, "fetch", async () => { fetches++; return new Response(data); });
  const cache = {
    match: async () => new Response("broken"),
    delete: async () => { deleted++; },
    put: async (_url, response) => { written++; assert.deepEqual(new Uint8Array(await response.arrayBuffer()), data); },
  };
  await loadVerifiedAsset({ ...pin, cache, onRetry: () => status++ });
  assert.deepEqual([fetches, deleted, written, status], [1, 1, 1, 1]);
});
test("a corrupt HTTP model never disables integrity or reaches cache", async (t) => {
  let written = 0;
  t.mock.method(globalThis, "fetch", async () => new Response("inflated tar", { headers: { "Content-Encoding": "gzip" } }));
  await assert.rejects(loadVerifiedAsset({ ...pin, cache: { match: async () => undefined, put: async () => written++ } }), /checksum failed.*HTTP encoding: gzip/);
  assert.equal(written, 0);
});
test("abort must not trigger cache-repair download", async (t) => {
  const controller = new AbortController();
  t.mock.method(globalThis, "fetch", async () => { throw Error("Must not fetch"); });
  const cache = { match: async () => { controller.abort(); return new Response(data); } };
  await assert.rejects(loadVerifiedAsset({ ...pin, cache, signal: controller.signal }), { name: "AbortError" });
});
test("cache failure is optional and a same-length wrong hash still fails", async (t) => {
  t.mock.method(globalThis, "fetch", async () => new Response(new Uint8Array(data.length)));
  await assert.rejects(loadVerifiedAsset({ ...pin, cache: { match: async () => { throw Error("Storage blocked"); } } }), /checksum failed/);
});
