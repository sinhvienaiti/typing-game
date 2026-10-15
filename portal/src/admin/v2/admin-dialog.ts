import "./admin-dialog.css";

export type AdminConfirmDialogOptions = {
  title: string;
  message: string;
  eyebrow?: string;
  confirmLabel?: string;
  cancelLabel?: string;
  tone?: "normal" | "danger";
  detail?: HTMLElement;
  returnFocus?: HTMLElement | null;
  onConfirm: () => void | Promise<void>;
};

function element<K extends keyof HTMLElementTagNameMap>(tag: K, className?: string, text?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (className !== undefined) node.className = className;
  if (text !== undefined) node.textContent = text;
  return node;
}

function focusableElements(root: HTMLElement): HTMLElement[] {
  return [...root.querySelectorAll<HTMLElement>(
    'a[href],button:not([disabled]),input:not([disabled]),select:not([disabled]),textarea:not([disabled]),[tabindex]:not([tabindex="-1"])',
  )].filter((node) => !node.hidden && node.getAttribute("aria-hidden") !== "true");
}

let dialogSequence = 0;

export function openAdminConfirmDialog(options: AdminConfirmDialogOptions): () => void {
  const previousActive = options.returnFocus ?? (document.activeElement instanceof HTMLElement ? document.activeElement : null);
  const id = `st-admin-confirm-${++dialogSequence}`;
  const titleId = `${id}-title`;
  const descriptionId = `${id}-description`;
  const backdrop = element("div", "st-admin-v2-dialog-backdrop");
  const dialog = element("section", `st-admin-v2-dialog ${options.tone === "danger" ? "danger" : ""}`.trim());
  dialog.id = id;
  dialog.setAttribute("role", "alertdialog");
  dialog.setAttribute("aria-modal", "true");
  dialog.setAttribute("aria-labelledby", titleId);
  dialog.setAttribute("aria-describedby", descriptionId);

  if (options.eyebrow) dialog.append(element("div", "st-admin-v2-eyebrow", options.eyebrow));
  const title = element("h2", undefined, options.title);
  title.id = titleId;
  const message = element("p", "st-admin-v2-dialog-message", options.message);
  message.id = descriptionId;
  dialog.append(title, message);
  if (options.detail) dialog.append(options.detail);

  const actions = element("div", "st-admin-v2-dialog-actions");
  const cancel = element("button", "st-admin-btn", options.cancelLabel ?? "Cancel");
  cancel.type = "button";
  const confirm = element("button", options.tone === "danger" ? "st-admin-btn st-admin-v2-danger-action" : "st-admin-btn primary", options.confirmLabel ?? "Confirm");
  confirm.type = "button";
  actions.append(cancel, confirm);
  dialog.append(actions);
  backdrop.append(dialog);
  document.body.append(backdrop);

  const controller = new AbortController();
  const { signal } = controller;
  let closed = false;
  let confirming = false;

  const close = (): void => {
    if (closed || confirming) return;
    closed = true;
    controller.abort();
    backdrop.remove();
    if (previousActive?.isConnected) previousActive.focus();
  };

  cancel.addEventListener("click", close, { signal });
  backdrop.addEventListener("pointerdown", (event) => {
    if (event.target === backdrop) close();
  }, { signal });
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      event.preventDefault();
      close();
      return;
    }
    if (event.key !== "Tab") return;
    const focusables = focusableElements(dialog);
    if (focusables.length === 0) return;
    const first = focusables[0];
    const last = focusables[focusables.length - 1];
    if (event.shiftKey && document.activeElement === first) {
      event.preventDefault();
      last.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault();
      first.focus();
    }
  }, { signal });

  confirm.addEventListener("click", async () => {
    if (confirming) return;
    confirming = true;
    confirm.disabled = true;
    cancel.disabled = true;
    const original = confirm.textContent;
    confirm.textContent = "Working…";
    try {
      await options.onConfirm();
      confirming = false;
      closed = true;
      controller.abort();
      backdrop.remove();
      if (previousActive?.isConnected) previousActive.focus();
    } catch (error) {
      confirming = false;
      confirm.disabled = false;
      cancel.disabled = false;
      confirm.textContent = original;
      const existing = dialog.querySelector(".st-admin-v2-dialog-error");
      existing?.remove();
      dialog.insertBefore(element("div", "st-admin-v2-dialog-error", error instanceof Error ? error.message : String(error)), actions);
      confirm.focus();
    }
  }, { signal });

  requestAnimationFrame(() => cancel.focus());
  return close;
}
