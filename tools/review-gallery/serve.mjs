// Read-only static server for the owner's review page: 127.0.0.1 only, files under ROOT, Range requests for video.
import { createServer } from "node:http";
import { createReadStream, realpathSync, statSync } from "node:fs";
import { dirname, extname, isAbsolute, relative, resolve, sep } from "node:path";
import { fileURLToPath } from "node:url";
import { parseArgs } from "node:util";

let ROOT, PORT;
try {
  const { values, positionals } = parseArgs({
    options: { root: { type: "string" }, port: { type: "string" } },
    allowPositionals: true,
  });
  if (positionals.length > 1) throw new Error("Chỉ nhận một cổng ở vị trí đầu.");
  const port = values.port ?? positionals[0] ?? "4330";
  if (!/^\d+$/.test(port)) throw new Error("Cổng phải là số nguyên.");
  PORT = Number(port);
  if (!Number.isSafeInteger(PORT) || PORT > 65535) throw new Error("Cổng phải từ 0 đến 65535.");
  ROOT = realpathSync(values.root ?? resolve(dirname(realpathSync(fileURLToPath(import.meta.url))), "../../.."));
  if (!statSync(ROOT).isDirectory()) throw new Error("--root phải là thư mục.");
} catch (error) {
  console.error(`${error.message}\nDùng: node serve.mjs [cổng] [--root htdocs] [--port 4330]`);
  process.exit(1);
}
const TYPES = { ".html": "text/html; charset=utf-8", ".mp4": "video/mp4", ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".json": "application/json", ".txt": "text/plain; charset=utf-8", ".css": "text/css", ".js": "text/javascript" };

function withinRoot(file) {
  const path = relative(ROOT, file);
  return path !== ".." && !path.startsWith(`..${sep}`) && !isAbsolute(path);
}

const server = createServer((req, res) => {
  if (req.method !== "GET" && req.method !== "HEAD") {
    res.writeHead(405, { Allow: "GET, HEAD" }).end(); return;
  }
  let file;
  try {
    const path = decodeURIComponent(new URL(req.url, "http://localhost").pathname);
    file = resolve(ROOT, "." + (path.endsWith("/") ? path + "index.html" : path));
    if (path.includes("\0")) throw new Error("Invalid path");
  } catch {
    res.writeHead(400).end("bad path"); return;
  }
  if (!withinRoot(file)) { res.writeHead(403).end(); return; }
  let st;
  try {
    file = realpathSync(file);
    if (!withinRoot(file)) { res.writeHead(403).end(); return; }
    st = statSync(file);
  } catch { res.writeHead(404).end("not found"); return; }
  if (!st.isFile()) { res.writeHead(404).end("not a file"); return; }
  const type = TYPES[extname(file).toLowerCase()] ?? "application/octet-stream";
  function stream(options) {
    if (req.method === "HEAD") { res.end(); return; }
    const source = createReadStream(file, options);
    source.on("error", () => res.destroy());
    res.on("close", () => source.destroy());
    source.pipe(res);
  }
  if (req.headers.range !== undefined) {
    const range = /^bytes=(\d*)-(\d*)$/.exec(req.headers.range);
    let start = NaN, end = NaN;
    if (range && (range[1] || range[2])) {
      if (range[1]) {
        start = Number(range[1]);
        end = range[2] ? Number(range[2]) : st.size - 1;
      } else if (Number(range[2]) > 0) {
        start = Math.max(0, st.size - Number(range[2]));
        end = st.size - 1;
      }
    }
    if (!Number.isSafeInteger(start) || !Number.isSafeInteger(end) || start < 0 || start >= st.size || end < start) {
      res.writeHead(416, { "Content-Range": `bytes */${st.size}`, "Accept-Ranges": "bytes" }).end(); return;
    }
    end = Math.min(end, st.size - 1);
    res.writeHead(206, { "Content-Type": type, "Content-Range": `bytes ${start}-${end}/${st.size}`, "Accept-Ranges": "bytes", "Content-Length": end - start + 1 });
    stream({ start, end });
    return;
  }
  res.writeHead(200, { "Content-Type": type, "Content-Length": st.size, "Accept-Ranges": "bytes" });
  stream();
});
server.on("error", error => { console.error(error.message); process.exitCode = 1; });
server.listen(PORT, "127.0.0.1", () => console.log(`review gallery on http://127.0.0.1:${server.address().port}/`));
