const NS = "http://www.w3.org/2000/svg";

const PATHS: Record<string, readonly string[]> = {
  "◫": ["M3 3h18v18H3z", "M3 9h18", "M9 9v12"],
  "⌁": ["M4 18V9", "M10 18V5", "M16 18v-7", "M22 18H2"],
  "◖": ["M11 5 6 9H3v6h3l5 4z", "M15 9a4 4 0 0 1 0 6", "M18 6a8 8 0 0 1 0 12"],
  "♫": ["M9 18V5l10-2v13", "M9 9l10-2", "M6 21a3 3 0 1 0 0-6 3 3 0 0 0 0 6Z", "M16 19a3 3 0 1 0 0-6 3 3 0 0 0 0 6Z"],
  "◎": ["M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20Z", "M12 7a5 5 0 1 0 0 10 5 5 0 0 0 0-10Z", "M12 10v4M10 12h4"],
  "△": ["M12 2 3 20h18L12 2Z", "M12 8v6", "M9 17h6"],
  "◇": ["M12 2 22 12 12 22 2 12 12 2Z", "M8 12h8", "M12 8v8"],
  "ϟ": ["M13 2 5 13h6l-1 9 9-13h-6l0-7Z"],
  "✦": ["M12 2l2.2 6.8L21 11l-6.8 2.2L12 20l-2.2-6.8L3 11l6.8-2.2L12 2Z"],
  "✹": ["M12 3v3M12 18v3M3 12h3M18 12h3M5.6 5.6l2.1 2.1M16.3 16.3l2.1 2.1M18.4 5.6l-2.1 2.1M7.7 16.3l-2.1 2.1", "M12 8a4 4 0 1 0 0 8 4 4 0 0 0 0-8Z"],
  "⌘": ["M8 6h8M6 10h12M4 14h16M7 18h10", "M5 3h14v18H5z"],
  "Aa": ["M3 18 8 6l5 12M5 14h6", "M14 11c1.4-1 5-1 5 1.5V18M19 14c-5-1-6 5-1 4"],
  "▣": ["M4 7h16l-1 14H5L4 7Z", "M8 7a4 4 0 0 1 8 0", "M9 12h6"],
  "◈": ["M12 3 20 12 12 21 4 12 12 3Z", "M12 7 16 12 12 17 8 12 12 7Z"],
  "✧": ["M12 2l2.4 7.6L22 12l-7.6 2.4L12 22l-2.4-7.6L2 12l7.6-2.4L12 2Z"],
  "⚡": ["M13 2 4 14h7l-1 8 10-13h-7V2Z"],
  "✓": ["M4 12l5 5L20 6", "M4 4h16v16H4z"],
  "↗": ["M5 19 19 5", "M10 5h9v9", "M5 5v14h14"],
  "◷": ["M12 3a9 9 0 1 0 9 9", "M12 7v5l4 2", "M12 3v3M18.4 5.6l-2.1 2.1"],
  "⚔": ["M5 3l14 14M19 3 5 17", "M3 5l4-2M17 21l4-4M21 5l-4-2M7 21l-4-4"],
  "♜": ["M6 4h3v3h6V4h3v6l-2 2v7H8v-7l-2-2V4Z", "M6 21h12"],
  "⇄": ["M4 7h14l-3-3M18 7l-3 3", "M20 17H6l3-3M6 17l3 3"],
  "▧": ["M3 4h18v16H3z", "M3 15l5-5 4 4 3-3 6 6", "M16 8h.01"],
  "✺": ["M12 2v4M12 18v4M2 12h4M18 12h4", "M5 5l3 3M16 16l3 3M19 5l-3 3M8 16l-3 3", "M12 9a3 3 0 1 0 0 6 3 3 0 0 0 0-6Z"],
  "▦": ["M3 3h18v18H3z", "M3 9h18M9 3v18M15 9v12"],
  "⚙": ["M12 8a4 4 0 1 0 0 8 4 4 0 0 0 0-8Z", "M12 2v3M12 19v3M4.9 4.9 7 7M17 17l2.1 2.1M2 12h3M19 12h3M4.9 19.1 7 17M17 7l2.1-2.1"],
  "⚑": ["M5 21V3", "M5 4h12l-2 4 2 4H5"],
  "↶": ["M9 7H4V2", "M4 7c3-4 10-5 14-1s3 11-2 14"],
  "⌬": ["M8 3h8l5 9-5 9H8l-5-9 5-9Z", "M9 12h6M12 9v6"],
};

export function adminNavIcon(key: string): SVGSVGElement {
  const svg = document.createElementNS(NS, "svg");
  svg.setAttribute("viewBox", "0 0 24 24");
  svg.setAttribute("aria-hidden", "true");
  svg.setAttribute("focusable", "false");
  svg.classList.add("st-admin-nav-svg", "st-admin-nav-icon");
  for (const d of PATHS[key] ?? PATHS["◫"] ?? []) {
    const path = document.createElementNS(NS, "path");
    path.setAttribute("d", d);
    path.setAttribute("fill", "none");
    path.setAttribute("stroke", "currentColor");
    path.setAttribute("stroke-width", "1.65");
    path.setAttribute("stroke-linecap", "round");
    path.setAttribute("stroke-linejoin", "round");
    svg.append(path);
  }
  return svg;
}
