import { readFile, mkdir, writeFile } from "node:fs/promises";
import { createHash } from "node:crypto";
import { fileURLToPath } from "node:url";
import path from "node:path";
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const args = process.argv.slice(2), check = args.includes("--check"), targetIndex = args.indexOf("--target");
for (let index = 0; index < args.length; index++) {
  if (args[index] === "--check") continue;
  if (args[index] === "--target" && args[index + 1] && !args[index + 1].startsWith("--")) { index++; continue; }
  throw new Error("Usage: sync-space-voice-contract.mjs [--check] [--target child-repository]");
}
const targetRoot = targetIndex < 0 ? path.join(root, "games/space-typing") : path.resolve(args[targetIndex + 1]);
const destination = path.join(targetRoot, "src/input/platform");
const files = ["protocol.mjs", "protocol.d.mts", "target-snapshot.mjs", "target-snapshot.d.mts", "result-policy.mjs", "result-policy.d.mts"];
const manifest = { source: "typing-game/shared/voice", protocolVersion: 1, files: {} };
if (!check) await mkdir(destination, { recursive: true });
for (const file of files) {
  const bytes = await readFile(path.join(root, "shared/voice", file));
  manifest.files[file] = createHash("sha256").update(bytes).digest("hex");
  if (check) {
    const copy = await readFile(path.join(destination, file));
    if (!copy.equals(bytes)) throw new Error(`Voice contract drift: ${file}; run pnpm voice:sync`);
  } else await writeFile(path.join(destination, file), bytes);
}
const manifestBytes = JSON.stringify(manifest, null, 2) + "\n";
if (check) {
  if (await readFile(path.join(destination, "contract-manifest.json"), "utf8") !== manifestBytes) throw new Error("Voice contract manifest drift");
} else await writeFile(path.join(destination, "contract-manifest.json"), manifestBytes);
console.log(`Voice protocol v1 ${check ? "verified" : "synced"}: ${files.length} canonical files`);
