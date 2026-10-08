import "./space-typing-ui.css";
import { SpaceTypingAdminApi, type AudioDefaults, type SpaceTypingAdminConfig } from "./api";

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

const CHILD_RECOMMENDED_DEFAULTS = {
  master: 1,
  pronunciation: 1,
  music: 0.26,
  ambient: 0.08,
  sfx: 0.5,
  credit: 1,
  announcer: 0.85,
  categories: {
    typing: 1,
    combat: 1,
    warnings: 1,
    ui: 1,
    rewards: 1,
  },
} as const;

const PRONUNCIATION_DUCK = {
  typing: 0.32,
  combat: 0.38,
  warnings: 0.68,
  ui: 0.45,
  rewards: 0.7,
} as const;

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
    credit: defaults.credit ?? CHILD_RECOMMENDED_DEFAULTS.credit,
    announcer: defaults.announcer,
    categories: {
      typing: defaults.categories?.typing ?? 1,
      combat: defaults.categories?.combat ?? 1,
      warnings: defaults.categories?.warnings ?? 1,
      ui: defaults.categories?.ui ?? 1,
      rewards: defaults.categories?.rewards ?? 1,
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

export function renderPhaseBAudio(navigate: Navigate): HTMLElement {
  const page = el("div");
  const revisionBadge = badge("ACTIVE · loading", "info");
  const head = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(
    el("div", "st-admin-eyebrow", "Audio · Published Default Profile · Phase B"),
    el("h1", undefined, "Audio Defaults"),
    el("p", undefined, "Canonical defaults for players without a saved audio preference. Existing player settings in spaceTypingSettingsV1 always win and are never rewritten by Admin Publish."),
  );
  const actions = el("div", "st-admin-page-actions");
  actions.append(revisionBadge, badge("DEFAULTS ONLY", "good"));
  head.append(copy, actions);
  page.append(head);

  const runtimeStatus = notice("Loading active revision…", "info");
  page.append(runtimeStatus);

  let loadedActiveRevision: string | null = null;
  let profileId = "recommended-v1";

  const master = slider("Master", CHILD_RECOMMENDED_DEFAULTS.master);
  const pronunciation = slider("Pronunciation", CHILD_RECOMMENDED_DEFAULTS.pronunciation);
  const music = slider("Music", CHILD_RECOMMENDED_DEFAULTS.music);
  const ambient = slider("Ambient", CHILD_RECOMMENDED_DEFAULTS.ambient);
  const sfx = slider("Global SFX", CHILD_RECOMMENDED_DEFAULTS.sfx);
  const credit = slider("Credits / Crystal pickup", CHILD_RECOMMENDED_DEFAULTS.credit, 2);
  const announcer = slider("Announcer", CHILD_RECOMMENDED_DEFAULTS.announcer);

  const core = panel("Default Player Mix", "Child runtime-backed gain preferences · 0–100% except Credit 0–200%");
  const coreList = el("div", "st-admin-audio-list");
  coreList.append(master.root, pronunciation.root, music.root, ambient.root, sfx.root, credit.root, announcer.root);
  core.append(coreList);

  const categorySliders = new Map<AudioCategory, Slider>();
  const categories = panel("SFX Category Preferences", "Per-player multipliers applied on top of Global SFX");
  const categoryList = el("div", "st-admin-audio-list");
  for (const category of Object.keys(CATEGORY_LABELS) as AudioCategory[]) {
    const control = slider(CATEGORY_LABELS[category], CHILD_RECOMMENDED_DEFAULTS.categories[category]);
    categorySliders.set(category, control);
    categoryList.append(control.root);
  }
  categories.append(categoryList);

  const focus = panel("Pronunciation Focus Policy", "Runtime calibration · read-only in B03");
  const focusList = el("div", "st-admin-audio-list");
  for (const category of Object.keys(PRONUNCIATION_DUCK) as AudioCategory[]) {
    const row = el("div", "st-admin-audio-row");
    row.append(el("span", undefined, CATEGORY_LABELS[category]), el("strong", "st-admin-audio-value", `${Math.round(PRONUNCIATION_DUCK[category] * 100)}%`));
    focusList.append(row);
  }
  focus.append(
    notice("These values are owned by the child AudioFocus/mix policy and are intentionally not persisted by Admin B03. They can become editable only after the child exposes a validated published-policy consumer.", "warn"),
    focusList,
  );

  const layout = el("div", "st-admin-audio-layout");
  layout.append(core, el("div", "st-admin-overview-stack"));
  (layout.lastElementChild as HTMLElement).append(categories, focus);
  page.append(layout);

  const applyDefaults = (defaults: AudioDefaults): void => {
    const value = normalizedAudio(defaults);
    master.input.value = String(value.master);
    pronunciation.input.value = String(value.pronunciation);
    music.input.value = String(value.music);
    ambient.input.value = String(value.ambient);
    sfx.input.value = String(value.sfx);
    credit.input.value = String(value.credit);
    announcer.input.value = String(value.announcer);
    for (const [category, control] of categorySliders) control.input.value = String(value.categories[category]);
    for (const input of [master.input, pronunciation.input, music.input, ambient.input, sfx.input, credit.input, announcer.input, ...[...categorySliders.values()].map((entry) => entry.input)]) {
      input.dispatchEvent(new Event("input"));
    }
  };

  void api.getState().then((payload) => {
    loadedActiveRevision = payload.state.activeRevision;
    revisionBadge.textContent = `ACTIVE · ${payload.state.activeRevision}`;
    profileId = payload.active.config.audio.profileId || "recommended-v1";
    applyDefaults(payload.active.config.audio.defaults);
    runtimeStatus.className = "st-admin-info-banner good";
    runtimeStatus.textContent = payload.active.config.audio.defaults.categories === undefined
      ? "Loaded legacy v1 audio defaults. Credit/category defaults are filled from the pinned child recommended profile until the first B03 draft is saved."
      : "Loaded canonical B03 audio default profile from the active revision.";
  }).catch((error: unknown) => {
    runtimeStatus.className = "st-admin-info-banner bad";
    runtimeStatus.textContent = `Admin service unavailable: ${error instanceof Error ? error.message : String(error)}`;
  });

  const saveBar = el("div", "st-admin-sticky-save");
  const saveStatus = el("span", undefined, "Save Draft creates a revision · player preferences remain untouched");
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
          master: Number(master.input.value),
          pronunciation: Number(pronunciation.input.value),
          music: Number(music.input.value),
          ambient: Number(ambient.input.value),
          sfx: Number(sfx.input.value),
          credit: Number(credit.input.value),
          announcer: Number(announcer.input.value),
          categories: Object.fromEntries(
            [...categorySliders].map(([category, control]) => [category, Number(control.input.value)]),
          ) as Required<AudioDefaults>["categories"],
        },
      };
      const revision = await api.createRevision({
        baseRevision: payload.active.revision,
        config,
        message: "Admin Phase B · Audio Defaults draft",
      });
      saveStatus.textContent = `Draft saved · ${revision.revision} · runtime unchanged`;
      runtimeStatus.className = "st-admin-info-banner good";
      runtimeStatus.textContent = `Audio draft ${revision.revision} created. Existing player preferences are untouched; Publish only changes the default profile fallback.`;
    } catch (error: unknown) {
      const message = error instanceof Error ? error.message : String(error);
      saveStatus.textContent = `Draft rejected · ${message}`;
      runtimeStatus.className = "st-admin-info-banner bad";
      runtimeStatus.textContent = `Validation/save failed: ${message}`;
    } finally {
      saveButton.disabled = false;
    }
  })(), "st-admin-btn primary");
  saveBar.append(
    el("strong", undefined, "Phase B Audio Draft"),
    saveStatus,
    el("div", "grow"),
    btn("Discard", () => navigate(`${BASE}/audio`)),
    saveButton,
  );
  page.append(saveBar);
  return page;
}
