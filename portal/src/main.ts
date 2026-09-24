import "./styles.css";
import { ParentLearningBridge } from "./learning/bridge";
import { SharedMusicPlayer } from "./music";

type Game = {
  id: string;
  name: string;
  description: string;
  path: string;
  appUrl: string;
  icon: string;
};

type Registry = {
  games: Game[];
};

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
const learningBridge = new ParentLearningBridge();

function normalizedPath(): string {
  return location.pathname.replace(/\/$/, "") || "/";
}

function navigate(path: string): void {
  if (normalizedPath() !== path) history.pushState({}, "", path);
  renderRoute();
}

function makeButton(label: string, path: string): HTMLButtonElement {
  const button = document.createElement("button");
  button.className = "nav-game";
  button.textContent = label;
  button.addEventListener("click", () => navigate(path));
  navButtons.set(path, button);
  return button;
}

function updateNavigation(path: string): void {
  for (const [buttonPath, button] of navButtons) {
    button.classList.toggle("active", path === buttonPath);
  }
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
for (const game of registry.games) {
  links.append(makeButton(game.name, game.path));
}
nav.append(brand, links, music.element);
shell.append(nav, routeHost);
app.replaceChildren(shell);

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
      window.setTimeout(() => loading.remove(), 180);
    },
    { once: true },
  );

  stage.append(frame, loading);
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
  updateNavigation(path);

  music.setSpeechActive(false);
  currentFrame = null;
  currentGame = null;

  if (path === "/") {
    music.setKaraokeActive(false);
    routeHost.replaceChildren(renderHome());
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
  if (data["type"] !== "typing-game:speech") return;
  if (typeof data["active"] !== "boolean") return;
  music.setSpeechActive(data["active"]);
});

window.addEventListener("pagehide", () => {
  void learningBridge.flush();
});
window.addEventListener("popstate", renderRoute);
renderRoute();
