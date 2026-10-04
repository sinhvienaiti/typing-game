import { Worker } from "node:worker_threads";
import { createServer } from "node:http";
import { readFile } from "node:fs/promises";
import { resolve, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { createHash } from "node:crypto";
import { loadOfflineVoskWorker } from "./offline-vosk-plugin.mjs";

// Runs the actual pinned WASM Worker in Node with browser transport shims.
// This is an engine smoke test, not microphone/browser/performance acceptance.
const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const manifest = JSON.parse(
  await readFile(resolve(root, "shared/voice/model-manifest.json"), "utf8"),
);
const model = await readFile(
  resolve(root, `portal/public/assets/voice/${manifest.modelId}.tar.gz`),
);
if (
  createHash("sha256").update(model).digest("hex") !== manifest.artifactSha256
)
  throw new Error("Prepare the pinned model first");
const fixturePath = process.argv[2];
if (!fixturePath)
  throw new Error("Usage: pnpm voice:smoke /path/to/mono-16k-pcm16.wav");
const wav = await readFile(fixturePath);
let audio = null;
if (
  wav.toString("ascii", 0, 4) !== "RIFF" ||
  wav.toString("ascii", 8, 12) !== "WAVE"
)
  throw new Error("PCM WAV required");
for (let offset = 12; offset + 8 <= wav.length; ) {
  const kind = wav.toString("ascii", offset, offset + 4),
    bytes = wav.readUInt32LE(offset + 4),
    data = offset + 8;
  if (
    kind === "fmt " &&
    (wav.readUInt16LE(data) !== 1 ||
      wav.readUInt16LE(data + 2) !== 1 ||
      wav.readUInt32LE(data + 4) !== 16000 ||
      wav.readUInt16LE(data + 14) !== 16)
  )
    throw new Error("Mono PCM16 16 kHz required");
  if (kind === "data") audio = wav.subarray(data, data + bytes);
  offset = data + bytes + (bytes % 2);
}
if (!audio) throw new Error("WAV audio missing");
const server = createServer((request, response) => {
  if (request.url !== "/model.tar.gz") {
    response.writeHead(404).end();
    return;
  }
  response.writeHead(200, {
    "Content-Type": "application/gzip",
    "Content-Length": model.length,
  });
  response.end(model);
});
await new Promise((resolve) => server.listen(0, "127.0.0.1", resolve));
const { port } = server.address();
const bootstrap = String.raw`
const {parentPort} = require('node:worker_threads');
globalThis.self=globalThis;globalThis.location={href:'http://127.0.0.1/voice-worker.js'};
globalThis.postMessage=value=>parentPort.postMessage(value);
globalThis.addEventListener=(event,callback)=>{if(event==='message')parentPort.on('message',data=>callback({data}));};
globalThis.close=()=>process.exit(0);
class XHR {
  open(method,url,async=true){this.method=method;this.url=url;this.async=async;this.readyState=1;}
  setRequestHeader(){}
  getResponseHeader(){return null;}
  getAllResponseHeaders(){return '';}
  abort(){this.aborted=true;}
  send(body){
    fetch(this.url,{method:this.method,body:body??undefined}).then(async response=>{
      this.status=response.status;this.responseURL=response.url;
      const bytes=await response.arrayBuffer();this.response=this.responseType==='arraybuffer'?bytes:new TextDecoder().decode(bytes);
      if(typeof this.response==='string')this.responseText=this.response;
      this.readyState=4;this.onreadystatechange?.();this.onload?.({target:this,loaded:bytes.byteLength,total:bytes.byteLength});
    }).catch(error=>{this.status=0;this.onerror?.(error);});
  }
}
globalThis.XMLHttpRequest=XHR;
`;
const { source } = loadOfflineVoskWorker();
const worker = new Worker(bootstrap + source, { eval: true });
const events = [],
  waiters = [];
const wait = (predicate) =>
  new Promise((resolve, reject) => {
    const cached = events.find(predicate);
    if (cached) {
      events.splice(events.indexOf(cached), 1);
      resolve(cached);
      return;
    }
    const timer = setTimeout(
      () => reject(new Error("Worker smoke timed out")),
      60000,
    );
    waiters.push({
      predicate,
      resolve: (value) => {
        clearTimeout(timer);
        resolve(value);
      },
      reject: (error) => {
        clearTimeout(timer);
        reject(error);
      },
    });
  });
worker.on("message", (value) => {
  if (!value || typeof value !== "object") return;
  if (value.event === "error") {
    waiters
      .splice(0)
      .forEach((waiter) => waiter.reject(new Error(value.error)));
    return;
  }
  const index = waiters.findIndex((waiter) => waiter.predicate(value));
  if (index >= 0) waiters.splice(index, 1)[0].resolve(value);
  else events.push(value);
});
worker.on("error", (error) =>
  waiters.splice(0).forEach((waiter) => waiter.reject(error)),
);
const start = performance.now();
try {
  worker.postMessage({ action: "set", key: "logLevel", value: -1 });
  worker.postMessage({
    action: "load",
    modelUrl: `http://127.0.0.1:${port}/model.tar.gz`,
  });
  const loaded = await wait((value) => value.event === "load");
  if (!loaded.result) throw new Error("WASM model failed to load");
  worker.postMessage({
    action: "create",
    recognizerId: "smoke",
    sampleRate: 16000,
  });
  await wait((value) => value.event === "recognizer-ready");
  worker.postMessage({
    action: "set",
    key: "words",
    value: true,
    recognizerId: "smoke",
  });
  const results = [],
    timings = [];
  for (let offset = 0; offset < audio.length; offset += 3200) {
    const chunk = audio.subarray(offset, Math.min(audio.length, offset + 3200));
    const data = Float32Array.from({ length: chunk.length / 2 }, (_, index) =>
      chunk.readInt16LE(index * 2),
    );
    const sent = performance.now();
    worker.postMessage(
      { action: "audioChunk", recognizerId: "smoke", sampleRate: 16000, data },
      [data.buffer],
    );
    const result = await wait(
      (value) =>
        value.recognizerId === "smoke" &&
        ["partialresult", "result"].includes(value.event),
    );
    timings.push(performance.now() - sent);
    if (result.event === "result" && result.result?.text)
      results.push(result.result);
  }
  worker.postMessage({ action: "retrieveFinalResult", recognizerId: "smoke" });
  const final = await wait(
    (value) => value.event === "result" && value.recognizerId === "smoke",
  );
  if (final.result?.text) results.push(final.result);
  if (!results.length || results.some((result) => !result.result?.length))
    throw new Error("No final timestamped lexical results");
  timings.sort((a, b) => a - b);
  console.log(
    JSON.stringify(
      {
        engine: manifest.engineId,
        fixtureSha256: createHash("sha256").update(wav).digest("hex"),
        finalResults: results,
        decodeBlockMedianMs: timings[Math.floor(timings.length / 2)],
        decodeBlockP95Ms: timings[Math.floor(timings.length * 0.95)],
        totalMs: performance.now() - start,
        scope:
          "Node WASM engine smoke; excludes microphone, browser and end-to-end latency",
      },
      null,
      2,
    ),
  );
} finally {
  waiters
    .splice(0)
    .forEach((waiter) => waiter.reject(new Error("Worker stopped")));
  await worker.terminate();
  await new Promise((resolve) => server.close(resolve));
}
