import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const file=path.join(root,"docs","ENGLISH_LEARNING_CONTENT_SYSTEM_MASTER_PLAN.md");
let text=await fs.readFile(file,"utf8");

function sync(oldValue,newValue,label){
  if(text.includes(oldValue)){
    text=text.replace(oldValue,newValue);
    console.log("updated:",label);
    return;
  }
  if(text.includes(newValue)){
    console.log("already current:",label);
    return;
  }
  throw new Error(label+": neither the previous nor current status snapshot was found; update the status-sync contract before changing runtime counts");
}

sync(
  "Current published runtime: `shared/dictionary` contains **300 lexemes + 300 senses (600)**; `shared/grammar` contains **161 topics**; `shared/sentences` contains **2,554 records** = **1,083 examples + 1,122 exercises + 100 dialogues + 249 reviewed common mistakes**; and `shared/phrases` contains **1,630 phrase/pattern records** (560 collocations + 510 verb patterns + 280 phrasal verbs + 155 chunks + 125 idioms). Candidate/draft records remain excluded from runtime.",
  "Current published runtime: `shared/dictionary` contains **300 lexemes + 300 senses + 300 usage sidecars (900)**; `shared/grammar` contains **300 reviewed topics**; `shared/sentences` contains **3,401 records** = **1,513 examples + 1,400 exercises + 100 dialogues + 388 reviewed common mistakes**; and `shared/phrases` contains **1,710 phrase/pattern records** (600 collocations + 510 verb patterns + 300 phrasal verbs + 165 chunks + 135 idioms). Candidate/draft records remain excluded from runtime. The E03 usage sidecar reuses already-reviewed primary-sense explanation/register/example evidence and adds no new prose.",
  "published runtime snapshot",
);

sync(
  "- The full 300-topic framework remains the curriculum/taxonomy; **161/300 topics now have reviewed rich runtime bodies**, including **45/45 A1**, **50/50 A2** and **60/60 B1**. Further expansion proceeds from B2 upward as controlled CEFR slices rather than generating the remaining topics in bulk.",
  "- The full 300-topic framework is now also the reviewed rich runtime body set: **300/300 topics published**, distributed as **45 A1 + 50 A2 + 60 B1 + 60 B2 + 50 C1 + 35 C2**. Further grammar work is quality maintenance and exercise/content enrichment rather than filling missing framework topics.",
  "E05 published-topic snapshot",
);

sync(
  "Current readiness measurements after E04 scale batch 23:",
  "Current readiness measurements after E04 focused scale batch 24 plus the reviewed E03 usage sidecar:",
  "E11 readiness snapshot heading",
);

sync(
  "- grammar topics: **300/300 framework entries**, with **161/300 reviewed rich topic bodies** currently published, including **45/45 A1**, **50/50 A2** and **60/60 B1**;",
  "- grammar topics: **300/300 framework entries and 300/300 reviewed rich topic bodies published**, distributed as **45 A1 + 50 A2 + 60 B1 + 60 B2 + 50 C1 + 35 C2**;",
  "E11 grammar readiness",
);
sync("- collocations: 560 / 5,000 minimum;","- collocations: 600 / 5,000 long-term target;","E11 collocation readiness");
sync("- phrasal verbs: 280 / 1,000 minimum;","- phrasal verbs: 300 / 1,000 long-term target;","E11 phrasal readiness");
sync("- idioms/chunks: 280 / 2,000 minimum;","- idioms/chunks: 300 / 2,000 long-term target (165 chunks + 135 idioms);","E11 idiom/chunk readiness");
sync(
  "- common mistakes: **249 / 2,000 minimum in published runtime** = the closed 100-record E06 pilot plus 149 reviewed A1-B1 grammar-scale mistakes;",
  "- common mistakes: **388 / 2,000 long-term target in published runtime** = the closed 100-record E06 pilot plus 288 reviewed grammar-linked mistakes;",
  "E11 common-mistake readiness",
);
sync(
  "- example sentences: candidate/source pipeline remains far below 100,000; current published runtime contains **1,083 examples** (483 E05 grammar-linked + 300 typing-text + 300 Tatoeba);",
  "- example sentences: the long-term corpus target remains far above the controlled pilot; current published runtime contains **1,513 examples** (900 grammar-linked + 13 E03 sense-support examples + 300 typing-text + 300 Tatoeba);",
  "E11 example readiness",
);

await fs.writeFile(file,text,"utf8");
console.log("English-content master-plan status snapshots are synchronized.");
