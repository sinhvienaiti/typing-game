import type { ParentVoiceBridge as ParentVoiceBridgeType } from "../../shared/voice/bridge.mjs";

type SpaceVoiceFrame = HTMLIFrameElement;
type SpaceVoiceGame = { id: "space-typing"; appUrl: string };

let bridge: ParentVoiceBridgeType | null = null;
let bridgeLoading: Promise<ParentVoiceBridgeType> | null = null;
let boundFrame: SpaceVoiceFrame | null = null;

function isVoiceMessage(value: unknown): value is Record<string, unknown> {
  return (
    value !== null &&
    typeof value === "object" &&
    "type" in value &&
    typeof (value as Record<string, unknown>).type === "string" &&
    ((value as Record<string, unknown>).type as string).startsWith("typing-game:voice:")
  );
}

function findSpaceTypingFrame(event: MessageEvent<unknown>): SpaceVoiceFrame | null {
  for (const frame of document.querySelectorAll<HTMLIFrameElement>("iframe.game-frame")) {
    if (frame.contentWindow !== event.source) continue;
    if (frame.title !== "Space Typing") return null;
    let origin: string;
    try {
      origin = new URL(frame.src, window.location.href).origin;
    } catch {
      return null;
    }
    if (event.origin !== origin) return null;
    return frame;
  }
  return null;
}

async function loadBridge(): Promise<ParentVoiceBridgeType> {
  if (bridge) return bridge;
  const loading = (bridgeLoading ??= Promise.all([
    import("../../shared/voice/bridge.mjs"),
    import("./voice/host-factory.mjs"),
  ]).then(([{ ParentVoiceBridge }, { createBrowserVoiceHost }]) =>
    new ParentVoiceBridge({ createHost: createBrowserVoiceHost }),
  ));
  try {
    bridge = await loading;
    return bridge;
  } catch (error) {
    if (bridgeLoading === loading) bridgeLoading = null;
    throw error;
  }
}

function postLoadFailure(frame: SpaceVoiceFrame, event: MessageEvent<unknown>): void {
  const request = event.data as Record<string, unknown>;
  if (
    request.version !== 1 ||
    request.type !== "typing-game:voice:v1:hello" ||
    typeof request.gameInstanceId !== "string" ||
    !request.gameInstanceId.trim() ||
    request.gameInstanceId.length > 160
  ) {
    return;
  }
  frame.contentWindow?.postMessage(
    {
      version: 1,
      type: "typing-game:voice:v1:error",
      gameId: "space-typing",
      gameInstanceId: request.gameInstanceId,
      code: "voice-service-load-failed",
      message: "Voice service could not load. Restart the Portal and reload this tab.",
    },
    event.origin,
  );
}

window.addEventListener("message", (event: MessageEvent<unknown>) => {
  if (!isVoiceMessage(event.data)) return;
  const frame = findSpaceTypingFrame(event);
  if (!frame) return;

  if (boundFrame && boundFrame !== frame) bridge?.reset();
  boundFrame = frame;
  const game: SpaceVoiceGame = { id: "space-typing", appUrl: frame.src };

  void loadBridge()
    .then((service) => service.handleMessage(event, frame, game))
    .catch((error) => {
      console.warn("Portal Voice service could not load", error);
      postLoadFailure(frame, event);
    });
});

const observer = new MutationObserver(() => {
  if (!boundFrame || boundFrame.isConnected) return;
  bridge?.reset();
  boundFrame = null;
});
observer.observe(document.documentElement, { childList: true, subtree: true });
