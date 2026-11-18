type GameCardSource = {
  id: string;
  name: string;
  description: string;
  appUrl: string;
  icon?: string;
  art?: { icon?: unknown; cover?: unknown } | null;
};

export type GameArtImage = {
  src: string;
  alt: string;
  width: number;
  height: number;
};

export function resolveGameArt(game: GameCardSource): {
  icon: string | null;
  cover: string | null;
} {
  const prefix = `/assets/${game.id}/portal/`;
  function resolve(path: unknown): string | null {
    if (
      typeof path !== "string" ||
      !path.startsWith(prefix) ||
      ["..", "\\", "//", "?", "#"].some((part) => path.includes(part))
    ) return null;

    try {
      let decoded = path;
      for (;;) {
        // Reject encoded separators at every encoding depth.
        if (/%(?:2f|5c)/i.test(decoded)) return null;
        const next = decodeURIComponent(decoded);
        if (next === decoded) break;
        decoded = next;
      }
      if (
        !decoded.startsWith(prefix) ||
        ["..", "\\", "//", "?", "#"].some((part) => decoded.includes(part))
      ) return null;
      const app = new URL(game.appUrl);
      const image = new URL(path, app);
      const normalized = new URL(decoded, app);
      if (
        image.origin !== app.origin || !image.pathname.startsWith(prefix) ||
        normalized.origin !== app.origin || !normalized.pathname.startsWith(prefix)
      ) return null;
      return image.href;
    } catch {
      return null;
    }
  }

  return {
    icon: resolve(game.art?.icon),
    cover: resolve(game.art?.cover),
  };
}

export function gameCardModel(game: GameCardSource): {
  title: string;
  description: string;
  glyph: string | null;
  icon: GameArtImage | null;
  cover: GameArtImage | null;
} {
  const art = resolveGameArt(game);
  return {
    title: game.name,
    description: game.description,
    glyph: "art" in game ? null : game.icon ?? null,
    icon: art.icon === null ? null : { src: art.icon, alt: "", width: 192, height: 192 },
    cover: art.cover === null ? null : {
      src: art.cover, alt: `${game.name} cover art`, width: 1600, height: 900,
    },
  };
}

export function hideImageOnError(
  img: {
    hidden: boolean;
    addEventListener(type: "error", listener: () => void, options: { once: boolean }): void;
  },
  onHide?: () => void,
): void {
  img.addEventListener("error", () => {
    img.hidden = true;
    onHide?.();
  }, { once: true });
}
