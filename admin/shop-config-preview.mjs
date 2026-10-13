import { spawn } from "node:child_process";
import { resolve } from "node:path";

export class ShopConfigPreviewError extends Error {}

export function parseShopConfigPreviewOutput(output) {
  const marker = output.match(/\{\s*"protocolVersion"\s*:/);
  if (marker?.index === undefined) throw new Error("preview JSON payload marker not found");
  return JSON.parse(output.slice(marker.index));
}

export async function runShopConfigPreview({
  rootDir,
  contract,
  policy,
  activeRevision = "admin-preview",
  shopType,
  stage,
  worldKey,
  luck,
  progression,
  discovered,
  timeoutMs = 10000,
}) {
  const protocol = contract?.previewProtocol;
  if (
    protocol?.version !== 1 ||
    protocol?.available !== true ||
    protocol?.plannedCommand !== "pnpm shop:admin-preview"
  ) {
    throw new ShopConfigPreviewError("Unsupported Space Typing Shop preview protocol.");
  }

  const childDir = resolve(rootDir, "games/space-typing");
  const child = spawn("pnpm", ["--dir", childDir, "shop:admin-preview"], {
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
    let settled = false;
    const finishReject = (error) => {
      if (settled) return;
      settled = true;
      reject(error);
    };
    const finishResolve = (value) => {
      if (settled) return;
      settled = true;
      resolveResult(value);
    };
    const timer = setTimeout(() => {
      child.kill("SIGKILL");
      finishReject(new ShopConfigPreviewError("Shop preview timed out."));
    }, timeoutMs);

    child.stdout.on("data", (chunk) => {
      stdoutBytes += chunk.length;
      if (stdoutBytes > maxBytes) {
        child.kill("SIGKILL");
        clearTimeout(timer);
        finishReject(new ShopConfigPreviewError("Shop preview output exceeded the safe limit."));
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
      finishReject(new ShopConfigPreviewError(`Could not start Shop preview process: ${error.message}`));
    });
    child.on("close", (code) => {
      clearTimeout(timer);
      if (settled) return;
      if (code !== 0) {
        finishReject(new ShopConfigPreviewError(
          `Shop preview failed (${code ?? "signal"}): ${Buffer.concat(stderr).toString("utf8").trim()}`,
        ));
        return;
      }
      try {
        const preview = parseShopConfigPreviewOutput(Buffer.concat(stdout).toString("utf8"));
        if (
          preview?.protocolVersion !== protocol.version ||
          preview?.kind !== "space-typing-shop-runtime-preview" ||
          preview?.runtime?.source !== "published" ||
          preview?.runtime?.applyBoundary !== contract?.runtime?.applyBoundary ||
          typeof preview?.runtime?.configRevision !== "string" ||
          preview?.policy === null || typeof preview?.policy !== "object" || Array.isArray(preview?.policy) ||
          preview?.request === null || typeof preview?.request !== "object" || Array.isArray(preview?.request) ||
          preview?.instance === null || typeof preview?.instance !== "object" || Array.isArray(preview?.instance) ||
          typeof preview?.available !== "boolean"
        ) {
          throw new Error("invalid preview payload");
        }
        finishResolve(preview);
      } catch (error) {
        finishReject(new ShopConfigPreviewError(
          `Shop preview returned invalid JSON: ${error instanceof Error ? error.message : "unknown error"}`,
        ));
      }
    });
  });

  const input = { activeRevision };
  if (policy !== undefined) input.policy = policy;
  if (shopType !== undefined) input.shopType = shopType;
  if (stage !== undefined) input.stage = stage;
  if (worldKey !== undefined) input.worldKey = worldKey;
  if (luck !== undefined) input.luck = luck;
  if (progression !== undefined) input.progression = progression;
  if (discovered !== undefined) input.discovered = discovered;
  child.stdin.end(JSON.stringify(input));
  return result;
}
