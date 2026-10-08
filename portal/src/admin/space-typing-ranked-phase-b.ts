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
  if (payload.capability !== "ranked.read" || !payload.ranked || !payload.route) {
    throw new Error("Pinned child Ranked contract does not expose ranked.read.");
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
    el("p", undefined, "Inspect the canonical Ranked ruleset, rating policy, matchmaking expansion and profile persistence used by the Duel authority. The current runtime has no season scheduler or Admin-owned competitive policy store, so authoring remains closed."),
  );
  const actions = el("div", "st-admin-page-actions");
  actions.append(badge("RUNTIME-BACKED · READ ONLY", "good"), badge("NO SEASON SERVICE", "warn"));
  head.append(copy, actions);
  page.append(head);

  const status = notice("Loading canonical Ranked runtime contract…");
  page.append(status);
  void (async () => {
    try {
      const payload = await fetchRankedContract();
      const ranked = payload.ranked;
      status.className = "stx-notice good";
      status.textContent = `${ranked.ruleset.id} · ${ranked.profile.persistenceOwner} · Admin writes closed.`;

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
        notice("Season dates, placement count, free-form matchmaking spread, enable toggles, rank-tier thresholds, season rewards and player-distribution percentages are not canonical runtime config and are intentionally unavailable."),
      );

      page.append(rules, rating, matchmaking, persistence, boundary);
    } catch (error: unknown) {
      status.className = "stx-notice bad";
      status.textContent = `Ranked contract unavailable: ${error instanceof Error ? error.message : String(error)}`;
    }
  })();
  return page;
}
