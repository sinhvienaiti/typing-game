export function loadVerifiedAsset(options: {
  url: string;
  bytes: number;
  sha256: string;
  cache?: Cache | null;
  signal?: AbortSignal;
  onRetry?: () => void;
  label: string;
}): Promise<ArrayBuffer>;
