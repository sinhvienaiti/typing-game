import {
  DuelRoom,
  defaultDuelRoomSettings,
  validateDuelRoomSettings,
  type DuelRoomSettingsInput,
} from "../../../games/space-typing/src/duel/room";
import type { DuelBotPersonality } from "../../../games/space-typing/src/duel/bots";
import type { DuelMapId } from "../../../games/space-typing/src/duel/maps";
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
      visibilities: Array<DuelRoomSettingsInput["visibility"]>;
      matchLengthSeconds: Array<DuelRoomSettingsInput["matchLengthSeconds"]>;
      roundFormats: Array<DuelRoomSettingsInput["roundFormat"]>;
      mapSelectionModes: Array<DuelRoomSettingsInput["mapSelection"]["mode"]>;
      mapIds: DuelMapId[];
      hazardLevels: Array<DuelRoomSettingsInput["hazardLevel"]>;
      specialFrequencies: Array<DuelRoomSettingsInput["mysteryFrequency"]>;
      seedModes: Array<DuelRoomSettingsInput["seedMode"]>;
      modifiers: Array<DuelRoomSettingsInput["modifier"]>;
      roomNameLength: { min: number; max: number };
      privatePasswordLength: { min: number; max: number };
      fixedSeed: { min: number; max: number; integer: boolean };
    };
    safeDefaults: Record<string, unknown>;
    bot: {
      wpm: { min: number; max: number; practiceDefault: number };
      accuracy: { min: number; max: number; practiceDefault: number };
      reactionMs: { min: number; max: number; practiceDefault: number };
      personalities: DuelBotPersonality[];
      practiceDefaultPersonality: DuelBotPersonality;
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
function field(label: string, control: HTMLElement): HTMLElement {
  const root = el("label", "stx-field");
  root.append(el("span", undefined, label), control);
  return root;
}
function select<T extends string | number>(values: readonly T[], value: T): HTMLSelectElement {
  const control = el("select", "st-admin-select") as HTMLSelectElement;
  for (const item of values) control.append(new Option(String(item), String(item)));
  control.value = String(value);
  return control;
}
function numeric(value: number, min: number, max: number, step = 1): HTMLInputElement {
  const input = el("input") as HTMLInputElement;
  input.type = "number";
  input.value = String(value);
  input.min = String(min);
  input.max = String(max);
  input.step = String(step);
  return input;
}
function check(label: string, checked: boolean): { root: HTMLElement; input: HTMLInputElement } {
  const root = el("label", "stx-toggle-row");
  root.append(el("strong", undefined, label));
  const input = el("input") as HTMLInputElement;
  input.type = "checkbox";
  input.checked = checked;
  root.append(input);
  return { root, input };
}
function isRecord(value: unknown): value is Record<string, unknown> { return value !== null && typeof value === "object" && !Array.isArray(value); }
function stringArray(value: unknown): value is string[] { return Array.isArray(value) && value.every((item) => typeof item === "string"); }
function numberArray(value: unknown): value is number[] { return Array.isArray(value) && value.every((item) => typeof item === "number" && Number.isFinite(item)); }
function validateDuelContract(value: unknown): DuelContractPayload {
  if (!isRecord(value) || value["capability"] !== "duel.read" || !isRecord(value["duel"])) throw new Error("Duel contract does not match duel.read.");
  const duel = value["duel"];
  if (duel["mode"] !== "runtime-derived-readonly") throw new Error("Duel contract is not runtime-derived read-only.");
  for (const key of ["runtimeSources", "authorableFields", "roomOwnerMutableFields", "unsupportedAdminMockFields"] as const) if (!stringArray(duel[key])) throw new Error(`Duel contract is missing ${key}.`);
  if (!isRecord(duel["roomSettings"]) || !isRecord(duel["bot"]) || !isRecord(duel["combat"]) || !isRecord(duel["safeDefaults"])) throw new Error("Duel contract metadata is incomplete.");
  const room = duel["roomSettings"];
  for (const key of ["visibilities", "mapSelectionModes", "mapIds", "hazardLevels", "specialFrequencies", "seedModes", "modifiers"] as const) if (!stringArray(room[key])) throw new Error(`Duel roomSettings is missing ${key}.`);
  for (const key of ["matchLengthSeconds", "roundFormats"] as const) if (!numberArray(room[key])) throw new Error(`Duel roomSettings is missing ${key}.`);
  if (duel["writeCapability"] !== false || duel["previewCapability"] !== false || typeof duel["persistenceOwner"] !== "string") throw new Error("Duel Admin ownership boundary changed; re-audit required.");
  return value as unknown as DuelContractPayload;
}

export function renderPhaseBDuel(): HTMLElement {
  const page = el("div");
  const head = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(
    el("div", "st-admin-eyebrow", "PvP · Session Rule Simulation"),
    el("h1", undefined, "Duel & Practice Rules"),
    el("p", undefined, "Test the same room settings and bot normalization used by gameplay. These controls are session-only simulation: they never create an Admin revision or change a live room."),
  );
  const actions = el("div", "st-admin-page-actions");
  actions.append(badge("PRODUCTION RULE VALIDATION", "good"), badge("NO ADMIN PERSISTENCE", "info"));
  head.append(copy, actions);
  page.append(head);

  const status = notice("Loading canonical Duel contract…");
  status.setAttribute("aria-live", "polite");
  const content = el("div");
  page.append(status, content);

  let generation = 0;
  const load = (): void => {
    const current = ++generation;
    setAdminStatus(status, "Loading canonical Duel contract and production room rules…", "loading");
    void api.requestJson<unknown>("/api/admin/space-typing/duel/contract").then(validateDuelContract).then((payload) => {
      if (current !== generation) return;
      const duel = payload.duel;
      const defaults = defaultDuelRoomSettings();
      setAdminStatus(status, `Duel ${duel.combat.contentVersion} · production room validator ready · Admin writes closed.`, "success");
      content.replaceChildren();

      const scenario = panel("Room Scenario", "Uses child validateDuelRoomSettings() and DuelRoom directly");
      const visibility = select(duel.roomSettings.visibilities, defaults.visibility);
      const length = select(duel.roomSettings.matchLengthSeconds, defaults.matchLengthSeconds);
      const rounds = select(duel.roomSettings.roundFormats, defaults.roundFormat);
      const mapMode = select(duel.roomSettings.mapSelectionModes, defaults.mapSelection.mode);
      const mapId = select(duel.roomSettings.mapIds, defaults.mapSelection.mode === "fixed" ? defaults.mapSelection.mapId : duel.roomSettings.mapIds[0] ?? "frost-wastes");
      const hazard = select(duel.roomSettings.hazardLevels, defaults.hazardLevel);
      const mystery = select(duel.roomSettings.specialFrequencies, defaults.mysteryFrequency);
      const fate = select(duel.roomSettings.specialFrequencies, defaults.fateFrequency);
      const modifier = select(duel.roomSettings.modifiers, defaults.modifier);
      const botAllowed = check("Practice bot allowed", defaults.botAllowed);
      const controls = el("div", "stx-grid");
      controls.append(
        field("Visibility", visibility), field("Match length", length), field("Rounds", rounds),
        field("Map mode", mapMode), field("Map", mapId), field("Hazard", hazard),
        field("Mystery", mystery), field("Fate", fate), field("Modifier", modifier), botAllowed.root,
      );

      const botWpm = numeric(duel.bot.wpm.practiceDefault, duel.bot.wpm.min, duel.bot.wpm.max);
      const botAccuracy = numeric(Math.round(duel.bot.accuracy.practiceDefault * 100), Math.round(duel.bot.accuracy.min * 100), Math.round(duel.bot.accuracy.max * 100));
      const botReaction = numeric(duel.bot.reactionMs.practiceDefault, duel.bot.reactionMs.min, duel.bot.reactionMs.max);
      const personality = select(duel.bot.personalities, duel.bot.practiceDefaultPersonality);
      const botControls = el("div", "stx-grid");
      botControls.append(field("Bot WPM", botWpm), field("Bot accuracy %", botAccuracy), field("Reaction ms", botReaction), field("Personality", personality));
      const result = notice("Change a rule to run an isolated production validation.", "info");
      const snapshot = el("div", "stx-grid");
      scenario.append(controls, botControls, result, snapshot);

      const simulate = (): void => {
        const chosenMode = mapMode.value as DuelRoomSettingsInput["mapSelection"]["mode"];
        const mapSelection: DuelRoomSettingsInput["mapSelection"] = chosenMode === "fixed"
          ? { mode: "fixed", mapId: mapId.value as DuelMapId }
          : { mode: chosenMode, pool: [...duel.roomSettings.mapIds] };
        const candidate: DuelRoomSettingsInput = {
          ...defaults,
          roomName: "Admin Preview",
          visibility: visibility.value as DuelRoomSettingsInput["visibility"],
          password: visibility.value === "private" ? "preview-only" : undefined,
          matchLengthSeconds: Number(length.value) as DuelRoomSettingsInput["matchLengthSeconds"],
          roundFormat: Number(rounds.value) as DuelRoomSettingsInput["roundFormat"],
          mapSelection,
          hazardLevel: hazard.value as DuelRoomSettingsInput["hazardLevel"],
          mysteryFrequency: mystery.value as DuelRoomSettingsInput["mysteryFrequency"],
          fateFrequency: fate.value as DuelRoomSettingsInput["fateFrequency"],
          botAllowed: botAllowed.input.checked,
          seedMode: "random",
          modifier: modifier.value as DuelRoomSettingsInput["modifier"],
        };
        const validation = validateDuelRoomSettings(candidate);
        if (!validation.ok) {
          result.className = "stx-notice bad";
          result.textContent = validation.errors.join(" ");
          snapshot.replaceChildren();
          return;
        }
        const room = new DuelRoom({
          roomId: "admin-preview",
          ownerParticipantId: "admin-preview-owner",
          ownerDisplayName: "Admin Preview",
          settings: validation.settings,
        });
        if (botAllowed.input.checked) {
          room.setBot({
            requesterId: "admin-preview-owner",
            displayName: "Practice Bot",
            config: {
              wpm: Number(botWpm.value),
              accuracy: Number(botAccuracy.value) / 100,
              reactionMs: Number(botReaction.value),
              personality: personality.value as DuelBotPersonality,
            },
          });
        }
        room.setReady("admin-preview-owner", true);
        const state = room.snapshot();
        result.className = "stx-notice good";
        result.textContent = "VALID · production DuelRoom accepted this isolated scenario · nothing persisted";
        snapshot.replaceChildren(
          notice(`${state.settings.mapSelection.mode.toUpperCase()} map · ${state.settings.matchLengthSeconds / 60} min · Bo${state.settings.roundFormat} · ${state.settings.hazardLevel} hazard`, "good"),
          notice(`Modifier ${state.settings.modifier} · mystery ${state.settings.mysteryFrequency} · fate ${state.settings.fateFrequency}`),
          notice(state.slots[1].bot ? `Practice bot normalized to ${state.slots[1].bot.wpm} WPM · ${Math.round(state.slots[1].bot.accuracy * 100)}% · ${state.slots[1].bot.reactionMs}ms · ${state.slots[1].bot.personality}` : "Practice bot disabled", state.slots[1].bot ? "good" : "info"),
        );
      };
      for (const control of [visibility, length, rounds, mapMode, mapId, hazard, mystery, fate, modifier, botWpm, botAccuracy, botReaction, personality]) control.addEventListener("change", simulate);
      botAllowed.input.addEventListener("change", simulate);
      mapMode.addEventListener("change", () => { mapId.disabled = mapMode.value !== "fixed"; });
      mapId.disabled = mapMode.value !== "fixed";
      simulate();

      const rankedBoundary = panel("Ranked Boundary", "Global competitive rules are not room-owner settings");
      rankedBoundary.append(
        notice("Friend and Practice settings belong to the room/session owner. Ranked rules are authority-owned and remain read-only in Admin.", "info"),
        notice("There is no canonical global Duel Admin policy store, so Save Draft/Publish is intentionally absent.", "warn"),
      );

      const advanced = el("details", "st-admin-panel solid stx-panel");
      advanced.append(el("summary", undefined, "Advanced authority & runtime details"));
      const advancedBody = el("div", "stx-grid");
      advancedBody.append(
        notice(`Persistence owner: ${duel.persistenceOwner}`),
        notice(`Room-owner mutable fields: ${duel.roomOwnerMutableFields.join(" · ")}`),
        notice(`Combat profile: ${duel.combat.combatProfile} · regulation ${duel.combat.defaultRegulationSeconds}s · overtime ${duel.combat.hardOvertimeSeconds}s`),
        notice(`Projectile presentation: base ${duel.combat.projectileBaseTravelMs}ms · cannon ${duel.combat.typingCannonTravelMs}ms · round break ${duel.combat.roundBreakSeconds}s`),
        notice(`Damage resolves on authority clock: ${String(duel.combat.damageResolvesOnAuthorityClock)}`, "good"),
        notice(`Runtime sources: ${duel.runtimeSources.join(" · ")}`),
        notice(`Unsupported Admin fields: ${duel.unsupportedAdminMockFields.join(" · ")}`, "warn"),
      );
      advanced.append(advancedBody);
      content.append(scenario, rankedBoundary, advanced);
    }).catch((error: unknown) => {
      if (current !== generation) return;
      setAdminStatus(status, "Duel runtime contract is unavailable.", "error");
      renderAdminFailureState(content, {
        title: "Duel Settings unavailable",
        fallbackMessage: "The canonical Duel contract could not be loaded.",
        error,
        onRetry: load,
      });
    });
  };
  load();
  return page;
}
