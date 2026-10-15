import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const child = resolve(root, "games/space-typing");
const read = (path) => readFile(resolve(root, path), "utf8");
const readChild = (path) => readFile(resolve(child, path), "utf8");

const [
  capabilities,
  skillPolicy,
  equipmentPolicy,
  skillWrapper,
  skillLegacy,
  equipmentWrapper,
  equipmentLegacy,
  skillRuntimePanel,
  equipmentRuntimePanel,
  sharedStudio,
  sharedHelp,
] = await Promise.all([
  readChild("src/admin/a6-skill-equipment-capabilities.ts"),
  readChild("src/admin/skill-runtime-policy.ts"),
  readChild("src/admin/equipment-runtime-policy.ts"),
  read("portal/src/admin/space-typing-skills-phase-b.ts"),
  read("portal/src/admin/space-typing-skills-phase-b-legacy.ts"),
  read("portal/src/admin/space-typing-equipment-phase-b.ts"),
  read("portal/src/admin/space-typing-equipment-phase-b-legacy.ts"),
  read("portal/src/admin/v2/preview/panels/system-runtime-preview.ts"),
  read("portal/src/admin/v2/preview/panels/equipment-runtime-preview.ts"),
  read("portal/src/admin/v2/asset-tuning-studio.ts"),
  read("portal/src/admin/v2/admin-help.ts"),
]);
const skillSurface = `${skillWrapper}\n${skillLegacy}`;
const equipmentSurface = `${equipmentWrapper}\n${equipmentLegacy}`;

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
]) requireText(capabilities, `id: "${id}"`, `A6 capability ${id} is registered`);
for (const status of ["SUPPORTED NOW", "REQUIRES CANONICAL MIGRATION", "READ-ONLY REFERENCE", "DEFERRED / UNSUPPORTED"]) {
  requireText(capabilities, `status: "${status}"`, `A6 capability matrix preserves ${status}`);
}

requireText(skillPolicy, "const AUTHORABLE_KEYS = new Set([", "Skill policy owns an explicit allow-list");
for (const field of ["name", "description", "energyCost", "cooldown", "charges", "perStageLimit", "typingCondition"]) {
  requireText(skillPolicy, `"${field}"`, `Skill field ${field} remains canonical`);
}
requireText(skillPolicy, "applySkillRuntimeOverride", "Skill policy reaches production definitions");
requireText(equipmentPolicy, 'const AUTHORABLE_KEYS = new Set(["name", "description", "stats", "perk"])', "Equipment policy keeps its explicit allow-list");
requireText(equipmentPolicy, "materializeEquipmentRuntimeSession", "Equipment policy materializes published overrides");
requireText(equipmentPolicy, "activeEquipmentRuntimeOverride", "Equipment runtime exposes the active canonical override");

for (const fakeField of ["effectPreset", "effectAssetVersionId", "vfxAssetVersionId", "sfxAssetVersionId", "mediaAssetVersionId", "iconAssetVersionId", "imageAssetVersionId"]) {
  forbidText(skillPolicy, fakeField, `Skill policy must not invent ${fakeField}`);
  forbidText(equipmentPolicy, fakeField, `Equipment policy must not invent ${fakeField}`);
}

// A10.5 wraps the stable authoring editors with production-runtime panels.
requireText(skillWrapper, "renderLegacySkills", "Skills retain the established authoring editor");
requireText(skillWrapper, "createSkillProductionRuntimePanel", "Skills attach the production SkillEngine panel");
requireText(equipmentWrapper, "renderLegacyEquipment", "Equipment retain the established authoring editor");
requireText(equipmentWrapper, "createEquipmentProductionRuntimePanel", "Equipment attach the production equipment resolver panel");

for (const [surface, previewCall, name] of [
  [skillSurface, "const validated = await previewSkills(policy)", "Skills"],
  [equipmentSurface, "const validated = await previewEquipment(policy)", "Equipment"],
]) {
  requireText(surface, previewCall, `${name} validate candidates through the canonical child preview`);
  requireText(surface, "api.createRevision", `${name} keep immutable Draft creation`);
  requireText(surface, "Publish from History to activate it", `${name} keep activation centralized in History`);
  forbidText(surface, "api.publish(", `${name} editor cannot bypass History with direct publish`);
  requireText(surface, "createAssetTuningCapabilityState", `${name} use shared capability states`);
  requireText(surface, "AdminHelpScope, createAdminFieldShell", `${name} retain shared field-help primitives`);
  requireText(surface, "helpScope.observeRoot(page)", `${name} clean help resources on route detach`);
}
for (const [surface, labels, name] of [
  [skillSurface, ["Gameplay Policy", "Media / VFX"], "Skills"],
  [equipmentSurface, ["Gameplay Policy", "Registry Icon", "Media Binding", "VFX / SFX"], "Equipment"],
]) {
  for (const label of labels) requireText(surface, `label: "${label}"`, `${name} expose ${label}`);
}
requireText(skillSurface, 'status: "AVAILABLE"', "Skills expose proven gameplay authoring as available");
requireText(skillSurface, 'status: "REQUIRES CANONICAL MIGRATION"', "Skills keep Media/VFX migration-gated");
requireText(equipmentSurface, 'status: "READ-ONLY REFERENCE"', "Equipment keep registry presentation read-only");
requireText(equipmentSurface, 'status: "REQUIRES CANONICAL MIGRATION"', "Equipment keep Media migration-gated");
requireText(equipmentSurface, 'status: "DEFERRED / UNSUPPORTED"', "Equipment keep generic VFX/SFX authoring closed");

requireText(sharedHelp, "export function createAdminFieldShell", "Shared V2 help exposes field shells");
requireText(sharedHelp, "export class AdminHelpScope", "Shared V2 help exposes lifecycle-scoped tooltips");
requireText(sharedStudio, "export function createAssetTuningCapabilityState", "A6 retains shared capability-state primitive");
requireText(sharedStudio, "export function createAssetTuningStudio", "Shared Studio remains available for production-backed domains");

// Each wrapper must hit the child-owned production behavior actually used by gameplay.
for (const token of ["SkillEngine", "runtimePreview", "energyBefore", "energyAfter", "Draft candidate executed through production SkillEngine", "/api/admin/space-typing/skills/preview"]) {
  requireText(skillRuntimePanel, token, `Skill production runtime evidence ${token}`);
}
for (const token of ["resolveEquipmentPerks", "perkEffects", "Effective stats", "Draft candidate resolved through production equipment perks", "/api/admin/space-typing/equipment/preview"]) {
  requireText(equipmentRuntimePanel, token, `Equipment production runtime evidence ${token}`);
}
// Numeric one is a real effect for non-multiplier perks such as stageBlocks.
requireText(equipmentRuntimePanel, "MULTIPLIER_EFFECTS.has(key) ? value !== 1 : value !== 0", "Equipment preview distinguishes multiplier baseline 1 from real numeric effect 1");

for (const fakeUi of ["effectPreset", "vfxAssetVersionId", "sfxAssetVersionId", "iconAssetVersionId", "imageAssetVersionId"]) {
  forbidText(skillSurface, fakeUi, `Skills UI must not expose unowned ${fakeUi}`);
  forbidText(equipmentSurface, fakeUi, `Equipment UI must not expose unowned ${fakeUi}`);
}

console.log("Space Typing Admin A6: PASS — Skills/Equipment preserve canonical Draft authoring and capability gates while A10.5 wrappers exercise child-owned SkillEngine/equipment resolver previews.");
