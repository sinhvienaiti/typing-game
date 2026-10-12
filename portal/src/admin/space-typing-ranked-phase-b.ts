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
    rating: {
      base: number;
      min: number;
      max: number;
      typingWeight: number;
      duelWeight: number;
      provisionalMatches: number;
      experiencedMatches: number;
      kFactors: number[];
    };
    matchmaking: {
      initialAllowedGap: number;
      gapIncreaseEverySeconds: number;
      gapIncrease: number;
      maxAllowedGap: number;
      reconnectGraceMs: number;
    };
    profile: {
      fields: string[];
      persistenceOwner: string;
      defaultStore: string;
      optionalStore: string;
      jsonStoreEnv: string;
    };
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
function listNotice(label: string, values: readonly (string | number)[], tone: Tone = "info"): HTMLElement {
  return notice(`${label}: ${values.length ? values.join(" · ") : "none exposed"}`, tone);
}
function scalar(label: string, value: string | number | boolean, tone: Tone = "info"): HTMLElement {
  return notice(`${label}: ${String(value)}`, tone);
}
function isRecord(value: unknown): value is Record<string, unknown> {
  return value !== null && typeof value === "object" && !Array.isArray(value);
}
function stringArray(value: unknown): value is string[] { return Array.isArray(value) && value.every((item) => typeof item === "string"); }
function numberArray(value: unknown): value is number[] { return Array.isArray(value) && value.every((item) => typeof item === "number" && Number.isFinite(item)); }

function validateRankedContract(value: unknown): RankedContractPayload {
  if (!isRecord(value) || value["capability"] !== "ranked.read" || !isRecord(value["ranked"]) || !isRecord(value["route"])) {
    throw new Error("Ranked contract does not match the canonical ranked.read boundary.");
  }
  const ranked = value["ranked"];
  if (ranked["mode"] !== "runtime-derived-readonly") throw new Error("Ranked contract is not runtime-derived read-only.");
  for (const key of ["runtimeSources", "authorableFields", "runtimeServices", "unsupportedAdminMockFields"] as const) {
    if (!stringArray(ranked[key])) throw new Error(`Ranked contract is missing ${key}.`);
  }
  if (!isRecord(ranked["ruleset"]) || !isRecord(ranked["rating"]) || !isRecord(ranked["matchmaking"]) || !isRecord(ranked["profile"])) {
    throw new Error("Ranked contract is missing ruleset, rating, matchmaking or profile metadata.");
  }
  const ruleset = ranked["ruleset"];
  const rating = ranked["rating"];
  const profile = ranked["profile"];
  if (!stringArray(ruleset["mapPool"]) || !numberArray(rating["kFactors"]) || !stringArray(profile["fields"])) {
    throw new Error("Ranked contract contains invalid ruleset/rating/profile collections.");
  }
  if (ranked["writeCapability"] !== false || ranked["previewCapability"] !== false || ranked["seasonService"] !== false || ranked["rewardTableService"] !== false) {
    throw new Error("Ranked contract contains an invalid fail-closed Admin boundary.");
  }
  return value as unknown as RankedContractPayload;
}

async function fetchRankedContract(): Promise<RankedContractPayload> {
  return validateRankedContract(await api.requestJson<unknown>("/api/admin/space-typing/ranked/contract"));
}

export function renderPhaseBRanked(): HTMLElement {
  const page = el("div");
  const head = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(
    el("div", "st-admin-eyebrow", "PvP · Ranked Authority"),
    el("h1", undefined, "Ranked"),
    el("p", undefined, "Inspect the canonical Ranked ruleset, rating policy, matchmaking expansion and profile persistence used by the Duel authority. The current runtime has no season scheduler or Admin-owned competitive policy store, so authoring remains closed."),
  );
  const actions = el("div", "st-admin-page-actions");
  actions.append(badge("RUNTIME-BACKED · READ ONLY", "good"), badge("NO SEASON SERVICE", "warn"));
  head.append(copy, actions);
  page.append(head);

  const status = notice("Loading canonical Ranked runtime contract…");
  status.setAttribute("aria-live", "polite");
  const content = el("div");
  page.append(status, content);

  let loadGeneration = 0;
  const load = (): void => {
    const generation = ++loadGeneration;
    setAdminStatus(status, "Loading canonical Ranked runtime contract…", "loading");
    content.replaceChildren(notice("Loading Ranked authority rules…", "info"));
    void fetchRankedContract().then((payload) => {
      if (generation !== loadGeneration) return;
      const ranked = payload.ranked;
      setAdminStatus(status, `${ranked.ruleset.id} · ${ranked.profile.persistenceOwner} · Admin writes closed.`, "success");
      content.replaceChildren();

      const rules = panel("Canonical Ruleset", "Code-owned DUEL_RANKED_RULESET");
      rules.append(
        scalar("Ruleset", ranked.ruleset.id, "good"),
        scalar("Combat profile", ranked.ruleset.combatProfile),
        scalar("Match length", `${ranked.ruleset.matchLengthSeconds}s`),
        scalar("Round format", `Bo${ranked.ruleset.roundFormat}`),
        scalar("Hazard", ranked.ruleset.hazardLevel),
        scalar("Mystery frequency", ranked.ruleset.mysteryFrequency),
        scalar("Fate frequency", ranked.ruleset.fateFrequency),
        scalar("Modifier", ranked.ruleset.modifier),
        scalar("Normalized loadout budget", ranked.ruleset.normalizedLoadoutBudget),
        listNotice("Map pool", ranked.ruleset.mapPool),
        scalar("PvE stat scaling", ranked.ruleset.allowPveStatScaling, "good"),
        scalar("PvE luck/pity", ranked.ruleset.allowPveLuckPity, "good"),
        scalar("Campaign credit minting", ranked.ruleset.allowCampaignCreditMinting, "good"),
      );

      const rating = panel("Rating Policy", "Canonical dual typing + Duel rating model");
      rating.append(
        scalar("Base rating", ranked.rating.base),
        scalar("Rating range", `${ranked.rating.min}–${ranked.rating.max}`),
        scalar("Matchmaking rating mix", `${Math.round(ranked.rating.typingWeight * 100)}% typing · ${Math.round(ranked.rating.duelWeight * 100)}% Duel`, "good"),
        scalar("Provisional boundary", `< ${ranked.rating.provisionalMatches} matches`),
        scalar("Experienced boundary", `< ${ranked.rating.experiencedMatches} matches`),
        listNotice("K factors", ranked.rating.kFactors),
      );

      const matchmaking = panel("Matchmaking & Presence", "Queue gap expands with wait time; disconnects use authority grace");
      matchmaking.append(
        scalar("Initial allowed gap", ranked.matchmaking.initialAllowedGap),
        scalar("Gap growth", `+${ranked.matchmaking.gapIncrease} every ${ranked.matchmaking.gapIncreaseEverySeconds}s`),
        scalar("Maximum allowed gap", ranked.matchmaking.maxAllowedGap),
        scalar("Reconnect grace", `${ranked.matchmaking.reconnectGraceMs / 1000}s`),
      );

      const persistence = panel("Profile Persistence", "Server-owned Ranked profile state");
      persistence.append(
        listNotice("Profile fields", ranked.profile.fields),
        scalar("Persistence owner", ranked.profile.persistenceOwner, "good"),
        scalar("Default store", ranked.profile.defaultStore),
        scalar("Optional store", ranked.profile.optionalStore),
        scalar("JSON store env", ranked.profile.jsonStoreEnv),
        listNotice("Runtime services", ranked.runtimeServices),
        listNotice("Runtime sources", ranked.runtimeSources),
      );

      const boundary = panel("Admin Boundary", "No synthetic season or reward authoring");
      boundary.append(
        scalar("Season service", ranked.seasonService, "warn"),
        scalar("Reward table service", ranked.rewardTableService, "warn"),
        scalar("Admin write capability", ranked.writeCapability, "warn"),
        scalar("Admin preview capability", ranked.previewCapability, "warn"),
        listNotice("Unsupported legacy mock fields", ranked.unsupportedAdminMockFields, "warn"),
        notice("Season dates, placement count, free-form matchmaking spread, enable toggles, rank-tier thresholds, season rewards and player-distribution percentages are intentionally unavailable because no canonical owner exists."),
      );
      content.append(rules, rating, matchmaking, persistence, boundary);
    }).catch((error: unknown) => {
      if (generation !== loadGeneration) return;
      setAdminStatus(status, "Ranked runtime contract is unavailable.", "error");
      renderAdminFailureState(content, {
        title: "Ranked unavailable",
        fallbackMessage: "The canonical Ranked contract could not be loaded. Check the local Admin runtime and try again.",
        error,
        onRetry: load,
      });
    });
  };

  load();
  return page;
}
