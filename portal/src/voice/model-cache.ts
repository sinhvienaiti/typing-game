import spec from "../../../shared/voice/model-manifest.json";
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
  let stored = await cache?.match(manifest.url);
  const modelWasCached = !!stored;
  if (!stored)
    stored = await fetch(manifest.url, { cache: "no-store", signal });
  if (!stored.ok)
    throw new Error("Offline model unavailable. Run ./dev.sh space.");
  const bytes = await stored.arrayBuffer();
  signal?.throwIfAborted();
  const hash = [...new Uint8Array(await crypto.subtle.digest("SHA-256", bytes))]
    .map((x) => x.toString(16).padStart(2, "0"))
    .join("");
  if (bytes.byteLength !== manifest.bytes || hash !== manifest.sha256) {
    await cache?.delete(manifest.url);
    throw new Error("Offline model checksum failed. Prepare it again.");
  }
  // A partially downloaded or unverified model never becomes a ready cache entry.
  try {
    if (!modelWasCached) {
      await cache?.put(
        manifest.url,
        new Response(bytes, {
          headers: { "Content-Type": "application/gzip" },
        }),
      );
    }
  } catch {
    /* Quota failure must not invalidate a verified in-memory model. */
  }
  const vocabularyUrl = "/assets/voice/vocabulary.json";
  const cachedVocabulary = await cache?.match(vocabularyUrl);
  const vocabularyResponse =
    cachedVocabulary ??
    (await fetch(vocabularyUrl, { cache: "no-store", signal }));
  if (!vocabularyResponse.ok)
    throw new Error("Offline model vocabulary missing. Run ./dev.sh space.");
  const vocabularyBytes = await vocabularyResponse.arrayBuffer();
  signal?.throwIfAborted();
  const vocabularyHash = [
    ...new Uint8Array(await crypto.subtle.digest("SHA-256", vocabularyBytes)),
  ]
    .map((x) => x.toString(16).padStart(2, "0"))
    .join("");
  if (
    vocabularyBytes.byteLength !== spec.vocabularyBytes ||
    vocabularyHash !== spec.vocabularySha256
  ) {
    await cache?.delete(vocabularyUrl);
    throw new Error("Offline vocabulary checksum failed.");
  }
  const vocabulary = new Set<string>(
    JSON.parse(new TextDecoder().decode(vocabularyBytes)) as string[],
  );
  try {
    if (!cachedVocabulary)
      await cache?.put(vocabularyUrl, new Response(vocabularyBytes));
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
