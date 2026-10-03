import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { normalizeEnglishKey, stableJson } from "./english-content-core.mjs";
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const file=path.join(root,"content","english","id-registry.json");
const type=process.argv[2],rawKey=process.argv.slice(3).join(" ");
if (!type||!rawKey) { console.error("Usage: node scripts/allocate-english-content-id.mjs <type> <stable-key>"); process.exit(2); }
const prefixes={lex:"lex.en",sense:"sense",morph:"morph",usage:"usage",col:"col",pat:"pat",pv:"pv",idiom:"idiom",chunk:"chunk",sent:"sent",trans:"trans",dlg:"dlg","ex-cloze":"ex.cloze","ex-correction":"ex.correction","ex-building":"ex.building","ex-translation":"ex.translation","ex-transformation":"ex.transformation","ex-listening":"ex.listening","ex-context":"ex.context","ex-collocation":"ex.collocation","ex-grammar-typing":"ex.grammar-typing",err:"err"};
if (!prefixes[type]) throw new Error("Unsupported content id type: "+type);
const registry=JSON.parse(await fs.readFile(file,"utf8")); const key=type+":"+normalizeEnglishKey(rawKey);
if (registry.entries[key]) { console.log(registry.entries[key]); process.exit(0); }
const next=(registry.sequences[type]??0)+1; registry.sequences[type]=next;
const id=prefixes[type]+"."+String(next).padStart(8,"0"); registry.entries[key]=id;
await fs.writeFile(file,stableJson(registry),"utf8"); console.log(id);
