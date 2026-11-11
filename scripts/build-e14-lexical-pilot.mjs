import path from "node:path";
import { fileURLToPath } from "node:url";
import { readJson } from "./english-content-core.mjs";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");

async function loadPublishedSentenceIds() {
  const manifest = await readJson(path.join(root, "shared", "sentences", "manifest.json"));
  const published = new Set();
  for (const shard of manifest.shards ?? []) {
    const doc = await readJson(path.join(root, "shared", "sentences", shard.path));
    for (const rec of doc.records ?? []) {
      if (rec?.id && rec?.quality?.state === "published") {
        published.add(rec.id);
      }
    }
  }
  return published;
}

async function main() {
  const pilotPath = path.join(root, "content", "english", "dictionary", "e14-sense-pilot.json");
  const reportPath = path.join(root, "content", "english", "reports", "e14-lexical-pilot-report.json");
  const [pilot, report, publishedSents] = await Promise.all([
    readJson(pilotPath),
    readJson(reportPath),
    loadPublishedSentenceIds(),
  ]);

  const entries = pilot.entries ?? [];
  if (entries.length !== 750) {
    throw new Error(`Expected 750 E14 entries, got ${entries.length}`);
  }

  const seenLexIds = new Set();
  const seenHeadwordKeys = new Set();
  const seenSenseIds = new Set();
  let polysemousLexemes = 0;
  let totalSenses = 0;
  let verifiedExampleLinks = 0;

  for (let i = 0; i < entries.length; i++) {
    const entry = entries[i];
    const seq = String(i + 1).padStart(4, "0");
    const expectedLexId = `lex.e14.${seq}`;
    if (entry.id !== expectedLexId) {
      throw new Error(`E14 entry index ${i} expected id ${expectedLexId}, got ${entry.id}`);
    }
    if (seenLexIds.has(entry.id)) {
      throw new Error(`Duplicate E14 lexeme id: ${entry.id}`);
    }
    seenLexIds.add(entry.id);

    const hwKey = String(entry.headwordKey ?? "").trim().toLowerCase();
    if (!hwKey || hwKey !== String(entry.headword ?? "").trim().toLowerCase()) {
      throw new Error(`E14 ${entry.id} has mismatched headwordKey/headword`);
    }
    if (seenHeadwordKeys.has(hwKey)) {
      throw new Error(`Duplicate E14 headwordKey: ${hwKey} (${entry.id})`);
    }
    seenHeadwordKeys.add(hwKey);

    const senses = entry.senses ?? [];
    if (senses.length === 0) {
      throw new Error(`E14 ${entry.id} has no senses`);
    }
    if (Boolean(entry.polysemous) !== (senses.length > 1)) {
      throw new Error(`E14 ${entry.id} polysemous flag disagrees with sense count (${senses.length})`);
    }
    if (entry.polysemous) polysemousLexemes++;

    const lexemeExamples = new Set();
    for (let si = 0; si < senses.length; si++) {
      const sense = senses[si];
      totalSenses++;
      const expectedSenseId = `sense.e14.${seq}.${String(si + 1).padStart(2, "0")}`;
      if (sense.id !== expectedSenseId) {
        throw new Error(`E14 sense id expected ${expectedSenseId}, got ${sense.id}`);
      }
      if (seenSenseIds.has(sense.id)) {
        throw new Error(`Duplicate E14 sense id: ${sense.id}`);
      }
      seenSenseIds.add(sense.id);
      if (sense.lexemeId !== entry.id) {
        throw new Error(`E14 ${sense.id} has wrong lexemeId ${sense.lexemeId}`);
      }
      if (!sense.partOfSpeech || sense.partOfSpeech === "core" || sense.partOfSpeech === "variant") {
        throw new Error(`E14 ${sense.id} has generic/empty partOfSpeech: ${sense.partOfSpeech}`);
      }
      if (!sense.definitionEn || /Primary meaning|Distinct sense/i.test(sense.definitionEn)) {
        throw new Error(`E14 ${sense.id} has template/missing definitionEn: ${sense.definitionEn}`);
      }
      if (!sense.explanationVi) {
        throw new Error(`E14 ${sense.id} is missing explanationVi`);
      }
      const exIds = sense.exampleIds ?? [];
      if (exIds.length === 0) {
        throw new Error(`E14 ${sense.id} has no exampleIds`);
      }
      const senseExamples = new Set();
      for (const exId of exIds) {
        verifiedExampleLinks++;
        if (senseExamples.has(exId)) {
          throw new Error(`Duplicate exampleId ${exId} inside ${sense.id}`);
        }
        senseExamples.add(exId);
        if (lexemeExamples.has(exId)) {
          throw new Error(`ExampleId ${exId} duplicated across senses of ${entry.id}`);
        }
        lexemeExamples.add(exId);
        if (!publishedSents.has(exId)) {
          throw new Error(`E14 ${sense.id} references unpublished or unknown exampleId: ${exId}`);
        }
      }
    }
  }

  const computed = {
    lexemes: entries.length,
    polysemousLexemes,
    senses: totalSenses,
    verifiedExampleLinks,
  };
  for (const [k, v] of Object.entries(computed)) {
    if (pilot.totals?.[k] !== v) {
      throw new Error(`e14-sense-pilot totals.${k} is ${pilot.totals?.[k]}, expected ${v}`);
    }
    if (report.totals?.[k] !== v) {
      throw new Error(`e14-lexical-pilot-report totals.${k} is ${report.totals?.[k]}, expected ${v}`);
    }
  }

  console.log("E14 Lexical Pilot verified (hand-curated):", computed);
}

main().catch((err) => {
  console.error(err);
  process.exitCode = 1;
});
