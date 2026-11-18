import { createAdminPageHeader, createAdminSkeleton } from "./admin-components";
import { openAdminConfirmDialog } from "./admin-dialog";
import { button, chip, el, failure, formatTime, getJson, offlineNotice, panel, postJson, textField } from "./players-shared";

/**
 * Chat moderation: the world room's recent messages (delete, mute the
 * author), the report queue, and system announcements to world chat.
 * Group and private rooms are opened only from a report.
 */
type Message = { id: string; from: { id: string; name: string; code: string }; text: string; at: number; system?: boolean; deleted?: boolean };
type Report = { id: number; channel: string; message_id: string; target_id: string; target_name: string; text: string; reason: string | null; created_at: string; resolved_at: string | null; resolution: string | null; target_reports: number };

export function renderAdminV2ChatModeration(): HTMLElement {
  const page = el("div", "pl-page");
  page.append(
    createAdminPageHeader({
      eyebrow: "Online · Chat",
      title: "Chat Moderation",
      subtitle: "Read the world room, remove messages, mute players and work through player reports. Links and common profanity are filtered automatically.",
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

  function mute(accountId: string, name: string, after: () => void): void {
    const detail = el("div", "pl-dialog-form");
    const minutes = el("select", "pl-select");
    for (const [value, label] of [["60", "1 hour"], ["1440", "1 day"], ["10080", "7 days"]]) minutes.append(new Option(label, value));
    detail.append(minutes);
    openAdminConfirmDialog({
      title: "Mute " + name + "?",
      message: "They can still read chat and play.",
      confirmLabel: "Mute",
      detail,
      onConfirm: async () => {
        try {
          await postJson("/players/" + accountId + "/mute", { minutes: Number(minutes.value), reason: "chat moderation" });
          flash(name + " muted.", "good");
          after();
        } catch (error) {
          flash(failure(error).message, "bad");
        }
      },
    });
  }

  // World room
  const world = panel("World chat", "Newest at the bottom. Deleted messages stay listed here, hidden from players.");
  const worldBody = el("div", "pl-chat-log");
  world.body.append(worldBody, button("Refresh", () => void loadWorld()));
  const announce = panel("System announcement", "Shown in world chat as “Fleet Command”.");
  const text = textField("Message", { maxLength: 300, multiline: true, placeholder: "Maintenance tonight at 23:00 (Vietnam time), about 10 minutes." });
  announce.body.append(
    text.root,
    button("Announce", async () => {
      try {
        await postJson("/chat/announce", { text: text.input.value });
        text.input.value = "";
        flash("Announcement sent.", "good");
        void loadWorld();
      } catch (error) {
        flash(failure(error).message, "bad");
      }
    }, "st-admin-btn primary"),
  );
  left.append(announce.root, world.root);

  async function loadWorld(): Promise<void> {
    worldBody.replaceChildren(createAdminSkeleton(6));
    try {
      const { messages, online } = await getJson<{ messages: Message[]; online: number }>("/chat/recent?channel=world:global");
      world.root.querySelector("p")!.textContent = online + " online · newest at the bottom. Deleted messages stay listed here, hidden from players.";
      if (messages.length === 0) {
        worldBody.replaceChildren(el("div", "pl-empty", "No messages yet."));
        return;
      }
      worldBody.replaceChildren(
        ...messages.map((message) => {
          const row = el("div", "pl-chat-row" + (message.deleted ? " deleted" : "") + (message.system ? " system" : ""));
          const head = el("div", "pl-chat-head");
          head.append(el("strong", undefined, message.from.name), el("small", undefined, (message.from.code ? message.from.code + " · " : "") + formatTime(message.at)));
          const actions = el("div", "pl-chat-actions");
          if (!message.deleted && !message.system) {
            actions.append(
              button("Delete", async () => {
                try {
                  await postJson("/chat/delete", { channel: "world:global", id: message.id });
                  void loadWorld();
                } catch (error) {
                  flash(failure(error).message, "bad");
                }
              }),
              button("Mute", () => mute(message.from.id, message.from.name, () => void loadWorld())),
            );
          }
          if (message.deleted) actions.append(chip("Deleted", "bad"));
          row.append(head, el("p", undefined, message.text), actions);
          return row;
        }),
      );
      worldBody.scrollTop = worldBody.scrollHeight;
    } catch (error) {
      worldBody.replaceChildren(offlineNotice(failure(error)));
    }
  }

  // Reports
  const reports = panel("Player reports", "Open reports first.");
  const reportBody = el("div", "pl-stack");
  reports.body.append(reportBody);
  right.append(reports.root);

  async function loadReports(): Promise<void> {
    reportBody.replaceChildren(createAdminSkeleton(4));
    try {
      const { reports: list } = await getJson<{ reports: Report[] }>("/chat/reports");
      if (list.length === 0) {
        reportBody.replaceChildren(el("div", "pl-empty", "No reports. Players report a message from its menu in chat."));
        return;
      }
      reportBody.replaceChildren(
        ...list.map((report) => {
          const card = el("article", "pl-report" + (report.resolved_at ? " resolved" : ""));
          const head = el("div", "pl-chat-head");
          head.append(
            el("strong", undefined, report.target_name),
            chip(report.channel.split(":")[0] ?? "chat", "info"),
            report.target_reports > 1 ? chip(report.target_reports + " reports", "warn") : el("span"),
            el("small", undefined, formatTime(report.created_at)),
          );
          card.append(head, el("p", "pl-quote", "“" + report.text + "”"));
          if (report.reason) card.append(el("small", undefined, "Reason: " + report.reason));
          if (report.resolved_at) card.append(chip("Resolved · " + (report.resolution ?? ""), "good"));
          else {
            const actions = el("div", "pl-chat-actions");
            const resolve = (resolution: string) => async () => {
              try {
                await postJson("/chat/reports/" + report.id + "/resolve", { resolution });
                void loadReports();
              } catch (error) {
                flash(failure(error).message, "bad");
              }
            };
            actions.append(
              button("Mute author", () => mute(report.target_id, report.target_name, () => void resolve("muted")())),
              button("Dismiss", () => void resolve("dismissed")()),
            );
            card.append(actions);
          }
          return card;
        }),
      );
    } catch (error) {
      reportBody.replaceChildren(offlineNotice(failure(error)));
    }
  }

  void loadWorld();
  void loadReports();
  return page;
}
