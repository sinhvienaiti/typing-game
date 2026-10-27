import "./styles.css";
import { SpaceTypingAdmin } from "./admin/space-typing";
import { ParentLearningBridge } from "./learning/bridge";
import { SharedMusicPlayer } from "./music";
import { SmartReviewDashboard } from "./review/dashboard";
import { SmartReviewFlow } from "./review/session";
import { LearningMaintenancePage } from "./review/maintenance";
import {
  clearPendingMonkeyReview,
  postPendingMonkeyReview,
  queueMonkeyReview,
  readPendingMonkeyReview,
} from "./review/monkey-adapter";
import {
  clearPendingRecallReview,
  postPendingRecallReview,
  queueRecallReview,
  readPendingRecallReview,
} from "./review/recall-adapter";
import {
  clearPendingShooterReview,
  postPendingShooterReview,
  queueShooterReview,
  readPendingShooterReview,
} from "./review/shooter-adapter";
import {
  clearPendingSpaceReview,
  postPendingSpaceReview,
  queueSpaceReview,
  readPendingSpaceReview,
} from "./review/space-adapter";
import {
  clearPendingKaraokeReview,
  postPendingKaraokeReview,
  queueKaraokeReview,
  readPendingKaraokeReview,
} from "./review/karaoke-adapter";
import {
  cancelMixedReviewSegmentStart,
  recordMixedLearningEvent,
} from "./review/mixed";
import type { LearningEvent } from "../../shared/learning/core.mjs";
import type { ReviewPlan } from "../../shared/learning/review-session.mjs";
import {
  pendingReviewAction,
  shouldAbandonReviewOnRouteChange,
} from "../../shared/learning/review-lifecycle.mjs";

type Game = {
  id: string;
  name: string;
  description: string;
  path: string;
  appUrl: string;
  icon: string;
  group?: string;
};

type Registry = {
  games: Game[];
};

type NavGroup = {
  id: string;
  label: string;
  element: HTMLDivElement;
  toggle: HTMLButtonElement;
  current: HTMLSpanElement;
  menu: HTMLDivElement;
  paths: Map<string, string>;
};

const NAV_GROUP_LABELS: ReadonlyArray<readonly [string, string]> = [
  ["practice", "Luyện gõ"],
  ["battle", "Game chiến đấu"],
];
const FALLBACK_NAV_GROUP: readonly [string, string] = ["other", "Khác"];

const appElement = document.querySelector<HTMLDivElement>("#app");
if (appElement === null) throw new Error("#app not found");
const app = appElement;

const response = await fetch("/games.json", { cache: "no-store" });
if (!response.ok) throw new Error("Could not load game registry");
const registry = (await response.json()) as Registry;
const gameOrigins = new Set(registry.games.map((game) => new URL(game.appUrl).origin));

for (const origin of gameOrigins) {
  if (document.head.querySelector(`link[data-game-origin="${origin}"]`) !== null) {
    continue;
  }

  const link = document.createElement("link");
  link.rel = "preconnect";
  link.href = origin;
  link.dataset["gameOrigin"] = origin;
  document.head.append(link);
}

const shell = document.createElement("div");
shell.className = "portal-shell";

const nav = document.createElement("nav");
nav.className = "global-nav";

const brand = document.createElement("button");
brand.className = "brand";
brand.textContent = "⌨ typing games";

const links = document.createElement("div");
links.className = "nav-links";

const routeHost = document.createElement("div");
routeHost.className = "route-host";

const music = new SharedMusicPlayer();
const navButtons = new Map<string, HTMLButtonElement>();
let currentFrame: HTMLIFrameElement | null = null;
let currentGame: Game | null = null;
let currentReviewStatus: HTMLDivElement | null = null;
function handlePersistedLearningEvent(event: LearningEvent): void {
  const result = recordMixedLearningEvent(event);
  if (!result.matched || !result.segmentCompleted) return;

  if (currentReviewStatus !== null) {
    currentReviewStatus.hidden = false;
    currentReviewStatus.textContent = result.sessionCompleted
      ? "Mixed Review complete · returning to session"
      : "Segment complete · loading next Mixed Review activity";
  }

  window.setTimeout(() => {
    navigate("/review/session");
  }, 250);
}

const learningBridge = new ParentLearningBridge(
  undefined,
  handlePersistedLearningEvent,
);
const reviewDashboard = new SmartReviewDashboard(navigate);
const reviewFlow = new SmartReviewFlow(navigate, startReview);
const learningMaintenance = new LearningMaintenancePage(navigate);
const spaceTypingAdmin = new SpaceTypingAdmin(navigate);

function normalizedPath(): string {
  return location.pathname.replace(/\/$/, "") || "/";
}

function clearPendingReviewForGame(
  gameId: string,
  requestId?: string,
): void {
  if (gameId === "monkeytype") {
    clearPendingMonkeyReview(requestId);
  } else if (gameId === "recall-typing") {
    clearPendingRecallReview(requestId);
  } else if (gameId === "vocab-shooter") {
    clearPendingShooterReview(requestId);
  } else if (gameId === "space-typing") {
    clearPendingSpaceReview(requestId);
  } else if (gameId === "karaoke-typing") {
    clearPendingKaraokeReview(requestId);
  }
}

function navigate(path: string): void {
  if (normalizedPath() !== path) history.pushState({}, "", path);
  renderRoute();
}

async function startReview(plan: ReviewPlan): Promise<void> {
  if (plan.options.game === "monkeytype") {
    const monkeytype = registry.games.find((game) => game.id === "monkeytype");
    if (monkeytype === undefined) {
      throw new Error("Monkeytype is not registered in the local portal.");
    }

    await queueMonkeyReview(plan);
    navigate(monkeytype.path);
    return;
  }

  if (plan.options.game === "recall-typing") {
    const recall = registry.games.find((game) => game.id === "recall-typing");
    if (recall === undefined) {
      throw new Error("Recall Typing is not registered in the local portal.");
    }

    queueRecallReview(plan);
    navigate(recall.path);
    return;
  }

  if (plan.options.game === "vocab-shooter") {
    const shooter = registry.games.find((game) => game.id === "vocab-shooter");
    if (shooter === undefined) {
      throw new Error("Vocabulary Shooter is not registered in the local portal.");
    }

    queueShooterReview(plan);
    navigate(shooter.path);
    return;
  }

  if (plan.options.game === "space-typing") {
    const space = registry.games.find((game) => game.id === "space-typing");
    if (space === undefined) {
      throw new Error("Space Typing is not registered in the local portal.");
    }

    queueSpaceReview(plan);
    navigate(space.path);
    return;
  }

  if (plan.options.game === "karaoke-typing") {
    const karaoke = registry.games.find((game) => game.id === "karaoke-typing");
    if (karaoke === undefined) {
      throw new Error("Karaoke Typing is not registered in the local portal.");
    }

    await queueKaraokeReview(plan);
    navigate(karaoke.path);
    return;
  }

  throw new Error(
    "This review adapter is not implemented for the selected game yet.",
  );
}

function makeButton(label: string, path: string): HTMLButtonElement {
  const button = document.createElement("button");
  button.className = "nav-game";
  button.textContent = label;
  button.addEventListener("click", () => navigate(path));
  navButtons.set(path, button);
  return button;
}

function makeGameButton(game: Game): HTMLButtonElement {
  const button = document.createElement("button");
  button.className = "nav-game";
  const icon = document.createElement("span");
  icon.className = "nav-game-icon";
  icon.setAttribute("aria-hidden", "true");
  icon.textContent = game.icon;
  const label = document.createElement("span");
  label.textContent = game.name;
  button.append(icon, label);
  button.addEventListener("click", () => navigate(game.path));
  navButtons.set(game.path, button);
  return button;
}

const navGroups: NavGroup[] = [];

function closeNavMenus(except: NavGroup | null = null): void {
  for (const group of navGroups) {
    if (group === except) continue;
    group.element.classList.remove("open");
    group.toggle.setAttribute("aria-expanded", "false");
  }
}

function openNavMenu(group: NavGroup, focusFirst: boolean): void {
  closeNavMenus(group);
  group.element.classList.add("open");
  group.toggle.setAttribute("aria-expanded", "true");
  // Fixed popover so the scrollable nav row never clips it.
  const rect = group.toggle.getBoundingClientRect();
  const width = group.menu.offsetWidth;
  const left = Math.max(8, Math.min(rect.left, window.innerWidth - width - 8));
  group.menu.style.left = `${Math.round(left)}px`;
  group.menu.style.top = `${Math.round(rect.bottom + 6)}px`;
  if (focusFirst) group.menu.querySelector<HTMLButtonElement>("button")?.focus();
}

function makeNavGroup(id: string, label: string, games: Game[]): NavGroup {
  const element = document.createElement("div");
  element.className = "nav-group";
  element.dataset["group"] = id;
  element.setAttribute("role", "group");
  element.setAttribute("aria-label", label);

  const caption = document.createElement("span");
  caption.className = "nav-group-caption";
  caption.setAttribute("aria-hidden", "true");
  caption.textContent = label;

  const menuId = `nav-group-${id}`;
  const toggle = document.createElement("button");
  toggle.type = "button";
  toggle.className = "nav-group-toggle";
  toggle.setAttribute("aria-haspopup", "true");
  toggle.setAttribute("aria-expanded", "false");
  toggle.setAttribute("aria-controls", menuId);
  const toggleLabel = document.createElement("span");
  toggleLabel.className = "nav-group-label";
  toggleLabel.textContent = label;
  const current = document.createElement("span");
  current.className = "nav-group-current";
  const caret = document.createElement("span");
  caret.className = "nav-group-caret";
  caret.setAttribute("aria-hidden", "true");
  caret.textContent = "▾";
  toggle.append(toggleLabel, current, caret);

  const menu = document.createElement("div");
  menu.className = "nav-group-items";
  menu.id = menuId;

  const paths = new Map<string, string>();
  for (const game of games) {
    menu.append(makeGameButton(game));
    paths.set(game.path, game.name);
  }

  element.append(caption, toggle, menu);
  const group: NavGroup = { id, label, element, toggle, current, menu, paths };

  toggle.addEventListener("click", (event) => {
    if (element.classList.contains("open")) {
      closeNavMenus();
    } else {
      // detail 0 means keyboard activation.
      openNavMenu(group, event.detail === 0);
    }
  });
  element.addEventListener("keydown", (event) => {
    if (event.key !== "Escape" || !element.classList.contains("open")) return;
    event.preventDefault();
    closeNavMenus();
    toggle.focus();
  });

  navGroups.push(group);
  return group;
}

function groupedGames(games: Game[]): Array<[string, string, Game[]]> {
  const known = new Map(NAV_GROUP_LABELS);
  const buckets = new Map<string, Game[]>();
  for (const [id] of NAV_GROUP_LABELS) buckets.set(id, []);
  for (const game of games) {
    const id = game.group !== undefined && known.has(game.group)
      ? game.group
      : FALLBACK_NAV_GROUP[0];
    const bucket = buckets.get(id) ?? [];
    bucket.push(game);
    buckets.set(id, bucket);
  }
  const result: Array<[string, string, Game[]]> = [];
  for (const [id, items] of buckets) {
    if (items.length === 0) continue;
    result.push([id, known.get(id) ?? FALLBACK_NAV_GROUP[1], items]);
  }
  return result;
}

// Inline groups when they fit; otherwise collapse each group into a menu.
function fitNavigation(): void {
  closeNavMenus();
  nav.classList.remove("nav-compact");
  if (links.scrollWidth > links.clientWidth + 1) {
    nav.classList.add("nav-compact");
  }
}

function updateNavigation(path: string): void {
  closeNavMenus();
  for (const [buttonPath, button] of navButtons) {
    const active =
      buttonPath === "/review"
        ? path === "/review" || path.startsWith("/review/")
        : buttonPath === "/admin/space-typing"
          ? path === "/admin/space-typing" || path.startsWith("/admin/space-typing/")
          : path === buttonPath;
    button.classList.toggle("active", active);
    if (active) button.setAttribute("aria-current", "page");
    else button.removeAttribute("aria-current");
  }
  for (const group of navGroups) {
    const activeName = group.paths.get(path);
    group.toggle.classList.toggle("active", activeName !== undefined);
    group.current.textContent = activeName ?? "";
  }
}

function portalFieldHasFocus(): boolean {
  const active = document.activeElement;
  if (!(active instanceof HTMLElement)) return false;
  if (active instanceof HTMLIFrameElement) return false;
  return (
    active.isContentEditable ||
    active instanceof HTMLInputElement ||
    active instanceof HTMLTextAreaElement ||
    active instanceof HTMLSelectElement
  );
}

// Send keyboard input to the game unless the player is editing a portal field.
function focusGameFrame(frame: HTMLIFrameElement): void {
  if (frame !== currentFrame || !frame.isConnected) return;
  if (portalFieldHasFocus()) return;
  frame.focus();
}

function sendSharedMusicState(): void {
  const frameWindow = currentFrame?.contentWindow;
  if (frameWindow == null || currentGame === null) return;
  frameWindow.postMessage(
    {
      type: "typing-game:shared-music",
      playing: music.isPlaying(),
    },
    new URL(currentGame.appUrl).origin,
  );
}

music.onPlaybackChange(() => {
  sendSharedMusicState();
});

brand.addEventListener("click", () => navigate("/"));
links.append(makeButton("Home", "/"));
links.append(makeButton("Smart Review", "/review"));
links.append(makeButton("Space Admin", "/admin/space-typing"));
for (const [id, label, games] of groupedGames(registry.games)) {
  links.append(makeNavGroup(id, label, games).element);
}
nav.append(brand, links, music.element);
shell.append(nav, routeHost);
app.replaceChildren(shell);

fitNavigation();
new ResizeObserver(() => fitNavigation()).observe(nav);
void document.fonts?.ready.then(() => fitNavigation());
document.addEventListener("pointerdown", (event) => {
  const target = event.target;
  if (target instanceof Node && navGroups.some((group) => group.element.contains(target))) {
    return;
  }
  closeNavMenus();
});
document.addEventListener("focusin", (event) => {
  const target = event.target;
  if (target instanceof Node && navGroups.some((group) => group.element.contains(target))) {
    return;
  }
  closeNavMenus();
});
// Clicking into the game iframe blurs the portal window.
window.addEventListener("blur", () => closeNavMenus());
links.addEventListener("scroll", () => closeNavMenus(), { passive: true });

function renderHome(): HTMLElement {
  const main = document.createElement("main");
  main.className = "home";

  const hero = document.createElement("section");
  hero.className = "hero";
  hero.innerHTML =
    '<div class="eyebrow">LOCAL LEARNING ARCADE</div><h1>Choose a game.<br><span>Keep typing.</span></h1><p>Independent games, one clean local portal.</p>';

  const grid = document.createElement("section");
  grid.className = "game-grid";
  for (const game of registry.games) {
    const card = document.createElement("button");
    card.className = "game-card";

    const icon = document.createElement("div");
    icon.className = "game-icon";
    icon.textContent = game.icon;

    const copy = document.createElement("div");
    copy.className = "game-copy";
    const title = document.createElement("h2");
    title.textContent = game.name;
    const desc = document.createElement("p");
    desc.textContent = game.description;
    copy.append(title, desc);

    const play = document.createElement("div");
    play.className = "play";
    play.textContent = "PLAY →";

    card.append(icon, copy, play);
    card.addEventListener("click", () => navigate(game.path));
    grid.append(card);
  }

  const attribution = document.createElement("a");
  attribution.className = "data-attribution";
  attribution.href = "/vocabulary/ATTRIBUTION.md";
  attribution.target = "_blank";
  attribution.rel = "noreferrer";
  attribution.textContent = "Vocabulary data attribution";

  main.append(hero, grid, attribution);
  return main;
}

function renderGame(game: Game): HTMLElement {
  const stage = document.createElement("main");
  stage.className = "game-stage";

  const reviewStatus = document.createElement("div");
  reviewStatus.className = "game-review-status";
  reviewStatus.hidden = true;
  currentReviewStatus = reviewStatus;

  const loading = document.createElement("div");
  loading.className = "game-loading";
  loading.innerHTML =
    '<div class="game-loading-spinner" aria-hidden="true"></div><strong>Loading game...</strong><span>Preparing the local game.</span>';

  const frame = document.createElement("iframe");
  frame.className = "game-frame loading";
  frame.src = game.appUrl;
  frame.title = game.name;
  frame.allow = "autoplay; clipboard-read; clipboard-write";

  currentFrame = frame;
  currentGame = game;

  frame.addEventListener(
    "load",
    () => {
      frame.classList.remove("loading");
      loading.classList.add("done");
      sendSharedMusicState();
      focusGameFrame(frame);

      const pending =
        game.id === "monkeytype"
          ? postPendingMonkeyReview(frame, game.appUrl)
          : game.id === "recall-typing"
            ? postPendingRecallReview(frame, game.appUrl)
            : game.id === "vocab-shooter"
              ? postPendingShooterReview(frame, game.appUrl)
              : game.id === "space-typing"
                ? postPendingSpaceReview(frame, game.appUrl)
                : game.id === "karaoke-typing"
                  ? postPendingKaraokeReview(frame, game.appUrl)
                  : null;
      if (pending !== null) {
        reviewStatus.hidden = false;
        reviewStatus.textContent =
          `Starting Smart Review · ${pending.items.length} item${pending.items.length === 1 ? "" : "s"} · ${pending.goal}`;
      }

      window.setTimeout(() => loading.remove(), 180);
    },
    { once: true },
  );

  stage.append(frame, loading, reviewStatus);
  return stage;
}

function renderMissing(): HTMLElement {
  const missing = document.createElement("main");
  missing.className = "not-found";
  missing.innerHTML =
    "<h1>Game not found</h1><p>The requested game is not registered.</p>";
  return missing;
}

function renderRoute(): void {
  const path = normalizedPath();
  const previousGame = currentGame;
  if (
    previousGame !== null &&
    shouldAbandonReviewOnRouteChange(previousGame.path, path)
  ) {
    clearPendingReviewForGame(previousGame.id);
    cancelMixedReviewSegmentStart();
  }
  updateNavigation(path);

  music.setSpeechActive(false);
  currentFrame = null;
  currentGame = null;
  currentReviewStatus = null;

  if (path === "/") {
    music.setKaraokeActive(false);
    routeHost.replaceChildren(renderHome());
    return;
  }

  if (path === "/review") {
    music.setKaraokeActive(false);
    routeHost.replaceChildren(reviewDashboard.render());
    return;
  }

  if (path === "/review/data") {
    music.setKaraokeActive(false);
    routeHost.replaceChildren(learningMaintenance.render());
    return;
  }

  if (path === "/review/build") {
    music.setKaraokeActive(false);
    routeHost.replaceChildren(reviewFlow.renderBuilder());
    return;
  }

  if (path === "/review/session") {
    music.setKaraokeActive(false);
    routeHost.replaceChildren(reviewFlow.renderSession());
    return;
  }

  if (path === "/admin/space-typing" || path.startsWith("/admin/space-typing/")) {
    music.setKaraokeActive(false);
    routeHost.replaceChildren(spaceTypingAdmin.render(path));
    return;
  }

  const game = registry.games.find((item) => item.path === path);
  if (game === undefined) {
    music.setKaraokeActive(false);
    routeHost.replaceChildren(renderMissing());
    return;
  }

  music.setKaraokeActive(game.id === "karaoke-typing");
  routeHost.replaceChildren(renderGame(game));
}

window.addEventListener("message", (event: MessageEvent<unknown>) => {
  if (learningBridge.handleMessage(event, currentFrame, currentGame)) return;

  if (!gameOrigins.has(event.origin)) return;
  if (currentFrame === null || event.source !== currentFrame.contentWindow) return;
  if (event.data === null || typeof event.data !== "object") return;

  const data = event.data as Record<string, unknown>;

  if (data["type"] === "typing-game:request-focus") {
    const gameId = data["gameId"];
    if (
      currentGame !== null &&
      event.origin === new URL(currentGame.appUrl).origin &&
      (gameId === undefined || gameId === currentGame.id)
    ) {
      focusGameFrame(currentFrame);
    }
    return;
  }

  if (
    (currentGame?.id === "monkeytype" ||
      currentGame?.id === "recall-typing" ||
      currentGame?.id === "vocab-shooter" ||
      currentGame?.id === "space-typing" ||
      currentGame?.id === "karaoke-typing") &&
    (data["type"] === "typing-game:learning:v1:review-ready" ||
      data["type"] === "typing-game:learning:v1:review-error")
  ) {
    const requestId =
      typeof data["requestId"] === "string" ? data["requestId"] : undefined;
    const pending =
      currentGame.id === "monkeytype"
        ? readPendingMonkeyReview()
        : currentGame.id === "recall-typing"
          ? readPendingRecallReview()
          : currentGame.id === "vocab-shooter"
            ? readPendingShooterReview()
            : currentGame.id === "space-typing"
              ? readPendingSpaceReview()
              : readPendingKaraokeReview();
    if (
      requestId !== undefined &&
      pending !== null &&
      pending.requestId === requestId
    ) {
      const pendingAction = pendingReviewAction(data["type"]);
      if (pendingAction === "clear") {
        clearPendingReviewForGame(currentGame.id, requestId);
        cancelMixedReviewSegmentStart();
      }

      if (currentReviewStatus !== null) {
        currentReviewStatus.hidden = false;
        if (data["type"] === "typing-game:learning:v1:review-ready") {
          currentReviewStatus.textContent =
            `Smart Review ready · ${pending.items.length} item${pending.items.length === 1 ? "" : "s"}`;
          const statusToClear = currentReviewStatus;
          window.setTimeout(() => {
            if (currentReviewStatus !== statusToClear) return;
            statusToClear.remove();
            currentReviewStatus = null;
          }, 1800);
        } else {
          currentReviewStatus.classList.add("error");
          currentReviewStatus.textContent =
            typeof data["message"] === "string"
              ? `Smart Review error: ${data["message"]}`
              : "Smart Review dataset could not be applied.";
        }
      }
    }
    return;
  }

  if (data["type"] !== "typing-game:speech") return;
  if (typeof data["active"] !== "boolean") return;
  music.setSpeechActive(data["active"]);
});

window.addEventListener("pagehide", () => {
  void learningBridge.flush();
});
window.addEventListener("popstate", renderRoute);
renderRoute();
