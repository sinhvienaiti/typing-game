import { existsSync } from "node:fs";
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

function serverBlockFor(config, serverName) {
  const marker = `server_name ${serverName};`;
  const markerIndex = config.indexOf(marker);
  if (markerIndex < 0) return null;
  const start = config.lastIndexOf("server {", markerIndex);
  if (start < 0) return null;
  let depth = 0;
  for (let index = start; index < config.length; index += 1) {
    if (config[index] === "{") depth += 1;
    if (config[index] === "}") {
      depth -= 1;
      if (depth === 0) return config.slice(start, index + 1);
    }
  }
  return null;
}

// Games split out of Space Typing; their directories may not exist yet.
const NEW_GAMES = [
  { dir: "dragon-hold", host: "dragon.typing-game.local", port: 3005, script: "dragon" },
  { dir: "typing-defense", host: "td.typing-game.local", port: 3006, script: "td" },
  {
    dir: "typing-survival",
    host: "survival.typing-game.local",
    port: 3007,
    script: "survival",
    aliases: ["/assets/space-typing/models/"],
  },
];

const packageJson = JSON.parse(await readFile("package.json", "utf8"));
function httpRedirectBlock(config) {
  const listen = config.indexOf("listen 80;");
  if (listen < 0) return "";
  return config.slice(config.lastIndexOf("server {", listen), config.indexOf("}", listen) + 1);
}
const redirectServer = httpRedirectBlock(nginx);
const devRedirectServer = httpRedirectBlock(devNginx);

for (const game of NEW_GAMES) {
  const output = `games/${game.dir}/dist/index.html`;
  if (!play.includes(`"${output}"`)) {
    failures.push(`Play mode does not build ${game.dir}: ${output}`);
  }
  if (!leafPlay.includes(`/${output}`)) {
    failures.push(`scripts/play.sh does not check ${output}`);
  }
  if (!setupNginx.includes(`"${game.host}"`)) {
    failures.push(`setup-nginx.sh HOSTS is missing ${game.host}`);
  }
  for (const [name, redirect] of [["play", redirectServer], ["dev", devRedirectServer]]) {
    if (!redirect.includes(` ${game.host}`)) {
      failures.push(`${name} nginx HTTP redirect is missing ${game.host}`);
    }
  }

  const playServer = serverBlockFor(nginx, game.host);
  if (playServer === null) {
    failures.push(`Play nginx is missing the ${game.host} HTTPS server block.`);
  } else {
    if (!playServer.includes(`root __ROOT_DIR__/games/${game.dir}/dist;`)) {
      failures.push(`Play nginx ${game.host} does not serve games/${game.dir}/dist`);
    }
    for (const route of ["/vocabulary/", "/typing-texts/", ...(game.aliases ?? [])]) {
      if (!playServer.includes(`location ${route} `)) {
        failures.push(`Play nginx ${game.host} does not expose ${route}`);
      }
    }
  }

  const devServer = serverBlockFor(devNginx, game.host);
  if (devServer === null) {
    failures.push(`Dev nginx is missing the ${game.host} HTTPS server block.`);
  } else {
    if (!devServer.includes(`proxy_pass http://127.0.0.1:${game.port};`)) {
      failures.push(`Dev nginx ${game.host} does not proxy to port ${game.port}`);
    }
    if (!devServer.includes('proxy_set_header Upgrade $http_upgrade;')) {
      failures.push(`Dev nginx ${game.host} does not forward the Vite HMR WebSocket`);
    }
    for (const route of ["/vocabulary/", "/typing-texts/", ...(game.aliases ?? [])]) {
      if (!devServer.includes(`location ${route} `)) {
        failures.push(`Dev nginx ${game.host} does not expose ${route}`);
      }
    }
  }

  const scripts = packageJson.scripts ?? {};
  const appScript = scripts[`dev:${game.script}:app`] ?? "";
  if (!appScript.includes(`DEV_ALLOWED_HOSTS=${game.host}`) ||
      !appScript.includes(`DEV_HMR_HOST=${game.host}`)) {
    failures.push(`package.json dev:${game.script}:app does not target ${game.host}`);
  }
  if (typeof scripts[`dev:${game.script}`] !== "string" ||
      typeof scripts[`build:${game.script}`] !== "string") {
    failures.push(`package.json is missing dev:${game.script} or build:${game.script}`);
  }
  if (!(scripts.dev ?? "").includes(`pnpm dev:${game.script}:app`) ||
      !(scripts.dev ?? "").includes(String(game.port))) {
    failures.push(`package.json dev does not start or clean up ${game.dir}`);
  }
  if (!(scripts["build:local"] ?? "").includes(`pnpm build:${game.script}`)) {
    failures.push(`package.json build:local does not build ${game.dir}`);
  }

  if (!existsSync(`games/${game.dir}/package.json`)) {
    console.warn(
      `WARN games/${game.dir} is not checked out yet; its config is checked, its build is skipped.`,
    );
  }
}

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
  ...NEW_GAMES.map((game) => game.host),
]) {
  if (!nginx.includes(`server_name ${host}`) &&
      !nginx.includes(` ${host}`)) {
    failures.push(`Play nginx is missing host: ${host}`);
  }
}

const portalPlayServer = serverBlockFor(nginx, "typing-game.local");
if (portalPlayServer === null) {
  failures.push("Play nginx is missing the typing-game.local HTTPS server block.");
} else {
  const adminLocation = "location /api/admin/space-typing/";
  const spaFallback = "location / { try_files $uri $uri/ /index.html; }";
  const adminLocationIndex = portalPlayServer.indexOf(adminLocation);
  const spaFallbackIndex = portalPlayServer.indexOf(spaFallback);

  if (adminLocationIndex < 0) {
    failures.push("Play nginx does not proxy Space Typing Admin API requests.");
  }
  if (!portalPlayServer.includes("proxy_pass http://127.0.0.1:3199;")) {
    failures.push("Play nginx Space Typing Admin API does not target the Admin service on port 3199.");
  }
  if (spaFallbackIndex < 0) {
    failures.push("Play nginx Portal server is missing its SPA fallback.");
  } else if (adminLocationIndex >= 0 && adminLocationIndex > spaFallbackIndex) {
    failures.push("Play nginx Admin API proxy must be declared before the Portal SPA fallback.");
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
  '--prefix',
  "render_config",
  "migrate_legacy_linux_certificate",
  "sudo nginx -t",
  'sudo "$NGINX_BIN" -t',
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
  "Play mode contract PASS: static apps, shared runtime data, Space Typing Admin API routing, Portal shared-learning rebuild dependency, and the dragon/td/survival hosts are covered.",
);
