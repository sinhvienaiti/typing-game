# Việc: bộ chất các hệ mới trong lab chiêu (agent 2)

**Anh (05/11 18:30):** "tôi nghĩ bạn nên thêm 2 agent để xử lý cho hình ảnh vào lab dần đi cũng đc". Agent 1 (`tasks/lab-flipbooks.md`) chuyển video Firefly thành flipbook. Agent 2 (việc này) viết mã để lab vẽ các chiêu Kiếm (phím 0–7) bằng chất liệu của từng hệ mới.

## Thiết kế phải theo
- `docs/games/tu-tien/skills/ELEMENT_LAYER.md` §1–3: vũ khí cho hình, hệ cho chất; **thay, không chồng**.
- `docs/games/tu-tien/skills/PRODUCTION_LIST_2026-11-05.md` §3 và §7: động từ, màu, lấp lánh của từng hệ.
- `docs/games/VFX_STANDARD.md`: 5 pha, bên ra chiêu trước. Mỗi pha có lớp lấp lánh (AGENTS.md: "Skill effects sparkle too").
- Mẫu mã: `src/view/skills/element-kit.ts` (giao diện hook), `element-fire.ts` (bộ Hỏa), `element-metal.ts`, `elements.ts` (danh sách), `element-stage.ts`, `flipbook.ts` (`FlipbookLibrary`, đọc `art-src/lab/vfx/<hệ>/manifest.json`).

## Lời anh cần giữ
- 17:08: "phải xử lý cả hiệu ứng vfx khi đánh vào nền đất cho từng hệ". Mỗi hệ có đòn đánh xuống đất (`role: groundImpact`) và dấu đất (`role: groundMark`).
- 17:08: "vẫn phải chi tiết nhưng tránh việc làm quá phức tạp khiến bạn không xử lý được". Mỗi hook dùng tối đa vài lớp flipbook có sẵn, đặt, định giờ và hoạt họa chúng. Không vẽ lửa, sét hay vết nứt bằng mã (luật "không vẽ bằng mã" của AGENTS.md).
- Hiệu ứng tấn công nhanh, tan chậm: giữ đỉnh, tan bằng ăn mòn (`holderode` trong `flipbook.ts`).

## Hợp đồng với agent 1
- Manifest mỗi hệ ở `art-src/lab/vfx/<hệ>/manifest.json`. Mỗi mục có `role`, thuộc một trong: `charge`, `release`, `ribbon`, `sheath`, `impact`, `burst`, `groundImpact`, `sparkle`, `slash`, `groundMark`.
- Mã hệ: `water thunder wind ice earth wood dark light poison blood void star`.
- **Clip chưa có thì hook trả `false`** để lớp gốc vẽ, nên việc này chạy được trước khi agent 1 xong. Có clip mới thì tải lại lab là thấy.

## Thứ tự
1. **Thủy trước.** Đây là mẫu cho các hệ sau và là hệ khó nhất theo D59.
2. Lôi.
3. Các hệ còn lại theo thứ tự clip có trên đĩa.
4. Cuối cùng: một phím trình diễn trong lab cho 4 cột trụ và các tuyệt kỹ (`art-src/lab/vfx/ult/`). Phím này phát lớp video tại sân, đúng góc camera chơi, chưa nối vào sim.

## Chỗ làm
- Worktree riêng: `git -C games/immortality-cultivation worktree add ../.wt-ic-lab-elements -b claude/lab-element-kits c15af6f`. Commit `c15af6f` là đầu nhánh `codex/fire-lot1-art`.
- Nếu cần `node_modules`, tạo link tới thư mục của game như các worktree khác.
- Commit file của mình theo từng hệ, ghi đúng đường dẫn; không push, không media.
- Không sửa `src/kit/**`, sim hay nội dung game. VFX chỉ ở view.

## Kiểm
- `tsc --noEmit -p .` không lỗi.
- Vitest qua đủ (`--no-cache --configLoader runner --maxWorkers 4`).
- Lab: chạy dev server của worktree ở **tab riêng**, đồng hồ cố định `?fixed=1`. Mỗi hệ một video phím 0–7 kèm đòn đánh xuống đất, dưới 30 MB, để ở `/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-05/tu-tien/lab-elements/`. Thư mục có `ABOUT.md`; chạy `node scripts/review-index.mjs`.
- **Không chạm, không tải lại, không đưa lên trước** các tab `seed` và `tab-3` tới `tab-7` (hàng Firefly, ChatGPT, Gemini). Đổi khổ tab của mình thì trả lại `desktop` khi xong.

## Báo
- Ghi mục "Nhật ký" bên dưới sau mỗi hệ: commit, số test, video.
- Hệ nào chưa đẹp thì ghi rõ lớp nào và vì sao.

## Nhật ký

**Claude 18:52 (điều phối):** hệ Ám có thêm lớp thân khói đen trên nền trắng (manifest `dark`, `"layer": "body"`, chế độ `smoke`); bản nền đen là `"layer": "rim"`. Vẽ `body` (trộn thường) dưới `rim` (cộng sáng) khi cả hai có mặt.

**Thủy (19:00, agent 2):**
- Commit `6b1492a` trên `claude/lab-element-kits` (worktree `games/.wt-ic-lab-elements`): bộ chung `element-clips.ts` (mỗi hook đặt, định giờ, hoạt họa vài clip theo `role`; vai trò chưa có clip thì trả `false` để lớp gốc vẽ), `element-water.ts`, đọc `role` và `timing.peak` trong manifest, `__lab.clipKit()`, kịch bản quay `scripts/visual/scenarios/lab-element-kits.mjs` và script ghép video có chú thích `scripts/visual/element-kit-video.py`.
- Nhịp: đánh tới khung đỉnh của clip trong 0,05–0,12 s, rồi giữ và tan trong thời lượng theo vai trò (va chạm 0,9 s, nổ lớn 1,5 s, dấu đất 2,8 s; Thủy × 1,2). Mọi đòn chạm đất: `groundImpact` bật lên, `groundMark` nằm phẳng trên đất (vẽ vuông nên hình bầu dục trong clip đọc thành tròn dưới camera chơi).
- Luật Thủy: sóng của đòn chảy tiếp qua con thú theo hướng đánh (clip `slash`, chưa có thì `ribbon`). Clip giữ màu gốc, cộng sáng và che đất mạnh (`occlude` 0,9) để thân nước thành khối, không thành màn lam nhạt.
- Video v1: `owner-review/2026-11-05/tu-tien/lab-elements/lab-water-v1.mp4` (9,8 MB, phím 0–7, cận cảnh đòn xuống đất của phím 1 và 5). Mới có 3 clip (`burst`, `slash`, `groundMark`); 7 vai trò còn lại đang để lớp gốc vẽ theo bảng màu Thủy, nên **chưa đẹp ở pha gom, phát chiêu, bay và lấp lánh**. Va chạm thường đang dùng nổ lớn thu nhỏ thay clip `impact`.
- Kiểm: `tsc --noEmit` sạch; test `element-clips` 8/8, `element-layer` 33/33 (Vitest toàn bộ: xem dòng của Lôi).

**Lôi (19:05, agent 2):**
- Commit `6775b72`: `element-thunder.ts`. Luật: đánh dấu rồi phán, con thú lóe lấp lánh, một nhịp sau clip `ribbon` dựng đứng giáng từ trên xuống (khi có clip `ribbon`), va chạm nổ, đất bị đánh và cháy sét. Cộng sáng, che đất nhẹ (`occlude` 0,35).
- Clip có: `impact`, `burst`, `slash`, `groundMark`.
- Video v1: `lab-thunder-v1.mp4` (9,4 MB). Chưa có `ribbon` nên chưa thấy cột sét giáng từ trời; các pha gom, phát chiêu, bay, lấp lánh đang là lớp gốc tô tím.
- Vitest toàn bộ sau Thủy và Lôi: 95 tệp, 1039 test qua.

**10 hệ còn lại (19:10, agent 2):**
- Commit `c0408ec`: bốn luật mới trong `element-clips.ts` (`shatter` Băng, Không gian: lóe giữ một nhịp rồi vỡ; `crush` Thổ: đòn xuống đất ngay dưới chân; `claim` Mộc, Độc: rễ hay vũng độc chiếm đất dưới con thú; `drain` Huyết: lấp lánh chạy ngược về người ra chiêu), `streamOf`, `auraOf`, 6 trạng thái trên thú mới.
- Mỗi hệ một commit: Phong `9f173b8`, Băng `30fd437`, Ám `029edd5`, Quang `03da075`, Mộc `34aa758`, Thổ `2b872a3`, Độc `dc0e488`, Huyết `6aec9f6`, Không gian `4579c3d`, Tinh tú `932de69`.
- Ám vẽ thân bằng chế độ `heat` (theo ghi chú agent 1): phần mờ của clip thành vật chất tím đen che đất, viền tím, chỉ nét sáng nhất là tím nhạt.
- Huyết giữ màu đỏ thẫm ở sắc độ ~338°, tối, tránh đỏ cảnh báo `#FF4A4A` của địch.
- Huyết, Không gian, Tinh tú chưa có clip nào trên đĩa: lab vẽ bằng lớp gốc theo bảng màu hệ; chưa quay video.

**Phím trình diễn (19:15, agent 2):** commit `c154f35`, `src/lab/showcase.ts`. Phím **8** phát lần lượt 4 cột trụ rồi các tuyệt kỹ của `art-src/lab/vfx/ult/` thành lớp video trên sân đúng góc camera chơi, chưa nối vào sim. Cột trụ đứng trên con thú gần giữa màn hình, chân cột ở 80 % chiều cao ô chạm đất, đỉnh vượt mép trên khung; cột trụ cả sân và tuyệt kỹ phủ cả tầm nhìn quanh điểm giữa màn hình. `__lab.showcase(id?)`. Changelog: `docs/changelog/2026-11-05-lab-element-kits.md` (commit `fc52067`).

**Video v1 (19:20, agent 2):** `owner-review/2026-11-05/tu-tien/lab-elements/`, mỗi tệp khoảng 9–10 MB, phím 0–7 và cận cảnh đòn xuống đất của phím 1 và 5; dòng chú thích trên đầu khung ghi clip nào đã có, vai trò nào còn để lớp gốc vẽ.
- `lab-water-v1`, `lab-thunder-v1`, `lab-wind-v1` (4 clip), `lab-ice-v1` (3), `lab-dark-v1` (2), `lab-light-v1` (2), `lab-wood-v1` (2), `lab-earth-v1` (1: chỉ `burst`), `lab-poison-v1` (1: chỉ `groundImpact`).
- `lab-showcase-pillars-ultimates-v1`: phím 8, 4 cột trụ rồi 6 tuyệt kỹ (gồm `ult-thunder-nine-heavens-v2`, `ult-water-profound-sea-v2`). Đỉnh cột Hỏa, Quang vượt mép trên khung như bản vẽ. **Tuyệt kỹ Ám chưa đẹp:** cộng sáng làm mất phần đen, chỉ còn vòng và tua tím (nên thử `heat` như thân Ám).
- **Chưa đẹp chung:** mọi hệ mới có 1–4 trong 10 vai trò; gom lực, phát chiêu, bay và lấp lánh của mọi hệ đang là lớp gốc tô màu hệ. Khi agent 1 thêm clip: chạy lại `scratchpad/batch.sh v2 <hệ>…` (xem ghi chú bàn giao trong thư mục ghi chú chung), không cần sửa mã.

**Sửa theo lời anh 19:12 (agent 2, 19:40):**
- `c49b844`: phím 8 bỏ hẳn hai tuyệt kỹ anh đã loại (`ult-water-profound-sea`, `ult-thunder-nine-heavens`) dù manifest có ghi; bản vẽ lại `-v2` chạy thay.
- `cf8241c`: lớp thân của điều phối 18:52. Clip khói nền trắng (`layer: "body"`, chế độ `smoke`) vẽ dưới clip nền đen cùng vai trò (`layer: "rim"`, cộng sáng như lúc quay), cùng chỗ, góc, chuyển động; vai trò chưa có thân thì giữ cách vẽ cũ (Ám: `heat`). Chưa thử trên clip thật vì bản nền trắng chưa có trên đĩa.
- `6ea578b`: "dạng vệt chém nên làm to vệt đó ra". Vệt chém lưỡi liềm của **mọi hệ** (Kim, Hỏa, và clip `slash` của 12 hệ) to gấp 1,8 lần cả dài lẫn rộng, đổi ở một chỗ (`CUT` trong `sword-grammar.ts`, `slashAt` của `sword-skills.ts`). Vệt lớn dần sang ngang và xuống theo trục lên của camera (tâm trượt xuống một nửa phần lớn thêm, không thấp hơn 0,25 m) nên mép trên nhô lên ít, chữ trên đầu thú không bị che. Vệt Kim giữ lâu hơn chút (0,22 s và 0,28 s); vệt clip tan mềm vào đất; sóng chảy tiếp của Thủy và vết cắt phím 7 cũng ×1,8. Đã xem cận cảnh phím 1 của Thủy và Kim: vệt to rõ, số sát thương phía trên vẫn đọc được.
- `bb0e009`: Ám "giống màu tím": **chưa đổi màu** (anh đang chọn A đen viền đỏ than hay B đen viền xám bạc). Mọi màu của Ám giờ lấy từ một hằng số `DARK_RAMP` trong `element-dark.ts` (core, rim, mid, deep, ink, soot): chọn xong chỉ sửa sáu giá trị đó.
- Lệnh nền đang chờ: quay v2 khi qua 20:55 và có thêm clip chất liệu.

**Ám bảng màu A (anh 19:20, agent 2, 19:30):**
- `7dfc6d7`: `DARK_RAMP` thành đen đỏ thẫm (core `#FFE2CC`, rim `#D0301F`, mid `#9A1A1A`, deep `#6A0D18`, ink `#12050A`, soot `#1C050B`), không còn tím ở đâu trong Ám; test kiểm mọi màu Ám nằm trong dải đỏ (330°–40°). Hai atlas tím v1 (`dark-slash-arc`, `dark-ground-mark`) bị bỏ qua theo md5 dù manifest còn ghi (`ClipKitSpec.rejected`), nên Ám vẽ bằng lớp gốc theo dải màu mới cho tới khi bản vẽ lại hệ A về (atlas mới, md5 mới, tự nhận).
- `104a3b5`: lõi sáng của lớp gốc Ám là trắng than hồng trên đỏ thẫm (`glowRamp`), không pha đỏ với trắng (ra hồng cá hồi, lẫn với Huyết).
- Còn lại: khi chưa có clip, Ám chỉ có lớp gốc là ánh sáng (đỏ), **chưa có phần đen**; phần đen sẽ có khi clip khói nền trắng hệ A về (lớp `body`).
- Lưu ý màu: viền `#D0301F` (sắc ~6°) gần sắc đỏ cảnh báo của địch `#FF4A4A` (D54), chỉ khác ở độ tối. Cần nhìn trong trận có thú đỏ cảnh báo trước khi chốt.

**Ám bảng màu B để anh so (anh ~19:35, agent 2, 19:50):**
- `de44ab1`: `DARK_RAMP_B` (đen, viền xám bạc: mực dưới ánh trăng; core `#F6F9FF`, rim `#9CAAC0`, mid `#5E6A7C`, deep `#343C48`, ink `#0B0D11`, soot `#0E1116`). A vẫn mặc định; lab đọc `?dark=b` một lần lúc tải và thay bộ Ám bằng B (`?dark=a` hay không có: A). Test: B chỉ có màu xám, không đỏ, không tím.
- Lab cố định cho anh: bản chụp `de44ab1` ở `/private/tmp/lab-elements-snapshot-0511`, dev server cổng **4310** (launch.json `ic-lab-owner-4310`), không sửa gì trong lúc anh thử. Atlas `art-src/lab/vfx/` (kể cả `ult/`) tải đủ (200/304), console không lỗi; cảnh báo WebGL "Feedback loop" có cả khi chọn Kim, là cảnh báo sẵn có của lab.
  - Ám A: http://127.0.0.1:4310/skills-lab.html?element=dark
  - Ám B: http://127.0.0.1:4310/skills-lab.html?element=dark&dark=b
  - Phím 8: http://127.0.0.1:4310/skills-lab.html (bấm 8 nhiều lần: 4 cột trụ rồi 7 tuyệt kỹ)

**Phím 2 dùng lưỡi liềm thiết kế (anh ~19:45, agent 2, 20:05):** "vì sao nhất tuyến xuyên vân chỉ sử dụng hình lưỡi liềm bằng tự style".
- Nguyên nhân: lúc trúng, phím 2 rải 9 lưỡi liềm nhỏ dọc đường và một lưỡi liềm ở mỗi con thú trúng; với Thủy, Phong thêm sóng lưỡi liềm "chảy tiếp" ở mỗi con. Thành chuỗi dấu nhỏ, đọc như hoa văn vẽ bằng mã.
- `d27a814`: mọi hệ (Kim, Hỏa và 12 hệ clip) có **một lưỡi liềm lớn bay cùng lưỡi kiếm** dọc đường, ngang đường, từ tay tới cuối đường (hook mới `flyingCut`; cỡ 2,0 × `CUT` 1,8), rồi đáp thành **một nhát lưỡi liềm lớn ở cuối đường**. Hệ có clip `slash` dùng chính clip đó (giữ ở khung đỉnh: cả lưỡi liềm); Hỏa dùng lưỡi liềm nóng chảy của nó; hệ chưa có clip dùng lưỡi liềm của Kim tô màu hệ. Bỏ hết lưỡi liềm nhỏ; dọc đường chỉ còn lấp lánh (lớp hào quang).
- `8b86fc6`: sóng "chảy tiếp" của Thủy, Phong dùng clip `ribbon` khi có; chỉ dùng clip lưỡi liềm cho đòn đơn, không cho các con trên đường của phím 2.
- Test: một lưỡi liềm bay mỗi khung suốt đường bay, ≥ 1,8 lần cỡ cũ, đúng một nhát ở cuối; với hook thật của Thủy số thẻ `slash` ≤ 13 (bỏ sửa thì 15). Đã xem trong lab: Thủy, Kim, Hỏa.
- Lab cố định của anh ở cổng 4310 đã chép `8b86fc6`.

**Phím 2 và vệt chém của Kim, Hỏa dùng clip thật (anh ~20:00 "fire, dark đều k có", agent 2, 20:20):**
- `877d3e4`: `CrescentClip` đọc clip `slash` của một thư mục cho bộ không vẽ theo vai trò. Kim (lớp gốc) và Hỏa (`element-fire.ts`) vẽ vệt chém và lưỡi liềm bay của phím 2 bằng `metal-slash-arc`, `fire-slash-arc`; lưỡi liềm vẽ bằng mã chỉ còn là lớp mảnh bên dưới. Hệ chưa có clip `slash` dùng clip Kim tô màu viền của hệ.
- `ae92feb`: khung ảnh va chạm kiểu manga của 12 hệ clip lấy màu từ dải màu của hệ (trước đó dùng lam của Kim: Ám đỏ thẫm ra khung lam).
- Kiểm phím 2 cả 14 hệ trong lab (bản 4310 = `ae92feb`): **clip thật** ở 13 hệ: Kim, Hỏa, Thủy, Lôi, Phong, Băng, Thổ, Mộc, Quang, Độc, Huyết, Không gian, Tinh tú (Tinh tú vừa có `star-slash-arc`); **dự phòng** (clip Kim tô đỏ thẫm): Ám, chờ `dark-slash-arc-a`.

**Phím 8 thành bảng trình diễn cho anh (anh ~20:00 "xử lý nhanh cho tôi lớp tuyệt kỹ, trình diễn trụ cột", agent 2, 20:40):** commit `b4e3af2`, bản 4310 đã chép.
- Thứ tự: 4 cột trụ (Lôi Trụ, Vạn Lôi Trụ, Thiên Quang Trụ, Hỏa Tinh Trụy) rồi mỗi hệ một tuyệt kỹ theo thứ tự anh nêu; mục nào có clip trong manifest `ult` mới hiện. Tối nay có 17 mục: đủ 4 cột trụ và 13 tuyệt kỹ, chỉ thiếu Ám (chờ `ult-dark-a`). Không bao giờ phát `ult-water-profound-sea`, `ult-thunder-nine-heavens` và `ult-dark` tím.
- Phím 8 tới, Shift+8 lùi, danh sách "Trình diễn (8)" trong bảng điều khiển chọn thẳng. Chú thích trên giữa màn hình: tên tiếng Anh, tên tiếng Việt, cột trụ hay tuyệt kỹ, hệ, vị trí trong danh sách. Tên 6 hệ mới lấy theo ảnh đã vẽ (skill-stills-0511.json) vì PRODUCTION_LIST §7 chỉ có mô tả.
- Đánh nhanh tới khung đỉnh của clip (0,2 s) rồi giữ và tan chậm (cột trụ 2,4 s, tuyệt kỹ 4,6 s); tuyệt kỹ rung và lóe màn hình ở bậc tuyệt kỹ, cột trụ ở bậc chiêu; phát `take1.wav` của âm Firefly tương ứng (chỉ trong lab).
- Kiểm trên 3068 và 4310: 17 mục đều phát, chú thích đúng, âm tải được, console không lỗi mới.
- `f062e63` (20:10): hai clip khói nền trắng đầu tiên của Ám hệ A (`dark-impact-white`, `dark-ground-impact-white`, lớp `body`) chưa có clip nền đen đi kèm, nên trước đó bị bỏ qua. Giờ vai trò chỉ có lớp thân thì vẽ lớp thân một mình, màu mực gần đen của Ám: đòn Ám ra khối khói mực đen dưới vệt chém đỏ thẫm. Bản 4310 đã chép.

**Phím 9: 30 kỹ năng mới (anh duyệt 20:20, agent 2, 20:35):** commit `64d919b`, bản 4310 đã chép.
- `showcase.ts` thành một lớp dùng chung cho mỗi danh mục: phím 8 giữ nguyên; phím 9 (Shift+9 lùi, danh sách "Kỹ năng mới (9)") cho 30 thiết kế của `SKILLS_EXPANSION_2026-11-05.md`, tên tiếng Anh và Hán Việt, nhóm, các hệ hợp nhất; khớp clip theo trường `code` (A1…D8) trong `art-src/lab/vfx/expansion/manifest.json` (vai trò `area`, `avatar`, `beast`, `treasure`).
- Đặt theo nhóm, đúng camera chơi: diện rộng và pháp bảo phủ sân; pháp tướng dựng trên người ra chiêu; thần thú phủ đàn thú (C3, C6 bay ngang sân); pháp tướng và thần thú trong suốt 32 % để chữ trên quái đọc được. Đánh nhanh, tan chậm; pháp tướng và thần thú rung, lóe ở bậc tuyệt kỹ, còn lại ở bậc chiêu. Âm tạm: `take1` của tuyệt kỹ hệ đầu tiên của thiết kế. Một chú thích dùng chung cho cả hai phím.
- Lúc 20:35 thư mục `expansion` chưa có clip: danh sách phím 9 trống, không lỗi. Clip vào thì **tải lại trang** là thấy.

**Vệt chém là vệt chém, không phải con dấu (anh ~20:50 "bạn có hiểu dạng vệt chém không", agent 2, 21:15):** commit `50ec720`, bản 4310 đã chép.
- Mọi vệt chém (clip `slash` của 12 hệ, clip của Kim và Hỏa, ảnh tĩnh của Ám) hiện bằng **một đầu sáng quét từ gốc tới mũi** trong 0,1 s, **giữ** 0,15 s, rồi **ăn mòn từ đuôi về mũi** trong 0,7 s (bản vá shader `sweepCard`, clip giữ ở khung đỉnh). Lưỡi liềm bay của phím 2 giữ nguyên hình. Lấp lánh rơi dọc cung khi đầu quét đi qua (Kim: tia sáng; Hỏa: tàn lửa; hệ clip: clip `sparkle` khi có).
- Bỏ hẳn lưỡi liềm vẽ bằng mã đóng dấu dưới clip (Kim, Hỏa chỉ vẽ nó khi không có clip).
- Lớp thân khói nền trắng chỉ dùng cho đòn xuống đất và nổ lớn, độ đục 55 %, mòn dần: `dark-impact-white` bị bỏ, không còn khối khói đen dưới vệt chém.
- Ám vẽ vệt chém bằng ảnh tĩnh hệ A anh duyệt (`dark-slash-arc-a.v1-try2.png`, Codex 299) cho tới khi có video; dải nhiệt của Ám đổi thành đen đỏ thẫm lên viền đỏ than, lõi trắng than hồng; vệt ở độ nóng 0,7: khói đen, mép đỏ than, không còn chút lam nào.
- Khung cho anh: `owner-review/2026-11-05/tu-tien/lab-elements/dark-slash-sweep-mid-50ec720.jpg` (đang quét) và `dark-slash-hold-50ec720.jpg` (lúc giữ). Đã xem Ám, Kim, Thủy, Hỏa trong lab.

**Lượt v2 (21:15):** đang quay nền 12 hệ (`lab-<hệ>-v2.mp4`).
- 21:20: phím 9 trên bản 4310 đã nhận clip đầu tiên của `expansion` (`myriad-lotus-domain`, A1): khớp theo mã, chú thích "A1 · Myriad Spirit Lotus Bloom · Vạn Linh Liên Hoa Trận · Diện rộng · Hệ Mộc, Quang, Thủy, Hỏa", không lỗi. Clip mới vào thì tải lại trang là thấy, không cần sửa mã.

**Lượt v2 xong (21:40):** `owner-review/2026-11-05/tu-tien/lab-elements/lab-<hệ>-v2.mp4`, 12 hệ (Thủy, Lôi, Phong, Băng, Thổ, Mộc, Ám, Quang, Độc, Huyết, Không gian, Tinh tú), mỗi tệp 8,7–10 MB. Quay trên bản `50ec720`: đã có vệt chém to, dấu đất của mọi hệ, Ám hệ A, phím 2 lưỡi liềm thiết kế. **Lưu ý:** v2 còn vệt chém lệch quét gốc→mũi, đã bị thay bằng lưỡi liềm đối xứng ngay sau đó (dưới đây); v3 sẽ có lưỡi liềm đối xứng. Clip chất liệu (gom, phát chiêu, bay, lấp lánh) vẫn chưa vào manifest nào lúc quay, nên các pha đó vẫn là lớp gốc.

**Khí kiếm là lưỡi liềm đối xứng (anh ~21:20 "chúng ta đang bắn kiếm thẳng ra cơ mà", agent 2, 21:45):** commit `b8ee9a8`, bản 4310 đã chép.
- Mọi chiêu Kiếm (phím 0–7, cả lưỡi liềm lớn của phím 2), mọi hệ: lưỡi liềm **đối xứng**, hai sừng đều, mặt lồi hướng về trước theo đường bay, nằm giữa đường bay, cỡ 1,8 lần như trước.
- Clip và ảnh tĩnh đang có đều lệch, nên shader lật gương nửa tốt hơn của ô qua trục giữa: nửa dày hơn đo theo độ sáng khung đỉnh của từng clip (Kim, Hỏa, Thổ, Mộc, Ám: nửa phải; các hệ khác: nửa trái). Khi ảnh đối xứng của Codex (`stills/skills/<hệ>-crescent-sym.v1-try1.png`) có trên đĩa thì tự dùng ảnh đó.
- Nhịp: nở từ giữa ra hai sừng trong 0,08 s, lóe 0,07 s, rồi mòn từ hai đầu sừng về giữa trong 0,6 s. Lưỡi liềm bay của phím 2 bay trước mũi kiếm.
- Luật chảy tiếp của Thủy, Phong giờ là chính lưỡi liềm đó trôi tiếp về phía trước (dải `ribbon` trước đó hiện thành mảng chữ nhật cạnh cứng).
- Vệt chém lệch quét gốc→mũi giữ cho phái Đao sau này: `SLASH_STYLE` = "sabre", trong lab `?cut=sabre`.
- Khung cho anh: `crescent-water-launch-b8ee9a8.jpg`, `crescent-water-impact-b8ee9a8.jpg`, `crescent-dark-launch-b8ee9a8.jpg`, `crescent-dark-impact-b8ee9a8.jpg` (cùng thư mục owner-review).

**Lưỡi liềm đối xứng của Codex 302 (agent 2, 22:00):** commit `6f33037` (+ test), bản 4310 đã chép.
- 14 ảnh `stills/skills/<hệ>-crescent-sym.v1-try1.png` thay cho nửa clip lật gương, vẽ nguyên (không lật gương), hoạt họa như trước (nở từ giữa, bay trước mũi kiếm ở phím 2, lóe, mòn từ hai sừng).
- Tâm sáng của mỗi ảnh (đọc lúc nạp) làm điểm neo, nên lưỡi liềm nằm đúng trên đường bay (các ảnh lệch lên hoặc xuống trong khung).
- Thổ vẽ mặt lồi hướng lên nên được lật ngược khi nạp: mặt lồi của mọi hệ đều hướng về trước.
- Khung cho anh: `crescent-sym-water-launch-6f33037.jpg`, `crescent-sym-earth-launch-6f33037.jpg` (đang bay), `crescent-sym-water-impact-6f33037.jpg`, `crescent-sym-earth-impact-6f33037.jpg` (lúc trúng).
- 22:05: phím 9 trên bản 4310 nhận đủ **30/30** thiết kế mở rộng (A1…D8), đúng thứ tự, mỗi mục có chú thích tên Anh và Hán Việt; phím 8 vẫn 17 mục; không lỗi, không ngoại lệ (kiểm bằng Chrome headless riêng). Khói nền trắng `dark-big-burst-white` (lớp thân, vai trò `burst`) tự vào nổ lớn của Ám dưới dạng khói mờ.

**06/11 11:41 · Claude (agent con skill-five-phase-samples, cùng checkout `games/.wt-ic-lab-elements`) gửi lab-element-kits:** hai bên đang sửa cùng `src/lab/meteor-rain.ts` (và tôi đã sửa `skills-main.ts`, `herd.ts`, `caster.ts`, `hand-sword.ts`, `flipbook.ts`; tệp mới `src/lab/five-phase.ts`, `src/lab/comet-head.ts`, chưa commit). Clip `comet` của 14 hệ (+ `dark-comet-white` lớp thân) đã vào manifest kèm `head`, `dir`, `video` 1080p (tôi làm 11:30–11:40). Đề nghị: **thân sao chổi trong `meteor-rain.ts` để bạn giữ** (`cometOf` + `videoCard` của bạn); tôi gỡ `CometHead` của tôi khỏi `meteor-rain.ts` và chỉ giữ các móc năm pha (`fiveNow`, `five.markAt/release/skyStreak/hit/aftermath`, `FIRST_S`, `FALL_S` 0,3, `Meteor.fall`). Xin đừng xóa các móc đó, đừng commit `five-phase.ts`/`comet-head.ts`/`skills-main.ts` của tôi; tôi commit phần của tôi bằng đường dẫn riêng. Ghi lại vào đây nếu bạn muốn chia khác.
**06/11 11:43 · Claude (agent con skill-five-phase-samples):** thấy bạn đã gỡ phần comet của bạn khỏi `meteor-rain.ts`/`showcase.ts` lúc 11:40, nên **bỏ qua đề nghị trên**: thân sao chổi (`src/lab/comet-head.ts`, video 1080p, đầu dẫn) và năm pha do tôi làm và commit. `tsc` sạch.
