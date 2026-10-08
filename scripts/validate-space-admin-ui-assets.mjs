import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";

const contract = JSON.parse(await readFile("games/space-typing/contracts/space-typing-admin-ui-assets.v1.json", "utf8"));
const page = await readFile("portal/src/admin/space-typing-ui-assets-phase-b.ts", "utf8");
const router = await readFile("portal/src/admin/space-typing-phase-b.ts", "utf8");
const server = await readFile("admin/server.mjs", "utf8");
const nav = await readFile("portal/src/admin/space-typing.ts", "utf8");

assert.equal(contract.contractRevision, "space-typing-admin-ui-assets-v1");
assert.equal(contract.capability, "ui-assets.read");
assert.equal(contract.route.path, "/admin/space-typing/ui-assets");
assert.equal(contract.uiAssets.mode, "runtime-derived-readonly");
assert.equal(contract.uiAssets.writeCapability, false);
assert.equal(contract.uiAssets.previewWriteCapability, false);
assert.equal(contract.uiAssets.applyBoundary, "none");
assert.deepEqual(contract.uiAssets.authorableFields, []);
assert.deepEqual(
  contract.uiAssets.surfaces.map((surface) => surface.id),
  ["shared-components", "game-hud", "duel-battle", "ranked"],
);
for (const source of contract.uiAssets.runtimeSources) {
  assert.equal(typeof source, "string");
  assert.ok(source.length > 0);
}

assert.match(page, /\/api\/admin\/space-typing\/ui-assets\/contract/);
assert.match(page, /RUNTIME-BACKED · READ ONLY/);
assert.match(page, /NO FAKE UI ASSET CRUD/);
assert.match(page, /Admin writes closed/);
assert.match(router, /renderPhaseBUiAssets/);
assert.match(router, /\$\{BASE\}\/ui-assets/);
assert.match(server, /space-typing-admin-ui-assets\.v1\.json/);
assert.match(server, /request\.method==="GET"&&url\.pathname==="\/api\/admin\/space-typing\/ui-assets\/contract"/);
for (const method of ["POST", "PUT", "PATCH", "DELETE"]) {
  assert.ok(
    !server.includes(`request.method==="${method}"&&url.pathname==="/api/admin/space-typing/ui-assets/contract"`),
    `UI Assets must not expose ${method} contract mutation`,
  );
}
assert.match(nav, /id:\s*"ui-assets"/);
assert.match(nav, /capability:\s*"ui-assets\.read"/);

console.log("Space Typing Admin UI Assets mapping: PASS (pinned child contract + read-only API/UI boundary verified).");
