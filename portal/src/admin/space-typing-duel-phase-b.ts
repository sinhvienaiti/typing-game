import { SpaceTypingAdminApi } from "./api";
import { renderAdminFailureState, setAdminStatus } from "./space-typing-admin-state";

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

function validateDuelContract(value: unknown): DuelContractPayload {
  if (!isRecord(value) || value["capability"] !== "duel.read" || !isRecord(value["duel"]) || !isRecord(value["route"])) {
    throw new Error("Duel contract does not match the canonical duel.read boundary.");
  }
  const duel = value["duel"];
  if (duel["mode"] !== "runtime-derived-readonly") throw new Error("Duel contract is not runtime-derived read-only.");
  for (const key of ["runtimeSources", "authorableFields", "roomOwnerMutableFields", "unsupportedAdminMockFields"] as const) {
    if (!stringArray(duel[key])) throw new Error(`Duel contract is missing ${key}.`);
  }
  if (!isRecord(duel["roomSettings"]) || !isRecord(duel["bot"]) || !isRecord(duel["combat"]) || !isRecord(duel["safeDefaults"])) {
    throw new Error("Duel contract is missing room, bot, combat or defaults metadata.");
  }
  const room = duel["roomSettings"];
  for (const key of ["visibilities", "mapSelectionModes", "mapIds", "hazardLevels", "specialFrequencies", "seedModes", "modifiers"] as const) {
    if (!stringArray(room[key])) throw new Error(`Duel roomSettings is missing ${key}.`);
  }
  for (const key of ["matchLengthSeconds", "roundFormats"] as const) if (!numberArray(room[key])) throw new Error(`Duel roomSettings is missing ${key}.`);
  if (duel["writeCapability"] !== false || duel["previewCapability"] !== false || typeof duel["persistenceOwner"] !== "string") {
    throw new Error("Duel contract contains an invalid Admin ownership boundary.");
  }
  return value as unknown as DuelContractPayload;
}

async function fetchDuelContract(): Promise<DuelContractPayload> {
  return validateDuelContract(await api.requestJson<unknown>("/api/admin/space-typing/duel/contract"));
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
  status.setAttribute("aria-live", "polite");
  const content = el("div");
  page.append(status, content);

  let loadGeneration = 0;
  const load = (): void => {
    const generation = ++loadGeneration;
    setAdminStatus(status, "Loading canonical Duel runtime contract…", "loading");
    content.replaceChildren(notice("Loading room-owner and authority rules…", "info"));
    void fetchDuelContract().then((payload) => {
      if (generation !== loadGeneration) return;
      const duel = payload.duel;
      setAdminStatus(status, `Duel ${duel.combat.contentVersion} · ${duel.persistenceOwner} · Admin writes closed.`, "success");
      content.replaceChildren();

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
      for (const [key, value] of Object.entries(duel.safeDefaults)) defaults.append(scalar(key, typeof value === "object" ? JSON.stringify(value) : String(value)));

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

      const unsupported = panel("Unavailable Admin Controls", "Controls without a canonical runtime owner remain intentionally unavailable");
      unsupported.append(
        listNotice("Unsupported fields", duel.unsupportedAdminMockFields, "warn"),
        notice("Lives, free-form match windows, impact-delay sliders, presentation toggles and Admin Save Draft are not promoted into production policy without a canonical owner."),
      );
      content.append(rules, defaults, bot, authority, ownership, unsupported);
    }).catch((error: unknown) => {
      if (generation !== loadGeneration) return;
      setAdminStatus(status, "Duel runtime contract is unavailable.", "error");
      renderAdminFailureState(content, {
        title: "Duel Settings unavailable",
        fallbackMessage: "The canonical Duel contract could not be loaded. Check the local Admin runtime and try again.",
        error,
        onRetry: load,
      });
    });
  };

  load();
  return page;
}
