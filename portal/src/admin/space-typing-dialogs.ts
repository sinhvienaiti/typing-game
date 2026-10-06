import "./space-typing-dialogs.css";

type DialogTone = "info" | "warn" | "bad" | "good";

function el<K extends keyof HTMLElementTagNameMap>(tag: K, cls?: string, text?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (cls) node.className = cls;
  if (text !== undefined) node.textContent = text;
  return node;
}

function field(label: string, value = "", type: string = "text"): HTMLLabelElement {
  const root = el("label", "stx-dialog-field");
  root.append(el("span", undefined, label));
  const input = el("input") as HTMLInputElement;
  input.type = type;
  input.value = value;
  input.name = label.toLowerCase().replace(/[^a-z0-9]+/g, "-");
  root.append(input);
  return root;
}

function selectField(label: string, value: string, options: readonly string[]): HTMLLabelElement {
  const root = el("label", "stx-dialog-field");
  root.append(el("span", undefined, label));
  const select = el("select") as HTMLSelectElement;
  select.name = label.toLowerCase().replace(/[^a-z0-9]+/g, "-");
  for (const option of options) select.append(new Option(option, option));
  select.value = value;
  root.append(select);
  return root;
}

function notice(text: string, tone: DialogTone = "info"): HTMLElement {
  return el("div", `stx-dialog-notice ${tone}`, text);
}

function closeDialog(dialog: HTMLDialogElement): void {
  dialog.close();
  dialog.remove();
}

function createDialog(eyebrow: string, title: string, description: string): { dialog: HTMLDialogElement; body: HTMLElement; footer: HTMLElement } {
  const dialog = el("dialog", "stx-admin-dialog") as HTMLDialogElement;
  dialog.setAttribute("aria-labelledby", `stx-dialog-title-${Date.now()}`);
  const frame = el("div", "stx-admin-dialog-frame");
  const head = el("header", "stx-admin-dialog-head");
  head.append(el("div", "st-admin-eyebrow", eyebrow));
  const titleNode = el("h2", undefined, title);
  titleNode.id = dialog.getAttribute("aria-labelledby") ?? "";
  head.append(titleNode, el("p", undefined, description));
  const close = el("button", "stx-dialog-close", "×") as HTMLButtonElement;
  close.type = "button";
  close.setAttribute("aria-label", "Close dialog");
  close.addEventListener("click", () => closeDialog(dialog));
  head.append(close);
  const body = el("div", "stx-admin-dialog-body");
  const footer = el("footer", "stx-admin-dialog-footer");
  frame.append(head, body, footer);
  dialog.append(frame);
  dialog.addEventListener("cancel", (event) => { event.preventDefault(); closeDialog(dialog); });
  dialog.addEventListener("click", (event) => { if (event.target === dialog) closeDialog(dialog); });
  document.body.append(dialog);
  return { dialog, body, footer };
}

export function openMusicUploadMockDialog(): void {
  const { dialog, body, footer } = createDialog(
    "Music Library · UI Workflow",
    "Upload Music Assets",
    "Review the complete upload workflow before backend mapping. Files stay local to this mock and are not written to the Space Typing authored catalog.",
  );

  const fileDrop = el("label", "stx-upload-drop");
  const fileInput = el("input") as HTMLInputElement;
  fileInput.type = "file";
  fileInput.multiple = true;
  fileInput.accept = "audio/mpeg,audio/ogg,audio/wav,audio/mp4,.mp3,.ogg,.wav,.m4a";
  const dropTitle = el("strong", undefined, "Drop multiple audio files here");
  const dropMeta = el("small", undefined, "MP3 · OGG · WAV · M4A · mock validation only");
  fileDrop.append(fileInput, el("span", "stx-upload-icon", "↑"), dropTitle, dropMeta);

  const selected = el("div", "stx-upload-files");
  const renderFiles = (): void => {
    selected.replaceChildren();
    const files = Array.from(fileInput.files ?? []);
    if (files.length === 0) {
      selected.append(el("div", "stx-upload-empty", "No files selected yet."));
      return;
    }
    for (const [index, file] of files.entries()) {
      const row = el("div", "stx-upload-file");
      const copy = el("span");
      copy.append(el("strong", undefined, file.name), el("small", undefined, `${(file.size / 1024 / 1024).toFixed(2)} MB · ${file.type || "unknown codec"}`));
      row.append(el("span", "st-admin-track-num", String(index + 1)), copy, el("span", "st-admin-status good", "READY TO REVIEW"));
      selected.append(row);
    }
  };
  fileInput.addEventListener("change", renderFiles);
  renderFiles();

  const metadata = el("section", "stx-dialog-section");
  metadata.append(el("h3", undefined, "Authored Metadata"));
  const fields = el("div", "stx-dialog-grid");
  fields.append(
    field("Track ID", "world-01-new-track"),
    field("Title", "New Space Theme"),
    selectField("World", "World 01", Array.from({ length: 50 }, (_, index) => `World ${String(index + 1).padStart(2, "0")}`)),
    selectField("Role", "Normal", ["Normal", "Boss Common", "Mini Boss", "World Boss", "Major Boss", "Ambient", "Victory", "Duel"]),
    field("Duration Seconds", "180", "number"),
    field("Mix-out Seconds", "176", "number"),
    field("BPM", "128", "number"),
    selectField("Mood", "Climactic", ["Hopeful", "Lonely", "Melancholic", "Climactic", "Aggressive", "Triumphant", "Atmospheric"]),
  );
  metadata.append(fields);

  const tags = field("Tags", "space, world-01, combat");
  metadata.append(tags);

  const validation = el("section", "stx-dialog-section");
  validation.append(el("h3", undefined, "Validation Preview"));
  const checks = el("div", "stx-dialog-checks");
  for (const [label, value, tone] of [
    ["Codec / extension", "Supported", "good"],
    ["Track ID", "Unique in mock catalog", "good"],
    ["World target", "Valid World identity", "good"],
    ["Duration / mix-out", "mix-out < duration", "good"],
    ["Runtime assignment", "Not assigned until World Music editor", "warn"],
  ] as const) {
    const row = el("div", "stx-dialog-check");
    row.append(el("span", undefined, label), el("strong", tone, value));
    checks.append(row);
  }
  validation.append(checks, notice("Upload preview does not create files in this UI-only phase. Backend implementation will later write authored track.json + audio and rebuild the deterministic catalog.", "warn"));

  body.append(fileDrop, selected, metadata, validation);
  const cancel = el("button", "st-admin-btn", "Cancel") as HTMLButtonElement;
  cancel.type = "button";
  cancel.addEventListener("click", () => closeDialog(dialog));
  const add = el("button", "st-admin-btn primary", "Add to Mock Library") as HTMLButtonElement;
  add.type = "button";
  add.addEventListener("click", () => {
    body.append(notice("Mock upload accepted for UI review. No file or catalog was changed.", "good"));
    add.disabled = true;
    add.textContent = "Added · UI Mock";
  });
  footer.append(cancel, add);
  dialog.showModal();
}

export function openPublishReviewDialog(revision = "r128"): void {
  const { dialog, body, footer } = createDialog(
    "History · Publish Gate",
    `Publish ${revision}`,
    "Preview the operational impact before a revision can become active. This is a UI-only confirmation flow.",
  );
  body.append(
    notice("This mock does not update the active runtime revision.", "info"),
  );
  const summary = el("div", "stx-dialog-summary");
  for (const [label, value, tone] of [
    ["Validation", "PASS", "good"],
    ["Changed domains", "Audio · World Music · Ships", "info"],
    ["Added / Modified / Removed", "3 / 8 / 1", "warn"],
    ["Apply boundary", "New sessions / safe runtime boundaries", "good"],
  ] as const) {
    const card = el("div", "stx-dialog-summary-card");
    card.append(el("span", undefined, label), el("strong", tone, value));
    summary.append(card);
  }
  const diff = el("pre", "stx-dialog-diff");
  diff.textContent = `World 05 / Stage 091 / Normal Music\n- stellar-dawn\n+ silent-orbit\n+ deep-nebula\n\nAudio Defaults / Music\n- 0.35\n+ 0.26\n\nVanguard / Shield\n- 120\n+ 135`;
  const message = field("Publish message", "Reviewed UI revision");
  const acknowledge = el("label", "stx-dialog-ack");
  const check = el("input") as HTMLInputElement;
  check.type = "checkbox";
  acknowledge.append(check, el("span", undefined, "I reviewed the validation result and change summary."));
  body.append(summary, diff, message, acknowledge);

  const cancel = el("button", "st-admin-btn", "Cancel") as HTMLButtonElement;
  cancel.type = "button";
  cancel.addEventListener("click", () => closeDialog(dialog));
  const publish = el("button", "st-admin-btn primary", "Publish Revision") as HTMLButtonElement;
  publish.type = "button";
  publish.disabled = true;
  check.addEventListener("change", () => { publish.disabled = !check.checked; });
  publish.addEventListener("click", () => {
    publish.disabled = true;
    publish.textContent = "Published · UI Mock";
    body.append(notice("Publish flow completed in mock state only. Runtime remains unchanged.", "good"));
  });
  footer.append(cancel, publish);
  dialog.showModal();
}

export function openRollbackReviewDialog(revision = "r127"): void {
  const { dialog, body, footer } = createDialog(
    "History · Rollback Gate",
    `Rollback to ${revision}`,
    "Rollback is destructive to the active configuration pointer, so the UX requires a target summary and explicit acknowledgement.",
  );
  body.append(
    notice("Production rollback will use immutable revisions and compare-and-swap. This dialog is UI mock only.", "warn"),
    el("div", "stx-dialog-summary"),
  );
  const summary = body.querySelector<HTMLElement>(".stx-dialog-summary")!;
  for (const [label, value, tone] of [
    ["Target revision", revision, "info"],
    ["Current active", "r127", "good"],
    ["Domains affected", "World Music · Audio", "warn"],
    ["Validation", "PASS", "good"],
  ] as const) {
    const card = el("div", "stx-dialog-summary-card");
    card.append(el("span", undefined, label), el("strong", tone, value));
    summary.append(card);
  }
  const acknowledge = el("label", "stx-dialog-ack");
  const check = el("input") as HTMLInputElement;
  check.type = "checkbox";
  acknowledge.append(check, el("span", undefined, `I understand the active configuration will point to ${revision}.`));
  body.append(acknowledge);
  const cancel = el("button", "st-admin-btn", "Cancel") as HTMLButtonElement;
  cancel.type = "button";
  cancel.addEventListener("click", () => closeDialog(dialog));
  const rollback = el("button", "st-admin-btn danger", "Rollback") as HTMLButtonElement;
  rollback.type = "button";
  rollback.disabled = true;
  check.addEventListener("change", () => { rollback.disabled = !check.checked; });
  rollback.addEventListener("click", () => {
    rollback.disabled = true;
    rollback.textContent = "Rolled Back · UI Mock";
    body.append(notice("Rollback flow completed in mock state only. Runtime remains unchanged.", "good"));
  });
  footer.append(cancel, rollback);
  dialog.showModal();
}
