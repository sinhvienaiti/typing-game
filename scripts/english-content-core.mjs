import crypto from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";

export const CEFR_LEVELS = Object.freeze(["A1","A2","B1","B2","C1","C2"]);

export function normalizeSpacing(value) {
  return String(value).normalize("NFKC").trim().replace(/\s+/g," ");
}
export function normalizeEnglishKey(value) {
  return normalizeSpacing(value).toLocaleLowerCase("en-US");
}
export function normalizeSentenceKey(value) {
  return String(value).normalize("NFC").trim().replace(/\s+/g," ").replace(/\s+([,.;:!?])/g,"$1").toLocaleLowerCase("en-US");
}
export function stableFingerprint(value) {
  return crypto.createHash("sha256").update(String(value),"utf8").digest("hex");
}
export function sentenceFingerprint(text) {
  return stableFingerprint(normalizeSentenceKey(text));
}
export function lexicalTokens(value) {
  return normalizeSentenceKey(value).replace(/[^\p{L}\p{N}'’-]+/gu," ").split(/\s+/).filter(Boolean);
}
export function tokenJaccard(left,right) {
  const a=new Set(lexicalTokens(left)); const b=new Set(lexicalTokens(right));
  if (a.size===0&&b.size===0) return 1;
  if (a.size===0||b.size===0) return 0;
  let intersection=0; for (const token of a) if (b.has(token)) intersection++;
  return intersection/(a.size+b.size-intersection);
}
export function nearDuplicatePairs(records,threshold=0.86) {
  if (!Number.isFinite(threshold)||threshold<0||threshold>1) throw new RangeError("Jaccard threshold must be between 0 and 1");
  // Exact prefix filtering: every qualifying pair must share a prefix token in
  // this one global token order. Length bounds and final full-set intersection
  // preserve the previous Jaccard semantics; this is not approximate sampling.
  const rows=records.map(record=>({record,key:normalizeSentenceKey(record.text),tokens:new Set(lexicalTokens(record.text))}));
  const frequency=new Map();
  for (const row of rows) for (const token of row.tokens) frequency.set(token,(frequency.get(token)??0)+1);
  const compare=(a,b)=>frequency.get(a)-frequency.get(b)||(a<b?-1:a>b?1:0);
  const postings=new Map();
  const empty=[];
  const pairs=[];
  for (let j=0;j<rows.length;j++) {
    const right=rows[j];
    const size=right.tokens.size;
    const ordered=[...right.tokens].sort(compare);
    const prefix=ordered.slice(0,Math.max(0,size-Math.ceil(threshold*size-1e-12)+1));
    const candidates=new Set();
    if (threshold===0) for (let i=0;i<j;i++) candidates.add(i);
    else if (size===0) for (const i of empty) candidates.add(i);
    else for (const token of prefix) for (const i of postings.get(token)??[]) {
      const otherSize=rows[i].tokens.size;
      if (otherSize+1e-12>=threshold*size&&size+1e-12>=threshold*otherSize) candidates.add(i);
    }
    for (const i of candidates) {
      const left=rows[i];
      if (left.key===right.key) continue;
      let intersection=0;
      const smaller=left.tokens.size<size?left.tokens:right.tokens;
      const larger=smaller===left.tokens?right.tokens:left.tokens;
      for (const token of smaller) if (larger.has(token)) intersection++;
      const union=left.tokens.size+size-intersection;
      const score=union===0?1:intersection/union;
      if (score>=threshold) pairs.push({i,j,leftId:left.record.id,rightId:right.record.id,score:Number(score.toFixed(4))});
    }
    if (size===0) empty.push(j);
    for (const token of prefix) {
      if (!postings.has(token)) postings.set(token,[]);
      postings.get(token).push(j);
    }
  }
  return pairs.sort((a,b)=>a.i-b.i||a.j-b.j).map(({i,j,...pair})=>pair);
}
export async function readJson(file) { return JSON.parse(await fs.readFile(file,"utf8")); }
export async function listJsonFiles(root) {
  const result=[];
  async function walk(dir) {
    let entries;
    try { entries=await fs.readdir(dir,{withFileTypes:true}); } catch (error) { if (error?.code==="ENOENT") return; throw error; }
    for (const entry of entries) {
      const target=path.join(dir,entry.name);
      if (entry.isDirectory()) await walk(target);
      else if (entry.isFile()&&entry.name.endsWith(".json")) result.push(target);
    }
  }
  await walk(root); return result.sort();
}
function resolvePointer(root,fragment) {
  if (!fragment||fragment==="#") return root;
  if (!fragment.startsWith("#/")) throw new Error("Unsupported schema fragment: "+fragment);
  return fragment.slice(2).split("/").reduce((value,raw)=>value?.[raw.replace(/~1/g,"/").replace(/~0/g,"~")],root);
}
function typeMatches(value,expected) {
  if (expected==="null") return value===null;
  if (expected==="array") return Array.isArray(value);
  if (expected==="object") return value!==null&&typeof value==="object"&&!Array.isArray(value);
  if (expected==="integer") return Number.isInteger(value);
  if (expected==="number") return typeof value==="number"&&Number.isFinite(value);
  return typeof value===expected;
}
export function createSchemaValidator(schemas) {
  const byId=new Map(schemas.map(schema=>[schema.$id,schema]));
  function validate(value,schema,at="$",errors=[],rootSchema=schema) {
    if (schema===true) return errors;
    if (schema===false) { errors.push(at+": schema rejects all values"); return errors; }
    if (schema.$ref) {
      const hash=schema.$ref.indexOf("#");
      const base=hash===-1?schema.$ref:schema.$ref.slice(0,hash);
      const fragment=hash===-1?"#":schema.$ref.slice(hash);
      const targetRoot=base?byId.get(base):rootSchema;
      if (!targetRoot) { errors.push(at+": unresolved $ref "+schema.$ref); return errors; }
      const target=resolvePointer(targetRoot,fragment);
      if (!target) { errors.push(at+": unresolved $ref "+schema.$ref); return errors; }
      return validate(value,target,at,errors,targetRoot);
    }
    if (schema.const!==undefined&&value!==schema.const) errors.push(at+": expected const "+JSON.stringify(schema.const));
    if (Array.isArray(schema.enum)&&!schema.enum.includes(value)) errors.push(at+": value is not in enum");
    if (schema.type!==undefined) {
      const types=Array.isArray(schema.type)?schema.type:[schema.type];
      if (!types.some(type=>typeMatches(value,type))) { errors.push(at+": expected type "+types.join("|")); return errors; }
    }
    if (typeof value==="string") {
      if (schema.minLength!==undefined&&value.length<schema.minLength) errors.push(at+": shorter than minLength");
      if (schema.maxLength!==undefined&&value.length>schema.maxLength) errors.push(at+": longer than maxLength");
      if (schema.pattern!==undefined&&!(new RegExp(schema.pattern)).test(value)) errors.push(at+": pattern mismatch");
    }
    if (typeof value==="number") {
      if (schema.minimum!==undefined&&value<schema.minimum) errors.push(at+": below minimum");
      if (schema.maximum!==undefined&&value>schema.maximum) errors.push(at+": above maximum");
    }
    if (Array.isArray(value)) {
      if (schema.minItems!==undefined&&value.length<schema.minItems) errors.push(at+": fewer than minItems");
      if (schema.maxItems!==undefined&&value.length>schema.maxItems) errors.push(at+": more than maxItems");
      if (schema.uniqueItems) {
        const seen=new Set();
        for (const item of value) { const key=JSON.stringify(item); if (seen.has(key)) { errors.push(at+": duplicate array item"); break; } seen.add(key); }
      }
      if (schema.items) value.forEach((item,index)=>validate(item,schema.items,at+"["+index+"]",errors,rootSchema));
    }
    if (value!==null&&typeof value==="object"&&!Array.isArray(value)) {
      for (const key of schema.required??[]) if (!(key in value)) errors.push(at+": missing required property "+key);
      const properties=schema.properties??{};
      for (const [key,item] of Object.entries(value)) {
        if (properties[key]!==undefined) validate(item,properties[key],at+"."+key,errors,rootSchema);
        else if (schema.additionalProperties===false) errors.push(at+": unsupported property "+key);
        else if (schema.additionalProperties&&typeof schema.additionalProperties==="object") validate(item,schema.additionalProperties,at+"."+key,errors,rootSchema);
      }
    }
    return errors;
  }
  return {validate};
}
export function stableJson(value) { return JSON.stringify(value,null,2)+"\n"; }
