// Keyboard sound profiles in the Lab: creamy (Creamy Linear), thock (Deep Thock), marbly, clack (Clean
// Clack), dome (Soft Dome). Keyboard-sound work is paused (owner 29/10: he sources the sounds himself), so
// no folder is wired and every profile shows as pending and stays silent. /lab-keys/ is mounted only when
// LAB_KEYS names a folder of <id>/keys-manifest.json. The kit synth is a labelled test sound, Lab only.
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
  pending: "Pending: keyboard sounds are paused until the owner picks them. Silent.",
  partial: "Staged in part: plays the files it has.",
  ready: "Audio Lab files, staged for review.",
  "synth-test": "Code-made test sound from the kit. Lab only, never in a game.",
  off: "No keyboard sound.",
};
