import { readFile } from "node:fs/promises";
import { resolve } from "node:path";

const cache = new Map();

async function readJson(path) {
  return JSON.parse(await readFile(path, "utf8"));
}

function vocabularyCefr(label) {
  const match = String(label).match(/\b(A1|A2|B1|B2|C1|C2)\b/);
  return match?.[1] ?? "Foundation";
}

function boundedInteger(value, fallback, minimum, maximum) {
  if (value === null || value === "") return fallback;
  const parsed = Number.parseInt(value, 10);
  if (!Number.isInteger(parsed)) return fallback;
  return Math.max(minimum, Math.min(maximum, parsed));
}

async function loadCanonicalCatalog(rootDir) {
  const key = resolve(rootDir);
  let pending = cache.get(key);
  if (pending) return pending;

  pending = (async () => {
    const vocabularyRoot = resolve(key, "shared/vocabulary");
    const typingTextRoot = resolve(key, "shared/typing-texts");
    const [vocabularyIndex, typingTextIndex, topicReverse] = await Promise.all([
      readJson(resolve(vocabularyRoot, "index.json")),
      readJson(resolve(typingTextRoot, "index.json")),
      readJson(resolve(vocabularyRoot, "topics/reverse.json")),
    ]);

    const vocabularyLevels = await Promise.all(
      vocabularyIndex.levels.map((entry) => readJson(resolve(vocabularyRoot, entry.file))),
    );
    const typingTextLevels = await Promise.all(
      typingTextIndex.levels.map((entry) => readJson(resolve(typingTextRoot, entry.file))),
    );

    const vocabulary = [];
    for (const file of vocabularyLevels) {
      const cefr = vocabularyCefr(file.label);
      for (const entry of file.entries) {
        const topics = topicReverse.reverseTopics?.[String(entry.en).toLowerCase()] ?? [];
        vocabulary.push({
          id: entry.id,
          title: entry.en,
          type: "vocabulary",
          cefr,
          topics,
          difficulty: `Level ${file.level}`,
          length: entry.en.length,
          usedBy: ["combat", "recall", "smart-review"],
          status: "canonical",
          source: "shared/vocabulary",
          level: file.level,
          meaning: entry.vi,
          ipa: entry.ipa,
          searchText: [entry.id, entry.en, entry.vi, entry.ipa, ...topics].join(" ").toLowerCase(),
        });
      }
    }

    const typingText = [];
    for (const file of typingTextLevels) {
      for (const passage of file.passages) {
        typingText.push({
          id: passage.id,
          title: passage.topic,
          type: "typing-text",
          cefr: file.cefr,
          topics: [passage.topic],
          difficulty: `Level ${file.level}`,
          length: passage.wordCount,
          usedBy: ["special-stage-typing"],
          status: "canonical",
          source: "shared/typing-texts",
          level: file.level,
          style: passage.style,
          setting: passage.setting,
          tone: passage.tone,
          targetWords: passage.targetWords,
          excerpt: passage.text.slice(0, 280),
          searchText: [passage.id, passage.topic, passage.style, passage.setting, passage.tone, ...passage.targetWords, passage.text]
            .join(" ")
            .toLowerCase(),
        });
      }
    }

    return {
      vocabularyIndex,
      typingTextIndex,
      vocabulary,
      typingText,
    };
  })();

  cache.set(key, pending);
  try {
    return await pending;
  } catch (error) {
    cache.delete(key);
    throw error;
  }
}

function publicItem(item) {
  const { searchText: _searchText, ...result } = item;
  return result;
}

export async function queryTypingContentCatalog({ rootDir, searchParams = new URLSearchParams() }) {
  const data = await loadCanonicalCatalog(rootDir);
  const kind = searchParams.get("kind") || "vocabulary";
  if (kind !== "vocabulary" && kind !== "typing-text") {
    throw new TypeError(`Unsupported typing-content kind: ${kind}`);
  }

  const q = (searchParams.get("q") || "").trim().toLowerCase();
  const cefr = (searchParams.get("cefr") || "").trim();
  const topic = (searchParams.get("topic") || "").trim().toLowerCase();
  const source = (searchParams.get("source") || "").trim();
  const usedBy = (searchParams.get("usedBy") || "").trim();
  const levelValue = searchParams.get("level");
  const level = levelValue ? boundedInteger(levelValue, 0, 1, 100) : 0;
  const offset = boundedInteger(searchParams.get("offset"), 0, 0, 1_000_000);
  const limit = boundedInteger(searchParams.get("limit"), 50, 1, 100);

  let items = kind === "vocabulary" ? data.vocabulary : data.typingText;
  if (q) items = items.filter((item) => item.searchText.includes(q));
  if (cefr) items = items.filter((item) => item.cefr === cefr);
  if (topic) items = items.filter((item) => item.topics.some((value) => value.toLowerCase().includes(topic)));
  if (source) items = items.filter((item) => item.source === source);
  if (usedBy) items = items.filter((item) => item.usedBy.includes(usedBy));
  if (level) items = items.filter((item) => item.level === level);

  const total = items.length;
  const page = items.slice(offset, offset + limit).map(publicItem);

  return {
    protocolVersion: 1,
    mode: "canonical-readonly",
    owner: "English Learning Content System",
    kind,
    total,
    offset,
    limit,
    items: page,
    canonicalTotals: {
      vocabulary: data.vocabularyIndex.totalEntries,
      vocabularyLevels: data.vocabularyIndex.availableLevels,
      typingText: data.typingTextIndex.totalPassages,
      typingTextLevels: data.typingTextIndex.availableLevels,
    },
    tabs: {
      vocabulary: { status: "canonical", source: "shared/vocabulary", consumers: ["combat", "recall", "smart-review"] },
      typingText: { status: "canonical", source: "shared/typing-texts", consumers: ["special-stage-typing"] },
      bossText: { status: "derived", source: "shared/vocabulary", note: "No standalone boss text corpus is currently consumed by Space Typing." },
      recall: { status: "derived", source: "shared/vocabulary", note: "Recall consumes canonical VocabularyEntry IDs and shared review datasets." },
      objectives: { status: "gameplay-owned", source: "games/space-typing/src/events/objectives", note: "Current stage objectives are gameplay rules, not English-learning content records." },
    },
  };
}

export function clearTypingContentCatalogCacheForTests() {
  cache.clear();
}
