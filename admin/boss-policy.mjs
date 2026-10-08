export class BossPolicyValidationError extends Error {}

function fail(message) {
  throw new BossPolicyValidationError(message);
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

export function validateBossPolicy(policy, bossContract) {
  const input = object(policy, "content.bosses");
  rejectUnknown(input, "content.bosses", ["configRevision", "bosses"]);
  text(input.configRevision, "content.bosses.configRevision", 120);
  if (input.bosses === undefined) return policy;

  const entries = object(input.bosses, "content.bosses.bosses");
  const ids = bossContract?.ids ?? [];
  const fields = bossContract?.authorableFields ?? [];
  const constraints = bossContract?.constraints;
  if (ids.length === 0 || fields.length === 0 || !constraints) {
    fail("Child Bosses Admin contract is incomplete.");
  }

  for (const [id, rawOverride] of Object.entries(entries)) {
    if (!ids.includes(id)) fail(`Unknown boss id: ${id}.`);
    const override = object(rawOverride, `content.bosses.bosses.${id}`);
    rejectUnknown(override, `content.bosses.bosses.${id}`, fields);
    if (override.name !== undefined) text(override.name, `content.bosses.bosses.${id}.name`, constraints.nameMax);
    if (override.title !== undefined) text(override.title, `content.bosses.bosses.${id}.title`, constraints.titleMax);
  }
  return policy;
}
