import type { VoiceSnapshot, VoiceTarget } from './protocol.mjs';
export type FinalWord = { word: string; conf: number; start: number; end: number };
export function matchFinalWords(words: FinalWord[], snapshots: VoiceSnapshot[], baseSample: number, sampleRate: number, confidenceFloor?: number): Array<{ target: VoiceTarget; snapshotId: string; form: string; audioStartSample: number; audioEndSample: number; length: number }>;
