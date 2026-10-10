import { createReadStream, stat } from "node:fs";
import { resolve } from "node:path";

/** An archive is payload, NOT HTTP Content-Encoding. Vite's static server
 * treats .gz as precompressed content; fetch would then hash an inflated tar. */
export function voiceModelMiddleware(publicDir, modelId) {
  const url = `/assets/voice/${modelId}.tar.gz`;
  const file = resolve(publicDir, `assets/voice/${modelId}.tar.gz`);
  return (request, response, next) => {
    if (request.url?.split("?")[0] !== url ||
        !["GET", "HEAD"].includes(request.method ?? "")) return next();
    stat(file, (error, info) => {
      if (error || !info.isFile()) {
        response.statusCode = 404;
        response.end("Offline Voice model not prepared. Run pnpm voice:prepare.");
        return;
      }
      response.setHeader("Content-Type", "application/gzip");
      response.setHeader("Content-Length", info.size);
      response.setHeader("Cache-Control", "no-cache, no-transform");
      response.removeHeader("Content-Encoding");
      if (request.method === "HEAD") return response.end();
      const stream = createReadStream(file);
      response.on("close", () => stream.destroy());
      stream.on("error", () => response.destroy());
      stream.pipe(response);
    });
  };
}
