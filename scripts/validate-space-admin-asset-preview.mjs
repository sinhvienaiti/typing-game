import { readFile } from "node:fs/promises";

const bridgePath = "portal/src/admin/space-typing-asset-preview.ts";
const shipsPath = "portal/src/admin/space-typing-ships-phase-b.ts";

const [bridge, ships] = await Promise.all([
  readFile(new URL(`../${bridgePath}`, import.meta.url), "utf8"),
  readFile(new URL(`../${shipsPath}`, import.meta.url), "utf8"),
]);

function requireText(source, needle, label) {
  if (!source.includes(needle)) {
    throw new Error(`${label}: expected ${JSON.stringify(needle)}`);
  }
}

function forbidText(source, needle, label) {
  if (source.includes(needle)) {
    throw new Error(`${label}: forbidden ${JSON.stringify(needle)}`);
  }
}

requireText(bridge, 'const ASSET_PREVIEW_PROTOCOL_VERSION = 1 as const', "protocol is versioned");
requireText(bridge, 'const PREVIEW_ENTRY_PATH = "/admin-preview.html"', "preview route is fixed");
requireText(bridge, 'game.id === "space-typing"', "target resolves through canonical game registry");
requireText(bridge, 'crypto.getRandomValues(bytes)', "session tokens use CSPRNG");
requireText(bridge, 'event.origin !== this.origin', "bridge checks exact child origin");
requireText(bridge, 'event.source !== this.iframe.contentWindow', "bridge checks exact child window");
requireText(bridge, 'this.iframe.setAttribute("sandbox", "allow-scripts allow-same-origin")', "iframe sandbox is explicit");
requireText(bridge, 'this.iframe.referrerPolicy = "strict-origin"', "child receives only exact parent origin referrer");
requireText(bridge, 'url.searchParams.set("previewSession", this.previewSessionId)', "session id is carried to controlled route");
requireText(bridge, 'url.searchParams.set("nonce", this.nonce)', "nonce is carried to controlled route");
requireText(bridge, 'private nextRequestId = 1', "request ids are monotonic");
requireText(bridge, 'type === "DISPOSE" ? "DISPOSED" : "APPLIED"', "command responses fail closed by type");
requireText(bridge, 'window.requestAnimationFrame(() =>', "high-frequency Ship candidate updates are frame-coalesced");
requireText(bridge, 'window.cancelAnimationFrame(this.queuedShipFrame)', "queued frame is cancelled on teardown");
requireText(bridge, 'window.removeEventListener("message", this.onMessage)', "bridge removes message listener");
requireText(bridge, 'this.pending.clear()', "bridge clears pending requests");
requireText(bridge, 'this.iframe.remove()', "bridge removes iframe");
forbidText(bridge, "ADMIN_TOKEN", "preview must not receive Admin credentials");
forbidText(bridge, "Authorization", "preview must not receive Authorization header/token");
forbidText(bridge, "Math.random", "preview security tokens must not use Math.random");

requireText(ships, '"Draft"', "Ships preview exposes Draft source");
requireText(ships, '"Published"', "Ships preview exposes Published source");
requireText(ships, '"Idle"', "Ships preview exposes Idle scenario");
requireText(ships, '"Move"', "Ships preview exposes Move scenario");
requireText(ships, '"Fire"', "Ships preview exposes Fire scenario");
requireText(ships, 'let publishedPreview: ShipAdminPreview | null = null', "Published source is tracked separately");
requireText(ships, 'previewSource === "published"', "source switch selects published data explicitly");
requireText(ships, 'SpaceTypingAssetPreviewBridge.mount(previewHost)', "Ships page uses child-owned preview harness");
requireText(ships, 'bridge.loadShip({ characterId: ship.id, visual: previewVisual(ship) })', "candidate is sent as typed Ship visual data");
requireText(ships, 'bridge.setScenario(previewScenario)', "scenario uses preview protocol");
requireText(ships, 'previewBridge?.disposeImmediately()', "route lifecycle tears down preview bridge");
requireText(ships, 'Save Draft', "existing revision lifecycle remains present");
requireText(ships, 'Published preview still reflects active', "saving Draft does not relabel it as Published");
forbidText(ships, 'publishedPreview = validated', "Draft validation must not overwrite Published preview");
forbidText(ships, 'publishedPreview = validatedDraft', "Draft validation must remain ephemeral");

console.log("Space Typing Admin A5 preview transport validation passed.");
