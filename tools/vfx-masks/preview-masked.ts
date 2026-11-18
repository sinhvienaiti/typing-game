/** Tickets 273/273b/274: CPU previews using the game's own functions, without ports. */
import { createHash } from "node:crypto";
import { mkdirSync, readFileSync, writeFileSync, statSync } from "node:fs";
import { fileURLToPath, pathToFileURL } from "node:url";
import { dirname, resolve } from "node:path";
import { spawnSync } from "node:child_process";
import type { FlipbookVec3, FlipbookVec4 } from "../../games/immortality-cultivation/src/view/skills/flipbook.ts";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "../..");
const ART = resolve(ROOT, "games/immortality-cultivation/art-src/lab/vfx/fire/impact-k1-r2");
const args = process.argv.slice(2);
let force = false, rampCool = 0, prefix = "";
let gamePath = resolve(ROOT, "games/immortality-cultivation/src/view/skills/flipbook.ts");
for (let i = 0; i < args.length; i++) {
  const flag = args[i];
  if (flag === "--force") { force = true; continue; }
  if (flag !== "--ramp-cool" && flag !== "--out-prefix" && flag !== "--flipbook") {
    throw new Error(`Cờ không hợp lệ: ${flag}`);
  }
  const value = args[++i];
  if (value === undefined || value.startsWith("--")) throw new Error(`Thiếu giá trị ${flag}.`);
  if (flag === "--ramp-cool") {
    rampCool = Number(value);
    if (!value.trim() || !Number.isFinite(rampCool)) throw new Error("--ramp-cool cần số hữu hạn.");
  } else if (flag === "--out-prefix") {
    if (!/^[a-z0-9][a-z0-9_-]*$/i.test(value)) throw new Error("--out-prefix cần tên tệp đơn giản.");
    prefix = value;
  } else gamePath = resolve(ROOT, value);
}
if (!force) throw new Error("Cần --force để ghi kết quả xem trước.");
const OUT = resolve(ROOT, `.local/codex-runs/${prefix ? "274" : "273"}-out`);
const output = (name: string) => resolve(OUT, prefix ? `${prefix}-${name}` : name);
async function main(): Promise<void> {
  const {
    composeFlipbookMasked, blendPremultiplied, flipbookControl, FLIPBOOK_TIMING,
    FLIPBOOK_MASKED_LOOK, srgbToLinear,
  } = await import(pathToFileURL(gamePath).href) as typeof import("../../games/immortality-cultivation/src/view/skills/flipbook.ts");
  const look = { ...FLIPBOOK_MASKED_LOOK, rampCool };
  const NAME = "fire-impact-k1-r2-v1a.a4";
  const CELL = 384, COLS = 6, ROWS = 4, WIDTH = COLS * CELL;
  const TICKS = [0, 1, 3, 6, 9, 12, 18, 24, 30, 36, 42];
  const MAGICK = process.env.ART_MAGICK ?? "/opt/homebrew/bin/magick";
  const FONT = "/System/Library/Fonts/Supplemental/Arial.ttf";
  const md5 = (path: string) => createHash("md5").update(readFileSync(path)).digest("hex");
  const metaPath = resolve(ART, `${NAME}.masks.json`);
  const meta = JSON.parse(readFileSync(metaPath, "utf8"));
  function magick(args: string[], input?: Buffer): Buffer {
    const p = spawnSync(MAGICK, args, { input, maxBuffer: 128 * 1024 * 1024 });
    if (p.error) throw p.error;
    if (p.status !== 0) throw new Error(p.stderr.toString());
    return p.stdout;
  }
  function load(name: string): Buffer {
    const path = resolve(ART, `${NAME}.${name}.png`);
    if (md5(path) !== meta.outputs[name].md5) throw new Error(`MD5 ${name} khác hồ sơ.`);
    const shape = magick([path, "-format", "%w %h %[channels]", "info:"]).toString();
    if (!shape.startsWith(`${WIDTH} ${ROWS * CELL} `) || !shape.includes("a")) {
      throw new Error(`Sai kích thước/kênh ${name}: ${shape}`);
    }
    const raw = magick([path, "-depth", "8", "RGBA:-"]);
    if (raw.length !== WIDTH * ROWS * CELL * 4) throw new Error(`Sai số byte ${name}.`);
    return raw;
  }
  const rgba = load("rgba"), maskA = load("maskA"), maskB = load("maskB");
  mkdirSync(OUT, { recursive: true });
  const linear = Float64Array.from({ length: 256 }, (_, i) => srgbToLinear(i / 255));
  const bg: FlipbookVec3 = [linear[42]!, linear[44]!, linear[48]!];
  const tint: FlipbookVec3 = [1, 1, 1];
  const sheetWidth = CELL * TICKS.length;
  const sheet = Buffer.alloc(sheetWidth * CELL * 3);
  const result: FlipbookVec4 & number[] = [0, 0, 0, 0];
  const blended = [0, 0, 0];
  const measurements: { tick: number; vFrame: number; f0: number; f1: number; w: number;
    ctl: number[]; bright_pixels: number; png_bright_pixels: number; hdr_clipped_pixels: number;
    bright_mean_srgb: number[] | null; surviving_pixels: number; surviving_mean_srgb: number[] | null }[] = [];
  const frames: Buffer[] = [];
  const pixelOffset = (frame: number, x: number, y: number) =>
    (((Math.floor(frame / COLS) * CELL + y) * WIDTH) + (frame % COLS) * CELL + x) * 4;
  function sample(data: Buffer, offset: number, color: boolean): FlipbookVec4 {
    return [color ? linear[data[offset]!]! : data[offset]! / 255,
      color ? linear[data[offset + 1]!]! : data[offset + 1]! / 255,
      color ? linear[data[offset + 2]!]! : data[offset + 2]! / 255, data[offset + 3]! / 255];
  }
  function srgbByte(value: number): number {
    const c = Math.max(0, Math.min(1, value));
    return Math.round(255 * (c <= 0.0031308 ? 12.92 * c : 1.055 * c ** (1 / 2.4) - 0.055));
  }
  for (let tick = 0; tick <= 42; tick++) {
    const vFrame = Math.min(23, Math.max(0, tick * 24 / 60));
    const f0 = Math.floor(vFrame), f1 = Math.min(f0 + 1, 23), w = vFrame - f0;
    const ctl: FlipbookVec4 & number[] = [0, 0, 0, 0];
    flipbookControl(tick / 60, 43 / 60, 0, 0, FLIPBOOK_TIMING["impact-key1"], ctl);
    let bright = 0, encodedBright = 0, hdrPixels = 0, surviving = 0;
    const brightSum = [0, 0, 0], survivingSum = [0, 0, 0];
    const frame = Buffer.alloc(CELL * CELL * 3);
    for (let y = 0; y < CELL; y++) for (let x = 0; x < CELL; x++) {
      const p0 = pixelOffset(f0, x, y), p1 = pixelOffset(f1, x, y);
      composeFlipbookMasked({ t0: sample(rgba, p0, true), t1: sample(rgba, p1, true),
        m0: sample(maskA, p0, false), m1: sample(maskA, p1, false),
        b0: maskB[p0]! / 255, b1: maskB[p1]! / 255, w, ctl, tint, soft: 1 },
      look, result);
      blendPremultiplied(result, bg, blended);
      const clamped = blended.map(c => Math.max(0, Math.min(1, c)));
      const isBright = 0.2126 * clamped[0]! + 0.7152 * clamped[1]! + 0.0722 * clamped[2]! > 0.1;
      if (isBright) bright++;
      if (blended.some(c => c > 1)) hdrPixels++;
      const p = (y * CELL + x) * 3;
      for (let c = 0; c < 3; c++) frame[p + c] = srgbByte(blended[c]!);
      if (result[3] > 0) surviving++;
      for (let c = 0; c < 3; c++) {
        if (isBright) brightSum[c]! += frame[p + c]!;
        if (result[3] > 0) survivingSum[c]! += frame[p + c]!;
      }
      if (0.2126 * linear[frame[p]!]! + 0.7152 * linear[frame[p + 1]!]! +
          0.0722 * linear[frame[p + 2]!]! > 0.1) encodedBright++;
    }
    frames.push(frame);
    const column = TICKS.indexOf(tick);
    if (column >= 0) for (let y = 0; y < CELL; y++) {
      frame.copy(sheet, (y * sheetWidth + column * CELL) * 3, y * CELL * 3, (y + 1) * CELL * 3);
    }
    measurements.push({ tick, vFrame, f0, f1, w, ctl, bright_pixels: bright,
      png_bright_pixels: encodedBright, hdr_clipped_pixels: hdrPixels,
      bright_mean_srgb: bright ? brightSum.map(c => c / bright) : null,
      surviving_pixels: surviving,
      surviving_mean_srgb: surviving ? survivingSum.map(c => c / surviving) : null });
  }
  const bright9 = measurements[9]!.bright_pixels, bright42 = measurements[42]!.bright_pixels;
  const pngBright9 = measurements[9]!.png_bright_pixels, pngBright42 = measurements[42]!.png_bright_pixels;
  if (bright9 <= 0 || pngBright9 <= 0) throw new Error("Tick 9 không có điểm sáng để chuẩn hóa.");
  const annotate = TICKS.flatMap((tick, col) => ["-annotate", `+${col * CELL + 12}+4`, `Tick ${tick}`]);
  const previewPath = output("preview-ticks.png");
  magick(["-size", `${sheetWidth}x${CELL}`, "-depth", "8", "rgb:-", "-colorspace", "sRGB",
    "-background", "#16171a", "-gravity", "northwest", "-splice", "0x28", "-font", FONT,
    "-pointsize", "18", "-fill", "white", ...annotate, "-alpha", "off", previewPath], sheet);

  const areaRows = measurements.map(m => ({ tick: m.tick, bright_pixels: m.bright_pixels,
    relative_to_tick9: m.bright_pixels / bright9, png_bright_pixels: m.png_bright_pixels,
    png_relative_to_tick9: m.png_bright_pixels / pngBright9 }));
  function areaChecks(key: "relative_to_tick9" | "png_relative_to_tick9") {
    const increases = areaRows.slice(10).map(m => m[key] - areaRows[m.tick - 1]![key]);
    return { monotone_with_2pct_tolerance: increases.every(v => v <= 0.02),
      max_increase_relative_to_tick9: Math.max(0, ...increases), tolerance_relative_to_tick9: 0.02,
      tick12_in_050_080: areaRows[12]![key] >= 0.50 && areaRows[12]![key] <= 0.80,
      tick18_in_010_030: areaRows[18]![key] >= 0.10 && areaRows[18]![key] <= 0.30,
      tick42_zero: areaRows[42]![key] === 0 };
  }
  const checks = areaChecks("relative_to_tick9"), pngChecks = areaChecks("png_relative_to_tick9");
  const areaPass = checks.monotone_with_2pct_tolerance && checks.tick12_in_050_080 &&
    checks.tick18_in_010_030 && checks.tick42_zero;
  const pngPass = pngChecks.monotone_with_2pct_tolerance && pngChecks.tick12_in_050_080 &&
    pngChecks.tick18_in_010_030 && pngChecks.tick42_zero;
  const luminance = "linear Rec.709 after HDR clamp, before sRGB encoding; threshold >0.1; labels excluded";
  const areaPath = output("preview-area.json");
  writeFileSync(areaPath, JSON.stringify({ luminance, reference_tick: 9, reference_bright_pixels: bright9,
    ticks: areaRows, checks, png_checks: pngChecks, pass: areaPass && pngPass }, null, 2) + "\n");
  console.log("Tick  bright_px  relative_to_tick9  PNG_relative");
  for (const m of areaRows) console.log(`${String(m.tick).padStart(2)} ${String(m.bright_pixels).padStart(9)} ` +
    `${m.relative_to_tick9.toFixed(6)} ${m.png_relative_to_tick9.toFixed(6)}`);
  for (const tick of [18, 24, 30, 36]) {
    const m = measurements[tick]!;
    console.log(`Tick ${tick}: bright=${m.bright_pixels}; mean sRGB (0–255)=${JSON.stringify(m.bright_mean_srgb)}; ` +
      `surviving=${m.surviving_pixels}; surviving mean sRGB=${JSON.stringify(m.surviving_mean_srgb)}`);
  }

  // Labels are added after measurements, entirely in memory; no raw frame files.
  const labelled = frames.map((frame, tick) => magick(["-size", `${CELL}x${CELL}`, "-depth", "8", "rgb:-",
    "-colorspace", "sRGB", "-gravity", "northwest", "-font", FONT, "-pointsize", "12",
    "-fill", "white", "-annotate", "+8+8", `Tick ${tick}`, "-depth", "8", "rgb:-"], frame));
  const onePass = [...labelled, ...labelled.flatMap(frame => [frame, frame, frame, frame])];
  const expectedFrames = onePass.length * 2; // (43 at 60 fps + 43 held 4x) repeated twice.
  const videoPath = output("preview.mp4");
  const encode = spawnSync("ffmpeg", ["-v", "error", "-y", "-threads", "1", "-f", "rawvideo",
    "-pixel_format", "rgb24", "-video_size", `${CELL}x${CELL}`, "-framerate", "60", "-i", "pipe:0",
    "-vf", "scale=768:768:flags=lanczos", "-an", "-c:v", "libx264", "-preset", "medium", "-crf", "18",
    "-pix_fmt", "yuv420p", "-threads", "2", "-frames:v", String(expectedFrames),
    "-movflags", "+faststart", videoPath], { input: Buffer.concat([...onePass, ...onePass]),
    maxBuffer: 8 * 1024 * 1024 });
  if (encode.error) throw encode.error;
  if (encode.status !== 0) throw new Error(encode.stderr.toString());
  const probe = spawnSync("ffprobe", ["-v", "error", "-select_streams", "v:0", "-count_frames",
    "-show_entries", "stream=codec_name,pix_fmt,width,height,r_frame_rate,nb_frames,nb_read_frames,duration",
    "-of", "json", videoPath], { encoding: "utf8" });
  if (probe.error) throw probe.error;
  if (probe.status !== 0) throw new Error(probe.stderr);
  const stream = JSON.parse(probe.stdout).streams[0];
  const videoBytes = statSync(videoPath).size;
  const videoPass = stream.codec_name === "h264" && stream.pix_fmt === "yuv420p" &&
    stream.width === CELL * 2 && stream.height === CELL * 2 && stream.r_frame_rate === "60/1" &&
    Number(stream.nb_read_frames) === expectedFrames && Number(stream.nb_frames) === expectedFrames && videoBytes < 5_000_000;
  const video = { path: videoPath, md5: md5(videoPath), bytes: videoBytes, stream,
    expected_frames: expectedFrames, timeline: "ticks 0–42 at 60 fps, then 15 fps; pair repeated twice",
    pass: videoPass };
  writeFileSync(output(prefix ? "video-verification.json" : "273b-video-verification.json"), JSON.stringify(video, null, 2) + "\n");
  const stats = { ticks: measurements, background_srgb: "#2a2c30", background_linear: bg,
    luminance,
    sampling: "cell pixel centres at native 384x384; row-major, no vertical flip",
    loopMode: "none", life_seconds: 43 / 60, tint, soft: 1, look,
    timing: FLIPBOOK_TIMING["impact-key1"], bright_tick9: bright9, bright_tick42: bright42,
    ratio42_to_9: bright42 / bright9, check5_pass: bright42 < 0.02 * bright9,
    png_bright_tick9: pngBright9, png_bright_tick42: pngBright42,
    png_ratio42_to_9: pngBright42 / pngBright9,
    game_cpu: { path: gamePath, md5: md5(gamePath) },
    preview_tool: { path: fileURLToPath(import.meta.url), md5: md5(fileURLToPath(import.meta.url)) },
    inputs: Object.fromEntries(["rgba", "maskA", "maskB"].map(n => [n, meta.outputs[n]])),
    preview: { path: previewPath, md5: md5(previewPath), size: [sheetWidth, CELL + 28] },
    area: { path: areaPath, md5: md5(areaPath), checks, png_checks: pngChecks, pass: areaPass && pngPass }, video };
  writeFileSync(output("preview-measurements.json"), JSON.stringify(stats, null, 2) + "\n");
  if (!prefix) {
    meta.preview = stats;
    meta.checks.preview_tick42_less_than_2pct_tick9 = stats.check5_pass;
    meta.checks.preview_area = areaPass && pngPass;
    meta.checks.preview_video = videoPass;
    meta.status = areaPass && pngPass && videoPass ? "candidate_complete_awaiting_owner_review" : "CPU_preview_checks_failed";
    writeFileSync(metaPath, JSON.stringify(meta, null, 2) + "\n");
    writeFileSync(resolve(OUT, "measurements.json"), JSON.stringify(meta, null, 2) + "\n");
  }
  console.log(`Bright pixels: tick9=${bright9}; tick42=${bright42}; ratio=${bright42 / bright9}; PASS`);
  console.log(`PNG bright pixels: tick9=${pngBright9}; tick42=${pngBright42}; ratio=${pngBright42 / pngBright9}; PASS`);
  console.log(`Preview: ${previewPath}`);
  console.log(`Area: ${areaPass && pngPass ? "PASS" : "FAIL"}; video: ${videoPass ? "PASS" : "FAIL"}; ` +
    `${videoBytes} bytes; ${stream.codec_name}/${stream.pix_fmt}; ${stream.nb_read_frames}/${expectedFrames} frames`);
  if (!areaPass || !pngPass || !videoPass) throw new Error("Kiểm 273b không đạt; đã giữ đầu ra và số đo để xem.");
}
void main().catch((error: unknown) => { console.error(error); process.exitCode = 1; });
