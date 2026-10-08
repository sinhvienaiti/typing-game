import { SpaceTypingAdminApi } from "./api";

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
  return notice(`${label}: ${values.join(" · ")}`, tone);
}
async function fetchVfxContract(): Promise<VfxContractPayload> {
  const response = await fetch("/api/admin/space-typing/vfx/contract", {
    cache: "no-store",
    headers: { "x-typing-game-admin-token": api.getToken() },
  });
  const payload = (await response.json().catch(() => ({}))) as Partial<VfxContractPayload> & { message?: string };
  if (!response.ok) throw new Error(payload.message ?? `VFX contract request failed (${response.status})`);
  if (payload.capability !== "vfx.read" || !payload.vfx || !payload.route) {
    throw new Error("Pinned child VFX contract does not expose vfx.read.");
  }
  return payload as VfxContractPayload;
}

export function renderPhaseBVfx(): HTMLElement {
  const page = el("div");
  const head = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(
    el("div", "st-admin-eyebrow", "Visuals · Production VFX Runtime"),
    el("h1", undefined, "VFX"),
    el("p", undefined, "Inspect the production combat, projectile, skill, boss and screen-feedback VFX systems together with their canonical quality budgets. Current VFX tuning is code-owned; Admin intentionally has no write/apply boundary."),
  );
  const actions = el("div", "st-admin-page-actions");
  actions.append(badge("RUNTIME-BACKED · READ ONLY", "good"), badge("NO FAKE VFX PROFILE", "warn"));
  head.append(copy, actions);
  page.append(head);

  const status = notice("Loading canonical VFX runtime contract…");
  page.append(status);
  void (async () => {
    try {
      const payload = await fetchVfxContract();
      const vfx = payload.vfx;
      status.className = "stx-notice good";
      status.textContent = `${vfx.domains.length} runtime domains · ${vfx.combatEvents.length} combat event classes · Admin writes closed.`;

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
        quality.append(notice(`${tier.toUpperCase()}: DPR ≤ ${profile.dprCap} · particles ×${profile.particleScale} · max particles ${profile.maxParticles} · stars ${profile.minStars}–${profile.maxStars} · glow ×${profile.glowScale} · grid ${profile.gridStep} · canvas ≤ ${profile.maxCanvasPixels.toLocaleString()} px · skill detail ${vfx.skillQualityDetailTier[tier]}`));
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
        notice("Scale, intensity, duration, opacity, blend and screen-shake controls stay locked until a real child config consumer and safe apply boundary exist."),
      );

      page.append(ownership, quality, combat, boundary);
    } catch (error: unknown) {
      status.className = "stx-notice bad";
      status.textContent = `VFX contract unavailable: ${error instanceof Error ? error.message : String(error)}`;
    }
  })();
  return page;
}
