import "./space-typing-world-music-v2.css";

const BASE = "/admin/space-typing";

type Navigate = (path: string) => void;

let currentNavigate: Navigate = () => undefined;

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

function badge(label: string, tone: "good" | "warn" | "bad" | "info" = "info"): HTMLElement {
  return el("span", `st-admin-status ${tone}`, label);
}

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

const state = {
  galaxy: 1,
  world: 1,
  stages: new Set<number>([1]),
  role: "Normal",
  view: "tree" as "tree" | "matrix",
  scope: "stage" as "all" | "galaxy" | "world" | "stage",
  assignment: "replace" as "inherit" | "replace",
};

const tracks = [
  ["g01-stellar-dawn", "Stellar Dawn", "02:34", "Hopeful"],
  ["g01-lonely-orbit", "Lonely Orbit", "03:04", "Melancholic"],
  ["g01-nebula-drift", "Nebula Drift", "02:18", "Atmospheric"],
  ["g01-awakening", "Awakening Protocol", "03:12", "Climactic"],
  ["global-last-light", "Last Light", "01:24", "Triumphant"],
  ["boss-inferno", "Inferno Assault", "03:42", "Aggressive"],
] as const;

function pageHeader(): HTMLElement {
  const root = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(
    el("div", "st-admin-eyebrow", "Audio & Music · Hierarchical Assignment"),
    el("h1", undefined, "World / Stage Music"),
    el("p", undefined, "Gán nhiều bài nhạc theo All Game → Galaxy → World → Stage → State. Scope thấp hơn override scope cao hơn; panel bên phải luôn cho biết Effective Playlist và nguồn fallback thực tế."),
  );
  const actions = el("div", "st-admin-page-actions");
  actions.append(btn(state.view === "tree" ? "Matrix View" : "Tree View", () => { state.view = state.view === "tree" ? "matrix" : "tree"; currentNavigate(`${BASE}/world-music`); }), btn("Bulk Assign", () => undefined, "st-admin-btn primary"));
  root.append(copy, actions);
  return root;
}

function scopeToolbar(): HTMLElement {
  const bar = el("div", "st-admin-filterbar");
  const seg = el("div", "st-admin-seg");
  const scopes: Array<[typeof state.scope, string]> = [["all", "All Game"], ["galaxy", "Galaxy"], ["world", "World"], ["stage", "Stage"]];
  for (const [value, label] of scopes) {
    const control = btn(label, () => { state.scope = value; if (value === "all") state.assignment = "replace"; currentNavigate(`${BASE}/world-music`); }, state.scope === value ? "active" : "");
    control.setAttribute("aria-pressed", String(state.scope === value));
    seg.append(control);
  }
  bar.append(seg, el("div", "st-admin-filter-spacer"), badge(`G${String(state.galaxy).padStart(2, "0")}`, "info"), badge(`WORLD ${String(state.world).padStart(2, "0")}`, "info"), badge(`${state.stages.size} STAGE SELECTED`, state.stages.size > 1 ? "warn" : "good"));
  return bar;
}

function tree(): HTMLElement {
  const root = panel("Scope Tree", "Select All, Galaxy, World, one or many stages");
  const body = el("div", "stx-music-tree");
  body.append(btn("All Game", () => { state.scope = "all"; state.assignment = "replace"; currentNavigate(`${BASE}/world-music`); }, `stx-music-scope ${state.scope === "all" ? "active" : ""}`));
  for (let g = 1; g <= 10; g++) {
    const details = el("details", "stx-music-galaxy");
    if (g === state.galaxy) details.open = true;
    const summary = el("summary");
    summary.append(el("span", undefined, `Galaxy ${String(g).padStart(2, "0")}`), el("small", undefined, `World ${String((g - 1) * 5 + 1).padStart(2, "0")}–${String(g * 5).padStart(2, "0")}`));
    details.append(summary);
    for (let wOffset = 1; wOffset <= 5; wOffset++) {
      const world = (g - 1) * 5 + wOffset;
      const worldRow = el("div", "stx-music-world-block");
      worldRow.append(btn(`World ${String(world).padStart(2, "0")}`, () => { state.galaxy = g; state.world = world; state.scope = "world"; state.stages = new Set([(world - 1) * 20 + 1]); currentNavigate(`${BASE}/world-music`); }, `stx-music-world ${world === state.world ? "active" : ""}`));
      if (world === state.world) {
        const stages = el("div", "stx-music-stage-list");
        for (let s = 1; s <= 20; s++) {
          const stageNumber = (world - 1) * 20 + s;
          const stageBtn = btn(String(stageNumber).padStart(3, "0"), () => {
            if (state.stages.has(stageNumber)) state.stages.delete(stageNumber); else state.stages.add(stageNumber);
            if (state.stages.size === 0) state.stages.add(stageNumber);
            state.scope = "stage";
            currentNavigate(`${BASE}/world-music`);
          }, `stx-music-stage ${state.stages.has(stageNumber) ? "active" : ""}`);
          stageBtn.setAttribute("aria-pressed", String(state.stages.has(stageNumber)));
          if (s === 20) stageBtn.title = "Boss stage";
          stages.append(stageBtn);
        }
        worldRow.append(stages);
      }
      details.append(worldRow);
    }
    body.append(details);
  }
  root.append(body);
  return root;
}

function assignmentEditor(): HTMLElement {
  const selectedLabel = state.scope === "stage" ? `${state.stages.size} selected stage${state.stages.size === 1 ? "" : "s"}` : state.scope === "world" ? `World ${String(state.world).padStart(2, "0")}` : state.scope === "galaxy" ? `Galaxy ${String(state.galaxy).padStart(2, "0")}` : "All Game";
  const root = panel("Assignment Editor", `${selectedLabel} · multi-file playlist`);
  const tabs = el("div", "st-admin-state-tabs");
  for (const role of ["Normal", "Boss Common", "Mini Boss", "World Boss", "Major Boss"]) {
    const control = btn(role, () => { state.role = role; currentNavigate(`${BASE}/world-music`); }, state.role === role ? "active" : "");
    control.setAttribute("aria-pressed", String(state.role === role));
    tabs.append(control);
  }
  root.append(tabs);
  const mode = el("div", "stx-music-assignment-head");
  const seg = el("div", "st-admin-seg");
  const inherit = btn("Inherit", () => { state.assignment = "inherit"; currentNavigate(`${BASE}/world-music`); }, state.assignment === "inherit" ? "active" : "");
  const replace = btn("Replace", () => { state.assignment = "replace"; currentNavigate(`${BASE}/world-music`); }, state.assignment === "replace" ? "active" : "");
  inherit.disabled = state.scope === "all";
  inherit.title = inherit.disabled ? "Global scope has no parent configuration to inherit from." : "Use the effective value from the parent scope.";
  inherit.setAttribute("aria-pressed", String(state.assignment === "inherit"));
  replace.setAttribute("aria-pressed", String(state.assignment === "replace"));
  seg.append(inherit, replace);
  const strategy = el("select", "st-admin-select");
  strategy.setAttribute("aria-label", "Playlist selection strategy");
  ["Shuffle Bag", "Ordered", "Random", "Weighted Random"].forEach((value) => strategy.append(new Option(value, value)));
  mode.append(el("span", "st-admin-chip", "Assignment"), seg, el("div", "grow"), strategy);
  root.append(mode);
  const playlist = el("div", "stx-music-track-picker");
  tracks.forEach(([id, title, duration, mood], index) => {
    const row = el("label", "stx-music-track");
    const input = el("input") as HTMLInputElement;
    input.type = "checkbox";
    input.checked = index < 3;
    const copy = el("span");
    copy.append(el("strong", undefined, title), el("small", undefined, `${id} · ${duration} · ${mood}`));
    const weight = el("input", "stx-weight") as HTMLInputElement;
    weight.type = "number";
    weight.value = String(index === 0 ? 50 : index === 1 ? 30 : 20);
    weight.min = "0";
    weight.max = "100";
    weight.setAttribute("aria-label", `${title} playlist weight`);
    row.append(input, copy, weight, badge(index < 3 ? "SELECTED" : "AVAILABLE", index < 3 ? "good" : "info"));
    playlist.append(row);
  });
  root.append(playlist);
  const bulk = el("div", "st-admin-page-actions stx-music-bulk");
  bulk.append(btn("Add Tracks"), btn("Set Inherit"), btn("Copy From…"), btn("Clear Override", () => undefined, "st-admin-btn danger"));
  root.append(bulk);
  return root;
}

function effective(): HTMLElement {
  const root = panel("Effective Playlist", `${state.role} · preview after hierarchy resolution`);
  const label = state.scope === "stage" ? `Stage ${Array.from(state.stages).sort((a,b) => a-b).join(", ")}` : state.scope === "world" ? `World ${String(state.world).padStart(2, "0")}` : state.scope === "galaxy" ? `Galaxy ${String(state.galaxy).padStart(2, "0")}` : "All Game";
  const configured = state.assignment === "replace" ? "Replace" : "Inherit";
  const resolvedSource = state.assignment === "replace" ? label : state.scope === "stage" ? `World ${String(state.world).padStart(2, "0")}` : state.scope === "world" ? `Galaxy ${String(state.galaxy).padStart(2, "0")}` : "Global";
  root.append(badge(state.assignment === "replace" ? "REPLACED" : "INHERIT", state.assignment === "replace" ? "good" : "info"), el("div", "stx-effective-source", `Configured: ${configured} · Effective source: ${resolvedSource} · ${state.role}`));
  const list = el("div", "stx-effective-tracks");
  tracks.slice(0, 3).forEach(([id, title, duration, mood], index) => {
    const row = el("div", "stx-effective-track");
    row.append(el("span", "st-admin-track-num", String(index + 1)), el("div"));
    const copy = row.lastElementChild as HTMLElement;
    copy.append(el("strong", undefined, title), el("small", undefined, `${duration} · ${mood} · ${id}`));
    list.append(row);
  });
  root.append(list);
  const fallback = el("div", "stx-fallback");
  fallback.append(el("span", undefined, "Fallback chain"), el("code", undefined, `${label} → World ${String(state.world).padStart(2, "0")} ${state.role} → World Normal → Galaxy Default → Global ${state.role} → Global Normal`));
  root.append(fallback);
  const player = el("div", "stx-music-player");
  player.append(btn("◀"), btn("▶ Preview", () => undefined, "st-admin-btn primary"), btn("▶▶"), btn("Validate"));
  root.append(player);
  return root;
}

function matrix(): HTMLElement {
  const root = panel("Stage Matrix", `World ${String(state.world).padStart(2, "0")} · all 20 stages`);
  const wrap = el("div", "st-admin-table-wrap");
  const table = el("table", "st-admin-table stx-music-matrix");
  table.innerHTML = "<thead><tr><th>Stage</th><th>Normal</th><th>Boss Common</th><th>Mini</th><th>World Boss</th><th>Major</th></tr></thead>";
  const body = el("tbody");
  for (let i = 1; i <= 20; i++) {
    const stage = (state.world - 1) * 20 + i;
    const tr = el("tr");
    const boss = i === 20;
    const cells = [String(stage).padStart(3, "0"), boss ? "inherit · 3" : i % 4 === 0 ? "replace · 2" : "inherit", boss ? "replace · 2" : "—", i % 7 === 0 ? "replace · 2" : "—", boss ? "replace · 3" : "—", boss && state.world % 5 === 0 ? "replace · 3" : "—"];
    cells.forEach((cell, index) => { const td = el("td", index === 0 ? "primary" : undefined, cell); tr.append(td); });
    body.append(tr);
  }
  table.append(body); wrap.append(table); root.append(wrap); return root;
}

export function renderWorldMusicV2(navigate: Navigate): HTMLElement {
  currentNavigate = navigate;
  const page = el("div");
  page.append(pageHeader(), scopeToolbar());
  if (state.view === "matrix") {
    page.append(matrix(), effective());
  } else {
    const layout = el("div", "stx-world-music-v2");
    layout.append(tree(), assignmentEditor(), effective());
    page.append(layout);
  }
  const save = el("div", "st-admin-sticky-save");
  save.append(el("strong", undefined, "Assignment draft"), el("span", undefined, "UI mock only · no production write"), el("div", "grow"), btn("Discard"), btn("Save Draft", () => undefined, "st-admin-btn primary"));
  page.append(save);
  return page;
}
