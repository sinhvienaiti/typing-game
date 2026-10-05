import { SpaceTypingAdminApi } from "./api";
import {
  QA_RUNTIME_ACCEPTED,
  QA_RUNTIME_CAPABILITY,
  createQaLaunchNonce,
  expectedQaOrigin,
  isQaRuntimeReadyMessage,
  qaLaunchUrl,
  type QaEnvironment,
  type QaSessionOverrides,
} from "./qa-session";

const SHIPS = [
  "vanguard", "aegis", "reaper", "zenith", "bastion",
  "oracle", "arsenal", "fortune", "wraith", "volt", "celestial",
];

function field(labelText: string, input: HTMLElement): HTMLElement {
  const wrap = document.createElement("label");
  wrap.className = "st-audio-row";
  const label = document.createElement("div");
  label.className = "st-admin-muted";
  label.textContent = labelText;
  wrap.append(label, input);
  return wrap;
}

export function renderQaSessionPage(input: {
  panel: HTMLElement;
  api: SpaceTypingAdminApi;
  header: HTMLElement;
}): void {
  const { panel, api, header } = input;
  panel.replaceChildren(header);

  const note = document.createElement("div");
  note.className = "st-admin-note";
  note.textContent = "QA runs are disposable: no Campaign progression/economy writes, no real Warp spend, and no production authorization. The bearer is sent only by postMessage after the game announces its runtime session.";

  const grid = document.createElement("div");
  grid.className = "st-audio-grid";
  const stage = document.createElement("input");
  stage.type = "number";
  stage.min = "1";
  stage.max = "1000";
  stage.value = "1";
  const ship = document.createElement("select");
  const normalShip = document.createElement("option");
  normalShip.value = "";
  normalShip.textContent = "Current ship";
  ship.append(normalShip);
  for (const id of SHIPS) {
    const option = document.createElement("option");
    option.value = id;
    option.textContent = id;
    ship.append(option);
  }
  const environment = document.createElement("select");
  for (const value of ["local", "development", "preview", "test"] satisfies QaEnvironment[]) {
    const option = document.createElement("option");
    option.value = value;
    option.textContent = value;
    if (value === "development") option.selected = true;
    environment.append(option);
  }
  const unlimitedWarp = document.createElement("input");
  unlimitedWarp.type = "checkbox";
  unlimitedWarp.checked = true;
  const forceStage = document.createElement("input");
  forceStage.type = "checkbox";
  forceStage.checked = true;
  const ttl = document.createElement("input");
  ttl.type = "number";
  ttl.min = "1";
  ttl.max = "30";
  ttl.value = "10";
  const gameUrl = document.createElement("input");
  gameUrl.type = "url";
  gameUrl.value = "http://127.0.0.1:3004/";

  grid.append(
    field("Stage (1–1000)", stage),
    field("Locked ship preview", ship),
    field("Environment", environment),
    field("Unlimited Warp", unlimitedWarp),
    field("Force selected stage", forceStage),
    field("TTL minutes", ttl),
    field("Space Typing URL", gameUrl),
  );

  const status = document.createElement("div");
  const actions = document.createElement("div");
  actions.className = "st-admin-actions";
  const launch = document.createElement("button");
  launch.type = "button";
  launch.className = "st-admin-action primary";
  launch.textContent = "Launch isolated QA run";
  launch.addEventListener("click", () => {
    const requestedStage = Number.parseInt(stage.value, 10);
    if (!Number.isSafeInteger(requestedStage) || requestedStage < 1 || requestedStage > 1000) {
      status.className = "st-admin-error";
      status.textContent = "Stage must be between 1 and 1000.";
      return;
    }
    const launchNonce = createQaLaunchNonce();
    const baseUrl = gameUrl.value.trim();
    let child: Window | null = null;
    let origin = "";
    try {
      origin = expectedQaOrigin(baseUrl);
      child = window.open(qaLaunchUrl(baseUrl, launchNonce), "_blank", "noopener=false");
    } catch (error) {
      status.className = "st-admin-error";
      status.textContent = error instanceof Error ? error.message : "Invalid game URL.";
      return;
    }
    if (!child) {
      status.className = "st-admin-error";
      status.textContent = "Browser blocked the QA window.";
      return;
    }
    launch.disabled = true;
    status.className = "st-admin-note";
    status.textContent = "Waiting for Space Typing QA runtime…";

    let finished = false;
    const cleanup = () => {
      window.removeEventListener("message", onMessage);
      launch.disabled = false;
    };
    const timer = window.setTimeout(() => {
      if (finished) return;
      finished = true;
      cleanup();
      status.className = "st-admin-error";
      status.textContent = "QA runtime handshake timed out. Confirm Space Typing is running at the configured URL.";
    }, 20_000);
    const onMessage = (event: MessageEvent) => {
      if (finished || event.source !== child || event.origin !== origin || !isQaRuntimeReadyMessage(event.data, launchNonce)) return;
      const overrides: QaSessionOverrides = {
        stageAccess: {
          stage: requestedStage,
          mode: forceStage.checked ? "force" : "allow",
        },
        unlimitedWarp: unlimitedWarp.checked,
        ...(ship.value ? { shipPreview: ship.value } : {}),
      };
      void api.issueQaSession({
        targetSessionId: event.data.runtimeSessionId,
        environment: event.data.environment,
        ttlMs: Math.max(1, Math.min(30, Number.parseInt(ttl.value, 10) || 10)) * 60_000,
        overrides,
      }).then((issued) => {
        child?.postMessage({
          type: QA_RUNTIME_CAPABILITY,
          launchNonce,
          id: issued.id,
          bearer: issued.bearer,
        }, origin);
        status.className = "st-admin-note";
        status.textContent = `Capability ${issued.id.slice(0, 8)}… issued for generation ${issued.generation}; waiting for game acceptance.`;
      }).catch((error: unknown) => {
        finished = true;
        window.clearTimeout(timer);
        cleanup();
        status.className = "st-admin-error";
        status.textContent = error instanceof Error ? error.message : "Could not issue QA capability.";
      });
    };
    window.addEventListener("message", onMessage);
    const onAccepted = (event: MessageEvent) => {
      if (finished || event.source !== child || event.origin !== origin) return;
      const data = event.data as { type?: unknown; launchNonce?: unknown } | null;
      if (!data || data.type !== QA_RUNTIME_ACCEPTED || data.launchNonce !== launchNonce) return;
      finished = true;
      window.clearTimeout(timer);
      cleanup();
      window.removeEventListener("message", onAccepted);
      status.className = "st-admin-success";
      status.textContent = "QA sandbox active. Closing or expiring this run cannot commit progression, economy, ship unlocks, or Warp.";
    };
    window.addEventListener("message", onAccepted);
  });
  actions.append(launch);
  panel.append(note, grid, actions, status);
}
