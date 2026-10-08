export const EQUIPMENT_RUNTIME_APPLY_BOUNDARY = "new-session";

export function createEquipmentRuntimeEnvelope(state, config) {
  return {
    applyBoundary: EQUIPMENT_RUNTIME_APPLY_BOUNDARY,
    activeRevision:
      typeof state?.activeRevision === "string" ? state.activeRevision : null,
    policy: config?.content?.equipment ?? null,
  };
}
