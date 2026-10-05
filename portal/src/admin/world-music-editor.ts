import {
  SpaceTypingAdminApi,
  type AdminStatePayload,
  type PlaylistAssignment,
  type PlaylistSelectionMode,
  type SpaceTypingAdminConfig,
  type WorldMusicPolicy,
  type WorldMusicPolicyEntry,
  type WorldMusicPreview,
} from "./api";

type AssignmentSlot = "normal" | "boss-common" | "mini" | "world" | "major";
type PreviewStateName = "normal" | "mini" | "world" | "major";

const SLOTS: readonly AssignmentSlot[] = ["normal", "boss-common", "mini", "world", "major"];
const STYLE_ID = "space-typing-world-music-editor-v1";

function ensureStyles(): void {
  if (document.getElementById(STYLE_ID) !== null) return;
  const style = document.createElement("style");
  style.id = STYLE_ID;
  style.textContent = `
    .st-wm-editor{margin:16px 0;padding:16px;border:1px solid rgba(93,217,255,.18);border-radius:14px;background:rgba(6,21,35,.72)}
    .st-wm-editor-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}.st-wm-field{display:grid;gap:6px}.st-wm-field.full{grid-column:1/-1}.st-wm-field label{font-size:12px;font-weight:800;color:#abd9ec}.st-wm-field input,.st-wm-field select,.st-wm-field textarea{box-sizing:border-box;width:100%;border:1px solid rgba(117,210,255,.2);border-radius:9px;background:#07111d;color:#dff7ff;padding:9px 10px}.st-wm-field textarea{min-height:72px;resize:vertical;font-family:ui-monospace,SFMono-Regular,Menlo,monospace}.st-wm-raw{margin-top:14px}.st-wm-raw summary{cursor:pointer;color:#9de9ff;font-weight:700}.st-wm-raw textarea{width:100%;min-height:210px;margin-top:10px;box-sizing:border-box;background:#050b13;color:#caeefe;border:1px solid rgba(117,210,255,.18);border-radius:10px;padding:12px;font-family:ui-monospace,SFMono-Regular,Menlo,monospace}.st-wm-preview{margin-top:18px}.st-wm-warning{color:#ffd18a}@media(max-width:900px){.st-wm-editor-grid{grid-template-columns:1fr}}
  `;
  document.head.append(style);
}

function button(label: string, onClick: () => void, className = "st-admin-action"): HTMLButtonElement {
  const element = document.createElement("button");
  element.type = "button";
  element.className = className;
  element.textContent = label;
  element.addEventListener("click", onClick);
  return element;
}

function field(labelText: string, control: HTMLElement, full = false): HTMLElement {
  const wrapper = document.createElement("div");
  wrapper.className = `st-wm-field${full ? " full" : ""}`;
  const label = document.createElement("label");
  label.textContent = labelText;
  wrapper.append(label, control);
  return wrapper;
}

function select(values: readonly string[]): HTMLSelectElement {
  const element = document.createElement("select");
  for (const value of values) {
    const option = document.createElement("option");
    option.value = value;
    option.textContent = value;
    element.append(option);
  }
  return element;
}

function stateForSlot(slot: AssignmentSlot): PreviewStateName {
  if (slot === "normal") return "normal";
  if (slot === "mini") return "mini";
  if (slot === "major") return "major";
  return "world";
}

function getAssignment(policy: WorldMusicPolicy, worldId: string, slot: AssignmentSlot): PlaylistAssignment | undefined {
  const entry = policy.worlds?.[worldId];
  if (slot === "normal") return entry?.normal;
  if (slot === "boss-common") return entry?.boss?.common;
  return entry?.boss?.[slot];
}

function setAssignment(policy: WorldMusicPolicy, worldId: string, slot: AssignmentSlot, assignment: PlaylistAssignment): void {
  policy.worlds ??= {};
  const entry: WorldMusicPolicyEntry = policy.worlds[worldId] ?? {};
  policy.worlds[worldId] = entry;
  if (slot === "normal") {
    entry.normal = assignment;
    return;
  }
  entry.boss ??= {};
  if (slot === "boss-common") entry.boss.common = assignment;
  else entry.boss[slot] = assignment;
}

function parseTrackIds(value: string): string[] {
  return [...new Set(value.split(/[\s,]+/).map((item) => item.trim()).filter(Boolean))];
}

function createDraftPolicy(state: AdminStatePayload, preview: WorldMusicPreview): WorldMusicPolicy {
  const existing = state.active.config.worldMusic.publishedPolicy;
  if (existing !== undefined) return structuredClone(existing);
  return {
    configRevision: `admin-world-music-${state.state.generation + 1}`,
    worlds: {},
  };
}

function renderPreviewCards(preview: WorldMusicPreview): HTMLElement {
  const list = document.createElement("div");
  list.className = "st-galaxy-list st-wm-preview";
  const galaxies = [...new Set(preview.worlds.map((world) => world.galaxy))];
  for (const galaxy of galaxies) {
    const section = document.createElement("section");
    section.className = "st-galaxy";
    const title = document.createElement("h3");
    title.textContent = `Galaxy ${String(galaxy).padStart(2, "0")}`;
    const worlds = document.createElement("div");
    worlds.className = "st-world-grid";
    for (const world of preview.worlds.filter((item) => item.galaxy === galaxy)) {
      const card = document.createElement("div");
      card.className = "st-world";
      const strong = document.createElement("strong");
      strong.textContent = `${world.worldId} · ${world.name}`;
      const range = document.createElement("small");
      range.textContent = `Stages ${world.stageRange[0]}–${world.stageRange[1]} · normal ${world.states.normal.trackCount} · boss ${world.states.world.trackCount}`;
      const badges = document.createElement("div");
      badges.className = "st-world-badges";
      for (const badge of [...new Set([...world.states.normal.badges, ...world.states.world.badges])]) {
        const chip = document.createElement("span");
        chip.className = "st-badge";
        chip.textContent = badge;
        badges.append(chip);
      }
      const source = document.createElement("div");
      source.className = "st-world-source";
      source.textContent = `normal: ${world.states.normal.resolvedFrom} · boss: ${world.states.world.resolvedFrom}`;
      source.title = [...world.states.normal.fallbackTrace, ...world.states.world.fallbackTrace].join("\n");
      card.append(strong, range, badges, source);
      worlds.append(card);
    }
    section.append(title, worlds);
    list.append(section);
  }
  return list;
}

function hasSilenceFailSafe(preview: WorldMusicPreview): boolean {
  return preview.worlds.some((world) =>
    Object.values(world.states).some((state) => state.badges.includes("EMPTY / SILENCE FAIL-SAFE")),
  );
}

export function renderWorldMusicEditor(options: {
  panel: HTMLElement;
  state: AdminStatePayload;
  preview: WorldMusicPreview;
  api: SpaceTypingAdminApi;
  navigate: (path: string) => void;
  header: HTMLElement;
}): void {
  ensureStyles();
  const { panel, state, api, navigate, header } = options;
  let currentPreview = options.preview;
  let policy = createDraftPolicy(state, currentPreview);
  const config: SpaceTypingAdminConfig = structuredClone(state.active.config);

  panel.replaceChildren(header);
  const note = document.createElement("div");
  note.className = "st-admin-note";
  const updateNote = (): void => {
    note.textContent = `Preview ${currentPreview.configRevision} · manifest ${currentPreview.manifestRevision} · mode ${currentPreview.musicMode} · active revision ${state.state.activeRevision}`;
  };
  updateNote();
  panel.append(note);

  const editor = document.createElement("section");
  editor.className = "st-wm-editor";
  const grid = document.createElement("div");
  grid.className = "st-wm-editor-grid";

  const revisionInput = document.createElement("input");
  revisionInput.value = policy.configRevision;
  const modeInput = select(["map", "random"]);
  modeInput.value = currentPreview.musicMode;
  const worldInput = select(currentPreview.worlds.map((world) => world.worldId));
  const slotInput = select(SLOTS);
  const assignmentInput = select(["inherit", "replace"]);
  const selectionInput = select(["ordered", "shuffle-bag"]);
  const tracksInput = document.createElement("textarea");
  tracksInput.placeholder = "track-id-1, track-id-2";

  grid.append(
    field("Policy revision", revisionInput),
    field("Preview mode", modeInput),
    field("World", worldInput),
    field("Assignment slot", slotInput),
    field("Assignment", assignmentInput),
    field("Selection", selectionInput),
    field("Track IDs (comma / whitespace separated)", tracksInput, true),
  );
  editor.append(grid);

  const status = document.createElement("div");
  const raw = document.createElement("details");
  raw.className = "st-wm-raw";
  const rawSummary = document.createElement("summary");
  rawSummary.textContent = "Advanced canonical policy JSON";
  const rawText = document.createElement("textarea");
  raw.append(rawSummary, rawText);

  const syncRaw = (): void => {
    rawText.value = `${JSON.stringify(policy, null, 2)}\n`;
  };
  const loadControls = (): void => {
    revisionInput.value = policy.configRevision;
    const assignment = getAssignment(policy, worldInput.value, slotInput.value as AssignmentSlot) ?? { kind: "inherit" };
    assignmentInput.value = assignment.kind;
    if (assignment.kind === "replace") {
      tracksInput.value = assignment.trackIds.join(", ");
      selectionInput.value = assignment.selectionMode ?? "shuffle-bag";
    } else {
      tracksInput.value = "";
      selectionInput.value = "ordered";
    }
    tracksInput.disabled = assignmentInput.value === "inherit";
    selectionInput.disabled = assignmentInput.value === "inherit";
    syncRaw();
  };
  const applyControls = (): void => {
    const revision = revisionInput.value.trim();
    if (revision.length === 0) throw new Error("Policy revision is required.");
    policy.configRevision = revision;
    const slot = slotInput.value as AssignmentSlot;
    if (assignmentInput.value === "inherit") {
      setAssignment(policy, worldInput.value, slot, { kind: "inherit" });
    } else {
      const trackIds = parseTrackIds(tracksInput.value);
      if (trackIds.length === 0) throw new Error("Replace requires at least one track id.");
      setAssignment(policy, worldInput.value, slot, {
        kind: "replace",
        trackIds,
        selectionMode: selectionInput.value as PlaylistSelectionMode,
      });
    }
    syncRaw();
  };

  worldInput.addEventListener("change", loadControls);
  slotInput.addEventListener("change", loadControls);
  assignmentInput.addEventListener("change", () => {
    const inherit = assignmentInput.value === "inherit";
    tracksInput.disabled = inherit;
    selectionInput.disabled = inherit;
  });

  const actions = document.createElement("div");
  actions.className = "st-admin-actions";
  const apply = button("Apply assignment to draft", () => {
    try {
      applyControls();
      status.className = "st-admin-success";
      status.textContent = "Assignment applied to the in-memory draft. Runtime is unchanged.";
    } catch (error) {
      status.className = "st-admin-error";
      status.textContent = error instanceof Error ? error.message : "Invalid assignment.";
    }
  });
  const useResolved = button("Use resolved tracks", () => {
    const world = currentPreview.worlds.find((item) => item.worldId === worldInput.value);
    const stateName = stateForSlot(slotInput.value as AssignmentSlot);
    tracksInput.value = world?.states[stateName].trackIds.join(", ") ?? "";
    assignmentInput.value = "replace";
    tracksInput.disabled = false;
    selectionInput.disabled = false;
  });
  const previewButton = button("Preview draft", () => {
    previewButton.disabled = true;
    status.className = "st-admin-note";
    status.textContent = "Running canonical child resolver…";
    try {
      applyControls();
    } catch (error) {
      previewButton.disabled = false;
      status.className = "st-admin-error";
      status.textContent = error instanceof Error ? error.message : "Invalid draft.";
      return;
    }
    void api.previewWorldMusic({
      publishedPolicy: policy,
      musicMode: modeInput.value as "map" | "random",
    }).then((next) => {
      currentPreview = next;
      updateNote();
      previewHost.replaceChildren(renderPreviewCards(currentPreview));
      status.className = hasSilenceFailSafe(next) ? "st-admin-error" : "st-admin-success";
      status.textContent = hasSilenceFailSafe(next)
        ? "Preview contains EMPTY / SILENCE FAIL-SAFE. Fix the draft before publishing."
        : "Canonical preview passed. Review badges/traces before saving the draft.";
    }).catch((error: unknown) => {
      status.className = "st-admin-error";
      status.textContent = error instanceof Error ? error.message : "Preview failed.";
    }).finally(() => {
      previewButton.disabled = false;
    });
  }, "st-admin-action primary");
  const save = button("Save immutable draft", () => {
    save.disabled = true;
    status.className = "st-admin-note";
    status.textContent = "Validating draft through canonical resolver…";
    try {
      applyControls();
    } catch (error) {
      save.disabled = false;
      status.className = "st-admin-error";
      status.textContent = error instanceof Error ? error.message : "Invalid draft.";
      return;
    }
    void api.previewWorldMusic({ publishedPolicy: policy, musicMode: "map" })
      .then((validated) => {
        if (hasSilenceFailSafe(validated)) {
          throw new Error("Draft contains EMPTY / SILENCE FAIL-SAFE and was not saved.");
        }
        config.worldMusic.policyRevision = policy.configRevision;
        config.worldMusic.assignments = {};
        config.worldMusic.publishedPolicy = structuredClone(policy);
        return api.createRevision({
          baseRevision: state.state.activeRevision,
          config,
          message: `Update World Music policy ${policy.configRevision}`,
        });
      })
      .then((revision) => {
        status.className = "st-admin-success";
        status.textContent = `Draft ${revision.revision} saved. Runtime stays on ${state.state.activeRevision} until Publish.`;
      })
      .catch((error: unknown) => {
        status.className = "st-admin-error";
        status.textContent = error instanceof Error ? error.message : "Could not save World Music draft.";
      })
      .finally(() => {
        save.disabled = false;
      });
  }, "st-admin-action primary");
  const loadRaw = button("Load advanced JSON into draft", () => {
    try {
      const parsed = JSON.parse(rawText.value) as WorldMusicPolicy;
      if (typeof parsed.configRevision !== "string" || parsed.configRevision.trim().length === 0) {
        throw new Error("Advanced policy JSON needs configRevision.");
      }
      policy = structuredClone(parsed);
      loadControls();
      status.className = "st-admin-success";
      status.textContent = "Advanced JSON loaded into the in-memory draft. Preview it before saving.";
    } catch (error) {
      status.className = "st-admin-error";
      status.textContent = error instanceof Error ? error.message : "Invalid policy JSON.";
    }
  });
  const reset = button("Reset Admin overrides", () => {
    policy = { configRevision: revisionInput.value.trim() || `admin-world-music-${state.state.generation + 1}`, worlds: {} };
    loadControls();
    status.className = "st-admin-note";
    status.textContent = "Admin overrides cleared in the draft. Generated/legacy fallback remains available after preview.";
  });
  actions.append(apply, useResolved, previewButton, save, button("History / Publish", () => navigate("/admin/space-typing/history")), reset);
  editor.append(actions, status, raw);
  panel.append(editor);

  const previewHost = document.createElement("div");
  previewHost.append(renderPreviewCards(currentPreview));
  panel.append(previewHost);
  loadControls();
  actions.append(loadRaw);
}
