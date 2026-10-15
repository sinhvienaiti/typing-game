import { spawn } from "node:child_process";
import { resolve } from "node:path";

export class EquipmentRegistryPreviewError extends Error {}

export function parseEquipmentRegistryPreviewOutput(output) {
  const marker = output.match(/\{\s*"protocolVersion"\s*:/);
  if (marker?.index === undefined) throw new Error("preview JSON payload marker not found");
  return JSON.parse(output.slice(marker.index));
}

export async function runEquipmentRegistryPreview({
  rootDir,
  contract,
  policy,
  timeoutMs = 10000,
}) {
  const protocol = contract?.equipment?.previewProtocol;
  if (protocol?.version !== 1 || protocol?.command !== "pnpm equipment:admin-preview") {
    throw new EquipmentRegistryPreviewError("Unsupported Space Typing Equipment preview protocol.");
  }

  const childDir = resolve(rootDir, "games/space-typing");
  const child = spawn("pnpm", ["--dir", childDir, "equipment:admin-preview"], {
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
      reject(new EquipmentRegistryPreviewError("Equipment preview timed out."));
    }, timeoutMs);

    child.stdout.on("data", (chunk) => {
      stdoutBytes += chunk.length;
      if (stdoutBytes > maxBytes) {
        child.kill("SIGKILL");
        clearTimeout(timer);
        reject(new EquipmentRegistryPreviewError("Equipment preview output exceeded the safe limit."));
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
      reject(new EquipmentRegistryPreviewError(`Could not start Equipment preview process: ${error.message}`));
    });
    child.on("close", (code) => {
      clearTimeout(timer);
      if (code !== 0) {
        reject(new EquipmentRegistryPreviewError(
          `Equipment preview failed (${code ?? "signal"}): ${Buffer.concat(stderr).toString("utf8").trim()}`,
        ));
        return;
      }
      try {
        const preview = parseEquipmentRegistryPreviewOutput(Buffer.concat(stdout).toString("utf8"));
        if (
          preview?.protocolVersion !== protocol.version ||
          typeof preview?.configRevision !== "string" ||
          !Array.isArray(preview?.equipment) ||
          preview.equipment.length !== contract.equipment.ids.length
        ) {
          throw new Error("invalid preview payload");
        }
        resolveResult(preview);
      } catch (error) {
        reject(new EquipmentRegistryPreviewError(
          `Equipment preview returned invalid JSON: ${error instanceof Error ? error.message : "unknown error"}`,
        ));
      }
    });
  });

  child.stdin.end(JSON.stringify(policy === undefined ? {} : { policy }));
  return result;
}
