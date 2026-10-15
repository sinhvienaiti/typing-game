import "./admin-runtime-preview-fixes.css";
import { openAdminMediaAssetPicker, type MediaAssetSelection } from "./asset-picker";
import { MediaAdminApi, type MediaPreviewHandle } from "./media-api";

export type ImageMediaCandidateTester = Readonly<{
  root: HTMLElement;
  selectedAssetVersionId: () => string | null;
  dispose: () => void;
}>;

type ImageMediaCandidateTesterOptions = Readonly<{
  title: string;
  description: string;
}>;

function el<K extends keyof HTMLElementTagNameMap>(tag: K, cls?: string, text?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (cls) node.className = cls;
  if (text !== undefined) node.textContent = text;
  return node;
}

export function createImageMediaCandidateTester(options: ImageMediaCandidateTesterOptions): ImageMediaCandidateTester {
  const api = new MediaAdminApi();
  const root = el("section", "st-admin-media-candidate-test");
  const head = el("div", "st-admin-media-candidate-head");
  const copy = el("div");
  copy.append(el("strong", undefined, options.title), el("small", undefined, options.description));
  const actions = el("div", "st-admin-media-candidate-actions");
  const choose = el("button", "st-admin-btn", "Choose candidate image") as HTMLButtonElement;
  choose.type = "button";
  const clear = el("button", "st-admin-btn", "Clear candidate") as HTMLButtonElement;
  clear.type = "button";
  clear.disabled = true;
  actions.append(choose, clear);
  head.append(copy, actions);

  const visual = el("div", "st-admin-media-candidate-visual");
  visual.tabIndex = -1;
  visual.setAttribute("aria-label", "Candidate replacement image preview");
  const empty = (): HTMLElement => el("span", undefined, "No candidate image selected. Current production art remains visible beside this panel for comparison.");
  visual.append(empty());
  const status = el("div", "st-admin-asset-preview-status info", "CANDIDATE · preview-only Media V2 image · nothing is persisted or published.");
  status.setAttribute("aria-live", "polite");
  root.append(head, visual, status);

  let selected: MediaAssetSelection | null = null;
  let previewHandle: MediaPreviewHandle | null = null;
  let generation = 0;
  let disposed = false;

  const release = (): void => {
    previewHandle?.revoke();
    previewHandle = null;
  };

  const revealVisual = (): void => {
    visual.focus({ preventScroll: true });
    visual.scrollIntoView({ block: "nearest", behavior: "smooth" });
  };

  const renderSelection = async (selection: MediaAssetSelection): Promise<void> => {
    const current = ++generation;
    release();
    const component = selection.version.components.find((entry) => entry.role === "primary" && entry.mimeType.startsWith("image/"))
      ?? selection.version.components.find((entry) => entry.mimeType.startsWith("image/"));
    if (!component) {
      visual.replaceChildren(el("span", undefined, "The selected version has no image component."));
      status.className = "st-admin-asset-preview-status bad";
      status.textContent = "Selected Media V2 version is not an image candidate.";
      revealVisual();
      return;
    }
    status.className = "st-admin-asset-preview-status info";
    status.textContent = "Loading exact immutable candidate image for comparison…";
    try {
      const handle = await api.previewHandle(selection.version.assetVersionId, component);
      if (disposed || current !== generation) {
        handle?.revoke();
        return;
      }
      if (handle === null) {
        visual.replaceChildren(el("span", undefined, "This image is source/runtime referenced and has no direct Admin preview URL."));
        status.className = "st-admin-asset-preview-status warn";
        status.textContent = `CANDIDATE · ${selection.asset.title} · ${selection.version.assetVersionId} · preview handle unavailable.`;
        revealVisual();
        return;
      }
      previewHandle = handle;
      const image = el("img") as HTMLImageElement;
      image.alt = `${selection.asset.title} candidate replacement preview`;
      image.src = handle.url;
      visual.replaceChildren(image);
      status.className = "st-admin-asset-preview-status good";
      status.textContent = `CANDIDATE · ${selection.asset.title} · exact version ${selection.version.assetVersionId} · preview-only comparison.`;
      revealVisual();
    } catch (error) {
      if (disposed || current !== generation) return;
      visual.replaceChildren(el("span", undefined, error instanceof Error ? error.message : String(error)));
      status.className = "st-admin-asset-preview-status bad";
      status.textContent = "Could not preview the selected candidate image.";
      revealVisual();
    }
  };

  choose.addEventListener("click", () => {
    if (disposed) return;
    openAdminMediaAssetPicker({
      title: "Choose candidate image",
      message: "Select an exact immutable image version. It will render beside current production art for direct visual comparison and will not be persisted by this preview-only tester.",
      allowedKinds: ["image"],
      selectedAssetVersionId: selected?.version.assetVersionId ?? null,
      returnFocus: choose,
      onSelect: async (selection) => {
        selected = selection;
        clear.disabled = false;
        await renderSelection(selection);
      },
    });
  });

  clear.addEventListener("click", () => {
    if (disposed) return;
    generation += 1;
    selected = null;
    release();
    clear.disabled = true;
    visual.replaceChildren(empty());
    status.className = "st-admin-asset-preview-status info";
    status.textContent = "Candidate cleared. Current production art remains unchanged.";
  });

  return Object.freeze({
    root,
    selectedAssetVersionId: () => selected?.version.assetVersionId ?? null,
    dispose: () => {
      if (disposed) return;
      disposed = true;
      generation += 1;
      release();
    },
  });
}
