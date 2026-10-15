import { SpaceTypingAdminApi } from "./api";
import { renderAdminFailureState, setAdminStatus } from "./space-typing-admin-state";

const api = new SpaceTypingAdminApi();
type Navigate = (path: string) => void;
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
type ShopCapabilityField = {
  name: string;
  source: string;
  authorable: boolean;
  reason: string;
};
type ShopCapabilityManifest = {
  protocolVersion: 4;
  mode: "runtime-backed-authoring" | "runtime-backed-readonly";
  fields: ShopCapabilityField[];
  capabilities: {
    offerWrite: boolean;
    schedules: boolean;
    preview: boolean;
  } & Record<string, boolean>;
  authoring: {
    enabled: boolean;
    configNamespace: string;
    applyBoundary: string;
    reason: string;
  };
  preview: {
    available: boolean;
    mutation: boolean;
    reason: string;
  };
};

function el<K extends keyof HTMLElementTagNameMap>(tag: K, cls?: string, text?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (cls) node.className = cls;
  if (text !== undefined) node.textContent = text;
  return node;
}
function badge(label: string, tone: Tone = "info"): HTMLElement { return el("span", `st-admin-status ${tone}`, label); }
function notice(text: string, tone: Tone = "info"): HTMLElement { return el("div", `stx-notice ${tone}`, text); }
function button(label: string, onClick: () => void, cls = "st-admin-btn"): HTMLButtonElement {
  const node = el("button", cls, label) as HTMLButtonElement;
  node.type = "button";
  node.addEventListener("click", onClick);
  return node;
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
function isRecord(value: unknown): value is Record<string, unknown> {
  return value !== null && typeof value === "object" && !Array.isArray(value);
}
function stringArray(value: unknown): value is string[] {
  return Array.isArray(value) && value.every((entry) => typeof entry === "string");
}
function validateEventsContract(value: unknown): EventsContractPayload {
  if (!isRecord(value) || value["capability"] !== "events.read" || !isRecord(value["events"])) {
    throw new Error("Events contract does not match the canonical events.read boundary.");
  }
  const events = value["events"];
  for (const key of ["runtimeSources", "domains", "authorableFields", "runtimeDerivedFields", "stageRandomEventIds", "stageRandomEventTones", "galaxyModifierIds", "sourceFunctions", "unsupportedMasterPlanFields"] as const) {
    if (!stringArray(events[key])) throw new Error(`Events contract is missing ${key}.`);
  }
  if (
    events["mode"] !== "runtime-derived-readonly" ||
    events["scheduledLiveOpsService"] !== false ||
    events["calendarService"] !== false ||
    events["writeCapability"] !== false ||
    events["previewCapability"] !== false ||
    typeof events["gameplayConsumer"] !== "string" ||
    typeof events["persistenceOwner"] !== "string"
  ) throw new Error("Events contract contains an invalid runtime ownership boundary.");
  return value as unknown as EventsContractPayload;
}
function validateShopCapabilities(value: unknown): ShopCapabilityManifest {
  if (!isRecord(value) || value["protocolVersion"] !== 4 || !isRecord(value["capabilities"]) || !isRecord(value["authoring"]) || !isRecord(value["preview"]) || !Array.isArray(value["fields"])) {
    throw new Error("Shop capability response does not match protocol v4.");
  }
  return value as unknown as ShopCapabilityManifest;
}
async function fetchLiveOpsCapabilities(): Promise<Readonly<{ events: EventsContractPayload; shop: ShopCapabilityManifest }>> {
  const [events, shop] = await Promise.all([
    api.requestJson<unknown>("/api/admin/space-typing/events/contract").then(validateEventsContract),
    api.requestJson<unknown>("/api/admin/space-typing/shop/capabilities").then(validateShopCapabilities),
  ]);
  return Object.freeze({ events, shop });
}

export function renderPhaseBEvents(navigate: Navigate): HTMLElement {
  const page = el("div");
  const header = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(
    el("div", "st-admin-eyebrow", "Operations · Runtime-owned Live Ops"),
    el("h1", undefined, "Live Ops"),
    el("p", undefined, "Operate only capabilities that production currently owns. Shop offers provide real unscheduled promotions/discount presentation; gameplay events remain runtime-driven, and no remote calendar or announcement service is fabricated."),
  );
  const actions = el("div", "st-admin-page-actions");
  actions.append(badge("RUNTIME-BACKED", "good"), badge("NO CALENDAR SERVICE", "warn"), badge("NO FAKE ANNOUNCEMENTS", "info"));
  header.append(copy, actions);
  page.append(header);

  const status = notice("Loading Live Ops capabilities…");
  status.setAttribute("aria-live", "polite");
  const content = el("div");
  page.append(status, content);

  let loadGeneration = 0;
  const load = (): void => {
    const generation = ++loadGeneration;
    setAdminStatus(status, "Loading canonical Events and Shop capability contracts…", "loading");
    content.replaceChildren(notice("Resolving production ownership for Events, Promotions, Discounts and Announcements…"));

    void fetchLiveOpsCapabilities().then(({ events: payload, shop }) => {
      if (generation !== loadGeneration) return;
      const events = payload.events;
      const originalPrice = shop.fields.find((field) => field.name === "Original Price");
      const badgeField = shop.fields.find((field) => field.name === "Badge / Label");
      const enabledField = shop.fields.find((field) => field.name === "Enabled");
      const offerAuthoring = shop.authoring.enabled && shop.capabilities.offerWrite && originalPrice?.authorable === true && badgeField?.authorable === true && enabledField?.authorable === true;

      setAdminStatus(
        status,
        offerAuthoring
          ? "Live Ops ownership resolved · Shop promotions/discounts authorable · scheduling/announcements unavailable."
          : "Live Ops ownership resolved · no safe promotion authoring seam · scheduling/announcements unavailable.",
        offerAuthoring ? "success" : "warning",
      );

      const overview = el("div", "stx-grid");
      const gameplay = panel("Gameplay Events", "Stage-owned chance/deterministic systems");
      gameplay.append(
        badge("READ ONLY", "good"),
        notice(`${events.stageRandomEventIds.length} stage random events · ${events.galaxyModifierIds.length} galaxy modifiers.`),
        notice("These events are selected by production stage/runtime logic. Admin does not turn them into a remote campaign calendar."),
      );

      const promotions = panel("Promotions & Discounts", "Canonical owner: Shop Offers");
      if (offerAuthoring) {
        promotions.append(
          badge("AUTHORABLE IN SHOP", "good"),
          notice("Price + Original Price drive discount presentation; Badge / Label and Enabled are persisted in the canonical Shop policy. Discount percentage remains derived, not independently stored."),
          notice(shop.preview.available ? "Production Shop simulation is available before saving/publishing." : "Shop preview is currently unavailable.", shop.preview.available ? "good" : "warn"),
          button("Open Shop offers", () => navigate("/admin/space-typing/shop"), "st-admin-btn primary"),
        );
      } else {
        promotions.append(
          badge("READ ONLY", "warn"),
          notice("The pinned runtime does not expose a safe writable Shop offer seam, so promotion controls remain closed.", "warn"),
        );
      }

      const announcements = panel("Announcements", "No canonical player-facing announcement service");
      announcements.append(
        badge("UNAVAILABLE", "warn"),
        notice("There is no production announcement/message owner, delivery channel, audience model or persistence contract. Admin does not save fake announcement drafts."),
      );

      const scheduling = panel("Scheduling", "No production calendar/recurrence service");
      scheduling.append(
        badge("UNAVAILABLE", "warn"),
        notice(`Gameplay Events calendar: ${String(events.calendarService)} · Shop schedules: ${String(shop.capabilities.schedules)}.`),
        notice("Start/end windows, timezone, recurrence and audience targeting remain closed until a canonical runtime/backend service owns them."),
      );
      overview.append(gameplay, promotions, announcements, scheduling);

      const advanced = el("details", "st-admin-panel solid stx-panel");
      const summary = el("summary", undefined, "Advanced runtime evidence");
      const evidence = el("div", "stx-grid");
      evidence.append(
        notice(`Events consumer: ${events.gameplayConsumer}`),
        notice(`Events persistence: ${events.persistenceOwner}`),
        notice(`Event domains: ${events.domains.join(" · ") || "none"}`),
        notice(`Runtime sources: ${events.runtimeSources.join(" · ") || "none"}`),
        notice(`Shop namespace: ${shop.authoring.configNamespace} · apply boundary: ${shop.authoring.applyBoundary}`),
        notice(`Unsupported Live Ops fields: ${events.unsupportedMasterPlanFields.join(" · ") || "none"}`, "warn"),
      );
      advanced.append(summary, evidence);
      content.replaceChildren(overview, advanced);
    }).catch((error: unknown) => {
      if (generation !== loadGeneration) return;
      setAdminStatus(status, "Live Ops capability contracts are unavailable.", "error");
      renderAdminFailureState(content, {
        title: "Live Ops unavailable",
        fallbackMessage: "The canonical Events/Shop capability contracts could not be loaded.",
        error,
        onRetry: load,
      });
    });
  };

  load();
  return page;
}
