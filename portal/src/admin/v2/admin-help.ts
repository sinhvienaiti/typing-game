export type AdminTooltipPlacement = "auto" | "top" | "right" | "bottom" | "left";
export type AdminTooltipInteraction = "hover-focus" | "popover";

export type AdminTooltipOptions = {
  title?: string;
  content: string;
  placement?: AdminTooltipPlacement;
  interaction?: AdminTooltipInteraction;
};

export type AdminHelpDrawerOptions = {
  title: string;
  content: string | HTMLElement;
  eyebrow?: string;
  returnFocus?: HTMLElement | null;
};

export type AdminInfoIconOptions = AdminTooltipOptions & {
  label?: string;
};

export type AdminFieldShellOptions = {
  label: string;
  control: HTMLElement;
  required?: boolean;
  help?: Omit<AdminInfoIconOptions, "label">;
  stateMessage?: string;
  stateTone?: "info" | "good" | "warn" | "bad";
};

let tooltipSequence = 0;
let drawerSequence = 0;

function element<K extends keyof HTMLElementTagNameMap>(tag: K, className?: string, text?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (className !== undefined) node.className = className;
  if (text !== undefined) node.textContent = text;
  return node;
}

function nextId(prefix: string): string {
  const sequence = prefix === "tooltip" ? ++tooltipSequence : ++drawerSequence;
  return `st-admin-${prefix}-${sequence}`;
}

function focusableElements(root: HTMLElement): HTMLElement[] {
  return [...root.querySelectorAll<HTMLElement>(
    'a[href],button:not([disabled]),input:not([disabled]),select:not([disabled]),textarea:not([disabled]),[tabindex]:not([tabindex="-1"])',
  )].filter((node) => !node.hidden && node.getAttribute("aria-hidden") !== "true");
}

function clamp(value: number, min: number, max: number): number {
  return Math.min(Math.max(value, min), max);
}

function placeTooltip(trigger: HTMLElement, tooltip: HTMLElement, preferred: AdminTooltipPlacement): void {
  if (tooltip.hidden) return;

  const margin = 10;
  const viewportPadding = 8;
  const triggerRect = trigger.getBoundingClientRect();
  const tooltipRect = tooltip.getBoundingClientRect();
  const available = {
    top: triggerRect.top,
    right: window.innerWidth - triggerRect.right,
    bottom: window.innerHeight - triggerRect.bottom,
    left: triggerRect.left,
  };

  const fits = {
    top: available.top >= tooltipRect.height + margin,
    right: available.right >= tooltipRect.width + margin,
    bottom: available.bottom >= tooltipRect.height + margin,
    left: available.left >= tooltipRect.width + margin,
  };

  let placement: Exclude<AdminTooltipPlacement, "auto">;
  if (preferred !== "auto" && fits[preferred]) {
    placement = preferred;
  } else if (fits.right) {
    placement = "right";
  } else if (fits.bottom) {
    placement = "bottom";
  } else if (fits.left) {
    placement = "left";
  } else {
    placement = "top";
  }

  let left = triggerRect.left + (triggerRect.width - tooltipRect.width) / 2;
  let top = triggerRect.bottom + margin;
  if (placement === "top") top = triggerRect.top - tooltipRect.height - margin;
  if (placement === "right") {
    left = triggerRect.right + margin;
    top = triggerRect.top + (triggerRect.height - tooltipRect.height) / 2;
  }
  if (placement === "left") {
    left = triggerRect.left - tooltipRect.width - margin;
    top = triggerRect.top + (triggerRect.height - tooltipRect.height) / 2;
  }

  left = clamp(left, viewportPadding, Math.max(viewportPadding, window.innerWidth - tooltipRect.width - viewportPadding));
  top = clamp(top, viewportPadding, Math.max(viewportPadding, window.innerHeight - tooltipRect.height - viewportPadding));
  tooltip.style.left = `${Math.round(left)}px`;
  tooltip.style.top = `${Math.round(top)}px`;
  tooltip.dataset.placement = placement;
}

export function createAdminTooltip(trigger: HTMLElement, options: AdminTooltipOptions): () => void {
  const tooltip = element("div", "st-admin-v2-tooltip");
  tooltip.id = nextId("tooltip");
  tooltip.role = "tooltip";
  tooltip.hidden = true;

  if (options.title) tooltip.append(element("strong", "st-admin-v2-tooltip-title", options.title));
  tooltip.append(element("span", "st-admin-v2-tooltip-body", options.content));
  document.body.append(tooltip);

  const previousDescribedBy = trigger.getAttribute("aria-describedby");
  trigger.setAttribute("aria-describedby", [previousDescribedBy, tooltip.id].filter(Boolean).join(" "));

  const controller = new AbortController();
  const { signal } = controller;
  const placement = options.placement ?? "auto";
  const interaction = options.interaction ?? "popover";
  let pointerInsideTrigger = false;
  let pointerInsideTooltip = false;
  let pinned = false;
  let closeTimer: number | null = null;

  const cancelClose = (): void => {
    if (closeTimer !== null) {
      window.clearTimeout(closeTimer);
      closeTimer = null;
    }
  };

  const show = (persist = false): void => {
    cancelClose();
    if (persist) pinned = true;
    tooltip.hidden = false;
    tooltip.dataset.open = "true";
    requestAnimationFrame(() => placeTooltip(trigger, tooltip, placement));
  };

  const hide = (restoreFocus = false): void => {
    cancelClose();
    pinned = false;
    tooltip.hidden = true;
    delete tooltip.dataset.open;
    if (restoreFocus && trigger.isConnected) trigger.focus();
  };

  const scheduleHide = (): void => {
    cancelClose();
    closeTimer = window.setTimeout(() => {
      if (!pinned && !pointerInsideTrigger && !pointerInsideTooltip && document.activeElement !== trigger) hide();
    }, 70);
  };

  trigger.addEventListener("pointerenter", () => {
    pointerInsideTrigger = true;
    show(false);
  }, { signal });
  trigger.addEventListener("pointerleave", () => {
    pointerInsideTrigger = false;
    scheduleHide();
  }, { signal });
  trigger.addEventListener("focus", () => show(false), { signal });
  trigger.addEventListener("blur", scheduleHide, { signal });
  tooltip.addEventListener("pointerenter", () => {
    pointerInsideTooltip = true;
    cancelClose();
  }, { signal });
  tooltip.addEventListener("pointerleave", () => {
    pointerInsideTooltip = false;
    scheduleHide();
  }, { signal });

  if (interaction === "popover") {
    trigger.addEventListener("click", (event) => {
      event.stopPropagation();
      if (pinned && !tooltip.hidden) hide();
      else show(true);
    }, { signal });
  }

  document.addEventListener("pointerdown", (event) => {
    if (!pinned) return;
    const target = event.target;
    if (target instanceof Node && (trigger.contains(target) || tooltip.contains(target))) return;
    hide();
  }, { signal, capture: true });

  document.addEventListener("keydown", (event) => {
    if (event.key !== "Escape" || tooltip.hidden) return;
    event.preventDefault();
    hide(interaction === "popover");
  }, { signal });

  window.addEventListener("resize", () => placeTooltip(trigger, tooltip, placement), { signal });
  window.addEventListener("scroll", () => placeTooltip(trigger, tooltip, placement), { signal, capture: true });

  return () => {
    cancelClose();
    controller.abort();
    tooltip.remove();
    if (previousDescribedBy) trigger.setAttribute("aria-describedby", previousDescribedBy);
    else trigger.removeAttribute("aria-describedby");
  };
}

export function createAdminInfoIcon(options: AdminInfoIconOptions): { button: HTMLButtonElement; destroy: () => void } {
  const button = element("button", "st-admin-v2-info", "i");
  button.type = "button";
  button.setAttribute("aria-label", options.label ?? `More information${options.title ? ` about ${options.title}` : ""}`);
  button.dataset.adminHelp = "info";
  const destroy = createAdminTooltip(button, {
    title: options.title,
    content: options.content,
    placement: options.placement ?? "auto",
    interaction: options.interaction ?? "popover",
  });
  return { button, destroy };
}

export function openAdminHelpDrawer(options: AdminHelpDrawerOptions): () => void {
  const previousActive = options.returnFocus ?? (document.activeElement instanceof HTMLElement ? document.activeElement : null);
  const backdrop = element("div", "st-admin-v2-drawer-backdrop");
  const drawer = element("aside", "st-admin-v2-help-drawer");
  const drawerId = nextId("drawer");
  const titleId = `${drawerId}-title`;
  drawer.id = drawerId;
  drawer.setAttribute("role", "dialog");
  drawer.setAttribute("aria-modal", "true");
  drawer.setAttribute("aria-labelledby", titleId);
  drawer.tabIndex = -1;

  const head = element("header", "st-admin-v2-help-drawer-head");
  const copy = element("div");
  if (options.eyebrow) copy.append(element("span", "st-admin-v2-help-eyebrow", options.eyebrow));
  const title = element("h2", undefined, options.title);
  title.id = titleId;
  copy.append(title);
  const closeButton = element("button", "st-admin-v2-help-close", "×");
  closeButton.type = "button";
  closeButton.setAttribute("aria-label", "Close help");
  head.append(copy, closeButton);

  const body = element("div", "st-admin-v2-help-drawer-body");
  if (typeof options.content === "string") body.append(element("p", undefined, options.content));
  else body.append(options.content);
  drawer.append(head, body);
  backdrop.append(drawer);
  document.body.append(backdrop);

  const controller = new AbortController();
  const { signal } = controller;
  let closed = false;

  const close = (): void => {
    if (closed) return;
    closed = true;
    controller.abort();
    backdrop.remove();
    if (previousActive?.isConnected) previousActive.focus();
  };

  closeButton.addEventListener("click", close, { signal });
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
    const focusables = focusableElements(drawer);
    if (focusables.length === 0) {
      event.preventDefault();
      drawer.focus();
      return;
    }
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

  requestAnimationFrame(() => closeButton.focus());
  return close;
}

export function createAdminFieldShell(scope: AdminHelpScope, options: AdminFieldShellOptions): HTMLElement {
  const root = element("label", "st-admin-v2-field");
  const labelRow = element("span", "st-admin-v2-field-label");
  labelRow.append(element("span", undefined, options.label));
  if (options.required) {
    const required = element("span", "st-admin-v2-required", "Required");
    required.setAttribute("aria-hidden", "true");
    labelRow.append(required);
  }
  if (options.help) labelRow.append(scope.infoIcon({ ...options.help, label: `Help for ${options.label}` }));
  root.append(labelRow, options.control);
  if (options.stateMessage) {
    root.append(element("span", `st-admin-v2-field-state ${options.stateTone ?? "info"}`, options.stateMessage));
  }
  return root;
}

export class AdminHelpScope {
  private readonly disposers = new Set<() => void>();
  private drawerClose: (() => void) | null = null;

  tooltip(trigger: HTMLElement, options: AdminTooltipOptions): HTMLElement {
    const dispose = createAdminTooltip(trigger, options);
    this.disposers.add(dispose);
    return trigger;
  }

  infoIcon(options: AdminInfoIconOptions): HTMLButtonElement {
    const { button, destroy } = createAdminInfoIcon(options);
    this.disposers.add(destroy);
    return button;
  }

  openDrawer(options: AdminHelpDrawerOptions): void {
    this.drawerClose?.();
    this.drawerClose = openAdminHelpDrawer(options);
  }

  destroy(): void {
    this.drawerClose?.();
    this.drawerClose = null;
    for (const dispose of this.disposers) dispose();
    this.disposers.clear();
    document.querySelectorAll(".st-admin-v2-tooltip,.st-admin-v2-drawer-backdrop").forEach((node) => node.remove());
  }
}
