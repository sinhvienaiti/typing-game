import path from "node:path";
import { fileURLToPath } from "node:url";
import { readJson } from "./english-content-core.mjs";
import { applyEnglishExampleLinks, readEnglishExampleLinkLedger } from "./english-example-link-core.mjs";

/**
 * Non-destructive validator for E13 morphological/example enrichment links and report.
 * content/english/reviews/enrichment-links.d/e13-morphological-links.json and
 * content/english/reports/e13-enrichment-recovery-report.json are hand-curated
 * and must never be overwritten by a script.
 */
const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const LEDGER_PATH = "content/english/reviews/enrichment-links.d/e13-morphological-links.json";
const REPORT_PATH = "content/english/reports/e13-enrichment-recovery-report.json";

async function loadSharedShards(baseDir, prefix) {
  const manifest = await readJson(path.join(ROOT, baseDir, "manifest.json"));
  const matching = (manifest.shards ?? []).filter((shard) => shard.path.startsWith(prefix));
  const records = [];
  for (const shard of matching) {
    const data = await readJson(path.join(ROOT, baseDir, shard.path));
    if (Array.isArray(data.records)) records.push(...data.records);
  }
  return records;
}

async function main() {
  const e13File = await readJson(path.join(ROOT, LEDGER_PATH));
  const report = await readJson(path.join(ROOT, REPORT_PATH));
  const allLedgerLinks = await readEnglishExampleLinkLedger(ROOT);

  const e13LinksFromAll = allLedgerLinks.filter((link) => link.sourceFile === LEDGER_PATH || link.sourceFile?.endsWith("e13-morphological-links.json"));
  const links = e13File.links ?? [];

  const errors = [];
  if (e13File.schemaVersion !== 1) {
    errors.push(`${LEDGER_PATH}: schemaVersion must be 1`);
  }
  if (e13LinksFromAll.length !== links.length) {
    errors.push(`Ledger loader returned ${e13LinksFromAll.length} E13 links, expected ${links.length}`);
  }

  const collocations = await loadSharedShards("shared/phrases", "collocations/");
  const phrases = await loadSharedShards("shared/phrases", "items/");
  const examples = await loadSharedShards("shared/sentences", "examples/");

  const collocationLinks = links.filter((link) => link.targetType === "collocation");
  const phraseLinks = links.filter((link) => link.targetType === "phrase");
  const otherLinks = links.filter((link) => link.targetType !== "collocation" && link.targetType !== "phrase");
  if (otherLinks.length > 0) {
    errors.push(`${LEDGER_PATH}: found ${otherLinks.length} links with unexpected targetType`);
  }

  const colResult = applyEnglishExampleLinks(
    collocations.map((record) => ({ ...record, exampleIds: [] })),
    collocationLinks,
    { targetType: "collocation", examples }
  );
  const phrResult = applyEnglishExampleLinks(
    phrases.map((record) => ({ ...record, exampleIds: [] })),
    phraseLinks,
    { targetType: "phrase", examples }
  );

  if (colResult.applied !== collocationLinks.length) {
    errors.push(`Collocation links applied ${colResult.applied}, expected ${collocationLinks.length}`);
  }
  if (phrResult.applied !== phraseLinks.length) {
    errors.push(`Phrase links applied ${phrResult.applied}, expected ${phraseLinks.length}`);
  }

  const collocationMap = new Map(collocations.map((record) => [record.id, record]));
  const phraseMap = new Map(phrases.map((record) => [record.id, record]));
  for (const link of collocationLinks) {
    const target = collocationMap.get(link.targetId);
    if (!target?.exampleIds?.includes(link.exampleId)) {
      errors.push(`Published collocation ${link.targetId} missing exampleId ${link.exampleId}`);
    }
  }
  for (const link of phraseLinks) {
    const target = phraseMap.get(link.targetId);
    if (!target?.exampleIds?.includes(link.exampleId)) {
      errors.push(`Published phrase ${link.targetId} missing exampleId ${link.exampleId}`);
    }
  }

  const colTargets = new Set(collocationLinks.map((link) => link.targetId)).size;
  const phrTargets = new Set(phraseLinks.map((link) => link.targetId)).size;

  if (report.totalLinksAdded !== links.length) {
    errors.push(`${REPORT_PATH}: totalLinksAdded (${report.totalLinksAdded}) !== ${links.length}`);
  }
  const stats = report.stats ?? {};
  if (stats.collocationTargets !== colTargets) {
    errors.push(`${REPORT_PATH}: stats.collocationTargets (${stats.collocationTargets}) !== ${colTargets}`);
  }
  if (stats.collocationLinks !== collocationLinks.length) {
    errors.push(`${REPORT_PATH}: stats.collocationLinks (${stats.collocationLinks}) !== ${collocationLinks.length}`);
  }
  if (stats.phraseTargets !== phrTargets) {
    errors.push(`${REPORT_PATH}: stats.phraseTargets (${stats.phraseTargets}) !== ${phrTargets}`);
  }
  if (stats.phraseLinks !== phraseLinks.length) {
    errors.push(`${REPORT_PATH}: stats.phraseLinks (${stats.phraseLinks}) !== ${phraseLinks.length}`);
  }

  const linkByPair = new Map(links.map((link) => [`${link.targetId}\u0000${link.exampleId}`, link]));
  for (const sample of report.sampleLinks ?? []) {
    const actual = linkByPair.get(`${sample.targetId}\u0000${sample.exampleId}`);
    if (!actual) {
      errors.push(`${REPORT_PATH}: sampleLink ${sample.targetId}/${sample.exampleId} is no longer in ${LEDGER_PATH}`);
    } else if (actual.targetSnapshot?.text !== sample.target || actual.exampleText !== sample.exampleText) {
      errors.push(`${REPORT_PATH}: sampleLink ${sample.targetId}/${sample.exampleId} mismatches ${LEDGER_PATH}`);
    }
  }

  if (errors.length > 0) {
    console.error(`E13 enrichment links validation FAILED (${errors.length} issue(s)):`);
    for (const err of errors.slice(0, 25)) console.error(` - ${err}`);
    process.exit(1);
  }

  console.log(
    JSON.stringify(
      {
        status: "validated-only",
        totalLinks: links.length,
        collocationTargets: colTargets,
        collocationLinks: collocationLinks.length,
        phraseTargets: phrTargets,
        phraseLinks: phraseLinks.length,
      },
      null,
      2
    )
  );
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
