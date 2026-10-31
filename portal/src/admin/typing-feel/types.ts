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
  /** Decision 5: status, owner score and (Provisional) reason of each added set; the summary lines carry them too. */
  addedDetails?: { id: string; status: string; ownerScore: number | null; note: string | null }[];
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

// Add sound set (G7, admin/typing-feel/jobs.mjs): capabilities, the upload check and Format jobs.

export type TypingFeelUploadRule = { id: string; label: string; ok: boolean; level: "error" | "warning"; value: unknown; limit: unknown; message: string };

export type TypingFeelTakeFacts = {
  file?: string;
  bytes?: number;
  sha256?: string;
  format?: string;
  subtype?: string;
  sampleRate?: number;
  channels?: number;
  durationS?: number | null;
  peakDbfs?: number;
  noiseFloorDbfs?: number;
  tapsFound?: number;
  tapsUsable?: number;
  tapsMain?: number;
  tapsPerSecond?: number;
};

export type TypingFeelMachine = { ready: boolean; venv?: boolean; ffmpeg?: boolean; problems: string[]; setupCommand?: string };

/** POST sources/check: the §3.8 upload rules on one uploaded take. */
export type TypingFeelUploadCheck = {
  ok: boolean;
  errors: string[];
  warnings: string[];
  notes: string[];
  rules: TypingFeelUploadRule[];
  source: TypingFeelTakeFacts;
  machine?: TypingFeelMachine;
  message?: string;
};

export type TypingFeelJobPermissions = { check: boolean; format: boolean; accept: boolean; discard: boolean; upload: boolean; draft: boolean };

export type TypingFeelCapabilities = {
  recipes: string[];
  machine: TypingFeelMachine;
  upload: {
    formats: string[];
    sampleFormats: string[];
    sampleRates: number[];
    channels: number[];
    minSeconds: number;
    maxSeconds: number;
    maxBytes: number;
    minUsableTaps: number;
    usableWithinDb: number;
    usableGapMs: number;
    fullScale: number;
    noiseFloorDbfs: number;
    tapsPerSecond: number;
    sourceTags: string[];
  };
  timeoutSeconds: number;
  publishedOwnerScore: number;
  defaultLicence: string;
  running: string | null;
  permissions: TypingFeelJobPermissions;
  requiredPermissions: Record<keyof TypingFeelJobPermissions, string>;
};

export type TypingFeelJobStatus = "queued" | "running" | "succeeded" | "failed" | "accepted" | "discarded";

export type TypingFeelJobSource = { assetId: string; assetVersionId: string; title: string; fileName: string; sha256: string; byteSize: number };

export type TypingFeelJob = {
  jobId: string;
  recipe: string;
  status: TypingFeelJobStatus;
  failure: null | { kind: string; message: string; errors?: string[]; setupCommand?: string };
  source: TypingFeelJobSource;
  set: { id: string; name: string; family: string | null };
  createdAt: string;
  createdBy: string;
  startedAt: string | null;
  finishedAt: string | null;
  exitCode: number | null;
  accepted: null | { setId: string; name: string; family: string; status: string; ownerScore: number; assetId: string; assetVersionId: string; folder: string; acceptedAt: string; row: TypingFeelSet };
};

export type TypingFeelReportFile = {
  file: string;
  set: "key" | "space";
  durationMs: number;
  peakDbfs?: number | null;
  truePeakDbtp?: number | null;
  lufsMMax?: number | null;
  riseMs?: number | null;
  mainStrikeMs?: number | null;
  leadIn?: boolean;
  tickDb?: number | null;
  energyAfter120msPct?: number | null;
  stereoCorrelation?: number | null;
  phaseWarning?: boolean;
  gates?: Record<string, boolean>;
};

/** report.json of keys natural (typing-feel/natural-report-1); only what the page reads. */
export type TypingFeelFormatReport = {
  status: "formatted" | "refused";
  upload?: TypingFeelUploadCheck;
  warnings: string[];
  counts?: { key: number; space: number };
  minimum?: { key: number; space: number };
  acceptAllowed?: boolean;
  taps?: { found: number; usable: number; main: number };
  lengthsMs?: { key: [number, number] | null; space: [number, number] | null };
  loudness?: { min: number | null; max: number | null; spreadDb: number | null; truePeakMaxDbtp: number | null; peakMaxDbfs: number | null };
  leadIns?: { file: string; set: string; mainStrikeMs: number; tickDb: number | null }[];
  gates?: { pass: boolean; failed: string[] };
  files?: TypingFeelReportFile[];
  preview?: { durationMs: number; lufsMMax?: number | null; truePeakDbtp?: number | null; endLevelDb?: number | null; fadeOutMs?: number };
  ab?: { rawCut?: { lufsI: number | null; seconds: number; wpm: number; recipe?: string }; natural?: { lufsI: number | null; seconds: number; wpm: number; recipe?: string } };
  seconds?: number;
  accept?: { ownerScore: number; status: string; reason: string | null };
};

export type TypingFeelJobView = {
  job: TypingFeelJob;
  log: string;
  report: TypingFeelFormatReport | null;
  elapsedSeconds: number | null;
  timeoutSeconds: number;
  filesBase: string;
};

export type TypingFeelJobListEntry = {
  jobId: string;
  status: TypingFeelJobStatus;
  recipe: string;
  source: TypingFeelJobSource;
  set: { id: string; name: string; family: string | null };
  createdAt: string;
  finishedAt: string | null;
  failure: null | { kind: string; message: string };
  accepted: null | { setId: string; assetVersionId: string; status: string };
  counts: { key: number; space: number } | null;
  acceptAllowed: boolean | null;
};

export type TypingFeelAcceptInput = { setId: string; name: string; family: string; licence: string; ownerScore: number; reason?: string; note?: string };

export type TypingFeelAcceptResult = { job: TypingFeelJob; row: TypingFeelSet; version: { assetVersionId: string; assetId: string; contentFingerprint: string } };
