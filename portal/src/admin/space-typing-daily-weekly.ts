function el<K extends keyof HTMLElementTagNameMap>(tag: K, cls?: string, text?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (cls) node.className = cls;
  if (text !== undefined) node.textContent = text;
  return node;
}

function btn(label: string, cls = "st-admin-btn"): HTMLButtonElement {
  const node = el("button", cls, label);
  node.type = "button";
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
  const table = el("table", "st-admin-table");
  const thead = el("thead");
  const tr = el("tr");
  headers.forEach((h) => tr.append(el("th", undefined, h)));
  thead.append(tr);
  const body = el("tbody");
  rows.forEach((row) => {
    const r = el("tr");
    row.forEach((cell) => { const td = el("td"); if (cell instanceof HTMLElement) td.append(cell); else td.textContent = cell; r.append(td); });
    body.append(r);
  });
  table.append(thead, body); wrap.append(table); return wrap;
}

export function renderDailyWeekly(): HTMLElement {
  const page = el("div");
  const head = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(el("div", "st-admin-eyebrow", "Live Ops · Recurring Rotation"), el("h1", undefined, "Daily / Weekly"), el("p", undefined, "Quản lý recurring resets, reward pools, rotating challenges và weekly milestones tách khỏi mission definition để Admin thấy rõ lịch Live Ops."));
  const actions = el("div", "st-admin-page-actions"); actions.append(btn("Rotation Calendar"), btn("+ New Rotation", "st-admin-btn primary")); head.append(copy, actions); page.append(head);

  const summary = el("div", "stx-stats");
  for (const [label, value, note, tone] of [["Daily Reset", "00:00 UTC", "23:03 remaining", "good"], ["Weekly Reset", "Monday", "6d 13h", "info"], ["Active Rotations", "7", "5 daily · 2 weekly", "good"], ["Scheduled", "3", "next 14 days", "warn"]] as const) {
    const card = el("article", "stx-stat"); card.append(el("span", undefined, label), el("strong", tone, value), el("small", undefined, note)); summary.append(card);
  }
  page.append(summary);

  const daily = panel("Daily Rotation", "Reset every day · Asia/Ho_Chi_Minh display");
  daily.append(table(["Slot", "Content", "Reward", "Requirement", "Reset", "Status"], [
    ["01", "Precision Pilot", "1,200 Credits", "Accuracy ≥95% ×3", "Daily", badge("ACTIVE", "good")],
    ["02", "Campaign Sprint", "1 Rare Credit", "Clear 5 stages", "Daily", badge("ACTIVE", "good")],
    ["03", "Duel Warmup", "800 Credits", "Play 3 Duel matches", "Daily", badge("ACTIVE", "good")],
    ["04", "Expedition Bonus", "+20% chest", "Complete 1 run", "Daily", badge("ACTIVE", "good")],
  ]));

  const weekly = panel("Weekly Rotation", "Longer objectives and larger rewards");
  weekly.append(table(["Milestone", "Target", "Reward", "Progress Window", "Status"], [
    ["Fleet Commander", "Clear 50 stages", "8 Rare Credits", "Mon → Sun", badge("ACTIVE", "good")],
    ["Arena Veteran", "Win 20 Duel matches", "Champion Chest", "Mon → Sun", badge("ACTIVE", "good")],
    ["Boss Hunter", "Defeat 10 bosses", "Legendary Fragment", "Mon → Sun", badge("ACTIVE", "good")],
    ["Perfect Week", "7 daily completions", "Event Crystal ×12", "Mon → Sun", badge("SCHEDULED", "warn")],
  ]));

  const calendar = panel("Upcoming Rotations", "Preview next 14 days");
  const timeline = el("div", "stx-event-timeline");
  for (const [title, when, detail, tone] of [["Aurora Daily", "Oct 07", "Aurora backdrop · accuracy mission", "good"], ["Boss Rush Weekly", "Oct 12", "Boss chain · rare credit bonus", "warn"], ["Void Week", "Oct 19", "World 46 spotlight · special drops", "info"]] as const) {
    const card = panel(title, when); card.append(el("p", "stx-copy", detail), badge("ROTATION", tone)); timeline.append(card);
  }
  calendar.append(timeline);
  page.append(daily, weekly, calendar);
  return page;
}
