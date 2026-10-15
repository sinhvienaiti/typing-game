import { renderPhaseBSettings as renderLegacyPhaseBSettings } from "./space-typing-settings-phase-b-legacy";
import { SpaceTypingAdminApi } from "./api";

type Navigate = (path: string) => void;
const api = new SpaceTypingAdminApi();

function el<K extends keyof HTMLElementTagNameMap>(tag: K, cls?: string, text?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (cls) node.className = cls;
  if (text !== undefined) node.textContent = text;
  return node;
}

export function renderPhaseBSettings(navigate: Navigate): HTMLElement {
  const page = renderLegacyPhaseBSettings(navigate);
  const access = el("section", "st-admin-panel solid stx-panel");
  const head = el("div", "st-admin-panel-head");
  const copy = el("div");
  copy.append(
    el("h2", undefined, "Access & Permissions"),
    el("p", undefined, "Review the server-enforced role template and effective permissions for this local Admin deployment."),
  );
  const button = el("button", "st-admin-btn", "Open Roles & Permissions") as HTMLButtonElement;
  button.type = "button";
  button.addEventListener("click", () => navigate("/admin/space-typing/roles"));
  head.append(copy, button);
  access.append(head);
  const status = el("div", "stx-notice info", "Loading effective role…");
  access.append(status);
  void api.getActor().then((actor) => {
    status.className = "stx-notice good";
    status.textContent = `${actor.actorDisplayName} · ${actor.role} · ${actor.permissions.length} effective permissions.`;
  }).catch(() => {
    status.className = "stx-notice warn";
    status.textContent = "Effective role could not be loaded. Server authorization remains authoritative.";
  });
  const header = page.querySelector(".st-admin-page-head");
  if (header !== null) header.insertAdjacentElement("afterend", access);
  else page.prepend(access);
  return page;
}
