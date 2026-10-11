import { SpaceTypingAdminApi } from "./api";

const api = new SpaceTypingAdminApi();

type QaContractPayload = {
  contractRevision: string;
  schemaVersion: number;
  capability: "qa.execute";
  route: { id: string; path: string; label: string };
  qa: {
    mode: "runtime-backed-ephemeral-sandbox";
    runtimeSources: string[];
    runtimeOwner: string;
    persistence: {
      session: "isolated-in-memory";
      preset: "test-lab-only-browser-local-storage";
      presetKey: string;
      productionCampaign: "no-write";
    };
    applyBoundary: "new-qa-run";
    sandboxMutationCapability: true;
    presetWriteCapability: true;
    productionPersistenceWriteCapability: false;
    publishCapability: false;
    lifecycleActions: string[];
    inspection: string[];
    currentRuntimeCoverage: {
      weeklyChallenge: { owner: string; mode: "read-only" };
      alternativeModes: { owner: string; modes: string[]; rankedEligible: false };
      historicalAnalytics: { owner: string; scope: "current-local-profile"; crossPlayerSupported: false };
      rankedHistory: {
        owner: string;
        queryServiceAvailable: true;
        productionTransportExposed: false;
        parentAdminQueryBridge: false;
        authenticationRequired: true;
        crossPlayerAuthorizationRequired: true;
      };
      voiceHybrid: { owner: string; hardwareAcceptance: "manual" };
    };
    catalogDomains: string[];
    safety: {
      usesProductionGameRuntime: true;
      isolatedSessionState: true;
      neverAutosavesCampaignProgression: true;
      gameMethodsGuardedByTestLabEnabled: true;
      productionSaveMutation: false;
    };
    unsupportedAdminOperations: string[];
  };
};

type GamesPayload = { games?: Array<{ id?: string; appUrl?: string }> };

function escapeHtml(value: unknown): string {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

async function fetchQaContract(): Promise<QaContractPayload> {
  const response = await fetch("/api/admin/space-typing/qa/contract", {
    cache: "no-store",
    headers: { "x-typing-game-admin-token": api.getToken() },
  });
  if (!response.ok) throw new Error(`QA contract request failed (${response.status})`);
  const payload = (await response.json()) as QaContractPayload;
  if (
    payload.capability !== "qa.execute" ||
    payload.qa?.mode !== "runtime-backed-ephemeral-sandbox" ||
    payload.qa.currentRuntimeCoverage?.rankedHistory?.productionTransportExposed !== false ||
    payload.qa.currentRuntimeCoverage?.rankedHistory?.parentAdminQueryBridge !== false ||
    payload.qa.currentRuntimeCoverage?.voiceHybrid?.hardwareAcceptance !== "manual"
  ) {
    throw new Error("QA contract is not the canonical isolated current-runtime Test Lab contract.");
  }
  return payload;
}

async function resolveSpaceTypingAppUrl(): Promise<string> {
  const response = await fetch("/games.json", { cache: "no-store" });
  if (!response.ok) throw new Error(`Game registry request failed (${response.status})`);
  const payload = (await response.json()) as GamesPayload;
  const appUrl = payload.games?.find((game) => game.id === "space-typing")?.appUrl;
  if (!appUrl) throw new Error("Space Typing appUrl is missing from games.json.");
  return appUrl;
}

function renderList(values: readonly string[]): string {
  return `<ul>${values.map((value) => `<li><code>${escapeHtml(value)}</code></li>`).join("")}</ul>`;
}

export function renderPhaseBQa(): HTMLElement {
  const root = document.createElement("section");
  root.className = "space-admin-page space-admin-page--phase-b";
  root.innerHTML = `
    <header class="space-admin-page__header">
      <div>
        <p class="st-admin-eyebrow">Developer · Production Test Lab</p>
        <h1>QA Sandbox</h1>
        <p>Launch the real Space Typing Test Lab in its own isolated runtime session. Current feature ownership is surfaced here without pretending unexposed Ranked transport or real microphone hardware is already accepted.</p>
      </div>
      <div class="space-admin-page__badges">
        <span class="st-admin-badge">RUNTIME-BACKED · EPHEMERAL</span>
        <span class="st-admin-badge">PRODUCTION SAVE · NO WRITE</span>
        <span class="st-admin-badge">RANKED HISTORY TRANSPORT · CLOSED</span>
        <span class="st-admin-badge">MIC HARDWARE · MANUAL</span>
      </div>
    </header>
    <p class="st-admin-notice" data-qa-status>Loading canonical QA ownership…</p>
    <div class="space-admin-grid" data-qa-content></div>
  `;

  const status = root.querySelector<HTMLElement>("[data-qa-status]");
  const content = root.querySelector<HTMLElement>("[data-qa-content]");
  if (!status || !content) return root;

  void Promise.all([fetchQaContract(), resolveSpaceTypingAppUrl()])
    .then(([contract, appUrl]) => {
      const qa = contract.qa;
      const coverage = qa.currentRuntimeCoverage;
      status.textContent = `${qa.catalogDomains.length} runtime QA domains · current drift coverage declared · isolated session · production persistence closed.`;
      content.innerHTML = `
        <article class="st-admin-card">
          <div class="st-admin-card__header"><div><p class="st-admin-eyebrow">Execute</p><h2>Production Test Lab</h2></div><span class="st-admin-badge">REAL RUNTIME</span></div>
          <p>The child runtime owns the launcher <code>Developer Test Lab</code>. Opening the game hands control to that canonical launcher instead of reimplementing Game logic in Admin.</p>
          <p><strong>Apply boundary:</strong> ${escapeHtml(qa.applyBoundary)}</p>
          <p><strong>Runtime owner:</strong> ${escapeHtml(qa.runtimeOwner)}</p>
          <button type="button" class="st-admin-btn primary" data-qa-launch>Open Space Typing · Developer Test Lab ↗</button>
        </article>
        <article class="st-admin-card">
          <div class="st-admin-card__header"><div><p class="st-admin-eyebrow">Safety</p><h2>Persistence Boundary</h2></div></div>
          <p><strong>Session:</strong> ${escapeHtml(qa.persistence.session)}</p>
          <p><strong>Preset:</strong> ${escapeHtml(qa.persistence.preset)} · <code>${escapeHtml(qa.persistence.presetKey)}</code></p>
          <p><strong>Production Campaign:</strong> ${escapeHtml(qa.persistence.productionCampaign)}</p>
          <p><strong>Production persistence write:</strong> ${String(qa.productionPersistenceWriteCapability)}</p>
          <p><strong>Publish:</strong> ${String(qa.publishCapability)}</p>
        </article>
        <article class="st-admin-card space-admin-card--wide">
          <div class="st-admin-card__header"><div><p class="st-admin-eyebrow">Current runtime</p><h2>Re-audit coverage</h2></div></div>
          <p><strong>Weekly:</strong> ${escapeHtml(coverage.weeklyChallenge.mode)} · <code>${escapeHtml(coverage.weeklyChallenge.owner)}</code></p>
          <p><strong>Alternative Modes:</strong> ${coverage.alternativeModes.modes.map(escapeHtml).join(" · ")} · Ranked eligible ${String(coverage.alternativeModes.rankedEligible)}</p>
          <p><strong>Historical Analytics:</strong> ${escapeHtml(coverage.historicalAnalytics.scope)} · cross-player ${String(coverage.historicalAnalytics.crossPlayerSupported)}</p>
          <p><strong>Ranked History service:</strong> ${String(coverage.rankedHistory.queryServiceAvailable)} · production transport ${String(coverage.rankedHistory.productionTransportExposed)} · Parent query bridge ${String(coverage.rankedHistory.parentAdminQueryBridge)}</p>
          <p><strong>Ranked History auth:</strong> authenticated ${String(coverage.rankedHistory.authenticationRequired)} · cross-player authorization ${String(coverage.rankedHistory.crossPlayerAuthorizationRequired)}</p>
          <p><strong>Voice/Hybrid:</strong> hardware acceptance = ${escapeHtml(coverage.voiceHybrid.hardwareAcceptance)}</p>
          <p class="st-admin-notice">Automated QA may verify software boundaries; Ranked history transport remains closed and microphone/browser/device acceptance remains a manual gate.</p>
        </article>
        <article class="st-admin-card">
          <div class="st-admin-card__header"><div><p class="st-admin-eyebrow">Coverage</p><h2>QA Catalog Domains</h2></div></div>
          <p>${qa.catalogDomains.map((domain) => `<span class="st-admin-chip">${escapeHtml(domain)}</span>`).join(" ")}</p>
          ${renderList(qa.runtimeSources)}
        </article>
        <article class="st-admin-card">
          <div class="st-admin-card__header"><div><p class="st-admin-eyebrow">Closed</p><h2>Unsupported Production Writes</h2></div></div>
          ${renderList(qa.unsupportedAdminOperations)}
        </article>
      `;

      content.querySelector<HTMLButtonElement>("[data-qa-launch]")?.addEventListener("click", () => {
        window.open(appUrl, "_blank", "noopener,noreferrer");
      });
    })
    .catch((error) => {
      status.textContent = error instanceof Error ? error.message : "Unable to load QA Sandbox contract.";
      status.classList.add("st-admin-notice--error");
    });

  return root;
}
