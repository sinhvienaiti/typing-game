import test from "node:test";
import assert from "node:assert/strict";
import { mkdtempSync, readFileSync, writeFileSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";
import { selectTypingTextReviewSlice } from "./typing-text-review-core.mjs";

const candidate = id => ({ id, text: `Sentence ${id}.`, quality: { state: "candidate" } });
const select = options => selectTypingTextReviewSlice({ candidates: [], controlled: [], reviewedIds: [], ...options });

test("preserves generator order while excluding controlled and any previously reviewed IDs", () => {
  const input = ["a", "b", "c", "d"].map(candidate);
  const before = structuredClone(input);
  const result = select({ candidates: input, controlled: [{ id: "a" }], reviewedIds: ["a", "c"], limit: 1 });
  assert.equal(result.state, "ready");
  assert.deepEqual(result.records.map(r => r.id), ["b"]);
  assert.equal(result.selection.excludedCount, 2);
  assert.equal(result.selection.remainingAfterSelection, 1);
  assert.deepEqual(input, before);
});

test("returns the final four candidates as a partial 24-record request without fabricating replacements", () => {
  const result = select({ candidates: ["a", "b", "c", "d"].map(candidate) });
  assert.equal(result.state, "partial");
  assert.equal(result.selection.requestedLimit, 24);
  assert.equal(result.selection.selectedCount, 4);
  assert.equal(result.selection.remainingAfterSelection, 0);
});

test("an exhausted queue produces an explicit empty packet rather than replaying reviewed records", () => {
  const result = select({ candidates: [candidate("rejected"), candidate("published")], reviewedIds: ["rejected", "published"] });
  assert.equal(result.state, "source-exhausted");
  assert.deepEqual(result.records, []);
  assert.equal(result.selection.remainingBeforeSelection, 0);
});

test("still rejects duplicate or missing stable IDs", () => {
  assert.throws(() => select({ candidates: [candidate("a"), candidate("a")] }), /duplicate id/);
  assert.throws(() => select({ controlled: [{ id: "a" }, { id: "a" }] }), /duplicate id/);
  assert.throws(() => select({ candidates: [{}] }), /missing record id/);
});

test("still rejects noncandidate intake and invalid limits", () => {
  assert.throws(() => select({ candidates: [{ id: "a", quality: { state: "published" } }] }), /must remain candidate/);
  for (const limit of [0, 201, 1.5, NaN]) assert.throws(() => select({ limit }), /integer from 1 to 200/);
});

test("CLI replaces a stale packet when only four records remain and when the source is exhausted", () => {
  const dir = mkdtempSync(path.join(tmpdir(), "typing-review-"));
  const candidatePath = path.join(dir, "candidates.json");
  const controlledPath = path.join(dir, "controlled.json");
  const output = path.join(dir, "packet.json");
  const records = ["fixture.a", "fixture.b", "fixture.c", "fixture.d"].map(candidate);
  try {
    writeFileSync(candidatePath, JSON.stringify({ records }));
    for (const [controlled, state, count] of [[[], "partial", 4], [records, "source-exhausted", 0]]) {
      writeFileSync(controlledPath, JSON.stringify({ records: controlled }));
      writeFileSync(output, JSON.stringify({ records: [candidate("stale")] }));
      const result = spawnSync(process.execPath, [
        fileURLToPath(new URL("./prepare-typing-text-e11-review-slice.mjs", import.meta.url)),
        "--candidate-path", candidatePath, "--controlled-path", controlledPath,
        "--output", output, "--limit", "24",
      ], { encoding: "utf8" });
      assert.equal(result.status, 0, result.stderr);
      const packet = JSON.parse(readFileSync(output, "utf8"));
      assert.equal(packet.state, state);
      assert.equal(packet.records.length, count);
      assert.equal(packet.selection.requestedLimit, 24);
      assert(!packet.records.some(r => r.id === "stale"));
    }
  } finally {
    rmSync(dir, { recursive: true, force: true });
  }
});

test("CLI rejects fractional and malformed limits instead of silently truncating them", () => {
  for (const limit of ["1.5", "24oops", "0", "201"]) {
    const result = spawnSync(process.execPath, [
      fileURLToPath(new URL("./prepare-typing-text-e11-review-slice.mjs", import.meta.url)),
      "--limit", limit,
    ], { encoding: "utf8" });
    assert.notEqual(result.status, 0);
    assert.match(result.stderr, /integer from 1 to 200/);
  }
});
