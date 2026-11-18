// node --test tests/no-media.test.mjs
// No media in Git (TYPING_FEEL_SERVICE.md §6.1): every sound, image, model and
// video file under typing-feel/ is ignored wherever it lands, and so is all of
// art-src/; the JSON, code and docs stay tracked. Skips outside a Git work tree.
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const git = (args, input) => spawnSync("git", ["-C", ROOT, ...args], { encoding: "utf8", input });

const IGNORED = [
  "public/v1/keys/sets/deep/0123456789ab/key-01.ogg",
  "public/v1/keys/sets/deep/0123456789ab/PREVIEW.OGG",
  "public/v1/keys/sets/deep/0123456789ab/key-01.opus",
  "public/x.png",
  "public/x.mp3",
  "public/fx/spark.webp",
  "art-src/raw/0123abcd.wav",
  "art-src/x.mp3",
  "art-src/x.flac",
  "art-src/x.ogg",
  "art-src/notes.txt",
  "x.ogg",
  "x.glb",
  "x.gltf",
  "x.bin",
  "x.m4a",
  "x.webm",
  "x.mp4",
  "x.jpg",
  "x.svg",
  "tools/x.ogg",
  "tmp/x.wav",
  "tmp/report.json",
  "dist/typing-feel.js",
  ".media-pulled",
  "public/v1/keys/keys-manifest.json.123.tmp",
  "public/v1/keys/sets/deep/.incoming-0123456789ab-42/keys-manifest.json",
];
const TRACKED = [
  "public/v1/keys/keys-manifest.json",
  "public/v1/keys/sets/deep/0123456789ab/keys-manifest.json",
  "public/v1/health.json",
  "contract/typing-feel.v1.json",
  "tools/import-staging.mjs",
  "tests/fixture.mjs",
  "README.md",
  "package.json",
  ".gitignore",
  "media.md5",
];

test("typing-feel/.gitignore keeps every media file out of Git and the JSON in", (t) => {
  const inside = git(["rev-parse", "--is-inside-work-tree"]);
  if (inside.error || inside.status !== 0 || inside.stdout.trim() !== "true") {
    t.skip(`${ROOT} is not in a Git work tree (or git is missing): .gitignore check skipped`);
    return;
  }
  // --no-index tests the rules themselves, whether or not a path is tracked.
  const result = git(["check-ignore", "--no-index", "--stdin"], `${[...IGNORED, ...TRACKED].join("\n")}\n`);
  assert.ok(result.status === 0 || result.status === 1, `git check-ignore failed: ${result.stderr}`);
  const ignored = new Set(result.stdout.split("\n").filter(Boolean));
  assert.deepEqual(IGNORED.filter((file) => !ignored.has(file)), [], "media or scratch that Git would track");
  assert.deepEqual(TRACKED.filter((file) => ignored.has(file)), [], "JSON, code or docs that Git would ignore");
});
