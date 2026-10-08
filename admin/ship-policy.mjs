export class ShipPolicyValidationError extends Error {}

const VISUAL_KEYS = [
  "silhouette",
  "primary",
  "secondary",
  "accent",
  "core",
  "engine",
  "glow",
  "wingSpan",
  "bodyLength",
  "engineCount",
];
const COLOR_KEYS = ["primary", "secondary", "accent", "core", "engine", "glow"];
const TEXT_LIMITS = {
  name: 80,
  role: 100,
  summary: 240,
  passiveName: 100,
  activeName: 100,
  ultimateName: 100,
};

function fail(message) {
  throw new ShipPolicyValidationError(message);
}

function object(value, path) {
  if (value === null || typeof value !== "object" || Array.isArray(value)) {
    fail(`${path} must be an object.`);
  }
  return value;
}

function nonEmptyString(value, path, max) {
  if (typeof value !== "string" || value.trim().length === 0 || value.length > max) {
    fail(`${path} must be a non-empty string up to ${max} characters.`);
  }
}

function finiteNumber(value, path, min, max) {
  if (typeof value !== "number" || !Number.isFinite(value) || value < min || value > max) {
    fail(`${path} must be a finite number from ${min} to ${max}.`);
  }
}

function rejectUnknownKeys(value, path, allowed) {
  for (const key of Object.keys(value)) {
    if (!allowed.includes(key)) fail(`${path}.${key} is not authorable.`);
  }
}

export function validateShipPolicy(policy, shipContract) {
  const input = object(policy, "content.ships");
  rejectUnknownKeys(input, "content.ships", ["configRevision", "ships"]);
  nonEmptyString(input.configRevision, "content.ships.configRevision", 120);
  if (input.ships === undefined) return policy;

  const ships = object(input.ships, "content.ships.ships");
  const ids = shipContract?.ids ?? [];
  const authorableFields = shipContract?.authorableFields ?? [];
  const coreStatKeys = shipContract?.coreStatKeys ?? [];
  const constraints = shipContract?.constraints;
  if (ids.length === 0 || authorableFields.length === 0 || !constraints) {
    fail("Child Ships Admin contract is incomplete.");
  }

  for (const [id, rawOverride] of Object.entries(ships)) {
    if (!ids.includes(id)) fail(`Unknown ship id: ${id}.`);
    const override = object(rawOverride, `content.ships.ships.${id}`);
    rejectUnknownKeys(override, `content.ships.ships.${id}`, authorableFields);

    for (const [key, max] of Object.entries(TEXT_LIMITS)) {
      if (override[key] !== undefined) {
        nonEmptyString(override[key], `content.ships.ships.${id}.${key}`, max);
      }
    }

    if (override.unlockStage !== undefined) {
      const range = constraints.unlockStage;
      if (!Number.isInteger(override.unlockStage)) {
        fail(`content.ships.ships.${id}.unlockStage must be an integer.`);
      }
      finiteNumber(override.unlockStage, `content.ships.ships.${id}.unlockStage`, range.min, range.max);
    }

    if (override.statBonus !== undefined) {
      const stats = object(override.statBonus, `content.ships.ships.${id}.statBonus`);
      for (const [key, value] of Object.entries(stats)) {
        if (!coreStatKeys.includes(key)) {
          fail(`content.ships.ships.${id}.statBonus.${key} is not a core stat.`);
        }
        finiteNumber(
          value,
          `content.ships.ships.${id}.statBonus.${key}`,
          constraints.statBonus.min,
          constraints.statBonus.max,
        );
      }
    }

    if (override.visual !== undefined) {
      const visual = object(override.visual, `content.ships.ships.${id}.visual`);
      rejectUnknownKeys(visual, `content.ships.ships.${id}.visual`, VISUAL_KEYS);
      if (visual.silhouette !== undefined && !constraints.visual.silhouettes.includes(visual.silhouette)) {
        fail(`content.ships.ships.${id}.visual.silhouette is invalid.`);
      }
      for (const key of COLOR_KEYS) {
        if (visual[key] !== undefined) {
          nonEmptyString(visual[key], `content.ships.ships.${id}.visual.${key}`, 32);
        }
      }
      for (const key of ["wingSpan", "bodyLength"]) {
        if (visual[key] !== undefined) {
          finiteNumber(
            visual[key],
            `content.ships.ships.${id}.visual.${key}`,
            constraints.visual[key].min,
            constraints.visual[key].max,
          );
        }
      }
      if (visual.engineCount !== undefined && !constraints.visual.engineCounts.includes(visual.engineCount)) {
        fail(`content.ships.ships.${id}.visual.engineCount must be one of ${constraints.visual.engineCounts.join(", ")}.`);
      }
    }
  }

  return policy;
}
