export class StagePolicyValidationError extends Error {}

function fail(message) {
  throw new StagePolicyValidationError(message);
}

function object(value, path) {
  if (value === null || typeof value !== "object" || Array.isArray(value)) {
    fail(`${path} must be an object.`);
  }
  return value;
}

function rejectUnknown(value, path, allowed) {
  for (const key of Object.keys(value)) {
    if (!allowed.includes(key)) fail(`${path}.${key} is not authorable.`);
  }
}

function finite(value, path) {
  if (typeof value !== "number" || !Number.isFinite(value)) fail(`${path} must be a finite number.`);
  return value;
}

export function validateStagePolicy(policy, stageContract) {
  const input = object(policy, "content.stages");
  rejectUnknown(input, "content.stages", ["configRevision", "stages"]);
  if (typeof input.configRevision !== "string" || input.configRevision.trim().length === 0 || input.configRevision.length > 120) {
    fail("content.stages.configRevision must be a non-empty string up to 120 characters.");
  }
  if (!Array.isArray(input.stages)) fail("content.stages.stages must be an array.");

  const fields = stageContract?.authorableFields ?? [];
  const constraints = stageContract?.constraints;
  if (fields.length === 0 || !constraints) fail("Child Stages Admin contract is incomplete.");

  const seen = new Set();
  for (let index = 0; index < input.stages.length; index += 1) {
    const override = object(input.stages[index], `content.stages.stages[${index}]`);
    const path = `content.stages.stages[${index}]`;
    rejectUnknown(override, path, ["stage", ...fields]);
    const stage = override.stage;
    if (!Number.isInteger(stage) || stage < constraints.stage.min || stage > constraints.stage.max) {
      fail(`${path}.stage must be an integer from ${constraints.stage.min} to ${constraints.stage.max}.`);
    }
    if (seen.has(stage)) fail(`Duplicate stage override: ${stage}.`);
    seen.add(stage);

    let fieldCount = 0;
    if (override.enemyBudget !== undefined) {
      const value = finite(override.enemyBudget, `${path}.enemyBudget`);
      if (value <= constraints.enemyBudget.minExclusive) fail(`${path}.enemyBudget must be greater than ${constraints.enemyBudget.minExclusive}.`);
      fieldCount += 1;
    }
    if (override.eliteChance !== undefined) {
      const value = finite(override.eliteChance, `${path}.eliteChance`);
      if (value < constraints.eliteChance.min || value > constraints.eliteChance.max) fail(`${path}.eliteChance must be between ${constraints.eliteChance.min} and ${constraints.eliteChance.max}.`);
      fieldCount += 1;
    }
    if (override.modifierSlots !== undefined) {
      const value = finite(override.modifierSlots, `${path}.modifierSlots`);
      if (!Number.isInteger(value) || value < constraints.modifierSlots.min || value > constraints.modifierSlots.max) fail(`${path}.modifierSlots must be an integer from ${constraints.modifierSlots.min} to ${constraints.modifierSlots.max}.`);
      fieldCount += 1;
    }
    if (fieldCount === 0) fail(`${path} must override at least one authorable Stage field.`);
  }
  return policy;
}
