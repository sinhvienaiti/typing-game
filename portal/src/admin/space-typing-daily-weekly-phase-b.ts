import { SpaceTypingAdminApi } from "./api";

const api = new SpaceTypingAdminApi();

type DailyWeeklyContract = {
  contractRevision: string;
  schemaVersion: number;
  capability: "daily-weekly.read";
  liveOps: {
    mode: "runtime-partial-readonly";
    runtimeSources: string[];
    daily: {
      available: true;
      owner: string;
      challengeKind: "daily";
      cadence: "utc-day";
      dayKeyFormat: "YYYY-MM-DD";
      seedPolicy: string;
      identityFields: string[];
      adaptivePolicy: "frozen";
      personalBest: boolean;
      personalGhost: boolean;
      profileStorageKey: string;
      remoteScheduler: false;
      remoteLeaderboard: false;
    };
    weekly: { available: false; reason: string };
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

async function fetchContract(): Promise<DailyWeeklyContract> {
  const response = await fetch("/api/admin/space-typing/daily-weekly/contract", {
    cache: "no-store",
    headers: { "x-typing-game-admin-token": api.getToken() },
  });
  if (!response.ok) throw new Error(`Daily / Weekly contract request failed (${response.status})`);
  const payload = (await response.json()) as DailyWeeklyContract;
  if (
    payload.capability !== "daily-weekly.read" ||
    payload.liveOps?.mode !== "runtime-partial-readonly" ||
    payload.liveOps.daily?.available !== true ||
    payload.liveOps.weekly?.available !== false ||
    payload.liveOps.adminWriteCapability !== false
  ) {
    throw new Error("Daily / Weekly contract does not match the canonical partial read-only runtime boundary.");
  }
  return payload;
}

function chipList(values: string[]): string {
  return `<div class="st-admin-chip-list">${values.map((value) => `<span class="st-admin-chip">${escapeHtml(value)}</span>`).join("")}</div>`;
}

export function renderPhaseBDailyWeekly(): HTMLElement {
  const root = document.createElement("section");
  root.className = "space-admin-page space-admin-page--phase-b";
  root.innerHTML = `
    <header class="space-admin-page__header">
      <div>
        <p class="st-admin-eyebrow">Live Ops · Runtime Ownership</p>
        <h1>Daily / Weekly</h1>
        <p>Inspect the fixed Daily Expedition challenge that exists in production and keep Weekly explicitly absent until a real runtime owner is implemented.</p>
      </div>
      <div class="space-admin-page__badges">
        <span class="st-admin-badge">DAILY · RUNTIME-BACKED</span>
        <span class="st-admin-badge">WEEKLY · NOT IMPLEMENTED</span>
        <span class="st-admin-badge">READ ONLY</span>
      </div>
    </header>
    <p class="st-admin-notice" data-daily-weekly-status>Loading canonical Daily / Weekly ownership…</p>
    <div class="space-admin-grid" data-daily-weekly-content></div>
  `;

  const status = root.querySelector<HTMLElement>("[data-daily-weekly-status]");
  const content = root.querySelector<HTMLElement>("[data-daily-weekly-content]");
  if (!status || !content) return root;

  void fetchContract()
    .then((contract) => {
      const liveOps = contract.liveOps;
      const daily = liveOps.daily;
      status.textContent = "Daily Expedition is canonical and deterministic per UTC day; Weekly has no canonical runtime implementation. Admin writes are closed.";
      content.innerHTML = `
        <article class="st-admin-card">
          <div class="st-admin-card__header"><div><p class="st-admin-eyebrow">Supported</p><h2>Daily Expedition</h2></div></div>
          <p><strong>Owner:</strong> ${escapeHtml(daily.owner)}</p>
          <p><strong>Cadence:</strong> ${escapeHtml(daily.cadence)} · ${escapeHtml(daily.dayKeyFormat)}</p>
          <p><strong>Seed policy:</strong> <code>${escapeHtml(daily.seedPolicy)}</code></p>
          <p><strong>Adaptive policy:</strong> ${escapeHtml(daily.adaptivePolicy)}</p>
          <p><strong>Personal Best:</strong> ${String(daily.personalBest)} · <strong>Personal Ghost:</strong> ${String(daily.personalGhost)}</p>
          <p><strong>Browser profile key:</strong> <code>${escapeHtml(daily.profileStorageKey)}</code></p>
          <p class="st-admin-notice">No remote scheduler or remote leaderboard is owned by this contract.</p>
        </article>
        <article class="st-admin-card">
          <div class="st-admin-card__header"><div><p class="st-admin-eyebrow">Absent</p><h2>Weekly</h2></div></div>
          <p>${escapeHtml(liveOps.weekly.reason)}</p>
          <p class="st-admin-notice">Admin does not fabricate a weekly seed, reset scheduler, reward track, or publish flow.</p>
        </article>
        <article class="st-admin-card space-admin-card--wide">
          <div class="st-admin-card__header"><div><p class="st-admin-eyebrow">Comparability</p><h2>Daily identity fields</h2></div></div>
          ${chipList(daily.identityFields)}
        </article>
        <article class="st-admin-card space-admin-card--wide">
          <div class="st-admin-card__header"><div><p class="st-admin-eyebrow">Boundary</p><h2>No synthetic live-ops authoring</h2></div></div>
          <ul>${liveOps.unsupportedAdminOperations.map((item) => `<li>${escapeHtml(item)}</li>`).join("")}</ul>
        </article>
      `;
    })
    .catch((error) => {
      status.textContent = error instanceof Error ? error.message : "Unable to load Daily / Weekly contract.";
      status.classList.add("st-admin-notice--error");
    });

  return root;
}
