import { SpaceTypingAdminApi } from "./api";
import { renderAdminFailureState, setAdminStatus } from "./space-typing-admin-state";

const api = new SpaceTypingAdminApi();
type Tone = "good" | "warn" | "bad" | "info";
type BackgroundBudget = {
  dprCap: number;
  pixelBudget: number;
  plateSize: number;
  sheetSize: number;
  heroSize: number;
  atlasSize: number;
  flowSheets: number;
  frameInterval: number;
};
type BackgroundsContractPayload = {
  contractRevision: string;
  schemaVersion: number;
  capability: "backgrounds.read";
  route: { id: string; path: string; label: string };
  backgrounds: {
    mode: "runtime-derived-readonly";
    runtimeSources: string[];
    compositionCount: number;
    galaxyKitCount: number;
    qualityTiers: string[];
    presentationModes: string[];
    qualityBudgets: Record<string, BackgroundBudget>;
    compositionDomains: string[];
    assetManifest: { root: string; file: string; strictParser: string; contentAddressedVariants: boolean };
    preview: { available: boolean; owner: string; path: string; queryParameters: string[]; renderer: string; productionRenderer: boolean };
    runtimeFunctions: string[];
    persistenceOwner: string;
    authorableFields: string[];
    writeCapability: false;
    adminPreviewWriteCapability: false;
    applyBoundary: "none";
    unsupportedAdminMockFields: string[];
  };
};

function el<K extends keyof HTMLElementTagNameMap>(tag: K, cls?: string, text?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (cls) node.className = cls;
  if (text !== undefined) node.textContent = text;
  return node;
}
function badge(label: string, tone: Tone = "info"): HTMLElement { return el("span", `st-admin-status ${tone}`, label); }
function notice(text: string, tone: Tone = "info"): HTMLElement { return el("div", `stx-notice ${tone}`, text); }
function panel(title: string, subtitle?: string): HTMLElement {
  const root = el("section", "st-admin-panel solid stx-panel");
  const head = el("div", "st-admin-panel-head");
  const copy = el("div");
  copy.append(el("h2", undefined, title));
  if (subtitle) copy.append(el("p", undefined, subtitle));
  head.append(copy);
  root.append(head);
  return root;
}
function button(label: string, onClick: () => void): HTMLButtonElement {
  const node = el("button", "st-admin-btn", label);
  node.type = "button";
  node.addEventListener("click", onClick);
  return node;
}
function listNotice(label: string, values: readonly string[], tone: Tone = "info"): HTMLElement {
  return notice(`${label}: ${values.join(" · ") || "none exposed"}`, tone);
}
function isRecord(value: unknown): value is Record<string, unknown> {
  return value !== null && typeof value === "object" && !Array.isArray(value);
}
function validateBackgroundsContract(value: unknown): BackgroundsContractPayload {
  if (!isRecord(value) || value["capability"] !== "backgrounds.read" || !isRecord(value["route"]) || !isRecord(value["backgrounds"])) {
    throw new Error("Backgrounds response does not match the canonical backgrounds.read contract.");
  }
  const backgrounds = value["backgrounds"];
  if (
    backgrounds["mode"] !== "runtime-derived-readonly" ||
    !Array.isArray(backgrounds["runtimeSources"]) ||
    !Array.isArray(backgrounds["qualityTiers"]) ||
    !Array.isArray(backgrounds["presentationModes"]) ||
    !Array.isArray(backgrounds["compositionDomains"]) ||
    !Array.isArray(backgrounds["runtimeFunctions"]) ||
    !Array.isArray(backgrounds["unsupportedAdminMockFields"]) ||
    !isRecord(backgrounds["qualityBudgets"]) ||
    !isRecord(backgrounds["assetManifest"]) ||
    !isRecord(backgrounds["preview"]) ||
    typeof backgrounds["compositionCount"] !== "number" ||
    typeof backgrounds["galaxyKitCount"] !== "number"
  ) {
    throw new Error("Backgrounds response is missing required runtime ownership data.");
  }
  const preview = backgrounds["preview"];
  if (typeof preview["path"] !== "string" || typeof preview["available"] !== "boolean" || !Array.isArray(preview["queryParameters"])) {
    throw new Error("Backgrounds response is missing the production gallery preview contract.");
  }
  return value as unknown as BackgroundsContractPayload;
}
async function fetchBackgroundsContract(): Promise<BackgroundsContractPayload> {
  return validateBackgroundsContract(await api.requestJson<unknown>("/api/admin/space-typing/backgrounds/contract"));
}

export function renderPhaseBBackgrounds(): HTMLElement {
  const page = el("div");
  const head = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(
    el("div", "st-admin-eyebrow", "Visuals · Production Background Runtime"),
    el("h1", undefined, "Backgrounds"),
    el("p", undefined, "Inspect canonical world compositions, Galaxy kits, quality budgets and the production renderer without creating a second background policy."),
  );
  const actions = el("div", "st-admin-page-actions");
  actions.append(badge("RUNTIME-BACKED · READ ONLY", "good"), badge("PRODUCTION GALLERY", "info"));
  head.append(copy, actions);
  page.append(head);

  const status = notice("Loading canonical Backgrounds runtime contract…");
  status.setAttribute("aria-live", "polite");
  const content = el("div");
  page.append(status, content);

  let loadGeneration = 0;
  const load = (): void => {
    const generation = ++loadGeneration;
    setAdminStatus(status, "Loading canonical Backgrounds runtime contract…", "loading");
    content.replaceChildren(notice("Loading production background ownership and gallery…", "info"));

    void fetchBackgroundsContract().then((payload) => {
      if (generation !== loadGeneration) return;
      const backgrounds = payload.backgrounds;
      setAdminStatus(status, `${backgrounds.compositionCount} World compositions · ${backgrounds.galaxyKitCount} Galaxy kits · Admin writes closed.`, "success");

      const catalog = panel("Runtime Catalog", "Production BGV composition ownership");
      catalog.append(
        notice(`World compositions: ${backgrounds.compositionCount}`, "good"),
        notice(`Galaxy kits: ${backgrounds.galaxyKitCount}`, "good"),
        listNotice("Composition domains", backgrounds.compositionDomains),
        listNotice("Presentation modes", backgrounds.presentationModes),
        listNotice("Runtime functions", backgrounds.runtimeFunctions),
      );

      const quality = panel("Quality Budgets", "Canonical Low / Medium / High / Ultra GPU budgets");
      for (const tier of backgrounds.qualityTiers) {
        const budget = backgrounds.qualityBudgets[tier];
        if (!budget) {
          quality.append(notice(`${tier.toUpperCase()}: budget unavailable in canonical contract`, "warn"));
          continue;
        }
        quality.append(notice(`${tier.toUpperCase()}: DPR ≤ ${budget.dprCap} · ${budget.pixelBudget.toLocaleString()} px · plate ${budget.plateSize} · sheet ${budget.sheetSize} · hero ${budget.heroSize} · atlas ${budget.atlasSize} · flow ${budget.flowSheets} · frame interval ${budget.frameInterval}`));
      }

      const assets = panel("Kit Manifests", "Generated art manifests validated before runtime use");
      assets.append(
        notice(`Root: ${backgrounds.assetManifest.root}`),
        notice(`Manifest: ${backgrounds.assetManifest.file}`),
        notice(`Strict parser: ${backgrounds.assetManifest.strictParser}`, "good"),
        notice(`Content-addressed variants: ${String(backgrounds.assetManifest.contentAddressedVariants)}`, "good"),
      );

      const preview = panel("Production Renderer Preview", "The embedded gallery uses the same production BackgroundStage renderer as gameplay");
      if (backgrounds.preview.available) {
        const galleryUrl = `${backgrounds.preview.path}?q=high&grid=1&labels=1`;
        const frame = document.createElement("iframe");
        frame.title = "Space Typing production background gallery";
        frame.src = galleryUrl;
        frame.loading = "lazy";
        frame.style.width = "100%";
        frame.style.minHeight = "520px";
        frame.style.border = "0";
        frame.style.borderRadius = "12px";
        const previewActions = el("div", "st-admin-page-actions");
        previewActions.append(
          button("Open World 01 · High", () => window.open(`${backgrounds.preview.path}?world=world-01&q=high&labels=1`, "_blank", "noopener")),
          button("Open Gallery in New Tab", () => window.open(galleryUrl, "_blank", "noopener")),
        );
        preview.append(
          notice(`Owner: ${backgrounds.preview.owner}`),
          notice(`Renderer: ${backgrounds.preview.renderer} · production=${String(backgrounds.preview.productionRenderer)}`, "good"),
          listNotice("Query parameters", backgrounds.preview.queryParameters),
          previewActions,
          frame,
        );
      } else {
        preview.append(notice("Production gallery preview is intentionally unavailable in this runtime contract.", "warn"));
      }

      const boundary = panel("Admin Boundary", "Source/art pipeline ownership remains canonical");
      boundary.append(
        notice(`Persistence owner: ${backgrounds.persistenceOwner}`),
        notice(`Admin write capability: ${String(backgrounds.writeCapability)}`, "warn"),
        notice(`Admin preview write capability: ${String(backgrounds.adminPreviewWriteCapability)}`, "warn"),
        listNotice("Unsupported legacy mock controls", backgrounds.unsupportedAdminMockFields, "warn"),
        listNotice("Runtime sources", backgrounds.runtimeSources),
        notice("Brightness, parallax, motion and per-quality inline sliders are not standalone Admin fields. Their real values live inside typed WorldComposition structures and runtime quality budgets."),
      );

      content.replaceChildren(catalog, quality, assets, preview, boundary);
    }).catch((error: unknown) => {
      if (generation !== loadGeneration) return;
      setAdminStatus(status, "Backgrounds service unavailable.", "error");
      renderAdminFailureState(content, {
        title: "Backgrounds unavailable",
        fallbackMessage: "Unable to load the canonical Backgrounds runtime contract.",
        error,
        onRetry: load,
      });
    });
  };

  load();
  return page;
}
