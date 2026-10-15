import spec from "../../../shared/voice/model-manifest.json";
import { loadVerifiedAsset } from "../../../shared/voice/verified-asset.mjs";
type ModelManifest = {
  schemaVersion: number;
  engineId: string;
  modelId: string;
  sampleRate: number;
  sourceSha256: string;
  sha256: string;
  bytes: number;
  url: string;
  confidenceFloor: number;
};
export async function loadVoiceModel(
  onStatus: (text: string) => void,
  signal?: AbortSignal,
): Promise<{
  manifest: ModelManifest;
  vocabulary: Set<string>;
  url: string;
  release(): void;
}> {
  onStatus("Loading offline English model…");
  signal?.throwIfAborted();
  let manifest: ModelManifest;
  try {
    const response = await fetch("/assets/voice/manifest.json", {
      cache: "no-cache",
      signal,
    });
    if (!response.ok) throw new Error("Manifest unavailable");
    manifest = (await response.json()) as ModelManifest;
  } catch {
    signal?.throwIfAborted();
    // The compiled pin can reopen a previously verified offline cache.
    manifest = {
      ...spec,
      sha256: spec.artifactSha256,
      bytes: spec.artifactBytes,
      url: `/assets/voice/${spec.modelId}.tar.gz`,
    };
  }
  if (
    manifest.schemaVersion !== 1 ||
    manifest.modelId !== spec.modelId ||
    manifest.engineId !== spec.engineId ||
    manifest.sampleRate !== 16000 ||
    manifest.sha256 !== spec.artifactSha256 ||
    manifest.bytes !== spec.artifactBytes ||
    !Number.isSafeInteger(manifest.bytes) ||
    manifest.bytes < 1000000 ||
    manifest.bytes > 80000000 ||
    manifest.url !== `/assets/voice/${manifest.modelId}.tar.gz`
  )
    throw new Error("Invalid offline model manifest.");
  const cacheName = `typing-voice-model-${manifest.modelId}-${manifest.sha256}`;
  let cache: Cache | null = null;
  try {
    if (typeof caches !== "undefined") cache = await caches.open(cacheName);
  } catch {
    /* Cache storage is optional; verified local assets still work. */
  }
  const bytes = await loadVerifiedAsset({
    url: manifest.url, bytes: manifest.bytes, sha256: manifest.sha256,
    cache, signal, label: "Offline model",
    onRetry: () => onStatus("Repairing cached offline model…"),
  });
  const vocabularyUrl = "/assets/voice/vocabulary.json";
  const vocabularyBytes = await loadVerifiedAsset({
    url: vocabularyUrl, bytes: spec.vocabularyBytes, sha256: spec.vocabularySha256,
    cache, signal, label: "Offline vocabulary",
    onRetry: () => onStatus("Repairing cached offline vocabulary…"),
  });
  const vocabulary = new Set<string>(
    JSON.parse(new TextDecoder().decode(vocabularyBytes)) as string[],
  );
  try {
    if (cache)
      for (const name of await caches.keys())
        if (name.startsWith("typing-voice-model-") && name !== cacheName)
          await caches.delete(name);
  } catch {
    /* Keep the current verified model usable without persistent caching. */
  }
  signal?.throwIfAborted();
  const url = URL.createObjectURL(
    new Blob([bytes], { type: "application/gzip" }),
  );
  onStatus("Preparing speech recognizer…");
  return { manifest, vocabulary, url, release: () => URL.revokeObjectURL(url) };
}
