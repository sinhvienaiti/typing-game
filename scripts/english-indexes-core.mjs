import crypto from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { createSchemaValidator, listJsonFiles, readJson, stableJson } from "./english-content-core.mjs";
import { ENGLISH_ACTIVITY_SOURCES } from "../shared/english-content/activity-source.mjs";
import { indexBucketHex } from "../shared/english-content/index-bucket.mjs";

export { indexBucketHex };
const DATASETS = ["dictionary", "grammar", "sentences", "phrases"];

export function compactJson(value) {
  return JSON.stringify(value) + "\n";
}

function recordIdOf(record) {
  if (typeof record?.id === "string" && record.id !== "") return record.id;
  if (typeof record?.lexemeId === "string" && record.lexemeId !== "") return record.lexemeId;
  return null;
}

function isVerifiedGrammarAttribution(record) {
  const id = String(record?.id ?? "");
  if (record?.targetConfidence === "verified") return true;
  if (
    id.startsWith("ex.cloze.e11.") ||
    id.startsWith("ex.transformation.e11.") ||
    id.startsWith("err.e11.")
  ) {
    // Only curated E05/E06 grammar sources carry true grammatical topic attribution;
    // E11 generated expansions use CEFR round-robin assignment on Tatoeba sentences.
    const src = String(record?.sourceSentenceIds?.[0] ?? record?.provenance?.sources?.[0]?.sourceId ?? "");
    return src.startsWith("sent.gr");
  }
  return true;
}

function firstGrammarForm(record) {
  for (const key of ["positive", "negative", "question"]) {
    const values = record?.forms?.[key];
    if (Array.isArray(values)) {
      const found = values.find((value) => typeof value === "string" && value.trim() !== "");
      if (found !== undefined) return found;
    }
  }
  return "";
}

function answerLengthForActivity(activity, record) {
  if (activity === "vocabulary") return String(record?.en ?? record?.headword ?? "").trim().length;
  if (activity === "collocation" || activity === "phrasal-verb" || activity === "chunk" || activity === "idiom") {
    return String(record?.text ?? "").trim().length;
  }
  if (activity === "verb-pattern") {
    return (String(record?.lemma ?? "").trim() + " · " + String(record?.frame ?? "").trim()).length;
  }
  if (activity === "grammar-topic" || activity === "grammar-challenge") {
    if (typeof record?.id === "string" && record.id.startsWith("gr.")) {
      return firstGrammarForm(record).trim().length;
    }
    return String(record?.acceptedAnswers?.[0] ?? "").trim().length;
  }
  if (activity === "dialogue") {
    const turns = Array.isArray(record?.turns) ? record.turns : [];
    let maxTurn = 0;
    for (const turn of turns) {
      const len = String(turn?.text ?? "").trim().length;
      if (len > maxTurn) maxTurn = len;
    }
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

function addEvidenceLink(evidenceMap, targetId, kind, refId) {
  if (typeof targetId !== "string" || targetId === "" || typeof refId !== "string" || refId === "") return;
  let entry = evidenceMap.get(targetId);
  if (!entry) {
    entry = {};
    evidenceMap.set(targetId, entry);
  }
  let set = entry[kind];
  if (!set) {
    set = new Set();
    entry[kind] = set;
  }
  set.add(refId);
}

async function readPublishedPacks(root, byIdMap) {
  const packDir = path.join(root, "content", "english", "packs");
  const files = await listJsonFiles(packDir);
  if (files.length === 0) return [];

  const schemaDir = path.join(root, "shared", "schemas", "english-content");
  const schemaNames = (await fs.readdir(schemaDir)).filter((n) => n.endsWith(".schema.json")).sort();
  const schemas = await Promise.all(schemaNames.map((n) => readJson(path.join(schemaDir, n))));
  const topicPackSchema = schemas.find((s) => s.$id?.endsWith("/topic-pack.schema.json"));
  if (!topicPackSchema) throw new Error("Missing topic-pack.schema.json");
  const { validate } = createSchemaValidator(schemas);

  const packs = [];
  const seenIds = new Set();
  for (const file of files) {
    const rel = path.relative(root, file);
    const pack = await readJson(file);
    const problems = validate(pack, topicPackSchema);
    if (problems.length > 0) {
      throw new Error(`${rel} failed topic-pack schema validation: ${problems.join("; ")}`);
    }
    if (seenIds.has(pack.id)) {
      throw new Error(`Duplicate topic pack id: ${pack.id}`);
    }
    seenIds.add(pack.id);
    if (pack?.quality?.state !== "published") continue;

    for (const [idx, item] of pack.items.entries()) {
      if (!byIdMap.has(item.contentId)) {
        throw new Error(`${rel}#items[${idx}]: unresolved published contentId ${item.contentId}`);
      }
    }
    packs.push(pack);
  }
  return packs.sort((a, b) => a.id.localeCompare(b.id, "en"));
}

export async function generateEnglishContentIndexes(root) {
  const manifests = {};
  const manifestRawStrings = [];
  for (const ds of DATASETS) {
    const manifestPath = path.join(root, "shared", ds, "manifest.json");
    const raw = await fs.readFile(manifestPath, "utf8");
    const parsed = JSON.parse(raw);
    manifests[ds] = parsed;
    manifestRawStrings.push(`${ds}:${parsed.contentVersion}:${parsed.count}:${parsed.shards.length}`);
  }

  const versions = new Set(Object.values(manifests).map((m) => m.contentVersion));
  if (versions.size !== 1) {
    throw new Error("Dataset manifests have mismatched contentVersions: " + [...versions].join(", "));
  }
  const contentVersion = [...versions][0];

  const byIdBuckets = Array.from({ length: 256 }, () => ({}));
  const byIdFlat = new Map();
  const evidenceMap = new Map();

  // Group activity specs by (dataset, prefix) so we inspect every shard in a single disk read pass
  const activityList = Object.keys(ENGLISH_ACTIVITY_SOURCES).sort((a, b) => a.localeCompare(b, "en"));
  const activityShards = Object.fromEntries(activityList.map((a) => [a, []]));
  const activitySeenIds = Object.fromEntries(activityList.map((a) => [a, new Set()]));
  const activityStats = Object.fromEntries(
    activityList.map((a) => [a, { total: 0, byCefr: {}, within200: 0, within240: 0, curatedTargets: 0 }]),
  );

  const shardSpecsByDataset = {};
  for (const activity of activityList) {
    for (const spec of ENGLISH_ACTIVITY_SOURCES[activity]) {
      (shardSpecsByDataset[spec.dataset] ??= []).push({ activity, prefix: spec.prefix, type: spec.type });
    }
  }

  const totals = { records: 0, dictionary: 0, grammar: 0, sentences: 0, phrases: 0 };

  for (const ds of DATASETS) {
    const manifest = manifests[ds];
    const datasetSpecs = shardSpecsByDataset[ds] ?? [];

    for (const shard of manifest.shards ?? []) {
      const shardDoc = await readJson(path.join(root, "shared", ds, shard.path));
      const records = Array.isArray(shardDoc.records) ? shardDoc.records : [];
      const matchingSpecs = datasetSpecs.filter((s) => String(shard.id).startsWith(s.prefix));

      // Per-activity accumulator for this single shard
      const perActShard = new Map();

      for (let offset = 0; offset < records.length; offset++) {
        const record = records[offset];
        if (!record || record?.quality?.state !== "published") continue;

        const id = recordIdOf(record);
        if (id) {
          if (byIdFlat.has(id)) {
            throw new Error(`Duplicate published record id in runtime: ${id}`);
          }
          const loc = [ds, shard.path, offset];
          byIdFlat.set(id, loc);
          byIdBuckets[parseInt(indexBucketHex(id), 16)][id] = loc;
          totals.records++;
          totals[ds]++;
        }

        // Accumulate verified evidence graph
        if (ds === "dictionary") {
          if (id?.startsWith("sense.") && typeof record.lexemeId === "string") {
            addEvidenceLink(evidenceMap, record.lexemeId, "senseIds", id);
            for (const exId of record.exampleIds ?? []) {
              addEvidenceLink(evidenceMap, id, "exampleIds", exId);
              addEvidenceLink(evidenceMap, record.lexemeId, "exampleIds", exId);
            }
          } else if (id?.startsWith("usage.") && typeof record.targetId === "string") {
            addEvidenceLink(evidenceMap, record.targetId, "usageIds", id);
            for (const exId of record.exampleIds ?? []) {
              addEvidenceLink(evidenceMap, record.targetId, "exampleIds", exId);
            }
          }
        } else if (ds === "grammar" && id?.startsWith("gr.")) {
          for (const exId of record.exampleIds ?? []) addEvidenceLink(evidenceMap, id, "exampleIds", exId);
          for (const excId of record.exerciseIds ?? []) addEvidenceLink(evidenceMap, id, "exerciseIds", excId);
        } else if (ds === "phrases" && id) {
          for (const exId of record.exampleIds ?? []) {
            addEvidenceLink(evidenceMap, id, "exampleIds", exId);
            addEvidenceLink(evidenceMap, exId, "phraseIds", id);
          }
        } else if (ds === "sentences" && id) {
          if (shard.id.startsWith("examples-")) {
            for (const gId of record.grammarIds ?? []) addEvidenceLink(evidenceMap, gId, "exampleIds", id);
            for (const lId of record.lexicalIds ?? []) addEvidenceLink(evidenceMap, lId, "exampleIds", id);
          } else if (shard.id.startsWith("exercises-")) {
            for (const sId of record.sourceSentenceIds ?? []) addEvidenceLink(evidenceMap, sId, "exerciseIds", id);
            const verified = isVerifiedGrammarAttribution(record);
            for (const tId of record.targetIds ?? []) {
              if (!verified && tId.startsWith("gr.")) continue;
              addEvidenceLink(evidenceMap, tId, "exerciseIds", id);
            }
          } else if (shard.id.startsWith("mistakes-")) {
            const verified = isVerifiedGrammarAttribution(record);
            for (const tId of record.targetIds ?? []) {
              if (!verified && tId.startsWith("gr.")) continue;
              addEvidenceLink(evidenceMap, tId, "mistakeIds", id);
            }
          }
        }

        // Accumulate activity shard stats
        for (const spec of matchingSpecs) {
          if (spec.type !== undefined && record?.type !== spec.type) continue;
          const seen = activitySeenIds[spec.activity];
          const dedupKey = id ?? JSON.stringify(record);
          if (seen.has(dedupKey)) continue;
          seen.add(dedupKey);

          const len = answerLengthForActivity(spec.activity, record);
          const cefr = typeof record.cefr === "string" && record.cefr !== "" ? record.cefr : "unknown";
          const verified = isVerifiedGrammarAttribution(record);

          const globalStat = activityStats[spec.activity];
          globalStat.total++;
          globalStat.byCefr[cefr] = (globalStat.byCefr[cefr] ?? 0) + 1;
          if (len <= 200) globalStat.within200++;
          if (len <= 240) globalStat.within240++;
          if (verified) globalStat.curatedTargets++;

          let shardAcc = perActShard.get(spec.activity);
          if (!shardAcc) {
            shardAcc = {
              dataset: ds,
              shardId: shard.id,
              path: shard.path,
              count: shard.count,
              matchedCount: 0,
              byCefr: {},
              minLen: Number.POSITIVE_INFINITY,
              maxLen: 0,
              within200Count: 0,
              within240Count: 0,
              curatedTargetCount: 0,
            };
            perActShard.set(spec.activity, shardAcc);
          }
          shardAcc.matchedCount++;
          shardAcc.byCefr[cefr] = (shardAcc.byCefr[cefr] ?? 0) + 1;
          if (len < shardAcc.minLen) shardAcc.minLen = len;
          if (len > shardAcc.maxLen) shardAcc.maxLen = len;
          if (len <= 200) shardAcc.within200Count++;
          if (len <= 240) shardAcc.within240Count++;
          if (verified) shardAcc.curatedTargetCount++;
        }
      }

      for (const [act, shardAcc] of perActShard.entries()) {
        if (shardAcc.matchedCount > 0) {
          activityShards[act].push({
            ...shardAcc,
            minLen: Number.isFinite(shardAcc.minLen) ? shardAcc.minLen : 0,
          });
        }
      }
    }
  }

  // Read & validate E14 lexical sense pilot (additive v2 sidecar) if present
  let e14Pilot = null;
  try {
    e14Pilot = await readJson(path.join(root, "content", "english", "dictionary", "e14-sense-pilot.json"));
    for (const entry of e14Pilot?.entries ?? []) {
      for (const sense of entry.senses ?? []) {
        addEvidenceLink(evidenceMap, entry.id, "senseIds", sense.id);
        for (const exId of sense.exampleIds ?? []) {
          addEvidenceLink(evidenceMap, entry.id, "exampleIds", exId);
          addEvidenceLink(evidenceMap, sense.id, "exampleIds", exId);
        }
      }
      if (entry.e03LexemeId) {
        for (const s of entry.senses ?? []) {
          addEvidenceLink(evidenceMap, entry.e03LexemeId, "senseIds", s.id);
          for (const exId of s.exampleIds ?? []) addEvidenceLink(evidenceMap, entry.e03LexemeId, "exampleIds", exId);
        }
      }
    }
  } catch {
    e14Pilot = null;
  }

  // Read & validate Topic Packs against published byId index
  const packs = await readPublishedPacks(root, byIdFlat);
  for (const pack of packs) {
    for (const item of pack.items) {
      addEvidenceLink(evidenceMap, item.contentId, "packIds", pack.id);
    }
  }

  // Distribute evidence map into 256 deterministic buckets
  const evidenceBuckets = Array.from({ length: 256 }, () => ({}));
  const sortedEvidenceKeys = [...evidenceMap.keys()].sort((a, b) => a.localeCompare(b, "en"));
  for (const targetId of sortedEvidenceKeys) {
    const rawEntry = evidenceMap.get(targetId);
    const normalized = {};
    for (const kind of Object.keys(rawEntry).sort()) {
      normalized[kind] = [...rawEntry[kind]].sort((a, b) => a.localeCompare(b, "en"));
    }
    evidenceBuckets[parseInt(indexBucketHex(targetId), 16)][targetId] = normalized;
  }

  const indexRoot = path.join(root, "shared", "indexes");
  const byIdDir = path.join(indexRoot, "by-id");
  const evidenceDir = path.join(indexRoot, "evidence");
  const activitiesDir = path.join(indexRoot, "activities");
  const packsDir = path.join(indexRoot, "packs");
  const lexicalDir = path.join(indexRoot, "lexical");

  await fs.rm(indexRoot, { recursive: true, force: true });
  await Promise.all([
    fs.mkdir(byIdDir, { recursive: true }),
    fs.mkdir(evidenceDir, { recursive: true }),
    fs.mkdir(activitiesDir, { recursive: true }),
    fs.mkdir(packsDir, { recursive: true }),
    fs.mkdir(lexicalDir, { recursive: true }),
  ]);

  if (e14Pilot !== null) {
    await fs.writeFile(
      path.join(lexicalDir, "e14-pilot.json"),
      compactJson({ schemaVersion: 1, contentVersion, ...e14Pilot }),
      "utf8",
    );
  }

  // Write 256 by-id & evidence buckets deterministically
  for (let b = 0; b < 256; b++) {
    const hex = b.toString(16).padStart(2, "0");
    const sortedById = {};
    for (const k of Object.keys(byIdBuckets[b]).sort((x, y) => x.localeCompare(y, "en"))) {
      sortedById[k] = byIdBuckets[b][k];
    }
    await fs.writeFile(
      path.join(byIdDir, `${hex}.json`),
      compactJson({ schemaVersion: 1, contentVersion, bucket: hex, entries: sortedById }),
      "utf8",
    );
    await fs.writeFile(
      path.join(evidenceDir, `${hex}.json`),
      compactJson({ schemaVersion: 1, contentVersion, bucket: hex, entries: evidenceBuckets[b] }),
      "utf8",
    );
  }

  // Write per-activity shard manifests
  for (const act of activityList) {
    await fs.writeFile(
      path.join(activitiesDir, `${act}.json`),
      compactJson({
        schemaVersion: 1,
        contentVersion,
        activity: act,
        total: activityStats[act].total,
        byCefr: activityStats[act].byCefr,
        shards: activityShards[act],
      }),
      "utf8",
    );
  }

  // Write availability.json
  const availability = {
    schemaVersion: 1,
    contentVersion,
    activities: activityStats,
  };
  await fs.writeFile(path.join(indexRoot, "availability.json"), stableJson(availability), "utf8");

  // Write packs manifest & pack files
  const packSummaries = [];
  for (const pack of packs) {
    const file = `${pack.id}.json`;
    await fs.writeFile(path.join(packsDir, file), stableJson({ schemaVersion: 1, contentVersion, pack }), "utf8");
    packSummaries.push({
      id: pack.id,
      title: pack.title,
      titleVi: pack.titleVi,
      description: pack.description,
      cefr: pack.cefr,
      estimatedMinutes: pack.estimatedMinutes ?? 10,
      itemCount: pack.items.length,
      path: file,
    });
  }
  await fs.writeFile(
    path.join(packsDir, "manifest.json"),
    stableJson({ schemaVersion: 1, contentVersion, count: packSummaries.length, packs: packSummaries }),
    "utf8",
  );

  // Compute deterministic releaseDigest
  const releaseDigest = crypto
    .createHash("sha256")
    .update(
      manifestRawStrings.join("|") + "|packs:" + packSummaries.map((p) => p.id + ":" + p.itemCount).join(","),
      "utf8",
    )
    .digest("hex");

  const indexManifest = {
    schemaVersion: 1,
    contentVersion,
    releaseDigest,
    bucketCount: 256,
    totals: {
      ...totals,
      evidenceTargets: sortedEvidenceKeys.length,
      packs: packSummaries.length,
      e14LexicalPilotEntries: e14Pilot?.entries?.length ?? 0,
    },
    activities: activityList,
    availabilityPath: "availability.json",
    packsPath: "packs/manifest.json",
  };
  await fs.writeFile(path.join(indexRoot, "manifest.json"), stableJson(indexManifest), "utf8");

  return indexManifest;
}
