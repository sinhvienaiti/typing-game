import { listEnglishActivities } from "./capabilities.mjs";
import { buildGameEnglishActivityDataset } from "./game-adapters.mjs";

export const ENGLISH_ACTIVITY_SOURCES = Object.freeze({
  vocabulary: [{ dataset: "dictionary", prefix: "lexemes-" }],
  collocation: [{ dataset: "phrases", prefix: "collocations-" }],
  "verb-pattern": [{ dataset: "phrases", prefix: "verb-patterns-" }],
  "phrasal-verb": [{ dataset: "phrases", prefix: "phrases-", type: "phrasal-verb" }],
  chunk: [{ dataset: "phrases", prefix: "phrases-", type: "chunk" }],
  idiom: [{ dataset: "phrases", prefix: "phrases-", type: "idiom" }],
  "grammar-topic": [{ dataset: "grammar", prefix: "topics-" }],
  "grammar-challenge": [{ dataset: "grammar", prefix: "topics-" }],
  "example-typing": [{ dataset: "sentences", prefix: "examples-" }],
  "listening-typing": [
    { dataset: "sentences", prefix: "exercises-", type: "listening-typing" },
    { dataset: "sentences", prefix: "examples-" },
  ],
  translation: [{ dataset: "sentences", prefix: "exercises-", type: "translation" }],
  cloze: [{ dataset: "sentences", prefix: "exercises-", type: "cloze" }],
  "error-correction": [
    { dataset: "sentences", prefix: "exercises-", type: "error-correction" },
    { dataset: "sentences", prefix: "mistakes-" },
  ],
  "sentence-building": [{ dataset: "sentences", prefix: "exercises-", type: "sentence-building" }],
  transformation: [{ dataset: "sentences", prefix: "exercises-", type: "transformation" }],
  "contextual-usage": [{ dataset: "sentences", prefix: "exercises-", type: "contextual-usage" }],
  dialogue: [{ dataset: "sentences", prefix: "dialogues-" }],
});

const GAME_MAX_ANSWER_LENGTH = Object.freeze({
  "recall-typing": 200,
  "vocab-shooter": 200,
  "space-typing": 240,
});

function sourceSpecs(activity) {
  const specs = ENGLISH_ACTIVITY_SOURCES[activity];
  if (!Array.isArray(specs)) throw new TypeError("No published runtime source for activity: " + activity);
  return specs;
}
function published(record) {
  return record !== null && typeof record === "object" && !Array.isArray(record) && record.quality?.state === "published";
}
function matchesType(record, type) {
  return type === undefined || record?.type === type;
}
function boundedLimit(value) {
  const limit = Number(value ?? 20);
  if (!Number.isInteger(limit) || limit < 1 || limit > 100) {
    throw new TypeError("English activity limit must be an integer from 1 to 100");
  }
  return limit;
}

function recordAnswerLength(activity, record) {
  if (activity === "vocabulary") return String(record?.en ?? record?.headword ?? "").trim().length;
  if (activity === "collocation" || activity === "phrasal-verb" || activity === "chunk" || activity === "idiom") {
    return String(record?.text ?? "").trim().length;
  }
  if (activity === "verb-pattern") {
    return (String(record?.lemma ?? "").trim() + " · " + String(record?.frame ?? "").trim()).length;
  }
  if (activity === "grammar-topic" || activity === "grammar-challenge") {
    for (const k of ["positive", "negative", "question"]) {
      const f = record?.forms?.[k]?.[0];
      if (typeof f === "string" && f.trim() !== "") return f.trim().length;
    }
    return String(record?.acceptedAnswers?.[0] ?? "").trim().length;
  }
  if (activity === "dialogue") {
    const turns = Array.isArray(record?.turns) ? record.turns : [];
    let maxTurn = 0;
    for (const turn of turns) maxTurn = Math.max(maxTurn, String(turn?.text ?? "").trim().length);
    return maxTurn;
  }
  if (activity === "error-correction" && typeof record?.id === "string" && record.id.startsWith("err.")) {
    return String(record?.corrections?.[0] ?? "").trim().length;
  }
  if (typeof record?.type === "string" && Array.isArray(record?.acceptedAnswers)) {
    return String(record.acceptedAnswers[0] ?? "").trim().length;
  }
  return String(record?.text ?? "").trim().length;
}

function seededPrng(seed) {
  let a = (Number(seed) || 1) >>> 0;
  return function () {
    a |= 0;
    a = (a + 0x6d2b79f5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function shuffled(arr, seed) {
  const out = [...arr];
  const rand = seededPrng(seed);
  for (let i = out.length - 1; i > 0; i--) {
    const j = Math.floor(rand() * (i + 1));
    [out[i], out[j]] = [out[j], out[i]];
  }
  return out;
}

function matchesOptions(activity, record, options) {
  if (!published(record)) return false;
  if (options.cefr && record.cefr !== options.cefr) return false;
  if (options.maxAnswerLength && recordAnswerLength(activity, record) > options.maxAnswerLength) return false;
  return true;
}

export async function loadPublishedEnglishActivityRecords(loader, activity, options = {}) {
  if (loader === null || typeof loader !== "object" || typeof loader.loadDataset !== "function") {
    throw new TypeError("English runtime loader is required");
  }
  const limit = boundedLimit(options.limit);
  const specs = sourceSpecs(activity);

  // Fast indexed shard selection when loader exposes activity indexes
  if (typeof loader.loadActivityIndex === "function" && typeof loader.loadShard === "function") {
    const actIdx = await loader.loadActivityIndex(activity);
    if (actIdx && Array.isArray(actIdx.shards)) {
      let candidates = actIdx.shards.filter((s) => {
        if (s.matchedCount <= 0) return false;
        if (options.cefr && !(s.byCefr?.[options.cefr] > 0)) return false;
        if (options.maxAnswerLength && s.minLen > options.maxAnswerLength) return false;
        return true;
      });

      if (candidates.length === 0) return [];
      const offset = Number.isInteger(options.offset) && options.offset >= 0 ? options.offset : 0;
      if (offset > 0 && candidates.length > 1) {
        const shift = offset % candidates.length;
        candidates = [...candidates.slice(shift), ...candidates.slice(0, shift)];
      }
      if (options.seed !== undefined && options.seed !== null) {
        candidates = shuffled(candidates, options.seed);
      }

      const results = [];
      const seen = new Set();
      for (const shardInfo of candidates) {
        const shardRecords = await loader.loadShard(shardInfo.dataset, {
          id: shardInfo.shardId,
          path: shardInfo.path,
          count: shardInfo.count,
        });
        const orderedRecords = options.seed !== undefined && options.seed !== null
          ? shuffled(shardRecords, Number(options.seed) + results.length + shardInfo.shardId.length)
          : shardRecords;

        const expectedTypes = specs
          .filter((sp) => sp.dataset === shardInfo.dataset && String(shardInfo.shardId).startsWith(sp.prefix))
          .map((sp) => sp.type);

        for (const record of orderedRecords) {
          if (!matchesOptions(activity, record, options)) continue;
          if (!expectedTypes.some((t) => matchesType(record, t))) continue;
          const id = typeof record.id === "string" ? record.id : typeof record.lexemeId === "string" ? record.lexemeId : "";
          const key = id || JSON.stringify(record);
          if (seen.has(key)) continue;
          seen.add(key);
          results.push(record);
          if (results.length >= limit) return results;
        }
      }
      return results;
    }
  }

  // Fallback for unindexed mock loaders / tests
  const results = [];
  const seen = new Set();
  for (const spec of specs) {
    const records = await loader.loadDataset(spec.dataset, { prefix: spec.prefix });
    for (const record of records) {
      if (!matchesOptions(activity, record, options) || !matchesType(record, spec.type)) continue;
      const id = typeof record.id === "string" ? record.id : typeof record.lexemeId === "string" ? record.lexemeId : "";
      const key = id || JSON.stringify(record);
      if (seen.has(key)) continue;
      seen.add(key);
      results.push(record);
      if (results.length >= limit) return results;
    }
  }
  return results;
}

export async function countPublishedEnglishActivityRecords(loader, activity, options = {}) {
  if (loader === null || typeof loader !== "object" || typeof loader.loadDataset !== "function") {
    throw new TypeError("English runtime loader is required");
  }
  sourceSpecs(activity);

  if (typeof loader.loadAvailability === "function") {
    const avail = await loader.loadAvailability();
    const entry = avail?.activities?.[activity];
    if (entry && typeof entry.total === "number") {
      if (!options.cefr && !options.maxAnswerLength) return entry.total;
      if (options.cefr && !options.maxAnswerLength) return entry.byCefr?.[options.cefr] ?? 0;
      if (!options.cefr && options.maxAnswerLength === 200) return entry.within200 ?? entry.total;
      if (!options.cefr && options.maxAnswerLength === 240) return entry.within240 ?? entry.total;
      if (typeof loader.loadActivityIndex === "function") {
        const actIdx = await loader.loadActivityIndex(activity);
        if (actIdx?.shards) {
          let sum = 0;
          for (const s of actIdx.shards) {
            if (options.cefr && !(s.byCefr?.[options.cefr] > 0)) continue;
            if (options.maxAnswerLength && s.minLen > options.maxAnswerLength) continue;
            sum += options.cefr ? (s.byCefr?.[options.cefr] ?? 0) : s.matchedCount;
          }
          return sum;
        }
      }
    }
  }

  const seen = new Set();
  for (const spec of sourceSpecs(activity)) {
    const records = await loader.loadDataset(spec.dataset, { prefix: spec.prefix });
    for (const record of records) {
      if (!matchesOptions(activity, record, options) || !matchesType(record, spec.type)) continue;
      const id = typeof record.id === "string" ? record.id : typeof record.lexemeId === "string" ? record.lexemeId : "";
      seen.add(id || JSON.stringify(record));
    }
  }
  return seen.size;
}

export async function publishedEnglishActivityAvailability(loader, gameCapabilityId) {
  const activities = listEnglishActivities(gameCapabilityId);
  if (typeof loader.loadAvailability === "function") {
    const avail = await loader.loadAvailability();
    if (avail?.activities) {
      return Object.fromEntries(activities.map((activity) => [activity, avail.activities[activity]?.total ?? 0]));
    }
  }
  const pairs = await Promise.all(
    activities.map(async (activity) => [
      activity,
      await countPublishedEnglishActivityRecords(loader, activity),
    ]),
  );
  return Object.fromEntries(pairs);
}

export async function buildPublishedGameEnglishActivityDataset(
  loader,
  gameId,
  gameCapabilityId,
  activity,
  requestId,
  options = {},
) {
  if (!listEnglishActivities(gameCapabilityId).includes(activity)) {
    throw new TypeError("English activity is not supported by " + gameId);
  }
  const effectiveMaxAnswerLength = options.maxAnswerLength ?? GAME_MAX_ANSWER_LENGTH[gameId];
  const fetchLimit = activity === "dialogue" ? Math.min(Number(options.limit ?? 20), 10) : options.limit;
  const records = await loadPublishedEnglishActivityRecords(loader, activity, {
    ...options,
    limit: fetchLimit,
    ...(effectiveMaxAnswerLength === undefined ? {} : { maxAnswerLength: effectiveMaxAnswerLength }),
  });
  if (records.length === 0) throw new Error("No published English content is available for " + activity);
  return buildGameEnglishActivityDataset(
    gameId,
    activity,
    records,
    requestId,
    {
      createdAt: options.createdAt,
      boundDialogueTurns: activity === "dialogue",
      maxItems: 100,
    },
  );
}
