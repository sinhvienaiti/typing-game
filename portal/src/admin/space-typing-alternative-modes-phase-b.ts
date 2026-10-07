import { SpaceTypingAdminApi } from "./api";

const api = new SpaceTypingAdminApi();
type Tone = "good" | "warn" | "bad" | "info";
type AlternativeModesContractPayload = {
  contractRevision: string;
  schemaVersion: number;
  capability: "alternative-modes.read";
  route: { id: string; path: string; label: string };
  alternativeModes: {
    mode: "runtime-absence-diagnostic";
    runtimeSources: string[];
    supportedDuelMatchModes: string[];
    requestedPrototypeModes: string[];
    runtimeImplementations: Record<string, boolean>;
    authorableFields: string[];
    writeCapability: false;
    previewCapability: false;
    rankedAdmissionCapability: false;
    persistenceOwner: "none";
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
    el("p", undefined, "This screen reports what the current Space Typing Duel runtime actually implements. Reflex and Word Chain remain prototype concepts only; Admin does not create settings, admission rules or Ranked toggles for modes that have no canonical runtime owner."),
  );
  const actions = el("div", "st-admin-page-actions");
  actions.append(badge("RUNTIME AUDIT · READ ONLY", "good"), badge("REFLEX / WORD CHAIN NOT CONNECTED", "warn"));
  head.append(copy, actions);
  page.append(head);

  const status = notice("Loading canonical Alternative Modes capability audit…");
  page.append(status);
  void (async () => {
    try {
      const payload = await fetchAlternativeModesContract();
      const modes = payload.alternativeModes;
      status.className = "stx-notice good";
      status.textContent = `${modes.supportedDuelMatchModes.length} canonical Duel match modes · ${modes.requestedPrototypeModes.length} unimplemented prototypes · Admin writes closed.`;

      const canonical = panel("Canonical Duel Modes", "Modes present in Duel authority/client match views");
      canonical.append(
        listNotice("Supported match modes", modes.supportedDuelMatchModes, "good"),
        notice("Friend, Ranked and Practice are the only canonical Duel match modes exposed by the current authority model."),
      );

      const prototypes = panel("Prototype Status", "Requested concepts without a runtime owner");
      for (const id of modes.requestedPrototypeModes) {
        prototypes.append(notice(`${id}: ${modes.runtimeImplementations[id] === true ? "IMPLEMENTED" : "NOT RUNTIME CONNECTED"}`, modes.runtimeImplementations[id] === true ? "good" : "warn"));
      }
      prototypes.append(notice(modes.diagnostic, "warn"));

      const evidence = panel("Audit Evidence", "Canonical files checked before closing Admin authoring");
      evidence.append(listNotice("Runtime sources", modes.runtimeSources));

      const boundary = panel("Admin Boundary", "No synthetic alternative-mode policy");
      boundary.append(
        notice(`Persistence owner: ${modes.persistenceOwner}`),
        notice(`Apply boundary: ${modes.applyBoundary}`),
        notice(`Admin write capability: ${String(modes.writeCapability)}`, "warn"),
        notice(`Admin preview capability: ${String(modes.previewCapability)}`, "warn"),
        notice(`Ranked admission capability: ${String(modes.rankedAdmissionCapability)}`, "warn"),
        listNotice("Unsupported legacy mock fields", modes.unsupportedAdminMockFields, "warn"),
        notice("Reaction/beat windows, damage values, challenge pools, lexicon/chain rules and Practice/Friend/Ranked enable toggles stay unavailable until a real runtime implementation owns them."),
      );

      page.append(canonical, prototypes, evidence, boundary);
    } catch (error: unknown) {
      status.className = "stx-notice bad";
      status.textContent = `Alternative Modes contract unavailable: ${error instanceof Error ? error.message : String(error)}`;
    }
  })();
  return page;
}
