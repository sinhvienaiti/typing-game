// Typing Feedback Lab: a Vite page to try the kit's focus strip, letter styles and key sounds before
// they go into a game (docs/games/TYPING_FEEDBACK_REVIEW.md). Run from the parent repo:
//   shared/game-kit/node_modules/.bin/vite --config tools/typing-feedback-lab/vite.config.mjs
// Read-only mounts: the games' pinned vocabulary and font files, the Audio Lab's staged keyboard
// sounds (~/AudioLab/review/staging/keys, owner 29/10) and backdrops kept in this tool's tmp/.
import { createReadStream, existsSync, statSync } from "node:fs";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));
const repo = path.resolve(here, "../..");
// Keyboard profiles: Codex's ticket 182 output (<repo>/tmp/keys-codex/<id>/) once it exists, else the Audio Lab staging folder.
const CODEX_KEYS = path.join(repo, "tmp/keys-codex");
const MOUNTS = {
  "/lab-keys/": process.env.LAB_KEYS ?? (existsSync(CODEX_KEYS) ? CODEX_KEYS : path.join(os.homedir(), "AudioLab/review/staging/keys")),
  "/lab-vocab/dragon-hold/": path.join(repo, "games/dragon-hold/public/vocabulary"),
  "/lab-vocab/typing-defense/": path.join(repo, "games/typing-defense/public/vocabulary"),
  "/lab-vocab/typing-survival/": path.join(repo, "games/typing-survival/public/vocabulary"),
  "/lab-fonts/": path.join(repo, "games/dragon-hold/node_modules/@fontsource/be-vietnam-pro/files"),
  "/lab-backdrop/": path.join(here, "tmp/backdrops"),
};
const TYPES = { ".json": "application/json", ".ogg": "audio/ogg", ".wav": "audio/wav", ".woff2": "font/woff2", ".jpg": "image/jpeg", ".png": "image/png", ".webp": "image/webp" };

/** Serves each mount read-only; a path that leaves its folder is refused. */
const mounts = {
  name: "typing-fx-lab-mounts",
  configureServer(server) {
    server.middlewares.use((req, res, next) => {
      const url = (req.url ?? "").split("?")[0];
      for (const [prefix, dir] of Object.entries(MOUNTS)) {
        if (!url.startsWith(prefix)) continue;
        const file = path.resolve(dir, decodeURIComponent(url.slice(prefix.length)));
        if (!file.startsWith(path.resolve(dir) + path.sep) || !existsSync(file) || !statSync(file).isFile()) {
          res.statusCode = 404;
          res.end("not found");
          return;
        }
        res.setHeader("Content-Type", TYPES[path.extname(file).toLowerCase()] ?? "application/octet-stream");
        res.setHeader("Cache-Control", "no-cache");
        createReadStream(file).pipe(res);
        return;
      }
      next();
    });
  },
};

export default {
  root: here,
  plugins: [mounts],
  clearScreen: false,
  server: { host: "127.0.0.1", port: Number(process.env.PORT ?? 4192), strictPort: true, fs: { allow: [repo] }, watch: { ignored: ["**/tmp/**"] } },
};
