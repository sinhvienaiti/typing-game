import { listEnglishActivities } from "../../../shared/english-content/capabilities.mjs";
import {
  publishedEnglishActivityCount,
  type RichPracticeGameId,
} from "./activity-session";

type Game = {
  id: string;
  name: string;
  path: string;
};

type StartActivity = (
  gameId: RichPracticeGameId,
  activity: string,
  limit: number,
) => Promise<void>;

const CAPABILITY_ID: Record<RichPracticeGameId, string> = {
  "recall-typing": "recall",
  "vocab-shooter": "shooter",
  "karaoke-typing": "karaoke",
  "space-typing": "space",
};
const GAME_ORDER: RichPracticeGameId[] = [
  "karaoke-typing",
  "space-typing",
  "recall-typing",
  "vocab-shooter",
];
const ACTIVITY_LABELS: Record<string, string> = {
  vocabulary: "Vocabulary",
  collocation: "Collocations",
  "phrasal-verb": "Phrasal verbs",
  chunk: "Chunks",
  idiom: "Idioms",
  "verb-pattern": "Verb patterns",
  "grammar-topic": "Grammar lesson",
  "grammar-challenge": "Grammar challenge",
  "example-typing": "Example typing",
  "listening-typing": "Listening typing",
  translation: "Vietnamese → English",
  cloze: "Cloze",
  "error-correction": "Error correction",
  "sentence-building": "Sentence building",
  transformation: "Sentence transformation",
  "contextual-usage": "Contextual usage",
  dialogue: "Dialogue typing",
};

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

export class EnglishPracticePage {
  readonly #games: Game[];
  readonly #start: StartActivity;

  constructor(games: Game[], start: StartActivity) {
    this.#games = games;
    this.#start = start;
  }

  render(): HTMLElement {
    const main = element("main", "review-page english-practice-page");
    const header = element("header", "review-flow-heading");
    const heading = element("div");
    heading.append(
      element("div", "review-eyebrow", "PUBLISHED ENGLISH CONTENT"),
      element("h1", undefined, "English Practice"),
      element(
        "p",
        undefined,
        "Launch reviewed content in the game whose UX fits the activity. Draft and candidate records are excluded automatically.",
      ),
    );
    header.append(heading);

    const card = element(
      "section",
      "review-builder-card english-practice-card",
    );
    card.append(element("h2", undefined, "Choose a game and activity"));

    const grid = element(
      "div",
      "review-builder-grid english-practice-grid",
    );
    const gameField = element("label", "review-builder-field");
    gameField.append(element("span", undefined, "Game"));
    const gameSelect = document.createElement("select");
    for (const id of GAME_ORDER) {
      const game = this.#games.find((item) => item.id === id);
      if (game === undefined) continue;
      const option = document.createElement("option");
      option.value = id;
      option.textContent = game.name;
      gameSelect.append(option);
    }
    gameField.append(gameSelect);

    const activityField = element("label", "review-builder-field");
    activityField.append(element("span", undefined, "Activity"));
    const activitySelect = document.createElement("select");
    activityField.append(activitySelect);

    const countField = element("label", "review-builder-field");
    countField.append(element("span", undefined, "Items"));
    const countSelect = document.createElement("select");
    for (const count of [5, 10, 20, 40, 100]) {
      const option = document.createElement("option");
      option.value = String(count);
      option.textContent = String(count);
      option.selected = count === 20;
      countSelect.append(option);
    }
    countField.append(countSelect);

    const availability = element(
      "div",
      "english-practice-availability",
      "Checking published content…",
    );
    const start = element(
      "button",
      "review-primary",
      "Start English Practice",
    );
    start.type = "button";
    start.disabled = true;

    grid.append(gameField, activityField, countField);
    card.append(grid, availability, start);

    const note = element(
      "section",
      "review-quick-start english-practice-note",
    );
    const noteCopy = element("div");
    noteCopy.append(
      element(
        "strong",
        undefined,
        "One content library · game-specific practice",
      ),
      element(
        "span",
        undefined,
        "Recall/Shooter focus on words and phrases, Karaoke on sentences/listening/translation, and Space on combat-friendly phrase or grammar challenges.",
      ),
    );
    note.append(noteCopy);

    let refreshToken = 0;
    const selectedGame = (): RichPracticeGameId =>
      gameSelect.value as RichPracticeGameId;

    const populateActivities = (): void => {
      activitySelect.replaceChildren();
      const capability = CAPABILITY_ID[selectedGame()];
      for (const activity of listEnglishActivities(capability)) {
        const option = document.createElement("option");
        option.value = activity;
        option.textContent = ACTIVITY_LABELS[activity] ?? activity;
        activitySelect.append(option);
      }
    };

    const refreshAvailability = async (): Promise<void> => {
      const token = ++refreshToken;
      start.disabled = true;
      availability.classList.remove("available", "unavailable");
      availability.textContent = "Checking published content…";
      const gameId = selectedGame();
      const activity = activitySelect.value;
      if (activity === "") {
        availability.textContent =
          "No activity is configured for this game.";
        availability.classList.add("unavailable");
        return;
      }
      try {
        const count = await publishedEnglishActivityCount(
          gameId,
          activity,
        );
        if (token !== refreshToken) return;
        if (count === 0) {
          availability.textContent =
            "0 published records · this activity stays locked until its quality gate passes.";
          availability.classList.add("unavailable");
          return;
        }
        availability.textContent =
          String(count) +
          " published record" +
          (count === 1 ? "" : "s") +
          " available · runtime-only, candidate content excluded.";
        availability.classList.add("available");
        start.disabled = false;
      } catch (error) {
        if (token !== refreshToken) return;
        availability.textContent =
          error instanceof Error
            ? error.message
            : "Could not read English content.";
        availability.classList.add("unavailable");
      }
    };

    gameSelect.addEventListener("change", () => {
      populateActivities();
      void refreshAvailability();
    });
    activitySelect.addEventListener("change", () => {
      void refreshAvailability();
    });
    start.addEventListener("click", () => {
      const gameId = selectedGame();
      const activity = activitySelect.value;
      const limit = Number(countSelect.value);
      start.disabled = true;
      start.textContent = "Preparing published content…";
      void this.#start(gameId, activity, limit).catch(
        (error: unknown) => {
          start.disabled = false;
          start.textContent = "Start English Practice";
          availability.textContent =
            error instanceof Error
              ? error.message
              : "Could not start English Practice.";
          availability.classList.add("unavailable");
        },
      );
    });

    populateActivities();
    void refreshAvailability();
    main.append(header, card, note);
    return main;
  }
}
