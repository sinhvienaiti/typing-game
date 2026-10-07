import { AdminValidationError, RevisionStore } from "./store.mjs";
import { ShipPolicyValidationError, validateShipPolicy } from "./ship-policy.mjs";
import { EquipmentPolicyValidationError, validateEquipmentPolicy } from "./equipment-policy.mjs";
import { SkillPolicyValidationError, validateSkillPolicy } from "./skill-policy.mjs";
import { EnemyPolicyValidationError, validateEnemyPolicy } from "./enemy-policy.mjs";
import { BossPolicyValidationError, validateBossPolicy } from "./boss-policy.mjs";
import { StagePolicyValidationError, validateStagePolicy } from "./stage-policy.mjs";

export class SpaceTypingRevisionStore extends RevisionStore {
  validateConfig(config) {
    super.validateConfig(config);
    if (config.content === undefined) return config;
    if (config.content === null || typeof config.content !== "object" || Array.isArray(config.content)) {
      throw new AdminValidationError("content must be an object.");
    }
    for (const key of Object.keys(config.content)) {
      if (!["ships", "equipment", "skills", "enemies", "bosses", "stages"].includes(key)) {
        throw new AdminValidationError(`content.${key} is not supported by the current canonical schema.`);
      }
    }

    if (config.content.ships !== undefined) {
      try { validateShipPolicy(config.content.ships, this.contract.ships); }
      catch (error) { if (error instanceof ShipPolicyValidationError) throw new AdminValidationError(error.message); throw error; }
    }
    if (config.content.equipment !== undefined) {
      try { validateEquipmentPolicy(config.content.equipment, this.contract.equipment); }
      catch (error) { if (error instanceof EquipmentPolicyValidationError) throw new AdminValidationError(error.message); throw error; }
    }
    if (config.content.skills !== undefined) {
      try { validateSkillPolicy(config.content.skills, this.contract.skills); }
      catch (error) { if (error instanceof SkillPolicyValidationError) throw new AdminValidationError(error.message); throw error; }
    }
    if (config.content.enemies !== undefined) {
      try { validateEnemyPolicy(config.content.enemies, this.contract.enemies); }
      catch (error) { if (error instanceof EnemyPolicyValidationError) throw new AdminValidationError(error.message); throw error; }
    }
    if (config.content.bosses !== undefined) {
      try { validateBossPolicy(config.content.bosses, this.contract.bosses); }
      catch (error) { if (error instanceof BossPolicyValidationError) throw new AdminValidationError(error.message); throw error; }
    }
    if (config.content.stages !== undefined) {
      try { validateStagePolicy(config.content.stages, this.contract.stages); }
      catch (error) { if (error instanceof StagePolicyValidationError) throw new AdminValidationError(error.message); throw error; }
    }
    return config;
  }
}
