# Admin ownership and verification

Re-read current source when applying this reference: progress documents contain historical checkpoints, and parent/child HEADs can differ.

| Concern | Read first | Follow through |
| --- | --- | --- |
| Administrator surface/backend | [Portal Admin V2](../../../../portal/src/admin/v2/), [Admin server](../../../../admin/server.mjs) | [Admin store](../../../../admin/store.mjs), domain route/adapter and child policy |
| Schema/runtime policy | [Child contracts](../../../../games/space-typing/contracts/), [runtime policies](../../../../games/space-typing/src/admin/) | Validator, materializer, production consumer and new-session/runtime/build boundary |
| Ships, media and projectiles | [A5 capabilities](../../../../games/space-typing/src/admin/asset-tuning-capabilities.ts), [Ship policy](../../../../games/space-typing/src/admin/ship-runtime-policy.ts) | Exact image/relief resolution and production renderer; arbitrary Admin GLB assignment is not established by the separate bundled GLB pipeline |
| Skills/equipment | [A6 capabilities](../../../../games/space-typing/src/admin/a6-skill-equipment-capabilities.ts) | Policy validation and production definitions; avoid implying Media/VFX binding where the chain is absent |
| Enemies/bosses | [A7 capabilities](../../../../games/space-typing/src/admin/a7-enemy-boss-capabilities.ts) | Persisted metadata or registry preview alone does not establish gameplay authority |
| Worlds/stages | [A8 capabilities](../../../../games/space-typing/src/admin/a8-world-stage-content-capabilities.ts) | Session snapshot, progression selection and actual runtime |
| Unlocks/economy/shop | [A10 capabilities](../../../../games/space-typing/src/admin/a10-unlock-economy-capabilities.ts), [shop policy](../../../../games/space-typing/src/admin/shop-runtime-policy.ts) | Access/price resolver and effective player session; coordinate with progression-economy |
| Preview lifecycle | [Parent bridge](../../../../portal/src/admin/v2/preview/production-preview-bridge.ts), [classification](../../../../portal/src/admin/v2/preview/preview-classification.ts) | [Child protocol](../../../../games/space-typing/src/admin/asset-preview-protocol.ts), [lifecycle](../../../../games/space-typing/src/admin/asset-preview-lifecycle.ts), [mutation queue](../../../../games/space-typing/src/admin/asset-preview-mutation-queue.ts) |

## Media and revisions

Read [Media V2 architecture](../../../../docs/SPACE_TYPING_ADMIN_V2_MEDIA_ARCHITECTURE.md) for immutable versions, ownership, reference protection and generation provenance; check against the current [media API](../../../../portal/src/admin/v2/media-api.ts) and [picker](../../../../portal/src/admin/v2/asset-picker.ts).

- Published config binds an exact version, never implicit `latest`, arbitrary filesystem paths or unchecked URLs.
- Derived/code-owned backgrounds, UI and procedural VFX do not become editable media merely because a binary can be previewed.
- Candidate preview stays isolated from Published gameplay. Superseded/unmounted candidates release their own resources; late asynchronous results must not resurrect disposed previews.
- Price, discount, unlock and enabled controls use the domain schema and runtime resolver. If a requested control lacks that chain, describe the required migration and implement only within authorized scope.

## Checks by changed boundary

Inspect [root scripts](../../../../package.json), [child scripts](../../../../games/space-typing/package.json), and the relevant validator before running it. Examples from repo root:

```bash
pnpm admin:contract:validate
pnpm admin:v2:media:validate
pnpm --dir games/space-typing test tests/admin-ship-visual-authority.test.ts
pnpm --dir games/space-typing test tests/admin-a7-enemy-boss-capabilities.test.ts
```

Select only checks relevant to the edit. Preview scripts can exercise data paths without proving visual fidelity. For browser acceptance, walk the operator path and check gameplay after the declared apply boundary. In Play mode verify API requests reach the Admin service; a working static page can mask proxy failure.

Use [manual acceptance](../../../../docs/SPACE_TYPING_ADMIN_V2_MANUAL_ACCEPTANCE.md) for scenarios and [remediation plan](../../../../docs/SPACE_TYPING_ADMIN_RUNTIME_UIUX_REMEDIATION_PLAN.md) for known UX/request-path failures. [Progress](../../../../docs/SPACE_TYPING_ADMIN_V2_PROGRESS.md) and [asset-tuning progress](../../../../docs/SPACE_TYPING_ADMIN_ASSET_TUNING_PROGRESS.md) explain history; verify completion claims against today's source.
