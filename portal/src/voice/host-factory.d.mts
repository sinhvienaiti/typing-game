import type { VoiceHost } from "../../../shared/voice/host.mjs";
export function createBrowserVoiceHost(
  onEvent: (event: Record<string, unknown>) => void,
): VoiceHost;
