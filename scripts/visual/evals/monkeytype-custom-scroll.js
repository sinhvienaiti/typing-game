// Browser evaluation for the visual:shot runner documented in docs/VISUAL_TESTING.md.
// Opens the real custom-text modal and scrolls its settings; no game state is seeded.
(async () => {
  const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));
  const wait = async predicate => {
    for (let i = 0; i < 100; i++) {
      const value = predicate();
      if (value) return value;
      await sleep(50);
    }
    throw new Error('UI did not become ready');
  };
  const button = (root, text) => [...root.querySelectorAll('button')].find(el => el.textContent.trim() === text);
  button(document, 'reject non-essential')?.click();
  await sleep(200);
  (await wait(() => button(document.querySelector('.pageTest'), 'custom'))).click();
  (await wait(() => button(document.querySelector('.pageTest'), 'change'))).click();
  const dialog = await wait(() => document.querySelector('#CustomTextModal[open]'));
  const tabs = await wait(() => dialog.querySelector('[data-custom-settings-tabs]'));
  await sleep(200);
  const before = tabs.getBoundingClientRect();
  const scroll = dialog.querySelector('[data-custom-settings-scroll]') ?? dialog.querySelector('.modal');
  scroll.scrollTop = 350;
  await sleep(200);
  const after = tabs.getBoundingClientRect();
  return {
    location: location.href,
    viewport: [innerWidth, innerHeight, devicePixelRatio],
    sources: ['custom text','level passages','Everyday'].filter(text => !!button(dialog,text)),
    tabTopBefore: before.top,
    tabTopAfter: after.top,
    tabDelta: after.top-before.top,
    tabsPosition: getComputedStyle(tabs).position,
    hasSeparateScrollArea: scroll.hasAttribute('data-custom-settings-scroll'),
    scrollTop: scroll.scrollTop,
    scrollHeight: scroll.scrollHeight,
    clientHeight: scroll.clientHeight,
  };
})()
