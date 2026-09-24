import { readFile } from "node:fs/promises";

const play = await readFile("play.sh", "utf8");
const nginx = await readFile(
  "infra/nginx/typing-game.local.play.conf",
  "utf8",
);

const failures = [];

for (const output of [
  "portal/dist/index.html",
  "games/vocab-shooter/dist/index.html",
  "games/recall-typing/dist/index.html",
  "games/karaoke-typing/dist/index.html",
  "games/space-typing/dist/index.html",
  "games/monkeytype/frontend/dist/index.html",
]) {
  if (!play.includes(output)) {
    failures.push(`Play mode does not track static output: ${output}`);
  }
}

if (!play.includes('"shared/learning"')) {
  failures.push(
    "Portal stale-build detection does not include shared/learning",
  );
}

for (const route of ["/vocabulary/", "/typing-texts/", "/music/"]) {
  if (!nginx.includes(`location ${route}`)) {
    failures.push(`Play nginx does not expose runtime shared data: ${route}`);
  }
}

for (const host of [
  "typing-game.local",
  "monkeytype.typing-game.local",
  "shooter.typing-game.local",
  "recall.typing-game.local",
  "karaoke.typing-game.local",
  "space.typing-game.local",
]) {
  if (!nginx.includes(`server_name ${host}`) &&
      !nginx.includes(` ${host}`)) {
    failures.push(`Play nginx is missing host: ${host}`);
  }
}

if (failures.length > 0) {
  for (const failure of failures) console.error(failure);
  process.exit(1);
}

console.log(
  "Play mode contract PASS: all static apps, shared runtime data, and Portal shared-learning rebuild dependency are covered.",
);
