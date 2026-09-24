import fs from "node:fs/promises";
import path from "node:path";

export function normalizeCurriculumKey(value) {
  return String(value).normalize("NFKC").trim().replace(/\s+/g, " ").toLowerCase();
}

export function stableJson(value) {
  return JSON.stringify(value, null, 2) + "\n";
}

function resolveTerms(terms, lookupEntries) {
  const seen = new Set();
  const entries = [];
  const missing = [];

  for (const raw of terms) {
    const key = normalizeCurriculumKey(raw);
    if (!key || seen.has(key)) continue;
    seen.add(key);
    const level = lookupEntries[key];
    if (Number.isInteger(level)) entries.push({ key, level });
    else missing.push(key);
  }

  return { entries, missing };
}

export function buildVocabularyCurriculum(source, lookup) {
  if (source?.version !== 1) throw new Error("Curriculum source version must be 1.");
  if (lookup?.version !== 1 || typeof lookup.entries !== "object") {
    throw new Error("Vocabulary lookup version 1 is required.");
  }

  const lookupEntries = lookup.entries;
  const reverseTopics = {};
  const topicCoverage = [];
  const groups = [];
  const topicIndex = [];
  const topicIds = new Set();

  for (const group of source.groups ?? []) {
    const generatedTopics = [];

    for (const topic of group.topics ?? []) {
      if (topicIds.has(topic.id)) throw new Error("Duplicate topic id: " + topic.id);
      topicIds.add(topic.id);

      const resolved = resolveTerms(topic.terms ?? [], lookupEntries);
      const entries = resolved.entries.map((entry, index) => ({
        ...entry,
        priority: index < 8 ? "core" : "support",
      }));

      for (const entry of entries) {
        const list = reverseTopics[entry.key] ?? [];
        if (!list.includes(topic.id)) list.push(topic.id);
        reverseTopics[entry.key] = list;
      }

      const generated = {
        id: topic.id,
        label: topic.label,
        levels: topic.levels ?? [],
        entries,
      };
      generatedTopics.push(generated);
      topicIndex.push({
        id: topic.id,
        label: topic.label,
        group: group.id,
        groupLabel: group.label,
        levels: topic.levels ?? [],
        count: entries.length,
        entries: resolved.entries.map((entry) => ({ ...entry })),
        keys: entries.map((entry) => entry.key),
      });
      topicCoverage.push({
        id: topic.id,
        requested: new Set((topic.terms ?? []).map(normalizeCurriculumKey)).size,
        resolved: entries.length,
        missing: resolved.missing,
      });
    }

    groups.push({
      id: group.id,
      label: group.label,
      topics: generatedTopics,
    });
  }

  const posCategories = Object.entries(source.partsOfSpeech ?? {}).map(([id, terms]) => {
    const resolved = resolveTerms(terms, lookupEntries);
    return {
      id,
      tokens: [...new Set(terms.map(normalizeCurriculumKey))],
      entries: resolved.entries,
      missing: resolved.missing,
    };
  });

  const grammarModules = (source.grammar ?? []).map((module) => {
    const resolved = resolveTerms(module.signals ?? [], lookupEntries);
    return {
      id: module.id,
      label: module.label,
      group: module.group,
      focus: module.focus ?? [],
      topicIds: module.topicIds ?? [],
      signalTokens: [...new Set((module.signals ?? []).map(normalizeCurriculumKey))],
      signalEntries: resolved.entries,
      missingSignalKeys: resolved.missing,
    };
  });

  const requested = topicCoverage.reduce((sum, item) => sum + item.requested, 0);
  const resolved = topicCoverage.reduce((sum, item) => sum + item.resolved, 0);
  const uniqueTopicKeys = Object.keys(reverseTopics).length;

  const catalog = { version: 1, groups };
  const index = {
    version: 1,
    totalGroups: groups.length,
    totalTopics: topicIndex.length,
    uniqueVocabularyKeys: uniqueTopicKeys,
    topics: topicIndex,
    reverseTopics,
  };
  const partsOfSpeech = { version: 1, categories: posCategories };
  const grammar = {
    version: 1,
    primaryTimeGroups: ["time.present", "time.past", "time.future"],
    modules: grammarModules,
  };
  const coverage = {
    version: 1,
    vocabularyTotal: lookup.totalEntries,
    topicRequestedReferences: requested,
    topicResolvedReferences: resolved,
    topicExactMatchRate: requested === 0 ? 0 : Number((resolved / requested).toFixed(4)),
    uniqueTopicVocabularyKeys: uniqueTopicKeys,
    topics: topicCoverage,
    partsOfSpeech: posCategories.map((category) => ({
      id: category.id,
      requested: category.tokens.length,
      resolved: category.entries.length,
      missing: category.missing,
    })),
    grammar: grammarModules.map((module) => ({
      id: module.id,
      requested: module.signalTokens.length,
      resolved: module.signalEntries.length,
      missing: module.missingSignalKeys,
    })),
  };

  return { catalog, index, partsOfSpeech, grammar, coverage };
}

export async function loadCurriculumInputs(root) {
  const vocabularyDir = path.join(root, "shared", "vocabulary");
  const [sourceRaw, lookupRaw] = await Promise.all([
    fs.readFile(path.join(vocabularyDir, "curriculum", "source.json"), "utf8"),
    fs.readFile(path.join(vocabularyDir, "lookup.json"), "utf8"),
  ]);
  return {
    vocabularyDir,
    source: JSON.parse(sourceRaw),
    lookup: JSON.parse(lookupRaw),
  };
}

export const CURRICULUM_ARTIFACTS = {
  "topics/catalog.json": "catalog",
  "topics/index.json": "index",
  "parts-of-speech/index.json": "partsOfSpeech",
  "grammar/index.json": "grammar",
  "curriculum/coverage.json": "coverage",
};

export async function writeCurriculumArtifacts(root, artifacts) {
  const vocabularyDir = path.join(root, "shared", "vocabulary");
  for (const [relativePath, key] of Object.entries(CURRICULUM_ARTIFACTS)) {
    const target = path.join(vocabularyDir, relativePath);
    await fs.mkdir(path.dirname(target), { recursive: true });
    await fs.writeFile(target, stableJson(artifacts[key]), "utf8");
  }
}
