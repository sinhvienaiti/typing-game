import {
  parseEnglishActivityDataset,
  type EnglishActivityDataset,
} from "../../../shared/english-content/activity-dataset.mjs";
import { listEnglishActivities } from "../../../shared/english-content/capabilities.mjs";
import {
  buildPublishedGameEnglishActivityDataset,
  countPublishedEnglishActivityRecords,
} from "../../../shared/english-content/activity-source.mjs";
import { createEnglishRuntimeLoader } from "../../../shared/english-content/runtime-loader.mjs";

export type RichPracticeGameId =
  | "recall-typing"
  | "vocab-shooter"
  | "karaoke-typing"
  | "space-typing";

const PENDING_KEY = "typingGamePendingEnglishActivityV1";
const CAPABILITY_ID: Record<RichPracticeGameId, string> = {
  "recall-typing": "recall",
  "vocab-shooter": "shooter",
  "karaoke-typing": "karaoke",
  "space-typing": "space",
};
const loader = createEnglishRuntimeLoader();

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
): Promise<number> {
  if (!listEnglishActivities(CAPABILITY_ID[gameId]).includes(activity)) {
    return 0;
  }
  return await countPublishedEnglishActivityRecords(loader, activity);
}

export async function queuePublishedEnglishActivity(
  gameId: RichPracticeGameId,
  activity: string,
  limit: number,
): Promise<EnglishActivityDataset> {
  const dataset = await buildPublishedGameEnglishActivityDataset(
    loader,
    gameId,
    CAPABILITY_ID[gameId],
    activity,
    requestId(gameId, activity),
    { limit },
  );
  sessionStorage.setItem(PENDING_KEY, JSON.stringify(dataset));
  return dataset;
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
