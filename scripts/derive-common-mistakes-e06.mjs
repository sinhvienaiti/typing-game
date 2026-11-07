import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { readJson, stableJson } from "./english-content-core.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const [correctionsDoc,topicsDoc]=await Promise.all([
  readJson(path.join(root,"content","english","review-queues","grammar-e06-corrections.json")),
  readJson(path.join(root,"content","english","grammar","pilot-topics.json")),
]);
const topics=new Map((topicsDoc.records??[]).map(topic=>[topic.id,topic]));
const corrections=correctionsDoc.records??[];
if (corrections.length!==100) throw new Error("Expected 100 E06 corrections before deriving common mistakes");

const records=corrections.map((exercise,index)=>{
  const grammarId=exercise.targetIds?.find(id=>typeof id==="string"&&id.startsWith("gr."));
  if (!grammarId) throw new Error(exercise.id+": correction has no gr.* target");
  const topic=topics.get(grammarId);
  if (!topic) throw new Error(exercise.id+": unknown grammar topic "+grammarId);
  const answer=exercise.acceptedAnswers?.[0];
  if (typeof answer!=="string"||answer.trim()==="") throw new Error(exercise.id+": missing correction answer");
  const conceptVi=typeof topic.concept?.vi==="string"&&topic.concept.vi.trim()!==""
    ?topic.concept.vi.trim()
    :"Hãy đối chiếu cấu trúc mục tiêu và câu chuẩn để nhận ra lỗi.";
  return {
    schemaVersion:1,
    id:"err.e06."+String(index+1).padStart(3,"0"),
    incorrect:exercise.prompt,
    corrections:[answer],
    explanationVi:"Lỗi này thuộc chủ điểm \""+topic.title+"\". "+conceptVi+" So sánh câu sai với câu sửa và chú ý đúng cấu trúc mục tiêu.",
    targetIds:[grammarId],
    evidenceType:"pedagogical",
    quality:{
      state:"candidate",
      checks:{
        schema:{status:"pass",method:"e06-common-mistake-derivation-v1"},
        sourceLink:{status:"pass",method:"correction-exercise-link-v1"},
        exactDuplicate:{status:"pass",method:"normalized-incorrect-v1"},
        grammar:{status:"pending",method:"independent-review-required"},
        translation:{status:"pending",method:"bilingual-review-required"},
        naturalness:{status:"pending",method:"editor-review-required"},
      },
    },
    provenance:{
      sources:[{
        dataset:"project-original",
        sourceId:exercise.id,
        sourceUrl:"content/english/review-queues/grammar-e06-corrections.json",
        snapshot:"2026-10",
        license:"LicenseRef-Project-Original",
        modified:true,
      }],
      note:"Derived from the controlled E06 correction pilot. Explanation remains candidate until grammar and bilingual review.",
    },
  };
});

await fs.writeFile(
  path.join(root,"content","english","review-queues","grammar-e06-common-mistakes.json"),
  stableJson({schemaVersion:1,records}),
  "utf8",
);
console.log("E06 common mistakes:",records.length);
