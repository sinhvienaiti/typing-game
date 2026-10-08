import test from "node:test";
import assert from "node:assert/strict";
import { loadOfflineVoskWorker } from "../../scripts/offline-vosk-plugin.mjs";

test("pinned worker avoids PCM serialization and retains explicit ready acknowledgement", () => {
  const { source, hash, fileName } = loadOfflineVoskWorker();
  assert.ok(!source.includes("this.logger.debug(JSON.stringify(message))"));
  assert.ok(source.includes("this.logger.debug(message.action)"));
  assert.ok(source.includes('event: "recognizer-ready"'));
  assert.ok(fileName.includes(hash.slice(0, 12)));
});

test("cancellation disposes buffers/recognizer without decoding discarded final speech", () => {
  const { source } = loadOfflineVoskWorker();
  const removal = source.slice(source.indexOf("        removeRecognizer(recognizerId) {"), source.indexOf("        terminate() {"));
  assert.ok(!removal.includes(".FinalResult()"));
  assert.ok(removal.includes("this.freeBuffer(recognizer)"));
  assert.ok(removal.includes("recognizer.recognizer.delete()"));
  assert.ok(removal.includes("this.recognizers.delete(recognizerId)"));
  // Explicit retrieval elsewhere remains upstream behavior; only cancellation changes.
  assert.ok(source.includes("recognizer.recognizer.FinalResult()"));
});
