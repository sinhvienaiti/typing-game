// node --test scripts/sync-game-kit.test.mjs
import assert from "node:assert/strict";
import { execFileSync, spawnSync } from "node:child_process";
import { createHash } from "node:crypto";
import { existsSync, mkdirSync, mkdtempSync, readFileSync, rmSync, writeFileSync, appendFileSync, unlinkSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";
import { after, describe, it } from "node:test";
import { fileURLToPath } from "node:url";
import { checkAll, checkGame, driftReport, parseSourceHeader, planKit, syncGame } from "./sync-game-kit.mjs";

const SCRIPT = fileURLToPath(new URL("./sync-game-kit.mjs", import.meta.url));
const roots = [];
after(() => {
  for (const root of roots) rmSync(root, { recursive: true, force: true });
});

function write(root, relative, text) {
  const file = path.join(root, relative);
  mkdirSync(path.dirname(file), { recursive: true });
  writeFileSync(file, text);
}

/** A tiny parent repo: kit modules alpha and beta (beta imports alpha), one Space original, game demo. */
function fixture(modules = ["alpha", "beta"]) {
  const root = mkdtempSync(path.join(tmpdir(), "kit-sync-"));
  roots.push(root);
  write(root, "shared/game-kit/package.json", JSON.stringify({ name: "@typing-game/game-kit", version: "0.1.0" }));
  write(root, "shared/game-kit/alpha/index.ts", 'export { twice } from "./util";\n');
  write(root, "shared/game-kit/alpha/util.ts", "// Source: games/space-typing/src/util.ts (kit copy)\nexport function twice(value: number): number {\n  return value * 2;\n}\n");
  write(root, "shared/game-kit/alpha/util.test.ts", 'import { twice } from "./util";\n');
  write(root, "shared/game-kit/alpha/fake.test-helper.ts", "export const fake = 1;\n");
  write(root, "shared/game-kit/alpha/__fixtures__/data.json", "{}\n");
  write(root, "shared/game-kit/beta/index.ts", '/**\n * Example: import { x } from "./not-here";\n */\nimport { twice } from "../alpha/util";\nexport const four = twice(2);\n');
  write(root, "games/space-typing/src/util.ts", "export function twice(value: number): number {\n  return value * 2;\n}\n");
  write(root, "games/demo/kit.config.json", JSON.stringify({ modules }));
  return root;
}

const sha = (file) => createHash("sha256").update(readFileSync(file)).digest("hex");
const kitDir = (root) => path.join(root, "games/demo/src/kit");
const runVerify = (root) => spawnSync(process.execPath, [path.join(kitDir(root), "verify-kit.mjs")], { encoding: "utf8" });
const gitIn = (root, ...args) =>
  execFileSync("git", ["-C", root, "-c", "user.name=kit-test", "-c", "user.email=kit-test@example.invalid", "-c", "commit.gpgsign=false", ...args], { encoding: "utf8" }).trim();

describe("sync", () => {
  it("copies the listed modules without tests, helpers or fixtures", () => {
    const root = fixture();
    syncGame({ root, target: "games/demo" });
    const kit = kitDir(root);
    for (const file of ["alpha/index.ts", "alpha/util.ts", "beta/index.ts", "verify-kit.mjs", "README.md", "kit-manifest.json"]) {
      assert.ok(existsSync(path.join(kit, file)), file);
    }
    for (const file of ["alpha/util.test.ts", "alpha/fake.test-helper.ts", "alpha/__fixtures__/data.json"]) {
      assert.ok(!existsSync(path.join(kit, file)), file);
    }
    assert.equal(readFileSync(path.join(kit, "alpha/util.ts"), "utf8"), readFileSync(path.join(root, "shared/game-kit/alpha/util.ts"), "utf8"));
  });

  it("writes a manifest with the kit version, modules and a sha256 per file", () => {
    const root = fixture();
    syncGame({ root, target: "games/demo" });
    const manifest = JSON.parse(readFileSync(path.join(kitDir(root), "kit-manifest.json"), "utf8"));
    assert.equal(manifest.kitVersion, "0.1.0");
    assert.deepEqual(manifest.modules, ["alpha", "beta"]);
    assert.equal(manifest.parentCommit, null);
    assert.deepEqual(Object.keys(manifest.files), ["README.md", "alpha/index.ts", "alpha/util.ts", "beta/index.ts", "verify-kit.mjs"]);
    for (const [file, hash] of Object.entries(manifest.files)) assert.equal(hash, sha(path.join(kitDir(root), file)), file);
  });

  it("is idempotent and removes files of a module that is no longer listed", () => {
    const root = fixture();
    syncGame({ root, target: "games/demo" });
    const again = syncGame({ root, target: "games/demo" });
    assert.deepEqual(again.written, []);
    write(root, "games/demo/kit.config.json", JSON.stringify({ modules: ["alpha"] }));
    const smaller = syncGame({ root, target: "games/demo" });
    assert.deepEqual(smaller.removed, ["beta/index.ts"]);
    assert.ok(!existsSync(path.join(kitDir(root), "beta")));
  });

  it("refuses a module whose import the config leaves out", () => {
    const root = fixture(["beta"]);
    assert.throws(() => syncGame({ root, target: "games/demo" }), /add "alpha" to kit.config.json/);
    assert.ok(!existsSync(kitDir(root)));
  });

  it("refuses a missing module unless allowMissing, and then check reports it", () => {
    const root = fixture(["alpha", "gamma"]);
    assert.throws(() => syncGame({ root, target: "games/demo" }), /not found.*gamma/);
    const partial = syncGame({ root, target: "games/demo", allowMissing: true });
    assert.deepEqual(partial.missing, ["gamma"]);
    assert.deepEqual(partial.manifest.missingModules, ["gamma"]);
    assert.equal(runVerify(root).status, 0);
    assert.match(checkGame({ root, gameDir: path.join(root, "games/demo") }).join("\n"), /gamma/);
  });

  it("refuses media in the kit", () => {
    const root = fixture();
    write(root, "shared/game-kit/alpha/icon.png", "not really a png");
    assert.throws(() => syncGame({ root, target: "games/demo" }), /media never goes in the kit/);
  });
});

describe("tamper detection", () => {
  it("verify-kit.mjs passes on a fresh copy and fails on an edit, an extra file or a deleted file", () => {
    const root = fixture();
    syncGame({ root, target: "games/demo" });
    const clean = runVerify(root);
    assert.equal(clean.status, 0, clean.stderr);
    assert.match(clean.stdout, /src\/kit OK: 5 files/);

    appendFileSync(path.join(kitDir(root), "alpha/util.ts"), "// hand edit\n");
    const edited = runVerify(root);
    assert.equal(edited.status, 1);
    assert.match(edited.stderr, /changed: alpha\/util\.ts/);

    syncGame({ root, target: "games/demo" });
    write(root, "games/demo/src/kit/alpha/extra.ts", "export {};\n");
    assert.match(runVerify(root).stderr, /not in manifest: alpha\/extra\.ts/);

    syncGame({ root, target: "games/demo" });
    unlinkSync(path.join(kitDir(root), "beta/index.ts"));
    assert.match(runVerify(root).stderr, /missing: beta\/index\.ts/);
  });

  it("verify-kit.mjs works in a game copied without its parent repo", () => {
    const root = fixture();
    syncGame({ root, target: "games/demo" });
    const alone = mkdtempSync(path.join(tmpdir(), "kit-alone-"));
    roots.push(alone);
    execFileSync("cp", ["-R", path.join(root, "games/demo"), alone]);
    rmSync(root, { recursive: true, force: true });
    const result = spawnSync(process.execPath, [path.join(alone, "demo/src/kit/verify-kit.mjs")], { encoding: "utf8" });
    assert.equal(result.status, 0, result.stderr);
    assert.match(result.stdout, /src\/kit OK/);
  });

  it("check flags a hand edit and a kit that moved on", () => {
    const root = fixture();
    syncGame({ root, target: "games/demo" });
    assert.deepEqual(checkAll(root), [{ game: "games/demo", problems: [] }]);

    appendFileSync(path.join(kitDir(root), "alpha/util.ts"), "// hand edit\n");
    assert.match(checkAll(root)[0].problems.join("\n"), /edited by hand: alpha\/util\.ts/);

    syncGame({ root, target: "games/demo" });
    write(root, "shared/game-kit/alpha/util.ts", "export function twice(value: number): number {\n  return value + value;\n}\n");
    assert.match(checkAll(root)[0].problems.join("\n"), /out of date with the current kit: alpha\/util\.ts/);
  });

  it("the CLI exits 1 on --check problems and 0 once re-synced", () => {
    const root = fixture();
    const sync = spawnSync(process.execPath, [SCRIPT, "--root", root, "--target", "games/demo"], { encoding: "utf8" });
    assert.equal(sync.status, 0, sync.stderr);
    appendFileSync(path.join(kitDir(root), "beta/index.ts"), "export const five = 5;\n");
    const bad = spawnSync(process.execPath, [SCRIPT, "--root", root, "--check"], { encoding: "utf8" });
    assert.equal(bad.status, 1);
    assert.match(bad.stderr, /games\/demo: \d+ problem/);
    spawnSync(process.execPath, [SCRIPT, "--root", root, "--target", "games/demo"], { encoding: "utf8" });
    const good = spawnSync(process.execPath, [SCRIPT, "--root", root, "--check"], { encoding: "utf8" });
    assert.equal(good.status, 0, good.stderr);
    assert.match(good.stdout, /games\/demo: OK/);
  });

  it("check skips worktrees and other dot-folders", () => {
    const root = fixture();
    syncGame({ root, target: "games/demo" });
    write(root, "games/.wt-demo/kit.config.json", JSON.stringify({ modules: ["alpha"] }));
    assert.deepEqual(checkAll(root).map((result) => result.game), ["games/demo"]);
  });
});

describe("git and pinning", () => {
  it("records the last parent commit of the kit and follows a pinned commit", () => {
    const root = fixture();
    gitIn(root, "init", "-q");
    gitIn(root, "add", "-A");
    gitIn(root, "commit", "-q", "-m", "kit v1");
    const v1 = gitIn(root, "rev-parse", "HEAD");
    const synced = syncGame({ root, target: "games/demo" });
    assert.equal(synced.manifest.parentCommit, v1);
    assert.equal(synced.manifest.parentDirty, false);

    write(root, "shared/game-kit/alpha/util.ts", "export function twice(value: number): number {\n  return value + value;\n}\n");
    assert.equal(planKit({ root, gameDir: path.join(root, "games/demo") }).manifest.parentDirty, true);

    write(root, "games/demo/kit.config.json", JSON.stringify({ modules: ["alpha", "beta"], pinned: { commit: v1.slice(0, 10), reason: "test" } }));
    const pinned = syncGame({ root, target: "games/demo" });
    assert.equal(pinned.manifest.parentCommit, v1);
    assert.match(readFileSync(path.join(kitDir(root), "alpha/util.ts"), "utf8"), /value \* 2/);
    assert.deepEqual(checkAll(root)[0].problems, []);

    write(root, "games/demo/kit.config.json", JSON.stringify({ modules: ["alpha"], pinned: { commit: v1, reason: " " } }));
    assert.throws(() => syncGame({ root, target: "games/demo" }), /pinned.reason is required/);
  });
});

describe("drift", () => {
  it("reads Source headers", () => {
    assert.equal(parseSourceHeader("// Source: new for the kit\n"), "new");
    assert.equal(parseSourceHeader("export {};\n"), null);
    assert.deepEqual(parseSourceHeader("// Source: shared/learning/a.mjs + games/space-typing/src/b.ts (notes; more)\n"), [
      { repo: "shared", ref: null, path: "learning/a.mjs" },
      { repo: "games/space-typing", ref: null, path: "src/b.ts" },
    ]);
    assert.deepEqual(parseSourceHeader("#!/usr/bin/env node\n// Source: games/space-typing@feat/x src/a.ts, src/b.ts (part), src/c.ts; note\n"), [
      { repo: "games/space-typing", ref: "feat/x", path: "src/a.ts" },
      { repo: "games/space-typing", ref: "feat/x", path: "src/b.ts" },
      { repo: "games/space-typing", ref: "feat/x", path: "src/c.ts" },
    ]);
  });

  it("reports same, changed, kit only and missing sources", () => {
    const root = fixture();
    write(root, "shared/game-kit/beta/gone.ts", "// Source: games/space-typing/src/gone.ts\nexport {};\n");
    const status = (file) => driftReport(root).find((row) => row.file === file)?.status;
    assert.equal(status("alpha/util.ts"), "same");
    assert.equal(status("alpha/index.ts"), "kit only");
    assert.equal(status("beta/gone.ts"), "source missing");
    assert.equal(driftReport(root).some((row) => row.file.includes(".test")), false);
    write(root, "games/space-typing/src/util.ts", "export function twice(value: number): number {\n  return 2 * value;\n}\n");
    assert.equal(status("alpha/util.ts"), "changed +1 -1");
    const cli = spawnSync(process.execPath, [SCRIPT, "--root", root, "--drift"], { encoding: "utf8" });
    assert.equal(cli.status, 0);
    assert.match(cli.stdout, /alpha\s+same 0, changed 1/);
  });
});
