import { spawn } from "node:child_process";
import { resolve } from "node:path";

export class WorldMusicPreviewError extends Error {}

export function parseWorldMusicPreviewOutput(output) {
  const marker = output.match(/\{\s*"protocolVersion"\s*:/);
  if (marker?.index === undefined) {
    throw new Error("preview JSON payload marker not found");
  }
  return JSON.parse(output.slice(marker.index));
}

export async function runWorldMusicPreview({
  rootDir,
  contract,
  publishedPolicy,
  musicMode = "map",
  stageNumber,
  timeoutMs = 10000,
}) {
  const protocol = contract?.worldMusic?.previewProtocol;
  if (protocol?.version !== 1 || protocol?.command !== "pnpm music:admin-preview") {
    throw new WorldMusicPreviewError("Unsupported Space Typing World Music preview protocol.");
  }
  if (musicMode !== "map" && musicMode !== "random") {
    throw new WorldMusicPreviewError("musicMode must be map or random.");
  }
  if (
    stageNumber !== undefined &&
    (!Number.isInteger(stageNumber) || stageNumber < 1 || stageNumber > 1000)
  ) {
    throw new WorldMusicPreviewError("stageNumber must be an integer from 1 to 1000.");
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
        // pnpm may print supply-chain verification/status text to stdout before
        // the child CLI payload on a cold install. Anchor parsing at the
        // protocol envelope instead of assuming stdout contains JSON only.
        const preview = parseWorldMusicPreviewOutput(Buffer.concat(stdout).toString("utf8"));
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
      ...(stageNumber === undefined ? {} : { stageNumber }),
      ...(publishedPolicy === undefined ? {} : { publishedPolicy }),
    }),
  );

  return result;
}
