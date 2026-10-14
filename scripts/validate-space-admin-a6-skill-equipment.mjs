import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const child = resolve(root, "games/space-typing");

const [
  capabilities,
  skillPolicy,
  equipmentPolicy,
  skillPage,
  equipmentPage,
  sharedStudio,
] = await Promise.all([
  readFile(resolve(child, "src/admin/a6-skill-equipment-capabilities.ts"), "utf8"),
  readFile(resolve(child, "src/admin/skill-runtime-policy.ts"), "utf8"),
  readFile(resolve(child, "src/admin/equipment-runtime-policy.ts"), "utf8"),
  readFile(resolve(root, "portal/src/admin/space-typing-skills-phase-b.ts"), "utf8"),
  readFile(resolve(root, "portal/src/admin/space-typing-equipment-phase-b.ts"), "utf8"),
  readFile(resolve(root, "portal/src/admin/v2/asset-tuning-studio.ts"), "utf8"),
]);

function requireText(source, needle, label) {
  assert.ok(source.includes(needle), `${label}: expected ${JSON.stringify(needle)}`);
}

function forbidText(source, needle, label) {
  assert.ok(!source.includes(needle), `${label}: forbidden ${JSON.stringify(needle)}`);
}

for (const id of [
  "skill.gameplay-policy",
  "skill.media-vfx-binding",
  "equipment.gameplay-policy",
  "equipment.registry-icon",
  "equipment.media-binding",
  "equipment.vfx-sfx-binding",
]) {
  requireText(capabilities, `id: "${id}"`, `A6 capability ${id} is registered`);
}
requireText(capabilities, 'status: "SUPPORTED NOW"', "A6 keeps proven gameplay authoring available");
requireText(capabilities, 'status: "REQUIRES CANONICAL MIGRATION"', "A6 keeps unproven media bindings migration-gated");
requireText(capabilities, 'status: "READ-ONLY REFERENCE"', "A6 keeps registry presentation references read-only");
requireText(capabilities, 'status: "DEFERRED / UNSUPPORTED"', "A6 keeps unsupported generic effects closed");

requireText(skillPolicy, 'const AUTHORABLE_KEYS = new Set([', "Skill policy owns an explicit authorable allow-list");
for (const field of ["name", "description", "energyCost", "cooldown", "charges", "perStageLimit", "typingCondition"]) {
  requireText(skillPolicy, `"${field}"`, `Skill gameplay field ${field} remains canonical`);
}
requireText(skillPolicy, 'applySkillRuntimeOverride', "Skill gameplay policy reaches production definitions");

requireText(equipmentPolicy, 'const AUTHORABLE_KEYS = new Set(["name", "description", "stats", "perk"])', "Equipment policy keeps its canonical allow-list");
requireText(equipmentPolicy, 'materializeEquipmentRuntimeSession', "Equipment policy materializes published overrides");
requireText(equipmentPolicy, 'activeEquipmentRuntimeOverride', "Equipment runtime exposes the active canonical override");

for (const fakeField of [
  "effectPreset",
  "effectAssetVersionId",
  "vfxAssetVersionId",
  "sfxAssetVersionId",
  "mediaAssetVersionId",
  "iconAssetVersionId",
  "imageAssetVersionId",
]) {
  forbidText(skillPolicy, fakeField, `Skill policy must not invent ${fakeField}`);
  forbidText(equipmentPolicy, fakeField, `Equipment policy must not invent ${fakeField}`);
}

// These pages own Draft creation, not direct activation. Each Draft is first
// materialized through the child registry-preview validator, then persisted as
// an immutable revision. Publish/rollback remains centralized in History.
requireText(skillPage, 'const validated = await previewSkills(policy)', "Skills validate the candidate through the canonical child preview before Draft creation");
requireText(skillPage, 'api.createRevision', "Skills retain immutable revision authoring");
requireText(skillPage, 'Publish from History to activate it', "Skills keep activation in the shared History / Publish boundary");
forbidText(skillPage, 'api.publish(', "Skills editor must not bypass History with direct publish");
requireText(equipmentPage, 'const validated = await previewEquipment(policy)', "Equipment validates the candidate through the canonical child preview before Draft creation");
requireText(equipmentPage, 'api.createRevision', "Equipment retains immutable revision authoring");
requireText(equipmentPage, 'Publish from History to activate it', "Equipment keeps activation in the shared History / Publish boundary");
forbidText(equipmentPage, 'api.publish(', "Equipment editor must not bypass History with direct publish");

for (const fakeUi of [
  "effectPreset",
  "vfxAssetVersionId",
  "sfxAssetVersionId",
  "iconAssetVersionId",
  "imageAssetVersionId",
]) {
  forbidText(skillPage, fakeUi, `Skills UI must not expose unowned ${fakeUi}`);
  forbidText(equipmentPage, fakeUi, `Equipment UI must not expose unowned ${fakeUi}`);
}

requireText(sharedStudio, 'export function createAssetTuningCapabilityState', "A6 can reuse the shared capability-state primitive");
requireText(sharedStudio, 'export function createAssetTuningStudio', "A6 can reuse the shared Studio shell once a production preview chain exists");

console.log("Space Typing Admin A6.0 Skills/Equipment capability boundary: PASS — gameplay authoring remains canonical; Drafts are child-preview validated; Media/VFX authoring stays fail-closed until migrated.");
