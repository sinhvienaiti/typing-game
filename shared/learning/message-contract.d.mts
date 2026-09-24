import type { LearningEvent } from "./core.mjs";
import type {
  LearningQuery,
  LearningQueryResult,
} from "./query.mjs";

export const LEARNING_MESSAGE_NAMESPACE: string;
export const LEARNING_ATTEMPT_MESSAGE: string;
export const LEARNING_QUERY_MESSAGE: string;
export const LEARNING_ACK_MESSAGE: string;
export const LEARNING_QUERY_RESULT_MESSAGE: string;
export const LEARNING_ERROR_MESSAGE: string;

export type ParsedLearningMessage =
  | {
      type: string;
      requestId: string;
      event: LearningEvent;
    }
  | {
      type: string;
      requestId: string;
      query: LearningQuery;
    };

export function isLearningMessage(
  value: unknown,
): value is Record<string, unknown> & { type: string };
export function parseLearningMessage(value: unknown): ParsedLearningMessage;
export function makeLearningAck(requestId: string): {
  type: string;
  requestId: string;
};
export function makeLearningQueryResult(
  requestId: string,
  result: LearningQueryResult,
): {
  type: string;
  requestId: string;
  result: LearningQueryResult;
};
export function makeLearningError(
  requestId: string,
  code: string,
  message: string,
): {
  type: string;
  requestId: string;
  error: { code: string; message: string };
};
