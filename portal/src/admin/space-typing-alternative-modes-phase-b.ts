import { SpaceTypingAdminApi } from "./api";
import { renderAdminFailureState, setAdminStatus } from "./space-typing-admin-state";

const api = new SpaceTypingAdminApi();
type Tone = "good" | "warn" | "bad" | "info";
type AlternativeModeImplementation = {
  id: string;
  available: boolean;
  supportedMatchTypes: string[];
  rankedEligible: boolean;
  persistence: string;
  reconnect: boolean;
};
type AlternativeModesContractPayload = {
  contractRevision: string;
  schemaVersion: number;
  capability: "alternative-modes.read";
  route: { id: string; path: string; label: string };
  alternativeModes: {
    mode: "runtime-backed-readonly";
    runtimeSources: string[];
    runtimeOwner: string;
    supportedDuelMatchModes: string[];
    requestedPrototypeModes: string[];
    runtimeImplementations: Record<string, boolean>;
    implementations: AlternativeModeImplementation[];
    authorableFields: string[];
    writeCapability: false;
    previewCapability: false;
    rankedAdmissionCapability: false;
    persistenceOwner: string;
    applyBoundary: "none";
    unsupportedAdminMockFields: string[];
    diagnostic: string;
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
function listNotice(label: string, values: readonly string[], tone: Tone = "info"): HTMLElement {
  return notice(`${label}: ${values.length ? values.join(" · ") : "none exposed"}`, tone);
}
function isRecord(value: unknown): value is Record<string, unknown> {
  return value !== null && typeof value === "object" && !Array.isArray(value);
}
function stringArray(value: unknown): value is string[] { return Array.isArray(value) && value.every((entry) => typeof entry === "string"); }

function validateAlternativeModesContract(value: unknown): AlternativeModesContractPayload {
  if (!isRecord(value) || value["capability"] !== "alternative-modes.read" || !isRecord(value["alternativeModes"]) || !isRecord(value["route"])) {
    throw new Error("Alternative Modes contract does not match the canonical alternative-modes.read boundary.");
  }
  const modes = value["alternativeModes"];
  if (modes["mode"] !== "runtime-backed-readonly") throw new Error("Alternative Modes contract is not runtime-backed read-only.");
  for (const key of ["runtimeSources", "supportedDuelMatchModes", "requestedPrototypeModes", "authorableFields", "unsupportedAdminMockFields"] as const) {
    if (!stringArray(modes[key])) throw new Error(`Alternative Modes contract is missing ${key}.`);
  }
  if (!Array.isArray(modes["implementations"]) || !isRecord(modes["runtimeImplementations"])) {
    throw new Error("Alternative Modes contract is missing implementation metadata.");
  }
  for (const implementation of modes["implementations"]) {
    if (!isRecord(implementation) || typeof implementation["id"] !== "string" || typeof implementation["available"] !== "boolean" || !stringArray(implementation["supportedMatchTypes"])) {
      throw new Error("Alternative Modes contract contains an invalid runtime implementation.");
    }
  }
  if (
    typeof modes["runtimeOwner"] !== "string" ||
    typeof modes["persistenceOwner"] !== "string" ||
    modes["applyBoundary"] !== "none" ||
    modes["writeCapability"] !== false ||
    modes["previewCapability"] !== false ||
    modes["rankedAdmissionCapability"] !== false ||
    typeof modes["diagnostic"] !== "string"
  ) {
    throw new Error("Alternative Modes contract contains an invalid fail-closed ownership boundary.");
  }
  return value as unknown as AlternativeModesContractPayload;
}

async function fetchAlternativeModesContract(): Promise<AlternativeModesContractPayload> {
  return validateAlternativeModesContract(await api.requestJson<unknown>("/api/admin/space-typing/alternative-modes/contract"));
}

export function renderPhaseBAlternativeModes(): HTMLElement {
  const page = el("div");
  const head = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(
    el("div", "st-admin-eyebrow", "PvP · Runtime Capability Audit"),
    el("h1", undefined, "Alternative Modes"),
    el("p", undefined, "Inspect the canonical Alternative Modes runtime. Reflex and Word Chain are runtime-backed for Friend and Practice matches, while Ranked admission remains fail-closed and Admin authoring stays unavailable."),
  );
  const actions = el("div", "st-admin-page-actions");
  actions.append(badge("RUNTIME-BACKED · READ ONLY", "good"), badge("RANKED FAIL-CLOSED", "warn"));
  head.append(copy, actions);
  page.append(head);

  const status = notice("Loading canonical Alternative Modes runtime contract…");
  status.setAttribute("aria-live", "polite");
  const content = el("div");
  page.append(status, content);

  let loadGeneration = 0;
  const load = (): void => {
    const generation = ++loadGeneration;
    setAdminStatus(status, "Loading canonical Alternative Modes runtime contract…", "loading");
    content.replaceChildren(notice("Loading runtime mode ownership…", "info"));
    void fetchAlternativeModesContract().then((payload) => {
      if (generation !== loadGeneration) return;
      const modes = payload.alternativeModes;
      const availableCount = modes.implementations.filter((entry) => entry.available).length;
      setAdminStatus(status, `${modes.supportedDuelMatchModes.length} canonical Duel match modes · ${availableCount} runtime-backed alternative modes · Admin writes closed.`, "success");
      content.replaceChildren();

      const canonical = panel("Canonical Duel Modes", "Match modes present in the Duel authority model");
      canonical.append(
        listNotice("Supported match modes", modes.supportedDuelMatchModes, "good"),
        notice("Friend, Ranked and Practice remain the canonical Duel match-mode envelope; Alternative Modes are admitted only through their own runtime policy."),
      );

      const implementations = panel("Alternative Runtime", "Canonical Friend/Practice implementations; Ranked admission remains closed");
      if (modes.implementations.length === 0) implementations.append(notice("No Alternative Mode implementations are exposed by the current runtime.", "info"));
      for (const implementation of modes.implementations) {
        const state = implementation.available ? "RUNTIME-BACKED" : "UNAVAILABLE";
        const ranked = implementation.rankedEligible ? "ranked eligible" : "ranked blocked";
        implementations.append(
          notice(
            `${implementation.id}: ${state} · ${implementation.supportedMatchTypes.join("/") || "no match type"} · ${implementation.persistence} · reconnect ${implementation.reconnect ? "yes" : "no"} · ${ranked}`,
            implementation.available ? "good" : "warn",
          ),
        );
      }
      implementations.append(notice(modes.diagnostic, "info"));

      const evidence = panel("Runtime Evidence", "Canonical owners used by the pinned child runtime");
      evidence.append(notice(`Runtime owner: ${modes.runtimeOwner}`), listNotice("Runtime sources", modes.runtimeSources));

      const boundary = panel("Admin Boundary", "Runtime truth is visible; gameplay policy is not authorable here");
      boundary.append(
        notice(`Persistence owner: ${modes.persistenceOwner}`),
        notice(`Apply boundary: ${modes.applyBoundary}`),
        notice(`Admin write capability: ${String(modes.writeCapability)}`, "warn"),
        notice(`Admin preview capability: ${String(modes.previewCapability)}`, "warn"),
        notice(`Ranked admission capability: ${String(modes.rankedAdmissionCapability)}`, "warn"),
        listNotice("Unsupported legacy mock fields", modes.unsupportedAdminMockFields, "warn"),
        notice("Reaction/beat windows, damage values, challenge pools, lexicon/chain rules and enable toggles remain unavailable to Admin. The canonical runtime owns Friend/Practice execution and Ranked stays fail-closed."),
      );
      content.append(canonical, implementations, evidence, boundary);
    }).catch((error: unknown) => {
      if (generation !== loadGeneration) return;
      setAdminStatus(status, "Alternative Modes runtime contract is unavailable.", "error");
      renderAdminFailureState(content, {
        title: "Alternative Modes unavailable",
        fallbackMessage: "The canonical Alternative Modes contract could not be loaded. Check the local Admin runtime and try again.",
        error,
        onRetry: load,
      });
    });
  };

  load();
  return page;
}
