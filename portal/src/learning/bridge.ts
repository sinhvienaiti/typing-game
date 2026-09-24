import { BrowserLearningProfileStore } from "../../../shared/learning/browser-store.mjs";
import {
  isLearningMessage,
  makeLearningAck,
  makeLearningError,
  makeLearningQueryResult,
  parseLearningMessage,
} from "../../../shared/learning/message-contract.mjs";
import { queryLearningProfile } from "../../../shared/learning/query.mjs";
import type { LearningEvent } from "../../../shared/learning/core.mjs";

type GameTarget = {
  id: string;
  appUrl: string;
};

type PendingAttempt = {
  requestId: string;
  event: LearningEvent;
  target: Window;
  targetOrigin: string;
};

const MAX_BATCH_SIZE = 32;
const FLUSH_DELAY_MS = 150;
const REQUEST_ID_PATTERN = /^[A-Za-z0-9._:-]{1,100}$/;

function safeRequestId(value: unknown): string | null {
  if (
    value === null ||
    typeof value !== "object" ||
    Array.isArray(value)
  ) {
    return null;
  }

  const requestId = (value as Record<string, unknown>)["requestId"];
  return typeof requestId === "string" &&
    REQUEST_ID_PATTERN.test(requestId)
    ? requestId
    : null;
}

function errorText(error: unknown): string {
  return error instanceof Error ? error.message : "Learning request failed";
}

export class ParentLearningBridge {
  readonly #store: BrowserLearningProfileStore;
  readonly #onApplied: ((event: LearningEvent) => void) | null;
  #pending: PendingAttempt[] = [];
  #flushTimer: number | null = null;
  #flushPromise: Promise<void> | null = null;

  constructor(
    store = new BrowserLearningProfileStore(),
    onApplied: ((event: LearningEvent) => void) | null = null,
  ) {
    this.#store = store;
    this.#onApplied = onApplied;
  }

  handleMessage(
    event: MessageEvent<unknown>,
    currentFrame: HTMLIFrameElement | null,
    currentGame: GameTarget | null,
  ): boolean {
    if (!isLearningMessage(event.data)) return false;

    if (currentFrame === null || currentGame === null) return true;

    const frameWindow = currentFrame.contentWindow;
    const expectedOrigin = new URL(currentGame.appUrl).origin;
    if (
      frameWindow === null ||
      event.source !== frameWindow ||
      event.origin !== expectedOrigin
    ) {
      return true;
    }

    try {
      const message = parseLearningMessage(event.data);
      if ("event" in message) {
        if (message.event.gameId !== currentGame.id) {
          throw new TypeError(
            "learning event gameId does not match the active game",
          );
        }

        this.#queueAttempt({
          requestId: message.requestId,
          event: message.event,
          target: frameWindow,
          targetOrigin: expectedOrigin,
        });
        return true;
      }

      void this.#handleQuery(
        message.requestId,
        message.query,
        frameWindow,
        expectedOrigin,
      );
    } catch (error) {
      const requestId = safeRequestId(event.data);
      if (requestId !== null) {
        this.#post(
          frameWindow,
          expectedOrigin,
          makeLearningError(
            requestId,
            "invalid-request",
            errorText(error),
          ),
        );
      }
    }

    return true;
  }

  #queueAttempt(attempt: PendingAttempt): void {
    this.#pending.push(attempt);

    if (this.#pending.length >= MAX_BATCH_SIZE) {
      void this.flush();
      return;
    }

    if (this.#flushTimer !== null) return;
    this.#flushTimer = window.setTimeout(() => {
      this.#flushTimer = null;
      void this.flush();
    }, FLUSH_DELAY_MS);
  }

  async #handleQuery(
    requestId: string,
    query: unknown,
    target: Window,
    targetOrigin: string,
  ): Promise<void> {
    try {
      await this.flush();
      const profile = await this.#store.load();
      const result = queryLearningProfile(profile, query);
      this.#post(
        target,
        targetOrigin,
        makeLearningQueryResult(requestId, result),
      );
    } catch (error) {
      this.#post(
        target,
        targetOrigin,
        makeLearningError(
          requestId,
          "query-failed",
          errorText(error),
        ),
      );
    }
  }

  async #drain(): Promise<void> {
    while (this.#pending.length > 0) {
      const batch = this.#pending.splice(0, MAX_BATCH_SIZE);
      try {
        await this.#store.applyMany(batch.map((item) => item.event));
        for (const item of batch) {
          this.#onApplied?.(item.event);
          this.#post(
            item.target,
            item.targetOrigin,
            makeLearningAck(item.requestId),
          );
        }
      } catch (error) {
        for (const item of batch) {
          this.#post(
            item.target,
            item.targetOrigin,
            makeLearningError(
              item.requestId,
              "persist-failed",
              errorText(error),
            ),
          );
        }
      }
    }
  }

  flush(): Promise<void> {
    if (this.#flushTimer !== null) {
      window.clearTimeout(this.#flushTimer);
      this.#flushTimer = null;
    }

    if (this.#flushPromise !== null) return this.#flushPromise;

    this.#flushPromise = this.#drain().finally(() => {
      this.#flushPromise = null;
      if (this.#pending.length > 0) void this.flush();
    });
    return this.#flushPromise;
  }

  #post(
    target: Window,
    targetOrigin: string,
    message: unknown,
  ): void {
    target.postMessage(message, targetOrigin);
  }
}
