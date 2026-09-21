import { readFile } from "node:fs/promises";

const css = await readFile("portal/src/styles.css", "utf8");

const rules = [
  {
    name: "portal shell reserves a definite game row",
    pattern: /\.portal-shell\s*\{[^}]*height:\s*100%[^}]*grid-template-rows:\s*48px\s+minmax\(0,\s*1fr\)/s,
  },
  {
    name: "route host has a definite height",
    pattern: /\.route-host\s*\{[^}]*height:\s*100%/s,
  },
  {
    name: "game stage fills the route host",
    pattern: /\.game-stage\s*\{[^}]*height:\s*100%/s,
  },
  {
    name: "game iframe fills the game stage",
    pattern: /\.game-frame\s*\{[^}]*position:\s*absolute[^}]*inset:\s*0[^}]*height:\s*100%/s,
  },
];

const failed = rules.filter((rule) => !rule.pattern.test(css));
if (failed.length > 0) {
  for (const rule of failed) {
    console.error(`Portal layout contract failed: ${rule.name}`);
  }
  process.exit(1);
}

console.log("Portal full-height game layout contract: OK");
