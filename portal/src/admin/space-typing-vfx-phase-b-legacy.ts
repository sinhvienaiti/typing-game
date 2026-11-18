import { SpaceTypingAdminApi } from "./api";
import { renderAdminFailureState, setAdminStatus } from "./space-typing-admin-state";

const api = new SpaceTypingAdminApi();
type Tone = "good" | "warn" | "bad" | "info";
type VisualQuality = "low" | "medium" | "high" | "ultra";
type QualityProfile = {
  dprCap: number;
  particleScale: number;
  maxParticles: number;
  minStars: number;
  maxStars: number;
  starAreaDivisor: number;
  glowScale: number;
  gridStep: number;
  maxCanvasPixels: number;
};
type VfxContractPayload = {
  contractRevision: string;
  schemaVersion: number;
  capability: "vfx.read";
  route: { id: string; path: string; label: string };
  vfx: {
    mode: "runtime-derived-readonly";
    runtimeSources: string[];
    runtimeOwner: string;
    qualityTiers: VisualQuality[];
    qualityProfiles: Record<VisualQuality, QualityProfile>;
    combatFxLimits: { maxParticles: number; maxRings: number };
    combatEvents: string[];
    domains: string[];
    skillQualityDetailTier: Record<VisualQuality, number>;
    dataFlow: string;
    persistenceOwner: string;
    authorableFields: string[];
    writeCapability: false;
    adminPreviewWriteCapability: false;
    applyBoundary: "none";
    unsupportedAdminMockFields: string[];
  };
};

function el<K extends keyof HTMLElementTagNameMap>(tag: K, cls?: string, text?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (cls) node.className = cls;
  if (text !== undefined) node.textContent = text;
  return node;
}
function badge(label: string, tone: Tone = "info"): HTMLElement { return el("span", `st-admin-status ${tone}`, label); }
function notice(text: string, tone: Tone = "info"): HTMLElement { return el("div", `stx-notice ${tone}`, text); }
function panel(title: string, subtitle?: string): HTMLElement {
  const root = el("section", "st-admin-panel solid stx-panel");
  const head = el("div", "st-admin-panel-head");
  const copy = el("div");
  copy.append(el("h2", undefined, title));
  if (subtitle) copy.append(el("p", undefined, subtitle));
  head.append(copy);
  root.append(head);
  return root;
}
function listNotice(label: string, values: readonly string[], tone: Tone = "info"): HTMLElement {
  return notice(`${label}: ${values.join(" · ") || "none exposed"}`, tone);
}
function isRecord(value: unknown): value is Record<string, unknown> {
  return value !== null && typeof value === "object" && !Array.isArray(value);
}
function validateVfxContract(value: unknown): VfxContractPayload {
  if (!isRecord(value) || value["capability"] !== "vfx.read" || !isRecord(value["route"]) || !isRecord(value["vfx"])) {
    throw new Error("VFX response does not match the canonical vfx.read contract.");
  }
  const vfx = value["vfx"];
  if (
    vfx["mode"] !== "runtime-derived-readonly" ||
    !Array.isArray(vfx["runtimeSources"]) ||
    !Array.isArray(vfx["qualityTiers"]) ||
    !Array.isArray(vfx["combatEvents"]) ||
    !Array.isArray(vfx["domains"]) ||
    !Array.isArray(vfx["authorableFields"]) ||
    !Array.isArray(vfx["unsupportedAdminMockFields"]) ||
    !isRecord(vfx["qualityProfiles"]) ||
    !isRecord(vfx["skillQualityDetailTier"]) ||
    !isRecord(vfx["combatFxLimits"]) ||
    typeof vfx["runtimeOwner"] !== "string" ||
    typeof vfx["dataFlow"] !== "string" ||
    typeof vfx["persistenceOwner"] !== "string"
  ) {
    throw new Error("VFX response is missing required runtime ownership or quality data.");
  }
  const limits = vfx["combatFxLimits"];
  if (typeof limits["maxParticles"] !== "number" || typeof limits["maxRings"] !== "number") {
    throw new Error("VFX response is missing canonical CombatFx limits.");
  }
  for (const tier of vfx["qualityTiers"]) {
    if (typeof tier !== "string" || !isRecord(vfx["qualityProfiles"][tier]) || typeof vfx["skillQualityDetailTier"][tier] !== "number") {
      throw new Error(`VFX response is missing the ${String(tier)} quality profile.`);
    }
  }
  return value as unknown as VfxContractPayload;
}
async function fetchVfxContract(): Promise<VfxContractPayload> {
  return validateVfxContract(await api.requestJson<unknown>("/api/admin/space-typing/vfx/contract"));
}

export function renderPhaseBVfx(): HTMLElement {
  const page = el("div");
  const head = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(
    el("div", "st-admin-eyebrow", "Visuals · Production VFX Runtime"),
    el("h1", undefined, "VFX"),
    el("p", undefined, "Inspect production combat, projectile, skill, boss and screen-feedback VFX together with their canonical quality budgets. Tuning remains code-owned until a real apply boundary exists."),
  );
  const actions = el("div", "st-admin-page-actions");
  actions.append(
    badge("RUNTIME-BACKED · READ ONLY", "good"),
    badge("CODE-OWNED TUNING", "info"),
    badge("NO FAKE VFX PROFILE", "warn"),
  );
  head.append(copy, actions);
  page.append(head);

  const status = notice("Loading canonical VFX runtime contract…");
  status.setAttribute("aria-live", "polite");
  const content = el("div");
  page.append(status, content);

  let loadGeneration = 0;
  const load = (): void => {
    const generation = ++loadGeneration;
    setAdminStatus(status, "Loading canonical VFX runtime contract…", "loading");
    content.replaceChildren(notice("Loading production VFX ownership and quality budgets…", "info"));

    void fetchVfxContract().then((payload) => {
      if (generation !== loadGeneration) return;
      const vfx = payload.vfx;
      setAdminStatus(status, `${vfx.domains.length} runtime domains · ${vfx.combatEvents.length} combat event classes · Admin writes closed.`, "success");

      const ownership = panel("Runtime Ownership", "The child gameplay runtime remains the only source of truth");
      ownership.append(
        notice(`Owner: ${vfx.runtimeOwner}`, "good"),
        notice(`Data flow: ${vfx.dataFlow}`),
        listNotice("Runtime sources", vfx.runtimeSources),
        listNotice("VFX domains", vfx.domains),
      );

      const quality = panel("Visual Quality Profiles", "Canonical Low / Medium / High / Ultra performance budgets");
      for (const tier of vfx.qualityTiers) {
        const profile = vfx.qualityProfiles[tier];
        const detail = vfx.skillQualityDetailTier[tier];
        quality.append(notice(`${tier.toUpperCase()}: DPR ≤ ${profile.dprCap} · particles ×${profile.particleScale} · max particles ${profile.maxParticles} · stars ${profile.minStars}–${profile.maxStars} · glow ×${profile.glowScale} · grid ${profile.gridStep} · canvas ≤ ${profile.maxCanvasPixels.toLocaleString()} px · skill detail ${detail}`));
      }

      const combat = panel("Combat VFX Surface", "Events actually emitted into production VFX systems");
      combat.append(
        notice(`CombatFx hard limits: ${vfx.combatFxLimits.maxParticles} particles · ${vfx.combatFxLimits.maxRings} rings`, "good"),
        listNotice("Combat events", vfx.combatEvents),
        notice("Projectile, explosion, skill, boss and screen-feedback effects are rendered by gameplay systems rather than an Admin-authored profile."),
      );

      const boundary = panel("Admin Boundary", "No canonical VFX persistence/apply seam exists today");
      boundary.append(
        notice(`Persistence owner: ${vfx.persistenceOwner}`),
        notice(`Apply boundary: ${vfx.applyBoundary}`),
        notice(`Admin write capability: ${String(vfx.writeCapability)}`, "warn"),
        notice(`Admin preview write capability: ${String(vfx.adminPreviewWriteCapability)}`, "warn"),
        listNotice("Authorable fields", vfx.authorableFields.length > 0 ? vfx.authorableFields : ["none"], "warn"),
        listNotice("Unsupported legacy mock controls", vfx.unsupportedAdminMockFields, "warn"),
        notice("NO FAKE VFX PROFILE: scale, intensity, duration, opacity, blend and screen-shake controls stay locked until a real child config consumer and safe apply boundary exist."),
      );

      content.replaceChildren(ownership, quality, combat, boundary);
    }).catch((error: unknown) => {
      if (generation !== loadGeneration) return;
      setAdminStatus(status, "VFX service unavailable.", "error");
      renderAdminFailureState(content, {
        title: "VFX unavailable",
        fallbackMessage: "Unable to load the canonical VFX runtime contract.",
        error,
        onRetry: load,
      });
    });
  };

  load();
  return page;
}
