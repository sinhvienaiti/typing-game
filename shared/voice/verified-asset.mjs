/** Cache entries are untrusted until verified. A corrupt/stale cache gets one
 * network retry, while a corrupt network response is never cached or accepted. */
export async function loadVerifiedAsset({ url, bytes, sha256, cache, signal, onRetry, label }) {
  const verify = async (response) => {
    if (!response.ok) throw new Error(`${label} unavailable (HTTP ${response.status}). Run pnpm voice:prepare.`);
    const data = await response.arrayBuffer();
    signal?.throwIfAborted();
    const hash = [...new Uint8Array(await crypto.subtle.digest("SHA-256", data))]
      .map((x) => x.toString(16).padStart(2, "0")).join("");
    if (data.byteLength !== bytes || hash !== sha256) {
      const encoding = response.headers.get("Content-Encoding");
      throw new Error(`${label} checksum failed (${data.byteLength}/${bytes} bytes${encoding ? `; HTTP encoding: ${encoding}` : ""}). Check the local asset server and run pnpm voice:prepare.`);
    }
    return data;
  };
  signal?.throwIfAborted();
  let stored;
  try { stored = await cache?.match(url); } catch { /* Cache storage is optional. */ }
  if (stored) {
    try { return await verify(stored); } catch {
      signal?.throwIfAborted();
      try { await cache?.delete(url); } catch { /* Still retry the local server. */ }
      onRetry?.();
    }
  }
  const data = await verify(await fetch(url, { cache: "no-store", signal }));
  signal?.throwIfAborted();
  try { await cache?.put(url, new Response(data)); } catch { /* Quota must not invalidate verified bytes. */ }
  return data;
}
