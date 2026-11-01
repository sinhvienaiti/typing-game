// Typing Feedback Lab: a Vite page to try the kit's focus strip, letter styles and key sounds before
// they go into a game (docs/games/TYPING_FEEDBACK_REVIEW.md). Run from the parent repo:
//   shared/game-kit/node_modules/.bin/vite --config tools/typing-feedback-lab/vite.config.mjs
// Read-only mounts: the games' vocabulary, font and ticket-180 speaker art; external keyboard
// staging (LAB_KEYS overrides the ticket-218 v2 default); backdrops kept in this tool's tmp/.
import { createReadStream, existsSync, realpathSync, statSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));
const repo = path.resolve(here, "../..");
// External staging is read-only. No media is copied into the repo.
const MOUNTS = {
  "/lab-keys/": process.env.LAB_KEYS ?? path.join(repo, "tmp/keys-firefly/staging-v2/keys-firefly"),
  "/lab-keyboard-icon/": path.join(repo, "games/dragon-hold/art-src/ui/quick-settings/selected"),
  "/lab-vocab/dragon-hold/": path.join(repo, "games/dragon-hold/public/vocabulary"),
  "/lab-vocab/typing-defense/": path.join(repo, "games/typing-defense/public/vocabulary"),
  "/lab-vocab/typing-survival/": path.join(repo, "games/typing-survival/public/vocabulary"),
  "/lab-fonts/": path.join(repo, "games/dragon-hold/node_modules/@fontsource/be-vietnam-pro/files"),
  "/lab-backdrop/": path.join(here, "tmp/backdrops"),
  // Last Line's UI art (the word plate for the Load host mode), read-only from its own asset folder.
  "/lab-ui/typing-survival/": path.join(repo, "games/typing-survival/public/assets/typing-survival/ui"),
};
const TYPES = { ".webp": "image/webp", ".json": "application/json", ".ogg": "audio/ogg", ".wav": "audio/wav", ".woff2": "font/woff2", ".jpg": "image/jpeg", ".png": "image/png", ".webp": "image/webp" };

/** Serves each mount read-only; a path that leaves its folder is refused. */
const mounts = {
  name: "typing-fx-lab-mounts",
  configureServer(server) {
    server.middlewares.use((req, res, next) => {
      const url = (req.url ?? "").split("?")[0];
      for (const [prefix, dir] of Object.entries(MOUNTS)) {
        if (!url.startsWith(prefix)) continue;
        if (req.method !== "GET" && req.method !== "HEAD") {
          res.statusCode = 405;
          res.setHeader("Allow", "GET, HEAD");
          res.end();
          return;
        }
        let relative;
        try { relative = decodeURIComponent(url.slice(prefix.length)); }
        catch { res.statusCode = 400; res.end("bad path"); return; }
        const file = path.resolve(dir, relative);
        if (!file.startsWith(path.resolve(dir) + path.sep) || !existsSync(file) || !statSync(file).isFile() || !realpathSync(file).startsWith(realpathSync(dir) + path.sep)) {
          res.statusCode = 404;
          res.end("not found");
          return;
        }
        res.setHeader("Content-Type", TYPES[path.extname(file).toLowerCase()] ?? "application/octet-stream");
        res.setHeader("Cache-Control", "no-cache");
        if (req.method === "HEAD") res.end();
        else createReadStream(file).pipe(res);
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
