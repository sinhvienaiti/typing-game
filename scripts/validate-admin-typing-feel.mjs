#!/usr/bin/env node
// Typing Feel Admin (phase G6, docs/games/TYPING_FEEL_SERVICE.md §9) against
// today's real catalogue, on a temp copy only:
//   1. the seed import of a copy of typing-feel/public (with the Audio Lab staging
//      when it is on this machine, read only) is a no-op the second time;
//   2. its export is catalogue r1 byte for byte, health and every set folder too;
//   3. the kit's own reader (loadKeyboardCatalog, keyboardFiles) loads it;
//   4. server.mjs serves the preview before the token check and the Admin routes after it;
//   5. admin:test runs every Typing Feel test;
//   6. source guards for the G6 review fixes (Host check, git read, registry lock, Publish gate, focus, radio keys).
//   7. G7 source guards: Format jobs never run through a shell.
// Never writes typing-feel/public, .local/admin or ~/AudioLab.
import { spawnSync } from "node:child_process";
import { existsSync, readFileSync, readdirSync } from "node:fs";
import { cp, mkdtemp, readFile, readdir, rm } from "node:fs/promises";
import { homedir, tmpdir } from "node:os";
import { join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { MediaAssetStore } from "../admin/media-assets-v2.mjs";
import { importTypingFeelSeed } from "../admin/typing-feel/import-staging.mjs";
import { TypingFeelService } from "../admin/typing-feel/service.mjs";
import { TypingFeelRevisionStore } from "../admin/typing-feel/store.mjs";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const realPublic = join(root, "typing-feel/public");
const staging = join(homedir(), "AudioLab/review/staging/keys-firefly");
const failures = [];
const check = (condition, message) => {
  if (!condition) failures.push(message);
  return condition;
};

async function snapshot(dir) {
  const files = new Map();
  const walk = async (relative) => {
    for (const entry of await readdir(join(dir, relative), { withFileTypes: true })) {
      const child = relative ? `${relative}/${entry.name}` : entry.name;
      if (entry.isDirectory()) await walk(child);
      else files.set(child, await readFile(join(dir, child)));
    }
  };
  await walk("");
  return files;
}

function differences(left, right) {
  const out = [];
  for (const [path, bytes] of left) if (!right.get(path)?.equals(bytes)) out.push(path);
  for (const path of right.keys()) if (!left.has(path)) out.push(`${path} (new)`);
  return out;
}

const catalogueFile = join(realPublic, "v1/keys/keys-manifest.json");
if (!existsSync(catalogueFile)) {
  console.error("validate-admin-typing-feel: typing-feel/public/v1/keys/keys-manifest.json is missing (run pnpm feel:import first).");
  process.exit(1);
}
const catalogue = JSON.parse(readFileSync(catalogueFile, "utf8"));
const firstPreview = join(realPublic, "v1/keys", catalogue.profiles[0].preview);
if (!existsSync(firstPreview)) {
  console.error("validate-admin-typing-feel: the Typing Feel sound files are not on this machine (run pnpm media:pull).");
  process.exit(1);
}

const work = await mkdtemp(join(process.env.TYPING_FEEL_VALIDATE_TMP || tmpdir(), "validate-admin-typing-feel-"));
try {
  const publicDir = join(work, "public");
  await cp(realPublic, publicDir, { recursive: true });
  const original = await snapshot(publicDir);
  const mediaStore = new MediaAssetStore({ rootDir: join(work, "data") });
  await mediaStore.initialize();
  const store = new TypingFeelRevisionStore({ rootDir: join(work, "shared") });
  const useStaging = existsSync(join(staging, "keys-manifest.json"));
  const options = { publicDir, stagingDir: useStaging ? staging : null, restore: !useStaging, mediaStore, store };
  const first = await importTypingFeelSeed(options);
  check(first.sets === catalogue.profiles.length, `seed registered ${first.sets} sets, the catalogue has ${catalogue.profiles.length}`);
  check(first.warnings.length === 0, `seed warnings: ${first.warnings.join(" | ")}`);
  check(first.hidden.length === 0 && first.retired.length === 0, `set folders with no catalogue row: hidden ${first.hidden.join(", ")}; retired ${first.retired.map((entry) => entry.id).join(", ")}`);
  const second = await importTypingFeelSeed(options);
  check(second.changed === false, "the second seed import changed something");
  const service = new TypingFeelService({ store, mediaStore, publicDir });
  check((await service.syncOnStartup()).status === "in-sync", "the seed's export is not the catalogue on disk");
  await rm(join(publicDir, "v1/keys/keys-manifest.json"));
  await rm(join(publicDir, "v1/health.json"));
  const exported = await service.syncOnStartup();
  check(exported.status === "re-exported" && exported.folders.created.length === 0, "the export did not reuse every seed folder");
  const changed = differences(original, await snapshot(publicDir));
  check(changed.length === 0, `export differs from r1: ${changed.slice(0, 5).join(", ")}`);

  const kitAudio = join(root, "shared/game-kit/feedback/typing-fx/audio.ts");
  if (check(existsSync(kitAudio), "shared/game-kit/feedback/typing-fx/audio.ts is missing")) {
    const reader = join(root, "admin/typing-feel/kit-reader");
    const result = spawnSync(process.execPath, ["--experimental-transform-types", "--no-warnings", "--import", join(reader, "register.mjs"), join(reader, "read-catalogues.mjs"), kitAudio, publicDir], { encoding: "utf8" });
    if (check(result.status === 0, `kit reader failed: ${result.stderr.trim().split("\n").slice(-3).join(" ")}`)) {
      const [read] = JSON.parse(result.stdout);
      check(read.state === "ready", `kit catalogue state ${read.state}`);
      check(read.options.length === catalogue.profiles.length + 1, `kit options ${read.options.length}, expected ${catalogue.profiles.length + 1} (Off + every set)`);
      check(read.revision === catalogue.revision && read.defaultId === catalogue.default, "kit revision/default differ from the catalogue");
      check(read.sets.every((set) => set.keys >= 10 && set.spaces >= 3), "a set loads fewer than 10 keys or 3 spaces in the kit");
    }
  }
} finally {
  await rm(work, { recursive: true, force: true });
}

const server = readFileSync(join(root, "admin/server.mjs"), "utf8");
const at = (text) => server.indexOf(text);
check(at("handleTypingFeelRuntimeRequest({ request, response, url })") > 0 && at("handleTypingFeelRuntimeRequest({ request, response, url })") < at("if (!authorized(request))"), "the Typing Feel preview must be served before the token check");
check(at("handleTypingFeelRequest({ request, response, url, actor })") > at("handleMediaV2Request({ request, response, url, actor })"), "the Typing Feel Admin routes must come after Media V2, behind the token");
check(at("!localHostHeader(request.headers.host)") > 0 && at("!localHostHeader(request.headers.host)") < at("handleTypingFeelRuntimeRequest({ request, response, url })"), "Admin routes and the preview must refuse non-local Host names (DNS rebinding) before any handler");
// G6 review fixes that only a browser shows: keep them from sliding back.
const source = (path) => readFileSync(join(root, path), "utf8");
check(/"--no-optional-locks"/.test(source("admin/typing-feel/service.mjs")), "Release & History must read git status without taking .git/index.lock");
check(/acquireRegistryFileLock\(key\)/.test(source("admin/media-assets-v2.mjs")), "Media V2 writes must hold the cross-process registry lock file");
check(/publish\.disabled = !publishable/.test(source("portal/src/admin/typing-feel/release-bar.ts")), "Publish must need a review that is valid and still on the live revision");
check(/data-focus-group/.test(source("portal/src/admin/typing-feel/ui.ts")), "keepFocus must fall back to the card or row when its control is disabled");
check(/ArrowRight/.test(source("portal/src/admin/typing-feel/typing-effects.ts")) && /tabIndex = value === checked \? 0 : -1/.test(source("portal/src/admin/typing-feel/typing-effects.ts")), "effect choices must follow the ARIA radio pattern (one Tab stop, arrow keys)");
// G7 Format jobs: the tool runs without a shell, arguments as one array, paths only from the store.
const jobsSource = source("admin/typing-feel/jobs.mjs");
check(/spawn\(this\.tool\.command, args, \{[^}]*shell: false/.test(jobsSource), "Format jobs must spawn the tool with an argument array and shell: false");
check(/^import \{ spawn \} from "node:child_process";$/m.test(jobsSource) && !/execSync|execFile|child_process"\)\.exec/.test(jobsSource), "Format jobs import only spawn from node:child_process (no exec, no shell)");
check(/`--src=\$\{sourceFile\}`, `--out=\$\{outDir\}`/.test(jobsSource), "Format jobs pass only the copied source and the job's out folder as paths");
check(/requireAdminPermission\(actor, JOB_PERMISSIONS\.check\)/.test(source("admin/typing-feel/http.mjs")), "the upload check needs its permission");
const adminTest = JSON.parse(readFileSync(join(root, "package.json"), "utf8")).scripts["admin:test"] ?? "";
for (const name of readdirSync(join(root, "admin/typing-feel")).filter((file) => file.endsWith(".test.mjs"))) {
  check(adminTest.includes(`admin/typing-feel/${name}`), `admin:test does not run admin/typing-feel/${name}`);
}
check(adminTest.includes("admin/media-write-lock.test.mjs"), "admin:test does not run admin/media-write-lock.test.mjs");

if (failures.length) {
  console.error(`validate-admin-typing-feel: ${failures.length} problem(s)`);
  for (const failure of failures) console.error(`  - ${failure}`);
  process.exit(1);
}
console.log(`validate-admin-typing-feel: OK (catalogue ${catalogue.revision}, ${catalogue.profiles.length} sets; seed export byte-identical; kit reader loads it).`);
