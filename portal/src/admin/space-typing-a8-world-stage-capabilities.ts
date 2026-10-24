type A8Surface = "world" | "stage";
type Tone = "good" | "warn" | "info";

function el<K extends keyof HTMLElementTagNameMap>(tag: K, cls?: string, text?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (cls) node.className = cls;
  if (text !== undefined) node.textContent = text;
  return node;
}

function badge(label: string, tone: Tone): HTMLElement {
  return el("span", `st-admin-status ${tone}`, label);
}

function capabilityRow(label: string, detail: string, status: string, tone: Tone): HTMLElement {
  const row = el("div", "stx-toggle-row");
  const copy = el("div");
  copy.append(el("strong", undefined, label), el("small", undefined, detail));
  row.append(copy, badge(status, tone));
  return row;
}

export function attachA8WorldStageCapabilitySummary(page: HTMLElement, surface: A8Surface): HTMLElement {
  const panel = el("section", "st-admin-panel solid stx-panel");
  const head = el("div", "st-admin-panel-head");
  const copy = el("div");
  copy.append(
    el("h2", undefined, "A8 Capability Boundary"),
    el("p", undefined, "Only published fields with a validated production consumer are writable. Adjacent campaign systems stay read-only until a canonical persisted policy and runtime resolver exist."),
  );
  head.append(copy, badge("AUTHORITY VERIFIED", "good"));
  panel.append(head);

  panel.append(
    capabilityRow(
      "World Enemy Roster",
      "enemyRoster is revision-backed and resolved before production enemy selection. Publish applies on the next game session.",
      surface === "world" ? "EDITING · SUPPORTED NOW" : "SUPPORTED NOW",
      "good",
    ),
    capabilityRow(
      "Stage Gameplay Tuning",
      "enemyBudget, eliteChance and modifierSlots are resolved by the production Stage factory. Structural Stage identity remains bundled.",
      surface === "stage" ? "EDITING · SUPPORTED NOW" : "SUPPORTED NOW",
      "good",
    ),
    capabilityRow(
      "Routes",
      "Route graphs are deterministic campaign/player runtime state; there is no Admin route-authoring policy.",
      "READ-ONLY REFERENCE",
      "info",
    ),
    capabilityRow(
      "Objectives",
      "Objective definitions are derived from StageConfig and DifficultyProfile; no revision-backed per-Stage objective editor exists.",
      "READ-ONLY REFERENCE",
      "info",
    ),
    capabilityRow(
      "Daily / Weekly Challenges",
      "Challenge identity and seeds are deterministic runtime contracts and remain owned by the dedicated Live Ops surfaces.",
      "READ-ONLY REFERENCE",
      "info",
    ),
    capabilityRow(
      "Typing Assignment",
      "Typing Content remains a canonical read/reference catalog. No Stage-to-vocabulary or Stage-to-text assignment contract exists yet.",
      "DEFERRED / UNSUPPORTED",
      "warn",
    ),
  );

  const ownership = el("div", "stx-notice info", "World Music, Backgrounds and Rewards remain separate canonical Admin domains. A8 does not invent generic World media/reward fields.");
  panel.append(ownership);

  const anchor = page.children.item(1);
  if (anchor) page.insertBefore(panel, anchor);
  else page.append(panel);
  return page;
}
