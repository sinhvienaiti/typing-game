import { createAdminPageHeader, createAdminSkeleton } from "./admin-components";
import { openAdminConfirmDialog } from "./admin-dialog";
import { ago, button, chip, el, failure, formatTime, getJson, offlineNotice, panel, postJson, textField } from "./players-shared";

/**
 * Player feedback: the ideas, bug reports and contact messages players send
 * from the game (Feedback button on the title deck, or "Report a bug" in the
 * pause menu). New ones first; open one to read it with the game context it
 * came with, mark it read or resolved, leave a note for other Admins, or
 * answer the player with an in-game letter (their Daily Hub mailbox).
 */
type Status = "new" | "read" | "resolved";
type Category = "idea" | "bug" | "contact";
type FeedbackRow = {
  id: string;
  account_id: string | null;
  account_kind: string | null;
  display_name: string | null;
  category: Category;
  message: string;
  contact_email: string | null;
  context: Record<string, unknown>;
  status: Status;
  admin_note: string | null;
  created_at: string;
  handled_at: string | null;
  handled_by: string | null;
  account_status: string | null;
  pilot_code: string | null;
  account_email: string | null;
};
type FeedbackList = { total: number; counts: Record<Status, number>; feedback: FeedbackRow[] };

const PAGE = 30;
const CATEGORY_LABEL: Record<Category, string> = { idea: "Idea", bug: "Bug report", contact: "Contact" };
const CATEGORY_TONE: Record<Category, "info" | "good" | "warn" | "bad"> = { idea: "good", bug: "bad", contact: "info" };
const STATUS_LABEL: Record<Status, string> = { new: "New", read: "Read", resolved: "Resolved" };
const STATUS_TONE: Record<Status, "info" | "good" | "warn" | "bad"> = { new: "warn", read: "info", resolved: "good" };
/** Context keys in the order they are worth reading, with a label. */
const CONTEXT_LABELS: readonly [string, string][] = [
  ["screen", "Screen"],
  ["phase", "Game phase"],
  ["mode", "Mode"],
  ["stage", "Stage"],
  ["ship", "Ship"],
  ["quality", "Graphics"],
  ["online", "Online"],
  ["version", "Game version"],
  ["saveVersion", "Save version"],
  ["page", "Page"],
  ["viewport", "Window"],
  ["language", "Language"],
  ["userAgent", "Browser"],
];

export function renderAdminV2Feedback(): HTMLElement {
  const page = el("div", "pl-page");
  page.append(
    createAdminPageHeader({
      eyebrow: "Online · Players",
      title: "Player Feedback",
      subtitle: "Ideas, bug reports and contact messages sent from the game. A report carries the screen, stage, ship, browser and recent errors when the player allowed it.",
    }),
  );
  const status = el("div");
  const stats = el("div", "pl-stats");
  const layout = el("div", "pl-layout");
  const listSide = el("div", "pl-list-side");
  const detailSide = el("div", "pl-detail-side");
  layout.append(listSide, detailSide);
  page.append(status, stats, layout);

  let statusFilter: Status | "open" | "" = "open";
  let categoryFilter: Category | "" = "";
  let query = "";
  let offset = 0;
  let selected: string | null = null;
  let rows: FeedbackRow[] = [];

  function flash(message: string, tone: "good" | "bad"): void {
    const note = el("div", "stx-notice " + tone, message);
    status.replaceChildren(note);
    window.setTimeout(() => note.isConnected && note.remove(), 6000);
  }

  // ---------- Filters ----------
  const search = el("input", "st-admin-v2-search");
  search.type = "search";
  search.placeholder = "Words in the message, pilot name, email or account id…";
  search.setAttribute("aria-label", "Search feedback");
  const statusSelect = el("select", "pl-select");
  for (const [value, label] of [["open", "Open (new + read)"], ["new", "New"], ["read", "Read"], ["resolved", "Resolved"], ["", "All"]]) statusSelect.append(new Option(label, value));
  const categorySelect = el("select", "pl-select");
  for (const [value, label] of [["", "All kinds"], ["bug", "Bug reports"], ["idea", "Ideas"], ["contact", "Contact"]]) categorySelect.append(new Option(label, value));
  const filters = el("div", "st-admin-v2-filter-bar pl-filters");
  filters.append(search, statusSelect, categorySelect, button("Refresh", () => void loadList()));
  const table = el("div", "pl-table-wrap");
  const pager = el("div", "pl-pager");
  listSide.append(filters, table, pager);

  let searchTimer = 0;
  search.addEventListener("input", () => {
    window.clearTimeout(searchTimer);
    searchTimer = window.setTimeout(() => {
      query = search.value.trim();
      offset = 0;
      void loadList();
    }, 250);
  });
  statusSelect.addEventListener("change", () => {
    statusFilter = statusSelect.value as Status | "open" | "";
    offset = 0;
    void loadList();
  });
  categorySelect.addEventListener("change", () => {
    categoryFilter = categorySelect.value as Category | "";
    offset = 0;
    void loadList();
  });

  function renderStats(counts: Record<Status, number>): void {
    stats.replaceChildren(
      ...(["new", "read", "resolved"] as const).map((key) => {
        const card = el("button", "pl-stat");
        card.type = "button";
        card.append(el("strong", undefined, String(counts[key] ?? 0)), el("span", undefined, STATUS_LABEL[key]));
        card.addEventListener("click", () => {
          statusFilter = key;
          statusSelect.value = key;
          offset = 0;
          void loadList();
        });
        return card;
      }),
    );
  }

  async function loadList(): Promise<void> {
    table.replaceChildren(createAdminSkeleton(6));
    const params = new URLSearchParams({ limit: String(PAGE), offset: String(offset) });
    if (statusFilter) params.set("status", statusFilter);
    if (categoryFilter) params.set("category", categoryFilter);
    if (query) params.set("q", query);
    try {
      const data = await getJson<FeedbackList>("/feedback?" + params.toString());
      rows = data.feedback;
      renderStats(data.counts);
      if (rows.length === 0) {
        table.replaceChildren(
          el("div", "pl-empty", query ? "Nothing matches “" + query + "”." : statusFilter === "new" || statusFilter === "open" ? "Nothing waiting. Players send feedback from the Feedback button on the title screen or “Report a bug” in the pause menu." : "No feedback here."),
        );
      } else {
        const grid = el("table", "pl-table");
        const head = el("thead");
        const headRow = el("tr");
        for (const label of ["Sent", "Kind", "From", "Message", "Status"]) headRow.append(el("th", undefined, label));
        head.append(headRow);
        const body = el("tbody");
        for (const row of rows) {
          const tr = el("tr", row.id === selected ? "selected" : "");
          tr.tabIndex = 0;
          const who = el("td", "pl-who");
          who.append(el("strong", undefined, row.display_name ?? "Deleted pilot"), el("small", undefined, row.account_kind === "registered" ? "Registered" : row.account_id === null ? "Account deleted" : "Guest"));
          const preview = row.message.replace(/\s+/g, " ");
          tr.append(
            el("td", undefined, ago(row.created_at)),
            el("td").appendChild(chip(CATEGORY_LABEL[row.category] ?? row.category, CATEGORY_TONE[row.category] ?? "info")).parentElement!,
            who,
            el("td", undefined, preview.length > 90 ? preview.slice(0, 90) + "…" : preview),
            el("td").appendChild(chip(STATUS_LABEL[row.status] ?? row.status, STATUS_TONE[row.status] ?? "info")).parentElement!,
          );
          const open = (): void => {
            selected = row.id;
            for (const other of body.querySelectorAll("tr")) other.classList.toggle("selected", other === tr);
            void openRow(row);
          };
          tr.addEventListener("click", open);
          tr.addEventListener("keydown", (event) => {
            if (event.key === "Enter" || event.key === " ") {
              event.preventDefault();
              open();
            }
          });
          body.append(tr);
        }
        grid.append(head, body);
        table.replaceChildren(grid);
      }
      pager.replaceChildren(
        el("span", undefined, data.total === 0 ? "0 messages" : offset + 1 + "–" + Math.min(data.total, offset + PAGE) + " of " + data.total.toLocaleString()),
        Object.assign(button("Previous", () => {
          offset = Math.max(0, offset - PAGE);
          void loadList();
        }), { disabled: offset === 0 }),
        Object.assign(button("Next", () => {
          offset += PAGE;
          void loadList();
        }), { disabled: offset + PAGE >= data.total }),
      );
      // The open message stays open even when it leaves this filter (read, resolved).
      const still = rows.find((row) => row.id === selected);
      if (still !== undefined) renderDetail(still);
      else if (selected === null) emptyDetail();
    } catch (error) {
      table.replaceChildren(offlineNotice(failure(error)));
      pager.replaceChildren();
    }
  }

  // ---------- Detail ----------
  function emptyDetail(): void {
    detailSide.replaceChildren(el("div", "pl-empty", "Select a message to read it in full, with the game context it was sent from."));
  }

  async function setStatus(row: FeedbackRow, next: Status, note?: string): Promise<void> {
    try {
      await postJson("/feedback/" + row.id + "/status", { status: next, note });
      flash(next === "resolved" ? "Marked resolved." : next === "read" ? "Marked read." : "Moved back to New.", "good");
      row.status = next;
      if (note !== undefined && note.trim() !== "") row.admin_note = note.trim();
      renderDetail(row);
      void loadList();
    } catch (error) {
      flash(failure(error).message, "bad");
    }
  }

  function reply(row: FeedbackRow): void {
    const detail = el("div", "pl-dialog-form");
    const title = textField("Title", { maxLength: 120, placeholder: "Thanks for your report" });
    title.input.value = row.category === "bug" ? "About the problem you reported" : row.category === "idea" ? "Thanks for your idea" : "About your message";
    const body = textField("Message", { maxLength: 600, multiline: true, placeholder: "We fixed it in today's update. Thank you for telling us!" });
    detail.append(title.root, body.root, el("small", undefined, "Arrives in the player's Daily Hub mailbox as a letter, with no reward. The message is then marked resolved."));
    openAdminConfirmDialog({
      title: "Reply to " + (row.display_name ?? "this pilot"),
      message: "A plain in-game letter.",
      confirmLabel: "Send reply",
      detail,
      onConfirm: async () => {
        await postJson("/feedback/" + row.id + "/reply", { title: title.input.value, body: body.input.value });
        flash("Reply sent to the player's mailbox.", "good");
        void loadList();
      },
    });
  }

  function renderDetail(row: FeedbackRow): void {
    const card = panel(CATEGORY_LABEL[row.category] ?? "Message", "Sent " + formatTime(row.created_at) + " · " + ago(row.created_at));
    const head = el("div", "pl-chat-head");
    head.append(
      chip(CATEGORY_LABEL[row.category] ?? row.category, CATEGORY_TONE[row.category] ?? "info"),
      chip(STATUS_LABEL[row.status] ?? row.status, STATUS_TONE[row.status] ?? "info"),
    );
    const message = el("p", "pl-feedback-message", row.message);
    card.body.append(head, message);

    const sender = el("dl", "pl-facts");
    const fact = (label: string, value: string): void => {
      sender.append(el("dt", undefined, label), el("dd", undefined, value));
    };
    fact("Pilot", (row.display_name ?? "Deleted pilot") + (row.pilot_code ? " · " + row.pilot_code : ""));
    fact("Account", row.account_id === null ? "Deleted" : (row.account_kind === "registered" ? "Registered" : "Guest") + " · " + row.account_id + (row.account_status && row.account_status !== "active" ? " (" + row.account_status + ")" : ""));
    fact("Reply to", row.contact_email ?? row.account_email ?? "No email given (reply by in-game mail)");
    if (row.handled_at) fact("Handled", formatTime(row.handled_at) + (row.handled_by ? " by " + row.handled_by : ""));
    if (row.admin_note) fact("Admin note", row.admin_note);
    card.body.append(el("h3", "pl-sub", "Sender"), sender);

    const context = el("dl", "pl-facts");
    let shown = 0;
    for (const [key, label] of CONTEXT_LABELS) {
      const value = row.context[key];
      if (value === undefined || value === null || value === "") continue;
      context.append(el("dt", undefined, label), el("dd", undefined, String(value)));
      shown += 1;
    }
    const errors = Array.isArray(row.context.errors) ? (row.context.errors as unknown[]).map(String) : [];
    card.body.append(el("h3", "pl-sub", "Game context"));
    card.body.append(shown === 0 ? el("div", "pl-empty", "The player chose not to attach game details.") : context);
    if (errors.length > 0) {
      card.body.append(el("h3", "pl-sub", "Recent errors in the game"));
      const list = el("pre", "pl-feedback-errors", errors.join("\n"));
      card.body.append(list);
    }

    const note = textField("Note for other Admins (optional)", { maxLength: 500, multiline: true, placeholder: "Fixed in build of 20/10; duplicate of …" });
    const actions = el("div", "pl-actions");
    const manage = (label: string, run: () => void): HTMLButtonElement => {
      const node = button(label, run);
      node.dataset["adminPermission"] = "feedback.manage";
      return node;
    };
    if (row.status === "new") actions.append(manage("Mark read", () => void setStatus(row, "read", note.input.value)));
    if (row.status !== "resolved") actions.append(manage("Mark resolved", () => void setStatus(row, "resolved", note.input.value)));
    if (row.status !== "new") actions.append(manage("Move back to New", () => void setStatus(row, "new", note.input.value)));
    if (row.account_id !== null) {
      const answer = manage("Reply by in-game mail", () => reply(row));
      answer.className = "st-admin-btn primary";
      actions.append(answer);
    }
    card.body.append(note.root, actions);
    detailSide.replaceChildren(card.root);
  }

  /** Opening a new message marks it read (as mail does), when this role may. */
  async function openRow(row: FeedbackRow): Promise<void> {
    renderDetail(row);
    if (row.status !== "new") return;
    try {
      await postJson("/feedback/" + row.id + "/status", { status: "read" });
      row.status = "read";
      if (selected === row.id) renderDetail(row);
      void loadList();
    } catch {
      // A read-only role: it stays New for whoever handles it.
    }
  }

  emptyDetail();
  void loadList();
  return page;
}
