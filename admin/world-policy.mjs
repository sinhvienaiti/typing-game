export class WorldPolicyValidationError extends Error {}

function fail(message) { throw new WorldPolicyValidationError(message); }
function object(value, path) {
  if (value === null || typeof value !== "object" || Array.isArray(value)) fail(`${path} must be an object.`);
  return value;
}
function rejectUnknown(value, path, allowed) {
  for (const key of Object.keys(value)) if (!allowed.includes(key)) fail(`${path}.${key} is not authorable.`);
}

export function validateWorldPolicy(policy, worldContract, enemyContract) {
  const input = object(policy, "content.worlds");
  rejectUnknown(input, "content.worlds", ["configRevision", "worlds"]);
  if (typeof input.configRevision !== "string" || input.configRevision.trim().length === 0 || input.configRevision.length > 120) {
    fail("content.worlds.configRevision must be a non-empty string up to 120 characters.");
  }
  const worlds = object(input.worlds, "content.worlds.worlds");
  const fields = worldContract?.authorableFields ?? [];
  const roster = worldContract?.constraints?.enemyRoster;
  const count = worldContract?.count;
  const enemyIds = enemyContract?.ids ?? [];
  if (!Number.isInteger(count) || count < 1 || fields.length === 0 || !roster || enemyIds.length === 0) {
    fail("Child Worlds Admin contract is incomplete.");
  }
  const allowedWorldIds = new Set(Array.from({ length: count }, (_, index) => `world-${String(index + 1).padStart(2, "0")}`));
  for (const [worldId, rawOverride] of Object.entries(worlds)) {
    if (!allowedWorldIds.has(worldId)) fail(`Unknown world id: ${worldId}.`);
    const override = object(rawOverride, `content.worlds.worlds.${worldId}`);
    rejectUnknown(override, `content.worlds.worlds.${worldId}`, fields);
    if (!Array.isArray(override.enemyRoster)) fail(`content.worlds.worlds.${worldId}.enemyRoster must be an array.`);
    if (override.enemyRoster.length < roster.minItems || override.enemyRoster.length > roster.maxItems) {
      fail(`content.worlds.worlds.${worldId}.enemyRoster must contain ${roster.minItems}..${roster.maxItems} entries.`);
    }
    const seen = new Set();
    for (const enemyId of override.enemyRoster) {
      if (typeof enemyId !== "string" || !enemyIds.includes(enemyId)) fail(`Unknown enemy id in ${worldId} roster: ${String(enemyId)}.`);
      if (seen.has(enemyId)) fail(`Duplicate enemy id in ${worldId} roster: ${enemyId}.`);
      seen.add(enemyId);
    }
  }
  return policy;
}
