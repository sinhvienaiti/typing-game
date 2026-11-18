import { describe, expect, it } from "vitest";
import {
  KIT_CSS,
  KIT_STYLE_ID,
  LEARNING_FRAME_CLASSES,
  SEMANTIC_COLORS,
  applyUiScale,
  installKitStyles,
  uiScale,
} from "./index";

function relativeLuminance(hex: string): number {
  const channels = [1, 3, 5].map((start) => parseInt(hex.slice(start, start + 2), 16) / 255);
  const [r, g, b] = channels.map((value) => (value <= 0.03928 ? value / 12.92 : ((value + 0.055) / 1.055) ** 2.4)) as [number, number, number];
  return 0.2126 * r + 0.7152 * g + 0.0722 * b;
}

describe("ui tokens", () => {
  it("keeps the four semantic colours of 05 §2.2", () => {
    expect(SEMANTIC_COLORS).toEqual({ danger: "#FF4A4A", urgent: "#FFB020", money: "#FFC83A", typing: "#7FF5E0" });
  });

  it("keeps typed letters readable on the learning frame (≥ 7:1)", () => {
    const frame = relativeLuminance("#14100D");
    const typed = relativeLuminance(SEMANTIC_COLORS.typing);
    expect((typed + 0.05) / (frame + 0.05)).toBeGreaterThanOrEqual(7);
  });

  it("scales --ui between 0.8 and 1.2 from 1600 × 900", () => {
    expect(uiScale(1600, 900)).toBe(1);
    expect(uiScale(1280, 720)).toBe(0.8);
    expect(uiScale(2560, 1440)).toBe(1.2);
    expect(uiScale(1920, 900)).toBe(1);
    expect(uiScale(0, 900)).toBe(1);
  });

  it("defines the tokens and a learning frame that never moves", () => {
    for (const name of ["--ui", "--kit-danger", "--kit-urgent", "--kit-money", "--kit-typing", "--kit-font-battle"]) {
      expect(KIT_CSS).toContain(name + ":");
    }
    expect(KIT_CSS).toContain("." + LEARNING_FRAME_CLASSES.root + " {");
    expect(KIT_CSS).toContain("animation: none;");
    expect(KIT_CSS).toContain("Be Vietnam Pro");
  });

  it("installs the styles once and writes --ui", () => {
    const nodes = new Map<string, unknown>();
    const properties = new Map<string, string>();
    const doc = {
      getElementById: (id: string) => nodes.get(id) ?? null,
      createElement: () => ({ id: "", textContent: null as string | null }),
      head: { append: (node: unknown) => nodes.set((node as { id: string }).id, node) },
      documentElement: { style: { setProperty: (name: string, value: string) => properties.set(name, value) } },
    };
    expect(installKitStyles(doc)).toBe(true);
    expect(installKitStyles(doc)).toBe(false);
    expect((nodes.get(KIT_STYLE_ID) as { textContent: string }).textContent).toBe(KIT_CSS);
    expect(applyUiScale(1280, 720, doc)).toBe(0.8);
    expect(properties.get("--ui")).toBe("0.8000");
  });
});
