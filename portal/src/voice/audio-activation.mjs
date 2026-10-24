/** A suspended browser context must never make Voice preparation wait forever. */
export async function resumeVoiceAudio(audio, signal) {
  signal?.throwIfAborted();
  await new Promise((resolve, reject) => {
    let settled = false;
    const finish = (callback, value) => {
      if (settled) return;
      settled = true;
      clearTimeout(timer);
      signal?.removeEventListener("abort", abort);
      callback(value);
    };
    const abort = () => finish(reject, signal.reason);
    const timer = setTimeout(
      () =>
        finish(
          reject,
          new Error(
            "Browser audio capture did not start. Enable sound for this website and reconnect the microphone.",
          ),
        ),
      10000,
    );
    signal?.addEventListener("abort", abort, { once: true });
    try {
      audio.resume().then(
        () =>
          audio.state === "running"
            ? finish(resolve)
            : finish(
                reject,
                new Error(
                  "Browser audio capture is suspended. Enable sound for this website and reconnect the microphone.",
                ),
              ),
        (error) => finish(reject, error),
      );
    } catch (error) {
      finish(reject, error);
    }
  });
}
