import { SpaceTypingAdminApi } from "./api";

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
  return notice(`${label}: ${values.join(" · ")}`, tone);
}
async function fetchAlternativeModesContract(): Promise<AlternativeModesContractPayload> {
  const response = await fetch("/api/admin/space-typing/alternative-modes/contract", {
    cache: "no-store",
    headers: { "x-typing-game-admin-token": api.getToken() },
  });
  const payload = (await response.json().catch(() => ({}))) as Partial<AlternativeModesContractPayload> & { message?: string };
  if (!response.ok) throw new Error(payload.message ?? `Alternative Modes contract request failed (${response.status})`);
  if (payload.capability !== "alternative-modes.read" || !payload.alternativeModes || !payload.route) {
    throw new Error("Pinned child Alternative Modes contract does not expose alternative-modes.read.");
  }
  return payload as AlternativeModesContractPayload;
}

export function renderPhaseBAlternativeModes(): HTMLElement {
  const page = el("div");
  const head = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(
    el("div", "st-admin-eyebrow", "PvP · Runtime Capability Audit"),
    el("h1", undefined, "Alternative Modes"),
    el("p", undefined, "This screen reports the canonical Alternative Modes runtime. Reflex and Word Chain are runtime-backed for Friend and Practice matches, while Ranked admission remains fail-closed and Admin authoring stays unavailable."),
  );
  const actions = el("div", "st-admin-page-actions");
  actions.append(badge("RUNTIME-BACKED · READ ONLY", "good"), badge("RANKED FAIL-CLOSED", "warn"));
  head.append(copy, actions);
  page.append(head);

  const status = notice("Loading canonical Alternative Modes runtime contract…");
  page.append(status);
  void (async () => {
    try {
      const payload = await fetchAlternativeModesContract();
      const modes = payload.alternativeModes;
      const availableCount = modes.implementations.filter((entry) => entry.available).length;
      status.className = "stx-notice good";
      status.textContent = `${modes.supportedDuelMatchModes.length} canonical Duel match modes · ${availableCount} runtime-backed alternative modes · Admin writes closed.`;

      const canonical = panel("Canonical Duel Modes", "Match modes present in the Duel authority model");
      canonical.append(
        listNotice("Supported match modes", modes.supportedDuelMatchModes, "good"),
        notice("Friend, Ranked and Practice remain the canonical Duel match-mode envelope; Alternative Modes are admitted only through their own runtime policy."),
      );

      const implementations = panel("Alternative Runtime", "Canonical Friend/Practice implementations; Ranked admission remains closed");
      for (const implementation of modes.implementations) {
        const state = implementation.available ? "RUNTIME-BACKED" : "UNAVAILABLE";
        const ranked = implementation.rankedEligible ? "ranked eligible" : "ranked blocked";
        implementations.append(
          notice(
            `${implementation.id}: ${state} · ${implementation.supportedMatchTypes.join("/")} · ${implementation.persistence} · reconnect ${implementation.reconnect ? "yes" : "no"} · ${ranked}`,
            implementation.available ? "good" : "warn",
          ),
        );
      }
      implementations.append(notice(modes.diagnostic, "info"));

      const evidence = panel("Runtime Evidence", "Canonical owners used by the pinned child runtime");
      evidence.append(
        notice(`Runtime owner: ${modes.runtimeOwner}`),
        listNotice("Runtime sources", modes.runtimeSources),
      );

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

      page.append(canonical, implementations, evidence, boundary);
    } catch (error: unknown) {
      status.className = "stx-notice bad";
      status.textContent = `Alternative Modes contract unavailable: ${error instanceof Error ? error.message : String(error)}`;
    }
  })();
  return page;
}
