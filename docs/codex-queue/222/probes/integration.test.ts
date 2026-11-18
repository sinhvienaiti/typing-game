import { readFileSync } from "node:fs";
import { resolve } from "node:path";
import { afterEach, expect, it, vi } from "vitest";
import { createTitle } from "../../src/ui/title";

class ElementStub {
  className = ""; textContent = ""; hidden = false; disabled = false; src = ""; alt = ""; href = ""; target = "";
  dataset: Record<string, string> = {}; children: ElementStub[] = [];
  events = new Map<string, ((e: any) => void)[]>();
  classList = { toggle() {} };
  constructor(readonly ownerDocument: DocumentStub) {}
  append(...nodes: ElementStub[]) { this.children.push(...nodes); }
  setAttribute() {}
  addEventListener(key: string, fn: (e: any) => void) { this.events.set(key, [...this.events.get(key) ?? [], fn]); }
  remove() {}
}
class DocumentStub {
  nodes: ElementStub[] = [];
  createElement() { const node = new ElementStub(this); this.nodes.push(node); return node; }
}
afterEach(() => { vi.unstubAllEnvs(); vi.restoreAllMocks(); });

it("existing HUD and results headings must not receive the full-screen title layout", () => {
  const consumers = ["src/ui/hud.ts", "src/ui/results.ts", "src/ui/shop-strip.ts"];
  for (const file of consumers) expect(readFileSync(file, "utf8")).toMatch(/el\(doc,\s*"(?:span|div)",\s*"dh-title"/);
  const declarations: Record<string, string> = {};
  // Only direct single-class rules: these match every legacy heading regardless of its ancestors.
  for (const file of ["src/ui/styles/dh.css", "src/ui/styles/title.css"]) {
    const css = readFileSync(file, "utf8").replace(/\/\*[\s\S]*?\*\//g, "");
    for (const rule of css.matchAll(/([^{}]+)\{([^{}]*)\}/g)) {
      if (!rule[1]!.split(",").some(selector => selector.trim() === ".dh-title")) continue;
      for (const declaration of rule[2]!.split(";")) {
        const colon = declaration.indexOf(":");
        if (colon >= 0) declarations[declaration.slice(0, colon).trim()] = declaration.slice(colon + 1).trim();
      }
    }
  }
  expect(declarations, "HUD Hỏa Long, Loadout and Wordbook all match this global rule").not.toMatchObject({ position: "absolute", inset: "0", "z-index": "40", background: "#17130f" });
});

it("the default title must preserve the vocabulary Retry recovery promised by ticket 195", () => {
  vi.stubEnv("VITE_PORTAL_URL", ""); vi.spyOn(console, "warn").mockImplementation(() => {});
  const doc = new DocumentStub(); const title = createTitle(doc.createElement() as unknown as HTMLElement, { onStart: vi.fn() });
  title.show(); title.settle("words", "load-failed");
  for (const source of ["models", "ground", "dragons"] as const) title.settle(source);
  expect(title.state).toBe("blocked");
  expect(doc.nodes.find(node => node.textContent === "Start")?.disabled).toBe(true);
  expect(doc.nodes.filter(node => node.textContent === "Retry"), "network restored: user needs a recovery action without reloading the page").toHaveLength(1);
  title.dispose();
});

it("the normal test suite must not depend on an ignored file outside the standalone game repository", () => {
  const source = readFileSync("tests/app/idle-estimate.test.ts", "utf8");
  const literal = source.match(/resolve\("([^\"]*samples\.json)"\)/)![1]!;
  const gameRoot = resolve("."); const requiredFixture = resolve(literal);
  expect(requiredFixture.startsWith(gameRoot + "/"), "clean clone has no " + requiredFixture).toBe(true);
});
