import { SpaceTypingAdminApi, type AdminActor } from "../../api";

const api = new SpaceTypingAdminApi();

type ActionRule = Readonly<{ permission: string; pattern: RegExp; reason: string }>;
const ACTION_RULES: readonly ActionRule[] = [
  { permission: "config.draft", pattern: /^(save|create) draft\b/i, reason: "This role cannot create configuration drafts." },
  { permission: "config.publish", pattern: /^publish\b/i, reason: "This role cannot publish configuration." },
  { permission: "config.rollback", pattern: /^roll back\b|^rollback\b/i, reason: "This role cannot roll back published configuration." },
  { permission: "media.upload", pattern: /^upload\b/i, reason: "This role cannot upload media." },
  { permission: "media.delete", pattern: /^(archive|delete|remove)\b/i, reason: "This role cannot perform destructive media actions." },
];

function requiredPermission(button: HTMLButtonElement): ActionRule | null {
  const explicit = button.dataset["adminPermission"];
  if (explicit) return { permission: explicit, pattern: /.*/, reason: `This role does not have ${explicit}.` };
  const label = button.textContent?.trim() ?? "";
  return ACTION_RULES.find((rule) => rule.pattern.test(label)) ?? null;
}

function applyActor(root: HTMLElement, actor: AdminActor): void {
  const permissions = new Set(actor.permissions);
  root.dataset["adminRole"] = actor.role;
  for (const button of root.querySelectorAll<HTMLButtonElement>("button")) {
    const rule = requiredPermission(button);
    if (rule === null || permissions.has(rule.permission)) continue;
    button.disabled = true;
    button.setAttribute("aria-disabled", "true");
    button.dataset["permissionDenied"] = rule.permission;
    button.title = rule.reason;
  }
  for (const node of root.querySelectorAll<HTMLElement>("[data-admin-permission]")) {
    const permission = node.dataset["adminPermission"];
    if (permission && !permissions.has(permission)) node.hidden = true;
  }
}

export function attachRoleAwareActionGates(root: HTMLElement): HTMLElement {
  const generation = Symbol("permission-gate");
  (root as HTMLElement & { __permissionGateGeneration?: symbol }).__permissionGateGeneration = generation;
  void api.getActor().then((actor) => {
    const target = root as HTMLElement & { __permissionGateGeneration?: symbol };
    if (target.__permissionGateGeneration !== generation || !root.isConnected) return;
    applyActor(root, actor);
  }).catch(() => {
    // Server authorization remains authoritative. A failed actor hydration must never grant extra client-side capability.
  });
  return root;
}
