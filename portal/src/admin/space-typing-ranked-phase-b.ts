import { SpaceTypingAdminApi } from "./api";
import { renderAdminFailureState, setAdminStatus } from "./space-typing-admin-state";

const api = new SpaceTypingAdminApi();
type Tone = "good" | "warn" | "bad" | "info";
type RankedContractPayload = {
  contractRevision: string;
  schemaVersion: number;
  capability: "ranked.read";
  route: { id: string; path: string; label: string };
  ranked: {
    mode: "runtime-derived-readonly";
    runtimeSources: string[];
    authorableFields: string[];
    ruleset: {
      id: string;
      combatProfile: string;
      matchLengthSeconds: number;
      roundFormat: number;
      hazardLevel: string;
      mysteryFrequency: string;
      fateFrequency: string;
      modifier: string;
      allowPveStatScaling: boolean;
      allowPveLuckPity: boolean;
      allowCampaignCreditMinting: boolean;
      normalizedLoadoutBudget: number;
      mapPool: string[];
    };
    rating: { base: number; min: number; max: number; typingWeight: number; duelWeight: number; provisionalMatches: number; experiencedMatches: number; kFactors: number[] };
    matchmaking: { initialAllowedGap: number; gapIncreaseEverySeconds: number; gapIncrease: number; maxAllowedGap: number; reconnectGraceMs: number };
    profile: { fields: string[]; persistenceOwner: string; defaultStore: string; optionalStore: string; jsonStoreEnv: string };
    runtimeServices: string[];
    writeCapability: false;
    previewCapability: false;
    seasonService: false;
    rewardTableService: false;
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
function isRecord(value: unknown): value is Record<string, unknown> { return value !== null && typeof value === "object" && !Array.isArray(value); }
function stringArray(value: unknown): value is string[] { return Array.isArray(value) && value.every((item) => typeof item === "string"); }
function numberArray(value: unknown): value is number[] { return Array.isArray(value) && value.every((item) => typeof item === "number" && Number.isFinite(item)); }
function validateRankedContract(value: unknown): RankedContractPayload {
  if (!isRecord(value) || value["capability"] !== "ranked.read" || !isRecord(value["ranked"])) throw new Error("Ranked contract does not match ranked.read.");
  const ranked = value["ranked"];
  if (ranked["mode"] !== "runtime-derived-readonly") throw new Error("Ranked contract is not runtime-derived read-only.");
  for (const key of ["runtimeSources", "authorableFields", "runtimeServices", "unsupportedAdminMockFields"] as const) if (!stringArray(ranked[key])) throw new Error(`Ranked contract is missing ${key}.`);
  if (!isRecord(ranked["ruleset"]) || !isRecord(ranked["rating"]) || !isRecord(ranked["matchmaking"]) || !isRecord(ranked["profile"])) throw new Error("Ranked contract metadata is incomplete.");
  if (!stringArray(ranked["ruleset"]["mapPool"]) || !numberArray(ranked["rating"]["kFactors"]) || !stringArray(ranked["profile"]["fields"])) throw new Error("Ranked contract collections are invalid.");
  if (ranked["writeCapability"] !== false || ranked["previewCapability"] !== false || ranked["seasonService"] !== false || ranked["rewardTableService"] !== false) throw new Error("Ranked ownership boundary changed; re-audit required.");
  return value as unknown as RankedContractPayload;
}

export function renderPhaseBRanked(): HTMLElement {
  const page = el("div");
  const head = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(
    el("div", "st-admin-eyebrow", "PvP · Competitive Rules"),
    el("h1", undefined, "Ranked"),
    el("p", undefined, "Review the competitive rules players actually enter. Ranked is authority-owned and intentionally read-only in Admin; no season scheduler, reward table or enable switch is fabricated."),
  );
  const actions = el("div", "st-admin-page-actions");
  actions.append(badge("AUTHORITY-OWNED · READ ONLY", "good"), badge("NO SEASON SERVICE", "warn"));
  head.append(copy, actions);
  page.append(head);

  const status = notice("Loading canonical Ranked rules…");
  status.setAttribute("aria-live", "polite");
  const content = el("div");
  page.append(status, content);

  let generation = 0;
  const load = (): void => {
    const current = ++generation;
    setAdminStatus(status, "Loading canonical Ranked rules…", "loading");
    void api.requestJson<unknown>("/api/admin/space-typing/ranked/contract").then(validateRankedContract).then((payload) => {
      if (current !== generation) return;
      const ranked = payload.ranked;
      setAdminStatus(status, `${ranked.ruleset.id} · production competitive rules loaded · Admin writes closed.`, "success");
      content.replaceChildren();

      const rules = panel("Player-facing Ruleset", "The fixed production rules used for Ranked admission");
      const ruleGrid = el("div", "stx-grid");
      ruleGrid.append(
        notice(`${ranked.ruleset.matchLengthSeconds / 60} minute matches · Bo${ranked.ruleset.roundFormat}`, "good"),
        notice(`${ranked.ruleset.hazardLevel} hazard · ${ranked.ruleset.modifier} modifier`),
        notice(`Mystery ${ranked.ruleset.mysteryFrequency} · Fate ${ranked.ruleset.fateFrequency}`),
        notice(`Normalized loadout budget: ${ranked.ruleset.normalizedLoadoutBudget}`),
        notice(`Map pool: ${ranked.ruleset.mapPool.join(" · ")}`),
      );
      rules.append(ruleGrid);

      const fairness = panel("Competitive Fairness", "Campaign/economy advantages are intentionally excluded");
      fairness.append(
        notice(`Combat profile: ${ranked.ruleset.combatProfile}`, "good"),
        notice(`PvE stat scaling: ${ranked.ruleset.allowPveStatScaling ? "allowed" : "blocked"}`, ranked.ruleset.allowPveStatScaling ? "warn" : "good"),
        notice(`PvE luck / pity: ${ranked.ruleset.allowPveLuckPity ? "allowed" : "blocked"}`, ranked.ruleset.allowPveLuckPity ? "warn" : "good"),
        notice(`Campaign credit minting: ${ranked.ruleset.allowCampaignCreditMinting ? "allowed" : "blocked"}`, ranked.ruleset.allowCampaignCreditMinting ? "warn" : "good"),
      );

      const unavailable = panel("Unavailable Administration", "No canonical owner exists for these Live competitive controls");
      unavailable.append(
        badge("FAIL-CLOSED", "warn"),
        notice("Season dates, placement count overrides, tier thresholds, season rewards, player-distribution targets and Ranked enable toggles are unavailable."),
        notice(`Season service: ${String(ranked.seasonService)} · reward table service: ${String(ranked.rewardTableService)} · Admin write: ${String(ranked.writeCapability)}`, "warn"),
      );

      const advanced = el("details", "st-admin-panel solid stx-panel");
      advanced.append(el("summary", undefined, "Advanced rating, matchmaking & persistence details"));
      const body = el("div", "stx-grid");
      body.append(
        notice(`Rating ${ranked.rating.min}–${ranked.rating.max} · base ${ranked.rating.base} · ${Math.round(ranked.rating.typingWeight * 100)}% typing / ${Math.round(ranked.rating.duelWeight * 100)}% Duel`),
        notice(`K factors: ${ranked.rating.kFactors.join(" · ")} · provisional < ${ranked.rating.provisionalMatches} · experienced < ${ranked.rating.experiencedMatches}`),
        notice(`Matchmaking gap ${ranked.matchmaking.initialAllowedGap} → max ${ranked.matchmaking.maxAllowedGap}; +${ranked.matchmaking.gapIncrease} every ${ranked.matchmaking.gapIncreaseEverySeconds}s`),
        notice(`Reconnect grace: ${ranked.matchmaking.reconnectGraceMs / 1000}s`),
        notice(`Profile persistence: ${ranked.profile.persistenceOwner} · default ${ranked.profile.defaultStore} · optional ${ranked.profile.optionalStore}`),
        notice(`Runtime services: ${ranked.runtimeServices.join(" · ")}`),
        notice(`Runtime sources: ${ranked.runtimeSources.join(" · ")}`),
        notice(`Unsupported Admin fields: ${ranked.unsupportedAdminMockFields.join(" · ")}`, "warn"),
      );
      advanced.append(body);
      content.append(rules, fairness, unavailable, advanced);
    }).catch((error: unknown) => {
      if (current !== generation) return;
      setAdminStatus(status, "Ranked runtime contract is unavailable.", "error");
      renderAdminFailureState(content, {
        title: "Ranked unavailable",
        fallbackMessage: "The canonical Ranked contract could not be loaded.",
        error,
        onRetry: load,
      });
    });
  };
  load();
  return page;
}
