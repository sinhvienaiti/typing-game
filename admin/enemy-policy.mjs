export class EnemyPolicyValidationError extends Error {}

function fail(message) {
  throw new EnemyPolicyValidationError(message);
}

function object(value, path) {
  if (value === null || typeof value !== "object" || Array.isArray(value)) {
    fail(`${path} must be an object.`);
  }
  return value;
}

function text(value, path, max) {
  if (typeof value !== "string" || value.trim().length === 0 || value.length > max) {
    fail(`${path} must be a non-empty string up to ${max} characters.`);
  }
}

function rejectUnknown(value, path, allowed) {
  for (const key of Object.keys(value)) {
    if (!allowed.includes(key)) fail(`${path}.${key} is not authorable.`);
  }
}

export function validateEnemyPolicy(policy, enemyContract) {
  const input = object(policy, "content.enemies");
  rejectUnknown(input, "content.enemies", ["configRevision", "enemies"]);
  text(input.configRevision, "content.enemies.configRevision", 120);
  if (input.enemies === undefined) return policy;

  const entries = object(input.enemies, "content.enemies.enemies");
  const ids = enemyContract?.ids ?? [];
  const fields = enemyContract?.authorableFields ?? [];
  const range = enemyContract?.constraints?.minStage;
  if (ids.length === 0 || fields.length === 0 || !range) {
    fail("Child Enemies Admin contract is incomplete.");
  }

  for (const [id, rawOverride] of Object.entries(entries)) {
    if (!ids.includes(id)) fail(`Unknown enemy id: ${id}.`);
    const override = object(rawOverride, `content.enemies.enemies.${id}`);
    rejectUnknown(override, `content.enemies.enemies.${id}`, fields);
    if (override.minStage !== undefined) {
      if (!Number.isInteger(override.minStage) || override.minStage < range.min || override.minStage > range.max) {
        fail(`content.enemies.enemies.${id}.minStage must be an integer from ${range.min} to ${range.max}.`);
      }
    }
  }
  return policy;
}
