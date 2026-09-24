import { parseLearningEvent } from "./core.mjs";
import { parseLearningQuery } from "./query.mjs";

export const LEARNING_MESSAGE_NAMESPACE = "typing-game:learning:v1";
export const LEARNING_ATTEMPT_MESSAGE =
  `${LEARNING_MESSAGE_NAMESPACE}:attempt`;
export const LEARNING_QUERY_MESSAGE =
  `${LEARNING_MESSAGE_NAMESPACE}:query`;
export const LEARNING_ACK_MESSAGE = `${LEARNING_MESSAGE_NAMESPACE}:ack`;
export const LEARNING_QUERY_RESULT_MESSAGE =
  `${LEARNING_MESSAGE_NAMESPACE}:query-result`;
export const LEARNING_ERROR_MESSAGE =
  `${LEARNING_MESSAGE_NAMESPACE}:error`;

function plainObject(value) {
  return value !== null && typeof value === "object" && !Array.isArray(value);
}

function requestId(value) {
  if (
    typeof value !== "string" ||
    !/^[A-Za-z0-9._:-]{1,100}$/.test(value)
  ) {
    throw new TypeError("requestId is invalid");
  }
  return value;
}

export function isLearningMessage(value) {
  return (
    plainObject(value) &&
    typeof value.type === "string" &&
    value.type.startsWith(`${LEARNING_MESSAGE_NAMESPACE}:`)
  );
}

export function parseLearningMessage(value) {
  if (!plainObject(value)) {
    throw new TypeError("learning message must be an object");
  }

  const id = requestId(value.requestId);
  if (value.type === LEARNING_ATTEMPT_MESSAGE) {
    return {
      type: LEARNING_ATTEMPT_MESSAGE,
      requestId: id,
      event: parseLearningEvent(value.event),
    };
  }
  if (value.type === LEARNING_QUERY_MESSAGE) {
    return {
      type: LEARNING_QUERY_MESSAGE,
      requestId: id,
      query: parseLearningQuery(value.query),
    };
  }
  throw new TypeError("learning message type is not supported");
}

export function makeLearningAck(requestIdValue) {
  return {
    type: LEARNING_ACK_MESSAGE,
    requestId: requestId(requestIdValue),
  };
}

export function makeLearningQueryResult(requestIdValue, result) {
  return {
    type: LEARNING_QUERY_RESULT_MESSAGE,
    requestId: requestId(requestIdValue),
    result,
  };
}

export function makeLearningError(requestIdValue, code, message) {
  return {
    type: LEARNING_ERROR_MESSAGE,
    requestId: requestId(requestIdValue),
    error: {
      code: typeof code === "string" ? code.slice(0, 64) : "invalid-request",
      message:
        typeof message === "string"
          ? message.slice(0, 300)
          : "Learning request failed",
    },
  };
}
