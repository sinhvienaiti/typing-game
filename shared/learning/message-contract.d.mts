import type { LearningEvent } from "./core.mjs";
import type {
  LearningQuery,
  LearningQueryResult,
  LearningLookup,
  LearningLookupResult,
} from "./query.mjs";

export const LEARNING_MESSAGE_NAMESPACE: string;
export const LEARNING_ATTEMPT_MESSAGE: "typing-game:learning:v1:attempt";
export const LEARNING_QUERY_MESSAGE: "typing-game:learning:v1:query";
export const LEARNING_LOOKUP_MESSAGE: "typing-game:learning:v1:lookup";
export const LOOKUP_MAX_IDS: 200;
export const LEARNING_ACK_MESSAGE: string;
export const LEARNING_QUERY_RESULT_MESSAGE: string;
export const LEARNING_ERROR_MESSAGE: string;

export type ParsedLearningMessage =
  | {
      type: typeof LEARNING_ATTEMPT_MESSAGE;
      requestId: string;
      event: LearningEvent;
    }
  | {
      type: typeof LEARNING_QUERY_MESSAGE;
      requestId: string;
      query: LearningQuery;
    }
  | {
      type: typeof LEARNING_LOOKUP_MESSAGE;
      requestId: string;
      lookup: LearningLookup;
    };

export function isLearningMessage(
  value: unknown,
): value is Record<string, unknown> & { type: string };
export function parseLearningMessage(value: unknown): ParsedLearningMessage;
export function makeLearningAck(requestId: string): {
  type: string;
  requestId: string;
};
export function makeLearningQueryResult<
  Result extends LearningQueryResult | LearningLookupResult,
>(
  requestId: string,
  result: Result,
): {
  type: string;
  requestId: string;
  result: Result;
};
export function makeLearningError(
  requestId: string,
  code: string,
  message?: string,
): {
  type: string;
  requestId: string;
  error: { code: string; message?: string };
};
