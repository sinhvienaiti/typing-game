import type { AdminArea } from "./types";
import { renderSharedOverview } from "../shared-overview";
import { renderPhaseBTypingContent } from "../space-typing-typing-content-phase-b";
import { attachProductionPreviewClassification } from "../v2/preview/preview-classification";
import { attachRoleAwareActionGates } from "../v2/security/permission-gates";

const LEARNING_CONTENT = "/admin/shared/learning-content";

// Same Phase B decoration the page had in the Space area: classification badge and role gates.
function decorated(path: string, screen: HTMLElement): HTMLElement {
  attachProductionPreviewClassification(screen, path);
  attachRoleAwareActionGates(screen);
  return screen;
}

export const sharedArea: AdminArea = {
  id: "shared", label: "All games", base: "/admin/shared",
  navGroups: [{
    id: "shared", label: "All games", description: "Read shared services and canonical learning content.",
    items: [
      { label: "Overview", path: "/admin/shared", icon: "◫", description: "See games using Typing Feel and the imported catalogue." },
      { label: "Learning Content", path: LEARNING_CONTENT, icon: "Aa", description: "Browse shared vocabulary and typing texts. Read only." },
    ],
  }],
  renderPage(path, { navigate }) {
    if (path === "/admin/shared") return renderSharedOverview();
    if (path === LEARNING_CONTENT) return decorated(path, renderPhaseBTypingContent(navigate));
    return null;
  },
};
