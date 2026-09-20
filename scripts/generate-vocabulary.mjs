import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { buildArtifacts, readLevels, stableJson, validateLevels } from "./vocabulary-core.mjs";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const vocabularyDir = path.join(root, "shared", "vocabulary");
const documents = await readLevels(vocabularyDir);
const { errors } = validateLevels(documents);

if (errors.length > 0) {
  console.error(errors.join("\n"));
  process.exit(1);
}

const artifacts = buildArtifacts(documents);
await fs.writeFile(path.join(vocabularyDir, "index.json"), stableJson(artifacts.index));
await fs.writeFile(path.join(vocabularyDir, "lookup.json"), stableJson(artifacts.lookup));
console.log(`Generated vocabulary index/lookup for ${artifacts.index.totalEntries} entries across ${artifacts.index.availableLevels} levels.`);
