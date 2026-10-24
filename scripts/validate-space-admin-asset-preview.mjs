import { readFile } from "node:fs/promises";

const paths = {
  facade: "portal/src/admin/space-typing-asset-preview.ts",
  bridge: "portal/src/admin/v2/preview/production-preview-bridge.ts",
  contract: "portal/src/admin/v2/preview/preview-contract.ts",
  studio: "portal/src/admin/v2/preview/production-preview-studio.ts",
  shipAdapter: "portal/src/admin/v2/preview/adapters/ships.ts",
  ships: "portal/src/admin/space-typing-ships-phase-b.ts",
  tuningStudio: "portal/src/admin/v2/asset-tuning-studio.ts",
  tuningCss: "portal/src/admin/v2/asset-tuning-studio.css",
  childPolicy: "games/space-typing/src/admin/ship-runtime-policy.ts",
  childProjectiles: "games/space-typing/src/characters/projectiles.ts",
  childShots: "games/space-typing/src/vfx/player-shots.ts",
  childPreview: "games/space-typing/src/admin/asset-preview-main.ts",
  childSfx: "games/space-typing/src/audio/Sfx.ts",
};

const source = Object.fromEntries(await Promise.all(
  Object.entries(paths).map(async ([key, path]) => [
    key,
    await readFile(new URL(`../${path}`, import.meta.url), "utf8"),
  ]),
));

function requireText(input, needle, label) {
  if (!input.includes(needle)) throw new Error(`${label}: expected ${JSON.stringify(needle)}`);
}

function forbidText(input, needle, label) {
  if (input.includes(needle)) throw new Error(`${label}: forbidden ${JSON.stringify(needle)}`);
}

requireText(source.contract, 'ProductionPreviewLifecycle = "loading" | "ready" | "error" | "unsupported"', "shared lifecycle contract is explicit");
requireText(source.contract, "ProductionPreviewDomainAdapter", "shared domain adapter contract exists");
requireText(source.bridge, 'const ASSET_PREVIEW_PROTOCOL_VERSION = 1 as const', "protocol remains versioned");
requireText(source.bridge, 'const PREVIEW_ENTRY_PATH = "/admin-preview.html"', "production preview route remains fixed");
requireText(source.bridge, 'game.id === "space-typing"', "target resolves through canonical game registry");
requireText(source.bridge, 'crypto.getRandomValues(bytes)', "session tokens use CSPRNG");
requireText(source.bridge, 'event.origin !== this.origin', "bridge checks exact child origin");
requireText(source.bridge, 'event.source !== this.iframe.contentWindow', "bridge checks exact child window");
requireText(source.bridge, 'this.iframe.setAttribute("sandbox", "allow-scripts allow-same-origin")', "iframe sandbox remains explicit");
requireText(source.bridge, 'this.iframe.referrerPolicy = "strict-origin"', "child receives only exact parent-origin referrer");
requireText(source.bridge, 'url.searchParams.set("previewSession", this.previewSessionId)', "session id reaches controlled route");
requireText(source.bridge, 'url.searchParams.set("nonce", this.nonce)', "nonce reaches controlled route");
requireText(source.bridge, 'private nextRequestId = 1', "request ids remain monotonic");
requireText(source.bridge, 'type === "DISPOSE" ? "DISPOSED" : "APPLIED"', "command response type remains fail-closed");
requireText(source.bridge, 'window.requestAnimationFrame(() =>', "candidate updates remain frame-coalesced");
requireText(source.bridge, 'window.cancelAnimationFrame(this.queuedFrame)', "queued frame is cancelled during teardown");
requireText(source.bridge, 'window.removeEventListener("message", this.onMessage)', "message listener is removed on teardown");
requireText(source.bridge, 'this.pending.clear()', "pending command registry is cleared");
requireText(source.bridge, 'this.iframe.remove()', "isolated iframe is removed");
requireText(source.bridge, 'candidateGeneration', "stale async generation guard is shared");
requireText(source.bridge, 'ProductionPreviewStaleError', "superseded async work is explicit");
requireText(source.bridge, 'async replay()', "shared bridge exposes replay");
requireText(source.bridge, 'async reset()', "shared bridge exposes reset");
forbidText(source.bridge, "ADMIN_TOKEN", "preview must not receive Admin credentials");
forbidText(source.bridge, "Authorization", "preview must not receive Authorization headers");
forbidText(source.bridge, "Math.random", "security tokens must not use Math.random");

requireText(source.studio, "createProductionPreviewStudio", "shared production preview studio exists");
requireText(source.studio, '"Reset"', "studio exposes reset");
requireText(source.studio, '"Replay"', "studio exposes replay");
requireText(source.studio, '"Fullscreen"', "studio exposes fullscreen when browser supports it");
requireText(source.studio, '"Fullscreen preview is not supported by this browser."', "fullscreen fails soft as unsupported");
requireText(source.studio, "lifecycleTone", "studio maps lifecycle states to administrator status tones");

requireText(source.facade, "ProductionPreviewBridge.mount(host, shipProductionPreviewAdapter)", "Ships facade delegates to shared ProductionPreviewBridge");
requireText(source.facade, "const operation = this.bridge.loadCandidate(candidate)", "Ship load delegates to shared candidate transport");
requireText(source.facade, "this.latestCandidate = operation", "Ship facade tracks the authoritative candidate operation");
requireText(source.facade, "return operation", "Ship load returns the shared candidate transport promise");
requireText(source.facade, "await this.latestCandidate", "Ship scenario/tuning/replay ordering waits for candidate materialization");
requireText(source.facade, "return this.bridge.replay()", "Ships inherits shared replay lifecycle");
requireText(source.shipAdapter, 'domain: "ship"', "Ship adapter identifies the child production domain");
requireText(source.shipAdapter, 'defaultScenario: "idle"', "Ship adapter owns production default scenario");
requireText(source.shipAdapter, 'imageAssetVersionId?: string', "Ship candidate keeps exact image version");
requireText(source.shipAdapter, 'reliefAssetVersionId?: string | null', "Ship candidate keeps exact relief bundle version");
requireText(source.shipAdapter, 'projectileArchetype?: string', "Ship candidate keeps production projectile recipe");
requireText(source.shipAdapter, 'imageAssetVersionId: candidate.imageAssetVersionId', "adapter forwards exact Ship image version");
requireText(source.shipAdapter, 'reliefAssetVersionId: candidate.reliefAssetVersionId', "adapter forwards exact relief bundle version");
requireText(source.shipAdapter, 'projectileArchetype: candidate.projectileArchetype', "adapter forwards projectile recipe");
requireText(source.shipAdapter, 'tuningPayload: (visual: Readonly<Record<string, unknown>>) => Object.freeze({ visual })', "Ship tuning remains an explicitly typed domain adapter operation");

requireText(source.tuningStudio, 'export function createAssetTuningStudio', "A5.1 shared Studio shell remains available");
requireText(source.tuningStudio, 'element("details", "st-admin-asset-studio-advanced")', "technical/advanced controls remain progressively disclosed");
requireText(source.tuningStudio, 'export function createAssetTuningScalarControl', "canonical scalar primitive remains shared");
requireText(source.tuningStudio, 'slider.type = "range"', "scalar primitive keeps keyboard-capable slider");
requireText(source.tuningStudio, 'number.type = "number"', "scalar primitive keeps numeric alternative");
requireText(source.tuningStudio, 'commit(options.defaultValue)', "reset remains domain/profile-default based");
requireText(source.tuningStudio, 'openAdminMediaAssetPicker', "immutable Media V2 picker remains reused");
requireText(source.tuningCss, 'grid-template-columns: minmax(340px, 420px) minmax(0, 1fr)', "production preview remains visually dominant");
requireText(source.ships, '"Draft"', "Ships exposes Draft source");
requireText(source.ships, '"Published"', "Ships exposes Published source");
requireText(source.ships, '"Idle"', "Ships exposes Idle scenario");
requireText(source.ships, '"Move"', "Ships exposes Move scenario");
requireText(source.ships, '"Fire"', "Ships exposes Fire scenario");
requireText(source.ships, 'let publishedPreview: ShipAdminPreview | null = null', "Published data remains separate from Draft");
requireText(source.ships, 'previewSource === "published"', "Published source is selected explicitly");
requireText(source.ships, 'SpaceTypingAssetPreviewBridge.mount(previewHost)', "Ships still mounts isolated child production preview");
requireText(source.ships, 'imageAssetVersionId: ship.imageAssetVersionId', "Ships sends exact image version");
requireText(source.ships, 'reliefAssetVersionId: ship.reliefAssetVersionId ?? null', "Ships sends exact relief bundle version");
requireText(source.ships, 'projectileArchetypeFor(ship)', "Ships resolves canonical projectile recipe");
requireText(source.ships, 'bridge.setScenario(previewScenario)', "scenario uses production preview protocol");
requireText(source.ships, 'previewBridge?.disposeImmediately()', "route teardown disposes preview");
requireText(source.ships, 'openAdminMediaAssetPicker({', "Ship media still uses canonical Asset Picker");
requireText(source.ships, 'allowedKinds: ["image"]', "Ship image picker remains image-only");
requireText(source.ships, 'allowedKinds: ["model"]', "Ship relief picker remains model-only");
requireText(source.ships, 'isVersionCompatible: isSpaceTypingReliefMediaVersionCompatible', "strict relief compatibility remains enforced");
requireText(source.ships, 'studio.lifecycleHost.append(saveBar)', "Save Draft lifecycle remains integrated");
forbidText(source.ships, 'publishedPreview = validated', "Draft validation must not overwrite Published preview");
forbidText(source.ships, 'publishedPreview = validatedDraft', "Draft validation remains ephemeral");

requireText(source.childPolicy, 'reliefAssetVersionId?: string', "child canonical Ship policy persists relief version");
requireText(source.childPolicy, 'isShipReliefAssetVersionId', "child validator rejects non-canonical relief assignments");
requireText(source.childPolicy, 'projectileArchetype?: ShipRuntimeProjectileArchetype', "child policy persists projectile recipe");
requireText(source.childPolicy, 'PROJECTILE_ARCHETYPES.has', "child validator rejects unknown projectile recipes");
requireText(source.childProjectiles, 'withPlayerProjectileRuntimeSession', "child supports isolated projectile runtime sessions");
requireText(source.childProjectiles, 'session.ships[id]?.projectileArchetype', "production projectile profile consumes Ship policy binding");
requireText(source.childShots, 'export function shotRecipeFor', "child exposes production shot recipe resolver");
requireText(source.childShots, 'playerProjectileProfile(characterId).archetype', "production shot recipe derives from canonical profile");
requireText(source.childPreview, 'const shots = new PlayerShotSystem<number>()', "preview owns real production PlayerShotSystem");
requireText(source.childPreview, 'const sfx = new Sfx()', "preview owns real production Sfx");
requireText(source.childPreview, 'shots.fire({', "Fire scenario uses production projectile path");
requireText(source.childPreview, 'withShipAssetPreviewRuntime(activeCandidate', "preview scopes runtime to ephemeral candidate");
requireText(source.childPreview, 'prepareShipAssetPreviewCandidate(', "preview prepares candidate-owned exact media");
requireText(source.childPreview, 'releaseShipAssetPreviewCandidate(', "preview releases superseded/disposed candidate resources");
requireText(source.childSfx, 'boltImpact(power = 1, pan = 0, variant: ImpactVariant = "crystal"): void', "production Sfx keeps typed impact variants");
forbidText(source.childPolicy, 'projectileUrl', "child policy must not accept arbitrary projectile URLs");
forbidText(source.childPolicy, 'projectilePath', "child policy must not accept arbitrary projectile filesystem paths");
forbidText(source.childPolicy, 'impactSfxAssetVersionId', "independent impact binding must not drift from recipe");
forbidText(source.childPolicy, 'launchSfxAssetVersionId', "generic launch cue must not become fake per-Ship authoring");

console.log("Space Typing Admin A10.5 shared production preview foundation + retained A5 invariants validation passed.");
