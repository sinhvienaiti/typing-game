import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { normalizeSentenceKey, readJson, stableJson } from "./english-content-core.mjs";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");

const STOPWORDS = new Set([
  "a", "an", "the", "to", "of", "in", "on", "at", "for", "from", "by", "with",
  "up", "out", "off", "down", "away", "back", "over", "into", "onto", "through",
  "someone", "something", "somebody", "sb", "sth", "oneself", "one's", "your",
  "my", "his", "her", "their", "our", "its", "be", "is", "are", "am", "was", "were",
  "do", "does", "did", "done", "make", "made", "take", "took", "taken", "have", "has", "had",
  "get", "got", "gotten", "go", "went", "gone", "give", "gave", "given", "keep", "kept",
  "put", "set", "run", "ran", "come", "came", "see", "saw", "seen", "it", "this", "that",
  "and", "or", "but", "not", "no", "as", "than", "so"
]);

const IRREGULAR_TO_BASE = new Map([
  ["am", "be"], ["is", "be"], ["are", "be"], ["was", "be"], ["were", "be"], ["been", "be"], ["being", "be"],
  ["has", "have"], ["had", "have"], ["having", "have"],
  ["does", "do"], ["did", "do"], ["done", "do"], ["doing", "do"],
  ["made", "make"], ["makes", "make"], ["making", "make"],
  ["took", "take"], ["taken", "take"], ["takes", "take"], ["taking", "take"],
  ["got", "get"], ["gotten", "get"], ["gets", "get"], ["getting", "get"],
  ["gave", "give"], ["given", "give"], ["gives", "give"], ["giving", "give"],
  ["went", "go"], ["gone", "go"], ["goes", "go"], ["going", "go"],
  ["came", "come"], ["comes", "come"], ["coming", "come"],
  ["saw", "see"], ["seen", "see"], ["sees", "see"], ["seeing", "see"],
  ["ran", "run"], ["runs", "run"], ["running", "run"],
  ["kept", "keep"], ["keeps", "keep"], ["keeping", "keep"],
  ["left", "leave"], ["leaves", "leave"], ["leaving", "leave"],
  ["felt", "feel"], ["feels", "feel"], ["feeling", "feel"],
  ["brought", "bring"], ["brings", "bring"], ["bringing", "bring"],
  ["bought", "buy"], ["buys", "buy"], ["buying", "buy"],
  ["thought", "think"], ["thinks", "think"], ["thinking", "think"],
  ["taught", "teach"], ["teaches", "teach"], ["teaching", "teach"],
  ["caught", "catch"], ["catches", "catch"], ["catching", "catch"],
  ["fought", "fight"], ["fights", "fight"], ["fighting", "fight"],
  ["found", "find"], ["finds", "find"], ["finding", "find"],
  ["told", "tell"], ["tells", "tell"], ["telling", "tell"],
  ["sold", "sell"], ["sells", "sell"], ["selling", "sell"],
  ["held", "hold"], ["holds", "hold"], ["holding", "hold"],
  ["paid", "pay"], ["pays", "pay"], ["paying", "pay"],
  ["said", "say"], ["says", "say"], ["saying", "say"],
  ["sent", "send"], ["sends", "send"], ["sending", "send"],
  ["spent", "spend"], ["spends", "spend"], ["spending", "spend"],
  ["built", "build"], ["builds", "build"], ["building", "build"],
  ["lost", "lose"], ["loses", "lose"], ["losing", "lose"],
  ["met", "meet"], ["meets", "meet"], ["meeting", "meet"],
  ["led", "lead"], ["leads", "lead"], ["leading", "lead"],
  ["understood", "understand"], ["understands", "understand"], ["understanding", "understand"],
  ["broke", "break"], ["broken", "break"], ["breaks", "break"], ["breaking", "break"],
  ["chose", "choose"], ["chosen", "choose"], ["chooses", "choose"], ["choosing", "choose"],
  ["spoke", "speak"], ["spoken", "speak"], ["speaks", "speak"], ["speaking", "speak"],
  ["wrote", "write"], ["written", "write"], ["writes", "write"], ["writing", "write"],
  ["drove", "drive"], ["driven", "drive"], ["drives", "drive"], ["driving", "drive"],
  ["fell", "fall"], ["fallen", "fall"], ["falls", "fall"], ["falling", "fall"],
  ["grew", "grow"], ["grown", "grow"], ["grows", "grow"], ["growing", "grow"],
  ["knew", "know"], ["known", "know"], ["knows", "know"], ["knowing", "know"],
  ["threw", "throw"], ["thrown", "throw"], ["throws", "throw"], ["throwing", "throw"],
  ["wore", "wear"], ["worn", "wear"], ["wears", "wear"], ["wearing", "wear"],
  ["won", "win"], ["wins", "win"], ["winning", "win"],
  ["began", "begin"], ["begun", "begin"], ["begins", "begin"], ["beginning", "begin"],
  ["drank", "drink"], ["drunk", "drink"], ["drinks", "drink"],
  ["sang", "sing"], ["sung", "sing"], ["sings", "sing"],
  ["swam", "swim"], ["swum", "swim"], ["swims", "swim"],
  ["ate", "eat"], ["eaten", "eat"], ["eats", "eat"], ["eating", "eat"],
  ["stood", "stand"], ["stands", "stand"], ["standing", "stand"],
  ["sat", "sit"], ["sits", "sit"], ["sitting", "sit"],
  ["slept", "sleep"], ["sleeps", "sleep"], ["sleeping", "sleep"],
  ["children", "child"], ["men", "man"], ["women", "woman"], ["people", "person"],
  ["feet", "foot"], ["teeth", "tooth"], ["mice", "mouse"], ["geese", "goose"],
  ["better", "good"], ["best", "good"], ["worse", "bad"], ["worst", "bad"],
]);

function lemmatize(word) {
  const w = word.toLowerCase();
  if (IRREGULAR_TO_BASE.has(w)) return [IRREGULAR_TO_BASE.get(w), w];
  const forms = new Set([w]);
  if (w.length > 4 && w.endsWith("ies")) forms.add(w.slice(0, -3) + "y");
  if (w.length > 4 && w.endsWith("ied")) forms.add(w.slice(0, -3) + "y");
  if (w.length > 4 && w.endsWith("es")) forms.add(w.slice(0, -2));
  if (w.length > 3 && w.endsWith("s") && !w.endsWith("ss")) forms.add(w.slice(0, -1));
  if (w.length > 4 && w.endsWith("ed")) {
    forms.add(w.slice(0, -2));
    forms.add(w.slice(0, -1));
    if (w.length > 5 && w[w.length - 3] === w[w.length - 4]) forms.add(w.slice(0, -3));
  }
  if (w.length > 5 && w.endsWith("ing")) {
    forms.add(w.slice(0, -3));
    forms.add(w.slice(0, -3) + "e");
    if (w.length > 6 && w[w.length - 4] === w[w.length - 5]) forms.add(w.slice(0, -4));
  }
  return [...forms];
}

function tokenizeLower(text) {
  return String(text)
    .normalize("NFKC")
    .toLowerCase()
    .replace(/['’]s\b/g, "")
    .match(/[a-z]+/g) || [];
}

const PLACEHOLDER_TOKENS = new Set(["someone", "something", "somebody", "sb", "sth", "oneself"]);
const DETERMINERS = new Set(["a", "an", "the", "my", "your", "his", "her", "their", "our", "its", "some", "any", "no", "this", "that"]);

function tokenMatchesSlot(phraseToken, sentWord, sentLemmaSet) {
  if (PLACEHOLDER_TOKENS.has(phraseToken)) return true;
  if ((phraseToken === "a" || phraseToken === "an" || phraseToken === "the") && DETERMINERS.has(sentWord)) {
    return true;
  }
  const targetLemmas = lemmatize(phraseToken);
  return targetLemmas.some((l) => sentLemmaSet.has(l));
}

function isOrderedSubsequenceWithinWindow(phraseTokens, sentenceWords, sentenceLemmasList, maxGapTotal = 3) {
  // Check ordered match where phraseTokens[0..k] match lemmas/placeholders of sentence tokens with bounded gaps
  const n = sentenceLemmasList.length;
  const m = phraseTokens.length;
  if (m === 0 || n < m) return null;

  for (let start = 0; start <= n - m; start++) {
    if (PLACEHOLDER_TOKENS.has(phraseTokens[0])) continue;
    if (!tokenMatchesSlot(phraseTokens[0], sentenceWords[start], sentenceLemmasList[start])) continue;

    let pos = start;
    let totalGap = 0;
    let matched = true;
    const positions = [start];

    for (let pi = 1; pi < m; pi++) {
      const pTok = phraseTokens[pi];
      if (PLACEHOLDER_TOKENS.has(pTok)) {
        // Placeholder slot matches 1–2 content/pronoun tokens inside window
        if (pos + 1 >= n) {
          matched = false;
          break;
        }
        pos = pos + 1;
        positions.push(pos);
        continue;
      }
      let foundAt = -1;
      for (let scan = pos + 1; scan < n && scan <= pos + 1 + maxGapTotal; scan++) {
        if (tokenMatchesSlot(pTok, sentenceWords[scan], sentenceLemmasList[scan])) {
          foundAt = scan;
          break;
        }
      }
      if (foundAt === -1) {
        matched = false;
        break;
      }
      totalGap += foundAt - pos - 1;
      if (totalGap > maxGapTotal) {
        matched = false;
        break;
      }
      pos = foundAt;
      positions.push(foundAt);
    }

    if (matched) return { start, end: pos, totalGap, positions };
  }
  return null;
}

async function loadDatasetRecords(dataset) {
  const manifest = await readJson(path.join(root, "shared", dataset, "manifest.json"));
  const byGroup = {};
  for (const s of manifest.shards) {
    const g = s.path.split("/")[0];
    const doc = await readJson(path.join(root, "shared", dataset, s.path));
    (byGroup[g] ??= []).push(...doc.records);
  }
  return byGroup;
}

async function main() {
  console.log("=== E13 Full Causal Gap Classification Audit ===");
  const [dictGroups, sentGroups, phraseGroups, vocabLookup] = await Promise.all([
    loadDatasetRecords("dictionary"),
    loadDatasetRecords("sentences"),
    loadDatasetRecords("phrases"),
    readJson(path.join(root, "shared", "vocabulary", "lookup.json")),
  ]);

  const examples = (sentGroups.examples ?? []).filter((r) => r?.quality?.state === "published");
  console.log(`Loaded ${examples.length} published examples. Building inverted lemma index...`);

  const inverted = new Map();
  const exampleRows = examples.map((ex, idx) => {
    const norm = " " + normalizeSentenceKey(ex.text) + " ";
    const tokens = tokenizeLower(ex.text);
    const tokenLemmas = tokens.map((t) => new Set(lemmatize(t)));
    const allLemmas = new Set();
    for (const s of tokenLemmas) {
      for (const l of s) allLemmas.add(l);
    }
    for (const l of allLemmas) {
      let arr = inverted.get(l);
      if (!arr) {
        arr = [];
        inverted.set(l, arr);
      }
      arr.push(idx);
    }
    return { id: ex.id, text: ex.text, cefr: ex.cefr, norm, tokens, tokenLemmas };
  });

  function candidateIndicesForTokens(tokens) {
    // Pick rarest token index using inverted list size
    let bestArr = null;
    for (const tok of tokens) {
      if (STOPWORDS.has(tok)) continue;
      for (const l of lemmatize(tok)) {
        const arr = inverted.get(l);
        if (arr && (!bestArr || arr.length < bestArr.length)) {
          bestArr = arr;
        }
      }
    }
    if (!bestArr) {
      for (const tok of tokens) {
        for (const l of lemmatize(tok)) {
          const arr = inverted.get(l);
          if (arr && (!bestArr || arr.length < bestArr.length)) {
            bestArr = arr;
          }
        }
      }
    }
    return bestArr ?? [];
  }

  function classifyPhraseFamily(records, familyName) {
    const counts = {
      total: records.length,
      "already-linked": 0,
      "matcher-false-negative": 0,
      "pending-editorial-review": 0,
      "unsupported-frame": 0,
      "true-absence": 0,
    };
    const samples = {
      "matcher-false-negative": [],
      "pending-editorial-review": [],
      "unsupported-frame": [],
      "true-absence": [],
    };
    let totalMatchedCandidates = 0;

    for (const rec of records) {
      if (Array.isArray(rec.exampleIds) && rec.exampleIds.length > 0) {
        counts["already-linked"]++;
        continue;
      }

      if (familyName === "verbPatterns") {
        // Check if lemma even appears in examples; complex syntactic frame needs structural check
        const lemmaToks = tokenizeLower(rec.lemma);
        const candidates = candidateIndicesForTokens(lemmaToks);
        if (candidates.length === 0) {
          counts["true-absence"]++;
          if (samples["true-absence"].length < 15) {
            samples["true-absence"].push({ id: rec.id, lemma: rec.lemma, frame: rec.frame });
          }
        } else {
          counts["unsupported-frame"]++;
          if (samples["unsupported-frame"].length < 15) {
            samples["unsupported-frame"].push({
              id: rec.id,
              lemma: rec.lemma,
              frame: rec.frame,
              lemmaHitsInCorpus: candidates.length,
              sampleSentence: exampleRows[candidates[0]].text,
            });
          }
        }
        continue;
      }

      const rawText = String(rec.text || "").trim();
      const tokens = tokenizeLower(rawText);
      if (tokens.length === 0) {
        counts["true-absence"]++;
        continue;
      }

      const cleanNorm = " " + normalizeSentenceKey(rawText) + " ";
      const cands = candidateIndicesForTokens(tokens);

      let bestExact = null;
      let bestContiguousMorph = null;
      let bestGapped = null;
      let hitCount = 0;

      for (const idx of cands) {
        const row = exampleRows[idx];
        if (cleanNorm.length > 2 && row.norm.includes(cleanNorm)) {
          bestExact ??= row;
          hitCount++;
          continue;
        }
        const mZero = isOrderedSubsequenceWithinWindow(tokens, row.tokens, row.tokenLemmas, 0);
        if (mZero) {
          bestContiguousMorph ??= row;
          hitCount++;
          continue;
        }
        const mGap = isOrderedSubsequenceWithinWindow(tokens, row.tokens, row.tokenLemmas, rec.type === "phrasal-verb" ? 2 : 2);
        if (mGap) {
          bestGapped ??= row;
          hitCount++;
        }
      }

      if (bestExact || bestContiguousMorph) {
        // Contiguous inflected match (or unlinked exact match) missed by previous Step 10 matcher
        counts["matcher-false-negative"]++;
        totalMatchedCandidates++;
        const ex = bestExact ?? bestContiguousMorph;
        if (samples["matcher-false-negative"].length < 20) {
          samples["matcher-false-negative"].push({
            id: rec.id,
            text: rawText,
            type: rec.type ?? familyName,
            hitCount,
            sampleId: ex.id,
            sampleText: ex.text,
          });
        }
      } else if (bestGapped) {
        counts["pending-editorial-review"]++;
        totalMatchedCandidates++;
        if (samples["pending-editorial-review"].length < 20) {
          samples["pending-editorial-review"].push({
            id: rec.id,
            text: rawText,
            type: rec.type ?? familyName,
            hitCount,
            sampleId: bestGapped.id,
            sampleText: bestGapped.text,
          });
        }
      } else {
        counts["true-absence"]++;
        if (samples["true-absence"].length < 20) {
          samples["true-absence"].push({ id: rec.id, text: rawText, type: rec.type ?? familyName });
        }
      }
    }

    const eligibleWithoutExamples = counts.total - counts["already-linked"];
    const recoverablePct = eligibleWithoutExamples === 0
      ? 0
      : Number((((counts["matcher-false-negative"] + counts["pending-editorial-review"]) / eligibleWithoutExamples) * 100).toFixed(2));

    return {
      counts,
      eligibleWithoutExamples,
      recoverableCandidates: totalMatchedCandidates,
      recoverableShareOfMissingPct: recoverablePct,
      samples,
    };
  }

  const collocations = phraseGroups.collocations ?? [];
  const verbPatterns = phraseGroups["verb-patterns"] ?? [];
  const phraseItems = phraseGroups.items ?? [];
  const phrasalVerbs = phraseItems.filter((r) => r.type === "phrasal-verb");
  const chunks = phraseItems.filter((r) => r.type === "chunk");
  const idioms = phraseItems.filter((r) => r.type === "idiom");

  // Vocabulary <-> E03 Lexemes overlap
  const lexemes = dictGroups.lexemes ?? [];
  const e03Keys = new Set(lexemes.map((l) => String(l.headwordKey || l.headword).toLowerCase()));
  const rawEntries = vocabLookup.entries;
  const vocabKeys = new Set(
    Array.isArray(rawEntries)
      ? rawEntries.map((e) => String(e.en || "").toLowerCase().trim()).filter(Boolean)
      : rawEntries && typeof rawEntries === "object"
        ? Object.keys(rawEntries).map((k) => k.toLowerCase().trim()).filter(Boolean)
        : []
  );
  let e03InLegacy = 0;
  for (const k of e03Keys) if (vocabKeys.has(k)) e03InLegacy++;

  const report = {
    schemaVersion: 1,
    phase: "Phase 0 / E13 Causal Gap Classification",
    generatedAt: new Date().toISOString(),
    corpusScanned: {
      publishedExamples: examples.length,
      collocations: collocations.length,
      verbPatterns: verbPatterns.length,
      phrasalVerbs: phrasalVerbs.length,
      chunks: chunks.length,
      idioms: idioms.length,
      e03Lexemes: lexemes.length,
      legacyVocabularyUniqueKeys: vocabKeys.size,
      e03OverlapWithLegacyVocab: e03InLegacy,
    },
    families: {
      collocations: classifyPhraseFamily(collocations, "collocations"),
      phrasalVerbs: classifyPhraseFamily(phrasalVerbs, "phrasalVerbs"),
      chunks: classifyPhraseFamily(chunks, "chunks"),
      idioms: classifyPhraseFamily(idioms, "idioms"),
      verbPatterns: classifyPhraseFamily(verbPatterns, "verbPatterns"),
    },
  };

  const outPath = path.join(root, "content", "english", "reports", "e13-causal-gap-audit.json");
  await fs.mkdir(path.dirname(outPath), { recursive: true });
  await fs.writeFile(outPath, stableJson(report), "utf8");

  console.log("Summary:");
  for (const [k, f] of Object.entries(report.families)) {
    console.log(`- ${k}:`, JSON.stringify(f.counts), `| recoverable%=${f.recoverableShareOfMissingPct}%`);
  }
  console.log("Vocabulary overlap:", report.corpusScanned.e03OverlapWithLegacyVocab, "/", lexemes.length, "in", vocabKeys.size, "legacy keys");
  console.log("Report written to:", outPath);
}

main().catch((err) => {
  console.error(err);
  process.exitCode = 1;
});
