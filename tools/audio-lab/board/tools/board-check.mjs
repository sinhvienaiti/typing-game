// CDP scenario for the Listening Board (run by board/browser_check.py through cdp-run.mjs).
// Rates the demo session by keyboard only, checks blindness and loudness wiring, takes
// screenshots at 1280x720 and 1920x1080. Env: URL (…/?s=demo), OUT_DIR.
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const VK = { Enter: 13, Backspace: 8, Space: 32, Escape: 27, ArrowLeft: 37, ArrowUp: 38, ArrowRight: 39, ArrowDown: 40, Slash: 191 };
const vk = (code) => VK[code] ?? (/^Digit\d$/.test(code) ? 48 + Number(code[5]) : /^Key[A-Z]$/.test(code) ? code.charCodeAt(3) : 0);
const SHIFTED = { 1: "!", 2: "@", 3: "#", 4: "$", 5: "%", 0: ")" };

export default async function (page) {
  const URL = process.env.URL;
  const OUT = process.env.OUT_DIR;
  const shots = [];
  const c = {};
  const overflow = {};
  const shot = async (name) => {
    overflow[name] = await page.eval(`document.documentElement.scrollHeight - innerHeight`);
    shots.push(await page.shot(`${OUT}/${name}.png`));
  };
  const press = async (code, { shift = false, wait = 70 } = {}) => {
    let key = code.startsWith("Key") ? code.slice(3).toLowerCase() : code.startsWith("Digit") ? code.slice(5) : code;
    if (code === "Space") key = " ";
    if (code === "Slash") key = shift ? "?" : "/";
    if (shift && code.startsWith("Digit")) key = SHIFTED[code.slice(5)];
    const base = { key, code, modifiers: shift ? 8 : 0, windowsVirtualKeyCode: vk(code) };
    const text = key.length === 1 ? key : code === "Enter" ? "\r" : undefined;
    await page.send("Input.dispatchKeyEvent", { type: "keyDown", ...base, ...(text ? { text } : {}) });
    await page.send("Input.dispatchKeyEvent", { type: "keyUp", ...base });
    await sleep(wait);
  };
  const S = (expr) => page.eval(`(() => { const {S, AU} = window.__board; return ${expr}; })()`);
  const waitFor = async (expr, ms = 15000) => {
    for (let t = 0; t < ms; t += 100) {
      if (await page.eval(`(() => { try { return !!(${expr}); } catch (_) { return false; } })()`)) return true;
      await sleep(100);
    }
    throw new Error("timeout waiting for " + expr);
  };
  const blind = () => page.eval(`(() => {
    const html = document.documentElement.outerHTML;
    const net = performance.getEntriesByType("resource").map((e) => e.name).join(" ");
    const leak = /\\.(wav|ogg|flac|mp3)\\b|phim-|chuong-|trung-|xu-\\d|nen-ong|probe|distinct/i;
    return { domClean: !leak.test(html), netClean: !leak.test(net) };
  })()`);

  // ---- start dialog (1280x720)
  await page.goto(URL, { settle: 200 });
  await waitFor(`window.__board && __board.S.phase === "start" && document.querySelector(".modal h2")`);
  c.startTitle = await page.eval(`document.querySelector('.modal h2')?.textContent`);
  await shot("01-start-1280x720");
  await press("Digit1");                       // headphones
  await press("Enter", { wait: 100 });
  await waitFor(`__board.S.phase === "item"`);
  c.phase = await S("S.phase");

  // ---- item 1: demo.phim, 3 candidates, one of them 10 dB louder before matching
  c.item1 = await S("S.sess.items[S.idx].id");
  c.ctxDefault1 = await S("S.ctx");
  c.cardBefore = await page.eval(`fetch('/api/card/demo/02-demo.chuong/A/0').then((r) => r.status)`);
  c.revealBefore = await page.eval(`fetch('/api/reveal/demo/01-demo.phim').then((r) => r.status)`);
  for (const d of ["Digit1", "Digit2", "Digit3"]) await press(d, { wait: 250 });
  c.digitInLoop = await S("AU.play && { kind: AU.play.kind, label: AU.play.label }");
  await press("Escape");
  await press("Space", { wait: 600 });
  c.loop = await S("AU.play && { kind: AU.play.kind, events: AU.play.events.length, label: AU.play.label }");
  c.audio = await S("({ state: AU.ctx.state, t: AU.ctx.currentTime, rate: AU.ctx.sampleRate, live: AU.live.size })");
  c.gains1 = await S("S.sess.items[0].candidates.map((x) => x.files[0].gainDb)");
  await shot("02-item1-loop-1280x720");
  await press("Escape");
  await press("ArrowDown");                    // next context
  c.ctxAfterDown = await S("S.ctx");
  await press("Digit1", { wait: 120 });
  await press("Digit4", { shift: true });      // A: 4 stars
  await press("Digit2", { wait: 120 });
  await press("Digit2", { shift: true });      // B: 2 stars
  await press("KeyC");                         // B: chói
  await press("KeyY");                         // B: yếu/mỏng
  await press("Digit3", { wait: 120 });
  await press("Digit3", { shift: true });      // C: 3 stars
  c.autoPick1 = await S("({ pick: S.drafts['01-demo.phim'].pick, auto: S.drafts['01-demo.phim'].pickAuto })");
  c.blindBeforeRating = await blind();
  await press("Slash");
  await page.send("Input.insertText", { text: "A gọn, B mỏng" });
  await press("Enter", { wait: 700 });         // Enter in the note field saves
  c.saved1 = await S("!!S.sess.items[0].rating");
  c.status1 = await page.eval(`document.getElementById('status').textContent`);
  c.reveal1 = await page.eval(`document.querySelectorAll('.reveal').length`);
  await shot("03-item1-saved-1280x720");
  await press("Enter", { wait: 400 });         // next id

  // ---- item 2: demo.chuong, explicit pick, demo cards
  c.item2 = await S("S.sess.items[S.idx].id");
  c.tryEarlyEnter = await (async () => { await press("Enter", { wait: 200 }); return page.eval(`document.getElementById('status').textContent`); })();
  await press("Digit1", { wait: 200 });
  await press("Digit3", { shift: true });      // A: 3
  await press("Digit2", { wait: 200 });
  await press("Digit5", { shift: true });      // B: 5
  await press("KeyH");                         // B: hay
  await press("KeyG");                         // B: hợp game
  await press("KeyV");                         // B: picked by hand
  await press("Enter", { wait: 800 });
  c.cardAfter = await page.eval(`fetch('/api/card/demo/02-demo.chuong/A/0').then((r) => r.status)`);
  await sleep(400);
  c.thumbs = await page.eval(`[...document.querySelectorAll('.reveal img')].map((i) => i.naturalWidth)`);
  await shot("04-item2-revealed-1280x720");
  await press("KeyI", { wait: 400 });
  c.lightbox = await page.eval(`!!document.querySelector('.lightbox img')`);
  await shot("05-card-lightbox-1280x720");
  await press("Escape");

  // ---- back and forth keeps ratings
  await press("Backspace", { wait: 400 });
  c.back = await S("({ id: S.sess.items[S.idx].id, stars: S.drafts[S.sess.items[S.idx].key].stars, revealed: !!S.reveals[S.sess.items[S.idx].key] })");
  await press("Enter", { wait: 300 });         // unchanged -> next (item 2)
  await press("Enter", { wait: 400 });         // unchanged -> next (item 3)
  c.item3 = await S("S.sess.items[S.idx].id");

  // ---- 1920x1080
  await page.viewport(1920, 1080);
  await sleep(300);
  await press("Space", { wait: 700 });
  c.loop3 = await S("AU.play && { kind: AU.play.kind, events: AU.play.events.length }");
  await shot("06-item3-loop-1920x1080");
  await press("Escape");
  await press("Backspace", { wait: 600 });
  await shot("07-item2-revealed-1920x1080");
  await press("Slash", { shift: true, wait: 300 });
  c.help = await page.eval(`!!document.querySelector('.modal .keys')`);
  await shot("08-help-1920x1080");
  await press("Escape");

  // ---- resume after reload, then the variants pass (item 4)
  await page.goto(URL, { settle: 200 });
  await waitFor(`window.__board && __board.S.phase === "start" && document.querySelector(".modal .btn.primary")`);
  c.resumeButton = await page.eval(`document.querySelector('.modal .btn.primary')?.textContent`);
  c.resumeDevice = await S("S.device");
  await shot("09-resume-1920x1080");
  await press("Enter", { wait: 400 });
  await press("Enter", { shift: true, wait: 400 });   // skip item 3 without saving
  c.item4 = await S("({ id: S.sess.items[S.idx].id, mode: S.sess.items[S.idx].mode, ctx: S.ctx })");
  await press("Digit3", { wait: 150 });
  c.variantOnce = await S("AU.play && { kind: AU.play.kind, label: AU.play.label }");
  await press("Escape");
  await press("KeyX");                                  // drop variant C
  await press("Space", { wait: 900 });                  // whole set in rotation
  c.loop4 = await S("AU.play && { kind: AU.play.kind, label: AU.play.label, labels: [...new Set(AU.play.events.map((e) => e.label))].sort() }");
  await shot("10-item4-variants-1920x1080");
  await press("Escape");
  await press("Enter", { wait: 700 });
  c.saved4 = await S("!!S.sess.items[3].rating");
  c.blindEnd = await blind();
  await page.viewport(1280, 720);
  await sleep(200);
  await shot("11-item4-saved-1280x720");
  c.overflow = overflow;
  return { checks: c, shots };
}
