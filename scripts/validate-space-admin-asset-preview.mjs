import { readFile } from "node:fs/promises";

const bridgePath = "portal/src/admin/space-typing-asset-preview.ts";
const shipsPath = "portal/src/admin/space-typing-ships-phase-b.ts";
const studioPath = "portal/src/admin/v2/asset-tuning-studio.ts";
const studioCssPath = "portal/src/admin/v2/asset-tuning-studio.css";

const [bridge, ships, studio, studioCss] = await Promise.all([
  readFile(new URL(`../${bridgePath}`, import.meta.url), "utf8"),
  readFile(new URL(`../${shipsPath}`, import.meta.url), "utf8"),
  readFile(new URL(`../${studioPath}`, import.meta.url), "utf8"),
  readFile(new URL(`../${studioCssPath}`, import.meta.url), "utf8"),
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

requireText(studio, 'export function createAssetTuningStudio', "A5.1 exposes a shared Studio shell");
requireText(studio, 'element("section", "st-admin-asset-studio")', "Studio shell owns shared layout chrome");
requireText(studio, 'element("details", "st-admin-asset-studio-advanced")', "Studio provides Basic/Advanced disclosure");
requireText(studio, 'export function createAssetTuningScalarControl', "Studio exposes canonical scalar primitive");
requireText(studio, 'slider.type = "range"', "scalar primitive includes keyboard-capable slider");
requireText(studio, 'number.type = "number"', "scalar primitive includes numeric alternative");
requireText(studio, 'commit(options.defaultValue)', "Reset comes from domain/profile default");
requireText(studio, 'openAdminMediaAssetPicker', "Studio reuses the existing immutable-version Asset Picker");
requireText(studio, 'A domain should render', "Asset Picker remains capability-gated by the owning domain");
requireText(studio, 'export function createAssetTuningCapabilityState', "unsupported/migration capability state is explicit");
requireText(studioCss, 'grid-template-columns: minmax(340px, 420px) minmax(0, 1fr)', "preview receives dominant flexible width");
requireText(studioCss, '.st-admin-asset-studio-lifecycle', "Studio exposes lifecycle bar integration");

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
requireText(ships, 'createAssetTuningStudio({', "Ships adopts the shared A5.1 Studio shell");
requireText(ships, 'createAssetTuningScalarControl(helpScope', "Ships uses shared slider + numeric + reset primitive");
requireText(ships, 'defaultValue: baseline.visual.wingSpan', "Wing Span reset uses canonical bundled default");
requireText(ships, 'defaultValue: baseline.visual.bodyLength', "Body Length reset uses canonical bundled default");
requireText(ships, 'status: "REQUIRES CANONICAL MIGRATION"', "migration-required features remain capability state");
requireText(ships, 'status: "READ-ONLY REFERENCE"', "read-only features remain capability state");
requireText(ships, 'status: "DEFERRED / UNSUPPORTED"', "unsupported features remain capability state");
requireText(ships, 'studio.lifecycleHost.append(saveBar)', "existing Save Draft lifecycle is integrated into Studio");
requireText(ships, 'Save Draft', "existing revision lifecycle remains present");
requireText(ships, 'Published preview still reflects active', "saving Draft does not relabel it as Published");
forbidText(ships, 'publishedPreview = validated', "Draft validation must not overwrite Published preview");
forbidText(ships, 'publishedPreview = validatedDraft', "Draft validation must remain ephemeral");
forbidText(ships, 'panel("Visual Profile"', "Ships no longer duplicates Asset Tuning settings in a legacy panel");

console.log("Space Typing Admin A5 preview + A5.1 Studio validation passed.");
