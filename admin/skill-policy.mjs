export class SkillPolicyValidationError extends Error {}

function fail(message) {
  throw new SkillPolicyValidationError(message);
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

function number(value, path, min, max) {
  if (typeof value !== "number" || !Number.isFinite(value) || value < min || value > max) {
    fail(`${path} must be a finite number from ${min} to ${max}.`);
  }
  return value;
}

function nullableInteger(value, path, range) {
  if (value === null) return;
  const parsed = number(value, path, range.min, range.max);
  if (!Number.isInteger(parsed)) fail(`${path} must be an integer or null.`);
}

function rejectUnknown(value, path, allowed) {
  for (const key of Object.keys(value)) {
    if (!allowed.includes(key)) fail(`${path}.${key} is not authorable.`);
  }
}

function typingCondition(value, path, constraints) {
  if (value === null) return;
  const input = object(value, path);
  rejectUnknown(input, path, ["minStreak", "minAccuracy"]);
  if (input.minStreak !== undefined) {
    const streak = number(input.minStreak, `${path}.minStreak`, constraints.minStreak.min, constraints.minStreak.max);
    if (!Number.isInteger(streak)) fail(`${path}.minStreak must be an integer.`);
  }
  if (input.minAccuracy !== undefined) {
    number(input.minAccuracy, `${path}.minAccuracy`, constraints.minAccuracy.min, constraints.minAccuracy.max);
  }
}

export function validateSkillPolicy(policy, skillContract) {
  const input = object(policy, "content.skills");
  rejectUnknown(input, "content.skills", ["configRevision", "skills"]);
  text(input.configRevision, "content.skills.configRevision", 120);
  if (input.skills === undefined) return policy;

  const entries = object(input.skills, "content.skills.skills");
  const ids = skillContract?.ids ?? [];
  const fields = skillContract?.authorableFields ?? [];
  const constraints = skillContract?.constraints;
  if (ids.length === 0 || fields.length === 0 || !constraints) {
    fail("Child Skills Admin contract is incomplete.");
  }

  for (const [id, rawOverride] of Object.entries(entries)) {
    if (!ids.includes(id)) fail(`Unknown skill id: ${id}.`);
    const override = object(rawOverride, `content.skills.skills.${id}`);
    rejectUnknown(override, `content.skills.skills.${id}`, fields);
    if (override.name !== undefined) text(override.name, `content.skills.skills.${id}.name`, constraints.nameMax);
    if (override.description !== undefined) text(override.description, `content.skills.skills.${id}.description`, constraints.descriptionMax);
    if (override.energyCost !== undefined) number(override.energyCost, `content.skills.skills.${id}.energyCost`, constraints.energyCost.min, constraints.energyCost.max);
    if (override.cooldown !== undefined) number(override.cooldown, `content.skills.skills.${id}.cooldown`, constraints.cooldown.min, constraints.cooldown.max);
    if (override.charges !== undefined) nullableInteger(override.charges, `content.skills.skills.${id}.charges`, constraints.charges);
    if (override.perStageLimit !== undefined) nullableInteger(override.perStageLimit, `content.skills.skills.${id}.perStageLimit`, constraints.perStageLimit);
    if (override.typingCondition !== undefined) typingCondition(override.typingCondition, `content.skills.skills.${id}.typingCondition`, constraints.typingCondition);
  }
  return policy;
}
