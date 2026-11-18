// What a Typing Feel revision changes against another (§3.4 "Phạm vi thay đổi").
// Always for all games: the Review step shows this with an "Affects all games" chip.

function setsById(config) {
  return new Map((config?.keyboard?.sets ?? []).map((set) => [set.id, set]));
}

/** Shown set ids in catalogue order (family order, then set order), as the export writes them. */
export function catalogueOrder(config) {
  const families = new Map((config?.keyboard?.families ?? []).map((family) => [family.id, family.order]));
  return (config?.keyboard?.sets ?? [])
    .filter((set) => set.enabled)
    .sort((a, b) => (families.get(a.family) ?? 0) - (families.get(b.family) ?? 0) || a.order - b.order || a.id.localeCompare(b.id))
    .map((set) => set.id);
}

const same = (left, right) => JSON.stringify(left ?? null) === JSON.stringify(right ?? null);

export function describeTypingFeelChangeScope({ baseRevision = null, targetRevision = null, baseConfig, targetConfig }) {
  const base = setsById(baseConfig);
  const target = setsById(targetConfig);
  const retiredBefore = new Set(baseConfig?.keyboard?.retiredIds ?? []);
  const scope = {
    added: [],
    addedDetails: [],
    hidden: [],
    shown: [],
    retired: [],
    reformatted: [],
    renamed: [],
    familyChanged: [],
    statusChanged: [],
    detailsChanged: [],
    reordered: [],
    defaultChanged: null,
    effectsChanged: [],
    familiesChanged: false,
  };
  for (const [id, set] of target) {
    const before = base.get(id);
    if (!before) {
      scope.added.push(id);
      continue;
    }
    if (before.enabled && !set.enabled) scope.hidden.push(id);
    if (!before.enabled && set.enabled) scope.shown.push(id);
    if (before.assetVersionId !== set.assetVersionId) scope.reformatted.push(id);
    if (before.name !== set.name) scope.renamed.push({ id, from: before.name, to: set.name });
    if (before.family !== set.family) scope.familyChanged.push({ id, from: before.family, to: set.family });
    if (before.status !== set.status) scope.statusChanged.push({ id, from: before.status, to: set.status });
    if (!same(before.note, set.note) || !same(before.ownerScore, set.ownerScore) || !same(before.labels, set.labels) || before.ownerPick !== set.ownerPick || before.recipe !== set.recipe || !same(before.score, set.score)) {
      scope.detailsChanged.push(id);
    }
  }
  for (const id of targetConfig?.keyboard?.retiredIds ?? []) if (!retiredBefore.has(id)) scope.retired.push(id);
  const beforeOrder = catalogueOrder(baseConfig);
  const afterOrder = catalogueOrder(targetConfig);
  const beforeIndex = new Map(beforeOrder.map((id, index) => [id, index]));
  // A set "moved" when its neighbours changed, not merely because a set above it was added or hidden.
  const common = afterOrder.filter((id) => beforeIndex.has(id));
  const commonBefore = beforeOrder.filter((id) => target.get(id)?.enabled);
  common.forEach((id, index) => {
    if (commonBefore[index] !== id) scope.reordered.push(id);
  });
  if (baseConfig?.keyboard?.defaultSet !== targetConfig?.keyboard?.defaultSet) {
    scope.defaultChanged = { from: baseConfig?.keyboard?.defaultSet ?? null, to: targetConfig?.keyboard?.defaultSet ?? null };
  }
  const effectsBefore = baseConfig?.effects?.defaults ?? {};
  const effectsAfter = targetConfig?.effects?.defaults ?? {};
  for (const field of ["style", "intensity", "size", "volume"]) {
    if (!same(effectsBefore[field], effectsAfter[field])) scope.effectsChanged.push({ field, from: effectsBefore[field] ?? null, to: effectsAfter[field] ?? null });
  }
  scope.familiesChanged = !same(baseConfig?.keyboard?.families, targetConfig?.keyboard?.families);

  const summary = [];
  const list = (ids) => ids.join(", ");
  // Decision 5 (§8.3): whoever publishes to every game sees a new sound's status, owner score and, for a
  // Provisional set, its reason, in the Review and in the audit change scope.
  const verdict = (id) => {
    const set = target.get(id);
    const status = set.status === "provisional" ? "Provisional" : set.status === "published" ? "Published" : set.status;
    const score = typeof set.ownerScore === "number" ? `, owner score ${set.ownerScore}` : "";
    const reason = set.status === "provisional" && typeof set.note === "string" ? `: ${set.note}` : "";
    return `${id} (${status}${score}${reason})`;
  };
  scope.addedDetails = scope.added.map((id) => ({ id, status: target.get(id).status, ownerScore: target.get(id).ownerScore ?? null, note: target.get(id).note ?? null }));
  for (const id of scope.added) summary.push(`Add ${verdict(id)}.`);
  for (const id of scope.reformatted) summary.push(`New sound for ${verdict(id)}.`);
  if (scope.hidden.length) summary.push(`Hide ${list(scope.hidden)}: players using it move to the default on their next load.`);
  if (scope.shown.length) summary.push(`Show ${list(scope.shown)} again.`);
  if (scope.retired.length) summary.push(`Retire ${list(scope.retired)} for good: the id is never used again.`);
  for (const rename of scope.renamed) summary.push(`Rename ${rename.id}: ${rename.from} → ${rename.to}.`);
  for (const move of scope.familyChanged) summary.push(`Move ${move.id} from family ${move.from} to ${move.to}.`);
  for (const status of scope.statusChanged) summary.push(`${status.id}: ${status.from} → ${status.to}.`);
  if (scope.reordered.length) summary.push(`New order for ${list(scope.reordered)}.`);
  if (scope.familiesChanged) summary.push("Families renamed, added or reordered.");
  if (scope.defaultChanged) summary.push(`Default set: ${scope.defaultChanged.from} → ${scope.defaultChanged.to} (only players without a saved choice).`);
  for (const effect of scope.effectsChanged) summary.push(`Typing effect default ${effect.field}: ${effect.from} → ${effect.to} (only players without saved settings).`);
  if (scope.detailsChanged.length) summary.push(`Notes, labels or scores of ${list(scope.detailsChanged)}.`);
  const changed = summary.length > 0;
  return Object.freeze({
    model: "typing-feel-revision",
    affects: "all games",
    baseRevision,
    targetRevision,
    changed,
    ...scope,
    summary,
    publishWarning: changed
      ? "Publishing changes the keyboard sounds and typing defaults of every game on its next page load."
      : "No Typing Feel changes between these revisions.",
  });
}
