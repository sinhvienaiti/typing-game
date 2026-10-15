import { renderPhaseBSkills as renderLegacySkills } from "./space-typing-skills-phase-b-legacy";
import { createSkillProductionRuntimePanel } from "./v2/preview/panels/system-runtime-preview";

type Navigate = (path: string) => void;

export function renderPhaseBSkills(navigate: Navigate): HTMLElement {
  const page = document.createElement("div");
  page.append(createSkillProductionRuntimePanel(), renderLegacySkills(navigate));
  return page;
}
