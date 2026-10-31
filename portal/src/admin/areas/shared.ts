import type { AdminArea } from "./types";
import { renderSharedOverview } from "../shared-overview";
import { renderPhaseBTypingContent } from "../space-typing-typing-content-phase-b";
import { attachProductionPreviewClassification } from "../v2/preview/preview-classification";
import { attachRoleAwareActionGates } from "../v2/security/permission-gates";
import { renderTypingFeelAddSoundSet } from "../typing-feel/add-sound-set";
import { renderTypingFeelKeyboardSounds } from "../typing-feel/keyboard-sounds";
import { renderTypingFeelRelease } from "../typing-feel/release";
import { TYPING_FEEL_ROUTES } from "../typing-feel/routes";
import { renderTypingFeelTypingEffects } from "../typing-feel/typing-effects";

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
    id: "shared", label: "All games", description: "Shared services every game reads: the Typing Feel overview and canonical learning content.",
    items: [
      { label: "Overview", path: "/admin/shared", icon: "◫", description: "See games using Typing Feel and the live catalogue." },
      { label: "Learning Content", path: LEARNING_CONTENT, icon: "Aa", description: "Browse shared vocabulary and typing texts. Read only." },
    ],
  }, {
    id: "typing-feel", label: "Typing Feel", description: "Keyboard sounds and typing effects every game shares: edit a draft, review it, publish it to all games.",
    items: [
      { label: "Keyboard Sounds", path: TYPING_FEEL_ROUTES.keyboardSounds, icon: "◖", description: "Order, hide, rename and choose the default key-sound set for every game." },
      { label: "Add sound set", path: TYPING_FEEL_ROUTES.addSoundSet, icon: "+", description: "Upload a take, Format it (natural), listen A/B, score it and add it to the draft." },
      { label: "Typing Effects", path: TYPING_FEEL_ROUTES.typingEffects, icon: "✧", description: "Default typing-effect style, intensity, size and key volume for new players." },
      { label: "Release & History", path: TYPING_FEEL_ROUTES.release, icon: "↶", description: "Live revision, Git and Drive status, the draft, Publish and Rollback with audit." },
    ],
  }],
  renderPage(path, { navigate }) {
    if (path === "/admin/shared") return renderSharedOverview(navigate);
    if (path === LEARNING_CONTENT) return decorated(path, renderPhaseBTypingContent(navigate));
    // Role gates only: the explicit data-admin-permission of every Typing Feel button wins over label rules (§3.13).
    if (path === TYPING_FEEL_ROUTES.keyboardSounds) return attachRoleAwareActionGates(renderTypingFeelKeyboardSounds(navigate));
    if (path === TYPING_FEEL_ROUTES.addSoundSet) return attachRoleAwareActionGates(renderTypingFeelAddSoundSet(navigate));
    if (path === TYPING_FEEL_ROUTES.typingEffects) return attachRoleAwareActionGates(renderTypingFeelTypingEffects(navigate));
    if (path === TYPING_FEEL_ROUTES.release) return attachRoleAwareActionGates(renderTypingFeelRelease(navigate));
    return null;
  },
};
