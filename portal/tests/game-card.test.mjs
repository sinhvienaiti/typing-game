import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

const { games } = JSON.parse(await readFile(new URL("../public/games.json", import.meta.url), "utf8"));
const legacy = JSON.parse(await readFile(new URL("./fixtures/legacy-games.json", import.meta.url), "utf8"));
const expectedNames = {
  "dragon-hold": "Dragonhold",
  "typing-defense": "Wordwoven",
  "typing-survival": "Last Line",
};
const expectedOrder = [
  "monkeytype", "vocab-shooter", "recall-typing", "karaoke-typing", "space-typing",
  "dragon-hold", "typing-defense", "typing-survival", "immortality-cultivation",
];
const sample = {
  id: "dragon-hold", name: "Dragonhold", description: "A test description.",
  appUrl: "https://dragon.typing-game.local",
  art: {
    icon: "/assets/dragon-hold/portal/icon-192.png",
    cover: "/assets/dragon-hold/portal/cover-wide.webp",
  },
};
// Import inside each test so the red run records each missing contract independently.
const helpers = () => import("../src/game-card.ts");

for (const [id, name] of Object.entries(expectedNames)) {
  const game = games.find((entry) => entry.id === id);
  test(`${id} has its English name`, () => assert.equal(game.name, name));
  test(`${id} has one English description of 50–110 characters`, () => {
    assert.ok(game.description.length >= 50 && game.description.length <= 110);
    assert.match(game.description, /^[^.?!]+\.$/u);
    assert.doesNotMatch(game.description, /[^\x20-\x7e]/u);
    assert.doesNotMatch(game.description, /\p{Extended_Pictographic}/u);
  });
  test(`${id} has game-owned art paths and no legacy icon field`, () => {
    assert.equal(Object.hasOwn(game, "icon"), false);
    assert.deepEqual(game.art, {
      icon: `/assets/${id}/portal/icon-192.png`,
      cover: `/assets/${id}/portal/cover-wide.webp`,
    });
  });
  test(`${id} model contains only images with the required metadata`, async () => {
    const { gameCardModel } = await helpers();
    const model = gameCardModel(game);
    assert.deepEqual(model, {
      title: name, description: game.description, glyph: null,
      icon: { src: `${game.appUrl}/assets/${id}/portal/icon-192.png`, alt: "", width: 192, height: 192 },
      cover: { src: `${game.appUrl}/assets/${id}/portal/cover-wide.webp`, alt: `${name} cover art`, width: 1600, height: 900 },
    });
  });
}

test("the six legacy entries keep every value and their order", () => {
  assert.equal(legacy.length, 6);
  assert.deepEqual(games.filter((game) => !Object.hasOwn(expectedNames, game.id)), legacy);
});

test("all registry ids retain their original order", () => {
  assert.deepEqual(games.map((game) => game.id), expectedOrder);
});

test("new entries retain routes, origins and groups", () => {
  for (const [id, host] of [["dragon-hold", "dragon"], ["typing-defense", "td"], ["typing-survival", "survival"]]) {
    const game = games.find((entry) => entry.id === id);
    assert.equal(game.path, `/${id}`);
    assert.equal(game.appUrl, `https://${host}.typing-game.local`);
    assert.equal(game.group, "battle");
  }
});

test("valid art resolves to absolute game-origin URLs without mutating input", async () => {
  const { resolveGameArt } = await helpers();
  const input = structuredClone(sample);
  assert.deepEqual(resolveGameArt(input), {
    icon: sample.appUrl + sample.art.icon, cover: sample.appUrl + sample.art.cover,
  });
  assert.deepEqual(input, sample);
});

for (const [label, art] of [
  ["missing", undefined], ["null", null], ["empty", {}],
  ["numeric values", { icon: 192, cover: 900 }],
]) {
  test(`resolveGameArt rejects ${label} art`, async () => {
    const { resolveGameArt } = await helpers();
    assert.deepEqual(resolveGameArt({ ...sample, art }), { icon: null, cover: null });
  });
}

for (const path of [
  "/assets/space-typing/portal/a.png",
  "/assets/dragon-hold/portal-other/a.png",
  "https://evil.example/a.png", "//evil.example/a.png",
  "/assets/dragon-hold/portal/../a.png",
  "/assets/dragon-hold/portal/a\\b.png",
  "/assets/dragon-hold/portal//a.png",
  "/assets/dragon-hold/portal/a.png?size=192",
  "/assets/dragon-hold/portal/a.png#icon",
  "/assets/dragon-hold/portal/%2e%2e/a.png",
]) {
  test(`resolveGameArt rejects unsafe path ${JSON.stringify(path)} independently`, async () => {
    const { resolveGameArt } = await helpers();
    assert.deepEqual(resolveGameArt({ ...sample, art: { icon: path, cover: sample.art.cover } }), {
      icon: null, cover: sample.appUrl + sample.art.cover,
    });
    assert.deepEqual(resolveGameArt({ ...sample, art: { icon: sample.art.icon, cover: path } }), {
      icon: sample.appUrl + sample.art.icon, cover: null,
    });
  });
}

for (const suffix of ["/", "/play/session", "/play/session/"]) {
  test(`appUrl suffix ${suffix} retains the origin and root asset path`, async () => {
    const { resolveGameArt } = await helpers();
    const result = resolveGameArt({ ...sample, appUrl: sample.appUrl + suffix });
    assert.deepEqual(result, { icon: sample.appUrl + sample.art.icon, cover: sample.appUrl + sample.art.cover });
    assert.equal(new URL(result.icon).origin, new URL(sample.appUrl + suffix).origin);
    assert.equal(new URL(result.cover).origin, new URL(sample.appUrl + suffix).origin);
  });
}

test("invalid appUrl yields no images", async () => {
  const { resolveGameArt } = await helpers();
  assert.deepEqual(resolveGameArt({ ...sample, appUrl: "not a URL" }), { icon: null, cover: null });
});

test("art suppresses a legacy glyph even when images are invalid or absent", async () => {
  const { gameCardModel } = await helpers();
  for (const art of [sample.art, {}, null, undefined, { icon: 192, cover: 900 }]) {
    assert.equal(gameCardModel({ ...sample, art, icon: legacy[0].icon }).glyph, null);
  }
});

test("legacy entries retain their glyph, title and description without art", async () => {
  const { gameCardModel } = await helpers();
  for (const game of legacy) {
    assert.deepEqual(gameCardModel(game), {
      title: game.name, description: game.description, glyph: game.icon, icon: null, cover: null,
    });
  }
});

test("an entry without art or a legacy icon has no glyph", async () => {
  const { gameCardModel } = await helpers();
  const { art, ...withoutArt } = sample;
  assert.equal(gameCardModel(withoutArt).glyph, null);
});

function fakeImage() {
  const listeners = [];
  return {
    hidden: false,
    listeners,
    addEventListener(type, callback, options) { listeners.push({ type, callback, options }); },
    emit(type) {
      for (const entry of [...listeners]) {
        if (entry.type !== type) continue;
        if (entry.options?.once) listeners.splice(listeners.indexOf(entry), 1);
        entry.callback();
      }
    },
  };
}

test("image error hides the image and its cover frame exactly once", async () => {
  const { hideImageOnError } = await helpers();
  const img = fakeImage();
  const frame = { hidden: false };
  let calls = 0;
  hideImageOnError(img, () => { frame.hidden = true; calls += 1; });
  assert.equal(img.hidden, false);
  assert.equal(frame.hidden, false);
  assert.equal(calls, 0);
  assert.equal(img.listeners.length, 1);
  assert.equal(img.listeners[0].type, "error");
  assert.equal(img.listeners[0].options.once, true);
  img.emit("load");
  assert.equal(img.hidden, false);
  img.emit("error");
  img.emit("error");
  assert.equal(img.hidden, true);
  assert.equal(frame.hidden, true);
  assert.equal(calls, 1);
});

test("image error needs no optional callback", async () => {
  const { hideImageOnError } = await helpers();
  const img = fakeImage();
  hideImageOnError(img);
  img.emit("error");
  assert.equal(img.hidden, true);
});

test("main.ts does not read game.icon directly", async () => {
  const source = await readFile(new URL("../src/main.ts", import.meta.url), "utf8");
  assert.doesNotMatch(source, /game\.icon/u);
});

for (const suffix of [
  "%2e%2e/a.png",
  "%2E%2E/a.png",
  "%2F/a.png",
  "%2e%2e%2F%2e%2e%2Fspace-typing/portal/icon.png",
  "%2E%2E%2f%2E%2E%2fspace-typing/portal/icon.png",
  "%2e%2e%5C%2e%2e%5Cspace-typing/portal/icon.png",
  "%2e%2e%2F%2e%2e%5cspace-typing/portal/icon.png",
  "%252e%252e%252F%252e%252e%252Fspace-typing/portal/icon.png",
  "%252e%252e%255C%252e%252e%255Cspace-typing/portal/icon.png",
  "%252e%2e%252f%2e%252e%5Cspace-typing/portal/icon.png",
  "%25252e%25252e%25252fspace-typing/portal/icon.png",
  "a%2Fb.png", "a%5Cb.png", "a%252Fb.png", "a%255Cb.png",
  "a.png%253Fsize=192", "a.png%2523icon", "%zz.png",
]) {
  test(`F5 rejects fully decoded unsafe art ${suffix}`, async () => {
    const { resolveGameArt } = await helpers();
    const path = "/assets/dragon-hold/portal/" + suffix;
    for (const appUrl of [sample.appUrl, sample.appUrl + "/play/session/", "HTTPS://DRAGON.TYPING-GAME.LOCAL"]) {
      assert.deepEqual(resolveGameArt({ ...sample, appUrl, art: { icon: path, cover: sample.art.cover } }), {
        icon: null, cover: sample.appUrl + sample.art.cover,
      });
      assert.deepEqual(resolveGameArt({ ...sample, appUrl, art: { icon: sample.art.icon, cover: path } }), {
        icon: sample.appUrl + sample.art.icon, cover: null,
      });
    }
  });
}

test("F5 preserves safe encoded filenames within the game prefix", async () => {
  const { resolveGameArt } = await helpers();
  for (const suffix of ["a%20b.png", "%69con.png", "a%2520b.png"]) {
    const path = "/assets/dragon-hold/portal/" + suffix;
    assert.equal(resolveGameArt({ ...sample, art: { icon: path } }).icon, sample.appUrl + path);
  }
});
