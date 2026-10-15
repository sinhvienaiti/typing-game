import { spawn } from "node:child_process";
import { resolve } from "node:path";

export class StageConfigPreviewError extends Error {}

export function parseStageConfigPreviewOutput(output) {
  const marker = output.match(/\{\s*"protocolVersion"\s*:/);
  if (marker?.index === undefined) throw new Error("preview JSON payload marker not found");
  return JSON.parse(output.slice(marker.index));
}

export async function runStageConfigPreview({ rootDir, contract, policy, timeoutMs = 10000 }) {
  const protocol = contract?.stages?.previewProtocol;
  if (protocol?.version !== 1 || protocol?.command !== "pnpm stages:admin-preview") {
    throw new StageConfigPreviewError("Unsupported Space Typing Stages preview protocol.");
  }
  const childDir = resolve(rootDir, "games/space-typing");
  const child = spawn("pnpm", ["--dir", childDir, "stages:admin-preview"], {
    cwd: rootDir, env: process.env, stdio: ["pipe", "pipe", "pipe"], shell: false,
  });
  const stdout = []; const stderr = []; let stdoutBytes = 0; let stderrBytes = 0;
  const maxBytes = 8 * 1024 * 1024;
  const result = new Promise((resolveResult, reject) => {
    const timer = setTimeout(() => { child.kill("SIGKILL"); reject(new StageConfigPreviewError("Stages preview timed out.")); }, timeoutMs);
    child.stdout.on("data", (chunk) => { stdoutBytes += chunk.length; if (stdoutBytes > maxBytes) { child.kill("SIGKILL"); clearTimeout(timer); reject(new StageConfigPreviewError("Stages preview output exceeded the safe limit.")); return; } stdout.push(chunk); });
    child.stderr.on("data", (chunk) => { stderrBytes += chunk.length; if (stderrBytes <= maxBytes) stderr.push(chunk); });
    child.on("error", (error) => { clearTimeout(timer); reject(new StageConfigPreviewError(`Could not start Stages preview process: ${error.message}`)); });
    child.on("close", (code) => {
      clearTimeout(timer);
      if (code !== 0) { reject(new StageConfigPreviewError(`Stages preview failed (${code ?? "signal"}): ${Buffer.concat(stderr).toString("utf8").trim()}`)); return; }
      try {
        const preview = parseStageConfigPreviewOutput(Buffer.concat(stdout).toString("utf8"));
        if (preview?.protocolVersion !== protocol.version || typeof preview?.configRevision !== "string" || !Array.isArray(preview?.stages) || preview.stages.length !== contract.stages.count) throw new Error("invalid preview payload");
        resolveResult(preview);
      } catch (error) { reject(new StageConfigPreviewError(`Stages preview returned invalid JSON: ${error instanceof Error ? error.message : "unknown error"}`)); }
    });
  });
  child.stdin.end(JSON.stringify(policy === undefined ? {} : { policy }));
  return result;
}
