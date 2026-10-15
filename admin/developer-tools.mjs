const BASE = "/admin/space-typing";

export const DEVELOPER_TOOLS_MANIFEST = Object.freeze({
  version: 2,
  permission: "developer.runtime-inspect",
  sections: Object.freeze([
    Object.freeze({
      id: "runtime-inspector",
      label: "Runtime Inspector",
      description: "Inspect effective Admin identity, active revision and runtime/session state in one developer-only workspace.",
      tools: Object.freeze([
        Object.freeze({ label: "Analytics / Telemetry", path: `${BASE}/analytics`, description: "Inspect session/runtime telemetry and local-profile history." }),
        Object.freeze({ label: "Currencies", path: `${BASE}/currencies`, description: "Inspect runtime-owned currency caps, sources and persistence semantics." }),
        Object.freeze({ label: "Rewards & Drops", path: `${BASE}/rewards`, description: "Inspect runtime reward/drop resolution where no administrator authoring owner exists." }),
        Object.freeze({ label: "Stamina / Warp", path: `${BASE}/warp`, description: "Inspect stamina regeneration, reserve and persistence ownership." }),
        Object.freeze({ label: "Expedition", path: `${BASE}/expedition`, description: "Inspect Expedition runtime/save boundaries without exposing browser-local progression as Admin policy." }),
      ]),
    }),
    Object.freeze({
      id: "contract-inspector",
      label: "Contract Inspector",
      description: "Inspect canonical child contracts for Live Ops, PvP and presentation ownership without exposing raw JSON on normal administrator routes.",
      tools: Object.freeze([
        Object.freeze({ label: "Live Ops", path: `${BASE}/events`, description: "Inspect gameplay Events ownership and the Shop-owned promotion boundary." }),
        Object.freeze({ label: "Missions", path: `${BASE}/missions`, description: "Inspect mission/progression ownership where no separate Admin authoring service exists." }),
        Object.freeze({ label: "Daily / Weekly", path: `${BASE}/daily-weekly`, description: "Inspect recurring challenge ownership and the absence of a canonical weekly scheduler where applicable." }),
        Object.freeze({ label: "Duel", path: `${BASE}/duel`, description: "Inspect Duel room/session authority and supported scenario values." }),
        Object.freeze({ label: "Ranked", path: `${BASE}/ranked`, description: "Inspect fixed competitive rules and authority-owned constraints." }),
        Object.freeze({ label: "Alternative Modes", path: `${BASE}/alternative-modes`, description: "Inspect runtime mode availability and admission boundaries." }),
      ]),
    }),
    Object.freeze({
      id: "validation",
      label: "Validation",
      description: "Run read-only validation against the currently published immutable revision and inspect exact change scope evidence.",
      tools: Object.freeze([
        Object.freeze({ label: "History & Publish", path: `${BASE}/history`, description: "Open the administrator-facing version review, validation, publish and rollback workflow." }),
        Object.freeze({ label: "Feature Gates", path: `${BASE}/feature-gates`, description: "Inspect developer/operational gate ownership and unsupported targeting boundaries." }),
      ]),
    }),
    Object.freeze({
      id: "asset-diagnostics",
      label: "Asset Diagnostics",
      description: "Inspect media ownership, generated/background assets and production presentation diagnostics without creating a parallel asset store.",
      tools: Object.freeze([
        Object.freeze({ label: "Media Library", path: `${BASE}/media`, description: "Inspect canonical Media V2 assets, versions, usage and provenance." }),
        Object.freeze({ label: "Backgrounds", path: `${BASE}/backgrounds`, description: "Inspect production background composition and source ownership." }),
        Object.freeze({ label: "VFX", path: `${BASE}/vfx`, description: "Inspect representative production projectile/VFX contexts." }),
        Object.freeze({ label: "UI Assets", path: `${BASE}/ui-assets`, description: "Inspect code/source-owned UI asset presentation contracts." }),
      ]),
    }),
    Object.freeze({
      id: "qa-sandbox",
      label: "QA Sandbox",
      description: "Run isolated developer/test workflows that never write Campaign progression or publish Admin configuration.",
      tools: Object.freeze([
        Object.freeze({ label: "QA Sandbox", path: `${BASE}/qa`, description: "Open the isolated Space Typing Test Lab." }),
      ]),
    }),
  ]),
});

export function createDeveloperToolsManifest() {
  return DEVELOPER_TOOLS_MANIFEST;
}
