// One Typing Feel working copy for the whole Admin tab (§3.7 bottom bar, P05:
// Edit → Save draft → Review → Publish). Keyboard Sounds and Typing Effects edit
// the same copy, so moving between them keeps unsaved edits; Release & History
// shows the same draft. Revisions are immutable: Save draft always creates a new
// one on top of the live revision, which is the only kind the server publishes.
import { TypingFeelApiError, typingFeelApi, typingFeelErrorProblems } from "./api";
import { cloneConfig, localChangeSummary, sameConfig } from "./draft-model";
import type {
  TypingFeelConfig,
  TypingFeelPublishResult,
  TypingFeelReadyState,
  TypingFeelRevision,
  TypingFeelState,
  TypingFeelValidation,
} from "./types";

/** A Review the server can act on: checks passed and the draft still sits on the live revision. */
export function reviewPublishable(review: TypingFeelValidation | null): boolean {
  return review !== null && review.valid && review.publishable;
}

export type SessionPhase = "loading" | "ready" | "not-imported" | "unavailable" | "error";
export type SessionTone = "info" | "good" | "warn" | "bad";
export type SessionNotice = { tone: SessionTone; message: string; problems?: string[] };
export type SessionBusy = null | "load" | "save" | "review" | "publish" | "rollback";

type Listener = () => void;

export class TypingFeelSession {
  phase: SessionPhase = "loading";
  state: TypingFeelState | null = null;
  /** Server message when Typing Feel is off (503) or the state could not be read. */
  failure: string | null = null;
  /** The revision the working copy started from: the draft waiting, a picked revision, or the live revision. */
  source: TypingFeelRevision | null = null;
  working: TypingFeelConfig | null = null;
  review: TypingFeelValidation | null = null;
  busy: SessionBusy = null;
  notice: SessionNotice | null = null;
  private readonly listeners = new Set<Listener>();
  private pending: Promise<void> | null = null;

  get ready(): TypingFeelReadyState | null {
    return this.state?.initialized ? this.state : null;
  }

  get active(): TypingFeelRevision | null {
    return this.ready?.active ?? null;
  }

  get dirty(): boolean {
    return this.source !== null && this.working !== null && !sameConfig(this.source.config, this.working);
  }

  /** The saved draft the working copy shows, when there are no unsaved edits on top of it. */
  get savedDraft(): TypingFeelRevision | null {
    const source = this.source;
    if (!source || this.dirty || source.relation !== "draft" || source.publishable !== true) return null;
    return source;
  }

  /** The review of the saved draft, if it is still current. */
  get currentReview(): TypingFeelValidation | null {
    const draft = this.savedDraft;
    return draft && this.review?.revision === draft.revision ? this.review : null;
  }

  get changeSummary(): { count: number; parts: string[] } {
    if (!this.source || !this.working) return { count: 0, parts: [] };
    return localChangeSummary(this.source.config, this.working);
  }

  subscribe(listener: Listener): () => void {
    this.listeners.add(listener);
    return () => this.listeners.delete(listener);
  }

  private emit(): void {
    for (const listener of [...this.listeners]) listener();
  }

  setNotice(notice: SessionNotice | null): void {
    this.notice = notice;
    this.emit();
  }

  /** Loads the state once per call site burst; keeps unsaved edits while the live revision stays the same. */
  load(options: { reset?: boolean; sourceRevision?: string } = {}): Promise<void> {
    if (this.pending && !options.reset && !options.sourceRevision) return this.pending;
    const run = this.#load(options).finally(() => {
      if (this.pending === run) this.pending = null;
    });
    this.pending = run;
    return run;
  }

  async #load({ reset = false, sourceRevision }: { reset?: boolean; sourceRevision?: string }): Promise<void> {
    if (this.state === null) this.phase = "loading";
    this.busy = this.busy ?? "load";
    this.emit();
    let next: TypingFeelState;
    try {
      next = await typingFeelApi.state();
    } catch (error) {
      if (this.busy === "load") this.busy = null;
      this.state = null;
      this.source = null;
      this.working = null;
      this.review = null;
      this.phase = error instanceof TypingFeelApiError && error.status === 503 ? "unavailable" : "error";
      this.failure = error instanceof Error ? error.message : String(error);
      this.emit();
      return;
    }
    if (this.busy === "load") this.busy = null;
    if (!next || typeof next !== "object" || !next.options || !next.permissions) {
      // The page and the Admin service ship together; a service started before an update lacks the newer fields.
      this.state = null;
      this.source = null;
      this.working = null;
      this.review = null;
      this.phase = "error";
      this.failure = "This Admin service is older than the page. Restart it (pnpm dev:admin, or the Admin process of pnpm dev), then reload.";
      this.emit();
      return;
    }
    this.failure = null;
    const previousActive = this.ready?.state.activeRevision ?? null;
    const hadEdits = this.dirty;
    this.state = next;
    if (!next.initialized) {
      this.phase = "not-imported";
      this.source = null;
      this.working = null;
      this.review = null;
      this.emit();
      return;
    }
    this.phase = "ready";
    const find = (id: string | undefined | null) => (id ? next.history.find((entry) => entry.revision === id) ?? null : null);
    const activeChanged = previousActive !== null && previousActive !== next.state.activeRevision;
    const kept = !reset && !sourceRevision && !activeChanged ? find(this.source?.revision) : null;
    if (kept && this.working && this.source) {
      // Same live revision: keep the working copy and refresh the source's relation flags.
      this.source = { ...kept, config: this.source.config };
    } else {
      // A revision the user picked, else the server's draft waiting (never published, saved
      // after the live revision went live), else the live revision. Drafts left from before
      // a Publish or a Rollback are only used when picked in History.
      const picked = sourceRevision ? await this.#whole(next, sourceRevision) : null;
      this.source = picked ?? next.draft ?? next.active;
      this.working = cloneConfig(this.source.config);
      this.review = null;
      if (activeChanged && hadEdits && !reset) {
        this.notice = { tone: "warn", message: `The live revision changed to ${next.state.activeRevision} in another tab or session; unsaved edits were dropped. Make them again on top of the new live revision.` };
      }
    }
    this.emit();
  }

  /** One revision with its config: History rows come without it. */
  async #whole(next: TypingFeelReadyState, revision: string): Promise<TypingFeelRevision | null> {
    if (revision === next.active.revision) return next.active;
    if (revision === next.draft?.revision) return next.draft;
    const entry = next.history.find((candidate) => candidate.revision === revision);
    if (!entry) return null;
    try {
      const whole = await typingFeelApi.revision(revision);
      return { ...entry, config: whole.config };
    } catch (error) {
      this.notice = { tone: "bad", message: `Revision ${revision} could not be loaded.`, problems: typingFeelErrorProblems(error) };
      return null;
    }
  }

  /** Replaces the working copy with an edited one (only local; nothing is saved). */
  edit(config: TypingFeelConfig): void {
    if (!this.working) return;
    this.working = config;
    this.review = null;
    this.notice = null;
    this.emit();
  }

  editError(message: string): void {
    this.setNotice({ tone: "bad", message });
  }

  /** Drops unsaved edits: back to the draft or live revision the copy started from. */
  discard(): void {
    if (!this.source) return;
    this.working = cloneConfig(this.source.config);
    this.review = null;
    this.notice = { tone: "info", message: "Unsaved edits discarded." };
    this.emit();
  }

  /** Starts over from the live revision, leaving the saved draft as it is (it is simply never published). */
  startFromLive(): void {
    const active = this.active;
    if (!active) return;
    this.source = active;
    this.working = cloneConfig(active.config);
    this.review = null;
    this.notice = { tone: "info", message: `Working copy reset to the live revision ${active.revision}. The saved draft stays in History and is not published.` };
    this.emit();
  }

  async saveDraft(): Promise<TypingFeelRevision | null> {
    const ready = this.ready;
    if (!ready || !this.working || !this.dirty || this.busy) return null;
    const summary = this.changeSummary;
    this.busy = "save";
    this.notice = null;
    this.emit();
    try {
      const created = await typingFeelApi.saveDraft({
        baseRevision: ready.state.activeRevision,
        config: this.working,
        message: `Typing Feel draft: ${summary.parts.join(", ") || "no changes"}`,
      });
      this.busy = null;
      await this.load({ sourceRevision: created.revision });
      this.setNotice({ tone: "good", message: `Draft ${created.revision} saved. Nothing changes in the games until it is published. Next: Review.` });
      return created;
    } catch (error) {
      this.busy = null;
      this.setNotice({ tone: "bad", message: "The draft was not saved.", problems: typingFeelErrorProblems(error) });
      return null;
    }
  }

  async runReview(): Promise<TypingFeelValidation | null> {
    const draft = this.savedDraft;
    if (!draft || this.busy) return null;
    this.busy = "review";
    this.notice = null;
    this.emit();
    try {
      const review = await typingFeelApi.validate(draft.revision);
      this.busy = null;
      // Stale only when the live revision moved; a draft with failed checks keeps its review so its problems show.
      const stale = review.activeRevision !== this.ready?.state.activeRevision || review.parentRevision !== review.activeRevision;
      if (stale) {
        // Another tab, session or a Rollback changed the live revision: the draft no longer sits
        // on it, so it cannot be published and its change scope would leave out what reverts.
        this.review = null;
        await this.load();
        this.setNotice({ tone: "warn", message: `The live revision is now ${review.activeRevision}, changed in another tab or session. Draft ${draft.revision} was based on ${review.parentRevision ?? "no revision"}, so it cannot be published. Make the edits again on top of the live revision.` });
        return null;
      }
      this.review = review;
      this.emit();
      return review;
    } catch (error) {
      this.busy = null;
      this.review = null;
      this.setNotice({ tone: "bad", message: "The review could not run.", problems: typingFeelErrorProblems(error) });
      return null;
    }
  }

  /** Publish the reviewed draft. Throws, so the confirm dialog can show the error and stay open. */
  async publish(): Promise<TypingFeelPublishResult> {
    const ready = this.ready;
    const review = this.currentReview;
    if (!ready || !review || !reviewPublishable(review)) throw new Error("Review the saved draft before publishing.");
    this.busy = "publish";
    this.emit();
    try {
      const result = await typingFeelApi.publish(review.revision, ready.state.activeRevision);
      this.busy = null;
      await this.load({ reset: true });
      this.setNotice({ tone: "good", message: `Published to all games: catalogue ${result.catalogue.revision}, ${result.catalogue.sets} sets in ${result.catalogue.families} families, default ${result.catalogue.default}. Each game picks it up on its next load.` });
      return result;
    } catch (error) {
      this.busy = null;
      this.emit();
      if (error instanceof TypingFeelApiError && error.status === 409) void this.load();
      throw new Error(typingFeelErrorProblems(error).join(" "));
    }
  }

  /** Roll every game back to an earlier published revision. Throws for the confirm dialog. */
  async rollback(targetRevision: string): Promise<TypingFeelPublishResult> {
    const ready = this.ready;
    if (!ready) throw new Error("Typing Feel is not loaded.");
    this.busy = "rollback";
    this.emit();
    try {
      const result = await typingFeelApi.rollback(targetRevision, ready.state.activeRevision);
      this.busy = null;
      await this.load({ reset: true });
      this.setNotice({ tone: "good", message: `Rolled back all games to ${targetRevision} (catalogue ${result.catalogue.revision}, ${result.catalogue.sets} sets). Each game picks it up on its next load.` });
      return result;
    } catch (error) {
      this.busy = null;
      this.emit();
      if (error instanceof TypingFeelApiError && error.status === 409) void this.load();
      throw new Error(typingFeelErrorProblems(error).join(" "));
    }
  }
}

export const typingFeelSession = new TypingFeelSession();

// A reload or a closed tab loses unsaved edits; moving between Admin pages does not.
if (typeof window !== "undefined") {
  window.addEventListener("beforeunload", (event) => {
    if (!typingFeelSession.dirty) return;
    event.preventDefault();
    event.returnValue = "";
  });
}
