import assert from "node:assert/strict";
import { mkdtemp, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import test from "node:test";
import {
  ADMIN_PERMISSIONS,
  AdminAuthorizationError,
  LocalAdminAuditLog,
  createLocalAdminActor,
  describeConfigChangeScope,
  hasAdminPermission,
  requireAdminPermission,
  runAuthorizedAdminMutation,
} from "./admin-security.mjs";

test("local actor preserves backward-compatible super-admin permissions", () => {
  const actor = createLocalAdminActor({ actorId: "toan", displayName: "Toan" });
  assert.equal(actor.actorId, "toan");
  assert.equal(actor.actorDisplayName, "Toan");
  assert.equal(actor.authMethod, "local-admin-token");
  assert.equal(actor.role, "super-admin");
  assert.equal(hasAdminPermission(actor, ADMIN_PERMISSIONS.CONFIG_DRAFT), true);
  assert.equal(hasAdminPermission(actor, ADMIN_PERMISSIONS.CONFIG_PUBLISH), true);
  assert.equal(hasAdminPermission(actor, ADMIN_PERMISSIONS.MEDIA_UPLOAD), true);
});

test("authorization fails closed when permission is absent", () => {
  const actor = { actorId: "viewer", permissions: [] };
  assert.equal(hasAdminPermission(actor, ADMIN_PERMISSIONS.CONFIG_PUBLISH), false);
  assert.throws(
    () => requireAdminPermission(actor, ADMIN_PERMISSIONS.CONFIG_PUBLISH),
    (error) => error instanceof AdminAuthorizationError && error.permission === ADMIN_PERMISSIONS.CONFIG_PUBLISH,
  );
});

test("whole-revision change scope reports every changed domain/path", () => {
  const baseConfig = {
    audio: { defaults: { music: 0.2, sfx: 1 } },
    content: { ships: { ships: { vanguard: { name: "Vanguard" } } } },
    system: { maintenance: { enabled: false } },
  };
  const targetConfig = structuredClone(baseConfig);
  targetConfig.audio.defaults.music = 0.3;
  targetConfig.content.ships.ships.vanguard.name = "Vanguard Mk II";
  targetConfig.system.maintenance.enabled = true;

  const scope = describeConfigChangeScope({
    baseRevision: "base-1",
    targetRevision: "draft-2",
    baseConfig,
    targetConfig,
  });

  assert.equal(scope.model, "whole-config-revision");
  assert.equal(scope.changed, true);
  assert.deepEqual(scope.domains, ["audio", "content.ships", "system"]);
  assert.deepEqual(scope.changedPaths, [
    "audio.defaults.music",
    "content.ships.ships.vanguard.name",
    "system.maintenance.enabled",
  ]);
  assert.match(scope.publishWarning, /complete target revision/i);
});

test("audit log records attempt and success with resolved revision identity", async (t) => {
  const rootDir = await mkdtemp(join(tmpdir(), "typing-game-admin-audit-"));
  t.after(() => rm(rootDir, { recursive: true, force: true }));
  let event = 0;
  const auditLog = new LocalAdminAuditLog({
    rootDir,
    now: () => new Date("2026-10-13T02:00:00.000Z"),
    idFactory: () => `event-${++event}`,
  });
  const actor = createLocalAdminActor({ actorId: "toan", displayName: "Toan", requestId: "req-1" });
  const draftScope = { model: "whole-config-revision", baseRevision: "seed-v1", targetRevision: null, domains: ["audio"] };

  const result = await runAuthorizedAdminMutation({
    actor,
    permission: ADMIN_PERMISSIONS.CONFIG_DRAFT,
    auditLog,
    action: "revision.create",
    domain: "config",
    entityType: "revision",
    changeScope: draftScope,
    resolveEntityId: (revision) => revision.revision,
    resolveChangeScope: (revision) => ({ ...draftScope, targetRevision: revision.revision }),
    operation: async () => ({ revision: "draft-1" }),
  });
  assert.equal(result.revision, "draft-1");

  const events = await auditLog.list();
  assert.equal(events.length, 2);
  assert.equal(events[0].result, "success");
  assert.equal(events[0].entityId, "draft-1");
  assert.equal(events[0].changeScope.targetRevision, "draft-1");
  assert.equal(events[0].actor.actorId, "toan");
  assert.equal(events[0].requestId, "req-1");
  assert.equal(events[1].result, "attempt");
});

test("denied mutations are audited and never execute", async (t) => {
  const rootDir = await mkdtemp(join(tmpdir(), "typing-game-admin-audit-denied-"));
  t.after(() => rm(rootDir, { recursive: true, force: true }));
  const auditLog = new LocalAdminAuditLog({ rootDir });
  const actor = { ...createLocalAdminActor(), actorId: "viewer", permissions: [] };
  let executed = false;

  await assert.rejects(
    runAuthorizedAdminMutation({
      actor,
      permission: ADMIN_PERMISSIONS.CONFIG_PUBLISH,
      auditLog,
      action: "revision.publish",
      domain: "config",
      entityType: "revision",
      entityId: "draft-1",
      operation: async () => {
        executed = true;
        return "should-not-run";
      },
    }),
    AdminAuthorizationError,
  );

  assert.equal(executed, false);
  const events = await auditLog.list();
  assert.equal(events.length, 1);
  assert.equal(events[0].result, "denied");
  assert.equal(events[0].actor.actorId, "viewer");
});

test("audit attempt failure prevents mutation from running", async () => {
  let executed = false;
  const auditLog = {
    async record() {
      throw new Error("audit disk unavailable");
    },
  };

  await assert.rejects(
    runAuthorizedAdminMutation({
      actor: createLocalAdminActor(),
      permission: ADMIN_PERMISSIONS.CONFIG_DRAFT,
      auditLog,
      action: "revision.create",
      domain: "config",
      operation: async () => {
        executed = true;
        return { revision: "draft-1" };
      },
    }),
    /audit disk unavailable/,
  );
  assert.equal(executed, false);
});

test("final audit append failure does not make a completed mutation look failed", async () => {
  let writes = 0;
  let auditError = null;
  const auditLog = {
    async record() {
      writes += 1;
      if (writes === 2) throw new Error("final audit append failed");
    },
  };

  const result = await runAuthorizedAdminMutation({
    actor: createLocalAdminActor(),
    permission: ADMIN_PERMISSIONS.CONFIG_DRAFT,
    auditLog,
    action: "revision.create",
    domain: "config",
    operation: async () => ({ revision: "draft-1" }),
    onAuditError: (error) => { auditError = error; },
  });

  assert.equal(result.revision, "draft-1");
  assert.match(auditError?.message ?? "", /final audit append failed/);
});
