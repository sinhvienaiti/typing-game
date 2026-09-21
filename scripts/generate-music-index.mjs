import { promises as fs } from "node:fs";
import path from "node:path";

const root = path.resolve("shared/music");
const output = path.join(root, "index.local.json");
const extensions = new Set([".mp3", ".m4a", ".aac", ".wav", ".ogg", ".webm"]);

async function walk(directory) {
  const entries = await fs.readdir(directory, { withFileTypes: true });
  const files = [];

  for (const entry of entries) {
    const fullPath = path.join(directory, entry.name);
    if (entry.isDirectory()) {
      files.push(...(await walk(fullPath)));
      continue;
    }

    if (!entry.isFile()) continue;
    if (!extensions.has(path.extname(entry.name).toLowerCase())) continue;
    files.push(fullPath);
  }

  return files;
}

function titleFromFile(file) {
  const base = path.basename(file, path.extname(file));
  return base.replace(/[_-]+/g, " ").replace(/\s+/g, " ").trim();
}

await fs.mkdir(root, { recursive: true });
const files = (await walk(root)).sort((a, b) => a.localeCompare(b, "en"));

const tracks = files.map((file) => {
  const relative = path.relative(root, file).split(path.sep).join("/");
  return {
    id: `local:${relative}`,
    title: titleFromFile(file),
    file: relative,
  };
});

await fs.writeFile(
  output,
  `${JSON.stringify({ version: 1, tracks }, null, 2)}\n`,
  "utf8",
);

console.log(`Indexed ${tracks.length} local music track(s) -> ${output}`);
