import "./space-typing-extended.css";

const BASE = "/admin/space-typing";
const ASSET = "https://space.typing-game.local/assets/space-typing";

type Tone = "good" | "warn" | "bad" | "info";
type Navigate = (path: string) => void;

type Row = readonly (string | number | HTMLElement)[];

const uiState = {
  analyticsTab: "Players",
  contentTab: "Vocabulary",
  missionTab: "Daily",
  selectedEquipment: "plasma-lance",
  selectedSkill: "chain-lightning",
  selectedEnemy: "prism-scout",
  selectedBoss: "celestial-warden",
  selectedStage: "314",
  selectedShopItem: "warp-cell-50",
  selectedRevision: "r128",
};

function el<K extends keyof HTMLElementTagNameMap>(tag: K, cls?: string, text?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (cls) node.className = cls;
  if (text !== undefined) node.textContent = text;
  return node;
}

function btn(label: string, onClick: () => void = () => undefined, cls = "st-admin-btn"): HTMLButtonElement {
  const node = el("button", cls, label);
  node.type = "button";
  node.addEventListener("click", onClick);
  return node;
}

function badge(label: string, tone: Tone = "info"): HTMLElement {
  return el("span", `st-admin-status ${tone}`, label);
}

function header(eyebrow: string, title: string, description: string, actions: readonly HTMLElement[] = []): HTMLElement {
  const root = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(el("div", "st-admin-eyebrow", eyebrow), el("h1", undefined, title), el("p", undefined, description));
  root.append(copy);
  if (actions.length) {
    const tools = el("div", "st-admin-page-actions");
    tools.append(...actions);
    root.append(tools);
  }
  return root;
}

function panel(title: string, subtitle?: string, cls = ""): HTMLElement {
  const root = el("section", `st-admin-panel solid stx-panel ${cls}`.trim());
  const head = el("div", "st-admin-panel-head");
  const copy = el("div");
  copy.append(el("h2", undefined, title));
  if (subtitle) copy.append(el("p", undefined, subtitle));
  head.append(copy);
  root.append(head);
  return root;
}

function field(label: string, value: string, kind: "text" | "number" | "select" = "text", options: readonly string[] = []): HTMLElement {
  const root = el("label", "stx-field");
  root.append(el("span", undefined, label));
  if (kind === "select") {
    const select = el("select", "st-admin-select");
    for (const option of options) select.append(new Option(option, option));
    select.value = value;
    root.append(select);
  } else {
    const input = el("input") as HTMLInputElement;
    input.type = kind;
    input.value = value;
    root.append(input);
  }
  return root;
}

function rangeField(label: string, value: number, min = 0, max = 100, suffix = ""): HTMLElement {
  const root = el("div", "stx-range");
  const top = el("div");
  const valueLabel = el("strong", undefined, `${value}${suffix}`);
  top.append(el("span", undefined, label), valueLabel);
  const input = el("input") as HTMLInputElement;
  input.type = "range";
  input.min = String(min);
  input.max = String(max);
  input.value = String(value);
  input.addEventListener("input", () => { valueLabel.textContent = `${input.value}${suffix}`; });
  root.append(top, input);
  return root;
}

function toggle(label: string, enabled = true, description?: string): HTMLElement {
  const root = el("div", "stx-toggle-row");
  const copy = el("div");
  copy.append(el("strong", undefined, label));
  if (description) copy.append(el("small", undefined, description));
  const control = el("button", `st-admin-switch${enabled ? " on" : ""}`) as HTMLButtonElement;
  control.type = "button";
  control.setAttribute("aria-label", `Toggle ${label}`);
  control.append(el("i"));
  control.addEventListener("click", () => control.classList.toggle("on"));
  root.append(copy, control);
  return root;
}

function tabs(labels: readonly string[], active: string, onSelect: (value: string) => void): HTMLElement {
  const root = el("div", "st-admin-state-tabs stx-tabs");
  for (const label of labels) root.append(btn(label, () => onSelect(label), label === active ? "active" : ""));
  return root;
}

function stat(label: string, value: string, note?: string, tone?: Tone): HTMLElement {
  const root = el("article", "stx-stat");
  root.append(el("span", undefined, label), el("strong", tone ? tone : undefined, value));
  if (note) root.append(el("small", undefined, note));
  return root;
}

function stats(items: readonly (readonly [string, string, string?, Tone?])[]): HTMLElement {
  const root = el("div", "stx-stats");
  for (const [label, value, note, tone] of items) root.append(stat(label, value, note, tone));
  return root;
}

function makeTable(headers: readonly string[], rows: readonly Row[]): HTMLElement {
  const wrap = el("div", "st-admin-table-wrap");
  const table = el("table", "st-admin-table stx-table");
  const thead = el("thead");
  const hrow = el("tr");
  for (const h of headers) hrow.append(el("th", undefined, h));
  thead.append(hrow);
  const tbody = el("tbody");
  for (const row of rows) {
    const tr = el("tr");
    for (const cell of row) {
      const td = el("td");
      if (cell instanceof HTMLElement) td.append(cell); else td.textContent = String(cell);
      tr.append(td);
    }
    tbody.append(tr);
  }
  table.append(thead, tbody);
  wrap.append(table);
  return wrap;
}

function bars(items: readonly (readonly [string, number, string])[]): HTMLElement {
  const root = el("div", "stx-bars");
  for (const [label, value, trailing] of items) {
    const row = el("div", "stx-bar");
    const top = el("div");
    top.append(el("span", undefined, label), el("strong", undefined, trailing));
    const track = el("span");
    const fill = el("i");
    fill.style.width = `${Math.max(0, Math.min(100, value))}%`;
    track.append(fill);
    row.append(top, track);
    root.append(row);
  }
  return root;
}

function notice(text: string, tone: Tone = "info"): HTMLElement {
  return el("div", `stx-notice ${tone}`, text);
}

function grid(...children: HTMLElement[]): HTMLElement {
  const root = el("div", "stx-grid");
  root.append(...children);
  return root;
}

function editorShell(list: HTMLElement, detail: HTMLElement): HTMLElement {
  const root = el("div", "stx-editor-shell");
  root.append(list, detail);
  return root;
}

function actionBar(label = "UI mock · no production write"): HTMLElement {
  const root = el("div", "st-admin-sticky-save stx-savebar");
  root.append(el("strong", undefined, "Draft changes"), el("span", undefined, label), el("div", "grow"), btn("Discard"), btn("Save Draft", () => undefined, "st-admin-btn primary"));
  return root;
}

const equipment = [
  ["plasma-lance", "Plasma Lance", "Weapon", "Epic", "+18% damage · +6% crit"],
  ["aegis-core", "Aegis Core", "Shield", "Legendary", "+32 shield · absorb pulse"],
  ["ion-drive", "Ion Drive", "Engine", "Rare", "+14 speed · +8 dodge"],
  ["oracle-chip", "Oracle Chip", "Chip", "Epic", "+12 accuracy · combo shield"],
] as const;

const skills = [
  ["chain-lightning", "Chain Lightning", "Active", "8.0s", "3 targets"],
  ["meteor", "Meteor", "Active", "12.0s", "AoE 220"],
  ["rage", "Rage Drive", "Active", "18.0s", "+35% fire rate"],
  ["guardian-field", "Guardian Field", "Passive", "—", "+20 shield regen"],
] as const;

const enemies = [
  ["prism-scout", "Prism Scout", "Scout", 420, 82, "Stages 201–260"],
  ["prism-sniper", "Prism Sniper", "Sniper", 610, 58, "Stages 221–280"],
  ["frost-tank", "Frost Tank", "Tank", 1400, 34, "Stages 281–340"],
  ["void-oppressor", "Void Oppressor", "Elite", 2100, 49, "Stages 701–820"],
] as const;

const bosses = [
  ["celestial-warden", "Celestial Warden", "World 01", 3, "Stage 020"],
  ["infernal-core", "Infernal Core", "World 08", 4, "Stage 160"],
  ["prism-sovereign", "Prism Sovereign", "World 15", 4, "Stage 300"],
  ["void-cathedral", "Void Cathedral", "World 46", 5, "Stage 920"],
] as const;

const revisions = [
  ["r128", "Draft", "admin", "Update World 05 boss music", "12 changes", "10:02"],
  ["r127", "Published", "admin", "Stage 314 balance pass", "8 changes", "Yesterday"],
  ["r126", "Published", "system", "Audio pronunciation defaults", "6 changes", "Oct 05"],
  ["r125", "Rolled back", "admin", "Rare credit multiplier experiment", "3 changes", "Oct 04"],
] as const;

const backgroundKits = [
  ["g01-celestial", "Celestial Reach"], ["g02-infernal", "Infernal Belt"], ["g03-frost-prism", "Frost Prism"],
  ["g04-verdant", "Verdant Sector"], ["g05-shadow-nature", "Shadow Nature"], ["g06-cosmic-forge", "Cosmic Forge"],
  ["g07-abyssal", "Abyssal Line"], ["g08-aurora-cosmic", "Aurora Expanse"], ["g09-void-cathedral", "Void Cathedral"], ["g10-eternity", "Eternity Gate"],
] as const;

function renderAnalytics(navigate: Navigate): HTMLElement {
  const page = el("div");
  const rerender = (tab: string) => { uiState.analyticsTab = tab; navigate(`${BASE}/analytics`); };
  page.append(header("Dashboard · Deep Intelligence", "Analytics", "Drill-down cho player, gameplay, stage, mode, retention, economy, performance và lỗi. Mock data giữ đúng information architecture trước khi nối telemetry.", [btn("Export View"), btn("Save View", () => undefined, "st-admin-btn primary")]));
  page.append(tabs(["Players", "Gameplay", "Stages", "Modes", "Retention", "Economy", "Performance", "Errors"], uiState.analyticsTab, rerender));
  const filters = el("div", "st-admin-filterbar");
  filters.append(field("", "7 Days", "select", ["Today", "24 Hours", "7 Days", "30 Days", "90 Days"]).querySelector("select")!, field("", "All Players", "select", ["All Players", "New", "Returning", "Duel", "Campaign"]).querySelector("select")!, el("div", "st-admin-filter-spacer"), badge("COMPARE · PREVIOUS PERIOD", "info"));
  page.append(filters);

  if (uiState.analyticsTab === "Players") {
    const activity = panel("Active Players", "Audience growth and session quality");
    activity.append(stats([["DAU", "8,421", "+6.4%", "good"], ["WAU", "31,506", "+9.7%", "good"], ["MAU", "92,184", "+11.2%", "good"], ["New", "1,206", "+14.8%", "good"], ["Returning", "7,215", "+4.9%", "info"], ["Avg Session", "28m 42s", "+3m 11s", "good"]]));
    const curve = panel("Concurrent Users", "24-hour curve · mock");
    curve.append(bars([["00–04", 28, "420"], ["04–08", 44, "701"], ["08–12", 76, "1,214"], ["12–16", 89, "1,421"], ["16–20", 100, "1,642"], ["20–24", 92, "1,508"]]));
    page.append(grid(activity, curve));
  } else if (uiState.analyticsTab === "Stages") {
    page.append(makeTable(["Stage", "Role", "Plays", "Unique", "Clear", "Retry", "WPM", "Accuracy", "Duration"], [
      ["314", "Elite", 384, 351, "18%", "4.8×", 47, "86.4%", "04:38"], ["488", "Boss", 291, 265, "26%", "4.1×", 51, "88.1%", "04:12"], ["650", "Major Boss", 246, 220, "42%", "3.2×", 55, "90.7%", "05:44"], ["742", "Elite", 211, 196, "49%", "2.9×", 58, "91.3%", "04:51"], ["919", "Boss", 168, 153, "53%", "2.6×", 62, "92.2%", "05:07"],
    ]));
  } else if (uiState.analyticsTab === "Modes") {
    page.append(grid(panel("Mode Share", "Current play distribution"), panel("Duel Breakdown", "Alternative mode adoption")));
    const panels = page.querySelectorAll<HTMLElement>(".stx-panel");
    panels[0]?.append(bars([["Campaign", 46, "46%"], ["Expedition", 21, "21%"], ["Duel", 18, "18%"], ["Recall", 12, "12%"], ["Other", 3, "3%"]]));
    panels[1]?.append(bars([["Standard", 64, "64%"], ["Reflex", 21, "21%"], ["Word Chain", 15, "15%"]]));
  } else if (uiState.analyticsTab === "Retention") {
    const cohort = panel("Retention Cohorts", "Players returning after first active day");
    cohort.append(makeTable(["Cohort", "Size", "D1", "D3", "D7", "D14", "D30"], [["Sep 01–07", "7,842", "64%", "51%", "42%", "34%", "26%"], ["Sep 08–14", "8,109", "63%", "49%", "40%", "32%", "25%"], ["Sep 15–21", "8,488", "61%", "47%", "38%", "31%", "24%"], ["Sep 22–28", "9,021", "62%", "48%", "39%", "31%", "—"]]));
    page.append(cohort);
  } else if (uiState.analyticsTab === "Economy") {
    const source = panel("Currency Sources", "Credits created"); source.append(bars([["Stage clear", 100, "2.4M"], ["Boss", 61, "1.46M"], ["Missions", 28, "672K"], ["Events", 12, "288K"]]));
    const sinks = panel("Currency Sinks", "Credits spent"); sinks.append(bars([["Equipment", 100, "1.9M"], ["Ships", 71, "1.35M"], ["Stamina", 36, "684K"], ["Shop misc", 20, "380K"]]));
    page.append(grid(source, sinks), notice("Net credit inflation +510K (+1.4%). Review source/sink balance before changing reward multipliers.", "warn"));
  } else if (uiState.analyticsTab === "Errors") {
    page.append(stats([["JS Error Rate", "0.42%", "+0.08%", "warn"], ["Asset Load", "0.09%", "-0.02%", "good"], ["Audio Load", "0.05%", "flat", "info"], ["WS Disconnect", "1.8%", "-0.4%", "good"]]), makeTable(["Signature", "Count", "Users", "First Seen", "Last Seen", "Status"], [["DUEL_SOCKET_TIMEOUT", 82, 61, "09:04", "10:11", badge("WATCH", "warn")], ["AUDIO_SOURCE_404", 17, 14, "08:32", "09:58", badge("OPEN", "bad")], ["ASSET_DECODE_FAIL", 9, 8, "Yesterday", "09:12", badge("OPEN", "warn")]]));
  } else {
    const snapshot = panel(`${uiState.analyticsTab} Snapshot`, "Detailed mock analytics pattern");
    snapshot.append(stats([["Battles", "42,810", "+7.2%", "good"], ["Clear Rate", "71.4%", "+1.8%", "good"], ["Avg WPM", "57.8", "+2.1", "good"], ["Accuracy", "92.1%", "+0.5%", "good"], ["Retry", "1.84×", "-0.12", "good"], ["Median Duration", "03:18", "-0:09", "good"]]), bars([["Excellent", 36, "36%"], ["Healthy", 44, "44%"], ["Needs Review", 15, "15%"], ["Critical", 5, "5%"]]));
    page.append(snapshot);
  }
  return page;
}

function registryScreen(title: string, eyebrow: string, description: string, rows: readonly (readonly string[])[], selectedId: string, onSelect: (id: string) => void, detail: (record: readonly string[]) => HTMLElement, actions: readonly HTMLElement[] = []): HTMLElement {
  const page = el("div");
  page.append(header(eyebrow, title, description, actions));
  const list = panel(`${title} Registry`, `${rows.length} mock records · searchable editor pattern`);
  const search = el("input", "st-admin-search") as HTMLInputElement; search.placeholder = `Search ${title.toLowerCase()}…`; list.append(search);
  const host = el("div", "stx-registry-list"); list.append(host);
  const render = () => {
    host.replaceChildren();
    const query = search.value.toLowerCase();
    for (const record of rows.filter((r) => r.join(" ").toLowerCase().includes(query))) {
      const card = el("button", `stx-registry-card${record[0] === selectedId ? " active" : ""}`) as HTMLButtonElement;
      card.type = "button";
      card.append(el("strong", undefined, record[1]), el("small", undefined, record.slice(2).join(" · ")), badge(record[0] === selectedId ? "SELECTED" : "READY", record[0] === selectedId ? "info" : "good"));
      card.addEventListener("click", () => onSelect(record[0]));
      host.append(card);
    }
  };
  search.addEventListener("input", render); render();
  const record = rows.find((r) => r[0] === selectedId) ?? rows[0];
  page.append(list, record ? detail(record) : panel("No selection"), actionBar());
  return page;
}

function renderEquipment(navigate: Navigate): HTMLElement {
  return registryScreen("Equipment", "Game Content · Loadout System", "Quản lý weapon, armor, shield, engine, chip, module và artifact với stat modifiers, upgrade scaling, drop source và shop availability.", equipment, uiState.selectedEquipment, (id) => { uiState.selectedEquipment = id; navigate(`${BASE}/equipment`); }, (record) => {
    const detail = panel("Equipment Editor", `${record[0]} · ${record[3]}`);
    detail.append(grid(field("Equipment ID", record[0]), field("Name", record[1]), field("Category", record[2], "select", ["Weapon", "Armor", "Shield", "Engine", "Chip", "Module", "Artifact"]), field("Rarity", record[3], "select", ["Common", "Rare", "Epic", "Legendary"])), notice(record[4], "info"));
    const statsPanel = panel("Stats & Upgrade Scaling", "Preview resulting modifiers"); statsPanel.append(stats([["Base Damage", "+18%", "Level 1", "good"], ["Critical", "+6%", "Level 1", "good"], ["Level Cap", "20", "Upgrade", "info"], ["Set", "Prism Hunter", "2/4 bonus", "info"]]));
    const source = panel("Acquisition", "Unlock, drops and Shop"); source.append(grid(field("Unlock", "World 11"), field("Drop Source", "Elite · Prism family"), field("Shop Price", "18 Rare Credits"), toggle("Enabled", true)));
    detail.append(grid(statsPanel, source)); return detail;
  }, [btn("Compare Loadouts"), btn("+ New Equipment", () => undefined, "st-admin-btn primary")]);
}

function renderSkills(navigate: Navigate): HTMLElement {
  return registryScreen("Skills", "Game Content · Combat Abilities", "Quản lý cooldown, damage, radius, duration, energy, level scaling, projectile, VFX, SFX và unlock condition.", skills, uiState.selectedSkill, (id) => { uiState.selectedSkill = id; navigate(`${BASE}/skills`); }, (record) => {
    const detail = panel("Skill Editor", `${record[0]} · ${record[2]}`);
    detail.append(grid(field("Skill ID", record[0]), field("Name", record[1]), field("Type", record[2], "select", ["Active", "Passive", "Ultimate"]), field("Cooldown", record[3])), grid(rangeField("Damage", 78), rangeField("Radius", 62), rangeField("Duration", 45), rangeField("Energy Cost", 30)));
    const presentation = panel("Presentation", "Projectile / animation / VFX / SFX"); presentation.append(grid(field("Projectile", "chain-bolt"), field("VFX", `${record[0]}-impact`), field("SFX", `${record[0]}-cast`), field("Camera", "medium-shake")));
    detail.append(presentation, notice(`Runtime preview target: ${record[4]}`, "info")); return detail;
  }, [btn("Test Lab Preview"), btn("+ New Skill", () => undefined, "st-admin-btn primary")]);
}

function renderEnemies(navigate: Navigate): HTMLElement {
  return registryScreen("Enemies", "Game Content · Enemy Families", "Enemy editor cho identity, family, combat stats, AI behaviour, stage range, spawn weight, skills, projectile, VFX/SFX và drop table.", enemies.map((r) => r.map(String)), uiState.selectedEnemy, (id) => { uiState.selectedEnemy = id; navigate(`${BASE}/enemies`); }, (record) => {
    const detail = panel("Enemy Editor", `${record[0]} · ${record[2]}`);
    detail.append(grid(field("Enemy ID", record[0]), field("Name", record[1]), field("Role", record[2], "select", ["Scout", "Sniper", "Tank", "Elite", "Commander"]), field("Stage Range", record[5])), stats([["HP", record[3], "base", "info"], ["Speed", record[4], "0–100", "info"], ["Armor", "38", "base", "info"], ["Damage", "64", "base", "warn"]]));
    const ai = panel("AI & Spawn", "Behaviour and encounter weighting"); ai.append(grid(field("AI Profile", "strafe-burst"), field("Spawn Weight", "1.0", "number"), field("Projectile", "enemy-plasma"), field("Drop Table", "enemy-common-v2")));
    detail.append(ai); return detail;
  }, [btn("Preview Family"), btn("+ New Enemy", () => undefined, "st-admin-btn primary")]);
}

function renderBosses(navigate: Navigate): HTMLElement {
  return registryScreen("Bosses", "Game Content · Boss Command", "Boss editor tách riêng enemy thường: phase thresholds, attack patterns, music, announcer, VFX và reward table.", bosses.map((r) => r.map(String)), uiState.selectedBoss, (id) => { uiState.selectedBoss = id; navigate(`${BASE}/bosses`); }, (record) => {
    const detail = panel("Boss Editor", `${record[1]} · ${record[2]} · ${record[4]}`);
    detail.append(grid(field("Boss ID", record[0]), field("Name", record[1]), field("World", record[2]), field("Stage", record[4])), stats([["HP", "24,800", "scaled", "warn"], ["Shield", "8,200", "phase 1", "info"], ["Phases", record[3], "timeline", "info"], ["Enrage", "90s", "timeout", "bad"]]));
    const phase = panel("Phase Timeline", "Threshold-based attacks and presentation"); phase.append(makeTable(["Phase", "Threshold", "Attacks", "Music", "Presentation"], [["P1", "100–70%", "Pulse · Strafe", "Boss Common", "Intro glow"], ["P2", "70–35%", "Mine · Beam", "World Boss", "Armor break"], ["P3", "35–0%", "Rage · Barrage", "Major Boss", "Burn + shake"]]));
    const reward = panel("Rewards", "First clear and repeat clear"); reward.append(stats([["Credits", "18,000", "first clear", "good"], ["Rare Credits", "6", "first clear", "good"], ["Repeat Credits", "4,500", "repeat", "info"], ["Legendary Drop", "3%", "boss table", "warn"]]));
    detail.append(phase, reward); return detail;
  }, [btn("Boss Preview"), btn("+ New Boss", () => undefined, "st-admin-btn primary")]);
}

function renderStages(navigate: Navigate): HTMLElement {
  const page = el("div");
  page.append(header("Game Content · 1000 Stage Operations", "Worlds & Stages", "Quản trị hierarchy Galaxy → World → Stage với stage role, background, music, enemy pool, boss, typing pool, objective, reward, Warp cost và unlock.", [btn("Bulk Edit"), btn("+ New Stage", () => undefined, "st-admin-btn primary")]));
  const tree = panel("World Tree", "10 Galaxies · 50 Worlds · 1000 Stages");
  const scopes = el("div", "stx-scope-list");
  for (let g = 1; g <= 10; g++) {
    const row = btn(`G${String(g).padStart(2, "0")} · World ${String((g - 1) * 5 + 1).padStart(2, "0")}–${String(g * 5).padStart(2, "0")}`, () => undefined, "stx-scope");
    scopes.append(row);
  }
  tree.append(scopes);
  const list = panel("Stage Registry", "Filtered mock rows");
  const rows = [["314", "W16", "Elite", "Hard", "Prism Elite", "CEFR B1", "10 Warp", badge("WARNING", "warn")], ["315", "W16", "Normal", "Hard", "Prism Scout", "CEFR B1", "10 Warp", badge("READY", "good")], ["320", "W16", "Boss", "Boss", "Prism Sovereign", "Boss Text", "12 Warp", badge("READY", "good")], ["650", "W33", "Major Boss", "Extreme", "Solar Tyrant", "CEFR B2", "15 Warp", badge("REVIEW", "warn")]] as const;
  list.append(makeTable(["Stage", "World", "Role", "Difficulty", "Encounter", "Typing", "Cost", "Status"], rows));
  const detail = panel("Stage 314 Editor", "Selected stage · mock detail");
  detail.append(grid(field("Stage ID", uiState.selectedStage), field("World", "World 16"), field("Role", "Elite", "select", ["Normal", "Elite", "Mini Boss", "Boss", "Major Boss", "Challenge", "Hidden"]), field("Difficulty", "Hard", "select", ["Easy", "Normal", "Hard", "Extreme"])), grid(field("Background", "g04-verdant"), field("Music", "World 16 · Normal"), field("Enemy Pool", "prism-elite-v3"), field("Boss", "None")), grid(field("CEFR", "B1"), field("Word Pool", "world16-tech"), field("Word Count", "18", "number"), field("Objective", "Accuracy ≥ 90%")), grid(field("Warp Cost", "10", "number"), field("First Clear", "4,200 Credits"), field("Repeat", "1,100 Credits"), field("Unlock", "Stage 313")));
  page.append(editorShell(tree, el("div", "stx-stack")), actionBar());
  const detailHost = page.querySelector<HTMLElement>(".stx-stack"); detailHost?.append(list, detail);
  return page;
}

function renderTypingContent(navigate: Navigate): HTMLElement {
  const page = el("div");
  const selectTab = (value: string) => { uiState.contentTab = value; navigate(`${BASE}/typing-content`); };
  page.append(header("Game Content · Learning Corpus", "Typing Content", "Admin-facing index cho Vocabulary, Typing Text, Boss Text, Recall và Objectives. Nội dung nguồn sau này map sang English Learning Content System thay vì duplicate dataset.", [btn("Validate References"), btn("Open Content Source", () => undefined, "st-admin-btn primary")]));
  page.append(tabs(["Vocabulary", "Typing Text", "Boss Text", "Recall", "Objectives"], uiState.contentTab, selectTab));
  const filters = el("div", "st-admin-filterbar");
  for (const config of [["All CEFR", "A1", "A2", "B1", "B2", "C1"], ["All Topics", "Space", "Daily", "Technology", "Business"], ["All Status", "Ready", "Draft", "Review"]]) {
    const select = el("select", "st-admin-select"); for (const option of config) select.append(new Option(option, option)); filters.append(select);
  }
  const search = el("input", "st-admin-search") as HTMLInputElement; search.placeholder = "Search content ID, word, topic…"; filters.prepend(search); page.append(filters);
  page.append(makeTable(["ID", "Title / Item", "CEFR", "Topic", "Difficulty", "Used By", "Status"], [["lex-orbit-001", "orbit", "A2", "Space", "2/5", "18 stages", badge("READY", "good")], ["txt-b1-space-08", "Life aboard a research station", "B1", "Space", "3/5", "6 stages", badge("READY", "good")], ["boss-w16-01", "Prism Sovereign challenge", "B1", "Boss", "4/5", "Stage 320", badge("REVIEW", "warn")], ["recall-a2-14", "Travel & direction recall", "A2", "Daily", "2/5", "Recall", badge("READY", "good")]]));
  return page;
}

function renderShop(navigate: Navigate): HTMLElement {
  void navigate;
  const page = el("div");
  page.append(header("Economy · Store Operations", "Shop", "Catalog, featured rotation, price, currency, purchase limits, availability windows, requirements và preview vị trí trong game.", [btn("Preview Shop"), btn("+ Add Offer", () => undefined, "st-admin-btn primary")]));
  page.append(tabs(["Catalog", "Featured", "Daily", "Weekly", "Bundles", "History"], "Catalog", () => undefined));
  const offers = makeTable(["Item", "Category", "Price", "Currency", "Limit", "Availability", "Featured", "Status"], [["Warp Cell · 50", "Energy", "3", "Rare Credit", "3/day", "Always", badge("FEATURED", "info"), badge("ACTIVE", "good")], ["Aegis Core", "Equipment", "18", "Rare Credit", "1", "World 12+", "—", badge("ACTIVE", "good")], ["Vanguard Skin · Azure", "Cosmetic", "42,000", "Credits", "1", "Oct 06–20", badge("FEATURED", "info"), badge("SCHEDULED", "warn")], ["Starter Upgrade Pack", "Bundle", "24,000", "Credits", "1/account", "New player", "—", badge("ACTIVE", "good")]]);
  const editor = panel("Offer Editor", "warp-cell-50"); editor.append(grid(field("Offer ID", "warp-cell-50"), field("Item", "Warp Cell · 50"), field("Category", "Energy"), field("Currency", "Rare Credit"), field("Price", "3", "number"), field("Daily Limit", "3", "number"), field("Starts", "Always"), field("Ends", "Never")), grid(toggle("Enabled", true), toggle("Featured", true), toggle("New Player Eligible", true)));
  page.append(grid(panel("Catalog", "Current mock offers"), editor)); page.querySelector(".stx-panel")?.append(offers); page.append(actionBar()); return page;
}

function renderCurrencies(): HTMLElement {
  const page = el("div"); page.append(header("Economy · Currency Control", "Currencies", "Định nghĩa currency identity và quan sát source/sink balance. Các thay đổi currency thực tế sẽ yêu cầu impact validation ở phase backend.", [btn("Economy Report"), btn("+ Currency", () => undefined, "st-admin-btn primary")]));
  const cards = el("div", "stx-currency-grid");
  for (const [name, symbol, generated, spent, net, tone] of [["Credits", "C", "4.82M", "4.31M", "+510K", "warn"], ["Rare Credits", "◆", "18.4K", "17.9K", "+514", "good"], ["Event Crystal", "◇", "7.2K", "6.9K", "+301", "good"], ["Premium", "✦", "—", "—", "External", "info"]] as const) {
    const card = panel(name, `Currency · ${symbol}`); card.append(stats([["Generated", generated], ["Spent", spent], ["Net", net, "period", tone as Tone]]), grid(field("Display Name", name), field("Cap", "9999999", "number"), field("Precision", "0", "number"), toggle("Enabled", true))); cards.append(card);
  }
  page.append(cards, notice("Economy-changing publishes should require impact estimate + explicit confirmation. UI reserves that flow before backend mapping.", "warn")); return page;
}

function renderRewards(): HTMLElement {
  const page = el("div"); page.append(header("Economy · Loot Operations", "Rewards & Drops", "Quản lý drop table cho Normal, Elite, Mini Boss, World Boss, Major Boss, Stage Clear, Mission và Event. Có validation probability và simulator UI.", [btn("Validate Tables"), btn("Simulate 1,000 Drops", () => undefined, "st-admin-btn primary")]));
  const scope = el("div", "st-admin-filterbar"); scope.append(badge("SCOPE · World Boss", "info"), btn("Normal"), btn("Elite"), btn("Mini Boss"), btn("World Boss", () => undefined, "st-admin-btn primary"), btn("Major Boss")); page.append(scope);
  page.append(makeTable(["Item", "Probability", "Min", "Max", "Condition", "Status"], [["Diamond Small", "55%", 1, 3, "Always", badge("READY", "good")], ["Diamond Medium", "30%", 1, 2, "Always", badge("READY", "good")], ["Diamond Large", "12%", 1, 1, "Accuracy ≥ 90%", badge("READY", "good")], ["Rare Crystal", "3%", 1, 1, "Boss clear", badge("RARE", "warn")]]));
  const simulation = panel("Simulation Preview", "1,000 mock rolls"); simulation.append(stats([["Small", "1,104", "55.2%"], ["Medium", "604", "30.2%"], ["Large", "122", "12.2%"], ["Rare", "24", "2.4%", "warn"]]), notice("Probability total = 100%. Guaranteed-drop conditions are evaluated separately.", "good")); page.append(simulation, actionBar()); return page;
}

function renderWarp(): HTMLElement {
  const page = el("div"); page.append(header("Economy · Session Pacing", "Stamina / Warp", "Cấu hình UI cho max Warp, stage/boss cost, recovery, potion restore và price. Simulator giúp đánh giá pacing trước khi backend áp dụng.", [btn("Reset Recommended"), btn("Compare Economy", () => undefined, "st-admin-btn primary")]));
  const settings = panel("Warp Settings", "Default economy values"); settings.append(rangeField("Maximum Warp", 100, 50, 200), rangeField("Stage Cost", 10, 1, 30), rangeField("Boss Cost", 12, 1, 30), rangeField("Recovery Amount", 1, 1, 10), rangeField("Recovery Interval", 6, 1, 30, " min"), rangeField("Potion Restore", 50, 10, 100), rangeField("Potion Price", 3, 1, 20, " RC"));
  const sim = panel("Pacing Simulator", "Calculated preview from current sliders"); sim.append(stats([["0 → 100", "10h 00m", "natural recovery"], ["Stages / full bar", "10", "at 10 Warp"], ["Bosses / full bar", "8", "at 12 Warp"], ["Daily natural Warp", "240", "24h capless"], ["Potion value", "5 stages", "50 Warp"], ["Rare Credit / stage", "0.6", "via potion"]]), notice("Changing recovery/cost affects retention and currency sinks. Publish UX must show affected-player estimate.", "warn")); page.append(grid(settings, sim), actionBar()); return page;
}

function renderMissions(navigate: Navigate): HTMLElement {
  const page = el("div"); const select = (value: string) => { uiState.missionTab = value; navigate(`${BASE}/missions`); };
  page.append(header("Live Ops · Objective Scheduling", "Missions", "Daily, Weekly, Achievement và Special mission editor với requirement, target, reward, reset, start/end và status.", [btn("Mission Calendar"), btn("+ New Mission", () => undefined, "st-admin-btn primary")]));
  page.append(tabs(["Daily", "Weekly", "Achievements", "Special"], uiState.missionTab, select));
  page.append(makeTable(["Mission", "Requirement", "Target", "Reward", "Reset / Window", "Status"], [["Precision Pilot", "Accuracy", "≥ 95% × 3", "1,200 Credits", "Daily", badge("ACTIVE", "good")], ["Campaign Runner", "Clear stages", "10", "2 Rare Credits", "Daily", badge("ACTIVE", "good")], ["Duel Specialist", "Win Duel", "5", "3 Rare Credits", "Weekly", badge("ACTIVE", "good")], ["Void Hunter", "Defeat Boss", "World 46", "Legendary Chest", "Oct 06–13", badge("SCHEDULED", "warn")]]));
  const editor = panel("Mission Editor", "precision-pilot-daily"); editor.append(grid(field("Mission ID", "precision-pilot-daily"), field("Name", "Precision Pilot"), field("Requirement", "Accuracy"), field("Target", "95% × 3"), field("Reward", "1,200 Credits"), field("Reset", uiState.missionTab)), grid(toggle("Enabled", true), toggle("Track Progress Live", true))); page.append(editor, actionBar()); return page;
}

function renderExpedition(): HTMLElement {
  const page = el("div"); page.append(header("Live Ops · Roguelike Run", "Expedition", "Cấu hình Daily Expedition, encounter count, difficulty scaling, modifiers, rewards, Ghost, boss và entry cost.", [btn("Preview Run"), btn("New Rotation", () => undefined, "st-admin-btn primary")]));
  const config = panel("Daily Expedition", "Current mock rotation"); config.append(grid(field("Rotation ID", "exp-2026-10-06"), field("Encounters", "8", "number"), field("Entry Cost", "0 Warp"), field("Boss", "Prism Sovereign"), field("Difficulty Curve", "1.00 → 1.85"), field("Ghost", "Enabled")), grid(toggle("Daily", true), toggle("Ghost Recording", true), toggle("Campaign Progress Safe", true)));
  const path = panel("Run Path", "8 encounters + final reward"); const nodes = el("div", "stx-run-path"); for (const [i, type] of ["Combat", "Elite", "Choice", "Combat", "Rest", "Elite", "Challenge", "Boss"].entries()) nodes.append(el("div", `stx-run-node ${type.toLowerCase()}`, `${i + 1}\n${type}`)); path.append(nodes);
  const reward = panel("Reward Preview", "Run completion"); reward.append(stats([["Credits", "6,800"], ["Rare Credits", "3"], ["Chest", "Epic"], ["Daily Bonus", "+20%", "first run", "good"]])); page.append(config, grid(path, reward), actionBar()); return page;
}

function renderEvents(): HTMLElement {
  const page = el("div"); page.append(header("Live Ops · Scheduled Operations", "Events", "Calendar/timeline cho event banner, start/end, timezone, music, background, missions, Shop, rewards và gameplay modifiers.", [btn("Calendar View"), btn("+ New Event", () => undefined, "st-admin-btn primary")]));
  const timeline = el("div", "stx-event-timeline");
  for (const [status, title, window, detail, tone] of [["LIVE", "Aurora Offensive", "Oct 04 → Oct 11", "2× Boss Credits · Aurora backdrop · Event missions", "good"], ["SCHEDULED", "Void Cathedral Hunt", "Oct 12 → Oct 19", "World 46 spotlight · Rare Crystal +25%", "warn"], ["DRAFT", "Eternity Gate Finale", "Oct 20 → Oct 27", "Major Boss chain · special BGM · legendary rewards", "info"]] as const) { const card = panel(title, window); card.append(badge(status, tone), el("p", "stx-copy", detail), grid(field("Timezone", "Asia/Ho_Chi_Minh"), toggle("Event Enabled", status !== "DRAFT"))); timeline.append(card); }
  page.append(timeline, actionBar("Scheduling is mock-only until Live Ops backend mapping.")); return page;
}

function renderDuel(): HTMLElement {
  const page = el("div"); page.append(header("PvP · Match Operations", "Duel Settings", "Core match rules, Friend Room, Practice, bots và announcer settings. Competitive changes cần apply-boundary rõ ở backend phase.", [btn("Preview Rules"), btn("Save UI Draft", () => undefined, "st-admin-btn primary")]));
  page.append(tabs(["Core", "Friend Room", "Practice", "Match Rules", "Bots", "Announcer"], "Core", () => undefined));
  const rules = panel("Core Rules", "Shared combat settings"); rules.append(grid(rangeField("Lives", 6, 1, 10), rangeField("Match Time", 4, 1, 10, " min"), rangeField("Round Window", 12, 5, 30, " s"), rangeField("Projectile Impact Delay", 420, 100, 900, " ms")), grid(toggle("Projectile/Damage Impact Sync", true), toggle("Burn FX at Low HP", true), toggle("Large KO Explosion", true), toggle("Announcer Milestones", true)));
  const bot = panel("Bot Presets", "WPM / accuracy / reaction"); bot.append(makeTable(["Preset", "WPM", "Accuracy", "Reaction", "Enabled"], [["Rookie", 28, "88%", "650ms", badge("ON", "good")], ["Pilot", 48, "94%", "420ms", badge("ON", "good")], ["Ace", 72, "97%", "270ms", badge("ON", "good")], ["Champion", 96, "99%", "180ms", badge("LAB", "warn")]])); page.append(grid(rules, bot), actionBar()); return page;
}

function renderRanked(): HTMLElement {
  const page = el("div"); page.append(header("PvP · Competitive Operations", "Ranked", "Season, rating, placement, matchmaking spread, map/mode pool và rewards. Đây là domain nguy hiểm: UI luôn hiển thị impact warning.", [badge("COMPETITIVE", "warn"), btn("Season Preview", () => undefined, "st-admin-btn primary")]));
  page.append(notice("Competitive changes must apply to NEW MATCHES only. Never hot-apply rules in an active match.", "warn"));
  const season = panel("Season 01", "Current mock competitive season"); season.append(grid(field("Season ID", "S01"), field("Name", "First Contact"), field("Starts", "2026-10-01"), field("Ends", "2026-11-01"), rangeField("Placement Matches", 5, 1, 10), rangeField("Matchmaking Spread", 180, 50, 500, " MMR")), grid(toggle("Ranked Enabled", true), toggle("Standard Mode", true), toggle("Reflex Ranked", false), toggle("Word Chain Ranked", false)));
  const tiers = panel("Rank Tiers", "Rating thresholds and rewards"); tiers.append(makeTable(["Tier", "MMR", "Season Reward", "Players"], [["Bronze", "0–1099", "1,500 Credits", "28%"], ["Silver", "1100–1399", "3,000 Credits", "34%"], ["Gold", "1400–1699", "5 Rare Credits", "24%"], ["Platinum", "1700–1999", "10 Rare Credits", "11%"], ["Champion", "2000+", "Legendary Banner", "3%"]])); page.append(grid(season, tiers), actionBar("Dangerous publish flow must include affected-match estimate.")); return page;
}

function renderAlternativeModes(): HTMLElement {
  const page = el("div"); page.append(header("PvP · Alternative Mode Lab", "Alternative Modes", "Reflex và Word Chain control surface với reaction window, challenge pool, beat rules, damage và bot quality. UI mirrors server-authority design.", [btn("Mode Test Lab"), btn("Compare Modes", () => undefined, "st-admin-btn primary")]));
  const reflex = panel("Reflex", "Authority-owned reaction challenges"); reflex.append(badge("ENABLED · FRIEND ROOM", "good"), grid(rangeField("Reaction Window", 1200, 400, 2500, " ms"), rangeField("Round Damage", 18, 5, 40), field("Challenge Pool", "reflex-core-v1"), field("Bot Reaction", "420ms")), grid(toggle("Practice", true), toggle("Friend Room", true), toggle("Ranked", false)));
  const chain = panel("Word Chain", "Beat-based lexical chain"); chain.append(badge("ENABLED · FRIEND ROOM", "good"), grid(rangeField("Beat Window", 2400, 800, 5000, " ms"), rangeField("Penalty Damage", 14, 5, 40), field("Lexicon", "english-core"), field("Chain Rule", "last-letter")), grid(toggle("Practice", true), toggle("Friend Room", true), toggle("Ranked", false)));
  page.append(grid(reflex, chain), notice("Ranked remains gated in this UI until admission evidence is explicitly approved.", "warn"), actionBar()); return page;
}

function renderBackgrounds(): HTMLElement {
  const page = el("div"); page.append(header("Visuals · Galaxy Art", "Backgrounds", "Quản lý G01–G10 background kits, plate/glow/hero, parallax, animation, brightness và quality variants. Preview dùng asset thật của Space Typing.", [btn("Compare Quality"), btn("Validate Assets", () => undefined, "st-admin-btn primary")]));
  const gallery = el("div", "stx-bg-gallery");
  for (const [id, name] of backgroundKits) {
    const card = panel(name, id, "stx-bg-card"); const image = el("img") as HTMLImageElement; image.src = `${ASSET}/backgrounds/${id}/plate-c.1280.webp`; image.alt = `${name} background`; image.loading = "lazy"; card.append(image, grid(rangeField("Brightness", 78), rangeField("Parallax", 42), rangeField("Motion", 36)), el("div", "st-admin-env-row")); const badges = card.querySelector(".st-admin-env-row"); badges?.append(badge("LOW", "info"), badge("MEDIUM", "info"), badge("HIGH", "good"), badge("ULTRA", "good")); gallery.append(card);
  }
  page.append(gallery); return page;
}

function renderVfx(): HTMLElement {
  const page = el("div"); page.append(header("Visuals · Combat Presentation", "VFX", "Player, Enemy, Boss, Skill, Hit, Explosion, Burn, Shield, Rage, Credit và Victory effects với scale/duration/opacity/intensity/blend/screen shake.", [btn("Play Sequence"), btn("+ VFX Profile", () => undefined, "st-admin-btn primary")]));
  const categories = ["Player Projectile", "Enemy Projectile", "Impact", "Explosion", "Burning", "Shield", "Rage", "Credit Pickup", "Victory"];
  const gallery = el("div", "stx-vfx-grid");
  categories.forEach((name, index) => { const card = panel(name, `vfx-profile-${index + 1}`); const preview = el("div", `stx-vfx-preview v${(index % 4) + 1}`); preview.append(el("i"), el("b")); card.append(preview, grid(rangeField("Scale", 70), rangeField("Intensity", 62), rangeField("Duration", 48))); gallery.append(card); });
  page.append(gallery); return page;
}

function renderUiAssets(): HTMLElement {
  const page = el("div"); page.append(header("Visuals · Interface Asset Registry", "UI Assets", "Registry cho icon, portrait, badge, currency, card và banner. Preview trên nền transparent/dark/light để tránh asset lỗi contrast.", [btn("Validate Registry"), btn("+ Asset", () => undefined, "st-admin-btn primary")]));
  const items = [["ship-vanguard", "Ship Portrait", "512×512"], ["credit-rare", "Currency", "128×128"], ["skill-chain", "Skill Icon", "256×256"], ["rank-champion", "Rank Badge", "256×256"], ["event-aurora", "Event Banner", "1920×640"], ["boss-warden", "Boss Portrait", "768×768"]];
  const gallery = el("div", "stx-asset-gallery");
  items.forEach(([id, type, size], index) => { const card = panel(id, `${type} · ${size}`); const preview = el("div", `stx-ui-asset-preview p${(index % 4) + 1}`, id.slice(0, 2).toUpperCase()); card.append(preview, el("div", "st-admin-env-row")); card.querySelector(".st-admin-env-row")?.append(badge("DARK", "good"), badge("LIGHT", "good"), badge("ALPHA", "info")); gallery.append(card); }); page.append(gallery); return page;
}

function renderSettings(): HTMLElement {
  const page = el("div"); page.append(header("System · Global Configuration", "General Settings", "Global defaults cho game, tutorial, save, network, maintenance và version. UI tách rõ dangerous settings khỏi normal defaults.", [btn("Validate"), btn("Save UI Draft", () => undefined, "st-admin-btn primary")]));
  const game = panel("Game Defaults", "Normal product defaults"); game.append(grid(field("Default Mode", "Campaign", "select", ["Campaign", "Recall", "Expedition"]), field("Default Ship", "Vanguard"), field("Difficulty", "Normal", "select", ["Easy", "Normal", "Hard"]), toggle("Tutorial Enabled", true), toggle("Pronunciation Default", true), toggle("Auto Save", true)));
  const system = panel("System & Network", "Runtime boundaries"); system.append(grid(field("Minimum Version", "0.1.0"), field("Auto-save Interval", "30s"), field("Reconnect Window", "20s"), toggle("Offline Play", true), toggle("Telemetry", true)));
  const danger = panel("Maintenance", "Danger zone", "stx-danger-panel"); danger.append(toggle("Maintenance Mode", false, "Blocks normal gameplay when production backend is mapped."), field("Maintenance Message", "Scheduled maintenance"), notice("Production maintenance requires explicit confirmation and affected-player estimate.", "bad")); page.append(grid(game, system), danger, actionBar()); return page;
}

function renderFlags(): HTMLElement {
  const page = el("div"); page.append(header("System · Controlled Rollout", "Feature Flags", "Rollout theo All, New Players, Cohort, Environment hoặc account list. Save/economy/competitive flags được đánh dấu dangerous.", [btn("Create Flag"), btn("Audit Rollouts", () => undefined, "st-admin-btn primary")]));
  const flags = [["voice-mode", "Voice Mode", 100, "All", "normal"], ["stamina", "Stamina / Warp", 100, "All", "economy"], ["pvp-reflex", "PvP Reflex", 100, "All", "competitive"], ["pvp-word-chain", "PvP Word Chain", 100, "All", "competitive"], ["new-boss-renderer", "New Boss Renderer", 25, "Cohort", "normal"], ["world-music-v2", "World Music Runtime V2", 100, "All", "normal"]] as const;
  const host = el("div", "stx-flag-list");
  for (const [id, name, rollout, scope, risk] of flags) { const row = panel(name, id); row.append(el("div", "stx-flag-row")); const body = row.querySelector<HTMLElement>(".stx-flag-row")!; body.append(rangeField("Rollout", rollout, 0, 100, "%"), field("Scope", scope, "select", ["All", "New Players", "Cohort", "Environment", "Accounts"]), badge(risk.toUpperCase(), risk === "normal" ? "info" : "warn"), toggle("Enabled", rollout > 0)); host.append(row); }
  page.append(host, actionBar("Mock rollout only. No production flag service write.")); return page;
}

function renderHistory(navigate: Navigate): HTMLElement {
  const page = el("div"); page.append(header("System · Immutable Operations", "History & Publish", "Revision history chi tiết với author, status, changed domains, deep diff, compare, validation, publish và rollback workflow.", [btn("Compare Revisions"), btn("New Draft", () => undefined, "st-admin-btn primary")]));
  const list = panel("Revisions", "Immutable mock history"); const host = el("div", "stx-revision-list");
  for (const row of revisions) { const item = el("button", `stx-revision${uiState.selectedRevision === row[0] ? " active" : ""}`) as HTMLButtonElement; item.type = "button"; item.append(el("strong", undefined, row[0]), badge(row[1], row[1] === "Published" ? "good" : row[1] === "Draft" ? "warn" : "bad"), el("span", undefined, row[3]), el("small", undefined, `${row[2]} · ${row[4]} · ${row[5]}`)); item.addEventListener("click", () => { uiState.selectedRevision = row[0]; navigate(`${BASE}/history`); }); host.append(item); } list.append(host);
  const detail = panel(`Revision ${uiState.selectedRevision}`, "Deep diff · mock"); detail.append(stats([["Added", "3", "changes", "good"], ["Modified", "8", "changes", "warn"], ["Removed", "1", "change", "bad"], ["Validation", "PASS", "UI mock", "good"]]));
  const diff = el("pre", "stx-diff"); diff.textContent = `World 05\n  Stage 091\n    Normal Music\n-   stellar-dawn\n+   silent-orbit\n+   deep-nebula\n\nAudio Defaults\n- Music 0.35\n+ Music 0.26\n\nVanguard\n- Shield 120\n+ Shield 135`;
  detail.append(diff, el("div", "st-admin-page-actions")); const actions = detail.querySelector<HTMLElement>(".st-admin-page-actions")!; actions.append(btn("Clone Draft"), btn("Validate"), btn("Rollback", () => undefined, "st-admin-btn danger"), btn("Publish", () => undefined, "st-admin-btn primary")); page.append(editorShell(list, detail)); return page;
}

function renderQa(): HTMLElement {
  const page = el("div"); page.append(header("Developer · Isolated Test Session", "QA Sandbox", "Tạo phiên test UI cho World/Stage/Ship/Equipment/Warp/Feature Flags mà không động canonical save và không nhận production rewards.", [badge("DEVELOPER ONLY", "warn"), btn("Create QA Session", () => undefined, "st-admin-btn primary")]));
  page.append(notice("QA SANDBOX · NO PRODUCTION REWARDS · NO CANONICAL SAVE. Đây hiện là UI design; capability/runtime isolation được map ở phase sau.", "warn"));
  const setup = panel("Session Setup", "Ephemeral QA profile"); setup.append(grid(field("Target World", "World 50", "select", ["World 01", "World 16", "World 33", "World 50"]), field("Stage", "998"), field("Ship", "Aegis", "select", ["Vanguard", "Aegis", "Reaper", "Volt"]), field("Equipment Preset", "All Legendary"), field("Warp", "Unlimited"), field("Credits", "999999"), field("Expiration", "60 minutes"), field("Mode", "Campaign")), grid(toggle("Disable Rewards", true), toggle("Sandbox Save", true), toggle("Allow Stage Override", true), toggle("Allow Ship Override", true)));
  const lifecycle = panel("Lifecycle", "Capability/session state"); lifecycle.append(makeTable(["State", "Behaviour"], [["Create", "Issue ephemeral capability"], ["Start", "New QA run boundary"], ["Active", "Sandbox persistence only"], ["Expire / Revoke", "Reject stale callbacks"], ["Destroy", "Dispose sandbox state"]])); page.append(grid(setup, lifecycle)); return page;
}

const renderers: Record<string, (navigate: Navigate) => HTMLElement> = {
  [`${BASE}/analytics`]: renderAnalytics,
  [`${BASE}/equipment`]: renderEquipment,
  [`${BASE}/skills`]: renderSkills,
  [`${BASE}/enemies`]: renderEnemies,
  [`${BASE}/bosses`]: renderBosses,
  [`${BASE}/stages`]: renderStages,
  [`${BASE}/typing-content`]: renderTypingContent,
  [`${BASE}/shop`]: renderShop,
  [`${BASE}/currencies`]: () => renderCurrencies(),
  [`${BASE}/rewards`]: () => renderRewards(),
  [`${BASE}/warp`]: () => renderWarp(),
  [`${BASE}/missions`]: renderMissions,
  [`${BASE}/expedition`]: () => renderExpedition(),
  [`${BASE}/events`]: () => renderEvents(),
  [`${BASE}/duel`]: () => renderDuel(),
  [`${BASE}/ranked`]: () => renderRanked(),
  [`${BASE}/alternative-modes`]: () => renderAlternativeModes(),
  [`${BASE}/backgrounds`]: () => renderBackgrounds(),
  [`${BASE}/vfx`]: () => renderVfx(),
  [`${BASE}/ui-assets`]: () => renderUiAssets(),
  [`${BASE}/settings`]: () => renderSettings(),
  [`${BASE}/flags`]: () => renderFlags(),
  [`${BASE}/history`]: renderHistory,
  [`${BASE}/qa`]: () => renderQa(),
};

export function renderExtendedAdminScreen(path: string, navigate: Navigate): HTMLElement | null {
  return renderers[path]?.(navigate) ?? null;
}
