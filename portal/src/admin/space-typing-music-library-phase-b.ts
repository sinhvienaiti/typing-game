import { SpaceTypingAdminApi } from "./api";

const api = new SpaceTypingAdminApi();

type CatalogSource = { src: string; codec?: string };
type CatalogPlayback =
  | { kind: "single"; sources: CatalogSource[] }
  | { kind: "stems"; calm: CatalogSource[]; intense: CatalogSource[]; syncGroup: string };
type MusicCatalogTrack = {
  id: string;
  title: string;
  playback: CatalogPlayback;
  durationSeconds: number;
  mixOutSeconds?: number;
  loop?: boolean;
  metadata?: Record<string, unknown>;
  uploadedByAdmin: boolean;
};
type MusicCatalogPayload = {
  schemaVersion: number;
  manifestRevision: string;
  tracks: MusicCatalogTrack[];
};

function escapeHtml(value: unknown): string {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

async function errorMessage(response: Response): Promise<string> {
  const payload = (await response.json().catch(() => ({}))) as Record<string, unknown>;
  return typeof payload.message === "string"
    ? payload.message
    : typeof payload.error === "string"
      ? payload.error
      : `Admin request failed (${response.status})`;
}

async function loadCatalog(): Promise<MusicCatalogPayload> {
  const response = await fetch("/api/admin/space-typing/music/library", {
    cache: "no-store",
    headers: { "x-typing-game-admin-token": api.getToken() },
  });
  if (!response.ok) throw new Error(await errorMessage(response));
  return (await response.json()) as MusicCatalogPayload;
}

async function uploadTrack(input: {
  file: File;
  trackId: string;
  title: string;
  worldId: string;
  durationSeconds: string;
  mixOutSeconds: string;
  mood: string;
}): Promise<MusicCatalogPayload> {
  const headers: Record<string, string> = {
    "x-typing-game-admin-token": api.getToken(),
    "x-music-file-name": input.file.name,
    "x-music-track-id": input.trackId.trim(),
    "x-music-title": input.title.trim(),
    "x-music-world-id": input.worldId,
    "x-music-duration-seconds": input.durationSeconds.trim(),
  };
  if (input.file.type) headers["content-type"] = input.file.type;
  if (input.mixOutSeconds.trim()) headers["x-music-mix-out-seconds"] = input.mixOutSeconds.trim();
  if (input.mood.trim()) headers["x-music-mood"] = input.mood.trim();

  const response = await fetch("/api/admin/space-typing/music/upload", {
    method: "POST",
    headers,
    body: input.file,
  });
  if (!response.ok) throw new Error(await errorMessage(response));
  const payload = (await response.json()) as { catalog: MusicCatalogPayload };
  return payload.catalog;
}

async function deleteTrack(trackId: string): Promise<MusicCatalogPayload> {
  const response = await fetch(`/api/admin/space-typing/music/tracks/${encodeURIComponent(trackId)}`, {
    method: "DELETE",
    headers: { "x-typing-game-admin-token": api.getToken() },
  });
  if (!response.ok) throw new Error(await errorMessage(response));
  return (await response.json()) as MusicCatalogPayload;
}

function playbackSummary(track: MusicCatalogTrack): string {
  if (track.playback.kind === "single") return `single · ${track.playback.sources.length} source${track.playback.sources.length === 1 ? "" : "s"}`;
  return `stems · ${track.playback.calm.length} calm / ${track.playback.intense.length} intense`;
}

export function renderPhaseBMusicLibrary(): HTMLElement {
  const root = document.createElement("section");
  root.className = "space-admin-page space-admin-page--phase-b";
  root.innerHTML = `
    <header class="space-admin-page__header">
      <div>
        <p class="st-admin-eyebrow">Audio · Authored Asset Service · Phase B</p>
        <h1>Music Library</h1>
        <p>Manage authored tracks through the canonical World Music catalog. Upload/delete rebuilds the bundled catalog consumed by the production MusicController.</p>
      </div>
      <div class="space-admin-page__badges">
        <span class="st-admin-badge">RUNTIME CATALOG · CONNECTED</span>
        <span class="st-admin-badge">APPLY · CATALOG REBUILD</span>
        <span class="st-admin-badge">DELETE · ADMIN UPLOADS ONLY</span>
      </div>
    </header>
    <p class="st-admin-notice" data-music-status>Loading canonical World Music catalog…</p>
    <div class="space-admin-grid">
      <article class="st-admin-card space-admin-card--wide">
        <div class="st-admin-card__header"><div><p class="st-admin-eyebrow">Authoring</p><h2>Upload track</h2></div></div>
        <div class="stx-grid">
          <label class="stx-field"><span>Audio file</span><input data-music-file type="file" accept="audio/mpeg,audio/ogg,audio/wav,audio/mp4,.mp3,.ogg,.wav,.m4a"></label>
          <label class="stx-field"><span>Track ID</span><input data-music-id placeholder="lowercase-track-id" maxlength="80"></label>
          <label class="stx-field"><span>Title</span><input data-music-title maxlength="160"></label>
          <label class="stx-field"><span>World</span><select data-music-world>${Array.from({ length: 50 }, (_, i) => `<option value="world-${String(i + 1).padStart(2, "0")}">World ${String(i + 1).padStart(2, "0")}</option>`).join("")}</select></label>
          <label class="stx-field"><span>Duration (seconds)</span><input data-music-duration type="number" min="0.01" step="0.01"></label>
          <label class="stx-field"><span>Mix-out (seconds, optional)</span><input data-music-mixout type="number" min="0.01" step="0.01"></label>
          <label class="stx-field"><span>Mood (optional)</span><input data-music-mood maxlength="80"></label>
        </div>
        <p class="st-admin-notice">Accepted: mp3, ogg, wav, m4a · max 96 MiB. A successful upload writes one authored manifest, rebuilds <code>world-music-catalog.json</code>, and then becomes part of the bundled runtime catalog.</p>
        <button class="st-admin-btn primary" type="button" data-music-upload>Upload & rebuild catalog</button>
      </article>
      <article class="st-admin-card space-admin-card--wide">
        <div class="st-admin-card__header"><div><p class="st-admin-eyebrow">Canonical catalog</p><h2>Tracks</h2></div><strong data-music-revision>—</strong></div>
        <div data-music-list></div>
      </article>
    </div>
  `;

  const status = root.querySelector<HTMLElement>("[data-music-status]");
  const list = root.querySelector<HTMLElement>("[data-music-list]");
  const revision = root.querySelector<HTMLElement>("[data-music-revision]");
  const uploadButton = root.querySelector<HTMLButtonElement>("[data-music-upload]");
  const fileInput = root.querySelector<HTMLInputElement>("[data-music-file]");
  const idInput = root.querySelector<HTMLInputElement>("[data-music-id]");
  const titleInput = root.querySelector<HTMLInputElement>("[data-music-title]");
  const worldInput = root.querySelector<HTMLSelectElement>("[data-music-world]");
  const durationInput = root.querySelector<HTMLInputElement>("[data-music-duration]");
  const mixoutInput = root.querySelector<HTMLInputElement>("[data-music-mixout]");
  const moodInput = root.querySelector<HTMLInputElement>("[data-music-mood]");
  if (!status || !list || !revision || !uploadButton || !fileInput || !idInput || !titleInput || !worldInput || !durationInput || !mixoutInput || !moodInput) return root;

  const render = (catalog: MusicCatalogPayload): void => {
    revision.textContent = `${catalog.tracks.length} tracks · ${catalog.manifestRevision.slice(0, 20)}…`;
    status.textContent = `Catalog schema v${catalog.schemaVersion} loaded. Only tracks with provenance local-admin-upload can be deleted from this surface.`;
    if (catalog.tracks.length === 0) {
      list.innerHTML = '<p class="st-admin-notice">Catalog is empty.</p>';
      return;
    }
    list.innerHTML = `<div class="st-admin-table-wrap"><table class="st-admin-table"><thead><tr><th>ID</th><th>Title</th><th>Playback</th><th>Duration</th><th>Provenance</th><th>Action</th></tr></thead><tbody>${catalog.tracks.map((track) => {
      const provenance = String(track.metadata?.provenance ?? "catalog");
      return `<tr><td><code>${escapeHtml(track.id)}</code></td><td>${escapeHtml(track.title)}</td><td>${escapeHtml(playbackSummary(track))}</td><td>${escapeHtml(track.durationSeconds)}s</td><td>${escapeHtml(provenance)}</td><td>${track.uploadedByAdmin ? `<button type="button" class="st-admin-btn danger" data-delete-track="${escapeHtml(track.id)}">Delete</button>` : '<span class="st-admin-badge">SOURCE-OWNED</span>'}</td></tr>`;
    }).join("")}</tbody></table></div>`;

    for (const button of list.querySelectorAll<HTMLButtonElement>("[data-delete-track]")) {
      button.addEventListener("click", () => {
        const trackId = button.dataset.deleteTrack ?? "";
        if (!trackId || !window.confirm(`Delete Admin-uploaded track ${trackId} and rebuild the catalog?`)) return;
        button.disabled = true;
        status.textContent = `Deleting ${trackId} and rebuilding canonical catalog…`;
        void deleteTrack(trackId)
          .then(render)
          .catch((error) => {
            status.textContent = error instanceof Error ? error.message : "Delete failed.";
            status.classList.add("st-admin-notice--error");
            button.disabled = false;
          });
      });
    }
  };

  uploadButton.addEventListener("click", () => {
    const file = fileInput.files?.[0];
    if (!file) {
      status.textContent = "Choose an audio file first.";
      status.classList.add("st-admin-notice--error");
      return;
    }
    uploadButton.disabled = true;
    status.classList.remove("st-admin-notice--error");
    status.textContent = "Uploading authored track and rebuilding canonical catalog…";
    void uploadTrack({
      file,
      trackId: idInput.value,
      title: titleInput.value,
      worldId: worldInput.value,
      durationSeconds: durationInput.value,
      mixOutSeconds: mixoutInput.value,
      mood: moodInput.value,
    })
      .then((catalog) => {
        fileInput.value = "";
        idInput.value = "";
        titleInput.value = "";
        durationInput.value = "";
        mixoutInput.value = "";
        moodInput.value = "";
        render(catalog);
      })
      .catch((error) => {
        status.textContent = error instanceof Error ? error.message : "Upload failed.";
        status.classList.add("st-admin-notice--error");
      })
      .finally(() => { uploadButton.disabled = false; });
  });

  void loadCatalog().then(render).catch((error) => {
    status.textContent = error instanceof Error ? error.message : "Unable to load music catalog.";
    status.classList.add("st-admin-notice--error");
  });
  return root;
}
