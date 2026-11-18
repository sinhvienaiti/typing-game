import type { VoiceHost } from "./host.mjs";
export class ParentVoiceBridge {
  constructor(options?: { createHost?: ((onEvent: (event: Record<string, unknown>) => void) => VoiceHost) | null; unavailableReason?: string });
  reset(): void;
  handleMessage(event: MessageEvent<unknown>, frame: HTMLIFrameElement | null, game: { id: string; appUrl: string } | null): boolean;
}
