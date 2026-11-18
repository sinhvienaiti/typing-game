export const SHOP_RUNTIME_APPLY_BOUNDARY = "new-session+new-shop-instance";

export function createShopRuntimeEnvelope(state, config) {
  return {
    applyBoundary: SHOP_RUNTIME_APPLY_BOUNDARY,
    activeRevision:
      typeof state?.activeRevision === "string" ? state.activeRevision : null,
    policy: config?.economy?.shop ?? null,
  };
}
