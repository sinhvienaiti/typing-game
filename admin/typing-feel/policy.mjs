// Typing Feel revision rules (docs/games/TYPING_FEEL_SERVICE.md §3.4, §3.13, §8.3).
// Pure checks of one typing-feel-admin/1 config, and of a draft against the
// revision it was based on. Media checks (assetVersionId, components) live in
// export.mjs, because they read Media V2 and the set manifests.
import { AdminValidationError } from "../store.mjs";

export const TYPING_FEEL_CONFIG_SCHEMA = "typing-feel-admin/1";
/** §8.3 / decision 5: a set added or re-formatted through the Admin is Published only from this owner score. */
export const PUBLISHED_OWNER_SCORE = 9;
export const SET_NAME_MAX = 60;
export const FAMILY_NAME_MAX = 40;
export const NOTE_MAX = 500;
const MEDIA_VERSION_ID = /^[a-z0-9][a-z0-9._:-]{0,159}$/;
const CONTROL = /[\u0000-\u001f\u007f]/;

export class TypingFeelValidationError extends AdminValidationError {
  constructor(problems) {
    const list = [problems].flat().filter(Boolean);
    super(list.length === 1 ? list[0] : `${list.length} problems: ${list.join(" ")}`);
    this.name = "TypingFeelValidationError";
    this.problems = list;
  }
}

function isObject(value) {
  return value !== null && typeof value === "object" && !Array.isArray(value);
}

function describe(value) {
  return JSON.stringify(value) ?? String(value);
}

/** Collects every problem of `config` (schema, ids, families, default, effects). Returns [] when it is valid. */
export function configProblems(config, contract) {
  const problems = [];
  const add = (message) => problems.push(message);
  const keys = (value, path, allowed, required = allowed) => {
    for (const key of Object.keys(value)) if (!allowed.includes(key)) add(`${path}.${key} is not part of ${TYPING_FEEL_CONFIG_SCHEMA}.`);
    for (const key of required) if (!Object.hasOwn(value, key)) add(`${path}.${key} is required.`);
  };
  const idPattern = new RegExp(contract.id.pattern);
  const reserved = new Set(contract.id.reserved ?? []);
  const text = (value, path, max) => {
    if (typeof value !== "string" || value.trim() === "" || value !== value.trim() || value.length > max || CONTROL.test(value)) {
      add(`${path} must be text of 1 to ${max} characters without leading or trailing spaces.`);
      return false;
    }
    return true;
  };
  const id = (value, path, { set = false } = {}) => {
    if (typeof value !== "string" || !idPattern.test(value)) {
      add(`${path} ${describe(value)} must match ${contract.id.pattern}.`);
      return false;
    }
    if (set && reserved.has(value)) {
      add(`${path} ${describe(value)} is reserved for the games' silent choice.`);
      return false;
    }
    return true;
  };

  if (!isObject(config)) return ["The Typing Feel config must be an object."];
  keys(config, "config", ["schema", "contract", "keyboard", "effects"]);
  if (config.schema !== TYPING_FEEL_CONFIG_SCHEMA) add(`config.schema must be ${describe(TYPING_FEEL_CONFIG_SCHEMA)}.`);
  if (config.contract !== contract.contract) add(`config.contract must be ${contract.contract}.`);

  const keyboard = config.keyboard;
  if (!isObject(keyboard)) {
    add("config.keyboard must be an object.");
  } else {
    keys(keyboard, "keyboard", ["defaultSet", "families", "sets", "retiredIds"]);
    const familyIds = new Set();
    if (!Array.isArray(keyboard.families) || keyboard.families.length === 0) {
      add("keyboard.families must list at least one family.");
    } else {
      const names = new Set();
      const orders = new Set();
      keyboard.families.forEach((family, index) => {
        const path = `keyboard.families[${index}]`;
        if (!isObject(family)) return add(`${path} must be an object.`);
        keys(family, path, ["id", "name", "order"]);
        if (id(family.id, `${path}.id`)) {
          if (familyIds.has(family.id)) add(`Family id ${family.id} is listed twice.`);
          familyIds.add(family.id);
        }
        if (text(family.name, `${path}.name`, FAMILY_NAME_MAX)) {
          if (names.has(family.name)) add(`Family name ${describe(family.name)} is used twice; the games group sets by family name.`);
          names.add(family.name);
        }
        if (!Number.isInteger(family.order) || family.order < 0 || family.order > 9999) add(`${path}.order must be a whole number from 0 to 9999.`);
        else if (orders.has(family.order)) add(`Two families share order ${family.order}.`);
        else orders.add(family.order);
      });
    }

    const retired = new Set();
    if (!Array.isArray(keyboard.retiredIds)) {
      add("keyboard.retiredIds must be a list.");
    } else {
      keyboard.retiredIds.forEach((value, index) => {
        if (!id(value, `keyboard.retiredIds[${index}]`)) return;
        if (retired.has(value)) add(`Retired id ${value} is listed twice.`);
        retired.add(value);
      });
    }

    const sets = new Map();
    if (!Array.isArray(keyboard.sets)) {
      add("keyboard.sets must be a list.");
    } else {
      const familyOrders = new Map();
      keyboard.sets.forEach((set, index) => {
        const path = `keyboard.sets[${index}]`;
        if (!isObject(set)) return add(`${path} must be an object.`);
        keys(set, path,
          ["id", "name", "family", "order", "enabled", "status", "assetVersionId", "ownerPick", "ownerScore", "recipe", "note", "score", "labels"],
          ["id", "name", "family", "order", "enabled", "status", "assetVersionId", "ownerPick", "ownerScore", "recipe"]);
        const label = typeof set.id === "string" ? `Set ${set.id}` : path;
        if (id(set.id, `${path}.id`, { set: true })) {
          if (sets.has(set.id)) add(`Set id ${set.id} is listed twice.`);
          else sets.set(set.id, set);
          if (retired.has(set.id)) add(`${label} is retired; a retired id is never used again.`);
        }
        text(set.name, `${label} name`, SET_NAME_MAX);
        if (typeof set.family !== "string" || !familyIds.has(set.family)) add(`${label} uses family ${describe(set.family)}, which is not in keyboard.families.`);
        if (!Number.isInteger(set.order) || set.order < 0 || set.order > 9999) {
          add(`${label} order must be a whole number from 0 to 9999.`);
        } else if (typeof set.family === "string") {
          const used = familyOrders.get(set.family) ?? new Set();
          if (used.has(set.order)) add(`Two sets of family ${set.family} share order ${set.order}.`);
          used.add(set.order);
          familyOrders.set(set.family, used);
        }
        if (typeof set.enabled !== "boolean") add(`${label} enabled must be true or false.`);
        if (!contract.statuses.includes(set.status)) add(`${label} status must be one of ${contract.statuses.join(", ")}.`);
        if (typeof set.assetVersionId !== "string" || !MEDIA_VERSION_ID.test(set.assetVersionId)) add(`${label} needs a Media V2 assetVersionId.`);
        if (typeof set.ownerPick !== "boolean") add(`${label} ownerPick must be true or false.`);
        if (set.ownerScore !== null && (typeof set.ownerScore !== "number" || !Number.isFinite(set.ownerScore) || set.ownerScore < 0 || set.ownerScore > 10)) {
          add(`${label} ownerScore must be null or a number from 0 to 10.`);
        }
        if (!Object.hasOwn(contract.recipes, set.recipe)) add(`${label} recipe must be one of ${Object.keys(contract.recipes).join(", ")}.`);
        if (set.note !== undefined) text(set.note, `${label} note`, NOTE_MAX);
        if (set.score !== undefined && set.score !== null && (typeof set.score !== "number" || !Number.isFinite(set.score))) add(`${label} score must be null or a number.`);
        if (set.labels !== undefined) {
          if (!Array.isArray(set.labels) || set.labels.some((value) => !Object.hasOwn(contract.labels, value)) || new Set(set.labels).size !== set.labels.length) {
            add(`${label} labels must be distinct ids from: ${Object.keys(contract.labels).join(", ")}.`);
          }
        }
        // §8.3: a provisional set carries its reason.
        if (set.status === "provisional" && set.note === undefined) add(`${label} is provisional and needs a note giving the reason.`);
      });
      if (![...sets.values()].some((set) => set.enabled === true)) add("At least one set must be shown: a catalogue with no set is invalid in every game.");
    }

    if (id(keyboard.defaultSet, "keyboard.defaultSet", { set: true })) {
      const chosen = sets.get(keyboard.defaultSet);
      if (!chosen) add(`Default set ${keyboard.defaultSet} is not in keyboard.sets.`);
      else {
        if (chosen.enabled !== true) add(`Default set ${keyboard.defaultSet} is hidden; the default must be shown.`);
        if (chosen.status === "provisional") add(`Default set ${keyboard.defaultSet} is provisional; a provisional set cannot be the default.`);
      }
    }
  }

  const effects = config.effects;
  if (!isObject(effects)) {
    add("config.effects must be an object.");
  } else {
    keys(effects, "effects", ["defaults"]);
    const defaults = effects.defaults;
    if (!isObject(defaults)) {
      add("effects.defaults must be an object.");
    } else {
      keys(defaults, "effects.defaults", ["style", "intensity", "size", "volume"]);
      const rules = contract.effects;
      if (!rules.styles.includes(defaults.style)) add(`effects.defaults.style must be one of ${rules.styles.join(", ")}.`);
      if (!rules.intensities.includes(defaults.intensity)) add(`effects.defaults.intensity must be one of ${rules.intensities.join(", ")}.`);
      if (!rules.sizes.includes(defaults.size)) add(`effects.defaults.size must be one of ${rules.sizes.join(", ")}.`);
      if (typeof defaults.volume !== "number" || !Number.isFinite(defaults.volume) || defaults.volume < rules.volume.min || defaults.volume > rules.volume.max) {
        add(`effects.defaults.volume must be a number from ${rules.volume.min} to ${rules.volume.max}.`);
      }
    }
  }
  return problems;
}

/**
 * What the Admin pages may offer, straight from the contract, so the page and
 * the checks above never disagree (§3.4, §3.10): effect lists and range, set
 * statuses, labels, recipes, id rule and text limits.
 */
export function editorOptions(contract) {
  const effects = contract.effects;
  return {
    effects: {
      styles: [...effects.styles],
      intensities: [...effects.intensities],
      sizes: [...effects.sizes],
      volume: { min: effects.volume.min, max: effects.volume.max },
      defaults: { ...effects.defaults },
    },
    statuses: [...contract.statuses],
    labels: Object.keys(contract.labels),
    recipes: Object.keys(contract.recipes),
    idPattern: contract.id.pattern,
    reservedIds: [...(contract.id.reserved ?? [])],
    setNameMax: SET_NAME_MAX,
    familyNameMax: FAMILY_NAME_MAX,
    noteMax: NOTE_MAX,
    publishedOwnerScore: PUBLISHED_OWNER_SCORE,
    minimum: { key: contract.set.minimum.key, space: contract.set.minimum.space },
  };
}

export function validateTypingFeelConfig(config, contract) {
  const problems = configProblems(config, contract);
  if (problems.length) throw new TypingFeelValidationError(problems);
  return config;
}

/**
 * Rules for a draft against the revision it is based on (§3.4, §3.13):
 * - a set id the base had is kept or retired, never dropped (player saves store it);
 * - a retired id stays retired; an id retired in any published revision is never reused;
 * - a set that is new or re-formatted (other assetVersionId) is Published only with
 *   an owner score of 9 or more, otherwise it is Provisional with a reason (§8.3);
 * - an id that was live in any published revision (and left the catalogue by a
 *   Rollback) comes back only with a sound it was published with: player saves may
 *   still hold it (`publishedVersions`: Map<setId, Set<assetVersionId>>).
 */
export function baseProblems(config, baseConfig, { reservedIds = [], publishedVersions = new Map() } = {}) {
  const problems = [];
  const sets = config?.keyboard?.sets ?? [];
  const retired = new Set(config?.keyboard?.retiredIds ?? []);
  const baseSets = new Map((baseConfig?.keyboard?.sets ?? []).map((set) => [set.id, set]));
  const ids = new Set(sets.map((set) => set.id));
  for (const id of baseSets.keys()) {
    if (!ids.has(id) && !retired.has(id)) problems.push(`Set ${id} was removed; hide it or retire it instead, because player saves store its id.`);
  }
  for (const id of baseConfig?.keyboard?.retiredIds ?? []) {
    if (!retired.has(id)) problems.push(`Retired id ${id} must stay retired.`);
  }
  const reserved = new Set(reservedIds);
  for (const set of sets) {
    const base = baseSets.get(set.id);
    if (reserved.has(set.id) && base?.assetVersionId !== set.assetVersionId) {
      problems.push(`Set id ${set.id} was retired in a published revision and is never used again; choose another id.`);
    } else if (!base && publishedVersions.has(set.id) && !publishedVersions.get(set.id).has(set.assetVersionId)) {
      problems.push(`Set id ${set.id} was published before with another sound, and player saves may still hold it; give the new sound a new id.`);
    }
    const changedSound = !base || base.assetVersionId !== set.assetVersionId;
    if (changedSound && set.status === "published" && !(typeof set.ownerScore === "number" && set.ownerScore >= PUBLISHED_OWNER_SCORE)) {
      problems.push(`Set ${set.id} is new or re-formatted: it needs an owner score of ${PUBLISHED_OWNER_SCORE} or more to be Published. Mark it Provisional with a reason, or score it.`);
    }
  }
  return problems;
}
