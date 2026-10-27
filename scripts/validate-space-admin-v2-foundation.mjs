import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const read = (path) => readFile(resolve(root, path), "utf8");

const [security, server, packageJson] = await Promise.all([
  read("admin/admin-security.mjs"),
  read("admin/server.mjs"),
  read("package.json"),
]);
const pkg = JSON.parse(packageJson);

for (const permission of [
  "config.draft",
  "config.publish",
  "config.rollback",
  "media.upload",
  "media.delete",
  "audit.read",
  "developer.runtime-inspect",
]) {
  assert.match(security, new RegExp(`"${permission.replaceAll(".", "\\.")}"`), `Missing Admin V2 permission ${permission}`);
}

assert.match(security, /result:\s*"attempt"/, "Mutation helper must write a durable attempt audit before mutation.");
assert.match(security, /resolveEntityId/, "Mutation helper must support post-create entity identity resolution.");
assert.match(security, /resolveChangeScope/, "Mutation helper must support post-create change-scope resolution.");
assert.match(security, /model:\s*"whole-config-revision"/, "Change-scope contract must explicitly expose whole-config revision semantics.");
assert.match(security, /Publishing activates the complete target revision/, "Publish-scope warning must explain complete revision activation.");

assert.match(server, /createLocalAdminActorFromRequest/, "Admin server must establish actor context after authentication.");
assert.match(server, /LocalAdminAuditLog/, "Admin server must initialize the audit sink.");
assert.match(server, /\/api\/admin\/space-typing\/actor/, "Admin actor endpoint is missing.");
assert.match(server, /\/api\/admin\/space-typing\/audit/, "Admin audit endpoint is missing.");
assert.match(server, /\/api\/admin\/space-typing\/change-scope/, "Admin publish change-scope endpoint is missing.");
assert.match(server, /ADMIN_PERMISSIONS\.MEDIA_UPLOAD/, "Media upload mutations must enforce media.upload permission.");
assert.match(server, /ADMIN_PERMISSIONS\.MEDIA_DELETE/, "Media delete/archive mutations must enforce media.delete permission.");
assert.match(server, /ADMIN_PERMISSIONS\.CONFIG_DRAFT/, "Revision creation must enforce config.draft permission.");
assert.match(server, /ADMIN_PERMISSIONS\.CONFIG_PUBLISH/, "Publish must enforce config.publish permission.");
assert.match(server, /ADMIN_PERMISSIONS\.CONFIG_ROLLBACK/, "Rollback must enforce config.rollback permission.");
assert.match(server, /error:\s*"forbidden"/, "Authorization failures must map to HTTP 403.");
assert.match(server, /author:\s*actor\.actorId/, "Revision author must come from the authenticated actor context.");
assert.match(server, /resolveEntityId:\s*\(created\)\s*=>\s*created\.revision/, "Revision create audit must resolve the created revision ID.");
assert.match(server, /changeScope:\s*await revisionChangeScope\(input\.revision\)/, "Revision validation must expose publish change scope.");

const adminTest = pkg.scripts["admin:test"];
assert.equal(typeof adminTest, "string", "admin:test script is missing.");
for (const requiredTest of [
  "admin/store.test.mjs",
  "admin/admin-security.test.mjs",
]) {
  assert.ok(adminTest.includes(requiredTest), `admin:test must retain required A0.5 coverage: ${requiredTest}`);
}
assert.match(adminTest, /^node --test\b/, "admin:test must continue using the Node test runner.");
assert.equal(
  pkg.scripts["admin:v2:foundation:validate"],
  "node scripts/validate-space-admin-v2-foundation.mjs",
  "Admin V2 foundation validator script entry is missing.",
);

console.log("Admin V2 A0.5 foundation wiring: OK");
