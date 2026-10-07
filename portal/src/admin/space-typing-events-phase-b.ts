import { SpaceTypingAdminApi } from "./api";

const api = new SpaceTypingAdminApi();
type Tone = "good" | "warn" | "bad" | "info";
type EventsRuntimeContract = {
  mode: "runtime-derived-readonly";
  runtimeSources: string[];
  domains: string[];
  authorableFields: string[];
  runtimeDerivedFields: string[];
  stageRandomEventIds: string[];
  stageRandomEventTones: string[];
  galaxyModifierIds: string[];
  sourceFunctions: string[];
  gameplayConsumer: string;
  persistenceOwner: string;
  scheduledLiveOpsService: false;
  calendarService: false;
  writeCapability: false;
  previewCapability: false;
  unsupportedMasterPlanFields: string[];
};
type EventsContractPayload = {
  contractRevision: string;
  schemaVersion: number;
  capability: "events.read";
  route: { id: string; path: string; label: string };
  events: EventsRuntimeContract;
};

function el<K extends keyof HTMLElementTagNameMap>(tag: K, cls?: string, text?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (cls) node.className = cls;
  if (text !== undefined) node.textContent = text;
  return node;
}
function badge(label: string, tone: Tone = "info"): HTMLElement { return el("span", `st-admin-status ${tone}`, label); }
function notice(text: string, tone: Tone = "info"): HTMLElement { return el("div", `stx-notice ${tone}`, text); }
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
function listNotice(label: string, values: string[], tone: Tone = "info"): HTMLElement {
  return notice(`${label}: ${values.join(" · ")}`, tone);
}
async function fetchEventsContract(): Promise<EventsContractPayload> {
  const response = await fetch("/api/admin/space-typing/events/contract", {
    cache: "no-store",
    headers: { "x-typing-game-admin-token": api.getToken() },
  });
  const payload = (await response.json().catch(() => ({}))) as Partial<EventsContractPayload> & { message?: string };
  if (!response.ok) throw new Error(payload.message ?? `Events contract request failed (${response.status})`);
  if (payload.capability !== "events.read" || !payload.events || !payload.route) {
    throw new Error("Pinned child Events contract does not expose events.read.");
  }
  return payload as EventsContractPayload;
}

export function renderPhaseBEvents(): HTMLElement {
  const page = el("div");
  const header = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(
    el("div", "st-admin-eyebrow", "Gameplay · Runtime Event Systems"),
    el("h1", undefined, "Events"),
    el("p", undefined, "Inspect event systems actually consumed during Space Typing stages. These are deterministic/chance-driven gameplay systems, not a remote Live Ops calendar, so Admin authoring and scheduling remain intentionally closed."),
  );
  const actions = el("div", "st-admin-page-actions");
  actions.append(badge("RUNTIME-BACKED · READ ONLY", "good"), badge("NO CALENDAR SERVICE", "warn"));
  header.append(copy, actions);
  page.append(header);

  const status = notice("Loading canonical Events runtime contract…");
  page.append(status);
  void (async () => {
    try {
      const payload = await fetchEventsContract();
      const events = payload.events;
      status.className = "stx-notice good";
      status.textContent = `${events.domains.length} runtime event domains · stage-session ownership · Admin writes closed.`;

      const stageEvents = panel("Stage Random Events", "Canonical stage-scheduler registry");
      stageEvents.append(
        listNotice("Event IDs", events.stageRandomEventIds, "good"),
        listNotice("Tones", events.stageRandomEventTones),
        notice("Selection is stage-seeded/chance-driven and bounded by each StageConfig modifierSlots value."),
      );

      const galaxyEvents = panel("Galaxy Stage Modifiers", "Special, hazard and gauntlet modifiers owned by runtime code");
      galaxyEvents.append(
        listNotice("Modifier IDs", events.galaxyModifierIds, "good"),
        notice("Galaxy modifiers are selected from StageConfig role/galaxy. Admin does not create a parallel event calendar."),
      );

      const runtimeSystems = panel("Chance-driven Stage Systems", "Additional event-like gameplay systems consumed by Game.ts");
      runtimeSystems.append(
        listNotice("Domains", events.domains),
        listNotice("Runtime functions", events.sourceFunctions),
        listNotice("Runtime-derived fields", events.runtimeDerivedFields),
      );

      const ownership = panel("Runtime Ownership", "Canonical sources and lifecycle boundary");
      ownership.append(
        listNotice("Runtime sources", events.runtimeSources),
        notice(`Gameplay consumer: ${events.gameplayConsumer}`, "good"),
        notice(`Persistence owner: ${events.persistenceOwner}`, "good"),
      );

      const boundary = panel("Admin Boundary", "No synthetic Live Ops scheduling is exposed");
      boundary.append(
        notice("Scheduled Live Ops service: unavailable", "warn"),
        notice("Calendar service: unavailable", "warn"),
        listNotice("Unsupported master-plan fields", events.unsupportedMasterPlanFields, "warn"),
        notice("Event creation, start/end windows, timezone/recurrence, audience targeting, enable toggles, draft saves and publishing are intentionally unavailable until a canonical runtime service owns them."),
      );
      page.append(stageEvents, galaxyEvents, runtimeSystems, ownership, boundary);
    } catch (error: unknown) {
      status.className = "stx-notice bad";
      status.textContent = `Events contract unavailable: ${error instanceof Error ? error.message : String(error)}`;
    }
  })();
  return page;
}
