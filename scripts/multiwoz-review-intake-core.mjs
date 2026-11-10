import fs from "node:fs/promises";
import path from "node:path";
import { englishContentRecordDigest, englishContentReviewSourceDigest } from "./english-review-core.mjs";
import { stableJson } from "./english-content-core.mjs";

function requireText(value,label) {
  if (typeof value!=="string"||value.trim()==="") throw new TypeError(label+" must be a non-empty string");
  return value.trim();
}

function expectedRecordId(sourceId) {
  return "dlg.multiwoz."+sourceId.toLocaleLowerCase("en-US").replace(/[^a-z0-9._-]+/gu,"-");
}

function pinnedFiles(pin) {
  return [
    {path:requireText(pin?.path,"MultiWOZ pin path"),blobSha1:requireText(pin?.blobSha1,"MultiWOZ pin blobSha1")},
    ...(pin?.additionalFiles??[]).map((item,index)=>({
      path:requireText(item?.path,"MultiWOZ additionalFiles["+index+"] path"),
      blobSha1:requireText(item?.blobSha1,"MultiWOZ additionalFiles["+index+"] blobSha1"),
    })),
  ].sort((left,right)=>left.path.localeCompare(right.path,"en"));
}

function assertObservedFiles(packet,pin) {
  const expected=pinnedFiles(pin);
  const observed=(packet?.source?.observedFiles??[])
    .map((item,index)=>({
      path:requireText(item?.path,"packet observedFiles["+index+"] path"),
      blobSha1:requireText(item?.blobSha1,"packet observedFiles["+index+"] blobSha1"),
    }))
    .sort((left,right)=>left.path.localeCompare(right.path,"en"));
  if (stableJson(observed)!==stableJson(expected)) {
    throw new TypeError("MultiWOZ review packet observed files do not match the pinned Git blobs");
  }
  return expected;
}

function assertPacketSource(packet,pin) {
  if (packet?.schemaVersion!==1||packet?.kind!=="english-content-review-packet") {
    throw new TypeError("MultiWOZ intake requires an english-content-review-packet schemaVersion 1");
  }
  if (packet?.batchFamily!=="e11.dialogue-multiwoz") {
    throw new TypeError("MultiWOZ intake requires batchFamily e11.dialogue-multiwoz");
  }
  if (packet?.source?.dataset!=="multiwoz") throw new TypeError("MultiWOZ intake requires dataset multiwoz");
  if (packet?.source?.repository!==pin.repository||packet?.source?.commit!==pin.commit||packet?.source?.version!==pin.version) {
    throw new TypeError("MultiWOZ review packet source identity does not match the pinned source");
  }
  if (packet?.source?.pinned!==true) throw new TypeError("MultiWOZ review packet must declare pinned=true");
  return assertObservedFiles(packet,pin);
}

export function buildMultiwozDialogueReviewIntake(packet,pin) {
  const files=assertPacketSource(packet,pin);
  if (packet?.recordSet?.recordSetId!=="dialogues"||!Array.isArray(packet?.recordSet?.records)) {
    throw new TypeError("MultiWOZ intake requires recordSet dialogues with records[]");
  }
  const records=packet.recordSet.records;
  if (records.length===0) throw new TypeError("MultiWOZ intake requires at least one candidate record");
  const requestedLimit=packet?.selection?.requestedLimit;
  if (!Number.isInteger(requestedLimit)||requestedLimit<1||records.length>requestedLimit) {
    throw new TypeError("MultiWOZ intake record count must not exceed selection.requestedLimit");
  }

  const selectedIds=packet?.selection?.selectedDialogueIds;
  if (!Array.isArray(selectedIds)||selectedIds.length!==records.length) {
    throw new TypeError("MultiWOZ intake requires selectedDialogueIds for every candidate");
  }
  const selectedSet=new Set(selectedIds.map(value=>requireText(value,"selectedDialogueIds item")));
  if (selectedSet.size!==selectedIds.length) throw new TypeError("MultiWOZ intake selectedDialogueIds contain duplicates");

  const seenRecordIds=new Set();
  const seenSourceIds=new Set();
  const entries=[];
  for (const [index,record] of records.entries()) {
    const recordId=requireText(record?.id,"candidate record["+index+"] id");
    if (seenRecordIds.has(recordId)) throw new TypeError("MultiWOZ intake duplicate record id: "+recordId);
    seenRecordIds.add(recordId);
    if (record?.quality?.state!=="candidate") {
      throw new TypeError(recordId+": MultiWOZ intake only accepts quality.state=candidate");
    }
    if (record?.quality?.checks?.sourcePin?.status!=="pass") {
      throw new TypeError(recordId+": MultiWOZ intake requires sourcePin=pass");
    }

    const sources=record?.provenance?.sources;
    if (!Array.isArray(sources)||sources.length!==1||sources[0]?.dataset!=="multiwoz") {
      throw new TypeError(recordId+": MultiWOZ intake requires exactly one multiwoz provenance source");
    }
    const source=sources[0];
    const sourceId=requireText(source?.sourceId,recordId+" sourceId");
    if (seenSourceIds.has(sourceId)) throw new TypeError("MultiWOZ intake duplicate sourceId: "+sourceId);
    seenSourceIds.add(sourceId);
    if (!selectedSet.has(sourceId)) throw new TypeError(recordId+": sourceId is absent from selectedDialogueIds");
    if (recordId!==expectedRecordId(sourceId)) throw new TypeError(recordId+": record id does not match stable MultiWOZ source identity");
    if (source.snapshot!==pin.commit||source.license!==pin.license||source.attribution!==pin.attribution||source.modified!==false) {
      throw new TypeError(recordId+": provenance does not match the pinned MultiWOZ source");
    }
    const allowedPrefix="https://github.com/"+pin.repository+"/blob/"+pin.commit+"/";
    const sourceUrl=requireText(source?.sourceUrl,recordId+" sourceUrl");
    const sourcePath=sourceUrl.startsWith(allowedPrefix)?sourceUrl.slice(allowedPrefix.length):"";
    if (!files.some(file=>file.path===sourcePath)) {
      throw new TypeError(recordId+": sourceUrl is outside the pinned MultiWOZ files");
    }
    entries.push({recordId,sourceId,sourceDigest:englishContentReviewSourceDigest(record)});
  }
  if (seenSourceIds.size!==selectedSet.size||[...selectedSet].some(id=>!seenSourceIds.has(id))) {
    throw new TypeError("MultiWOZ intake selectedDialogueIds do not match candidate provenance source IDs");
  }

  entries.sort((left,right)=>left.recordId.localeCompare(right.recordId,"en"));
  const recordSetDigest=englishContentRecordDigest(entries.map(({recordId,sourceDigest})=>({recordId,sourceDigest})));
  return {
    schemaVersion:1,
    kind:"english-content-review-intake",
    intakeId:"e11.dialogue-multiwoz.next",
    batchFamily:packet.batchFamily,
    recordSetId:packet.recordSet.recordSetId,
    state:"candidate",
    source:{
      dataset:"multiwoz",
      version:pin.version,
      repository:pin.repository,
      commit:pin.commit,
      files,
      pinned:true,
    },
    candidateCount:entries.length,
    recordSetDigest,
    records:entries,
    lifecycle:{
      batchRegistration:"pending-editorial-authoring",
      reviewDecisions:"not-created",
      runtimePublication:"blocked",
    },
  };
}

export async function writeImmutableReviewIntake(filePath,intake) {
  const body=stableJson(intake);
  try {
    const current=await fs.readFile(filePath,"utf8");
    if (current!==body) {
      throw new Error("Review intake collision at "+filePath+": existing bytes differ from the deterministic intake");
    }
    return {state:"unchanged",bytes:Buffer.byteLength(body)};
  } catch (error) {
    if (error?.code!=="ENOENT") throw error;
  }
  await fs.mkdir(path.dirname(filePath),{recursive:true});
  await fs.writeFile(filePath,body,"utf8");
  return {state:"written",bytes:Buffer.byteLength(body)};
}
