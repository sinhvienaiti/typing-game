import {
  calculateMastery,
  type LearningProfile,
  type LearningRecord,
} from "../../../shared/learning/core.mjs";
import { BrowserLearningProfileStore } from "../../../shared/learning/browser-store.mjs";
import {
  queryLearningProfile,
  type LearningQueryItem,
} from "../../../shared/learning/query.mjs";
import { isAtRiskReviewItem } from "../../../shared/learning/review-session.mjs";
import {
  ReviewVocabularyRepository,
  type ReviewOption,
  type VocabularyEntry,
} from "./vocabulary";

type ReviewTab = "words" | "grammar" | "sentences";
type EntityType = "vocabulary" | "grammar" | "sentence";

type ReviewState = {
  tab: ReviewTab;
  search: string;
  status: string;
  sourceGame: string;
  dateRange: string;
  mastery: string;
  sort: string;
  page: number;
  pageSize: number;
  quick: string;
  mistakeMin: number | null;
  hintMin: number | null;
  replayMin: number | null;
  responseMsMin: number | null;
  correctStreakMax: number | null;
  topic: string;
  wordType: string;
  level: number | null;
  grammarCategory: string;
  lastSeenFrom: string;
  lastSeenTo: string;
  lastWrongFrom: string;
  lastWrongTo: string;
};

type Navigate = (url: string) => void;

const SOURCE_GAMES = [
  ["", "All Games"],
  ["monkeytype", "Monkeytype"],
  ["recall-typing", "Recall Typing"],
  ["vocab-shooter", "Vocabulary Shooter"],
  ["space-typing", "Space Typing"],
  ["karaoke-typing", "Karaoke Typing"],
] as const;

const SORT_OPTIONS = [
  ["smart-priority", "Smart Priority"],
  ["lowest-mastery", "Lowest Mastery"],
  ["most-mistakes", "Most Mistakes"],
  ["recent-mistake", "Most Recent Mistake"],
  ["oldest-review", "Oldest Review"],
  ["slowest-response", "Slowest Response"],
  ["most-attempts", "Most Attempts"],
  ["a-z", "A-Z"],
  ["z-a", "Z-A"],
] as const;

const QUICK_FILTERS = [
  ["needs-review", "Needs Review"],
  ["missed-today", "Missed Today"],
  ["slow", "Slow Words"],
  ["used-hint", "Used Hint"],
  ["not-seen-7d", "Not Seen 7d+"],
  ["at-risk", "At Risk"],
] as const;

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

function entityTypeForTab(tab: ReviewTab): EntityType {
  if (tab === "words") return "vocabulary";
  if (tab === "grammar") return "grammar";
  return "sentence";
}

function collectionFor(
  profile: LearningProfile,
  entityType: EntityType,
): Record<string, LearningRecord> {
  if (entityType === "vocabulary") return profile.vocabulary;
  if (entityType === "grammar") return profile.grammar;
  return profile.sentences;
}

function recordId(record: LearningRecord, entityType: EntityType): string {
  if (entityType === "vocabulary") return record.wordKey ?? "";
  if (entityType === "grammar") return record.grammarId ?? "";
  return record.sentenceId ?? "";
}

function safeInt(
  params: URLSearchParams,
  key: string,
  fallback: number,
): number {
  const value = Number(params.get(key));
  return Number.isInteger(value) && value >= 0 ? value : fallback;
}

function optionalPositiveInt(
  params: URLSearchParams,
  key: string,
): number | null {
  const raw = params.get(key);
  if (raw === null || raw === "") return null;
  const value = Number(raw);
  return Number.isInteger(value) && value >= 0 ? value : null;
}

function parseState(): ReviewState {
  const params = new URLSearchParams(location.search);
  const tabParam = params.get("tab");
  const tab: ReviewTab =
    tabParam === "grammar" || tabParam === "sentences" ? tabParam : "words";
  const pageSize = safeInt(params, "pageSize", 25);

  return {
    tab,
    search: params.get("q") ?? "",
    status: params.get("status") ?? "",
    sourceGame: params.get("game") ?? "",
    dateRange: params.get("date") ?? "",
    mastery: params.get("mastery") ?? "",
    sort: params.get("sort") ?? "smart-priority",
    page: Math.max(1, safeInt(params, "page", 1)),
    pageSize: [10, 25, 50, 100].includes(pageSize) ? pageSize : 25,
    quick: params.get("quick") ?? "",
    mistakeMin: optionalPositiveInt(params, "mistakes"),
    hintMin: optionalPositiveInt(params, "hints"),
    replayMin: optionalPositiveInt(params, "replays"),
    responseMsMin: optionalPositiveInt(params, "slowMs"),
    correctStreakMax: optionalPositiveInt(params, "streakMax"),
    topic: params.get("topic") ?? "",
    wordType: params.get("wordType") ?? "",
    level: optionalPositiveInt(params, "level"),
    grammarCategory: params.get("grammar") ?? "",
    lastSeenFrom: params.get("seenFrom") ?? "",
    lastSeenTo: params.get("seenTo") ?? "",
    lastWrongFrom: params.get("wrongFrom") ?? "",
    lastWrongTo: params.get("wrongTo") ?? "",
  };
}

function dateStart(daysAgo: number): string {
  const date = new Date();
  date.setHours(0, 0, 0, 0);
  date.setDate(date.getDate() - daysAgo);
  return date.toISOString();
}

function dayKey(value: string | null): string {
  if (value === null) return "";
  const date = new Date(value);
  if (!Number.isFinite(date.getTime())) return "";
  return [
    date.getFullYear(),
    String(date.getMonth() + 1).padStart(2, "0"),
    String(date.getDate()).padStart(2, "0"),
  ].join("-");
}


function matchesQuick(
  record: LearningRecord,
  quick: string,
  now: string,
): boolean {
  if (quick === "") return true;
  const mastery = calculateMastery(record, now);
  if (quick === "needs-review") return mastery < 40;
  if (quick === "missed-today") {
    return dayKey(record.lastWrongAt) === dayKey(now);
  }
  if (quick === "slow") return (record.avgResponseMs ?? 0) >= 5000;
  if (quick === "used-hint") return record.hints > 0;
  if (quick === "not-seen-7d") {
    if (record.lastSeenAt === null) return true;
    return Date.parse(now) - Date.parse(record.lastSeenAt) >= 7 * 86_400_000;
  }
  if (quick === "at-risk") {
    return isAtRiskReviewItem(
      {
        mastery,
        lastCorrectAt: record.lastCorrectAt,
        lastWrongAt: record.lastWrongAt,
      },
      now,
    );
  }
  if (quick === "due") {
    return record.nextReviewAt !== null && Date.parse(record.nextReviewAt) <= Date.parse(now);
  }
  return true;
}

function scopedProfile(
  profile: LearningProfile,
  entityType: EntityType,
  keep: (record: LearningRecord) => boolean,
): LearningProfile {
  const source = collectionFor(profile, entityType);
  const filtered = Object.fromEntries(
    Object.entries(source).filter(([, record]) => keep(record)),
  );

  if (entityType === "vocabulary") {
    return { ...profile, vocabulary: filtered };
  }
  if (entityType === "grammar") {
    return { ...profile, grammar: filtered };
  }
  return { ...profile, sentences: filtered };
}

function formatDate(value: unknown): string {
  if (typeof value !== "string" || value === "") return "—";
  const date = new Date(value);
  if (!Number.isFinite(date.getTime())) return "—";
  return new Intl.DateTimeFormat(undefined, {
    year: "numeric",
    month: "short",
    day: "numeric",
  }).format(date);
}

function formatResponse(value: unknown): string {
  return typeof value === "number" && Number.isFinite(value)
    ? `${(value / 1000).toFixed(1)}s`
    : "—";
}

function sourceLabel(source: string): string {
  return SOURCE_GAMES.find(([id]) => id === source)?.[1] ?? source;
}

function masteryLabel(mastery: number): string {
  if (mastery < 40) return "Needs Review";
  if (mastery < 70) return "Learning";
  if (mastery < 90) return "Improving";
  return "Mastered";
}

function select(
  labelText: string,
  value: string,
  options: ReadonlyArray<readonly [string, string]>,
  onChange: (value: string) => void,
): HTMLLabelElement {
  const label = element("label", "review-field");
  label.append(element("span", undefined, labelText));
  const control = document.createElement("select");
  for (const [optionValue, optionLabel] of options) {
    const option = document.createElement("option");
    option.value = optionValue;
    option.textContent = optionLabel;
    option.selected = optionValue === value;
    control.append(option);
  }
  control.addEventListener("change", () => onChange(control.value));
  label.append(control);
  return label;
}

function dateInput(
  labelText: string,
  value: string,
  onChange: (value: string) => void,
): HTMLLabelElement {
  const label = element("label", "review-field");
  label.append(element("span", undefined, labelText));
  const input = document.createElement("input");
  input.type = "date";
  input.value = value;
  input.addEventListener("change", () => onChange(input.value));
  label.append(input);
  return label;
}

function numberInput(
  labelText: string,
  value: number | null,
  placeholder: string,
  onChange: (value: string) => void,
): HTMLLabelElement {
  const label = element("label", "review-field");
  label.append(element("span", undefined, labelText));
  const input = document.createElement("input");
  input.type = "number";
  input.min = "0";
  input.placeholder = placeholder;
  input.value = value === null ? "" : String(value);
  input.addEventListener("change", () => onChange(input.value));
  label.append(input);
  return label;
}

function whyReview(item: LearningQueryItem, now: string): string[] {
  const reasons: string[] = [];
  if (item.mastery < 40) {
    reasons.push("Learning strength is currently below 40%.");
  }
  if (item.wrong > 0) {
    reasons.push(`${item.wrong} mistake${item.wrong === 1 ? "" : "s"} recorded.`);
  }
  if (typeof item.avgResponseMs === "number" && item.avgResponseMs >= 5000) {
    reasons.push(
      `Average response is ${(item.avgResponseMs / 1000).toFixed(1)} seconds.`,
    );
  }
  if (typeof item.hints === "number" && item.hints > 0) {
    reasons.push(`Hints were used ${item.hints} time${item.hints === 1 ? "" : "s"}.`);
  }
  if (typeof item.replays === "number" && item.replays > 0) {
    reasons.push(
      `Audio/replay was used ${item.replays} time${item.replays === 1 ? "" : "s"}.`,
    );
  }
  if (typeof item.lastCorrectAt === "string") {
    const days = Math.floor(
      (Date.parse(now) - Date.parse(item.lastCorrectAt)) / 86_400_000,
    );
    if (days >= 7) {
      reasons.push(`Last successful recall was ${days} days ago.`);
    }
  }
  if (
    typeof item.nextReviewAt === "string" &&
    Date.parse(item.nextReviewAt) <= Date.parse(now)
  ) {
    reasons.push("This item is due for review now.");
  }
  if (reasons.length === 0) {
    reasons.push("Smart Priority selected this item from its current learning history.");
  }
  return reasons;
}

export class SmartReviewDashboard {
  #store = new BrowserLearningProfileStore();
  #vocabulary = new ReviewVocabularyRepository();
  #navigate: Navigate;

  constructor(navigate: Navigate) {
    this.#navigate = navigate;
  }

  render(): HTMLElement {
    const main = element("main", "review-page");
    main.append(
      element("div", "review-loading", "Loading your learning profile…"),
    );
    void this.#renderInto(main).catch((error: unknown) => {
      const message =
        error instanceof Error ? error.message : "Could not load Smart Review.";
      main.replaceChildren();
      const errorBox = element("section", "review-error");
      errorBox.append(
        element("h1", undefined, "Smart Review"),
        element("p", undefined, message),
      );
      const retry = element("button", "review-primary", "Retry");
      retry.addEventListener("click", () => {
        this.#navigate(location.pathname + location.search);
      });
      errorBox.append(retry);
      main.append(errorBox);
    });
    return main;
  }

  #setParam(key: string, value: string, resetPage = true): void {
    const params = new URLSearchParams(location.search);
    if (value === "") params.delete(key);
    else params.set(key, value);
    if (resetPage && key !== "page") params.delete("page");
    const query = params.toString();
    this.#navigate(query === "" ? "/review" : `/review?${query}`);
  }

  #setNumberParam(key: string, value: string): void {
    const normalized = value.trim();
    if (normalized === "" || Number(normalized) < 0) {
      this.#setParam(key, "");
      return;
    }
    this.#setParam(key, String(Math.floor(Number(normalized))));
  }

  async #renderInto(main: HTMLElement): Promise<void> {
    const profile = await this.#store.load();
    const state = parseState();
    const now = new Date().toISOString();
    const entityType = entityTypeForTab(state.tab);
    const [topicOptions, wordTypeOptions, grammarOptions] = await Promise.all([
      entityType === "vocabulary" ? this.#vocabulary.topicOptions() : Promise.resolve([]),
      entityType === "vocabulary" ? this.#vocabulary.wordTypeOptions() : Promise.resolve([]),
      entityType === "grammar" ? this.#vocabulary.grammarOptions() : Promise.resolve([]),
    ]);

    let workingProfile = scopedProfile(
      profile,
      entityType,
      (record) => matchesQuick(record, state.quick, now),
    );

    if (
      entityType === "vocabulary" &&
      (state.topic !== "" || state.wordType !== "" || state.level !== null)
    ) {
      const learnedKeys = Object.keys(workingProfile.vocabulary);
      const allowed = await this.#vocabulary.filterLearnedKeys(learnedKeys, {
        ...(state.topic === "" ? {} : { topicId: state.topic }),
        ...(state.wordType === "" ? {} : { wordTypeId: state.wordType }),
        ...(state.level === null ? {} : { level: state.level }),
      });
      workingProfile = scopedProfile(
        workingProfile,
        entityType,
        (record) => allowed.has(record.wordKey ?? ""),
      );
    }

    if (entityType === "grammar" && state.grammarCategory !== "") {
      workingProfile = scopedProfile(
        workingProfile,
        entityType,
        (record) => record.grammarId === state.grammarCategory,
      );
    }

    let querySearch = state.search;
    if (state.search.trim() !== "") {
      const records = collectionFor(workingProfile, entityType);
      if (entityType === "vocabulary") {
        const matches = await this.#vocabulary.searchLearnedKeys(
          Object.keys(records),
          state.search,
        );
        workingProfile = scopedProfile(
          workingProfile,
          entityType,
          (record) => matches.has(record.wordKey ?? ""),
        );
        querySearch = "";
      } else {
        const search = state.search.toLocaleLowerCase();
        workingProfile = scopedProfile(
          workingProfile,
          entityType,
          (record) => {
            const id = recordId(record, entityType).toLocaleLowerCase();
            if (id.includes(search)) return true;
            if (
              entityType === "grammar" &&
              Object.keys(record.errorTypes ?? {}).some((key) =>
                key.toLocaleLowerCase().includes(search),
              )
            ) {
              return true;
            }
            return (record.recentAnswers ?? []).some((answer) => {
              const text =
                typeof answer["answer"] === "string" ? answer["answer"] : "";
              return text.toLocaleLowerCase().includes(search);
            });
          },
        );
        querySearch = "";
      }
    }

    const filters: Record<string, unknown> = {};
    if (state.status !== "") filters["status"] = state.status;
    if (state.sourceGame !== "") filters["sourceGame"] = state.sourceGame;
    if (state.dateRange === "today") filters["lastWrongFrom"] = dateStart(0);
    if (state.dateRange === "7d") filters["lastWrongFrom"] = dateStart(6);
    if (state.dateRange === "30d") filters["lastWrongFrom"] = dateStart(29);
    if (state.lastSeenFrom !== "") {
      filters["lastSeenFrom"] = new Date(`${state.lastSeenFrom}T00:00:00`).toISOString();
    }
    if (state.lastSeenTo !== "") {
      filters["lastSeenTo"] = new Date(`${state.lastSeenTo}T23:59:59.999`).toISOString();
    }
    if (state.lastWrongFrom !== "") {
      filters["lastWrongFrom"] = new Date(`${state.lastWrongFrom}T00:00:00`).toISOString();
    }
    if (state.lastWrongTo !== "") {
      filters["lastWrongTo"] = new Date(`${state.lastWrongTo}T23:59:59.999`).toISOString();
    }
    if (state.mastery === "needs") {
      filters["masteryMin"] = 0;
      filters["masteryMax"] = 39;
    } else if (state.mastery === "learning") {
      filters["masteryMin"] = 40;
      filters["masteryMax"] = 69;
    } else if (state.mastery === "improving") {
      filters["masteryMin"] = 70;
      filters["masteryMax"] = 89;
    } else if (state.mastery === "mastered") {
      filters["masteryMin"] = 90;
      filters["masteryMax"] = 100;
    }
    if (state.mistakeMin !== null) filters["mistakeMin"] = state.mistakeMin;
    if (state.hintMin !== null) filters["hintMin"] = state.hintMin;
    if (state.replayMin !== null) filters["replayMin"] = state.replayMin;
    if (state.responseMsMin !== null) {
      filters["responseMsMin"] = state.responseMsMin;
    }
    if (state.correctStreakMax !== null) {
      filters["correctStreakMax"] = state.correctStreakMax;
    }

    const result = queryLearningProfile(
      workingProfile,
      {
        entityType,
        page: state.page,
        pageSize: state.pageSize,
        search: querySearch,
        sort: state.sort,
        filters,
      },
      now,
    );

    const vocabulary =
      entityType === "vocabulary"
        ? await this.#vocabulary.getMany(result.items.map((item) => item.entityId))
        : new Map<string, VocabularyEntry>();

    main.replaceChildren();
    main.append(
      this.#renderHeader(profile, now),
      this.#renderTabs(state),
      this.#renderQuickFilters(state),
      this.#renderFilters(state, topicOptions, wordTypeOptions, grammarOptions),
      this.#renderResults(result, vocabulary, now),
    );
  }

  #renderHeader(profile: LearningProfile, now: string): HTMLElement {
    const section = element("section", "review-header");
    const heading = element("div", "review-heading");
    const copy = element("div");
    copy.append(
      element("div", "review-eyebrow", "SHARED LEARNING MEMORY"),
      element("h1", undefined, "Smart Review"),
      element(
        "p",
        undefined,
        "See what is weak, why it needs attention, and what to review next.",
      ),
    );

    const headingActions = element("div", "review-heading-actions");
    const dataButton = element("button", "review-secondary", "Learning Data");
    dataButton.addEventListener("click", () =>
      this.#navigate("/review/data"),
    );
    const start = element("button", "review-primary", "Start Smart Review");
    start.addEventListener("click", () =>
      this.#navigate("/review/build?mode=quick"),
    );
    headingActions.append(dataButton, start);
    heading.append(copy, headingActions);

    const all = [
      ...Object.values(profile.vocabulary),
      ...Object.values(profile.grammar),
      ...Object.values(profile.sentences),
    ];
    const summary = {
      needs: 0,
      improving: 0,
      mastered: 0,
      due: 0,
    };
    for (const record of all) {
      const mastery = calculateMastery(record, now);
      if (mastery < 40) summary.needs += 1;
      else if (mastery < 90) summary.improving += 1;
      else summary.mastered += 1;
      if (
        record.nextReviewAt !== null &&
        Date.parse(record.nextReviewAt) <= Date.parse(now)
      ) {
        summary.due += 1;
      }
    }

    const cards = element("div", "review-summary");
    for (const [label, value, action] of [
      ["Needs Review", summary.needs, "needs-review"],
      ["Improving", summary.improving, ""],
      ["Mastered", summary.mastered, ""],
      ["Review Today", summary.due, "due"],
    ] as const) {
      const card = element("button", "review-summary-card");
      card.append(
        element("strong", undefined, String(value)),
        element("span", undefined, label),
      );
      if (action !== "") {
        card.addEventListener("click", () => this.#setParam("quick", action));
      } else {
        card.disabled = true;
      }
      cards.append(card);
    }

    section.append(heading, cards);
    return section;
  }

  #renderTabs(state: ReviewState): HTMLElement {
    const tabs = element("div", "review-tabs");
    for (const [id, label] of [
      ["words", "Words"],
      ["grammar", "Grammar"],
      ["sentences", "Sentences"],
    ] as const) {
      const button = element("button", "review-tab", label);
      button.classList.toggle("active", state.tab === id);
      button.setAttribute("aria-pressed", String(state.tab === id));
      button.addEventListener("click", () => this.#setParam("tab", id));
      tabs.append(button);
    }
    return tabs;
  }

  #renderQuickFilters(state: ReviewState): HTMLElement {
    const wrap = element("section", "review-quick");
    wrap.append(element("span", "review-filter-label", "Quick filters"));
    const chips = element("div", "review-chips");
    for (const [id, label] of QUICK_FILTERS) {
      const button = element("button", "review-chip", label);
      button.classList.toggle("active", state.quick === id);
      button.setAttribute("aria-pressed", String(state.quick === id));
      button.addEventListener("click", () =>
        this.#setParam("quick", state.quick === id ? "" : id),
      );
      chips.append(button);
    }
    if (state.quick === "due") {
      const due = element("button", "review-chip active", "Due Now");
      due.setAttribute("aria-pressed", "true");
      due.addEventListener("click", () => this.#setParam("quick", ""));
      chips.prepend(due);
    }
    wrap.append(chips);
    return wrap;
  }

  #renderFilters(
    state: ReviewState,
    topicOptions: ReviewOption[],
    wordTypeOptions: ReviewOption[],
    grammarOptions: ReviewOption[],
  ): HTMLElement {
    const section = element("section", "review-filters");
    const searchLabel = element("label", "review-field review-search");
    searchLabel.append(element("span", undefined, "Search"));
    const search = document.createElement("input");
    search.type = "search";
    search.placeholder =
      state.tab === "words"
        ? "English or Vietnamese meaning"
        : state.tab === "grammar"
          ? "Grammar label or error type"
          : "Sentence ID or recent answer";
    search.value = state.search;
    let timer = 0;
    search.addEventListener("input", () => {
      window.clearTimeout(timer);
      timer = window.setTimeout(() => {
        const path = location.pathname.replace(/\/$/, "") || "/";
        if (!search.isConnected || path !== "/review") return;
        this.#setParam("q", search.value);
      }, 280);
    });
    searchLabel.append(search);

    const primary = element("div", "review-filter-grid");
    primary.append(
      searchLabel,
      select(
        "Status",
        state.status,
        [
          ["", "All statuses"],
          ["needs-review", "Needs Review"],
          ["learning", "Learning"],
          ["improving", "Improving"],
          ["mastered", "Mastered"],
        ],
        (value) => this.#setParam("status", value),
      ),
      select(
        "Source",
        state.sourceGame,
        SOURCE_GAMES,
        (value) => this.#setParam("game", value),
      ),
      select(
        "Last mistake",
        state.dateRange,
        [
          ["", "Any time"],
          ["today", "Today"],
          ["7d", "Last 7 days"],
          ["30d", "Last 30 days"],
        ],
        (value) => this.#setParam("date", value),
      ),
      select(
        "Mastery",
        state.mastery,
        [
          ["", "Any mastery"],
          ["needs", "0-39 Needs Review"],
          ["learning", "40-69 Learning"],
          ["improving", "70-89 Improving"],
          ["mastered", "90-100 Mastered"],
        ],
        (value) => this.#setParam("mastery", value),
      ),
      select(
        "Sort",
        state.sort,
        SORT_OPTIONS,
        (value) => this.#setParam("sort", value),
      ),
    );

    const advanced = document.createElement("details");
    advanced.className = "review-more";
    const hasAdvanced =
      state.mistakeMin !== null ||
      state.hintMin !== null ||
      state.replayMin !== null ||
      state.responseMsMin !== null ||
      state.correctStreakMax !== null ||
      state.topic !== "" ||
      state.wordType !== "" ||
      state.level !== null ||
      state.grammarCategory !== "" ||
      state.lastSeenFrom !== "" ||
      state.lastSeenTo !== "" ||
      state.lastWrongFrom !== "" ||
      state.lastWrongTo !== "";
    advanced.open = hasAdvanced;
    const summary = document.createElement("summary");
    summary.textContent = "More filters";
    const advancedGrid = element("div", "review-filter-grid review-advanced");

    if (state.tab === "words") {
      advancedGrid.append(
        select(
          "Topic",
          state.topic,
          [["", "All topics"], ...topicOptions.map((option) => [option.id, option.label] as const)],
          (value) => this.#setParam("topic", value),
        ),
        select(
          "Word type",
          state.wordType,
          [["", "All word types"], ...wordTypeOptions.map((option) => [option.id, option.label] as const)],
          (value) => this.#setParam("wordType", value),
        ),
        select(
          "Library level",
          state.level === null ? "" : String(state.level),
          [
            ["", "All levels"],
            ...Array.from({ length: 100 }, (_, index) => {
              const value = String(index + 1);
              return [value, `Level ${value.padStart(3, "0")}`] as const;
            }),
          ],
          (value) => this.#setParam("level", value),
        ),
      );
    }

    if (state.tab === "grammar") {
      advancedGrid.append(
        select(
          "Grammar category",
          state.grammarCategory,
          [["", "All grammar"], ...grammarOptions.map((option) => [option.id, option.label] as const)],
          (value) => this.#setParam("grammar", value),
        ),
      );
    }

    advancedGrid.append(
      dateInput("Last seen from", state.lastSeenFrom, (value) =>
        this.#setParam("seenFrom", value),
      ),
      dateInput("Last seen to", state.lastSeenTo, (value) =>
        this.#setParam("seenTo", value),
      ),
      dateInput("Last mistake from", state.lastWrongFrom, (value) =>
        this.#setParam("wrongFrom", value),
      ),
      dateInput("Last mistake to", state.lastWrongTo, (value) =>
        this.#setParam("wrongTo", value),
      ),
      numberInput("Mistakes ≥", state.mistakeMin, "0", (value) =>
        this.#setNumberParam("mistakes", value),
      ),
      numberInput("Hints ≥", state.hintMin, "0", (value) =>
        this.#setNumberParam("hints", value),
      ),
      numberInput("Replays ≥", state.replayMin, "0", (value) =>
        this.#setNumberParam("replays", value),
      ),
      numberInput(
        "Response ≥ ms",
        state.responseMsMin,
        "5000",
        (value) => this.#setNumberParam("slowMs", value),
      ),
      numberInput(
        "Correct streak ≤",
        state.correctStreakMax,
        "2",
        (value) => this.#setNumberParam("streakMax", value),
      ),
    );
    advanced.append(summary, advancedGrid);

    section.append(primary, advanced);
    return section;
  }

  #renderResults(
    result: ReturnType<typeof queryLearningProfile>,
    vocabulary: Map<string, VocabularyEntry>,
    now: string,
  ): HTMLElement {
    const section = element("section", "review-results");

    const top = element("div", "review-results-top");
    top.append(
      element(
        "p",
        undefined,
        result.totalItems === 0
          ? "No matching learning items."
          : `Showing ${(result.page - 1) * result.pageSize + 1}-${Math.min(
              result.page * result.pageSize,
              result.totalItems,
            )} of ${result.totalItems}`,
      ),
    );

    const pageSize = select(
      "Rows",
      String(result.pageSize),
      [
        ["10", "10"],
        ["25", "25"],
        ["50", "50"],
        ["100", "100"],
      ],
      (value) => this.#setParam("pageSize", value),
    );
    pageSize.classList.add("review-page-size");
    top.append(pageSize);

    const tableWrap = element("div", "review-table-wrap");
    const table = document.createElement("table");
    table.className = "review-table";
    const thead = document.createElement("thead");
    const headerRow = document.createElement("tr");
    for (const label of [
      "Item",
      "Mastery",
      "Mistakes",
      "Last mistake",
      "Source",
    ]) {
      headerRow.append(element("th", undefined, label));
    }
    thead.append(headerRow);
    const tbody = document.createElement("tbody");

    const mobile = element("div", "review-mobile-list");
    for (const item of result.items) {
      const vocab = vocabulary.get(item.entityId);
      const row = document.createElement("tr");
      row.tabIndex = 0;
      row.setAttribute("role", "button");
      row.addEventListener("click", () => this.#openDrawer(item, vocab, now));
      row.addEventListener("keydown", (event) => {
        if (event.key === "Enter" || event.key === " ") {
          event.preventDefault();
          this.#openDrawer(item, vocab, now);
        }
      });

      const itemCell = document.createElement("td");
      const itemStack = element("div", "review-item-stack");
      itemStack.append(element("strong", undefined, vocab?.en ?? item.entityId));
      if (vocab !== undefined) {
        itemStack.append(
          element("span", undefined, vocab.vi),
          element("small", undefined, vocab.ipa),
        );
      }
      itemCell.append(itemStack);

      const masteryCell = document.createElement("td");
      const mastery = element("div", "review-mastery");
      const meter = element("div", "review-meter");
      const fill = element("span");
      fill.style.width = `${item.mastery}%`;
      meter.append(fill);
      mastery.append(
        element(
          "strong",
          undefined,
          `${item.mastery}% ${masteryLabel(item.mastery)}`,
        ),
        meter,
      );
      masteryCell.append(mastery);

      row.append(
        itemCell,
        masteryCell,
        element("td", undefined, String(item.wrong)),
        element("td", undefined, formatDate(item.lastWrongAt)),
        element(
          "td",
          undefined,
          item.sourceGames.length === 0
            ? "—"
            : item.sourceGames.map(sourceLabel).join(", "),
        ),
      );
      tbody.append(row);

      const card = element("button", "review-mobile-card");
      card.addEventListener("click", () => this.#openDrawer(item, vocab, now));
      const cardTop = element("div", "review-mobile-top");
      const title = element("div", "review-item-stack");
      title.append(element("strong", undefined, vocab?.en ?? item.entityId));
      if (vocab !== undefined) {
        title.append(element("span", undefined, vocab.vi));
      }
      cardTop.append(
        title,
        element("strong", "review-mobile-mastery", `${item.mastery}%`),
      );
      card.append(
        cardTop,
        element(
          "span",
          "review-mobile-meta",
          `${item.wrong} mistakes · ${formatDate(
            item.lastWrongAt,
          )} · ${item.sourceGames.map(sourceLabel).join(", ") || "No source"}`,
        ),
      );
      mobile.append(card);
    }

    table.append(thead, tbody);
    tableWrap.append(table);

    const pagination = this.#renderPagination(
      result.page,
      result.totalPages,
    );
    section.append(top, tableWrap, mobile, pagination);
    return section;
  }

  #renderPagination(page: number, totalPages: number): HTMLElement {
    const nav = element("nav", "review-pagination");
    nav.setAttribute("aria-label", "Review pages");

    const previous = element("button", undefined, "Previous");
    previous.disabled = page <= 1;
    previous.addEventListener("click", () =>
      this.#setParam("page", String(page - 1), false),
    );
    nav.append(previous);

    const candidates = new Set<number>([
      1,
      totalPages,
      page - 2,
      page - 1,
      page,
      page + 1,
      page + 2,
    ]);
    const pages = [...candidates]
      .filter((value) => value >= 1 && value <= totalPages)
      .sort((a, b) => a - b);
    let last = 0;
    for (const value of pages) {
      if (last !== 0 && value - last > 1) {
        nav.append(element("span", "review-page-gap", "…"));
      }
      const button = element("button", value === page ? "active" : "", String(value));
      button.setAttribute("aria-current", value === page ? "page" : "false");
      button.addEventListener("click", () =>
        this.#setParam("page", String(value), false),
      );
      nav.append(button);
      last = value;
    }

    const next = element("button", undefined, "Next");
    next.disabled = page >= totalPages;
    next.addEventListener("click", () =>
      this.#setParam("page", String(page + 1), false),
    );
    nav.append(next);
    return nav;
  }

  #openDrawer(
    item: LearningQueryItem,
    vocabulary: VocabularyEntry | undefined,
    now: string,
  ): void {
    document.querySelector(".review-drawer-backdrop")?.remove();

    const backdrop = element("div", "review-drawer-backdrop");
    const drawer = element("aside", "review-drawer");
    drawer.setAttribute("aria-label", "Learning item details");

    const top = element("div", "review-drawer-top");
    const title = element("div");
    title.append(
      element("div", "review-eyebrow", item.entityType.toUpperCase()),
      element("h2", undefined, vocabulary?.en ?? item.entityId),
    );
    if (vocabulary !== undefined) {
      title.append(
        element("p", "review-drawer-meaning", vocabulary.vi),
        element("p", "review-drawer-ipa", vocabulary.ipa),
      );
    }
    const close = element("button", "review-drawer-close", "×");
    close.setAttribute("aria-label", "Close details");
    close.addEventListener("click", () => backdrop.remove());
    top.append(title, close);

    const metrics = element("div", "review-detail-grid");
    const details: Array<[string, string]> = [
      ["Mastery", `${item.mastery}% · ${masteryLabel(item.mastery)}`],
      ["Attempts", String(item.attempts)],
      ["Correct", String(item.correct)],
      ["Mistakes", String(item.wrong)],
      ["Hints", String(item.hints ?? 0)],
      ["Replays", String(item.replays ?? 0)],
      ["Average response", formatResponse(item.avgResponseMs)],
      ["Correct streak", String(item.correctStreak ?? 0)],
      ["Last seen", formatDate(item.lastSeenAt)],
      ["Last mistake", formatDate(item.lastWrongAt)],
      ["Next review", formatDate(item.nextReviewAt)],
      [
        "Source games",
        item.sourceGames.length === 0
          ? "—"
          : item.sourceGames.map(sourceLabel).join(", "),
      ],
    ];
    if (vocabulary !== undefined) {
      details.push(["Library level", String(vocabulary.level)]);
    }
    for (const [label, value] of details) {
      const box = element("div", "review-detail");
      box.append(element("span", undefined, label), element("strong", undefined, value));
      metrics.append(box);
    }

    const reasonSection = element("section", "review-why");
    reasonSection.append(element("h3", undefined, "Why Review"));
    const reasons = document.createElement("ul");
    for (const reason of whyReview(item, now)) {
      reasons.append(element("li", undefined, reason));
    }
    reasonSection.append(reasons);

    const mistakes = Array.isArray(item.recentMistakes)
      ? item.recentMistakes
      : [];
    const mistakeSection = element("section", "review-recent");
    mistakeSection.append(element("h3", undefined, "Recent mistakes"));
    if (mistakes.length === 0) {
      mistakeSection.append(element("p", undefined, "No recent mistake samples."));
    } else {
      const list = document.createElement("ul");
      for (const raw of mistakes.slice(-8).reverse()) {
        const sample = raw as Record<string, unknown>;
        const answer =
          typeof sample["userAnswer"] === "string"
            ? sample["userAnswer"]
            : "Incorrect attempt";
        const expected =
          typeof sample["expectedAnswer"] === "string"
            ? sample["expectedAnswer"]
            : vocabulary?.en ?? item.entityId;
        list.append(
          element("li", undefined, `${answer} → ${expected}`),
        );
      }
      mistakeSection.append(list);
    }

    const practice = element("button", "review-primary review-practice", "Practice now");
    practice.addEventListener("click", () => {
      const params = new URLSearchParams();
      params.set("item", item.entityId);
      params.set("entity", item.entityType);
      this.#navigate(`/review/build?${params.toString()}`);
      backdrop.remove();
    });

    drawer.append(top, metrics, reasonSection, mistakeSection, practice);
    backdrop.append(drawer);
    backdrop.addEventListener("click", (event) => {
      if (event.target === backdrop) backdrop.remove();
    });
    document.body.append(backdrop);
    close.focus();
  }
}
