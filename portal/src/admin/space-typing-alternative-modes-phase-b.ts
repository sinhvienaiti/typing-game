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
function isRecord(value: unknown): value is Record<string, unknown> { return value !== null && typeof value === "object" && !Array.isArray(value); }
function stringArray(value: unknown): value is string[] { return Array.isArray(value) && value.every((entry) => typeof entry === "string"); }
function validateAlternativeModesContract(value: unknown): AlternativeModesContractPayload {
  if (!isRecord(value) || value["capability"] !== "alternative-modes.read" || !isRecord(value["alternativeModes"])) throw new Error("Alternative Modes contract does not match alternative-modes.read.");
  const modes = value["alternativeModes"];
  if (modes["mode"] !== "runtime-backed-readonly") throw new Error("Alternative Modes contract is not runtime-backed read-only.");
  for (const key of ["runtimeSources", "supportedDuelMatchModes", "requestedPrototypeModes", "authorableFields", "unsupportedAdminMockFields"] as const) if (!stringArray(modes[key])) throw new Error(`Alternative Modes contract is missing ${key}.`);
  if (!Array.isArray(modes["implementations"]) || !isRecord(modes["runtimeImplementations"])) throw new Error("Alternative Modes implementation metadata is missing.");
  if (typeof modes["runtimeOwner"] !== "string" || typeof modes["persistenceOwner"] !== "string" || modes["writeCapability"] !== false || modes["previewCapability"] !== false || modes["rankedAdmissionCapability"] !== false) throw new Error("Alternative Modes ownership boundary changed; re-audit required.");
  return value as unknown as AlternativeModesContractPayload;
}

export function renderPhaseBAlternativeModes(): HTMLElement {
  const page = el("div");
  const head = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(
    el("div", "st-admin-eyebrow", "PvP · Runtime Mode Availability"),
    el("h1", undefined, "Alternative Modes"),
    el("p", undefined, "See which special Duel modes production actually supports and where players may use them. Runtime-owned tuning stays out of Admin until a publishable policy exists."),
  );
  const actions = el("div", "st-admin-page-actions");
  actions.append(badge("RUNTIME-BACKED", "good"), badge("RANKED FAIL-CLOSED", "warn"));
  head.append(copy, actions);
  page.append(head);

  const status = notice("Loading canonical Alternative Modes…");
  status.setAttribute("aria-live", "polite");
  const content = el("div");
  page.append(status, content);

  let generation = 0;
  const load = (): void => {
    const current = ++generation;
    setAdminStatus(status, "Loading canonical Alternative Modes…", "loading");
    void api.requestJson<unknown>("/api/admin/space-typing/alternative-modes/contract").then(validateAlternativeModesContract).then((payload) => {
      if (current !== generation) return;
      const modes = payload.alternativeModes;
      const available = modes.implementations.filter((entry) => entry.available);
      setAdminStatus(status, `${available.length} production alternative modes available · Ranked admission remains closed.`, "success");
      content.replaceChildren();

      const cards = el("div", "stx-grid");
      for (const implementation of modes.implementations) {
        const card = panel(implementation.id === "word-chain" ? "Word Chain" : implementation.id.charAt(0).toUpperCase() + implementation.id.slice(1), "Production capability");
        card.append(
          badge(implementation.available ? "AVAILABLE" : "UNAVAILABLE", implementation.available ? "good" : "warn"),
          notice(`Playable in: ${implementation.supportedMatchTypes.join(" · ") || "none"}`, implementation.available ? "good" : "warn"),
          notice(`Reconnect: ${implementation.reconnect ? "supported" : "not supported"} · persistence ${implementation.persistence}`),
          notice(`Ranked: ${implementation.rankedEligible ? "eligible" : "blocked"}`, implementation.rankedEligible ? "warn" : "good"),
        );
        cards.append(card);
      }

      const policy = panel("Admission Policy", "Alternative modes remain Friend / Practice features");
      policy.append(
        notice(`Canonical Duel match envelope: ${modes.supportedDuelMatchModes.join(" · ")}`),
        notice("Reflex and Word Chain are admitted only where the runtime implementation declares support. Ranked remains fail-closed.", "good"),
        notice("Mode enable toggles and tuning values are not exposed because no canonical Admin policy consumer exists.", "warn"),
      );

      const advanced = el("details", "st-admin-panel solid stx-panel");
      advanced.append(el("summary", undefined, "Advanced runtime ownership details"));
      const body = el("div", "stx-grid");
      body.append(
        notice(`Runtime owner: ${modes.runtimeOwner}`),
        notice(`Persistence: ${modes.persistenceOwner} · apply boundary ${modes.applyBoundary}`),
        notice(`Runtime sources: ${modes.runtimeSources.join(" · ")}`),
        notice(`Requested prototype modes: ${modes.requestedPrototypeModes.join(" · ")}`),
        notice(`Admin write: ${String(modes.writeCapability)} · Admin preview: ${String(modes.previewCapability)} · Ranked admission: ${String(modes.rankedAdmissionCapability)}`),
        notice(modes.diagnostic),
        notice(`Unsupported Admin fields: ${modes.unsupportedAdminMockFields.join(" · ")}`, "warn"),
      );
      advanced.append(body);
      content.append(cards, policy, advanced);
    }).catch((error: unknown) => {
      if (current !== generation) return;
      setAdminStatus(status, "Alternative Modes runtime contract is unavailable.", "error");
      renderAdminFailureState(content, {
        title: "Alternative Modes unavailable",
        fallbackMessage: "The canonical Alternative Modes contract could not be loaded.",
        error,
        onRetry: load,
      });
    });
  };
  load();
  return page;
}
