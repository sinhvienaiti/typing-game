import { spawn } from "node:child_process";
import { resolve } from "node:path";

export class ShipRegistryPreviewError extends Error {}

export function parseShipRegistryPreviewOutput(output) {
  const marker = output.match(/\{\s*"protocolVersion"\s*:/);
  if (marker?.index === undefined) {
    throw new Error("preview JSON payload marker not found");
  }
  return JSON.parse(output.slice(marker.index));
}

export async function runShipRegistryPreview({
  rootDir,
  contract,
  policy,
  timeoutMs = 10000,
}) {
  const protocol = contract?.ships?.previewProtocol;
  if (protocol?.version !== 1 || protocol?.command !== "pnpm ships:admin-preview") {
    throw new ShipRegistryPreviewError("Unsupported Space Typing Ships preview protocol.");
  }

  const childDir = resolve(rootDir, "games/space-typing");
  const child = spawn("pnpm", ["--dir", childDir, "ships:admin-preview"], {
    cwd: rootDir,
    env: process.env,
    stdio: ["pipe", "pipe", "pipe"],
    shell: false,
  });

  const stdout = [];
  const stderr = [];
  let stdoutBytes = 0;
  let stderrBytes = 0;
  const maxBytes = 4 * 1024 * 1024;

  const result = new Promise((resolveResult, reject) => {
    const timer = setTimeout(() => {
      child.kill("SIGKILL");
      reject(new ShipRegistryPreviewError("Ships preview timed out."));
    }, timeoutMs);

    child.stdout.on("data", (chunk) => {
      stdoutBytes += chunk.length;
      if (stdoutBytes > maxBytes) {
        child.kill("SIGKILL");
        clearTimeout(timer);
        reject(new ShipRegistryPreviewError("Ships preview output exceeded the safe limit."));
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
      reject(new ShipRegistryPreviewError(`Could not start Ships preview process: ${error.message}`));
    });
    child.on("close", (code) => {
      clearTimeout(timer);
      if (code !== 0) {
        reject(
          new ShipRegistryPreviewError(
            `Ships preview failed (${code ?? "signal"}): ${Buffer.concat(stderr).toString("utf8").trim()}`,
          ),
        );
        return;
      }
      try {
        const preview = parseShipRegistryPreviewOutput(Buffer.concat(stdout).toString("utf8"));
        if (
          preview?.protocolVersion !== protocol.version ||
          typeof preview?.configRevision !== "string" ||
          !Array.isArray(preview?.ships) ||
          preview.ships.length !== contract.ships.ids.length
        ) {
          throw new Error("invalid preview payload");
        }
        resolveResult(preview);
      } catch (error) {
        reject(
          new ShipRegistryPreviewError(
            `Ships preview returned invalid JSON: ${error instanceof Error ? error.message : "unknown error"}`,
          ),
        );
      }
    });
  });

  child.stdin.end(JSON.stringify(policy === undefined ? {} : { policy }));
  return result;
}
