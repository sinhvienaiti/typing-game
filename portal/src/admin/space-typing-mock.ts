import "@fontsource/exo-2/600.css";
import "@fontsource/exo-2/700.css";
import "@fontsource/exo-2/800.css";
import "@fontsource/be-vietnam-pro/400.css";
import "@fontsource/be-vietnam-pro/500.css";
import "@fontsource/be-vietnam-pro/600.css";
import "@fontsource/be-vietnam-pro/700.css";

export type AdminMetric = {
  label: string;
  value: string;
  delta: string;
  trend: "up" | "down" | "flat";
  tone?: "good" | "warn" | "bad" | "neutral";
  spark: readonly number[];
};

export type StageHealthRow = {
  stage: string;
  world: string;
  plays: number;
  clearRate: number;
  retryRate: number;
  wpm: number;
  accuracy: number;
  duration: string;
  status: "healthy" | "warning" | "critical";
};

export type MusicTrack = {
  id: string;
  title: string;
  type: "BGM" | "Boss" | "Ambient" | "Victory" | "Duel";
  duration: string;
  format: "MP3" | "OGG" | "WAV";
  bpm: number;
  mood: string;
  usage: number;
  status: "READY" | "UNUSED" | "WARNING";
  file: string;
  size: string;
  worlds: readonly string[];
};

export type ShipMock = {
  id: string;
  name: string;
  className: string;
  rarity: "Common" | "Rare" | "Epic" | "Legendary";
  enabled: boolean;
  unlock: string;
  price: string;
  hp: number;
  shield: number;
  armor: number;
  speed: number;
  fireRate: number;
  damage: number;
};

export const overviewMetrics: readonly AdminMetric[] = [
  { label: "Online Users", value: "1,284", delta: "+8.4%", trend: "up", tone: "good", spark: [22, 26, 25, 31, 34, 38, 42, 45] },
  { label: "Playing Now", value: "932", delta: "+5.1%", trend: "up", tone: "good", spark: [18, 21, 24, 25, 30, 29, 34, 36] },
  { label: "In Lobby", value: "221", delta: "-2.3%", trend: "down", tone: "neutral", spark: [28, 27, 29, 24, 25, 23, 22, 21] },
  { label: "Active Duel Rooms", value: "64", delta: "+12.0%", trend: "up", tone: "good", spark: [9, 12, 12, 15, 17, 16, 19, 21] },
  { label: "Peak Concurrent", value: "1,642", delta: "+6.7%", trend: "up", tone: "good", spark: [30, 29, 34, 37, 39, 41, 44, 47] },
  { label: "Client Error Rate", value: "0.42%", delta: "+0.08%", trend: "up", tone: "warn", spark: [4, 5, 4, 6, 5, 7, 8, 9] },
];

export const audienceMetrics = [
  ["DAU", "8,421", "+6.4%"],
  ["WAU", "31,506", "+9.7%"],
  ["MAU", "92,184", "+11.2%"],
  ["New Players", "1,206", "+14.8%"],
  ["Returning", "7,215", "+4.9%"],
  ["Avg Session", "28m 42s", "+3m 11s"],
] as const;

export const modeSplit = [
  { label: "Campaign", value: 46, count: 429 },
  { label: "Expedition", value: 21, count: 196 },
  { label: "Duel", value: 18, count: 168 },
  { label: "Recall", value: 12, count: 112 },
  { label: "Other", value: 3, count: 27 },
] as const;

export const retention = [
  ["D1", 62],
  ["D3", 48],
  ["D7", 39],
  ["D14", 31],
  ["D30", 24],
] as const;

export const problemStages: readonly StageHealthRow[] = [
  { stage: "314", world: "W16 · Cinder Rift", plays: 384, clearRate: 18, retryRate: 4.8, wpm: 47, accuracy: 86.4, duration: "04:38", status: "critical" },
  { stage: "488", world: "W25 · Dark Meridian", plays: 291, clearRate: 26, retryRate: 4.1, wpm: 51, accuracy: 88.1, duration: "04:12", status: "critical" },
  { stage: "650", world: "W33 · Solar Forge", plays: 246, clearRate: 42, retryRate: 3.2, wpm: 55, accuracy: 90.7, duration: "05:44", status: "warning" },
  { stage: "742", world: "W38 · Aurora Grave", plays: 211, clearRate: 49, retryRate: 2.9, wpm: 58, accuracy: 91.3, duration: "04:51", status: "warning" },
  { stage: "919", world: "W46 · Void Cathedral", plays: 168, clearRate: 53, retryRate: 2.6, wpm: 62, accuracy: 92.2, duration: "05:07", status: "warning" },
];

export const systemHealth = [
  { label: "Game Runtime", value: "Healthy", tone: "good" },
  { label: "Duel WebSocket", value: "Healthy", tone: "good" },
  { label: "Music Catalog", value: "v2.3.1", tone: "good" },
  { label: "Reconnect Rate", value: "97.8%", tone: "good" },
  { label: "Asset Failures", value: "3", tone: "warn" },
  { label: "API Latency p95", value: "82 ms", tone: "good" },
] as const;

export const alertFeed = [
  { severity: "critical", title: "Stage 314 clear rate below 20%", detail: "18% clear rate across 384 runs · 4.8 average retries", time: "4m ago" },
  { severity: "warning", title: "World 17 Major Boss uses fallback music", detail: "No dedicated Major Boss assignment. Effective source: World 17 Normal.", time: "18m ago" },
  { severity: "warning", title: "3 music assets failed validation", detail: "2 unsupported metadata records · 1 missing source file", time: "31m ago" },
  { severity: "info", title: "Config revision v2.3.1 published", detail: "12 tracks and 8 World assignments changed", time: "1h ago" },
] as const;

export const economyMetrics = [
  ["Credits Generated", "4.82M", "+8.2%"],
  ["Credits Spent", "4.31M", "+6.8%"],
  ["Net Inflation", "+510K", "+1.4%"],
  ["Rare Credits In", "18,420", "+4.2%"],
  ["Rare Credits Out", "17,906", "+5.9%"],
  ["Warp Consumed", "61,280", "+3.1%"],
] as const;

export const audioDefaults = [
  ["Master", 100],
  ["Pronunciation", 100],
  ["Music", 26],
  ["Ambient", 8],
  ["Typing SFX", 70],
  ["Combat SFX", 80],
  ["Warnings", 78],
  ["UI", 60],
  ["Rewards", 72],
  ["Announcer", 85],
  ["Voice", 100],
] as const;

export const duckingDefaults = [
  ["Music duck", 70],
  ["Ambient duck", 76],
  ["Combat duck", 80],
  ["UI duck", 35],
  ["Warnings duck", 15],
  ["Announcer duck", 55],
] as const;

export const musicTracks: readonly MusicTrack[] = [
  { id: "g01-stellar-dawn", title: "Stellar Dawn", type: "BGM", duration: "02:34", format: "MP3", bpm: 118, mood: "Hopeful", usage: 16, status: "READY", file: "g01_space_dawn.mp3", size: "5.2 MB", worlds: ["World 01", "World 02"] },
  { id: "g01-boss-awakening", title: "Awakening Protocol", type: "Boss", duration: "03:12", format: "OGG", bpm: 146, mood: "Climactic", usage: 8, status: "READY", file: "g01_boss_awakening.ogg", size: "6.8 MB", worlds: ["World 01"] },
  { id: "g02-nebula-drift", title: "Nebula Drift", type: "BGM", duration: "02:18", format: "MP3", bpm: 104, mood: "Lonely", usage: 12, status: "READY", file: "g02_nebula_drift.mp3", size: "4.9 MB", worlds: ["World 06", "World 07"] },
  { id: "g02-boss-void-me", title: "Void Machine", type: "Boss", duration: "03:45", format: "MP3", bpm: 158, mood: "Aggressive", usage: 5, status: "READY", file: "g02_boss_void_me.mp3", size: "8.1 MB", worlds: ["World 08"] },
  { id: "g03-starfall", title: "Starfall Memory", type: "Ambient", duration: "02:56", format: "OGG", bpm: 92, mood: "Melancholic", usage: 0, status: "UNUSED", file: "g03_starfall.ogg", size: "5.7 MB", worlds: [] },
  { id: "g05-last-light", title: "Last Light", type: "Victory", duration: "01:24", format: "MP3", bpm: 126, mood: "Triumphant", usage: 50, status: "READY", file: "last_light.mp3", size: "3.6 MB", worlds: ["Global"] },
  { id: "duel-infernal", title: "Infernal Duel", type: "Duel", duration: "02:41", format: "OGG", bpm: 164, mood: "Competitive", usage: 3, status: "WARNING", file: "duel_infernal.ogg", size: "6.1 MB", worlds: ["Duel"] },
];

export const galaxyWorlds = Array.from({ length: 10 }, (_, galaxyIndex) => ({
  galaxy: galaxyIndex + 1,
  name: ["Celestial Reach", "Infernal Belt", "Frost Prism", "Verdant Sector", "Shadow Nature", "Cosmic Forge", "Abyssal Line", "Aurora Expanse", "Void Cathedral", "Eternity Gate"][galaxyIndex] ?? `Galaxy ${galaxyIndex + 1}`,
  worlds: Array.from({ length: 5 }, (_, worldIndex) => {
    const world = galaxyIndex * 5 + worldIndex + 1;
    return {
      id: `world-${String(world).padStart(2, "0")}`,
      label: `World ${String(world).padStart(2, "0")}`,
      trackCount: 3 + ((world * 7) % 6),
      warning: world === 17 || world === 33,
    };
  }),
}));

export const ships: readonly ShipMock[] = [
  { id: "vanguard", name: "Vanguard", className: "Interceptor", rarity: "Common", enabled: true, unlock: "Starter", price: "Free", hp: 100, shield: 82, armor: 46, speed: 92, fireRate: 78, damage: 64 },
  { id: "phoenix", name: "Phoenix", className: "Assault", rarity: "Rare", enabled: true, unlock: "Stage 080", price: "24,000 Credits", hp: 118, shield: 74, armor: 52, speed: 84, fireRate: 86, damage: 79 },
  { id: "raven", name: "Raven", className: "Stealth", rarity: "Epic", enabled: true, unlock: "Stage 220", price: "18 Rare Credits", hp: 88, shield: 62, armor: 38, speed: 100, fireRate: 93, damage: 83 },
  { id: "aurora", name: "Aurora", className: "Guardian", rarity: "Legendary", enabled: false, unlock: "Stage 500 + Challenge", price: "42 Rare Credits", hp: 148, shield: 100, armor: 90, speed: 68, fireRate: 61, damage: 92 },
];

export const recentChanges = [
  { revision: "v2.3.1", title: "Galaxy 03 music refresh", author: "admin", time: "09:12", tone: "draft" },
  { revision: "v2.3.0", title: "Add Major Boss fallback", author: "admin", time: "Yesterday", tone: "published" },
  { revision: "v2.2.1", title: "Pronunciation focus defaults", author: "system", time: "Oct 04", tone: "published" },
] as const;
