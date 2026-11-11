import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { createSchemaValidator, listJsonFiles, readJson } from "./english-content-core.mjs";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");

async function collectKnownRecords() {
  const known = new Map();
  for (const ds of ["dictionary", "grammar", "sentences", "phrases"]) {
    const manifest = await readJson(path.join(root, "shared", ds, "manifest.json"));
    for (const shard of manifest.shards ?? []) {
      const doc = await readJson(path.join(root, "shared", ds, shard.path));
      for (const rec of doc.records ?? []) {
        const id = rec?.id ?? rec?.lexemeId;
        if (typeof id === "string" && id !== "") known.set(id, rec);
      }
    }
  }
  const sentDir = path.join(root, "content", "english", "sentences");
  for (const file of await listJsonFiles(sentDir)) {
    if (!path.basename(file).startsWith("v2-")) continue;
    const raw = await readJson(file);
    const items = Array.isArray(raw) ? raw : (raw.items ?? raw.records ?? []);
    for (const rec of items) {
      if (typeof rec?.id === "string" && rec.id !== "") known.set(rec.id, rec);
    }
  }
  return known;
}

async function main() {
  const schemaDir = path.join(root, "shared", "schemas", "english-content");
  const schemaFiles = (await fs.readdir(schemaDir)).filter((n) => n.endsWith(".schema.json")).sort();
  const schemas = await Promise.all(schemaFiles.map((n) => readJson(path.join(schemaDir, n))));
  const topicPackSchema = schemas.find((s) => s.$id?.endsWith("/topic-pack.schema.json"));
  if (!topicPackSchema) throw new Error("Missing topic-pack.schema.json");
  const { validate } = createSchemaValidator(schemas);

  const knownRecords = await collectKnownRecords();
  const packsDir = path.join(root, "content", "english", "packs");
  const packFiles = await listJsonFiles(packsDir);

  let totalItems = 0;
  for (const file of packFiles) {
    const pack = await readJson(file);
    const problems = validate(pack, topicPackSchema);
    if (problems.length > 0) {
      throw new Error(`${path.basename(file)} failed topic-pack schema validation: ${problems.join("; ")}`);
    }
    const seen = new Set();
    for (const it of pack.items) {
      if (seen.has(it.contentId)) {
        throw new Error(`${pack.id} contains duplicate item ${it.contentId}`);
      }
      seen.add(it.contentId);
      const rec = knownRecords.get(it.contentId);
      if (!rec) {
        throw new Error(`${pack.id} references unknown contentId: ${it.contentId}`);
      }
      if (it.activity === "translation") {
        const prompt = String(rec.prompt ?? "");
        const ans = String(rec.acceptedAnswers?.[0] ?? "");
        if (ans && prompt.includes(ans)) {
          throw new Error(`${pack.id} references untranslated prompt in ${it.contentId}`);
        }
      }
    }
    totalItems += pack.items.length;
    console.log(`Verified hand-curated ${path.relative(root, file)} (${pack.items.length} items)`);
  }
  console.log(`E15 Topic Packs verified: ${packFiles.length} packs, ${totalItems} hand-curated items.`);
}

main().catch((err) => {
  console.error(err);
  process.exitCode = 1;
});
