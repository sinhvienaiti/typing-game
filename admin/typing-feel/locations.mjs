// Where the Typing Feel Admin reads and writes (§3.3, §6.1). The Media V2
// registry (TYPING_GAME_ADMIN_DATA_DIR), the Typing Feel store
// (TYPING_GAME_ADMIN_SHARED_DIR) and the published folder (TYPING_FEEL_PUBLIC_DIR)
// are one set: a revision names Media versions and the export writes their files.
// So they are all defaults or all overridden. A partial override (a test that
// only moves the data dir) leaves Typing Feel switched off instead of letting it
// write the real store or the folder every game reads.
import { resolve } from "node:path";

export const LOCATION_ENV = Object.freeze({
  dataDir: "TYPING_GAME_ADMIN_DATA_DIR",
  sharedDir: "TYPING_GAME_ADMIN_SHARED_DIR",
  publicDir: "TYPING_FEEL_PUBLIC_DIR",
});

export function defaultLocations(root) {
  return {
    dataDir: resolve(root, ".local/admin/space-typing"),
    sharedDir: resolve(root, ".local/admin/shared/typing-feel"),
    publicDir: resolve(root, "typing-feel/public"),
  };
}

/**
 * { available, mode: "default" | "override" | "mismatch", dataDir, sharedDir, publicDir, reason? }.
 * `values` may hold explicit paths (CLI flags); they count as overrides like the env.
 */
export function resolveTypingFeelLocations({ root, env = process.env, values = {} }) {
  const defaults = defaultLocations(root);
  const chosen = {};
  const given = [];
  for (const [key, name] of Object.entries(LOCATION_ENV)) {
    const raw = values[key] ?? env[name];
    if (typeof raw === "string" && raw.trim() !== "") {
      chosen[key] = resolve(root, raw);
      given.push(name);
    } else chosen[key] = defaults[key];
  }
  // An explicit path equal to the default is the default.
  const overridden = Object.keys(LOCATION_ENV).filter((key) => chosen[key] !== defaults[key]);
  if (overridden.length === 0) return { available: true, mode: "default", ...chosen };
  if (overridden.length === Object.keys(LOCATION_ENV).length) return { available: true, mode: "override", ...chosen };
  const names = Object.values(LOCATION_ENV);
  return {
    available: false,
    mode: "mismatch",
    ...chosen,
    reason: `Typing Feel is off: set ${names.join(", ")} together or none of them (given: ${given.join(", ") || "none"}). They are one set: the store names Media V2 versions and the export writes their files.`,
  };
}
