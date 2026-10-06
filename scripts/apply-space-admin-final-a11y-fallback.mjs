import fs from "node:fs";

function replaceRequired(file, before, after, label) {
  const source = fs.readFileSync(file, "utf8");
  if (!source.includes(before)) throw new Error(`Missing expected source for ${label}: ${file}`);
  fs.writeFileSync(file, source.replace(before, after));
}

replaceRequired(
  "portal/src/admin/space-typing.ts",
  '    player.append(button("▶", () => undefined, "st-admin-play"));',
  '    const play = button("▶", () => undefined, "st-admin-play");\n    play.setAttribute("aria-label", "Play track preview");\n    play.title = "Play track preview";\n    player.append(play);',
  "Music Library preview accessible name",
);

replaceRequired(
  "portal/src/admin/space-typing-world-music-v2.ts",
  '  const fallback = el("div", "stx-fallback");\n  fallback.append(el("span", undefined, "Fallback chain"), el("code", undefined, `${label} → World ${String(state.world).padStart(2, "0")} ${state.role} → World Normal → Galaxy Default → Global ${state.role} → Global Normal`));\n  root.append(fallback);',
  '  const fallback = el("div", "stx-fallback");\n  const fallbackParts: string[] = [];\n  const worldLabel = `World ${String(state.world).padStart(2, "0")}`;\n  const galaxyLabel = `Galaxy ${String(state.galaxy).padStart(2, "0")}`;\n  if (state.scope === "stage") fallbackParts.push(`${label} ${state.role}`);\n  if (state.scope === "stage" || state.scope === "world") {\n    fallbackParts.push(`${worldLabel} ${state.role}`);\n    if (state.role !== "Normal") fallbackParts.push(`${worldLabel} Normal`);\n  }\n  if (state.scope !== "all") {\n    fallbackParts.push(`${galaxyLabel} ${state.role}`);\n    if (state.role !== "Normal") fallbackParts.push(`${galaxyLabel} Normal`);\n  }\n  fallbackParts.push(`Global ${state.role}`);\n  if (state.role !== "Normal") fallbackParts.push("Global Normal");\n  fallback.append(el("span", undefined, "Fallback chain"), el("code", undefined, fallbackParts.join(" → ")));\n  root.append(fallback);',
  "World Music scope-aware fallback trace",
);

replaceRequired(
  "portal/src/admin/space-typing-world-music-v2.ts",
  '  const player = el("div", "stx-music-player");\n  player.append(btn("◀"), btn("▶ Preview", () => undefined, "st-admin-btn primary"), btn("▶▶"), btn("Validate"));\n  root.append(player);',
  '  const player = el("div", "stx-music-player");\n  const previous = btn("◀");\n  previous.setAttribute("aria-label", "Previous track");\n  previous.title = "Previous track";\n  const next = btn("▶▶");\n  next.setAttribute("aria-label", "Next track");\n  next.title = "Next track";\n  player.append(previous, btn("▶ Preview", () => undefined, "st-admin-btn primary"), next, btn("Validate"));\n  root.append(player);',
  "World Music preview accessible names",
);

const validatorFile = "scripts/validate-space-admin-ui.mjs";
let validator = fs.readFileSync(validatorFile, "utf8");
const anchor = 'assert(worldMusic.includes("Fallback chain"), "World Music effective fallback preview is missing");';
if (!validator.includes(anchor)) throw new Error("Validator fallback anchor missing");
validator = validator.replace(
  anchor,
  anchor + '\nassert(worldMusic.includes(\'const fallbackParts: string[] = []\') && worldMusic.includes(\'const galaxyLabel = `Galaxy ${String(state.galaxy).padStart(2, "0")}`\') && worldMusic.includes(\'fallbackParts.join(" → ")\'), "World Music fallback trace is not scope-aware");\nassert(worldMusic.includes(\'previous.setAttribute("aria-label", "Previous track")\') && worldMusic.includes(\'next.setAttribute("aria-label", "Next track")\'), "World Music symbol-only preview controls need accessible names");',
);
const mainAnchor = 'assert(main.includes(\'status.setAttribute("aria-label", "Filter music by status")\'), "Music status filter aria-label is missing");';
if (!validator.includes(mainAnchor)) throw new Error("Validator Music Library a11y anchor missing");
validator = validator.replace(
  mainAnchor,
  mainAnchor + '\nassert(main.includes(\'play.setAttribute("aria-label", "Play track preview")\'), "Music Library symbol-only preview control needs an accessible name");',
);
fs.writeFileSync(validatorFile, validator);
