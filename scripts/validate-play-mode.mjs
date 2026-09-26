import { readFile } from "node:fs/promises";

const play = await readFile("play.sh", "utf8");
const nginx = await readFile(
  "infra/nginx/typing-game.local.play.conf",
  "utf8",
);

const setupNginx = await readFile("scripts/setup-nginx.sh", "utf8");
const leafPlay = await readFile("scripts/play.sh", "utf8");
const devNginx = await readFile(
  "infra/nginx/typing-game.local.dev.conf",
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


for (const [name, config] of [
  ["play", nginx],
  ["dev", devNginx],
]) {
  if (config.includes("/Users/jokerit/")) {
    failures.push(`${name} nginx config still hard-codes the old macOS project path`);
  }
  if (!config.includes("__ROOT_DIR__")) {
    failures.push(`${name} nginx config is missing the runtime project-root token`);
  }
  if (!config.includes("__SSL_CERT__") || !config.includes("__SSL_KEY__")) {
    failures.push(`${name} nginx config is missing portable TLS tokens`);
  }
}

for (const required of [
  'PLATFORM="macos"',
  'PLATFORM="linux"',
  'NGINX_BASE="/etc/nginx"',
  'NGINX_BASE="/usr/local/etc/nginx"',
  "render_config",
  "migrate_legacy_linux_certificate",
  "sudo nginx -t",
  "brew services restart nginx",
]) {
  if (!setupNginx.includes(required)) {
    failures.push(`setup-nginx.sh is missing cross-platform contract: ${required}`);
  }
}

if (!play.includes("bash scripts/setup-nginx.sh play")) {
  failures.push("Top-level play.sh does not use the platform-aware nginx setup.");
}

for (const opener of ["open", "wslview", "cmd.exe", "powershell.exe", "xdg-open"]) {
  if (!leafPlay.includes(opener)) {
    failures.push(`scripts/play.sh is missing URL opener fallback: ${opener}`);
  }
}

if (failures.length > 0) {
  for (const failure of failures) console.error(failure);
  process.exit(1);
}

console.log(
  "Play mode contract PASS: all static apps, shared runtime data, and Portal shared-learning rebuild dependency are covered.",
);
