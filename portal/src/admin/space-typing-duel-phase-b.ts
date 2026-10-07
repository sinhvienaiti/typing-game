import { SpaceTypingAdminApi } from "./api";

const api = new SpaceTypingAdminApi();
type Tone = "good" | "warn" | "bad" | "info";
type DuelContractPayload = {
  contractRevision: string;
  schemaVersion: number;
  capability: "duel.read";
  route: { id: string; path: string; label: string };
  duel: {
    mode: "runtime-derived-readonly";
    runtimeSources: string[];
    authorableFields: string[];
    roomOwnerMutableFields: string[];
    roomSettings: {
      visibilities: string[];
      matchLengthSeconds: number[];
      roundFormats: number[];
      mapSelectionModes: string[];
      mapIds: string[];
      hazardLevels: string[];
      specialFrequencies: string[];
      seedModes: string[];
      modifiers: string[];
      roomNameLength: { min: number; max: number };
      privatePasswordLength: { min: number; max: number };
      fixedSeed: { min: number; max: number; integer: boolean };
    };
    safeDefaults: Record<string, unknown>;
    bot: {
      wpm: { min: number; max: number; practiceDefault: number };
      accuracy: { min: number; max: number; practiceDefault: number };
      reactionMs: { min: number; max: number; practiceDefault: number };
      personalities: string[];
      practiceDefaultPersonality: string;
    };
    combat: {
      contentVersion: string;
      defaultRegulationSeconds: number;
      hardOvertimeSeconds: number;
      combatProfile: string;
      projectileBaseTravelMs: number;
      typingCannonTravelMs: number;
      roundBreakSeconds: number;
      damageResolvesOnAuthorityClock: boolean;
    };
    persistenceOwner: string;
    roomOwnerWriteCapability: boolean;
    writeCapability: false;
    previewCapability: false;
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
async function fetchDuelContract(): Promise<DuelContractPayload> {
  const response = await fetch("/api/admin/space-typing/duel/contract", {
    cache: "no-store",
    headers: { "x-typing-game-admin-token": api.getToken() },
  });
  const payload = (await response.json().catch(() => ({}))) as Partial<DuelContractPayload> & { message?: string };
  if (!response.ok) throw new Error(payload.message ?? `Duel contract request failed (${response.status})`);
  if (payload.capability !== "duel.read" || !payload.duel || !payload.route) {
    throw new Error("Pinned child Duel contract does not expose duel.read.");
  }
  return payload as DuelContractPayload;
}

export function renderPhaseBDuel(): HTMLElement {
  const page = el("div");
  const head = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(
    el("div", "st-admin-eyebrow", "PvP · Authority-owned Room Rules"),
    el("h1", undefined, "Duel Settings"),
    el("p", undefined, "Inspect the Duel rules actually owned by Space Typing. Friend Room and Practice settings are changed by the room owner inside the Duel session; there is no canonical global Admin policy store, so Admin publishing is intentionally closed."),
  );
  const actions = el("div", "st-admin-page-actions");
  actions.append(badge("RUNTIME-BACKED · READ ONLY", "good"), badge("ROOM OWNER CONFIG", "info"));
  head.append(copy, actions);
  page.append(head);

  const status = notice("Loading canonical Duel runtime contract…");
  page.append(status);
  void (async () => {
    try {
      const payload = await fetchDuelContract();
      const duel = payload.duel;
      status.className = "stx-notice good";
      status.textContent = `Duel ${duel.combat.contentVersion} · ${duel.persistenceOwner} · Admin writes closed.`;

      const rules = panel("Room Rules", "Validated by src/duel/room.ts");
      rules.append(
        listNotice("Visibility", duel.roomSettings.visibilities),
        listNotice("Match length (seconds)", duel.roomSettings.matchLengthSeconds, "good"),
        listNotice("Round formats", duel.roomSettings.roundFormats.map((value) => `Bo${value}`)),
        listNotice("Map selection", duel.roomSettings.mapSelectionModes),
        listNotice("Map IDs", duel.roomSettings.mapIds),
        listNotice("Hazard", duel.roomSettings.hazardLevels),
        listNotice("Mystery / Fate frequency", duel.roomSettings.specialFrequencies),
        listNotice("Modifiers", duel.roomSettings.modifiers),
        scalar("Room name length", `${duel.roomSettings.roomNameLength.min}–${duel.roomSettings.roomNameLength.max}`),
        scalar("Private password length", `${duel.roomSettings.privatePasswordLength.min}–${duel.roomSettings.privatePasswordLength.max}`),
      );

      const defaults = panel("Runtime Defaults", "Safe public defaults; password value is intentionally not exposed");
      for (const [key, value] of Object.entries(duel.safeDefaults)) {
        const display = typeof value === "object" ? JSON.stringify(value) : String(value);
        defaults.append(scalar(key, display));
      }

      const bot = panel("Practice Bot Bounds", "Canonical normalization and Practice defaults");
      bot.append(
        scalar("WPM", `${duel.bot.wpm.min}–${duel.bot.wpm.max} · default ${duel.bot.wpm.practiceDefault}`),
        scalar("Accuracy", `${Math.round(duel.bot.accuracy.min * 100)}–${Math.round(duel.bot.accuracy.max * 100)}% · default ${Math.round(duel.bot.accuracy.practiceDefault * 100)}%`),
        scalar("Reaction", `${duel.bot.reactionMs.min}–${duel.bot.reactionMs.max}ms · default ${duel.bot.reactionMs.practiceDefault}ms`),
        listNotice("Personalities", duel.bot.personalities),
      );

      const authority = panel("Combat Authority & Impact Timing", "Damage and presentation timing come from the Duel authority clock");
      authority.append(
        scalar("Combat profile", duel.combat.combatProfile, "good"),
        scalar("Default regulation", `${duel.combat.defaultRegulationSeconds}s`),
        scalar("Hard overtime", `${duel.combat.hardOvertimeSeconds}s`),
        scalar("Projectile base travel", `${duel.combat.projectileBaseTravelMs}ms`),
        scalar("Typing cannon travel", `${duel.combat.typingCannonTravelMs}ms`),
        scalar("Between-round break", `${duel.combat.roundBreakSeconds}s`),
        scalar("Damage resolves on authority clock", duel.combat.damageResolvesOnAuthorityClock, "good"),
        notice("Admin does not expose a manual projectile-delay slider because timing and damage synchronization share authority-owned runtime constants.", "warn"),
      );

      const ownership = panel("Ownership Boundary", "Room mutation is gameplay behavior, not Admin publishing");
      ownership.append(
        listNotice("Room-owner mutable fields", duel.roomOwnerMutableFields, "good"),
        listNotice("Runtime sources", duel.runtimeSources),
        scalar("Room owner write capability", duel.roomOwnerWriteCapability, "good"),
        scalar("Admin write capability", duel.writeCapability, "warn"),
        scalar("Admin preview capability", duel.previewCapability, "warn"),
      );

      const unsupported = panel("Removed Mock Controls", "Legacy Admin controls without a canonical runtime owner stay unavailable");
      unsupported.append(
        listNotice("Unsupported fields", duel.unsupportedAdminMockFields, "warn"),
        notice("The old Lives=6, free-form match-time/round-window sliders, impact-delay slider, presentation toggles and Save UI Draft were UI mock concepts. They are not treated as production Duel policy."),
      );
      page.append(rules, defaults, bot, authority, ownership, unsupported);
    } catch (error: unknown) {
      status.className = "stx-notice bad";
      status.textContent = `Duel contract unavailable: ${error instanceof Error ? error.message : String(error)}`;
    }
  })();
  return page;
}
