import { renderPhaseBSkills as renderLegacySkills } from "./space-typing-skills-phase-b-legacy";
import { createSkillProductionRuntimePanel } from "./v2/preview/panels/system-runtime-preview";
import { wireLegacyRegistrySelection } from "./v2/preview/registry-selection-sync";

type Navigate = (path: string) => void;

export function renderPhaseBSkills(navigate: Navigate): HTMLElement {
  const page = document.createElement("div");
  const preview = createSkillProductionRuntimePanel();
  const legacy = renderLegacySkills(navigate);
  wireLegacyRegistrySelection(legacy, ["Edit", "Editing"], preview.selectSkill);
  page.append(preview.root, legacy);
  return page;
}
