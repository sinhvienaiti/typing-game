import type { AdminArea, NavGroup } from "./types";
import { renderPhaseBAdminScreen } from "../space-typing-phase-b";
import { renderAdminV2Dashboard } from "../v2/dashboard";
import { renderAdminV2DeveloperTools } from "../v2/developer-tools";
const ADMIN_BASE = "/admin/space-typing";
const DEVELOPER_PERMISSION = "developer.runtime-inspect";
export const NAV_GROUPS: readonly NavGroup[] = [
  {
    id: "dashboard",
    label: "Dashboard",
    description: "Published state, drafts and administrator activity that need attention now.",
    items: [
      { label: "Overview", path: ADMIN_BASE, icon: "◫", description: "See real Admin state, pending drafts and recent administrator activity." },
    ],
  },
  {
    id: "content",
    label: "Content",
    description: "Manage worlds, stages and learning-content assignments backed by canonical game data.",
    items: [
      { label: "Worlds & Stages", path: `${ADMIN_BASE}/stages`, icon: "⌘", description: "Manage supported world and stage configuration through the revision-backed workflow." },
    ],
  },
  {
    id: "gameplay",
    label: "Gameplay",
    description: "Manage revision-backed gameplay entities currently connected to the Space Typing runtime.",
    items: [
      { label: "Ships", path: `${ADMIN_BASE}/ships`, icon: "△", description: "Manage the ship properties currently supported by the canonical runtime." },
      { label: "Equipment", path: `${ADMIN_BASE}/equipment`, icon: "◇", description: "Manage supported equipment definitions, stats and perks." },
      { label: "Skills", path: `${ADMIN_BASE}/skills`, icon: "ϟ", description: "Manage supported combat-skill definitions and parameters." },
      { label: "Enemies", path: `${ADMIN_BASE}/enemies`, icon: "✦", description: "Manage supported enemy admission and projectile policy values." },
      { label: "Bosses", path: `${ADMIN_BASE}/bosses`, icon: "✹", description: "Manage supported boss identity values through the canonical revision workflow." },
    ],
  },
  {
    id: "economy-live-ops",
    label: "Economy",
    description: "Manage canonical Shop merchandising.",
    items: [
      { label: "Shop", path: `${ADMIN_BASE}/shop`, icon: "▱", description: "Manage supported Shop offers, pricing and merchandising through the canonical Shop owner." },
    ],
  },
  {
    id: "players-live-ops",
    label: "Players & Live Ops",
    description: "Online accounts (Cloudflare Worker + D1), chat moderation, Daily Hub mail and gift codes, and the read-only event catalog.",
    items: [
      { label: "Players", path: `${ADMIN_BASE}/players`, icon: "☺", description: "Look up pilots, their cloud save, Daily Hub progress, rewards and sessions; ban, sign out, restore saves, send gifts." },
      { label: "Mail & Gift Codes", path: `${ADMIN_BASE}/liveops-mail`, icon: "✉", description: "Send gifts and announcements to every player and create gift codes; read the email outbox and account audit." },
      { label: "Chat Moderation", path: `${ADMIN_BASE}/chat`, icon: "☏", description: "Read world chat, delete messages, mute players, handle reports and post system announcements." },
      { label: "Feedback", path: `${ADMIN_BASE}/feedback`, icon: "✎", description: "Read ideas, bug reports and contact messages players send from the game; mark them handled or reply by in-game mail." },
      { label: "Events (read-only)", path: `${ADMIN_BASE}/events`, icon: "⌁", description: "Read the in-stage event catalog owned by the game code. Scheduling is not available yet." },
    ],
  },
  {
    id: "media",
    label: "Media",
    description: "Browse canonical game media, upload Admin-managed assets and keep source-owned runtime media read-only.",
    items: [
      { label: "Music Library", path: `${ADMIN_BASE}/music-library`, icon: "♫", description: "Browse, upload and manage the legacy authored music capability while it is migrated into Media V2." },
      { label: "SFX", path: `${ADMIN_BASE}/sfx`, icon: "◉", description: "Inspect production sample-backed sound effects and test the exact committed runtime assets without changing game policy." },
      { label: "World / Stage Music", path: `${ADMIN_BASE}/world-music`, icon: "◎", description: "Assign music to global, galaxy, world and stage contexts and preview the canonical result." },
    ],
  },
  {
    id: "system",
    label: "System",
    description: "Manage safe global settings, access review and the revision lifecycle.",
    items: [
      { label: "Audio Defaults", path: `${ADMIN_BASE}/audio`, icon: "◖", description: "Set default audio behavior while preserving player-specific preferences." },
      { label: "General Settings", path: `${ADMIN_BASE}/settings`, icon: "⚙", description: "Manage global game defaults, network behavior and maintenance settings." },
      { label: "History & Publish", path: `${ADMIN_BASE}/history`, icon: "↶", description: "Review drafts, validate complete change scope, publish or roll back safely." },
    ],
  },
  {
    id: "developer",
    label: "Developer Tools",
    description: "Runtime contracts, capability diagnostics and isolated QA tools separated from normal administrator workflows.",
    requiredPermission: DEVELOPER_PERMISSION,
    items: [
      { label: "Developer Tools", path: `${ADMIN_BASE}/developer-tools`, icon: "⌬", description: "Open permission-gated runtime, economy, Live Ops, PvP, visual and QA diagnostics." },
    ],
  },
];

export const spaceTypingArea: AdminArea = {
  id: "space-typing", label: "Space Typing", base: ADMIN_BASE, navGroups: NAV_GROUPS,
  renderPage(path, { navigate, help }) {
    if (path === ADMIN_BASE) return renderAdminV2Dashboard(navigate, help);
    if (path === `${ADMIN_BASE}/developer-tools`) return renderAdminV2DeveloperTools(navigate, help);
    const phaseB = renderPhaseBAdminScreen(path, navigate);
    if (phaseB !== null) return phaseB;
    return null;
  },
};
