/** Stateful band-limited conversion. Capture, including suspended periods, owns this clock. */
export class StreamingResampler {
  constructor(inputRate, outputRate = 16000, taps = 32) {
    if (
      !Number.isFinite(inputRate) ||
      !Number.isFinite(outputRate) ||
      inputRate < outputRate ||
      outputRate < 8000 ||
      !Number.isInteger(taps) ||
      taps % 2 !== 0 ||
      taps < 16
    )
      throw new RangeError("Unsupported capture rate");
    this.ratio = inputRate / outputRate;
    this.taps = taps;
    this.input = Array(taps / 2).fill(0);
    this.position = taps / 2;
    this.base = 0;
    this.cutoff = 0.45 / this.ratio;
    // 48 kHz uses one fractional phase; 44.1 kHz uses 160. Reuse FIR
    // coefficients instead of evaluating ~1M sin/cos calls per audio second.
    this.kernels = new Map();
  }
  kernel(fraction) {
    const key = Math.round(fraction * 1e9);
    const cached = this.kernels.get(key);
    if (cached) return cached;
    const half = this.taps / 2, weights = new Float64Array(this.taps);
    let total = 0;
    for (let i = 0; i < this.taps; i++) {
      const distance = i - half + 1 - fraction;
      const x = 2 * this.cutoff * distance;
      const sinc = Math.abs(x) < 1e-9 ? 1 : Math.sin(Math.PI * x) / (Math.PI * x);
      const window = 0.5 + 0.5 * Math.cos(Math.PI * distance / half);
      total += weights[i] = 2 * this.cutoff * sinc * window;
    }
    if (total) for (let i = 0; i < weights.length; i++) weights[i] /= total;
    // Unusual fractional device rates must not grow a session-long cache.
    if (this.kernels.size < 512) this.kernels.set(key, weights);
    return weights;
  }
  push(block) {
    for (const value of block)
      this.input.push(Number.isFinite(value) ? value : 0);
    const result = [],
      half = this.taps / 2;
    while (this.position + half < this.input.length) {
      let sum = 0;
      const center = Math.floor(this.position);
      const weights = this.kernel(this.position - center);
      for (let j = center - half + 1; j <= center + half; j++) {
        sum += this.input[j] * weights[j - center + half - 1];
      }
      result.push(sum);
      this.position += this.ratio;
    }
    const discard = Math.max(0, Math.floor(this.position) - half);
    if (discard) {
      this.input.splice(0, discard);
      this.position -= discard;
      this.base += discard;
    }
    return Float32Array.from(result);
  }
}
