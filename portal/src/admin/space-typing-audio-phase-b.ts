import "./space-typing-ui.css";
import { SpaceTypingAdminApi, type AudioDefaults, type SpaceTypingAdminConfig } from "./api";
import { adminErrorMessage } from "./admin-http";

const BASE = "/admin/space-typing";
const api = new SpaceTypingAdminApi();

type Navigate = (path: string) => void;
type Tone = "good" | "warn" | "bad" | "info";
type AudioCategory = "typing" | "combat" | "warnings" | "ui" | "rewards";

type Slider = {
  root: HTMLElement;
  input: HTMLInputElement;
};

const CATEGORY_LABELS: Readonly<Record<AudioCategory, string>> = {
  typing: "Typing",
  combat: "Combat",
  warnings: "Warnings",
  ui: "UI",
  rewards: "Rewards / Credits",
};

const CHILD_PLAYER_DEFAULTS = {
  pronunciation: 1,
  music: 0.26,
  ambient: 0.08,
  sfx: 0.5,
  credit: 1,
} as const;

const LEGACY_COMPATIBILITY_DEFAULTS = {
  master: 1,
  announcer: 0.85,
  categories: {
    typing: 1,
    combat: 1,
    warnings: 1,
    ui: 1,
    rewards: 1,
  },
} as const;

const AUDIO_GROUP_GAIN: Readonly<Record<AudioCategory, number>> = {
  typing: 0.82,
  combat: 0.72,
  warnings: 0.9,
  ui: 0.62,
  rewards: 0.86,
};

const PRONUNCIATION_DUCK: Readonly<Record<AudioCategory, number>> = {
  typing: 0.32,
  combat: 0.38,
  warnings: 0.68,
  ui: 0.45,
  rewards: 0.7,
};

function el<K extends keyof HTMLElementTagNameMap>(tag: K, cls?: string, text?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (cls) node.className = cls;
  if (text !== undefined) node.textContent = text;
  return node;
}

function btn(label: string, fn: () => void = () => undefined, cls = "st-admin-btn"): HTMLButtonElement {
  const node = el("button", cls, label);
  node.type = "button";
  node.addEventListener("click", fn);
  return node;
}

function badge(label: string, tone: Tone = "info"): HTMLElement {
  return el("span", `st-admin-status ${tone}`, label);
}

function panel(title: string, subtitle?: string): HTMLElement {
  const root = el("section", "st-admin-panel solid");
  const head = el("div", "st-admin-panel-head");
  const copy = el("div");
  copy.append(el("h2", undefined, title));
  if (subtitle) copy.append(el("p", undefined, subtitle));
  head.append(copy);
  root.append(head);
  return root;
}

function notice(text: string, tone: Tone = "info"): HTMLElement {
  return el("div", `st-admin-info-banner ${tone}`, text);
}

function slider(label: string, value: number, max = 1): Slider {
  const root = el("div", "st-admin-audio-row");
  const input = el("input") as HTMLInputElement;
  input.type = "range";
  input.min = "0";
  input.max = String(max);
  input.step = "0.01";
  input.value = String(value);
  input.setAttribute("aria-label", label);
  const output = el("span", "st-admin-audio-value", `${Math.round(value * 100)}%`);
  input.addEventListener("input", () => {
    output.textContent = `${Math.round(Number(input.value) * 100)}%`;
  });
  root.append(el("label", undefined, label), input, output);
  return { root, input };
}

function normalizedAudio(defaults: AudioDefaults): Required<AudioDefaults> {
  return {
    master: defaults.master,
    pronunciation: defaults.pronunciation,
    music: defaults.music,
    ambient: defaults.ambient,
    sfx: defaults.sfx,
    credit: defaults.credit ?? CHILD_PLAYER_DEFAULTS.credit,
    announcer: defaults.announcer,
    categories: {
      typing: defaults.categories?.typing ?? LEGACY_COMPATIBILITY_DEFAULTS.categories.typing,
      combat: defaults.categories?.combat ?? LEGACY_COMPATIBILITY_DEFAULTS.categories.combat,
      warnings: defaults.categories?.warnings ?? LEGACY_COMPATIBILITY_DEFAULTS.categories.warnings,
      ui: defaults.categories?.ui ?? LEGACY_COMPATIBILITY_DEFAULTS.categories.ui,
      rewards: defaults.categories?.rewards ?? LEGACY_COMPATIBILITY_DEFAULTS.categories.rewards,
    },
  };
}

function assertStableActiveRevision(loadedActiveRevision: string | null, currentActiveRevision: string): void {
  if (loadedActiveRevision === null) {
    throw new Error("Active revision has not finished loading. Reload this screen before saving.");
  }
  if (loadedActiveRevision !== currentActiveRevision) {
    throw new Error(`Active revision changed from ${loadedActiveRevision} to ${currentActiveRevision}. Reload this screen before saving to avoid overwriting newer published changes.`);
  }
}

function cloneConfig(config: SpaceTypingAdminConfig): SpaceTypingAdminConfig {
  return structuredClone(config);
}

function runtimeRow(label: string, value: string): HTMLElement {
  const row = el("div", "st-admin-audio-row");
  row.append(el("span", undefined, label), el("strong", "st-admin-audio-value", value));
  return row;
}

export function renderPhaseBAudio(navigate: Navigate): HTMLElement {
  const page = el("div");
  const revisionBadge = badge("ACTIVE · loading", "info");
  const head = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(
    el("div", "st-admin-eyebrow", "Audio · Published Default Profile · Phase B"),
    el("h1", undefined, "Audio Defaults"),
    el("p", undefined, "Author only defaults that still exist in the pinned child GameSettings. Existing player settings in spaceTypingSettingsV1 always win and are never rewritten by Admin Publish."),
  );
  const actions = el("div", "st-admin-page-actions");
  actions.append(revisionBadge, badge("CURRENT CHILD FIELDS ONLY", "good"));
  head.append(copy, actions);
  page.append(head);

  const runtimeStatus = notice("Loading active revision…", "info");
  runtimeStatus.setAttribute("aria-live", "polite");
  page.append(runtimeStatus);

  let loadedActiveRevision: string | null = null;
  let profileId = "recommended-v1";
  let compatibilityDefaults: Pick<Required<AudioDefaults>, "master" | "announcer" | "categories"> = {
    master: LEGACY_COMPATIBILITY_DEFAULTS.master,
    announcer: LEGACY_COMPATIBILITY_DEFAULTS.announcer,
    categories: { ...LEGACY_COMPATIBILITY_DEFAULTS.categories },
  };

  const pronunciation = slider("Pronunciation", CHILD_PLAYER_DEFAULTS.pronunciation);
  const music = slider("Music", CHILD_PLAYER_DEFAULTS.music);
  const ambient = slider("Ambient", CHILD_PLAYER_DEFAULTS.ambient);
  const sfx = slider("Global SFX", CHILD_PLAYER_DEFAULTS.sfx);
  const credit = slider("Credits / Crystal pickup", CHILD_PLAYER_DEFAULTS.credit, 2);
  const editableInputs = [pronunciation.input, music.input, ambient.input, sfx.input, credit.input];
  editableInputs.forEach((input) => { input.disabled = true; });

  const core = panel("Current Player Defaults", "Pinned child GameSettings fields · 0–100% except Credit 0–200%");
  const coreList = el("div", "st-admin-audio-list");
  coreList.append(pronunciation.root, music.root, ambient.root, sfx.root, credit.root);
  core.append(coreList);

  const ownership = panel("Runtime-owned Mix", "Read-only ownership discovered from the pinned child runtime");
  const ownershipList = el("div", "st-admin-audio-list");
  ownershipList.append(
    runtimeRow("Master", "not exposed in current GameSettings"),
    runtimeRow("Announcer", "derived from warning mix × 1.08"),
  );
  for (const category of Object.keys(CATEGORY_LABELS) as AudioCategory[]) {
    ownershipList.append(runtimeRow(`${CATEGORY_LABELS[category]} base gain`, `${Math.round(AUDIO_GROUP_GAIN[category] * 100)}%`));
  }
  ownership.append(
    notice("Pinned child no longer exposes masterVolume, announcerVolume, or audioCategoryVolumes as player settings. Legacy revision keys are preserved for schema compatibility but are not authorable here.", "warn"),
    ownershipList,
  );

  const focus = panel("Pronunciation Focus Policy", "Code-owned runtime calibration · read-only");
  const focusList = el("div", "st-admin-audio-list");
  for (const category of Object.keys(PRONUNCIATION_DUCK) as AudioCategory[]) {
    focusList.append(runtimeRow(CATEGORY_LABELS[category], `${Math.round(PRONUNCIATION_DUCK[category] * 100)}%`));
  }
  focus.append(
    notice("Pronunciation attenuates only the listed SFX mix groups. BGM / music is intentionally not ducked by pronunciation.", "good"),
    notice("These values are owned by src/audio/mix.ts and are intentionally not persisted by Admin. They can become editable only after the child exposes a validated published-policy consumer.", "warn"),
    focusList,
  );

  const layout = el("div", "st-admin-audio-layout");
  layout.append(core, el("div", "st-admin-overview-stack"));
  (layout.lastElementChild as HTMLElement).append(ownership, focus);
  page.append(layout);

  const applyDefaults = (defaults: AudioDefaults): void => {
    const value = normalizedAudio(defaults);
    compatibilityDefaults = {
      master: value.master,
      announcer: value.announcer,
      categories: { ...value.categories },
    };
    pronunciation.input.value = String(value.pronunciation);
    music.input.value = String(value.music);
    ambient.input.value = String(value.ambient);
    sfx.input.value = String(value.sfx);
    credit.input.value = String(value.credit);
    for (const input of editableInputs) input.dispatchEvent(new Event("input"));
  };

  const saveBar = el("div", "st-admin-sticky-save");
  const saveStatus = el("span", undefined, "Load the active revision before editing audio defaults");
  const saveButton = btn("Save Draft", () => void (async () => {
    saveButton.disabled = true;
    saveStatus.textContent = "Saving immutable audio draft…";
    try {
      const payload = await api.getState();
      assertStableActiveRevision(loadedActiveRevision, payload.state.activeRevision);
      const config = cloneConfig(payload.active.config);
      config.audio = {
        profileId,
        defaults: {
          master: compatibilityDefaults.master,
          pronunciation: Number(pronunciation.input.value),
          music: Number(music.input.value),
          ambient: Number(ambient.input.value),
          sfx: Number(sfx.input.value),
          credit: Number(credit.input.value),
          announcer: compatibilityDefaults.announcer,
          categories: { ...compatibilityDefaults.categories },
        },
      };
      const revision = await api.createRevision({
        baseRevision: payload.active.revision,
        config,
        message: "Admin Phase B · Audio Defaults draft",
      });
      saveStatus.textContent = `Draft saved · ${revision.revision} · runtime unchanged`;
      runtimeStatus.className = "st-admin-info-banner good";
      runtimeStatus.textContent = `Audio draft ${revision.revision} created. Existing player preferences are untouched; removed legacy mix fields were preserved without exposing fake authoring controls.`;
    } catch (error: unknown) {
      const message = error instanceof Error ? error.message : "The audio draft could not be saved.";
      saveStatus.textContent = `Draft rejected · ${message}`;
      runtimeStatus.className = "st-admin-info-banner bad";
      runtimeStatus.textContent = `Validation/save failed: ${message}`;
    } finally {
      saveButton.disabled = loadedActiveRevision === null;
    }
  })(), "st-admin-btn primary");
  saveButton.disabled = true;
  saveBar.append(
    el("strong", undefined, "Phase B Audio Draft"),
    saveStatus,
    el("div", "grow"),
    btn("Discard", () => navigate(`${BASE}/audio`)),
    saveButton,
  );
  page.append(saveBar);

  let loadGeneration = 0;
  const loadState = (): void => {
    const generation = ++loadGeneration;
    loadedActiveRevision = null;
    revisionBadge.className = "st-admin-status info";
    revisionBadge.textContent = "ACTIVE · loading";
    runtimeStatus.className = "st-admin-info-banner info";
    runtimeStatus.textContent = "Loading active revision…";
    saveStatus.textContent = "Load the active revision before editing audio defaults";
    saveButton.disabled = true;
    editableInputs.forEach((input) => { input.disabled = true; });

    void api.getState().then((payload) => {
      if (generation !== loadGeneration) return;
      loadedActiveRevision = payload.state.activeRevision;
      revisionBadge.className = "st-admin-status good";
      revisionBadge.textContent = `ACTIVE · ${payload.state.activeRevision}`;
      profileId = payload.active.config.audio.profileId || "recommended-v1";
      applyDefaults(payload.active.config.audio.defaults);
      editableInputs.forEach((input) => { input.disabled = false; });
      saveButton.disabled = false;
      saveStatus.textContent = "Save Draft changes current child-backed defaults only · player preferences remain untouched";
      runtimeStatus.className = "st-admin-info-banner good";
      runtimeStatus.textContent = "Loaded canonical audio profile. Current child-backed player defaults are authorable; removed legacy master/announcer/category preferences are preserved read-only for revision compatibility.";
    }).catch((error: unknown) => {
      if (generation !== loadGeneration) return;
      loadedActiveRevision = null;
      revisionBadge.className = "st-admin-status bad";
      revisionBadge.textContent = "ACTIVE · unavailable";
      saveButton.disabled = true;
      editableInputs.forEach((input) => { input.disabled = true; });
      runtimeStatus.className = "st-admin-info-banner bad";
      runtimeStatus.replaceChildren();
      runtimeStatus.append(document.createTextNode(adminErrorMessage(
        error,
        "The active audio revision could not be loaded. Check the local Admin runtime and try again.",
      )));
      const retry = btn("Retry", loadState, "st-admin-btn");
      retry.setAttribute("aria-label", "Retry loading Audio Defaults");
      runtimeStatus.append(document.createTextNode(" "), retry);
    });
  };

  loadState();
  return page;
}
