// Pure helpers of the Add sound set page (docs/games/TYPING_FEEL_SERVICE.md §3.8):
// loudness-matched A/B, the blind order, the per-key grid and the defaults the
// tool uses for a new set. No DOM and no imports besides types:
// portal/tests/typing-feel-add-sound-set.test.mjs runs it in Node.
import type { TypingFeelFormatReport, TypingFeelReportFile } from "./types";

export type AbTake = "raw" | "natural";

/**
 * Player volumes (0…1) that put both takes at the quieter take's integrated
 * loudness, so the A/B compares sound, not level (§3.8 "Cân độ to giữa các bản").
 * An element can only turn down, so the louder take is lowered.
 */
export function matchedVolumes(rawLufs: number | null | undefined, naturalLufs: number | null | undefined): { raw: number; natural: number; offsetDb: number } {
  if (typeof rawLufs !== "number" || typeof naturalLufs !== "number" || !Number.isFinite(rawLufs) || !Number.isFinite(naturalLufs)) return { raw: 1, natural: 1, offsetDb: 0 };
  const target = Math.min(rawLufs, naturalLufs);
  const volume = (lufs: number) => Math.round(Math.min(1, 10 ** ((target - lufs) / 20)) * 1000) / 1000;
  return { raw: volume(rawLufs), natural: volume(naturalLufs), offsetDb: Math.round(Math.abs(rawLufs - naturalLufs) * 10) / 10 };
}

/** The two takes in a random order for a blind listen (SHARED_SYSTEMS_BAR §2). */
export function blindOrder(random: () => number = Math.random): [AbTake, AbTake] {
  return random() < 0.5 ? ["raw", "natural"] : ["natural", "raw"];
}

export type GridCell = { file: string; set: "key" | "space"; label: string; durationMs: number; leadInMs: number | null; warnings: string[] };

/** Every key and space of a formatted set with its length and what to listen for, keys first. */
export function keyGrid(report: TypingFeelFormatReport | null): GridCell[] {
  const rows: TypingFeelReportFile[] = Array.isArray(report?.files) ? report!.files! : [];
  return rows
    .filter((row) => row.set === "key" || row.set === "space")
    .sort((a, b) => (a.set === b.set ? a.file.localeCompare(b.file) : a.set === "key" ? -1 : 1))
    .map((row) => {
      const warnings: string[] = [];
      const leadInMs = row.leadIn && typeof row.mainStrikeMs === "number" ? Math.round(row.mainStrikeMs) : null;
      if (leadInMs !== null) warnings.push(`Soft tick, then the main strike ${leadInMs} ms later (kept as recorded).`);
      if (row.phaseWarning) warnings.push(`Left and right partly cancel (correlation ${row.stereoCorrelation}); may sound thin on a mono speaker.`);
      const failed = Object.entries(row.gates ?? {}).filter(([, ok]) => !ok).map(([gate]) => gate);
      if (failed.length) warnings.push(`Hard gate failed: ${failed.join(", ")}.`);
      return { file: row.file, set: row.set, label: row.file.replace(/\.ogg$/, ""), durationMs: row.durationMs, leadInMs, warnings };
    });
}

/** What keeps Accept locked (§3.8: under 10 keys or 3 spaces, or a hard gate failed), or null. */
export function acceptLock(report: TypingFeelFormatReport | null): string | null {
  if (!report || report.status !== "formatted") return "Format the take first.";
  if (report.acceptAllowed) return null;
  const counts = report.counts ?? { key: 0, space: 0 };
  const minimum = report.minimum ?? { key: 10, space: 3 };
  if (counts.key < minimum.key || counts.space < minimum.space) return `${counts.key} keys and ${counts.space} spaces; a set needs at least ${minimum.key} keys and ${minimum.space} spaces. Record a take with more taps.`;
  if (report.gates && !report.gates.pass) return `Hard gates failed: ${report.gates.failed.join(", ")}.`;
  return "The report does not allow Accept.";
}

/** The tool's default set id from a file name (natural.py slug, admin/typing-feel/jobs.mjs slugFromName). */
export function slugFromName(text: string): string {
  const value = text.replace(/\.[A-Za-z0-9]{1,8}$/, "").toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "").slice(0, 32).replace(/-+$/, "");
  return value && /^[a-z0-9]/.test(value) && value !== "off" ? value : "new-set";
}

/** The tool's default set name from a file name (natural.py title). */
export function titleFromName(text: string): string {
  const words = text.replace(/\.[A-Za-z0-9]{1,8}$/, "").split(/[^A-Za-z0-9]+/).filter(Boolean);
  return words.map((word) => word[0].toUpperCase() + word.slice(1)).join(" ").slice(0, 60).trim() || "New Set";
}

/** A take the page may upload: WAV by name, not empty, at most the limit (the server checks again). */
export function takeFileProblem(file: { name: string; size: number }, maxBytes: number): string | null {
  if (!/\.wav$/i.test(file.name)) return `${file.name} is not a WAV file. Export the take as WAV (PCM 16-bit, 24-bit or 32-bit float).`;
  if (file.size <= 0) return `${file.name} is empty.`;
  if (file.size > maxBytes) return `${file.name} is ${megabytesPast(file.size)} MB; the limit is ${Math.round(maxBytes / 1024 / 1024)} MB.`;
  return null;
}

/** Megabytes of a file over the limit, rounded up to two decimals, so 50 MiB + 1 byte never reads as 50 MB (natural.py fmt_past). */
export function megabytesPast(bytes: number): string {
  const value = Math.ceil((bytes / 1024 / 1024) * 100 - 1e-6) / 100;
  return value.toFixed(2).replace(/\.?0+$/, "");
}

export function formatMs(range: [number, number] | null | undefined): string {
  return range ? `${range[0]}–${range[1]} ms` : "–";
}

export function formatDb(value: number | null | undefined, unit = "dB"): string {
  return typeof value === "number" && Number.isFinite(value) ? `${value.toFixed(1)} ${unit}` : "–";
}
