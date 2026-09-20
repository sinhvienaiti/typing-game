import "./styles.css";

type Game = { id: string; name: string; description: string; path: string; appUrl: string; icon: string };
type Registry = { games: Game[] };

const appElement = document.querySelector<HTMLDivElement>("#app");
if (appElement === null) throw new Error("#app not found");
const app: HTMLDivElement = appElement;

const response = await fetch("/games.json", { cache: "no-store" });
if (!response.ok) throw new Error("Could not load game registry");
const registry = (await response.json()) as Registry;

for (const game of registry.games) {
  const origin = new URL(game.appUrl).origin;
  if (document.head.querySelector(`link[data-game-origin="${origin}"]`) !== null) {
    continue;
  }

  const link = document.createElement("link");
  link.rel = "preconnect";
  link.href = origin;
  link.dataset["gameOrigin"] = origin;
  document.head.append(link);
}

function navigate(path: string): void {
  if (location.pathname !== path) history.pushState({}, "", path);
  render();
}

function makeButton(label: string, path: string): HTMLButtonElement {
  const button = document.createElement("button");
  button.className = "nav-game";
  button.textContent = label;
  if ((location.pathname.replace(/\/$/, "") || "/") === path) button.classList.add("active");
  button.addEventListener("click", () => navigate(path));
  return button;
}

function renderShell(content: HTMLElement): void {
  app.replaceChildren();
  const shell = document.createElement("div");
  shell.className = "portal-shell";
  const nav = document.createElement("nav");
  nav.className = "global-nav";
  const brand = document.createElement("button");
  brand.className = "brand";
  brand.textContent = "⌨ typing games";
  brand.addEventListener("click", () => navigate("/"));
  const links = document.createElement("div");
  links.className = "nav-links";
  links.append(makeButton("Home", "/"));
  for (const game of registry.games) links.append(makeButton(game.name, game.path));
  nav.append(brand, links);
  shell.append(nav, content);
  app.append(shell);
}

function renderHome(): void {
  const main = document.createElement("main");
  main.className = "home";
  const hero = document.createElement("section");
  hero.className = "hero";
  hero.innerHTML = '<div class="eyebrow">LOCAL LEARNING ARCADE</div><h1>Choose a game.<br><span>Keep typing.</span></h1><p>Independent games, one clean local portal.</p>';
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
  renderShell(main);
}

function renderGame(game: Game): void {
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

  frame.addEventListener(
    "load",
    () => {
      frame.classList.remove("loading");
      loading.classList.add("done");
      window.setTimeout(() => loading.remove(), 180);
    },
    { once: true },
  );

  stage.append(frame, loading);
  renderShell(stage);
}

function render(): void {
  const path = location.pathname.replace(/\/$/, "") || "/";
  if (path === "/") return renderHome();
  const game = registry.games.find((item) => item.path === path);
  if (game !== undefined) return renderGame(game);
  const missing = document.createElement("main");
  missing.className = "not-found";
  missing.innerHTML = "<h1>Game not found</h1><p>The requested game is not registered.</p>";
  renderShell(missing);
}

window.addEventListener("popstate", render);
render();
