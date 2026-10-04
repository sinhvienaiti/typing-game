import { createHash } from "node:crypto";
import { readFileSync } from "node:fs";
import { createRequire } from "node:module";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");

/** Pin the upstream Worker and replace only its redundant IndexedDB extraction cache. */
export function loadOfflineVoskWorker() {
  const require = createRequire(resolve(root, "portal/package.json"));
  const bundle = readFileSync(require.resolve("vosk-browser"), "utf8");
  const encoded = /WorkerFactory = createBase64WorkerFactory\('([^']+)'/.exec(
    bundle,
  )?.[1];
  if (!encoded) throw new Error("Pinned Vosk worker is missing");
  let source = Buffer.from(encoded, "base64").toString("utf8");
  const upstreamHash = createHash("sha256").update(source).digest("hex");
  if (
    upstreamHash !==
    "7ba6b482f49ff3d49290b85f4ca13d5c6a5787b237cac1c6d15129668d36f529"
  )
    throw new Error("Vosk worker changed; review its binding before upgrading");
  for (const [before, after] of [
    [
      "this.Vosk.FS.mount(this.Vosk.IDBFS, {}, storagePath);",
      "/* Verified archive is cached by the host; extracted files stay in Worker MEMFS. */",
    ],
    ["return this.Vosk.syncFilesystem(true);", "return Promise.resolve();"],
    ["return this.Vosk.syncFilesystem(false);", "return Promise.resolve();"],
  ]) {
    if (source.split(before).length !== 2)
      throw new Error("Unexpected Vosk cache binding");
    source = source.replace(before, after);
  }
  const createAck =
    /this\.createRecognizer\(message\)(\r?\n\s+)\.then\(\(result\) => \{(\r?\n\s+)ctx\.postMessage\(result\);/;
  if (!createAck.test(source))
    throw new Error("Unexpected Vosk recognizer readiness binding");
  source = source.replace(
    createAck,
    (_, gap, indent) =>
      `this.createRecognizer(message)${gap}.then(() => {${indent}ctx.postMessage({ event: "recognizer-ready", recognizerId: message.recognizerId });`,
  );
  const hash = createHash("sha256").update(source).digest("hex");
  return {
    source,
    fileName: `assets/vosk-worker-${hash.slice(0, 12)}.js`,
    hash,
  };
}

export function offlineVoskPlugin() {
  const worker = loadOfflineVoskWorker();
  const id = "\0offline-vosk-worker";
  return {
    name: "offline-vosk-worker",
    resolveId(value) {
      if (value === "virtual:offline-vosk-worker") return id;
    },
    load(value) {
      if (value === id)
        return `export default ${JSON.stringify("/" + worker.fileName)};`;
    },
    buildStart() {
      this.emitFile({
        type: "asset",
        fileName: worker.fileName,
        source: worker.source,
      });
    },
    configureServer(server) {
      server.middlewares.use((request, response, next) => {
        if (request.url?.split("?")[0] !== "/" + worker.fileName) {
          next();
          return;
        }
        response.setHeader("Content-Type", "application/javascript");
        response.setHeader("Cache-Control", "no-cache");
        response.end(worker.source);
      });
    },
  };
}
