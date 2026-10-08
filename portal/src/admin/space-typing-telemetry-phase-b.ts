import { SpaceTypingAdminApi } from "./api";

const api = new SpaceTypingAdminApi();

type TelemetryContractPayload = {
  contractRevision: string;
  schemaVersion: number;
  capability: "telemetry.read";
  routes: Array<{ id: "overview" | "analytics"; path: string; label: string }>;
  telemetry: {
    mode: "runtime-derived-session-readonly";
    runtimeSources: string[];
    runtimeOwner: string;
    persistence: "session-memory-only";
    applyBoundary: "none";
    writeCapability: false;
    publishCapability: false;
    historicalAggregationCapability: false;
    centralTelemetryBackendCapability: false;
    overviewSignals: string[];
    analyticsSignals: string[];
    performanceDiagnostics: {
      available: boolean;
      scope: string;
      signals: string[];
      adminReadableSnapshot: false;
    };
    privacy: {
      playerIdentityCollectedByContract: false;
      networkTransportOwnedByContract: false;
      crossSessionRetentionOwnedByContract: false;
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
    payload.telemetry?.mode !== "runtime-derived-session-readonly" ||
    payload.telemetry.historicalAggregationCapability !== false ||
    payload.telemetry.centralTelemetryBackendCapability !== false
  ) {
    throw new Error("Telemetry contract does not match the canonical read-only session boundary.");
  }
  return payload;
}

function signalList(signals: string[]): string {
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
          ? "Inspect the canonical per-stage/session telemetry model without fabricating historical or cross-player aggregates."
          : "Inspect the production session signals that can truthfully back an operational overview today."}</p>
      </div>
      <div class="space-admin-page__badges">
        <span class="st-admin-badge">RUNTIME-BACKED · SESSION READ ONLY</span>
        <span class="st-admin-badge">NO HISTORICAL BACKEND</span>
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
      status.textContent = `${signals.length} canonical ${analytics ? "analytics" : "overview"} signals · session-memory only · Admin writes closed.`;
      content.innerHTML = `
        <article class="st-admin-card">
          <div class="st-admin-card__header"><div><p class="st-admin-eyebrow">Canonical</p><h2>Runtime telemetry owner</h2></div></div>
          <p><strong>Owner:</strong> ${escapeHtml(telemetry.runtimeOwner)}</p>
          <p><strong>Persistence:</strong> ${escapeHtml(telemetry.persistence)}</p>
          <p><strong>Apply boundary:</strong> ${escapeHtml(telemetry.applyBoundary)}</p>
          <p><strong>Sources:</strong></p>
          <ul>${telemetry.runtimeSources.map((source) => `<li><code>${escapeHtml(source)}</code></li>`).join("")}</ul>
        </article>
        <article class="st-admin-card">
          <div class="st-admin-card__header"><div><p class="st-admin-eyebrow">Boundary</p><h2>What Admin can truthfully report</h2></div></div>
          <p>The child runtime owns these measurements inside the active stage/session. This Admin adapter exposes their canonical schema and ownership. No live cross-process feed or historical telemetry store exists.</p>
          <p><strong>Write capability:</strong> ${String(telemetry.writeCapability)}</p>
          <p><strong>Publish capability:</strong> ${String(telemetry.publishCapability)}</p>
          <p><strong>Historical aggregation:</strong> ${String(telemetry.historicalAggregationCapability)}</p>
          <p><strong>Central telemetry backend:</strong> ${String(telemetry.centralTelemetryBackendCapability)}</p>
        </article>
        <article class="st-admin-card space-admin-card--wide">
          <div class="st-admin-card__header"><div><p class="st-admin-eyebrow">${analytics ? "Session detail" : "Operational summary"}</p><h2>Canonical signals</h2></div></div>
          ${signalList(signals)}
        </article>
        ${analytics ? `
        <article class="st-admin-card">
          <div class="st-admin-card__header"><div><p class="st-admin-eyebrow">Performance</p><h2>Adaptive render diagnostics</h2></div></div>
          <p><strong>Runtime diagnostics exist:</strong> ${String(telemetry.performanceDiagnostics.available)}</p>
          <p><strong>Scope:</strong> ${escapeHtml(telemetry.performanceDiagnostics.scope)}</p>
          <p><strong>Admin-readable live snapshot:</strong> ${String(telemetry.performanceDiagnostics.adminReadableSnapshot)}</p>
          ${signalList(telemetry.performanceDiagnostics.signals)}
          <p class="st-admin-notice">Internal frame/draw samples remain runtime-private until a real bridge is introduced.</p>
        </article>
        <article class="st-admin-card">
          <div class="st-admin-card__header"><div><p class="st-admin-eyebrow">Unsupported</p><h2>No synthetic analytics</h2></div></div>
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
