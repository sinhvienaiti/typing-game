import fs from "node:fs/promises";
import path from "node:path";
import { readJson } from "./english-content-core.mjs";

export const E11_TYPING_TEXT_BATCH_ID="e06.typing-text-reviewed-slice";
export const E11_TYPING_TEXT_RECORD_SET_ID="reviewed-typing-text-sentences";
const SHARD_RE=/^e11-reviewed-typing-text-sentences-slice-[0-9]+-[0-9]+\.json$/u;

export function isE11TypingTextRecordSet(batch,set) {
  return batch?.id===E11_TYPING_TEXT_BATCH_ID&&set?.id===E11_TYPING_TEXT_RECORD_SET_ID;
}

export async function readE11TypingTextReviewShards(root) {
  const dir=path.join(root,"content","english","sentences");
  let names=[];
  try {
    names=(await fs.readdir(dir))
      .filter(name=>SHARD_RE.test(name))
      .sort((a,b)=>a.localeCompare(b,"en"));
  } catch (error) {
    if (error?.code!=="ENOENT") throw error;
  }
  const result=[];
  for (const name of names) {
    const relativePath=path.posix.join("content","english","sentences",name);
    const doc=await readJson(path.join(root,relativePath));
    if (doc.schemaVersion!==1||!Array.isArray(doc.records)) {
      throw new TypeError(relativePath+" must contain schemaVersion=1 and records[]");
    }
    result.push({relativePath,records:doc.records});
  }
  return result;
}
