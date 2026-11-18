import { existsSync } from "node:fs";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

export const SELF_SERVED_HOSTS = [
  "dragon.typing-game.local",
  "td.typing-game.local",
  "survival.typing-game.local",
];
export const SHARED_DATA_ROUTES = ["/vocabulary/", "/typing-texts/", "/shared/typing-texts/"];
// Folders a game host must never alias: shared data, and Typing Feel, which games
// read across origins from FEEL_HOST (a same-origin alias would hide CORS bugs).
export const SHARED_DATA_ROOTS = ["__ROOT_DIR__/shared/", "__ROOT_DIR__/typing-feel/"];

// Typing Feel host (docs/games/TYPING_FEEL_SERVICE.md §4.2, §6.2): static files only.
export const FEEL_HOST = "feel.typing-game.local";
export const FEEL_CATALOGUE = "typing-feel/public/v1/keys/keys-manifest.json";
const FEEL_ROOT = "__ROOT_DIR__/typing-feel/";
const FEEL_HEADERS = [
  ["Access-Control-Allow-Origin", "*"],
  ["Cross-Origin-Resource-Policy", "cross-origin"],
  ["X-Content-Type-Options", "nosniff"],
];
const IMMUTABLE = "public, max-age=31536000, immutable";
const FEEL_LOCATIONS = [
  { route: "/v1/keys/sets/", alias: `${FEEL_ROOT}public/v1/keys/sets/`, cache: IMMUTABLE, ogg: true },
  { route: "= /v1/health.json", alias: `${FEEL_ROOT}public/v1/health.json`, cache: "no-cache" },
  { route: "/v1/keys/", alias: `${FEEL_ROOT}public/v1/keys/`, cache: "no-cache" },
  { route: "/", cache: "no-cache", tryFiles: ["$uri", "=404"] },
];

// Tokenize nginx directives while keeping source offsets and ignoring comments.
// Quoted or escaped braces are values, never block delimiters.
function configTree(config) {
  const tokens = [];
  let line = 1;
  for (let index = 0; index < config.length;) {
    const char = config[index];
    if (/\s/.test(char)) {
      if (char === "\n") line += 1;
      index += 1;
    } else if (char === "#") {
      while (index < config.length && config[index] !== "\n") index += 1;
    } else if ("{};".includes(char)) {
      tokens.push({ value: char, delimiter: true, start: index, end: index + 1, line });
      index += 1;
    } else {
      const start = index;
      const startLine = line;
      let value = "";
      let quote = null;
      while (index < config.length) {
        const next = config[index];
        if (next === "\\" && index + 1 < config.length) {
          index += 1;
          value += config[index];
          if (config[index] === "\n") line += 1;
          index += 1;
        } else if (quote) {
          if (next === quote) quote = null;
          else value += next;
          if (next === "\n") line += 1;
          index += 1;
        } else if (next === '"' || next === "'") {
          quote = next;
          index += 1;
        } else if (/\s/.test(next) || "{};#".includes(next)) {
          break;
        } else {
          value += next;
          index += 1;
        }
      }
      tokens.push({ value, start, end: index, line: startLine });
    }
  }
  const root = { children: [] };
  const stack = [root];
  const errors = [];
  let pending = [];
  for (const token of tokens) {
    if (!token.delimiter) {
      pending.push(token);
    } else if (token.value === "}" ) {
      if (stack.length === 1) errors.push(`unexpected closing brace (line ${token.line})`);
      else stack.pop().end = token.end;
      pending = [];
    } else {
      const node = {
        name: pending[0]?.value,
        args: pending.slice(1).map((part) => part.value),
        start: pending[0]?.start ?? token.start,
        line: pending[0]?.line ?? token.line,
        end: token.end,
        children: [],
      };
      stack.at(-1).children.push(node);
      pending = [];
      if (token.value === "{") stack.push(node);
    }
  }
  for (const node of stack.slice(1)) errors.push(`unclosed opening brace (line ${node.line})`);
  return { servers: root.children.filter((node) => node.name === "server"), errors };
}

function namesHost(server, host) {
  return server.children.some((node) => node.name === "server_name" &&
    node.args.length === 1 && node.args[0] === host);
}

export function configStructureErrors(config) {
  const { servers, errors } = configTree(config);
  for (const host of [...SELF_SERVED_HOSTS, "tutien.typing-game.local"]) {
    const count = servers.filter((server) => namesHost(server, host)).length;
    if (count !== 1) errors.push(`must have exactly one server_name ${host}; block (found ${count})`);
  }
  return errors;
}

function serverBlockFor(config, serverName) {
  const server = configTree(config).servers.find((node) => namesHost(node, serverName) &&
    node.children.some((child) => child.name === "listen" && child.args.includes("443")));
  return server ? config.slice(server.start, server.end) : null;
}

export function sharedDataAliases(config, host) {
  const block = serverBlockFor(config, host);
  if (block === null) return [];
  const offset = config.slice(0, config.indexOf(block)).split("\n").length - 1;
  const found = [];
  function visit(nodes, location = null) {
    for (const node of nodes) {
      if (node.name === "location") {
        const route = node.args.filter((arg) => !["=", "^~", "~", "~*"].includes(arg)).join(" ");
        const entry = { host, route, line: offset + node.line };
        const forbidden = SHARED_DATA_ROUTES.some((prefix) => route.startsWith(prefix.slice(0, -1)));
        const sharedTarget = (children) => children.some((child) =>
          (["alias", "root"].includes(child.name) && SHARED_DATA_ROOTS.some((root) => child.args[0]?.startsWith(root))) ||
          (child.name !== "location" && sharedTarget(child.children)));
        if (forbidden || sharedTarget(node.children)) found.push(entry);
        visit(node.children, entry);
      } else {
        // A server-level shared root also violates self-serving, without a location.
        if (!location && ["alias", "root"].includes(node.name) &&
            SHARED_DATA_ROOTS.some((root) => node.args[0]?.startsWith(root))) {
          found.push({ host, route: "/", line: offset + node.line });
        }
        visit(node.children, location);
      }
    }
  }
  visit(configTree(block).servers[0].children);
  return found;
}

function headerArgs(node, name) {
  return node.children.filter((child) => child.name === "add_header" && child.args[0]?.toLowerCase() === name.toLowerCase());
}

/**
 * Typing Feel host problems: one HTTPS block with http2 and gzip for JSON (the
 * §8.4 set manifest budget is the transfer size), every location repeats the
 * CORS, CORP and nosniff headers (a location's add_header drops the server's)
 * plus a Cache-Control, no SPA fallback anywhere (try_files ends in =404, no
 * error_page), alias without try_files, OGG typed audio/ogg and never gzipped,
 * and only typing-feel/ served. The immutable Cache-Control has no "always",
 * so a 404 is never cached for a year.
 */
export function feelHostErrors(config) {
  const errors = [];
  const servers = configTree(config).servers.filter((server) => namesHost(server, FEEL_HOST) &&
    server.children.some((child) => child.name === "listen" && child.args.includes("443")));
  if (servers.length !== 1) return [`must have exactly one HTTPS server_name ${FEEL_HOST}; block (found ${servers.length})`];
  const server = servers[0];
  if (!server.children.some((child) => child.name === "http2" && child.args[0] === "on")) {
    errors.push(`${FEEL_HOST} must turn on HTTP/2 (http2 on;, line ${server.line})`);
  }
  const gzipTypes = server.children.filter((child) => child.name === "gzip_types").flatMap((child) => child.args);
  if (!server.children.some((child) => child.name === "gzip" && child.args[0] === "on") || !gzipTypes.includes("application/json")) {
    errors.push(`${FEEL_HOST} must gzip JSON (gzip on; gzip_types application/json;, line ${server.line}): set manifests are over 4 KB raw (§8.4)`);
  }
  if (gzipTypes.some((type) => type === "*" || type.startsWith("audio/"))) {
    errors.push(`${FEEL_HOST} must not gzip audio (gzip_types ${gzipTypes.join(" ")}, line ${server.line})`);
  }
  const locations = [];
  const visit = (nodes) => {
    for (const node of nodes) {
      const where = `${FEEL_HOST} line ${node.line}`;
      if (node.name === "location") locations.push(node);
      if (node.name === "error_page") errors.push(`${where}: error_page can turn a missing file into a page; a missing file must stay 404`);
      if (node.name === "gzip" && node.args[0] !== "on") errors.push(`${where}: gzip ${node.args.join(" ")} undoes the server's JSON gzip`);
      if (node.name === "try_files" && (node.args.at(-1) !== "=404" || node.args.some((arg) => arg.includes("index.html")))) {
        errors.push(`${where}: try_files ${node.args.join(" ")} is an SPA fallback; end it with =404`);
      }
      if (["proxy_pass", "return", "rewrite"].includes(node.name)) errors.push(`${where}: ${node.name} has no place on the static Typing Feel host`);
      if (["alias", "root"].includes(node.name) && !node.args[0]?.startsWith(FEEL_ROOT)) {
        errors.push(`${where}: ${node.name} ${node.args[0]} is outside typing-feel/`);
      }
      if (node.name !== "types") visit(node.children);
    }
  };
  visit(server.children);
  for (const location of locations) {
    const route = location.args.join(" ");
    const where = `${FEEL_HOST} location ${route} (line ${location.line})`;
    for (const [name, value] of FEEL_HEADERS) {
      if (!headerArgs(location, name).some((node) => node.args[1] === value && node.args[2] === "always")) {
        errors.push(`${where} lacks add_header ${name} "${value}" always`);
      }
    }
    if (headerArgs(location, "Cache-Control").length !== 1) errors.push(`${where} needs exactly one add_header Cache-Control`);
    const alias = location.children.some((child) => child.name === "alias");
    if (alias && location.children.some((child) => child.name === "try_files")) errors.push(`${where}: alias with try_files; alias answers 404 itself`);
  }
  for (const want of FEEL_LOCATIONS) {
    const location = locations.find((node) => node.args.join(" ") === want.route);
    if (!location) {
      errors.push(`${FEEL_HOST} is missing location ${want.route}`);
      continue;
    }
    const where = `${FEEL_HOST} location ${want.route} (line ${location.line})`;
    const cache = headerArgs(location, "Cache-Control")[0];
    if (cache && cache.args[1] !== want.cache) errors.push(`${where}: Cache-Control must be "${want.cache}"`);
    if (cache && want.cache === IMMUTABLE && cache.args.includes("always")) {
      errors.push(`${where}: the immutable Cache-Control must not use always (a 404 would be cached for a year)`);
    }
    if (want.alias && !location.children.some((child) => child.name === "alias" && child.args[0] === want.alias)) {
      errors.push(`${where}: must alias ${want.alias}`);
    }
    if (want.tryFiles && !location.children.some((child) => child.name === "try_files" && child.args.join(" ") === want.tryFiles.join(" "))) {
      errors.push(`${where}: must use try_files ${want.tryFiles.join(" ")}`);
    }
    if (want.ogg && !location.children.some((child) => child.name === "types" &&
        child.children.some((type) => type.name === "audio/ogg" && type.args.includes("ogg")))) {
      errors.push(`${where}: must map ogg to audio/ogg (types { audio/ogg ogg; ... })`);
    }
  }
  return errors;
}

/**
 * Every place an HTTPS host other than FEEL_HOST serves typing-feel/ through
 * alias or root: games read Typing Feel across origins from FEEL_HOST, so a
 * same-origin copy would hide CORS bugs (the Codex 216 rule, for every host).
 */
export function feelAliases(config) {
  const found = [];
  for (const server of configTree(config).servers) {
    if (!server.children.some((child) => child.name === "listen" && child.args.includes("443"))) continue;
    if (namesHost(server, FEEL_HOST)) continue;
    const host = server.children.find((child) => child.name === "server_name")?.args.join(" ") ?? "";
    const visit = (nodes, location) => {
      for (const node of nodes) {
        if (node.name === "location") {
          visit(node.children, node);
          continue;
        }
        if (["alias", "root"].includes(node.name) && node.args[0]?.startsWith(FEEL_ROOT)) {
          const route = location ? location.args.filter((arg) => !["=", "^~", "~", "~*"].includes(arg)).join(" ") : "/";
          found.push({ host, route, line: (location ?? node).line });
        }
        visit(node.children, location);
      }
    };
    visit(server.children, null);
  }
  return found;
}

export async function main(args = process.argv.slice(2)) {
  const paths = {
    "--play-conf": "infra/nginx/typing-game.local.play.conf",
    "--dev-conf": "infra/nginx/typing-game.local.dev.conf",
  };
  for (let index = 0; index < args.length; index += 2) {
    if (!Object.hasOwn(paths, args[index]) || !args[index + 1] || args[index + 1].startsWith("--")) {
      console.error("Usage: node scripts/validate-play-mode.mjs [--play-conf <path>] [--dev-conf <path>]");
      return 2;
    }
    paths[args[index]] = args[index + 1];
  }
  const play = await readFile("play.sh", "utf8");
  const nginx = await readFile(
    paths["--play-conf"],
    "utf8",
  );

  const setupNginx = await readFile("scripts/setup-nginx.sh", "utf8");
  const leafPlay = await readFile("scripts/play.sh", "utf8");
  const devNginx = await readFile(
    paths["--dev-conf"],
    "utf8",
  );

  const failures = [];

  // Games split out of Space Typing; their directories may not exist yet.
  const NEW_GAMES = [
    { dir: "dragon-hold", host: "dragon.typing-game.local", port: 3005, script: "dragon" },
    { dir: "typing-defense", host: "td.typing-game.local", port: 3006, script: "td" },
    {
      dir: "typing-survival",
      host: "survival.typing-game.local",
      port: 3007,
      script: "survival",
    },
    {
      dir: "immortality-cultivation",
      host: "tutien.typing-game.local",
      port: 3008,
      script: "tutien",
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
      for (const route of [...(game.host === "tutien.typing-game.local" ? ["/vocabulary/", "/typing-texts/"] : []), ...(game.aliases ?? [])]) {
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
      for (const route of [...(game.host === "tutien.typing-game.local" ? ["/vocabulary/", "/typing-texts/"] : []), ...(game.aliases ?? [])]) {
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
    // Whole-prefix blocks only: "location /api/admin/space-typing/" must not satisfy this.
    const spaFallback = "location / { try_files $uri $uri/ /index.html; }";
    const adminLocationIndex = portalPlayServer.search(/location \/api\/admin\/\s*\{/);
    const feelRuntimeIndex = portalPlayServer.search(/location \/api\/runtime\/typing-feel\/\s*\{/);
    const spaFallbackIndex = portalPlayServer.indexOf(spaFallback);

    if (adminLocationIndex < 0) {
      failures.push("Play nginx does not proxy Admin API requests (location /api/admin/ {).");
    }
    if (feelRuntimeIndex < 0) {
      failures.push("Play nginx does not proxy Typing Feel runtime requests (location /api/runtime/typing-feel/ {).");
    }
    if (!portalPlayServer.includes("proxy_pass http://127.0.0.1:3199;")) {
      failures.push("Play nginx Space Typing Admin API does not target the Admin service on port 3199.");
    }
    if (spaFallbackIndex < 0) {
      failures.push("Play nginx Portal server is missing its SPA fallback.");
    } else if (adminLocationIndex >= 0 && adminLocationIndex > spaFallbackIndex) {
      failures.push("Play nginx Admin API proxy must be declared before the Portal SPA fallback.");
    }
    if (spaFallbackIndex >= 0 && feelRuntimeIndex > spaFallbackIndex) {
      failures.push("Play nginx Typing Feel runtime proxy must be declared before the Portal SPA fallback.");
    }
  }

  if (!setupNginx.includes(`"${FEEL_HOST}"`)) failures.push(`setup-nginx.sh HOSTS is missing ${FEEL_HOST}`);
  if (!leafPlay.includes(FEEL_CATALOGUE)) failures.push(`scripts/play.sh does not check ${FEEL_CATALOGUE}`);

  for (const [name, config] of [
    ["play", nginx],
    ["dev", devNginx],
  ]) {
    for (const error of configStructureErrors(config)) failures.push(`${name} nginx ${error}`);
    for (const host of SELF_SERVED_HOSTS) {
      for (const { route, line } of sharedDataAliases(config, host)) {
        failures.push(`${name} nginx ${host} must serve its own pinned vocabulary and read Typing Feel from ${FEEL_HOST}; remove ${route} (line ${line})`);
      }
    }
    for (const { host, route, line } of feelAliases(config)) {
      // The three self-served hosts are already reported above.
      if (SELF_SERVED_HOSTS.includes(host)) continue;
      failures.push(`${name} nginx ${host} must read Typing Feel from ${FEEL_HOST}, never serve typing-feel/ itself; remove ${route} (line ${line})`);
    }
    for (const error of feelHostErrors(config)) failures.push(`${name} nginx ${error}`);
    if (!httpRedirectBlock(config).includes(` ${FEEL_HOST}`)) failures.push(`${name} nginx HTTP redirect is missing ${FEEL_HOST}`);
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
    return 1;
  }

  console.log(
    "Play mode contract PASS: static apps, shared runtime data, Space Typing Admin API routing, Portal shared-learning rebuild dependency, and the dragon/td/survival/tutien hosts are covered; dragon, td, survival serve their own pinned vocabulary without shared data aliases; the Typing Feel host (feel.typing-game.local) is static, HTTP/2, gzips JSON, CORS in every location, 404 without SPA fallback, and no other host serves typing-feel/.",
  );
  return 0;
}

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  process.exitCode = await main();
}
