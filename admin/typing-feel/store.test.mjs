// node --test admin/typing-feel/store.test.mjs
// TypingFeelRevisionStore (own typing-feel-admin/1 rules, one write queue,
// publication records), the seedMessage option of RevisionStore, the policy and
// the change scope (docs/games/TYPING_FEEL_SERVICE.md §3.3, §3.4).
import assert from "node:assert/strict";
import { existsSync } from "node:fs";
import { join } from "node:path";
import test from "node:test";
import { loadContract } from "../../typing-feel/tools/import-staging.mjs";
import { AdminValidationError, DEFAULT_SEED_MESSAGE, RevisionStore } from "../store.mjs";
import { describeTypingFeelChangeScope } from "./change-scope.mjs";
import { activeConfig, makeTypingFeelFixture, tempDir } from "./fixture.mjs";
import { TypingFeelValidationError, baseProblems, configProblems } from "./policy.mjs";
import { TypingFeelService } from "./service.mjs";
import { TypingFeelRevisionStore, runTypingFeelExclusive } from "./store.mjs";

const contract = loadContract();

test("RevisionStore takes a seed message instead of the Space text", async (t) => {
  class Plain extends RevisionStore {
    validateConfig(config) {
      return config;
    }
  }
  const dir = await tempDir(t);
  const space = new Plain({ rootDir: join(dir, "space"), contract: {} });
  await space.initialize({ any: 1 });
  assert.equal((await space.getRevision("seed-v1")).message, DEFAULT_SEED_MESSAGE);
  assert.equal(DEFAULT_SEED_MESSAGE, "Initial Space Typing Admin seed", "Space keeps its seed text");
  const shared = new Plain({ rootDir: join(dir, "shared"), contract: {}, seedMessage: "Shared seed" });
  await shared.initialize({ any: 1 });
  assert.equal((await shared.getRevision("seed-v1")).message, "Shared seed");
  const restored = new Plain({ rootDir: join(dir, "restored"), contract: {} });
  const state = await restored.initialize({ any: 2 }, { revision: "restored-r7", message: "From Git", author: "restore" });
  assert.equal(state.activeRevision, "restored-r7");
  assert.equal((await restored.getRevision("restored-r7")).author, "restore");
});

test("the Typing Feel store validates typing-feel-admin/1 only and refuses a Space config", async (t) => {
  const fx = await makeTypingFeelFixture(t);
  const { config } = await activeConfig(fx.store);
  assert.equal(fx.store.validateConfig(config), config);
  assert.throws(() => fx.store.validateConfig({ contractRevision: "space", audio: {} }), TypingFeelValidationError);
  const problemsOf = (edit) => {
    const copy = structuredClone(config);
    edit(copy);
    return configProblems(copy, contract).join("\n");
  };
  assert.match(problemsOf((c) => { c.keyboard.extra = 1; }), /keyboard\.extra is not part of typing-feel-admin\/1/);
  assert.match(problemsOf((c) => { c.keyboard.sets[0].id = "off"; }), /reserved/);
  assert.match(problemsOf((c) => { c.keyboard.sets[1].id = c.keyboard.sets[0].id; }), /listed twice/);
  assert.match(problemsOf((c) => { c.keyboard.sets[0].family = "nowhere"; }), /not in keyboard\.families/);
  assert.match(problemsOf((c) => { c.keyboard.families[1].name = c.keyboard.families[0].name; }), /used twice/);
  assert.match(problemsOf((c) => { c.keyboard.sets[1].order = c.keyboard.sets[0].order; c.keyboard.sets[1].family = c.keyboard.sets[0].family; }), /share order/);
  assert.match(problemsOf((c) => { c.keyboard.sets[0].name = " Padded "; }), /leading or trailing spaces/);
  assert.match(problemsOf((c) => { c.keyboard.sets[0].ownerScore = 11; }), /ownerScore/);
  assert.match(problemsOf((c) => { c.keyboard.sets[0].labels = ["made-up"]; }), /labels/);
  assert.match(problemsOf((c) => { c.keyboard.sets[0].status = "provisional"; delete c.keyboard.sets[0].note; }), /needs a note giving the reason/);
  assert.match(problemsOf((c) => { c.keyboard.retiredIds = [c.keyboard.sets[0].id]; }), /retired; a retired id is never used again/);
  assert.match(problemsOf((c) => { for (const set of c.keyboard.sets) set.enabled = false; }), /At least one set must be shown/);
  assert.match(problemsOf((c) => { c.effects.defaults.style = "sparkle"; }), /style must be one of stamp, flare, smash, shatter, rune, minimal/);
  assert.match(problemsOf((c) => { c.effects.defaults.volume = 1.5; }), /volume must be a number from 0 to 1/);
  assert.match(problemsOf((c) => { c.keyboard.defaultSet = "missing"; }), /not in keyboard\.sets/);
  assert.equal(problemsOf(() => {}), "");
});

test("draft rules against the base: ids kept, retirement kept, new sounds gated", () => {
  const set = (id, assetVersionId, extra = {}) => ({ id, name: id, family: "deep", order: 0, enabled: true, status: "published", assetVersionId, ownerPick: false, ownerScore: null, recipe: "natural-v1", ...extra });
  const base = { keyboard: { sets: [set("a", "v1"), set("b", "v2")], retiredIds: ["z"] } };
  assert.deepEqual(baseProblems({ keyboard: { sets: [set("a", "v1"), set("b", "v2")], retiredIds: ["z"] } }, base), []);
  assert.match(baseProblems({ keyboard: { sets: [set("a", "v1")], retiredIds: ["z"] } }, base).join(), /Set b was removed/);
  assert.deepEqual(baseProblems({ keyboard: { sets: [set("a", "v1")], retiredIds: ["z", "b"] } }, base), [], "retiring is the way to remove");
  assert.match(baseProblems({ keyboard: { sets: [set("a", "v1"), set("b", "v2")], retiredIds: [] } }, base).join(), /Retired id z must stay retired/);
  assert.match(baseProblems({ keyboard: { sets: [set("a", "v9"), set("b", "v2")], retiredIds: ["z"] } }, base).join(), /re-formatted: it needs an owner score of 9/);
  assert.deepEqual(baseProblems({ keyboard: { sets: [set("a", "v9", { ownerScore: 9 }), set("b", "v2")], retiredIds: ["z"] } }, base), []);
  assert.deepEqual(baseProblems({ keyboard: { sets: [set("a", "v9", { status: "provisional", note: "Waiting" }), set("b", "v2")], retiredIds: ["z"] } }, base), []);
  assert.match(baseProblems({ keyboard: { sets: [set("a", "v1"), set("b", "v2"), set("q", "v5", { ownerScore: 9.5 })], retiredIds: ["z"] } }, base, { reservedIds: ["q"] }).join(), /never used again/);
});

test("one write queue per store folder, shared by every store instance and re-entrant", async (t) => {
  const dir = await tempDir(t);
  const one = new TypingFeelRevisionStore({ rootDir: dir });
  const two = new TypingFeelRevisionStore({ rootDir: dir });
  const trace = [];
  const slow = (name, ms) => async () => {
    trace.push(`${name}:start`);
    await new Promise((done) => setTimeout(done, ms));
    trace.push(`${name}:end`);
  };
  await Promise.all([one.exclusive(slow("a", 20)), two.exclusive(slow("b", 1)), one.exclusive(slow("c", 1))]);
  assert.deepEqual(trace, ["a:start", "a:end", "b:start", "b:end", "c:start", "c:end"]);
  const nested = await one.exclusive(() => two.exclusive(async () => "inner"));
  assert.equal(nested, "inner", "a nested call in the same chain does not wait for itself");
  await assert.rejects(runTypingFeelExclusive(dir, async () => { throw new Error("boom"); }), /boom/);
  assert.equal(await one.exclusive(async () => "after a failure"), "after a failure");
});

test("an unimported store reads as empty and writes nothing", async (t) => {
  const dir = await tempDir(t);
  const store = new TypingFeelRevisionStore({ rootDir: join(dir, "shared") });
  assert.equal(await store.isInitialized(), false);
  assert.deepEqual(await store.listPublications(), []);
  assert.deepEqual(await store.reservedRetiredIds(), []);
  const service = new TypingFeelService({ store, mediaStore: { rootDir: join(dir, "data") }, publicDir: join(dir, "public") });
  assert.equal((await service.state()).initialized, false);
  assert.deepEqual(await service.syncOnStartup(), { status: "not-initialized" });
  assert.equal(existsSync(join(dir, "shared")), false, "no folder is created");
  assert.equal(existsSync(join(dir, "public")), false, "the published folder is never touched");
});

test("a publication record is written once and never changed", async (t) => {
  const fx = await makeTypingFeelFixture(t);
  const record = { revision: "seed-v1", catalogueRevision: "r1", publishedAt: "2026-10-30T18:04:19Z", builtAt: "2026-10-30T18:04:19Z" };
  assert.equal(await fx.store.writePublication(record), false, "the seed already holds this record");
  await assert.rejects(fx.store.writePublication({ ...record, publishedAt: "2026-11-01T00:00:00Z" }), AdminValidationError);
  assert.equal((await fx.store.getPublication("seed-v1")).publishedAt, record.publishedAt);
  assert.equal(await fx.store.getPublication("r-unknown"), null);
});

test("the change scope names every kind of change and always affects all games", () => {
  const set = (id, extra = {}) => ({ id, name: id, family: "deep", order: 0, enabled: true, status: "published", assetVersionId: `v-${id}`, ownerPick: false, ownerScore: null, recipe: "natural-v1", ...extra });
  const baseConfig = {
    keyboard: { defaultSet: "a", families: [{ id: "deep", name: "Deep", order: 0 }], retiredIds: [], sets: [set("a"), set("b", { order: 1 }), set("c", { order: 2 }), set("d", { order: 3 })] },
    effects: { defaults: { style: "stamp", intensity: "normal", size: "large", volume: 1 } },
  };
  const targetConfig = structuredClone(baseConfig);
  const [a, b, c] = targetConfig.keyboard.sets;
  a.order = 1;
  b.order = 0;
  c.enabled = false;
  c.name = "C2";
  targetConfig.keyboard.sets = targetConfig.keyboard.sets.filter((entry) => entry.id !== "d");
  targetConfig.keyboard.retiredIds = ["d"];
  targetConfig.keyboard.sets.push(set("e", { order: 4, status: "provisional", note: "Waiting" }));
  targetConfig.keyboard.defaultSet = "b";
  targetConfig.effects.defaults.size = "huge";
  const scope = describeTypingFeelChangeScope({ baseRevision: "base", targetRevision: "next", baseConfig, targetConfig });
  assert.equal(scope.affects, "all games");
  assert.equal(scope.changed, true);
  assert.deepEqual(scope.added, ["e"]);
  assert.deepEqual(scope.hidden, ["c"]);
  assert.deepEqual(scope.retired, ["d"]);
  assert.deepEqual(scope.renamed, [{ id: "c", from: "c", to: "C2" }]);
  assert.deepEqual(scope.reordered, ["b", "a"]);
  assert.deepEqual(scope.defaultChanged, { from: "a", to: "b" });
  assert.deepEqual(scope.effectsChanged, [{ field: "size", from: "large", to: "huge" }]);
  assert.ok(scope.summary.some((line) => /Retire d for good/.test(line)));
  const none = describeTypingFeelChangeScope({ baseConfig, targetConfig: structuredClone(baseConfig) });
  assert.equal(none.changed, false);
  assert.deepEqual(none.summary, []);
});
