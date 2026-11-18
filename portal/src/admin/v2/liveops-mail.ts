import { createAdminPageHeader, createAdminSkeleton } from "./admin-components";
import { openAdminConfirmDialog } from "./admin-dialog";
import {
  button,
  chip,
  el,
  failure,
  formatTime,
  getJson,
  localToIso,
  offlineNotice,
  panel,
  postJson,
  rewardInputs,
  rewardText,
  textField,
} from "./players-shared";

/**
 * Mail & Gift Codes: Daily Hub mail to every player (patch gifts, event
 * announcements) and gift codes. Players claim both in the game's mailbox;
 * the account service pays each one once per player (reward ledger).
 * Also shows the email outbox (local development has no SMTP: verification
 * and reset links are read here) and the account service audit.
 */
type Mail = { id: string; target_name: string | null; target_account_id: string | null; title: string; body: string; reward: unknown; starts_at: string; ends_at: string | null; created_by: string; created_at: string; revoked_at: string | null; claimed: number };
type Code = { id: string; code_hint: string; title: string; reward: unknown; max_redemptions: number | null; redeemed_count: number; starts_at: string; ends_at: string | null; created_by: string; disabled_at: string | null };
type Email = { id: number; to_email: string; subject: string; body: string; created_at: string };
type AuditEntry = { id: number; actor: string; action: string; target: string | null; details: unknown; created_at: string };

function windowText(start: string, end: string | null): string {
  return formatTime(start) + " → " + (end ? formatTime(end) : "no end");
}

function liveState(start: string, end: string | null, revoked: string | null): HTMLElement {
  const now = Date.now();
  if (revoked) return chip("Revoked", "bad");
  if (new Date(start).getTime() > now) return chip("Scheduled", "info");
  if (end !== null && new Date(end).getTime() <= now) return chip("Ended", "warn");
  return chip("Live", "good");
}

function randomCode(): string {
  const alphabet = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789";
  const bytes = crypto.getRandomValues(new Uint8Array(10));
  const chars = [...bytes].map((byte) => alphabet[byte % alphabet.length]).join("");
  return "ST-" + chars.slice(0, 5) + "-" + chars.slice(5);
}

export function renderAdminV2LiveopsMail(): HTMLElement {
  const page = el("div", "pl-page");
  page.append(
    createAdminPageHeader({
      eyebrow: "Online · Live Ops",
      title: "Mail & Gift Codes",
      subtitle: "Send gifts and announcements to every player, and create gift codes. Rewards are paid once per player and recorded in the reward ledger.",
    }),
  );
  const status = el("div");
  const columns = el("div", "pl-two");
  const left = el("div", "pl-stack");
  const right = el("div", "pl-stack");
  columns.append(left, right);
  page.append(status, columns);

  function flash(message: string, tone: "good" | "bad"): void {
    const note = el("div", "stx-notice " + tone, message);
    status.replaceChildren(note);
    window.setTimeout(() => note.isConnected && note.remove(), 6000);
  }

  // ---------- Broadcast mail ----------
  const send = panel("Mail to every player", "Shown in the Daily Hub mailbox between the start and end time.");
  const title = textField("Title", { placeholder: "Weekend supply drop", maxLength: 120 });
  const body = textField("Message", { placeholder: "Thanks for flying with us!", maxLength: 600, multiline: true });
  const reward = rewardInputs();
  const timing = el("div", "pl-reward-grid");
  const starts = textField("Starts (empty = now)", { type: "datetime-local" });
  const ends = textField("Ends (empty = no end)", { type: "datetime-local" });
  timing.append(starts.root, ends.root);
  send.body.append(title.root, body.root, reward.root, timing);
  send.body.append(
    button("Send to everyone…", () => {
      if (title.input.value.trim() === "") return flash("Give the mail a title.", "bad");
      const amounts = reward.read();
      openAdminConfirmDialog({
        title: "Send to every player?",
        message: "“" + title.input.value.trim() + "” · " + rewardText(amounts) + ". Players who already claimed it keep the reward even if you revoke it later.",
        tone: "danger",
        confirmLabel: "Send to everyone",
        onConfirm: async () => {
          try {
            await postJson("/mail", {
              target: "all",
              title: title.input.value,
              body: body.input.value,
              reward: amounts,
              startsAt: localToIso((starts.input as HTMLInputElement).value),
              endsAt: localToIso((ends.input as HTMLInputElement).value),
            });
            title.input.value = "";
            body.input.value = "";
            reward.reset();
            flash("Mail sent.", "good");
            void loadMail();
          } catch (error) {
            flash(failure(error).message, "bad");
          }
        },
      });
    }, "st-admin-btn primary"),
  );
  const mailList = panel("Sent mail", "Newest first. Claimed = players who collected the reward.");
  const mailBody = el("div", "pl-table-wrap");
  mailList.body.append(mailBody);
  left.append(send.root, mailList.root);

  async function loadMail(): Promise<void> {
    mailBody.replaceChildren(createAdminSkeleton(4));
    try {
      const { mail } = await getJson<{ mail: Mail[] }>("/mail");
      if (mail.length === 0) {
        mailBody.replaceChildren(el("div", "pl-empty", "No mail sent yet."));
        return;
      }
      const table = el("table", "pl-table compact");
      const hr = el("tr");
      for (const label of ["Title", "To", "Reward", "Window", "Claimed", "", ""]) hr.append(el("th", undefined, label));
      table.append(el("thead").appendChild(hr).parentElement!);
      const tbody = el("tbody");
      for (const item of mail) {
        const tr = el("tr");
        const state = el("td");
        state.append(liveState(item.starts_at, item.ends_at, item.revoked_at));
        const actions = el("td");
        if (item.revoked_at === null) {
          actions.append(
            button("Revoke", () =>
              openAdminConfirmDialog({
                title: "Revoke this mail?",
                message: "Players who have not claimed it yet will no longer receive it.",
                tone: "danger",
                confirmLabel: "Revoke",
                onConfirm: async () => {
                  try {
                    await postJson("/mail/" + item.id + "/revoke");
                    void loadMail();
                  } catch (error) {
                    flash(failure(error).message, "bad");
                  }
                },
              }),
            ),
          );
        }
        tr.append(
          el("td", undefined, item.title),
          el("td", undefined, item.target_account_id ? item.target_name ?? item.target_account_id.slice(0, 8) : "Everyone"),
          el("td", undefined, rewardText(item.reward)),
          el("td", undefined, windowText(item.starts_at, item.ends_at)),
          el("td", "num", String(item.claimed)),
          state,
          actions,
        );
        tbody.append(tr);
      }
      table.append(tbody);
      mailBody.replaceChildren(table);
    } catch (error) {
      mailBody.replaceChildren(offlineNotice(failure(error)));
    }
  }

  // ---------- Gift codes ----------
  const create = panel("New gift code", "Players type the code in Daily Hub → Mail. Codes are stored hashed; copy it now.");
  const codeRow = el("div", "pl-inline");
  const code = textField("Code", { placeholder: "ST-XXXXX-XXXXX", maxLength: 40 });
  (code.input as HTMLInputElement).style.textTransform = "uppercase";
  codeRow.append(code.root, button("Generate", () => {
    code.input.value = randomCode();
  }));
  const codeTitle = textField("Mail title", { placeholder: "Launch gift", maxLength: 120 });
  const codeBody = textField("Mail message", { maxLength: 600, multiline: true });
  const codeReward = rewardInputs();
  const codeLimits = el("div", "pl-reward-grid");
  const maxUses = textField("Max uses (empty = unlimited)", { type: "number" });
  const codeStart = textField("Starts (empty = now)", { type: "datetime-local" });
  const codeEnd = textField("Ends (empty = no end)", { type: "datetime-local" });
  codeLimits.append(maxUses.root, codeStart.root, codeEnd.root);
  create.body.append(codeRow, codeTitle.root, codeBody.root, codeReward.root, codeLimits);
  create.body.append(
    button("Create code", async () => {
      try {
        const result = await postJson<{ id: string; code: string }>("/gift-codes", {
          code: code.input.value,
          title: codeTitle.input.value,
          body: codeBody.input.value,
          reward: codeReward.read(),
          maxRedemptions: maxUses.input.value === "" ? null : Number(maxUses.input.value),
          startsAt: localToIso((codeStart.input as HTMLInputElement).value),
          endsAt: localToIso((codeEnd.input as HTMLInputElement).value),
        });
        flash("Code " + result.code + " created. It is stored hashed and cannot be shown again.", "good");
        code.input.value = "";
        codeReward.reset();
        void loadCodes();
      } catch (error) {
        flash(failure(error).message, "bad");
      }
    }, "st-admin-btn primary"),
  );
  const codeList = panel("Gift codes");
  const codeBodyList = el("div", "pl-table-wrap");
  codeList.body.append(codeBodyList);
  right.append(create.root, codeList.root);

  async function loadCodes(): Promise<void> {
    codeBodyList.replaceChildren(createAdminSkeleton(3));
    try {
      const { codes } = await getJson<{ codes: Code[] }>("/gift-codes");
      if (codes.length === 0) {
        codeBodyList.replaceChildren(el("div", "pl-empty", "No gift codes yet."));
        return;
      }
      const table = el("table", "pl-table compact");
      const hr = el("tr");
      for (const label of ["Code", "Title", "Reward", "Uses", "Window", "", ""]) hr.append(el("th", undefined, label));
      table.append(el("thead").appendChild(hr).parentElement!);
      const tbody = el("tbody");
      for (const item of codes) {
        const tr = el("tr");
        const state = el("td");
        state.append(item.disabled_at ? chip("Disabled", "bad") : item.max_redemptions !== null && item.redeemed_count >= item.max_redemptions ? chip("Used up", "warn") : liveState(item.starts_at, item.ends_at, null));
        const actions = el("td");
        if (item.disabled_at === null) {
          actions.append(
            button("Disable", async () => {
              try {
                await postJson("/gift-codes/" + item.id + "/disable");
                void loadCodes();
              } catch (error) {
                flash(failure(error).message, "bad");
              }
            }),
          );
        }
        tr.append(
          el("td", "pl-key", item.code_hint),
          el("td", undefined, item.title),
          el("td", undefined, rewardText(item.reward)),
          el("td", "num", item.redeemed_count + (item.max_redemptions === null ? "" : " / " + item.max_redemptions)),
          el("td", undefined, windowText(item.starts_at, item.ends_at)),
          state,
          actions,
        );
        tbody.append(tr);
      }
      table.append(tbody);
      codeBodyList.replaceChildren(table);
    } catch (error) {
      codeBodyList.replaceChildren(offlineNotice(failure(error)));
    }
  }

  // ---------- Outbox and audit ----------
  const outbox = panel("Email outbox", "Local development has no mail server: verification and password-reset emails are listed here.");
  const outboxBody = el("div", "pl-outbox");
  outbox.body.append(outboxBody);
  const audit = panel("Account audit", "Every Admin action on players, mail and codes.");
  const auditBody = el("div", "pl-table-wrap short");
  audit.body.append(auditBody);
  right.append(outbox.root, audit.root);

  async function loadOutbox(): Promise<void> {
    try {
      const { emails } = await getJson<{ emails: Email[] }>("/outbox");
      outboxBody.replaceChildren(
        ...(emails.length === 0
          ? [el("div", "pl-empty", "No emails yet.")]
          : emails.slice(0, 20).map((email) => {
              const details = el("details", "pl-email");
              details.append(el("summary", undefined, formatTime(email.created_at) + " · " + email.to_email + " · " + email.subject), el("pre", undefined, email.body));
              return details;
            })),
      );
    } catch (error) {
      outboxBody.replaceChildren(offlineNotice(failure(error)));
    }
  }

  async function loadAudit(): Promise<void> {
    try {
      const { entries } = await getJson<{ entries: AuditEntry[] }>("/audit");
      if (entries.length === 0) {
        auditBody.replaceChildren(el("div", "pl-empty", "No actions yet."));
        return;
      }
      const table = el("table", "pl-table compact");
      const tbody = el("tbody");
      for (const entry of entries.slice(0, 60)) {
        const tr = el("tr");
        tr.append(el("td", undefined, formatTime(entry.created_at)), el("td", undefined, entry.actor), el("td", "pl-key", entry.action), el("td", "pl-key", entry.target?.slice(0, 8) ?? ""));
        tbody.append(tr);
      }
      table.append(tbody);
      auditBody.replaceChildren(table);
    } catch (error) {
      auditBody.replaceChildren(offlineNotice(failure(error)));
    }
  }

  void loadMail();
  void loadCodes();
  void loadOutbox();
  void loadAudit();
  return page;
}
