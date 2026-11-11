import { listEnglishActivities } from "../../../shared/english-content/capabilities.mjs";
import {
  evaluateGuidedPracticeAnswer,
  listPublishedTopicPacks,
  loadGuidedActivityItems,
  loadResolvedTopicPack,
  publishedEnglishActivityCount,
  recordGuidedPracticeOutcome,
  type GuidedPracticeItem,
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
  options?: { cefr?: string; seed?: number },
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
const CEFR_OPTIONS = ["", "A1", "A2", "B1", "B2", "C1", "C2"] as const;
const GUIDED_ACTIVITIES = [
  { id: "contextual-usage", label: "Contextual usage" },
  { id: "sentence-building", label: "Sentence building" },
  { id: "translation", label: "Vietnamese → English (multi-answer & guided)" },
  { id: "transformation", label: "Sentence transformation (multi-answer)" },
  { id: "cloze", label: "Cloze grammar & lexis" },
  { id: "error-correction", label: "Error correction" },
  { id: "collocation", label: "Collocation recall" },
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
      element("div", "review-eyebrow", "PUBLISHED ENGLISH CONTENT · V2.1 INDEXED"),
      element("h1", undefined, "English Practice"),
      element(
        "p",
        undefined,
        "O(1) indexed content selection by CEFR and random seed across published records, plus multi-answer guided Topic Packs.",
      ),
    );
    header.append(heading);

    // Card 1: Game Launcher (uses indexed availability + CEFR + fresh seed)
    const card = element(
      "section",
      "review-builder-card english-practice-card",
    );
    card.append(element("h2", undefined, "Launch in an integrated game"));

    const grid = element(
      "div",
      "review-builder-grid english-practice-grid english-practice-grid-v2",
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

    const cefrField = element("label", "review-builder-field");
    cefrField.append(element("span", undefined, "CEFR"));
    const cefrSelect = document.createElement("select");
    for (const lvl of CEFR_OPTIONS) {
      const option = document.createElement("option");
      option.value = lvl;
      option.textContent = lvl === "" ? "All CEFR" : lvl;
      cefrSelect.append(option);
    }
    cefrField.append(cefrSelect);

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

    const orderField = element("label", "review-builder-field");
    orderField.append(element("span", undefined, "Selection"));
    const orderSelect = document.createElement("select");
    const optFresh = document.createElement("option");
    optFresh.value = "random";
    optFresh.textContent = "Fresh random slice";
    optFresh.selected = true;
    const optSeq = document.createElement("option");
    optSeq.value = "sequential";
    optSeq.textContent = "Starter slice";
    orderSelect.append(optFresh, optSeq);
    orderField.append(orderSelect);

    const availability = element(
      "div",
      "english-practice-availability",
      "Checking indexed content…",
    );
    const start = element(
      "button",
      "review-primary",
      "Start English Practice",
    );
    start.type = "button";
    start.disabled = true;

    grid.append(gameField, activityField, cefrField, countField, orderField);
    card.append(grid, availability, start);

    // Card 2: Portal Guided Multi-Answer & Topic Pack Practice (v2)
    const guidedCard = element(
      "section",
      "review-builder-card english-practice-card english-guided-card",
    );
    guidedCard.append(
      element("h2", undefined, "Topic Packs & Multi-Answer Guided Practice (v2)"),
    );
    const guidedGrid = element("div", "review-builder-grid english-practice-grid");
    const sourceField = element("label", "review-builder-field");
    sourceField.append(element("span", undefined, "Topic Pack or Activity"));
    const sourceSelect = document.createElement("select");
    for (const act of GUIDED_ACTIVITIES) {
      const opt = document.createElement("option");
      opt.value = "activity:" + act.id;
      opt.textContent = act.label;
      sourceSelect.append(opt);
    }
    sourceField.append(sourceSelect);

    const guidedCefrField = element("label", "review-builder-field");
    guidedCefrField.append(element("span", undefined, "CEFR Filter"));
    const guidedCefrSelect = document.createElement("select");
    for (const lvl of CEFR_OPTIONS) {
      const opt = document.createElement("option");
      opt.value = lvl;
      opt.textContent = lvl === "" ? "All CEFR" : lvl;
      guidedCefrSelect.append(opt);
    }
    guidedCefrField.append(guidedCefrSelect);

    const guidedCountField = element("label", "review-builder-field");
    guidedCountField.append(element("span", undefined, "Items"));
    const guidedCountSelect = document.createElement("select");
    for (const count of [5, 10, 20]) {
      const opt = document.createElement("option");
      opt.value = String(count);
      opt.textContent = String(count);
      opt.selected = count === 10;
      guidedCountSelect.append(opt);
    }
    guidedCountField.append(guidedCountSelect);

    const startGuidedBtn = element("button", "review-primary", "Start Guided Session");
    startGuidedBtn.type = "button";

    const runnerBox = element("div", "english-guided-runner");
    runnerBox.hidden = true;
    const runnerMeta = element("div", "english-guided-meta");
    const runnerPrompt = element("div", "english-guided-prompt");
    const runnerSub = element("div", "english-guided-sub");
    const answerInput = document.createElement("input");
    answerInput.type = "text";
    answerInput.className = "english-guided-input";
    answerInput.placeholder = "Type your English answer and press Enter…";

    const actionRow = element("div", "english-guided-actions");
    const checkBtn = element("button", "review-primary", "Check Answer");
    checkBtn.type = "button";
    const selfPassBtn = element("button", "review-secondary", "Mark Valid");
    selfPassBtn.type = "button";
    selfPassBtn.hidden = true;
    const selfRetryBtn = element("button", "review-secondary", "Mark Needs Practice");
    selfRetryBtn.type = "button";
    selfRetryBtn.hidden = true;
    const nextBtn = element("button", "review-secondary", "Next →");
    nextBtn.type = "button";
    nextBtn.hidden = true;
    actionRow.append(checkBtn, selfPassBtn, selfRetryBtn, nextBtn);

    const feedbackBox = element("div", "english-guided-feedback");
    runnerBox.append(runnerMeta, runnerPrompt, runnerSub, answerInput, actionRow, feedbackBox);

    guidedGrid.append(sourceField, guidedCefrField, guidedCountField);
    guidedCard.append(guidedGrid, startGuidedBtn, runnerBox);

    const note = element(
      "section",
      "review-quick-start english-practice-note",
    );
    const noteCopy = element("div");
    noteCopy.append(
      element(
        "strong",
        undefined,
        "Root runtime optimized (v2.1) · Child game submodules unchanged",
      ),
      element(
        "span",
        undefined,
        "Counts & slices load from bucketed shared/indexes/. Topic Packs & multi-answer guided checks run directly above; game submodule updates (e.g. Monkeytype crawler) are documented in docs/CLAUDE_GAME_SUBMODULES_HANDOFF.md.",
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
      availability.textContent = "Checking indexed content…";
      const gameId = selectedGame();
      const activity = activitySelect.value;
      const cefr = cefrSelect.value;
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
          cefr === "" ? undefined : cefr,
        );
        if (token !== refreshToken) return;
        if (count === 0) {
          availability.textContent =
            "0 published records for this filter · choose another CEFR or activity.";
          availability.classList.add("unavailable");
          return;
        }
        availability.textContent =
          String(count) +
          " published record" +
          (count === 1 ? "" : "s") +
          (cefr === "" ? "" : " (" + cefr + ")") +
          " · indexed selection, drafts excluded.";
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

    // Load published Topic Packs into guided selector asynchronously
    void listPublishedTopicPacks()
      .then((packs) => {
        if (packs.length === 0) return;
        const divider = document.createElement("optgroup");
        divider.label = "Curated Topic Packs (v2)";
        for (const pack of packs) {
          const opt = document.createElement("option");
          opt.value = "pack:" + pack.id;
          opt.textContent = `${pack.title} (${pack.cefr.join("/")} · ${pack.itemCount} items)`;
          divider.append(opt);
        }
        sourceSelect.prepend(divider);
        sourceSelect.selectedIndex = 0;
      })
      .catch(() => {
        // Packs manifest optional if empty
      });

    // Guided Practice Runner State
    let guidedItems: GuidedPracticeItem[] = [];
    let guidedIdx = 0;
    let guidedStartedAt = 0;
    let guidedEvaluated = false;

    const renderGuidedItem = (): void => {
      const item = guidedItems[guidedIdx];
      if (item === undefined) {
        runnerMeta.textContent = "Session Complete";
        runnerPrompt.textContent = `Finished all ${guidedItems.length} item(s).`;
        runnerSub.textContent = "Semantic skill evidence saved separately from typing speed.";
        answerInput.hidden = true;
        checkBtn.hidden = true;
        selfPassBtn.hidden = true;
        selfRetryBtn.hidden = true;
        nextBtn.hidden = true;
        feedbackBox.textContent = "";
        return;
      }
      guidedEvaluated = false;
      guidedStartedAt = performance.now();
      answerInput.hidden = false;
      answerInput.disabled = false;
      answerInput.value = "";
      checkBtn.hidden = false;
      checkBtn.disabled = false;
      selfPassBtn.hidden = true;
      selfRetryBtn.hidden = true;
      nextBtn.hidden = true;
      feedbackBox.className = "english-guided-feedback";
      feedbackBox.textContent = "";
      runnerMeta.textContent =
        `${guidedIdx + 1} / ${guidedItems.length} · ${item.activity}` +
        (item.cefr !== undefined ? ` · ${item.cefr}` : "") +
        (item.stage !== undefined ? ` · stage: ${item.stage}` : "") +
        ` · skill: ${item.learningFocus}`;
      runnerPrompt.textContent = item.promptText;
      runnerSub.textContent =
        item.secondaryText ??
        (item.acceptedAnswers.length > 1
          ? `${item.acceptedAnswers.length} accepted answers supported`
          : "");
      answerInput.focus();
    };

    const submitGuided = async (): Promise<void> => {
      const item = guidedItems[guidedIdx];
      if (item === undefined || guidedEvaluated) return;
      const userAnswer = answerInput.value;
      if (userAnswer.trim() === "") {
        feedbackBox.className = "english-guided-feedback incorrect";
        feedbackBox.textContent = "Please type an answer first.";
        return;
      }
      const evaluation = evaluateGuidedPracticeAnswer(item, userAnswer);
      const elapsed = performance.now() - guidedStartedAt;
      guidedEvaluated = true;
      answerInput.disabled = true;
      checkBtn.disabled = true;

      await recordGuidedPracticeOutcome({
        item,
        evaluation,
        userAnswer,
        responseMs: elapsed,
      });

      if (evaluation.outcome === "correct") {
        feedbackBox.className = "english-guided-feedback correct";
        feedbackBox.textContent = `Correct! Matched: "${evaluation.matchedAnswer ?? item.acceptedAnswers[0]}"`;
        nextBtn.hidden = false;
      } else if (evaluation.outcome === "needs-review") {
        feedbackBox.className = "english-guided-feedback needs-review";
        feedbackBox.textContent =
          `Open-ended / Needs Review (not scored wrong). Reference answer: "${item.acceptedAnswers[0]}"`;
        selfPassBtn.hidden = false;
        selfRetryBtn.hidden = false;
        nextBtn.hidden = false;
      } else {
        feedbackBox.className = "english-guided-feedback incorrect";
        feedbackBox.textContent =
          `Not matched (${evaluation.reasonCode ?? "mismatch"}). Accepted: ${item.acceptedAnswers.join(" | ")}`;
        nextBtn.hidden = false;
      }
    };

    checkBtn.addEventListener("click", () => {
      void submitGuided();
    });
    answerInput.addEventListener("keydown", (event) => {
      if (event.key === "Enter") {
        event.preventDefault();
        if (!guidedEvaluated) void submitGuided();
        else if (!nextBtn.hidden) {
          guidedIdx++;
          renderGuidedItem();
        }
      }
    });
    selfPassBtn.addEventListener("click", () => {
      const item = guidedItems[guidedIdx];
      if (item === undefined) return;
      const evalRef = evaluateGuidedPracticeAnswer(item, answerInput.value);
      void recordGuidedPracticeOutcome({
        item,
        evaluation: evalRef,
        userAnswer: answerInput.value,
        responseMs: performance.now() - guidedStartedAt,
        overrideOutcome: "correct",
      }).then(() => {
        guidedIdx++;
        renderGuidedItem();
      });
    });
    selfRetryBtn.addEventListener("click", () => {
      const item = guidedItems[guidedIdx];
      if (item === undefined) return;
      const evalRef = evaluateGuidedPracticeAnswer(item, answerInput.value);
      void recordGuidedPracticeOutcome({
        item,
        evaluation: evalRef,
        userAnswer: answerInput.value,
        responseMs: performance.now() - guidedStartedAt,
        overrideOutcome: "incorrect",
      }).then(() => {
        guidedIdx++;
        renderGuidedItem();
      });
    });
    nextBtn.addEventListener("click", () => {
      guidedIdx++;
      renderGuidedItem();
    });

    startGuidedBtn.addEventListener("click", () => {
      const target = sourceSelect.value;
      const cefr = guidedCefrSelect.value;
      const limit = Number(guidedCountSelect.value);
      startGuidedBtn.disabled = true;
      startGuidedBtn.textContent = "Loading…";
      void (async () => {
        if (target.startsWith("pack:")) {
          const loaded = await loadResolvedTopicPack(target.slice(5));
          guidedItems = loaded?.items ?? [];
        } else {
          const activity = target.slice("activity:".length);
          guidedItems = await loadGuidedActivityItems(activity, {
            limit,
            ...(cefr === "" ? {} : { cefr }),
            seed: Date.now(),
          });
        }
        guidedIdx = 0;
        runnerBox.hidden = false;
        renderGuidedItem();
      })()
        .catch((err: unknown) => {
          runnerBox.hidden = false;
          feedbackBox.className = "english-guided-feedback incorrect";
          feedbackBox.textContent =
            err instanceof Error ? err.message : "Could not load guided items.";
        })
        .finally(() => {
          startGuidedBtn.disabled = false;
          startGuidedBtn.textContent = "Start Guided Session";
        });
    });

    gameSelect.addEventListener("change", () => {
      populateActivities();
      void refreshAvailability();
    });
    activitySelect.addEventListener("change", () => {
      void refreshAvailability();
    });
    cefrSelect.addEventListener("change", () => {
      void refreshAvailability();
    });
    start.addEventListener("click", () => {
      const gameId = selectedGame();
      const activity = activitySelect.value;
      const limit = Number(countSelect.value);
      const cefr = cefrSelect.value;
      const seed = orderSelect.value === "random" ? Date.now() : undefined;
      start.disabled = true;
      start.textContent = "Preparing indexed content…";
      void this.#start(gameId, activity, limit, {
        ...(cefr === "" ? {} : { cefr }),
        ...(seed === undefined ? {} : { seed }),
      }).catch((error: unknown) => {
        start.disabled = false;
        start.textContent = "Start English Practice";
        availability.textContent =
          error instanceof Error
            ? error.message
            : "Could not start English Practice.";
        availability.classList.add("unavailable");
      });
    });

    populateActivities();
    void refreshAvailability();
    main.append(header, card, guidedCard, note);
    return main;
  }
}
