// Source: new for the kit: typing feedback settings shared by every game (docs/games/TYPING_FEEDBACK_REVIEW.md §7)
/**
 * The player's typing-feedback choice. Every game stores the same object
 * under the same field name (`typingFx`) inside its own save; nothing here
 * touches storage, so a game keeps its own key and its own safe storage.
 */
export const TYPING_FX_STYLES = ["stamp", "flare", "smash", "shatter", "rune", "minimal"] as const;
export type TypingFxStyle = (typeof TYPING_FX_STYLES)[number];

export const TYPING_FX_INTENSITIES = ["off", "low", "normal", "high", "ultra"] as const;
export type TypingFxIntensity = (typeof TYPING_FX_INTENSITIES)[number];

export type TypingFxSettings = {
  style: TypingFxStyle;
  intensity: TypingFxIntensity;
  /** A keyboard sound profile id (KEYBOARD_PROFILES: creamy, thock, clicky, dome, spring); "off" plays none. */
  soundProfile: string;
  /** Key sound volume 0 … 1 (under the game's own sfx volume). */
  volume: number;
};

/** The field every game uses inside its settings object. */
export const TYPING_FX_FIELD = "typingFx";

export const DEFAULT_TYPING_FX: Readonly<TypingFxSettings> = Object.freeze({ style: "stamp", intensity: "normal", soundProfile: "creamy", volume: 0.7 });

/** Player-facing names (English: the games are English). */
export const TYPING_FX_STYLE_NAMES: Readonly<Record<TypingFxStyle, string>> = {
  stamp: "Stamp",
  flare: "Flare",
  smash: "Smash",
  shatter: "Shatter",
  rune: "Rune",
  minimal: "Minimal",
};

export const TYPING_FX_INTENSITY_NAMES: Readonly<Record<TypingFxIntensity, string>> = {
  off: "Off",
  low: "Low",
  normal: "Normal",
  high: "High",
  ultra: "Ultra",
};

const pick = <T extends string>(value: unknown, list: readonly T[], fallback: T): T =>
  typeof value === "string" && (list as readonly string[]).includes(value) ? (value as T) : fallback;

/** Any stored value (old, partial or broken) as valid settings; each bad field falls back on its own. */
export function sanitizeTypingFx(raw: unknown, defaults: Readonly<TypingFxSettings> = DEFAULT_TYPING_FX): TypingFxSettings {
  const source = raw !== null && typeof raw === "object" ? (raw as Record<string, unknown>) : {};
  const volume = typeof source.volume === "number" && Number.isFinite(source.volume) ? Math.max(0, Math.min(1, source.volume)) : defaults.volume;
  const profile = typeof source.soundProfile === "string" && /^[a-z0-9][a-z0-9-]{0,31}$/.test(source.soundProfile) ? source.soundProfile : defaults.soundProfile;
  return {
    style: pick(source.style, TYPING_FX_STYLES, defaults.style),
    intensity: pick(source.intensity, TYPING_FX_INTENSITIES, defaults.intensity),
    soundProfile: profile,
    volume,
  };
}
