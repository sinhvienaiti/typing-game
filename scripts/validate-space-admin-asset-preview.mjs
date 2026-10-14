import { readFile } from "node:fs/promises";

const bridgePath = "portal/src/admin/space-typing-asset-preview.ts";
const shipsPath = "portal/src/admin/space-typing-ships-phase-b.ts";
const studioPath = "portal/src/admin/v2/asset-tuning-studio.ts";
const studioCssPath = "portal/src/admin/v2/asset-tuning-studio.css";
const childPolicyPath = "games/space-typing/src/admin/ship-runtime-policy.ts";
const childProjectilesPath = "games/space-typing/src/characters/projectiles.ts";
const childShotsPath = "games/space-typing/src/vfx/player-shots.ts";
const childPreviewPath = "games/space-typing/src/admin/asset-preview-main.ts";
const childSfxPath = "games/space-typing/src/audio/Sfx.ts";

const [bridge, ships, studio, studioCss, childPolicy, childProjectiles, childShots, childPreview, childSfx] = await Promise.all([
  readFile(new URL(`../${bridgePath}`, import.meta.url), "utf8"),
  readFile(new URL(`../${shipsPath}`, import.meta.url), "utf8"),
  readFile(new URL(`../${studioPath}`, import.meta.url), "utf8"),
  readFile(new URL(`../${studioCssPath}`, import.meta.url), "utf8"),
  readFile(new URL(`../${childPolicyPath}`, import.meta.url), "utf8"),
  readFile(new URL(`../${childProjectilesPath}`, import.meta.url), "utf8"),
  readFile(new URL(`../${childShotsPath}`, import.meta.url), "utf8"),
  readFile(new URL(`../${childPreviewPath}`, import.meta.url), "utf8"),
  readFile(new URL(`../${childSfxPath}`, import.meta.url), "utf8"),
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
requireText(bridge, 'imageAssetVersionId?: string', "Ship preview candidate carries optional exact image version");
requireText(bridge, 'imageAssetVersionId: nextCandidate.imageAssetVersionId', "bridge forwards exact Ship image version to child preview");
requireText(bridge, 'reliefAssetVersionId?: string | null', "A5.4 Ship preview candidate carries optional exact relief bundle version");
requireText(bridge, 'reliefAssetVersionId: nextCandidate.reliefAssetVersionId', "A5.4 bridge forwards exact Ship relief bundle version to child preview");
requireText(bridge, 'projectileArchetype?: string', "Ship preview candidate carries optional production projectile recipe");
requireText(bridge, 'projectileArchetype: nextCandidate.projectileArchetype', "bridge forwards Ship projectile recipe to child preview");
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
requireText(ships, 'imageAssetVersionId: ship.imageAssetVersionId', "candidate sends exact Ship image version through typed preview bridge");
requireText(ships, 'reliefAssetVersionId: ship.reliefAssetVersionId ?? null', "A5.4 candidate sends exact Ship relief bundle version through typed preview bridge");
requireText(ships, 'projectileArchetypeFor(ship)', "candidate resolves canonical Ship projectile recipe");
requireText(ships, '{ projectileArchetype }', "candidate sends Ship projectile recipe through preview bridge");
requireText(ships, 'bridge.setScenario(previewScenario)', "scenario uses preview protocol");
requireText(ships, 'previewBridge?.disposeImmediately()', "route lifecycle tears down preview bridge");
requireText(ships, 'createAssetTuningStudio({', "Ships adopts the shared A5.1 Studio shell");
requireText(ships, 'createAssetTuningScalarControl(helpScope', "Ships uses shared slider + numeric + reset primitive");
requireText(ships, 'defaultValue: baseline.visual.wingSpan', "Wing Span reset uses canonical bundled default");
requireText(ships, 'defaultValue: baseline.visual.bodyLength', "Body Length reset uses canonical bundled default");
requireText(ships, 'openAdminMediaAssetPicker({', "Ship Image reuses the canonical Media V2 Asset Picker");
requireText(ships, 'allowedKinds: ["image"]', "Ship picker is constrained to image assets");
requireText(ships, 'selectedAssetVersionId: ship.imageAssetVersionId ?? null', "picker restores the current exact image version");
requireText(ships, 'overrideFor(selectedId).imageAssetVersionId = version.assetVersionId', "selection persists immutable version id into draft policy");
requireText(ships, 'delete override.imageAssetVersionId', "Clear removes only the image override");
requireText(ships, 'label: "Ship Image"', "Ship image control uses standard Admin field shell");
requireText(ships, 'title: "Ship Image"', "Ship image guidance uses tooltip help instead of permanent long copy");
requireText(ships, 'allowedKinds: ["model"]', "A5.4 relief picker is constrained to model assets");
requireText(ships, 'isVersionCompatible: isSpaceTypingReliefMediaVersionCompatible', "A5.4 relief picker enforces strict bundle compatibility");
requireText(ships, 'selectedAssetVersionId: ship.reliefAssetVersionId ?? null', "A5.4 relief picker restores the current exact bundle version");
requireText(ships, 'overrideFor(selectedId).reliefAssetVersionId = version.assetVersionId', "A5.4 selection persists immutable relief version into draft policy");
requireText(ships, 'delete override.reliefAssetVersionId', "A5.4 bundled-default action removes only the relief override");
requireText(ships, 'label: "3D Relief Bundle"', "A5.4 relief bundle control uses standard Admin field shell");
requireText(ships, 'const PROJECTILE_ARCHETYPES = [', "A5.3 exposes only production-backed recipe identities");
requireText(ships, 'label: "Projectile Recipe"', "A5.3 Ship projectile binding uses standard Admin field shell");
requireText(ships, 'override.projectileArchetype = next', "A5.3 persists recipe binding into Ship draft policy");
requireText(ships, 'delete override.projectileArchetype', "A5.3 can restore bundled recipe without fake null values");
requireText(ships, 'Fire preview uses the production PlayerShotSystem', "A5.3 UI states production Fire preview ownership");
requireText(ships, 'Projectile muzzle / trail / sprite internals', "recipe internals remain read-only derived presentation");
requireText(ships, 'Projectile launch / impact SFX', "audio capability boundary remains explicit");
requireText(ships, 'Miss presentation / Weapon Admin entity', "unsupported miss/Weapon authoring remains explicit");
requireText(ships, 'status: "AVAILABLE"', "production-backed A5 capabilities are promoted");
requireText(ships, 'status: "REQUIRES CANONICAL MIGRATION"', "remaining migration-required features remain capability state");
requireText(ships, 'status: "READ-ONLY REFERENCE"', "read-only features remain capability state");
requireText(ships, 'status: "DEFERRED / UNSUPPORTED"', "unsupported features remain capability state");
requireText(ships, 'studio.lifecycleHost.append(saveBar)', "existing Save Draft lifecycle is integrated into Studio");
requireText(ships, 'Save Draft', "existing revision lifecycle remains present");
requireText(ships, 'Published preview still reflects active', "saving Draft does not relabel it as Published");
forbidText(ships, 'REQUIRES CANONICAL MIGRATION\",\n        description: \"The current production path does not yet expose a writable exact-version Ship image field', "obsolete Ship media blocker is removed");
forbidText(ships, 'publishedPreview = validated', "Draft validation must not overwrite Published preview");
forbidText(ships, 'publishedPreview = validatedDraft', "Draft validation must remain ephemeral");
forbidText(ships, 'panel("Visual Profile"', "Ships no longer duplicates Asset Tuning settings in a legacy panel");

requireText(childPolicy, 'reliefAssetVersionId?: string', "A5.4 child canonical Ship policy persists exact relief bundle version");
requireText(childPolicy, 'isShipReliefAssetVersionId', "A5.4 child runtime validator rejects non-canonical relief assignments");
requireText(childPolicy, 'projectileArchetype?: ShipRuntimeProjectileArchetype', "child canonical Ship policy persists projectile recipe");
requireText(childPolicy, 'PROJECTILE_ARCHETYPES.has', "child runtime validator rejects unknown projectile recipes");
requireText(childProjectiles, 'withPlayerProjectileRuntimeSession', "child supports isolated preview resolution without mutating active session");
requireText(childProjectiles, 'session.ships[id]?.projectileArchetype', "child production projectile profile resolves Ship policy binding");
requireText(childProjectiles, 'playerImpactVariantForArchetype', "projectile recipe derives a production impact sound identity");
requireText(childProjectiles, 'impactVariant: playerImpactVariantForArchetype(archetype)', "runtime recipe override cannot retain a mismatched Ship impact sound");
requireText(childShots, 'export function shotRecipeFor', "child exposes production recipe resolver");
requireText(childShots, 'playerProjectileProfile(characterId).archetype', "production PlayerShot recipe derives from canonical Ship projectile profile");
requireText(childPreview, 'const shots = new PlayerShotSystem<number>()', "Fire preview owns real production PlayerShotSystem");
requireText(childPreview, 'const sfx = new Sfx()', "Fire preview owns the real production Sfx implementation");
requireText(childPreview, 'shots.fire({', "Fire preview invokes production projectile fire path");
requireText(childPreview, 'sfx.shot(1);', "Fire preview uses the production launch cue without inventing a writable launch binding");
requireText(childPreview, 'flashShipAssetPreviewRelief(activeCandidate, nextReliefGun++)', "A5.4 Fire preview drives production relief gun feedback on the same fired-shot event");
requireText(childPreview, 'sfx.boltImpact(power, pan, variant)', "Fire arrivals use the production impact cue");
requireText(childPreview, 'playerProjectileProfile(activeCandidate.characterId).impactVariant', "Fire preview resolves impact audio from the same recipe-derived production profile");
requireText(childPreview, 'withShipAssetPreviewRuntime(activeCandidate', "Fire preview scopes production runtime to ephemeral candidate");
requireText(childPreview, 'prepareShipAssetPreviewCandidate(', "A5.4 preview prepares candidate-owned exact media resources before rendering");
requireText(childPreview, 'releaseShipAssetPreviewCandidate(', "A5.4 preview releases superseded/disposed candidate resources");
requireText(childSfx, 'export type ImpactVariant = PlayerImpactVariant | "energy"', "production Sfx keeps a typed impact-variant boundary");
requireText(childSfx, 'boltImpact(power = 1, pan = 0, variant: ImpactVariant = "crystal"): void', "production Sfx exposes typed impact variants with the current production default");
requireText(childSfx, 'shot(multiplier = 1): void', "production Sfx owns the generic launch cue");
forbidText(childPolicy, 'projectileUrl', "child policy must not accept arbitrary projectile URLs");
forbidText(childPolicy, 'projectilePath', "child policy must not accept arbitrary projectile filesystem paths");
forbidText(childPolicy, 'impactSfxAssetVersionId', "A5.3 must not introduce an independent impact-SFX field that can drift from the recipe");
forbidText(childPolicy, 'launchSfxAssetVersionId', "A5.3 must not invent a per-Ship launch-SFX binding for a generic production cue");

console.log("Space Typing Admin A5 preview + A5.2 Ship Media + A5.3 projectile/SFX + A5.4 relief bundle validation passed.");
