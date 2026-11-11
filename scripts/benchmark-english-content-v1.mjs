import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { performance } from "node:perf_hooks";
import { createEnglishRuntimeLoader } from "../shared/english-content/runtime-loader.mjs";
import {
  loadPublishedEnglishActivityRecords,
  publishedEnglishActivityAvailability,
} from "../shared/english-content/activity-source.mjs";
import { stableJson } from "./english-content-core.mjs";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");

function createFileStatsFetcher({ allowIndexes = true } = {}) {
  const stats = {
    requests: 0,
    bytesRead: 0,
    manifestRequests: 0,
    shardRequests: 0,
    indexRequests: 0,
  };

  async function fetcher(url) {
    const clean = String(url).replace(/^https:\/\/typing-game\.local\/english-content\//, "");
    const [dataset, ...rest] = clean.split("/");
    if (!allowIndexes && dataset === "indexes") {
      return { ok: false, status: 404, json: async () => ({}) };
    }
    const diskDataset = dataset === "attribution" ? path.join("attribution", "english-content") : dataset;
    const abs = path.join(root, "shared", diskDataset, ...rest);
    try {
      const raw = await fs.readFile(abs, "utf8");
      const bytes = Buffer.byteLength(raw, "utf8");
      stats.requests++;
      stats.bytesRead += bytes;
      if (clean.endsWith("/manifest.json")) stats.manifestRequests++;
      else if (dataset === "indexes") stats.indexRequests++;
      else stats.shardRequests++;
      return { ok: true, status: 200, json: async () => JSON.parse(raw) };
    } catch {
      return { ok: false, status: 404, json: async () => ({}) };
    }
  }

  return {
    fetcher,
    stats,
    reset: () => {
      stats.requests = 0;
      stats.bytesRead = 0;
      stats.manifestRequests = 0;
      stats.shardRequests = 0;
      stats.indexRequests = 0;
    },
  };
}

async function measure(label, mock, fn) {
  mock.reset();
  const t0 = performance.now();
  const summary = await fn();
  return {
    label,
    elapsedMs: Number((performance.now() - t0).toFixed(2)),
    requests: mock.stats.requests,
    shardRequests: mock.stats.shardRequests,
    indexRequests: mock.stats.indexRequests,
    bytesRead: mock.stats.bytesRead,
    mbRead: Number((mock.stats.bytesRead / 1_000_000).toFixed(4)),
    summary,
  };
}

async function runSuite(allowIndexes) {
  const mock = createFileStatsFetcher({ allowIndexes });
  const samplePairs = [
    ["sentences", "sent.tatoeba.13855320"],
    ["sentences", "ex.cloze.e11.50.250"],
    ["sentences", "ex.transformation.e11.30.100"],
    ["sentences", "dlg.mw.e11.05.010"],
    ["sentences", "err.e11.10.050"],
    ["phrases", "col.00002500"],
    ["phrases", "pv.00000500"],
    ["phrases", "idiom.00000500"],
    ["dictionary", "lex.en.000150"],
    ["grammar", "gr.b2.inversion-negative"],
  ];

  const out = {};
  {
    const loader = createEnglishRuntimeLoader({ fetcher: mock.fetcher });
    out.resolve_10_ids_batch_cold = await measure("resolve_10_ids_batch_cold", mock, async () => {
      const res = await loader.resolvePublishedByIds(samplePairs.map(([, id]) => id));
      if (!res.usedIndex) {
        let found = 0;
        for (const [ds, id] of samplePairs) if (await loader.findById(ds, id)) found++;
        return { found, usedIndex: false };
      }
      return { found: res.recordsById.size, usedIndex: true };
    });
  }
  for (const activity of ["cloze", "translation", "example-typing", "collocation"]) {
    const loader = createEnglishRuntimeLoader({ fetcher: mock.fetcher });
    out[`activity_${activity}_20`] = await measure(`activity_${activity}_20`, mock, async () => {
      const rows = await loadPublishedEnglishActivityRecords(loader, activity, { limit: 20, cefr: "B1", seed: 42 });
      return { count: rows.length };
    });
  }
  {
    const loader = createEnglishRuntimeLoader({ fetcher: mock.fetcher });
    out.availability_monkeytype = await measure("availability_monkeytype", mock, async () => {
      return await publishedEnglishActivityAvailability(loader, "monkeytype");
    });
  }
  return out;
}

async function main() {
  const beforeBaseline = await runSuite(false);
  const afterIndexed = await runSuite(true);

  const comparison = {};
  for (const key of Object.keys(afterIndexed)) {
    const b = beforeBaseline[key];
    const a = afterIndexed[key];
    comparison[key] = {
      beforeMs: b.elapsedMs,
      afterMs: a.elapsedMs,
      beforeRequests: b.requests,
      afterRequests: a.requests,
      beforeMB: b.mbRead,
      afterMB: a.mbRead,
      byteReductionX: a.bytesRead > 0 ? Number((b.bytesRead / a.bytesRead).toFixed(1)) : null,
      speedupX: a.elapsedMs > 0 ? Number((b.elapsedMs / a.elapsedMs).toFixed(1)) : null,
    };
  }

  const report = {
    schemaVersion: 1,
    phase: "Phase 0 vs Phase 1 Runtime Comparison",
    generatedAt: new Date().toISOString(),
    beforeBaseline,
    afterIndexed,
    comparison,
  };

  await fs.writeFile(
    path.join(root, "content", "english", "reports", "v2-phase0-runtime-baseline.json"),
    stableJson({ schemaVersion: 1, phase: "Phase 0 Unindexed Baseline", generatedAt: report.generatedAt, scenarios: beforeBaseline }),
    "utf8",
  );
  await fs.writeFile(
    path.join(root, "content", "english", "reports", "v2-phase1-runtime-benchmark.json"),
    stableJson(report),
    "utf8",
  );
  console.log("=== Phase 0 vs Phase 1 Benchmark ===");
  console.table(comparison);
}

main().catch((err) => {
  console.error(err);
  process.exitCode = 1;
});
