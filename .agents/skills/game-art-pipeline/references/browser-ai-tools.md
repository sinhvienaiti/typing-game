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
  - Ask for a thorough search: many sources, official pages and repos, not one listicle. Ask for a URL behind each claim.
  - Before using the answer, send a self-review message (owner, 01/11: "luôn phải kêu chatgpt tìm thật kỹ, tự review lại trước khi bàn giao"): reopen each link and confirm it exists and does what was said; re-check each licence on the official page or LICENSE file; drop anything the licence rules forbid; mark what is uncertain; add strong options it missed; give the corrected final list. Use only the corrected list.
  - Open the key sources and mark each claim verified, partly verified, unsupported or wrong.
  - Add what it missed, write your own evaluation and say where you disagree. Run your own research in parallel when the decision matters.
  - Owner, 01/11: "bạn và chatgpt chỉ là trao đổi và tham khảo".

## 3. Gemini (gemini.google.com)

- Use it when ChatGPT refuses an image because of its limit. The owner signed in to Gemini on 01/11 (about 17:20) for exactly this case (`docs/OWNER_QUEUE.md`).
- Send the same message, in your own tab. The same gates apply.
- **Never mix tools inside one set.** If a set started in ChatGPT, redo the whole set (turnaround and every view, or every piece of the set) in one Gemini chat with the same standard block.
- The "Adobe models only" rule applies inside Firefly, not to Gemini's own site.
- **Driving it** (Tu Tien, 02/11/2026): the mode picker is the button whose aria-label starts "Mở công cụ chọn chế độ" (models such as 3.8 Flash, 3.1 Pro, 4 Argon, plus a thinking level). For images, open "Nội dung tải lên và công cụ" and pick "Tạo hình ảnh"; a "Hình ảnh" chip then shows. The prompt box is `rich-textarea .ql-editor` (`execCommand('insertText')` works, newlines included); send with the button labelled "Gửi tin nhắn". Start the prompt with "Create an image." An image takes about a minute.
- **Image out:** the inline image is a 1024 px blob preview. The button "Tải hình ảnh có kích thước đầy đủ xuống" downloads the full size (2528×1696 for 3:2) to `~/Downloads/Gemini_Generated_Image_*.png`. That is a browser download: move your own file into `art-src` right away and say so in the report.
- **Reference images cannot be pushed in from this machine:** the page's CSP blocks `fetch` and `<img>` from 127.0.0.1, writing the clipboard from a local page is denied, and in the in-app browser `window.open` replaces the current tab, so there is no opener to post to. Either generate from text only (describe the frame and presentation in words), or ask the owner to drag the reference files into the chat.
- **Visible logo:** Gemini stamps a small sparkle in the bottom-right corner. Crop it off (for example 2380×1580 from the top left) before a blind round, or the judges know the tool.

## 4. Getting files out: the local receiver

**Why it is needed:**
- Download buttons do not save files from the in-app browser frame.
- Page CSPs (ChatGPT, Gemini, Firefly's image pages) block `fetch` to localhost. On 03/11/2026 Firefly's Generate Sound Effects and Generate Speech pages allowed a `fetch` POST to `127.0.0.1`, so check per page.
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
  - **Exception (owner, 05/11/2026, button "GPT Image trong Firefly"):** GPT Image, a partner model inside Firefly Image, may be used for images that need our reference images. ChatGPT and Gemini in the in-app browser cannot receive our files (see §3), but Firefly's page can. The owner's plan lists partner models as unlimited. Other partner models stay banned unless he says so. Never click a partner-terms or age dialog: that click is the owner's.
  - **Check the model picker before every Generate:** on 05/11 the page defaulted to the partner model Gemini 3.1 (Nano Banana 2).
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
  - Chinese weapons drift to Japanese ones (katana tsuka-ito, tsuba, kissaki tip) and come out as flat cel illustrations with little detail. Tu Tien test, 02/11: Firefly 6–6.8 market and appeal and 4–5.5 fitness, against 7.6–8 for ChatGPT with the same prompt template. Use ChatGPT, or Gemini if ChatGPT is unavailable, for hero weapons and items.
- **Video VFX:**
  - "Transparent background" mode gives 540p, 16:9, 24 fps, 5 s. It is hidden while a Style or Camera preset is on.
  - Each clip comes out as a colour video and a grey alpha video. Post both blobs to the receiver.
  - About 2–3 generations, then "try again later" for about 4 minutes.
  - Ingest and numbers: `docs/games/vfx/FIREFLY_VFX_LIST.md` (§5) and [game-vfx-layered](../../game-vfx-layered/SKILL.md).
- **Sound effects and speech** (Claude generates them since 03/11; rules in [audio.md](audio.md)):
  - **Page anatomy.** Everything sits in shadow roots, so walk them with a deep query.
    - Sound Effects: a `TEXTAREA` with `aria-label="Prompt"`; an `SP-SLIDER` with `label="Duration"` (minimum 1 s); an `SP-BUTTON` reading "Generate".
    - Speech: a tiptap `ProseMirror` editor; `SP-PICKER`s for the model (`tts-model-firefly-dnt` is Adobe's Firefly Speech) and the language (`zh-CN` for Mandarin); voices are `role="option"` rows.
    - Results are `<audio src="blob:…">` elements.
  - **Fill and start.** Set the prompt with the native value setter plus `input` and `change` events, set the slider's `value` and dispatch the same events, then click Generate.
  - **Collect.** Wait for blob audio not yet posted, `fetch` each blob, and post a `FormData` to a receiver on `127.0.0.1`.
    - The receiver must be threaded (`ThreadingHTTPServer`): one stalled request hung a single-threaded one.
  - **Output:** each sound generation gives 4 WAV takes at 48 kHz stereo, peak-normalized near 0 dBFS. Speech gives 1 take and costs 1 credit.
  - **Keep the Firefly tab in front, and run one job at a time across tabs.** A background tab stalls its generations, and a second tab's job blocked the first.
  - **Retry dropped results.** The results panel sometimes resets and drops a generation: count the takes per id and regenerate the missing ones.
  - **Run long batches inside the page** as an async loop that logs to `window`. Poll the log with short calls (the JS tool times out at 45 s).
  - **Partner models** (ElevenLabs and others) open a consent dialog: partner terms and an 18+ confirmation. That click is the owner's; press Cancel.
  - **Firefly Speech** reads Mandarin cleanly, but in a narration tone. Use short lines with a dash or ellipsis before the key word for a shout's shape.
  - **Speech speed and pitch: verify before you generate.** On 03/11 a whole 10-voice batch came out at the defaults (1x, Normal) while its labels said +2 and 1.1. The cause was page state, not the API:
    - The `Speed` (0.7–1.5, step 0.05) and `Pitch` (−3…+3, step 1) `SP-SLIDER`s exist only while the Voice list is collapsed. The list is a `<details>` in `FIREFLY-EXPANDABLE-PICKER`'s shadow root, and "View more" opens a separate "Voice options" panel that closes with its "Go back" `SP-BUTTON` (match it by `textContent`; `innerText` misses it).
    - Set the inner `input[type=range]` with the native value setter plus `input` and `change` events.
    - Before each Generate, read the selected voice's chips (`aria-label` `speed-button` and `pitch-button`, for example "1.1x" and "High" for +3) and the voice's name; skip the job when they differ.
    - The history cards show each take's speed and pitch: check them after a batch. Measure the median F0 too (High lifted one voice from 262 to 372 Hz).
- **Upscale a painting 2× (Adobe's own model, 03/11):** Firefly web, Edit > Upscale, "Firefly Upscaler · Adobe models" (powered by Photoshop). It added real detail to a 1836 px ChatGPT painting (lashes, hair strands, halo cracks), where a plain Lanczos 2× only blurred.
  - Open `https://firefly.adobe.com/hub?hData=…"workflow":"upscaleImage"…` (the home page's "Upscale image" link).
  - Feed the image without a file dialog: `fetch` it from a local CORS server (the page allows `127.0.0.1`), put it in a `DataTransfer`, set `files` on the hidden `INPUT#empty-state-uploader-file-input` (deep query), and dispatch `change`.
  - Click the `SP-BUTTON[aria-label="Upscale"]`. The result is a new blob `IMG` about 2× wide (JPEG); `fetch` it and post it to the receiver. The panel then offers 4×.
  - Name the result `<id>-up2x.v<n>-try<k>.jpg` and note the source and tool in its `.prompt.txt`.
