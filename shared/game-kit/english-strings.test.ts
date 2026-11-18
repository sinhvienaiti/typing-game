import { readdirSync, readFileSync } from "node:fs";
import { dirname, join, relative } from "node:path";
import { fileURLToPath } from "node:url";
import ts from "typescript";
import { describe, expect, it } from "vitest";

const ROOT = dirname(fileURLToPath(import.meta.url));
const TEST_FILE = /\.(?:test|spec)(?:-helper)?\.ts$/;
const VIETNAMESE = /[àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ]/iu;
// Unambiguous words and phrases from kit UI/report copy, including unaccented copy.
const UNACCENTED = /\b(?:trong|sau|thieu|khong|nhanh|thang|thap|cao|lech|bat dau|hoan hao|can bang|thu gian|thu thach)\b/iu;
const MEANING_FIELDS = new Set(["vi", "meaningVi", "translationVi", "glossVi", "definitionVi", "exampleVi", "sentenceVi"]);
// Exact IME detection data, never display copy.
const IME_LETTERS = new Set([
  "àáạảãâầấậẩẫăằắặẳẵ", "èéẹẻẽêềếệểễ", "ìíịỉĩ", "òóọỏõôồốộổỗơờớợởỡ",
  "ùúụủũưừứựửữ", "ỳýỵỷỹ", "đ",
]);

function sourceFiles(dir: string): string[] {
  return readdirSync(dir, { withFileTypes: true }).flatMap((entry) => {
    if (entry.name === "node_modules") return [];
    const path = join(dir, entry.name);
    return entry.isDirectory() ? sourceFiles(path) : path.endsWith(".ts") && !TEST_FILE.test(path) ? [path] : [];
  }).sort();
}

function isMeaning(node: ts.Node): boolean {
  for (let parent = node.parent; parent; parent = parent.parent) {
    if (ts.isPropertyAssignment(parent) || ts.isPropertyDeclaration(parent) || ts.isVariableDeclaration(parent)) {
      return (ts.isIdentifier(parent.name) || ts.isStringLiteral(parent.name)) && MEANING_FIELDS.has(parent.name.text);
    }
  }
  return false;
}

function isImeData(file: string, node: ts.Node, text: string): boolean {
  if (file !== "input/keys.ts" || !IME_LETTERS.has(text)) return false;
  for (let parent = node.parent; parent; parent = parent.parent) {
    if (ts.isVariableDeclaration(parent)) return ts.isIdentifier(parent.name) && parent.name.text === "VIETNAMESE_LETTERS";
  }
  return false;
}

function violations(file: string, text: string): string[] {
  if (TEST_FILE.test(file)) return [];
  const source = ts.createSourceFile(file, text, ts.ScriptTarget.Latest, true);
  const found: string[] = [];
  function visit(node: ts.Node): void {
    if (ts.isStringLiteral(node) || ts.isNoSubstitutionTemplateLiteral(node) || ts.isTemplateHead(node) || ts.isTemplateMiddle(node) || ts.isTemplateTail(node)) {
      const value = node.text.normalize("NFC");
      if ((VIETNAMESE.test(value) || UNACCENTED.test(value)) && !isMeaning(node) && !isImeData(file, node, value)) {
        const line = source.getLineAndCharacterOfPosition(node.getStart(source)).line + 1;
        found.push(`${file}:${line}: ${JSON.stringify(node.text)}`);
      }
    }
    ts.forEachChild(node, visit);
  }
  visit(source);
  return found;
}

describe("English kit strings", () => {
  it("keeps UI and developer report literals in English", () => {
    const files = sourceFiles(ROOT);
    const found = files.flatMap((path) => violations(relative(ROOT, path), readFileSync(path, "utf8")));
    console.log(`English string scan: ${files.length} source files; ${found.length} violations`);
    expect(found, found.join("\n")).toEqual([]);
  });

  it("detects accents, escapes, decomposed text and unaccented Vietnamese", () => {
    for (const value of ["Bắt đầu", "Thiếu", "trong", "sau", "Nhanh", "bat dau", "Bắt đầu".normalize("NFD"), "\\u0042\\u1eaf\\u0074 \\u0111\\u1ea7\\u0075"]) {
      expect(violations("ui/example.ts", `export const label = "${value}";`)).toHaveLength(1);
    }
  });

  it("checks every static part of a template and nested expressions", () => {
    const source = 'const hint = `Bắt đầu ${count} sau ${time} Thiếu`; const other = `${"trong"}`;';
    expect(violations("ui/example.ts", source)).toHaveLength(4);
  });

  it("allows comments, tests and vocabulary meanings without hiding nearby labels", () => {
    expect(violations("ui/example.ts", '// "Bắt đầu"\n/* "Thiếu" */\nconst label = "Start";')).toEqual([]);
    expect(violations("ui/example.test.ts", 'const label = "Bắt đầu";')).toEqual([]);
    expect(violations("ui/example.ts", 'const word = { vi: "cảm ơn", meaningVi: `nghĩa ${id}`, label: "Bắt đầu" };')).toHaveLength(1);
    expect(violations("ui/example.ts", 'const word = { vi: { label: "Bắt đầu" } };')).toHaveLength(1);
  });

  it("limits the IME exemption to exact character data in its original binding", () => {
    const source = 'const VIETNAMESE_LETTERS = new Set(["đ", "Bắt đầu"]); const label = "đ";';
    expect(violations("input/keys.ts", source)).toHaveLength(2);
    expect(violations("ui/example.ts", source)).toHaveLength(3);
  });
});
