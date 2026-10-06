import fs from "node:fs";

const file = "scripts/validate-space-admin-ui.mjs";
const lines = fs.readFileSync(file, "utf8").split("\n");

const cleanupIndex = lines.findIndex((line) => line.includes("wire-space-admin-") && line.includes("Temporary Admin wiring script remains"));
if (cleanupIndex < 0) throw new Error("Temporary-script validator line not found");
lines[cleanupIndex] = '    assert(!/^(?:wire|apply)-space-admin-.*\\.mjs$/i.test(entry), `Temporary Admin one-shot script remains: ${entry}`);';

const segmentIndex = lines.findIndex((line) => line.includes("World Music assignment segmented aria state is missing"));
if (segmentIndex < 0) throw new Error("World Music assignment validator line not found");
lines[segmentIndex] = 'assert(worldMusic.includes(\'inherit.setAttribute("aria-pressed", "false")\') && worldMusic.includes(\'replace.setAttribute("aria-pressed", "true")\'), "World Music assignment segmented aria state is missing");';

const outputIndex = lines.findIndex((line) => line.includes("Space Typing Admin UI contract: PASS"));
if (outputIndex < 0) throw new Error("Validator PASS output line not found");
lines[outputIndex] = 'console.log(`Space Typing Admin UI contract: PASS (${routes.length} registered screens + operational mock workflows + final A11y/state guards).`);';

fs.writeFileSync(file, lines.join("\n"));
