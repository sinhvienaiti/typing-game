import { StreamingResampler } from "../../../shared/voice/audio-resampler.mjs";
import { CAPTURE_BLOCK_SAMPLES, CAPTURE_MAX_PENDING } from "./capture-policy";
declare const sampleRate: number;
declare class AudioWorkletProcessor {
  port: MessagePort;
}
declare function registerProcessor(
  name: string,
  processor: typeof AudioWorkletProcessor,
): void;

class VoiceCapture extends AudioWorkletProcessor {
  private resampler = new StreamingResampler(sampleRate);
  private clock = 0;
  private enabled = false;
  private generation = 0;
  private credits = CAPTURE_MAX_PENDING;
  private buffer = new Float32Array(CAPTURE_BLOCK_SAMPLES);
  private used = 0;
  constructor() {
    super();
    this.port.onmessage = ({ data }) => {
      if (data.type === "gate") {
        this.enabled = data.enabled;
        this.generation = data.generation;
        this.used = 0;
        this.credits = CAPTURE_MAX_PENDING;
      }
      if (data.type === "credit" && data.generation === this.generation)
        this.credits = Math.min(CAPTURE_MAX_PENDING, this.credits + 1);
    };
  }
  process(inputs: Float32Array[][]): boolean {
    const channel = inputs[0]?.[0];
    if (!channel) return true;
    const samples = this.resampler.push(channel);
    for (const value of samples) {
      this.clock++;
      if (!this.enabled) {
        if (this.clock % CAPTURE_BLOCK_SAMPLES === 0)
          this.port.postMessage({ type: "clock", sample: this.clock });
        continue;
      }
      this.buffer[this.used++] = value;
      if (this.used !== this.buffer.length) continue;
      if (this.credits === 0) {
        this.enabled = false;
        this.used = 0;
        this.port.postMessage({
          type: "overflow",
          sample: this.clock,
          generation: this.generation,
        });
        continue;
      }
      this.credits--;
      this.port.postMessage(
        {
          type: "pcm",
          sample: this.clock,
          generation: this.generation,
          data: this.buffer,
        },
        [this.buffer.buffer],
      );
      this.buffer = new Float32Array(CAPTURE_BLOCK_SAMPLES);
      this.used = 0;
    }
    return true;
  }
}
registerProcessor("typing-voice-capture", VoiceCapture);
