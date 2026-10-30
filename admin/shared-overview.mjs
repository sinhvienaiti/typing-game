import { readFile } from "node:fs/promises";
import { resolve } from "node:path";

const CONSUMERS_PATH = "admin/typing-feel/consumers.json";
const CATALOGUE_PATH = "typing-feel/public/v1/keys/keys-manifest.json";

// File problems come back as data so one bad file never turns the whole overview into a 500.
async function readJson(rootDir, path) {
  try {
    return { value: JSON.parse(await readFile(resolve(rootDir, path), "utf8")) };
  } catch (error) {
    return { error };
  }
}

function problem(status, error) {
  return { status, message: error instanceof Error ? error.message : String(error) };
}

async function readConsumers(rootDir) {
  const { value, error } = await readJson(rootDir, CONSUMERS_PATH);
  if (error) return { consumers: [], consumersError: problem(error.code === "ENOENT" ? "missing" : "invalid", error) };
  if (!Array.isArray(value)) return { consumers: [], consumersError: problem("invalid", `${CONSUMERS_PATH} must be a JSON array.`) };
  return { consumers: value, consumersError: null };
}

// null: not imported yet (no manifest). { status: "invalid" }: present but unreadable.
async function readCatalogue(rootDir) {
  const { value, error } = await readJson(rootDir, CATALOGUE_PATH);
  if (error) return error.code === "ENOENT" ? null : problem("invalid", error);
  if (!Array.isArray(value?.profiles)) return problem("invalid", "Typing Feel catalogue is missing profiles.");
  return { status: "imported", revision: value.revision ?? null, setCount: value.profiles.length };
}

export async function readSharedOverview({ rootDir, spaceAvailable, spaceStatus = spaceAvailable ? "available" : "not-checked-out" }) {
  const [consumers, catalogue] = await Promise.all([readConsumers(rootDir), readCatalogue(rootDir)]);
  return { ...consumers, catalogue, spaceAvailable, spaceStatus };
}
