// Pure edits of a typing-feel-admin/1 working copy (docs/games/TYPING_FEEL_SERVICE.md §3.4, §3.7).
// Every edit returns a new config and only touches the local working copy; the
// server checks everything again on Save draft and Publish. No DOM, no imports
// besides types: portal/tests/typing-feel-draft-model.test.mjs runs it in Node.
import type { TypingFeelConfig, TypingFeelFamily, TypingFeelSet } from "./types";

export type EditResult = { config: TypingFeelConfig; error: null } | { config: null; error: string };

const ok = (config: TypingFeelConfig): EditResult => ({ config, error: null });
const fail = (error: string): EditResult => ({ config: null, error });

export function cloneConfig(config: TypingFeelConfig): TypingFeelConfig {
  return JSON.parse(JSON.stringify(config)) as TypingFeelConfig;
}

/** JSON with sorted keys, so two configs compare by content, not by key order. */
export function canonicalJson(value: unknown): string {
  const sort = (input: unknown): unknown => {
    if (Array.isArray(input)) return input.map(sort);
    if (input !== null && typeof input === "object") {
      return Object.fromEntries(Object.keys(input as Record<string, unknown>).sort().map((key) => [key, sort((input as Record<string, unknown>)[key])]));
    }
    return input;
  };
  return JSON.stringify(sort(value));
}

export function sameConfig(left: TypingFeelConfig | null, right: TypingFeelConfig | null): boolean {
  return canonicalJson(left) === canonicalJson(right);
}

export function orderedFamilies(config: TypingFeelConfig): TypingFeelFamily[] {
  return [...config.keyboard.families].sort((a, b) => a.order - b.order || a.id.localeCompare(b.id));
}

/** The family's sets in their order (shown and hidden). */
export function familySets(config: TypingFeelConfig, familyId: string): TypingFeelSet[] {
  return config.keyboard.sets.filter((set) => set.family === familyId).sort((a, b) => a.order - b.order || a.id.localeCompare(b.id));
}

/** Shown set ids in the order the exported catalogue lists them (family order, then set order). */
export function catalogueOrder(config: TypingFeelConfig): string[] {
  return orderedFamilies(config).flatMap((family) => familySets(config, family.id).filter((set) => set.enabled).map((set) => set.id));
}

function findSet(config: TypingFeelConfig, setId: string): TypingFeelSet | undefined {
  return config.keyboard.sets.find((set) => set.id === setId);
}

/** Renumbers one family's sets 0, 1, 2… in the given order. */
function renumber(sets: TypingFeelSet[]): void {
  sets.forEach((set, index) => {
    set.order = index;
  });
}

/** Moves a set one place up (-1) or down (+1) inside its family. */
export function moveSet(config: TypingFeelConfig, setId: string, delta: -1 | 1): EditResult {
  const next = cloneConfig(config);
  const set = findSet(next, setId);
  if (!set) return fail(`Set ${setId} is not in this draft.`);
  const list = familySets(next, set.family);
  const from = list.indexOf(set);
  const to = from + delta;
  if (to < 0 || to >= list.length) return fail(delta < 0 ? `${set.name} is already first in its family.` : `${set.name} is already last in its family.`);
  list.splice(from, 1);
  list.splice(to, 0, set);
  renumber(list);
  return ok(next);
}

/**
 * Puts a set into `familyId` at `index` (counted without the set itself), the
 * way a drag and drop or the Family menu does. `index` past the end appends.
 */
export function placeSet(config: TypingFeelConfig, setId: string, familyId: string, index: number): EditResult {
  const next = cloneConfig(config);
  const set = findSet(next, setId);
  if (!set) return fail(`Set ${setId} is not in this draft.`);
  if (!next.keyboard.families.some((family) => family.id === familyId)) return fail(`Family ${familyId} is not in this draft.`);
  const source = familySets(next, set.family).filter((entry) => entry !== set);
  renumber(source);
  const target = familySets(next, familyId).filter((entry) => entry !== set);
  const at = Math.max(0, Math.min(Number.isFinite(index) ? Math.trunc(index) : target.length, target.length));
  target.splice(at, 0, set);
  set.family = familyId;
  renumber(target);
  return ok(next);
}

/**
 * Where a set dropped on `targetSetId` lands: it takes the target's place.
 * Dragged down inside one family it goes after the target, otherwise before it.
 */
export function dropOnSet(config: TypingFeelConfig, setId: string, targetSetId: string): EditResult {
  if (setId === targetSetId) return ok(cloneConfig(config));
  const set = findSet(config, setId);
  const target = findSet(config, targetSetId);
  if (!set || !target) return fail("That set is not in this draft.");
  const list = familySets(config, target.family);
  const without = list.filter((entry) => entry.id !== setId);
  let index = without.findIndex((entry) => entry.id === targetSetId);
  if (set.family === target.family && list.indexOf(set) < list.indexOf(target)) index += 1;
  return placeSet(config, setId, target.family, index);
}

export function setShown(config: TypingFeelConfig, setId: string, enabled: boolean): EditResult {
  const next = cloneConfig(config);
  const set = findSet(next, setId);
  if (!set) return fail(`Set ${setId} is not in this draft.`);
  if (!enabled && next.keyboard.defaultSet === setId) return fail(`${set.name} is the default set. Choose another default before hiding it.`);
  if (!enabled && next.keyboard.sets.filter((entry) => entry.enabled).length <= 1) return fail("At least one set must stay shown.");
  set.enabled = enabled;
  return ok(next);
}

export function setDefault(config: TypingFeelConfig, setId: string): EditResult {
  const next = cloneConfig(config);
  const set = findSet(next, setId);
  if (!set) return fail(`Set ${setId} is not in this draft.`);
  if (!set.enabled) return fail(`${set.name} is hidden. Show it before making it the default.`);
  if (set.status === "provisional") return fail(`${set.name} is provisional. A provisional set cannot be the default.`);
  next.keyboard.defaultSet = setId;
  return ok(next);
}

function cleanName(raw: string, max: number, what: string): { name: string; error: null } | { name: null; error: string } {
  const name = raw.replace(/\s+/g, " ").trim();
  if (!name) return { name: null, error: `${what} cannot be empty.` };
  if (name.length > max) return { name: null, error: `${what} can have at most ${max} characters.` };
  if (/[\u0000-\u001f\u007f]/.test(name)) return { name: null, error: `${what} cannot contain control characters.` };
  return { name, error: null };
}

/** Changes the display name only; the id stays, because player saves store it. */
export function renameSet(config: TypingFeelConfig, setId: string, rawName: string, max = 60): EditResult {
  const next = cloneConfig(config);
  const set = findSet(next, setId);
  if (!set) return fail(`Set ${setId} is not in this draft.`);
  const cleaned = cleanName(rawName, max, "The set name");
  if (cleaned.error !== null) return fail(cleaned.error);
  set.name = cleaned.name;
  return ok(next);
}

export function renameFamily(config: TypingFeelConfig, familyId: string, rawName: string, max = 40): EditResult {
  const next = cloneConfig(config);
  const family = next.keyboard.families.find((entry) => entry.id === familyId);
  if (!family) return fail(`Family ${familyId} is not in this draft.`);
  const cleaned = cleanName(rawName, max, "The family name");
  if (cleaned.error !== null) return fail(cleaned.error);
  if (next.keyboard.families.some((entry) => entry.id !== familyId && entry.name.toLowerCase() === cleaned.name.toLowerCase())) {
    return fail(`Another family is already called ${cleaned.name}. The games group sets by family name.`);
  }
  family.name = cleaned.name;
  return ok(next);
}

/** Moves a family one place up or down; family orders become 0, 1, 2… */
export function moveFamily(config: TypingFeelConfig, familyId: string, delta: -1 | 1): EditResult {
  const next = cloneConfig(config);
  const list = orderedFamilies(next);
  const from = list.findIndex((family) => family.id === familyId);
  if (from < 0) return fail(`Family ${familyId} is not in this draft.`);
  const to = from + delta;
  if (to < 0 || to >= list.length) return fail(delta < 0 ? "This family is already first." : "This family is already last.");
  const [family] = list.splice(from, 1);
  list.splice(to, 0, family);
  list.forEach((entry, index) => {
    entry.order = index;
  });
  return ok(next);
}

/** A family id from its name: lower case, a-z 0-9 and dashes, unique, never a reserved id. */
export function familyIdFor(config: TypingFeelConfig, name: string, idPattern = "^[a-z0-9][a-z0-9-]{0,31}$", reserved: readonly string[] = ["off"]): string | null {
  const base = name.toLowerCase().normalize("NFKD").replace(/[̀-ͯ]/g, "").replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "").slice(0, 28).replace(/-+$/g, "");
  if (!base) return null;
  const pattern = new RegExp(idPattern);
  const taken = new Set([...config.keyboard.families.map((family) => family.id), ...reserved]);
  for (let suffix = 1; suffix < 100; suffix += 1) {
    const candidate = suffix === 1 ? base : `${base}-${suffix}`;
    if (!taken.has(candidate) && pattern.test(candidate)) return candidate;
  }
  return null;
}

/** Adds an empty family at the end. Families with no shown set stay out of the games' catalogue. */
export function addFamily(config: TypingFeelConfig, rawName: string, options: { idPattern?: string; reserved?: readonly string[]; max?: number } = {}): EditResult {
  const cleaned = cleanName(rawName, options.max ?? 40, "The family name");
  if (cleaned.error !== null) return fail(cleaned.error);
  if (config.keyboard.families.some((family) => family.name.toLowerCase() === cleaned.name.toLowerCase())) return fail(`A family called ${cleaned.name} already exists.`);
  const id = familyIdFor(config, cleaned.name, options.idPattern, options.reserved);
  if (!id) return fail("Use letters or numbers in the family name.");
  const next = cloneConfig(config);
  const order = orderedFamilies(next).reduce((max, family) => Math.max(max, family.order + 1), 0);
  next.keyboard.families.push({ id, name: cleaned.name, order });
  return ok(next);
}

/** Retire: the row leaves the draft and its id goes to retiredIds, never to be used again (§3.4). */
export function retireSet(config: TypingFeelConfig, setId: string): EditResult {
  const next = cloneConfig(config);
  const set = findSet(next, setId);
  if (!set) return fail(`Set ${setId} is not in this draft.`);
  if (next.keyboard.defaultSet === setId) return fail(`${set.name} is the default set. Choose another default before retiring it.`);
  if (set.enabled && next.keyboard.sets.filter((entry) => entry.enabled).length <= 1) return fail("At least one set must stay shown.");
  next.keyboard.sets = next.keyboard.sets.filter((entry) => entry !== set);
  if (!next.keyboard.retiredIds.includes(setId)) next.keyboard.retiredIds.push(setId);
  renumber(familySets(next, set.family));
  return ok(next);
}

export type EffectField = "style" | "intensity" | "size" | "volume";

/** Volume is kept to two decimals inside 0 … 1; the other fields take the contract's ids. */
export function setEffectDefault(config: TypingFeelConfig, field: EffectField, value: string | number): TypingFeelConfig {
  const next = cloneConfig(config);
  if (field === "volume") next.effects.defaults.volume = Math.round(Math.max(0, Math.min(1, Number(value))) * 100) / 100;
  else next.effects.defaults[field] = String(value);
  return next;
}

/** Positions (in `sequence`) of one longest increasing run, the sets that kept their relative order. */
function longestIncreasing(sequence: readonly number[]): Set<number> {
  const tails: number[] = [];
  const previous: number[] = new Array(sequence.length).fill(-1);
  sequence.forEach((value, index) => {
    let low = 0;
    let high = tails.length;
    while (low < high) {
      const middle = (low + high) >> 1;
      if (sequence[tails[middle]] < value) low = middle + 1;
      else high = middle;
    }
    if (low > 0) previous[index] = tails[low - 1];
    tails[low] = index;
  });
  const kept = new Set<number>();
  for (let cursor = tails.length ? tails[tails.length - 1] : -1; cursor >= 0; cursor = previous[cursor]) kept.add(cursor);
  return kept;
}

/**
 * What the working copy changes against `base` (the live revision), per set, so
 * each card can carry a "Draft change" chip: a field changed (name, family,
 * shown, status…), the set was retired, it gains or loses the default, or it was
 * moved. "Moved" means it left the longest run of sets that kept their order in
 * its family, so moving one set to the top marks that set, not every set it passed.
 */
export function changedSetIds(base: TypingFeelConfig, working: TypingFeelConfig): Set<string> {
  const withoutOrder = (set: TypingFeelSet): string => canonicalJson({ ...set, order: null });
  const before = new Map(base.keyboard.sets.map((set) => [set.id, set]));
  const changed = new Set<string>();
  for (const set of working.keyboard.sets) {
    const old = before.get(set.id);
    if (!old || withoutOrder(old) !== withoutOrder(set)) changed.add(set.id);
  }
  const kept = new Set(working.keyboard.sets.map((set) => set.id));
  for (const id of before.keys()) if (!kept.has(id)) changed.add(id);
  for (const family of working.keyboard.families) {
    const oldOrder = new Map(familySets(base, family.id).map((set, index) => [set.id, index]));
    const stayed = familySets(working, family.id).filter((set) => oldOrder.has(set.id));
    const run = longestIncreasing(stayed.map((set) => oldOrder.get(set.id) as number));
    stayed.forEach((set, index) => {
      if (!run.has(index)) changed.add(set.id);
    });
  }
  if (base.keyboard.defaultSet !== working.keyboard.defaultSet) {
    changed.add(base.keyboard.defaultSet);
    changed.add(working.keyboard.defaultSet);
  }
  return changed;
}

/** A short count of what the working copy changes against `source`, for the draft bar. */
export function localChangeSummary(source: TypingFeelConfig, working: TypingFeelConfig): { count: number; parts: string[] } {
  const parts: string[] = [];
  const sets = changedSetIds(source, working);
  if (sets.size) parts.push(`${sets.size} ${sets.size === 1 ? "set" : "sets"}`);
  if (canonicalJson(source.keyboard.families) !== canonicalJson(working.keyboard.families)) parts.push("families");
  if (canonicalJson(source.effects) !== canonicalJson(working.effects)) parts.push("typing effects");
  return { count: parts.length, parts };
}

/** Decision 5: an owner score of `threshold` (9) or more is Published; under it only Provisional, with a reason. */
export function acceptStatus(score: number | null, threshold = 9): "published" | "provisional" | null {
  if (score === null || !Number.isFinite(score) || score < 0 || score > 10) return null;
  return score >= threshold ? "published" : "provisional";
}

/** Why `setId` cannot name a new set in this working copy, or null (§3.4: a live id or a retired id is never reused). */
export function newSetIdProblem(config: TypingFeelConfig, setId: string, options: { idPattern?: string; reserved?: readonly string[]; retired?: readonly string[] } = {}): string | null {
  const pattern = new RegExp(options.idPattern ?? "^[a-z0-9][a-z0-9-]{0,31}$");
  if (!pattern.test(setId)) return "The id needs 1 to 32 lower-case letters, digits or dashes, starting with a letter or digit.";
  if ((options.reserved ?? ["off"]).includes(setId)) return `"${setId}" is reserved for the games' silent choice.`;
  if (config.keyboard.sets.some((set) => set.id === setId)) return `"${setId}" is already a set in this draft; choose a new id.`;
  if (config.keyboard.retiredIds.includes(setId) || (options.retired ?? []).includes(setId)) return `"${setId}" was retired and is never used again; choose another id.`;
  return null;
}

/**
 * Adds a set accepted in Add sound set (§3.8 step 4) at the end of its family.
 * The row comes from the server's Accept; the draft then goes through Save draft → Review → Publish.
 */
export function addSet(config: TypingFeelConfig, row: TypingFeelSet, options: { idPattern?: string; reserved?: readonly string[]; retired?: readonly string[]; threshold?: number } = {}): EditResult {
  const problem = newSetIdProblem(config, row.id, options);
  if (problem) return fail(problem);
  if (!config.keyboard.families.some((family) => family.id === row.family)) return fail(`Family ${row.family} is not in this draft.`);
  const status = acceptStatus(row.ownerScore, options.threshold);
  if (status === null) return fail("The set needs the owner's listening score (0 to 10).");
  if (row.status !== status) return fail(status === "provisional" ? `A score under ${options.threshold ?? 9} can only be Provisional.` : "A set scored 9 or more is Published.");
  if (row.status === "provisional" && !row.note?.trim()) return fail("A Provisional set needs a note giving the reason.");
  const next = cloneConfig(config);
  const set = { ...row, ...(row.labels ? { labels: [...row.labels] } : {}) };
  set.order = familySets(next, row.family).reduce((max, entry) => Math.max(max, entry.order + 1), 0);
  next.keyboard.sets.push(set);
  return ok(next);
}
