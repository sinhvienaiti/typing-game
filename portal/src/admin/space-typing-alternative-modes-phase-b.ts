import { SpaceTypingAdminApi } from "./api";

const api = new SpaceTypingAdminApi();
type Tone = "good" | "warn" | "bad" | "info";
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
    implementations: Array<{
      id: "reflex" | "word-chain";
      available: true;
      supportedMatchTypes: Array<"friend" | "practice">;
      rankedEligible: false;
      persistence: "snapshot-v1";
      reconnect: true;
    }>;
    authorableFields: string[];
    writeCapability: false;
    previewCapability: false;
    rankedAdmissionCapability: false;
    persistenceOwner: string;
    applyBoundary: "none";
    unsupportedAdminMockFields: string[];
    diagnostic: string;
    unsupportedAdminOperations: string[];
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
  if (
    payload.capability !== "alternative-modes.read" ||
    payload.alternativeModes?.mode !== "runtime-backed-readonly" ||
    !payload.route
  ) {
    throw new Error("Pinned child Alternative Modes contract does not expose the canonical runtime-backed read-only boundary.");
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
    el("p", undefined, "Inspect the canonical Reflex and Word Chain runtimes. They support Friend and Practice only; Ranked admission remains fail-closed and Admin does not fabricate tuning or enable toggles."),
  );
  const actions = el("div", "st-admin-page-actions");
  actions.append(badge("RUNTIME-BACKED · READ ONLY", "good"), badge("RANKED · FAIL CLOSED", "warn"));
  head.append(copy, actions);
  page.append(head);

  const status = notice("Loading canonical Alternative Modes runtime contract…");
  page.append(status);
  void (async () => {
    try {
      const payload = await fetchAlternativeModesContract();
      const modes = payload.alternativeModes;
      status.className = "stx-notice good";
      status.textContent = `${modes.implementations.length} canonical alternative modes · Friend/Practice runtime-backed · Admin writes closed.`;

      const implementations = panel("Canonical Alternative Modes", "Current authoritative runtime registration");
      for (const mode of modes.implementations) {
        implementations.append(
          notice(`${mode.id}: AVAILABLE · ${mode.supportedMatchTypes.join(" / ")} · persistence ${mode.persistence} · reconnect ${String(mode.reconnect)}`, "good"),
          notice(`${mode.id}: Ranked eligible = ${String(mode.rankedEligible)}`, "warn"),
        );
      }
      implementations.append(notice(modes.diagnostic));

      const evidence = panel("Runtime Ownership", "Contract is bound to real current Child owners");
      evidence.append(
        notice(`Runtime owner: ${modes.runtimeOwner}`, "good"),
        notice(`Persistence owner: ${modes.persistenceOwner}`),
        listNotice("Runtime sources", modes.runtimeSources),
      );

      const boundary = panel("Admin Boundary", "No synthetic alternative-mode policy");
      boundary.append(
        notice(`Apply boundary: ${modes.applyBoundary}`),
        notice(`Admin write capability: ${String(modes.writeCapability)}`, "warn"),
        notice(`Admin preview capability: ${String(modes.previewCapability)}`, "warn"),
        notice(`Ranked admission capability: ${String(modes.rankedAdmissionCapability)}`, "warn"),
        listNotice("Unsupported authoring fields", modes.unsupportedAdminMockFields, "warn"),
        listNotice("Unsupported operations", modes.unsupportedAdminOperations, "warn"),
      );

      page.append(implementations, evidence, boundary);
    } catch (error: unknown) {
      status.className = "stx-notice bad";
      status.textContent = `Alternative Modes contract unavailable: ${error instanceof Error ? error.message : String(error)}`;
    }
  })();
  return page;
}
