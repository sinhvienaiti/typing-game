// The runtime offsets this synthetic prefix from live word timestamps.
export const WARMUP_SAMPLES = 16000;
/** Prime the SAME recognizer that will receive live audio. First-window work
 * is per recognizer, so warming a disposable instance is insufficient. */
export async function primeRecognizer(recognizer, signal) {
  signal?.throwIfAborted();
  let timer, abort, finished = false;
  try {
    await new Promise((resolve, reject) => {
      timer = setTimeout(() => reject(new Error("Speech engine warmup timed out.")), 15000);
      abort = () => reject(signal.reason);
      signal?.addEventListener("abort", abort, { once: true });
      recognizer.on("partialresult", resolve);
      recognizer.on("result", resolve);
      recognizer.on("error", message => reject(new Error(message.error ?? "Speech engine warmup failed.")));
      recognizer.ready().then(() => {
        if (finished) return;
        signal?.throwIfAborted();
        recognizer.acceptWaveformFloat(new Float32Array(WARMUP_SAMPLES), 16000);
      }).catch(reject);
    });
    signal?.throwIfAborted();
  } finally {
    finished = true;
    clearTimeout(timer);
    if (abort) signal?.removeEventListener("abort", abort);
  }
}
