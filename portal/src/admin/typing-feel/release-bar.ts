// The P05 bar of every Typing Feel page: Save draft → Review → Publish to all games
// (docs/games/TYPING_FEEL_SERVICE.md §3.7, §3.11). Review runs the server's checks
// on the saved draft and shows its change scope with "Affects all games"; Publish
// is enabled only for a draft whose review passed, and asks once more.
import { openAdminConfirmDialog } from "../v2/admin-dialog";
import { TYPING_FEEL_PERMISSIONS, TYPING_FEEL_ROUTES } from "./routes";
import { reviewPublishable, type TypingFeelSession } from "./session";
import type { TypingFeelChangeScope, TypingFeelValidation } from "./types";
import { bindSession, button, chip, el, focusKey, formatTime, keepFocus, permissionButton } from "./ui";

export type ReleaseBarPage = "keyboard-sounds" | "typing-effects" | "release";

export function scopeList(scope: TypingFeelChangeScope): HTMLElement {
  const list = el("ul", "tf-scope-list");
  const lines = scope.summary.length ? scope.summary : ["No Typing Feel changes against the live revision."];
  for (const line of lines) list.append(el("li", undefined, line));
  return list;
}

function problemList(problems: readonly string[]): HTMLElement {
  const list = el("ul", "tf-problem-list");
  for (const problem of problems) list.append(el("li", undefined, problem));
  return list;
}

function reviewPanel(review: TypingFeelValidation): HTMLElement {
  const root = el("section", `tf-review ${review.valid ? "good" : "bad"}`);
  root.setAttribute("aria-label", "Review of the saved draft");
  const head = el("div", "tf-review-head");
  const heading = el("div");
  heading.append(el("div", "st-admin-v2-eyebrow", "Review"), el("h2", undefined, `Draft ${review.revision}`));
  const chips = el("div", "tf-chips");
  chips.append(chip("Affects all games", "warn"), review.valid ? chip("Checks passed", "good") : chip(`${review.problems.length} ${review.problems.length === 1 ? "problem" : "problems"}`, "bad"));
  head.append(heading, chips);
  root.append(head);
  if (!review.valid) {
    root.append(el("p", "tf-review-lead", "Publishing is blocked. Fix these in the draft, then Save draft and Review again:"), problemList(review.problems));
  }
  const grid = el("div", "tf-review-grid");
  const changes = el("div");
  changes.append(el("h3", undefined, "What changes"), scopeList(review.changeScope));
  grid.append(changes);
  if (review.catalogue) {
    const result = el("div");
    result.append(el("h3", undefined, "Catalogue after publishing"));
    const facts = el("ul", "tf-scope-list");
    facts.append(
      el("li", undefined, `${review.catalogue.sets} sets in ${review.catalogue.families} families; default ${review.catalogue.default}.`),
      el("li", undefined, review.catalogue.hidden.length ? `Hidden (left out of the catalogue): ${review.catalogue.hidden.join(", ")}.` : "No hidden sets."),
    );
    if (review.plan) {
      facts.append(el("li", undefined, review.plan.created.length
        ? `Writes ${review.plan.created.length} new set ${review.plan.created.length === 1 ? "folder" : "folders"}: ${review.plan.created.join(", ")}.`
        : "No new set folders: every set keeps its URL, so the games' caches stay valid."));
    }
    result.append(facts);
    const link = el("a", "tf-link", "Open the draft catalogue (JSON)");
    link.href = `${review.previewBase}keys-manifest.json`;
    link.target = "_blank";
    link.rel = "noopener";
    result.append(link);
    grid.append(result);
  }
  root.append(grid, el("p", "tf-review-warning", review.changeScope.publishWarning));
  return root;
}

/**
 * Puts keyboard focus on the bar's notice (it announces the outcome), for actions
 * whose trigger is gone after the re-render: Publish, Rollback, Retire. Runs after
 * the confirm dialog has closed and tried its own return focus.
 */
export function focusTypingFeelNotice(scope: ParentNode = document): void {
  setTimeout(() => {
    const target = scope.querySelector<HTMLElement>('[data-focus-key="bar:notice"]')
      ?? scope.querySelector<HTMLElement>('[data-focus-key="bar:heading"]');
    target?.focus({ preventScroll: true });
  }, 0);
}

function openPublishDialog(session: TypingFeelSession, review: TypingFeelValidation, trigger: HTMLElement, scope: ParentNode): void {
  const detail = el("div", "tf-dialog-detail");
  detail.append(chip("Affects all games", "warn"), scopeList(review.changeScope));
  openAdminConfirmDialog({
    eyebrow: "All games · Typing Feel",
    title: "Publish to all games?",
    message: `${review.changeScope.publishWarning} Draft ${review.revision} replaces live revision ${review.activeRevision}. Rollback stays available in Release & History.`,
    detail,
    tone: "danger",
    confirmLabel: "Publish to all games",
    returnFocus: trigger,
    onConfirm: async () => {
      await session.publish();
      focusTypingFeelNotice(scope);
    },
  });
}

/** The review panel, the last notice and the sticky bar, re-rendered on every session change. */
export function createTypingFeelReleaseBar(session: TypingFeelSession, page: ReleaseBarPage, navigate: (path: string) => void): HTMLElement {
  const root = el("div", "tf-release-host");
  const focusStep = (key: string): void => {
    const next = root.querySelector<HTMLButtonElement>(`[data-focus-key="${key}"]`);
    if (next && !next.disabled && !next.hidden) next.focus({ preventScroll: true });
  };
  const render = (): void => keepFocus(root, draw);
  const draw = (): void => {
    root.replaceChildren();
    const ready = session.ready;
    if (!ready || !session.working) return;
    const permissions = ready.permissions;
    const dirty = session.dirty;
    const draft = session.savedDraft;
    const review = session.currentReview;
    const busy = session.busy;
    const summary = session.changeSummary;

    if (review) root.append(reviewPanel(review));

    const publishable = reviewPublishable(review);
    const bar = el("div", `st-admin-v2-draft-bar tf-release-bar ${dirty ? "warn" : publishable ? "good" : review ? "bad" : "info"}`);
    bar.setAttribute("role", "region");
    bar.setAttribute("aria-label", "Typing Feel draft: Save draft, Review, Publish to all games");
    const copy = el("div", "st-admin-v2-draft-copy");
    let heading: string;
    let status: string;
    if (dirty) {
      heading = "Unsaved edits";
      status = `${summary.parts.join(", ")} changed in this tab. Save draft to keep them; the games do not change yet.`;
    } else if (draft && publishable) {
      heading = "Review passed";
      status = `Draft ${draft.revision} is ready to publish. Every game picks it up on its next load.`;
    } else if (draft && review?.valid) {
      heading = "Not publishable";
      status = `Draft ${draft.revision} passed its checks, but the live revision is now ${review.activeRevision}. Make the edits again on top of the live revision.`;
    } else if (draft && review) {
      heading = "Review failed";
      status = `Draft ${draft.revision} cannot be published. Fix the problems in the review, then Save draft and Review again.`;
    } else if (draft) {
      heading = "Draft saved";
      status = `Draft ${draft.revision}, saved ${formatTime(draft.createdAt)} by ${draft.author}. Review it before publishing.`;
    } else {
      heading = "No draft";
      status = `Live: ${ready.active.revision}${ready.active.publication ? ` (catalogue ${ready.active.publication.catalogueRevision})` : ""}. ${page === "release" ? "Edit Keyboard Sounds or Typing Effects to start a draft." : "Edits here stay in this tab until you save a draft."}`;
    }
    const headingRow = el("div", "tf-bar-heading");
    const headingText = focusKey(el("strong", undefined, heading), "bar:heading");
    headingText.tabIndex = -1;
    headingRow.append(headingText, chip("Affects all games", "warn"));
    copy.append(headingRow, el("span", undefined, status));
    if (session.notice) {
      const notice = focusKey(el("div", `tf-bar-notice ${session.notice.tone}`), "bar:notice");
      notice.tabIndex = -1;
      notice.setAttribute("role", session.notice.tone === "bad" ? "alert" : "status");
      notice.append(el("span", undefined, session.notice.message));
      if (session.notice.problems?.length) notice.append(problemList(session.notice.problems));
      copy.append(notice);
    }
    if (!permissions.draft && !permissions.publish) copy.append(el("span", "tf-bar-role", "Your role can review drafts but not save or publish them."));
    else if (!permissions.publish) copy.append(el("span", "tf-bar-role", "Your role can save drafts; publishing to all games needs shared.publish."));

    const actions = el("div", "st-admin-v2-draft-actions tf-steps");
    if (dirty) actions.append(focusKey(button("Discard", () => session.discard()), "bar:discard"));
    else if (draft && page !== "release") {
      const reset = focusKey(button("Start from live", () => session.startFromLive()), "bar:start-live");
      reset.title = "Leave the saved draft unpublished and edit the live revision instead.";
      actions.append(reset);
    }
    const save = permissionButton(busy === "save" ? "Saving…" : "Save draft", TYPING_FEEL_PERMISSIONS.saveDraft, permissions.draft, () => {
      void session.saveDraft().then((created) => {
        if (created) focusStep("bar:review");
      });
    }, "st-admin-btn primary");
    focusKey(save, "bar:save");
    save.disabled = !dirty || busy !== null;
    if (!dirty) save.title = "No unsaved edits.";
    const reviewButton = button(busy === "review" ? "Reviewing…" : "Review", () => {
      void session.runReview().then((result) => {
        if (!result) {
          focusTypingFeelNotice(root);
          return;
        }
        root.querySelector(".tf-review")?.scrollIntoView({ block: "start", behavior: "smooth" });
        focusStep(reviewPublishable(result) ? "bar:publish" : "bar:review");
      });
    });
    focusKey(reviewButton, "bar:review");
    reviewButton.disabled = !draft || busy !== null;
    reviewButton.title = dirty ? "Save the draft first." : draft ? "Run the server checks and show what changes." : "There is no saved draft to review.";
    const publish = permissionButton(busy === "publish" ? "Publishing…" : "Publish to all games", TYPING_FEEL_PERMISSIONS.publish, permissions.publish, () => {
      const current = session.currentReview;
      if (current && reviewPublishable(current)) openPublishDialog(session, current, publish, root);
    }, "st-admin-btn st-admin-v2-publish");
    focusKey(publish, "bar:publish");
    publish.disabled = !publishable || busy !== null;
    publish.title = publishable ? "Publish this draft to every game." : "Review a saved draft first; only a draft whose checks pass, on top of the live revision, can be published.";
    const arrow = (shown: boolean) => {
      const node = el("span", "tf-step-arrow", "→");
      node.setAttribute("aria-hidden", "true");
      node.hidden = !shown;
      return node;
    };
    actions.append(save, arrow(permissions.draft), reviewButton, arrow(permissions.publish), publish);
    if (page !== "release") {
      const history = focusKey(button("Release & History", () => navigate(TYPING_FEEL_ROUTES.release), "st-admin-btn tf-ghost"), "bar:history");
      actions.append(history);
    }
    bar.append(copy, actions);
    root.append(bar);
  };
  bindSession(root, session, render);
  render();
  return root;
}
