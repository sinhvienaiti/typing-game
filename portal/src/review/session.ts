import type {
  LearningEntityType,
  LearningProfile,
} from "../../../shared/learning/core.mjs";
import { BrowserLearningProfileStore } from "../../../shared/learning/browser-store.mjs";
import {
  buildQuickReviewPlan,
  buildReviewPlan,
  type ReviewPlan,
  type ReviewPlanInput,
} from "../../../shared/learning/review-session.mjs";

type Navigate = (url: string) => void;
type StartReview = (plan: ReviewPlan) => Promise<void>;

const SESSION_KEY = "typingGameReviewSessionV1";

const GAME_LABELS: Record<string, string> = {
  monkeytype: "Monkeytype",
  "recall-typing": "Recall Typing",
  "vocab-shooter": "Vocabulary Shooter",
  "space-typing": "Space Typing",
  "karaoke-typing": "Karaoke Typing",
  "mixed-review": "Mixed Review",
};

const CONTENT_LABELS: Record<LearningEntityType, string> = {
  vocabulary: "Vocabulary",
  grammar: "Grammar",
  sentence: "Sentences",
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

function selectField(
  labelText: string,
  options: ReadonlyArray<readonly [string, string]>,
  value: string,
): { label: HTMLLabelElement; select: HTMLSelectElement } {
  const label = element("label", "review-builder-field");
  label.append(element("span", undefined, labelText));
  const select = document.createElement("select");
  for (const [id, text] of options) {
    const option = document.createElement("option");
    option.value = id;
    option.textContent = text;
    option.selected = id === value;
    select.append(option);
  }
  label.append(select);
  return { label, select };
}

function inputField(
  labelText: string,
  type: "number" | "date",
  placeholder = "",
): { label: HTMLLabelElement; input: HTMLInputElement } {
  const label = element("label", "review-builder-field");
  label.append(element("span", undefined, labelText));
  const input = document.createElement("input");
  input.type = type;
  input.placeholder = placeholder;
  if (type === "number") input.min = "0";
  label.append(input);
  return { label, input };
}

function entityCollection(
  profile: LearningProfile,
  entityType: LearningEntityType,
): Record<string, unknown> {
  if (entityType === "vocabulary") return profile.vocabulary;
  if (entityType === "grammar") return profile.grammar;
  return profile.sentences;
}

function onlyRequestedItem(
  profile: LearningProfile,
  entityType: LearningEntityType,
  entityId: string,
): LearningProfile {
  const record = entityCollection(profile, entityType)[entityId];
  if (record === undefined) return profile;

  if (entityType === "vocabulary") {
    return {
      ...profile,
      vocabulary: { [entityId]: profile.vocabulary[entityId] },
      grammar: {},
      sentences: {},
    };
  }
  if (entityType === "grammar") {
    return {
      ...profile,
      vocabulary: {},
      grammar: { [entityId]: profile.grammar[entityId] },
      sentences: {},
    };
  }
  return {
    ...profile,
    vocabulary: {},
    grammar: {},
    sentences: { [entityId]: profile.sentences[entityId] },
  };
}

function storeSession(plan: ReviewPlan): void {
  sessionStorage.setItem(
    SESSION_KEY,
    JSON.stringify({
      version: 1,
      savedAt: new Date().toISOString(),
      plan,
    }),
  );
}

function readSession(): ReviewPlan | null {
  const raw = sessionStorage.getItem(SESSION_KEY);
  if (raw === null) return null;
  try {
    const parsed = JSON.parse(raw) as {
      version?: unknown;
      plan?: ReviewPlan;
    };
    return parsed.version === 1 && parsed.plan?.version === 1
      ? parsed.plan
      : null;
  } catch {
    return null;
  }
}

export class SmartReviewFlow {
  #store = new BrowserLearningProfileStore();
  #navigate: Navigate;
  #startReview: StartReview;

  constructor(navigate: Navigate, startReview: StartReview) {
    this.#navigate = navigate;
    this.#startReview = startReview;
  }

  renderBuilder(): HTMLElement {
    const main = element("main", "review-page review-builder-page");
    main.append(element("div", "review-loading", "Preparing Review Builder…"));
    void this.#renderBuilderInto(main).catch((error: unknown) => {
      main.replaceChildren();
      main.append(
        element(
          "div",
          "review-error",
          error instanceof Error
            ? error.message
            : "Could not prepare Review Builder.",
        ),
      );
    });
    return main;
  }

  async #renderBuilderInto(main: HTMLElement): Promise<void> {
    const fullProfile = await this.#store.load();
    const params = new URLSearchParams(location.search);
    const requestedEntity = params.get("entity");
    const requestedItem = params.get("item");
    const validEntity: LearningEntityType | null =
      requestedEntity === "vocabulary" ||
      requestedEntity === "grammar" ||
      requestedEntity === "sentence"
        ? requestedEntity
        : null;
    const profile =
      validEntity !== null && requestedItem !== null
        ? onlyRequestedItem(fullProfile, validEntity, requestedItem)
        : fullProfile;

    main.replaceChildren();

    const heading = element("section", "review-flow-heading");
    const headingCopy = element("div");
    headingCopy.append(
      element("div", "review-eyebrow", "SMART REVIEW"),
      element("h1", undefined, "Review Builder"),
      element(
        "p",
        undefined,
        "Choose what to review and where. The parent planner keeps mastery and compatibility rules consistent across every game.",
      ),
    );
    const back = element("button", "review-secondary", "Back to Dashboard");
    back.addEventListener("click", () => this.#navigate("/review"));
    heading.append(headingCopy, back);

    const quick = element("section", "review-quick-start");
    const quickCopy = element("div");
    quickCopy.append(
      element("strong", undefined, "Smart Review — 15 min"),
      element(
        "span",
        undefined,
        "Due items first, mixed content, and only compatible activities.",
      ),
    );
    const quickPlan = buildQuickReviewPlan(fullProfile);
    const quickButton = element(
      "button",
      "review-primary",
      quickPlan.selectedCount === 0
        ? "Nothing due now"
        : `Start ${quickPlan.selectedCount} items`,
    );
    quickButton.disabled = quickPlan.selectedCount === 0;
    quickButton.addEventListener("click", () => {
      storeSession(quickPlan);
      this.#navigate("/review/session");
    });
    quick.append(quickCopy, quickButton);

    const form = element("section", "review-builder-card");
    form.append(element("h2", undefined, "Custom Review"));

    const reviewSet = selectField(
      "Review set",
      [
        ["due", "Due Now"],
        ["today", "Today"],
        ["7d", "Recent 7 Days"],
        ["30d", "Recent 30 Days"],
        ["weakest", "Weakest"],
        ["at-risk", "At Risk"],
        ["custom", "Custom"],
      ],
      validEntity !== null && requestedItem !== null ? "custom" : "due",
    );

    const amount = selectField(
      "Amount",
      [
        ["10", "10"],
        ["20", "20"],
        ["30", "30"],
        ["50", "50"],
        ["all", "All"],
      ],
      validEntity !== null && requestedItem !== null ? "10" : "20",
    );

    const source = selectField(
      "Source filter",
      [
        ["", "All Games"],
        ["monkeytype", "Monkeytype"],
        ["recall-typing", "Recall Typing"],
        ["vocab-shooter", "Vocabulary Shooter"],
        ["space-typing", "Space Typing"],
        ["karaoke-typing", "Karaoke Typing"],
      ],
      "",
    );

    const goal = selectField(
      "Review goal",
      [
        ["remember-words", "Remember words"],
        ["spelling", "Spelling"],
        ["listening", "Listening"],
        ["grammar", "Grammar"],
        ["sentence-building", "Sentence building"],
        ["mixed", "Mixed"],
      ],
      "mixed",
    );

    const game = selectField(
      "Game",
      [
        ["monkeytype", "Monkeytype"],
        ["recall-typing", "Recall Typing"],
        ["vocab-shooter", "Vocabulary Shooter"],
        ["space-typing", "Space Typing"],
        ["karaoke-typing", "Karaoke Typing"],
        ["mixed-review", "Mixed Review"],
      ],
      "mixed-review",
    );

    const controls = element("div", "review-builder-grid");
    controls.append(
      reviewSet.label,
      amount.label,
      source.label,
      goal.label,
      game.label,
    );

    const contentField = element("fieldset", "review-content-field");
    contentField.append(element("legend", undefined, "Content"));
    const contentChecks = new Map<LearningEntityType, HTMLInputElement>();
    for (const entityType of [
      "vocabulary",
      "grammar",
      "sentence",
    ] as const) {
      const label = element("label");
      const input = document.createElement("input");
      input.type = "checkbox";
      input.checked =
        validEntity === null ? true : validEntity === entityType;
      contentChecks.set(entityType, input);
      label.append(input, document.createTextNode(CONTENT_LABELS[entityType]));
      contentField.append(label);
    }

    const custom = element("div", "review-custom-fields");
    const masteryMin = inputField("Mastery min", "number", "0");
    const masteryMax = inputField("Mastery max", "number", "100");
    const mistakeMin = inputField("Mistakes ≥", "number", "0");
    const wrongFrom = inputField("Last mistake from", "date");
    const wrongTo = inputField("Last mistake to", "date");
    custom.append(
      masteryMin.label,
      masteryMax.label,
      mistakeMin.label,
      wrongFrom.label,
      wrongTo.label,
    );

    const preview = element("div", "review-plan-preview");
    const start = element("button", "review-primary", "Start Review");
    const actions = element("div", "review-builder-actions");
    actions.append(preview, start);

    form.append(controls, contentField, custom, actions);
    main.append(heading, quick, form);

    const currentInput = (): ReviewPlanInput => {
      const selectedContent = [...contentChecks.entries()]
        .filter(([, input]) => input.checked)
        .map(([entityType]) => entityType);
      const amountValue =
        amount.select.value === "all"
          ? "all"
          : Number(amount.select.value) as 10 | 20 | 30 | 50;

      const customFilters: ReviewPlanInput["custom"] = {};
      const min = Number(masteryMin.input.value);
      const max = Number(masteryMax.input.value);
      const mistakes = Number(mistakeMin.input.value);
      if (masteryMin.input.value !== "") customFilters.masteryMin = min;
      if (masteryMax.input.value !== "") customFilters.masteryMax = max;
      if (mistakeMin.input.value !== "") customFilters.mistakeMin = mistakes;
      if (wrongFrom.input.value !== "") {
        customFilters.lastWrongFrom = new Date(
          `${wrongFrom.input.value}T00:00:00`,
        ).toISOString();
      }
      if (wrongTo.input.value !== "") {
        customFilters.lastWrongTo = new Date(
          `${wrongTo.input.value}T23:59:59.999`,
        ).toISOString();
      }

      return {
        reviewSet: reviewSet.select.value as ReviewPlanInput["reviewSet"],
        content: selectedContent,
        amount: amountValue,
        sourceGame: source.select.value,
        goal: goal.select.value as ReviewPlanInput["goal"],
        game: game.select.value as ReviewPlanInput["game"],
        custom: customFilters,
      };
    };

    let latestPlan: ReviewPlan | null = null;
    const updatePreview = (): void => {
      try {
        latestPlan = buildReviewPlan(profile, currentInput());
        preview.classList.remove("error");
        preview.replaceChildren(
          element(
            "strong",
            undefined,
            `${latestPlan.selectedCount} ready to review`,
          ),
          element(
            "span",
            undefined,
            `${latestPlan.compatibleCount} compatible · ${latestPlan.excludedCount} kept for another activity`,
          ),
        );
        start.disabled = latestPlan.selectedCount === 0;
      } catch (error) {
        latestPlan = null;
        preview.classList.add("error");
        preview.replaceChildren(
          element(
            "span",
            undefined,
            error instanceof Error ? error.message : "Invalid review setup",
          ),
        );
        start.disabled = true;
      }
    };

    const allInputs = form.querySelectorAll<
      HTMLInputElement | HTMLSelectElement
    >("input, select");
    for (const control of allInputs) {
      control.addEventListener("change", updatePreview);
    }

    start.addEventListener("click", () => {
      updatePreview();
      if (latestPlan === null || latestPlan.selectedCount === 0) return;
      storeSession(latestPlan);
      this.#navigate("/review/session");
    });

    updatePreview();
  }

  renderSession(): HTMLElement {
    const main = element("main", "review-page review-session-page");
    const plan = readSession();

    if (plan === null) {
      const empty = element("section", "review-error");
      empty.append(
        element("h1", undefined, "No active review session"),
        element(
          "p",
          undefined,
          "Create a Smart Review plan first so the parent can route compatible material safely.",
        ),
      );
      const build = element("button", "review-primary", "Open Review Builder");
      build.addEventListener("click", () => this.#navigate("/review/build"));
      empty.append(build);
      main.append(empty);
      return main;
    }

    const heading = element("section", "review-flow-heading");
    const copy = element("div");
    copy.append(
      element("div", "review-eyebrow", "REVIEW SESSION"),
      element(
        "h1",
        undefined,
        plan.options.game === "mixed-review"
          ? "Mixed Review"
          : GAME_LABELS[plan.options.game] ?? plan.options.game,
      ),
      element(
        "p",
        undefined,
        `${plan.selectedCount} selected · ${plan.durationMinutes} min target · ${plan.excludedCount} incompatible item${plan.excludedCount === 1 ? "" : "s"} preserved`,
      ),
    );
    const edit = element("button", "review-secondary", "Edit plan");
    edit.addEventListener("click", () => this.#navigate("/review/build"));
    heading.append(copy, edit);

    const shell = element("section", "review-session-shell");
    const summary = element("div", "review-session-summary");
    for (const [label, value] of [
      ["Review set", plan.options.reviewSet],
      ["Goal", plan.options.goal],
      ["Game", GAME_LABELS[plan.options.game] ?? plan.options.game],
      ["Items", String(plan.selectedCount)],
    ]) {
      const box = element("div");
      box.append(
        element("span", undefined, label),
        element("strong", undefined, value),
      );
      summary.append(box);
    }

    const notice = element("div", "review-session-notice");
    notice.append(
      element("strong", undefined, "Session core is ready"),
      element(
        "p",
        undefined,
        "This parent plan owns ordering and compatibility. Each child-game milestone will attach its adapter to consume this exact queue without creating a second Smart Review engine.",
      ),
    );

    const queue = element("div", "review-session-queue");
    queue.append(element("h2", undefined, "Review queue"));
    const list = element("ol");
    for (const item of plan.items.slice(0, 50)) {
      const row = element("li");
      const itemCopy = element("div");
      itemCopy.append(
        element("strong", undefined, item.entityId),
        element(
          "span",
          undefined,
          `${CONTENT_LABELS[item.entityType]} · ${item.mastery}% mastery · priority ${item.reviewPriority}`,
        ),
      );
      row.append(
        itemCopy,
        element(
          "small",
          undefined,
          item.compatibleGames.map((game) => GAME_LABELS[game] ?? game).join(", "),
        ),
      );
      list.append(row);
    }
    queue.append(list);
    if (plan.items.length > 50) {
      queue.append(
        element(
          "p",
          "review-session-more",
          `+${plan.items.length - 50} more items in the session queue`,
        ),
      );
    }

    const footer = element("div", "review-session-footer");
    const dashboard = element("button", "review-secondary", "Finish for now");
    dashboard.addEventListener("click", () => this.#navigate("/review"));
    const rebuild = element("button", "review-secondary", "Change activity");
    rebuild.addEventListener("click", () => this.#navigate("/review/build"));
    footer.append(dashboard, rebuild);

    if (
      plan.options.game === "monkeytype" ||
      plan.options.game === "recall-typing" ||
      plan.options.game === "vocab-shooter"
    ) {
      const gameLabel =
        GAME_LABELS[plan.options.game] ?? plan.options.game;
      const start = element(
        "button",
        "review-primary",
        `Start ${gameLabel}`,
      );
      start.addEventListener("click", () => {
        start.disabled = true;
        start.textContent = `Preparing ${gameLabel}…`;
        void this.#startReview(plan).catch((error: unknown) => {
          start.disabled = false;
          start.textContent = `Start ${gameLabel}`;
          notice.classList.add("error");
          notice.replaceChildren(
            element(
              "strong",
              undefined,
              `Could not start ${gameLabel} review`,
            ),
            element(
              "p",
              undefined,
              error instanceof Error
                ? error.message
                : "The review dataset could not be prepared.",
            ),
          );
        });
      });
      footer.append(start);
    }

    shell.append(summary, notice, queue, footer);
    main.append(heading, shell);
    return main;
  }
}
