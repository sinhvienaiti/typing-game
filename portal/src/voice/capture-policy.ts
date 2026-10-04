// 100 ms blocks; one second is a hard outstanding-audio ceiling, not a batching
// delay. Each block is dispatched immediately. Vosk decoding is bursty (notably
// its first feature window); the old 3-block cap disconnected healthy startup.
export const CAPTURE_BLOCK_SAMPLES = 1600;
export const CAPTURE_MAX_PENDING = 10;
