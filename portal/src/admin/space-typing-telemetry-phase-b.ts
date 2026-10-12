import { SpaceTypingAdminApi } from "./api";
import { requestAdminJson } from "./admin-http";
import { renderAdminFailureState, setAdminStatus } from "./space-typing-admin-state";

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
      persistenceOwner: "ExpansionV2Profile.history";
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
      crossSessionRetentionScope: "browser-local-current-profile-only";
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
  const payload = await requestAdminJson<TelemetryContractPayload>(
    "/api/admin/space-typing/telemetry/contract",
    { token: api.getToken() },
  );
  if (
    payload.capability !== "telemetry.read" ||
    payload.telemetry?.mode !== "runtime-derived-readonly" ||
    payload.telemetry.historicalAggregationCapability !== true ||
    payload.telemetry.historical?.mode !== "local-profile-persisted-readonly" ||
    payload.telemetry.historical.crossPlayerSupported !== false ||
    payload.telemetry.centralTelemetryBackendCapability !== false
  ) {
    throw new Error("Telemetry contract does not match the canonical session + local-profile read-only boundary.");
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
          ? "Inspect canonical session telemetry plus persisted historical aggregates for the current local profile without fabricating cross-player data."
          : "Inspect production session signals and the local-profile historical ownership that can truthfully back an operational overview today."}</p>
      </div>
      <div class="space-admin-page__badges">
        <span class="st-admin-badge">RUNTIME-BACKED · READ ONLY</span>
        <span class="st-admin-badge">LOCAL PROFILE HISTORY</span>
        <span class="st-admin-badge">NO CENTRAL BACKEND</span>
      </div>
    </header>
    <p class="st-admin-notice" data-telemetry-status aria-live="polite">Loading canonical telemetry ownership…</p>
    <div class="space-admin-grid" data-telemetry-content></div>
  `;

  const status = root.querySelector<HTMLElement>("[data-telemetry-status]");
  const content = root.querySelector<HTMLElement>("[data-telemetry-content]");
  if (!status || !content) return root;

  let requestGeneration = 0;

  const load = (): void => {
    const generation = ++requestGeneration;
    setAdminStatus(status, "Loading canonical telemetry ownership…", "loading");
    content.replaceChildren();

    void fetchTelemetryContract()
      .then((contract) => {
        if (generation !== requestGeneration) return;
        const telemetry = contract.telemetry;
        const signals = analytics ? telemetry.analyticsSignals : telemetry.overviewSignals;
        setAdminStatus(
          status,
          `${signals.length} canonical ${analytics ? "analytics" : "overview"} signals · local-profile history ${telemetry.historical.available ? "available" : "unavailable"} · Admin writes closed.`,
          "success",
        );
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
            <p>The child runtime owns live stage/session measurements and persisted history for the current browser-local profile. There is no central or cross-player telemetry backend and no Admin mutation path.</p>
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
            <div class="st-admin-card__header"><div><p class="st-admin-eyebrow">Historical</p><h2>Local-profile persisted analytics</h2></div></div>
            <p><strong>Available:</strong> ${String(telemetry.historical.available)}</p>
            <p><strong>Mode:</strong> ${escapeHtml(telemetry.historical.mode)}</p>
            <p><strong>Owner:</strong> ${escapeHtml(telemetry.historical.persistenceOwner)}</p>
            <p><strong>Scope:</strong> ${escapeHtml(telemetry.historical.scope)}</p>
            <p><strong>Cross-player supported:</strong> ${String(telemetry.historical.crossPlayerSupported)}</p>
            <p><strong>Live fallback when empty:</strong> ${String(telemetry.historical.liveTelemetryFallbackWhenEmpty)}</p>
            <p class="st-admin-notice">Historical rows come only from persisted ExpansionV2Profile history; empty history is not backfilled from live telemetry.</p>
          </article>
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
        if (generation !== requestGeneration) return;
        setAdminStatus(status, "Telemetry data is unavailable.", "error");
        renderAdminFailureState(content, {
          title: `${analytics ? "Analytics" : "Overview"} data unavailable`,
          fallbackMessage: "The telemetry contract could not be verified. Check the local Admin runtime and try again.",
          error,
          onRetry: load,
        });
      });
  };

  load();
  return root;
}
