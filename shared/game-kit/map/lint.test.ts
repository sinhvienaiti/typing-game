import { readdirSync, readFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import ts from "typescript";
import { describe, expect, it } from "vitest";

const mapDirectory = dirname(fileURLToPath(import.meta.url));

function isCoreFile(relativePath: string): boolean {
  return relativePath.endsWith(".ts") && !relativePath.endsWith(".test.ts");
}

function coreFiles(directory: string, prefix = ""): string[] {
  return readdirSync(directory, { withFileTypes: true }).flatMap((entry) => {
    const relativePath = prefix + entry.name;
    if (entry.isDirectory()) return coreFiles(join(directory, entry.name), relativePath + "/");
    return entry.isFile() && isCoreFile(relativePath) ? [relativePath] : [];
  }).sort();
}

const bannedMath = new Set([
  "acos", "acosh", "asin", "asinh", "atan", "atanh", "atan2", "cbrt", "cos", "cosh",
  "exp", "expm1", "hypot", "log", "log1p", "log10", "log2", "pow", "random",
  "sin", "sinh", "tan", "tanh",
]);

const K = ts.SyntaxKind;
const expressionEnds = new Set<ts.SyntaxKind>([
  K.Identifier, K.ThisKeyword, K.SuperKeyword, K.TrueKeyword, K.FalseKeyword,
  K.NullKeyword, K.NumericLiteral, K.BigIntLiteral, K.StringLiteral,
  K.NoSubstitutionTemplateLiteral, K.TemplateTail, K.RegularExpressionLiteral,
  K.CloseParenToken, K.CloseBracketToken, K.CloseBraceToken,
  K.PlusPlusToken, K.MinusMinusToken,
]);

type ScannedToken = { kind: ts.SyntaxKind; text: string; position: number };

function violations(file: string, text: string): string[] {
  const scanner = ts.createScanner(ts.ScriptTarget.ES2022, true, ts.LanguageVariant.Standard, text);
  const stack: ("tpl" | "brace")[] = [];
  const tokens: ScannedToken[] = [];
  let previous = K.Unknown;
  for (let kind = scanner.scan(); kind !== K.EndOfFileToken; kind = scanner.scan()) {
    if ((kind === K.SlashToken || kind === K.SlashEqualsToken) && !expressionEnds.has(previous)) {
      kind = scanner.reScanSlashToken();
    }
    if (kind === K.TemplateHead) {
      stack.push("tpl");
    } else if (kind === K.OpenBraceToken) {
      stack.push("brace");
    } else if (kind === K.CloseBraceToken) {
      if (stack.at(-1) === "tpl") {
        kind = scanner.reScanTemplateToken(false);
        if (kind === K.TemplateTail) stack.pop();
      } else if (stack.at(-1) === "brace") {
        stack.pop();
      }
    }
    tokens.push({ kind, text: scanner.getTokenText(), position: scanner.getTokenPos() });
    previous = kind;
  }

  const found: string[] = [];
  const isAccess = (token: ScannedToken | undefined): boolean =>
    token?.kind === K.DotToken || token?.kind === K.QuestionDotToken;
  for (let index = 0; index < tokens.length; index += 1) {
    const token = tokens[index]!;
    let banned = token.kind === K.AsteriskAsteriskToken || token.kind === K.AsteriskAsteriskEqualsToken;
    if (token.kind === K.Identifier && !isAccess(tokens[index - 1])) {
      if (token.text === "Date" || token.text === "performance") banned = true;
      if (token.text === "Math") {
        const next = tokens[index + 1];
        const member = tokens[index + 2];
        if (next?.kind === K.OpenBracketToken) banned = true;
        if (isAccess(next) && member?.kind === K.Identifier && bannedMath.has(member.text)) banned = true;
      }
    }
    if (banned) {
      const line = text.slice(0, token.position).split("\n").length;
      found.push(`${file}:${line}: ${token.text}`);
    }
  }
  return found;
}

describe("map deterministic lint", () => {
  it.each([
    ["hash.ts", true],
    ["layers/fields.ts", true],
    ["edt.test.ts", false],
    ["lint.test.ts", false],
    ["nested/performance.test.ts", false],
    ["tsconfig.json", false],
  ] as const)("filters %s: %s", (file, expected) => {
    expect(isCoreFile(file)).toBe(expected);
  });

  const bannedSamples = [
    "const a = Math.sin(x);",
    "Math.cos(x)",
    "Math.tan(x)",
    "Math.atan2(y, x)",
    "Math.pow(x, 2)",
    "Math.hypot(x, y)",
    "Math.exp(x)",
    "Math.log(x)",
    "Math.cbrt(x)",
    "Math.random()",
    "const t = Date.now();",
    "new Date()",
    "performance.now()",
    "x ** 2",
    "x **= 2",
    "Math['sin'](x)",
    'const s = `${Math.sin(x)}`;',
    'const s = `a ${b} c ${Math.pow(x, 2)} d`;',
    "if (x) { y = 1; } const z = 2 ** 3;",
  ];
  it.each(bannedSamples)("finds exactly one violation: %s", (sample) => {
    expect(violations("sample.ts", sample)).toHaveLength(1);
  });

  const cleanSamples = [
    "/** Uses no Math.sin; enumerate cells. x ** 2 Date performance */ const a = 1;",
    "// Math.sin is banned, so is Date and **\nconst a = 1;",
    'const s = "enumerate Math.sin Date performance **";',
    "const s = 'Math.cos';",
    'const t = `Math.cos ${x} Date ** performance`;',
    "const r = /[**]/;",
    "const r = a / b / c;",
    "const q = (a) / 2 / (b);",
    "const v = Math.sqrt(x) + Math.floor(y) + Math.round(z) + Math.imul(a, b) + Math.max(1, 2) + Math.min(1, 2) + Math.abs(x) + Math.trunc(x) + Math.sign(x) + Math.clz32(x);",
    "const p = item.performance + item.Date;",
    'const t = { a: `${`${x}`}` }; const r2 = /\\*\\*/g;',
  ];
  it.each(cleanSamples)("accepts the clean sample: %s", (sample) => {
    expect(violations("sample.ts", sample)).toEqual([]);
  });

  it.each([...bannedMath])("rejects all approximate/random Math methods, including optional access: %s", (method) => {
    expect(violations("sample.ts", `Math.${method}(x)`)).toHaveLength(1);
    expect(violations("sample.ts", `Math?.${method}(x)`)).toHaveLength(1);
  });

  it("handles nested templates, expression braces, computed access and regex rescanning", () => {
    expect(violations("sample.ts", 'const t = `${({ a: `${Math.sin(x)}` }).a} ${Date.now()}`;')).toHaveLength(2);
    expect(violations("sample.ts", "const r = /=Math.sin Date performance **/; const n = 1;")).toEqual([]);
    expect(violations("sample.ts", "item.Math.sin(x); item?.Math.random(); item?.Date; item?.performance;")).toEqual([]);
    expect(violations("sample.ts", "Math[x](y)")).toHaveLength(1);
    expect(violations("sample.ts", "Math.ceil(x) + Math.fround(x)")).toEqual([]);
    expect(violations("sample.ts", "performance.now()")).toHaveLength(1);
    expect(isCoreFile("timing.test.ts")).toBe(false);
  });

  it("reports each location once as file:line:token", () => {
    expect(violations("layers/sample.ts", "// ignored\nMath.sin(x);\nDate.now(); performance.now(); x **= 2;"))
      .toEqual(["layers/sample.ts:2: Math", "layers/sample.ts:3: Date", "layers/sample.ts:3: performance", "layers/sample.ts:3: **="]);
  });

  it("scans every core file recursively in filename order", () => {
    const files = coreFiles(mapDirectory);
    const found = files.flatMap((file) => violations(file, readFileSync(join(mapDirectory, file), "utf8")));
    console.info(`Map core files (${files.length}): ${files.join(", ")}; violations: ${found.length}`);
    expect(files.length).toBeGreaterThanOrEqual(3);
    expect(found).toEqual([]);
  });

  it("enforces erasableSyntaxOnly on virtual sources with a clean control", () => {
    const config = ts.readConfigFile(join(mapDirectory, "tsconfig.json"), ts.sys.readFile);
    expect(config.error).toBeUndefined();
    const parsed = ts.parseJsonConfigFileContent(config.config, ts.sys, mapDirectory);
    expect(parsed.errors).toEqual([]);
    expect(parsed.options.erasableSyntaxOnly).toBe(true);

    const virtualFile = join(mapDirectory, "__virtual__", "sample.ts");
    const diagnosticsFor = (source: string): readonly ts.Diagnostic[] => {
      const host = ts.createCompilerHost(parsed.options);
      const originalGetSourceFile = host.getSourceFile.bind(host);
      const originalFileExists = host.fileExists.bind(host);
      const originalReadFile = host.readFile.bind(host);
      const isVirtual = (file: string): boolean => resolve(file) === virtualFile;
      host.getSourceFile = (file, languageVersion, onError, shouldCreateNewSourceFile) =>
        isVirtual(file)
          ? ts.createSourceFile(file, source, languageVersion, true)
          : originalGetSourceFile(file, languageVersion, onError, shouldCreateNewSourceFile);
      host.fileExists = (file) => isVirtual(file) || originalFileExists(file);
      host.readFile = (file) => isVirtual(file) ? source : originalReadFile(file);
      const program = ts.createProgram([virtualFile], parsed.options, host);
      return ts.getPreEmitDiagnostics(program);
    };

    for (const source of [
      "export enum Kind { A, B }",
      "export namespace N { export const a = 1; }",
      "export class C { constructor(private readonly a: number) {} }",
    ]) {
      expect(diagnosticsFor(source).map((diagnostic) => diagnostic.code), source).toContain(1294);
    }
    expect(diagnosticsFor("export const a: number = 1;")).toEqual([]);
  }, 30000);
});
