// Keyboard Sounds (/admin/shared/keyboard-sounds): the sound-set library every
// game offers, by family order (docs/games/TYPING_FEEL_SERVICE.md §3.7). Every
// action edits the shared working copy only; the P05 bar saves, reviews and
// publishes it. Add sound set (/keyboard-sounds/new, G7) adds a new set to the same working copy.
import { openAdminConfirmDialog } from "../v2/admin-dialog";
import { createAdminPageHeader, createAdminSearchInput, createAdminValidationMessage } from "../v2/admin-components";
import { cachedLibrary, clearLibraryCache, typingFeelErrorProblems } from "./api";
import {
  addFamily,
  changedSetIds,
  dropOnSet,
  familySets,
  moveFamily,
  moveSet,
  orderedFamilies,
  placeSet,
  renameFamily,
  renameSet,
  retireSet,
  setDefault,
  setShown,
  type EditResult,
} from "./draft-model";
import { createTypingFeelReleaseBar, focusTypingFeelNotice } from "./release-bar";
import { TYPING_FEEL_PERMISSIONS, TYPING_FEEL_ROUTES } from "./routes";
import { typingFeelSession as session } from "./session";
import type { TypingFeelLibrary, TypingFeelLibrarySet, TypingFeelSet } from "./types";
import { bindSession, button, chip, el, focusGroup, focusKey, keepFocus, permissionButton, sessionGate } from "./ui";

const DRAG_TYPE = "application/x-typing-feel-set";

function apply(result: EditResult): boolean {
  if (result.config === null) {
    session.editError(result.error);
    return false;
  }
  session.edit(result.config);
  return true;
}

export function renderTypingFeelKeyboardSounds(navigate: (path: string) => void): HTMLElement {
  const page = el("div", "tf-page tf-keyboard-sounds");
  const reload = button("Reload", () => {
    clearLibraryCache();
    void session.load();
  });
  // Add sound set: Format, Accept and Discard need shared.publish (the WAV upload also needs media.upload; the page says so).
  const addButton = permissionButton("Add sound set", TYPING_FEEL_PERMISSIONS.format, true, () => navigate(TYPING_FEEL_ROUTES.addSoundSet), "st-admin-btn primary");
  page.append(createAdminPageHeader({
    eyebrow: "All games · Typing Feel",
    title: "Keyboard Sounds",
    subtitle: "The key-sound sets every game offers, in the order players see them. Reorder, hide, rename or change the default here; nothing reaches the games until the draft is published.",
    actions: [addButton, reload],
  }));
  const body = el("div", "tf-body");
  page.append(body, createTypingFeelReleaseBar(session, "keyboard-sounds", navigate));

  const player = new Audio();
  player.preload = "none";
  let playing: string | null = null;
  let library: TypingFeelLibrary | null = null;
  let libraryRevision: string | null = null;
  let libraryProblem: string | null = null;
  let query = "";
  let renaming: string | null = null;
  let dragged: string | null = null;

  const stopPreview = (): void => {
    player.pause();
    playing = null;
    for (const node of page.querySelectorAll<HTMLButtonElement>(".tf-play[aria-pressed='true']")) {
      node.setAttribute("aria-pressed", "false");
      node.textContent = "▶ Preview";
    }
  };
  player.addEventListener("ended", stopPreview);
  player.addEventListener("error", () => {
    if (playing) session.setNotice({ tone: "bad", message: `The preview of ${playing} could not play.` });
    stopPreview();
  });

  const playPreview = (set: TypingFeelLibrarySet["media"], id: string, trigger: HTMLButtonElement): void => {
    if (!set) return;
    if (playing === id) {
      stopPreview();
      return;
    }
    stopPreview();
    playing = id;
    trigger.setAttribute("aria-pressed", "true");
    trigger.textContent = "■ Stop";
    player.src = set.preview;
    player.currentTime = 0;
    void player.play().catch(() => {
      if (playing === id) {
        session.setNotice({ tone: "bad", message: `The preview of ${id} could not play in this browser.` });
        stopPreview();
      }
    });
  };

  const ensureLibrary = (): void => {
    const source = session.source;
    if (!source || libraryRevision === source.revision) return;
    libraryRevision = source.revision;
    libraryProblem = null;
    const wanted = source.revision;
    cachedLibrary(wanted).then((loaded) => {
      if (libraryRevision !== wanted) return;
      library = loaded;
      libraryProblem = loaded.problems.length ? loaded.problems.join(" ") : null;
      render();
    }).catch((error: unknown) => {
      if (libraryRevision !== wanted) return;
      libraryProblem = `Sound details could not be loaded: ${typingFeelErrorProblems(error).join(" ")}`;
      render();
    });
  };

  const mediaOf = (id: string): TypingFeelLibrarySet["media"] => library?.sets.find((set) => set.id === id)?.media ?? null;

  const card = (set: TypingFeelSet, index: number, count: number, changed: Set<string>, canEdit: boolean): HTMLElement => {
    const working = session.working!;
    const live = session.active!.config;
    const liveSet = live.keyboard.sets.find((entry) => entry.id === set.id) ?? null;
    const isDefault = working.keyboard.defaultSet === set.id;
    const media = mediaOf(set.id);
    const root = focusGroup(el("article", "tf-set-card"), `set:${set.id}`);
    root.dataset["setId"] = set.id;
    root.classList.toggle("is-hidden", !set.enabled);
    root.classList.toggle("is-default", isDefault);
    root.classList.toggle("is-changed", changed.has(set.id));
    root.setAttribute("aria-label", `${set.name}${isDefault ? ", default" : ""}${set.enabled ? "" : ", hidden"}`);

    const head = el("div", "tf-set-head");
    if (canEdit) {
      root.draggable = true;
      const handle = el("span", "tf-drag-handle", "⠿");
      handle.setAttribute("aria-hidden", "true");
      handle.title = "Drag to reorder or move to another family";
      head.append(handle);
    }
    const name = el("div", "tf-set-title");
    if (renaming === set.id) {
      const form = el("form", "tf-rename");
      const input = el("input", "st-admin-input");
      input.value = set.name;
      input.maxLength = session.ready?.options.setNameMax ?? 60;
      input.setAttribute("aria-label", `New name for ${set.id}`);
      focusKey(input, `${set.id}:rename-input`);
      const save = button("Save", () => form.requestSubmit(), "st-admin-btn primary tf-mini");
      save.type = "submit";
      const cancel = button("Cancel", () => {
        renaming = null;
        render();
      }, "st-admin-btn tf-mini");
      form.addEventListener("submit", (event) => {
        event.preventDefault();
        if (apply(renameSet(working, set.id, input.value, session.ready?.options.setNameMax))) renaming = null;
        render();
      });
      input.addEventListener("keydown", (event) => {
        if (event.key === "Escape") {
          renaming = null;
          render();
        }
      });
      form.append(input, save, cancel);
      name.append(form);
      queueMicrotask(() => {
        input.focus();
        input.select();
      });
    } else {
      name.append(el("h3", undefined, set.name));
    }
    name.append(el("code", "tf-set-id", set.id));
    head.append(name);
    const play = focusKey(button("▶ Preview", () => playPreview(media, set.id, play), "st-admin-btn tf-play"), `${set.id}:play`);
    play.setAttribute("aria-pressed", String(playing === set.id));
    if (playing === set.id) play.textContent = "■ Stop";
    play.setAttribute("aria-label", `Play the 1 second preview of ${set.name}`);
    play.disabled = media === null;
    // A set added in this tab (Add sound set) has its sound in the next saved draft, not in the revision shown.
    if (media === null && !library?.sets.some((entry) => entry.id === set.id)) play.title = "New in this draft: Save draft to listen here.";
    head.append(play);
    root.append(head);

    const chips = el("div", "tf-chips");
    if (set.status === "provisional") chips.append(chip("Provisional", "warn"));
    else if (liveSet?.enabled) chips.append(chip("Published", "good"));
    if (changed.has(set.id)) chips.append(chip("Draft change", "warn"));
    if (!set.enabled) chips.append(chip("Hidden", "bad"));
    if (isDefault) chips.append(chip("Default", "info"));
    for (const label of set.labels ?? []) chips.append(chip(label, "info"));
    if (set.ownerPick) chips.append(chip("Owner pick", "good"));
    root.append(chips);

    const meta = el("dl", "tf-set-meta");
    const fact = (term: string, value: string) => {
      const row = el("div");
      row.append(el("dt", undefined, term), el("dd", undefined, value));
      meta.append(row);
    };
    const fresh = media === null && library !== null && !library.sets.some((entry) => entry.id === set.id);
    fact("Keys", media ? String(media.keys) : fresh ? "after Save draft" : "…");
    fact("Spaces", media ? String(media.spaces) : fresh ? "after Save draft" : "…");
    fact("Recipe", set.recipe);
    if (set.ownerScore !== null) fact("Owner score", String(set.ownerScore));
    root.append(meta);
    if (set.note) root.append(el("p", "tf-set-note", set.note));

    if (canEdit) {
      const actions = el("div", "tf-set-actions");
      const permission = TYPING_FEEL_PERMISSIONS.edit;
      const up = permissionButton("↑", permission, true, () => apply(moveSet(working, set.id, -1)), "st-admin-btn tf-mini");
      focusKey(up, `${set.id}:up`).setAttribute("aria-label", `Move ${set.name} up`);
      up.title = "Move up in its family";
      up.disabled = index === 0;
      const down = permissionButton("↓", permission, true, () => apply(moveSet(working, set.id, 1)), "st-admin-btn tf-mini");
      focusKey(down, `${set.id}:down`).setAttribute("aria-label", `Move ${set.name} down`);
      down.title = "Move down in its family";
      down.disabled = index === count - 1;
      const family = el("select", "st-admin-select tf-family-select");
      family.dataset["adminPermission"] = permission;
      focusKey(family, `${set.id}:family`).setAttribute("aria-label", `Family of ${set.name}`);
      for (const entry of orderedFamilies(working)) {
        const option = el("option", undefined, entry.name);
        option.value = entry.id;
        option.selected = entry.id === set.family;
        family.append(option);
      }
      family.addEventListener("change", () => {
        if (!apply(placeSet(working, set.id, family.value, Number.POSITIVE_INFINITY))) family.value = set.family;
      });
      const toggle = permissionButton(set.enabled ? "Hide" : "Show", permission, true, () => apply(setShown(working, set.id, !set.enabled)), "st-admin-btn tf-mini");
      focusKey(toggle, `${set.id}:toggle`);
      if (set.enabled && isDefault) {
        toggle.disabled = true;
        toggle.title = "The default set must stay shown. Choose another default first.";
      }
      const makeDefault = permissionButton(isDefault ? "Default" : "Set default", permission, true, () => apply(setDefault(working, set.id)), "st-admin-btn tf-mini");
      focusKey(makeDefault, `${set.id}:default`).disabled = isDefault || !set.enabled || set.status === "provisional";
      if (!set.enabled) makeDefault.title = "Show the set before making it the default.";
      else if (set.status === "provisional") makeDefault.title = "A provisional set cannot be the default.";
      const rename = permissionButton("Rename", permission, true, () => {
        renaming = set.id;
        render();
      }, "st-admin-btn tf-mini");
      focusKey(rename, `${set.id}:rename`);
      const retire = permissionButton("Retire", permission, true, () => {
        openAdminConfirmDialog({
          eyebrow: "Keyboard Sounds · draft",
          title: `Retire ${set.name}?`,
          message: `Retiring removes ${set.name} from the draft for good and reserves its id "${set.id}" forever, so old saves never point at another sound. Players using it move to the default on their next load. Hide it instead if it may come back. This changes only the draft until it is published.`,
          tone: "danger",
          confirmLabel: "Retire in draft",
          returnFocus: retire,
          onConfirm: () => {
            const result = retireSet(session.working!, set.id);
            if (result.config === null) throw new Error(result.error);
            session.edit(result.config);
            // The card is gone: the bar's heading ("Unsaved edits") takes focus.
            focusTypingFeelNotice(page);
          },
        });
      }, "st-admin-btn tf-mini danger");
      if (isDefault) {
        retire.disabled = true;
        retire.title = "Choose another default before retiring this set.";
      }
      actions.append(up, down, family, toggle, makeDefault, rename, retire);
      root.append(actions);

      root.addEventListener("dragstart", (event) => {
        dragged = set.id;
        event.dataTransfer?.setData(DRAG_TYPE, set.id);
        event.dataTransfer?.setData("text/plain", set.id);
        if (event.dataTransfer) event.dataTransfer.effectAllowed = "move";
        root.classList.add("is-dragging");
      });
      root.addEventListener("dragend", () => {
        dragged = null;
        root.classList.remove("is-dragging");
        for (const node of page.querySelectorAll(".is-drop-target")) node.classList.remove("is-drop-target");
      });
      // A drop target cancels both dragenter and dragover, or the browser may refuse the drop.
      const acceptDrag = (event: DragEvent): void => {
        if (!dragged || dragged === set.id) return;
        event.preventDefault();
        event.stopPropagation();
        if (event.dataTransfer) event.dataTransfer.dropEffect = "move";
        root.classList.add("is-drop-target");
      };
      root.addEventListener("dragenter", acceptDrag);
      root.addEventListener("dragover", acceptDrag);
      root.addEventListener("dragleave", () => root.classList.remove("is-drop-target"));
      root.addEventListener("drop", (event) => {
        event.preventDefault();
        event.stopPropagation();
        const id = event.dataTransfer?.getData(DRAG_TYPE) || dragged;
        dragged = null;
        root.classList.remove("is-drop-target");
        if (id && id !== set.id) apply(dropOnSet(session.working!, id, set.id));
      });
    }
    return root;
  };

  const familiesPanel = (canEdit: boolean): HTMLElement => {
    const working = session.working!;
    const details = el("details", "st-admin-panel solid tf-panel tf-families");
    const summary = el("summary", "tf-families-summary");
    summary.append(el("strong", undefined, "Families"), el("span", undefined, `${working.keyboard.families.length} families · the order and names players see as group headings`));
    details.append(summary);
    const list = el("ol", "tf-family-list");
    const families = orderedFamilies(working);
    families.forEach((family, index) => {
      const sets = familySets(working, family.id);
      const row = focusGroup(el("li", "tf-family-row"), `family:${family.id}`);
      row.setAttribute("aria-label", `Family ${family.name}, place ${index + 1}`);
      // A role without config.draft reads the name; it gets no disabled input (§3.13: hidden, not disabled).
      let nameField: HTMLElement = el("strong", "tf-family-name", family.name);
      if (canEdit) {
        const nameInput = el("input", "st-admin-input");
        nameInput.value = family.name;
        nameInput.maxLength = session.ready?.options.familyNameMax ?? 40;
        nameInput.dataset["adminPermission"] = TYPING_FEEL_PERMISSIONS.edit;
        focusKey(nameInput, `family:${family.id}:name`).setAttribute("aria-label", `Name of family ${family.id}`);
        nameInput.addEventListener("change", () => {
          if (!apply(renameFamily(session.working!, family.id, nameInput.value, session.ready?.options.familyNameMax))) nameInput.value = family.name;
        });
        nameField = nameInput;
      }
      const count = el("span", "tf-family-count", `${sets.filter((set) => set.enabled).length} shown · ${sets.length} total`);
      const id = el("code", "tf-set-id", family.id);
      row.append(el("span", "tf-family-index", String(index + 1)), nameField, id, count);
      if (canEdit) {
        const up = permissionButton("↑", TYPING_FEEL_PERMISSIONS.edit, true, () => apply(moveFamily(session.working!, family.id, -1)), "st-admin-btn tf-mini");
        focusKey(up, `family:${family.id}:up`).setAttribute("aria-label", `Move family ${family.name} up`);
        up.disabled = index === 0;
        const down = permissionButton("↓", TYPING_FEEL_PERMISSIONS.edit, true, () => apply(moveFamily(session.working!, family.id, 1)), "st-admin-btn tf-mini");
        focusKey(down, `family:${family.id}:down`).setAttribute("aria-label", `Move family ${family.name} down`);
        down.disabled = index === families.length - 1;
        row.append(up, down);
      }
      list.append(row);
    });
    details.append(list);
    if (canEdit) {
      const form = el("form", "tf-add-family");
      const input = el("input", "st-admin-input");
      input.placeholder = "New family name";
      input.maxLength = session.ready?.options.familyNameMax ?? 40;
      input.setAttribute("aria-label", "New family name");
      input.dataset["adminPermission"] = TYPING_FEEL_PERMISSIONS.edit;
      const add = permissionButton("Add family", TYPING_FEEL_PERMISSIONS.edit, true, () => form.requestSubmit(), "st-admin-btn tf-mini");
      add.type = "submit";
      form.addEventListener("submit", (event) => {
        event.preventDefault();
        const options = session.ready?.options;
        if (apply(addFamily(session.working!, input.value, { idPattern: options?.idPattern, reserved: options?.reservedIds, max: options?.familyNameMax }))) input.value = "";
      });
      form.append(input, add);
      details.append(form, el("p", "tf-hint", "A family with no shown set is left out of the games' catalogue."));
    }
    details.open = familiesOpen;
    details.addEventListener("toggle", () => {
      familiesOpen = details.open;
    });
    return details;
  };
  let familiesOpen = false;

  const render = (): void => keepFocus(body, draw);
  const draw = (): void => {
    const gate = sessionGate(session, () => void session.load());
    if (gate) {
      body.replaceChildren(gate);
      return;
    }
    ensureLibrary();
    const ready = session.ready!;
    const working = session.working!;
    const canEdit = ready.permissions.draft;
    const changed = changedSetIds(ready.active.config, working);
    const shown = working.keyboard.sets.filter((set) => set.enabled);
    const defaultSet = working.keyboard.sets.find((set) => set.id === working.keyboard.defaultSet);

    const content = el("div", "tf-library");
    const stats = el("div", "tf-stats");
    const stat = (label: string, value: string, tone = "") => {
      const node = el("div", `tf-stat ${tone}`.trim());
      node.append(el("span", undefined, label), el("strong", undefined, value));
      stats.append(node);
    };
    stat("Shown", String(shown.length));
    stat("Hidden", String(working.keyboard.sets.length - shown.length), working.keyboard.sets.length > shown.length ? "warn" : "");
    stat("Families", String(working.keyboard.families.length));
    stat("Default", defaultSet?.name ?? working.keyboard.defaultSet);
    stat("Live", `${ready.active.revision}${ready.active.publication ? ` · ${ready.active.publication.catalogueRevision}` : ""}`);
    content.append(stats);

    if (!canEdit) content.append(createAdminValidationMessage({ tone: "info", message: "Your role can listen and review, but not edit: editing needs config.draft." }));
    if (libraryProblem) content.append(createAdminValidationMessage({ tone: "warn", title: "Sound files", message: libraryProblem }));
    if (working.keyboard.retiredIds.length) {
      content.append(createAdminValidationMessage({ tone: "info", title: "Retired ids", message: `${working.keyboard.retiredIds.join(", ")}: never used again, so old saves fall back to the default.` }));
    }

    const search = focusKey(createAdminSearchInput({ label: "Filter sound sets", placeholder: "Filter by name or id…", value: query, onInput: (value) => {
      query = value;
      render();
      const next = body.querySelector<HTMLInputElement>(".st-admin-v2-search");
      if (next && document.activeElement === next) next.setSelectionRange(next.value.length, next.value.length);
    } }), "search");
    const filterBar = el("div", "st-admin-v2-filter-bar tf-filter");
    filterBar.append(search, el("span", "tf-hint", canEdit ? "Drag a card onto another to take its place, or onto a family to move it there. Hidden sets leave the games' list; players using one move to the default on their next load." : "Hidden sets leave the games' list; players using one move to the default on their next load."));
    content.append(familiesPanel(canEdit), filterBar);

    const needle = query.trim().toLowerCase();
    for (const family of orderedFamilies(working)) {
      const sets = familySets(working, family.id);
      const visible = needle ? sets.filter((set) => `${set.name} ${set.id}`.toLowerCase().includes(needle)) : sets;
      if (needle && visible.length === 0) continue;
      const section = el("section", "tf-family");
      section.dataset["familyId"] = family.id;
      const header = el("header", "tf-family-head");
      header.append(el("h2", undefined, family.name), el("span", undefined, `${sets.filter((set) => set.enabled).length} shown · ${sets.length} ${sets.length === 1 ? "set" : "sets"}`));
      section.append(header);
      const grid = el("div", "tf-set-grid");
      if (sets.length === 0) grid.append(el("p", "tf-empty-family", canEdit ? "No sets yet. Drag a card here or choose this family on a card." : "No sets in this family."));
      visible.forEach((set) => grid.append(card(set, sets.indexOf(set), sets.length, changed, canEdit)));
      section.append(grid);
      if (canEdit) {
        const acceptDrag = (event: DragEvent): void => {
          if (!dragged) return;
          event.preventDefault();
          if (event.dataTransfer) event.dataTransfer.dropEffect = "move";
          section.classList.add("is-drop-family");
        };
        section.addEventListener("dragenter", acceptDrag);
        section.addEventListener("dragover", acceptDrag);
        section.addEventListener("dragleave", (event) => {
          if (!section.contains(event.relatedTarget as Node | null)) section.classList.remove("is-drop-family");
        });
        section.addEventListener("drop", (event) => {
          event.preventDefault();
          section.classList.remove("is-drop-family");
          const id = event.dataTransfer?.getData(DRAG_TYPE) || dragged;
          dragged = null;
          if (id) apply(placeSet(session.working!, id, family.id, Number.POSITIVE_INFINITY));
        });
      }
      content.append(section);
    }
    if (needle && !content.querySelector(".tf-family")) content.append(createAdminValidationMessage({ tone: "info", message: `No set matches "${query}".` }));
    body.replaceChildren(content);
  };

  bindSession(page, session, render);
  render();
  void session.load();
  return page;
}
