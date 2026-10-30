import { readFileSync } from "node:fs";
import assert from "node:assert/strict";

const platform = JSON.parse(readFileSync("package.json", "utf8"));
const monkeyTurbo = JSON.parse(
  readFileSync("games/monkeytype/turbo.json", "utf8"),
);
const buildScript = platform.scripts["build:monkeytype"];
const buildEnvironment =
  monkeyTurbo.tasks["@monkeytype/frontend#build"]?.env ?? [];

assert.match(
  buildScript,
  /LOCAL_STATIC=true/,
  "Play-mode Monkeytype build must explicitly enable LOCAL_STATIC",
);
assert.ok(
  buildEnvironment.includes("LOCAL_STATIC"),
  "Turbo strict environment must forward LOCAL_STATIC to Monkeytype Vite",
);

// Typing Feel (docs/games/TYPING_FEEL_SERVICE.md B6): the home build reads keyboard sounds from the feel host.
const devScript = platform.scripts["dev:monkeytype:app"];
const devEnvironment = monkeyTurbo.tasks["@monkeytype/frontend#dev"]?.env ?? [];
for (const [name, script] of [["build:monkeytype", buildScript], ["dev:monkeytype:app", devScript]]) {
  assert.match(
    script,
    /TYPING_FEEL_URL=https:\/\/feel\.typing-game\.local(\s|$)/,
    `${name} must set TYPING_FEEL_URL to the home Typing Feel host`,
  );
}
assert.doesNotMatch(buildScript, /sync-keys/, "build:monkeytype must not run the removed sync-keys copy");
assert.ok(
  buildEnvironment.includes("TYPING_FEEL_URL") && devEnvironment.includes("TYPING_FEEL_URL"),
  "Turbo strict environment must forward TYPING_FEEL_URL to Monkeytype build and dev",
);

console.log("Monkeytype local-static Play build configuration PASS");
