const DEFAULT_ROW_SELECTOR = ".stx-toggle-row";

export function wireLegacyRegistrySelection(
  root: HTMLElement,
  acceptedActions: readonly string[],
  onSelect: (id: string) => void,
): void {
  const accepted = new Set(acceptedActions);
  root.addEventListener("click", (event) => {
    const target = event.target;
    if (!(target instanceof Element)) return;
    const button = target.closest("button");
    if (!(button instanceof HTMLButtonElement)) return;
    if (!accepted.has(button.textContent?.trim() ?? "")) return;

    const row = button.closest(DEFAULT_ROW_SELECTOR);
    const metadata = row?.querySelector("small")?.textContent?.trim() ?? "";
    const [id] = metadata.split(" · ", 1);
    if (id?.trim()) onSelect(id.trim());
  });
}
