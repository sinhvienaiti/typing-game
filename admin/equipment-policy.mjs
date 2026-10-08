export class EquipmentPolicyValidationError extends Error {}

function fail(message) {
  throw new EquipmentPolicyValidationError(message);
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
}

function rejectUnknown(value, path, allowed) {
  for (const key of Object.keys(value)) {
    if (!allowed.includes(key)) fail(`${path}.${key} is not authorable.`);
  }
}

export function validateEquipmentPolicy(policy, equipmentContract) {
  const input = object(policy, "content.equipment");
  rejectUnknown(input, "content.equipment", ["configRevision", "equipment"]);
  text(input.configRevision, "content.equipment.configRevision", 120);
  if (input.equipment === undefined) return policy;

  const entries = object(input.equipment, "content.equipment.equipment");
  const ids = equipmentContract?.ids ?? [];
  const fields = equipmentContract?.authorableFields ?? [];
  const coreStats = equipmentContract?.coreStatKeys ?? [];
  const perkIds = equipmentContract?.perkIds ?? [];
  const constraints = equipmentContract?.constraints;
  if (ids.length === 0 || fields.length === 0 || coreStats.length === 0 || !constraints) {
    fail("Child Equipment Admin contract is incomplete.");
  }

  for (const [id, rawOverride] of Object.entries(entries)) {
    if (!ids.includes(id)) fail(`Unknown equipment id: ${id}.`);
    const override = object(rawOverride, `content.equipment.equipment.${id}`);
    rejectUnknown(override, `content.equipment.equipment.${id}`, fields);

    if (override.name !== undefined) {
      text(override.name, `content.equipment.equipment.${id}.name`, constraints.nameMax);
    }
    if (override.description !== undefined) {
      text(override.description, `content.equipment.equipment.${id}.description`, constraints.descriptionMax);
    }
    if (override.stats !== undefined) {
      const stats = object(override.stats, `content.equipment.equipment.${id}.stats`);
      for (const [key, value] of Object.entries(stats)) {
        if (!coreStats.includes(key)) {
          fail(`content.equipment.equipment.${id}.stats.${key} is not a core stat.`);
        }
        number(
          value,
          `content.equipment.equipment.${id}.stats.${key}`,
          constraints.statBonus.min,
          constraints.statBonus.max,
        );
      }
    }
    if (
      override.perk !== undefined &&
      override.perk !== null &&
      (typeof override.perk !== "string" || !perkIds.includes(override.perk))
    ) {
      fail(`content.equipment.equipment.${id}.perk is invalid.`);
    }
  }
  return policy;
}
