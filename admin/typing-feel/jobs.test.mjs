// node --test admin/typing-feel/jobs.test.mjs
// Format jobs of Add sound set (docs/games/TYPING_FEEL_SERVICE.md §3.8, §3.9):
// one at a time, the tool as an argument array (never a shell), every failure
// with a reason, recovery after a restart, Accept as one immutable Media V2
// bundle, and an accepted set through Save draft → Publish → Rollback.
// The tool is fake-natural-tool.mjs, except one test that runs the real Audio
// Lab tool on the owner's raindrop.wav when this machine has it (read only,
// AUDIOLAB_HOME in a temp folder so nothing is written under ~/AudioLab).
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { existsSync } from "node:fs";
import { mkdir, readdir, readFile, symlink, writeFile } from "node:fs/promises";
import { homedir } from "node:os";
import { join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import test from "node:test";
import { AdminConflictError } from "../store.mjs";
import { FAKE_NATURAL_TOOL as FAKE_TOOL, activeConfig, fakeWav, makeTypingFeelFixture, readCatalogue, tempDir } from "./fixture.mjs";
import {
  FORMATTED_RETENTION_MS,
  JOB_RETENTION_MS,
  SOURCE_TAGS,
  TypingFeelJobError,
  TypingFeelJobs,
  UPLOAD_RULES,
  checkFormatMachine,
  defaultFormatTool,
  megabytesPast,
  provenanceNote,
  slugFromName,
  stopFormatToolOnExit,
  titleFromName,
} from "./jobs.mjs";
import { TypingFeelNotFoundError } from "./service.mjs";

const HERE = fileURLToPath(new URL(".", import.meta.url));
const REPO = resolve(HERE, "../..");
const quiet = { log() {}, warn() {}, error() {} };
const READY = async () => ({ ready: true, venv: true, ffmpeg: true, problems: [] });

async function jobsHarness(t, { mode = "ok", env = {}, timeoutMs, machine = READY } = {}) {
  const fx = await makeTypingFeelFixture(t);
  const logFile = join(fx.base, "fake-runs.jsonl");
  const tool = { command: process.execPath, args: [FAKE_TOOL], cwd: fx.base, env: { PATH: process.env.PATH, FAKE_NATURAL_MODE: mode, FAKE_NATURAL_LOG: logFile, ...env } };
  const jobs = new TypingFeelJobs({ store: fx.store, service: fx.service, mediaStore: fx.mediaStore, tool, machine, ...(timeoutMs ? { timeoutMs } : {}), logger: quiet });
  const upload = async ({ name = "raindrop.wav", bytes = fakeWav(name), tags = SOURCE_TAGS } = {}) => (await fx.mediaStore.createUploadAsset({ kind: "audio", title: name, filename: name, mimeType: "audio/wav", buffer: bytes, tags, actorId: "test" })).version;
  const runs = async () => (existsSync(logFile) ? (await readFile(logFile, "utf8")).split("\n").filter(Boolean).map((line) => JSON.parse(line)) : []);
  const format = async (input = {}) => {
    const source = input.source ?? (await upload());
    const job = await jobs.create({ sourceAssetVersionId: source.assetVersionId, ...input, source: undefined });
    await jobs.whenIdle();
    return { source, job, result: await jobs.get(job.jobId) };
  };
  return { fx, jobs, tool, upload, runs, format };
}

test("the page defaults follow the tool: id and name from the file name", () => {
  assert.equal(slugFromName("raindrop.wav"), "raindrop");
  assert.equal(slugFromName("Hail Stone v4.WAV"), "hail-stone-v4");
  assert.equal(slugFromName("off.wav"), "new-set");
  assert.equal(slugFromName("---.wav"), "new-set");
  assert.equal(titleFromName("hail-v4.wav"), "Hail V4");
  assert.equal(titleFromName("raindrop.wav"), "Raindrop");
});

test("the upload rules the page shows are the tool's (natural.py UPLOAD)", async () => {
  const source = await readFile(join(REPO, "tools/audio-lab/keys/natural.py"), "utf8");
  const block = /^UPLOAD = \{([\s\S]*?)^\}/m.exec(source)?.[1] ?? "";
  const number = (key) => {
    const match = new RegExp(`"${key}": ([^,\\n]+),`).exec(block);
    assert.ok(match, `natural.py UPLOAD has ${key}`);
    return Function(`return (${match[1].replace(/[()]/g, "")})`)();
  };
  for (const key of ["minSeconds", "maxSeconds", "maxBytes", "minUsableTaps", "usableWithinDb", "usableGapMs", "fullScale", "noiseFloorDbfs", "tapsPerSecond"]) {
    assert.equal(UPLOAD_RULES[key], number(key), key);
  }
  assert.match(block, /"sampleRates": \(44100, 48000\)/);
  assert.match(block, /"channels": \(1, 2\)/);
  assert.deepEqual(UPLOAD_RULES.sampleRates, [44100, 48000]);
});

test("Format runs the tool once with an argument array, never a shell, and records every state", async (t) => {
  const { fx, jobs, runs, upload } = await jobsHarness(t);
  const marker = join(fx.base, "pwned");
  const name = `Rain "Drop" $(touch ${marker}); rm -rf x`.slice(0, 60);
  const source = await upload();
  const job = await jobs.create({ sourceAssetVersionId: source.assetVersionId, setId: "rain-tile", name, family: "bright-clack", actorId: "owner" });
  assert.equal(job.status, "queued");
  assert.match(job.jobId, /^j\d{8}-\d{6}-[0-9a-f]{6}$/);
  assert.equal(job.source.assetVersionId, source.assetVersionId);
  assert.equal(job.source.fileName, "raindrop.wav");
  await jobs.whenIdle();
  const result = await jobs.get(job.jobId);
  assert.equal(result.job.status, "succeeded", JSON.stringify(result.job.failure));
  assert.ok(result.job.startedAt && result.job.finishedAt);
  assert.equal(result.job.exitCode, 0);
  assert.deepEqual(result.job.summary.counts, { key: 12, space: 8 });
  assert.equal(result.job.summary.acceptAllowed, true);
  assert.equal(result.job.summary.leadIns, 1);
  assert.match(result.log, /rain-tile: 12 keys, 8 spaces/);
  assert.equal(result.report.status, "formatted");
  assert.equal(existsSync(marker), false, "nothing ran through a shell");
  const [run] = await runs();
  const dir = jobs.jobDir(job.jobId);
  assert.deepEqual(run.argv, [`--src=${join(dir, "in", "source.wav")}`, `--out=${join(dir, "out")}`, "--id=rain-tile", `--name=${name}`, "--family=bright-clack"]);
  assert.deepEqual(await readFile(join(dir, "in", "source.wav")), fakeWav("raindrop.wav"), "the tool reads a copy of the Media V2 blob");

  // Listen: files by one-segment name; nothing outside the job's out folder.
  const preview = await jobs.file(job.jobId, "preview.ogg");
  assert.equal(preview.contentType, "audio/ogg");
  assert.match(preview.body.toString("utf8"), /^OggS fake rain-tile preview\.ogg/);
  assert.equal((await jobs.file(job.jobId, "raw-cut.mp3")).contentType, "audio/mpeg");
  assert.equal((await jobs.file(job.jobId, "natural.mp3")).contentType, "audio/mpeg");
  assert.match((await jobs.file(job.jobId, "log.txt")).body.toString("utf8"), /keys natural/);
  for (const bad of ["../job.json", "job.json", "in/source.wav", "source.wav", "key-1.ogg", "ab/raw-cut.mp3", "..%2Fjob.json"]) assert.equal(await jobs.file(job.jobId, bad), null, bad);
  await assert.rejects(jobs.get("../../etc"), TypingFeelNotFoundError);
  await assert.rejects(jobs.get("j20261031-000000-abcdef"), TypingFeelNotFoundError);

  const listed = await jobs.list();
  assert.equal(listed.jobs[0].jobId, job.jobId);
  assert.equal(listed.jobs[0].status, "succeeded");
  assert.equal(listed.running, null);
});

test("one job at a time: a second Format waits for the first", async (t) => {
  const { jobs, runs, upload } = await jobsHarness(t, { env: { FAKE_NATURAL_DELAY_MS: "250" } });
  const a = await upload({ name: "take-a.wav" });
  const b = await upload({ name: "take-b.wav" });
  const first = await jobs.create({ sourceAssetVersionId: a.assetVersionId });
  const second = await jobs.create({ sourceAssetVersionId: b.assetVersionId });
  assert.equal(second.status, "queued");
  await jobs.whenIdle();
  const [one, two] = await runs();
  assert.ok(one.end <= two.start, `runs overlap: ${JSON.stringify([one, two])}`);
  assert.equal((await jobs.get(first.jobId)).job.status, "succeeded");
  assert.equal((await jobs.get(second.jobId)).job.status, "succeeded");
  assert.equal((await jobs.get(second.jobId)).job.set.id, "take-b");
});

test("every failure says why: refused take, machine problem, crash, timeout, bad output, missing venv", async (t) => {
  const { jobs, tool, format } = await jobsHarness(t, { timeoutMs: 700 });
  const run = async (mode) => {
    tool.env.FAKE_NATURAL_MODE = mode;
    return (await format()).result;
  };
  const refused = await run("refuse");
  assert.equal(refused.job.status, "failed");
  assert.equal(refused.job.failure.kind, "refused");
  assert.deepEqual(refused.job.failure.errors, ["Found 7 usable taps; need at least 12, each at least 150 ms before the next."]);
  assert.equal(refused.report.status, "refused");

  const machine = await run("machine");
  assert.equal(machine.job.failure.kind, "machine");
  assert.match(machine.job.failure.message, /ffmpeg is not on this machine's PATH/);
  assert.match(machine.job.failure.message, /bash tools\/audio-lab\/common\/setup\.sh/);

  const crashed = await run("crash");
  assert.equal(crashed.job.failure.kind, "crashed");
  assert.match(crashed.job.failure.message, /exit 3/);

  const started = Date.now();
  const slow = await run("sleep");
  assert.equal(slow.job.failure.kind, "timeout");
  assert.match(slow.job.failure.message, /longer than 1 s and was stopped/);
  assert.ok(Date.now() - started < 8000, "the tool was stopped, not waited for");

  const bad = await run("bad-output");
  assert.equal(bad.job.failure.kind, "output");
  assert.ok(bad.job.failure.errors.includes("Unexpected file evil.sh."));

  jobs.machine = async () => ({ ready: false, venv: false, ffmpeg: true, problems: ["The Audio Lab venv is missing (/nowhere/.venv)."] });
  const missing = await run("ok");
  assert.equal(missing.job.failure.kind, "machine");
  assert.match(missing.job.failure.message, /venv is missing.*Run `bash tools\/audio-lab\/common\/setup\.sh` on this machine/);
});

test("the machine check reads the Audio Lab venv and ffmpeg from the env the tool gets", async (t) => {
  const home = await tempDir(t);
  const missing = await checkFormatMachine({ env: { AUDIOLAB_HOME: home, PATH: home } });
  assert.equal(missing.ready, false);
  assert.equal(missing.problems.length, 2);
  await mkdir(join(home, ".venv", "bin"), { recursive: true });
  for (const name of ["python", "ffmpeg"]) await writeFile(join(home, ".venv", "bin", name), "#!/bin/sh\n", { mode: 0o755 });
  assert.equal((await checkFormatMachine({ env: { AUDIOLAB_HOME: home, PATH: "" } })).ready, true);
  const tool = defaultFormatTool({ repoRoot: REPO, env: { AUDIOLAB_HOME: home } });
  assert.equal(tool.command, "bash");
  assert.deepEqual(tool.args, [join(REPO, "tools/audio-lab/run.sh"), "keys", "natural"]);
});

test("Format refuses a bad source, a recipe it does not offer and an id that is live or retired", async (t) => {
  const { fx, jobs, upload } = await jobsHarness(t);
  const source = await upload();
  await assert.rejects(jobs.create({ sourceAssetVersionId: source.assetVersionId, recipe: "firefly-218" }), /offers natural-v1 only/);
  await assert.rejects(jobs.create({ sourceAssetVersionId: "media-version.nope" }), TypingFeelNotFoundError);
  await assert.rejects(jobs.create({ sourceAssetVersionId: "../../etc/passwd" }), TypingFeelJobError);
  const untagged = await upload({ name: "music.wav", tags: ["typing-feel"] });
  await assert.rejects(jobs.create({ sourceAssetVersionId: untagged.assetVersionId }), /must carry the tag keyboard-source/);
  for (const setId of ["off", "Bad Id", "-x", "a".repeat(33)]) await assert.rejects(jobs.create({ sourceAssetVersionId: source.assetVersionId, setId }), TypingFeelJobError, setId);
  await assert.rejects(jobs.create({ sourceAssetVersionId: source.assetVersionId, setId: "deep-amber" }), /already a live set/);
  await assert.rejects(jobs.create({ sourceAssetVersionId: source.assetVersionId, name: " padded" }), /without leading or trailing spaces/);

  // A take over 50 MB is refused before anything is copied or run.
  const getVersion = fx.mediaStore.getVersion.bind(fx.mediaStore);
  fx.mediaStore.getVersion = async (id) => {
    const version = await getVersion(id);
    if (id === source.assetVersionId) version.components[0].byteSize = UPLOAD_RULES.maxBytes + 1;
    return version;
  };
  await assert.rejects(jobs.create({ sourceAssetVersionId: source.assetVersionId }), /the limit is 50 MB/);
  fx.mediaStore.getVersion = getVersion;

  // Retired in a published revision: never used again.
  const { revision: seed, config } = await activeConfig(fx.store);
  config.keyboard.sets = config.keyboard.sets.filter((set) => set.id !== "deep-amber");
  config.keyboard.retiredIds = ["deep-amber"];
  const draft = await fx.service.saveDraft({ baseRevision: seed, config });
  await fx.service.publish({ revision: draft.revision, expectedActiveRevision: seed });
  await assert.rejects(jobs.create({ sourceAssetVersionId: source.assetVersionId, setId: "deep-amber" }), /was retired and is never used again/);
});

test("a restart marks queued and running jobs interrupted; old failed and discarded jobs are removed", async (t) => {
  const { fx, jobs, format } = await jobsHarness(t);
  const { job } = await format();
  const dir = jobs.jobDir(job.jobId);
  const record = JSON.parse(await readFile(join(dir, "job.json"), "utf8"));
  await writeFile(join(dir, "job.json"), JSON.stringify({ ...record, status: "running" }));
  const now = Date.now();
  const make = async (jobId, status, ageMs) => {
    await mkdir(jobs.jobDir(jobId), { recursive: true });
    const at = new Date(now - ageMs).toISOString();
    await writeFile(join(jobs.jobDir(jobId), "job.json"), JSON.stringify({ ...record, jobId, status, createdAt: at, finishedAt: at, updatedAt: at }));
  };
  await make("j20261001-000000-aaaaaa", "failed", JOB_RETENTION_MS + 60_000);
  await make("j20261002-000000-bbbbbb", "discarded", JOB_RETENTION_MS + 60_000);
  await make("j20261030-000000-cccccc", "failed", 60_000);
  await make("j20261003-000000-dddddd", "succeeded", JOB_RETENTION_MS + 60_000);

  const restarted = new TypingFeelJobs({ store: fx.store, service: fx.service, mediaStore: fx.mediaStore, tool: jobs.tool, machine: READY, logger: quiet });
  const { recovered, removed } = await restarted.recover();
  assert.deepEqual(recovered, [job.jobId]);
  assert.deepEqual(removed.sort(), ["j20261001-000000-aaaaaa", "j20261002-000000-bbbbbb"]);
  const after = (await restarted.get(job.jobId)).job;
  assert.equal(after.status, "failed");
  assert.equal(after.failure.kind, "interrupted");
  assert.deepEqual((await readdir(restarted.jobsDir)).sort(), [job.jobId, "j20261003-000000-dddddd", "j20261030-000000-cccccc"].sort(), "a recent failure and a waiting succeeded job stay");
});

test("Accept stores one immutable bundle, rewrites only the set manifest JSON and returns the draft row", async (t) => {
  const { fx, jobs, format } = await jobsHarness(t);
  const { job, source } = await format({ setId: "raindrop", name: "Raindrop" });
  const out = join(jobs.jobDir(job.jobId), "out");
  const before = new Map();
  for (const name of await readdir(out)) if (name.endsWith(".ogg")) before.set(name, await readFile(join(out, name)));
  const rawCut = await readFile(join(out, "ab", "raw-cut.mp3"));

  await assert.rejects(jobs.accept(job.jobId, { setId: "rain-two", name: "Rain Two", family: "bright-clack" }), /Owner score must be a number/);
  await assert.rejects(jobs.accept(job.jobId, { setId: "rain-two", name: "Rain Two", family: "bright-clack", ownerScore: 11 }), /from 0 to 10/);
  await assert.rejects(jobs.accept(job.jobId, { setId: "rain-two", name: "Rain Two", family: "bright-clack", ownerScore: 8.5 }), /only be Provisional, and a Provisional set needs a reason/);
  await assert.rejects(jobs.accept(job.jobId, { setId: "raindrop-tile", name: "Rain Two", family: "bright-clack", ownerScore: 9 }), /already a live set/);
  await assert.rejects(jobs.accept(job.jobId, { setId: "rain-two", name: "Rain Two", ownerScore: 9 }), /Choose the family/);

  const accepted = await jobs.accept(job.jobId, { setId: "rain-two", name: "Rain Two", family: "bright-clack", ownerScore: 9 }, { actorId: "owner" });
  assert.deepEqual(accepted.row, { id: "rain-two", name: "Rain Two", family: "bright-clack", order: 0, enabled: true, status: "published", assetVersionId: accepted.version.assetVersionId, ownerPick: false, ownerScore: 9, recipe: "natural-v1", score: null });
  const version = await fx.mediaStore.getVersion(accepted.version.assetVersionId);
  const asset = await fx.mediaStore.getAsset(version.assetId);
  assert.deepEqual(asset.tags, ["keyboard-set", "typing-feel"]);
  assert.equal(asset.title, "Rain Two");
  assert.equal(version.provenance, "admin-upload");
  const roles = version.components.map((component) => component.role);
  assert.deepEqual(roles.filter((role) => !/^(key|space)-/.test(role)), ["ab-natural", "ab-raw", "manifest", "preview", "report"]);
  assert.equal(roles.filter((role) => role.startsWith("key-")).length, 12);
  assert.equal(roles.filter((role) => role.startsWith("space-")).length, 8);
  assert.equal(version.source.sourcePath, source.assetVersionId, "§3.6: the source WAV's Media version");
  assert.equal(version.source.generator, "typing-feel natural-v1 (tools/audio-lab keys natural @fake)");
  assert.match(version.source.license, /Adobe Firefly/);
  assert.equal(JSON.parse(version.source.note).ownerScore, 9);
  const blob = async (role) => readFile((await fx.mediaStore.resolveComponent(version.assetVersionId, role)).absolutePath);
  for (const [name, bytes] of before) assert.deepEqual(await blob(name.replace(/\.ogg$/, "")), bytes, `${name} is stored byte for byte`);
  assert.deepEqual(await blob("ab-raw"), rawCut);
  const manifest = JSON.parse((await blob("manifest")).toString("utf8"));
  assert.equal(manifest.id, "rain-two");
  assert.equal(manifest.name, "Rain Two");
  assert.match((await blob("manifest")).toString("utf8"), /^\{\n {2}"schema": "typing-feel\/set-1",\n/, "one file per line, as import-staging writes it");
  const report = JSON.parse((await blob("report")).toString("utf8"));
  assert.deepEqual(report.set, { id: "rain-two", name: "Rain Two", family: "bright-clack", licence: manifest.licence });
  assert.equal(report.accept.ownerScore, 9);
  assert.equal(report.accept.status, "published");

  // The job keeps its record; its work folders go once the bytes are blobs.
  assert.equal(existsSync(out), false);
  assert.equal(existsSync(join(jobs.jobDir(job.jobId), "in")), false);
  const after = await jobs.get(job.jobId);
  assert.equal(after.job.status, "accepted");
  assert.equal(after.job.accepted.assetVersionId, version.assetVersionId);
  assert.equal(after.job.accepted.folder, `sets/rain-two/${version.contentFingerprint.slice(0, 12)}`);
  assert.equal(after.report.accept.jobId, job.jobId, "the report now comes from Media V2");
  assert.deepEqual((await jobs.file(job.jobId, "key-01.ogg")).body, before.get("key-01.ogg"));
  await assert.rejects(jobs.accept(job.jobId, { setId: "rain-three", name: "Rain Three", family: "deep", ownerScore: 9 }), AdminConflictError);
  await assert.rejects(jobs.discard(job.jobId), AdminConflictError);
});

test("a score under 9 accepts only as Provisional with its reason; a set under the minimum cannot be accepted", async (t) => {
  const { jobs, tool, format } = await jobsHarness(t);
  const { job } = await format({ setId: "rain-soft" });
  const provisional = await jobs.accept(job.jobId, { setId: "rain-soft", name: "Rain Soft", family: "deep", ownerScore: 7.5, reason: "Spaces too dull; waiting for a second take." });
  assert.equal(provisional.row.status, "provisional");
  assert.equal(provisional.row.ownerScore, 7.5);
  assert.equal(provisional.row.note, "Spaces too dull; waiting for a second take.");

  tool.env.FAKE_NATURAL_MODE = "few";
  const few = await format({ setId: "rain-few" });
  assert.equal(few.result.job.status, "succeeded");
  assert.equal(few.result.job.summary.acceptAllowed, false);
  await assert.rejects(jobs.accept(few.job.jobId, { setId: "rain-few", name: "Rain Few", family: "deep", ownerScore: 9 }), /8 keys and 8 spaces; a set needs at least 10 and 3/);
  tool.env.FAKE_NATURAL_MODE = "gate-fail";
  const gate = await format({ setId: "rain-gate" });
  await assert.rejects(jobs.accept(gate.job.jobId, { setId: "rain-gate", name: "Rain Gate", family: "deep", ownerScore: 9 }), /hard gates failed \(key-02\.ogg:tail\)/);

  // Discard: the job and its files go; it can never be accepted after.
  const discarded = await jobs.discard(few.job.jobId, { actorId: "owner" });
  assert.equal(discarded.status, "discarded");
  assert.equal(existsSync(join(jobs.jobDir(few.job.jobId), "out")), false);
  assert.equal((await jobs.discard(few.job.jobId)).status, "discarded", "discard twice is harmless");
  await assert.rejects(jobs.accept(few.job.jobId, { setId: "rain-few", name: "Rain Few", family: "deep", ownerScore: 9 }), /is discarded; only a formatted job/);
});

test("an accepted set goes through Save draft, Review and Publish to the catalogue, and Rollback removes it", async (t) => {
  const { fx, jobs, format } = await jobsHarness(t);
  const r1 = await readCatalogue(fx.publicDir);
  const { job } = await format({ setId: "rain-new" });
  const accepted = await jobs.accept(job.jobId, { setId: "rain-new", name: "Rain New", family: "bright-clack", ownerScore: 9.5 });
  const { revision: seed, config } = await activeConfig(fx.store);
  const order = Math.max(...config.keyboard.sets.filter((set) => set.family === "bright-clack").map((set) => set.order)) + 1;

  // Never the default while provisional (decision 5).
  const provisionalDefault = structuredClone(config);
  provisionalDefault.keyboard.sets.push({ ...accepted.row, order, status: "provisional", note: "test" });
  provisionalDefault.keyboard.defaultSet = "rain-new";
  await assert.rejects(fx.service.saveDraft({ baseRevision: seed, config: provisionalDefault }), /provisional set cannot be the default/);

  config.keyboard.sets.push({ ...accepted.row, order });
  const draft = await fx.service.saveDraft({ baseRevision: seed, config, message: "Add Rain New" });
  const review = await fx.service.validate(draft.revision);
  assert.equal(review.valid, true, review.problems.join(" "));
  assert.deepEqual(review.changeScope.added, ["rain-new"]);
  assert.deepEqual(review.plan.created, [accepted.job.accepted.folder]);
  const published = await fx.service.publish({ revision: draft.revision, expectedActiveRevision: seed });
  assert.deepEqual(published.folders.created, [accepted.job.accepted.folder]);
  const catalogue = JSON.parse(await readCatalogue(fx.publicDir));
  const row = catalogue.profiles.find((profile) => profile.id === "rain-new");
  assert.equal(row.name, "Rain New");
  assert.equal(row.familyId, "bright-clack");
  assert.equal(row.status, "published");
  assert.equal(row.keys, 12);
  assert.equal(row.spaces, 8);
  assert.equal(row.manifest, `${accepted.job.accepted.folder}/keys-manifest.json`);
  const folder = join(fx.publicDir, "v1/keys", accepted.job.accepted.folder);
  const written = (await readdir(folder)).sort();
  assert.equal(written.length, 12 + 8 + 2, "keys, spaces, preview and the set manifest; no report, A/B or source");
  assert.ok(!written.some((name) => /report|raw-cut|natural|source/.test(name)));
  const manifest = JSON.parse(await readFile(join(folder, "keys-manifest.json"), "utf8"));
  assert.equal(manifest.id, "rain-new");
  const references = await fx.mediaStore.listReferences({ assetVersionId: accepted.version.assetVersionId });
  assert.ok(references.some((reference) => reference.domain === "typing-feel.keyboard" && reference.entityId === "rain-new"));
  const sourceReferences = await fx.mediaStore.listReferences({ assetVersionId: job.source.assetVersionId });
  assert.ok(sourceReferences.some((reference) => reference.domain === "typing-feel.source" && reference.entityId === "rain-new"), "§3.6: the source WAV is referenced too");

  await fx.service.rollback({ targetRevision: seed, expectedActiveRevision: draft.revision });
  const back = await readCatalogue(fx.publicDir);
  assert.equal(JSON.parse(back).profiles.some((profile) => profile.id === "rain-new"), false);
  assert.equal(back, r1, "Rollback restores the seed catalogue byte for byte");
  assert.equal(existsSync(folder), true, "set folders are immutable and stay");
});

const RAINDROP = join(REPO, "tmp/keys-firefly/raindrop/src/raindrop.wav");
const REAL_VENV = join(homedir(), "AudioLab/.venv");
const ffmpeg = spawnSync("sh", ["-c", "command -v ffmpeg"], { encoding: "utf8" }).status === 0;
const realTool = existsSync(RAINDROP) && existsSync(join(REAL_VENV, "bin/python")) && ffmpeg;

test("the real Audio Lab tool formats the owner's raindrop.wav (read only; skipped without it)", { skip: realTool ? false : "no raindrop.wav, Audio Lab venv or ffmpeg on this machine", timeout: 180_000 }, async (t) => {
  const fx = await makeTypingFeelFixture(t);
  // AUDIOLAB_HOME in a temp folder (bytecode and caches land there), the real venv linked in read only.
  const home = await tempDir(t, "typing-feel-audiolab-");
  await symlink(REAL_VENV, join(home, ".venv"));
  const env = { ...process.env, AUDIOLAB_HOME: home };
  const jobs = new TypingFeelJobs({ store: fx.store, service: fx.service, mediaStore: fx.mediaStore, tool: defaultFormatTool({ repoRoot: REPO, env }), logger: quiet });
  assert.equal((await jobs.capabilities()).machine.ready, true);
  const bytes = await readFile(RAINDROP);
  const { version: source } = await fx.mediaStore.createUploadAsset({ kind: "audio", title: "raindrop.wav", filename: "raindrop.wav", mimeType: "audio/wav", buffer: bytes, tags: SOURCE_TAGS });
  const check = await jobs.check(source.assetVersionId);
  assert.equal(check.ok, true, JSON.stringify(check.errors));
  assert.equal(check.source.tapsFound, 22);
  assert.equal(check.source.tapsUsable, 17);
  assert.equal(check.source.file, "raindrop.wav");
  const job = await jobs.create({ sourceAssetVersionId: source.assetVersionId, setId: "raindrop-admin", name: "Raindrop Admin", family: "bright-clack" });
  await jobs.whenIdle();
  const result = await jobs.get(job.jobId);
  assert.equal(result.job.status, "succeeded", JSON.stringify(result.job.failure));
  assert.deepEqual(result.job.summary.counts, { key: 17, space: 8 });
  assert.equal(result.job.summary.acceptAllowed, true);
  assert.equal(result.report.preview.durationMs, 1000);
  const accepted = await jobs.accept(job.jobId, { setId: "raindrop-admin", name: "Raindrop Admin", family: "bright-clack", ownerScore: 9 });
  assert.equal(accepted.row.status, "published");
  const { revision: seed, config } = await activeConfig(fx.store);
  config.keyboard.sets.push({ ...accepted.row, order: 99 });
  const draft = await fx.service.saveDraft({ baseRevision: seed, config });
  await fx.service.publish({ revision: draft.revision, expectedActiveRevision: seed });
  const row = JSON.parse(await readCatalogue(fx.publicDir)).profiles.find((profile) => profile.id === "raindrop-admin");
  assert.equal(row.keys, 17);
  assert.equal(row.spaces, 8);
});

// ---------------------------------------------------------------- G7 review fixes (31/10)

test("a take named like a live, retired or once-published set still formats: the default id steps to a free one", async (t) => {
  const { fx, jobs, format, upload } = await jobsHarness(t);
  // Live: "Raindrop Tile.wav" slugs to the live raindrop-tile.
  const live = await format({ source: await upload({ name: "Raindrop Tile.wav" }) });
  assert.equal(live.result.job.status, "succeeded", JSON.stringify(live.result.job.failure));
  assert.equal(live.job.set.id, "raindrop-tile-2");
  assert.equal(live.job.set.name, "Raindrop Tile");
  // A typed id is never changed: refused with the reason.
  await assert.rejects(jobs.create({ sourceAssetVersionId: live.source.assetVersionId, setId: "raindrop-tile" }), /already a live set; choose a new id\. Replacing a live set's sound \(Re-format\) is not available yet/);
  // Retired, and the 32-character limit with a suffix.
  const { revision: seed, config } = await activeConfig(fx.store);
  config.keyboard.sets = config.keyboard.sets.filter((set) => set.id !== "deep-amber");
  config.keyboard.retiredIds = ["deep-amber"];
  const draft = await fx.service.saveDraft({ baseRevision: seed, config });
  await fx.service.publish({ revision: draft.revision, expectedActiveRevision: seed });
  const retired = await jobs.create({ sourceAssetVersionId: (await upload({ name: "deep amber.wav" })).assetVersionId });
  assert.equal(retired.set.id, "deep-amber-2");
  const long = await jobs.create({ sourceAssetVersionId: (await upload({ name: `${"a".repeat(30)}-raindrop-tile.wav` })).assetVersionId });
  assert.ok(long.set.id.length <= 32 && /^[a-z0-9][a-z0-9-]*$/.test(long.set.id), long.set.id);
  await jobs.whenIdle();
});

test("an id published once and taken out by Rollback never names another sound; the same sound may come back", async (t) => {
  const { fx, jobs, format } = await jobsHarness(t);
  const { job } = await format({ setId: "rain-back" });
  const accepted = await jobs.accept(job.jobId, { setId: "rain-back", name: "Rain Back", family: "bright-clack", ownerScore: 9 });
  const { revision: seed, config } = await activeConfig(fx.store);
  config.keyboard.sets.push({ ...accepted.row, order: 50 });
  const draft = await fx.service.saveDraft({ baseRevision: seed, config });
  await fx.service.publish({ revision: draft.revision, expectedActiveRevision: seed });
  await fx.service.rollback({ targetRevision: seed, expectedActiveRevision: draft.revision });

  // Format and Accept refuse the id for a new take; a take named like it steps on.
  const again = await format({ setId: "rain-back-two" });
  await assert.rejects(jobs.create({ sourceAssetVersionId: again.source.assetVersionId, setId: "rain-back" }), /was published before and taken out by a Rollback/);
  await assert.rejects(jobs.accept(again.job.jobId, { setId: "rain-back", name: "Rain Back", family: "bright-clack", ownerScore: 9 }), /was published before/);
  const other = await jobs.accept(again.job.jobId, { setId: "rain-back-two", name: "Rain Back Two", family: "bright-clack", ownerScore: 9 });

  // A draft cannot give the id a different sound…
  const after = await activeConfig(fx.store);
  const swapped = structuredClone(after.config);
  swapped.keyboard.sets.push({ ...other.row, id: "rain-back", order: 51 });
  await assert.rejects(fx.service.saveDraft({ baseRevision: after.revision, config: swapped }), /Set id rain-back was published before with another sound/);
  // …but the sound it was published with may come back under it.
  const restored = structuredClone(after.config);
  restored.keyboard.sets.push({ ...accepted.row, order: 50 });
  const back = await fx.service.saveDraft({ baseRevision: after.revision, config: restored });
  assert.equal((await fx.service.validate(back.revision)).valid, true);
});

test("decision 5 holds against the client: a draft keeps the status and owner score recorded at Accept", async (t) => {
  const { fx, jobs, format } = await jobsHarness(t);
  const { job } = await format({ setId: "probe-soft" });
  const accepted = await jobs.accept(job.jobId, { setId: "probe-soft", name: "Probe Soft", family: "bright-clack", ownerScore: 8, reason: "Spaces dull" });
  assert.equal(accepted.row.status, "provisional");
  const { revision: seed, config } = await activeConfig(fx.store);
  const add = (row) => {
    const next = structuredClone(config);
    next.keyboard.sets.push({ ...row, order: 60 });
    return next;
  };
  // The review's probe: Provisional (8, with reason) sent as Published 9.5 without a note.
  const { note, ...noNote } = accepted.row;
  assert.equal(note, "Spaces dull");
  await assert.rejects(
    fx.service.saveDraft({ baseRevision: seed, config: add({ ...noNote, status: "published", ownerScore: 9.5 }) }),
    /Set probe-soft: the owner accepted this sound as Provisional, owner score 8; the draft says Published, owner score 9\.5/,
  );
  await assert.rejects(fx.service.saveDraft({ baseRevision: seed, config: add({ ...accepted.row, ownerScore: 8.5 }) }), /owner score 8; the draft says Provisional, owner score 8\.5/);
  // As accepted: saved, and the Review names the status, the score and the reason.
  const draft = await fx.service.saveDraft({ baseRevision: seed, config: add(accepted.row) });
  const review = await fx.service.validate(draft.revision);
  assert.equal(review.valid, true, review.problems.join(" "));
  assert.ok(review.changeScope.summary.includes("Add probe-soft (Provisional, owner score 8: Spaces dull)."), review.changeScope.summary.join(" | "));
  assert.deepEqual(review.changeScope.addedDetails, [{ id: "probe-soft", status: "provisional", ownerScore: 8, note: "Spaces dull" }]);
  await fx.service.publish({ revision: draft.revision, expectedActiveRevision: seed });
  // Published as Provisional, a later draft cannot promote it either.
  const live = await activeConfig(fx.store);
  live.config.keyboard.sets = live.config.keyboard.sets.map((set) => (set.id === "probe-soft" ? { ...set, status: "published", ownerScore: 9.5 } : set));
  await assert.rejects(fx.service.saveDraft({ baseRevision: live.revision, config: live.config }), /accepted this sound as Provisional/);
});

test("a restart marks only jobs whose runner is gone; another live Admin's job is left alone", async (t) => {
  const { fx, jobs, format } = await jobsHarness(t);
  const { job } = await format();
  const record = JSON.parse(await readFile(join(jobs.jobDir(job.jobId), "job.json"), "utf8"));
  assert.deepEqual(record.runner, jobs.runner, "job.json names its runner");
  const now = Date.now();
  const make = async (jobId, status, runner, ageMs = 1000) => {
    await mkdir(jobs.jobDir(jobId), { recursive: true });
    const at = new Date(now - ageMs).toISOString();
    await writeFile(join(jobs.jobDir(jobId), "job.json"), JSON.stringify({ ...record, jobId, status, runner, createdAt: at, startedAt: at, updatedAt: at, finishedAt: null }));
  };
  const OTHER = 424242;
  await make("j20261031-000001-aaaaaa", "running", { pid: OTHER, token: "other" });                       // another live Admin
  await make("j20261031-000002-bbbbbb", "queued", { pid: OTHER, token: "other" });
  await make("j20261031-000003-cccccc", "running", { pid: 515151, token: "dead" });                        // its Admin stopped
  await make("j20261031-000004-dddddd", "running", { pid: process.pid, token: "an-earlier-start" });     // this pid, earlier start
  await make("j20261031-000005-eeeeee", "running", { pid: OTHER, token: "other" }, 2 * 60 * 60 * 1000);  // live pid, but stale
  await make("j20261031-000006-ffffff", "running", undefined);                                             // written before runners
  const restarted = new TypingFeelJobs({ store: fx.store, service: fx.service, mediaStore: fx.mediaStore, tool: jobs.tool, machine: READY, logger: quiet, pidAlive: (pid) => pid === OTHER });
  const { recovered } = await restarted.recover();
  assert.deepEqual(recovered.sort(), ["j20261031-000003-cccccc", "j20261031-000004-dddddd", "j20261031-000005-eeeeee", "j20261031-000006-ffffff"]);
  assert.equal((await restarted.get("j20261031-000001-aaaaaa")).job.status, "running");
  assert.equal((await restarted.get("j20261031-000002-bbbbbb")).job.status, "queued");
});

test("formatted jobs nobody accepted go after 30 days; failed jobs can be discarded at once", async (t) => {
  const { fx, jobs, format, tool } = await jobsHarness(t);
  const { job } = await format();
  tool.env.FAKE_NATURAL_MODE = "crash";
  const failed = await format();
  assert.equal(failed.result.job.status, "failed");
  assert.deepEqual(await jobs.sweep(), [], "a formatted job waits for its owner");
  const record = JSON.parse(await readFile(join(jobs.jobDir(job.jobId), "job.json"), "utf8"));
  const at = new Date(Date.now() - FORMATTED_RETENTION_MS - 60_000).toISOString();
  await writeFile(join(jobs.jobDir(job.jobId), "job.json"), JSON.stringify({ ...record, finishedAt: at, updatedAt: at }));
  const removed = await jobs.sweep();
  assert.deepEqual(removed, [job.jobId]);
  assert.equal(existsSync(jobs.jobDir(job.jobId)), false);
  const discarded = await jobs.discard(failed.job.jobId);
  assert.equal(discarded.status, "discarded");
  assert.equal(existsSync(join(jobs.jobDir(failed.job.jobId), "in")), false, "the take copy goes at once");
  assert.ok(fx);
});

test("stopping the Admin stops the running Format tool with its process group", async (t) => {
  const { jobs, upload } = await jobsHarness(t, { mode: "sleep", timeoutMs: 60_000 });
  const source = await upload();
  const job = await jobs.create({ sourceAssetVersionId: source.assetVersionId });
  for (let i = 0; i < 100 && !jobs.running; i += 1) await new Promise((done) => setTimeout(done, 20));
  assert.ok(jobs.running, "the tool is running");
  const pid = jobs.running.child.pid;
  const started = Date.now();
  // What the service's SIGTERM does (stopFormatToolOnExit), on a stand-in process object.
  const { EventEmitter } = await import("node:events");
  const proc = Object.assign(new EventEmitter(), { pid: 1234, kills: [], kill(target, signal) { this.kills.push([target, signal]); } });
  stopFormatToolOnExit(jobs, proc);
  proc.emit("SIGTERM", "SIGTERM");
  await jobs.whenIdle();
  assert.ok(Date.now() - started < 5000, "the tool stopped at once, not after its 60 s sleep");
  assert.throws(() => process.kill(pid, 0), /ESRCH/, "the tool process is gone");
  assert.deepEqual(proc.kills, [[1234, "SIGTERM"]], "the signal goes on to the service once the tool is stopped");
  assert.equal(proc.listenerCount("SIGTERM"), 0);
  assert.equal((await jobs.get(job.jobId)).job.status, "failed");
  assert.equal(jobs.stopRunning(), false, "nothing left to stop");
});

test("provenance: sizes past the limit never read as the limit; the Media note stays JSON with the tool's hashes", () => {
  assert.equal(megabytesPast(50 * 1024 * 1024 + 1), "50.01");
  assert.equal(megabytesPast(51 * 1024 * 1024), "51");
  assert.equal(megabytesPast(50 * 1024 * 1024 + 150 * 1024), "50.15");
  const tool = { gitSha: "e44906a8e03e", dirty: true, files: { "natural.py": "a".repeat(64), "onsets.py": "b".repeat(64) } };
  const note = JSON.parse(provenanceNote({ recipe: "natural-v1", jobId: "j20261031-000000-abcdef", ownerScore: 9, status: "published", take: "raindrop.wav", sourceSha256: "c".repeat(64), tool }));
  assert.deepEqual(note.toolSha256, { "natural.py": "a".repeat(16), "onsets.py": "b".repeat(16) });
  assert.equal(note.toolDirty, true);
  const long = provenanceNote({ recipe: "natural-v1", jobId: "j20261031-000000-abcdef", ownerScore: 9, status: "published", take: "x".repeat(600), sourceSha256: "c".repeat(64), tool });
  assert.ok(long.length <= 500);
  assert.equal(JSON.parse(long).ownerScore, 9);
});
