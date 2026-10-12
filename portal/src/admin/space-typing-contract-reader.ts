import { SpaceTypingAdminApi } from "./api";

const api = new SpaceTypingAdminApi();

function isRecord(value: unknown): value is Record<string, unknown> {
  return value !== null && typeof value === "object" && !Array.isArray(value);
}

export async function readMainAdminContractSection<T>(
  section: string,
  capability: string,
  validateSection?: (value: unknown) => value is T,
): Promise<T> {
  const payload = await api.requestJson<unknown>("/api/admin/space-typing/contract");
  if (!isRecord(payload) || !Array.isArray(payload["capabilities"])) {
    throw new Error("The Space Typing Admin contract is missing its canonical capabilities list.");
  }

  const capabilities = payload["capabilities"];
  if (!capabilities.every((value) => typeof value === "string")) {
    throw new Error("The Space Typing Admin contract contains an invalid capabilities list.");
  }
  if (!capabilities.includes(capability)) {
    throw new Error(`The valid pinned child contract does not expose ${capability}.`);
  }

  const value = payload[section];
  if (value === undefined) {
    throw new Error(`The valid pinned child contract exposes ${capability} but is missing its ${section} section.`);
  }
  if (validateSection && !validateSection(value)) {
    throw new Error(`The ${section} section does not match the canonical ${capability} contract shape.`);
  }
  return value as T;
}

export function isContractRecord(value: unknown): value is Record<string, unknown> {
  return isRecord(value);
}
