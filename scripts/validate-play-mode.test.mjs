// node --test scripts/validate-play-mode.test.mjs
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { mkdirSync, mkdtempSync, readFileSync, rmdirSync, rmSync, writeFileSync } from "node:fs";
import path from "node:path";
import { after, test } from "node:test";
import { fileURLToPath } from "node:url";
import * as validator from "./validate-play-mode.mjs";

const ROOT = fileURLToPath(new URL("../", import.meta.url));
const SCRIPT = path.join(ROOT, "scripts/validate-play-mode.mjs");
const HOSTS = ["dragon", "td", "survival"].map((name) => `${name}.typing-game.local`);
const ROUTES = ["/vocabulary/", "/typing-texts/", "/shared/typing-texts/"];
const configs = Object.fromEntries(["play", "dev"].map((mode) => [
  mode, readFileSync(path.join(ROOT, `infra/nginx/typing-game.local.${mode}.conf`), "utf8"),
]));
const fixtureRoot = path.join(ROOT, "tmp/validate-play-mode-test");
const fixtures = [];
after(() => {
  for (const directory of fixtures) rmSync(directory, { recursive: true, force: true });
  // Leave any fixtures owned by another concurrent test run intact.
  try { rmdirSync(fixtureRoot); } catch (error) {
    if (!["ENOENT", "ENOTEMPTY", "EISDIR"].includes(error.code)) throw error;
  }
});

function insert(config, host, directive) {
  const marker = `server_name ${host};`;
  assert.ok(config.includes(marker));
  return config.replace(marker, `${marker}\n    ${directive}`);
}
function run(...args) {
  return spawnSync(process.execPath, [SCRIPT, ...args], { cwd: ROOT, encoding: "utf8" });
}
function fixture(config) {
  mkdirSync(fixtureRoot, { recursive: true });
  const directory = mkdtempSync(path.join(fixtureRoot, "run-"));
  fixtures.push(directory);
  const file = path.join(directory, "nginx.conf");
  writeFileSync(file, config);
  return file;
}
function expectAlias(config, host, route) {
  const found = validator.sharedDataAliases(config, host);
  const line = config.slice(0, config.indexOf("location", config.indexOf(`server_name ${host};`))).split("\n").length;
  assert.deepEqual(found, [{ host, route, line }]);
}

test("import exposes pure checks without running the CLI or reading repo files", () => {
  const result = spawnSync(process.execPath, ["--input-type=module", "-e",
    `process.chdir('/'); await import(${JSON.stringify(new URL("./validate-play-mode.mjs", import.meta.url).href)});`,
  ], { cwd: ROOT, encoding: "utf8" });
  assert.equal(result.status, 0, result.stderr);
  assert.equal(result.stdout, "");
  assert.equal(result.stderr, "");
});

for (const [mode, config] of Object.entries(configs)) {
  test(`${mode}: real configs have no shared data aliases in the three hosts`, () => {
    for (const host of HOSTS) assert.deepEqual(validator.sharedDataAliases(config, host), []);
    assert.deepEqual(validator.configStructureErrors(config), []);
  });
  for (const host of HOSTS) {
    for (const route of ROUTES) {
      test(`${mode}: catches ${host} ${route}`, () => {
        expectAlias(insert(config, host, `location ${route} { alias __ROOT_DIR__/shared/vocabulary/; }`), host, route);
      });
    }
    const variants = [
      ["location ^~ /vocabulary/ { alias __ROOT_DIR__/shared/vocabulary/; }", "/vocabulary/"],
      ["location = /vocabulary { alias __ROOT_DIR__/shared/vocabulary/; }", "/vocabulary"],
      ["location ~ /typing-texts/ { alias __ROOT_DIR__/shared/typing-texts/; }", "/typing-texts/"],
      ["location ~* /shared/typing-texts/ { alias __ROOT_DIR__/shared/typing-texts/; }", "/shared/typing-texts/"],
      ["location\t ^~\t /vocabulary/\t{\n\talias\t__ROOT_DIR__/shared/vocabulary/;\n}", "/vocabulary/"],
      ["location /words/ { alias __ROOT_DIR__/shared/vocabulary/; }", "/words/"],
      ["location /words/ { root __ROOT_DIR__/shared/vocabulary/; }", "/words/"],
      ['location "/words/" { root "__ROOT_DIR__/shared/vocabulary/"; }', "/words/"],
      ["location /vocabulary/ { try_files $uri =404; }", "/vocabulary/"],
    ];
    for (const [directive, route] of variants) {
      test(`${mode}: catches ${host} variant ${directive}`, () => expectAlias(insert(config, host, directive), host, route));
    }
    test(`${mode}: ignores commented locations for ${host}`, () => {
      assert.deepEqual(validator.sharedDataAliases(insert(config, host,
        "# location /vocabulary/ { alias __ROOT_DIR__/shared/vocabulary/; }\n    location /safe/ { # alias __ROOT_DIR__/shared/vocabulary/;\n        try_files $uri =404;\n    }"), host), []);
    });
  }
  test(`${mode}: other hosts and survival models stay allowed`, () => {
    for (const host of ["tutien.typing-game.local", "space.typing-game.local", "typing-game.local"]) {
      assert.ok(config.includes(`server_name ${host};`));
      // The CLI scopes enforcement to SELF_SERVED_HOSTS; inspection remains reusable.
      for (const target of HOSTS) assert.deepEqual(validator.sharedDataAliases(insert(config, host,
        "location /words/ { alias __ROOT_DIR__/shared/vocabulary/; }"), target), []);
    }
    const survival = HOSTS[2];
    assert.ok(config.includes("location /assets/space-typing/models/"));
    assert.deepEqual(validator.sharedDataAliases(config, survival), []);
  });
  test(`${mode}: rejects missing and early closing braces`, () => {
    assert.match(validator.configStructureErrors(config.slice(0, config.lastIndexOf("}"))).join("\n"), /brace/i);
    assert.match(validator.configStructureErrors(`}\n{\n${config}`).join("\n"), /brace/i);
  });
  test(`${mode}: ignores comments and quoted braces, including escaped quotes`, () => {
    const extra = String.raw`# } { }
location /quoted/ { add_header Example "} # { \" }"; add_header Other '{'; }
`;
    assert.deepEqual(validator.configStructureErrors(insert(config, HOSTS[0], extra)), []);
  });
  test(`${mode}: each game host must have exactly one server block`, () => {
    for (const host of [...HOSTS, "tutien.typing-game.local"]) {
      const missing = config.replace(`server_name ${host};`, "server_name unused.local;");
      const duplicate = `${config}\nserver { listen 443 ssl; server_name ${host}; }\n`;
      assert.ok(validator.configStructureErrors(missing).some((message) => message.includes(host)));
      assert.ok(validator.configStructureErrors(duplicate).some((message) => message.includes(host)));
    }
  });
}

test("CLI on the repo prints PASS and exits 0", () => {
  const result = run();
  assert.equal(result.status, 0, result.stderr);
  assert.match(result.stdout, /PASS/);
  assert.match(result.stdout, /pinned vocabulary/);
});
for (const [mode, host, route] of [["play", HOSTS[0], "/vocabulary/"], ["dev", HOSTS[1], "/shared/typing-texts/"]]) {
  test(`CLI --${mode}-conf catches ${host} ${route}`, () => {
    const result = run(`--${mode}-conf`, fixture(insert(configs[mode], host,
      `location ${route} { alias __ROOT_DIR__/shared/vocabulary/; }`)));
    assert.equal(result.status, 1, result.stderr);
    assert.ok(result.stderr.includes(host), result.stderr);
    assert.ok(result.stderr.includes(route), result.stderr);
    assert.match(result.stderr, /line \d+/);
  });
}
test("CLI rejects unknown options and missing paths with usage and exit 2", () => {
  for (const args of [["--unknown"], ["--play-conf"], ["--dev-conf", "--play-conf"]]) {
    const result = run(...args);
    assert.equal(result.status, 2, result.stderr);
    assert.match(result.stderr, /Usage:/);
  }
});
test("CLI rejects malformed braces and duplicate hosts in either config", () => {
  for (const mode of Object.keys(configs)) {
    for (const config of [`}\n{\n${configs[mode]}`, `${configs[mode]}\nserver { listen 443 ssl; server_name ${HOSTS[0]}; }`]) {
      const result = run(`--${mode}-conf`, fixture(config));
      assert.equal(result.status, 1, result.stderr);
      assert.match(result.stderr, /brace|exactly one/);
    }
  }
});

// The Portal server must proxy the whole Admin API and the Typing Feel runtime before its SPA fallback.
const ADMIN_BLOCK = "location /api/admin/ {";
const FEEL_BLOCK = "location /api/runtime/typing-feel/ {";
test("CLI play-conf rejects an Admin proxy narrowed to /api/admin/space-typing/", () => {
  assert.ok(configs.play.includes(ADMIN_BLOCK));
  const result = run("--play-conf", fixture(configs.play.replace(ADMIN_BLOCK, "location /api/admin/space-typing/ {")));
  assert.equal(result.status, 1, result.stderr);
  assert.match(result.stderr, /does not proxy Admin API requests/);
});
test("CLI play-conf rejects a missing Typing Feel runtime proxy", () => {
  assert.ok(configs.play.includes(FEEL_BLOCK));
  const result = run("--play-conf", fixture(configs.play.replace(FEEL_BLOCK, "location /api/runtime/other/ {")));
  assert.equal(result.status, 1, result.stderr);
  assert.match(result.stderr, /does not proxy Typing Feel runtime requests/);
});
test("CLI play-conf rejects Admin and Typing Feel proxies declared after the SPA fallback", () => {
  const fallback = "location / { try_files $uri $uri/ /index.html; }";
  const start = configs.play.indexOf(FEEL_BLOCK);
  const end = configs.play.indexOf(fallback, start);
  assert.ok(start > 0 && end > start);
  const moved = configs.play.slice(0, start) + fallback + "\n    " +
    configs.play.slice(start, end).trimEnd() + configs.play.slice(end + fallback.length);
  const result = run("--play-conf", fixture(moved));
  assert.equal(result.status, 1, result.stderr);
  assert.match(result.stderr, /Admin API proxy must be declared before/);
  assert.match(result.stderr, /Typing Feel runtime proxy must be declared before/);
});
