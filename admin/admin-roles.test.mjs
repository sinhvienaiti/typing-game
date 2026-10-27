import assert from "node:assert/strict";
import test from "node:test";
import {
  ADMIN_PERMISSIONS,
  ADMIN_ROLE_TEMPLATES,
  createLocalAdminActor,
  hasAdminPermission,
  requireAdminPermission,
  resolveAdminRolePermissions,
  AdminAuthorizationError,
} from "./admin-security.mjs";

test("A13 role templates expose least-privilege defaults", () => {
  const roles = Object.fromEntries(ADMIN_ROLE_TEMPLATES.map((role) => [role.id, role]));
  assert.deepEqual(roles.viewer.permissions, []);
  assert.equal(roles.editor.permissions.includes(ADMIN_PERMISSIONS.CONFIG_DRAFT), true);
  assert.equal(roles.editor.permissions.includes(ADMIN_PERMISSIONS.CONFIG_PUBLISH), false);
  assert.equal(roles.publisher.permissions.includes(ADMIN_PERMISSIONS.CONFIG_PUBLISH), true);
  assert.equal(roles.developer.permissions.includes(ADMIN_PERMISSIONS.DEVELOPER_INSPECT), true);
  assert.equal(roles.developer.permissions.includes(ADMIN_PERMISSIONS.CONFIG_DRAFT), false);
  assert.equal(roles["media-manager"].permissions.includes(ADMIN_PERMISSIONS.MEDIA_DELETE), true);
});

test("A13 unknown roles fail closed", () => {
  const actor = createLocalAdminActor({ role: "does-not-exist" });
  assert.equal(actor.roleKnown, false);
  assert.deepEqual(actor.permissions, []);
  assert.throws(() => requireAdminPermission(actor, ADMIN_PERMISSIONS.CONFIG_DRAFT), AdminAuthorizationError);
});

test("A13 granular deployment overrides only affect known permissions", () => {
  const resolved = resolveAdminRolePermissions("editor", "+config.publish,-media.upload");
  assert.equal(resolved.permissions.includes(ADMIN_PERMISSIONS.CONFIG_DRAFT), true);
  assert.equal(resolved.permissions.includes(ADMIN_PERMISSIONS.CONFIG_PUBLISH), true);
  assert.equal(resolved.permissions.includes(ADMIN_PERMISSIONS.MEDIA_UPLOAD), false);
  assert.deepEqual(resolved.overrides.map((entry) => `${entry.operation}:${entry.permission}`), [
    "add:config.publish",
    "remove:media.upload",
  ]);
  assert.throws(() => resolveAdminRolePermissions("viewer", "+root.shell"), /Unknown Admin permission override/);
});

test("A13 restricted role cannot execute forbidden permission checks", () => {
  const editor = createLocalAdminActor({ role: "editor" });
  assert.equal(hasAdminPermission(editor, ADMIN_PERMISSIONS.CONFIG_DRAFT), true);
  assert.equal(hasAdminPermission(editor, ADMIN_PERMISSIONS.CONFIG_PUBLISH), false);
  assert.throws(
    () => requireAdminPermission(editor, ADMIN_PERMISSIONS.CONFIG_PUBLISH),
    (error) => error instanceof AdminAuthorizationError && error.permission === ADMIN_PERMISSIONS.CONFIG_PUBLISH,
  );
  const developer = createLocalAdminActor({ role: "developer" });
  assert.equal(hasAdminPermission(developer, ADMIN_PERMISSIONS.DEVELOPER_INSPECT), true);
  assert.equal(hasAdminPermission(developer, ADMIN_PERMISSIONS.MEDIA_DELETE), false);
});

test("A13 actor exposes templates/effective access without a browser-controlled role selector", () => {
  const actor = createLocalAdminActor({ role: "publisher", actorId: "ops-1", displayName: "Ops" });
  assert.equal(actor.role, "publisher");
  assert.equal(actor.roleAssignmentOwner, "deployment");
  assert.equal(actor.roleTemplates.length, ADMIN_ROLE_TEMPLATES.length);
  assert.equal(actor.permissionCatalog.some((permission) => permission.dangerous), true);
  assert.equal(actor.permissions.includes(ADMIN_PERMISSIONS.CONFIG_PUBLISH), true);
});
