# Browser AI tools: rules and recipes that worked

These recipes were tried in the app's in-app browser (`mcp__Claude_Browser__*`, loaded with ToolSearch) in October and November 2026. Sites change. When a selector stops matching, inspect the page again and update this file.

## 1. Rules for every tool

- **Never sign in, type a password or a key, accept terms, or buy credits.** The owner is signed in to chatgpt.com, gemini.google.com, firefly.adobe.com and tripo3d.ai. If a site shows signed out, stop and tell the owner.
- **Use your own tab.**
  - Open it with `tabs_create`, or with `navigate` if the pane is closed. Use only that tab and close it when you finish.
  - Never touch the coordinator's, the owner's or another session's tabs, even when one sits on the page you need. Open your own tab to the same URL instead.
  - The pane holds about 9 tabs. If you cannot open one, report it; do not borrow a tab.
- **`window.open` in the in-app browser navigates the same tab away.** Do not use it.
- **Leave no unsent draft.** Clear the composer before you paste, and leave it empty at the end.
- **Keep batches to what was approved.** Name the ids and the count. Firefly and ChatGPT both rate-limit bursts.
- **Delete any local file that holds a signed URL** once the download is done.
- **Workflow agents:** give each browser agent the tab it owns and the tabs it must not touch. Never send a message to a running workflow agent: it resumed a duplicate that edited the same checkout. Relay through files or later steps.

## 2. ChatGPT (chatgpt.com)

- **Mode:** Chat mode with thinking effort **High**; check that the composer shows "High". **Never Work or agent mode.**
  - The "1% usage remaining" meter belongs to Work. Chat mode is free to use; owner, 01/11: "bạn chỉ cần k dùng work, cứ dùng chế độ chat như bình thường thì k lo".
- **Chats:** start a new chat per set or topic, and keep one set in one chat so the design stays consistent.
- **Composer trap.** `document.querySelector('.ProseMirror')` can match an old "writing block" (`data-testid="chatgpt-writing-block"`, label "Start writing") inside an earlier message instead of the real composer.
  - Select `form .ProseMirror` or `.ProseMirror[aria-label="Ask ChatGPT"]`.
  - If you pasted into the writing block, press cmd+z until it is empty again, and never send from it.
- **Paste a long message:**
  1. Store the text first with one `javascript_tool` call, e.g. `window.__msg = <JSON string>`, so quoting cannot break the next snippet.
  2. Click the composer, press cmd+a then Delete, and check that it is empty.
  3. Paste:
     ```js
     const ed = document.querySelector('form .ProseMirror') || document.querySelector('.ProseMirror[aria-label="Ask ChatGPT"]');
     ed.focus();
     const dt = new DataTransfer(); dt.setData('text/plain', window.__msg);
     ed.dispatchEvent(new ClipboardEvent('paste', {clipboardData: dt, bubbles: true, cancelable: true}));
     ```
  4. Check the text. Numbered and dashed lines turn into list nodes, so compare after normalising whitespace and stripping `1.` and `- ` markers.
  5. Press Enter.
- **Wait for the answer.** Images take 1–3 minutes; check every 20–30 s with `get_page_text` or a small script. On an error, click Regenerate once. If ChatGPT asks a question, answer briefly and go on.
- **Ask for a transparent PNG** for objects and sources. It delivered a matching six-piece set with alpha, so no key colour was needed.
- **Base images and references cannot be attached by an agent.** ChatGPT's page CSP blocks `fetch` and `img` to `127.0.0.1`, so a local file cannot reach the composer.
  - Ask the owner to attach the base image in the chat.
  - Without a base frame, ChatGPT drifts from the layout: layout scores were 5.5–7.5.
  - With a base frame, give a coordinate legend in the frame's pixels and ask it to keep every position.
- **Research as a second opinion.**
  - Ask for a URL behind each claim.
  - Open the key sources and mark each claim verified, partly verified, unsupported or wrong.
  - Add what it missed, write your own evaluation and say where you disagree. Run your own research in parallel when the decision matters.
  - Owner, 01/11: "bạn và chatgpt chỉ là trao đổi và tham khảo".

## 3. Gemini (gemini.google.com)

- Use it when ChatGPT refuses an image because of its limit. The owner signed in to Gemini on 01/11 (about 17:20) for exactly this case (`docs/OWNER_QUEUE.md`).
- Send the same message, in your own tab. The same gates apply.
- **Never mix tools inside one set.** If a set started in ChatGPT, redo the whole set (turnaround and every view, or every piece of the set) in one Gemini chat with the same standard block.
- The "Adobe models only" rule applies inside Firefly, not to Gemini's own site.
- The image-out route has not yet been recorded for Gemini. On the first image, try §4 and write down here what worked.

## 4. Getting files out: the local receiver

**Why it is needed:**
- Download buttons do not save files from the in-app browser frame.
- Page CSPs (ChatGPT, Firefly) block `fetch` to localhost.
- They do not block `form-action`, so a multipart form POST to a receiver on `127.0.0.1` gets through.

**Set it up:**
1. Copy `.local/ff-bridge/recv-img.py` (outside Git) into your scratchpad. In the copy, edit five things:
   - `INBOX`, the folder it writes to;
   - `NAME`, a regex that accepts only this task's file names, for example `^ts-gun-(pulse|heat)\.v\d-try\d+\.png$`;
   - `LOG`;
   - the 303 `Location`, set to the page you post from (the chat URL, or Firefly's generate page);
   - the port in the last line (the original is hard-coded to 8765).
   - If `.local/ff-bridge/` is missing (a fresh checkout), write a small receiver with the same behaviour: `POST /upload` multipart, bind `127.0.0.1` only, a file-name regex, never overwrite, a log line per file, then a 303 back to your page.
2. Pick a port no other session uses. 8765 has been the coordinator's; Tu Tien used 8775.
3. Start it in the background with the system Python: `/usr/bin/python3 -I recv-img.py`. The script uses the `cgi` module, which Python 3.13 removed.
4. It binds `127.0.0.1` only, never overwrites a file, and skips names that do not match. Read the log after each post.

**Post an image from the page** (ChatGPT; the same idea works for any blob):

```js
const imgs = [...document.querySelectorAll('img')].filter(i => i.naturalWidth >= 900);
const img = imgs[imgs.length - 1];                    // newest generated image of the latest answer
const b = await (await fetch(img.src)).blob();        // same-origin fetch inside the page works
const dt = new DataTransfer(); dt.items.add(new File([b], NAME, {type: b.type}));
const f = document.createElement('form');
f.method = 'POST'; f.action = 'http://127.0.0.1:PORT/upload'; f.enctype = 'multipart/form-data';
const i = document.createElement('input'); i.type = 'file'; i.name = 'f'; i.multiple = true; i.files = dt.files;
f.appendChild(i); document.body.appendChild(f); f.submit();
```

- The tab follows the 303. If it lands anywhere other than your chat, navigate back to the chat URL.
- On Firefly Video, posting into a hidden `<iframe>` (`f.target = '<iframe name>'`) kept the page in place. Use that where the page allows frames, and confirm through the receiver log.
- **Verify every file:**
  - a log line;
  - the received size equals the blob size;
  - `sips -g pixelWidth -g pixelHeight <file>`.
  - Then `cp -n` it into the game's `art-src/...` together with its `.prompt.txt`.
- Stop the receiver when the task ends.

## 5. Adobe Firefly (firefly.adobe.com)

- **Adobe models only:** Firefly Image 5, Firefly Video, and the Firefly Audio model in Generate Sound Effects. Never Firefly's partner models (Gemini, GPT Image and others), never buy credits.
- **Prompts:** at most about 1024 characters. Aspect ratios: 1:1 for props and sheets, 3:4 for standing objects, 16:9 for scenes.
- **Style reference:**
  - Image 5's reference image tends to copy the subject and force its own aspect ratio. Use it only to pull a family finish (for example three accepted icons).
  - Then check at play size: on one icon set the reference made the icons busier at 28 px.
  - Firefly allows `<img>` from `127.0.0.1` but blocks `fetch`. So serve references with a copy of `.local/ff-bridge/serve-ref.py` (CORS, `127.0.0.1` only; edit its `ROOT`, and its port in the last line if 8767 is taken), then inject:
    ```js
    let input = null; const walk = r => { r.querySelectorAll('input[type=file]').forEach(e => input = e); r.querySelectorAll('*').forEach(e => e.shadowRoot && walk(e.shadowRoot)); }; walk(document);
    const im = new Image(); im.crossOrigin = 'anonymous'; im.src = 'http://127.0.0.1:8767/<ref>.png'; await im.decode();
    const c = document.createElement('canvas'); c.width = im.naturalWidth; c.height = im.naturalHeight; c.getContext('2d').drawImage(im, 0, 0);
    const blob = await new Promise(r => c.toBlob(r, 'image/png'));
    const dt = new DataTransfer(); dt.items.add(new File([blob], '<ref>.png', {type: 'image/png'}));
    input.files = dt.files; input.dispatchEvent(new Event('change', {bubbles: true}));
    ```
- **Known weak spots:**
  - Firefly does not hold one design across views (use ChatGPT, [briefs-and-sets.md](briefs-and-sets.md) §3).
  - It does not keep a flat `#00FF00` background.
  - It refused some gun prompts; reword the request or use ChatGPT.
- **Video VFX:**
  - "Transparent background" mode gives 540p, 16:9, 24 fps, 5 s. It is hidden while a Style or Camera preset is on.
  - Each clip comes out as a colour video and a grey alpha video. Post both blobs to the receiver.
  - About 2–3 generations, then "try again later" for about 4 minutes.
  - Ingest and numbers: `docs/games/vfx/FIREFLY_VFX_LIST.md` (§5) and [game-vfx-layered](../../game-vfx-layered/SKILL.md).
- **Sound effects:** see [audio.md](audio.md).
