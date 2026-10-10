import { createHash } from "node:crypto";
import { readFile, mkdir, writeFile, rename } from "node:fs/promises";
import { resolve, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const spec = JSON.parse(
  await readFile(resolve(root, "shared/voice/model-manifest.json"), "utf8"),
);
const output = resolve(root, "portal/public/assets/voice");
const modelName = `${spec.modelId}.tar.gz`;
const manifestPath = resolve(output, "manifest.json");
const digest = (bytes) => createHash("sha256").update(bytes).digest("hex");
try {
  const old = JSON.parse(await readFile(manifestPath, "utf8"));
  const bytes = await readFile(resolve(output, modelName));
  const vocabulary = await readFile(resolve(output, "vocabulary.json"));
  if (
    old.modelId === spec.modelId &&
    old.engineId === spec.engineId &&
    old.bytes === bytes.length &&
    old.sha256 === spec.artifactSha256 &&
    digest(bytes) === spec.artifactSha256 &&
    old.vocabularySha256 === spec.vocabularySha256 &&
    digest(vocabulary) === spec.vocabularySha256 &&
    (await readFile(resolve(output, "LICENSE.txt"), "utf8").then(
      (text) => text.length > 10000,
    ))
  ) {
    console.log("Voice offline model already prepared.");
    process.exit(0);
  }
} catch {
  /* First install or incomplete artifact: rebuild before publishing manifest. */
}
await mkdir(output, { recursive: true });
const cache = resolve(root, ".cache/voice");
await mkdir(cache, { recursive: true });
const archive = resolve(cache, "vosk-model-small-en-us-0.15.zip");
let zip;
try {
  zip = await readFile(archive);
} catch {
  /* Download only on first preparation. */
}
if (
  !zip ||
  zip.length !== spec.sourceBytes ||
  digest(zip) !== spec.sourceSha256
) {
  console.log("Preparing the English offline voice model (40 MB, once)...");
  const response = await fetch(spec.source, {
    signal: AbortSignal.timeout(120000),
  });
  if (!response.ok)
    throw new Error(`Voice model download failed: HTTP ${response.status}`);
  zip = Buffer.from(await response.arrayBuffer());
  if (zip.length !== spec.sourceBytes || digest(zip) !== spec.sourceSha256)
    throw new Error("Voice model checksum mismatch.");
  await writeFile(archive + ".partial", zip);
  await rename(archive + ".partial", archive);
}
const temp = resolve(output, modelName + ".partial");
// Python's standard library is available on macOS/WSL. No pip/Docker dependency.
// Verify the source ZIP first; deterministic repacking pins the actual browser artifact.
const python = String.raw`
import gzip,io,sys,tarfile,zipfile,struct,json
z=zipfile.ZipFile(sys.argv[1])
# Extract the model's own OpenFst symbol table for capability checks; no guessed dictionary.
b=z.read('vosk-model-small-en-us-0.15/graph/Gr.fst');o=4
def string():
 global o
 n=struct.unpack_from('<i',b,o)[0];o+=4
 if n<0 or n>1000000: raise ValueError('Invalid symbol length')
 v=b[o:o+n].decode();o+=n;return v
if struct.unpack_from('<I',b)[0]!=0x7eb2fdd6: raise ValueError('Invalid FST header')
string();string();o+=40
if struct.unpack_from('<I',b,o)[0]!=0x7eb2fb74: raise ValueError('Missing FST vocabulary')
o+=4;string();available,count=struct.unpack_from('<qq',b,o);o+=16
if count<1 or count>200000: raise ValueError('Invalid symbol count')
words=[]
for _ in range(count):
 word=string();o+=8
 if word and not word.startswith(('<','[','#','!')): words.append(word.lower())
with open(sys.argv[3],'wb') as out: out.write((json.dumps(sorted(set(words)),separators=(',',':'))+'\n').encode())
with open(sys.argv[2],'wb') as out:
 with gzip.GzipFile(filename='',mode='wb',fileobj=out,mtime=0,compresslevel=9) as gz:
  with tarfile.open(fileobj=gz,mode='w',format=tarfile.USTAR_FORMAT) as tar:
   for name in sorted(z.namelist()):
    parts=name.rstrip('/').split('/')[1:]
    if any(p in ('','..','.') for p in parts): raise ValueError('Invalid model archive path')
    if name.endswith('/'):
     info=tarfile.TarInfo('model'+('/'+'/'.join(parts) if parts else ''));info.type=tarfile.DIRTYPE;info.mode=0o755;info.mtime=0
     tar.addfile(info);continue
    if not parts: raise ValueError('Invalid model file path')
    data=z.read(name)
    if '/'.join(parts)=='conf/model.conf':
     data=data.decode().replace('--endpoint.rule2.min-trailing-silence=0.5','--endpoint.rule2.min-trailing-silence=0.25').replace('--endpoint.rule3.min-trailing-silence=0.75','--endpoint.rule3.min-trailing-silence=0.35').replace('--endpoint.rule4.min-trailing-silence=1.0','--endpoint.rule4.min-trailing-silence=0.5').encode()
    info=tarfile.TarInfo('model/'+'/'.join(parts));info.size=len(data);info.mode=0o644;info.mtime=0
    tar.addfile(info,io.BytesIO(data))
`;
const vocabularyTemp = resolve(output, "vocabulary.json.partial");
const packed = spawnSync(
  "python3",
  ["-c", python, archive, temp, vocabularyTemp],
  { stdio: "inherit" },
);
if (packed.status !== 0)
  throw new Error(
    "Unable to prepare Voice model. Install Python 3 and retry ./dev.sh space.",
  );
const bytes = await readFile(temp);
if (
  bytes.length !== spec.artifactBytes ||
  digest(bytes) !== spec.artifactSha256
)
  throw new Error("Prepared Voice artifact does not match the pinned build.");
const vocabulary = await readFile(vocabularyTemp);
if (
  vocabulary.length !== spec.vocabularyBytes ||
  digest(vocabulary) !== spec.vocabularySha256
)
  throw new Error("Voice model vocabulary does not match the pinned build.");
await rename(temp, resolve(output, modelName));
await rename(vocabularyTemp, resolve(output, "vocabulary.json"));
await writeFile(
  resolve(output, "LICENSE.txt"),
  await readFile(resolve(root, "shared/voice/vendor/APACHE-2.0.txt")),
);
await writeFile(
  resolve(output, "NOTICE.txt"),
  await readFile(resolve(root, "shared/voice/vendor/NOTICE.txt")),
);
const manifest = {
  ...spec,
  url: `/assets/voice/${modelName}`,
  bytes: bytes.length,
  sha256: digest(bytes),
};
await writeFile(
  manifestPath + ".partial",
  JSON.stringify(manifest, null, 2) + "\n",
);
await rename(manifestPath + ".partial", manifestPath);
console.log(
  `Voice model ready: ${bytes.length} bytes; SHA-256 ${manifest.sha256}`,
);
