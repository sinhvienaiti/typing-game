// Add sound set (/admin/shared/keyboard-sounds/new), docs/games/TYPING_FEEL_SERVICE.md §3.8:
//   1 Upload  the owner's WAV goes to Media V2 (tags typing-feel, keyboard-source); the
//             upload rules run at once and show before Format.
//   2 Format  natural-v1 (the owner's pick of 30/10, fixed parameters) as a server job.
//   3 Listen  raw cut vs natural at 70 WPM, loudness-matched, blind, 20 loops; the 1 s
//             preview; every key and space with its length; lead-ins and warnings.
//   4 Score   the owner's score (9 or more: Published; under 9: Provisional with a
//             reason, never the default) and the set's id, name and family.
//   Add to draft stores the set as one Media V2 bundle and adds its row to the shared
//   working copy; Save draft → Review → Publish to all games does the rest.
// The flow lives in this module, so moving to another Admin page and back keeps it.
import { openAdminConfirmDialog } from "../v2/admin-dialog";
import { createAdminPageHeader, createAdminValidationMessage } from "../v2/admin-components";
import { MediaAdminApi } from "../v2/media-api";
import { jobFileUrl, typingFeelApi, typingFeelErrorProblems } from "./api";
import { acceptStatus, addSet, newSetIdProblem, orderedFamilies } from "./draft-model";
import { acceptLock, blindOrder, formatDb, formatMs, keyGrid, matchedVolumes, slugFromName, takeFileProblem, titleFromName, type AbTake } from "./listen-model";
import { TYPING_FEEL_PERMISSIONS, TYPING_FEEL_ROUTES } from "./routes";
import { typingFeelSession as session } from "./session";
import type { TypingFeelCapabilities, TypingFeelJobListEntry, TypingFeelJobView, TypingFeelUploadCheck } from "./types";
import { bindSession, button, chip, el, focusKey, formatTime, keepFocus, panel, permissionButton, sessionGate } from "./ui";

type Busy = null | "capabilities" | "upload" | "check" | "format" | "accept" | "discard" | "open";
type FlowError = { step: "page" | "upload" | "format" | "listen" | "accept"; message: string; problems?: string[] };
type Form = { setId: string; name: string; family: string; licence: string; score: string; reason: string; note: string; touched: { setId: boolean; name: boolean } };

const SOURCE_TAGS = ["typing-feel", "keyboard-source"];
const LOOP_COUNT = 20;
const POLL_MS = 700;

const flow: {
  capabilities: TypingFeelCapabilities | null;
  source: { assetVersionId: string; fileName: string; byteSize: number } | null;
  check: TypingFeelUploadCheck | null;
  view: TypingFeelJobView | null;
  recent: TypingFeelJobListEntry[] | null;
  busy: Busy;
  error: FlowError | null;
  form: Form;
  blind: { order: [AbTake, AbTake]; revealed: boolean } | null;
  loop: boolean;
} = {
  capabilities: null,
  source: null,
  check: null,
  view: null,
  recent: null,
  busy: null,
  error: null,
  form: emptyForm(),
  blind: null,
  loop: false,
};

function emptyForm(licence = ""): Form {
  return { setId: "", name: "", family: "", licence, score: "", reason: "", note: "", touched: { setId: false, name: false } };
}

/** Object URLs of job files, by job id and file name; revoked when the job leaves the page. */
const fileUrls = new Map<string, Promise<string>>();

function fileUrl(jobId: string, name: string): Promise<string> {
  const key = `${jobId}/${name}`;
  let pending = fileUrls.get(key);
  if (!pending) {
    pending = jobFileUrl(jobId, name);
    pending.catch(() => fileUrls.delete(key));
    fileUrls.set(key, pending);
  }
  return pending;
}

function forgetFiles(): void {
  for (const pending of fileUrls.values()) void pending.then((url) => URL.revokeObjectURL(url)).catch(() => undefined);
  fileUrls.clear();
}

const isActive = (view: TypingFeelJobView | null): boolean => view?.job.status === "queued" || view?.job.status === "running";

const STATUS_TONE: Readonly<Record<string, "info" | "good" | "warn" | "bad">> = { queued: "info", running: "info", succeeded: "good", failed: "bad", accepted: "good", discarded: "warn" };
const STATUS_LABEL: Readonly<Record<string, string>> = { queued: "Queued", running: "Formatting", succeeded: "Formatted", failed: "Failed", accepted: "Accepted", discarded: "Discarded" };

function megabytes(bytes: number): string {
  return `${(bytes / 1024 / 1024).toFixed(bytes < 1024 * 1024 ? 2 : 1)} MB`;
}

function fact(list: HTMLElement, term: string, value: string): void {
  const row = el("div");
  row.append(el("dt", undefined, term), el("dd", undefined, value));
  list.append(row);
}

export function renderTypingFeelAddSoundSet(navigate: (path: string) => void): HTMLElement {
  const page = el("div", "tf-page tf-add");
  const back = button("← Keyboard Sounds", () => {
    player.pause();
    navigate(TYPING_FEEL_ROUTES.keyboardSounds);
  });
  page.append(createAdminPageHeader({
    eyebrow: "All games · Typing Feel · Keyboard Sounds",
    title: "Add sound set",
    subtitle: "Upload one take, format it with the owner's natural recipe, listen, score it, then add it to the draft. Nothing reaches the games until the draft is published.",
    actions: [back],
  }));
  const body = el("div", "tf-body");
  page.append(body);

  const media = new MediaAdminApi();
  const player = new Audio();
  player.preload = "auto";
  let playing: { key: string; loops: number } | null = null;
  let polling = false;
  // The shell attaches the page right after renderPage returns; after that, detached means gone.
  let settled = false;
  setTimeout(() => {
    settled = true;
  }, 0);

  const render = (): void => keepFocus(body, draw);
  const fail = (step: FlowError["step"], error: unknown, message?: string): void => {
    const problems = typingFeelErrorProblems(error);
    flow.error = { step, message: message ?? problems[0] ?? "Something went wrong.", problems: message ? problems : problems.slice(1) };
  };

  // ---------------------------------------------------------------- audio
  const stop = (): void => {
    player.pause();
    playing = null;
    for (const node of page.querySelectorAll<HTMLButtonElement>("[aria-pressed='true'][data-play]")) {
      node.setAttribute("aria-pressed", "false");
      node.textContent = node.dataset["label"] ?? "▶";
    }
  };
  player.addEventListener("ended", () => {
    if (playing && flow.loop && playing.key.startsWith("ab:") && playing.loops + 1 < LOOP_COUNT) {
      playing.loops += 1;
      const counter = page.querySelector<HTMLElement>(`[data-loop-for="${playing.key}"]`);
      if (counter) counter.textContent = `${playing.loops + 1}/${LOOP_COUNT}`;
      player.currentTime = 0;
      void player.play().catch(stop);
      return;
    }
    stop();
  });
  player.addEventListener("error", () => {
    if (playing) flow.error = { step: "listen", message: "That file could not play in this browser." };
    stop();
    render();
  });

  const playButton = (key: string, label: string, name: string, volume: () => number, ariaLabel: string, className = "st-admin-btn tf-play"): HTMLButtonElement => {
    const node = focusKey(button(label, () => {
      const view = flow.view;
      if (!view) return;
      if (playing?.key === key) {
        stop();
        return;
      }
      stop();
      playing = { key, loops: 0 };
      node.setAttribute("aria-pressed", "true");
      node.textContent = "■ Stop";
      const jobId = view.job.jobId;
      void fileUrl(jobId, name).then((url) => {
        if (playing?.key !== key) return;
        player.src = url;
        player.volume = Math.max(0, Math.min(1, volume()));
        player.currentTime = 0;
        return player.play();
      }).catch((error: unknown) => {
        if (playing?.key !== key) return;
        stop();
        fail("listen", error, `${name} could not play.`);
        render();
      });
    }, className), key);
    node.dataset["play"] = key;
    node.dataset["label"] = label;
    node.setAttribute("aria-pressed", String(playing?.key === key));
    node.setAttribute("aria-label", ariaLabel);
    if (playing?.key === key) node.textContent = "■ Stop";
    return node;
  };

  // ---------------------------------------------------------------- server calls
  const loadCapabilities = async (): Promise<void> => {
    flow.busy = flow.busy ?? "capabilities";
    try {
      flow.capabilities = await typingFeelApi.capabilities();
      if (!flow.form.licence) flow.form.licence = flow.capabilities.defaultLicence;
      if (flow.error?.step === "page") flow.error = null;
    } catch (error) {
      fail("page", error, "The Add sound set service could not be read.");
    } finally {
      if (flow.busy === "capabilities") flow.busy = null;
    }
    render();
  };

  const loadRecent = async (): Promise<void> => {
    try {
      flow.recent = (await typingFeelApi.jobs()).jobs;
    } catch {
      flow.recent = flow.recent ?? [];
    }
    render();
  };

  const poll = (): void => {
    if (polling || !isActive(flow.view)) return;
    polling = true;
    const tick = async (): Promise<void> => {
      const view = flow.view;
      if (!view || !isActive(view)) {
        polling = false;
        return;
      }
      if (!page.isConnected && settled) {
        polling = false;
        return;
      }
      try {
        const next = await typingFeelApi.job(view.job.jobId);
        if (flow.view?.job.jobId !== next.job.jobId) {
          polling = false;
          return;
        }
        flow.view = next;
        if (!isActive(next)) {
          polling = false;
          void loadRecent();
          if (next.job.status === "succeeded") flow.blind = null;
        }
      } catch (error) {
        polling = false;
        fail("format", error, "The job status could not be read.");
      }
      render();
      if (polling) setTimeout(() => void tick(), POLL_MS);
    };
    setTimeout(() => void tick(), POLL_MS);
  };

  const prefillFrom = (fileName: string, set?: { id: string; name: string; family: string | null }): void => {
    if (!flow.form.touched.setId) flow.form.setId = set?.id ?? slugFromName(fileName);
    if (!flow.form.touched.name) flow.form.name = set?.name ?? titleFromName(fileName);
    if (set?.family && !flow.form.family) flow.form.family = set.family;
  };

  const runCheck = async (): Promise<void> => {
    if (!flow.source) return;
    flow.busy = "check";
    flow.check = null;
    render();
    try {
      flow.check = await typingFeelApi.checkSource(flow.source.assetVersionId);
      flow.error = null;
    } catch (error) {
      fail("upload", error, "The upload check could not run.");
    } finally {
      flow.busy = null;
      render();
    }
  };

  const upload = async (file: File): Promise<void> => {
    const capabilities = flow.capabilities;
    if (!capabilities || flow.busy) return;
    const problem = takeFileProblem(file, capabilities.upload.maxBytes);
    if (problem) {
      flow.error = { step: "upload", message: problem };
      render();
      return;
    }
    stop();
    forgetFiles();
    flow.view = null;
    flow.check = null;
    flow.blind = null;
    flow.busy = "upload";
    flow.error = null;
    render();
    try {
      const created = await media.createAsset(file, { kind: "audio", title: file.name, tags: SOURCE_TAGS });
      flow.source = { assetVersionId: created.version.assetVersionId, fileName: file.name, byteSize: file.size };
      prefillFrom(file.name);
    } catch (error) {
      flow.busy = null;
      fail("upload", error, `${file.name} could not be uploaded.`);
      render();
      return;
    }
    flow.busy = null;
    await runCheck();
  };

  const format = async (): Promise<void> => {
    const source = flow.source;
    if (!source || flow.busy) return;
    const ready = session.ready;
    // Only an id someone typed (step 4) is checked and sent. The default from the file name is a placeholder:
    // the server steps it to the next free id when it is live, retired or was published before, and Accept
    // sets the final id, so a take named like an existing set still formats.
    const typedId = flow.form.touched.setId ? flow.form.setId : null;
    const idProblem = typedId !== null && ready && session.working ? newSetIdProblem(session.working, typedId, { idPattern: ready.options.idPattern, reserved: ready.options.reservedIds, retired: ready.reservedIds }) : null;
    if (idProblem) {
      flow.error = { step: "format", message: `Set id: ${idProblem}` };
      render();
      return;
    }
    stop();
    forgetFiles();
    flow.busy = "format";
    flow.error = null;
    flow.blind = null;
    render();
    try {
      const started = await typingFeelApi.format({ sourceAssetVersionId: source.assetVersionId, ...(typedId !== null ? { setId: typedId } : {}), name: flow.form.name.trim(), family: flow.form.family || null });
      if (!flow.form.touched.setId) flow.form.setId = started.job.set.id;
      flow.view = { job: started.job, log: "", report: null, elapsedSeconds: 0, timeoutSeconds: flow.capabilities?.timeoutSeconds ?? 180, filesBase: "" };
      void loadRecent();
    } catch (error) {
      fail("format", error, "Format did not start.");
    } finally {
      flow.busy = null;
      render();
      poll();
    }
  };

  const openJob = async (jobId: string): Promise<void> => {
    if (flow.busy) return;
    stop();
    forgetFiles();
    flow.busy = "open";
    render();
    try {
      const view = await typingFeelApi.job(jobId);
      flow.view = view;
      flow.source = { assetVersionId: view.job.source.assetVersionId, fileName: view.job.source.fileName, byteSize: view.job.source.byteSize };
      flow.check = null;
      flow.blind = null;
      flow.error = null;
      flow.form = { ...emptyForm(flow.capabilities?.defaultLicence ?? ""), setId: view.job.set.id, name: view.job.set.name, family: view.job.set.family ?? "" };
    } catch (error) {
      fail("format", error, `Job ${jobId} could not be opened.`);
    } finally {
      flow.busy = null;
      render();
      poll();
    }
  };

  const discard = (trigger: HTMLElement): void => {
    const view = flow.view;
    if (!view) return;
    openAdminConfirmDialog({
      eyebrow: "Add sound set",
      title: "Discard this Format job?",
      message: `${view.job.status === "failed" ? `The failed job ${view.job.jobId} and its copy of the take are deleted now` : `The formatted files of ${view.job.set.name} (${view.job.jobId}) are deleted`}. The uploaded take stays in the Media Library, so you can Format it again.`,
      tone: "danger",
      confirmLabel: "Discard job",
      returnFocus: trigger,
      onConfirm: async () => {
        stop();
        await typingFeelApi.discard(view.job.jobId);
        forgetFiles();
        flow.view = null;
        flow.blind = null;
        flow.error = null;
        void loadRecent();
        render();
      },
    });
  };

  const accept = async (): Promise<void> => {
    const view = flow.view;
    const ready = session.ready;
    const working = session.working;
    if (!view || !ready || !working || flow.busy) return;
    const form = flow.form;
    const score = form.score.trim() === "" ? null : Number(form.score);
    const threshold = flow.capabilities?.publishedOwnerScore ?? ready.options.publishedOwnerScore;
    const status = acceptStatus(score, threshold);
    const problems: string[] = [];
    const idProblem = newSetIdProblem(working, form.setId, { idPattern: ready.options.idPattern, reserved: ready.options.reservedIds, retired: ready.reservedIds });
    if (idProblem) problems.push(`Set id: ${idProblem}`);
    if (!form.name.trim()) problems.push("Give the set an English name.");
    if (!form.family) problems.push("Choose the family the set joins.");
    if (status === null) problems.push("Score the set from 0 to 10 after listening (half points allowed).");
    if (status === "provisional" && !form.reason.trim()) problems.push(`A score under ${threshold} makes the set Provisional; give the reason.`);
    if (problems.length) {
      flow.error = { step: "accept", message: problems[0], problems: problems.slice(1) };
      render();
      return;
    }
    flow.busy = "accept";
    flow.error = null;
    render();
    try {
      const accepted = await typingFeelApi.accept(view.job.jobId, {
        setId: form.setId,
        name: form.name.trim(),
        family: form.family,
        licence: form.licence.trim(),
        ownerScore: score as number,
        ...(form.reason.trim() ? { reason: form.reason.trim() } : {}),
        ...(form.note.trim() ? { note: form.note.trim() } : {}),
      });
      // The live working copy may have moved while the request ran; add to what is there now.
      const result = addSet(session.working ?? working, accepted.row, { idPattern: ready.options.idPattern, reserved: ready.options.reservedIds, retired: ready.reservedIds, threshold });
      if (result.config === null) {
        flow.busy = null;
        flow.error = { step: "accept", message: `The set was stored as ${accepted.version.assetVersionId}, but the draft refused it: ${result.error}` };
        render();
        return;
      }
      stop();
      session.edit(result.config);
      session.setNotice({ tone: "good", message: `${accepted.row.name} (${accepted.row.id}) is in the draft as ${accepted.row.status === "published" ? "Published" : "Provisional"}, owner score ${accepted.row.ownerScore}. Save draft, Review, then Publish to all games.` });
      forgetFiles();
      flow.view = null;
      flow.source = null;
      flow.check = null;
      flow.blind = null;
      flow.busy = null;
      flow.form = emptyForm(flow.capabilities?.defaultLicence ?? "");
      navigate(TYPING_FEEL_ROUTES.keyboardSounds);
    } catch (error) {
      flow.busy = null;
      fail("accept", error, "The set was not accepted.");
      render();
    }
  };

  // ---------------------------------------------------------------- panels
  const errorFor = (step: FlowError["step"]): HTMLElement | null => {
    if (flow.error?.step !== step) return null;
    const box = createAdminValidationMessage({ tone: "bad", message: flow.error.message });
    if (flow.error.problems?.length) {
      const list = el("ul", "tf-problem-list");
      for (const problem of flow.error.problems) list.append(el("li", undefined, problem));
      box.append(list);
    }
    return box;
  };

  const rulesTable = (capabilities: TypingFeelCapabilities): HTMLElement => {
    const rules = capabilities.upload;
    const table = el("table", "tf-rules");
    const head = el("thead");
    const headRow = el("tr");
    for (const label of ["Item", "Required", "If not"]) headRow.append(el("th", undefined, label));
    head.append(headRow);
    const rows: [string, string, string][] = [
      ["File", `WAV: ${rules.sampleFormats.join(", ")}`, "refused"],
      ["Sample rate", rules.sampleRates.map((rate) => `${rate / 1000} kHz`).join(" or "), "refused"],
      ["Channels", "mono or stereo", "refused"],
      ["Length", `${rules.minSeconds}–${rules.maxSeconds} s`, "refused"],
      ["Size", `at most ${Math.round(rules.maxBytes / 1024 / 1024)} MB`, "refused"],
      ["Usable taps", `at least ${rules.minUsableTaps}, within ${rules.usableWithinDb} dB of the loudest, each ${rules.usableGapMs} ms before the next`, "refused"],
      ["Peak near 0 dBFS", `a tap with samples over ${rules.fullScale}`, "warning per tap"],
      ["Background noise", `below ${rules.noiseFloorDbfs} dBFS`, "warning"],
      ["Rhythm and room", `about ${rules.tapsPerSecond} taps a second; dry, close to the microphone, no music`, "note"],
    ];
    const tbody = el("tbody");
    for (const [item, required, otherwise] of rows) {
      const row = el("tr");
      row.append(el("th", undefined, item), el("td", undefined, required), el("td", otherwise === "refused" ? "bad" : otherwise === "note" ? "" : "warn", otherwise));
      tbody.append(row);
    }
    table.append(head, tbody);
    return table;
  };

  const checkResult = (check: TypingFeelUploadCheck): HTMLElement => {
    // A clipped tap passes the upload rules (decision 7) but locks Accept after Format: say so up front.
    const clipped = check.ok && check.rules.some((rule) => rule.id.startsWith("clipped.") && !rule.ok);
    const tone = !check.ok ? "bad" : clipped ? "warn" : "good";
    const root = el("div", `tf-check ${tone}`);
    root.setAttribute("aria-label", "Upload check");
    const head = el("div", "tf-check-head");
    const title = !check.ok ? "The take breaks an upload rule" : clipped ? "The take passes the upload rules, but a clipped tap will lock Accept" : "The take passes the upload rules";
    head.append(el("strong", undefined, title), chip(!check.ok ? "Refused" : clipped ? "Formats, Accept locked" : "Ready to Format", tone));
    root.append(head);
    if (check.message) root.append(el("p", "tf-hint", check.message));
    const lines = el("ul", "tf-check-lines");
    for (const message of check.errors) lines.append(el("li", "bad", message));
    for (const message of check.warnings) lines.append(el("li", "warn", message));
    for (const message of check.notes) lines.append(el("li", undefined, message));
    if (lines.childElementCount) root.append(lines);
    const facts = el("dl", "tf-facts tf-check-facts");
    const source = check.source;
    if (source.tapsFound !== undefined) fact(facts, "Taps", `${source.tapsFound} found · ${source.tapsUsable} usable · ${source.tapsMain ?? "–"} fade out`);
    if (source.peakDbfs !== undefined) fact(facts, "Peak", formatDb(source.peakDbfs, "dBFS"));
    if (source.noiseFloorDbfs !== undefined) fact(facts, "Noise floor", formatDb(source.noiseFloorDbfs, "dBFS"));
    if (source.sampleRate) fact(facts, "Format", `${source.subtype ?? ""} · ${source.sampleRate / 1000} kHz · ${source.channels === 1 ? "mono" : "stereo"} · ${source.durationS ?? "–"} s`);
    if (facts.childElementCount) root.append(facts);
    return root;
  };

  const uploadPanel = (capabilities: TypingFeelCapabilities): HTMLElement => {
    const { root, body: content } = panel("1 · Upload the take", "One WAV take of the owner's keyboard sound. It goes to the Media Library; nothing in the games changes.", "tf-add-step");
    root.dataset["step"] = "upload";
    const details = el("details", "tf-rules-wrap");
    details.open = !flow.source;
    details.append(el("summary", undefined, "Upload rules"), rulesTable(capabilities));
    content.append(details);
    const canUpload = capabilities.permissions.upload && capabilities.permissions.check;
    if (canUpload) {
      const row = el("div", "tf-upload-row");
      const input = focusKey(el("input", "tf-file"), "upload:file");
      input.type = "file";
      input.accept = ".wav,audio/wav,audio/x-wav,audio/wave";
      input.setAttribute("aria-label", flow.source ? "Upload another WAV take" : "Choose a WAV take");
      input.dataset["adminPermission"] = TYPING_FEEL_PERMISSIONS.upload;
      input.disabled = flow.busy !== null;
      input.addEventListener("change", () => {
        const file = input.files?.[0];
        if (file) void upload(file);
      });
      row.append(el("span", "tf-field-label", flow.source ? "Another take" : "WAV take"), input);
      if (flow.busy === "upload") row.append(el("span", "tf-busy", "Uploading…"));
      if (flow.busy === "check") row.append(el("span", "tf-busy", "Checking the take…"));
      content.append(row);
    } else {
      content.append(createAdminValidationMessage({ tone: "info", message: `Uploading a take needs ${capabilities.requiredPermissions.upload} and ${capabilities.requiredPermissions.check}.` }));
    }
    if (flow.source) {
      const facts = el("dl", "tf-facts");
      fact(facts, "Take", `${flow.source.fileName} · ${megabytes(flow.source.byteSize)}`);
      fact(facts, "Media version", flow.source.assetVersionId);
      content.append(facts);
      if (flow.check) content.append(checkResult(flow.check));
      else if (flow.busy !== "check" && canUpload) content.append(focusKey(button("Run the upload check", () => void runCheck(), "st-admin-btn tf-mini"), "upload:check"));
    }
    const error = errorFor("upload");
    if (error) content.append(error);
    return root;
  };

  const formatPanel = (capabilities: TypingFeelCapabilities): HTMLElement => {
    const { root, body: content } = panel("2 · Format", "Natural (owner pick, 30/10). The parameters are fixed.", "tf-add-step");
    root.dataset["step"] = "format";
    const recipe = el("ul", "tf-scope-list tf-recipe");
    for (const line of [
      "Each tap kept from its start to just before the next, at most 450 ms; natural tails and drops stay.",
      "No EQ; the highs stay. Loudness differences shrunk 60%, at most 9 dB.",
      "Variety from the real taps. Spaces: the 8 taps with the longest room after them, 3 semitones lower, +1.5 dB.",
      "OGG Vorbis 48 kHz, the whole set at a -2 dBFS peak; a 1 s preview with a 10 ms fade at the end.",
      "Lead-ins (a soft tick, then the main strike) are reported, never trimmed.",
    ]) recipe.append(el("li", undefined, line));
    content.append(recipe);
    const view = flow.view;
    const canFormat = capabilities.permissions.format;
    const checkRefused = flow.check !== null && !flow.check.ok;
    const formatButton = permissionButton(flow.busy === "format" ? "Starting…" : view && view.job.status !== "discarded" ? "Format again" : "Format", TYPING_FEEL_PERMISSIONS.format, canFormat, () => void format(), "st-admin-btn primary");
    focusKey(formatButton, "format:run");
    formatButton.disabled = !flow.source || flow.busy !== null || isActive(view) || checkRefused || !capabilities.machine.ready;
    formatButton.title = !flow.source ? "Upload a take first." : checkRefused ? "The take breaks an upload rule." : !capabilities.machine.ready ? "The Format tool is not set up on this machine." : "Run natural-v1 on this take.";
    const line = el("div", "tf-format-row");
    line.append(formatButton);
    if (flow.source) {
      const name = flow.form.name.trim() || titleFromName(flow.source.fileName);
      const id = flow.form.touched.setId ? `as id ${flow.form.setId}` : `with the id ${slugFromName(flow.source.fileName)} (or the next free one when a set has it)`;
      line.append(el("span", "tf-hint", `Formats ${flow.source.fileName} as "${name}" ${id}. Step 4 sets the final id and name before Accept.`));
    }
    content.append(line);
    if (!canFormat) content.append(createAdminValidationMessage({ tone: "info", message: `Format needs ${capabilities.requiredPermissions.format}.` }));
    if (view) {
      const status = el("div", "tf-job-status");
      status.setAttribute("role", "status");
      status.setAttribute("aria-live", "polite");
      const label = STATUS_LABEL[view.job.status] ?? view.job.status;
      status.append(chip(label, STATUS_TONE[view.job.status] ?? "info"), el("code", "tf-set-id", view.job.jobId));
      if (view.elapsedSeconds !== null) status.append(el("span", "tf-hint", isActive(view) ? `${view.elapsedSeconds.toFixed(1)} s (stops at ${view.timeoutSeconds} s)` : `took ${view.elapsedSeconds.toFixed(1)} s`));
      content.append(status);
      if (view.job.failure) {
        const box = createAdminValidationMessage({ tone: "bad", title: view.job.failure.kind === "refused" ? "Refused" : "Format failed", message: view.job.failure.message });
        if (view.job.failure.errors?.length) {
          const list = el("ul", "tf-problem-list");
          for (const problem of view.job.failure.errors) list.append(el("li", undefined, problem));
          box.append(list);
        }
        content.append(box);
      }
      if (view.log.trim() && (isActive(view) || view.job.status === "failed")) {
        const log = el("pre", "tf-log", view.log.trim().split("\n").slice(-14).join("\n"));
        log.setAttribute("aria-label", "Format log, last lines");
        content.append(log);
      }
      // A failed job keeps a copy of its take until it is discarded (or for 7 days).
      if (view.job.status === "failed") {
        const drop = permissionButton("Discard job", TYPING_FEEL_PERMISSIONS.discard, capabilities.permissions.discard, () => discard(drop), "st-admin-btn danger tf-mini");
        focusKey(drop, "format:discard");
        drop.disabled = flow.busy !== null;
        drop.title = "Delete this failed job and its copy of the take now. The upload stays in the Media Library.";
        content.append(drop);
      }
    }
    const error = errorFor("format");
    if (error) content.append(error);
    return root;
  };

  const listenPanel = (view: TypingFeelJobView): HTMLElement => {
    const report = view.report;
    const { root, body: content } = panel("3 · Listen", "Compare the raw cut the owner heard on 30/10 with the natural set, at the same loudness. Then the preview and every key.", "tf-add-step");
    root.dataset["step"] = "listen";
    if (!report) {
      content.append(el("p", "tf-hint", "The report is not available."));
      return root;
    }
    const volumes = matchedVolumes(report.ab?.rawCut?.lufsI, report.ab?.natural?.lufsI);
    const takes: Record<AbTake, { label: string; file: string; volume: number; detail: string }> = {
      raw: { label: "Raw cut · 70 WPM", file: "raw-cut.mp3", volume: volumes.raw, detail: "120 ms per tap, levelled, three playback rates per tap (build.py, what the owner heard on 30/10)" },
      natural: { label: "Natural · 70 WPM", file: "natural.mp3", volume: volumes.natural, detail: "natural-v1: this set, as the games will play it" },
    };
    const controls = el("div", "tf-ab-controls");
    const blindToggle = focusKey(button(flow.blind ? "Blind: on" : "Blind: off", () => {
      stop();
      flow.blind = flow.blind ? null : { order: blindOrder(), revealed: false };
      render();
    }, "st-admin-btn tf-mini"), "listen:blind");
    blindToggle.setAttribute("aria-pressed", String(flow.blind !== null));
    blindToggle.title = "Hide the labels and shuffle the order (SHARED_SYSTEMS_BAR §2).";
    const loopToggle = focusKey(button(flow.loop ? `Loop ×${LOOP_COUNT}: on` : `Loop ×${LOOP_COUNT}: off`, () => {
      flow.loop = !flow.loop;
      render();
    }, "st-admin-btn tf-mini"), "listen:loop");
    loopToggle.setAttribute("aria-pressed", String(flow.loop));
    loopToggle.title = "Play a take 20 times in a row: the ear-fatigue test (SHARED_SYSTEMS_BAR §3).";
    controls.append(blindToggle, loopToggle);
    if (flow.blind && !flow.blind.revealed) controls.append(focusKey(button("Reveal", () => {
      if (flow.blind) flow.blind.revealed = true;
      render();
    }, "st-admin-btn tf-mini"), "listen:reveal"));
    controls.append(el("span", "tf-hint", volumes.offsetDb ? `Loudness matched: the louder take plays ${volumes.offsetDb} dB lower.` : "Both takes play at full volume."));
    content.append(controls);

    const ab = el("div", "tf-ab");
    const order: AbTake[] = flow.blind ? flow.blind.order : ["raw", "natural"];
    order.forEach((take, index) => {
      const info = takes[take];
      const hidden = flow.blind !== null && !flow.blind.revealed;
      const card = el("div", "tf-ab-take");
      card.dataset["take"] = hidden ? `take-${index + 1}` : take;
      const name = hidden ? `Take ${index + 1}` : info.label;
      const key = `ab:${hidden ? `take-${index + 1}` : take}`;
      const head = el("div", "tf-ab-head");
      head.append(el("strong", undefined, name), playButton(key, "▶ Play", info.file, () => info.volume, `Play ${name}`));
      card.append(head);
      card.append(el("p", "tf-hint", hidden ? "Labels hidden. Reveal after scoring." : info.detail));
      const loop = el("span", "tf-loop-count", flow.loop ? `1/${LOOP_COUNT}` : "");
      loop.dataset["loopFor"] = key;
      if (flow.loop) card.append(loop);
      if (flow.blind?.revealed) card.append(chip(index === 0 ? "Take 1" : "Take 2", "info"));
      ab.append(card);
    });
    content.append(ab);

    const previewRow = el("div", "tf-preview-row");
    previewRow.append(el("strong", undefined, "Preview · 1 s"), playButton("preview", "▶ Preview", "preview.ogg", () => 1, "Play the 1 second preview"), el("span", "tf-hint", `What a player hears on hover in the sound list${report.preview?.fadeOutMs ? `; the last ${report.preview.fadeOutMs} ms fade out` : ""}.`));
    content.append(previewRow);

    const numbers = el("dl", "tf-facts tf-report-facts");
    fact(numbers, "Set", `${report.counts?.key ?? 0} keys · ${report.counts?.space ?? 0} spaces (at least ${report.minimum?.key ?? 10} and ${report.minimum?.space ?? 3})`);
    if (report.taps) fact(numbers, "Taps", `${report.taps.found} found · ${report.taps.usable} usable · ${report.taps.main} kept`);
    fact(numbers, "Lengths", `keys ${formatMs(report.lengthsMs?.key)} · spaces ${formatMs(report.lengthsMs?.space)}`);
    if (report.loudness) fact(numbers, "LUFS-M max", `${formatDb(report.loudness.min, "")} to ${formatDb(report.loudness.max, "")} (spread ${formatDb(report.loudness.spreadDb)}) · true peak ${formatDb(report.loudness.truePeakMaxDbtp, "dBTP")}`);
    fact(numbers, "Hard gates", report.gates?.pass ? "pass (clip, silence, tail, DC, true peak, 48 kHz, channels)" : `failed: ${report.gates?.failed.join(", ") ?? "unknown"}`);
    fact(numbers, "Lead-ins", report.leadIns?.length ? `${report.leadIns.length}: ${report.leadIns.map((entry) => `${entry.file.replace(/\.ogg$/, "")} ${Math.round(entry.mainStrikeMs)} ms`).join(", ")}` : "none");
    content.append(numbers);

    const grid = el("div", "tf-key-grid");
    grid.setAttribute("aria-label", "Every key and space");
    for (const cell of keyGrid(report)) {
      const item = el("div", `tf-key ${cell.set}${cell.warnings.length ? " has-warning" : ""}`);
      const play = playButton(`file:${cell.file}`, cell.label, cell.file, () => 1, `Play ${cell.label}, ${cell.durationMs} ms${cell.leadInMs !== null ? `, lead-in ${cell.leadInMs} ms` : ""}`, "st-admin-btn tf-key-play");
      item.append(play, el("span", "tf-key-length", `${cell.durationMs} ms`));
      if (cell.leadInMs !== null) item.append(el("span", "tf-key-flag", `lead-in ${cell.leadInMs} ms`));
      if (cell.warnings.length) item.title = cell.warnings.join(" ");
      grid.append(item);
    }
    content.append(el("h3", "tf-sub", "Keys and spaces"), grid);

    if (report.warnings.length) {
      const warnings = el("details", "tf-warnings");
      warnings.open = report.warnings.length <= 8;
      warnings.append(el("summary", undefined, `Warnings (${report.warnings.length}) · reported, never fixed by hand`));
      const list = el("ul", "tf-check-lines");
      for (const warning of report.warnings) list.append(el("li", "warn", warning));
      warnings.append(list);
      content.append(warnings);
    }
    const error = errorFor("listen");
    if (error) content.append(error);
    return root;
  };

  const acceptPanel = (view: TypingFeelJobView, capabilities: TypingFeelCapabilities): HTMLElement => {
    const ready = session.ready!;
    const working = session.working!;
    const report = view.report;
    const { root, body: content } = panel("4 · Score and add to the draft", "Score after listening. 9 or more: Published. Under 9: Provisional with a reason; a Provisional set is never the default.", "tf-add-step");
    root.dataset["step"] = "accept";
    const threshold = capabilities.publishedOwnerScore;
    const form = flow.form;
    const grid = el("div", "tf-accept-grid");
    const field = (label: string, control: HTMLElement, hint?: string): HTMLElement => {
      const wrap = el("label", "tf-field");
      wrap.append(el("span", "tf-field-label", label), control);
      if (hint) wrap.append(el("small", "tf-hint", hint));
      return wrap;
    };
    const statusChip = el("span", "tf-score-status");
    const reasonWrap = el("div");
    const paintStatus = (): void => {
      const score = form.score.trim() === "" ? null : Number(form.score);
      const status = acceptStatus(score, threshold);
      statusChip.replaceChildren(status === null ? chip("Not scored", "info") : status === "published" ? chip("Published", "good") : chip("Provisional", "warn"));
      reasonWrap.hidden = status !== "provisional";
    };

    const score = focusKey(el("input", "st-admin-input tf-score"), "accept:score");
    score.type = "number";
    score.min = "0";
    score.max = "10";
    score.step = "0.5";
    score.inputMode = "decimal";
    score.placeholder = "0–10";
    score.value = form.score;
    score.addEventListener("input", () => {
      form.score = score.value;
      paintStatus();
    });
    const scoreRow = el("div", "tf-score-row");
    scoreRow.append(score, statusChip);
    grid.append(field("Owner score", scoreRow, `Your listening score, never filled in for you. ${threshold} or more publishes the set.`));

    const reason = focusKey(el("textarea", "st-admin-input tf-reason"), "accept:reason");
    reason.rows = 2;
    reason.maxLength = ready.options.noteMax;
    reason.value = form.reason;
    reason.placeholder = "Why it is not a 9 yet, for example: spaces too dull.";
    reason.addEventListener("input", () => {
      form.reason = reason.value;
    });
    reasonWrap.append(field("Reason (Provisional)", reason, "Shown as the set's note in the library and logged."));
    grid.append(reasonWrap);

    const id = focusKey(el("input", "st-admin-input"), "accept:id");
    id.value = form.setId;
    id.maxLength = 32;
    id.spellcheck = false;
    id.autocomplete = "off";
    id.addEventListener("input", () => {
      form.setId = id.value.trim().toLowerCase();
      form.touched.setId = true;
    });
    grid.append(field("Id", id, "Fixed once published (player saves store it). Never a retired id."));

    const name = focusKey(el("input", "st-admin-input"), "accept:name");
    name.value = form.name;
    name.maxLength = ready.options.setNameMax;
    name.addEventListener("input", () => {
      form.name = name.value;
      form.touched.name = true;
    });
    grid.append(field("Name", name, "English, as players read it."));

    const family = focusKey(el("select", "st-admin-select"), "accept:family");
    const none = el("option", undefined, "Choose a family…");
    none.value = "";
    family.append(none);
    for (const entry of orderedFamilies(working)) {
      const option = el("option", undefined, entry.name);
      option.value = entry.id;
      option.selected = entry.id === form.family;
      family.append(option);
    }
    family.value = form.family;
    family.addEventListener("change", () => {
      form.family = family.value;
    });
    grid.append(field("Family", family, "Joins the end of the family; reorder it in Keyboard Sounds."));

    const licence = focusKey(el("input", "st-admin-input"), "accept:licence");
    licence.value = form.licence;
    licence.maxLength = 300;
    licence.addEventListener("input", () => {
      form.licence = licence.value;
    });
    grid.append(field("Licence", licence));

    const note = focusKey(el("input", "st-admin-input"), "accept:note");
    note.value = form.note;
    note.maxLength = ready.options.noteMax;
    note.placeholder = "Optional note shown with the set";
    note.addEventListener("input", () => {
      form.note = note.value;
    });
    grid.append(field("Note", note));
    content.append(grid);
    paintStatus();

    const lock = acceptLock(report);
    if (lock) content.append(createAdminValidationMessage({ tone: "warn", title: "Accept is locked", message: lock }));
    const actions = el("div", "tf-accept-actions");
    const canAccept = capabilities.permissions.accept && ready.permissions.draft;
    const add = permissionButton(flow.busy === "accept" ? "Adding…" : "Add to draft", TYPING_FEEL_PERMISSIONS.accept, canAccept, () => void accept(), "st-admin-btn primary");
    focusKey(add, "accept:add");
    add.disabled = lock !== null || flow.busy !== null;
    add.title = lock ?? "Store the set in Media V2 and add it to the draft. The games change only after Publish.";
    const drop = permissionButton("Discard job", TYPING_FEEL_PERMISSIONS.discard, capabilities.permissions.discard, () => discard(drop), "st-admin-btn danger");
    focusKey(drop, "accept:discard");
    drop.disabled = flow.busy !== null;
    actions.append(add, drop);
    if (!canAccept) actions.append(el("span", "tf-hint", `Adding a set needs ${capabilities.requiredPermissions.accept} and ${ready.requiredPermissions.draft}.`));
    content.append(actions);
    const error = errorFor("accept");
    if (error) content.append(error);
    return root;
  };

  /**
   * An accepted job. Accept cannot run twice, and the set's row lives only in the
   * working copy until Save draft, so a row lost to a reload, a closed tab or a
   * refused add can be put back here from the server's own Accept record.
   */
  const acceptedPanel = (accepted: NonNullable<TypingFeelJobView["job"]["accepted"]>): HTMLElement => {
    const ready = session.ready!;
    const working = session.working!;
    const wrap = el("div", "tf-accepted");
    wrap.dataset["step"] = "accepted";
    const inDraft = working.keyboard.sets.find((set) => set.id === accepted.setId);
    const where = inDraft ? (inDraft.assetVersionId === accepted.assetVersionId ? " It is in the draft." : ` The draft holds another sound under ${accepted.setId}.`) : "";
    wrap.append(createAdminValidationMessage({ tone: "good", title: "Accepted", message: `This job was accepted as ${accepted.name} (${accepted.setId}), ${accepted.status}, owner score ${accepted.ownerScore}; Media version ${accepted.assetVersionId}.${where}` }));
    if (inDraft) return wrap;
    const threshold = flow.capabilities?.publishedOwnerScore ?? ready.options.publishedOwnerScore;
    const options = { idPattern: ready.options.idPattern, reserved: ready.options.reservedIds, retired: ready.reservedIds, threshold };
    const readd = permissionButton("Add to draft", TYPING_FEEL_PERMISSIONS.edit, ready.permissions.draft, () => {
      const current = session.working;
      if (!current) return;
      const result = addSet(current, accepted.row, options);
      if (result.config === null) {
        flow.error = { step: "accept", message: `${accepted.name} could not go back into the draft: ${result.error}` };
        render();
        return;
      }
      stop();
      session.edit(result.config);
      session.setNotice({ tone: "good", message: `${accepted.name} (${accepted.setId}) is back in the draft as ${accepted.status === "published" ? "Published" : "Provisional"}, owner score ${accepted.ownerScore}. Save draft, Review, then Publish to all games.` });
      flow.error = null;
      navigate(TYPING_FEEL_ROUTES.keyboardSounds);
    }, "st-admin-btn primary tf-mini");
    focusKey(readd, "accepted:add");
    readd.disabled = flow.busy !== null;
    readd.title = "Put the accepted set back into the working copy. Nothing is stored again; the games change only after Publish.";
    const actions = el("div", "tf-accept-actions");
    actions.append(readd, el("span", "tf-hint", ready.permissions.draft
      ? "It is not in the draft (the working copy was reloaded or the add was refused). Add it again; Accept is not repeated."
      : `It is not in the draft. Adding it again needs ${ready.requiredPermissions.draft}.`));
    wrap.append(actions);
    const error = errorFor("accept");
    if (error) wrap.append(error);
    return wrap;
  };

  const recentPanel = (): HTMLElement => {
    const { root, body: content } = panel("Recent Format jobs", "Open one to listen again, compare takes or finish it. Failed and discarded jobs are removed after 7 days, formatted jobs nobody accepted or discarded after 30 days.", "tf-add-recent");
    const jobs = flow.recent;
    if (jobs === null) {
      content.append(el("p", "tf-hint", "Loading…"));
      return root;
    }
    if (jobs.length === 0) {
      content.append(el("p", "tf-hint", "No Format jobs yet."));
      return root;
    }
    const list = el("ul", "tf-history");
    for (const job of jobs) {
      const row = el("li", `tf-history-row${flow.view?.job.jobId === job.jobId ? " active" : ""}`);
      const main = el("div", "tf-history-main");
      const title = el("div", "tf-history-title");
      title.append(el("strong", undefined, `${job.set.name} · ${job.set.id}`), chip(STATUS_LABEL[job.status] ?? job.status, STATUS_TONE[job.status] ?? "info"));
      main.append(title, el("span", undefined, `${job.source.fileName}${job.counts ? ` · ${job.counts.key} keys, ${job.counts.space} spaces` : ""}${job.accepted ? ` · accepted as ${job.accepted.setId} (${job.accepted.status})` : ""}${job.failure ? ` · ${job.failure.message}` : ""}`), el("small", undefined, `${job.jobId} · ${formatTime(job.createdAt)}`));
      const open = focusKey(button(flow.view?.job.jobId === job.jobId ? "Open now" : "Open", () => void openJob(job.jobId), "st-admin-btn tf-mini"), `recent:${job.jobId}`);
      open.disabled = flow.busy !== null || flow.view?.job.jobId === job.jobId;
      open.setAttribute("aria-label", `Open job ${job.jobId}, ${job.set.name}`);
      row.append(main, open);
      list.append(row);
    }
    content.append(list);
    return root;
  };

  const draw = (): void => {
    if (settled && !page.isConnected) {
      stop();
      return;
    }
    const gate = sessionGate(session, () => void session.load());
    if (gate) {
      body.replaceChildren(gate);
      return;
    }
    const capabilities = flow.capabilities;
    const content = el("div", "tf-add-layout");
    if (!capabilities) {
      content.append(errorFor("page") ?? el("p", "st-admin-notice", "Loading Add sound set…"));
      body.replaceChildren(content);
      return;
    }
    if (!capabilities.machine.ready) {
      const box = createAdminValidationMessage({ tone: "warn", title: "Format is not set up on this machine", message: `${capabilities.machine.problems.join(" ")} Run this once at the project root, then reload:` });
      const command = el("code", "tf-command", capabilities.machine.setupCommand ?? "bash tools/audio-lab/common/setup.sh");
      command.tabIndex = 0;
      box.append(command);
      content.append(box);
    }
    if (!capabilities.permissions.format) content.append(createAdminValidationMessage({ tone: "info", message: `Your role can listen to Format jobs. Uploading needs ${capabilities.requiredPermissions.upload}; Format, Accept and Discard need ${capabilities.requiredPermissions.format}.` }));
    const steps = el("div", "tf-add-steps");
    steps.append(uploadPanel(capabilities), formatPanel(capabilities));
    const view = flow.view;
    if (view && (view.job.status === "succeeded" || view.job.status === "accepted")) {
      steps.append(listenPanel(view));
      if (view.job.status === "succeeded") steps.append(acceptPanel(view, capabilities));
      else if (view.job.accepted) steps.append(acceptedPanel(view.job.accepted));
    }
    content.append(steps, recentPanel());
    body.replaceChildren(content);
  };

  bindSession(page, session, render);
  render();
  void session.load();
  void loadCapabilities();
  void loadRecent();
  poll();
  return page;
}
