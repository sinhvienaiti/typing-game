// Keyboard Sounds and Typing Effects edits of the working copy
// (portal/src/admin/typing-feel/draft-model.ts, docs/games/TYPING_FEEL_SERVICE.md §3.4, §3.7).
import assert from "node:assert/strict";
import test from "node:test";

const model = () => import("../src/admin/typing-feel/draft-model.ts");

const set = (id, family, order, extra = {}) => ({
  id, name: id.replace(/-/g, " "), family, order, enabled: true, status: "published",
  assetVersionId: `media-version.${id}`, ownerPick: false, ownerScore: null, recipe: "firefly-218", ...extra,
});

function seed() {
  return {
    schema: "typing-feel-admin/1",
    contract: 1,
    keyboard: {
      defaultSet: "bright-clack",
      families: [{ id: "deep", name: "Deep", order: 0 }, { id: "crisp", name: "Crisp", order: 1 }, { id: "bright-clack", name: "Bright Clack", order: 2 }],
      sets: [
        set("deep", "deep", 0), set("deep-amber", "deep", 1), set("deep-cedar", "deep", 2),
        set("crisp", "crisp", 0), set("raindrop-tile", "crisp", 1, { ownerPick: true, recipe: "natural-v1", note: "Owner pick" }),
        set("bright-clack", "bright-clack", 0), set("bright-clack-moss", "bright-clack", 1),
      ],
      retiredIds: [],
    },
    effects: { defaults: { style: "stamp", intensity: "normal", size: "large", volume: 1 } },
  };
}

test("catalogue order follows family order, then set order, and leaves hidden sets out", async () => {
  const { catalogueOrder, setShown } = await model();
  const base = seed();
  assert.deepEqual(catalogueOrder(base), ["deep", "deep-amber", "deep-cedar", "crisp", "raindrop-tile", "bright-clack", "bright-clack-moss"]);
  const hidden = setShown(base, "deep-amber", false).config;
  assert.deepEqual(catalogueOrder(hidden), ["deep", "deep-cedar", "crisp", "raindrop-tile", "bright-clack", "bright-clack-moss"]);
  assert.equal(base.keyboard.sets[1].enabled, true, "edits never change their input");
});

test("move up and down stay inside the family and renumber it from 0", async () => {
  const { moveSet, familySets } = await model();
  const moved = moveSet(seed(), "deep-cedar", -1).config;
  assert.deepEqual(familySets(moved, "deep").map((entry) => [entry.id, entry.order]), [["deep", 0], ["deep-cedar", 1], ["deep-amber", 2]]);
  assert.match(moveSet(seed(), "deep", -1).error, /already first/);
  assert.match(moveSet(seed(), "deep-cedar", 1).error, /already last/);
});

test("drag and drop takes the target's place, inside a family or across families", async () => {
  const { dropOnSet, placeSet, familySets } = await model();
  const down = dropOnSet(seed(), "deep", "deep-cedar").config;
  assert.deepEqual(familySets(down, "deep").map((entry) => entry.id), ["deep-amber", "deep-cedar", "deep"], "dragged down: after the target");
  const up = dropOnSet(seed(), "deep-cedar", "deep").config;
  assert.deepEqual(familySets(up, "deep").map((entry) => entry.id), ["deep-cedar", "deep", "deep-amber"], "dragged up: before the target");
  const across = dropOnSet(seed(), "raindrop-tile", "deep-amber").config;
  assert.deepEqual(familySets(across, "deep").map((entry) => [entry.id, entry.order]), [["deep", 0], ["raindrop-tile", 1], ["deep-amber", 2], ["deep-cedar", 3]]);
  assert.deepEqual(familySets(across, "crisp").map((entry) => [entry.id, entry.order]), [["crisp", 0]], "the old family closes the gap");
  assert.equal(across.keyboard.sets.find((entry) => entry.id === "raindrop-tile").family, "deep");
  const appended = placeSet(seed(), "deep", "bright-clack", Number.POSITIVE_INFINITY).config;
  assert.deepEqual(familySets(appended, "bright-clack").map((entry) => entry.id), ["bright-clack", "bright-clack-moss", "deep"]);
  assert.match(placeSet(seed(), "deep", "nope", 0).error, /not in this draft/);
});

test("the default must be shown and published; hide and retire refuse the default", async () => {
  const { setDefault, setShown, retireSet } = await model();
  assert.equal(setDefault(seed(), "raindrop-tile").config.keyboard.defaultSet, "raindrop-tile");
  const hidden = setShown(seed(), "deep", false).config;
  assert.match(setDefault(hidden, "deep").error, /hidden/);
  const provisional = seed();
  provisional.keyboard.sets[0].status = "provisional";
  assert.match(setDefault(provisional, "deep").error, /provisional/);
  assert.match(setShown(seed(), "bright-clack", false).error, /default set/);
  assert.match(retireSet(seed(), "bright-clack").error, /default/);
});

test("retire removes the row for good and reserves its id", async () => {
  const { retireSet, familySets, changedSetIds } = await model();
  const retired = retireSet(seed(), "deep-amber").config;
  assert.deepEqual(retired.keyboard.retiredIds, ["deep-amber"]);
  assert.equal(retired.keyboard.sets.some((entry) => entry.id === "deep-amber"), false);
  assert.deepEqual(familySets(retired, "deep").map((entry) => [entry.id, entry.order]), [["deep", 0], ["deep-cedar", 1]]);
  assert.ok(changedSetIds(seed(), retired).has("deep-amber"));
});

test("rename keeps the id; family names stay unique; families reorder and get new ids from names", async () => {
  const { renameSet, renameFamily, moveFamily, addFamily, orderedFamilies } = await model();
  const renamed = renameSet(seed(), "deep", "  Deep   Velvet  ").config;
  assert.deepEqual(renamed.keyboard.sets.find((entry) => entry.id === "deep").name, "Deep Velvet");
  assert.match(renameSet(seed(), "deep", "   ").error, /cannot be empty/);
  assert.match(renameSet(seed(), "deep", "x".repeat(61)).error, /at most 60/);
  assert.match(renameFamily(seed(), "deep", "crisp").error, /already called/);
  assert.equal(renameFamily(seed(), "deep", "Low").config.keyboard.families[0].name, "Low");
  const moved = moveFamily(seed(), "bright-clack", -1).config;
  assert.deepEqual(orderedFamilies(moved).map((family) => [family.id, family.order]), [["deep", 0], ["bright-clack", 1], ["crisp", 2]]);
  const added = addFamily(seed(), "Soft Rain").config;
  assert.deepEqual(orderedFamilies(added).at(-1), { id: "soft-rain", name: "Soft Rain", order: 3 });
  assert.equal(addFamily(seed(), "Off", { reserved: ["off"] }).config.keyboard.families.at(-1).id, "off-2", "never a reserved id");
  assert.match(addFamily(seed(), "Deep").error, /already exists/);
});

test("effect defaults take the contract ids; volume is clamped to 0 … 1 in hundredths", async () => {
  const { setEffectDefault } = await model();
  assert.equal(setEffectDefault(seed(), "style", "flare").effects.defaults.style, "flare");
  assert.equal(setEffectDefault(seed(), "volume", 0.8).effects.defaults.volume, 0.8);
  assert.equal(setEffectDefault(seed(), "volume", 1.7).effects.defaults.volume, 1);
  assert.equal(setEffectDefault(seed(), "volume", 0.333).effects.defaults.volume, 0.33);
});

test("draft-change marks and the bar summary compare by content, not key order", async () => {
  const { changedSetIds, localChangeSummary, sameConfig, setDefault, moveSet, setEffectDefault } = await model();
  const base = seed();
  const reordered = JSON.parse(JSON.stringify(base), (key, value) => (value && typeof value === "object" && !Array.isArray(value) ? Object.fromEntries(Object.entries(value).reverse()) : value));
  assert.equal(sameConfig(base, reordered), true);
  let working = setDefault(base, "deep").config;
  working = moveSet(working, "crisp", 1).config;
  working = setEffectDefault(working, "intensity", "high");
  // The swap marks one of the two sets (the one that left the longest unchanged run), plus both defaults.
  assert.deepEqual([...changedSetIds(base, working)].sort(), ["bright-clack", "deep", "raindrop-tile"]);
  assert.deepEqual(localChangeSummary(base, working).parts, ["3 sets", "typing effects"]);
  assert.deepEqual(localChangeSummary(base, base).parts, []);
});

test("moving one set to the top marks that set only, not every set it passed", async () => {
  const { changedSetIds, dropOnSet, placeSet, moveFamily } = await model();
  const base = seed();
  assert.deepEqual([...changedSetIds(base, dropOnSet(base, "deep-cedar", "deep").config)], ["deep-cedar"]);
  const across = placeSet(base, "deep", "crisp", 0).config;
  assert.deepEqual([...changedSetIds(base, across)], ["deep"], "a family change marks the moved set; both families keep their order");
  assert.deepEqual([...changedSetIds(base, moveFamily(base, "bright-clack", -1).config)], [], "family order is not a set change");
});
