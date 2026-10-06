import fs from "node:fs";

const BASE = "${BASE}";
const uiFile = "portal/src/admin/space-typing-world-music-v2.ts";
let ui = fs.readFileSync(uiFile, "utf8");

function replaceRequired(before, after, label) {
  if (!ui.includes(before)) throw new Error(`Missing expected source for ${label}`);
  ui = ui.replace(before, after);
}

replaceRequired(
  '  scope: "stage" as "all" | "galaxy" | "world" | "stage",\n};',
  '  scope: "stage" as "all" | "galaxy" | "world" | "stage",\n  assignment: "replace" as "inherit" | "replace",\n};',
  "assignment state",
);

replaceRequired(
  'const control = btn(label, () => { state.scope = value; currentNavigate(`${BASE}/world-music`); }, state.scope === value ? "active" : "");',
  'const control = btn(label, () => { state.scope = value; if (value === "all") state.assignment = "replace"; currentNavigate(`${BASE}/world-music`); }, state.scope === value ? "active" : "");',
  "scope assignment normalization",
);

replaceRequired(
  'body.append(btn("All Game", () => { state.scope = "all"; currentNavigate(`${BASE}/world-music`); }, `stx-music-scope ${state.scope === "all" ? "active" : ""}`));',
  'body.append(btn("All Game", () => { state.scope = "all"; state.assignment = "replace"; currentNavigate(`${BASE}/world-music`); }, `stx-music-scope ${state.scope === "all" ? "active" : ""}`));',
  "tree root assignment normalization",
);

replaceRequired(
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
`  const inherit = btn("Inherit", () => { state.assignment = "inherit"; currentNavigate(\`${BASE}/world-music\`); }, state.assignment === "inherit" ? "active" : "");
  const replace = btn("Replace", () => { state.assignment = "replace"; currentNavigate(\`${BASE}/world-music\`); }, state.assignment === "replace" ? "active" : "");
  inherit.disabled = state.scope === "all";
  inherit.title = inherit.disabled ? "Global scope has no parent configuration to inherit from." : "Use the effective value from the parent scope.";
  inherit.setAttribute("aria-pressed", String(state.assignment === "inherit"));
  replace.setAttribute("aria-pressed", String(state.assignment === "replace"));
  seg.append(inherit, replace);`,
  "assignment segmented state",
);

replaceRequired(
  '  root.append(badge("REPLACED", "good"), el("div", "stx-effective-source", `Configured: Replace · Effective source: ${label} · ${state.role}`));',
  '  const configured = state.assignment === "replace" ? "Replace" : "Inherit";\n  const resolvedSource = state.assignment === "replace" ? label : state.scope === "stage" ? `World ${String(state.world).padStart(2, "0")}` : state.scope === "world" ? `Galaxy ${String(state.galaxy).padStart(2, "0")}` : "Global";\n  root.append(badge(state.assignment === "replace" ? "REPLACED" : "INHERIT", state.assignment === "replace" ? "good" : "info"), el("div", "stx-effective-source", `Configured: ${configured} · Effective source: ${resolvedSource} · ${state.role}`));',
  "effective assignment preview",
);

fs.writeFileSync(uiFile, ui);

const validatorFile = "scripts/validate-space-admin-ui.mjs";
let validator = fs.readFileSync(validatorFile, "utf8");
const anchor = 'assert(worldMusic.includes(\'inherit.setAttribute("aria-pressed", "false")\') && worldMusic.includes(\'replace.setAttribute("aria-pressed", "true")\'), "World Music assignment segmented aria state is missing");';
if (!validator.includes(anchor)) throw new Error("Validator assignment anchor missing");
validator = validator.replace(
  anchor,
  'assert(worldMusic.includes(\'assignment: "replace" as "inherit" | "replace"\'), "World Music assignment mock state is missing");\nassert(worldMusic.includes(\'inherit.setAttribute("aria-pressed", String(state.assignment === "inherit"))\') && worldMusic.includes(\'replace.setAttribute("aria-pressed", String(state.assignment === "replace"))\'), "World Music assignment segmented aria state is missing");\nassert(worldMusic.includes(\'Configured: ${configured} · Effective source: ${resolvedSource}\'), "World Music effective playlist does not reflect assignment state");'
);
fs.writeFileSync(validatorFile, validator);
