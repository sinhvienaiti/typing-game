// Typing Effects (/admin/shared/typing-effects): the typing-effect defaults of
// every game (docs/games/TYPING_FEEL_SERVICE.md §3.10). The lists come from the
// contract through the state route, so the page offers exactly what the checks
// accept. The default sound set is only shown here; it is chosen in Keyboard Sounds.
import { createAdminPageHeader, createAdminValidationMessage } from "../v2/admin-components";
import { cachedLibrary } from "./api";
import { setEffectDefault, type EffectField } from "./draft-model";
import { createTypingFeelReleaseBar } from "./release-bar";
import { TYPING_FEEL_PERMISSIONS, TYPING_FEEL_ROUTES } from "./routes";
import { typingFeelSession as session } from "./session";
import type { TypingFeelEffectDefaults } from "./types";
import { bindSession, button, chip, el, focusKey, keepFocus, panel, sessionGate, title } from "./ui";

const FIELD_HELP: Readonly<Record<Exclude<EffectField, "volume">, string>> = {
  style: "How each typed letter reacts in the focus strip.",
  intensity: "How strong the letter effect is. Off keeps the strip still.",
  size: "How big the word in the focus strip is.",
};

/** Where each default reaches today (§3.10, §4.5). */
const GAMES: readonly { name: string; uses: string }[] = [
  { name: "Last Line", uses: "Style, intensity, size and key volume (typingFx)." },
  { name: "Monkeytype", uses: "Style (letterEffect), intensity (effectStrength) and key volume (keyboardVolume, 0–100). It has no word size." },
  { name: "Dragonhold", uses: "Key volume and the default sound set only; it draws its own letters." },
  { name: "Wordwoven", uses: "Key volume and the default sound set only; it draws its own letters." },
];

const percent = (volume: number): string => `${Math.round(volume * 100)}%`;

export function renderTypingFeelTypingEffects(navigate: (path: string) => void): HTMLElement {
  const page = el("div", "tf-page tf-typing-effects");
  const reload = button("Reload", () => void session.load());
  page.append(createAdminPageHeader({
    eyebrow: "All games · Typing Feel",
    title: "Typing Effects",
    subtitle: "Typing-effect defaults for players who have not saved their own settings yet. A saved choice always wins.",
    actions: [reload],
  }));
  const body = el("div", "tf-body");
  page.append(body, createTypingFeelReleaseBar(session, "typing-effects", navigate));

  const player = new Audio();
  player.preload = "none";
  let defaultPreview: { revision: string; url: string | null } | null = null;

  const loadDefaultPreview = (): void => {
    const source = session.source;
    const working = session.working;
    if (!source || !working) return;
    const key = `${source.revision}:${working.keyboard.defaultSet}`;
    if (defaultPreview?.revision === key) return;
    defaultPreview = { revision: key, url: null };
    void cachedLibrary(source.revision).then((library) => {
      if (defaultPreview?.revision !== key) return;
      defaultPreview = { revision: key, url: library.sets.find((set) => set.id === working.keyboard.defaultSet)?.media?.preview ?? null };
      render();
    }).catch(() => undefined);
  };

  const choiceField = (field: Exclude<EffectField, "volume">, values: readonly string[], working: TypingFeelEffectDefaults, live: TypingFeelEffectDefaults, canEdit: boolean): HTMLElement => {
    const root = el("fieldset", "tf-effect-field");
    const legend = el("legend");
    legend.append(el("strong", undefined, title(field)), el("span", undefined, FIELD_HELP[field]));
    root.append(legend);
    const group = el("div", `tf-choice-group tf-choice-${field}`);
    group.setAttribute("role", "radiogroup");
    group.setAttribute("aria-label", title(field));
    const choose = (value: string): void => {
      if (session.working) session.edit(setEffectDefault(session.working, field, value));
    };
    // The ARIA radio pattern: one Tab stop (the checked option), arrow keys move and select.
    const checked = values.includes(working[field]) ? working[field] : values[0];
    const options = values.map((value) => {
      const option = el("button", "tf-choice");
      option.type = "button";
      option.setAttribute("role", "radio");
      option.setAttribute("aria-checked", String(working[field] === value));
      option.tabIndex = value === checked ? 0 : -1;
      option.dataset["value"] = value;
      focusKey(option, `${field}:${value}`);
      option.dataset["adminPermission"] = TYPING_FEEL_PERMISSIONS.edit;
      option.disabled = !canEdit;
      option.append(el("strong", undefined, title(value)));
      if (live[field] === value) option.append(el("small", undefined, "Live"));
      option.addEventListener("click", () => choose(value));
      group.append(option);
      return option;
    });
    group.addEventListener("keydown", (event) => {
      const index = options.indexOf(event.target as HTMLButtonElement);
      if (!canEdit || index < 0) return;
      const step: Readonly<Record<string, number>> = { ArrowRight: 1, ArrowDown: 1, ArrowLeft: -1, ArrowUp: -1 };
      let next: number;
      if (event.key in step) next = (index + step[event.key]! + options.length) % options.length;
      else if (event.key === "Home") next = 0;
      else if (event.key === "End") next = options.length - 1;
      else return;
      event.preventDefault();
      // Focus first: the re-render that choose() triggers keeps focus on this option.
      options[next]!.focus();
      choose(values[next]!);
    });
    root.append(group);
    if (working[field] !== live[field]) root.append(el("p", "tf-field-change", `Draft change: ${title(String(live[field]))} → ${title(working[field])}`));
    return root;
  };

  const render = (): void => keepFocus(body, draw);
  const draw = (): void => {
    const gate = sessionGate(session, () => void session.load());
    if (gate) {
      body.replaceChildren(gate);
      return;
    }
    loadDefaultPreview();
    const ready = session.ready!;
    const working = session.working!;
    const options = ready.options.effects;
    const defaults = working.effects.defaults;
    const live = ready.active.config.effects.defaults;
    const canEdit = ready.permissions.draft;
    const content = el("div", "tf-effects-layout");

    const editor = panel("Defaults for new players", "Used while a player's save has no typing-effect settings. Players who opened Settings once keep the values from that time, even for options they never touched.");
    if (!canEdit) editor.body.append(createAdminValidationMessage({ tone: "info", message: "Your role can review these defaults, but not change them: editing needs config.draft." }));
    editor.body.append(
      choiceField("style", options.styles, defaults, live, canEdit),
      choiceField("intensity", options.intensities, defaults, live, canEdit),
      choiceField("size", options.sizes, defaults, live, canEdit),
    );
    const volume = el("fieldset", "tf-effect-field");
    const legend = el("legend");
    legend.append(el("strong", undefined, "Key volume"), el("span", undefined, "Keyboard sound volume under each game's own sound volume. Monkeytype shows it on a 0–100 scale."));
    volume.append(legend);
    const row = el("div", "tf-volume-row");
    const range = el("input", "tf-volume");
    range.type = "range";
    range.min = String(options.volume.min);
    range.max = String(options.volume.max);
    range.step = "0.05";
    range.value = String(defaults.volume);
    range.disabled = !canEdit;
    range.dataset["adminPermission"] = TYPING_FEEL_PERMISSIONS.edit;
    focusKey(range, "volume").setAttribute("aria-label", "Key volume");
    range.setAttribute("aria-valuetext", percent(defaults.volume));
    const output = el("output", "tf-volume-value", percent(defaults.volume));
    range.addEventListener("input", () => {
      output.textContent = percent(Number(range.value));
    });
    range.addEventListener("change", () => {
      if (session.working) session.edit(setEffectDefault(session.working, "volume", Number(range.value)));
    });
    row.append(range, output, el("span", "tf-live-value", `Live ${percent(live.volume)}`));
    volume.append(row);
    if (defaults.volume !== live.volume) volume.append(el("p", "tf-field-change", `Draft change: ${percent(live.volume)} → ${percent(defaults.volume)}`));
    editor.body.append(volume);

    const side = el("div", "tf-effects-side");
    const sound = panel("Default sound set", "Chosen in Keyboard Sounds, so it lives in one place.");
    const defaultSet = working.keyboard.sets.find((set) => set.id === working.keyboard.defaultSet);
    const soundRow = el("div", "tf-default-sound");
    const soundCopy = el("div");
    soundCopy.append(el("strong", undefined, defaultSet?.name ?? working.keyboard.defaultSet), el("code", "tf-set-id", working.keyboard.defaultSet));
    if (working.keyboard.defaultSet !== ready.active.config.keyboard.defaultSet) soundCopy.append(chip("Draft change", "warn"));
    soundRow.append(soundCopy, button("Change in Keyboard Sounds", () => navigate(TYPING_FEEL_ROUTES.keyboardSounds)));
    sound.body.append(soundRow);

    const preview = panel("Preview", "A sample of what new players get.");
    const sample = el("dl", "tf-sample");
    for (const [term, value] of [["Style", title(defaults.style)], ["Intensity", title(defaults.intensity)], ["Size", title(defaults.size)], ["Key volume", percent(defaults.volume)], ["Sound set", defaultSet?.name ?? working.keyboard.defaultSet]] as const) {
      const item = el("div");
      item.append(el("dt", undefined, term), el("dd", undefined, value));
      sample.append(item);
    }
    const listen = button(`▶ Play the default set at ${percent(defaults.volume)}`, () => {
      const url = defaultPreview?.url;
      if (!url) return;
      player.pause();
      player.src = url;
      player.volume = Math.max(0, Math.min(1, defaults.volume));
      player.currentTime = 0;
      void player.play().catch(() => session.setNotice({ tone: "bad", message: "The preview could not play in this browser." }));
    }, "st-admin-btn tf-play");
    focusKey(listen, "play-default").disabled = !defaultPreview?.url;
    preview.body.append(sample, listen, el("p", "tf-hint", "The moving letter preview arrives with the shared Typing Feel module (phase G8). Until then this page shows the chosen values and plays the default set's 1 second preview at the chosen key volume."));

    const games = panel("Where these defaults apply", "Today, per game (each converts the volume to its own scale).");
    const list = el("dl", "tf-games");
    for (const game of GAMES) {
      const item = el("div");
      item.append(el("dt", undefined, game.name), el("dd", undefined, game.uses));
      list.append(item);
    }
    games.body.append(list);
    side.append(sound.root, preview.root, games.root);
    content.append(editor.root, side);
    body.replaceChildren(content);
  };

  bindSession(page, session, render);
  render();
  void session.load();
  return page;
}
