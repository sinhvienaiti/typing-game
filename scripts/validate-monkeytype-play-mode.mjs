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

console.log("Monkeytype local-static Play build configuration PASS");
