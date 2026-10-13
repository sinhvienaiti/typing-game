import "./asset-tuning-studio.css";
import { createAdminFieldShell, createAdminStatusChip } from "./admin-components";
import { AdminHelpScope, type AdminInfoIconOptions } from "./admin-help";
import {
  openAdminMediaAssetPicker,
  type AdminMediaAssetPickerOptions,
} from "./asset-picker";

export type AssetTuningCapabilityStatus =
  | "SUPPORTED NOW"
  | "REQUIRES CANONICAL MIGRATION"
  | "READ-ONLY REFERENCE"
  | "DEFERRED / UNSUPPORTED";

export type AssetTuningChoice = Readonly<{
  id: string;
  label: string;
  help?: string;
}>;

export type AssetTuningStudioOptions = Readonly<{
  helpScope: AdminHelpScope;
  title?: string;
  description?: string;
  basicLabel?: string;
  sources: readonly AssetTuningChoice[];
  activeSource: string;
  scenarios: readonly AssetTuningChoice[];
  activeScenario: string;
  onSourceChange: (sourceId: string) => void;
  onScenarioChange: (scenarioId: string) => void;
}>;

export type AssetTuningStudioHandle = Readonly<{
  root: HTMLElement;
  basicHost: HTMLElement;
  advancedHost: HTMLElement;
  previewHost: HTMLElement;
  previewStatus: HTMLElement;
  lifecycleHost: HTMLElement;
  setSource: (sourceId: string) => void;
  setScenario: (scenarioId: string) => void;
}>;

export type AssetTuningScalarOptions = Readonly<{
  label: string;
  value: number;
  defaultValue: number;
  min: number;
  max: number;
  step: number;
  onChange: (value: number) => void;
  help?: Omit<AdminInfoIconOptions, "label">;
  stateMessage?: string;
}>;

export type AssetTuningCapabilityOptions = Readonly<{
  label: string;
  status: AssetTuningCapabilityStatus;
  description: string;
}>;

function element<K extends keyof HTMLElementTagNameMap>(
  tag: K,
  className?: string,
  text?: string,
): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (className !== undefined) node.className = className;
  if (text !== undefined) node.textContent = text;
  return node;
}

function toneForCapability(status: AssetTuningCapabilityStatus): "good" | "warn" | "info" {
  if (status === "SUPPORTED NOW") return "good";
  if (status === "REQUIRES CANONICAL MIGRATION") return "warn";
  return "info";
}

function createChoiceGroup(
  label: string,
  choices: readonly AssetTuningChoice[],
  activeId: string,
  onSelect: (id: string) => void,
  helpScope: AdminHelpScope,
): Readonly<{
  root: HTMLElement;
  setActive: (id: string) => void;
}> {
  const root = element("div", "st-admin-asset-choice-group");
  root.setAttribute("role", "group");
  root.setAttribute("aria-label", label);
  const buttons = new Map<string, HTMLButtonElement>();

  for (const choice of choices) {
    const button = element("button", "st-admin-asset-choice", choice.label);
    button.type = "button";
    button.dataset.choiceId = choice.id;
    button.setAttribute("aria-pressed", choice.id === activeId ? "true" : "false");
    button.classList.toggle("active", choice.id === activeId);
    button.addEventListener("click", () => onSelect(choice.id));
    if (choice.help) {
      helpScope.tooltip(button, {
        title: choice.label,
        content: choice.help,
        interaction: "hover-focus",
      });
    }
    buttons.set(choice.id, button);
    root.append(button);
  }

  return Object.freeze({
    root,
    setActive: (id: string): void => {
      for (const [choiceId, button] of buttons) {
        const active = choiceId === id;
        button.classList.toggle("active", active);
        button.setAttribute("aria-pressed", active ? "true" : "false");
      }
    },
  });
}

/**
 * Shared A5.1 shell. Domain editors inject only controls that their capability
 * matrix marks SUPPORTED NOW. The shell owns layout/disclosure/preview chrome,
 * never domain persistence.
 */
export function createAssetTuningStudio(options: AssetTuningStudioOptions): AssetTuningStudioHandle {
  const root = element("section", "st-admin-asset-studio");
  const settings = element("div", "st-admin-asset-studio-settings");
  const settingsHead = element("div", "st-admin-asset-studio-section-head");
  const settingsCopy = element("div");
  settingsCopy.append(
    element("span", "st-admin-asset-studio-eyebrow", "Asset Tuning Studio"),
    element("h2", undefined, options.title ?? "Appearance"),
  );
  if (options.description) settingsCopy.append(element("p", undefined, options.description));
  settingsHead.append(
    settingsCopy,
    options.helpScope.infoIcon({
      label: "Asset Tuning Studio help",
      title: "Asset Tuning Studio",
      content: "Only production-backed capabilities are editable. Preview scenarios are runtime state and do not become persisted settings.",
    }),
  );

  const basic = element("section", "st-admin-asset-studio-basic");
  basic.append(element("h3", undefined, options.basicLabel ?? "Basic"));
  const basicHost = element("div", "st-admin-asset-studio-fields");
  basic.append(basicHost);

  const advanced = element("details", "st-admin-asset-studio-advanced");
  advanced.append(element("summary", undefined, "Advanced"));
  const advancedHost = element("div", "st-admin-asset-studio-advanced-body");
  advanced.append(advancedHost);
  settings.append(settingsHead, basic, advanced);

  const preview = element("div", "st-admin-asset-studio-preview");
  const previewHead = element("div", "st-admin-asset-studio-preview-head");
  const previewCopy = element("div");
  previewCopy.append(
    element("span", "st-admin-asset-studio-eyebrow", "Live Preview"),
    element("h2", undefined, "Production Renderer"),
  );
  const sourceGroup = createChoiceGroup(
    "Preview source",
    options.sources,
    options.activeSource,
    options.onSourceChange,
    options.helpScope,
  );
  previewHead.append(previewCopy, sourceGroup.root);

  const previewHost = element("div", "st-admin-asset-preview-stage st-admin-asset-studio-stage");
  const previewFooter = element("div", "st-admin-asset-studio-preview-footer");
  const scenarioLabel = element("strong", undefined, "Scenario");
  const scenarioGroup = createChoiceGroup(
    "Preview scenario",
    options.scenarios,
    options.activeScenario,
    options.onScenarioChange,
    options.helpScope,
  );
  const previewStatus = element(
    "div",
    "st-admin-asset-preview-status",
    "Waiting for the production preview harness…",
  );
  previewStatus.setAttribute("aria-live", "polite");
  previewFooter.append(scenarioLabel, scenarioGroup.root, previewStatus);
  preview.append(previewHead, previewHost, previewFooter);

  const lifecycleHost = element("div", "st-admin-asset-studio-lifecycle");
  root.append(settings, preview, lifecycleHost);

  return Object.freeze({
    root,
    basicHost,
    advancedHost,
    previewHost,
    previewStatus,
    lifecycleHost,
    setSource: sourceGroup.setActive,
    setScenario: scenarioGroup.setActive,
  });
}

/**
 * Canonical scalar primitive: slider + numeric input + Reset. Callers must pass
 * the domain/profile default; this helper intentionally has no UI hard-coded
 * reset value.
 */
export function createAssetTuningScalarControl(
  scope: AdminHelpScope,
  options: AssetTuningScalarOptions,
): HTMLElement {
  const control = element("div", "st-admin-asset-scalar-control");
  const slider = element("input", "st-admin-asset-scalar-range") as HTMLInputElement;
  slider.type = "range";
  slider.min = String(options.min);
  slider.max = String(options.max);
  slider.step = String(options.step);
  slider.value = String(options.value);

  const number = element("input", "st-admin-asset-scalar-number") as HTMLInputElement;
  number.type = "number";
  number.min = slider.min;
  number.max = slider.max;
  number.step = slider.step;
  number.value = String(options.value);

  const reset = element("button", "st-admin-btn st-admin-asset-scalar-reset", "Reset");
  reset.type = "button";

  const commit = (next: number): void => {
    if (!Number.isFinite(next)) return;
    const value = Math.min(options.max, Math.max(options.min, next));
    slider.value = String(value);
    number.value = String(value);
    options.onChange(value);
  };

  slider.addEventListener("input", () => commit(Number(slider.value)));
  number.addEventListener("change", () => commit(Number(number.value)));
  reset.addEventListener("click", () => commit(options.defaultValue));
  control.append(slider, number, reset);

  return createAdminFieldShell(scope, {
    label: options.label,
    control,
    help: options.help,
    stateMessage: options.stateMessage,
    stateTone: "info",
  });
}

/**
 * Reuses the existing immutable-version Media V2 picker. A domain should render
 * this button only after its capability metadata says the asset slot is writable.
 */
export function createAssetTuningMediaPickerButton(
  options: AdminMediaAssetPickerOptions & Readonly<{ buttonLabel?: string }>,
): HTMLButtonElement {
  const button = element("button", "st-admin-btn", options.buttonLabel ?? "Choose Media");
  button.type = "button";
  button.addEventListener("click", () => {
    openAdminMediaAssetPicker({
      ...options,
      returnFocus: button,
    });
  });
  return button;
}

export function createAssetTuningCapabilityState(options: AssetTuningCapabilityOptions): HTMLElement {
  const root = element("div", "st-admin-asset-capability");
  const head = element("div", "st-admin-asset-capability-head");
  head.append(
    element("strong", undefined, options.label),
    createAdminStatusChip(options.status, toneForCapability(options.status)),
  );
  root.append(head, element("span", "st-admin-asset-capability-copy", options.description));
  return root;
}
