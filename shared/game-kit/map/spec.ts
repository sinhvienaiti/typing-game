import { sha256Hex } from "./sha256";

export const SPEC_FORMAT = "map-spec/0";
export const SPEC_LAYERS = ["fields", "height", "water", "paths", "dressing", "vegetation", "paint"] as const;
export type SpecLayerName = (typeof SPEC_LAYERS)[number];
export const SPEC_ERROR_CODES = [
  "spec-json", "type", "required", "unknown-key", "not-integer", "range", "permille-range", "pattern", "const",
  "cell-not-even", "layer-version-missing", "pin-id-format", "budget-missing", "gameplay-missing",
  "gameplay-adapter-mismatch", "gameplay-commit-mismatch", "gameplay-hash-mismatch", "kit-unknown", "proto-unknown",
] as const;
export type SpecErrorCode = (typeof SPEC_ERROR_CODES)[number];
export interface SpecError { readonly code: SpecErrorCode; readonly path: string }

export type SpecValue = number | string | boolean | readonly SpecValue[] | { readonly [key: string]: SpecValue };
export type SpecPoint = readonly [number, number];
export type SpecLayerBlock = { readonly [key: string]: SpecValue };
export interface SpecRegion { readonly id: string; readonly poly: readonly SpecPoint[]; readonly reason?: string }
export type SpecPin =
  | { readonly keep: string }
  | { readonly proto: string; readonly at: SpecPoint; readonly yawDeg?: number; readonly scalePermille?: number;
      readonly variant?: string; readonly clearOnBuild?: boolean; readonly note?: string };
export interface SpecBudgetTier { readonly propTriangles: number; readonly drawCalls: number; readonly loadMs: number }
export interface MapSpec {
  readonly format: "map-spec/0";
  readonly id: string;
  readonly game: string;
  readonly title?: string;
  readonly unit: "cm";
  readonly seed: number;
  readonly generator: { readonly factory: string; readonly layers: { readonly [K in SpecLayerName]?: number } };
  readonly gameplay: { readonly adapter: string; readonly commit: string; readonly hash: string };
  readonly registry: { readonly scan: string; readonly kit: string };
  readonly extent: { readonly cellCm: number; readonly [key: string]: number };
  readonly review?: { readonly pitchesDeg: readonly number[]; readonly yawsDeg: readonly number[] };
  readonly layers: { readonly [K in SpecLayerName]?: SpecLayerBlock };
  readonly exclude?: readonly SpecRegion[];
  readonly include?: readonly SpecRegion[];
  readonly pins?: readonly SpecPin[];
  readonly budget: { readonly high: SpecBudgetTier; readonly medium?: SpecBudgetTier; readonly low?: SpecBudgetTier };
}
export interface SpecGameplayRef { readonly game: string; readonly map: string; readonly adapter: string; readonly commit: string; readonly hash: string }
export interface SpecKitRef { readonly kit: string; readonly game: string; readonly protos: readonly string[] }
export interface SpecContext { readonly gameplays?: readonly SpecGameplayRef[]; readonly kits?: readonly SpecKitRef[] }

type RecordValue = Record<string, unknown>;
const MAP_ID = /^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*$/;
const KEBAB = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;
const SEMVER = /^(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)$/;
const ADAPTER = /^([a-z0-9]+(?:-[a-z0-9]+)*)@[1-9][0-9]*$/;
const HEX40 = /^[0-9a-f]{40}$/;
const HEX64 = /^[0-9a-f]{64}$/;
const DATE_PATTERN = /^[0-9]{4}-[0-9]{2}-[0-9]{2}$/;
const KIT = /^[a-z0-9]+(?:-[a-z0-9]+)*@[1-9][0-9]*$/;
const EXTENT_KEY = /^[a-z][A-Za-z0-9]*Cm$/;
const PIN_ID = /^[a-z]+:[a-z][A-Za-z0-9]*:c(0|-?[1-9][0-9]*)_(0|-?[1-9][0-9]*):(0|[1-9][0-9]*)$/;

function object(value: unknown): value is RecordValue {
  return value !== null && typeof value === "object" && !Array.isArray(value);
}
function matches(value: unknown, pattern: RegExp): value is string {
  return typeof value === "string" && pattern.test(value);
}
function pointer(path: string, key: string | number): string {
  return path + "/" + String(key).replace(/~/g, "~0").replace(/\//g, "~1");
}
function unitKey(key: string): boolean {
  return ["Permille", "Deg", "Cm", "Ms"].some((suffix) => key.endsWith(suffix));
}

/** Structural validation only; layer semantics belong to later generator versions. */
export function validateSpec(value: unknown, context?: SpecContext): SpecError[] {
  const errors: SpecError[] = [];
  const protos: { name: string; path: string }[] = [];
  const add = (code: SpecErrorCode, path: string): void => { errors.push({ code, path }); };
  function strict(v: unknown, path: string, allowed: readonly string[], required: readonly string[] = []): v is RecordValue {
    if (!object(v)) { add("type", path); return false; }
    for (const key of Object.keys(v)) if (!allowed.includes(key)) add("unknown-key", pointer(path, key));
    for (const key of required) if (!Object.hasOwn(v, key)) add("required", pointer(path, key));
    return true;
  }
  function integer(v: unknown, path: string, min: number, max: number, code: SpecErrorCode = "range"): v is number {
    if (typeof v !== "number") { add("type", path); return false; }
    if (!Number.isSafeInteger(v)) { add("not-integer", path); return false; }
    if (v < min || v > max) { add(code, path); return false; }
    return true;
  }
  function string(v: unknown, path: string, pattern?: RegExp, maxLength?: number): boolean {
    if (typeof v !== "string") { add("type", path); return false; }
    if ((pattern && !pattern.test(v)) || (maxLength !== undefined && v.length > maxLength)) {
      add("pattern", path); return false;
    }
    return true;
  }
  function each(v: RecordValue, path: string, key: string, check: (v: unknown, path: string) => unknown): void {
    if (Object.hasOwn(v, key)) check(v[key], pointer(path, key));
  }
  function array(v: unknown, path: string, check: (v: unknown, path: string) => void, min = 0, max = Infinity): void {
    if (!Array.isArray(v)) { add("type", path); return; }
    if (v.length < min || v.length > max) add("range", path);
    for (let i = 0; i < v.length; i += 1) check(v[i], pointer(path, i));
  }
  function point(v: unknown, path: string): void {
    if (!Array.isArray(v) || v.length !== 2) { add("type", path); return; }
    v.forEach((coordinate, i) => integer(coordinate, pointer(path, i), -16384, 16384));
  }
  function proto(v: unknown, path: string): void {
    if (string(v, path, KEBAB)) protos.push({ name: v as string, path });
  }
  function layer(v: unknown, path: string, unit = ""): void {
    if (typeof v === "number") {
      if (!Number.isSafeInteger(v)) { add("not-integer", path); return; }
      if (unit.endsWith("Permille")) {
        const scale = unit.startsWith("scale");
        integer(v, path, scale ? 1 : 0, scale ? 10000 : 1000, scale ? "range" : "permille-range");
      } else if (unit.endsWith("Deg")) integer(v, path, -360, 360);
      else if (unit.endsWith("Cm")) integer(v, path, -100000, 100000);
      else if (unit.endsWith("Ms")) integer(v, path, 0, 60000);
    } else if (Array.isArray(v)) {
      for (let i = 0; i < v.length; i += 1) layer(v[i], pointer(path, i), unit);
    } else if (object(v)) {
      for (const key of Object.keys(v)) {
        const child = pointer(path, key);
        if (key === "id") string(v[key], child, MAP_ID);
        else if (key === "proto") proto(v[key], child);
        else if (key === "mix") {
          const mix = v[key];
          if (!object(mix)) { add("type", child); continue; }
          for (const name of Object.keys(mix)) {
            const entry = pointer(child, name);
            if (KEBAB.test(name)) protos.push({ name, path: entry });
            else add("pattern", entry);
            integer(mix[name], entry, 1, 1000);
          }
        } else layer(v[key], child, unitKey(key) ? key : unit);
      }
    } else if (typeof v !== "string" && typeof v !== "boolean") add("type", path);
  }
  function region(v: unknown, path: string): void {
    if (!strict(v, path, ["id", "poly", "reason"], ["id", "poly"])) return;
    each(v, path, "id", (v, p) => string(v, p, MAP_ID));
    each(v, path, "poly", (v, p) => array(v, p, point, 3));
    each(v, path, "reason", string);
  }
  function pin(v: unknown, path: string): void {
    if (!object(v)) { add("type", path); return; }
    if (Object.hasOwn(v, "keep")) {
      strict(v, path, ["keep"]);
      if (typeof v.keep !== "string") { add("type", pointer(path, "keep")); return; }
      const match = PIN_ID.exec(v.keep);
      if (!match || Number(match[1]) < -2147483648 || Number(match[1]) > 2147483647
          || Number(match[2]) < -2147483648 || Number(match[2]) > 2147483647 || Number(match[3]) > 2147483647) {
        add("pin-id-format", pointer(path, "keep"));
      }
    } else {
      strict(v, path, ["proto", "at", "yawDeg", "scalePermille", "variant", "clearOnBuild", "note"], ["proto", "at"]);
      each(v, path, "proto", proto);
      each(v, path, "at", point);
      each(v, path, "yawDeg", (v, p) => integer(v, p, -360, 360));
      each(v, path, "scalePermille", (v, p) => integer(v, p, 1, 10000));
      each(v, path, "variant", string);
      each(v, path, "note", string);
      each(v, path, "clearOnBuild", (v, p) => { if (typeof v !== "boolean") add("type", p); });
    }
  }
  const allowed = ["format", "id", "game", "title", "unit", "seed", "generator", "gameplay", "registry", "extent", "review", "layers", "exclude", "include", "pins", "budget"];
  if (!strict(value, "", allowed, ["format", "id", "game", "unit", "seed", "generator", "gameplay", "registry", "extent", "layers"])) return errors;
  each(value, "", "format", (v, p) => { if (v !== SPEC_FORMAT) add("const", p); });
  each(value, "", "unit", (v, p) => { if (v !== "cm") add("const", p); });
  each(value, "", "id", (v, p) => string(v, p, MAP_ID, 64));
  each(value, "", "game", (v, p) => string(v, p, KEBAB));
  each(value, "", "title", string);
  each(value, "", "seed", (v, p) => integer(v, p, 0, 4294967295));
  each(value, "", "generator", (v, p) => {
    if (!strict(v, p, ["factory", "layers"], ["factory", "layers"])) return;
    each(v, p, "factory", (v, p) => string(v, p, SEMVER));
    each(v, p, "layers", (v, p) => {
      if (!strict(v, p, SPEC_LAYERS)) return;
      for (const name of SPEC_LAYERS) each(v, p, name, (v, p) => integer(v, p, 1, 1000000));
    });
  });
  each(value, "", "gameplay", (v, p) => {
    if (!strict(v, p, ["adapter", "commit", "hash"], ["adapter", "commit", "hash"])) return;
    each(v, p, "adapter", (v, p) => {
      if (string(v, p, ADAPTER) && typeof value.game === "string" && ADAPTER.exec(v as string)![1] !== value.game) add("pattern", p);
    });
    each(v, p, "commit", (v, p) => string(v, p, HEX40));
    each(v, p, "hash", (v, p) => string(v, p, HEX64));
  });
  each(value, "", "registry", (v, p) => {
    if (!strict(v, p, ["scan", "kit"], ["scan", "kit"])) return;
    each(v, p, "scan", (v, p) => string(v, p, DATE_PATTERN));
    each(v, p, "kit", (v, p) => string(v, p, KIT));
  });
  each(value, "", "extent", (v, p) => {
    if (!object(v)) { add("type", p); return; }
    if (!Object.hasOwn(v, "cellCm")) add("required", pointer(p, "cellCm"));
    for (const key of Object.keys(v)) {
      const child = pointer(p, key);
      if (!EXTENT_KEY.test(key)) { add("unknown-key", child); continue; }
      if (integer(v[key], child, 1, 16384) && key === "cellCm" && (v[key] as number) % 2 !== 0) add("cell-not-even", child);
    }
  });
  each(value, "", "review", (v, p) => {
    if (!strict(v, p, ["pitchesDeg", "yawsDeg"], ["pitchesDeg", "yawsDeg"])) return;
    for (const key of ["pitchesDeg", "yawsDeg"]) each(v, p, key, (v, p) => array(v, p, (v, p) => { integer(v, p, 0, key === "pitchesDeg" ? 90 : 359); }, 1, 12));
  });
  each(value, "", "layers", (v, p) => {
    if (!strict(v, p, SPEC_LAYERS)) return;
    const versions = object(value.generator) && object(value.generator.layers) ? value.generator.layers : undefined;
    for (const key of SPEC_LAYERS) each(v, p, key, (v, p) => {
      if (versions && !Object.hasOwn(versions, key)) add("layer-version-missing", p);
      if (!object(v)) add("type", p);
      else layer(v, p);
    });
  });
  for (const key of ["exclude", "include"]) each(value, "", key, (v, p) => array(v, p, region));
  each(value, "", "pins", (v, p) => array(v, p, pin));
  if (!Object.hasOwn(value, "budget")) add("budget-missing", "/budget");
  each(value, "", "budget", (v, p) => {
    if (!strict(v, p, ["high", "medium", "low"])) return;
    if (!Object.hasOwn(v, "high")) add("budget-missing", pointer(p, "high"));
    for (const tier of ["high", "medium", "low"]) each(v, p, tier, (v, p) => {
      if (!strict(v, p, ["propTriangles", "drawCalls", "loadMs"], ["propTriangles", "drawCalls", "loadMs"])) return;
      each(v, p, "propTriangles", (v, p) => integer(v, p, 1, 100000000));
      each(v, p, "drawCalls", (v, p) => integer(v, p, 1, 100000));
      each(v, p, "loadMs", (v, p) => integer(v, p, 1, 60000));
    });
  });
  if (context?.gameplays && matches(value.game, KEBAB) && matches(value.id, MAP_ID) && value.id.length <= 64 && object(value.gameplay)) {
    const ref = context.gameplays.find((ref) => ref.game === value.game && ref.map === value.id);
    if (!ref) add("gameplay-missing", "/gameplay");
    else {
      const gp = value.gameplay;
      if (matches(gp.adapter, ADAPTER) && ADAPTER.exec(gp.adapter)![1] === value.game && gp.adapter !== ref.adapter) add("gameplay-adapter-mismatch", "/gameplay/adapter");
      if (matches(gp.commit, HEX40) && gp.commit !== ref.commit) add("gameplay-commit-mismatch", "/gameplay/commit");
      if (matches(gp.hash, HEX64) && gp.hash !== ref.hash) add("gameplay-hash-mismatch", "/gameplay/hash");
    }
  }
  if (context?.kits && object(value.registry) && matches(value.registry.kit, KIT)) {
    const kitName = value.registry.kit;
    const kit = context.kits.find((kit) => kit.kit === kitName);
    if (!kit || kit.game !== value.game) add("kit-unknown", "/registry/kit");
    else for (const { name, path } of protos) if (!kit.protos.includes(name)) add("proto-unknown", path);
  }
  const unique = new Map<string, SpecError>();
  for (const error of errors) unique.set(JSON.stringify([error.code, error.path]), error);
  return [...unique.values()].sort((a, b) => a.path < b.path ? -1 : a.path > b.path ? 1 : a.code < b.code ? -1 : a.code > b.code ? 1 : 0);
}

export function canonicalJson(value: unknown): string {
  if (typeof value === "number") {
    if (!Number.isSafeInteger(value)) throw new TypeError("Expected a safe integer");
    return String(value);
  }
  if (value === null || typeof value === "string" || typeof value === "boolean") return JSON.stringify(value);
  if (Array.isArray(value)) {
    const items: string[] = [];
    for (let i = 0; i < value.length; i += 1) {
      if (!Object.hasOwn(value, i)) throw new TypeError("Sparse arrays are not JSON");
      items.push(canonicalJson(value[i]));
    }
    return "[" + items.join(",") + "]";
  }
  if (object(value)) return "{" + Object.keys(value).sort().map((key) => JSON.stringify(key) + ":" + canonicalJson(value[key])).join(",") + "}";
  throw new TypeError("Unsupported JSON value");
}

const utf8 = new TextEncoder();
export function specHash(spec: unknown): string {
  return sha256Hex(utf8.encode(canonicalJson(spec)));
}
