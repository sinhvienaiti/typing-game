import { SpaceTypingAdminApi } from "./api";
import { renderAdminFailureState, setAdminStatus } from "./space-typing-admin-state";

const api = new SpaceTypingAdminApi();

type ExpeditionContractPayload = {
  contractRevision: string;
  schemaVersion: number;
  capability: "expedition.read";
  route: { id: "expedition"; path: string; label: string };
  expedition: {
    mode: "runtime-backed-browser-persisted-run-readonly";
    runtimeSources: string[];
    runtimeOwner: string;
    runVersion: number;
    rulesetVersion: string;
    contentVersion: string;
    startKitId: string;
    encounterCount: number;
    draftBeforeEncounterIndexes: number[];
    restAfterEncounterIndex: number;
    phases: string[];
    challengeKinds: string[];
    persistence: {
      owner: string;
      storageKey: string;
      revisionedEnvelope: boolean;
      writerOwnership: boolean;
      writeVerification: boolean;
      resumableNonTerminalRun: boolean;
    };
    safety: {
      campaignFixtureFrozenInRun: boolean;
      campaignFixtureHashChecked: boolean;
      adminWriteCapability: false;
      adminPublishCapability: false;
      adminRunMutationCapability: false;
      adminStorageMutationCapability: false;
    };
    adminReadableSignals: string[];
    unsupportedAdminOperations: string[];
  };
};

function escapeHtml(value: unknown): string {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}
function chipList(values: readonly (string | number)[]): string {
  return `<div class="st-admin-chip-list">${values.map((value) => `<span class="st-admin-chip">${escapeHtml(value)}</span>`).join("")}</div>`;
}
function record(value: unknown): value is Record<string, unknown> {
  return value !== null && typeof value === "object" && !Array.isArray(value);
}
function stringArray(value: unknown): value is string[] {
  return Array.isArray(value) && value.every((entry) => typeof entry === "string");
}
function numberArray(value: unknown): value is number[] {
  return Array.isArray(value) && value.every((entry) => typeof entry === "number" && Number.isFinite(entry));
}

async function fetchExpeditionContract(): Promise<ExpeditionContractPayload> {
  const payload = await api.requestJson<unknown>("/api/admin/space-typing/expedition/contract");
  if (!record(payload) || payload["capability"] !== "expedition.read" || !record(payload["expedition"])) {
    throw new Error("Expedition contract does not match the canonical read-only runtime boundary.");
  }
  const expedition = payload["expedition"];
  if (
    expedition["mode"] !== "runtime-backed-browser-persisted-run-readonly" ||
    typeof expedition["runtimeOwner"] !== "string" ||
    !stringArray(expedition["runtimeSources"]) ||
    !stringArray(expedition["phases"]) ||
    !stringArray(expedition["challengeKinds"]) ||
    !numberArray(expedition["draftBeforeEncounterIndexes"]) ||
    !record(expedition["persistence"]) ||
    !record(expedition["safety"]) ||
    !stringArray(expedition["adminReadableSignals"]) ||
    !stringArray(expedition["unsupportedAdminOperations"]) ||
    expedition["safety"]["adminWriteCapability"] !== false ||
    expedition["safety"]["adminStorageMutationCapability"] !== false
  ) {
    throw new Error("Expedition contract is missing canonical runtime ownership or safety metadata.");
  }
  return payload as unknown as ExpeditionContractPayload;
}

export function renderPhaseBExpedition(): HTMLElement {
  const root = document.createElement("section");
  root.className = "space-admin-page space-admin-page--phase-b";
  root.innerHTML = `
    <header class="space-admin-page__header">
      <div>
        <p class="st-admin-eyebrow">Live Ops · Expedition Runtime Ownership</p>
        <h1>Expedition</h1>
        <p>Inspect deterministic production Expedition rules and browser-owned persistence without creating a second run controller in Admin.</p>
      </div>
      <div class="space-admin-page__badges">
        <span class="st-admin-badge">RUNTIME-BACKED · READ ONLY</span>
        <span class="st-admin-badge">BROWSER SAVE · NO REMOTE MUTATION</span>
      </div>
    </header>
    <p class="st-admin-notice" data-expedition-status aria-live="polite">Loading canonical Expedition contract…</p>
    <div class="space-admin-grid" data-expedition-content></div>
  `;

  const status = root.querySelector<HTMLElement>("[data-expedition-status]");
  const content = root.querySelector<HTMLElement>("[data-expedition-content]");
  if (!status || !content) return root;

  let loadGeneration = 0;
  const load = (): void => {
    const generation = ++loadGeneration;
    setAdminStatus(status, "Loading canonical Expedition contract…", "loading");
    content.replaceChildren();

    void fetchExpeditionContract()
      .then((contract) => {
        if (generation !== loadGeneration) return;
        const expedition = contract.expedition;
        setAdminStatus(status, `Ruleset ${expedition.rulesetVersion} · ${expedition.encounterCount} encounters · browser-local resumable run · Admin writes closed.`, "success");
        content.innerHTML = `
          <article class="st-admin-card">
            <div class="st-admin-card__header"><div><p class="st-admin-eyebrow">Canonical</p><h2>Production run model</h2></div></div>
            <p><strong>Owner:</strong> ${escapeHtml(expedition.runtimeOwner)}</p>
            <p><strong>Run version:</strong> ${escapeHtml(expedition.runVersion)}</p>
            <p><strong>Ruleset:</strong> ${escapeHtml(expedition.rulesetVersion)}</p>
            <p><strong>Content:</strong> ${escapeHtml(expedition.contentVersion)}</p>
            <p><strong>Start kit:</strong> ${escapeHtml(expedition.startKitId)}</p>
            <p><strong>Runtime sources:</strong></p>
            <ul>${expedition.runtimeSources.map((source) => `<li><code>${escapeHtml(source)}</code></li>`).join("")}</ul>
          </article>
          <article class="st-admin-card">
            <div class="st-admin-card__header"><div><p class="st-admin-eyebrow">Flow</p><h2>Encounter boundaries</h2></div></div>
            <p><strong>Encounter count:</strong> ${escapeHtml(expedition.encounterCount)}</p>
            <p><strong>Draft before indexes:</strong></p>${chipList(expedition.draftBeforeEncounterIndexes)}
            <p><strong>Rest after index:</strong> ${escapeHtml(expedition.restAfterEncounterIndex)}</p>
            <p><strong>Phases:</strong></p>${chipList(expedition.phases)}
            <p><strong>Challenge kinds:</strong></p>${chipList(expedition.challengeKinds)}
          </article>
          <article class="st-admin-card">
            <div class="st-admin-card__header"><div><p class="st-admin-eyebrow">Persistence</p><h2>Browser-owned resumable run</h2></div></div>
            <p><strong>Owner:</strong> ${escapeHtml(expedition.persistence.owner)}</p>
            <p><strong>Storage key:</strong> <code>${escapeHtml(expedition.persistence.storageKey)}</code></p>
            <p><strong>Revisioned envelope:</strong> ${String(expedition.persistence.revisionedEnvelope)}</p>
            <p><strong>Writer ownership:</strong> ${String(expedition.persistence.writerOwnership)}</p>
            <p><strong>Write verification:</strong> ${String(expedition.persistence.writeVerification)}</p>
            <p><strong>Resumable non-terminal run:</strong> ${String(expedition.persistence.resumableNonTerminalRun)}</p>
          </article>
          <article class="st-admin-card">
            <div class="st-admin-card__header"><div><p class="st-admin-eyebrow">Safety</p><h2>No remote run control</h2></div></div>
            <p>Expedition save state belongs to the player's browser runtime. Admin exposes contract ownership only; it cannot read, clear, overwrite, create, resume, settle, or publish a player's run.</p>
            <p><strong>Campaign fixture frozen:</strong> ${String(expedition.safety.campaignFixtureFrozenInRun)}</p>
            <p><strong>Campaign fixture hash checked:</strong> ${String(expedition.safety.campaignFixtureHashChecked)}</p>
            <p><strong>Admin write:</strong> ${String(expedition.safety.adminWriteCapability)}</p>
            <p><strong>Admin storage mutation:</strong> ${String(expedition.safety.adminStorageMutationCapability)}</p>
          </article>
          <article class="st-admin-card space-admin-card--wide">
            <div class="st-admin-card__header"><div><p class="st-admin-eyebrow">Readable signals</p><h2>Admin-safe runtime metadata</h2></div></div>
            ${chipList(expedition.adminReadableSignals)}
          </article>
          <article class="st-admin-card space-admin-card--wide">
            <div class="st-admin-card__header"><div><p class="st-admin-eyebrow">Boundary</p><h2>No synthetic Expedition backend</h2></div></div>
            <ul>${expedition.unsupportedAdminOperations.map((item) => `<li>${escapeHtml(item)}</li>`).join("")}</ul>
          </article>
        `;
      })
      .catch((error: unknown) => {
        if (generation !== loadGeneration) return;
        setAdminStatus(status, "Expedition runtime contract is unavailable.", "error");
        renderAdminFailureState(content, {
          title: "Expedition unavailable",
          fallbackMessage: "The canonical Expedition contract could not be loaded. Check the local Admin runtime and try again.",
          error,
          onRetry: load,
        });
      });
  };

  load();
  return root;
}
