function uniqueRecordIds(records, label) {
  const ids = new Set();
  for (const record of records) {
    const id = record?.id;
    if (typeof id !== "string" || !id.trim()) throw new Error(`${label}: missing record id`);
    if (ids.has(id)) throw new Error(`${label}: duplicate id ${id}`);
    ids.add(id);
  }
  return ids;
}

export function selectTypingTextReviewSlice({ candidates, controlled, reviewedIds, limit = 24 }) {
  if (!Number.isInteger(limit) || limit < 1 || limit > 200) {
    throw new Error("Review limit must be an integer from 1 to 200");
  }
  uniqueRecordIds(candidates, "Candidate queue");
  const controlledIds = uniqueRecordIds(controlled, "Controlled source");
  const decisionIds = new Set(reviewedIds);
  const excluded = new Set([...controlledIds, ...decisionIds]);
  const remaining = candidates.filter(record => !excluded.has(record.id));
  const records = remaining.slice(0, limit);
  for (const record of records) {
    if (record?.quality?.state !== "candidate") {
      throw new Error(`Next review record ${record.id} must remain candidate`);
    }
  }
  return {
    state: records.length === 0 ? "source-exhausted" : records.length < limit ? "partial" : "ready",
    records,
    selection: {
      strategy: "generator-order-after-controlled-and-ledger-exclusion-v1",
      requestedLimit: limit,
      candidateCount: candidates.length,
      controlledCount: controlledIds.size,
      reviewedDecisionCount: decisionIds.size,
      excludedCount: excluded.size,
      remainingBeforeSelection: remaining.length,
      selectedCount: records.length,
      remainingAfterSelection: remaining.length - records.length,
    },
  };
}
