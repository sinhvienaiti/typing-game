import { BrowserLearningProfileStore } from "../../../shared/learning/browser-store.mjs";
import {
  createLearningProfileBackup,
  learningProfileCounts,
  parseLearningProfileBackup,
  resetAllLearningProfile,
  resetLearningProfileSelection,
} from "../../../shared/learning/profile-backup.mjs";
import type { LearningEntityType } from "../../../shared/learning/core.mjs";
import { clearPendingMonkeyReview } from "./monkey-adapter";
import { clearPendingRecallReview } from "./recall-adapter";
import { clearPendingShooterReview } from "./shooter-adapter";
import { clearPendingSpaceReview } from "./space-adapter";
import { clearPendingKaraokeReview } from "./karaoke-adapter";
import { clearMixedReview } from "./mixed";
import { clearStoredReviewSession } from "./session";

type Navigate = (url: string) => void;

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

function clearTransientReviewState(): void {
  clearStoredReviewSession();
  clearMixedReview();
  clearPendingMonkeyReview();
  clearPendingRecallReview();
  clearPendingShooterReview();
  clearPendingSpaceReview();
  clearPendingKaraokeReview();
}

function timestampedBackupName(): string {
  const stamp = new Date()
    .toISOString()
    .replaceAll(":", "-")
    .replace(".000Z", "Z");
  return `typing-game-learning-${stamp}.json`;
}

function downloadJson(name: string, value: unknown): void {
  const blob = new Blob(
    [JSON.stringify(value, null, 2) + "\n"],
    { type: "application/json" },
  );
  const url = URL.createObjectURL(blob);
  const anchor = document.createElement("a");
  anchor.href = url;
  anchor.download = name;
  anchor.click();
  window.setTimeout(() => URL.revokeObjectURL(url), 0);
}

export class LearningMaintenancePage {
  #store = new BrowserLearningProfileStore();
  #navigate: Navigate;

  constructor(navigate: Navigate) {
    this.#navigate = navigate;
  }

  render(): HTMLElement {
    const main = element(
      "main",
      "review-page learning-maintenance-page",
    );
    main.append(
      element(
        "div",
        "review-loading",
        "Loading learning-data controls…",
      ),
    );
    void this.#renderInto(main).catch((error: unknown) => {
      main.replaceChildren();
      const box = element("section", "review-error");
      box.append(
        element("h1", undefined, "Learning Data"),
        element(
          "p",
          undefined,
          error instanceof Error
            ? error.message
            : "Could not load learning-data controls.",
        ),
      );
      const back = element(
        "button",
        "review-secondary",
        "Back to Smart Review",
      );
      back.addEventListener("click", () => this.#navigate("/review"));
      box.append(back);
      main.append(box);
    });
    return main;
  }

  async #renderInto(main: HTMLElement): Promise<void> {
    const profile = await this.#store.load();
    const counts = learningProfileCounts(profile);

    main.replaceChildren();

    const heading = element("section", "review-flow-heading");
    const copy = element("div");
    copy.append(
      element("div", "review-eyebrow", "LOCAL LEARNING DATA"),
      element("h1", undefined, "Backup & Reset"),
      element(
        "p",
        undefined,
        "Export a local backup, restore one safely, or reset selected learning history. Nothing is uploaded.",
      ),
    );
    const back = element(
      "button",
      "review-secondary",
      "Back to Smart Review",
    );
    back.addEventListener("click", () => this.#navigate("/review"));
    heading.append(copy, back);

    const status = element("div", "learning-maintenance-status");
    status.setAttribute("role", "status");
    status.setAttribute("aria-live", "polite");

    const overview = element(
      "section",
      "learning-maintenance-card learning-maintenance-overview",
    );
    overview.append(
      element("h2", undefined, "Current profile"),
      element(
        "p",
        undefined,
        `${counts.total} learned item${counts.total === 1 ? "" : "s"} stored in the parent browser profile.`,
      ),
    );
    const countGrid = element("div", "learning-maintenance-counts");
    for (const [label, value] of [
      ["Words", counts.vocabulary],
      ["Grammar", counts.grammar],
      ["Sentences", counts.sentence],
    ] as const) {
      const card = element("div");
      card.append(
        element("span", undefined, label),
        element("strong", undefined, String(value)),
      );
      countGrid.append(card);
    }
    overview.append(countGrid);

    const backup = element(
      "section",
      "learning-maintenance-card",
    );
    backup.append(
      element("h2", undefined, "Backup"),
      element(
        "p",
        undefined,
        "Export saves the complete shared Learning Profile as versioned JSON. Import replaces the current profile only after validation.",
      ),
    );
    const backupActions = element(
      "div",
      "learning-maintenance-actions",
    );
    const exportButton = element(
      "button",
      "review-primary",
      "Export learning profile",
    );
    exportButton.addEventListener("click", async () => {
      try {
        const latest = await this.#store.load();
        const exported = createLearningProfileBackup(latest);
        downloadJson(timestampedBackupName(), exported);
        status.className = "learning-maintenance-status success";
        status.textContent =
          "Learning profile exported. Your browser data was not changed.";
      } catch (error) {
        status.className = "learning-maintenance-status error";
        status.textContent =
          error instanceof Error
            ? error.message
            : "Could not export learning profile.";
      }
    });

    const importInput = document.createElement("input");
    importInput.type = "file";
    importInput.accept = ".json,application/json";
    importInput.className = "learning-maintenance-file";
    importInput.setAttribute(
      "aria-label",
      "Choose learning profile backup JSON",
    );

    const importButton = element(
      "button",
      "review-secondary",
      "Import selected file",
    );
    importButton.addEventListener("click", async () => {
      const file = importInput.files?.[0];
      if (file === undefined) {
        status.className = "learning-maintenance-status error";
        status.textContent = "Choose a JSON backup file first.";
        return;
      }

      try {
        const imported = parseLearningProfileBackup(await file.text());
        const importedCounts = learningProfileCounts(imported);
        const confirmed = window.confirm(
          "Import this learning profile?\n\n" +
            `Words: ${importedCounts.vocabulary}\n` +
            `Grammar: ${importedCounts.grammar}\n` +
            `Sentences: ${importedCounts.sentence}\n\n` +
            "This replaces the current shared learning profile.",
        );
        if (!confirmed) return;

        await this.#store.save(imported);
        clearTransientReviewState();
        status.className = "learning-maintenance-status success";
        status.textContent =
          "Learning profile imported. Review sessions were cleared to prevent stale queues.";
        this.#navigate("/review/data");
      } catch (error) {
        status.className = "learning-maintenance-status error";
        status.textContent =
          error instanceof Error
            ? error.message
            : "Could not import this learning profile.";
      }
    });

    backupActions.append(exportButton, importInput, importButton);
    backup.append(backupActions);

    const selectedReset = element(
      "section",
      "learning-maintenance-card",
    );
    selectedReset.append(
      element("h2", undefined, "Reset selected history"),
      element(
        "p",
        undefined,
        "Choose exactly which learning groups to clear. Unselected groups remain unchanged.",
      ),
    );

    const choices = element(
      "fieldset",
      "learning-maintenance-choices",
    );
    choices.append(element("legend", undefined, "History to reset"));
    const selection = new Map<
      LearningEntityType,
      HTMLInputElement
    >();
    for (const [entityType, labelText, count] of [
      ["vocabulary", "Words", counts.vocabulary],
      ["grammar", "Grammar", counts.grammar],
      ["sentence", "Sentences", counts.sentence],
    ] as const) {
      const label = element("label");
      const input = document.createElement("input");
      input.type = "checkbox";
      input.disabled = count === 0;
      selection.set(entityType, input);
      label.append(
        input,
        document.createTextNode(
          `${labelText} (${count})`,
        ),
      );
      choices.append(label);
    }

    const resetSelected = element(
      "button",
      "review-danger",
      "Reset selected history",
    );
    resetSelected.addEventListener("click", async () => {
      const selected = [...selection.entries()]
        .filter(([, input]) => input.checked)
        .map(([entityType]) => entityType);
      if (selected.length === 0) {
        status.className = "learning-maintenance-status error";
        status.textContent =
          "Select at least one history group to reset.";
        return;
      }

      const labels = selected.map((entityType) =>
        entityType === "vocabulary"
          ? "Words"
          : entityType === "grammar"
            ? "Grammar"
            : "Sentences",
      );
      if (
        !window.confirm(
          "Reset selected learning history?\n\n" +
            labels.join(", ") +
            "\n\nThis cannot be undone unless you exported a backup.",
        )
      ) {
        return;
      }

      const latest = await this.#store.load();
      const next = resetLearningProfileSelection(
        latest,
        selected,
      );
      await this.#store.save(next);
      clearTransientReviewState();
      this.#navigate("/review/data");
    });

    selectedReset.append(choices, resetSelected);

    const resetAll = element(
      "section",
      "learning-maintenance-card learning-maintenance-danger",
    );
    resetAll.append(
      element("h2", undefined, "Reset all learning history"),
      element(
        "p",
        undefined,
        "Clears Words, Grammar and Sentences from the shared parent profile. Game settings and vocabulary source files are not removed.",
      ),
    );
    const resetAllButton = element(
      "button",
      "review-danger",
      "Reset all learning history",
    );
    resetAllButton.disabled = counts.total === 0;
    resetAllButton.addEventListener("click", async () => {
      if (
        !window.confirm(
          "Reset ALL shared learning history?\n\n" +
            "This clears Words, Grammar and Sentences. " +
            "This cannot be undone unless you exported a backup.",
        )
      ) {
        return;
      }

      await this.#store.save(resetAllLearningProfile());
      clearTransientReviewState();
      this.#navigate("/review/data");
    });
    resetAll.append(resetAllButton);

    main.append(
      heading,
      status,
      overview,
      backup,
      selectedReset,
      resetAll,
    );
  }
}
