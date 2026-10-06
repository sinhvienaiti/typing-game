import "./space-typing-ui.css";
import { renderExtendedAdminScreen } from "./space-typing-extended";
import { adminNavIcon } from "./space-typing-icons";
import { installAdminCommandShortcut, openAdminCommandPalette } from "./space-typing-command";
import { renderWorldMusicV2 } from "./space-typing-world-music-v2";
import { renderDailyWeekly } from "./space-typing-daily-weekly";
import {
  alertFeed,
  audienceMetrics,
  audioDefaults,
  duckingDefaults,
  economyMetrics,
  modeSplit,
  musicTracks,
  overviewMetrics,
  problemStages,
  recentChanges,
  retention,
  ships,
  systemHealth,
  type MusicTrack,
  type ShipMock,
} from "./space-typing-mock";

type NavItem = {
  label: string;
  path: string;
  icon: string;
  phase?: "ready" | "planned";
};

type NavGroup = {
  label: string;
  items: readonly NavItem[];
};

const ADMIN_BASE = "/admin/space-typing";
const SHIP_ASSET_BASE = "https://space.typing-game.local/assets/space-typing/ships/3d";

const NAV_GROUPS: readonly NavGroup[] = [
  {
    label: "Dashboard",
    items: [
      { label: "Overview", path: ADMIN_BASE, icon: "◫", phase: "ready" },
      { label: "Analytics", path: `${ADMIN_BASE}/analytics`, icon: "⌁", phase: "ready" },
    ],
  },
  {
    label: "Audio & Music",
    items: [
      { label: "Audio Defaults", path: `${ADMIN_BASE}/audio`, icon: "◖", phase: "ready" },
      { label: "Music Library", path: `${ADMIN_BASE}/music-library`, icon: "♫", phase: "ready" },
      { label: "World / Stage Music", path: `${ADMIN_BASE}/world-music`, icon: "◎", phase: "ready" },
    ],
  },
  {
    label: "Game Content",
    items: [
      { label: "Ships", path: `${ADMIN_BASE}/ships`, icon: "△", phase: "ready" },
      { label: "Equipment", path: `${ADMIN_BASE}/equipment`, icon: "◇", phase: "ready" },
      { label: "Skills", path: `${ADMIN_BASE}/skills`, icon: "ϟ", phase: "ready" },
      { label: "Enemies", path: `${ADMIN_BASE}/enemies`, icon: "✦", phase: "ready" },
      { label: "Bosses", path: `${ADMIN_BASE}/bosses`, icon: "✹", phase: "ready" },
      { label: "Worlds & Stages", path: `${ADMIN_BASE}/stages`, icon: "⌘", phase: "ready" },
      { label: "Typing Content", path: `${ADMIN_BASE}/typing-content`, icon: "Aa", phase: "ready" },
    ],
  },
  {
    label: "Economy",
    items: [
      { label: "Shop", path: `${ADMIN_BASE}/shop`, icon: "▣", phase: "ready" },
      { label: "Currencies", path: `${ADMIN_BASE}/currencies`, icon: "◈", phase: "ready" },
      { label: "Rewards & Drops", path: `${ADMIN_BASE}/rewards`, icon: "✧", phase: "ready" },
      { label: "Stamina / Warp", path: `${ADMIN_BASE}/warp`, icon: "⚡", phase: "ready" },
    ],
  },
  {
    label: "Live Ops",
    items: [
      { label: "Missions", path: `${ADMIN_BASE}/missions`, icon: "✓", phase: "ready" },
      { label: "Daily / Weekly", path: `${ADMIN_BASE}/daily-weekly`, icon: "◷", phase: "ready" },
      { label: "Expedition", path: `${ADMIN_BASE}/expedition`, icon: "↗", phase: "ready" },
      { label: "Events", path: `${ADMIN_BASE}/events`, icon: "◷", phase: "ready" },
    ],
  },
  {
    label: "PvP",
    items: [
      { label: "Duel Settings", path: `${ADMIN_BASE}/duel`, icon: "⚔", phase: "ready" },
      { label: "Ranked", path: `${ADMIN_BASE}/ranked`, icon: "♜", phase: "ready" },
      { label: "Alternative Modes", path: `${ADMIN_BASE}/alternative-modes`, icon: "⇄", phase: "ready" },
    ],
  },
  {
    label: "Visuals",
    items: [
      { label: "Backgrounds", path: `${ADMIN_BASE}/backgrounds`, icon: "▧", phase: "ready" },
      { label: "VFX", path: `${ADMIN_BASE}/vfx`, icon: "✺", phase: "ready" },
      { label: "UI Assets", path: `${ADMIN_BASE}/ui-assets`, icon: "▦", phase: "ready" },
    ],
  },
  {
    label: "System",
    items: [
      { label: "General Settings", path: `${ADMIN_BASE}/settings`, icon: "⚙", phase: "ready" },
      { label: "Feature Flags", path: `${ADMIN_BASE}/flags`, icon: "⚑", phase: "ready" },
      { label: "History & Publish", path: `${ADMIN_BASE}/history`, icon: "↶", phase: "ready" },
    ],
  },
  {
    label: "Developer",
    items: [{ label: "QA Sandbox", path: `${ADMIN_BASE}/qa`, icon: "⌬", phase: "ready" }],
  },
];

const READY_PATHS = new Set(
  NAV_GROUPS.flatMap((group) => group.items)
    .filter((item) => item.phase === "ready")
    .map((item) => item.path),
);

function element<K extends keyof HTMLElementTagNameMap>(
  tag: K,
  className?: string,
  text?: string,
): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (className !== undefined) node.className = className;
  if (text !== undefined) node.textContent = text;
  return node;
}

function button(
  label: string,
  onClick: () => void,
  className = "st-admin-btn",
): HTMLButtonElement {
  const node = element("button", className, label);
  node.type = "button";
  node.addEventListener("click", onClick);
  return node;
}

function pageHeader(
  eyebrow: string,
  title: string,
  description: string,
  actions: readonly HTMLElement[] = [],
): HTMLElement {
  const head = element("header", "st-admin-page-head");
  const copy = element("div", "st-admin-page-head-copy");
  copy.append(
    element("div", "st-admin-eyebrow", eyebrow),
    element("h1", undefined, title),
    element("p", undefined, description),
  );
  head.append(copy);
  if (actions.length > 0) {
    const tools = element("div", "st-admin-page-actions");
    tools.append(...actions);
    head.append(tools);
  }
  return head;
}

function panel(title?: string, subtitle?: string, solid = false): HTMLElement {
  const root = element("section", `st-admin-panel${solid ? " solid" : ""}`);
  if (title !== undefined) {
    const head = element("div", "st-admin-panel-head");
    const copy = element("div");
    copy.append(element("h2", undefined, title));
    if (subtitle !== undefined) copy.append(element("p", undefined, subtitle));
    head.append(copy);
    root.append(head);
  }
  return root;
}

function statusBadge(label: string, tone: "good" | "warn" | "bad" | "info" = "info"): HTMLElement {
  return element("span", `st-admin-status ${tone}`, label);
}

function sparkBars(values: readonly number[]): HTMLElement {
  const spark = element("span", "st-admin-spark");
  const max = Math.max(...values, 1);
  for (const value of values) {
    const bar = element("i");
    bar.style.height = `${Math.max(3, Math.round((value / max) * 24))}px`;
    spark.append(bar);
  }
  return spark;
}

function trackWave(seed: number): HTMLElement {
  const wave = element("div", "st-admin-waveform");
  for (let index = 0; index < 54; index += 1) {
    const line = element("i");
    const height = 8 + ((index * 17 + seed * 11) % 34);
    line.style.height = `${height}px`;
    wave.append(line);
  }
  return wave;
}

function shipImageUrl(shipId: string): string {
  return `${SHIP_ASSET_BASE}/${encodeURIComponent(shipId)}/color.webp`;
}

export class SpaceTypingAdmin {
  private selectedTrackId = musicTracks[0]?.id ?? "";
  private selectedWorldId = "world-01";
  private selectedWorldState = "Normal";
  private selectedShipId = ships[0]?.id ?? "vanguard";
  private audioChanges = 0;

  constructor(private readonly navigate: (path: string) => void) {
    installAdminCommandShortcut(this.navigate);
  }

  render(path: string): HTMLElement {
    const root = element("main", "st-admin");
    const shell = element("div", "st-admin-shell");
    shell.append(this.renderSidebar(path));

    const main = element("div", "st-admin-main");
    main.append(this.renderTopbar(path));
    const content = element("div", "st-admin-content");
    content.append(this.renderPage(path));
    main.append(content);

    shell.append(main);
    root.append(shell);
    return root;
  }

  private renderSidebar(path: string): HTMLElement {
    const aside = element("aside", "st-admin-sidebar");
    const brand = element("div", "st-admin-brand");
    const mark = element("div", "st-admin-brand-mark");
    mark.append(element("span", "st-admin-brand-logo", "ST"), element("span", undefined, "Space Typing"));
    brand.append(mark, element("h2", undefined, "Command Center"), element("p", undefined, "Live Ops · Content · Configuration"));
    const env = element("div", "st-admin-env-row");
    env.append(element("span", "st-admin-env", "LOCAL"), element("span", "st-admin-mock-badge", "UI MOCK DATA"));
    brand.append(env);
    aside.append(brand);

    const nav = element("nav", "st-admin-nav");
    for (const group of NAV_GROUPS) {
      const wrapper = element("section", "st-admin-nav-group");
      wrapper.append(element("h3", "st-admin-nav-label", group.label));
      for (const item of group.items) {
        const navButton = element(
          "button",
          `st-admin-nav-item${path === item.path ? " active" : ""}${item.phase === "planned" ? " planned" : ""}`,
        );
        navButton.type = "button";
        navButton.append(
          adminNavIcon(item.icon),
          element("span", "st-admin-nav-text", item.label),
          element("span", "st-admin-nav-phase", item.phase === "ready" ? "UI" : "plan"),
        );
        navButton.addEventListener("click", () => this.navigate(item.path));
        wrapper.append(navButton);
      }
      nav.append(wrapper);
    }
    aside.append(nav);
    return aside;
  }

  private renderTopbar(path: string): HTMLElement {
    const bar = element("div", "st-admin-topbar");
    const item = NAV_GROUPS.flatMap((group) => group.items).find((candidate) => candidate.path === path);
    const breadcrumb = element("div", "st-admin-breadcrumb");
    breadcrumb.append(document.createTextNode("Space Typing / "), element("strong", undefined, item?.label ?? "Admin"));
    bar.append(breadcrumb);
    bar.append(element("div", "st-admin-topbar-spacer"));
    bar.append(button("⌘K  Search command…", () => openAdminCommandPalette(this.navigate), "st-admin-command"));
    bar.append(element("span", "st-admin-revision", "UI REV · A-HOLO-04"));
    bar.append(statusBadge("LOCAL", "good"));
    return bar;
  }

  private renderPage(path: string): HTMLElement {
    if (path === ADMIN_BASE) return this.renderOverview();
    if (path === `${ADMIN_BASE}/audio`) return this.renderAudio();
    if (path === `${ADMIN_BASE}/music-library`) return this.renderMusicLibrary();
    if (path === `${ADMIN_BASE}/world-music`) return renderWorldMusicV2(this.navigate);
    if (path === `${ADMIN_BASE}/ships`) return this.renderShips();
    if (path === `${ADMIN_BASE}/daily-weekly`) return renderDailyWeekly();
    return renderExtendedAdminScreen(path, this.navigate) ?? this.renderPlanned(path);
  }

  private renderOverview(): HTMLElement {
    const page = element("div");
    const filters = this.timeFilters();
    page.append(pageHeader(
      "Fleet Operations · Realtime Intelligence",
      "Overview",
      "Theo dõi tình trạng người chơi, gameplay, economy và system health. Toàn bộ số liệu ở milestone UI này là mock data để review bố cục trước khi nối telemetry thật.",
      [button("⟳ Auto Refresh", () => undefined), button("Open Analytics →", () => this.navigate(`${ADMIN_BASE}/analytics`), "st-admin-btn primary")],
    ));
    page.append(filters);

    const kpis = element("div", "st-admin-grid cols-6");
    for (const metric of overviewMetrics) {
      const card = element("article", "st-admin-panel st-admin-kpi");
      card.append(element("div", "st-admin-kpi-label", metric.label), element("div", "st-admin-kpi-value", metric.value));
      const footer = element("div", "st-admin-kpi-footer");
      footer.append(element("span", `st-admin-delta ${metric.tone ?? "neutral"}`, `${metric.trend === "up" ? "↑" : metric.trend === "down" ? "↓" : "→"} ${metric.delta}`), sparkBars(metric.spark));
      card.append(footer);
      kpis.append(card);
    }
    page.append(kpis);

    const layout = element("div", "st-admin-overview-layout");
    const left = element("div", "st-admin-overview-stack");
    const audience = panel("Player Activity", "DAU / WAU / MAU và session health", true);
    const mini = element("div", "st-admin-mini-metrics");
    for (const [label, value, delta] of audienceMetrics) {
      const metric = element("div", "st-admin-mini-metric");
      metric.append(element("span", "st-admin-mini-metric-label", label), element("strong", undefined, value), element("small", undefined, delta));
      mini.append(metric);
    }
    audience.append(mini);

    const stages = panel("Problem Stages", "Các stage có anomaly cao nhất trong khoảng thời gian đang chọn", true);
    stages.append(this.renderStageTable());
    left.append(audience, stages);

    const right = element("div", "st-admin-overview-stack");
    const mode = panel("Playing Now", "Phân bố người chơi theo mode", true);
    const bars = element("div", "st-admin-bar-list");
    for (const row of modeSplit) {
      const bar = element("div", "st-admin-bar-row");
      const track = element("span", "st-admin-bar-track");
      const fill = element("i");
      fill.style.width = `${row.value}%`;
      track.append(fill);
      bar.append(element("span", undefined, row.label), track, element("strong", undefined, String(row.count)));
      bars.append(bar);
    }
    mode.append(bars);

    const retain = panel("Retention", "Cohort snapshot", true);
    const retentionBars = element("div", "st-admin-bar-list");
    for (const [label, value] of retention) {
      const row = element("div", "st-admin-bar-row");
      const track = element("span", "st-admin-bar-track");
      const fill = element("i");
      fill.style.width = `${value}%`;
      track.append(fill);
      row.append(element("span", undefined, label), track, element("strong", undefined, `${value}%`));
      retentionBars.append(row);
    }
    retain.append(retentionBars);

    const health = panel("System Health", "Runtime / network / assets", true);
    const healthList = element("div", "st-admin-health-list");
    for (const item of systemHealth) {
      const row = element("div", "st-admin-health");
      row.append(element("span", undefined, item.label), element("strong", item.tone, item.value));
      healthList.append(row);
    }
    health.append(healthList);
    right.append(mode, retain, health);
    layout.append(left, right);
    page.append(layout);

    const lower = element("div", "st-admin-grid cols-2");
    lower.style.marginTop = "12px";
    lower.append(this.renderEconomyPanel(), this.renderAlertsPanel());
    page.append(lower, this.renderRecentOperations());
    return page;
  }

  private renderRecentOperations(): HTMLElement {
    const root = panel("Recent Operations", "Latest draft / publish / rollback activity", true);
    const rows = element("div", "stx-revision-list");
    for (const change of recentChanges) {
      const row = element("div", "stx-revision");
      row.append(
        element("strong", undefined, change.revision),
        statusBadge(change.tone.toUpperCase(), change.tone === "published" ? "good" : "warn"),
        element("span", undefined, change.title),
        element("small", undefined, `${change.author} · ${change.time}`),
      );
      rows.append(row);
    }
    root.append(rows);
    return root;
  }

  private timeFilters(): HTMLElement {
    const bar = element("div", "st-admin-filterbar");
    const seg = element("div", "st-admin-seg");
    const labels = ["Today", "24h", "7d", "30d", "90d", "Custom"];
    for (const [index, label] of labels.entries()) {
      const control = button(label, () => {
        for (const child of Array.from(seg.children)) child.classList.remove("active");
        control.classList.add("active");
      }, index === 0 ? "active" : "");
      seg.append(control);
    }
    bar.append(seg, element("div", "st-admin-filter-spacer"));
    const tz = element("select", "st-admin-select");
    tz.append(new Option("Asia/Ho_Chi_Minh", "Asia/Ho_Chi_Minh"), new Option("UTC", "UTC"));
    const compare = element("select", "st-admin-select");
    compare.append(new Option("Compare previous period", "previous"), new Option("No comparison", "none"));
    bar.append(tz, compare, element("span", "st-admin-chip", "Updated 18s ago"));
    return bar;
  }

  private renderStageTable(): HTMLElement {
    const wrap = element("div", "st-admin-table-wrap");
    const table = element("table", "st-admin-table");
    table.innerHTML = "<thead><tr><th>Stage</th><th>World</th><th>Plays</th><th>Clear</th><th>Retry</th><th>WPM</th><th>Accuracy</th><th>Duration</th><th>Status</th></tr></thead>";
    const body = element("tbody");
    for (const row of problemStages) {
      const tr = element("tr");
      tr.innerHTML = `<td class="primary">${row.stage}</td><td>${row.world}</td><td>${row.plays}</td><td>${row.clearRate}%</td><td>${row.retryRate.toFixed(1)}×</td><td>${row.wpm}</td><td>${row.accuracy.toFixed(1)}%</td><td>${row.duration}</td>`;
      const status = element("td");
      status.append(statusBadge(row.status.toUpperCase(), row.status === "critical" ? "bad" : row.status === "warning" ? "warn" : "good"));
      tr.append(status);
      body.append(tr);
    }
    table.append(body);
    wrap.append(table);
    return wrap;
  }

  private renderEconomyPanel(): HTMLElement {
    const root = panel("Economy Pulse", "Nguồn / sink tổng hợp trong khoảng thời gian", true);
    const mini = element("div", "st-admin-mini-metrics");
    for (const [label, value, delta] of economyMetrics) {
      const metric = element("div", "st-admin-mini-metric");
      metric.append(element("span", "st-admin-mini-metric-label", label), element("strong", undefined, value), element("small", undefined, delta));
      mini.append(metric);
    }
    root.append(mini);
    return root;
  }

  private renderAlertsPanel(): HTMLElement {
    const root = panel("Command Alerts", "Cảnh báo cần Admin chú ý", true);
    const alerts = element("div", "st-admin-alerts");
    for (const item of alertFeed) {
      const row = element("article", `st-admin-alert ${item.severity}`);
      row.append(element("span", "st-admin-alert-dot"));
      const copy = element("div");
      copy.append(element("div", "st-admin-alert-title", item.title), element("div", "st-admin-alert-detail", item.detail));
      row.append(copy, element("span", "st-admin-alert-time", item.time));
      alerts.append(row);
    }
    root.append(alerts);
    return root;
  }

  private renderAudio(): HTMLElement {
    const page = element("div");
    page.append(pageHeader(
      "Audio · Default Player Profile",
      "Audio Defaults",
      "Cấu hình mặc định dành cho người chơi chưa từng tự chỉnh Audio. Người chơi đã có preference riêng sẽ không bị UI này ghi đè khi backend được map ở phase sau.",
      [statusBadge("DEFAULT PROFILE · recommended-v1", "info")],
    ));
    const banner = element("div", "st-admin-info-banner", "DEFAULT-ONLY RULE · Các giá trị dưới đây chỉ đại diện profile mặc định. Existing player preferences must remain untouched. UI milestone hiện dùng local mock state và chưa ghi backend.");
    page.append(banner);

    const layout = element("div", "st-admin-audio-layout");
    const volumes = panel("Default Volume Profile", "11 nhóm âm thanh mặc định", true);
    const list = element("div", "st-admin-audio-list");
    for (const [label, initial] of audioDefaults) list.append(this.audioSlider(label, initial));
    volumes.append(list);

    const side = element("div", "st-admin-overview-stack");
    const ducking = panel("Pronunciation Priority", "Ducking mặc định khi TTS phát", true);
    const duckList = element("div", "st-admin-audio-list");
    for (const [label, initial] of duckingDefaults) duckList.append(this.audioSlider(label, initial));
    ducking.append(duckList);

    const behavior = panel("Playback Behaviour", "Default behaviour policy", true);
    const behaviorBody = element("div", "st-admin-panel-pad");
    for (const [label, enabled] of [
      ["Pronunciation priority", true],
      ["Resume music after TTS", true],
      ["Allow overlapping pronunciation", false],
      ["Boss music priority", true],
      ["Victory music priority", true],
      ["Duel announcer priority", true],
    ] as const) behaviorBody.append(this.toggleRow(label, enabled));
    behavior.append(behaviorBody);

    const preview = panel("Mix Preview", "UI-only preview actions", true);
    const testGrid = element("div", "st-admin-test-grid");
    for (const label of ["Pronunciation", "Typing", "Combat", "Warning", "Announcer", "All Mix"]) {
      testGrid.append(button(`▶ ${label}`, () => this.flashPreview(preview, label)));
    }
    preview.append(testGrid);
    side.append(ducking, behavior, preview);
    layout.append(volumes, side);
    page.append(layout, this.renderUnsavedBar());
    return page;
  }

  private audioSlider(label: string, initial: number): HTMLElement {
    const row = element("div", "st-admin-audio-row");
    const control = element("input") as HTMLInputElement;
    control.type = "range";
    control.min = "0";
    control.max = "100";
    control.value = String(initial);
    const value = element("span", "st-admin-audio-value", `${initial}%`);
    control.addEventListener("input", () => {
      value.textContent = `${control.value}%`;
      this.audioChanges += 1;
      this.updateUnsavedBars();
    });
    row.append(element("label", undefined, label), control, value);
    return row;
  }

  private toggleRow(label: string, initial: boolean): HTMLElement {
    const row = element("div", "st-admin-switch-row");
    const toggle = element("button", `st-admin-switch${initial ? " on" : ""}`) as HTMLButtonElement;
    toggle.type = "button";
    toggle.setAttribute("aria-label", `Toggle ${label}`);
    toggle.append(element("i"));
    toggle.addEventListener("click", () => {
      toggle.classList.toggle("on");
      this.audioChanges += 1;
      this.updateUnsavedBars();
    });
    row.append(element("span", undefined, label), toggle);
    return row;
  }

  private flashPreview(root: HTMLElement, label: string): void {
    let chip = root.querySelector<HTMLElement>(".st-admin-preview-status");
    if (chip === null) {
      chip = element("div", "st-admin-info-banner st-admin-preview-status");
      root.append(chip);
    }
    chip.textContent = `UI preview trigger · ${label}. Audio engine mapping intentionally deferred to Phase B/C.`;
  }

  private renderUnsavedBar(): HTMLElement {
    const bar = element("div", "st-admin-sticky-save");
    bar.dataset["unsavedBar"] = "true";
    bar.append(element("strong", undefined, this.audioChanges === 0 ? "No unsaved changes" : `${this.audioChanges} unsaved changes`), element("span", undefined, "UI mock only · no backend write"), element("div", "grow"));
    bar.append(button("Discard", () => {
      this.audioChanges = 0;
      this.updateUnsavedBars();
      this.navigate(`${ADMIN_BASE}/audio`);
    }), button("Save Draft", () => {
      this.audioChanges = 0;
      this.updateUnsavedBars();
    }, "st-admin-btn primary"));
    return bar;
  }

  private updateUnsavedBars(): void {
    for (const bar of document.querySelectorAll<HTMLElement>("[data-unsaved-bar='true']")) {
      const strong = bar.querySelector("strong");
      if (strong !== null) strong.textContent = this.audioChanges === 0 ? "No unsaved changes" : `${this.audioChanges} unsaved changes`;
    }
  }

  private renderMusicLibrary(): HTMLElement {
    const page = element("div");
    page.append(pageHeader(
      "Audio & Music · Asset Operations",
      "Music Library",
      "Thư viện nhạc tập trung với metadata, trạng thái validation, usage và preview tích hợp. Upload/scan ở milestone này là UI-only để duyệt workflow.",
      [button("Scan Library", () => undefined), button("Upload Files", () => undefined, "st-admin-btn primary")],
    ));

    const filters = element("div", "st-admin-filterbar");
    const search = element("input", "st-admin-search") as HTMLInputElement;
    search.type = "search";
    search.placeholder = "Search track ID, title, filename…";
    const type = element("select", "st-admin-select");
    type.append(new Option("All types", ""), ...["BGM", "Boss", "Ambient", "Victory", "Duel"].map((value) => new Option(value, value)));
    const status = element("select", "st-admin-select");
    status.append(new Option("All status", ""), new Option("Ready", "READY"), new Option("Unused", "UNUSED"), new Option("Warning", "WARNING"));
    filters.append(search, type, status, element("div", "st-admin-filter-spacer"), button("Find Unused", () => {
      search.value = "";
      status.value = "UNUSED";
      renderRows();
    }), button("Validate", () => undefined));
    page.append(filters);

    const layout = element("div", "st-admin-library-layout");
    const library = panel("Track Library", `${musicTracks.length} UI mock tracks · table pattern for large catalog`, true);
    const tableHost = element("div", "st-admin-table-wrap");
    library.append(tableHost);
    const detail = element("div", "st-admin-track-preview");
    layout.append(library, detail);
    page.append(layout);

    const renderRows = (): void => {
      const query = search.value.trim().toLowerCase();
      const selectedType = type.value;
      const selectedStatus = status.value;
      const rows = musicTracks.filter((track) =>
        (query.length === 0 || `${track.id} ${track.title} ${track.file}`.toLowerCase().includes(query)) &&
        (selectedType.length === 0 || track.type === selectedType) &&
        (selectedStatus.length === 0 || track.status === selectedStatus),
      );
      tableHost.replaceChildren(this.renderTrackTable(rows, () => this.renderTrackDetail(detail)));
    };
    search.addEventListener("input", renderRows);
    type.addEventListener("change", renderRows);
    status.addEventListener("change", renderRows);
    renderRows();
    this.renderTrackDetail(detail);
    return page;
  }

  private renderTrackTable(tracks: readonly MusicTrack[], onSelect: () => void): HTMLElement {
    const table = element("table", "st-admin-table");
    table.innerHTML = "<thead><tr><th>Preview</th><th>Track</th><th>Type</th><th>Duration</th><th>Format</th><th>BPM</th><th>Mood</th><th>Usage</th><th>Status</th></tr></thead>";
    const body = element("tbody");
    for (const track of tracks) {
      const row = element("tr", "clickable");
      row.innerHTML = `<td>▶</td><td><span class="primary">${track.title}</span><br><small>${track.id}</small></td><td>${track.type}</td><td>${track.duration}</td><td>${track.format}</td><td>${track.bpm}</td><td>${track.mood}</td><td>${track.usage}</td>`;
      const state = element("td");
      state.append(statusBadge(track.status, track.status === "READY" ? "good" : track.status === "UNUSED" ? "warn" : "bad"));
      row.append(state);
      row.addEventListener("click", () => {
        this.selectedTrackId = track.id;
        onSelect();
      });
      body.append(row);
    }
    table.append(body);
    return table;
  }

  private renderTrackDetail(host: HTMLElement): void {
    const track = musicTracks.find((candidate) => candidate.id === this.selectedTrackId) ?? musicTracks[0];
    host.replaceChildren();
    if (track === undefined) return;
    const root = panel("Track Detail", "Integrated preview · no standalone preview page", true);
    root.append(element("div", "st-admin-track-cover", "♫"));
    const player = element("div", "st-admin-player");
    player.append(button("▶", () => undefined, "st-admin-play"));
    const progress = element("span", "st-admin-player-track");
    progress.append(element("i"));
    player.append(progress, element("span", "st-admin-chip", `00:43 / ${track.duration}`));
    root.append(player, trackWave(track.bpm));
    const details = element("dl", "st-admin-detail-list");
    for (const [label, value] of [
      ["Title", track.title], ["Track ID", track.id], ["File", track.file], ["Type", track.type], ["Format", track.format], ["Size", track.size], ["BPM", String(track.bpm)], ["Mood", track.mood], ["Usage", String(track.usage)], ["Status", track.status],
    ]) {
      const cell = element("div");
      cell.append(element("dt", undefined, label), element("dd", undefined, value));
      details.append(cell);
    }
    root.append(details);
    const usage = element("div", "st-admin-usage");
    usage.append(element("strong", undefined, "Used by"), element("small", undefined, track.worlds.length === 0 ? "No assignment · safe candidate for review" : track.worlds.join(" · ")));
    root.append(usage);
    host.append(root);
  }

  private renderShips(): HTMLElement {
    const page = element("div");
    page.append(pageHeader(
      "Game Content · Fleet Registry",
      "Ships",
      "UI editor cho toàn bộ identity, visual, base stats, combat presentation và unlock. Phase hiện tại chỉ review cấu trúc và thao tác; chưa ghi vào config thật.",
      [button("Compare Ships", () => undefined), button("+ New Ship", () => undefined, "st-admin-btn primary")],
    ));

    const layout = element("div", "st-admin-ships-layout");
    const listPanel = panel("Ship Registry", `${ships.length} mock ships`, true);
    const shipList = element("div", "st-admin-ship-list");
    for (const ship of ships) {
      const card = element("button", `st-admin-ship-card${ship.id === this.selectedShipId ? " active" : ""}`) as HTMLButtonElement;
      card.type = "button";
      const image = element("img", "st-admin-ship-thumb") as HTMLImageElement;
      image.src = shipImageUrl(ship.id);
      image.alt = "";
      const copy = element("span");
      copy.append(element("strong", undefined, ship.name), element("small", undefined, `${ship.className} · ${ship.rarity}`));
      card.append(image, copy, statusBadge(ship.enabled ? "ENABLED" : "DISABLED", ship.enabled ? "good" : "warn"));
      card.addEventListener("click", () => {
        this.selectedShipId = ship.id;
        this.navigate(`${ADMIN_BASE}/ships`);
      });
      shipList.append(card);
    }
    listPanel.append(shipList);

    const ship = ships.find((candidate) => candidate.id === this.selectedShipId) ?? ships[0];
    const editorPanel = panel("Ship Editor", ship === undefined ? "No ship selected" : `${ship.id} · UI draft`, true);
    if (ship !== undefined) editorPanel.append(this.renderShipEditor(ship));
    layout.append(listPanel, editorPanel);
    page.append(layout);
    return page;
  }

  private renderShipEditor(ship: ShipMock): HTMLElement {
    const editor = element("div", "st-admin-ship-editor");
    const form = element("div");
    const fields = element("div", "st-admin-form-grid");
    fields.append(
      this.textField("Ship ID", ship.id),
      this.textField("Name", ship.name),
      this.textField("Class", ship.className),
      this.textField("Rarity", ship.rarity),
      this.textField("Unlock", ship.unlock),
      this.textField("Price", ship.price),
    );
    form.append(fields);

    const statsSection = element("section", "st-admin-form-section");
    statsSection.append(element("h3", undefined, "Base Stats"));
    const stats = element("div", "st-admin-stat-grid");
    for (const [label, value] of [
      ["HP", ship.hp], ["Shield", ship.shield], ["Armor", ship.armor], ["Speed", ship.speed], ["Fire Rate", ship.fireRate], ["Damage", ship.damage],
    ] as const) {
      const stat = element("div", "st-admin-stat");
      stat.append(element("span", undefined, label), element("strong", undefined, String(value)));
      stats.append(stat);
    }
    statsSection.append(stats);

    const visualSection = element("section", "st-admin-form-section");
    visualSection.append(element("h3", undefined, "Visual & Combat Presentation"));
    const visual = element("div", "st-admin-form-grid");
    for (const [label, value] of [
      ["3D Model", `${ship.id}/color.webp`],
      ["Projectile", "vanguard-bolt"],
      ["Trail VFX", "cyan-engine-trail"],
      ["Hit VFX", "impact-cyan"],
      ["Explosion", "ship-explosion-medium"],
      ["Engine SFX", "engine-standard"],
    ]) visual.append(this.textField(label, value));
    visualSection.append(visual);
    form.append(statsSection, visualSection);

    const preview = element("div", "st-admin-ship-preview");
    const image = element("img") as HTMLImageElement;
    image.src = shipImageUrl(ship.id);
    image.alt = `${ship.name} preview`;
    preview.append(image, element("h3", undefined, ship.name), element("p", undefined, `${ship.className} · ${ship.rarity} · ${ship.enabled ? "Enabled" : "Disabled"}`));
    const previewActions = element("div", "st-admin-page-actions");
    previewActions.style.marginTop = "14px";
    previewActions.style.marginLeft = "0";
    previewActions.append(button("Transparent", () => undefined), button("Hangar", () => undefined), button("Gameplay", () => undefined));
    preview.append(previewActions);
    editor.append(form, preview);
    return editor;
  }

  private textField(label: string, value: string): HTMLElement {
    const field = element("div", "st-admin-field");
    const input = element("input") as HTMLInputElement;
    input.value = value;
    field.append(element("label", undefined, label), input);
    return field;
  }

  private renderPlanned(path: string): HTMLElement {
    const item = NAV_GROUPS.flatMap((group) => group.items).find((candidate) => candidate.path === path);
    const page = element("div");
    page.append(pageHeader(
      "Space Typing Admin · UI Roadmap",
      item?.label ?? "Planned Screen",
      "Route chưa có renderer UI. Đây là fallback guard; toàn bộ route trong master plan phải được render trước khi UI phase được coi là hoàn tất.",
      [statusBadge("PLANNED", "warn")],
    ));
    const planned = panel(undefined, undefined, true);
    planned.classList.add("st-admin-planned");
    const box = element("div", "st-admin-planned-box");
    box.append(element("div", "st-admin-planned-icon", item?.icon ?? "ST"), element("h2", undefined, item?.label ?? "Planned"), element("p", undefined, "Giữ route và vị trí navigation ngay từ đầu để review toàn bộ cấu trúc Admin, nhưng không giả lập tính năng chưa thiết kế xong. Sau khi Overview, Audio, Music Library, World Music và Ships được chốt, pattern sẽ được mở rộng sang màn này."));
    const statusRow = element("div", "st-admin-env-row");
    statusRow.style.justifyContent = "center";
    statusRow.append(statusBadge("HOLO COMMAND", "info"), statusBadge("UI ONLY", "warn"));
    box.append(statusRow);
    planned.append(box);
    page.append(planned);
    return page;
  }
}

void READY_PATHS;
