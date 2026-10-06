import fs from "node:fs/promises";
import path from "node:path";
import { readJson } from "./english-content-core.mjs";

const DEFAULT_LEDGER_DIR = path.join("content", "english", "reviews", "enrichment-links.d");

function requireText(value, label) {
  if (typeof value !== "string" || value.trim() === "") {
    throw new TypeError(label + " must be a non-empty string");
  }
}

function recordId(record) {
  return String(record?.id ?? record?.lexemeId ?? "");
}

function validateTargetSnapshot(link) {
  const snapshot = link.targetSnapshot;
  if (snapshot === null || typeof snapshot !== "object" || Array.isArray(snapshot)) {
    throw new TypeError(link.id + ": targetSnapshot must be an object");
  }
  if (link.targetType === "verb-pattern") {
    requireText(snapshot.lemma, link.id + ".targetSnapshot.lemma");
    requireText(snapshot.frame, link.id + ".targetSnapshot.frame");
    return;
  }
  if (link.targetType === "collocation" || link.targetType === "phrase") {
    requireText(snapshot.text, link.id + ".targetSnapshot.text");
    return;
  }
  throw new TypeError(link.id + ": unsupported targetType " + String(link.targetType));
}

function targetSnapshotMatches(record, link) {
  if (link.targetType === "verb-pattern") {
    return record.lemma === link.targetSnapshot.lemma && record.frame === link.targetSnapshot.frame;
  }
  return record.text === link.targetSnapshot.text;
}

export async function readEnglishExampleLinkLedger(root, relativeDir = DEFAULT_LEDGER_DIR) {
  const dir = path.join(root, relativeDir);
  let entries;
  try {
    entries = await fs.readdir(dir, { withFileTypes: true });
  } catch (error) {
    if (error?.code === "ENOENT") return [];
    throw error;
  }

  const files = entries
    .filter(entry => entry.isFile() && entry.name.endsWith(".json"))
    .map(entry => entry.name)
    .sort((a, b) => a.localeCompare(b, "en"));

  const links = [];
  const seenIds = new Set();
  const seenPairs = new Set();

  for (const file of files) {
    const relative = path.join(relativeDir, file);
    const doc = await readJson(path.join(root, relative));
    if (doc?.schemaVersion !== 1) {
      throw new TypeError(relative + ": schemaVersion must be 1");
    }
    if (!Array.isArray(doc.links)) {
      throw new TypeError(relative + ": links[] is required");
    }

    for (const [index, link] of doc.links.entries()) {
      const label = relative + "#links[" + index + "]";
      requireText(link?.id, label + ".id");
      requireText(link?.targetType, label + ".targetType");
      requireText(link?.targetId, label + ".targetId");
      requireText(link?.exampleId, label + ".exampleId");
      requireText(link?.exampleText, label + ".exampleText");
      requireText(link?.evidence?.method, label + ".evidence.method");
      requireText(link?.reviewedBy, label + ".reviewedBy");
      requireText(link?.reviewedAt, label + ".reviewedAt");
      if (link?.evidence?.status !== "pass") {
        throw new TypeError(label + ".evidence.status must be pass");
      }
      validateTargetSnapshot(link);

      if (seenIds.has(link.id)) throw new Error("duplicate enrichment-link id: " + link.id);
      seenIds.add(link.id);

      const pair = link.targetType + "\u0000" + link.targetId + "\u0000" + link.exampleId;
      if (seenPairs.has(pair)) {
        throw new Error("duplicate enrichment target/example pair: " + link.targetId + " -> " + link.exampleId);
      }
      seenPairs.add(pair);
      links.push({ ...link, sourceFile: relative });
    }
  }

  return links;
}

export function applyEnglishExampleLinks(records, links, { targetType, examples }) {
  const output = records.map(record => structuredClone(record));
  const targets = new Map(output.map(record => [recordId(record), record]));
  const exampleById = new Map(examples.map(record => [recordId(record), record]));
  let applied = 0;

  for (const link of links) {
    if (link.targetType !== targetType) continue;

    const target = targets.get(link.targetId);
    if (!target) throw new Error(link.id + ": target does not exist: " + link.targetId);
    if (target?.quality?.state !== "published") {
      throw new Error(link.id + ": target is not currently review-published: " + link.targetId);
    }
    if (!targetSnapshotMatches(target, link)) {
      throw new Error(link.id + ": target snapshot drifted; re-review this example link");
    }

    const example = exampleById.get(link.exampleId);
    if (!example) throw new Error(link.id + ": published example does not exist: " + link.exampleId);
    if (example?.quality?.state !== "published") {
      throw new Error(link.id + ": example is not published: " + link.exampleId);
    }
    if (example.text !== link.exampleText) {
      throw new Error(link.id + ": example text drifted; re-review this example link");
    }

    const current = Array.isArray(target.exampleIds) ? [...target.exampleIds] : [];
    if (!current.includes(link.exampleId)) {
      current.push(link.exampleId);
      target.exampleIds = current;
      applied += 1;
    }
  }

  return { records: output, applied };
}
