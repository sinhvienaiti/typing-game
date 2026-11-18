import { applyLearningEvent, createEmptyLearningProfile } from '../../../shared/learning/core.mjs';

const rows = [
  ['vocabulary', 'lantern', 'typing-attack', 'correct', false, 1],
  ['vocabulary', 'dragon', 'meaning-recall', 'correct', false, 2],
  ['vocabulary', 'river', 'listening', 'wrong', false, 3],
  ['vocabulary', 'lantern', 'meaning-recall', 'correct', false, 4],
  ['vocabulary', 'dragon', 'review-card', 'correct', true, 5],
  ['vocabulary', 'river', 'review-card', 'correct', false, 6],
  ['vocabulary', 'lantern', 'listening', 'correct', false, 7],
  ['vocabulary', 'dragon', 'typing-attack', 'wrong', true, 8],
  ['grammar', 'present.simple', 'meaning-recall', 'wrong', false, 9],
  ['sentence', 'The lantern shines.', 'review-card', 'wrong', true, 10],
  ['vocabulary', 'river', 'review-card', 'correct', true, 11],
  ['vocabulary', 'lantern', 'meaning-recall', 'wrong', false, 3],
];
let profile = createEmptyLearningProfile();
for (const [entityType, entityId, activityType, result, hintUsed, minute] of rows) {
  profile = applyLearningEvent(profile, {
    version: 1, entityType, entityId, activityType, result, hintUsed,
    gameId: minute % 2 ? 'dragon-hold' : 'recall-typing',
    occurredAt: new Date(Date.UTC(2026, 9, 30, 6, minute)).toISOString(),
    responseMs: 900 + minute * 130, replayUsed: minute % 3 === 0,
    userAnswer: result === 'correct' ? entityId : 'mistake', expectedAnswer: entityId,
    ...(result === 'wrong' ? { errorType: 'spelling' } : {}),
  });
}
for (const collection of [profile.vocabulary, profile.grammar, profile.sentences]) {
  for (const record of Object.values(collection)) delete record.recentSamples;
}
process.stdout.write(JSON.stringify(profile, null, 2) + '\n');
