// Typing Feel pages of the All games area (docs/games/TYPING_FEEL_SERVICE.md §3.2).
// No imports: scripts/validate-admin-shared-ia.mjs runs this file for real.

export const TYPING_FEEL_ROUTES = {
  keyboardSounds: "/admin/shared/keyboard-sounds",
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
} as const;
