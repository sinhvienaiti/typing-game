function el<K extends keyof HTMLElementTagNameMap>(tag: K, cls?: string, text?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (cls) node.className = cls;
  if (text !== undefined) node.textContent = text;
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

function table(headers: readonly string[], rows: readonly (readonly (string | HTMLElement)[])[]): HTMLElement {
  const wrap = el("div", "st-admin-table-wrap");
  const grid = el("table", "st-admin-table");
  const thead = el("thead");
  const tr = el("tr");
  headers.forEach((header) => tr.append(el("th", undefined, header)));
  thead.append(tr);
  const body = el("tbody");
  rows.forEach((row) => {
    const line = el("tr");
    row.forEach((cell) => {
      const td = el("td");
      if (cell instanceof HTMLElement) td.append(cell); else td.textContent = cell;
      line.append(td);
    });
    body.append(line);
  });
  grid.append(thead, body);
  wrap.append(grid);
  return wrap;
}

export function renderDailyWeekly(): HTMLElement {
  const page = el("div");
  const head = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(
    el("div", "st-admin-eyebrow", "Live Ops · UI Prototype"),
    el("h1", undefined, "Daily / Weekly"),
    el("p", undefined, "Layout prototype only. The canonical Space Typing runtime currently exposes Stage Objectives, not recurring Daily / Weekly mission definitions, reset schedules, rotation calendars or reward pools."),
  );
  const actions = el("div", "st-admin-page-actions");
  actions.append(badge("UI MOCK · NOT RUNTIME CONNECTED", "warn"));
  head.append(copy, actions);
  page.append(head);

  const boundary = el("div", "stx-notice warn", "Authoring is disabled. Do not treat the sample resets, rewards, requirements or rotation dates below as canonical runtime values. A real Daily / Weekly control plane requires a child-owned persistence/apply consumer first.");
  page.append(boundary);

  const summary = el("div", "stx-stats");
  for (const [label, value, note, tone] of [["Daily Reset", "SAMPLE", "mock display only", "warn"], ["Weekly Reset", "SAMPLE", "mock display only", "warn"], ["Active Rotations", "—", "runtime unavailable", "info"], ["Scheduled", "—", "runtime unavailable", "info"]] as const) {
    const card = el("article", "stx-stat");
    card.append(el("span", undefined, label), el("strong", tone, value), el("small", undefined, note));
    summary.append(card);
  }
  page.append(summary);

  const daily = panel("Daily Rotation · Sample Layout", "Non-canonical mock rows retained only for UI review");
  daily.append(table(["Slot", "Sample Content", "Sample Reward", "Sample Requirement", "Reset", "Status"], [
    ["01", "Precision Pilot", "1,200 Credits", "Accuracy ≥95% ×3", "Sample", badge("MOCK", "warn")],
    ["02", "Campaign Sprint", "1 Rare Credit", "Clear 5 stages", "Sample", badge("MOCK", "warn")],
    ["03", "Duel Warmup", "800 Credits", "Play 3 Duel matches", "Sample", badge("MOCK", "warn")],
    ["04", "Expedition Bonus", "+20% chest", "Complete 1 run", "Sample", badge("MOCK", "warn")],
  ]));

  const weekly = panel("Weekly Rotation · Sample Layout", "No runtime recurring mission catalog exists yet");
  weekly.append(table(["Sample Milestone", "Sample Target", "Sample Reward", "Window", "Status"], [
    ["Fleet Commander", "Clear 50 stages", "8 Rare Credits", "Sample", badge("MOCK", "warn")],
    ["Arena Veteran", "Win 20 Duel matches", "Champion Chest", "Sample", badge("MOCK", "warn")],
    ["Boss Hunter", "Defeat 10 bosses", "Legendary Fragment", "Sample", badge("MOCK", "warn")],
    ["Perfect Week", "7 daily completions", "Event Crystal ×12", "Sample", badge("MOCK", "warn")],
  ]));

  const next = panel("Runtime Requirement", "What must exist before this screen can become authorable");
  next.append(
    el("div", "stx-notice info", "Required child seams: recurring mission definitions, canonical reset semantics, rotation persistence, reward-pool references and a runtime apply boundary."),
    el("div", "stx-notice info", "Until those seams exist, Missions remains a read-only view of Stage Objectives and this Daily / Weekly screen remains a clearly labeled UI prototype."),
  );

  page.append(daily, weekly, next);
  return page;
}
