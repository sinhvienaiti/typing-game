import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { createShopCapabilityManifest, SHOP_AUDITED_CHILD_SHA, SHOP_FIELDS, SHOP_TABS } from "../admin/shop-capability.mjs";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const child = resolve(root, "games/space-typing");
const manifest = createShopCapabilityManifest();
const childHead = execFileSync("git", ["-C", child, "rev-parse", "HEAD"], { encoding: "utf8" }).trim();
const childPaths = execFileSync("git", ["-C", child, "ls-tree", "-r", "--name-only", "HEAD"], { encoding: "utf8" })
  .split("\n").filter(Boolean);
const ownershipPattern = /(^|\/)(?:shop|economy|monetization|wallet|purchase|currency|currencies|stamina)(?:\/|[-_.])/i;
const ownershipPaths = childPaths.filter((path) => ownershipPattern.test(path));

assert.equal(childHead, SHOP_AUDITED_CHILD_SHA, `Shop audit is stale: manifest=${SHOP_AUDITED_CHILD_SHA} pinned-child=${childHead}. Re-audit Shop before changing the SHA.`);
assert.deepEqual(ownershipPaths, [], `Potential Shop/economy owner paths appeared in the pinned child and require re-audit:\n${ownershipPaths.join("\n")}`);
assert.equal(manifest.mode, "runtime-audited-readonly");
assert.equal(manifest.authoring.enabled, false);
assert.equal(manifest.authoring.applyBoundary, "none");
assert.equal(SHOP_TABS.length, 6);
assert.equal(SHOP_FIELDS.length, 15);
assert.ok(manifest.fields.every((field) => field.authorable === false));

const [server, router, phaseMap, ui] = await Promise.all([
  readFile(resolve(root, "admin/server.mjs"), "utf8"),
  readFile(resolve(root, "portal/src/admin/space-typing-phase-b.ts"), "utf8"),
  readFile(resolve(root, "admin/space-typing-phase-b-map.v1.json"), "utf8"),
  readFile(resolve(root, "portal/src/admin/space-typing-shop-phase-b.ts"), "utf8"),
]);
assert.match(server, /GET"&&url\.pathname==="\/api\/admin\/space-typing\/shop\/capabilities"/);
assert.doesNotMatch(server, /POST"&&url\.pathname==="\/api\/admin\/space-typing\/shop/);
assert.match(router, /renderPhaseBShop/);
assert.match(router, /\/shop`\) return renderPhaseBShop/);
assert.match(ui, /RUNTIME AUDIT · READ ONLY/);
assert.match(ui, /Shop Preview/);
const map = JSON.parse(phaseMap);
const shop = map.screens.find((screen) => screen.route === "/admin/space-typing/shop");
assert.ok(shop, "Shop Phase B map row is required");
assert.equal(shop.status, "phase-b-ui-wired-runtime-audited-readonly");
assert.equal(shop.persistence, "runtime-audit-manifest");
assert.equal(shop.applyBoundary, "none");
console.log(`Shop runtime audit valid for ${childHead}: ${SHOP_TABS.length} tabs, ${SHOP_FIELDS.length} locked fields, no transactional owner paths.`);
