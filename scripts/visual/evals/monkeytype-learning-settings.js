// Use with games/space-typing/scripts/visual/shot.mjs (docs/VISUAL_TESTING.md).
// Opens the actual settings and reveals the learning-mode help trigger.
(async () => {
  const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));
  const wait = async predicate => {
    for (let i = 0; i < 120; i++) {
      const value = predicate();
      if (value) return value;
      await sleep(50);
    }
    throw new Error('Learning settings did not become ready');
  };
  const button = (root, text) => [...(root?.querySelectorAll('button') ?? [])]
    .find(element => element.textContent.trim() === text);
  button(document, 'reject non-essential')?.click();
  await sleep(300);
  (await wait(() => button(document.querySelector('.pageTest'), 'custom'))).click();
  (await wait(() => button(document.querySelector('.pageTest'), 'change'))).click();
  const dialog = await wait(() => document.querySelector('#CustomTextModal[open]'));
  (await wait(() => dialog.querySelector('[role="tab"][data-value="custom"]')
    ?? [...dialog.querySelectorAll('[role="tab"]')].find(el => el.textContent.trim() === 'custom'))).click();
  const options = await wait(() => dialog.querySelector('[data-learning-mode-options]'));
  options.scrollIntoView({ block: 'center' });
  await sleep(400);
  const trigger = dialog.querySelector('button[aria-label="Help for learning mode"]');
  trigger.dispatchEvent(new MouseEvent('mouseenter'));
  const tooltip = await wait(() => dialog.querySelector('[role="tooltip"]'));
  await sleep(200);
  const box = element => element.getBoundingClientRect().toJSON();
  return {
    viewport: [innerWidth, innerHeight, devicePixelRatio],
    options: [...options.children].map(element => ({
      label: element.textContent,
      fits: element.scrollWidth <= element.clientWidth,
      box: box(element),
    })),
    tooltip: {
      text: tooltip.textContent,
      box: box(tooltip),
      outsideScrollPane: tooltip.closest('[data-custom-settings-scroll]') === null,
      fitsHeight: tooltip.scrollHeight === tooltip.clientHeight,
    },
    positionChoices: [...dialog.querySelectorAll('[data-translation-position-options] button')]
      .map(element => element.textContent),
  };
})()
