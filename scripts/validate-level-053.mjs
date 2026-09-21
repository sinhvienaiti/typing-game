import path from "node:path";
import { fileURLToPath } from "node:url";
import { readTypingLevels, validateTypingLevels } from "./typing-text-core.mjs";
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),".."),typingTextDir=path.join(root,"shared","typing-texts"),vocabularyDir=path.join(root,"shared","vocabulary");
const result=await validateTypingLevels(await readTypingLevels(typingTextDir),vocabularyDir),errors=result.errors.filter(m=>m.startsWith("053.json")),warnings=result.warnings.filter(m=>m.startsWith("053.json")),report=result.levelReports.find(x=>x.level===53);
if(errors.length){console.error(errors.join("\n"));process.exit(1);}if(warnings.length){console.error(warnings.map(m=>`WARN: ${m}`).join("\n"));process.exit(1);}if(!report||report.passageCount<15){console.error("053.json did not produce a complete level report");process.exit(1);}console.log(`Level 053 PASS: ${report.passageCount} passages, ${report.wordCount} words, ${(report.coverage*100).toFixed(1)} percent vocabulary coverage, 0 duplicate/similarity warnings.`);
