import { spawn } from "node:child_process";
import { resolve } from "node:path";

export class WorldMusicPreviewError extends Error {}

export async function runWorldMusicPreview({
  rootDir,
  contract,
  publishedPolicy,
  musicMode = "map",
  timeoutMs = 10000,
}) {
  const protocol = contract?.worldMusic?.previewProtocol;
  if (protocol?.version !== 1 || protocol?.command !== "pnpm music:admin-preview") {
    throw new WorldMusicPreviewError("Unsupported Space Typing World Music preview protocol.");
  }
  if (musicMode !== "map" && musicMode !== "random") {
    throw new WorldMusicPreviewError("musicMode must be map or random.");
  }

  const childDir = resolve(rootDir, "games/space-typing");
  const child = spawn("pnpm", ["--dir", childDir, "music:admin-preview"], {
    cwd: rootDir,
    env: process.env,
    stdio: ["pipe", "pipe", "pipe"],
    shell: false,
  });

  const stdout = [];
  const stderr = [];
  let stdoutBytes = 0;
  let stderrBytes = 0;
  const maxBytes = 8 * 1024 * 1024;

  const result = new Promise((resolveResult, reject) => {
    const timer = setTimeout(() => {
      child.kill("SIGKILL");
      reject(new WorldMusicPreviewError("World Music preview timed out."));
    }, timeoutMs);

    child.stdout.on("data", (chunk) => {
      stdoutBytes += chunk.length;
      if (stdoutBytes > maxBytes) {
        child.kill("SIGKILL");
        clearTimeout(timer);
        reject(new WorldMusicPreviewError("World Music preview output exceeded the safe limit."));
        return;
      }
      stdout.push(chunk);
    });
    child.stderr.on("data", (chunk) => {
      stderrBytes += chunk.length;
      if (stderrBytes <= maxBytes) stderr.push(chunk);
    });
    child.on("error", (error) => {
      clearTimeout(timer);
      reject(new WorldMusicPreviewError(`Could not start preview process: ${error.message}`));
    });
    child.on("close", (code) => {
      clearTimeout(timer);
      if (code !== 0) {
        reject(
          new WorldMusicPreviewError(
            `World Music preview failed (${code ?? "signal"}): ${Buffer.concat(stderr).toString("utf8").trim()}`,
          ),
        );
        return;
      }
      try {
        const preview = JSON.parse(Buffer.concat(stdout).toString("utf8"));
        if (preview?.protocolVersion !== protocol.version || !Array.isArray(preview?.worlds)) {
          throw new Error("invalid preview payload");
        }
        resolveResult(preview);
      } catch (error) {
        reject(
          new WorldMusicPreviewError(
            `World Music preview returned invalid JSON: ${error instanceof Error ? error.message : "unknown error"}`,
          ),
        );
      }
    });
  });

  child.stdin.end(
    JSON.stringify({
      musicMode,
      ...(publishedPolicy === undefined ? {} : { publishedPolicy }),
    }),
  );

  return result;
}
