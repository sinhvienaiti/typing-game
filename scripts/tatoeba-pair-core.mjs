import crypto from "node:crypto";
import fs from "node:fs";
import readline from "node:readline";

export function parseTatoebaSentenceRow(line, expectedLang) {
  const parts=String(line).replace(/\r$/u,"").split("\t");
  if (parts.length<2) return null;
  const id=Number(parts[0]);
  if (!Number.isSafeInteger(id)||id<=0) return null;

  let text;
  if (parts.length>=3&&parts[1]===expectedLang) text=parts.slice(2).join("\t");
  else text=parts.slice(1).join("\t");
  text=text.normalize("NFC").trim();
  if (!text) return null;
  return {id,text};
}

export function parseTatoebaLinkRow(line) {
  const parts=String(line).replace(/\r$/u,"").split("\t");
  if (parts.length<2) return null;
  const englishId=Number(parts[0]);
  const vietnameseId=Number(parts[1]);
  if (
    !Number.isSafeInteger(englishId)||
    !Number.isSafeInteger(vietnameseId)||
    englishId<=0||
    vietnameseId<=0
  ) return null;
  return {englishId,vietnameseId};
}

export function normalizedPairKey(english,vietnamese) {
  const normalize=value=>String(value)
    .normalize("NFKC")
    .trim()
    .replace(/\s+/gu," ")
    .toLocaleLowerCase("en-US");
  return normalize(english)+"\u0000"+normalize(vietnamese);
}

export function looksLikeLearningPair(english,vietnamese) {
  const en=String(english).trim();
  const vi=String(vietnamese).trim();
  if (en.length<8||en.length>260||vi.length<4||vi.length>320) return false;
  if (/https?:\/\//iu.test(en)||/https?:\/\//iu.test(vi)) return false;
  if (/[<>\u0000-\u0008\u000B\u000C\u000E-\u001F]/u.test(en+vi)) return false;
  const enWords=en.match(/[A-Za-z]+(?:['’-][A-Za-z]+)*/gu)??[];
  if (enWords.length<4||enWords.length>22) return false;
  const enLetters=(en.match(/[A-Za-z]/gu)??[]).length;
  if (enLetters/Math.max(1,en.length)<0.55) return false;
  const viLetters=(vi.match(/\p{L}/gu)??[]).length;
  if (viLetters/Math.max(1,vi.length)<0.45) return false;
  return true;
}

export function selectEvenly(items,limit) {
  const count=Math.min(Math.max(0,Math.floor(limit)),items.length);
  if (count===0) return [];
  if (count===items.length) return [...items];
  const selected=[];
  const used=new Set();
  for (let index=0;index<count;index++) {
    let position=Math.floor(((index+0.5)*items.length)/count);
    position=Math.min(items.length-1,Math.max(0,position));
    while (used.has(position)&&position+1<items.length) position++;
    while (used.has(position)&&position>0) position--;
    used.add(position);
    selected.push(items[position]);
  }
  return selected;
}

export async function sha256File(file) {
  const hash=crypto.createHash("sha256");
  for await (const chunk of fs.createReadStream(file)) hash.update(chunk);
  return hash.digest("hex");
}

export async function readSentenceMap(file,expectedLang) {
  const result=new Map();
  const lines=readline.createInterface({
    input:fs.createReadStream(file,{encoding:"utf8"}),
    crlfDelay:Infinity,
  });
  for await (const line of lines) {
    const row=parseTatoebaSentenceRow(line,expectedLang);
    if (row!==null) result.set(row.id,row.text);
  }
  return result;
}

export async function readLinks(file) {
  const result=[];
  const lines=readline.createInterface({
    input:fs.createReadStream(file,{encoding:"utf8"}),
    crlfDelay:Infinity,
  });
  for await (const line of lines) {
    const row=parseTatoebaLinkRow(line);
    if (row!==null) result.push(row);
  }
  return result;
}
