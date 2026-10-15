import { SpaceTypingAdminApi, type AdminActor } from "../../api";

const api = new SpaceTypingAdminApi();

type ActionRule = Readonly<{ permission: string; pattern: RegExp; reason: string }>;
type ButtonGateSnapshot = Readonly<{
  ariaDisabled: string | null;
  title: string;
  permissionDenied: string | undefined;
  permissionGate: string | undefined;
}>;
type GateStatus = "pending" | "ready" | "unavailable";

const ACTION_RULES: readonly ActionRule[] = [
  { permission: "config.draft", pattern: /^(save|create) draft\b/i, reason: "This role cannot create configuration drafts." },
  { permission: "config.publish", pattern: /^publish\b/i, reason: "This role cannot publish configuration." },
  { permission: "config.rollback", pattern: /^roll back\b|^rollback\b/i, reason: "This role cannot roll back published configuration." },
  { permission: "media.upload", pattern: /^upload\b/i, reason: "This role cannot upload media." },
  { permission: "media.delete", pattern: /^(archive|delete|remove)\b/i, reason: "This role cannot perform destructive media actions." },
];

function explicitRule(node: HTMLElement): ActionRule | null {
  const permission = node.dataset["adminPermission"];
  return permission
    ? { permission, pattern: /.*/, reason: `This role does not have ${permission}.` }
    : null;
}

function requiredPermission(button: HTMLButtonElement): ActionRule | null {
  const explicit = explicitRule(button);
  if (explicit !== null) return explicit;
  const label = button.textContent?.trim() ?? "";
  return ACTION_RULES.find((rule) => rule.pattern.test(label)) ?? null;
}

function snapshotButton(button: HTMLButtonElement, snapshots: WeakMap<HTMLButtonElement, ButtonGateSnapshot>): ButtonGateSnapshot {
  const existing = snapshots.get(button);
  if (existing !== undefined) return existing;
  const snapshot = Object.freeze({
    ariaDisabled: button.getAttribute("aria-disabled"),
    title: button.title,
    permissionDenied: button.dataset["permissionDenied"],
    permissionGate: button.dataset["permissionGate"],
  });
  snapshots.set(button, snapshot);
  return snapshot;
}

function restoreAttribute(node: HTMLElement, name: string, value: string | null): void {
  if (value === null) node.removeAttribute(name);
  else node.setAttribute(name, value);
}

function restoreDataset(node: HTMLElement, key: string, value: string | undefined): void {
  if (value === undefined) delete node.dataset[key];
  else node.dataset[key] = value;
}

function markPending(button: HTMLButtonElement, snapshots: WeakMap<HTMLButtonElement, ButtonGateSnapshot>): void {
  snapshotButton(button, snapshots);
  button.setAttribute("aria-disabled", "true");
  button.dataset["permissionGate"] = "pending";
  button.title = "Checking permissions before enabling this action.";
}

function restoreAllowedButton(button: HTMLButtonElement, snapshots: WeakMap<HTMLButtonElement, ButtonGateSnapshot>): void {
  const snapshot = snapshots.get(button);
  if (snapshot === undefined) return;
  restoreAttribute(button, "aria-disabled", snapshot.ariaDisabled);
  restoreDataset(button, "permissionDenied", snapshot.permissionDenied);
  restoreDataset(button, "permissionGate", snapshot.permissionGate);
  button.title = snapshot.title;
}

function denyButton(button: HTMLButtonElement, rule: ActionRule, reason = rule.reason): void {
  button.disabled = true;
  button.setAttribute("aria-disabled", "true");
  button.dataset["permissionDenied"] = rule.permission;
  button.dataset["permissionGate"] = "denied";
  button.title = reason;
}

function primeFailClosed(root: HTMLElement, snapshots: WeakMap<HTMLButtonElement, ButtonGateSnapshot>): void {
  root.dataset["adminPermissionState"] = "pending" satisfies GateStatus;
  for (const button of root.querySelectorAll<HTMLButtonElement>("button")) {
    if (requiredPermission(button) !== null) markPending(button, snapshots);
  }
}

function applyActor(
  root: HTMLElement,
  actor: AdminActor,
  permissions: ReadonlySet<string>,
  snapshots: WeakMap<HTMLButtonElement, ButtonGateSnapshot>,
): void {
  root.dataset["adminRole"] = actor.role;
  root.dataset["adminPermissionState"] = "ready" satisfies GateStatus;
  for (const button of root.querySelectorAll<HTMLButtonElement>("button")) {
    const rule = requiredPermission(button);
    if (rule === null) continue;
    snapshotButton(button, snapshots);
    if (permissions.has(rule.permission)) restoreAllowedButton(button, snapshots);
    else denyButton(button, rule);
  }
  for (const node of root.querySelectorAll<HTMLElement>("[data-admin-permission]")) {
    const rule = explicitRule(node);
    if (rule !== null && !permissions.has(rule.permission)) node.hidden = true;
  }
}

function failUnavailable(root: HTMLElement, snapshots: WeakMap<HTMLButtonElement, ButtonGateSnapshot>): void {
  root.dataset["adminPermissionState"] = "unavailable" satisfies GateStatus;
  for (const button of root.querySelectorAll<HTMLButtonElement>("button")) {
    const rule = requiredPermission(button);
    if (rule === null) continue;
    snapshotButton(button, snapshots);
    denyButton(button, rule, "Permissions could not be verified. This action remains unavailable.");
  }
  for (const node of root.querySelectorAll<HTMLElement>("[data-admin-permission]")) {
    if (explicitRule(node) !== null) node.hidden = true;
  }
}

export function attachRoleAwareActionGates(root: HTMLElement): HTMLElement {
  const generation = Symbol("permission-gate");
  const snapshots = new WeakMap<HTMLButtonElement, ButtonGateSnapshot>();
  let permissions: ReadonlySet<string> | null = null;
  (root as HTMLElement & { __permissionGateGeneration?: symbol }).__permissionGateGeneration = generation;

  primeFailClosed(root, snapshots);

  root.addEventListener("click", (event) => {
    const target = event.target;
    if (!(target instanceof Element)) return;

    const explicitNode = target.closest<HTMLElement>("[data-admin-permission]");
    const explicit = explicitNode !== null && root.contains(explicitNode) ? explicitRule(explicitNode) : null;
    const button = target.closest<HTMLButtonElement>("button");
    const buttonInRoot = button !== null && root.contains(button) ? button : null;
    const rule = explicit ?? (buttonInRoot === null ? null : requiredPermission(buttonInRoot));
    if (rule === null || permissions?.has(rule.permission) === true) return;

    event.preventDefault();
    event.stopPropagation();
    event.stopImmediatePropagation();
    if (buttonInRoot !== null) {
      snapshotButton(buttonInRoot, snapshots);
      denyButton(
        buttonInRoot,
        rule,
        root.dataset["adminPermissionState"] === "pending"
          ? "Checking permissions before enabling this action."
          : rule.reason,
      );
    } else if (explicitNode !== null) {
      explicitNode.setAttribute("aria-disabled", "true");
      explicitNode.dataset["permissionGate"] = root.dataset["adminPermissionState"] ?? "unavailable";
    }
  }, true);

  void api.getActor().then((actor) => {
    const target = root as HTMLElement & { __permissionGateGeneration?: symbol };
    if (target.__permissionGateGeneration !== generation || !root.isConnected) return;
    permissions = new Set(actor.permissions);
    applyActor(root, actor, permissions, snapshots);
  }).catch(() => {
    const target = root as HTMLElement & { __permissionGateGeneration?: symbol };
    if (target.__permissionGateGeneration !== generation || !root.isConnected) return;
    permissions = null;
    failUnavailable(root, snapshots);
  });
  return root;
}
