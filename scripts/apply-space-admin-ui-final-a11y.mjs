import fs from "node:fs";

function replaceRequired(source, before, after, label) {
  if (!source.includes(before)) throw new Error(`Patch target not found: ${label}`);
  return source.replace(before, after);
}

{
  const file = "portal/src/admin/space-typing-extended.ts";
  let source = fs.readFileSync(file, "utf8");

  source = replaceRequired(
    source,
    '  input.value = String(value);\n  input.addEventListener("input", () => { valueLabel.textContent = `${input.value}${suffix}`; });',
    '  input.value = String(value);\n  input.setAttribute("aria-label", label);\n  input.addEventListener("input", () => { valueLabel.textContent = `${input.value}${suffix}`; });',
    "extended range aria-label",
  );

  source = replaceRequired(
    source,
    'const search = el("input", "st-admin-search") as HTMLInputElement; search.placeholder = `Search ${title.toLowerCase()}…`; list.append(search);',
    'const search = el("input", "st-admin-search") as HTMLInputElement; search.placeholder = `Search ${title.toLowerCase()}…`; search.setAttribute("aria-label", `Search ${title}`); list.append(search);',
    "registry search aria-label",
  );

  source = source.replace(
    'const search = el("input", "st-admin-search") as HTMLInputElement; search.placeholder = "Search content ID, word, topic…"; filters.prepend(search); page.append(filters);',
    'const search = el("input", "st-admin-search") as HTMLInputElement; search.placeholder = "Search content ID, word, topic…"; search.setAttribute("aria-label", "Search typing content"); filters.prepend(search); page.append(filters);',
  );

  source = replaceRequired(
    source,
    'detail.append(diff, el("div", "st-admin-page-actions")); const actions = detail.querySelector<HTMLElement>(".st-admin-page-actions")!; actions.append(btn("Clone Draft"), btn("Validate"), btn("Rollback", () => openRollbackReviewDialog(uiState.selectedRevision), "st-admin-btn danger"), btn("Publish", () => openPublishReviewDialog(uiState.selectedRevision), "st-admin-btn primary")); page.append(editorShell(list, detail)); return page;',
    `detail.append(diff, el("div", "st-admin-page-actions"));
  const actions = detail.querySelector<HTMLElement>(".st-admin-page-actions")!;
  const selectedRevision = revisions.find((row) => row[0] === uiState.selectedRevision);
  const selectedStatus = selectedRevision?.[1] ?? "Draft";
  const rollback = btn("Rollback", () => openRollbackReviewDialog(uiState.selectedRevision), "st-admin-btn danger");
  rollback.disabled = selectedStatus === "Draft" || uiState.selectedRevision === "r127";
  rollback.title = rollback.disabled ? "Select an older published revision to preview rollback." : "Review rollback impact";
  const publish = btn("Publish", () => openPublishReviewDialog(uiState.selectedRevision), "st-admin-btn primary");
  publish.disabled = selectedStatus !== "Draft";
  publish.title = publish.disabled ? "Only draft revisions can be published." : "Review and publish draft";
  actions.append(btn("Clone Draft"), btn("Validate"), rollback, publish);
  page.append(editorShell(list, detail)); return page;`,
    "history action state",
  );

  fs.writeFileSync(file, source);
}

{
  const file = "portal/src/admin/space-typing.ts";
  let source = fs.readFileSync(file, "utf8");

  source = replaceRequired(
    source,
    `      const control = button(label, () => {
        for (const child of Array.from(seg.children)) child.classList.remove("active");
        control.classList.add("active");
      }, index === 0 ? "active" : "");
      seg.append(control);`,
    `      const control = button(label, () => {
        for (const child of Array.from(seg.children)) {
          child.classList.remove("active");
          child.setAttribute("aria-pressed", "false");
        }
        control.classList.add("active");
        control.setAttribute("aria-pressed", "true");
      }, index === 0 ? "active" : "");
      control.setAttribute("aria-pressed", String(index === 0));
      seg.append(control);`,
    "overview time filter state",
  );

  source = source.replace(
    'search.placeholder = "Search track ID, title, filename…";',
    'search.placeholder = "Search track ID, title, filename…";\n    search.setAttribute("aria-label", "Search music library");',
  );
  source = source.replace(
    'const type = element("select", "st-admin-select");\n    type.append',
    'const type = element("select", "st-admin-select");\n    type.setAttribute("aria-label", "Filter music by type");\n    type.append',
  );
  source = source.replace(
    'const status = element("select", "st-admin-select");\n    status.append',
    'const status = element("select", "st-admin-select");\n    status.setAttribute("aria-label", "Filter music by status");\n    status.append',
  );

  fs.writeFileSync(file, source);
}

{
  const file = "portal/src/admin/space-typing-world-music-v2.ts";
  let source = fs.readFileSync(file, "utf8");

  source = replaceRequired(
    source,
    'for (const [value, label] of scopes) seg.append(btn(label, () => { state.scope = value; currentNavigate(`${BASE}/world-music`); }, state.scope === value ? "active" : ""));',
    `for (const [value, label] of scopes) {
    const control = btn(label, () => { state.scope = value; currentNavigate(\`${BASE}/world-music\`); }, state.scope === value ? "active" : "");
    control.setAttribute("aria-pressed", String(state.scope === value));
    seg.append(control);
  }`,
    "World Music scope aria state",
  );

  source = replaceRequired(
    source,
    'for (const role of ["Normal", "Boss Common", "Mini Boss", "World Boss", "Major Boss"]) tabs.append(btn(role, () => { state.role = role; currentNavigate(`${BASE}/world-music`); }, state.role === role ? "active" : ""));',
    `for (const role of ["Normal", "Boss Common", "Mini Boss", "World Boss", "Major Boss"]) {
    const control = btn(role, () => { state.role = role; currentNavigate(\`${BASE}/world-music\`); }, state.role === role ? "active" : "");
    control.setAttribute("aria-pressed", String(state.role === role));
    tabs.append(control);
  }`,
    "World Music role aria state",
  );

  source = source.replace(
    'weight.max = "100";\n    row.append',
    'weight.max = "100";\n    weight.setAttribute("aria-label", `${title} playlist weight`);\n    row.append',
  );
  source = source.replace(
    'if (s === 20) stageBtn.title = "Boss stage";',
    'stageBtn.setAttribute("aria-pressed", String(state.stages.has(stageNumber)));\n          if (s === 20) stageBtn.title = "Boss stage";',
  );

  fs.writeFileSync(file, source);
}

console.log("Applied final Space Typing Admin UI accessibility/state patch.");
