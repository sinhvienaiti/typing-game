import {
  createAdminSfxCatalog,
  type AdminSfxCatalogEntry,
} from "../../../games/space-typing/src/audio/admin-sfx-catalog";
import { SpaceTypingAdminApi } from "./api";
import { renderAdminFailureState, setAdminStatus } from "./space-typing-admin-state";

const api = new SpaceTypingAdminApi();
type GamesPayload = { games: Array<{ id: string; appUrl: string }> };

function el<K extends keyof HTMLElementTagNameMap>(tag: K, cls?: string, text?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (cls) node.className = cls;
  if (text !== undefined) node.textContent = text;
  return node;
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return value !== null && typeof value === "object" && !Array.isArray(value);
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

async function resolveSpaceTypingAppUrl(): Promise<string> {
  const payload = validateGamesPayload(await api.requestJson<unknown>("/games.json"));
  const appUrl = payload.games.find((game) => game.id === "space-typing")?.appUrl?.trim();
  if (!appUrl) throw new Error("Space Typing appUrl is missing from the canonical game registry.");
  return appUrl;
}

function productionSampleUrl(appUrl: string, source: string): string {
  if (!source.startsWith("/assets/audio/") || source.includes("..")) {
    throw new Error(`Refusing non-production SFX path: ${source}`);
  }
  return new URL(source, appUrl).toString();
}

function formatGain(value: number): string {
  return Number.isInteger(value) ? String(value) : value.toFixed(2).replace(/0+$/, "").replace(/\.$/, "");
}

export function renderPhaseBSfx(): HTMLElement {
  const page = el("section", "space-admin-page space-admin-page--phase-b");
  const header = el("header", "space-admin-page__header");
  const copy = el("div");
  copy.append(
    el("p", "st-admin-eyebrow", "Media · Production Sample SFX"),
    el("h1", undefined, "SFX"),
    el("p", undefined, "Inspect every sample-backed sound effect used by the production runtime and test the exact committed asset. Runtime gain and pool values are visible for diagnosis; authoring stays closed until the child owns a publishable SFX policy."),
  );
  const badges = el("div", "space-admin-page__badges");
  badges.append(
    el("span", "st-admin-badge", "RUNTIME-BACKED · READ ONLY"),
    el("span", "st-admin-badge", "TEST PLAYBACK"),
    el("span", "st-admin-badge", "NO FAKE SFX POLICY"),
  );
  header.append(copy, badges);

  const status = el("p", "st-admin-notice", "Loading canonical SAMPLE_SFX catalog…");
  status.setAttribute("aria-live", "polite");
  const failure = el("div");
  const toolbar = el("div", "st-admin-toolbar");
  const search = el("input", "st-admin-input") as HTMLInputElement;
  search.type = "search";
  search.placeholder = "Filter by ID, group or asset path…";
  search.setAttribute("aria-label", "Filter production SFX catalog");
  toolbar.append(search);
  const content = el("div");
  page.append(header, status, failure, toolbar, content);

  let activeAudio: HTMLAudioElement | null = null;
  let activeButton: HTMLButtonElement | null = null;

  const stopPlayback = (): void => {
    if (activeAudio) {
      activeAudio.pause();
      activeAudio.currentTime = 0;
      activeAudio = null;
    }
    if (activeButton) {
      activeButton.textContent = "Test Playback";
      activeButton = null;
    }
  };

  const renderRows = (entries: readonly AdminSfxCatalogEntry[], appUrl: string): void => {
    const query = search.value.trim().toLowerCase();
    const visible = entries.filter((entry) => `${entry.id} ${entry.eventBinding} ${entry.group} ${entry.source}`.toLowerCase().includes(query));
    const panel = el("section", "st-admin-panel solid stx-panel");
    const panelHead = el("div", "st-admin-panel-head");
    const panelCopy = el("div");
    panelCopy.append(
      el("h2", undefined, "Production SFX Catalog"),
      el("p", undefined, `${visible.length} of ${entries.length} sample-backed runtime events`),
    );
    panelHead.append(panelCopy);
    panel.append(panelHead);

    if (visible.length === 0) {
      panel.append(el("p", "st-admin-notice", "No production SFX matches this filter."));
      content.replaceChildren(panel);
      return;
    }

    const wrap = el("div", "st-admin-table-wrap");
    const table = el("table", "st-admin-table");
    const thead = el("thead");
    const headRow = el("tr");
    for (const label of ["SFX ID", "Event", "Group", "Source", "Runtime Gain", "Pool", "Preview"]) {
      headRow.append(el("th", undefined, label));
    }
    thead.append(headRow);
    const tbody = el("tbody");

    for (const entry of visible) {
      const row = el("tr");
      const id = el("td");
      const idCode = el("code", undefined, entry.id);
      idCode.title = "Canonical SampleSfxId owned by src/audio/sample-bank.ts";
      id.append(idCode);
      const event = el("td");
      event.append(el("code", undefined, entry.eventBinding));
      const group = el("td", undefined, entry.group);
      group.title = "Production mix group used by SampleSfxBank";
      const source = el("td");
      const sourceCode = el("code", undefined, entry.source);
      sourceCode.title = "Committed production audio asset path";
      source.append(sourceCode);
      const gain = el("td", undefined, formatGain(entry.runtimeGain));
      gain.title = "Code-owned SAMPLE_SFX gain; visible only, not authorable";
      const pool = el("td", undefined, String(entry.poolSize));
      pool.title = "Production HTMLAudioElement pool size";
      const preview = el("td");
      const play = el("button", "st-admin-btn", "Test Playback") as HTMLButtonElement;
      play.type = "button";
      play.title = "Play the exact production sample asset in this browser; does not mutate game or Admin state";
      play.addEventListener("click", () => {
        if (activeButton === play) {
          stopPlayback();
          return;
        }
        stopPlayback();
        try {
          const audio = new Audio(productionSampleUrl(appUrl, entry.preview.source));
          audio.preload = "auto";
          audio.volume = Math.max(0, Math.min(1, entry.runtimeGain));
          activeAudio = audio;
          activeButton = play;
          play.textContent = "Stop";
          const finish = (): void => {
            if (activeAudio === audio) stopPlayback();
          };
          audio.addEventListener("ended", finish, { once: true });
          audio.addEventListener("error", finish, { once: true });
          void audio.play().catch(() => finish());
        } catch {
          stopPlayback();
        }
      });
      preview.append(play);
      row.append(id, event, group, source, gain, pool, preview);
      tbody.append(row);
    }

    table.append(thead, tbody);
    wrap.append(table);
    panel.append(wrap);
    content.replaceChildren(panel);
  };

  const load = (): void => {
    stopPlayback();
    failure.replaceChildren();
    content.replaceChildren();
    setAdminStatus(status, "Loading canonical SAMPLE_SFX catalog and game origin…", "loading");
    void resolveSpaceTypingAppUrl().then((appUrl) => {
      const catalog = createAdminSfxCatalog();
      setAdminStatus(status, `${catalog.entries.length} production sample events · browser-local Test Playback · Admin writes closed.`, "success");
      renderRows(catalog.entries, appUrl);
      search.addEventListener("input", () => {
        stopPlayback();
        renderRows(catalog.entries, appUrl);
      });
    }).catch((error: unknown) => {
      setAdminStatus(status, "SFX catalog unavailable. Test Playback is disabled.", "error");
      renderAdminFailureState(failure, {
        title: "SFX unavailable",
        fallbackMessage: "Unable to load the canonical production SFX catalog and Space Typing app origin.",
        error,
        onRetry: load,
      });
    });
  };

  load();
  return page;
}
