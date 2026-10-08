import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const read = (path) => readFile(resolve(root, path), "utf8");

const [mapText, router, screen, server, catalog, childVocabulary, childTypingText, childRecall, childBoss] = await Promise.all([
  read("admin/space-typing-phase-b-map.v1.json"),
  read("portal/src/admin/space-typing-phase-b.ts"),
  read("portal/src/admin/space-typing-typing-content-phase-b.ts"),
  read("admin/server.mjs"),
  read("admin/typing-content-catalog.mjs"),
  read("games/space-typing/src/vocabulary.ts"),
  read("games/space-typing/src/typing-text.ts"),
  read("games/space-typing/src/recall/model.ts"),
  read("games/space-typing/src/boss/typing-mechanics.ts"),
]);

const map = JSON.parse(mapText);
const typingContent = map.screens.find((entry) => entry.route === "/admin/space-typing/typing-content");
assert.ok(typingContent, "Typing Content route must exist in Phase B map");
assert.equal(typingContent.domain, "learning-content-references");
assert.equal(typingContent.persistence, "reference-manifest");
assert.equal(typingContent.status, "phase-b-ui-wired-canonical-readonly");

assert.match(router, /renderPhaseBTypingContent/);
assert.match(router, /\/typing-content/);
assert.match(server, /\/api\/admin\/space-typing\/typing-content\/catalog/);
assert.match(catalog, /shared\/vocabulary/);
assert.match(catalog, /shared\/typing-texts/);
assert.match(catalog, /canonical-readonly/);

for (const label of ["Vocabulary", "Typing Text", "Boss Text", "Recall", "Objectives"]) assert.match(screen, new RegExp(label));
for (const column of ["Content ID", "Title / Word", "CEFR", "Topic", "Difficulty", "Length", "Used By", "Status"]) assert.match(screen, new RegExp(column.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")));
assert.doesNotMatch(screen, /Save Draft/);
assert.match(screen, /Editing is intentionally disabled here/);

assert.match(childVocabulary, /\/vocabulary\/index\.json/);
assert.match(childTypingText, /const DEFAULT_BASE = "\/shared\/typing-texts\/"/);
assert.match(childTypingText, /cleanBase\(base\) \+ "index\.json"/);
assert.match(childTypingText, /loadTypingTextChallenge/);
assert.match(childRecall, /VocabularyEntry/);
assert.match(childBoss, /TypingMechanic/);

console.log("Space Typing Typing Content canonical read/reference integration: PASS");
