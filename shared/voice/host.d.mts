import type { VoiceSnapshot } from "./protocol.mjs";
export type LocalRuntime = {
  engineId: string; modelId: string; sampleRate: number;
  nowSample(): number; suspend(): Promise<void>; resume(): Promise<void>; flush(): Promise<void>; close(): Promise<void>;
  applyTargets(snapshot: VoiceSnapshot): Promise<{ ready: string[]; unsupported: string[] }>;
  unsupportedForms?(forms: string[]): string[];
};
export class VoiceHost {
  constructor(options: {
    requestMicrophone(): Promise<MediaStream>;
    cancelMicrophone?(): void;
    createRuntime(stream: MediaStream, options: { sessionId: string; onDetection(value: unknown): boolean; onFeedback(value: unknown): boolean; onClock(sample: number): void }): Promise<LocalRuntime>;
    createSessionId(): string; onEvent?(event: Record<string, unknown>): void;
    waitTail?(ms: number): Promise<void>; echoTailMs?: number;
  });
  state: string; session: { sessionId: string; inputEpoch: number; audioEpoch: number } | null;
  start(inputEpoch: number): Promise<boolean>; stop(): Promise<void>;
  applyTargets(value: unknown): Promise<boolean>;
  checkVocabulary(value: Record<string, unknown>): boolean;
  suspend(inputEpoch: number): Promise<boolean>; resume(inputEpoch: number): Promise<boolean>;
  audioOutputIntent(generation: number): Promise<boolean>; audioOutputEnded(generation: number): Promise<boolean>;
}
