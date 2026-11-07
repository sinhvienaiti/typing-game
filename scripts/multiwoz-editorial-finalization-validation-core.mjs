import { stableJson } from "./english-content-core.mjs";
import { buildMultiwozDialogueEditorialFinalization } from "./multiwoz-editorial-finalization-core.mjs";

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

function assertStableEqual(actual,expected,label) {
  const actualBytes=stableJson(actual);
  const expectedBytes=stableJson(expected);
  if (actualBytes !== expectedBytes) {
    throw new TypeError(label+" drifted from the deterministic editorial finalization output");
  }
}

export function validateMultiwozDialogueEditorialFinalizationOutputs({
  authoring,
  proposal,
  handoff,
  packet,
  intake,
  pin,
}) {
  requireObject(authoring,"authoring");
  requireObject(proposal,"proposal");
  requireObject(handoff,"handoff");
  requireObject(packet,"packet");
  requireObject(intake,"intake");
  requireObject(pin,"pin");

  if (proposal.schemaVersion !== 1) throw new TypeError("proposal schemaVersion must be 1");
  if (proposal.kind !== "english-content-batch-registration-proposal") {
    throw new TypeError("proposal kind must be english-content-batch-registration-proposal");
  }
  const proposalId=requireText(proposal.proposalId,"proposal id");
  const batchId=requireText(proposal?.batch?.id,"proposal batch id");
  if (proposalId!==batchId) {
    throw new TypeError("proposal id must match proposal batch id");
  }
  const authoringPath=requireText(proposal.authoringPath,"proposal authoringPath");
  if (!authoringPath.startsWith("content/english/sentences/")) {
    throw new TypeError("proposal authoringPath must stay under content/english/sentences/");
  }

  const expected=buildMultiwozDialogueEditorialFinalization(
    handoff,
    packet,
    intake,
    pin,
    {authoringPath,batchId,proposalId},
  );

  assertStableEqual(authoring,expected.authoring,"authoring output");
  assertStableEqual(proposal,expected.proposal,"batch-registration proposal");

  const records=authoring.records;
  if (!Array.isArray(records) || records.length === 0) {
    throw new TypeError("authoring output must contain at least one finalized record");
  }
  for (const record of records) {
    if (record?.quality?.state !== "draft") {
      throw new TypeError(String(record?.id??"unknown")+": finalized authoring quality.state must remain draft");
    }
  }
  if (proposal?.batch?.state !== "draft") {
    throw new TypeError("batch-registration proposal must remain draft");
  }
  if (proposal?.lifecycle?.batchRegistration !== "ready-for-manifest-registration") {
    throw new TypeError("batch-registration proposal is not ready for manifest registration");
  }
  if (proposal?.lifecycle?.reviewDecisions !== "not-created") {
    throw new TypeError("batch-registration proposal must not contain created review decisions");
  }
  if (proposal?.lifecycle?.runtimePublication !== "blocked") {
    throw new TypeError("batch-registration proposal must keep runtime publication blocked");
  }

  return {
    state:"valid",
    proposalId:proposal.proposalId,
    authoringPath,
    authoringDigest:proposal.authoringDigest,
    recordCount:records.length,
    acceptedCount:proposal.acceptedCount,
    editedCount:proposal.editedCount,
    rejectedCount:proposal.rejectedCount,
    batchRegistration:proposal.lifecycle.batchRegistration,
    reviewDecisions:proposal.lifecycle.reviewDecisions,
    runtimePublication:proposal.lifecycle.runtimePublication,
  };
}
