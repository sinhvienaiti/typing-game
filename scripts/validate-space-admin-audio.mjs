import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { createDefaultSpaceTypingConfig } from "../admin/default-config.mjs";

const [childMain, childTypes, childMix, childSfx, uiSource, contract] = await Promise.all([
  readFile("games/space-typing/src/main.ts", "utf8"),
  readFile("games/space-typing/src/types.ts", "utf8"),
  readFile("games/space-typing/src/audio/mix.ts", "utf8"),
  readFile("games/space-typing/src/audio/Sfx.ts", "utf8"),
  readFile("portal/src/admin/space-typing-audio-phase-b.ts", "utf8"),
  readFile("games/space-typing/contracts/space-typing-admin.v1.json", "utf8").then(JSON.parse),
]);
const config = createDefaultSpaceTypingConfig(contract);

// Current pinned child player-preference ownership. These defaults still exist in GameSettings.
assert.match(childTypes, /sfxVolume:\s*number/);
assert.match(childTypes, /creditVolume\?:\s*number/);
assert.match(childTypes, /musicVolume:\s*number/);
assert.match(childTypes, /ambientVolume:\s*number/);
assert.match(childTypes, /pronunciationVolume:\s*number/);
assert.match(childMain, /const defaultSettings: GameSettings = \{[\s\S]*?sfxVolume:\s*0\.5,[\s\S]*?creditVolume:\s*1,[\s\S]*?musicVolume:\s*0\.26,[\s\S]*?ambientVolume:\s*0\.08,[\s\S]*?pronunciationVolume:\s*1,/);
assert.match(childMain, /const SETTINGS_KEY = "spaceTypingSettingsV1"/);
assert.match(childMain, /if \(raw === null\) return \{ \.\.\.defaultSettings \}/);
assert.match(childMain, /localStorage\.setItem\(SETTINGS_KEY, JSON\.stringify\(settings\)\)/);

// Removed player preferences must not silently reappear as fake Admin-authorable runtime fields.
for (const removed of ["masterVolume", "announcerVolume", "audioCategoryVolumes"]) {
  assert.doesNotMatch(childTypes, new RegExp(`\\b${removed}\\??:`), `${removed} unexpectedly reappeared in current GameSettings; re-audit Audio ownership.`);
}
assert.doesNotMatch(childMain, /sanitizeAudioCategoryVolumes\(parsed\.audioCategoryVolumes\)/);

// Canonical child mix/focus ownership remains code-owned.
assert.match(childMix, /export const AUDIO_GROUPS = \[[\s\S]*?"typing"[\s\S]*?"combat"[\s\S]*?"warnings"[\s\S]*?"ui"[\s\S]*?"rewards"/);
for (const [group, gain] of Object.entries({ typing: "0.82", combat: "0.72", warnings: "0.9", ui: "0.62", rewards: "0.86" })) {
  assert.match(childMix, new RegExp(`${group}:\\s*${gain.replace(".", "\\.")}`), `Current base gain missing for ${group}`);
}
for (const [group, duck] of Object.entries({ typing: "0.32", combat: "0.38", warnings: "0.68", ui: "0.45", rewards: "0.7" })) {
  assert.match(childMix, new RegExp(`${group}:\\s*${duck.replace(".", "\\.")}`), `Pronunciation duck missing for ${group}`);
}
assert.match(childMix, /export const PRONUNCIATION_DUCK/);
assert.match(childMix, /return safeMaster \* AUDIO_GROUP_GAIN\[group\] \* safeEvent \* duck/);

// SFX and announcer ownership moved into Sfx: SFX/Credit keep shipped defaults; announcer is derived from warning mix.
assert.match(childSfx, /private volume = 0\.5/);
assert.match(childSfx, /private creditVolume = 1/);
assert.match(childSfx, /private announcerVolume\(\): number/);
assert.match(childSfx, /mixedSfxGain\([\s\S]*?this\.volume,[\s\S]*?"warnings",[\s\S]*?1,[\s\S]*?this\.pronunciationActive,[\s\S]*?\) \* 1\.08/);

// Parent UI must expose only current child-backed player defaults as authorable controls.
for (const supported of ["Pronunciation", "Music", "Ambient", "Global SFX", "Credits / Crystal pickup"]) {
  assert.match(uiSource, new RegExp(`slider\\("${supported.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")}"`), `Missing current child-backed Audio control: ${supported}`);
}
assert.doesNotMatch(uiSource, /slider\("Master"/);
assert.doesNotMatch(uiSource, /slider\("Announcer"/);
assert.doesNotMatch(uiSource, /categorySliders/);
assert.match(uiSource, /Pinned child no longer exposes masterVolume, announcerVolume, or audioCategoryVolumes as player settings/);
assert.match(uiSource, /Legacy revision keys are preserved for schema compatibility but are not authorable here/);
assert.match(uiSource, /master:\s*compatibilityDefaults\.master/);
assert.match(uiSource, /announcer:\s*compatibilityDefaults\.announcer/);
assert.match(uiSource, /categories:\s*\{ \.\.\.compatibilityDefaults\.categories \}/);
assert.match(uiSource, /src\/audio\/mix\.ts/);

// Existing revision schema is retained for backward compatibility while authoring is constrained to real child fields.
assert.equal(config.audio.profileId, "recommended-v1");
assert.deepEqual(config.audio.defaults, {
  master: 1,
  pronunciation: 1,
  music: 0.26,
  ambient: 0.08,
  sfx: 0.5,
  credit: 1,
  announcer: 0.85,
  categories: {
    typing: 1,
    combat: 1,
    warnings: 1,
    ui: 1,
    rewards: 1,
  },
});

assert.ok(contract.capabilities.includes("audio.mix.read"));
assert.ok(contract.capabilities.includes("audio.mix.write"));
assert.equal(contract.applyBoundaries.mixPolicy, "safe-boundary");

console.log("Space Typing Admin Audio mapping: PASS (current child-backed player defaults authorable; removed master/announcer/category preferences preserved read-only; code-owned mix/focus policy verified against pinned child).");
