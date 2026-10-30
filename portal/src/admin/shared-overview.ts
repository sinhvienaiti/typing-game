import { SpaceTypingAdminApi } from "./api";
import { typingFeelApi } from "./typing-feel/api";
import { TYPING_FEEL_ROUTES } from "./typing-feel/routes";
import type { TypingFeelState } from "./typing-feel/types";

export type SpaceStatus = "available" | "not-checked-out" | "failed";
export type AdminStatus = { spaceAvailable: boolean; spaceStatus: SpaceStatus };

type FileProblem = { status: "missing" | "invalid"; message: string };
type SharedOverview = AdminStatus & {
  consumers: { id: string; name: string; host: string; readsTypingFeel: boolean }[];
  consumersError: FileProblem | null;
  catalogue: null | { status: "imported"; revision: string | number | null; setCount: number } | { status: "invalid"; message: string };
  /** Typing Feel Admin start-up status: available, not-initialized, unavailable or failed. */
  typingFeelStatus?: string;
};

/** Cheap probe used by the shell before Space pages; it reads no Typing Feel files. */
export function getAdminStatus(): Promise<AdminStatus> {
  return new SpaceTypingAdminApi().requestJson<AdminStatus>("/api/admin/shared/status");
}

export function getSharedOverview(): Promise<SharedOverview> {
  return new SpaceTypingAdminApi().requestJson<SharedOverview>("/api/admin/shared/overview");
}

function catalogueSummary(catalogue: SharedOverview["catalogue"]): string {
  if (catalogue === null) return "Not imported yet";
  if (catalogue.status === "invalid") return "Catalogue unreadable";
  return `Revision: ${catalogue.revision ?? "Unknown"} · ${catalogue.setCount} sound sets`;
}

function el<K extends keyof HTMLElementTagNameMap>(tag: K, text?: string, className?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (text) node.textContent = text;
  if (className) node.className = className;
  return node;
}

function linkButton(label: string, path: string, navigate: (path: string) => void, primary = false): HTMLButtonElement {
  const button = el("button", label, primary ? "st-admin-btn primary" : "st-admin-btn");
  button.type = "button";
  button.addEventListener("click", () => navigate(path));
  return button;
}

const TYPING_FEEL_STATUS: Readonly<Record<string, string>> = {
  "not-initialized": "Typing Feel editing opens after the one-off import; Keyboard Sounds shows the command.",
  unavailable: "Typing Feel editing is off on this Admin service; see Release & History for the reason.",
  failed: "Typing Feel failed to start; see the Admin server log.",
};

/** The live Typing Feel revision and the draft waiting (§3.2), or null when Typing Feel cannot say. */
function releaseSummary(state: TypingFeelState | null): string | null {
  if (state === null) return null;
  if (!state.initialized) return "Typing Feel is not imported yet: nothing has been published to the games from this Admin.";
  const live = state.active.publication ? `${state.active.revision} (catalogue ${state.active.publication.catalogueRevision})` : state.active.revision;
  return `Live Typing Feel revision ${live}, changed ${new Date(state.state.updatedAt).toLocaleString(undefined, { dateStyle: "medium", timeStyle: "short" })} · ${state.draft ? `draft ${state.draft.revision} waiting for review` : "no draft waiting"}.`;
}

export function renderSharedOverview(navigate: (path: string) => void = () => undefined): HTMLElement {
  const page = el("div");
  const header = el("header", undefined, "st-admin-page-head");
  const copy = el("div");
  copy.append(el("div", "All games", "st-admin-eyebrow"), el("h1", "Overview"), el("p", "Shared services and learning content across Typing Game. Typing Feel changes reach every game only through Publish in Release & History."));
  header.append(copy);
  const status = el("p", "Loading shared overview…", "st-admin-notice");
  status.setAttribute("role", "status");
  const body = el("div", undefined, "st-admin-shared-panels");
  page.append(header, status, body);
  const load = async () => {
    status.textContent = "Loading shared overview…";
    try {
      // Typing Feel off or not reachable must not hide the rest of the overview.
      const [overview, typingFeel] = await Promise.all([getSharedOverview(), typingFeelApi.state().catch(() => null)]);
      body.replaceChildren();
      const catalogue = el("section", undefined, "st-admin-panel solid");
      catalogue.append(el("h2", "Typing Feel catalogue"));
      catalogue.append(el("p", catalogueSummary(overview.catalogue)));
      if (overview.catalogue?.status === "invalid") {
        catalogue.append(el("p", `typing-feel/public/v1/keys/keys-manifest.json: ${overview.catalogue.message}`, "st-admin-notice"));
      }
      const note = overview.typingFeelStatus ? TYPING_FEEL_STATUS[overview.typingFeelStatus] : undefined;
      if (note) catalogue.append(el("p", note, "st-admin-notice"));
      const links = el("div", undefined, "st-admin-shared-links");
      links.append(
        linkButton("Keyboard Sounds", TYPING_FEEL_ROUTES.keyboardSounds, navigate, true),
        linkButton("Typing Effects", TYPING_FEEL_ROUTES.typingEffects, navigate),
        linkButton("Release & History", TYPING_FEEL_ROUTES.release, navigate),
      );
      catalogue.append(links);
      const games = el("section", undefined, "st-admin-panel solid");
      games.append(el("h2", "Games using Typing Feel"));
      const table = el("table", undefined, "st-admin-table");
      const head = el("thead");
      const headings = el("tr");
      for (const label of ["Game", "Host", "Reads Typing Feel", "Open game"]) headings.append(el("th", label));
      head.append(headings);
      const rows = el("tbody");
      for (const consumer of overview.consumers) {
        const row = el("tr");
        row.append(el("td", consumer.name), el("td", consumer.host), el("td", consumer.readsTypingFeel ? "Connected" : "Not yet · local copy"));
        const action = el("td");
        const link = el("a", "Open game", "st-admin-btn");
        link.href = `https://${consumer.host}`;
        link.target = "_blank";
        link.rel = "noopener noreferrer";
        link.setAttribute("aria-label", `Open ${consumer.name}`);
        action.append(link);
        row.append(action);
        rows.append(row);
      }
      table.append(head, rows);
      const scroll = el("div", undefined, "st-admin-shared-table");
      scroll.append(table);
      if (overview.consumersError !== null) {
        games.append(el("p", `Game list unreadable (admin/typing-feel/consumers.json ${overview.consumersError.status}): ${overview.consumersError.message}`, "st-admin-notice"));
      }
      games.append(scroll);
      body.append(catalogue, games);
      status.textContent = releaseSummary(typingFeel) ?? "Typing Feel release status unavailable; see Release & History.";
    } catch {
      status.textContent = "Shared overview unavailable. Check the local Admin service.";
      const retry = el("button", "Retry", "st-admin-btn");
      retry.type = "button";
      retry.addEventListener("click", () => { retry.remove(); void load(); });
      status.append(retry);
    }
  };
  void load();
  return page;
}
