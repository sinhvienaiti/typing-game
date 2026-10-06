import fs from "node:fs";

function replaceRequired(file, before, after, label) {
  const source = fs.readFileSync(file, "utf8");
  if (!source.includes(before)) throw new Error(`Missing ${label} anchor in ${file}`);
  fs.writeFileSync(file, source.replace(before, after));
}

replaceRequired(
  "portal/src/admin/space-typing.ts",
  'import { renderExtendedAdminScreen } from "./space-typing-extended";',
  'import { renderExtendedAdminScreen } from "./space-typing-extended";\nimport { renderPhaseBAdminScreen } from "./space-typing-phase-b";',
  "Phase B import",
);

replaceRequired(
  "portal/src/admin/space-typing.ts",
  '    if (path === `${ADMIN_BASE}/daily-weekly`) return renderDailyWeekly();\n    return renderExtendedAdminScreen(path, this.navigate) ?? this.renderUnknown(path);',
  '    if (path === `${ADMIN_BASE}/daily-weekly`) return renderDailyWeekly();\n    const phaseB = renderPhaseBAdminScreen(path, this.navigate);\n    if (phaseB !== null) return phaseB;\n    return renderExtendedAdminScreen(path, this.navigate) ?? this.renderUnknown(path);',
  "Phase B router",
);

const validatorPath = "scripts/validate-space-admin-phase-b.mjs";
let validator = fs.readFileSync(validatorPath, "utf8");
validator = validator.replace(
  'const api = await readFile(new URL("portal/src/admin/api.ts", root), "utf8");',
  'const api = await readFile(new URL("portal/src/admin/api.ts", root), "utf8");\nconst main = await readFile(new URL("portal/src/admin/space-typing.ts", root), "utf8");\nconst phaseB = await readFile(new URL("portal/src/admin/space-typing-phase-b.ts", root), "utf8");',
);
validator = validator.replace(
  'assert.equal(settings?.status, "phase-b-persistence-ready");',
  'assert.equal(settings?.status, "phase-b-ui-wired");',
);
validator = validator.replace(
  'assert.equal(flags?.status, "phase-b-persistence-ready");',
  'assert.equal(flags?.status, "phase-b-ui-wired");',
);
validator = validator.replace(
  'assert.match(api, /getRuntime\\(\\): Promise<AdminRuntimePayload>/);',
  'assert.match(api, /getRuntime\\(\\): Promise<AdminRuntimePayload>/);\nassert.match(main, /renderPhaseBAdminScreen/);\nassert.match(main, /if \\(phaseB !== null\\) return phaseB/);\nassert.match(phaseB, /Admin Phase B · General Settings draft/);\nassert.match(phaseB, /Admin Phase B · Feature Flags draft/);\nassert.match(phaseB, /api\\.createRevision/);\nassert.doesNotMatch(phaseB, /api\\.publish/);\nassert.match(phaseB, /runtime unchanged/);',
);
fs.writeFileSync(validatorPath, validator);

const mapPath = "admin/space-typing-phase-b-map.v1.json";
const map = JSON.parse(fs.readFileSync(mapPath, "utf8"));
for (const entry of map.screens) {
  if (entry.route === "/admin/space-typing/settings" || entry.route === "/admin/space-typing/flags") {
    entry.status = "phase-b-ui-wired";
  }
}
fs.writeFileSync(mapPath, `${JSON.stringify(map, null, 2)}\n`);

const docPath = "portal/src/admin/SPACE_TYPING_PHASE_B_MAPPING.md";
let doc = fs.readFileSync(docPath, "utf8");
doc = doc.replace(
  '2. **B02 — Wire General Settings + Feature Flags UI**: hydrate active/draft values, create revisions on Save Draft, validation/error state, no direct publish.',
  '2. **B02 — Wire General Settings + Feature Flags UI**: hydrate active values, create immutable revisions on Save Draft, surface validation/error state, and never direct-publish. **Implemented.**',
);
fs.writeFileSync(docPath, doc);
