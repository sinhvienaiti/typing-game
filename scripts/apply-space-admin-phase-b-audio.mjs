import fs from "node:fs";

function replaceRequired(file, before, after, label) {
  const source = fs.readFileSync(file, "utf8");
  if (!source.includes(before)) throw new Error(`Missing ${label} anchor in ${file}`);
  fs.writeFileSync(file, source.replace(before, after));
}

replaceRequired(
  "admin/default-config.mjs",
  '        sfx: 0.5,\n        announcer: 0.85',
  '        sfx: 0.5,\n        credit: 1,\n        announcer: 0.85,\n        categories: {\n          typing: 1,\n          combat: 1,\n          warnings: 1,\n          ui: 1,\n          rewards: 1\n        }',
  "B03 default audio profile",
);

const storePath = "admin/store.mjs";
let store = fs.readFileSync(storePath, "utf8");
const audioValidation = `function validateAudio(audio) {
  object(audio, "audio");
  string(audio.profileId, "audio.profileId", { max: 80, pattern: /^[a-z0-9][a-z0-9-]*$/ });
  const defaults = object(audio.defaults, "audio.defaults");
  for (const key of ["master", "pronunciation", "music", "ambient", "sfx", "announcer"]) {
    number(defaults[key], \`audio.defaults.\${key}\`, { min: 0, max: 1 });
  }
  if (defaults.credit !== undefined) number(defaults.credit, "audio.defaults.credit", { min: 0, max: 2 });
  if (defaults.categories !== undefined) {
    const categories = object(defaults.categories, "audio.defaults.categories");
    for (const key of ["typing", "combat", "warnings", "ui", "rewards"]) {
      number(categories[key], \`audio.defaults.categories.\${key}\`, { min: 0, max: 1 });
    }
  }
}

`;
const storeAnchor = "function validateSystem(system) {";
if (!store.includes(storeAnchor)) throw new Error("Missing store validation insertion anchor");
store = store.replace(storeAnchor, audioValidation + storeAnchor);
store = store.replace(
  '    if (config.audio === null || typeof config.audio !== "object") {\n      throw new AdminValidationError("audio config is required.");\n    }',
  '    validateAudio(config.audio);',
);
fs.writeFileSync(storePath, store);

const apiPath = "portal/src/admin/api.ts";
let api = fs.readFileSync(apiPath, "utf8");
api = api.replace(
  'export type AudioDefaults = {\n  master: number;\n  pronunciation: number;\n  music: number;\n  ambient: number;\n  sfx: number;\n  announcer: number;\n};',
  'export type AudioCategoryDefaults = {\n  typing: number;\n  combat: number;\n  warnings: number;\n  ui: number;\n  rewards: number;\n};\n\nexport type AudioDefaults = {\n  master: number;\n  pronunciation: number;\n  music: number;\n  ambient: number;\n  sfx: number;\n  /** Legacy revisions may omit this B03 field. Child runtime supports 0..2. */\n  credit?: number;\n  announcer: number;\n  /** Legacy revisions may omit these B03 category preferences. */\n  categories?: Partial<AudioCategoryDefaults>;\n};',
);
fs.writeFileSync(apiPath, api);

const phaseBPath = "portal/src/admin/space-typing-phase-b.ts";
let phaseB = fs.readFileSync(phaseBPath, "utf8");
phaseB = 'import { renderPhaseBAudio } from "./space-typing-audio-phase-b";\n' + phaseB;
phaseB = phaseB.replace(
  'export function renderPhaseBAdminScreen(path: string, navigate: Navigate): HTMLElement | null {\n  if (path === `${BASE}/settings`) return renderSettings(navigate);',
  'export function renderPhaseBAdminScreen(path: string, navigate: Navigate): HTMLElement | null {\n  if (path === `${BASE}/audio`) return renderPhaseBAudio(navigate);\n  if (path === `${BASE}/settings`) return renderSettings(navigate);',
);
fs.writeFileSync(phaseBPath, phaseB);

const mainPath = "portal/src/admin/space-typing.ts";
let main = fs.readFileSync(mainPath, "utf8");
main = main.replace('  audioDefaults,\n  duckingDefaults,\n', '');
main = main.replace('  private audioChanges = 0;\n', '');
main = main.replace(
  '    if (path === ADMIN_BASE) return this.renderOverview();\n    if (path === `${ADMIN_BASE}/audio`) return this.renderAudio();',
  '    if (path === ADMIN_BASE) return this.renderOverview();\n    const phaseB = renderPhaseBAdminScreen(path, this.navigate);\n    if (phaseB !== null) return phaseB;',
);
main = main.replace(
  '    if (path === `${ADMIN_BASE}/daily-weekly`) return renderDailyWeekly();\n    const phaseB = renderPhaseBAdminScreen(path, this.navigate);\n    if (phaseB !== null) return phaseB;\n    return renderExtendedAdminScreen(path, this.navigate) ?? this.renderUnknown(path);',
  '    if (path === `${ADMIN_BASE}/daily-weekly`) return renderDailyWeekly();\n    return renderExtendedAdminScreen(path, this.navigate) ?? this.renderUnknown(path);',
);
const legacyStart = main.indexOf('  private renderAudio(): HTMLElement {');
const legacyEnd = main.indexOf('  private renderMusicLibrary(): HTMLElement {', legacyStart);
if (legacyStart < 0 || legacyEnd < 0) throw new Error("Missing legacy Audio renderer block");
main = main.slice(0, legacyStart) + main.slice(legacyEnd);
fs.writeFileSync(mainPath, main);

const testsPath = "admin/store.test.mjs";
let tests = fs.readFileSync(testsPath, "utf8");
tests += `

test("B03 default audio profile matches runtime-backed gain fields", () => {
  const config = createDefaultSpaceTypingConfig(contract);
  assert.equal(config.audio.defaults.credit, 1);
  assert.deepEqual(config.audio.defaults.categories, {
    typing: 1,
    combat: 1,
    warnings: 1,
    ui: 1,
    rewards: 1,
  });
});

test("B03 audio draft stays isolated until publish and preserves legacy compatibility", async (t) => {
  const { store, rootDir } = await fixture();
  t.after(() => rm(rootDir, { recursive: true, force: true }));
  const active = await store.getActiveRevision();
  const config = structuredClone(active.config);
  config.audio.defaults.music = 0.2;
  config.audio.defaults.credit = 1.25;
  config.audio.defaults.categories.typing = 0.75;
  const draft = await store.createRevision({ baseRevision: active.revision, config, message: "B03 audio draft" });
  assert.equal((await store.getRuntimeConfig()).audio.defaults.music, 0.26);
  await store.publish({ revision: draft.revision, expectedActiveRevision: active.revision });
  const runtime = await store.getRuntimeConfig();
  assert.equal(runtime.audio.defaults.music, 0.2);
  assert.equal(runtime.audio.defaults.credit, 1.25);
  assert.equal(runtime.audio.defaults.categories.typing, 0.75);

  const legacy = structuredClone(runtime);
  delete legacy.audio.defaults.credit;
  delete legacy.audio.defaults.categories;
  const legacyDraft = await store.createRevision({ baseRevision: draft.revision, config: legacy, message: "Legacy audio compatibility" });
  assert.equal(legacyDraft.config.audio.defaults.credit, undefined);
});

test("B03 audio validation rejects out-of-range gain and category defaults", async (t) => {
  const { store, rootDir } = await fixture();
  t.after(() => rm(rootDir, { recursive: true, force: true }));
  const active = await store.getActiveRevision();
  const badCredit = structuredClone(active.config);
  badCredit.audio.defaults.credit = 2.01;
  await assert.rejects(store.createRevision({ baseRevision: active.revision, config: badCredit }), AdminValidationError);
  const badCategory = structuredClone(active.config);
  badCategory.audio.defaults.categories.combat = 1.01;
  await assert.rejects(store.createRevision({ baseRevision: active.revision, config: badCategory }), AdminValidationError);
  const badMaster = structuredClone(active.config);
  badMaster.audio.defaults.master = -0.01;
  await assert.rejects(store.createRevision({ baseRevision: active.revision, config: badMaster }), AdminValidationError);
});
`;
fs.writeFileSync(testsPath, tests);

const uiValidatorPath = "scripts/validate-space-admin-ui.mjs";
let uiValidator = fs.readFileSync(uiValidatorPath, "utf8");
uiValidator = uiValidator.replace(
  'const worldMusicFile = "portal/src/admin/space-typing-world-music-v2.ts";',
  'const worldMusicFile = "portal/src/admin/space-typing-world-music-v2.ts";\nconst audioPhaseBFile = "portal/src/admin/space-typing-audio-phase-b.ts";',
);
uiValidator = uiValidator.replace(
  'for (const file of [mainFile, extendedFile, worldMusicFile, dailyWeeklyFile, commandFile, iconFile, dialogFile, dialogCssFile, uiCssFile, packageFile]) {',
  'for (const file of [mainFile, extendedFile, worldMusicFile, audioPhaseBFile, dailyWeeklyFile, commandFile, iconFile, dialogFile, dialogCssFile, uiCssFile, packageFile]) {',
);
uiValidator = uiValidator.replace(
  'const worldMusic = read(worldMusicFile);',
  'const worldMusic = read(worldMusicFile);\nconst audioPhaseB = read(audioPhaseBFile);',
);
uiValidator = uiValidator.replace(
  'assert(main.includes(\'control.setAttribute("aria-label", label)\'), "Audio range aria-label is missing");',
  'assert(audioPhaseB.includes(\'input.setAttribute("aria-label", label)\'), "Audio range aria-label is missing");\nassert(audioPhaseB.includes("Existing player settings in spaceTypingSettingsV1 always win"), "Audio default-only player-preference rule is missing");',
);
fs.writeFileSync(uiValidatorPath, uiValidator);

const phaseBValidatorPath = "scripts/validate-space-admin-phase-b.mjs";
let phaseBValidator = fs.readFileSync(phaseBValidatorPath, "utf8");
phaseBValidator = phaseBValidator.replace(
  'const phaseB = await readFile(new URL("portal/src/admin/space-typing-phase-b.ts", root), "utf8");',
  'const phaseB = await readFile(new URL("portal/src/admin/space-typing-phase-b.ts", root), "utf8");\nconst audioPhaseB = await readFile(new URL("portal/src/admin/space-typing-audio-phase-b.ts", root), "utf8");',
);
phaseBValidator = phaseBValidator.replace(
  'const settings = map.screens.find((entry) => entry.route === "/admin/space-typing/settings");',
  'const audio = map.screens.find((entry) => entry.route === "/admin/space-typing/audio");\nconst settings = map.screens.find((entry) => entry.route === "/admin/space-typing/settings");',
);
phaseBValidator = phaseBValidator.replace(
  'assert.equal(settings?.domain, "system");',
  'assert.equal(audio?.domain, "audio");\nassert.equal(audio?.status, "phase-b-ui-wired");\nassert.equal(audio?.applyBoundary, "safe-boundary");\nassert.equal(settings?.domain, "system");',
);
phaseBValidator = phaseBValidator.replace(
  'assert.match(phaseB, /runtime unchanged/);',
  'assert.match(phaseB, /runtime unchanged/);\nassert.match(phaseB, /renderPhaseBAudio/);\nassert.match(audioPhaseB, /Admin Phase B · Audio Defaults draft/);\nassert.match(audioPhaseB, /api\\.createRevision/);\nassert.doesNotMatch(audioPhaseB, /api\\.publish/);\nassert.match(audioPhaseB, /spaceTypingSettingsV1/);\nassert.match(audioPhaseB, /PRONUNCIATION_DUCK/);\nassert.match(audioPhaseB, /assertStableActiveRevision/);',
);
phaseBValidator = phaseBValidator.replace(
  'console.log(`Space Typing Admin Phase B mapping: PASS (${map.screens.length} screens, B01 persistence + B02 revision-backed UI ready).`);',
  'console.log(`Space Typing Admin Phase B mapping: PASS (${map.screens.length} screens, B01-B03 revision-backed domains ready).`);',
);
fs.writeFileSync(phaseBValidatorPath, phaseBValidator);

const mapPath = "admin/space-typing-phase-b-map.v1.json";
const map = JSON.parse(fs.readFileSync(mapPath, "utf8"));
for (const entry of map.screens) {
  if (entry.route === "/admin/space-typing/audio") entry.status = "phase-b-ui-wired";
}
fs.writeFileSync(mapPath, `${JSON.stringify(map, null, 2)}\n`);

const docPath = "portal/src/admin/SPACE_TYPING_PHASE_B_MAPPING.md";
let doc = fs.readFileSync(docPath, "utf8");
doc = doc.replace(
  '3. **B03 — Audio Defaults**: replace local UI state with active/draft revision state while preserving player-preference semantics.',
  '3. **B03 — Audio Defaults**: real revision-backed default profile, child-aligned gains/categories, stale-active protection, and preserved player-preference override semantics. Ducking remains child-owned read-only policy until a validated published-policy consumer exists. **Implemented.**',
);
doc = doc.replace(
  '## Apply boundaries',
  '## B03 — Audio Defaults\n\nThe default profile is aligned with the pinned child runtime `RECOMMENDED_AUDIO`: Master 1.0, Pronunciation 1.0, Music 0.26, Ambient 0.08, Global SFX 0.5, Credit 1.0, Announcer 0.85, plus `typing/combat/warnings/ui/rewards` category preferences at 1.0. Credit supports the child runtime range `0..2`; other persisted preferences use `0..1`.\n\n`spaceTypingSettingsV1` remains the player-owned preference source. Admin Publish only changes the fallback default for players without saved preferences. Existing players are never rewritten. Pronunciation duck calibration is currently hard-coded child mix/focus policy and is displayed read-only rather than falsely persisted.\n\n## Apply boundaries',
);
fs.writeFileSync(docPath, doc);

const ciPath = ".github/workflows/admin-ci.yml";
let ci = fs.readFileSync(ciPath, "utf8");
ci = ci.replace(
  '      - name: Validate Admin Phase B mapping\n        run: node scripts/validate-space-admin-phase-b.mjs',
  '      - name: Validate Admin Phase B mapping\n        run: node scripts/validate-space-admin-phase-b.mjs\n\n      - name: Validate Admin Audio mapping against pinned child\n        run: node scripts/validate-space-admin-audio.mjs',
);
ci = ci.replace(
  '          node --check scripts/validate-space-admin-phase-b.mjs',
  '          node --check scripts/validate-space-admin-phase-b.mjs\n          node --check scripts/validate-space-admin-audio.mjs',
);
fs.writeFileSync(ciPath, ci);
