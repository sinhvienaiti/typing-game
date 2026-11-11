import { indexBucketHex } from "./index-bucket.mjs";

const DEFAULT_BASE = "https://typing-game.local/english-content";
const DATASETS = Object.freeze(["dictionary", "grammar", "sentences", "phrases"]);
const DEFAULT_MAX_CACHED_SHARDS = 24;
const DEFAULT_MAX_CACHED_BUCKETS = 32;
const DEFAULT_MAX_CONCURRENCY = 4;

function cleanBase(value) {
  const trimmed = String(value || DEFAULT_BASE).replace(/\/+$/, "");
  return trimmed || DEFAULT_BASE;
}

function isObject(value) {
  return value !== null && typeof value === "object" && !Array.isArray(value);
}

class BoundedLruCache {
  #maxEntries;
  #map = new Map();

  constructor(maxEntries) {
    this.#maxEntries = Math.max(1, Number(maxEntries) || 1);
  }

  get(key) {
    if (!this.#map.has(key)) return undefined;
    const value = this.#map.get(key);
    this.#map.delete(key);
    this.#map.set(key, value);
    return value;
  }

  set(key, value) {
    if (this.#map.has(key)) {
      this.#map.delete(key);
    }
    this.#map.set(key, value);
    while (this.#map.size > this.#maxEntries) {
      const oldestKey = this.#map.keys().next().value;
      this.#map.delete(oldestKey);
    }
  }

  delete(key) {
    this.#map.delete(key);
  }

  clear() {
    this.#map.clear();
  }

  get size() {
    return this.#map.size;
  }
}

async function mapBounded(items, concurrency, fn) {
  const results = new Array(items.length);
  const limit = Math.max(1, Math.min(concurrency, items.length || 1));
  let cursor = 0;

  async function worker() {
    while (cursor < items.length) {
      const idx = cursor++;
      results[idx] = await fn(items[idx], idx);
    }
  }

  await Promise.all(Array.from({ length: limit }, worker));
  return results;
}

export function parseRuntimeManifest(value, expectedDataset) {
  if (
    !isObject(value) ||
    value.schemaVersion !== 1 ||
    value.dataset !== expectedDataset ||
    !Number.isInteger(value.count) ||
    value.count < 0 ||
    !Array.isArray(value.shards)
  ) {
    throw new TypeError("Invalid runtime manifest for " + expectedDataset);
  }
  const ids = new Set();
  const paths = new Set();
  let sum = 0;
  const shards = value.shards.map((shard) => {
    if (
      !isObject(shard) ||
      typeof shard.id !== "string" ||
      !shard.id ||
      typeof shard.path !== "string" ||
      !shard.path ||
      !Number.isInteger(shard.count) ||
      shard.count < 0
    ) {
      throw new TypeError("Invalid runtime shard for " + expectedDataset);
    }
    if (shard.bytes !== undefined && (!Number.isInteger(shard.bytes) || shard.bytes < 0)) {
      throw new TypeError("Invalid shard bytes in " + expectedDataset);
    }
    if (shard.sha256 !== undefined && (typeof shard.sha256 !== "string" || !/^[a-f0-9]{64}$/.test(shard.sha256))) {
      throw new TypeError("Invalid shard sha256 in " + expectedDataset);
    }
    if (ids.has(shard.id) || paths.has(shard.path)) {
      throw new TypeError("Duplicate runtime shard in " + expectedDataset);
    }
    ids.add(shard.id);
    paths.add(shard.path);
    sum += shard.count;
    return {
      id: shard.id,
      path: shard.path,
      count: shard.count,
      ...(shard.bytes === undefined ? {} : { bytes: shard.bytes }),
      ...(shard.sha256 === undefined ? {} : { sha256: shard.sha256 }),
    };
  });
  if (sum !== value.count) {
    throw new TypeError("Runtime manifest count mismatch for " + expectedDataset);
  }
  return {
    schemaVersion: 1,
    contentVersion: String(value.contentVersion),
    dataset: expectedDataset,
    count: value.count,
    shards,
  };
}

export function createEnglishRuntimeLoader(options = {}) {
  const fetcher = options.fetcher ?? fetch;
  const base = cleanBase(options.baseUrl);
  const maxCachedShards = Math.max(1, Number(options.maxCachedShards ?? DEFAULT_MAX_CACHED_SHARDS));
  const maxCachedBuckets = Math.max(1, Number(options.maxCachedBuckets ?? DEFAULT_MAX_CACHED_BUCKETS));
  const maxConcurrency = Math.max(1, Number(options.maxConcurrency ?? DEFAULT_MAX_CONCURRENCY));

  let pinnedContentVersion = options.pinnedContentVersion ? String(options.pinnedContentVersion) : null;
  const manifestCache = new Map();
  const shardCache = new BoundedLruCache(maxCachedShards);
  const bucketCache = new BoundedLruCache(maxCachedBuckets);
  const staticIndexCache = new Map();

  function assertPinnedVersion(actualVersion, label) {
    if (typeof actualVersion !== "string" || actualVersion === "") return;
    if (pinnedContentVersion === null) {
      pinnedContentVersion = actualVersion;
      return;
    }
    if (actualVersion !== pinnedContentVersion) {
      throw new TypeError(
        `English contentVersion drift on ${label}: pinned ${pinnedContentVersion}, got ${actualVersion}`,
      );
    }
  }

  async function json(relative) {
    const response = await fetcher(base + "/" + relative.replace(/^\/+/, ""), { cache: "no-store" });
    if (!response.ok) {
      const err = new Error("English runtime request failed: " + response.status + " " + relative);
      err.status = response.status;
      throw err;
    }
    return response.json();
  }

  async function optionalIndexJson(relative) {
    try {
      const value = await json(relative);
      if (!isObject(value) || value.schemaVersion !== 1) return null;
      if (typeof value.contentVersion === "string") {
        assertPinnedVersion(value.contentVersion, relative);
      }
      return value;
    } catch (error) {
      if (error instanceof TypeError && error.message.includes("contentVersion drift")) {
        throw error;
      }
      return null;
    }
  }

  async function loadManifest(dataset) {
    if (!DATASETS.includes(dataset)) {
      throw new TypeError("Unsupported English runtime dataset: " + dataset);
    }
    let pending = manifestCache.get(dataset);
    if (!pending) {
      pending = json(dataset + "/manifest.json").then((value) => {
        const parsed = parseRuntimeManifest(value, dataset);
        assertPinnedVersion(parsed.contentVersion, dataset + "/manifest.json");
        return parsed;
      });
      manifestCache.set(dataset, pending);
    }
    try {
      return await pending;
    } catch (error) {
      if (manifestCache.get(dataset) === pending) manifestCache.delete(dataset);
      throw error;
    }
  }

  async function loadShard(dataset, shard) {
    const key = dataset + ":" + shard.path;
    let pending = shardCache.get(key);
    if (!pending) {
      pending = json(dataset + "/" + shard.path).then((value) => {
        if (!isObject(value) || value.schemaVersion !== 1 || !Array.isArray(value.records) || value.records.length !== shard.count) {
          throw new TypeError("Invalid English runtime shard: " + key);
        }
        return value.records;
      });
      shardCache.set(key, pending);
    }
    try {
      return await pending;
    } catch (error) {
      shardCache.delete(key);
      throw error;
    }
  }

  async function loadShardByPath(dataset, shardPath) {
    const manifest = await loadManifest(dataset);
    const shard = manifest.shards.find((s) => s.path === shardPath);
    if (!shard) throw new TypeError(`Runtime shard not found in ${dataset}: ${shardPath}`);
    return loadShard(dataset, shard);
  }

  async function loadDataset(dataset, { prefix } = {}) {
    const manifest = await loadManifest(dataset);
    const shards = prefix ? manifest.shards.filter((shard) => shard.id.startsWith(prefix)) : manifest.shards;
    const groups = await mapBounded(shards, maxConcurrency, (shard) => loadShard(dataset, shard));
    return groups.flat();
  }

  async function loadCachedStaticIndex(key, relative) {
    let pending = staticIndexCache.get(key);
    if (!pending) {
      pending = optionalIndexJson(relative);
      staticIndexCache.set(key, pending);
    }
    const res = await pending;
    if (res === null && staticIndexCache.get(key) === pending) {
      staticIndexCache.delete(key);
    }
    return res;
  }

  async function loadIndexManifest() {
    return loadCachedStaticIndex("manifest", "indexes/manifest.json");
  }

  async function loadAvailability() {
    return loadCachedStaticIndex("availability", "indexes/availability.json");
  }

  async function loadActivityIndex(activity) {
    return loadCachedStaticIndex("activity:" + activity, "indexes/activities/" + activity + ".json");
  }

  async function loadTopicPacksManifest() {
    return loadCachedStaticIndex("packs:manifest", "indexes/packs/manifest.json");
  }

  async function loadTopicPack(packId) {
    const cleanId = String(packId ?? "").trim();
    if (!cleanId) return null;
    const doc = await optionalIndexJson(`indexes/packs/${cleanId}.json`);
    return doc?.pack ?? null;
  }

  async function loadLexicalPilot() {
    return loadCachedStaticIndex("lexical:e14-pilot", "indexes/lexical/e14-pilot.json");
  }

  async function loadBucket(kind, hex) {
    const key = kind + ":" + hex;
    let pending = bucketCache.get(key);
    if (!pending) {
      pending = optionalIndexJson(`indexes/${kind}/${hex}.json`);
      bucketCache.set(key, pending);
    }
    const res = await pending;
    if (res === null) {
      bucketCache.delete(key);
    }
    return res;
  }

  async function resolvePublishedByIds(ids) {
    const uniqueIds = [...new Set((ids ?? []).map((id) => String(id ?? "").trim()).filter(Boolean))];
    const recordsById = new Map();
    if (uniqueIds.length === 0) {
      return { recordsById, missingIds: [], contentVersion: pinnedContentVersion, usedIndex: true };
    }

    const bucketIds = [...new Set(uniqueIds.map((id) => indexBucketHex(id)))];
    const buckets = await mapBounded(bucketIds, maxConcurrency, (hex) => loadBucket("by-id", hex));
    if (buckets.every((b) => b === null) && (await loadIndexManifest()) === null) {
      return { recordsById, missingIds: uniqueIds, contentVersion: pinnedContentVersion, usedIndex: false };
    }

    const bucketMap = new Map(bucketIds.map((hex, i) => [hex, buckets[i]]));
    const shardRequests = new Map();
    const missingIds = [];

    for (const id of uniqueIds) {
      const bucket = bucketMap.get(indexBucketHex(id));
      const loc = bucket?.entries?.[id];
      if (!Array.isArray(loc) || loc.length < 3) {
        missingIds.push(id);
        continue;
      }
      const [dataset, shardPath, offset] = loc;
      const shardKey = dataset + ":" + shardPath;
      let list = shardRequests.get(shardKey);
      if (!list) {
        list = { dataset, shardPath, targets: [] };
        shardRequests.set(shardKey, list);
      }
      list.targets.push({ id, offset });
    }

    await mapBounded([...shardRequests.values()], maxConcurrency, async ({ dataset, shardPath, targets }) => {
      const records = await loadShardByPath(dataset, shardPath);
      for (const { id, offset } of targets) {
        let record = records[offset];
        if (!record || (record.id ?? record.lexemeId) !== id) {
          record = records.find((r) => (r?.id ?? r?.lexemeId) === id);
        }
        if (record) {
          recordsById.set(id, record);
        } else {
          missingIds.push(id);
        }
      }
    });

    return { recordsById, missingIds, contentVersion: pinnedContentVersion, usedIndex: true };
  }

  async function findById(dataset, id) {
    if (!DATASETS.includes(dataset)) {
      throw new TypeError("Unsupported English runtime dataset: " + dataset);
    }
    const cleanId = String(id ?? "").trim();
    if (!cleanId) return null;

    // 1. Try O(1) bucketed index lookup first
    const hex = indexBucketHex(cleanId);
    const bucket = await loadBucket("by-id", hex);
    if (bucket !== null) {
      const loc = bucket.entries?.[cleanId];
      if (!Array.isArray(loc) || loc[0] !== dataset) return null;
      const records = await loadShardByPath(loc[0], loc[1]);
      const rec = records[loc[2]];
      if (rec && (rec.id ?? rec.lexemeId) === cleanId) return rec;
      return records.find((r) => (r?.id ?? r?.lexemeId) === cleanId) ?? null;
    }

    // 2. Fallback: scan shards sequentially & stop immediately on first match
    const manifest = await loadManifest(dataset);
    for (const shard of manifest.shards) {
      const records = await loadShard(dataset, shard);
      const found = records.find((record) => (record?.id ?? record?.lexemeId) === cleanId);
      if (found) return found;
    }
    return null;
  }

  async function getEvidence(targetId, filters = {}) {
    const cleanTarget = String(targetId ?? "").trim();
    if (!cleanTarget) return { targetId: cleanTarget, refs: {}, records: [] };

    const hex = indexBucketHex(cleanTarget);
    const bucket = await loadBucket("evidence", hex);
    const entry = bucket?.entries?.[cleanTarget];
    if (!entry) return { targetId: cleanTarget, refs: {}, records: [] };

    const wantedKinds = Array.isArray(filters.kinds) && filters.kinds.length > 0
      ? filters.kinds
      : ["exampleIds", "usageIds", "senseIds", "exerciseIds", "mistakeIds", "phraseIds", "packIds"];
    const limit = Math.max(1, Math.min(100, Number(filters.limit ?? 10)));

    const candidateIds = [];
    for (const kind of wantedKinds) {
      for (const refId of entry[kind] ?? []) {
        if (typeof refId === "string" && !candidateIds.includes(refId) && !refId.startsWith("pack.")) {
          candidateIds.push(refId);
        }
      }
    }
    if (candidateIds.length === 0) {
      return { targetId: cleanTarget, refs: entry, records: [] };
    }

    // Resolve bounded window first; expand if CEFR filter rejects some
    const batchIds = filters.cefr ? candidateIds.slice(0, Math.min(candidateIds.length, limit * 5)) : candidateIds.slice(0, limit);
    const { recordsById } = await resolvePublishedByIds(batchIds);
    const resolved = [];
    for (const refId of batchIds) {
      const rec = recordsById.get(refId);
      if (!rec) continue;
      if (filters.cefr && rec.cefr && rec.cefr !== filters.cefr) continue;
      resolved.push(rec);
      if (resolved.length >= limit) break;
    }
    return { targetId: cleanTarget, refs: entry, records: resolved };
  }

  function getPinnedContentVersion() {
    return pinnedContentVersion;
  }

  function clear() {
    manifestCache.clear();
    shardCache.clear();
    bucketCache.clear();
    staticIndexCache.clear();
    pinnedContentVersion = options.pinnedContentVersion ? String(options.pinnedContentVersion) : null;
  }

  return {
    loadManifest,
    loadShard,
    loadDataset,
    findById,
    resolvePublishedByIds,
    getEvidence,
    loadIndexManifest,
    loadAvailability,
    loadActivityIndex,
    loadTopicPacksManifest,
    loadTopicPack,
    loadLexicalPilot,
    getPinnedContentVersion,
    clear,
  };
}
