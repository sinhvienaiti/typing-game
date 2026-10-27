export type AdminHttpErrorCode =
  | "network-error"
  | "http-error"
  | "invalid-response-content-type"
  | "invalid-json"
  | "empty-response";

export type AdminHttpErrorDetails = {
  code: AdminHttpErrorCode;
  method: string;
  path: string;
  status: number;
  contentType: string;
};

export class AdminHttpError extends Error {
  readonly code: AdminHttpErrorCode;
  readonly method: string;
  readonly path: string;
  readonly status: number;
  readonly contentType: string;

  constructor(message: string, details: AdminHttpErrorDetails) {
    super(message);
    this.name = "AdminHttpError";
    this.code = details.code;
    this.method = details.method;
    this.path = details.path;
    this.status = details.status;
    this.contentType = details.contentType;
  }

  diagnostic(): string {
    const status = this.status > 0 ? ` · HTTP ${this.status}` : "";
    const contentType = this.contentType ? ` · ${this.contentType}` : "";
    return `${this.code} · ${this.method} ${this.path}${status}${contentType}`;
  }
}

export type AdminJsonRequestOptions = {
  token?: string;
  init?: RequestInit;
};

function isJsonContentType(value: string): boolean {
  const mediaType = value.split(";", 1)[0]?.trim().toLowerCase() ?? "";
  return mediaType === "application/json" || mediaType.endsWith("+json");
}

function responseMessage(payload: unknown): string | null {
  if (payload === null || typeof payload !== "object") return null;
  const record = payload as Record<string, unknown>;
  if (typeof record["message"] === "string" && record["message"].trim()) {
    return record["message"].trim();
  }
  if (typeof record["error"] === "string" && record["error"].trim()) {
    return record["error"].trim();
  }
  return null;
}

export async function requestAdminJson<T>(
  path: string,
  options: AdminJsonRequestOptions = {},
): Promise<T> {
  const init = options.init ?? {};
  const method = (init.method ?? "GET").toUpperCase();
  const headers = new Headers(init.headers ?? {});
  if (options.token) headers.set("x-typing-game-admin-token", options.token);
  if (typeof init.body === "string" && !headers.has("content-type")) {
    headers.set("content-type", "application/json");
  }

  let response: Response;
  try {
    response = await fetch(path, {
      ...init,
      cache: "no-store",
      headers,
    });
  } catch {
    throw new AdminHttpError(
      "The local Admin service could not be reached. Check the local runtime and try again.",
      {
        code: "network-error",
        method,
        path,
        status: 0,
        contentType: "",
      },
    );
  }

  const contentType = response.headers.get("content-type") ?? "";
  const body = await response.text();

  if (!isJsonContentType(contentType)) {
    throw new AdminHttpError(
      "The Admin service returned an unexpected response. Restart the local Admin runtime and try again.",
      {
        code: "invalid-response-content-type",
        method,
        path,
        status: response.status,
        contentType: contentType || "unknown content type",
      },
    );
  }

  if (!body.trim()) {
    throw new AdminHttpError("The Admin service returned an empty response. Try the request again.", {
      code: "empty-response",
      method,
      path,
      status: response.status,
      contentType,
    });
  }

  let payload: unknown;
  try {
    payload = JSON.parse(body) as unknown;
  } catch {
    throw new AdminHttpError(
      "The Admin service returned data that could not be read. Restart the local Admin runtime and try again.",
      {
        code: "invalid-json",
        method,
        path,
        status: response.status,
        contentType,
      },
    );
  }

  if (!response.ok) {
    throw new AdminHttpError(
      responseMessage(payload) ?? `The Admin request failed (HTTP ${response.status}).`,
      {
        code: "http-error",
        method,
        path,
        status: response.status,
        contentType,
      },
    );
  }

  return payload as T;
}

export function adminErrorMessage(error: unknown, fallback: string): string {
  if (error instanceof AdminHttpError) return error.message;
  return fallback;
}

export function adminErrorDiagnostic(error: unknown): string | null {
  if (error instanceof AdminHttpError) return error.diagnostic();
  if (error instanceof Error && error.message.trim()) return error.message.trim();
  return null;
}
