import {
  parseEnglishActivityDataset,
  type EnglishActivityDataset,
} from "../../../shared/english-content/activity-dataset.mjs";
import { listEnglishActivities } from "../../../shared/english-content/capabilities.mjs";
import {
  buildPublishedGameEnglishActivityDataset,
  countPublishedEnglishActivityRecords,
  loadPublishedEnglishActivityRecords,
} from "../../../shared/english-content/activity-source.mjs";
import { hasVerifiedTargetAttribution } from "../../../shared/english-content/game-adapters.mjs";
import {
  evaluateEnglishAnswer,
  type EnglishGradingEvaluation,
  type EnglishGradingMode,
} from "../../../shared/english-content/grading.mjs";
import {
  createEnglishRuntimeLoader,
  type EnglishTopicPack,
  type EnglishTopicPackSummary,
} from "../../../shared/english-content/runtime-loader.mjs";
import { BrowserLearningProfileStore } from "../../../shared/learning/browser-store.mjs";
import { BrowserLearningEvidenceStore } from "../../../shared/learning/browser-evidence-store.mjs";
import {
  defaultEvidenceDimensionForActivity,
  toCompatibleV1LearningEvent,
  type LearningEvidenceDimension,
} from "../../../shared/learning/evidence-v2.mjs";

export type RichPracticeGameId =
  | "recall-typing"
  | "vocab-shooter"
  | "karaoke-typing"
  | "space-typing";

export type GuidedPracticeItem = {
  contentId: string;
  entityId: string;
  activity: string;
  cefr?: string;
  promptText: string;
  secondaryText?: string;
  acceptedAnswers: string[];
  gradingMode: EnglishGradingMode;
  targetConfidence: "verified" | "unverified-rotational";
  learningFocus: LearningEvidenceDimension;
  packId?: string;
  stage?: string;
};

const PENDING_KEY = "typingGamePendingEnglishActivityV1";
const CAPABILITY_ID: Record<RichPracticeGameId, string> = {
  "recall-typing": "recall",
  "vocab-shooter": "shooter",
  "karaoke-typing": "karaoke",
  "space-typing": "space",
};
const loader = createEnglishRuntimeLoader();
const evidenceStore = new BrowserLearningEvidenceStore();
let v1Store: BrowserLearningProfileStore | null = null;

function getV1Store(): BrowserLearningProfileStore {
  v1Store ??= new BrowserLearningProfileStore();
  return v1Store;
}

function requestId(gameId: RichPracticeGameId, activity: string): string {
  return (
    "english-" +
    gameId +
    "-" +
    activity +
    "-" +
    Date.now().toString(36)
  );
}

export async function publishedEnglishActivityCount(
  gameId: RichPracticeGameId,
  activity: string,
  cefr?: string,
): Promise<number> {
  if (!listEnglishActivities(CAPABILITY_ID[gameId]).includes(activity)) {
    return 0;
  }
  return await countPublishedEnglishActivityRecords(
    loader,
    activity,
    cefr !== undefined && cefr !== "" ? { cefr } : undefined,
  );
}

export async function queuePublishedEnglishActivity(
  gameId: RichPracticeGameId,
  activity: string,
  limit: number,
  options: { cefr?: string; seed?: number } = {},
): Promise<EnglishActivityDataset> {
  const dataset = await buildPublishedGameEnglishActivityDataset(
    loader,
    gameId,
    CAPABILITY_ID[gameId],
    activity,
    requestId(gameId, activity),
    {
      limit,
      ...(options.cefr !== undefined && options.cefr !== "" ? { cefr: options.cefr } : {}),
      ...(options.seed !== undefined ? { seed: options.seed } : {}),
    },
  );
  sessionStorage.setItem(PENDING_KEY, JSON.stringify(dataset));
  return dataset;
}

export async function listPublishedTopicPacks(): Promise<EnglishTopicPackSummary[]> {
  const manifest = await loader.loadTopicPacksManifest();
  return manifest?.packs ?? [];
}

function normalizeRecordToGuidedItem(
  record: Record<string, unknown>,
  activity: string,
  meta: {
    packId?: string;
    stage?: string;
    learningFocus?: LearningEvidenceDimension;
    noteVi?: string;
  } = {},
): GuidedPracticeItem | null {
  const id = String(record["id"] ?? record["lexemeId"] ?? "").trim();
  if (id === "") return null;

  const targetConfidence = hasVerifiedTargetAttribution(record)
    ? "verified"
    : "unverified-rotational";
  const learningFocus =
    meta.learningFocus ?? defaultEvidenceDimensionForActivity(activity);
  const cefr =
    typeof record["cefr"] === "string" && record["cefr"].trim() !== ""
      ? record["cefr"].trim()
      : undefined;

  if (Array.isArray(record["acceptedAnswers"]) && typeof record["prompt"] === "string") {
    const answers = record["acceptedAnswers"]
      .filter((v): v is string => typeof v === "string" && v.trim() !== "")
      .map((v) => v.trim());
    if (answers.length === 0) return null;
    const srcIds = Array.isArray(record["sourceSentenceIds"]) ? record["sourceSentenceIds"] : [];
    const entityId = typeof srcIds[0] === "string" ? srcIds[0] : id;
    const gradingMode: EnglishGradingMode =
      record["type"] === "translation" && answers.length === 1
        ? "guided-self-check"
        : "exact-normalized";
    return {
      contentId: id,
      entityId,
      activity,
      ...(cefr === undefined ? {} : { cefr }),
      promptText: record["prompt"].trim(),
      ...(meta.noteVi === undefined ? {} : { secondaryText: meta.noteVi }),
      acceptedAnswers: answers,
      gradingMode,
      targetConfidence,
      learningFocus,
      ...(meta.packId === undefined ? {} : { packId: meta.packId }),
      ...(meta.stage === undefined ? {} : { stage: meta.stage }),
    };
  }

  if (typeof record["incorrect"] === "string" && Array.isArray(record["corrections"])) {
    const answers = record["corrections"]
      .filter((v): v is string => typeof v === "string" && v.trim() !== "");
    if (answers.length === 0) return null;
    return {
      contentId: id,
      entityId: id,
      activity: "error-correction",
      ...(cefr === undefined ? {} : { cefr }),
      promptText: record["incorrect"].trim(),
      secondaryText: typeof record["explanationVi"] === "string" ? record["explanationVi"] : meta.noteVi,
      acceptedAnswers: answers,
      gradingMode: "exact-normalized",
      targetConfidence,
      learningFocus,
      ...(meta.packId === undefined ? {} : { packId: meta.packId }),
      ...(meta.stage === undefined ? {} : { stage: meta.stage }),
    };
  }

  if (typeof record["text"] === "string" && typeof record["meaningVi"] === "string") {
    return {
      contentId: id,
      entityId: id,
      activity,
      ...(cefr === undefined ? {} : { cefr }),
      promptText: record["meaningVi"].trim(),
      ...(meta.noteVi === undefined ? {} : { secondaryText: meta.noteVi }),
      acceptedAnswers: [record["text"].trim()],
      gradingMode: "exact-normalized",
      targetConfidence: "verified",
      learningFocus,
      ...(meta.packId === undefined ? {} : { packId: meta.packId }),
      ...(meta.stage === undefined ? {} : { stage: meta.stage }),
    };
  }

  if (typeof record["headword"] === "string" && typeof record["vi"] === "string") {
    return {
      contentId: id,
      entityId: id,
      activity: "vocabulary",
      ...(cefr === undefined ? {} : { cefr }),
      promptText: record["vi"].trim(),
      ...(typeof record["ipa"] === "string" ? { secondaryText: record["ipa"] } : {}),
      acceptedAnswers: [record["headword"].trim()],
      gradingMode: "exact-normalized",
      targetConfidence: "verified",
      learningFocus,
      ...(meta.packId === undefined ? {} : { packId: meta.packId }),
      ...(meta.stage === undefined ? {} : { stage: meta.stage }),
    };
  }

  if (typeof record["text"] === "string") {
    return {
      contentId: id,
      entityId: id,
      activity: "example-typing",
      ...(cefr === undefined ? {} : { cefr }),
      promptText: record["text"].trim(),
      ...(meta.noteVi === undefined ? {} : { secondaryText: meta.noteVi }),
      acceptedAnswers: [record["text"].trim()],
      gradingMode: "exact-normalized",
      targetConfidence: "verified",
      learningFocus: "typing-fluency",
      ...(meta.packId === undefined ? {} : { packId: meta.packId }),
      ...(meta.stage === undefined ? {} : { stage: meta.stage }),
    };
  }

  return null;
}

export async function loadResolvedTopicPack(packId: string): Promise<{
  pack: EnglishTopicPack;
  items: GuidedPracticeItem[];
} | null> {
  const pack = await loader.loadTopicPack(packId);
  if (pack === null) return null;
  const resolved = await loader.resolvePublishedByIds(
    pack.items.map((item) => item.contentId),
  );
  const items: GuidedPracticeItem[] = [];
  for (const spec of pack.items) {
    const rec = resolved.recordsById.get(spec.contentId) as Record<string, unknown> | undefined;
    if (rec === undefined) continue;
    const item = normalizeRecordToGuidedItem(rec, spec.activity, {
      packId: pack.id,
      stage: spec.stage,
      learningFocus: spec.learningFocus,
      ...(spec.noteVi === undefined ? {} : { noteVi: spec.noteVi }),
    });
    if (item !== null) items.push(item);
  }
  return { pack, items };
}

export async function loadGuidedActivityItems(
  activity: string,
  options: { limit?: number; cefr?: string; seed?: number } = {},
): Promise<GuidedPracticeItem[]> {
  const records = await loadPublishedEnglishActivityRecords(loader, activity, {
    limit: options.limit ?? 10,
    ...(options.cefr !== undefined && options.cefr !== "" ? { cefr: options.cefr } : {}),
    ...(options.seed !== undefined ? { seed: options.seed } : {}),
  });
  const items: GuidedPracticeItem[] = [];
  for (const raw of records) {
    if (raw === null || typeof raw !== "object" || Array.isArray(raw)) continue;
    const item = normalizeRecordToGuidedItem(raw as Record<string, unknown>, activity);
    if (item !== null) items.push(item);
  }
  return items;
}

export function evaluateGuidedPracticeAnswer(
  item: GuidedPracticeItem,
  answer: string,
): EnglishGradingEvaluation {
  return evaluateEnglishAnswer(
    {
      answerText: item.acceptedAnswers[0],
      acceptedAnswers: item.acceptedAnswers,
      gradingMode: item.gradingMode,
    },
    answer,
  );
}

export async function recordGuidedPracticeOutcome(options: {
  item: GuidedPracticeItem;
  evaluation: EnglishGradingEvaluation;
  userAnswer: string;
  responseMs: number;
  overrideOutcome?: "correct" | "incorrect" | "needs-review";
}): Promise<void> {
  const outcome = options.overrideOutcome ?? options.evaluation.outcome;
  const event = {
    version: 2 as const,
    contentId: options.item.contentId,
    entityId: options.item.entityId,
    fallbackSentenceId: options.item.entityId,
    targetConfidence: options.item.targetConfidence,
    dimension: options.item.learningFocus,
    outcome,
    activityType: options.item.activity,
    source: "portal-guided",
    responseMs: Math.max(0, Math.round(options.responseMs)),
    ...(options.evaluation.reasonCode === undefined
      ? {}
      : { reasonCode: options.evaluation.reasonCode }),
    userAnswer: options.userAnswer,
    expectedAnswer: options.evaluation.matchedAnswer ?? options.item.acceptedAnswers[0],
    ...(options.item.packId === undefined ? {} : { packId: options.item.packId }),
    ...(options.item.stage === undefined ? {} : { stage: options.item.stage }),
    occurredAt: new Date().toISOString(),
  };
  await evidenceStore.apply(event);

  const v1 = toCompatibleV1LearningEvent(event);
  if (v1 !== null) {
    await getV1Store().apply(v1);
  }
}

export function readPendingEnglishActivity(): EnglishActivityDataset | null {
  const raw = sessionStorage.getItem(PENDING_KEY);
  if (raw === null) return null;
  try {
    const parsed = parseEnglishActivityDataset(JSON.parse(raw));
    if (parsed === null) {
      throw new TypeError("stored English activity is invalid");
    }
    return parsed;
  } catch {
    sessionStorage.removeItem(PENDING_KEY);
    return null;
  }
}

export function clearPendingEnglishActivity(
  requestIdValue?: string,
  gameId?: string,
): void {
  const pending = readPendingEnglishActivity();
  if (pending === null) return;
  if (
    requestIdValue !== undefined &&
    pending.requestId !== requestIdValue
  ) {
    return;
  }
  if (gameId !== undefined && pending.gameId !== gameId) return;
  sessionStorage.removeItem(PENDING_KEY);
}

export function postPendingEnglishActivity(
  frame: HTMLIFrameElement,
  gameId: string,
  appUrl: string,
): EnglishActivityDataset | null {
  const pending = readPendingEnglishActivity();
  const frameWindow = frame.contentWindow;
  if (
    pending === null ||
    pending.gameId !== gameId ||
    frameWindow === null
  ) {
    return null;
  }
  frameWindow.postMessage(pending, new URL(appUrl).origin);
  return pending;
}
