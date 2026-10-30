import { stableJson } from "./english-content-core.mjs";
import { validateMultiwozDialogueEditorialFinalizationOutputs } from "./multiwoz-editorial-finalization-validation-core.mjs";

function requireObject(value,label) {
  if (!value || typeof value !== "object" || Array.isArray(value)) {
    throw new TypeError(label+" must be an object");
  }
  return value;
}

function requireText(value,label) {
  if (typeof value !== "string" || value.trim() === "") {
    throw new TypeError(label+" must be a non-empty string");
  }
  return value.trim();
}

function recordSetPaths(batch) {
  if (!Array.isArray(batch?.recordSets) || batch.recordSets.length === 0) {
    throw new TypeError(String(batch?.id??"unknown batch")+": recordSets must be a non-empty array");
  }
  return batch.recordSets.map((recordSet,index)=>requireText(
    recordSet?.path,
    String(batch.id)+" recordSets["+index+"] path",
  ));
}

export function registerMultiwozDialogueBatchManifest({
  manifest,
  authoring,
  proposal,
  handoff,
  packet,
  intake,
  pin,
}) {
  requireObject(manifest,"batch manifest");
  if (manifest.schemaVersion !== 1) throw new TypeError("batch manifest schemaVersion must be 1");
  requireText(manifest.contentVersion,"batch manifest contentVersion");
  if (!Array.isArray(manifest.batches)) throw new TypeError("batch manifest batches must be an array");

  const finalization=validateMultiwozDialogueEditorialFinalizationOutputs({
    authoring,
    proposal,
    handoff,
    packet,
    intake,
    pin,
  });
  const proposedBatch=requireObject(proposal.batch,"proposal batch");
  const batchId=requireText(proposedBatch.id,"proposal batch id");
  const proposedPaths=recordSetPaths(proposedBatch);
  if (new Set(proposedPaths).size !== proposedPaths.length) {
    throw new TypeError(batchId+": proposal contains duplicate record-set paths");
  }

  const existingById=manifest.batches.find((batch)=>batch?.id===batchId);
  if (existingById) {
    if (stableJson(existingById) !== stableJson(proposedBatch)) {
      throw new TypeError("Batch registration collision for "+batchId+": existing manifest batch differs from validated proposal");
    }
    return {
      manifest,
      status:"already-registered",
      batchId,
      recordCount:finalization.recordCount,
      authoringDigest:finalization.authoringDigest,
      reviewDecisions:finalization.reviewDecisions,
      runtimePublication:finalization.runtimePublication,
    };
  }

  const proposedPathSet=new Set(proposedPaths);
  for (const batch of manifest.batches) {
    const existingId=requireText(batch?.id,"existing batch id");
    for (const existingPath of recordSetPaths(batch)) {
      if (proposedPathSet.has(existingPath)) {
        throw new TypeError(
          "Batch registration path collision: "+existingPath+" is already owned by "+existingId,
        );
      }
    }
  }

  const nextManifest=structuredClone(manifest);
  nextManifest.batches.push(structuredClone(proposedBatch));
  return {
    manifest:nextManifest,
    status:"registered",
    batchId,
    recordCount:finalization.recordCount,
    authoringDigest:finalization.authoringDigest,
    reviewDecisions:finalization.reviewDecisions,
    runtimePublication:finalization.runtimePublication,
  };
}
