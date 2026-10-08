import { SpaceTypingAdminApi } from "./api";

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

async function fetchUiAssetsContract(): Promise<UiAssetsContractPayload> {
  const response = await fetch("/api/admin/space-typing/ui-assets/contract", {
    cache: "no-store",
    headers: { "x-typing-game-admin-token": api.getToken() },
  });
  if (!response.ok) throw new Error(`UI Assets contract request failed (${response.status})`);
  const payload = (await response.json()) as UiAssetsContractPayload;
  if (payload.capability !== "ui-assets.read" || payload.uiAssets?.mode !== "runtime-derived-readonly") {
    throw new Error("UI Assets contract is not the canonical read-only runtime contract.");
  }
  return payload;
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
      <p>${surface.examples.map((item) => `<span class="st-admin-chip">${escapeHtml(item)}</span>`).join(" ")}</p>
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
        <p>Inspect the production HUD, shared components, Duel and Ranked presentation ownership without inventing an admin persistence layer.</p>
      </div>
      <div class="space-admin-page__badges">
        <span class="st-admin-badge">RUNTIME-BACKED · READ ONLY</span>
        <span class="st-admin-badge">NO FAKE UI ASSET CRUD</span>
      </div>
    </header>
    <p class="st-admin-notice" data-ui-assets-status>Loading canonical runtime ownership…</p>
    <div class="space-admin-grid" data-ui-assets-content></div>
  `;

  const status = root.querySelector<HTMLElement>("[data-ui-assets-status]");
  const content = root.querySelector<HTMLElement>("[data-ui-assets-content]");
  if (!status || !content) return root;

  void fetchUiAssetsContract()
    .then((contract) => {
      const ui = contract.uiAssets;
      status.textContent = `${ui.surfaces.length} runtime presentation surfaces · Admin writes closed.`;
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
        ${ui.surfaces.map(renderSurface).join("")}
      `;
    })
    .catch((error) => {
      status.textContent = error instanceof Error ? error.message : "Unable to load UI Assets contract.";
      status.classList.add("st-admin-notice--error");
    });

  return root;
}
