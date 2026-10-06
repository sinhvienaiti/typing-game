import fs from "node:fs";

function replaceRequired(file, before, after, label) {
  const source = fs.readFileSync(file, "utf8");
  if (!source.includes(before)) {
    throw new Error(`Missing expected source for ${label}: ${file}`);
  }
  fs.writeFileSync(file, source.replace(before, after));
}

replaceRequired(
  "portal/src/admin/space-typing-extended.ts",
  '  rollback.disabled = selectedStatus === "Draft" || uiState.selectedRevision === "r127";',
  '  const rollbackEligible = selectedStatus === "Published" && uiState.selectedRevision !== "r127";\n  rollback.disabled = !rollbackEligible;',
  "History rollback eligibility",
);

replaceRequired(
  "portal/src/admin/space-typing-world-music-v2.ts",
  '  seg.append(btn("Inherit"), btn("Replace", () => undefined, "active"));',
  `  const inherit = btn("Inherit", () => {
    inherit.setAttribute("aria-pressed", "true");
    replace.setAttribute("aria-pressed", "false");
    inherit.classList.add("active");
    replace.classList.remove("active");
  });
  const replace = btn("Replace", () => {
    inherit.setAttribute("aria-pressed", "false");
    replace.setAttribute("aria-pressed", "true");
    inherit.classList.remove("active");
    replace.classList.add("active");
  }, "active");
  inherit.setAttribute("aria-pressed", "false");
  replace.setAttribute("aria-pressed", "true");
  seg.append(inherit, replace);`,
  "World Music assignment segmented aria state",
);

const validator = "scripts/validate-space-admin-ui.mjs";
let source = fs.readFileSync(validator, "utf8");
const anchor = 'assert(dialogs.includes("I understand the active configuration will point to"), "Rollback acknowledgement gate is missing");';
const additions = `${anchor}\n\nassert(main.includes('control.setAttribute("aria-label", label)'), "Audio range aria-label is missing");\nassert(main.includes('search.setAttribute("aria-label", "Search music library")'), "Music search aria-label is missing");\nassert(main.includes('type.setAttribute("aria-label", "Filter music by type")'), "Music type filter aria-label is missing");\nassert(main.includes('status.setAttribute("aria-label", "Filter music by status")'), "Music status filter aria-label is missing");\nassert(main.includes('control.setAttribute("aria-pressed", String(index === 0))'), "Dashboard segmented aria state is missing");\nassert(extended.includes('input.setAttribute("aria-label", label)'), "Extended range aria-label is missing");\nassert(extended.includes('control.setAttribute("aria-pressed", String(enabled))'), "Extended toggle aria state is missing");\nassert(worldMusic.includes('stageBtn.setAttribute("aria-pressed", String(state.stages.has(stageNumber)))'), "World Music stage aria state is missing");\nassert(worldMusic.includes('replace.setAttribute("aria-pressed", "true")'), "World Music assignment segmented aria state is missing");\nassert(extended.includes('publish.disabled = selectedStatus !== "Draft"'), "History Publish must be limited to Draft revisions");\nassert(extended.includes('const rollbackEligible = selectedStatus === "Published" && uiState.selectedRevision !== "r127"'), "History Rollback must be limited to older Published revisions");`;
if (!source.includes(anchor)) throw new Error("Validator hardening anchor is missing");
source = source.replace(anchor, additions);
source = source.replace(
  '    assert(!/^wire-space-admin-.*\\.mjs$/i.test(entry), `Temporary Admin wiring script remains: ${entry}`);',
  '    assert(!/^(?:wire|apply)-space-admin-.*\\.mjs$/i.test(entry), `Temporary Admin one-shot script remains: ${entry}`);',
);
fs.writeFileSync(validator, source);
