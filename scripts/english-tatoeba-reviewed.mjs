import path from "node:path";
import { readJson } from "./english-content-core.mjs";
import { applyEnglishReviewDecision, buildEnglishReviewDecisionIndex } from "./english-review-core.mjs";
import { TATOEBA_ENGLISH_RECORD_SET } from "./tatoeba-english-intake-core.mjs";

export async function readReviewedTatoebaEnglish(root, manifest, ledger) {
  const records = [];
  const ids = new Set();
  const decisions = buildEnglishReviewDecisionIndex(ledger);
  for (const batch of manifest.batches ?? []) {
    if (!/^e11\.tatoeba-english-reviewed-slice-\d+$/u.test(batch.id)) continue;
    const sets = (batch.recordSets ?? []).filter(set => set.id === TATOEBA_ENGLISH_RECORD_SET);
    if (sets.length !== 1) throw new Error(`${batch.id}: expected exactly one English-only example set`);
    const set = sets[0];
    const doc = await readJson(path.join(root, set.path));
    const reviewed = doc.records.map(record => {
      const decision = decisions.get(`${batch.id}\u0000${set.id}\u0000${record.id}`);
      if (!decision) throw new Error(`${record.id}: expected one explicit English-only editorial decision`);
      return applyEnglishReviewDecision(record, decision, { requiredChecks: set.requiredChecks });
    });
    for (const record of reviewed) {
      if (ids.has(record.id)) throw new Error(`Duplicate English-only Tatoeba controlled ID: ${record.id}`);
      ids.add(record.id);
      if (record.quality.state === "published" && !["A1", "A2", "B1", "B2", "C1", "C2"].includes(record.cefr)) {
        throw new Error(`${record.id}: publication requires an explicit reviewed CEFR level`);
      }
      records.push(record);
    }
  }
  return records;
}

export function validateTatoebaControlledSource(records, rows, pin) {
  const byId = new Map(rows.map(row => [`sent.tatoeba.${row.id}`, row]));
  const ids = new Set();
  for (const record of records) {
    const row = byId.get(record.id);
    if (!row || ids.has(record.id)) throw new Error(`Unknown/duplicate Tatoeba intake ID: ${record.id}`);
    ids.add(record.id);
    const sources = record.provenance?.sources;
    const source = sources?.[0];
    if (sources?.length !== 1 || source.dataset !== "tatoeba" || source.sourceId !== String(row.id) ||
        source.snapshot !== pin.snapshot || source.license !== pin.license ||
        source.sourceUrl !== `https://tatoeba.org/en/sentences/show/${row.id}` ||
        !source.attribution?.includes(`current owner ${row.owner};`)) throw new Error(`${record.id}: source/attribution drift`);
    if (record.text !== row.text && (source.modified !== true || !record.provenance.note?.includes("Editorial edit:"))) {
      throw new Error(`${record.id}: undocumented editorial source-text change`);
    }
    if (record.text === row.text && source.modified !== false) throw new Error(`${record.id}: incorrect modification marker`);
  }
}
