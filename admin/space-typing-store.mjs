import { AdminValidationError, RevisionStore } from "./store.mjs";
import { ShipPolicyValidationError, validateShipPolicy } from "./ship-policy.mjs";

export class SpaceTypingRevisionStore extends RevisionStore {
  validateConfig(config) {
    super.validateConfig(config);
    if (config.content === undefined) return config;
    if (config.content === null || typeof config.content !== "object" || Array.isArray(config.content)) {
      throw new AdminValidationError("content must be an object.");
    }
    for (const key of Object.keys(config.content)) {
      if (key !== "ships") {
        throw new AdminValidationError(`content.${key} is not supported by the current canonical schema.`);
      }
    }
    if (config.content.ships === undefined) return config;
    try {
      validateShipPolicy(config.content.ships, this.contract.ships);
    } catch (error) {
      if (error instanceof ShipPolicyValidationError) {
        throw new AdminValidationError(error.message);
      }
      throw error;
    }
    return config;
  }
}
