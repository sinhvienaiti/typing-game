const BASE = "/admin/space-typing";

export const DEVELOPER_TOOLS_MANIFEST = Object.freeze({
  version: 1,
  permission: "developer.runtime-inspect",
  sections: Object.freeze([
    Object.freeze({
      id: "runtime",
      label: "Runtime & Telemetry",
      description: "Inspect runtime/session evidence and diagnostics without mixing it into normal administrator workflows.",
      tools: Object.freeze([
        Object.freeze({ label: "Analytics / Telemetry", path: `${BASE}/analytics`, description: "Inspect session/runtime telemetry and local-profile history." }),
      ]),
    }),
    Object.freeze({
      id: "economy",
      label: "Economy Diagnostics",
      description: "Inspect runtime-owned economy behavior that is not yet a canonical administrator authoring workflow.",
      tools: Object.freeze([
        Object.freeze({ label: "Shop Runtime Contract", path: `${BASE}/shop`, description: "Inspect current Shop pricing, stock and purchase ownership while Admin authoring remains intentionally closed." }),
        Object.freeze({ label: "Currencies", path: `${BASE}/currencies`, description: "Inspect current currency ownership, caps, sources and runtime semantics." }),
        Object.freeze({ label: "Rewards & Drops", path: `${BASE}/rewards`, description: "Inspect current reward and drop behavior before canonical authoring exists." }),
        Object.freeze({ label: "Stamina / Warp", path: `${BASE}/warp`, description: "Inspect Warp stamina, reserve, regeneration and persistence ownership." }),
      ]),
    }),
    Object.freeze({
      id: "live-ops",
      label: "Live Ops Diagnostics",
      description: "Inspect runtime behavior for systems that do not yet have a canonical scheduling/authoring control plane.",
      tools: Object.freeze([
        Object.freeze({ label: "Missions", path: `${BASE}/missions`, description: "Inspect mission/progression runtime ownership." }),
        Object.freeze({ label: "Daily / Weekly", path: `${BASE}/daily-weekly`, description: "Inspect recurring challenge runtime behavior and current capability gaps." }),
        Object.freeze({ label: "Expedition", path: `${BASE}/expedition`, description: "Inspect Expedition runtime/save boundaries." }),
        Object.freeze({ label: "Events", path: `${BASE}/events`, description: "Inspect current event runtime behavior before a genuine Admin scheduler exists." }),
        Object.freeze({ label: "Feature Gates", path: `${BASE}/feature-gates`, description: "Inspect feature-gate ownership until safe Live Ops gates are separated from developer gates." }),
      ]),
    }),
    Object.freeze({
      id: "pvp",
      label: "PvP Diagnostics",
      description: "Inspect competitive-mode ownership and authority boundaries.",
      tools: Object.freeze([
        Object.freeze({ label: "Duel", path: `${BASE}/duel`, description: "Inspect Duel room/rule ownership and runtime authority." }),
        Object.freeze({ label: "Ranked", path: `${BASE}/ranked`, description: "Inspect Ranked capability and backend ownership without fabricating season management." }),
        Object.freeze({ label: "Alternative Modes", path: `${BASE}/alternative-modes`, description: "Inspect alternative mode availability and runtime contracts." }),
      ]),
    }),
    Object.freeze({
      id: "visuals",
      label: "Visual Diagnostics",
      description: "Inspect source/code-owned visual assets until the Media architecture gate defines canonical asset ownership.",
      tools: Object.freeze([
        Object.freeze({ label: "Backgrounds", path: `${BASE}/backgrounds`, description: "Inspect background composition/generated asset ownership." }),
        Object.freeze({ label: "VFX", path: `${BASE}/vfx`, description: "Inspect code/runtime-owned VFX definitions." }),
        Object.freeze({ label: "UI Assets", path: `${BASE}/ui-assets`, description: "Inspect UI asset ownership and runtime presentation contracts." }),
      ]),
    }),
    Object.freeze({
      id: "qa",
      label: "QA & Test Lab",
      description: "Run isolated developer/test workflows without writing Campaign progression.",
      tools: Object.freeze([
        Object.freeze({ label: "QA Sandbox", path: `${BASE}/qa`, description: "Open the isolated Space Typing Test Lab." }),
      ]),
    }),
  ]),
});

export function createDeveloperToolsManifest() {
  return DEVELOPER_TOOLS_MANIFEST;
}
