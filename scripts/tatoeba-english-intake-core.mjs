import crypto from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { gunzipSync } from "node:zlib";
import { normalizeSentenceKey } from "./english-content-core.mjs";
import { englishContentReviewSourceDigest } from "./english-review-core.mjs";

export const TATOEBA_ENGLISH_PIN = "content/english/sources/tatoeba-english-2026-10-31.json";
export const TATOEBA_ENGLISH_RECORD_SET = "reviewed-tatoeba-english-examples";
const sha256 = value => crypto.createHash("sha256").update(value).digest("hex");
const timestamp = value => typeof value === "string" && /^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$/u.test(value);

export function validateTatoebaEnglishEvidence(row) {
  if (!Number.isSafeInteger(row?.id) || row.id < 1 || typeof row.owner !== "string" || !row.owner.trim()) {
    throw new Error("Invalid Tatoeba sentence ID/owner");
  }
  if (typeof row.text !== "string" || !/^[A-Z][\x20-\x7e]*[.?!]$/u.test(row.text) || row.text.length > 300 ||
      /https?:\/\/|www\.|\d|[<>\[\]{}@#]/u.test(row.text)) throw new Error(`Ineligible sentence text: ${row.id}`);
  const words = row.text.match(/[A-Za-z]+(?:'[A-Za-z]+)?/gu) ?? [];
  if (words.length < 5 || words.length > 30) throw new Error(`Ineligible sentence length: ${row.id}`);
  // The detailed export uses literal \N for unavailable creation timestamps.
  // Modification time must be known to establish that ratings are not stale.
  if (row.ownerEnglishLevel !== 5 || !timestamp(row.modified) || !(timestamp(row.created) || row.created === "\\N")) {
    throw new Error(`Missing native-owner/date evidence: ${row.id}`);
  }
  if (!Array.isArray(row.positiveReviews) || row.positiveReviews.length === 0 ||
      !Array.isArray(row.negativeReviews) || row.negativeReviews.length !== 0 ||
      !Array.isArray(row.actionTags) || row.actionTags.length !== 0) throw new Error(`Unresolved source evidence: ${row.id}`);
  const users = new Set();
  for (const review of row.positiveReviews) {
    if (typeof review?.user !== "string" || !review.user.trim() || review.user === row.owner ||
        users.has(review.user) || review.englishLevel !== 5 || !timestamp(review.modified) || review.modified < row.modified) {
      throw new Error(`Invalid/stale/non-independent source rating: ${row.id}`);
    }
    users.add(review.user);
  }
  return row;
}

export async function readTatoebaEnglishSnapshot(root, pinPath = TATOEBA_ENGLISH_PIN) {
  const pin = JSON.parse(await fs.readFile(path.join(root, pinPath), "utf8"));
  if (pin.schemaVersion !== 1 || pin.source !== "tatoeba" || pin.license !== "CC-BY-2.0-FR" ||
      !pin.snapshot || !Array.isArray(pin.canonicalShards) || !pin.canonicalShards.length) throw new Error("Invalid English intake pin");
  const rows = [];
  let previous = 0;
  for (const shard of pin.canonicalShards) {
    if (!/^content\/english\/sources\/tatoeba-english-2026-10-31\/\d{3}\.jsonl\.gz\.b64$/u.test(shard.path)) {
      throw new Error("Invalid canonical shard path");
    }
    const encoded = await fs.readFile(path.join(root, shard.path), "utf8");
    const compressed = Buffer.from(encoded.replace(/\s/gu, ""), "base64");
    if (compressed.toString("base64") !== encoded.replace(/\s/gu, "") || compressed.length !== shard.compressedBytes ||
        sha256(compressed) !== shard.compressedSha256) throw new Error(`Canonical compressed checksum mismatch: ${shard.path}`);
    const raw = gunzipSync(compressed, { maxOutputLength: 64 * 1024 * 1024 });
    if (raw.length !== shard.contentBytes || sha256(raw) !== shard.contentSha256 || !raw.toString("utf8").endsWith("\n")) {
      throw new Error(`Canonical content checksum mismatch: ${shard.path}`);
    }
    const lines = raw.toString("utf8").slice(0, -1).split("\n");
    if (lines.length !== shard.count) throw new Error(`Canonical shard count mismatch: ${shard.path}`);
    for (const line of lines) {
      const row = validateTatoebaEnglishEvidence(JSON.parse(line));
      if (row.id <= previous) throw new Error("Canonical IDs must be unique and strictly increasing");
      previous = row.id;
      rows.push(row);
    }
  }
  if (rows.length !== pin.candidateCount) throw new Error("Canonical snapshot total mismatch");
  return { pin, rows };
}

export function tatoebaEnglishCandidate(row, pin) {
  validateTatoebaEnglishEvidence(row);
  const pending = method => ({ status: "pending", method });
  return {
    schemaVersion: 1,
    id: `sent.tatoeba.${row.id}`,
    text: row.text,
    contexts: ["typing-practice"],
    quality: {
      state: "candidate",
      checks: {
        schema: { status: "pass", method: "tatoeba-english-intake-v1" },
        sourcePin: { status: "pass", method: "canonical-and-compressed-sha256-v1" },
        grammar: pending("editorial-review-required"),
        naturalness: pending("editorial-review-required"),
        sourceSuitability: pending("standalone-learning-content-review-required"),
        cefr: pending("editorial-cefr-review-required"),
        exactDuplicate: pending("controlled-corpus-review-required"),
        nearDuplicate: pending("controlled-corpus-review-required"),
        license: pending("source-attribution-review-required"),
      },
    },
    provenance: {
      sources: [{
        dataset: "tatoeba",
        sourceId: String(row.id),
        sourceUrl: `https://tatoeba.org/en/sentences/show/${row.id}`,
        snapshot: pin.snapshot,
        license: pin.license,
        attribution: `Tatoeba Project; current owner ${row.owner}; contributor history at the sentence URL`,
        modified: false,
      }],
      note: "Pinned English-only intake. Current owner is not asserted to be the original/sole author. Experimental upstream ratings prioritize review; they do not constitute local editorial approval or CEFR evidence.",
    },
  };
}

export function selectTatoebaEnglishReview({ rows, pin, controlled = [], reviewedIds = new Set(), limit = 24 }) {
  if (!Number.isInteger(limit) || limit < 1 || limit > 200) throw new Error("--limit must be an integer from 1 to 200");
  const ids = new Set(controlled.map(row => row.id));
  const texts = new Set(controlled.filter(row => typeof row.text === "string").map(row => normalizeSentenceKey(row.text)));
  const seen = new Set();
  const selected = [];
  const counts = { totalSource: rows.length, existingId: 0, existingText: 0, duplicateSourceText: 0, reviewed: 0, available: 0, selected: 0 };
  // Prefer two independent ratings, preserving a deterministic ID tie-break.
  const ordered = [...rows].sort((a, b) => b.positiveReviews.length - a.positiveReviews.length || a.id - b.id);
  for (const row of ordered) {
    const id = `sent.tatoeba.${row.id}`;
    const key = normalizeSentenceKey(row.text);
    if (reviewedIds.has(id)) { counts.reviewed++; continue; }
    if (ids.has(id)) { counts.existingId++; continue; }
    if (texts.has(key)) { counts.existingText++; continue; }
    if (seen.has(key)) { counts.duplicateSourceText++; continue; }
    seen.add(key);
    counts.available++;
    if (selected.length < limit) {
      const record = tatoebaEnglishCandidate(row, pin);
      selected.push({ record, sourceDigest: englishContentReviewSourceDigest(record), sourceEvidence: row });
    }
  }
  counts.selected = selected.length;
  return {
    schemaVersion: 1,
    kind: "english-content-review-packet",
    recordSetId: TATOEBA_ENGLISH_RECORD_SET,
    sourceSnapshot: pin.snapshot,
    state: selected.length === 0 ? "source-exhausted" : selected.length < limit ? "partial-source-tail" : "ready-for-editorial-review",
    approval: "pending-editorial-review",
    selection: { ...counts, remainingAfterSelection: counts.available - counts.selected, requestedLimit: limit },
    candidates: selected,
  };
}
