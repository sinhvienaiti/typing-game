export const SHIP_RUNTIME_APPLY_BOUNDARY = "new-session";

export function createShipRuntimeEnvelope(state, config) {
  return {
    applyBoundary: SHIP_RUNTIME_APPLY_BOUNDARY,
    activeRevision:
      typeof state?.activeRevision === "string" ? state.activeRevision : null,
    policy: config?.content?.ships ?? null,
  };
}
