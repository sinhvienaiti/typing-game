import { SpaceTypingAdminApi } from "./api";

const api = new SpaceTypingAdminApi();

type TelemetryContractPayload = {
  contractRevision: string;
  schemaVersion: number;
  capability: "telemetry.read";
  routes: Array<{ id: "overview" | "analytics"; path: string; label: string }>;
  telemetry: {
    mode: "runtime-derived-readonly";
    runtimeSources: string[];
    runtimeOwner: string;
    persistence: "session-memory-plus-local-profile-history";
    applyBoundary: "none";
    writeCapability: false;
    publishCapability: false;
    historicalAggregationCapability: true;
    centralTelemetryBackendCapability: false;
    overviewSignals: string[];
    analyticsSignals: string[];
    performanceDiagnostics: {
      available: boolean;
      scope: string;
      signals: string[];
      adminReadableSnapshot: false;
    };
    historical: {
      available: true;
      mode: "local-profile-persisted-readonly";
      persistenceOwner: string;
      scope: "current-local-profile";
      crossPlayerSupported: false;
      centralTelemetryBackendCapability: false;
      writeCapability: false;
      liveTelemetryFallbackWhenEmpty: false;
    };
    privacy: {
      playerIdentityCollectedByContract: false;
      networkTransportOwnedByContract: false;
      crossSessionRetentionOwnedByContract: true;
      crossSessionRetentionScope: string;
      crossPlayerAggregation: false;
    };
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

async function fetchTelemetryContract(): Promise<TelemetryContractPayload> {
  const response = await fetch("/api/admin/space-typing/telemetry/contract", {
    cache: "no-store",
    headers: { "x-typing-game-admin-token": api.getToken() },
  });
  if (!response.ok) throw new Error(`Telemetry contract request failed (${response.status})`);
  const payload = (await response.json()) as TelemetryContractPayload;
  if (
    payload.capability !== "telemetry.read" ||
    payload.telemetry?.mode !== "runtime-derived-readonly" ||
    payload.telemetry.historicalAggregationCapability !== true ||
    payload.telemetry.historical?.scope !== "current-local-profile" ||
    payload.telemetry.historical?.crossPlayerSupported !== false ||
    payload.telemetry.centralTelemetryBackendCapability !== false
  ) {
    throw new Error("Telemetry contract does not match the canonical live + local-profile historical read-only boundary.");
  }
  return payload;
}

function signalList(signals: readonly string[]): string {
  return `<div class="st-admin-chip-list">${signals
    .map((signal) => `<span class="st-admin-chip">${escapeHtml(signal)}</span>`)
    .join("")}</div>`;
}

export function renderPhaseBTelemetry(path: string): HTMLElement {
  const analytics = path.endsWith("/analytics");
  const root = document.createElement("section");
  root.className = "space-admin-page space-admin-page--phase-b";
  root.innerHTML = `
    <header class="space-admin-page__header">
      <div>
        <p class="st-admin-eyebrow">Telemetry · Production Runtime Ownership</p>
        <h1>${analytics ? "Analytics" : "Overview"}</h1>
        <p>${analytics
          ? "Inspect canonical live session metrics plus the persisted historical analytics capability for the current local profile. Cross-player/global analytics remain unsupported."
          : "Inspect production session signals and the truthful scope of persisted local-profile historical data."}</p>
      </div>
      <div class="space-admin-page__badges">
        <span class="st-admin-badge">RUNTIME-BACKED · READ ONLY</span>
        <span class="st-admin-badge">HISTORY · LOCAL PROFILE ONLY</span>
        <span class="st-admin-badge">CROSS-PLAYER · UNSUPPORTED</span>
      </div>
    </header>
    <p class="st-admin-notice" data-telemetry-status>Loading canonical telemetry ownership…</p>
    <div class="space-admin-grid" data-telemetry-content></div>
  `;

  const status = root.querySelector<HTMLElement>("[data-telemetry-status]");
  const content = root.querySelector<HTMLElement>("[data-telemetry-content]");
  if (!status || !content) return root;

  void fetchTelemetryContract()
    .then((contract) => {
      const telemetry = contract.telemetry;
      const signals = analytics ? telemetry.analyticsSignals : telemetry.overviewSignals;
      status.textContent = `${signals.length} canonical ${analytics ? "analytics" : "overview"} live signals · persisted history scope ${telemetry.historical.scope} · Admin writes closed.`;
      content.innerHTML = `
        <article class="st-admin-card">
          <div class="st-admin-card__header"><div><p class="st-admin-eyebrow">Canonical</p><h2>Runtime telemetry owner</h2></div></div>
          <p><strong>Owner:</strong> ${escapeHtml(telemetry.runtimeOwner)}</p>
          <p><strong>Persistence:</strong> ${escapeHtml(telemetry.persistence)}</p>
          <p><strong>Apply boundary:</strong> ${escapeHtml(telemetry.applyBoundary)}</p>
          <p><strong>Write capability:</strong> ${String(telemetry.writeCapability)}</p>
          <p><strong>Publish capability:</strong> ${String(telemetry.publishCapability)}</p>
        </article>
        <article class="st-admin-card">
          <div class="st-admin-card__header"><div><p class="st-admin-eyebrow">Historical</p><h2>Current local profile only</h2></div></div>
          <p><strong>Available:</strong> ${String(telemetry.historical.available)}</p>
          <p><strong>Owner:</strong> ${escapeHtml(telemetry.historical.persistenceOwner)}</p>
          <p><strong>Scope:</strong> ${escapeHtml(telemetry.historical.scope)}</p>
          <p><strong>Cross-player:</strong> ${String(telemetry.historical.crossPlayerSupported)}</p>
          <p><strong>Central backend:</strong> ${String(telemetry.historical.centralTelemetryBackendCapability)}</p>
          <p class="st-admin-notice">The Admin contract reports capability and scope; it does not fabricate browser-local history into a remote/global dashboard.</p>
        </article>
        <article class="st-admin-card space-admin-card--wide">
          <div class="st-admin-card__header"><div><p class="st-admin-eyebrow">${analytics ? "Session detail" : "Operational summary"}</p><h2>Canonical live signals</h2></div></div>
          ${signalList(signals)}
        </article>
        ${analytics ? `
        <article class="st-admin-card">
          <div class="st-admin-card__header"><div><p class="st-admin-eyebrow">Performance</p><h2>Adaptive render diagnostics</h2></div></div>
          <p><strong>Runtime diagnostics exist:</strong> ${String(telemetry.performanceDiagnostics.available)}</p>
          <p><strong>Scope:</strong> ${escapeHtml(telemetry.performanceDiagnostics.scope)}</p>
          <p><strong>Admin-readable live snapshot:</strong> ${String(telemetry.performanceDiagnostics.adminReadableSnapshot)}</p>
          ${signalList(telemetry.performanceDiagnostics.signals)}
        </article>
        <article class="st-admin-card">
          <div class="st-admin-card__header"><div><p class="st-admin-eyebrow">Fail closed</p><h2>No synthetic global analytics</h2></div></div>
          <ul>${telemetry.unsupportedAdminOperations.map((item) => `<li>${escapeHtml(item)}</li>`).join("")}</ul>
        </article>` : ""}
      `;
    })
    .catch((error) => {
      status.textContent = error instanceof Error ? error.message : "Unable to load telemetry contract.";
      status.classList.add("st-admin-notice--error");
    });

  return root;
}
