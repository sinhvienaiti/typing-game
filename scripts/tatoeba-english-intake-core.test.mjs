import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import crypto from "node:crypto";
import { gzipSync } from "node:zlib";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";
import { readTatoebaEnglishSnapshot, selectTatoebaEnglishReview, tatoebaEnglishCandidate, validateTatoebaEnglishEvidence, TATOEBA_ENGLISH_PIN } from "./tatoeba-english-intake-core.mjs";
import { applyEnglishReviewDecision, englishContentReviewSourceDigest } from "./english-review-core.mjs";
import { readEnglishReviewLedger } from "./english-review-core.mjs";
import { readReviewedTatoebaEnglish, validateTatoebaControlledSource } from "./english-tatoeba-reviewed.mjs";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const pin = { schemaVersion: 1, source: "tatoeba", snapshot: "test-only", license: "CC-BY-2.0-FR" };
const evidence = (id = 1, text = "We should take the next train.") => ({
  id, text, owner: "owner", ownerEnglishLevel: 5,
  created: "2019-01-01 00:00:00", modified: "2020-01-01 00:00:00",
  positiveReviews: [{ user: "other", englishLevel: 5, modified: "2021-01-01 00:00:00" }],
  negativeReviews: [], actionTags: [],
});

test("source evidence never becomes editorial approval or an invented CEFR level", () => {
  const record = tatoebaEnglishCandidate(evidence(), pin);
  assert.equal(record.quality.state, "candidate");
  assert.equal(record.cefr, undefined);
  for (const name of ["grammar", "naturalness", "cefr", "exactDuplicate", "nearDuplicate", "license"]) assert.equal(record.quality.checks[name].status, "pending");
  assert.throws(() => applyEnglishReviewDecision(record, {
    id: "test", recordId: record.id, sourceDigest: englishContentReviewSourceDigest(record), targetState: "published", checks: {},
  }), /publication blocked/);
});

test("rejects owner self-rating, stale ratings, non-native and duplicate raters", () => {
  for (const mutation of [
    row => { row.positiveReviews[0].user = row.owner; },
    row => { row.positiveReviews[0].modified = "2018-01-01 00:00:00"; },
    row => { row.positiveReviews[0].englishLevel = 4; },
    row => { row.ownerEnglishLevel = 4; },
    row => { row.positiveReviews.push({ ...row.positiveReviews[0] }); },
    row => { row.positiveReviews = []; },
    row => { row.negativeReviews.push({ user: "anyone" }); },
    row => { row.actionTags.push("@change"); },
  ]) {
    const row = evidence(); mutation(row); assert.throws(() => validateTatoebaEnglishEvidence(row));
  }
});

test("rejects malformed IDs, metadata and unsupported typing text", () => {
  for (const patch of [{ id: 0 }, { id: 1.5 }, { owner: "" }, { modified: "bad" }, { text: "Short." },
    { text: "We should take train number 42." }, { text: "we should take the next train." },
    { text: "We should take the next train" }, { text: "We should take the nächst train." }]) {
    assert.throws(() => validateTatoebaEnglishEvidence({ ...evidence(), ...patch }));
  }
});

test("preserves upstream null creation dates without inventing timestamps", () => {
  assert.equal(validateTatoebaEnglishEvidence({ ...evidence(), created: "\\N" }).created, "\\N");
  assert.throws(() => validateTatoebaEnglishEvidence({ ...evidence(), modified: "\\N" }));
});

test("prioritizes independent evidence, deduplicates and reserves historical IDs", () => {
  const a = evidence(3); a.positiveReviews.push({ user: "third", englishLevel: 5, modified: "2022-01-01 00:00:00" });
  const rows = [evidence(1), evidence(2, "We need a much larger room."), a, evidence(4, "We have already seen this film."), evidence(5, "I will be there tomorrow morning.")];
  const packet = selectTatoebaEnglishReview({ rows, pin, controlled: [{ id: "sent.tatoeba.2", text: "Historical text must remain intact." }, { id: "sent.local.x", text: "We have already seen this film." }], reviewedIds: new Set(["sent.tatoeba.5"]), limit: 24 });
  assert.deepEqual(packet.candidates.map(x => x.record.id), ["sent.tatoeba.3"]);
  assert.equal(packet.state, "partial-source-tail");
  assert.deepEqual(packet.selection, { totalSource: 5, existingId: 1, existingText: 1, duplicateSourceText: 1, reviewed: 1, available: 1, selected: 1, remainingAfterSelection: 0, requestedLimit: 24 });
});

test("empty source replaces stale work with a truthful exhausted packet", () => {
  const result = selectTatoebaEnglishReview({ rows: [evidence()], pin, reviewedIds: new Set(["sent.tatoeba.1"]) });
  assert.equal(result.state, "source-exhausted"); assert.deepEqual(result.candidates, []);
  assert.equal(result.approval, "pending-editorial-review");
});

test("strict limits reject fractions, missing values, garbage and out-of-range requests", () => {
  for (const limit of [0, 201, 1.2, NaN, Infinity, "24"]) assert.throws(() => selectTatoebaEnglishReview({ rows: [], pin, limit }));
  for (const arg of ["1.2", "24junk", "0"]) {
    const child = spawnSync(process.execPath, ["scripts/prepare-tatoeba-english-review.mjs", "--limit", arg], { cwd: root, encoding: "utf8" });
    assert.notEqual(child.status, 0); assert.match(child.stderr, /integer from 1 to 200/);
  }
});

async function fixture(t, rows = [evidence()]) {
  const dir = await fs.mkdtemp(path.join(os.tmpdir(), "tatoeba-english-test-"));
  t.after(() => fs.rm(dir, { recursive: true, force: true }));
  const raw = Buffer.from(rows.map(row => JSON.stringify(row)).join("\n") + "\n");
  const zipped = gzipSync(raw);
  const hash = data => crypto.createHash("sha256").update(data).digest("hex");
  const relative = "content/english/sources/tatoeba-english-2026-10-31/000.jsonl.gz.b64";
  const document = { ...pin, candidateCount: rows.length, canonicalShards: [{ path: relative, count: rows.length, compressedBytes: zipped.length, compressedSha256: hash(zipped), contentBytes: raw.length, contentSha256: hash(raw) }] };
  await fs.mkdir(path.dirname(path.join(dir, relative)), { recursive: true });
  await fs.writeFile(path.join(dir, relative), zipped.toString("base64") + "\n");
  const save = () => fs.writeFile(path.join(dir, TATOEBA_ENGLISH_PIN), JSON.stringify(document));
  await save(); return { dir, relative, document, save };
}

test("round-trips the canonical archive and rejects byte tampering", async t => {
  const f = await fixture(t);
  assert.deepEqual((await readTatoebaEnglishSnapshot(f.dir)).rows, [evidence()]);
  await fs.appendFile(path.join(f.dir, f.relative), "bogus!");
  await assert.rejects(readTatoebaEnglishSnapshot(f.dir), /checksum mismatch/);
});

test("rejects content hash drift, wrong counts and traversal paths", async t => {
  for (const mutate of [
    p => { p.canonicalShards[0].contentSha256 = "0".repeat(64); },
    p => { p.canonicalShards[0].count++; },
    p => { p.candidateCount++; },
    p => { p.canonicalShards[0].path = "../../outside"; },
  ]) {
    const f = await fixture(t); mutate(f.document); await f.save(); await assert.rejects(readTatoebaEnglishSnapshot(f.dir));
  }
});

test("rejects duplicate or unordered stable IDs inside an otherwise checksum-valid archive", async t => {
  for (const rows of [[evidence(), evidence()], [evidence(2), evidence(1)]]) {
    const f = await fixture(t, rows); await assert.rejects(readTatoebaEnglishSnapshot(f.dir), /unique and strictly increasing/);
  }
});

test("approved repository snapshot is independently decodable and remains candidate-only", async () => {
  const { pin: approved, rows } = await readTatoebaEnglishSnapshot(root);
  assert.equal(rows.length, 122212);
  assert.equal(approved.sourceAnalysis.englishRows, 2040024);
  assert.equal(rows.filter(row => row.positiveReviews.length >= 2).length, 623);
  const packet = selectTatoebaEnglishReview({ rows, pin: approved });
  assert.equal(packet.candidates.length, 24);
  assert.ok(packet.candidates.every(row => row.sourceDigest === englishContentReviewSourceDigest(row.record)));
  assert.ok(packet.candidates.every(row => row.record.quality.state === "candidate"));
});

test("controlled edits require modification disclosure and exact sentence-level attribution", () => {
  const row=evidence(); const record=tatoebaEnglishCandidate(row,pin);
  assert.doesNotThrow(()=>validateTatoebaControlledSource([record],[row],pin));
  for(const mutate of [
    r=>{r.text="We should take a different train.";},
    r=>{r.provenance.sources[0].license="unknown";},
    r=>{r.provenance.sources[0].sourceId="2";},
    r=>{r.provenance.sources[0].snapshot="other";},
    r=>{r.provenance.sources[0].attribution="Tatoeba";},
  ]) { const changed=structuredClone(record);mutate(changed);assert.throws(()=>validateTatoebaControlledSource([changed],[row],pin)); }
  record.text="We should take a different train.";
  record.provenance.sources[0].modified=true;
  record.provenance.note+=" Editorial edit: clarify the choice of train.";
  assert.doesNotThrow(()=>validateTatoebaControlledSource([record],[row],pin));
});

test("pilot decisions keep rejected source evidence out of the published set", async t=>{
  const manifest=JSON.parse(await fs.readFile(path.join(root,"content/english/batches/manifest.json"),"utf8"));
  const ledger=await readEnglishReviewLedger(root);
  const records=await readReviewedTatoebaEnglish(root,manifest,ledger);
  const pilotIds=new Set(["8732888","1286","16234","17019","17085","17100","17177","20916","20990","29357","29607","30605","34327","34340","35251","37773","38307","38869","43666","51773","54816","58092","58223","60190"].map(id=>`sent.tatoeba.${id}`));
  const pilot=records.filter(row=>pilotIds.has(row.id));
  assert.equal(pilot.length,24);
  assert.equal(pilot.filter(row=>row.quality.state==="published").length,20);
  for(const id of [8732888,30605,34327,38307]) assert.equal(pilot.find(row=>row.id===`sent.tatoeba.${id}`).quality.state,"deprecated");
  assert.equal(pilot.find(row=>row.id==="sent.tatoeba.54816").text,"I hurt my eye when my contact lens slipped out of place.");
  const snapshot=await readTatoebaEnglishSnapshot(root);
  validateTatoebaControlledSource(pilot,snapshot.rows,snapshot.pin);
  const missing=structuredClone(ledger);
  missing.decisions=missing.decisions.filter(row=>row.recordId!=="sent.tatoeba.1286");
  await assert.rejects(readReviewedTatoebaEnglish(root,manifest,missing),/explicit English-only editorial decision/);
  const temp=await fs.mkdtemp(path.join(os.tmpdir(),"tatoeba-no-cefr-"));
  t.after(()=>fs.rm(temp,{recursive:true,force:true}));
  const batch=manifest.batches.find(row=>row.id==="e11.tatoeba-english-reviewed-slice-01");
  const relative=batch.recordSets[0].path;
  const authoring=JSON.parse(await fs.readFile(path.join(root,relative),"utf8"));
  const changed=authoring.records.find(row=>row.id==="sent.tatoeba.1286");delete changed.cefr;
  const changedLedger=structuredClone(ledger);
  changedLedger.decisions.find(row=>row.batchId===batch.id&&row.recordId===changed.id).sourceDigest=englishContentReviewSourceDigest(changed);
  await fs.mkdir(path.dirname(path.join(temp,relative)),{recursive:true});
  await fs.writeFile(path.join(temp,relative),JSON.stringify(authoring));
  await assert.rejects(readReviewedTatoebaEnglish(temp,{batches:[batch]},changedLedger),/explicit reviewed CEFR/);
});
