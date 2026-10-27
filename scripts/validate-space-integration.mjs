import fs from "node:fs";

function read(path) {
  return fs.readFileSync(new URL("../" + path, import.meta.url), "utf8");
}

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

const expectedGames = [
  {
    id: "monkeytype",
    path: "/monkeytype",
    appUrl: "https://monkeytype.typing-game.local",
    submodule: "games/monkeytype",
  },
  {
    id: "vocab-shooter",
    path: "/vocab-shooter",
    appUrl: "https://shooter.typing-game.local",
    submodule: "games/vocab-shooter",
  },
  {
    id: "recall-typing",
    path: "/recall-typing",
    appUrl: "https://recall.typing-game.local",
    submodule: "games/recall-typing",
  },
  {
    id: "karaoke-typing",
    path: "/karaoke-typing",
    appUrl: "https://karaoke.typing-game.local",
    submodule: "games/karaoke-typing",
  },
  {
    id: "space-typing",
    path: "/space-typing",
    appUrl: "https://space.typing-game.local",
    submodule: "games/space-typing",
  },
  // Split from Space Typing; submodules are registered once their repos exist.
  {
    id: "dragon-hold",
    path: "/dragon-hold",
    appUrl: "https://dragon.typing-game.local",
    submodule: "games/dragon-hold",
    pendingSubmodule: true,
  },
  {
    id: "typing-defense",
    path: "/typing-defense",
    appUrl: "https://td.typing-game.local",
    submodule: "games/typing-defense",
    pendingSubmodule: true,
  },
  {
    id: "typing-survival",
    path: "/typing-survival",
    appUrl: "https://survival.typing-game.local",
    submodule: "games/typing-survival",
    pendingSubmodule: true,
  },
  {
    id: "immortality-cultivation",
    path: "/immortality-cultivation",
    appUrl: "https://tutien.typing-game.local",
    submodule: "games/immortality-cultivation",
  },
];

const registry = JSON.parse(read("portal/public/games.json"));
assert(Array.isArray(registry.games), "portal game registry must contain games[]");

const ids = registry.games.map((game) => game.id);
assert(
  JSON.stringify(ids) === JSON.stringify(expectedGames.map((game) => game.id)),
  "portal game order/routes changed unexpectedly",
);

for (const expected of expectedGames) {
  const game = registry.games.find((entry) => entry.id === expected.id);
  assert(game !== undefined, expected.id + " is missing from portal registry");
  assert(game.path === expected.path, expected.id + " route changed");
  assert(game.appUrl === expected.appUrl, expected.id + " origin changed");
}

const gitmodules = read(".gitmodules");
for (const expected of expectedGames) {
  if (gitmodules.includes("path = " + expected.submodule)) continue;
  if (expected.pendingSubmodule) {
    console.warn("WARN " + expected.submodule + " is not a submodule yet.");
    continue;
  }
  assert(false, expected.submodule + " is missing from .gitmodules");
}

const packageJson = JSON.parse(read("package.json"));
for (const name of [
  "dev:space",
  "dev:space:app",
  "build:space",
]) {
  assert(
    typeof packageJson.scripts?.[name] === "string",
    "missing package script " + name,
  );
}

const devLauncher = read("dev.sh");
assert(
  devLauncher.includes("space-typing") && devLauncher.includes("pnpm dev:space"),
  "dev.sh does not expose the Space Typing launcher",
);

const playLauncher = read("play.sh");
assert(
  playLauncher.includes('"Space Typing"') &&
    playLauncher.includes('"build:space"'),
  "play.sh does not include Space Typing static build checks",
);

for (const nginxFile of [
  "infra/nginx/typing-game.local.dev.conf",
  "infra/nginx/typing-game.local.play.conf",
]) {
  const nginx = read(nginxFile);
  for (const expected of expectedGames) {
    const host = new URL(expected.appUrl).hostname;
    assert(
      nginx.includes(host),
      nginxFile + " is missing host " + host,
    );
  }
  assert(
    nginx.includes("location /vocabulary/") &&
      nginx.includes("shared/vocabulary/"),
    nginxFile + " must expose shared vocabulary",
  );
  assert(
    nginx.includes("location /shared/typing-texts/") &&
      nginx.includes("shared/typing-texts/"),
    nginxFile + " must expose Space Typing shared typing texts",
  );
}

console.log(
  "Space Typing integration contract is valid; existing game routes remain unchanged.",
);
