import { SpaceTypingAdminApi } from "./api";
import { renderAdminFailureState, setAdminStatus } from "./space-typing-admin-state";

const api = new SpaceTypingAdminApi();

type ChallengeContract = {
  available: true;
  owner: string;
  challengeKind: "daily" | "weekly";
  cadence: "utc-day" | "utc-iso-week";
  seedPolicy: string;
  identityFields: string[];
  adaptivePolicy: "frozen";
  personalBest: true;
  personalGhost: true;
  profileStorageKey: string;
  remoteScheduler: false;
  remoteLeaderboard: false;
  writeCapability: false;
};

type DailyWeeklyContract = {
  contractRevision: string;
  schemaVersion: number;
  capability: "daily-weekly.read";
  liveOps: {
    mode: "runtime-readonly";
    runtimeSources: string[];
    daily: ChallengeContract & {
      challengeKind: "daily";
      cadence: "utc-day";
      dayKeyFormat: "YYYY-MM-DD";
      adminMode: "read-only";
    };
    weekly: ChallengeContract & {
      challengeKind: "weekly";
      cadence: "utc-iso-week";
      weekKeyFormat: "YYYY-Www";
      weekKeyOwner: string;
      seedOwner: string;
      adminMode: "read-only";
      readableState: string[];
      schedulerControlCapability: false;
      rewardAuthoringCapability: false;
      seedOverrideCapability: false;
    };
    adminWriteCapability: false;
    scheduleAuthoringCapability: false;
    rewardAuthoringCapability: false;
    publishCapability: false;
    applyBoundary: "none";
    unsupportedAdminOperations: string[];
  };
};

function escapeHtml(value: unknown): string {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}
function stringArray(value: unknown): value is string[] {
  return Array.isArray(value) && value.every((entry) => typeof entry === "string");
}
function record(value: unknown): value is Record<string, unknown> {
  return value !== null && typeof value === "object" && !Array.isArray(value);
}

async function fetchContract(): Promise<DailyWeeklyContract> {
  const payload = await api.requestJson<unknown>("/api/admin/space-typing/daily-weekly/contract");
  if (!record(payload) || payload["capability"] !== "daily-weekly.read" || !record(payload["liveOps"])) {
    throw new Error("Daily / Weekly contract does not match the canonical read-only runtime boundary.");
  }
  const liveOps = payload["liveOps"];
  if (liveOps["mode"] !== "runtime-readonly" || !record(liveOps["daily"]) || !record(liveOps["weekly"])) {
    throw new Error("Daily / Weekly contract is missing canonical runtime ownership metadata.");
  }
  const daily = liveOps["daily"];
  const weekly = liveOps["weekly"];
  if (
    daily["available"] !== true ||
    daily["challengeKind"] !== "daily" ||
    daily["writeCapability"] !== false ||
    !stringArray(daily["identityFields"]) ||
    weekly["available"] !== true ||
    weekly["challengeKind"] !== "weekly" ||
    weekly["writeCapability"] !== false ||
    !stringArray(weekly["identityFields"]) ||
    !stringArray(weekly["readableState"]) ||
    liveOps["adminWriteCapability"] !== false ||
    !stringArray(liveOps["runtimeSources"]) ||
    !stringArray(liveOps["unsupportedAdminOperations"])
  ) {
    throw new Error("Daily / Weekly contract contains an invalid runtime capability shape.");
  }
  return payload as unknown as DailyWeeklyContract;
}

function chipList(values: string[]): string {
  return `<div class="st-admin-chip-list">${values.map((value) => `<span class="st-admin-chip">${escapeHtml(value)}</span>`).join("")}</div>`;
}

function challengeCard(title: string, challenge: ChallengeContract, identityLabel: string, identityValue: string): string {
  return `
    <article class="st-admin-card">
      <div class="st-admin-card__header"><div><p class="st-admin-eyebrow">Runtime-backed</p><h2>${escapeHtml(title)}</h2></div></div>
      <p><strong>Owner:</strong> ${escapeHtml(challenge.owner)}</p>
      <p><strong>Cadence:</strong> ${escapeHtml(challenge.cadence)}</p>
      <p><strong>${escapeHtml(identityLabel)}:</strong> ${escapeHtml(identityValue)}</p>
      <p><strong>Seed policy:</strong> <code>${escapeHtml(challenge.seedPolicy)}</code></p>
      <p><strong>Adaptive policy:</strong> ${escapeHtml(challenge.adaptivePolicy)}</p>
      <p><strong>Personal Best:</strong> ${String(challenge.personalBest)} · <strong>Personal Ghost:</strong> ${String(challenge.personalGhost)}</p>
      <p><strong>Browser profile key:</strong> <code>${escapeHtml(challenge.profileStorageKey)}</code></p>
      <p class="st-admin-notice">No remote scheduler or remote leaderboard is owned by this contract. Admin writes remain closed.</p>
    </article>
  `;
}

export function renderPhaseBDailyWeekly(): HTMLElement {
  const root = document.createElement("section");
  root.className = "space-admin-page space-admin-page--phase-b";
  root.innerHTML = `
    <header class="space-admin-page__header">
      <div>
        <p class="st-admin-eyebrow">Live Ops · Runtime Ownership</p>
        <h1>Daily / Weekly</h1>
        <p>Inspect the deterministic Daily Expedition and Weekly Challenge runtimes without inventing remote scheduling, leaderboard, seed override, reward authoring, or player-progress mutation.</p>
      </div>
      <div class="space-admin-page__badges">
        <span class="st-admin-badge">DAILY · RUNTIME-BACKED</span>
        <span class="st-admin-badge">WEEKLY · RUNTIME-BACKED</span>
        <span class="st-admin-badge">READ ONLY</span>
      </div>
    </header>
    <p class="st-admin-notice" data-daily-weekly-status aria-live="polite">Loading canonical Daily / Weekly ownership…</p>
    <div class="space-admin-grid" data-daily-weekly-content></div>
  `;

  const status = root.querySelector<HTMLElement>("[data-daily-weekly-status]");
  const content = root.querySelector<HTMLElement>("[data-daily-weekly-content]");
  if (!status || !content) return root;

  let loadGeneration = 0;
  const load = (): void => {
    const generation = ++loadGeneration;
    setAdminStatus(status, "Loading canonical Daily / Weekly ownership…", "loading");
    content.replaceChildren();
    void fetchContract()
      .then((contract) => {
        if (generation !== loadGeneration) return;
        const liveOps = contract.liveOps;
        const daily = liveOps.daily;
        const weekly = liveOps.weekly;
        setAdminStatus(status, "Daily and Weekly are canonical deterministic browser-local challenge runtimes; Admin reads ownership only and cannot schedule, reseed, author rewards, publish, or mutate player progress.", "success");
        content.innerHTML = `
          ${challengeCard("Daily Expedition", daily, "Day key", daily.dayKeyFormat)}
          ${challengeCard("Weekly Challenge", weekly, "Week key", `${weekly.weekKeyFormat} · ${weekly.weekKeyOwner}`)}
          <article class="st-admin-card space-admin-card--wide">
            <div class="st-admin-card__header"><div><p class="st-admin-eyebrow">Comparability</p><h2>Daily identity fields</h2></div></div>
            ${chipList(daily.identityFields)}
          </article>
          <article class="st-admin-card space-admin-card--wide">
            <div class="st-admin-card__header"><div><p class="st-admin-eyebrow">Weekly state</p><h2>Canonical readable state</h2></div></div>
            ${chipList(weekly.readableState)}
            <p><strong>Seed owner:</strong> <code>${escapeHtml(weekly.seedOwner)}</code></p>
            <p><strong>Scheduler control:</strong> ${String(weekly.schedulerControlCapability)} · <strong>Reward authoring:</strong> ${String(weekly.rewardAuthoringCapability)} · <strong>Seed override:</strong> ${String(weekly.seedOverrideCapability)}</p>
          </article>
          <article class="st-admin-card space-admin-card--wide">
            <div class="st-admin-card__header"><div><p class="st-admin-eyebrow">Boundary</p><h2>No synthetic live-ops authoring</h2></div></div>
            <p>The following operations are intentionally unavailable because no canonical remote Live Ops service owns them:</p>
            <ul>${liveOps.unsupportedAdminOperations.map((item) => `<li>${escapeHtml(item)}</li>`).join("")}</ul>
          </article>
        `;
      })
      .catch((error: unknown) => {
        if (generation !== loadGeneration) return;
        setAdminStatus(status, "Daily / Weekly runtime contract is unavailable.", "error");
        renderAdminFailureState(content, {
          title: "Daily / Weekly unavailable",
          fallbackMessage: "The canonical Daily / Weekly contract could not be loaded. Check the local Admin runtime and try again.",
          error,
          onRetry: load,
        });
      });
  };

  load();
  return root;
}
