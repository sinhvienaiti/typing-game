import { SpaceTypingAdminApi } from "./api";

export type SpaceStatus = "available" | "not-checked-out" | "failed";
export type AdminStatus = { spaceAvailable: boolean; spaceStatus: SpaceStatus };

type FileProblem = { status: "missing" | "invalid"; message: string };
type SharedOverview = AdminStatus & {
  consumers: { id: string; name: string; host: string; readsTypingFeel: boolean }[];
  consumersError: FileProblem | null;
  catalogue: null | { status: "imported"; revision: string | number | null; setCount: number } | { status: "invalid"; message: string };
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

export function renderSharedOverview(): HTMLElement {
  const page = el("div");
  const header = el("header", undefined, "st-admin-page-head");
  const copy = el("div");
  copy.append(el("div", "All games", "st-admin-eyebrow"), el("h1", "Overview"), el("p", "Shared services and learning content across Typing Game."));
  header.append(copy, el("span", "READ ONLY", "st-admin-status info"));
  const status = el("p", "Loading shared overview…", "st-admin-notice");
  status.setAttribute("role", "status");
  const body = el("div", undefined, "st-admin-shared-panels");
  page.append(header, status, body);
  const load = async () => {
    status.textContent = "Loading shared overview…";
    try {
      const overview = await getSharedOverview();
      body.replaceChildren();
      const catalogue = el("section", undefined, "st-admin-panel solid");
      catalogue.append(el("h2", "Typing Feel catalogue"));
      catalogue.append(el("p", catalogueSummary(overview.catalogue)));
      if (overview.catalogue?.status === "invalid") {
        catalogue.append(el("p", `typing-feel/public/v1/keys/keys-manifest.json: ${overview.catalogue.message}`, "st-admin-notice"));
      }
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
      status.textContent = "Read-only overview · no shared settings have been changed.";
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
