from pathlib import Path


def replace_once(path, old, new):
    p = Path(path)
    text = p.read_text()
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{path}: expected one match, found {count}: {old[:120]!r}")
    p.write_text(text.replace(old, new, 1))


# Backend revision relations + publish/rollback safety.
replace_once(
    "admin/store.mjs",
    '''  async listRevisions() {
    const state = await this.getState();
    const names = (await readdir(this.revisionsDir)).filter((name) => name.endsWith(".json"));
    const revisions = await Promise.all(
      names.map((name) => readJson(join(this.revisionsDir, name))),
    );
    return revisions
      .sort((a, b) => b.createdAt.localeCompare(a.createdAt))
      .map((revision) => ({
        ...revision,
        active: revision.revision === state.activeRevision,
      }));
  }
''',
    '''  async listRevisions() {
    const state = await this.getState();
    const names = (await readdir(this.revisionsDir)).filter((name) => name.endsWith(".json"));
    const revisions = await Promise.all(
      names.map((name) => readJson(join(this.revisionsDir, name))),
    );
    const byId = new Map(revisions.map((revision) => [revision.revision, revision]));
    const ancestors = new Set();
    let cursor = byId.get(state.activeRevision);
    while (cursor?.parentRevision) {
      ancestors.add(cursor.parentRevision);
      cursor = byId.get(cursor.parentRevision);
    }
    return revisions
      .sort((a, b) => b.createdAt.localeCompare(a.createdAt))
      .map((revision) => {
        const active = revision.revision === state.activeRevision;
        const relation = active ? "active" : ancestors.has(revision.revision) ? "ancestor" : "draft";
        return {
          ...revision,
          active,
          relation,
          publishable: relation === "draft" && revision.parentRevision === state.activeRevision,
          rollbackEligible: relation === "ancestor",
        };
      });
  }

  async validateRevision(revision) {
    const state = await this.getState();
    const target = await this.getRevision(revision);
    this.validateConfig(target.config);
    const history = await this.listRevisions();
    const entry = history.find((candidate) => candidate.revision === revision);
    if (!entry) throw new AdminValidationError(`Revision ${revision} does not exist.`);
    return {
      revision,
      valid: true,
      activeRevision: state.activeRevision,
      parentRevision: target.parentRevision,
      relation: entry.relation,
      publishable: entry.publishable,
      rollbackEligible: entry.rollbackEligible,
    };
  }
''',
)

replace_once(
    "admin/store.mjs",
    '''  async publish({ revision, expectedActiveRevision }) {
    const state = await this.getState();
    if (state.activeRevision !== expectedActiveRevision) {
      throw new AdminConflictError(
        `Active revision changed from ${expectedActiveRevision} to ${state.activeRevision}.`,
      );
    }
    const target = await this.getRevision(revision);
    this.validateConfig(target.config);
    const nextState = {
      version: 1,
      activeRevision: revision,
      generation: state.generation + 1,
      updatedAt: this.now().toISOString(),
    };
    await writeJsonAtomic(this.statePath, nextState);
    return nextState;
  }

  async rollback({ targetRevision, expectedActiveRevision }) {
    return this.publish({ revision: targetRevision, expectedActiveRevision });
  }
''',
    '''  async publish({ revision, expectedActiveRevision }) {
    const state = await this.getState();
    if (state.activeRevision !== expectedActiveRevision) {
      throw new AdminConflictError(
        `Active revision changed from ${expectedActiveRevision} to ${state.activeRevision}.`,
      );
    }
    const target = await this.getRevision(revision);
    if (target.parentRevision !== state.activeRevision) {
      throw new AdminConflictError(
        `Revision ${revision} was based on ${target.parentRevision ?? "no parent"}; active revision is ${state.activeRevision}. Create a fresh draft before publishing.`,
      );
    }
    this.validateConfig(target.config);
    const nextState = {
      version: 1,
      activeRevision: revision,
      generation: state.generation + 1,
      updatedAt: this.now().toISOString(),
    };
    await writeJsonAtomic(this.statePath, nextState);
    return nextState;
  }

  async rollback({ targetRevision, expectedActiveRevision }) {
    const state = await this.getState();
    if (state.activeRevision !== expectedActiveRevision) {
      throw new AdminConflictError(
        `Active revision changed from ${expectedActiveRevision} to ${state.activeRevision}.`,
      );
    }
    let cursor = await this.getRevision(state.activeRevision);
    let eligible = false;
    while (cursor.parentRevision) {
      if (cursor.parentRevision === targetRevision) {
        eligible = true;
        break;
      }
      cursor = await this.getRevision(cursor.parentRevision);
    }
    if (!eligible) {
      throw new AdminValidationError(
        `Rollback target ${targetRevision} must be a published ancestor of active revision ${state.activeRevision}.`,
      );
    }
    const target = await this.getRevision(targetRevision);
    this.validateConfig(target.config);
    const nextState = {
      version: 1,
      activeRevision: targetRevision,
      generation: state.generation + 1,
      updatedAt: this.now().toISOString(),
    };
    await writeJsonAtomic(this.statePath, nextState);
    return nextState;
  }
''',
)

# Server-side validation endpoint used by B05 before pointer mutations.
replace_once(
    "admin/server.mjs",
    '''    if (request.method === "POST" && url.pathname === "/api/admin/space-typing/revisions") {
      const input = await body(request);
      const revision = await store.createRevision(input);
      json(response, 201, revision);
      return;
    }
''',
    '''    if (request.method === "POST" && url.pathname === "/api/admin/space-typing/validate-revision") {
      const input = await body(request);
      json(response, 200, await store.validateRevision(input.revision));
      return;
    }
    if (request.method === "POST" && url.pathname === "/api/admin/space-typing/revisions") {
      const input = await body(request);
      const revision = await store.createRevision(input);
      json(response, 201, revision);
      return;
    }
''',
)

# API relation/status contract + validation method.
replace_once(
    "portal/src/admin/api.ts",
    '''export type AdminRevision = {
  revision: string;
  parentRevision: string | null;
  createdAt: string;
  author: string;
  message: string;
  config: SpaceTypingAdminConfig;
  active?: boolean;
};
''',
    '''export type AdminRevisionRelation = "active" | "ancestor" | "draft";

export type AdminRevision = {
  revision: string;
  parentRevision: string | null;
  createdAt: string;
  author: string;
  message: string;
  config: SpaceTypingAdminConfig;
  active?: boolean;
  relation?: AdminRevisionRelation;
  publishable?: boolean;
  rollbackEligible?: boolean;
};

export type AdminRevisionValidation = {
  revision: string;
  valid: true;
  activeRevision: string;
  parentRevision: string | null;
  relation: AdminRevisionRelation;
  publishable: boolean;
  rollbackEligible: boolean;
};
''',
)
replace_once(
    "portal/src/admin/api.ts",
    '''  createRevision(input: {
    baseRevision: string;
    config: SpaceTypingAdminConfig;
    message: string;
  }): Promise<AdminRevision> {''',
    '''  validateRevision(revision: string): Promise<AdminRevisionValidation> {
    return this.request<AdminRevisionValidation>("/api/admin/space-typing/validate-revision", {
      method: "POST",
      body: JSON.stringify({ revision }),
    });
  }

  createRevision(input: {
    baseRevision: string;
    config: SpaceTypingAdminConfig;
    message: string;
  }): Promise<AdminRevision> {''',
)

# Route the real B05 renderer ahead of the Phase A mock History screen.
replace_once(
    "portal/src/admin/space-typing-phase-b.ts",
    '''import { renderPhaseBWorldMusic } from "./space-typing-world-music-phase-b";
import { SpaceTypingAdminApi,''',
    '''import { renderPhaseBWorldMusic } from "./space-typing-world-music-phase-b";
import { renderPhaseBHistory } from "./space-typing-history-phase-b";
import { SpaceTypingAdminApi,''',
)
replace_once(
    "portal/src/admin/space-typing-phase-b.ts",
    '''  if (path === `${BASE}/flags`) return renderFlags(navigate);
  return null;''',
    '''  if (path === `${BASE}/flags`) return renderFlags(navigate);
  if (path === `${BASE}/history`) return renderPhaseBHistory(navigate);
  return null;''',
)

# Machine-readable map and docs now mark B05 as UI-wired.
replace_once(
    "admin/space-typing-phase-b-map.v1.json",
    '''      "route": "/admin/space-typing/history",
      "screen": "History & Publish",
      "domain": "revisions",
      "persistence": "immutable-revision-store",
      "applyBoundary": "cas-publish",
      "status": "backend-foundation"''',
    '''      "route": "/admin/space-typing/history",
      "screen": "History & Publish",
      "domain": "revisions",
      "persistence": "immutable-revision-store",
      "applyBoundary": "cas-publish",
      "status": "phase-b-ui-wired"''',
)
replace_once(
    "portal/src/admin/SPACE_TYPING_PHASE_B_MAPPING.md",
    '''## Apply boundaries
''',
    '''## B05 — History & Publish

History now renders the real immutable revision store instead of mock rows. The backend classifies each revision as active, published ancestor, or draft; only a fresh draft whose parent equals the current active revision is publishable. Rollback is restricted to published ancestors. Validate re-runs the current server schema before either pointer operation, and both Publish/Rollback still require expected-active CAS. The screen compares immutable config snapshots and surfaces changed top-level domains without mutating revisions.

## Apply boundaries
''',
)
replace_once(
    "portal/src/admin/SPACE_TYPING_PHASE_B_MAPPING.md",
    '''5. **B05 — History & Publish**: replace mock history/diff/status with real revision data, real validation gates and CAS conflicts.''',
    '''5. **B05 — History & Publish**: real immutable revision data, config diff, backend validation, fresh-draft publish guard, ancestor-only rollback, and CAS conflicts. **Implemented.**''',
)

# Validator locks the B05 route and server/API safety contract.
replace_once(
    "scripts/validate-space-admin-phase-b.mjs",
    '''const worldMusicPhaseB = await readFile(new URL("portal/src/admin/space-typing-world-music-phase-b.ts", root), "utf8");''',
    '''const worldMusicPhaseB = await readFile(new URL("portal/src/admin/space-typing-world-music-phase-b.ts", root), "utf8");
const historyPhaseB = await readFile(new URL("portal/src/admin/space-typing-history-phase-b.ts", root), "utf8");
const server = await readFile(new URL("admin/server.mjs", root), "utf8");''',
)
replace_once(
    "scripts/validate-space-admin-phase-b.mjs",
    '''const flags = map.screens.find((entry) => entry.route === "/admin/space-typing/flags");''',
    '''const flags = map.screens.find((entry) => entry.route === "/admin/space-typing/flags");
const history = map.screens.find((entry) => entry.route === "/admin/space-typing/history");''',
)
replace_once(
    "scripts/validate-space-admin-phase-b.mjs",
    '''assert.equal(flags?.applyBoundary, "new-session");
''',
    '''assert.equal(flags?.applyBoundary, "new-session");
assert.equal(history?.domain, "revisions");
assert.equal(history?.status, "phase-b-ui-wired");
assert.equal(history?.applyBoundary, "cas-publish");
''',
)
replace_once(
    "scripts/validate-space-admin-phase-b.mjs",
    '''assert.match(phaseB, /Reload this screen before saving to avoid overwriting newer published changes/);
''',
    '''assert.match(phaseB, /Reload this screen before saving to avoid overwriting newer published changes/);
assert.match(phaseB, /renderPhaseBHistory/);
assert.match(historyPhaseB, /api\.validateRevision/);
assert.match(historyPhaseB, /api\.publish/);
assert.match(historyPhaseB, /api\.rollback/);
assert.match(historyPhaseB, /window\.confirm/);
assert.match(historyPhaseB, /publishable/);
assert.match(historyPhaseB, /rollbackEligible/);
assert.match(historyPhaseB, /diffValues/);
assert.match(store, /target\.parentRevision !== state\.activeRevision/);
assert.match(store, /must be a published ancestor/);
assert.match(server, /validate-revision/);
assert.match(api, /validateRevision\(revision: string\)/);
''',
)
replace_once(
    "scripts/validate-space-admin-phase-b.mjs",
    '''console.log(`Space Typing Admin Phase B mapping: PASS (${map.screens.length} screens, B01-B04.2 revision-backed domains ready).`);''',
    '''console.log(`Space Typing Admin Phase B mapping: PASS (${map.screens.length} screens, B01-B05 revision-backed domains ready).`);''',
)

# Regression coverage for stale-base publish and draft-as-rollback rejection.
store_test = Path("admin/store.test.mjs")
text = store_test.read_text()
anchor = '''test("rollback is a CAS pointer change to an immutable prior revision", async (t) => {'''
extra = '''test("publish rejects a stale-base draft even when expected active is current", async (t) => {
  const { store, rootDir } = await fixture();
  t.after(() => rm(rootDir, { recursive: true, force: true }));

  const seed = await store.getActiveRevision();
  const first = await store.createRevision({ baseRevision: seed.revision, config: seed.config, message: "First" });
  const stale = await store.createRevision({ baseRevision: seed.revision, config: seed.config, message: "Stale sibling" });
  await store.publish({ revision: first.revision, expectedActiveRevision: seed.revision });

  await assert.rejects(
    store.publish({ revision: stale.revision, expectedActiveRevision: first.revision }),
    AdminConflictError,
  );
  const validation = await store.validateRevision(stale.revision);
  assert.equal(validation.relation, "draft");
  assert.equal(validation.publishable, false);
});

test("rollback rejects a draft that is not on the active ancestry", async (t) => {
  const { store, rootDir } = await fixture();
  t.after(() => rm(rootDir, { recursive: true, force: true }));

  const seed = await store.getActiveRevision();
  const published = await store.createRevision({ baseRevision: seed.revision, config: seed.config, message: "Published" });
  const siblingDraft = await store.createRevision({ baseRevision: seed.revision, config: seed.config, message: "Never published" });
  await store.publish({ revision: published.revision, expectedActiveRevision: seed.revision });

  await assert.rejects(
    store.rollback({ targetRevision: siblingDraft.revision, expectedActiveRevision: published.revision }),
    AdminValidationError,
  );
  const history = await store.listRevisions();
  assert.equal(history.find((revision) => revision.revision === seed.revision)?.rollbackEligible, true);
  assert.equal(history.find((revision) => revision.revision === siblingDraft.revision)?.rollbackEligible, false);
});

'''
if text.count(anchor) != 1:
    raise SystemExit("admin/store.test.mjs: rollback anchor not found exactly once")
store_test.write_text(text.replace(anchor, extra + anchor, 1))

print("B05 History & Publish patch applied.")
