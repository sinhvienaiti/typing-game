import { mkdirSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { afterAll, describe, expect, it } from "vitest";
import { resolveSharedFile, serveSharedFolders, sharedMounts } from "./index";

const base = mkdtempSync(join(tmpdir(), "kit-shared-"));
const shared = join(base, "shared");
const game = join(base, "games", "dragon-hold");
mkdirSync(join(shared, "vocabulary", "levels"), { recursive: true });
mkdirSync(join(shared, "typing-texts"), { recursive: true });
mkdirSync(join(base, "models", "enemies"), { recursive: true });
mkdirSync(game, { recursive: true });
writeFileSync(join(shared, "vocabulary", "index.json"), '{"version":1}');
writeFileSync(join(shared, "vocabulary", "levels", "001.json"), '{"entries":[]}');
writeFileSync(join(shared, "typing-texts", "a.json"), "[]");
writeFileSync(join(shared, "secret.txt"), "no");
writeFileSync(join(base, "models", "enemies", "e01.glb"), "glb");

afterAll(() => rmSync(base, { recursive: true, force: true }));

describe("shared folders dev plugin", () => {
  const mounts = sharedMounts(game, { modelsDir: "../../models" });

  it("maps /vocabulary/ and /typing-texts/ under ../../shared by default", () => {
    expect(resolveSharedFile(mounts, "/vocabulary/index.json")).toBe(join(shared, "vocabulary", "index.json"));
    expect(resolveSharedFile(mounts, "/vocabulary/levels/001.json?v=2")).toBe(join(shared, "vocabulary", "levels", "001.json"));
    expect(resolveSharedFile(mounts, "/typing-texts/a.json")).toBe(join(shared, "typing-texts", "a.json"));
    expect(resolveSharedFile(mounts, "/shared-models/enemies/e01.glb")).toBe(join(base, "models", "enemies", "e01.glb"));
  });

  it("never serves outside its folders or missing files", () => {
    expect(resolveSharedFile(mounts, "/vocabulary/../secret.txt")).toBeNull();
    expect(resolveSharedFile(mounts, "/vocabulary/%2e%2e/secret.txt")).toBeNull();
    expect(resolveSharedFile(mounts, "/vocabulary/levels")).toBeNull();
    expect(resolveSharedFile(mounts, "/vocabulary/missing.json")).toBeNull();
    expect(resolveSharedFile(mounts, "/other/index.json")).toBeNull();
    expect(resolveSharedFile(mounts, "/vocabulary/%E0%A4%A")).toBeNull();
  });

  it("answers GET and HEAD with a content type and passes everything else on", async () => {
    const plugin = serveSharedFolders({ sharedRoot: shared });
    (plugin.configResolved as unknown as (config: { root: string }) => void)({ root: game });
    let middleware: ((req: unknown, res: unknown, next: () => void) => void) | undefined;
    (plugin.configureServer as unknown as (server: unknown) => void)({
      middlewares: { use: (handler: typeof middleware) => (middleware = handler) },
    });
    expect(plugin.apply).toBe("serve");

    const call = (method: string, url: string) =>
      new Promise<{ next: boolean; headers: Record<string, string>; body: string }>((done) => {
        const headers: Record<string, string> = {};
        const chunks: Buffer[] = [];
        const res = {
          setHeader: (name: string, value: string) => (headers[name] = value),
          end: () => done({ next: false, headers, body: Buffer.concat(chunks).toString() }),
          write: (chunk: Buffer) => chunks.push(Buffer.from(chunk)),
          on: () => res,
          once: () => res,
          emit: () => true,
          removeListener: () => res,
        };
        middleware!({ method, url }, res, () => done({ next: true, headers, body: "" }));
      });

    const got = await call("GET", "/vocabulary/index.json");
    expect(got.next).toBe(false);
    expect(got.headers["Content-Type"]).toBe("application/json");
    expect(got.body).toBe(readFileSync(join(shared, "vocabulary", "index.json"), "utf8"));
    expect((await call("HEAD", "/vocabulary/index.json")).body).toBe("");
    expect((await call("POST", "/vocabulary/index.json")).next).toBe(true);
    expect((await call("GET", "/src/main.ts")).next).toBe(true);
  });
});
