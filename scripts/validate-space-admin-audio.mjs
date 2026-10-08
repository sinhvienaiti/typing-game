import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { createDefaultSpaceTypingConfig } from "../admin/default-config.mjs";

const childSettings = await readFile("games/space-typing/src/audio/player-settings.ts", "utf8");
const childMix = await readFile("games/space-typing/src/audio/mix.ts", "utf8");
const childMain = await readFile("games/space-typing/src/main.ts", "utf8");
const contract = JSON.parse(await readFile("games/space-typing/contracts/space-typing-admin.v1.json", "utf8"));
const config = createDefaultSpaceTypingConfig(contract);

assert.match(childSettings, /RECOMMENDED_AUDIO/);
assert.match(childSettings, /masterVolume:\s*1/);
assert.match(childSettings, /pronunciationVolume:\s*1/);
assert.match(childSettings, /musicVolume:\s*0\.26/);
assert.match(childSettings, /ambientVolume:\s*0\.08/);
assert.match(childSettings, /sfxVolume:\s*0\.5/);
assert.match(childSettings, /creditVolume:\s*1/);
assert.match(childSettings, /announcerVolume:\s*0\.85/);
for (const group of ["typing", "combat", "warnings", "ui", "rewards"]) {
  assert.match(childSettings, new RegExp(`${group}:\\s*1`));
  assert.match(childMix, new RegExp(`${group}:\\s*0\\.`));
}
assert.match(childMix, /PRONUNCIATION_DUCK/);
assert.match(childMain, /const SETTINGS_KEY = "spaceTypingSettingsV1"/);
assert.match(childMain, /if \(raw === null\) return \{ \.\.\.defaultSettings \}/);
assert.match(childMain, /sanitizeAudioCategoryVolumes\(parsed\.audioCategoryVolumes\)/);

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

console.log("Space Typing Admin Audio mapping: PASS (recommended defaults + player-preference override + focus-policy ownership verified against pinned child).");
