import { SpaceTypingAdminApi } from "./api";

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
    history: {
      available: true;
      mode: "persisted-authoritative-readonly";
      adminSurfaceOwner: string;
      queryServiceOwner: string;
      queryServiceAvailable: true;
      productionTransportExposed: false;
      parentAdminQueryBridge: false;
      defaultScope: "self";
      crossPlayerScope: "authorized-cross-player";
      authenticationRequired: true;
      crossPlayerAuthorizationRequired: true;
      crossPlayerFailClosedWhenUnconfigured: true;
      eventFilters: string[];
      writeCapability: false;
    };
    writeCapability: false;
    previewCapability: false;
    seasonService: false;
    rewardTableService: false;
    unsupportedAdminMockFields: string[];
    unsupportedAdminOperations: string[];
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
  return notice(`${label}: ${values.join(" · ")}`, tone);
}
function scalar(label: string, value: string | number | boolean, tone: Tone = "info"): HTMLElement {
  return notice(`${label}: ${String(value)}`, tone);
}
async function fetchRankedContract(): Promise<RankedContractPayload> {
  const response = await fetch("/api/admin/space-typing/ranked/contract", {
    cache: "no-store",
    headers: { "x-typing-game-admin-token": api.getToken() },
  });
  const payload = (await response.json().catch(() => ({}))) as Partial<RankedContractPayload> & { message?: string };
  if (!response.ok) throw new Error(payload.message ?? `Ranked contract request failed (${response.status})`);
  if (
    payload.capability !== "ranked.read" ||
    !payload.ranked ||
    payload.ranked.history?.queryServiceAvailable !== true ||
    payload.ranked.history?.productionTransportExposed !== false ||
    payload.ranked.history?.parentAdminQueryBridge !== false ||
    !payload.route
  ) {
    throw new Error("Pinned child Ranked contract does not expose the canonical read-only service/transport boundary.");
  }
  return payload as RankedContractPayload;
}

export function renderPhaseBRanked(): HTMLElement {
  const page = el("div");
  const head = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(
    el("div", "st-admin-eyebrow", "PvP · Ranked Authority"),
    el("h1", undefined, "Ranked"),
    el("p", undefined, "Inspect canonical Ranked rules and the persisted history service boundary. History auth logic exists, but the production Duel transport and Parent Admin query bridge do not expose that data yet."),
  );
  const actions = el("div", "st-admin-page-actions");
  actions.append(
    badge("RUNTIME-BACKED · READ ONLY", "good"),
    badge("HISTORY SERVICE · READ ONLY", "good"),
    badge("HISTORY TRANSPORT · NOT EXPOSED", "warn"),
    badge("NO SEASON SERVICE", "warn"),
  );
  head.append(copy, actions);
  page.append(head);

  const status = notice("Loading canonical Ranked runtime contract…");
  page.append(status);
  void (async () => {
    try {
      const payload = await fetchRankedContract();
      const ranked = payload.ranked;
      status.className = "stx-notice good";
      status.textContent = `${ranked.ruleset.id} · ${ranked.profile.persistenceOwner} · history service present · Parent query bridge closed · Admin writes closed.`;

      const rules = panel("Canonical Ruleset", "Code-owned DUEL_RANKED_RULESET");
      rules.append(
        scalar("Ruleset", ranked.ruleset.id, "good"),
        scalar("Combat profile", ranked.ruleset.combatProfile),
        scalar("Match length", `${ranked.ruleset.matchLengthSeconds}s`),
        scalar("Round format", `Bo${ranked.ruleset.roundFormat}`),
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
        scalar("Rating mix", `${Math.round(ranked.rating.typingWeight * 100)}% typing · ${Math.round(ranked.rating.duelWeight * 100)}% Duel`, "good"),
        listNotice("K factors", ranked.rating.kFactors),
      );

      const persistence = panel("Profile Persistence", "Server-owned Ranked profile state");
      persistence.append(
        listNotice("Profile fields", ranked.profile.fields),
        scalar("Persistence owner", ranked.profile.persistenceOwner, "good"),
        scalar("Default store", ranked.profile.defaultStore),
        scalar("Optional store", ranked.profile.optionalStore),
        listNotice("Runtime services", ranked.runtimeServices),
      );

      const history = panel("Ranked History", "Persisted service exists · production Parent query bridge not exposed");
      history.append(
        scalar("History service available", ranked.history.queryServiceAvailable, "good"),
        scalar("Mode", ranked.history.mode),
        scalar("Production transport exposed", ranked.history.productionTransportExposed, "warn"),
        scalar("Parent Admin query bridge", ranked.history.parentAdminQueryBridge, "warn"),
        scalar("Default service scope", ranked.history.defaultScope),
        scalar("Authentication required", ranked.history.authenticationRequired, "good"),
        scalar("Cross-player authorization required", ranked.history.crossPlayerAuthorizationRequired, "warn"),
        scalar("Fail closed when unconfigured", ranked.history.crossPlayerFailClosedWhenUnconfigured, "good"),
        listNotice("Event filters", ranked.history.eventFilters),
        notice("Admin reports the real service/auth capability only. It does not display synthetic Ranked history or bypass the missing production query transport.", "warn"),
      );

      const boundary = panel("Admin Boundary", "No synthetic season, settlement or history mutation");
      boundary.append(
        scalar("Season service", ranked.seasonService, "warn"),
        scalar("Reward table service", ranked.rewardTableService, "warn"),
        scalar("Admin write capability", ranked.writeCapability, "warn"),
        scalar("Admin preview capability", ranked.previewCapability, "warn"),
        listNotice("Unsupported legacy mock fields", ranked.unsupportedAdminMockFields, "warn"),
        listNotice("Unsupported operations", ranked.unsupportedAdminOperations, "warn"),
      );

      page.append(rules, rating, persistence, history, boundary);
    } catch (error: unknown) {
      status.className = "stx-notice bad";
      status.textContent = `Ranked contract unavailable: ${error instanceof Error ? error.message : String(error)}`;
    }
  })();
  return page;
}
