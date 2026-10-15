import { SpaceTypingAdminApi } from "./api";
import { renderAdminFailureState, setAdminStatus } from "./space-typing-admin-state";

const api = new SpaceTypingAdminApi();

type UiAssetSurface = {
  id: string;
  owner: string;
  kind: string;
  examples: string[];
};

type UiAssetsContractPayload = {
  contractRevision: string;
  schemaVersion: number;
  capability: "ui-assets.read";
  route: { id: string; path: string; label: string };
  uiAssets: {
    mode: "runtime-derived-readonly";
    runtimeSources: string[];
    runtimeOwner: string;
    surfaces: UiAssetSurface[];
    assetCatalogOwnership: string;
    dataFlow: string;
    persistenceOwner: string;
    authorableFields: string[];
    writeCapability: false;
    previewWriteCapability: false;
    applyBoundary: "none";
    unsupportedAdminMockFields: string[];
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
function isRecord(value: unknown): value is Record<string, unknown> {
  return value !== null && typeof value === "object" && !Array.isArray(value);
}
function validateUiAssetsContract(value: unknown): UiAssetsContractPayload {
  if (!isRecord(value) || value["capability"] !== "ui-assets.read" || !isRecord(value["route"]) || !isRecord(value["uiAssets"])) {
    throw new Error("UI Assets response does not match the canonical ui-assets.read contract.");
  }
  const ui = value["uiAssets"];
  if (
    ui["mode"] !== "runtime-derived-readonly" ||
    !Array.isArray(ui["runtimeSources"]) ||
    !Array.isArray(ui["surfaces"]) ||
    !Array.isArray(ui["authorableFields"]) ||
    !Array.isArray(ui["unsupportedAdminMockFields"]) ||
    typeof ui["runtimeOwner"] !== "string" ||
    typeof ui["assetCatalogOwnership"] !== "string" ||
    typeof ui["dataFlow"] !== "string" ||
    typeof ui["persistenceOwner"] !== "string" ||
    ui["applyBoundary"] !== "none"
  ) {
    throw new Error("UI Assets response is missing required runtime ownership metadata.");
  }
  for (const surface of ui["surfaces"]) {
    if (!isRecord(surface) || typeof surface["id"] !== "string" || typeof surface["owner"] !== "string" || typeof surface["kind"] !== "string" || !Array.isArray(surface["examples"])) {
      throw new Error("UI Assets response contains an invalid runtime presentation surface.");
    }
  }
  return value as unknown as UiAssetsContractPayload;
}
async function fetchUiAssetsContract(): Promise<UiAssetsContractPayload> {
  return validateUiAssetsContract(await api.requestJson<unknown>("/api/admin/space-typing/ui-assets/contract"));
}

function renderSurface(surface: UiAssetSurface): string {
  return `
    <article class="st-admin-card">
      <div class="st-admin-card__header">
        <div>
          <p class="st-admin-eyebrow">${escapeHtml(surface.kind)}</p>
          <h3>${escapeHtml(surface.id)}</h3>
        </div>
        <span class="st-admin-badge">RUNTIME</span>
      </div>
      <p><strong>Owner:</strong> ${escapeHtml(surface.owner)}</p>
      <div class="st-admin-chip-list">${surface.examples.map((item) => `<span class="st-admin-chip">${escapeHtml(item)}</span>`).join("")}</div>
    </article>`;
}

export function renderPhaseBUiAssets(): HTMLElement {
  const root = document.createElement("section");
  root.className = "space-admin-page space-admin-page--phase-b";
  root.innerHTML = `
    <header class="space-admin-page__header">
      <div>
        <p class="st-admin-eyebrow">Visuals · Runtime UI Ownership</p>
        <h1>UI Assets</h1>
        <p>Inspect production HUD, shared components, Duel and Ranked presentation ownership without inventing an Admin persistence layer.</p>
      </div>
      <div class="space-admin-page__badges">
        <span class="st-admin-badge">RUNTIME-BACKED · READ ONLY</span>
        <span class="st-admin-badge">NO FAKE UI ASSET CRUD</span>
      </div>
    </header>
    <p class="st-admin-notice" data-ui-assets-status aria-live="polite">Loading canonical runtime ownership…</p>
    <div class="space-admin-grid" data-ui-assets-content></div>
  `;

  const status = root.querySelector<HTMLElement>("[data-ui-assets-status]");
  const content = root.querySelector<HTMLElement>("[data-ui-assets-content]");
  if (!status || !content) return root;

  let loadGeneration = 0;
  const load = (): void => {
    const generation = ++loadGeneration;
    setAdminStatus(status, "Loading canonical UI Assets runtime ownership…", "loading");
    content.innerHTML = `<article class="st-admin-card space-admin-card--wide"><p class="st-admin-notice">Loading production presentation surfaces…</p></article>`;

    void fetchUiAssetsContract().then((contract) => {
      if (generation !== loadGeneration) return;
      const ui = contract.uiAssets;
      setAdminStatus(status, `${ui.surfaces.length} runtime presentation surfaces · Admin writes closed.`, "success");
      content.innerHTML = `
        <article class="st-admin-card">
          <div class="st-admin-card__header"><div><p class="st-admin-eyebrow">Canonical</p><h2>Runtime Ownership</h2></div></div>
          <p><strong>Owner:</strong> ${escapeHtml(ui.runtimeOwner)}</p>
          <p><strong>Data flow:</strong> ${escapeHtml(ui.dataFlow)}</p>
          <p><strong>Asset catalog:</strong> ${escapeHtml(ui.assetCatalogOwnership)}</p>
          <p><strong>Sources:</strong></p>
          <ul>${ui.runtimeSources.map((source) => `<li><code>${escapeHtml(source)}</code></li>`).join("")}</ul>
        </article>
        <article class="st-admin-card">
          <div class="st-admin-card__header"><div><p class="st-admin-eyebrow">Boundary</p><h2>Admin Boundary</h2></div></div>
          <p><strong>Persistence owner:</strong> ${escapeHtml(ui.persistenceOwner)}</p>
          <p><strong>Apply boundary:</strong> ${escapeHtml(ui.applyBoundary)}</p>
          <p><strong>Write capability:</strong> ${String(ui.writeCapability)}</p>
          <p><strong>Preview write capability:</strong> ${String(ui.previewWriteCapability)}</p>
          <p><strong>Authorable fields:</strong> ${ui.authorableFields.length === 0 ? "none" : escapeHtml(ui.authorableFields.join(", "))}</p>
          <p class="st-admin-notice">Editor controls remain locked until the runtime exposes a real consumer and apply boundary.</p>
          <p><strong>Unsupported mock controls:</strong></p>
          <ul>${ui.unsupportedAdminMockFields.map((field) => `<li>${escapeHtml(field)}</li>`).join("")}</ul>
        </article>
        ${ui.surfaces.length > 0 ? ui.surfaces.map(renderSurface).join("") : `<article class="st-admin-card space-admin-card--wide"><p class="st-admin-notice">No runtime presentation surfaces were exposed by the canonical contract.</p></article>`}
      `;
    }).catch((error: unknown) => {
      if (generation !== loadGeneration) return;
      setAdminStatus(status, "UI Assets service unavailable.", "error");
      renderAdminFailureState(content, {
        title: "UI Assets unavailable",
        fallbackMessage: "Unable to load the canonical UI Assets runtime contract.",
        error,
        onRetry: load,
      });
    });
  };

  load();
  return root;
}
