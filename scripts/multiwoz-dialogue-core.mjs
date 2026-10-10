import crypto from "node:crypto";
import fs from "node:fs/promises";

export async function gitBlobSha1(file) {
  const body=await fs.readFile(file);
  const header=Buffer.from("blob "+String(body.length)+"\0","utf8");
  return crypto.createHash("sha1").update(header).update(body).digest("hex");
}

export function normalizeDialogueText(value) {
  return String(value)
    .normalize("NFKC")
    .trim()
    .replace(/\s+/gu," ")
    .toLocaleLowerCase("en-US");
}

export function parseMultiwozDialogue(raw) {
  if (raw===null||typeof raw!=="object"||Array.isArray(raw)) return null;
  if (typeof raw.dialogue_id!=="string"||raw.dialogue_id.trim()==="") return null;
  if (!Array.isArray(raw.services)||!Array.isArray(raw.turns)) return null;
  const services=raw.services
    .filter(value=>typeof value==="string"&&value.trim()!=="")
    .map(value=>value.trim().toLocaleLowerCase("en-US"));
  const turns=[];
  for (const rawTurn of raw.turns) {
    if (rawTurn===null||typeof rawTurn!=="object"||Array.isArray(rawTurn)) return null;
    const speaker=rawTurn.speaker;
    const utterance=typeof rawTurn.utterance==="string"
      ? rawTurn.utterance.normalize("NFC").trim().replace(/\s+/gu," ")
      : "";
    if ((speaker!=="USER"&&speaker!=="SYSTEM")||utterance==="") return null;
    turns.push({speaker,utterance});
  }
  return {dialogueId:raw.dialogue_id.trim(),services,turns};
}

export function isLearningDialogue(dialogue) {
  if (dialogue.services.length===0||dialogue.services.length>2) return false;
  if (dialogue.turns.length<4||dialogue.turns.length>10) return false;
  let totalWords=0;
  let previousSpeaker="";
  const utterances=new Set();
  for (const turn of dialogue.turns) {
    if (turn.speaker===previousSpeaker) return false;
    previousSpeaker=turn.speaker;
    if (turn.utterance.length<5||turn.utterance.length>240) return false;
    if (/https?:\/\//iu.test(turn.utterance)) return false;
    if (/\b\d{7,}\b/u.test(turn.utterance)) return false;
    if (/\b(?=[A-Z0-9]{7,}\b)(?=[A-Z0-9]*\d)[A-Z0-9]+\b/u.test(turn.utterance)) return false;
    if (/[\u0000-\u0008\u000B\u000C\u000E-\u001F]/u.test(turn.utterance)) return false;
    const normalized=normalizeDialogueText(turn.utterance);
    if (utterances.has(normalized)) return false;
    utterances.add(normalized);
    totalWords+=(turn.utterance.match(/[A-Za-z]+(?:['’-][A-Za-z]+)*/gu)??[]).length;
  }
  return totalWords>=30&&totalWords<=180;
}

export function selectEvenly(items,limit) {
  if (items.length<limit) throw new Error("Need "+limit+" candidates, got "+items.length);
  if (items.length===limit) return [...items];
  const selected=[],used=new Set();
  for (let index=0;index<limit;index++) {
    let position=Math.floor(((index+0.5)*items.length)/limit);
    position=Math.min(items.length-1,Math.max(0,position));
    while (used.has(position)&&position+1<items.length) position++;
    while (used.has(position)&&position>0) position--;
    used.add(position);
    selected.push(items[position]);
  }
  return selected;
}
