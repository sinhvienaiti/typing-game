# Duel authority, timing and acceptance

## Source map

| Concern | Source | Regression anchors |
| --- | --- | --- |
| Intents/network/session | [Protocol](../../../../games/space-typing/src/duel/protocol.ts), [network](../../../../games/space-typing/src/duel/network-client.ts), [room controller](../../../../games/space-typing/src/duel/online-room-controller.ts), [server](../../../../games/space-typing/server/duel/ws-server.ts) | [Protocol](../../../../games/space-typing/tests/duel-protocol.test.ts), [network](../../../../games/space-typing/tests/duel-network-client.test.ts) |
| Engine/health/effects | [Authority](../../../../games/space-typing/src/duel/authority.ts), [engine](../../../../games/space-typing/src/duel/engine.ts), [combat](../../../../games/space-typing/src/duel/combat.ts) | [Authority](../../../../games/space-typing/tests/duel-authority.test.ts), [engine](../../../../games/space-typing/tests/duel-engine.test.ts), [cannon](../../../../games/space-typing/tests/duel-typing-cannon.test.ts) |
| Accuracy/input | [Precision](../../../../games/space-typing/src/duel/precision-firepower.ts), [typing](../../../../games/space-typing/src/duel/typing.ts), [battle UI](../../../../games/space-typing/src/duel/battle-ui.ts) | [Precision](../../../../games/space-typing/tests/duel-precision-firepower.test.ts), [contracts](../../../../games/space-typing/tests/duel-contracts.test.ts) |
| Projectile/KO/audio | [Shared timing](../../../../games/space-typing/src/duel/presentation-timing.ts), [ordnance](../../../../games/space-typing/src/duel/ordnance.ts), [visuals](../../../../games/space-typing/src/duel/combat-visuals.ts), [juice](../../../../games/space-typing/src/duel/combat-juice.ts), [audio](../../../../games/space-typing/src/duel/audio.ts) | [Ordnance](../../../../games/space-typing/tests/duel-ordnance.test.ts), [round break](../../../../games/space-typing/tests/duel-round-break.test.ts), [audio](../../../../games/space-typing/tests/duel-audio.test.ts) |

[Lobby guide](../../../../games/space-typing/docs/DUEL_LOCAL_LOBBY_SETUP.md) covers services/proxy and independent sessions. [Final V3 plan](../../../../games/space-typing/docs/SPACE_TYPING_DUEL_MODE_MASTER_PLAN_FINAL_V3.md) and [V5 handoff](../../../../games/space-typing/docs/DUEL_COMBAT_V5_IMPLEMENTATION_HANDOFF_2026-10-02.md) supply intent/history; current engine/protocol/tests establish behavior.

## Review contracts

- Protocol accepts semantic input, rejects client claims such as word complete/damage applied. Inspect sequence and match/round guards on local and remote paths.
- Engine schedules travelling effects/cannon before damage. Shared timing currently has 600 ms cannon/base 860 ms attack flight; read current constants, do not duplicate values elsewhere.
- Inputs continue while attacks travel. Preserve simultaneous opposing hits, shield/hull resolution, stale rejection, round cleanup and protection from cancel/retype charge farming.
- Staggered secondary visual missile impacts differ from the authoritative lead hit. RAF stalls must not change damage. Check both Practice and online paths.
- KO chain, banner, break and announcer share timing. Late FX must not affect the next round. Review low-hull/victory feedback on the rendered page.
- PvE Voice/Hybrid availability does not authorize competitive support. Current Duel input is English ASCII, not a Vietnamese text-edit pipeline.

## Verification

From platform root:

```sh
pnpm --dir games/space-typing exec vitest run tests/duel-typing-cannon.test.ts tests/duel-authority.test.ts tests/duel-protocol.test.ts tests/duel-network-client.test.ts tests/duel-ordnance.test.ts tests/duel-round-break.test.ts
pnpm --dir games/space-typing duel:server:check
```

Use `pnpm --dir games/space-typing duel:local` when online local service is needed. Inspect [the launcher](../../../../games/space-typing/scripts/local-duel.mjs) before restart/stop: restarting ends active local rooms. [Game scripts](../../../../games/space-typing/package.json) define commands.

Browser checks: Practice; independent profiles/incognito in Friend Room; create/join/ready/start; wrong/correct/replayed input; simultaneous shots; latency; disconnect/reconnect; impact aligned with health; low-HP FX; KO/audio/next round; lobby/rematch. Two ordinary tabs may share identity. Practice or a lobby screenshot alone does not verify online authority. Record player-side visuals/console and checked service state without exposing tokens.
