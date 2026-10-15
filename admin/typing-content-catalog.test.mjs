import test from "node:test";
import assert from "node:assert/strict";
import { fileURLToPath } from "node:url";
import { resolve } from "node:path";
import { clearTypingContentCatalogCacheForTests, queryTypingContentCatalog } from "./typing-content-catalog.mjs";

const rootDir = resolve(fileURLToPath(new URL("..", import.meta.url)));

test("Typing Content catalog reads canonical shared vocabulary without copying it", async () => {
  clearTypingContentCatalogCacheForTests();
  const result = await queryTypingContentCatalog({
    rootDir,
    searchParams: new URLSearchParams({ kind: "vocabulary", q: "L001-001", limit: "10" }),
  });

  assert.equal(result.mode, "canonical-readonly");
  assert.equal(result.owner, "English Learning Content System");
  assert.equal(result.canonicalTotals.vocabulary, 18000);
  assert.equal(result.canonicalTotals.vocabularyLevels, 100);
  assert.equal(result.total, 1);
  assert.deepEqual(result.items[0], {
    id: "L001-001",
    title: "good",
    type: "vocabulary",
    cefr: "Foundation",
    topics: result.items[0].topics,
    difficulty: "Level 1",
    length: 4,
    usedBy: ["combat", "recall", "smart-review"],
    status: "canonical",
    source: "shared/vocabulary",
    level: 1,
    meaning: "tốt; hay",
    ipa: "/ɡʊd/",
  });
});

test("Typing Content catalog exposes canonical topic filters for vocabulary", async () => {
  const result = await queryTypingContentCatalog({
    rootDir,
    searchParams: new URLSearchParams({ kind: "vocabulary", q: "morning", topic: "everyday.greetings", limit: "20" }),
  });

  assert.ok(result.total >= 1);
  assert.ok(result.items.some((item) => item.title === "morning"));
  assert.ok(result.items.every((item) => item.topics.some((topic) => topic.includes("everyday.greetings"))));
});

test("Typing Content catalog reads canonical typing-text passages and preserves CEFR metadata", async () => {
  const result = await queryTypingContentCatalog({
    rootDir,
    searchParams: new URLSearchParams({ kind: "typing-text", q: "family morning", level: "1", cefr: "A1", limit: "10" }),
  });

  assert.equal(result.canonicalTotals.typingText, 300);
  assert.equal(result.canonicalTotals.typingTextLevels, 20);
  assert.ok(result.total >= 1);
  const passage = result.items.find((item) => item.id === "L001-P001");
  assert.ok(passage);
  assert.equal(passage.source, "shared/typing-texts");
  assert.equal(passage.cefr, "A1");
  assert.equal(passage.length, 256);
  assert.deepEqual(passage.usedBy, ["special-stage-typing"]);
  assert.ok(passage.excerpt.startsWith("Morning begins quietly"));
});

test("Typing Content metadata keeps non-catalog tabs explicit instead of inventing records", async () => {
  const result = await queryTypingContentCatalog({ rootDir, searchParams: new URLSearchParams({ limit: "1" }) });
  assert.equal(result.tabs.bossText.status, "derived");
  assert.equal(result.tabs.recall.status, "derived");
  assert.equal(result.tabs.objectives.status, "gameplay-owned");
});
