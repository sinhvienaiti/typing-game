import "./developer-tools.css";
import { SpaceTypingAdminApi, type DeveloperToolsManifest } from "../api";
import { adminErrorMessage } from "../admin-http";
import type { AdminHelpScope } from "./admin-help";
import {
  createAdminCardGrid,
  createAdminErrorState,
  createAdminPageHeader,
  createAdminSkeleton,
  createAdminStatusChip,
} from "./admin-components";

function element<K extends keyof HTMLElementTagNameMap>(tag: K, className?: string, text?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (className !== undefined) node.className = className;
  if (text !== undefined) node.textContent = text;
  return node;
}

function renderManifest(body: HTMLElement, manifest: DeveloperToolsManifest, navigate: (path: string) => void): void {
  const sections = manifest.sections.map((section) => {
    const card = element("section", "st-admin-v2-dev-card");
    const head = element("div", "st-admin-v2-dev-card-head");
    head.append(element("h2", undefined, section.label), createAdminStatusChip("Developer", "warn"));
    card.append(head, element("p", "st-admin-v2-dev-description", section.description));

    const tools = element("div", "st-admin-v2-dev-links");
    for (const tool of section.tools) {
      const button = element("button", "st-admin-v2-dev-link");
      button.type = "button";
      const copy = element("span");
      copy.append(element("strong", undefined, tool.label), element("small", undefined, tool.description));
      button.append(copy, element("span", "st-admin-v2-dev-arrow", "→"));
      button.addEventListener("click", () => navigate(tool.path));
      tools.append(button);
    }
    card.append(tools);
    return card;
  });
  body.replaceChildren(createAdminCardGrid(...sections));
}

export function renderAdminV2DeveloperTools(navigate: (path: string) => void, helpScope: AdminHelpScope): HTMLElement {
  const root = element("section", "st-admin-v2-developer-tools");
  root.append(createAdminPageHeader({
    eyebrow: "System",
    title: "Developer Tools",
    subtitle: "Runtime contracts, capability diagnostics and isolated QA tools are kept here so normal administrator workflows stay focused on game management.",
    helpScope,
    help: {
      title: "Developer-only area",
      content: "These tools expose runtime ownership and implementation diagnostics. Access is permission-gated and they are not substitutes for missing administrator authoring capabilities.",
    },
  }));

  const warning = element("div", "st-admin-v2-dev-warning");
  warning.append(
    createAdminStatusChip("Technical", "warn"),
    element("span", undefined, "Diagnostics may use runtime IDs, ownership terms and implementation details intentionally hidden from normal Admin screens."),
  );
  root.append(warning);

  const body = element("div", "st-admin-v2-dev-body");
  body.append(createAdminSkeleton(6));
  root.append(body);

  requestAnimationFrame(async () => {
    const api = new SpaceTypingAdminApi();
    try {
      const manifest = await api.getDeveloperToolsManifest();
      if (!root.isConnected) return;
      renderManifest(body, manifest, navigate);
    } catch (error) {
      if (!root.isConnected) return;
      body.replaceChildren(createAdminErrorState({
        title: "Developer Tools unavailable",
        message: adminErrorMessage(error, "You do not have permission to inspect developer diagnostics."),
      }));
    }
  });

  return root;
}
