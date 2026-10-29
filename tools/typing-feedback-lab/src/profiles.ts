// Keyboard sound profiles in the Lab (owner 29/10): every keypress sound is made in the Audio Lab, no
// downloaded packs. The five profiles load from the audio lane's staging folder
// (~/AudioLab/review/staging/keys/<id>/keys-manifest.json, served at /lab-keys/); until a profile is
// staged it shows as pending and stays silent. The kit synth is a labelled test sound, Lab only.
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
  pending: "Pending: the Audio Lab has not staged this profile yet. Silent until it does.",
  partial: "Staged in part: plays the files it has.",
  ready: "Audio Lab files, staged for review.",
  "synth-test": "Code-made test sound from the kit. Lab only, never in a game.",
  off: "No keyboard sound.",
};
