// Add sound set (portal/src/admin/typing-feel/listen-model.ts and the draft-model
// additions; docs/games/TYPING_FEEL_SERVICE.md §3.8, decision 5): the loudness-matched
// A/B, the blind order, the per-key grid, Accept locks, and the new row in the draft.
import assert from "node:assert/strict";
import test from "node:test";

const listen = () => import("../src/admin/typing-feel/listen-model.ts");
const model = () => import("../src/admin/typing-feel/draft-model.ts");

function seed() {
  const set = (id, family, order, extra = {}) => ({ id, name: id, family, order, enabled: true, status: "published", assetVersionId: `media-version.${id}`, ownerPick: false, ownerScore: null, recipe: "firefly-218", ...extra });
  return {
    schema: "typing-feel-admin/1",
    contract: 1,
    keyboard: {
      defaultSet: "deep",
      families: [{ id: "deep", name: "Deep", order: 0 }, { id: "crisp", name: "Crisp", order: 1 }],
      sets: [set("deep", "deep", 0), set("deep-amber", "deep", 1), set("crisp", "crisp", 0), set("raindrop-tile", "crisp", 4, { recipe: "natural-v1" })],
      retiredIds: ["old-tick"],
    },
    effects: { defaults: { style: "stamp", intensity: "normal", size: "large", volume: 1 } },
  };
}

const row = (extra = {}) => ({ id: "rain-two", name: "Rain Two", family: "crisp", order: 0, enabled: true, status: "published", assetVersionId: "media-version.new", ownerPick: false, ownerScore: 9, recipe: "natural-v1", score: null, ...extra });

test("A/B plays both takes at the quieter take's loudness; the louder one is turned down", async () => {
  const { matchedVolumes } = await listen();
  // The owner's raindrop on 30/10: raw cut -31.7 LUFS, natural -34.14 LUFS.
  const raindrop = matchedVolumes(-31.7, -34.14);
  assert.equal(raindrop.natural, 1);
  assert.equal(raindrop.raw, Math.round(10 ** (-2.44 / 20) * 1000) / 1000);
  assert.equal(raindrop.offsetDb, 2.4);
  assert.deepEqual(matchedVolumes(-20, -20), { raw: 1, natural: 1, offsetDb: 0 });
  assert.deepEqual(matchedVolumes(null, -20), { raw: 1, natural: 1, offsetDb: 0 });
  assert.deepEqual(matchedVolumes(-20, Number.NaN), { raw: 1, natural: 1, offsetDb: 0 });
  const reversed = matchedVolumes(-40, -30);
  assert.equal(reversed.raw, 1);
  assert.ok(reversed.natural < 1 && reversed.natural > 0.3);
});

test("blind mode shuffles the two takes", async () => {
  const { blindOrder } = await listen();
  assert.deepEqual(blindOrder(() => 0.1), ["raw", "natural"]);
  assert.deepEqual(blindOrder(() => 0.9), ["natural", "raw"]);
  const seen = new Set(Array.from({ length: 64 }, () => blindOrder().join(",")));
  assert.equal(seen.size, 2);
});

test("the key grid lists keys then spaces with lengths, lead-ins and warnings", async () => {
  const { keyGrid, acceptLock } = await listen();
  const report = {
    status: "formatted",
    warnings: [],
    acceptAllowed: true,
    counts: { key: 2, space: 1 },
    minimum: { key: 10, space: 3 },
    files: [
      { file: "space-01.ogg", set: "space", durationMs: 535, leadIn: true, mainStrikeMs: 205.6, gates: { tail: true } },
      { file: "key-02.ogg", set: "key", durationMs: 270, phaseWarning: true, stereoCorrelation: -0.14, gates: { tail: false, clip: true } },
      { file: "key-01.ogg", set: "key", durationMs: 450, leadIn: false, mainStrikeMs: 2 },
    ],
  };
  const grid = keyGrid(report);
  assert.deepEqual(grid.map((cell) => [cell.label, cell.durationMs, cell.leadInMs]), [["key-01", 450, null], ["key-02", 270, null], ["space-01", 535, 206]]);
  assert.match(grid[1].warnings.join(" "), /correlation -0\.14/);
  assert.match(grid[1].warnings.join(" "), /Hard gate failed: tail/);
  assert.match(grid[2].warnings[0], /main strike 206 ms later \(kept as recorded\)/);
  assert.deepEqual(keyGrid(null), []);

  assert.equal(acceptLock(report), null);
  assert.match(acceptLock({ ...report, acceptAllowed: false }), /2 keys and 1 spaces; a set needs at least 10 keys and 3 spaces/);
  assert.match(acceptLock({ ...report, acceptAllowed: false, counts: { key: 12, space: 8 }, gates: { pass: false, failed: ["key-02.ogg:tail"] } }), /Hard gates failed: key-02\.ogg:tail/);
  assert.equal(acceptLock(null), "Format the take first.");
  assert.equal(acceptLock({ ...report, status: "refused" }), "Format the take first.");
});

test("the page names a take the way the tool does and refuses what is not a WAV under 50 MB", async () => {
  const { slugFromName, titleFromName, takeFileProblem } = await listen();
  assert.equal(slugFromName("raindrop.wav"), "raindrop");
  assert.equal(slugFromName("Hail Stone v4.WAV"), "hail-stone-v4");
  assert.equal(slugFromName("off.wav"), "new-set");
  assert.equal(titleFromName("hail-v4.wav"), "Hail V4");
  const limit = 50 * 1024 * 1024;
  assert.equal(takeFileProblem({ name: "raindrop.wav", size: 1_536_770 }, limit), null);
  assert.equal(takeFileProblem({ name: "RAIN.WAV", size: 10 }, limit), null);
  assert.match(takeFileProblem({ name: "take.mp3", size: 10 }, limit), /not a WAV file/);
  assert.equal(takeFileProblem({ name: "big.wav", size: limit + 1 }, limit), "big.wav is 50.01 MB; the limit is 50 MB.", "just over the limit never reads as the limit");
  assert.equal(takeFileProblem({ name: "big.wav", size: 51 * 1024 * 1024 }, limit), "big.wav is 51 MB; the limit is 50 MB.");
  assert.match(takeFileProblem({ name: "empty.wav", size: 0 }, limit), /is empty/);
});

test("decision 5: 9 or more is Published, under 9 Provisional, no score no status", async () => {
  const { acceptStatus } = await model();
  assert.equal(acceptStatus(9), "published");
  assert.equal(acceptStatus(10), "published");
  assert.equal(acceptStatus(8.5), "provisional");
  assert.equal(acceptStatus(0), "provisional");
  assert.equal(acceptStatus(null), null);
  assert.equal(acceptStatus(11), null);
  assert.equal(acceptStatus(Number.NaN), null);
});

test("an accepted set joins the end of its family; live, retired and reserved ids are refused", async () => {
  const { addSet, newSetIdProblem, familySets } = await model();
  const base = seed();
  const added = addSet(base, row());
  assert.equal(added.error, null);
  const crisp = familySets(added.config, "crisp");
  assert.deepEqual(crisp.map((set) => [set.id, set.order]), [["crisp", 0], ["raindrop-tile", 4], ["rain-two", 5]]);
  assert.equal(base.keyboard.sets.length, 4, "edits never change their input");
  assert.equal(added.config.keyboard.defaultSet, "deep", "a new set never becomes the default by itself");

  assert.match(addSet(added.config, row()).error, /already a set in this draft/);
  assert.match(addSet(base, row({ id: "old-tick" })).error, /was retired and is never used again/);
  assert.match(addSet(base, row({ id: "gone" }), { retired: ["gone"] }).error, /was retired/);
  assert.match(addSet(base, row({ id: "off" })).error, /reserved/);
  assert.match(addSet(base, row({ id: "Bad Id" })).error, /lower-case/);
  assert.match(addSet(base, row({ family: "nope" })).error, /Family nope is not in this draft/);
  assert.match(addSet(base, row({ ownerScore: null })).error, /owner's listening score/);
  assert.match(addSet(base, row({ ownerScore: 8 })).error, /under 9 can only be Provisional/);
  assert.match(addSet(base, row({ ownerScore: 8, status: "provisional" })).error, /needs a note/);
  assert.equal(addSet(base, row({ ownerScore: 8, status: "provisional", note: "Spaces too dull." })).error, null);
  assert.match(addSet(base, row({ ownerScore: 9.5, status: "provisional", note: "x" })).error, /9 or more is Published/);
  assert.equal(newSetIdProblem(base, "fresh-id"), null);
});
