import { createAdminPageHeader, createAdminSkeleton } from "./admin-components";
import { openAdminConfirmDialog } from "./admin-dialog";
import {
  ago,
  button,
  chip,
  el,
  failure,
  formatTime,
  getJson,
  offlineNotice,
  panel,
  postJson,
  rewardInputs,
  rewardText,
  textField,
} from "./players-shared";

/**
 * Players: online accounts from the Space Typing online API (Cloudflare Worker + D1).
 * Look up a pilot, see their cloud save, Daily Hub progress, rewards and
 * sessions, and handle support: ban/unban, sign out everywhere, password
 * reset link, restore a save backup, send a compensation gift by mail.
 */
type Stats = Record<"players" | "registered" | "guests" | "banned" | "newToday" | "activeToday" | "activeWeek" | "rewardsToday" | "openReports", number>;
type PlayerRow = {
  id: string;
  kind: "guest" | "registered";
  email: string | null;
  email_verified_at: string | null;
  display_name: string;
  status: "active" | "banned" | "deleted";
  ban_reason: string | null;
  banned_until: string | null;
  chat_muted_until: string | null;
  pilot_code: string;
  created_at: string;
  last_seen_at: string | null;
  highest_stage: number | null;
  credits: number | null;
  save_updated_at: string | null;
};
type Detail = {
  account: PlayerRow & { birth_year: number | null; last_login_at: string | null };
  save: { revision: number; saveVersion: number; bytes: number; device: string | null; updatedAt: string; summary: Record<string, unknown> } | null;
  backups: { id: number; revision: number; reason: string; created_at: string }[];
  liveOps: { data: Record<string, unknown>; updated_at: string } | null;
  ledger: { key: string; source: string; reward: unknown; note: string | null; admin_actor: string | null; created_at: string }[];
  sessions: { id: string; created_at: string; last_seen_at: string; ip: string | null; user_agent: string | null }[];
  mail: { id: string; title: string; reward: unknown; created_at: string; created_by: string; revoked_at: string | null }[];
  wallet?: WalletDetail | null;
};
type Balances = Record<"credits" | "alloy" | "starCrystal" | "quantumCore", number>;
type WalletDetail = {
  phase: number;
  origin: string;
  balances: Balances;
  warp: { current: number; reserve: number };
  warpPending: number;
  held: { key: string; label: string }[];
  maxStage: number;
  earnedToday: Partial<Balances>;
  dailyCap: Partial<Balances>;
  flags: { t: number; code: string; detail?: string }[];
  pendingPurchases?: { o: string; s: string; d: Partial<Balances>; t: number }[];
  today: { day: number; ops: { o: string; k: string; s: string; d: Record<string, number>; w?: number; t: number }[] };
  days: { day: number; totals: Record<string, number> }[];
};

const PAGE = 40;

export function renderAdminV2Players(): HTMLElement {
  const page = el("div", "pl-page");
  page.append(
    createAdminPageHeader({
      eyebrow: "Online · Cloudflare D1",
      title: "Players",
      subtitle: "Look up pilots, their cloud save and Daily Hub progress, and handle support. Every action is permission-checked and written to the audit log.",
    }),
  );
  const status = el("div");
  const stats = el("div", "pl-stats");
  const layout = el("div", "pl-layout");
  const listSide = el("div", "pl-list-side");
  const detailSide = el("div", "pl-detail-side");
  layout.append(listSide, detailSide);
  page.append(status, stats, layout);

  let query = "";
  let statusFilter = "";
  let kindFilter = "";
  let offset = 0;
  let selected: string | null = null;

  // ---------- Stats ----------
  async function loadStats(): Promise<void> {
    try {
      const data = await getJson<Stats>("/stats");
      stats.replaceChildren(
        ...(
          [
            ["Players", data.players],
            ["Registered", data.registered],
            ["Guests", data.guests],
            ["Active today", data.activeToday],
            ["Active 7 days", data.activeWeek],
            ["New today", data.newToday],
            ["Banned", data.banned],
            ["Rewards today", data.rewardsToday],
            ["Open chat reports", data.openReports],
          ] as const
        ).map(([label, value]) => {
          const card = el("div", "pl-stat");
          card.append(el("strong", undefined, value.toLocaleString()), el("span", undefined, label));
          return card;
        }),
      );
      status.replaceChildren();
    } catch (error) {
      status.replaceChildren(offlineNotice(failure(error)));
      stats.replaceChildren();
    }
  }

  // ---------- List ----------
  const search = el("input", "st-admin-v2-search");
  search.type = "search";
  search.placeholder = "Name, email or player id…";
  search.setAttribute("aria-label", "Search players");
  const statusSelect = el("select", "pl-select");
  for (const [value, label] of [["", "Not deleted"], ["active", "Active"], ["banned", "Banned"], ["deleted", "Deleted"]]) statusSelect.append(new Option(label, value));
  const kindSelect = el("select", "pl-select");
  for (const [value, label] of [["", "All kinds"], ["registered", "Registered"], ["guest", "Guests"]]) kindSelect.append(new Option(label, value));
  const filters = el("div", "st-admin-v2-filter-bar pl-filters");
  filters.append(search, statusSelect, kindSelect);
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
    statusFilter = statusSelect.value;
    offset = 0;
    void loadList();
  });
  kindSelect.addEventListener("change", () => {
    kindFilter = kindSelect.value;
    offset = 0;
    void loadList();
  });

  async function loadList(): Promise<void> {
    table.replaceChildren(createAdminSkeleton(6));
    const params = new URLSearchParams({ limit: String(PAGE), offset: String(offset) });
    if (query) params.set("q", query);
    if (statusFilter) params.set("status", statusFilter);
    if (kindFilter) params.set("kind", kindFilter);
    try {
      const data = await getJson<{ total: number; players: PlayerRow[] }>("/players?" + params.toString());
      if (data.players.length === 0) {
        table.replaceChildren(el("div", "pl-empty", query ? "No pilot matches “" + query + "”." : "No players yet. They appear here after their first visit."));
      } else {
        const grid = el("table", "pl-table");
        const head = el("thead");
        const headRow = el("tr");
        for (const label of ["Pilot", "Kind", "Status", "Stage", "Credits", "Last seen"]) headRow.append(el("th", undefined, label));
        head.append(headRow);
        const body = el("tbody");
        for (const row of data.players) {
          const tr = el("tr", row.id === selected ? "selected" : "");
          tr.tabIndex = 0;
          const who = el("td", "pl-who");
          who.append(el("strong", undefined, row.display_name), el("small", undefined, row.email ?? row.id.slice(0, 8)));
          tr.append(
            who,
            el("td").appendChild(chip(row.kind === "registered" ? "Registered" : "Guest", row.kind === "registered" ? "good" : "info")).parentElement!,
            el("td").appendChild(chip(row.status, row.status === "active" ? "good" : row.status === "banned" ? "bad" : "warn")).parentElement!,
            el("td", "num", row.highest_stage === null ? "—" : String(row.highest_stage)),
            el("td", "num", row.credits === null ? "—" : Number(row.credits).toLocaleString()),
            el("td", undefined, ago(row.last_seen_at ?? row.created_at)),
          );
          const open = (): void => {
            selected = row.id;
            for (const other of body.querySelectorAll("tr")) other.classList.toggle("selected", other === tr);
            void loadDetail(row.id);
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
        el("span", undefined, data.total === 0 ? "0 players" : offset + 1 + "–" + Math.min(data.total, offset + PAGE) + " of " + data.total.toLocaleString()),
        Object.assign(button("Previous", () => {
          offset = Math.max(0, offset - PAGE);
          void loadList();
        }), { disabled: offset === 0 }),
        Object.assign(button("Next", () => {
          offset += PAGE;
          void loadList();
        }), { disabled: offset + PAGE >= data.total }),
      );
    } catch (error) {
      table.replaceChildren(offlineNotice(failure(error)));
      pager.replaceChildren();
    }
  }

  // ---------- Detail ----------
  function emptyDetail(): void {
    detailSide.replaceChildren(el("div", "pl-empty", "Select a pilot to see their account, cloud save, rewards and sessions."));
  }

  async function action(label: string, run: () => Promise<unknown>, id: string): Promise<void> {
    try {
      await run();
      flash(label, "good");
      await Promise.all([loadDetail(id), loadList(), loadStats()]);
    } catch (error) {
      flash(failure(error).message, "bad");
    }
  }

  function flash(message: string, tone: "good" | "bad"): void {
    const note = el("div", "stx-notice " + tone, message);
    note.setAttribute("role", tone === "bad" ? "alert" : "status");
    status.replaceChildren(note);
    window.setTimeout(() => {
      if (note.isConnected) note.remove();
    }, 6000);
  }

  async function loadDetail(id: string): Promise<void> {
    detailSide.replaceChildren(createAdminSkeleton(8));
    let detail: Detail;
    try {
      detail = await getJson<Detail>("/players/" + id);
    } catch (error) {
      detailSide.replaceChildren(offlineNotice(failure(error)));
      return;
    }
    const a = detail.account;
    const card = panel(a.display_name, a.email ?? "Guest account · " + a.id);
    const facts = el("dl", "pl-facts");
    const fact = (term: string, value: string | Node): void => {
      const dd = el("dd");
      dd.append(value);
      facts.append(el("dt", undefined, term), dd);
    };
    fact("Player id", el("code", undefined, a.id));
    fact("Kind", a.kind === "registered" ? "Registered" + (a.email_verified_at ? " · email verified" : " · email not verified") : "Guest (device key)");
    fact("Status", chip(a.status + (a.ban_reason ? " · " + a.ban_reason : "") + (a.banned_until ? " until " + formatTime(a.banned_until) : ""), a.status === "active" ? "good" : "bad"));
    fact("Pilot code", el("code", undefined, a.pilot_code));
    if (a.chat_muted_until !== null && new Date(a.chat_muted_until).getTime() > Date.now()) fact("Chat", chip("Muted until " + formatTime(a.chat_muted_until), "warn"));
    fact("Birth year", a.birth_year === null ? "—" : String(a.birth_year) + (new Date().getFullYear() - a.birth_year < 18 ? " (under 18)" : ""));
    fact("Created", formatTime(a.created_at));
    fact("Last sign-in", formatTime(a.last_login_at));
    fact("Last seen", ago(a.last_seen_at));
    card.body.append(facts);

    const actions = el("div", "pl-actions");
    if (a.status === "banned") {
      actions.append(button("Unban", () => void action("Player unbanned.", () => postJson("/players/" + id + "/unban"), id), "st-admin-btn primary"));
    } else if (a.status === "active") {
      actions.append(button("Ban…", () => openBan(id, a.display_name), "st-admin-btn st-admin-v2-danger-action"));
    }
    const muted = a.chat_muted_until !== null && new Date(a.chat_muted_until).getTime() > Date.now();
    actions.append(
      muted
        ? button("Unmute chat", () => void action("Chat unmuted.", () => postJson("/players/" + id + "/mute", { minutes: 0 }), id))
        : button("Mute chat…", () => openMute(id, a.display_name)),
    );
    actions.append(
      button("Sign out everywhere", () =>
        openAdminConfirmDialog({
          title: "Sign out every device?",
          message: a.display_name + " will have to sign in again on every device. Progress is kept.",
          confirmLabel: "Sign out",
          onConfirm: () => action("Sessions revoked.", () => postJson("/players/" + id + "/sessions/revoke"), id),
        }),
      ),
    );
    if (a.kind === "registered" && a.status !== "deleted") {
      actions.append(
        button("Password reset link", async () => {
          try {
            const result = await postJson<{ link: string }>("/players/" + id + "/password-reset-link");
            const box = el("div", "stx-notice good pl-link");
            const input = el("input");
            input.readOnly = true;
            input.value = result.link;
            box.append(el("span", undefined, "Link (also sent by email, valid 1 hour): "), input, button("Copy", () => void navigator.clipboard?.writeText(result.link)));
            status.replaceChildren(box);
          } catch (error) {
            flash(failure(error).message, "bad");
          }
        }),
      );
    }
    card.body.append(actions);

    // Save
    const savePanel = panel("Cloud save", detail.save ? "Revision " + detail.save.revision + " · " + (detail.save.bytes / 1024).toFixed(0) + " KB · " + formatTime(detail.save.updatedAt) : "No cloud save yet");
    if (detail.save !== null) {
      const summary = detail.save.summary;
      const grid = el("div", "pl-mini-grid");
      for (const [label, key] of [
        ["Highest stage", "highestUnlockedStage"],
        ["Stages cleared", "clearedStages"],
        ["Credits", "credits"],
        ["Alloy", "alloy"],
        ["Star Crystal", "starCrystal"],
        ["Quantum Core", "quantumCore"],
        ["Ship", "selectedShip"],
      ] as const) {
        const value = summary[key];
        const item = el("div", "pl-mini");
        item.append(el("span", undefined, label), el("strong", undefined, value === null || value === undefined ? "—" : typeof value === "number" ? value.toLocaleString() : String(value)));
        grid.append(item);
      }
      savePanel.body.append(grid);
      savePanel.body.append(
        button("Download save JSON", async () => {
          try {
            const save = await getJson<unknown>("/players/" + id + "/save");
            const blob = new Blob([JSON.stringify(save, null, 2)], { type: "application/json" });
            const link = el("a");
            link.href = URL.createObjectURL(blob);
            link.download = "space-typing-save-" + id.slice(0, 8) + ".json";
            link.click();
            URL.revokeObjectURL(link.href);
          } catch (error) {
            flash(failure(error).message, "bad");
          }
        }),
      );
    }
    if (detail.backups.length > 0) {
      const list = el("ul", "pl-backups");
      for (const backup of detail.backups) {
        const item = el("li");
        item.append(
          el("span", undefined, "Revision " + backup.revision + " · " + backup.reason + " · " + formatTime(backup.created_at)),
          button("Restore", () =>
            openAdminConfirmDialog({
              title: "Restore this cloud save?",
              message:
                "The current cloud save is kept as a backup first. The player's game loads the restored save the next time it syncs; ask them to reopen the game.",
              tone: "danger",
              confirmLabel: "Restore revision " + backup.revision,
              onConfirm: () => action("Save restored.", () => postJson("/players/" + id + "/save/restore", { backupId: backup.id }), id),
            }),
          ),
        );
        list.append(item);
      }
      savePanel.body.append(el("h3", "pl-sub", "Backups"), list);
    }

    // Server wallet (docs/ONLINE_SERVER_WALLET_DESIGN_2026-10-16.md)
    const wallet = detail.wallet ?? null;
    const walletPanel = panel(
      "Server wallet",
      wallet === null ? "No server wallet yet (opens on the player's next online visit)" : "Phase " + wallet.phase + " · created from " + wallet.origin + " · highest stage " + wallet.maxStage,
    );
    if (wallet !== null) {
      const grid = el("div", "pl-mini-grid");
      const rows: [string, string][] = [
        ["Credits", wallet.balances.credits.toLocaleString()],
        ["Alloy", wallet.balances.alloy.toLocaleString()],
        ["Star Crystal", wallet.balances.starCrystal.toLocaleString()],
        ["Quantum Core", wallet.balances.quantumCore.toLocaleString()],
        ["Warp", wallet.warp.current + " + " + wallet.warp.reserve + " reserve" + (wallet.warpPending > 0 ? " (+" + wallet.warpPending + " waiting)" : "")],
        ["Earned today", (wallet.earnedToday.credits ?? 0).toLocaleString() + " / " + (wallet.dailyCap.credits ?? 0).toLocaleString() + " Credits"],
        ["Held rewards", wallet.held.length === 0 ? "—" : wallet.held.map((item) => item.label).join(", ") + " (email not verified)"],
      ];
      for (const [label, value] of rows) {
        const item = el("div", "pl-mini");
        item.append(el("span", undefined, label), el("strong", undefined, value));
        grid.append(item);
      }
      walletPanel.body.append(grid);
      if (wallet.flags.length > 0) {
        const flags = el("ul", "pl-backups");
        for (const item of wallet.flags.slice(-10).reverse()) flags.append(el("li", undefined, formatTime(new Date(item.t).toISOString()) + " · " + item.code + (item.detail ? " · " + item.detail : "")));
        walletPanel.body.append(el("h3", "pl-sub", "Flags (" + wallet.flags.length + ")"), flags);
      }
      const ops = wallet.today.ops.slice(-30).reverse();
      if (ops.length > 0) {
        const t = el("table", "pl-table compact");
        const hr = el("tr");
        for (const label of ["When", "Kind", "Source", "Change"]) hr.append(el("th", undefined, label));
        t.append(el("thead").appendChild(hr).parentElement!);
        const tb = el("tbody");
        for (const row of ops) {
          const change = Object.entries(row.d).map(([key, value]) => (value > 0 ? "+" : "") + value.toLocaleString() + " " + key);
          if (row.w) change.push((row.w > 0 ? "+" : "") + row.w + " Warp");
          const tr = el("tr");
          tr.append(el("td", undefined, formatTime(new Date(row.t).toISOString())), el("td", undefined, row.k), el("td", "pl-key", row.s), el("td", undefined, change.join(" · ") || "—"));
          tb.append(tr);
        }
        t.append(tb);
        walletPanel.body.append(el("h3", "pl-sub", "Today's ledger"), el("div", "pl-table-wrap short").appendChild(t).parentElement!);
      }
      if (wallet.days.length > 0) {
        const list = el("ul", "pl-backups");
        for (const day of wallet.days) {
          list.append(el("li", undefined, "Day " + day.day + " · " + (Object.entries(day.totals).map(([key, value]) => (value > 0 ? "+" : "") + value.toLocaleString() + " " + key).join(" · ") || "no change")));
        }
        walletPanel.body.append(el("h3", "pl-sub", "Earlier days (kept 90 days)"), list);
      }
      // Correction: signed amounts, with a reason (Players: save permission; written to both audit logs).
      for (const pending of wallet.pendingPurchases ?? []) {
        const row = el("div", "pl-dialog-form");
        row.append(el("p", undefined, "Pending purchase · " + pending.o + " · " + pending.s + " · " + formatTime(new Date(pending.t).toISOString()) + " · " + JSON.stringify(pending.d)));
        const why = textField("Reason", { placeholder: "Explain why this purchase should be settled", maxLength: 300 });
        row.append(why.root);
        for (const purchaseAction of ["refund", "confirm"] as const) row.append(button(purchaseAction === "refund" ? "Refund…" : "Confirm saved…", () => {
          if (!why.input.value.trim()) return flash("A reason is required.", "bad");
          const reason = why.input.value.trim();
          const idempotencyKey = crypto.randomUUID();
          openAdminConfirmDialog({
            title: purchaseAction === "refund" ? "Refund this purchase?" : "Confirm this purchase was saved?",
            message: pending.o + ". Reason: " + reason,
            tone: "danger", confirmLabel: purchaseAction === "refund" ? "Refund" : "Confirm",
            onConfirm: () => action("Purchase settled.", () => postJson("/players/" + id + "/wallet", { purchaseAction, spendOpId: pending.o, reason, idempotencyKey }), id),
          });
        }));
        walletPanel.body.append(row);
      }
      const form = el("div", "pl-dialog-form");
      const amount = (label: string): HTMLInputElement => {
        const input = el("input");
        input.type = "number";
        input.step = "1";
        input.placeholder = label + " (+/−)";
        input.setAttribute("aria-label", label);
        form.append(input);
        return input;
      };
      const fields = { credits: amount("Credits"), alloy: amount("Alloy"), starCrystal: amount("Star Crystal"), quantumCore: amount("Quantum Core") };
      const warpField = amount("Warp");
      const reason = textField("Reason", { placeholder: "Refund for a lost purchase", maxLength: 300 });
      form.append(reason.root);
      walletPanel.body.append(el("h3", "pl-sub", "Correct the wallet"), form);
      walletPanel.body.append(
        button("Apply correction…", () => {
          const deltas: Record<string, number> = {};
          for (const [key, input] of Object.entries(fields)) {
            const value = Math.trunc(Number(input.value) || 0);
            if (value !== 0) deltas[key] = value;
          }
          const warp = Math.trunc(Number(warpField.value) || 0);
          if (Object.keys(deltas).length === 0 && warp === 0) return flash("Enter at least one amount.", "bad");
          if (reason.input.value.trim() === "") return flash("A correction needs a reason.", "bad");
          const summary = [...Object.entries(deltas).map(([key, value]) => (value > 0 ? "+" : "") + value + " " + key), ...(warp !== 0 ? [(warp > 0 ? "+" : "") + warp + " Warp"] : [])].join(", ");
          const idempotencyKey = crypto.randomUUID();
          openAdminConfirmDialog({
            title: "Correct " + a.display_name + "'s wallet?",
            message: summary + ". The game takes the new balances on its next sync. Reason: " + reason.input.value.trim(),
            tone: "danger",
            confirmLabel: "Apply",
            onConfirm: () => action("Wallet corrected.", () => postJson("/players/" + id + "/wallet", { deltas, warp, reason: reason.input.value, idempotencyKey }), id),
          });
        }, "st-admin-btn st-admin-v2-danger-action"),
      );
    }

    // Daily Hub
    const live = detail.liveOps?.data as
      | { streak?: { count?: number; best?: number; goal?: number; shields?: number }; newbie?: { claimed?: number }; monthly?: { claimed?: number; month?: string }; daily?: { counters?: { words?: number; activeSeconds?: number } }; inbox?: { title: string; claimed: boolean }[] }
      | undefined;
    const livePanel = panel("Daily Hub", detail.liveOps ? "Updated " + ago(detail.liveOps.updated_at) : "Not opened yet");
    if (live !== undefined) {
      const grid = el("div", "pl-mini-grid");
      const rows: [string, string][] = [
        ["Streak", (live.streak?.count ?? 0) + " days (best " + (live.streak?.best ?? 0) + ")"],
        ["Daily goal", String(live.streak?.goal ?? 100) + " words"],
        ["Shields", String(live.streak?.shields ?? 0)],
        ["Starter week", (live.newbie?.claimed ?? 0) + " / 7"],
        ["Monthly", (live.monthly?.claimed ?? 0) + " / 28 · " + (live.monthly?.month ?? "")],
        ["Today", (live.daily?.counters?.words ?? 0) + " words · " + Math.floor((live.daily?.counters?.activeSeconds ?? 0) / 60) + " min"],
        ["Mail", (live.inbox ?? []).filter((m) => !m.claimed).length + " unclaimed"],
      ];
      for (const [label, value] of rows) {
        const item = el("div", "pl-mini");
        item.append(el("span", undefined, label), el("strong", undefined, value));
        grid.append(item);
      }
      livePanel.body.append(grid);
    }

    // Gift by mail
    const giftPanel = panel("Send a gift or compensation", "Arrives in the player's Daily Hub mailbox; they claim it in game.");
    const title = textField("Title", { placeholder: "Sorry for the outage", maxLength: 120 });
    const body = textField("Message", { placeholder: "Here is a small gift…", maxLength: 600, multiline: true });
    const reward = rewardInputs();
    giftPanel.body.append(title.root, body.root, reward.root);
    giftPanel.body.append(
      button("Send gift…", () => {
        const amounts = reward.read();
        if (title.input.value.trim() === "") return flash("Give the mail a title.", "bad");
        openAdminConfirmDialog({
          title: "Send this mail to " + a.display_name + "?",
          message: "Reward: " + rewardText(amounts) + ". This cannot be taken back after the player claims it.",
          confirmLabel: "Send",
          onConfirm: () =>
            action("Gift sent.", async () => {
              await postJson("/players/" + id + "/mail", { title: title.input.value, body: body.input.value, reward: amounts });
              title.input.value = "";
              body.input.value = "";
              reward.reset();
            }, id),
        });
      }, "st-admin-btn primary"),
    );

    // Ledger
    const ledgerPanel = panel("Rewards granted", "Each key is paid once (Daily Hub claims, mail, codes).");
    if (detail.ledger.length === 0) ledgerPanel.body.append(el("div", "pl-empty", "No rewards yet."));
    else {
      const t = el("table", "pl-table compact");
      const hr = el("tr");
      for (const label of ["When", "Source", "Reward", "Key"]) hr.append(el("th", undefined, label));
      t.append(el("thead").appendChild(hr).parentElement!);
      const tb = el("tbody");
      for (const row of detail.ledger) {
        const tr = el("tr");
        tr.append(el("td", undefined, formatTime(row.created_at)), el("td", undefined, row.source), el("td", undefined, rewardText(row.reward)), el("td", "pl-key", row.key));
        tb.append(tr);
      }
      t.append(tb);
      ledgerPanel.body.append(el("div", "pl-table-wrap short").appendChild(t).parentElement!);
    }

    // Sessions
    const sessionPanel = panel("Signed-in devices", detail.sessions.length + " active");
    for (const session of detail.sessions) {
      const row = el("div", "pl-session");
      row.append(el("strong", undefined, (session.user_agent ?? "Unknown browser").slice(0, 70)), el("small", undefined, (session.ip ?? "?") + " · last seen " + ago(session.last_seen_at)));
      sessionPanel.body.append(row);
    }

    detailSide.replaceChildren(card.root, walletPanel.root, savePanel.root, livePanel.root, giftPanel.root, ledgerPanel.root, sessionPanel.root);
  }

  function openMute(id: string, name: string): void {
    const detail = el("div", "pl-dialog-form");
    const minutes = el("select", "pl-select");
    for (const [value, label] of [["60", "1 hour"], ["1440", "1 day"], ["10080", "7 days"], ["43200", "30 days"]]) minutes.append(new Option(label, value));
    const reason = textField("Reason", { placeholder: "Spam in world chat", maxLength: 200 });
    detail.append(minutes, reason.root);
    openAdminConfirmDialog({
      title: "Mute " + name + " in chat?",
      message: "They can still read chat and play. They are removed from the world room at once.",
      confirmLabel: "Mute",
      detail,
      onConfirm: () => action("Player muted.", () => postJson("/players/" + id + "/mute", { minutes: Number(minutes.value), reason: reason.input.value }), id),
    });
  }

  function openBan(id: string, name: string): void {
    const detail = el("div", "pl-dialog-form");
    const reason = textField("Reason (shown to the player)", { placeholder: "Cheating: modified save", maxLength: 300 });
    const until = textField("Until (empty = permanent)", { type: "datetime-local" });
    detail.append(reason.root, until.root);
    openAdminConfirmDialog({
      title: "Ban " + name + "?",
      message: "They are signed out at once and cannot sign in until unbanned.",
      tone: "danger",
      confirmLabel: "Ban player",
      detail,
      onConfirm: () =>
        action("Player banned.", () => {
          const value = (until.input as HTMLInputElement).value;
          return postJson("/players/" + id + "/ban", { reason: reason.input.value, until: value ? new Date(value).toISOString() : "" });
        }, id),
    });
  }

  emptyDetail();
  void loadStats();
  void loadList();
  return page;
}
