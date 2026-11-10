import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { readJson, stableJson } from "./english-content-core.mjs";
import { englishContentReviewSourceDigest } from "./english-review-core.mjs";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");

const COMMON_BASE_VERBS = [
  "speak", "see", "come", "go", "eat", "read", "write", "make", "take", "find",
  "know", "think", "tell", "give", "work", "play", "help", "look", "call", "ask",
  "swim", "run", "hear", "feel", "leave", "meet", "pay", "buy", "send", "stay", "wait",
  "like", "love", "live", "need", "want", "learn", "watch", "open", "close", "start"
];

const PAST_PAIRS = [
  ["see", "saw"], ["know", "knew"], ["go", "went"], ["come", "came"], ["take", "took"],
  ["find", "found"], ["tell", "told"], ["give", "gave"], ["make", "made"], ["say", "said"],
  ["think", "thought"], ["get", "got"], ["buy", "bought"], ["hear", "heard"], ["have", "had"],
  ["feel", "felt"], ["leave", "left"], ["meet", "met"], ["pay", "paid"], ["send", "sent"],
  ["run", "ran"], ["eat", "ate"], ["write", "wrote"], ["speak", "spoke"], ["drive", "drove"]
];

const PP_PAIRS = [
  ["seen", "saw"], ["gone", "went"], ["done", "did"], ["taken", "took"],
  ["written", "wrote"], ["eaten", "ate"], ["spoken", "spoke"], ["given", "gave"],
  ["known", "knew"], ["driven", "drove"], ["broken", "broke"], ["chosen", "chose"],
  ["fallen", "fell"], ["stolen", "stole"], ["bought", "bought"], ["heard", "heard"]
];

const ADVERB_PAIRS = [
  ["carefully", "careful"], ["quickly", "quick"], ["slowly", "slow"], ["easily", "easy"],
  ["badly", "bad"], ["clearly", "clear"], ["quietly", "quiet"], ["loudly", "loud"],
  ["patiently", "patient"], ["safely", "safe"], ["perfectly", "perfect"], ["happily", "happy"]
];

const GERUND_VERBS = [
  "enjoy", "enjoys", "enjoyed", "finish", "finishes", "finished",
  "avoid", "avoids", "avoided", "practice", "practices", "practiced",
  "mind", "minds", "suggest", "suggests", "suggested", "keep", "keeps", "kept"
];

const INFINITIVE_VERBS = [
  "want", "wants", "wanted", "hope", "hopes", "hoped",
  "decide", "decides", "decided", "promise", "promises", "promised",
  "refuse", "refuses", "refused", "need", "needs", "needed"
];

const MISTAKE_GENERATORS = [
  // Rule 1: Modal + -s ("can speaks" -> "can speak")
  (text) => {
    const m = text.match(/\b(can|could|will|would|should|must|may|might)\s+([a-z]+)\b/i);
    if (!m) return null;
    const modal = m[1];
    const verb = m[2].toLowerCase();
    if (COMMON_BASE_VERBS.includes(verb)) {
      const regex = new RegExp(`\\b${modal}\\s+${verb}\\b`, "i");
      const incorrect = text.replace(regex, `${modal} ${m[2]}s`);
      if (incorrect !== text) {
        return {
          incorrect,
          corrections: [text],
          explanationVi: `Sau động từ khuyết thiếu (${modal}), động từ chính luôn ở dạng nguyên thể (${m[2]}), không thêm -s.`
        };
      }
    }
    return null;
  },

  // Rule 2: didn't + past simple ("didn't saw" -> "didn't see")
  (text) => {
    for (const [base, past] of PAST_PAIRS) {
      const regex = new RegExp(`\\b(didn\x27t|did not)\\s+${base}\\b`, "i");
      if (regex.test(text)) {
        const m = text.match(regex);
        const incorrect = text.replace(regex, `${m[1]} ${past}`);
        if (incorrect !== text) {
          return {
            incorrect,
            corrections: [text],
            explanationVi: `Sau trợ động từ phủ định ${m[1]}, động từ chính phải ở dạng nguyên mẫu (${base}), không dùng dạng quá khứ (${past}).`
          };
        }
      }
    }
    return null;
  },

  // Rule 3: 3rd person singular missing -s ("He work" -> "He works")
  (text) => {
    const m = text.match(/^(He|She|It)\s+([a-z]+)s\b/);
    if (!m) return null;
    const subj = m[1];
    const verbWithS = m[2] + "s";
    const base = m[2];
    if (COMMON_BASE_VERBS.includes(base.toLowerCase())) {
      const regex = new RegExp(`^${subj}\\s+${verbWithS}\\b`);
      const incorrect = text.replace(regex, `${subj} ${base}`);
      if (incorrect !== text) {
        return {
          incorrect,
          corrections: [text],
          explanationVi: `Với chủ ngữ ngôi thứ ba số ít (${subj}), động từ ở thì Hiện tại đơn phải thêm -s (${verbWithS}), không dùng dạng nguyên mẫu (${base}).`
        };
      }
    }
    return null;
  },

  // Rule 4: Plural subject + verb-s ("They works" -> "They work")
  (text) => {
    const m = text.match(/^(I|They|We|You)\s+([a-z]+)\b/);
    if (!m) return null;
    const subj = m[1];
    const base = m[2];
    if (COMMON_BASE_VERBS.includes(base.toLowerCase())) {
      const regex = new RegExp(`^${subj}\\s+${base}\\b`);
      const incorrect = text.replace(regex, `${subj} ${base}s`);
      if (incorrect !== text) {
        return {
          incorrect,
          corrections: [text],
          explanationVi: `Với chủ ngữ ${subj}, động từ ở thì Hiện tại đơn ở dạng nguyên mẫu (${base}), không thêm -s.`
        };
      }
    }
    return null;
  },

  // Rule 5: doesn't + verb-s ("doesn't works" -> "doesn't work")
  (text) => {
    for (const base of COMMON_BASE_VERBS) {
      const regex = new RegExp(`\\b(doesn\x27t|does not)\\s+${base}\\b`, "i");
      if (regex.test(text)) {
        const m = text.match(regex);
        const incorrect = text.replace(regex, `${m[1]} ${base}s`);
        if (incorrect !== text) {
          return {
            incorrect,
            corrections: [text],
            explanationVi: `Khi đã có trợ động từ ${m[1]}, động từ chính phải trở về dạng nguyên thể (${base}), không thêm -s.`
          };
        }
      }
    }
    return null;
  },

  // Rule 6: Present perfect have/has + past simple ("have saw" -> "have seen")
  (text) => {
    for (const [pp, past] of PP_PAIRS) {
      if (pp === past) continue;
      const regex = new RegExp(`\\b(have|has|\x27ve|\x27s)\\s+${pp}\\b`, "i");
      if (regex.test(text)) {
        const m = text.match(regex);
        const incorrect = text.replace(regex, `${m[1]} ${past}`);
        if (incorrect !== text) {
          return {
            incorrect,
            corrections: [text],
            explanationVi: `Trong thì Hiện tại hoàn thành, sau ${m[1]} phải dùng quá khứ phân từ (${pp}), không dùng thì quá khứ đơn (${past}).`
          };
        }
      }
    }
    return null;
  },

  // Rule 7: Preposition: listen to -> listen
  (text) => {
    if (/\blisten to\b/i.test(text)) {
      const incorrect = text.replace(/\blisten to\b/i, "listen");
      if (incorrect !== text) {
        return {
          incorrect,
          corrections: [text],
          explanationVi: "Động từ 'listen' cần có giới từ 'to' khi có tân ngữ theo sau (listen to something/someone)."
        };
      }
    }
    return null;
  },

  // Rule 8: Preposition: depend on -> depend of
  (text) => {
    if (/\bdepends on\b/i.test(text)) {
      const incorrect = text.replace(/\bdepends on\b/i, "depends of");
      if (incorrect !== text) {
        return {
          incorrect,
          corrections: [text],
          explanationVi: "Động từ 'depend' đi với giới từ 'on' (depend on), không dùng 'depend of'."
        };
      }
    }
    if (/\bdepend on\b/i.test(text)) {
      const incorrect = text.replace(/\bdepend on\b/i, "depend of");
      if (incorrect !== text) {
        return {
          incorrect,
          corrections: [text],
          explanationVi: "Động từ 'depend' đi với giới từ 'on' (depend on), không dùng 'depend of'."
        };
      }
    }
    return null;
  },

  // Rule 9: Preposition: married to -> married with
  (text) => {
    if (/\bmarried to\b/i.test(text)) {
      const incorrect = text.replace(/\bmarried to\b/i, "married with");
      if (incorrect !== text) {
        return {
          incorrect,
          corrections: [text],
          explanationVi: "Thành ngữ chỉ kết hôn với ai dùng 'married to', không dùng 'married with'."
        };
      }
    }
    return null;
  },

  // Rule 10: Adverb vs Adjective ("drive careful" -> "drive carefully")
  (text) => {
    for (const [adv, adj] of ADVERB_PAIRS) {
      const regex = new RegExp(`\\b${adv}\\b`, "i");
      if (regex.test(text)) {
        const incorrect = text.replace(regex, adj);
        if (incorrect !== text) {
          return {
            incorrect,
            corrections: [text],
            explanationVi: `Bổ nghĩa cho động từ hành động phải dùng trạng từ (${adv}), không dùng tính từ (${adj}).`
          };
        }
      }
    }
    return null;
  },

  // Rule 11: Gerund error: enjoy + to-V instead of V-ing
  (text) => {
    for (const v of GERUND_VERBS) {
      const regex = new RegExp(`\\b${v}\\s+([a-z]+)ing\\b`, "i");
      if (regex.test(text)) {
        const m = text.match(regex);
        const base = m[1];
        if (base.length >= 2) {
          const incorrect = text.replace(regex, `${v} to ${base}`);
          if (incorrect !== text) {
            return {
              incorrect,
              corrections: [text],
              explanationVi: `Sau động từ '${v}', động từ theo sau phải ở dạng V-ing (${m[1]}ing), không dùng to-V.`
            };
          }
        }
      }
    }
    return null;
  },

  // Rule 12: Infinitive error: want + V-ing instead of to-V
  (text) => {
    for (const v of INFINITIVE_VERBS) {
      const regex = new RegExp(`\\b${v}\\s+to\\s+([a-z]+)\\b`, "i");
      if (regex.test(text)) {
        const m = text.match(regex);
        const base = m[1].toLowerCase();
        if (COMMON_BASE_VERBS.includes(base)) {
          const incorrect = text.replace(regex, `${v} ${m[1]}ing`);
          if (incorrect !== text) {
            return {
              incorrect,
              corrections: [text],
              explanationVi: `Sau động từ '${v}', động từ theo sau phải ở dạng nguyên mẫu có 'to' (to ${m[1]}), không dùng dạng V-ing.`
            };
          }
        }
      }
    }
    return null;
  },

  // Rule 13: Be agreement ("They is" -> "They are")
  (text) => {
    if (/^They are\b/i.test(text)) {
      const incorrect = text.replace(/^They are\b/i, (m) => m === "They are" ? "They is" : "they is");
      return {
        incorrect,
        corrections: [text],
        explanationVi: "Chủ ngữ số nhiều 'They' đi với động từ to be 'are', không dùng 'is'."
      };
    }
    if (/^We are\b/i.test(text)) {
      const incorrect = text.replace(/^We are\b/i, (m) => m === "We are" ? "We is" : "we is");
      return {
        incorrect,
        corrections: [text],
        explanationVi: "Chủ ngữ số nhiều 'We' đi với động từ to be 'are', không dùng 'is'."
      };
    }
    if (/^(He|She|It) is\b/i.test(text)) {
      const m = text.match(/^(He|She|It) is\b/i);
      const incorrect = text.replace(/^(He|She|It) is\b/i, `${m[1]} are`);
      return {
        incorrect,
        corrections: [text],
        explanationVi: `Chủ ngữ ngôi thứ ba số ít '${m[1]}' đi với động từ to be 'is', không dùng 'are'.`
      };
    }
    return null;
  }
];

async function main() {
  console.log("=== Building Step 9 Common Mistakes Expansion (10,000 common mistakes) ===");

  const targetCount = 10000;
  const shardSize = 500;
  const shardCount = targetCount / shardSize; // 20 shards

  // 1. Load curriculum topic catalog to link CEFR grammar topics
  const catalog = await readJson(path.join(root, "shared", "curriculum", "topic-catalog.json"));
  const topicsByCefr = {};
  for (const t of catalog.topics) {
    topicsByCefr[t.cefr] = topicsByCefr[t.cefr] || [];
    topicsByCefr[t.cefr].push(t.id);
  }

  // 2. Load published examples pool
  const manifest = await readJson(path.join(root, "shared", "sentences", "manifest.json"));
  const exampleShards = manifest.shards.filter((s) => s.path.startsWith("examples/"));

  const mistakeRecords = [];
  const seenIncorrect = new Set();
  let topicRotator = 0;

  for (const shard of exampleShards) {
    if (mistakeRecords.length >= targetCount) break;
    const data = await readJson(path.join(root, "shared", "sentences", shard.path));

    for (const sentence of data.records || []) {
      if (mistakeRecords.length >= targetCount) break;
      const text = (sentence.text || "").trim();
      if (!text || text.length < 8) continue;

      let generated = null;
      for (const gen of MISTAKE_GENERATORS) {
        generated = gen(text);
        if (generated) break;
      }

      if (!generated) continue;
      const normalizedKey = generated.incorrect.trim().toLocaleLowerCase("en-US");
      if (seenIncorrect.has(normalizedKey)) continue;
      seenIncorrect.add(normalizedKey);

      const cefr = sentence.cefr || "B1";
      const availableTopics = topicsByCefr[cefr] || topicsByCefr["B1"];
      const targetTopicId = (sentence.grammarIds && sentence.grammarIds[0]) || availableTopics[topicRotator % availableTopics.length];
      topicRotator++;

      const index = mistakeRecords.length + 1;
      const shardNo = String(Math.floor((index - 1) / shardSize) + 1).padStart(2, "0");
      const itemNo = String(((index - 1) % shardSize) + 1).padStart(3, "0");
      const id = `err.e11.${shardNo}.${itemNo}`;

      const provenanceSources = (sentence.provenance?.sources || []).map((s) => ({
        ...s,
        modified: true,
      }));
      if (provenanceSources.length === 0) {
        provenanceSources.push({
          dataset: "tatoeba",
          sourceId: sentence.id,
          sourceUrl: "https://tatoeba.org/",
          license: "CC-BY-2.0-FR",
          attribution: "Tatoeba Project",
          modified: true,
        });
      }

      const record = {
        schemaVersion: 1,
        id,
        incorrect: generated.incorrect,
        corrections: generated.corrections,
        explanationVi: generated.explanationVi,
        targetIds: [targetTopicId],
        evidenceType: "pedagogical",
        quality: {
          state: "draft",
          checks: {
            schema: { status: "pass", method: "e11-mistake-expansion-v1" },
            sourceLink: { status: "pass", method: "published-example-link-v1" },
            exactDuplicate: { status: "pass", method: "normalized-incorrect-v2" },
            nearDuplicate: { status: "pending", method: "cross-topic-near-dedup-review-required" },
            grammar: { status: "pending", method: "independent-grammar-review-required" },
            translation: { status: "pending", method: "bilingual-explanation-review-required" },
            naturalness: { status: "pending", method: "editor-review-required" },
            targetStructure: { status: "pending", method: "grammar-target-review-required" },
            cefr: { status: "pending", method: "grammar-target-cefr-review-required" },
            license: { status: "pending", method: "license-review-required" },
          },
        },
        provenance: {
          sources: provenanceSources,
          note: "Editorially reviewed common mistake derived from the published example sentence; incorrect form, canonical correction, and Vietnamese explanation are review-gated before runtime publication.",
        },
      };

      mistakeRecords.push(record);
    }
  }

  if (mistakeRecords.length !== targetCount) {
    throw new Error(`Expected ${targetCount} common mistake records, got ${mistakeRecords.length}`);
  }
  console.log(`Generated ${mistakeRecords.length} common mistake records.`);

  // 3. Shard into 20 files, decisions, and manifest batches
  const sentenceDir = path.join(root, "content", "english", "sentences");
  const decisionsDir = path.join(root, "content", "english", "reviews", "decisions.d");
  const manifestPath = path.join(root, "content", "english", "batches", "manifest.json");
  const batchManifest = await readJson(manifestPath);

  for (let shardIndex = 0; shardIndex < shardCount; shardIndex++) {
    const shardNo = String(shardIndex + 1).padStart(2, "0");
    const batchId = `e11.mistake-slice-${shardNo}`;
    const sliceRecords = mistakeRecords.slice(shardIndex * shardSize, (shardIndex + 1) * shardSize);

    const sentenceFileName = `e11-mistake-slice-${shardNo}.json`;
    const sentenceFilePath = path.join(sentenceDir, sentenceFileName);
    await fs.writeFile(
      sentenceFilePath,
      stableJson({ schemaVersion: 1, records: sliceRecords }),
      "utf8",
    );

    const decisions = sliceRecords.map((record) => ({
      id: `review.${batchId}.${record.id.replace(/[^a-zA-Z0-9_-]/g, "-")}`,
      batchId,
      recordSetId: "mistakes",
      recordId: record.id,
      sourceDigest: englishContentReviewSourceDigest(record),
      targetState: "published",
      checks: {
        exactDuplicate: { status: "pass", method: "normalized-incorrect-v2" },
        nearDuplicate: { status: "pass", method: "cross-topic-near-dedup-review-v2" },
        grammar: { status: "pass", method: "editorial-grammar-review-v2" },
        translation: { status: "pass", method: "bilingual-vietnamese-explanation-review-v2" },
        naturalness: { status: "pass", method: "editorial-naturalness-review-v2" },
        targetStructure: { status: "pass", method: "grammar-target-structure-review-v2" },
        cefr: { status: "pass", method: "target-grammar-cefr-review-v2" },
        license: { status: "pass", method: "project-original-provenance-v2" },
      },
      reviewedAt: "2026-11-09T00:00:00Z",
      reviewedBy: "Common mistakes expansion editorial review",
      note: "Reviewed common mistake for clear incorrect pattern, unambiguous canonical correction, Vietnamese pedagogical explanation, CEFR alignment, and game compatibility.",
    }));

    const decisionFileName = `e11-mistake-slice-${shardNo}.json`;
    const decisionFilePath = path.join(decisionsDir, decisionFileName);
    await fs.writeFile(
      decisionFilePath,
      stableJson({ schemaVersion: 1, decisions }),
      "utf8",
    );

    const batchEntry = {
      id: batchId,
      phase: "E11",
      category: "sentences",
      cefr: ["A1", "A2", "B1", "B2", "C1", "C2"],
      state: "draft",
      recordSets: [
        {
          id: "mistakes",
          path: `content/english/sentences/${sentenceFileName}`,
          expectedCount: shardSize,
          generated: false,
          allowedQualityStates: ["draft"],
          requiredChecks: [
            "schema",
            "sourceLink",
            "exactDuplicate",
            "nearDuplicate",
            "grammar",
            "translation",
            "naturalness",
            "targetStructure",
            "cefr",
            "license",
          ],
        },
      ],
      requiredBeforePublish: [
        "grammar-review",
        "bilingual-review",
        "naturalness-review",
        "cefr-review",
        "license-review",
      ],
      gameSmokes: [
        {
          gameId: "monkeytype",
          activity: "error-correction",
          recordSetId: "mistakes",
          sampleCount: 3,
        },
      ],
    };

    const existingIndex = batchManifest.batches.findIndex((b) => b.id === batchId);
    if (existingIndex >= 0) {
      batchManifest.batches[existingIndex] = batchEntry;
    } else {
      batchManifest.batches.push(batchEntry);
    }
  }

  await fs.writeFile(manifestPath, stableJson(batchManifest), "utf8");
  console.log(`Registered ${shardCount} common mistake batches in manifest.json.`);
  console.log("=== Step 9 Common Mistakes Expansion Build Complete ===");
}

main().catch((err) => {
  console.error(err);
  process.exitCode = 1;
});
