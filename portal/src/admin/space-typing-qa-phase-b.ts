import { SpaceTypingAdminApi } from "./api";
import { renderAdminFailureState, setAdminStatus } from "./space-typing-admin-state";

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
type GamesPayload = { games: Array<{ id: string; appUrl: string }> };

function escapeHtml(value: unknown): string {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}
function isRecord(value: unknown): value is Record<string, unknown> {
  return value !== null && typeof value === "object" && !Array.isArray(value);
}
function stringArray(value: unknown): value is string[] {
  return Array.isArray(value) && value.every((entry) => typeof entry === "string");
}
function validateQaContract(value: unknown): QaContractPayload {
  if (!isRecord(value) || value["capability"] !== "qa.execute" || !isRecord(value["route"]) || !isRecord(value["qa"])) {
    throw new Error("QA response does not match the canonical qa.execute contract.");
  }
  const qa = value["qa"];
  if (
    qa["mode"] !== "runtime-backed-ephemeral-sandbox" ||
    typeof qa["runtimeOwner"] !== "string" ||
    !stringArray(qa["runtimeSources"]) ||
    !isRecord(qa["persistence"]) ||
    qa["applyBoundary"] !== "new-qa-run" ||
    qa["sandboxMutationCapability"] !== true ||
    qa["presetWriteCapability"] !== true ||
    qa["productionPersistenceWriteCapability"] !== false ||
    qa["publishCapability"] !== false ||
    !stringArray(qa["lifecycleActions"]) ||
    !stringArray(qa["inspection"]) ||
    !stringArray(qa["catalogDomains"]) ||
    !isRecord(qa["safety"]) ||
    !stringArray(qa["unsupportedAdminOperations"])
  ) {
    throw new Error("QA response is missing required isolated Test Lab ownership data.");
  }
  const persistence = qa["persistence"];
  const safety = qa["safety"];
  if (
    persistence["session"] !== "isolated-in-memory" ||
    persistence["preset"] !== "test-lab-only-browser-local-storage" ||
    typeof persistence["presetKey"] !== "string" ||
    persistence["productionCampaign"] !== "no-write" ||
    safety["usesProductionGameRuntime"] !== true ||
    safety["isolatedSessionState"] !== true ||
    safety["neverAutosavesCampaignProgression"] !== true ||
    safety["gameMethodsGuardedByTestLabEnabled"] !== true ||
    safety["productionSaveMutation"] !== false
  ) {
    throw new Error("QA response violates the production-save isolation contract.");
  }
  return value as unknown as QaContractPayload;
}
function validateGamesPayload(value: unknown): GamesPayload {
  if (!isRecord(value) || !Array.isArray(value["games"])) throw new Error("Game registry response is missing games[].");
  for (const game of value["games"]) {
    if (!isRecord(game) || typeof game["id"] !== "string" || typeof game["appUrl"] !== "string") {
      throw new Error("Game registry contains an invalid game entry.");
    }
  }
  return value as unknown as GamesPayload;
}
async function fetchQaContract(): Promise<QaContractPayload> {
  return validateQaContract(await api.requestJson<unknown>("/api/admin/space-typing/qa/contract"));
}
async function resolveSpaceTypingAppUrl(): Promise<string> {
  const payload = validateGamesPayload(await api.requestJson<unknown>("/games.json"));
  const appUrl = payload.games.find((game) => game.id === "space-typing")?.appUrl?.trim();
  if (!appUrl) throw new Error("Space Typing appUrl is missing from the canonical game registry.");
  return appUrl;
}
function directTestLabUrl(appUrl: string): string {
  const url = new URL(appUrl, window.location.href);
  url.searchParams.set("testLab", "1");
  return url.toString();
}
function renderList(values: readonly string[]): string {
  if (values.length === 0) return `<p class="st-admin-notice">None exposed by the canonical contract.</p>`;
  return `<ul>${values.map((value) => `<li><code>${escapeHtml(value)}</code></li>`).join("")}</ul>`;
}

export function renderPhaseBQa(): HTMLElement {
  const root = document.createElement("section");
  root.className = "space-admin-page space-admin-page--phase-b";
  root.innerHTML = `
    <header class="space-admin-page__header">
      <div>
        <p class="st-admin-eyebrow">Developer · QA Sandbox</p>
        <h1>Test Lab Launcher</h1>
        <p>Launch the full Space Typing Developer Test Lab directly in its own isolated runtime session. Admin only opens the canonical child Test Lab; sandbox mutations never publish or autosave Campaign progression.</p>
      </div>
      <div class="space-admin-page__badges">
        <span class="st-admin-badge">RUNTIME-BACKED · EPHEMERAL</span>
        <span class="st-admin-badge">PRODUCTION SAVE · NO WRITE</span>
      </div>
    </header>
    <p class="st-admin-notice" data-qa-status aria-live="polite">Loading canonical QA ownership…</p>
    <div data-qa-failure></div>
    <div class="space-admin-grid" data-qa-content></div>
  `;

  const status = root.querySelector<HTMLElement>("[data-qa-status]");
  const failure = root.querySelector<HTMLElement>("[data-qa-failure]");
  const content = root.querySelector<HTMLElement>("[data-qa-content]");
  if (!status || !failure || !content) return root;

  let loadGeneration = 0;
  const load = (): void => {
    const generation = ++loadGeneration;
    failure.replaceChildren();
    content.replaceChildren();
    setAdminStatus(status, "Loading canonical QA ownership and direct Test Lab launcher…", "loading");

    void Promise.all([fetchQaContract(), resolveSpaceTypingAppUrl()]).then(([contract, appUrl]) => {
      if (generation !== loadGeneration) return;
      const qa = contract.qa;
      setAdminStatus(status, `${qa.catalogDomains.length} runtime QA domains · isolated session · production persistence closed.`, "success");
      content.innerHTML = `
        <article class="st-admin-card">
          <div class="st-admin-card__header">
            <div><p class="st-admin-eyebrow">Execute</p><h2>Full Developer Test Lab</h2></div>
            <span class="st-admin-badge">REAL RUNTIME</span>
          </div>
          <p>The child runtime owns the canonical <code>Developer Test Lab</code>. Admin opens that full Test Lab directly instead of reimplementing Game logic or requiring a second launcher click.</p>
          <p><strong>Apply boundary:</strong> ${escapeHtml(qa.applyBoundary)}</p>
          <p><strong>Runtime owner:</strong> ${escapeHtml(qa.runtimeOwner)}</p>
          <button type="button" class="st-admin-btn primary" data-qa-launch>Open Full Developer Test Lab ↗</button>
          <p class="st-admin-notice">The new game window opens directly into the built-in <strong>Developer Test Lab</strong>. Start/Restart, Pause/Resume and Reset Arena still operate only on the isolated Test Lab session.</p>
        </article>
        <article class="st-admin-card">
          <div class="st-admin-card__header"><div><p class="st-admin-eyebrow">Safety</p><h2>Persistence Boundary</h2></div></div>
          <p><strong>Session:</strong> ${escapeHtml(qa.persistence.session)}</p>
          <p><strong>Preset:</strong> ${escapeHtml(qa.persistence.preset)} · <code>${escapeHtml(qa.persistence.presetKey)}</code></p>
          <p><strong>Production Campaign:</strong> ${escapeHtml(qa.persistence.productionCampaign)}</p>
          <p><strong>Sandbox mutation:</strong> ${String(qa.sandboxMutationCapability)}</p>
          <p><strong>Production persistence write:</strong> ${String(qa.productionPersistenceWriteCapability)}</p>
          <p><strong>Publish:</strong> ${String(qa.publishCapability)}</p>
          <p class="st-admin-notice">NO FAKE QA CRUD · NO CAMPAIGN SAVE BRIDGE</p>
        </article>
        <article class="st-admin-card">
          <div class="st-admin-card__header"><div><p class="st-admin-eyebrow">Lifecycle</p><h2>Executable Actions</h2></div></div>
          ${renderList(qa.lifecycleActions)}
          <p><strong>Inspection:</strong></p>
          ${renderList(qa.inspection)}
        </article>
        <article class="st-admin-card">
          <div class="st-admin-card__header"><div><p class="st-admin-eyebrow">Coverage</p><h2>QA Catalog Domains</h2></div></div>
          <p>${qa.catalogDomains.map((domain) => `<span class="st-admin-chip">${escapeHtml(domain)}</span>`).join(" ") || "No domains exposed."}</p>
          <p><strong>Canonical sources:</strong></p>
          ${renderList(qa.runtimeSources)}
        </article>
        <article class="st-admin-card">
          <div class="st-admin-card__header"><div><p class="st-admin-eyebrow">Closed</p><h2>Unsupported Production Writes</h2></div></div>
          ${renderList(qa.unsupportedAdminOperations)}
        </article>
      `;

      const launch = content.querySelector<HTMLButtonElement>("[data-qa-launch]");
      launch?.addEventListener("click", () => window.open(directTestLabUrl(appUrl), "_blank", "noopener,noreferrer"));
    }).catch((error: unknown) => {
      if (generation !== loadGeneration) return;
      content.replaceChildren();
      setAdminStatus(status, "QA Sandbox unavailable. Test Lab launch is disabled.", "error");
      renderAdminFailureState(failure, {
        title: "QA Sandbox unavailable",
        fallbackMessage: "Unable to validate the isolated qa.execute contract and Space Typing launcher. No Test Lab action is available until Retry succeeds.",
        error,
        onRetry: load,
      });
    });
  };

  load();
  return root;
}
