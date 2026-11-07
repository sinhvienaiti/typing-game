import fs from "node:fs/promises";
import path from "node:path";
import crypto from "node:crypto";
import assert from "node:assert/strict";
import { fileURLToPath } from "node:url";
import { lexicalTokens, normalizeSentenceKey, readJson } from "./english-content-core.mjs";
import { readEnglishReviewLedger } from "./english-review-core.mjs";
import { assessExampleSourceCapacity } from "./english-example-capacity-core.mjs";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const read = relative => readJson(path.join(root, relative));
const fingerprint = async relative => crypto.createHash("sha256")
  .update(await fs.readFile(path.join(root, relative))).digest("hex");
const [index, sources, targets, manifest, queue, controlled, ledger] = await Promise.all([
  read("shared/typing-texts/index.json"), read("content/english/sources/manifest.json"),
  read("content/english/targets/long-term.json"), read("shared/sentences/manifest.json"),
  read("content/english/review-queues/typing-text-e06-sentences.json"),
  read("content/english/sentences/e06-reviewed-typing-text-sentences.json"),
  readEnglishReviewLedger(root),
]);
const source = sources.sources.find(s => s.id === "project-original");
assert.equal(source?.publishAllowed, true);
assert.equal(source.license, "LicenseRef-Project-Original");
const target = targets.targets.find(t => t.id === "example-sentences");
assert(Number.isInteger(target?.minimum) && target.minimum > 0);

// Match the existing derivation's eligibility/dedup rules; this is an intake
// capacity count, never an editorial approval or an instruction to publish.
const raw = new Map(), seenText = new Set(), inputs = [];
let passageCount = 0;
for (const level of index.levels) {
  const relative = "shared/typing-texts/" + level.file;
  const document = await read(relative);
  inputs.push({ path: relative, sha256: await fingerprint(relative) });
  for (const passage of document.passages) {
    passageCount++;
    const chunks = String(passage.text).normalize("NFC")
      .match(/[^.!?]+(?:[.!?]+|$)/gu)?.map(s => s.trim()).filter(Boolean) ?? [];
    for (let i = 0; i < chunks.length; i++) {
      const text = chunks[i], words = lexicalTokens(text).length;
      if (words < 5 || words > 40) continue;
      const key = normalizeSentenceKey(text);
      if (seenText.has(key)) continue;
      seenText.add(key);
      const id = "sent.tt." + passage.id.toLowerCase() + "." + String(i + 1).padStart(3, "0");
      assert(!raw.has(id), "Repeated stable ID in raw source: " + id);
      raw.set(id, text);
    }
  }
}
const published = [];
for (const shard of manifest.shards.filter(s => s.id.startsWith("examples-"))) {
  const document = await read("shared/sentences/" + shard.path);
  assert.equal(document.records.length, shard.count);
  for (const r of document.records) {
    assert.equal(r.quality?.state, "published");
    assert(!Object.values(r.quality.checks).some(c => c.status === "pending" || c.status === "fail"));
    published.push(r);
  }
}
assert.equal(new Set(published.map(r => r.id)).size, published.length);
for (const r of queue.records) assert.equal(raw.get(r.id), r.text, "Queue is stale against source: " + r.id);
const excluded = new Set([
  ...controlled.records.map(r => r.id),
  ...ledger.decisions.filter(d => d.recordSetId === "reviewed-typing-text-sentences").map(d => d.recordId),
]);
const queueRemaining = queue.records.filter(r => !excluded.has(r.id)).length;
const unreviewedRaw = [...raw.keys()].filter(id => !excluded.has(id)).length;
const capacity = assessExampleSourceCapacity({ minimum: target.minimum, published: published.length, unreviewedRaw });
const upperBound = capacity.optimisticPublishedUpperBound;
const report = {
  schemaVersion: 1,
  scope: "group-1-step-2-current-project-original-intake-capacity",
  reviewState: capacity.reviewState,
  target: { id: target.id, minimum: target.minimum, published: published.length,
    remainingPublishedDeficit: capacity.remainingPublishedDeficit },
  currentBoundedQueue: { candidates: queue.records.length, remainingUnreviewed: queueRemaining,
    state: queueRemaining === 0 ? "source-exhausted" : "ready" },
  currentProjectOriginalLane: {
    levels: index.levels.length, passages: passageCount,
    eligibleUniqueRawSentences: raw.size, unreviewedRawSentences: unreviewedRaw,
    optimisticPublishedUpperBound: upperBound,
    minimumAdditionalSourceGapEvenIfEveryRemainingRawSentencePasses: capacity.additionalSourceGap,
    caveat: "Upper bound for this configured project-original lane only; ignores future QA rejection and cross-source dedup. Other upstream sources require their own reproducible intake and review; their potential size is not credited as published content.",
  },
  source: { id: source.id, snapshot: source.snapshot, license: source.license, publishAllowed: source.publishAllowed },
  sourceFiles: inputs,
  currentEvidence: {
    sentenceManifestSha256: await fingerprint("shared/sentences/manifest.json"),
    reviewLedgerReportSha256: await fingerprint("content/english/reports/e10-review-ledger.json"),
  },
  transition: { step2Pass: capacity.step2Pass, step3Unlocked: capacity.step3Unlocked, group2Unlocked: capacity.group2Unlocked,
    reason: "A capacity audit or a partial corpus expansion does not satisfy the agreed 100,000-reviewed-published-example requirement." },
  remainingWork: [
    "Review remaining local raw candidates only through bounded digest-bound batches; none are approved by this report.",
    "Prepare sufficient additional versioned, checksum-pinned, license/attribution-reviewed example-source intake before claiming full target capacity.",
    "Preserve Tatoeba source-pin and completed MultiWOZ gates; do not silently substitute mutable exports.",
  ],
};
const output = path.join(root, "content/english/reports/example-source-capacity.json");
await fs.writeFile(output, JSON.stringify(report, null, 2) + "\n");
console.log(JSON.stringify({ reviewState: report.reviewState, target: report.target,
  currentBoundedQueue: report.currentBoundedQueue, capacity: report.currentProjectOriginalLane,
  transition: report.transition }, null, 2));
