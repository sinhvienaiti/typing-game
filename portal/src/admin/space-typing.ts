import contractJson from "./contracts/space-typing-admin.v1.json";
import { renderWorldMusicEditor } from "./world-music-editor";
import { renderQaSessionPage } from "./qa-session-page";
import {
  AdminApiError,
  SpaceTypingAdminApi,
  type AdminRevision,
  type AdminStatePayload,
  type SpaceTypingAdminConfig,
  type WorldMusicPreview,
} from "./api";

type AdminRoute = { id: string; path: string; label: string };
type AdminContract = {
  contractRevision: string;
  label: string;
  themeId: string;
  routes: AdminRoute[];
  worldMusic: {
    galaxyCount: number;
    worldsPerGalaxy: number;
    worldCount: number;
    validationBadges: string[];
  };
  qa?: {
    productionAllowed: boolean;
    persistenceTarget: string;
    rewardEligibility: string;
  };
};

const contract = contractJson as AdminContract;
const STYLE_ID = "space-typing-admin-v2-styles";

function ensureStyles(): void {
  if (document.getElementById(STYLE_ID) !== null) return;
  const style = document.createElement("style");
  style.id = STYLE_ID;
  style.textContent = `
    .st-admin{min-height:calc(100vh - 72px);padding:24px;background:radial-gradient(circle at 15% 0%,rgba(49,116,173,.18),transparent 38%),radial-gradient(circle at 90% 10%,rgba(125,75,190,.14),transparent 32%),#050912;color:#e9f7ff;font-family:Inter,ui-sans-serif,system-ui,sans-serif}.st-admin-grid{max-width:1440px;margin:0 auto;display:grid;grid-template-columns:230px minmax(0,1fr);gap:20px}.st-admin-side,.st-admin-panel{border:1px solid rgba(117,210,255,.16);background:rgba(7,18,31,.88);box-shadow:0 18px 60px rgba(0,0,0,.28);border-radius:18px}.st-admin-side{padding:18px;height:max-content;position:sticky;top:88px}.st-admin-kicker{font-size:11px;letter-spacing:.18em;color:#73ddff;font-weight:800}.st-admin-side h2{margin:7px 0 3px;font-size:20px}.st-admin-muted{color:#91a9ba;font-size:13px;line-height:1.5}.st-admin-nav{display:grid;gap:8px;margin-top:18px}.st-admin-nav button{all:unset;cursor:pointer;padding:11px 12px;border-radius:10px;color:#b9cbd8;border:1px solid transparent}.st-admin-nav button:hover,.st-admin-nav button.active{color:#f3fbff;background:rgba(58,185,235,.12);border-color:rgba(84,208,255,.22)}.st-admin-token{margin-top:18px;padding-top:16px;border-top:1px solid rgba(255,255,255,.08)}.st-admin-token input{width:100%;box-sizing:border-box;margin:7px 0;padding:9px 10px;border-radius:9px;border:1px solid rgba(117,210,255,.2);background:#07111d;color:#dff7ff}.st-admin-token button,.st-admin-action{border:1px solid rgba(93,217,255,.3);background:rgba(23,148,196,.16);color:#c9f4ff;border-radius:9px;padding:8px 11px;cursor:pointer}.st-admin-action.primary{background:linear-gradient(135deg,rgba(0,167,220,.34),rgba(109,73,207,.32));font-weight:700}.st-admin-action:disabled{opacity:.45;cursor:not-allowed}.st-admin-panel{padding:22px}.st-admin-head{display:flex;gap:16px;align-items:flex-start;justify-content:space-between;margin-bottom:18px}.st-admin-head h1{margin:2px 0 5px;font-size:28px}.st-admin-env{white-space:nowrap;border:1px solid rgba(126,247,189,.22);background:rgba(34,130,87,.13);color:#96f2c2;border-radius:999px;padding:7px 10px;font-size:11px;font-weight:800;letter-spacing:.08em}.st-admin-cards{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}.st-admin-card{padding:15px;border:1px solid rgba(255,255,255,.08);border-radius:13px;background:rgba(255,255,255,.025)}.st-admin-card strong{display:block;font-size:18px;margin-top:5px;word-break:break-word}.st-admin-section{margin-top:20px}.st-admin-section h3{margin:0 0 10px}.st-admin-note,.st-admin-error,.st-admin-success{padding:11px 13px;border-radius:10px;font-size:13px;margin:12px 0}.st-admin-note{background:rgba(83,151,189,.1);border:1px solid rgba(85,190,232,.18);color:#b9d9e7}.st-admin-error{background:rgba(173,55,72,.14);border:1px solid rgba(255,106,127,.25);color:#ffbdc7}.st-admin-success{background:rgba(34,139,92,.14);border:1px solid rgba(99,235,170,.22);color:#aaf0ca}.st-audio-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}.st-audio-row{padding:13px;border-radius:12px;border:1px solid rgba(255,255,255,.07);background:rgba(255,255,255,.02)}.st-audio-row label{display:flex;justify-content:space-between;font-size:13px;font-weight:700}.st-audio-row input,.st-audio-row select{width:100%;box-sizing:border-box;margin-top:10px;padding:9px 10px;border-radius:9px;border:1px solid rgba(117,210,255,.2);background:#07111d;color:#dff7ff}.st-audio-row input[type=checkbox]{width:auto}.st-audio-row input[type=range]{width:100%;margin-top:12px;padding:0}.st-admin-actions{display:flex;gap:8px;flex-wrap:wrap;margin-top:16px}.st-galaxy-list{display:grid;gap:14px}.st-galaxy{border:1px solid rgba(255,255,255,.07);border-radius:13px;padding:13px}.st-galaxy h3{margin:0 0 10px;color:#a9eaff}.st-world-grid{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:8px}.st-world{padding:10px;border:1px solid rgba(255,255,255,.07);border-radius:10px;background:rgba(255,255,255,.025)}.st-world strong{font-size:13px}.st-world small{display:block;color:#8faabb;margin-top:5px}.st-world-badges{display:flex;gap:4px;flex-wrap:wrap;margin-top:8px}.st-world-source{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:10px;color:#7fa2b8;margin-top:7px;overflow-wrap:anywhere}.st-history{display:grid;gap:9px}.st-history-row{display:grid;grid-template-columns:minmax(180px,1fr) minmax(170px,.8fr) auto;gap:12px;align-items:center;padding:12px;border:1px solid rgba(255,255,255,.07);border-radius:11px}.st-history-row code{font-size:12px;color:#9de9ff}.st-badge{display:inline-flex;align-items:center;border-radius:999px;padding:4px 8px;font-size:10px;font-weight:800;letter-spacing:.05em;background:rgba(87,203,241,.12);border:1px solid rgba(92,214,255,.18);color:#aeeeff}.st-admin-loading{padding:30px;text-align:center;color:#99b4c6}@media(max-width:900px){.st-admin-grid{grid-template-columns:1fr}.st-admin-side{position:static}.st-admin-cards,.st-audio-grid{grid-template-columns:1fr}.st-world-grid{grid-template-columns:repeat(2,minmax(0,1fr))}.st-history-row{grid-template-columns:1fr}}
  `;
  document.head.append(style);
}

function cloneConfig(config: SpaceTypingAdminConfig): SpaceTypingAdminConfig {
  return structuredClone(config);
}

function button(label: string, onClick: () => void, className = "st-admin-action"): HTMLButtonElement {
  const element = document.createElement("button");
  element.type = "button";
  element.className = className;
  element.textContent = label;
  element.addEventListener("click", onClick);
  return element;
}

export class SpaceTypingAdmin {
  private readonly api = new SpaceTypingAdminApi();

  constructor(private readonly navigate: (path: string) => void) {
    ensureStyles();
  }

  render(path: string): HTMLElement {
    const root = document.createElement("main");
    root.className = "st-admin";
    const grid = document.createElement("div");
    grid.className = "st-admin-grid";
    grid.append(this.renderSidebar(path));
    const panel = document.createElement("section");
    panel.className = "st-admin-panel";
    panel.innerHTML = '<div class="st-admin-loading">Loading Space Typing Admin…</div>';
    grid.append(panel);
    root.append(grid);
    void this.loadPage(panel, path);
    return root;
  }

  private renderSidebar(path: string): HTMLElement {
    const aside = document.createElement("aside");
    aside.className = "st-admin-side";
    const kicker = document.createElement("div");
    kicker.className = "st-admin-kicker";
    kicker.textContent = "LOCAL GAME ADMIN";
    const title = document.createElement("h2");
    title.textContent = contract.label;
    const revision = document.createElement("div");
    revision.className = "st-admin-muted";
    revision.textContent = contract.contractRevision;
    const nav = document.createElement("div");
    nav.className = "st-admin-nav";
    for (const route of contract.routes) {
      const item = button(route.label, () => this.navigate(route.path), "");
      item.className = path === route.path ? "active" : "";
      nav.append(item);
    }

    const token = document.createElement("div");
    token.className = "st-admin-token";
    const tokenLabel = document.createElement("div");
    tokenLabel.className = "st-admin-muted";
    tokenLabel.textContent = "Local Admin token";
    const input = document.createElement("input");
    input.type = "password";
    input.value = this.api.getToken();
    input.autocomplete = "off";
    const save = button("Save token", () => this.api.setToken(input.value));
    token.append(tokenLabel, input, save);
    aside.append(kicker, title, revision, nav, token);
    return aside;
  }

  private async loadPage(panel: HTMLElement, path: string): Promise<void> {
    try {
      const state = await this.api.getState();
      if (path === "/admin/space-typing/audio") {
        this.renderAudio(panel, state);
      } else if (path === "/admin/space-typing/world-music") {
        const preview = await this.api.previewWorldMusic();
        this.renderWorldMusic(panel, state, preview);
      } else if (path === "/admin/space-typing/history") {
        this.renderHistory(panel, state);
      } else if (path === "/admin/space-typing/qa") {
        renderQaSessionPage({
          panel,
          api: this.api,
          header: this.renderHeader(
            "QA Session",
            "Launch a scoped disposable run with temporary stage, ship, and Warp overrides.",
          ),
        });
      } else {
        this.renderOverview(panel, state);
      }
    } catch (error) {
      panel.replaceChildren(this.renderFailure(error));
    }
  }

  private renderHeader(title: string, subtitle: string): HTMLElement {
    const head = document.createElement("header");
    head.className = "st-admin-head";
    const copy = document.createElement("div");
    const kicker = document.createElement("div");
    kicker.className = "st-admin-kicker";
    kicker.textContent = "SPACE TYPING · ADMIN V2";
    const h1 = document.createElement("h1");
    h1.textContent = title;
    const p = document.createElement("div");
    p.className = "st-admin-muted";
    p.textContent = subtitle;
    copy.append(kicker, h1, p);
    const env = document.createElement("div");
    env.className = "st-admin-env";
    env.textContent = "LOCAL · 127.0.0.1";
    head.append(copy, env);
    return head;
  }

  private renderOverview(panel: HTMLElement, state: AdminStatePayload): void {
    panel.replaceChildren(this.renderHeader("Overview", "Runtime reads only the active immutable revision."));
    const cards = document.createElement("div");
    cards.className = "st-admin-cards";
    const items: Array<[string, string]> = [
      ["Active revision", state.state.activeRevision],
      ["Contract", contract.contractRevision],
      ["World topology", `${contract.worldMusic.galaxyCount} Galaxies · ${contract.worldMusic.worldCount} Worlds`],
    ];
    for (const [label, value] of items) {
      const card = document.createElement("div");
      card.className = "st-admin-card";
      const caption = document.createElement("div");
      caption.className = "st-admin-muted";
      caption.textContent = label;
      const strong = document.createElement("strong");
      strong.textContent = value;
      card.append(caption, strong);
      cards.append(card);
    }
    const note = document.createElement("div");
    note.className = "st-admin-note";
    note.textContent = "Draft revisions never leak into runtime. Publish and rollback use compare-and-swap against the active revision.";
    panel.append(cards, note);
  }

  private renderAudio(panel: HTMLElement, state: AdminStatePayload): void {
    panel.replaceChildren(this.renderHeader("Audio & Mix", "Edit product-owned defaults; player personal volume remains separate."));
    const config = cloneConfig(state.active.config);
    const grid = document.createElement("div");
    grid.className = "st-audio-grid";
    const keys = ["master", "pronunciation", "music", "ambient", "sfx", "announcer"] as const;
    for (const key of keys) {
      const row = document.createElement("div");
      row.className = "st-audio-row";
      const label = document.createElement("label");
      const name = document.createElement("span");
      name.textContent = key[0]?.toUpperCase() + key.slice(1);
      const value = document.createElement("span");
      value.textContent = config.audio.defaults[key].toFixed(2);
      label.append(name, value);
      const input = document.createElement("input");
      input.type = "range";
      input.min = "0";
      input.max = "1";
      input.step = "0.01";
      input.value = String(config.audio.defaults[key]);
      input.addEventListener("input", () => {
        const parsed = Number.parseFloat(input.value);
        config.audio.defaults[key] = Number.isFinite(parsed) ? parsed : 0;
        value.textContent = config.audio.defaults[key].toFixed(2);
      });
      row.append(label, input);
      grid.append(row);
    }
    const status = document.createElement("div");
    const actions = document.createElement("div");
    actions.className = "st-admin-actions";
    const save = button("Save immutable draft", () => {
      save.disabled = true;
      status.className = "st-admin-note";
      status.textContent = "Saving draft…";
      void this.api
        .createRevision({
          baseRevision: state.state.activeRevision,
          config,
          message: "Update product audio defaults",
        })
        .then((revision) => {
          status.className = "st-admin-success";
          status.textContent = `Draft ${revision.revision} saved. Runtime is unchanged until Publish.`;
        })
        .catch((error: unknown) => {
          status.className = "st-admin-error";
          status.textContent = error instanceof Error ? error.message : "Could not save draft.";
        })
        .finally(() => {
          save.disabled = false;
        });
    }, "st-admin-action primary");
    actions.append(save, button("History / Publish", () => this.navigate("/admin/space-typing/history")));
    panel.append(grid, actions, status);
  }

  private renderWorldMusic(
    panel: HTMLElement,
    state: AdminStatePayload,
    preview: WorldMusicPreview,
  ): void {
    renderWorldMusicEditor({
      panel,
      state,
      preview,
      api: this.api,
      navigate: this.navigate,
      header: this.renderHeader(
        "World Music",
        "Edit a canonical published policy, preview through the child resolver, then save an immutable draft.",
      ),
    });
  }

  private renderHistory(panel: HTMLElement, state: AdminStatePayload): void {
    panel.replaceChildren(this.renderHeader("History / Publish", "Activate a draft or roll back to any retained immutable revision with CAS protection."));
    const status = document.createElement("div");
    const list = document.createElement("div");
    list.className = "st-history";
    for (const revision of state.history) {
      list.append(this.renderHistoryRow(revision, state, status, panel));
    }
    panel.append(status, list);
  }

  private renderHistoryRow(
    revision: AdminRevision,
    state: AdminStatePayload,
    status: HTMLElement,
    panel: HTMLElement,
  ): HTMLElement {
    const row = document.createElement("div");
    row.className = "st-history-row";
    const identity = document.createElement("div");
    const code = document.createElement("code");
    code.textContent = revision.revision;
    const message = document.createElement("div");
    message.className = "st-admin-muted";
    message.textContent = revision.message;
    identity.append(code, message);
    const meta = document.createElement("div");
    meta.className = "st-admin-muted";
    meta.textContent = new Date(revision.createdAt).toLocaleString();
    const actions = document.createElement("div");
    if (revision.revision === state.state.activeRevision) {
      const active = document.createElement("span");
      active.className = "st-badge";
      active.textContent = "ACTIVE";
      actions.append(active);
    } else {
      const older = Date.parse(revision.createdAt) < Date.parse(state.active.createdAt);
      const activate = button(older ? "Rollback here" : "Publish draft", () => {
        activate.disabled = true;
        const request = older
          ? this.api.rollback(revision.revision, state.state.activeRevision)
          : this.api.publish(revision.revision, state.state.activeRevision);
        void request
          .then(() => this.loadPage(panel, "/admin/space-typing/history"))
          .catch((error: unknown) => {
            status.className = "st-admin-error";
            status.textContent = error instanceof Error ? error.message : "Publish failed.";
          })
          .finally(() => {
            activate.disabled = false;
          });
      }, "st-admin-action primary");
      actions.append(activate);
    }
    row.append(identity, meta, actions);
    return row;
  }

  private renderFailure(error: unknown): HTMLElement {
    const block = document.createElement("div");
    block.className = "st-admin-error";
    if (error instanceof AdminApiError && error.status === 401) {
      block.textContent = "Admin service rejected the token. Update the local Admin token in the sidebar.";
    } else {
      block.textContent = error instanceof Error
        ? `Admin service unavailable: ${error.message}`
        : "Admin service unavailable.";
    }
    return block;
  }
}
