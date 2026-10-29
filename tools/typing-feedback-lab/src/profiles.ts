// Keyboard sound profiles in the Lab (owner 29/10, Codex ticket 182: Creamy Linear, Deep Thock, Marbly,
// Clean Clack, Soft Dome). /lab-keys/ serves Codex's output (<repo>/tmp/keys-codex/<id>/keys-manifest.json)
// once that folder exists, else the Audio Lab staging folder (~/AudioLab/review/staging/keys); LAB_KEYS
// overrides both. Until a profile is there it shows as pending and stays silent. The kit synth is a
// labelled test sound, Lab only.
import { KEYBOARD_PROFILES, type TypingSoundProfile } from "../../../shared/game-kit/feedback/typing-fx";

/** Where the game would give its own base URL; the Lab's is the staging mount. */
export const KEYS_BASE = "/lab-keys/";

export const LAB_KEYBOARDS = KEYBOARD_PROFILES;

export const SYNTH_TEST: TypingSoundProfile = {
  id: "synth-test",
  name: "Kit synth (test only)",
  source: "synth",
  licence: "project-owned (kit AudioCues)",
  files: {},
};

export const PROFILE_NOTES: Readonly<Record<string, string>> = {
  pending: "Pending: no files for this profile yet (Codex ticket 182). Silent until they arrive.",
  partial: "Staged in part: plays the files it has.",
  ready: "Audio Lab files, staged for review.",
  "synth-test": "Code-made test sound from the kit. Lab only, never in a game.",
  off: "No keyboard sound.",
};
