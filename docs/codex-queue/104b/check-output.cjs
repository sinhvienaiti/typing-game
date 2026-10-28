// Keep generated check output inside the ticket folder.
const path = require("node:path");
const cli = process.argv[1] ?? "";
if (/[/\\]vitest(?:\.mjs)?$/.test(cli)) {
  process.argv.push("--no-cache", "--configLoader", "runner", "--maxWorkers", "1", "--no-file-parallelism");
} else if (/[/\\]vite(?:\.js)?$/.test(cli) && process.argv.includes("build")) {
  process.argv.push("--configLoader", "runner", "--outDir", path.join(process.cwd(), "docs/codex-queue/104b/check-output"));
}
