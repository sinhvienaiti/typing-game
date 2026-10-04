import type { OfflineRecognizer } from "./decoder";
export const WARMUP_SAMPLES: number;
export function primeRecognizer(recognizer: OfflineRecognizer, signal?: AbortSignal): Promise<void>;
