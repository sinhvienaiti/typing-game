// Typing Feel pages of the All games area (docs/games/TYPING_FEEL_SERVICE.md §3.2).
// No imports: scripts/validate-admin-shared-ia.mjs runs this file for real.

export const TYPING_FEEL_ROUTES = {
  keyboardSounds: "/admin/shared/keyboard-sounds",
  addSoundSet: "/admin/shared/keyboard-sounds/new",
  typingEffects: "/admin/shared/typing-effects",
  release: "/admin/shared/release",
} as const;

/**
 * The permission each Typing Feel button carries in data-admin-permission (§3.13).
 * Editing only changes the local working copy, but it is useless without config.draft,
 * so edit controls carry it too. Publish and Rollback need shared.publish:
 * Space's config.publish / config.rollback are not enough to change every game.
 */
export const TYPING_FEEL_PERMISSIONS = {
  edit: "config.draft",
  saveDraft: "config.draft",
  publish: "shared.publish",
  rollback: "shared.publish",
  // Add sound set (G7): the WAV goes up through Media V2 (media.upload); the upload
  // check, Format, Accept and Discard need shared.publish (admin/typing-feel/http.mjs JOB_PERMISSIONS).
  upload: "media.upload",
  format: "shared.publish",
  accept: "shared.publish",
  discard: "shared.publish",
} as const;
