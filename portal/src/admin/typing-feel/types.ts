// Shapes of the /api/admin/shared/typing-feel/* answers (admin/typing-feel/http.mjs).
import type { AdminAuditEvent } from "../api";

export type TypingFeelFamily = { id: string; name: string; order: number };

export type TypingFeelSet = {
  id: string;
  name: string;
  family: string;
  /** Position inside its family. */
  order: number;
  enabled: boolean;
  status: string;
  assetVersionId: string;
  ownerPick: boolean;
  ownerScore: number | null;
  recipe: string;
  note?: string;
  /** Ticket 218 machine score; null for new sets. */
  score?: number | null;
  labels?: string[];
};

export type TypingFeelEffectDefaults = { style: string; intensity: string; size: string; volume: number };

/** typing-feel-admin/1 */
export type TypingFeelConfig = {
  schema: string;
  contract: number;
  keyboard: {
    defaultSet: string;
    families: TypingFeelFamily[];
    sets: TypingFeelSet[];
    retiredIds: string[];
  };
  effects: { defaults: TypingFeelEffectDefaults };
};

export type TypingFeelPublication = { revision: string; catalogueRevision: string; publishedAt: string; builtAt: string };

export type TypingFeelRelation = "active" | "ancestor" | "draft";

export type TypingFeelRevision = {
  revision: string;
  parentRevision: string | null;
  createdAt: string;
  author: string;
  message: string;
  config: TypingFeelConfig;
  active?: boolean;
  relation?: TypingFeelRelation;
  publishable?: boolean;
  rollbackEligible?: boolean;
  publication?: TypingFeelPublication | null;
};

/** A History row: a revision without its config (GET revisions/:id reads one whole). */
export type TypingFeelHistoryEntry = Omit<TypingFeelRevision, "config">;

export type TypingFeelOptions = {
  effects: {
    styles: string[];
    intensities: string[];
    sizes: string[];
    volume: { min: number; max: number };
    defaults: TypingFeelEffectDefaults;
  };
  statuses: string[];
  labels: string[];
  recipes: string[];
  idPattern: string;
  reservedIds: string[];
  setNameMax: number;
  familyNameMax: number;
  noteMax: number;
  publishedOwnerScore: number;
  minimum: { key: number; space: number };
};

export type TypingFeelPermissions = { draft: boolean; publish: boolean; rollback: boolean };

type StateCommon = {
  startup: null | { status: string; [key: string]: unknown };
  permissions: TypingFeelPermissions;
  requiredPermissions: { draft: string; publish: string; rollback: string };
  options: TypingFeelOptions;
};

export type TypingFeelReadyState = StateCommon & {
  initialized: true;
  state: { version: number; activeRevision: string; generation: number; updatedAt: string };
  active: TypingFeelRevision;
  /** The draft waiting: never published, on top of the live revision, saved after it went live. */
  draft: TypingFeelRevision | null;
  history: TypingFeelHistoryEntry[];
  reservedIds: string[];
  local: {
    catalogue: null | { revision: string | null; publishedAt?: string | null; sets?: number | null; unreadable?: boolean };
    matchesActive: boolean;
  };
};

export type TypingFeelEmptyState = StateCommon & {
  initialized: false;
  setup: { importCommand: string; restoreCommand: string };
};

export type TypingFeelState = TypingFeelReadyState | TypingFeelEmptyState;

export type TypingFeelChangeScope = {
  model: "typing-feel-revision";
  affects: "all games";
  baseRevision: string | null;
  targetRevision: string | null;
  changed: boolean;
  added: string[];
  hidden: string[];
  shown: string[];
  retired: string[];
  reformatted: string[];
  renamed: { id: string; from: string; to: string }[];
  familyChanged: { id: string; from: string; to: string }[];
  statusChanged: { id: string; from: string; to: string }[];
  detailsChanged: string[];
  reordered: string[];
  defaultChanged: null | { from: string | null; to: string | null };
  effectsChanged: { field: string; from: unknown; to: unknown }[];
  familiesChanged: boolean;
  summary: string[];
  publishWarning: string;
};

export type TypingFeelValidation = {
  revision: string;
  valid: boolean;
  problems: string[];
  activeRevision: string;
  parentRevision: string | null;
  relation: TypingFeelRelation;
  publishable: boolean;
  rollbackEligible: boolean;
  changeScope: TypingFeelChangeScope;
  catalogue: null | { revision: string; default: string; families: number; sets: number; hidden: string[] };
  plan: null | { created: string[]; reused: string[] };
  previewBase: string;
};

export type TypingFeelLibrarySet = TypingFeelSet & {
  media: null | {
    assetId: string;
    provenance: string;
    folder: string;
    keys: number;
    spaces: number;
    legacy218: boolean;
    preview: string;
  };
};

export type TypingFeelLibrary = { revision: string; problems: string[]; sets: TypingFeelLibrarySet[] };

export type TypingFeelExportStatus = {
  local: null | { revision: string | null; publishedAt: string | null; sets: number };
  git: { status: string; message?: string; changedFiles?: number };
  drive: { status: string; message?: string; lockFile?: string; previewsListed?: number; previews?: number; backupCommand?: string };
  online: { status: string; message?: string; deployCommand?: string };
};

export type TypingFeelHistory = {
  initialized: boolean;
  history: TypingFeelHistoryEntry[];
  activeRevision: string | null;
  events: AdminAuditEvent[] | null;
  eventsHidden: boolean;
};

export type TypingFeelPublishResult = {
  state: { activeRevision: string; generation: number; updatedAt: string };
  catalogue: { revision: string; publishedAt: string; sets: number; families: number; default: string; sha256: string };
  folders: { created: string[]; reused: string[] };
  referencesCreated: number;
};
