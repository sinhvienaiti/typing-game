# Space Typing Admin V2 — Media / Asset Architecture

> A3.0 architecture source of truth for Administrator Media Library, Asset Picker, future Shop imagery, Ships/Weapons/Projectiles media, Audio, SFX and other binary presentation assets.
>
> This document intentionally defines architecture before A3.1 UI. It does not authorize generic write access to current code-owned/generated runtime assets.

## 1. Decision

Space Typing Admin V2 uses a **logical asset + immutable asset version** model.

A logical asset answers “what administrator-facing thing is this?” (for example `Vanguard ship model`, `Victory SFX`, `World 01 background`). An asset version answers “which exact immutable bytes/bundle does a published game definition reference?”.

Published runtime definitions MUST resolve an exact immutable `assetVersionId`. Production references MUST NOT silently follow “latest”. Replacing media means creating a new immutable version and explicitly migrating selected references to it.

This is required because the existing project contains several fundamentally different ownership classes:

- Admin-uploaded Music that can currently be written/deleted by the parent Admin service;
- heavy local source art under `art-src/**` that is intentionally not committed;
- generated runtime assets under `public/assets/space-typing/**` and `src/assets/**`;
- code-owned static SFX/UI assets;
- generated bundles such as 3D ships;
- procedural/config-owned VFX that are not equivalent to uploaded binary files.

A3.1 Media Library MUST sit on top of this model. It MUST NOT become a generic filesystem editor.

## 2. Current ownership inventory

### 2.1 Music

Current owner: `admin/music-assets.mjs` plus child Music catalog/build pipeline.

Current strengths:
- Admin upload has an explicit provenance (`local-admin-upload`);
- content SHA-256 is already recorded;
- catalog is rebuilt after upload/delete;
- deletion is restricted to Admin-uploaded tracks;
- generated song stems already use content-hash cache-busting URLs.

Current gaps:
- uploaded files are written directly into the child source/runtime tree;
- replacement is effectively delete + upload;
- no immutable logical asset/version history;
- no generic `usedBy` reference graph;
- old game revisions are not guaranteed to retain a resolvable old uploaded binary after deletion.

A3.0 does not delete this service. A later migration adapter can import/bridge its current catalog into Media V2.

### 2.2 Heavy local art source

Child `art-src/README.md` declares `art-src/**` as heavy local source art intentionally excluded from Git.

Prepare pipelines consume those source files and generate runtime assets. Examples include:
- `art:prepare`;
- `bg:prepare`;
- `sprites:prepare`;
- `ship3d:prepare`;
- `combat-vfx:prepare`;
- reward/icon/duel/chase pipelines.

Media V2 MUST NOT claim generated files are their original source. For imported generated assets the registry records generation provenance and source hints, but Admin does not gain write ownership over the original local source simply because it can preview the generated output.

### 2.3 3D ships / generated bundles

`ship3d:prepare` demonstrates why a media version cannot be modeled as one path. One source image such as:

`art-src/ships/<id>-top-hd.png`

generates a bundle such as:

- `color.webp`;
- `emissive.webp`;
- `height.bin`;
- `model.json`;
- shared `manifest.json` membership.

Therefore an asset version owns one or more **components**. Each component has its own role, MIME/format, byte/hash metadata and runtime/source reference.

The logical asset may be `ship-model:vanguard`; one immutable version may contain `color`, `emissive`, `height`, and `model` components.

### 2.4 SFX / static audio

The current build integrity checker treats many SFX/stingers/ambient files as code-owned static runtime assets, including Kenney-derived SFX paths under `public/assets/audio/sfx/**`.

Existing static SFX should initially bootstrap into Media V2 as reference-only assets. Importing their metadata does not grant Admin permission to overwrite those files in place.

### 2.5 Backgrounds

Current contract is `runtime-derived-readonly`, persisted as `code-owned-runtime-art` and explicitly rejects a parallel Admin shadow registry.

Backgrounds may appear in Media Library as searchable/reference-only media after bootstrap. Writable replacement requires a future canonical generation/source workflow; A3.0 MUST NOT fabricate one.

### 2.6 UI Assets

Current contract is `runtime-derived-readonly`, persisted as code-owned static/inline SVG. Generic upload/replace/delete/publish is unsupported.

Media V2 may index previewable binary UI assets as reference-only. Inline/programmatic UI definitions remain outside generic Media CRUD.

### 2.7 VFX

Current VFX is `runtime-derived-readonly`, persisted as `code-owned-runtime-vfx`. Significant VFX behavior is procedural/config-owned rather than a file.

**Boundary:** VFX definition authoring remains its own gameplay/presentation domain. Media V2 may own binary images, sprite sheets, textures, audio or models referenced by VFX definitions; it MUST NOT convert procedural VFX definitions into generic media records.

## 3. Canonical concepts

### 3.1 Logical Asset

A logical asset is stable across replacements.

Required fields:

- `assetId`: stable logical identifier;
- `kind`: administrator-facing binary/media kind;
- `title`;
- `lifecycle`: `active | archived`;
- `currentVersionId`: latest administrator-selected version for picker/default presentation only;
- `createdAt`, `createdBy`;
- `updatedAt`, `updatedBy`;
- optional tags/category metadata.

`currentVersionId` is **not** a production “follow latest” pointer. Runtime/game definitions pin exact version IDs.

### 3.2 Immutable Asset Version

Required fields:

- `assetVersionId`: immutable globally unique version identifier;
- `assetId`;
- `contentFingerprint`: deterministic SHA-256 fingerprint over the version component manifest;
- `provenance`;
- `storageClass`;
- `components[]`;
- `createdAt`, `createdBy`;
- source/generator metadata where known;
- optional dimensions/duration/technical metadata.

A version record is never modified after creation except for non-semantic integrity annotations that do not alter bytes, references or provenance. Replacement always creates a new version.

### 3.3 Supported media kinds

A3.0 canonical binary kinds:

- `image`;
- `model`;
- `music`;
- `sfx`;
- `audio`;
- `data`.

`data` supports bundle components such as immutable model/height metadata where the component is part of a binary media bundle. It is not an escape hatch for arbitrary gameplay JSON authoring.

Procedural VFX definitions are explicitly excluded as a Media kind.

### 3.4 Provenance

Canonical provenance values:

- `admin-upload`: bytes were introduced through the canonical Admin Media service;
- `generated-runtime`: runtime asset generated by a known project pipeline;
- `code-owned`: committed/static/inline project-owned asset;
- `external-reference`: externally hosted or otherwise referenced asset not owned by the Admin blob store.

Only `admin-upload` versions are candidates for Admin-owned binary lifecycle operations. Reference-only provenance never grants overwrite/delete permission on the underlying project file.

### 3.5 Storage classes

- `admin-blob`: immutable binary stored under Admin local data root;
- `runtime-reference`: immutable metadata points to a project/runtime URL/path without copying bytes;
- `source-reference`: metadata points to a source/generator input that Admin does not own;
- `external-reference`: immutable metadata points outside the local runtime tree.

A version may contain multiple components, but all component mutation follows the owning version/provenance rules.

### 3.6 Version components

Each component contains:

- `role`: stable semantic role such as `primary`, `color`, `emissive`, `height`, `model`, `calm`, `intense`;
- `mimeType`;
- `format`/extension where applicable;
- `byteSize` when known;
- `sha256` when bytes are locally available/owned;
- `storageClass`;
- `storageKey` for Admin blobs OR `runtimeUrl`/`sourcePath` for references;
- optional `width`, `height`, `durationSeconds`.

A version content fingerprint is computed from the canonicalized immutable component manifest. Component ordering MUST NOT change the fingerprint.

## 4. Identity rules

### 4.1 Asset ID

New Admin-owned logical assets use generated stable IDs such as `media.<uuid>`.

Bootstrap/reference assets use deterministic namespaced IDs where this improves idempotency, for example:

- `runtime.ship-model.vanguard`;
- `runtime.background.world-01`;
- `runtime.sfx.kenney.laser-small`.

Bootstrap MUST be idempotent: re-indexing the same project asset must not create a second logical asset.

### 4.2 Version ID

Every version gets a unique immutable `assetVersionId`. Content SHA/fingerprint is separate from version identity so audit/history can distinguish two intentional admissions of the same bytes when needed.

### 4.3 No implicit latest in published config

Authoring UI may show the logical asset/current version for convenience, but revision-backed domain definitions MUST persist an exact `assetVersionId` at the integration boundary.

This is the core rollback guarantee.

## 5. Reference model (`usedBy`)

References are first-class records rather than inferred only from path scanning.

Required reference fields:

- `referenceId`;
- `assetId`;
- `assetVersionId`;
- `domain`;
- `entityType`;
- `entityId`;
- `field`;
- optional `revisionId`;
- `createdAt`, `createdBy`.

Examples:

- Ships / `ship` / `vanguard` / `modelAssetVersionId`;
- Shop / `product` / `energy-drink` / `thumbnailAssetVersionId`;
- Worlds / `stage` / `42` / `backgroundAssetVersionId`;
- Audio / `worldMusic` / `world-01` / `trackAssetVersionId`.

### Reference rules

1. A reference always targets an exact version.
2. Replacing an asset does not rewrite references automatically.
3. Reference migration is explicit and auditable.
4. A version with any live/published reference cannot be hard-deleted.
5. Historical revision references count for rollback retention even if the version is no longer current.
6. Reference discovery adapters may initially import existing code-owned usages, but an adapter must identify its confidence/source rather than inventing ownership.

## 6. Replace / archive / delete semantics

### 6.1 Replace

`Replace` means:

1. validate/upload or register new immutable version;
2. set logical asset `currentVersionId` to the new version for future selection;
3. show affected `usedBy` references;
4. administrator explicitly chooses which draft/domain references to migrate;
5. migrated game definitions enter normal Save Draft → Validate → Preview → Review Changes → Publish flow.

No in-place binary overwrite.

### 6.2 Archive

Archive is the default removal mechanism.

Archiving:
- hides logical asset from normal picker results;
- does not remove any version;
- does not break existing draft/published/historical references;
- remains reversible.

### 6.3 Hard delete

Hard delete is exceptional.

A3.0 policy:
- code-owned/generated/external versions: never hard-delete underlying files through Media V2;
- referenced versions: never hard-delete;
- historical revision retention: never hard-delete;
- Admin-owned unreferenced version: may be eligible only through an explicit restricted cleanup operation;
- failed/uncommitted upload blobs may be garbage-collected.

A3.1 UI should not expose a casual “Delete file” button that can break rollback.

## 7. Cache-safe runtime URLs

Admin-owned blobs use immutable content/versioned URLs. The URL MUST change when bytes change.

Recommended URL shape:

`/api/admin/space-typing/media/blobs/<assetVersionId>/<role>?v=<sha256-prefix>`

or an equivalent immutable served path.

Generated/code-owned references retain their existing versioned/hash URL conventions when available. Bootstrap does not rewrite those URLs merely to make them look Admin-owned.

## 8. Rollback contract

Rollback safety requires both config and referenced media versions to remain resolvable.

Therefore:

- every published game revision pins exact asset version IDs;
- published and historical references participate in retention;
- archive never removes referenced versions;
- replacement never overwrites old blobs;
- cleanup must prove no retained revision/reference requires the version.

A configuration rollback must never silently resolve a newer image/model/audio version than the one originally published.

## 9. Persistence boundary

A3.0 canonical Media V2 metadata/blob store is local-first and lives under the existing Admin data root, for example:

`.local/admin/space-typing/media-v2/`

Suggested layout:

```text
media-v2/
  registry.json
  blobs/
    <sha256>.<ext>
```

`registry.json` is small local metadata for logical assets, immutable versions and references. Writes must be atomic. Binary blobs are content-addressed and immutable.

This store does not pretend to be a production remote object store. A future remote deployment can provide a storage adapter while preserving logical/version/reference semantics.

## 10. Registry invariants

The Media service MUST enforce:

- schema version;
- unique `assetId`;
- unique `assetVersionId`;
- version’s `assetId` must exist;
- `currentVersionId`, when set, belongs to the same logical asset;
- every reference’s asset/version pair exists and matches;
- immutable version metadata cannot be changed through replacement;
- normalized/safe identifiers and component roles;
- SHA-256 is 64 lowercase hexadecimal characters when present;
- `admin-blob` component must have hash/storage key/known byte size;
- reference-only components may not masquerade as `admin-upload` blobs;
- archived assets remain resolvable by ID/version;
- no hard deletion with references.

## 11. Bootstrap / import policy

A3.0 must support importing current project assets without duplicating binaries.

Bootstrap importer behavior:

1. map known runtime/project asset to deterministic logical asset ID;
2. create reference-only immutable version metadata;
3. include runtime URL/path, known hash/size/technical metadata where available;
4. record `generated-runtime` or `code-owned` provenance;
5. record generator/source hint where known;
6. do not copy binary into Admin blob storage unless the administrator explicitly creates a new Admin-owned version later;
7. do not claim source ownership over `art-src/**`;
8. rerun idempotently.

## 12. Generated bundle policy

For ship 3D and similar generated media, one version may own multiple components. Bootstrap/import should fingerprint the complete component manifest. If any component changes, the imported bundle gets a new version fingerprint/version record.

The shared generated `manifest.json` can be recorded as generator evidence; it is not itself the logical asset.

## 13. Music migration policy

Current `MusicAssetService` remains operational during A3.0.

A3.1 migration should:
- bootstrap existing built-in/code-owned music as reference-only Media assets;
- bootstrap `local-admin-upload` tracks with their current hashes/provenance;
- stop destructive delete/re-upload replacement for new Media V2 workflows;
- create immutable Media V2 versions for new uploads;
- use an adapter to rebuild the child world-music catalog from canonical selected versions only after that integration is proven.

A3.0 MUST NOT silently move/delete existing Music files and break current runtime behavior.

## 14. Security / permissions / audit

Existing A0.5 permissions remain authoritative:

- `media.upload` for creating Admin-owned assets/versions;
- `media.delete` for archive/restricted cleanup operations;
- `audit.read` for history visibility;
- `developer.runtime-inspect` for technical source/provenance diagnostics.

Every Media mutation records actor, action, asset ID, version ID where applicable, result and reference/change scope through the existing Admin audit infrastructure.

Permission enforcement is server-side; hiding a UI button is not authorization.

## 15. Revision integration boundary

Media binary/metadata storage and game-definition revisions are related but not the same persistence object.

- Media upload may create an available immutable asset version without changing gameplay.
- A gameplay/entity edit selects an exact `assetVersionId` into a domain draft.
- Publish of that domain/config revision activates the new reference.
- Media service must expose `usedBy`/reference APIs so Review Changes can show affected entities.
- whole-config revision semantics from A0.5 remain in force until a later revision/change-set redesign explicitly replaces them.

This prevents “uploading a picture” from accidentally changing the live game.

## 16. API/service foundation required before A3.1

A3.0 service must provide/test at minimum:

- initialize/read registry;
- list/get logical assets;
- list/get immutable versions;
- create Admin-owned single-file version;
- register/bootstrap reference-only version and multi-component bundle;
- replace by creating a new version (never mutate old version);
- archive/unarchive logical asset;
- add/remove/query explicit references;
- reject hard deletion of referenced versions;
- expose deterministic version/cache metadata;
- idempotent reference/bootstrap registration;
- atomic metadata writes.

A3.1 Media Library/Asset Picker starts only after this foundation is green.

## 17. Acceptance examples

### Replace ship image/model

1. Administrator uploads/registers a new immutable ship media version.
2. Current live ship still references old `assetVersionId`.
3. Preview selects new version in a ship draft.
4. Review Changes shows old → new media version plus all affected fields.
5. Publish activates exact new version.
6. Rollback resolves old version exactly.

### Replace Shop thumbnail

Same lifecycle. Upload alone does not alter Shop. Product draft pins the chosen version.

### Existing generated background

Media Library can show preview/provenance/used-by as reference-only. It cannot overwrite the generated runtime file until a canonical authoring/generation workflow exists.

### Procedural VFX

Media Library may manage a texture/sprite/sound referenced by the VFX domain. VFX timing/particles/gameplay parameters remain outside generic Media CRUD.

## 18. A3.0 exit criteria

A3.0 is complete only when:

- this architecture is implemented by a canonical local Media service;
- logical asset/version/reference invariants are automated tests;
- immutable replacement and rollback-retention semantics are tested;
- generated/code-owned bootstrap is reference-only/idempotent;
- bundle components are supported;
- referenced-version deletion is fail-closed;
- service is protected by existing permission/audit foundation when exposed through HTTP;
- validator + Admin CI cover the architecture/service;
- no current runtime owner is silently replaced by a shadow registry.

Only then may implementation proceed to A3.1 Media Library + Asset Picker.
