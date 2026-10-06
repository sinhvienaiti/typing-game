import fs from "node:fs";

function replaceRequired(file, before, after, label) {
  const source = fs.readFileSync(file, "utf8");
  if (!source.includes(before)) throw new Error(`Missing expected source for ${label}: ${file}`);
  fs.writeFileSync(file, source.replace(before, after));
}

replaceRequired(
  "portal/src/admin/space-typing-command.ts",
  'let current: HTMLElement | null = null;\nlet currentCleanup: (() => void) | null = null;',
  'let current: HTMLElement | null = null;\nlet currentCleanup: (() => void) | null = null;\nlet previousFocus: HTMLElement | null = null;',
  "command palette focus state",
);

replaceRequired(
  "portal/src/admin/space-typing-command.ts",
  'export function closeAdminCommandPalette(): void {\n  currentCleanup?.();\n  currentCleanup = null;\n  current?.remove();\n  current = null;\n}',
  'export function closeAdminCommandPalette(): void {\n  const focusTarget = previousFocus;\n  currentCleanup?.();\n  currentCleanup = null;\n  current?.remove();\n  current = null;\n  previousFocus = null;\n  focusTarget?.focus();\n}',
  "command palette focus restoration",
);

replaceRequired(
  "portal/src/admin/space-typing-command.ts",
  'export function openAdminCommandPalette(navigate: Navigate): void {\n  closeAdminCommandPalette();\n  const overlay = document.createElement("div");',
  'export function openAdminCommandPalette(navigate: Navigate): void {\n  closeAdminCommandPalette();\n  previousFocus = document.activeElement instanceof HTMLElement ? document.activeElement : null;\n  const overlay = document.createElement("div");',
  "command palette focus capture",
);

replaceRequired(
  "portal/src/admin/space-typing-command.ts",
  '  const onKey = (event: KeyboardEvent) => {\n    if (event.key === "Escape") closeAdminCommandPalette();\n  };',
  '  const onKey = (event: KeyboardEvent) => {\n    if (event.key === "Escape") {\n      closeAdminCommandPalette();\n      return;\n    }\n    if (event.key === "Tab") {\n      const focusables: HTMLElement[] = [input, ...Array.from(results.querySelectorAll<HTMLButtonElement>("button:not([disabled])"))];\n      const first = focusables[0];\n      const last = focusables[focusables.length - 1];\n      if (first === undefined || last === undefined) return;\n      if (event.shiftKey && document.activeElement === first) {\n        event.preventDefault();\n        last.focus();\n      } else if (!event.shiftKey && document.activeElement === last) {\n        event.preventDefault();\n        first.focus();\n      }\n    }\n  };',
  "command palette Tab focus trap",
);

replaceRequired(
  "portal/src/admin/space-typing.ts",
  '    for (const track of tracks) {\n      const row = element("tr", "clickable");\n      row.innerHTML = `<td>▶</td><td><span class="primary">${track.title}</span><br><small>${track.id}</small></td><td>${track.type}</td><td>${track.duration}</td><td>${track.format}</td><td>${track.bpm}</td><td>${track.mood}</td><td>${track.usage}</td>`;\n      const state = element("td");\n      state.append(statusBadge(track.status, track.status === "READY" ? "good" : track.status === "UNUSED" ? "warn" : "bad"));\n      row.append(state);\n      row.addEventListener("click", () => {\n        this.selectedTrackId = track.id;\n        onSelect();\n      });\n      body.append(row);\n    }',
  '    for (const track of tracks) {\n      const row = element("tr", "clickable");\n      const selectTrack = (): void => {\n        this.selectedTrackId = track.id;\n        onSelect();\n      };\n      row.innerHTML = `<td><span class="primary">${track.title}</span><br><small>${track.id}</small></td><td>${track.type}</td><td>${track.duration}</td><td>${track.format}</td><td>${track.bpm}</td><td>${track.mood}</td><td>${track.usage}</td>`;\n      const previewCell = element("td");\n      const preview = element("button", "st-admin-play", "▶") as HTMLButtonElement;\n      preview.type = "button";\n      preview.setAttribute("aria-label", `Open ${track.title} track details`);\n      preview.title = `Open ${track.title} track details`;\n      preview.addEventListener("click", (event) => {\n        event.stopPropagation();\n        selectTrack();\n      });\n      previewCell.append(preview);\n      row.prepend(previewCell);\n      const state = element("td");\n      state.append(statusBadge(track.status, track.status === "READY" ? "good" : track.status === "UNUSED" ? "warn" : "bad"));\n      row.append(state);\n      row.addEventListener("click", selectTrack);\n      body.append(row);\n    }',
  "Music Library keyboard-accessible row action",
);

const validatorFile = "scripts/validate-space-admin-ui.mjs";
let validator = fs.readFileSync(validatorFile, "utf8");
const commandAnchor = 'assert(command.includes("currentCleanup"), "Command palette listener cleanup is missing");';
if (!validator.includes(commandAnchor)) throw new Error("Validator command palette anchor missing");
validator = validator.replace(
  commandAnchor,
  commandAnchor + '\nassert(command.includes(\'event.key === "Tab"\') && command.includes("previousFocus") && command.includes("focusTarget?.focus()"), "Command palette keyboard focus trap/restoration is missing");',
);
const tableAnchor = 'assert(main.includes(\'play.setAttribute("aria-label", "Play track preview")\'), "Music Library symbol-only preview control needs an accessible name");';
if (!validator.includes(tableAnchor)) throw new Error("Validator Music Library preview anchor missing");
validator = validator.replace(
  tableAnchor,
  tableAnchor + '\nassert(main.includes(\'preview.setAttribute("aria-label", `Open ${track.title} track details`)\') && main.includes(\'event.stopPropagation()\'), "Music Library table action is not keyboard accessible");',
);
fs.writeFileSync(validatorFile, validator);
