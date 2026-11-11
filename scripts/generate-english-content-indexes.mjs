import path from "node:path";
import { fileURLToPath } from "node:url";
import { generateEnglishContentIndexes } from "./english-indexes-core.mjs";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const manifest = await generateEnglishContentIndexes(root);
console.log("Generated English content indexes:", JSON.stringify(manifest.totals));
