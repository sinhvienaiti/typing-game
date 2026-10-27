import { adminErrorDiagnostic, adminErrorMessage } from "./admin-http";

export type AdminFailureStateOptions = {
  title: string;
  fallbackMessage: string;
  error: unknown;
  retryLabel?: string;
  onRetry?: () => void;
};

export type AdminStatusTone = "loading" | "success" | "error" | "info" | "warning";

export function setAdminStatus(
  target: HTMLElement,
  message: string,
  tone: AdminStatusTone = "loading",
): void {
  target.textContent = message;
  target.classList.remove("st-admin-notice--error", "st-admin-notice--success");
  target.removeAttribute("aria-busy");

  if (target.classList.contains("stx-notice")) {
    target.classList.remove("good", "warn", "bad", "info");
    target.classList.add(
      tone === "success"
        ? "good"
        : tone === "error"
          ? "bad"
          : tone === "warning"
            ? "warn"
            : "info",
    );
  }

  if (tone === "loading") {
    target.setAttribute("aria-busy", "true");
    return;
  }
  if (tone === "error") target.classList.add("st-admin-notice--error");
  if (tone === "success") target.classList.add("st-admin-notice--success");
}

export function renderAdminFailureState(
  container: HTMLElement,
  options: AdminFailureStateOptions,
): void {
  container.replaceChildren();

  const card = document.createElement("article");
  card.className = "st-admin-card space-admin-card--wide";
  card.setAttribute("role", "alert");

  const header = document.createElement("div");
  header.className = "st-admin-card__header";
  const headingWrap = document.createElement("div");
  const eyebrow = document.createElement("p");
  eyebrow.className = "st-admin-eyebrow";
  eyebrow.textContent = "Service status";
  const heading = document.createElement("h2");
  heading.textContent = options.title;
  headingWrap.append(eyebrow, heading);
  header.append(headingWrap);

  const message = document.createElement("p");
  message.className = "stx-notice bad";
  message.textContent = adminErrorMessage(options.error, options.fallbackMessage);

  const actions = document.createElement("div");
  actions.className = "st-admin-actions";
  if (options.onRetry) {
    const retry = document.createElement("button");
    retry.type = "button";
    retry.className = "st-admin-btn primary";
    retry.textContent = options.retryLabel ?? "Retry";
    retry.addEventListener("click", options.onRetry);
    actions.append(retry);
  }

  const diagnostic = adminErrorDiagnostic(options.error);
  if (diagnostic) {
    const details = document.createElement("details");
    details.className = "st-admin-details";
    const summary = document.createElement("summary");
    summary.textContent = "Technical details";
    const code = document.createElement("code");
    code.textContent = diagnostic;
    details.append(summary, code);
    card.append(header, message, actions, details);
  } else {
    card.append(header, message, actions);
  }

  container.append(card);
}
