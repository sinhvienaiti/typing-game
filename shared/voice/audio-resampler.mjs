/** Stateful band-limited conversion. Capture, including suspended periods, owns this clock. */
export class StreamingResampler {
  constructor(inputRate, outputRate = 16000, taps = 32) {
    if (
      !Number.isFinite(inputRate) ||
      inputRate < outputRate ||
      outputRate < 8000 ||
      !Number.isInteger(taps) ||
      taps < 16
    )
      throw new RangeError("Unsupported capture rate");
    this.ratio = inputRate / outputRate;
    this.taps = taps;
    this.input = Array(taps / 2).fill(0);
    this.position = taps / 2;
    this.base = 0;
    this.cutoff = 0.45 / this.ratio;
  }
  push(block) {
    for (const value of block)
      this.input.push(Number.isFinite(value) ? value : 0);
    const result = [],
      half = this.taps / 2;
    while (this.position + half < this.input.length) {
      let sum = 0,
        weight = 0;
      const center = Math.floor(this.position);
      for (let j = center - half + 1; j <= center + half; j++) {
        const distance = j - this.position;
        const x = 2 * this.cutoff * distance;
        const sinc =
          Math.abs(x) < 1e-9 ? 1 : Math.sin(Math.PI * x) / (Math.PI * x);
        const window = 0.5 + 0.5 * Math.cos((Math.PI * distance) / half);
        const w = 2 * this.cutoff * sinc * window;
        sum += this.input[j] * w;
        weight += w;
      }
      result.push(weight ? sum / weight : 0);
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
