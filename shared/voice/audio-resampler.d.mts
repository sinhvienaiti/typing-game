export class StreamingResampler {
  constructor(inputRate: number, outputRate?: number, taps?: number);
  push(block: Float32Array): Float32Array;
}
