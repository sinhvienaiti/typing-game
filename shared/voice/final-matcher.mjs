import { normalizeSpokenForm, parseSnapshot } from "./protocol.mjs";

/** Match final, timestamped lexical spans against the snapshot at their capture time. */
export function matchFinalWords(
  words,
  snapshots,
  baseSample,
  sampleRate,
  confidenceFloor = 0.85,
) {
  if (
    !Array.isArray(words) ||
    words.length > 128 ||
    !Number.isSafeInteger(baseSample) ||
    baseSample < 0
  )
    return [];
  const matches = [];
  for (let i = 0; i < words.length; i++) {
    const first = words[i];
    if (
      !first ||
      !Number.isFinite(first.start) ||
      !Number.isFinite(first.end) ||
      first.start < 0 ||
      first.end <= first.start
    )
      continue;
    const start = baseSample + Math.floor(first.start * sampleRate);
    const snapshot = [...snapshots]
      .reverse()
      .find((s) => s.publishedAtSample <= start);
    if (!snapshot) continue;
    const valid = parseSnapshot(snapshot);
    let selected = null;
    for (let n = Math.min(8, words.length - i); n >= 1; n--) {
      const span = words.slice(i, i + n);
      if (
        span.some(
          (w, index) =>
            !w ||
            !Number.isFinite(w.conf) ||
            w.conf < confidenceFloor ||
            typeof w.word !== "string" ||
            !Number.isFinite(w.start) ||
            w.start < 0 ||
            !Number.isFinite(w.end) ||
            w.end <= w.start ||
            (index > 0 && w.start < span[index - 1].end),
        )
      )
        continue;
      const form = normalizeSpokenForm(span.map((w) => w.word).join(" "));
      const suppressed = valid.targets
        .filter((t) => !t.eligible)
        .some((t) => t.forms.includes(form));
      if (suppressed) continue;
      const targets = valid.targets.filter(
        (t) =>
          t.eligible && t.eligibleFromSample <= start && t.forms.includes(form),
      );
      if (targets.length !== 1) continue;
      selected = {
        target: targets[0],
        snapshotId: valid.snapshotId,
        form,
        audioStartSample: start,
        audioEndSample: baseSample + Math.ceil(span.at(-1).end * sampleRate),
        length: n,
      };
      break;
    }
    if (selected) {
      matches.push(selected);
      i += selected.length - 1;
    }
  }
  return matches;
}
