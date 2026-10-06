import { spawn } from "node:child_process";
import { resolve } from "node:path";

export class SkillRegistryPreviewError extends Error {}

export function parseSkillRegistryPreviewOutput(output) {
  const marker = output.match(/\{\s*"protocolVersion"\s*:/);
  if (marker?.index === undefined) throw new Error("preview JSON payload marker not found");
  return JSON.parse(output.slice(marker.index));
}

export async function runSkillRegistryPreview({ rootDir, contract, policy, timeoutMs = 10000 }) {
  const protocol = contract?.skills?.previewProtocol;
  if (protocol?.version !== 1 || protocol?.command !== "pnpm skills:admin-preview") {
    throw new SkillRegistryPreviewError("Unsupported Space Typing Skills preview protocol.");
  }

  const childDir = resolve(rootDir, "games/space-typing");
  const child = spawn("pnpm", ["--dir", childDir, "skills:admin-preview"], {
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
      reject(new SkillRegistryPreviewError("Skills preview timed out."));
    }, timeoutMs);

    child.stdout.on("data", (chunk) => {
      stdoutBytes += chunk.length;
      if (stdoutBytes > maxBytes) {
        child.kill("SIGKILL");
        clearTimeout(timer);
        reject(new SkillRegistryPreviewError("Skills preview output exceeded the safe limit."));
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
      reject(new SkillRegistryPreviewError(`Could not start Skills preview process: ${error.message}`));
    });
    child.on("close", (code) => {
      clearTimeout(timer);
      if (code !== 0) {
        reject(new SkillRegistryPreviewError(
          `Skills preview failed (${code ?? "signal"}): ${Buffer.concat(stderr).toString("utf8").trim()}`,
        ));
        return;
      }
      try {
        const preview = parseSkillRegistryPreviewOutput(Buffer.concat(stdout).toString("utf8"));
        if (
          preview?.protocolVersion !== protocol.version ||
          typeof preview?.configRevision !== "string" ||
          !Array.isArray(preview?.skills) ||
          preview.skills.length !== contract.skills.ids.length
        ) {
          throw new Error("invalid preview payload");
        }
        resolveResult(preview);
      } catch (error) {
        reject(new SkillRegistryPreviewError(
          `Skills preview returned invalid JSON: ${error instanceof Error ? error.message : "unknown error"}`,
        ));
      }
    });
  });

  child.stdin.end(JSON.stringify(policy === undefined ? {} : { policy }));
  return result;
}
