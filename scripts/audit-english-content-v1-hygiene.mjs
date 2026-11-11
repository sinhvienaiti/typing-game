import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { readJson, stableJson } from "./english-content-core.mjs";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");

async function loadDataset(ds) {
  const manifest = await readJson(path.join(root, "shared", ds, "manifest.json"));
  const out = [];
  for (const s of manifest.shards) {
    const doc = await readJson(path.join(root, "shared", ds, s.path));
    for (const r of doc.records) out.push({ shardId: s.id, record: r });
  }
  return out;
}

async function main() {
  console.log("=== Phase 0 V1 Content Hygiene & Attribution Audit ===");
  const sentences = await loadDataset("sentences");

  let totalExamples = 0, exWithCefr = 0, exWithGram = 0, exWithLex = 0, exWithCtx = 0;
  let totalCloze = 0, clozeE11 = 0, clozeMultiAns = 0, clozeE11ProperNounSuspect = 0;
  let totalTrans = 0, transE11 = 0, transMultiAns = 0, transE11NonMatchingTopicSuspect = 0;
  let totalTransl = 0, translMultiAns = 0, translSameSourceSentence = 0;
  let totalOtherEx = 0;
  let totalMistakes = 0, mistakeReadAmbiguity = 0;

  const translationSourceMap = new Map();
  const sampleRotationalCloze = [];
  const sampleReadAmbiguityMistakes = [];
  const sampleValidCuratedGrammarExercises = [];
  const emptyActivityTypes = new Set([
    "sentence-building", "contextual-usage", "listening-typing", "collocation", "grammar-typing"
  ]);

  for (const { shardId, record } of sentences) {
    if (shardId.startsWith("examples-")) {
      totalExamples++;
      if (record.cefr) exWithCefr++;
      if (Array.isArray(record.grammarIds) && record.grammarIds.length > 0) exWithGram++;
      if (Array.isArray(record.lexicalIds) && record.lexicalIds.length > 0) exWithLex++;
      if (Array.isArray(record.contexts) && record.contexts.length > 0) exWithCtx++;
    } else if (shardId.startsWith("exercises-")) {
      emptyActivityTypes.delete(record.type);
      const ansCount = Array.isArray(record.acceptedAnswers) ? record.acceptedAnswers.length : 0;
      if (record.type === "cloze") {
        totalCloze++;
        if (ansCount > 1) clozeMultiAns++;
        if (String(record.id).startsWith("ex.cloze.e11.")) {
          clozeE11++;
          const ans0 = String(record.acceptedAnswers?.[0] ?? "");
          if (/^[A-Z][a-z]+$/.test(ans0) && !String(record.prompt || "").startsWith("___")) {
            clozeE11ProperNounSuspect++;
            if (sampleRotationalCloze.length < 15) {
              sampleRotationalCloze.push({
                id: record.id,
                prompt: record.prompt,
                acceptedAnswers: record.acceptedAnswers,
                assignedTargetIds: record.targetIds,
              });
            }
          }
        } else if (sampleValidCuratedGrammarExercises.length < 10) {
          sampleValidCuratedGrammarExercises.push({
            id: record.id,
            type: record.type,
            prompt: record.prompt,
            acceptedAnswers: record.acceptedAnswers,
            targetIds: record.targetIds,
          });
        }
      } else if (record.type === "transformation") {
        totalTrans++;
        if (ansCount > 1) transMultiAns++;
        if (String(record.id).startsWith("ex.transformation.e11.")) {
          transE11++;
          // Check mismatch example: present modal/past simple target mismatch
          const prompt = String(record.prompt || "");
          const tId = String(record.targetIds?.[0] ?? "");
          if (tId.includes("past-simple") && /\bcan\b|\bwill\b|\bis\b|\bare\b/i.test(prompt) && !/\bwas\b|\bwere\b|\bdid\b|\byesterday\b|\bago\b/i.test(prompt)) {
            transE11NonMatchingTopicSuspect++;
          }
        }
      } else if (record.type === "translation") {
        totalTransl++;
        if (ansCount > 1) translMultiAns++;
        for (const sId of record.sourceSentenceIds ?? []) {
          translationSourceMap.set(sId, (translationSourceMap.get(sId) ?? 0) + 1);
        }
      } else {
        totalOtherEx++;
      }
    } else if (shardId.startsWith("mistakes-")) {
      totalMistakes++;
      const inc = String(record.incorrect || "");
      const corr0 = String(record.corrections?.[0] || "");
      // Detect "She/He/It read ..." where past tense "read" equals base spelling
      if (/\b(?:He|She|It)\s+read\b/.test(inc) && /\b(?:He|She|It)\s+reads\b/.test(corr0)) {
        mistakeReadAmbiguity++;
        if (sampleReadAmbiguityMistakes.length < 15) {
          sampleReadAmbiguityMistakes.push({
            id: record.id,
            incorrect: inc,
            corrections: record.corrections,
            note: "Grammatically valid Past Simple homograph ('read' /rɛd/) marked as 3sg Present Simple error.",
          });
        }
      }
    }
  }

  for (const [, count] of translationSourceMap) {
    if (count > 1) translSameSourceSentence += count;
  }

  const report = {
    schemaVersion: 1,
    phase: "Phase 0 V1 Hygiene & Attribution Audit",
    generatedAt: new Date().toISOString(),
    examplesMetadataCoverage: {
      totalExamples,
      withCefr: exWithCefr,
      withGrammarIds: exWithGram,
      withGrammarIdsPct: Number(((exWithGram / Math.max(1, totalExamples)) * 100).toFixed(2)),
      withLexicalIds: exWithLex,
      withLexicalIdsPct: Number(((exWithLex / Math.max(1, totalExamples)) * 100).toFixed(2)),
      withContexts: exWithCtx,
    },
    exercisesAudit: {
      cloze: {
        total: totalCloze,
        e11RotationalTargetSlice: clozeE11,
        curatedTargetSlice: totalCloze - clozeE11,
        multiAnswerCount: clozeMultiAns,
        properNounMidSentenceBlankSuspects: clozeE11ProperNounSuspect,
      },
      transformation: {
        total: totalTrans,
        e11RotationalTargetSlice: transE11,
        curatedTargetSlice: totalTrans - transE11,
        multiAnswerCount: transMultiAns,
        heuristicTopicMismatchCount: transE11NonMatchingTopicSuspect,
      },
      translation: {
        total: totalTransl,
        multiAnswerCount: translMultiAns,
        singleAnswerOnlyPct: Number((((totalTransl - translMultiAns) / Math.max(1, totalTransl)) * 100).toFixed(2)),
        recordsSharingSourceSentenceId: translSameSourceSentence,
      },
      otherExercisesCount: totalOtherEx,
      totalMultiAnswerExercisesTruncatedByV1Adapter: clozeMultiAns + transMultiAns + translMultiAns,
      exerciseTypesWithZeroPublishedRecordsInExercisesShards: [...emptyActivityTypes],
    },
    mistakesAudit: {
      totalMistakes,
      pastTenseHomographReadAmbiguityCount: mistakeReadAmbiguity,
    },
    samples: {
      rotationalClozeProperNounSuspects: sampleRotationalCloze,
      curatedGrammarClozeSamples: sampleValidCuratedGrammarExercises,
      readHomographAmbiguousMistakes: sampleReadAmbiguityMistakes,
    },
  };

  const outPath = path.join(root, "content", "english", "reports", "v2-phase0-v1-hygiene-audit.json");
  await fs.writeFile(outPath, stableJson(report), "utf8");
  console.log(JSON.stringify({
    examplesMetadataCoverage: report.examplesMetadataCoverage,
    exercisesAudit: report.exercisesAudit,
    mistakesAudit: report.mistakesAudit,
  }, null, 2));
  console.log("Report written to:", outPath);
}

main().catch((err) => {
  console.error(err);
  process.exitCode = 1;
});
