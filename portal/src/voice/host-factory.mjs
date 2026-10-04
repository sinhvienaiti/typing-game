import { VoiceHost } from "../../../shared/voice/host.mjs";

export function createBrowserVoiceHost(
  onEvent,
  loadRuntime = () => import("./runtime"),
) {
  let releaseOwner = null;
  let permissionEpoch = 0;
  let preparation = null;
  return new VoiceHost({
    createSessionId: () => crypto.randomUUID(),
    cancelMicrophone: () => {
      permissionEpoch++;
      preparation?.abort();
      preparation = null;
      releaseOwner?.();
      releaseOwner = null;
    },
    onEvent,
    requestMicrophone: async () => {
      const epoch = permissionEpoch;
      if (!window.isSecureContext || !navigator.mediaDevices?.getUserMedia)
        throw new Error(
          "Voice needs HTTPS or localhost with microphone access.",
        );
      if (navigator.locks) {
        await new Promise((resolve, reject) => {
          void navigator.locks
            .request(
              "typing-game-microphone",
              { ifAvailable: true },
              async (lock) => {
                if (epoch !== permissionEpoch) {
                  reject(new Error("Microphone request cancelled"));
                  return;
                }
                if (!lock) {
                  reject(
                    new Error(
                      "Microphone is active in another Typing Games tab.",
                    ),
                  );
                  return;
                }
                await new Promise((release) => {
                  releaseOwner = release;
                  resolve();
                });
              },
            )
            .catch(reject);
        });
      }
      const release = releaseOwner;
      if (epoch !== permissionEpoch) {
        release?.();
        throw new Error("Microphone request cancelled");
      }
      try {
        const stream = await navigator.mediaDevices.getUserMedia({
          audio: {
            channelCount: 1,
            echoCancellation: true,
            noiseSuppression: true,
            autoGainControl: true,
          },
          video: false,
        });
        for (const track of stream.getTracks()) {
          const stop = track.stop.bind(track);
          track.stop = () => {
            stop();
            release?.();
            if (releaseOwner === release) releaseOwner = null;
          };
        }
        return stream;
      } catch (error) {
        release?.();
        if (releaseOwner === release) releaseOwner = null;
        throw error;
      }
    },
    createRuntime: async (stream, callbacks) => {
      const release = releaseOwner;
      const epoch = permissionEpoch;
      const controller = (preparation = new AbortController());
      let runtime;
      try {
        const { BrowserVoiceRuntime } = await loadRuntime();
        if (epoch !== permissionEpoch)
          throw new Error("Microphone preparation cancelled");
        runtime = await BrowserVoiceRuntime.create(
          stream,
          {
            ...callbacks,
            onError: (message) =>
              onEvent({
                type: "error",
                code: "microphone-runtime-failed",
                message,
              }),
            onStatus: () => {},
          },
          controller.signal,
        );
      } finally {
        if (preparation === controller) preparation = null;
      }
      const close = runtime.close.bind(runtime);
      runtime.close = async () => {
        try {
          await close();
        } finally {
          release?.();
          if (releaseOwner === release) releaseOwner = null;
        }
      };
      return runtime;
    },
  });
}
