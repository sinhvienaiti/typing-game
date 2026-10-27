// 100 ms blocks, each dispatched immediately. Three seconds is the outstanding-
// audio ceiling: decoding is bursty (the first feature window, and the final
// lattice at each utterance end), and the runtime recovers from an overflow by
// dropping that utterance and restarting the recognizer, not by failing.
export const CAPTURE_BLOCK_SAMPLES = 1600;
export const CAPTURE_MAX_PENDING = 30;
