import test from "node:test";
import assert from "node:assert/strict";
import { createServer } from "node:http";
import { mkdtemp, mkdir, writeFile, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { gzipSync } from "node:zlib";
import { voiceModelMiddleware } from "../../scripts/voice-model-middleware.mjs";

test("GET/HEAD serve pinned gzip archive as bytes, not HTTP transfer encoding", async () => {
  const dir = await mkdtemp(join(tmpdir(), "voice-model-serving-"));
  const archive = gzipSync(Buffer.from("tar archive fixture"));
  await mkdir(join(dir, "assets/voice"), { recursive: true });
  await writeFile(join(dir, "assets/voice/test.tar.gz"), archive);
  const middleware = voiceModelMiddleware(dir, "test");
  const server = createServer((req, res) => middleware(req, res, () => { res.statusCode = 418; res.end(); }));
  try {
    await new Promise((resolve, reject) => { server.once("error", reject); server.listen(0, "127.0.0.1", resolve); });
    const base = `http://127.0.0.1:${server.address().port}`;
    for (const method of ["GET", "HEAD"]) {
      const response = await fetch(`${base}/assets/voice/test.tar.gz?cache-bust=1`, { method });
      assert.equal(response.status, 200);
      assert.equal(response.headers.get("Content-Encoding"), null);
      assert.equal(response.headers.get("Content-Type"), "application/gzip");
      assert.equal(Number(response.headers.get("Content-Length")), archive.length);
      assert.deepEqual(Buffer.from(await response.arrayBuffer()), method === "GET" ? archive : Buffer.alloc(0));
    }
    assert.equal((await fetch(`${base}/other.tar.gz`)).status, 418);
    await rm(join(dir, "assets/voice/test.tar.gz"));
    assert.equal((await fetch(`${base}/assets/voice/test.tar.gz`)).status, 404);
  } finally {
    server.closeAllConnections();
    await new Promise((resolve) => server.close(resolve));
    await rm(dir, { recursive: true, force: true });
  }
});
