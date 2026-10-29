// Ticket 190: the root ticket-189 catalogue, mounted read-only by Vite.
/** Override with ?keysBase=/another-mounted-folder/ (or an HTTP base with suitable CORS). */
export const KEYS_BASE = new URLSearchParams(window.location.search).get("keysBase") ?? "/lab-keys/";
