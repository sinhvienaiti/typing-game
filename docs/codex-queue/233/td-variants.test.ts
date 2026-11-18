import { spawnSync } from "node:child_process";
import { copyFileSync, mkdirSync, mkdtempSync, readFileSync, readdirSync, readlinkSync, rmSync, symlinkSync, writeFileSync } from "node:fs";
import { dirname, join, relative, resolve } from "node:path";
import { build } from "vite";
import { afterEach, expect, it, vi } from "vitest";

const root = resolve(__dirname, "..");
const contract = join(root, "src/kit/learning/contract.ts");
afterEach(() => { vi.unstubAllEnvs(); vi.unstubAllGlobals(); });
function fixture(prefix: string): string {
  mkdirSync(join(root, "tmp"), { recursive: true });
  return mkdtempSync(join(root, "tmp/233-" + prefix + "-"));
}
for (const url of [undefined, "https://portal.example:444/learn/?game=td#book"])
  for (const variant of ["query-hash", "double-symlink", "double-symlink-query-hash"])
    it(`P1-01 additional real build ${variant}/${url}`, async () => {
      vi.stubEnv("VITE_PORTAL_URL", url);
      const dir = fixture("id");
      const before = readFileSync(contract);
      try {
        const first = join(dir, "first"); const second = join(dir, "second");
        symlinkSync(root, first, "dir"); symlinkSync(first, second, "dir");
        let spec = variant === "query-hash" ? contract : join(second, "src/kit/learning/contract.ts");
        if (variant.includes("query-hash")) spec += "?v=233#learning";
        const input = join(dir, "entry.ts");
        writeFileSync(input, `export { PARENT_ORIGIN } from ${JSON.stringify(spec)};`);
        const result = await build({ configFile: join(second, "vite.config.ts"), logLevel: "silent",
          resolve: { preserveSymlinks: true },
          build: { outDir: join(dir, "out"), copyPublicDir: false, minify: false,
            rollupOptions: { input, preserveEntrySignatures: "strict", output: { manualChunks: () => undefined } } } });
        if (!("output" in result)) throw new Error("Expected one build");
        const chunks = result.output.filter((x) => x.type === "chunk");
        expect(chunks).toHaveLength(1);
        const code = chunks[0]!.code;
        expect(code).not.toContain("typing-game.local");
        const executed = spawnSync(process.execPath, ["--input-type=module", "--eval",
          'import {readFileSync} from "node:fs"; const m=await import("data:text/javascript;base64,"+readFileSync(0).toString("base64")); console.log(JSON.stringify(m.PARENT_ORIGIN));'],
          { input: code, encoding: "utf8", timeout: 5000 });
        expect(executed.status, executed.stderr).toBe(0);
        expect(JSON.parse(executed.stdout)).toBe(url ? new URL(url).origin : "");
      } finally { expect(readFileSync(contract)).toEqual(before); rmSync(dir, { recursive: true, force: true }); }
    });

function snapshot(dir: string): Record<string, string> {
  return Object.fromEntries(readdirSync(dir, { withFileTypes: true }).flatMap((item): [string, string][] => {
    const p = join(dir, item.name);
    if (item.isSymbolicLink()) return [[item.name, "link:" + readlinkSync(p)]];
    if (item.isDirectory()) return [[item.name + "/", "directory"], ...Object.entries(snapshot(p)).map(([k,v]): [string,string] => [item.name + "/" + k,v])];
    return [[item.name, readFileSync(p).toString("base64")]];
  }));
}
for (const location of ["assets", "assets/typing-defense", "assets/typing-defense/models", "assets/typing-defense/models/deep/a/link", ".vite", ".vite/deep/a/link"])
  for (const keys of [[], ["keep"]])
    it(`P1-02 relative dangling outside dist ${location}/${keys.length}`, () => {
      const dir = fixture("prune");
      try {
        const dist = join(dir, "dist"); const outside = join(dir, "outside");
        mkdirSync(join(dist, "assets/typing-defense/models/keep"), { recursive: true });
        mkdirSync(join(dist, ".vite")); mkdirSync(outside);
        writeFileSync(join(outside, "sentinel.txt"), "PRIVATE_SENTINEL");
        writeFileSync(join(dist, "index.html"), "game");
        writeFileSync(join(dist, ".vite/manifest.json"), "{}");
        writeFileSync(join(dist, "assets/typing-defense/models/keep/high.glb"), "model");
        writeFileSync(join(dist, "assets/typing-defense/models/manifest.json"), JSON.stringify({models:{keep:{tiers:{high:{url:"/assets/typing-defense/models/keep/high.glb"}}}}}));
        const link = join(dist, location);
        rmSync(link, { recursive: true, force: true }); mkdirSync(dirname(link), { recursive: true });
        // The link target is absent and lies outside dist; resolve before taking the snapshot.
        const target = join(outside, "missing");
        symlinkSync(relative(dirname(link), target), link);
        mkdirSync(join(dir, "scripts/deploy"), { recursive: true });
        copyFileSync(join(root, "scripts/deploy/prune.mjs"), join(dir, "scripts/deploy/prune.mjs"));
        writeFileSync(join(dir, "deploy-models.json"), JSON.stringify({models:keys}));
        const before = snapshot(dir);
        const result = spawnSync(process.execPath, [join(dir, "scripts/deploy/prune.mjs"), dist], { encoding: "utf8", timeout: 5000 });
        expect(result.status, result.stderr).toBe(1);
        expect(result.stderr).toMatch(/symlink/i);
        expect(snapshot(dir)).toEqual(before);
      } finally { rmSync(dir, { recursive: true, force: true }); }
    });

it("P2-01 refuses a two-link ancestor chain before changing the real package", () => {
  const dir = fixture("ancestor");
  try {
    const dist = join(dir, "real/dist");
    mkdirSync(join(dist, ".vite"), { recursive: true });
    writeFileSync(join(dist, "index.html"), "game"); writeFileSync(join(dist, ".vite/manifest.json"), "{}");
    symlinkSync("real", join(dir, "first"), "dir"); symlinkSync("first", join(dir, "second"), "dir");
    mkdirSync(join(dir, "scripts/deploy"), { recursive: true });
    copyFileSync(join(root, "scripts/deploy/prune.mjs"), join(dir, "scripts/deploy/prune.mjs"));
    writeFileSync(join(dir, "deploy-models.json"), '{"models":[]}');
    const before = snapshot(dir);
    const result = spawnSync(process.execPath, [join(dir, "scripts/deploy/prune.mjs"), join(dir, "second/dist")], {encoding:"utf8",timeout:5000});
    expect(result.status, result.stderr).toBe(1); expect(result.stderr).toMatch(/symlink/i);
    expect(snapshot(dir)).toEqual(before);
  } finally { rmSync(dir, {recursive:true,force:true}); }
});

it.each(["", "https://portal.example:444/path#fragment"])("P2-02 concurrent imports remain lazy with URL %j", async (url) => {
  vi.resetModules(); vi.stubEnv("VITE_PORTAL_URL",url);
  const add = vi.fn(); const remove = vi.fn(); const post = vi.fn();
  vi.stubGlobal("window", {parent:{postMessage:post},addEventListener:add,removeEventListener:remove,setTimeout,clearTimeout});
  const actual = await import("../src/kit/learning");
  const create = vi.fn(actual.createLearningBridge);
  vi.doMock("../src/kit/learning",async (original)=>({...await original<typeof import("../src/kit/learning")>(),createLearningBridge:create}));
  try {
    const [a,b] = await Promise.all([import("../src/app/learning"),import("../src/app/learning")]);
    expect(a).toBe(b); expect(create).not.toHaveBeenCalled(); expect(add).not.toHaveBeenCalled(); expect(post).not.toHaveBeenCalled();
    const first = a.learningBridge(); expect(b.learningBridge()).toBe(first); expect(create).toHaveBeenCalledTimes(1);
    expect(first.parentOrigin).toBe(url ? new URL(url).origin : ""); expect(add).toHaveBeenCalledTimes(url ? 1 : 0);
  } finally {
    for (const result of create.mock.results) if(result.type==="return") result.value.dispose();
    expect(remove.mock.calls).toEqual(add.mock.calls);vi.doUnmock("../src/kit/learning");vi.resetModules();
  }
});
