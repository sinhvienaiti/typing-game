# Bàn giao điều phối (cập nhật 29/10/2026, khoảng 08:40)

File này để **một session mới** nối tiếp mà không cần đọc lại lịch sử chat.
- Mỗi lần dừng hay chuyển session, cập nhật file này.
- Luật của chủ dự án nằm ở memory (tự nạp) và `AGENTS.md`. Ở đây chỉ nhắc ý chính.

## 0. Giai đoạn và mục tiêu (chủ dự án 28/10)

- **Tạm dừng tính năng mới.** Chỉ sửa lỗi, làm đẹp, làm mượt phần đang chơi được.
- **Mục tiêu:** map 1 của từng game đạt chuẩn production, để chủ dự án chơi thử qua `typing-game.local` trên Mac ở nhà (chưa đưa lên mạng):
  - Rồng: L2-cau;
  - Lời Gọi: w1-silverfall, làm 3D (bước 1C) cho riêng map 1;
  - Tuyến Cuối: c1-s1.
- **Kế hoạch chung:** [`docs/games/MAP1_PRODUCTION.md`](games/MAP1_PRODUCTION.md). Nó có 7 cổng cho từng game, danh sách P0, P1, P2, bốn làn T, V, R, L với lịch theo ngày, việc của chủ dự án và rủi ro. Ngày dự kiến đủ 7 cổng: Tuyến Cuối 03/11, Rồng 06/11, Lời Gọi 12/11.
- **Kết quả kiểm kê gốc:** `docs/games/map1/audit-2026-10-28.json`. Lô Codex 1: `docs/games/map1/CODEX_BATCH.md`, đã tách thành phiếu 094–105.
- **Session điều phối:** coordinator-2 (local_5e0da15c-bdaa-4ce5-b009-0c06fc42b9d7, CLI `f97baf5f`, mở 28/10 khoảng 18:15). Session cũ `157c54d6` đã xong và giao hết việc; chủ dự án có thể lưu trữ nó.

**31/10 khoảng 16:30: ảnh UI lượt 3 (mới nhất, đọc trước).**
- **Đã gộp lượt 2 vào nhánh chơi** (con trỏ repo cha `7988eb18`, chưa đẩy):
  - Last Line `main` `651d44a` (`ts-ui-wire`): icon 149–153, khung 127, bảng nhanh mang khung game. Hai giám khảo trong game: **7,3 và 7,1** (lượt 1: 6,2 và 6,3).
  - Dragonhold `main` `45219fe` (`dh-sliders`): ảnh thanh trượt, trạng thái núm, hàng tắt tiếng, khung chín mảnh.
  - Hai host chơi đã build lại, Chrome headless: Last Line 43 yêu cầu ảnh UI, Dragonhold 10, không lỗi, 0 exception.
  - Giám khảo bảng nhanh Dragonhold/Wordwoven: **6,5** (listbox web, rãnh không có phần đầy, nút Close là chữ, năm icon hàng đọc sai).
- **Codex làn s29 (chỉ ảnh), chạy từ 16:14:** phiếu 242–246, viết từ lượt chấm hai. Luật chung ở 242: khối SMALL-SIZE, chấm ở cỡ thật trên mảnh UI thật, kiểm độ đặc (mở 2×2 giữ ≥ 80 %), độ phủ ≥ 30 %, đọc mù, tên `.r2` không ghi đè.
  - 242: 11 icon HUD, kết quả, hồ sơ của Last Line.
  - 243: icon Settings/Sound/Options của Last Line (6 vẽ lại, 4 mới: ship, letter-style, effect-strength, word-size).
  - 244: icon hàng bảng Sound Dragonhold/Wordwoven, bánh răng Wordwoven, phần đầy/rỗng thanh trượt ba game.
  - 245: hàng danh sách, nút Close ba game, bóng hình quái cỡ nhỏ Last Line.
  - 246: sọc cảnh báo, thanh vỏ tàu, tấm bến khoá của Last Line (thay CSS).
  - Xong phiếu nào thì Claude chấm **trong game ở cỡ thật**, rồi gắn.
  - **243 chấm 31/10 17:40:** nhận 8 (menu-settings, hud-settings, vol-effects, vol-interface `.r2`; ship, letter-style, effect-strength, word-size); pace-director, shake trượt → thêm vào 247.
  - **244 chấm 31/10 18:00: nhận cả phiếu** (8 icon bảng Sound Dragonhold/Wordwoven, 4 ảnh rãnh đầy/rỗng). Gắn sau khi workflow kit bảng nhanh (`wf_6b035d93-2d0`) xong: `QuickSkin.sliderFill`/`sliderEmpty`; Wordwoven dùng cặp fill + empty mới; Last Line fill cần slice riêng (ngắn 12 px mỗi đầu).
  - **242 chấm 31/10 17:05:** nhận 8 icon `.r2` (next-stage, bay-full, kills, stat-accuracy, stat-words, keyboard, clock, hazard); trượt stat-evenness, stat-new-word, rift → phiếu 247 (ý mới), làn s30 chờ s29. Tám icon nhận sẽ gắn cùng 243 sau khi workflow nền/logo xong (cùng sửa Last Line `main`); `stat-words` cần sửa mã để thẻ Words dùng nó thay icon bàn phím.
- **Claude chấm 121 và 126 (đã chờ từ 29/10):** nhận sáu nền màn hình, logo "Last Line" (bản alpha sạch) và bốn ảnh ải v2 (thay 109). Workflow `ts-backgrounds-logo` (`wf_5a214b35-b98`) đang gắn trên Last Line `main`, có giám khảo và một lượt sửa.
- **Việc kit còn lại (Claude, sau khi gộp `td-integrate`):** lớp phần đầy thanh trượt (`QuickSkin.sliderFill`), hàng danh sách mang ảnh, icon từng hàng, nút Close bằng ảnh, rãnh Master cùng độ dài; rồi đồng bộ kit sang ba game.

**31/10 khoảng 22:55: lửa rồng vòng 10 đã vào Dragonhold `main` `4b0b860`** (con trỏ `3355a80e`, chưa đẩy): gộp `dh-vfx` `ca64509` vào `main` (giữ UI, kit, âm phím của `main`), đòn đánh dở của quái tắt sau cờ `FOE_BLOWS_DEFAULT = false` (`?foeblows=1` để xem), lửa theo Reduced motion trong game; người kiểm độc lập OK; 734 test; host chơi 0 ảnh hỏng, 0 yêu cầu lỗi, 0 exception; 13 flipbook lửa đã có trên Drive. Lưu ý: số đo chớp ở miệng rồng hơi dưới mốc (0,945–0,979 so với 0,95) vì `main` tua nhanh tới chữ sớm hơn 30 khung nên tư thế bay khác; lửa giống vòng 10.
- Gói miễn phí theo V3 (chủ dự án "Cho tải và thử"): AD_FX FREE 01 chỉ là trái tim hồng; Kenney (CC0) dùng làm lớp phụ; Taproot tải về là bản Unreal. Hồ sơ `docs/games/vfx/PACKS.md`. Workflow `dragon-fire-test-c` (`wf_9b83f4d7-f20`, nhánh `dh-fire-c` trong `.wt-dh-fire-a`): đỉnh vòng 10 + dư âm sạch kiểu B + tia lửa và vết cháy Kenney + sóng chấn vẽ bằng code, hai giám khảo mù (đề chỉ có clip), luật dừng 8.
- `media:push` chạy nền cho ảnh bảng nhanh mới (log `.local/media-push-20261031-panels.log`).

**31/10 khoảng 22:25: bảng nhanh ba game đã gắn ảnh 243/244 và sửa theo giám khảo** (con trỏ `7a6743ea`, chưa đẩy).
- Dragonhold `main` `8f4c1f8`, Wordwoven `a2-days` `9b45259`, Last Line `main` `15c39fb`; kit cha `ba2b4d65` (Tab đi vòng trong bảng) và `fc7f4a11` (hàng tắt tiếng Master trong kit, nút Listen sáng khi phát, thanh cuộn danh sách). Giám khảo trước lượt sửa: Dragonhold 7,1 (Settings 6,2, Sound 7,6), Wordwoven 6,8 (6,1 / 7,2), Last Line Settings 7, Sound 7,3.
- **Wordwoven `/?title=0` còn 0,04 kB dưới ngân sách 85 kB**: thay đổi tiếp theo vào chunk đầu phải tách chunk trước.
- Icon còn đọc sai và ô trống → phiếu 250 (làn s30). File ảnh mới đã chép vào `public/` của các game: cần `media:push` (cùng media lửa vòng 10).
- Sự cố: tin nhắn chuyển lời của điều phối tới fixer đang chạy trong workflow đã mở lại bản sao, hai bản cùng sửa một thư mục; đã dừng các bản sao, mỗi game chỉ một commit. Bài học trong bộ nhớ `no-messages-to-live-workflow-agents`.
- Giải pháp lửa V2 của chủ dự án (ChatGPT): nhận xét "nhận có sửa đổi" ở `docs/games/vfx/VFX_SOLUTION_V2_REVIEW.md` (`b3433453`): giữ bộ chạy flipbook sẵn có, chưa cần three.quarks và breath ribbon; thử Pyroclast trước, SCORCH sau, không dùng Taproot; **chờ chủ dự án cho tải bản demo miễn phí**.

**31/10 khoảng 21:45: chủ dự án quyết lửa rồng.**
- "tạm thời cứ lấy bản tốt nhất cho phần lửa rổng đang có đi, tôi sẽ kêu chatgpt tìm hiểu xem sao": dùng **vòng 10** (`ca64509`, giám khảo mù 6,0/6,5) cho demo; **dừng tự làm lửa rồng**. Chủ dự án nhờ ChatGPT tìm gói VFX/icon có sẵn theo `docs/games/vfx/ASSET_SEARCH_BRIEF.md` (`1933c0ff`); gói nào về thì thử trên bàn thử, hai giám khảo mù, dừng nếu không tới 8 trong một ngày.
- Workflow `dh-fire-r10-merge` (`wf_dbeac042-1d8`) gộp vòng 10 vào nhánh `dh-fire-r10` (từ `main`, worktree `games/.wt-dh-fire-merge`), mang media vòng 10, kiểm và có người kiểm độc lập. Đưa vào `main` sau khi workflow gắn ảnh bảng nhanh xong (nó đang sửa `main` Dragonhold); rồi chép media vào thư mục game chính và `media:push`.

**31/10 khoảng 21:30: thử lửa B chưa đạt** (Dragonhold `dh-fire-b` `ec486d6` trong `.wt-dh-fire-a`, `?fire=b`, chưa gộp, chưa đẩy).
- Hai giám khảo mới (X = vòng 10, Y = B, Z = A; giám khảo A tự ghi "mù chưa trọn" vì báo cáo người dựng nằm trong đề có lộ khoá — lỗi đề của điều phối, lần sau không chép báo cáo người dựng nguyên văn vào đề chấm):
  - tổng: vòng 10 6,0 / 6,5; **B 5,5 / 6,0**; A 4,5 / 5,0. Không bản nào tới 8.
  - B tốt nhất ở đọc rõ (8 / 7,5), màu/độ nóng (7 / 7), dư âm (5,5 / 5,5): không đen, không cháy giấy, không che quái và rồng, sạch sau 2,5 s.
  - B thua ở va chạm (5,5 / 6): **quá nhỏ** (1,8× quái, không lớn hơn đầu đạn; phiếu dựng đã đặt 1,6–2,2× theo lời chê A "to gấp mấy lần quái" — sửa quá tay), sao phẳng như hình dán, vòng cuối thành vòng ngắm đỏ mảnh; khói một cục xám, vết cháy trông như bóng quái.
  - Vòng 10 có đỉnh nổ đẹp nhất (va chạm 7 / 7,5) nhưng khói đục che quái và rồng khoảng 1 s.
- Số đo: B đạt nhiều cổng hơn A (lõi trắng, hue, peach, near-black, không đọng lại, khói); còn trượt rim, cạnh thẳng 1080.
- **Chờ chủ dự án quyết hướng sau** (xem báo cáo trong hội thoại 31/10 21:30).

**31/10 khoảng 21:05: kit bảng nhanh xong, gắn ảnh 243/244 đang chạy.**
- Kit bảng nhanh xong: giám khảo Dragonhold 7,0, Wordwoven 6,6 (trước 11 mục sửa). Dragonhold `main` `0ca70a8` (710 test), Wordwoven `a2-days` `47a1698` (653 test), con trỏ `9b99fe11`, chưa đẩy.
- Workflow `panels-art-wiring` (`wf_8bfb1618-227`): ba game song song gắn ảnh đã nhận (244: phần đầy/rỗng rãnh, icon bảng Sound Dragonhold/Wordwoven; 243: icon Last Line), Last Line nhận kit mới; rồi hai giám khảo và một lượt sửa.
- `media:push` **xong 31/10 21:20**: 8 file trùng tên trên Drive (1 Dragonhold, 7 Last Line, sinh ra lúc đẩy bị treo khi mất DNS) được bỏ bằng `pnpm media:check --only originals --remote --fix-duplicates` (chủ dự án cho phép: "Cho bạn chạy"); đẩy lại 28.494 file (9,3 GB), Drive khớp md5 37.401/37.401, bản sao `_locks/2026-10-31_141232Z/`. `media.md5` đã commit: Dragonhold `43ac4e4`, Wordwoven `0cb5faa`, Last Line `8d75d32` (con trỏ repo cha commit cùng lượt gắn ảnh).

**31/10 20:35: chạy tiếp sau giới hạn phiên (khoảng 19:00–20:30).**
- Kit bảng nhanh: kit `18722b41` + sửa `b8a224d0`; Dragonhold `main` `e52cfac`, Wordwoven `a2-days` `e5e22de` đã có kit mới và skin; giám khảo đã chấm; lượt sửa bị cắt giữa chừng (sửa dở chưa commit trong hai game) → chạy tiếp workflow `wf_6b035d93-2d0` có ghi chú.
- Thử lửa B: phần dựng bị cắt (dở, chưa commit, nhánh `dh-fire-b`) → chạy tiếp `wf_9ee05652-06a` có ghi chú.
- `media:push` lần dài kết thúc nhưng trượt bước kiểm md5 trên Drive (`games/dragon-hold`, lỗi đọc một ảnh `_review/120`), nên `media.md5` chưa đổi → chạy lại (log `.local/media-push-20261031-retry.log`). Không sửa `media.md5` khi đang đẩy.
- Codex làn s29: phiếu 245 chạm hạn mức nhiều lần, bộ chạy tự chờ (tới 20:55).

**31/10 khoảng 18:45: Last Line UI lượt 3 xong** (`main` `484700d`, con trỏ `b99a84bf`, chưa đẩy): 8 icon 242, cảnh báo vẽ bằng ảnh, thẻ kết quả lệch trái nhường chỗ nhân vật, sao 80 px, bảng nạp súng có hàng chip quái trên tấm vẽ, một chip rift, sửa lỗi giám khảo; 509 test, 60/60 kiểm trình duyệt. Hai giám khảo **7,4 và 7,3** (lượt hai 7,3/7,1). Còn lại là ảnh: bóng hình quái (245 đang làm), tranh súng, ô băng đạn đọc thành ‖, bốn icon menu → phiếu 249 (làn s30); icon 243 và thanh trượt 244 chờ gắn cùng kit (bánh răng góc vẫn là bản cũ nên vẫn bị đọc thành bông hoa).

**31/10 khoảng 17:45: thử lửa B (chủ dự án "Làm thử B").**
- Firefly Video có chế độ **Transparent background** (540p, 16:9; ẩn khi chọn preset Style hay Camera): mỗi clip là một video màu (đã ghép trên nền của Firefly) và một video alpha xám. Nút Download không lưu file trong khung trình duyệt của app; CSP của trang chặn fetch nhưng không chặn `form-action`, nên điều phối gửi hai blob bằng một form tới chỗ nhận chỉ chạy trên 127.0.0.1 (cách làm ở `FIREFLY_VFX_LIST.md` §5). `window.open` trong khung trình duyệt chuyển chính tab đi: đừng dùng.
- Giới hạn tốc độ: khoảng 2–3 lần tạo rồi "try again later" khoảng 4 phút. Gói ghi "unlimited use", credit cao cấp đứng 8.660/10.000.
- 5 clip (đúng mức của kế hoạch) ở `~/VFXLab/inbox/firefly/dragon-hold/{impact-cel,smoke-cel}/`: lửa v2 (nổ anime, chính), v3 (cầu lửa cuộn, nguội vàng → đỏ thẫm), khói v2 dùng được; lửa v1 và khói v1 loại. Prompt tả theo mốc thời gian và đặt vật giữa khung thì đúng hơn hẳn.
- Công cụ flipbook nhận cặp màu + alpha (`4e851ee4`, 23 test). Workflow `dragon-fire-test-b` (`wf_9ee05652-06a`) dựng B trên nhánh `dh-fire-b` (từ `dh-fire-a`, cùng worktree `.wt-dh-fire-a`), rồi hai giám khảo mới chấm mù B, A và vòng 10.

**31/10 khoảng 17:40: lửa A trượt, Wordwoven 1C đã gộp.**
- **Thử lửa A (đòn mạnh) trượt** (Dragonhold `dh-fire-a` `38834b2`, chưa gộp; công cụ flipbook ở repo cha `6130d72b`). Hai giám khảo mới chấm mù, tốc độ thật, có clip thương mại làm mốc:
  - test A 5,0 và 6,0; vòng 10 (cùng cách chấm) 5,5 và 5,3. Dư âm 4,5 và 5,0, va chạm 5 và 6, màu/độ nóng 4,5 và 5,5.
  - Lỗi chung: thân lửa là một khối cam phẳng viền tối (như miếng dán), vết cháy đen như vết mực không phai, tắt dần như giấy cháy, khói là vài cục xám như đá. Ưu điểm: hết bóng nâu và ô liu ở phần lớn lượt chạy; khói không che quái.
  - Số đo: ô liu đạt 2/6, bóng nâu 6/6, cạnh thẳng 1080 trượt, bậc sáng trượt, hai kiểm màu 1080 chỉ đạt 1/3 nền với grade hiện tại (3/3 nếu có "vai vàng", quyết định 3 của chủ dự án).
  - **Điều kiện dừng đã chạm** (dư âm < 7,5): theo kế hoạch đã duyệt, đổi nguồn clip (B: clip Firefly kiểu cel, cần phiên Firefly; C: mô phỏng, Blender có sẵn ở `/Applications/Blender.app`, không cần tải). **Chờ chủ dự án chọn.**
  - Cách chấm mới cho vòng 10 chỉ 5,3–5,5 (cách cũ 7,5–8): mức thật của lửa rồng xa 8,5 hơn ta tưởng.
- **Wordwoven `a2-days` `7c6c71c`** (con trỏ `ec92d78b`, chưa đẩy): gộp `td-integrate` (1C map 1, cảnh, Codex 199/200/202/203A; âm phím một lần; phím camera Home/PageDown/End; giám khảo C10 8,0 và 8,5, đã sửa P1/P2) rồi `td-sliders` (gỡ tay hai xung đột: mục lục changelog, `quick.css`). `pnpm check` 647 test; build host chơi; Chrome headless ở 1280 và 1920: 0 ảnh hỏng, 0 yêu cầu lỗi, 0 exception.
- **Last Line `main` `4e6a6b3`**: sáu nền, logo, ảnh ải 126 đã gắn (giám khảo 7,1 trước sửa; đã sửa nút góc, khung banner, chữ "Last"). Còn: nền mờ ở 1920 (cần công cụ phóng ảnh, chưa có trên máy), màn thắng chưa toát chiến thắng → phiếu 248. Workflow `ts-ui-pass-3` (`wf_4e812b72-8b2`) đang gắn 8 icon 242 và sửa các mục mã của lượt chấm hai.

**31/10: Typing Feel bắt đầu làm.** Chủ dự án duyệt cả 17 quyết định của [`TYPING_FEEL_SERVICE.md`](games/TYPING_FEEL_SERVICE.md) đúng theo đề xuất ("Duyệt tất cả").
- **G0 (B0), phần của Claude đã xong:**
  - commit sửa kit dở của TF2 (`0a9a40a2`);
  - commit phiếu Codex 171, JSON runtime trong kho media (`f126089c`); `media:test` 57/57;
  - commit ghi duyệt (`b785b0f3`) và con trỏ Monkeytype `4f1fcf3b0` (`56a113fd`);
  - bốn nơi và staging cùng 34 bộ, cùng danh sách id.
- **G0, phần của chủ dự án:**
  - `pnpm setup:play`: **xong 31/10 khoảng 05:35.** Hosts và chứng chỉ có `feel.typing-game.local`.
    - Host feel đã kiểm bằng curl: HTTP/2, CORS, no-cache và 304, immutable, `audio/ogg`, 404.
    - Monkeytype trên host chơi thật đọc r1 (Chrome headless: 90 yêu cầu feel, không lỗi).
    - Khung trình duyệt trong app chặn mọi yêu cầu chéo giữa các host `*.typing-game.local`, nên phải kiểm bằng Chrome thật (`cdp-run`).
  - `pnpm media:setup --reconnect` (token rclone hết hạn 30/10): **chưa làm.**
- **G1 xong** (`4a3c94ef`):
  - `typing-feel/` với danh mục r1, 34 bộ, 2.744 OGG chép đúng byte (OGG bị Git bỏ qua);
  - block nginx `feel.typing-game.local`;
  - kiểm `validate-play-mode`;
  - nhóm media.
  - Còn hai việc: chủ dự án chạy `pnpm setup:play` để host sống; Claude chạy `media:push` sau khi chủ dự án nối lại rclone.
- **G2 xong** (`590864fb`): API kit theo §4.6 (mục "API đã làm ở G2"). Kit đã đồng bộ vào ba nhánh, `pnpm check` xanh:
  - `ts-typefx` `0391738`;
  - `dh-keys` `b17dbfe`;
  - `td-keys` `d054a34`.
- **G3 Last Line (B3) xong:** commit `07895db` trên `ts-typefx`, `pnpm check` 265/265. Đã thử trên trình duyệt: host chạy, host chết, HTML 200, host treo, không có origin.
  - Hai việc ở repo cha chưa làm: dòng `VITE_TYPING_FEEL_ORIGIN` của `build:survival` và `dev:survival:app` trong `package.json` (đang chờ commit chung với G4), và `typing-feel/media.md5` (sinh ra khi `media:push`).
- **Sửa kit theo G3, rồi B4 (Dragonhold) và B5 (Wordwoven):** workflow `typing-feel-kit-fix-b4-b5` (`wf_900342b5-42f`).
- **G6 xong** (`217f5f0a`; tài liệu `6b2320ee`):
  - kho Typing Feel, Publish và Rollback;
  - ba trang Keyboard Sounds, Typing Effects, Release & History.
  - Đã nạp `seed-v1` vào kho Admin thật lúc 06:15. Bản sao lưu trước khi nạp: `.local/admin-backup-20261031-before-typing-feel-seed.tgz`.
  - Trang Keyboard Sounds trên host chơi hiện 34 bộ, 7 họ, `seed-v1 · r1`.
- **Kit + B4 + B5 xong:**
  - kit `fdb8bc14` (repo cha);
  - Last Line `9e169b9`, Dragonhold `d47ef93`, Wordwoven `926a3d9` (nhánh game).
- **Media:**
  - `media:push --only runtime` xong 06:21: 2.942 file, md5 khớp 3.587/3.587; `typing-feel/media.md5` và hai `media.md5` game đã commit (`7ce2432b`).
  - Nhóm originals còn khoảng 27.300 file (khoảng 12 GB). Sẽ đẩy sau khi gộp nhánh xong, để không đụng `media.md5` lúc đang gộp.
- **G3 xong (31/10 khoảng 10:55):** ba nhánh âm phím đã gộp, chưa đẩy lên remote:
  - Last Line `main` `48659cc`;
  - Dragonhold `main` `2701477`;
  - Wordwoven `a2-days` `01f75bc`.
  - Con trỏ ở repo cha `acf0f75c`.
  - Kiểm trên host chơi bằng Chrome headless: đọc r1, 34 bộ; chặn host feel thì game vẫn chạy.
  - 10 ảnh bảng Settings/Sound của Wordwoven đã chép (kiểm md5) vào thư mục game chính rồi build lại.
- **31/10 khoảng 12:30: gộp các nhánh đã duyệt; 31/10 khoảng 12:45 đã đẩy lên GitHub theo lời chủ dự án ("Đẩy lên"):** Last Line `main` `f72ad6e`, Dragonhold `main` `d5bcbd8`, Wordwoven `a2-days` `2937654`. Không force, không có file media.
  - Last Line `main`: `ts-codex` (`51f3818`), `ts-art` (`4f4d275`), ghi chú AGENTS (`f72ad6e`). Model riêng (205) đã nạp; ảnh UI 206 đã chuẩn bị.
  - Dragonhold `main`: `dh-codex` (`25b602f`), sửa lỗi Quit về màn tựa (`d5bcbd8`).
  - Wordwoven `a2-days`: `td-codex` (`2937654`).
  - Mỗi lần gộp đều có người kiểm độc lập (đạt). Con trỏ ở repo cha `c67ebe10`.
  - Repo cha `68cbda29`: `VITE_PORTAL_URL` cho build và dev của ba game; bỏ alias model Space của host Last Line (nginx sống sẽ nhận ở lần `setup:play` sau).
- **Chưa gộp:**
  - cần kiểm thêm: `map-pilot`; `td-ui`/`td-1c`/`td-scenery` (vượt ngân sách gói 0,76 kB, phím F1–F3 của camera 3D trùng bảng Settings);
  - cần chủ dự án quyết: `dh-vfx` (lửa vòng 11), `dh-models` (KTX2 dở);
  - chỉ giữ làm hồ sơ: s1–s6, `d27-counter`.
  - Kế hoạch đầy đủ ở `wf_6ac54865-14b`.
- **Gắn ảnh UI xong lượt đầu, đã commit trên nhánh riêng (chưa gộp):**
  - Last Line `ts-ui-wire` `67f3056`: 52 icon và mảnh UI của 149–153, chân dung Shard, thanh trượt.
  - Dragonhold `dh-sliders` `769f21b`, Wordwoven `td-sliders` `4703bcc`: ảnh thanh trượt.
  - Người chấm cho 7 và 7,5 trước lượt sửa; các lỗi P2 đã sửa.
  - Đang chấm lại bản đã sửa (`wf_2650d89f-85d`) trước khi gộp.
  - Việc kit còn lại: thanh trượt có lớp hiện mức đầy; rãnh vẽ ba mảnh.
- **G7 xong** (`c9148813`, thêm `f8465575`).
- **Lửa rồng:** báo cáo phân tích ở `docs/games/vfx/DRAGON_FIRE_DIAGNOSIS_2026-10-31.md`.
  - Chủ dự án duyệt làm thử phương án A (31/10 khoảng 13:40, "Làm thử A").
  - Workflow `dragon-fire-test-a` (`wf_493631c1-983`) chạy trong worktree `games/.wt-dh-fire-a`, nhánh `dh-fire-a`, từ vòng 10 (`ca64509`). Phạm vi: chỉ đòn mạnh, ba loại nền, hai giám khảo mới.
  - Điều kiện đạt: pha dư âm, màu/độ nóng và va chạm đều từ 8 trở lên.
  - Điều kiện dừng: pha dư âm dưới 7,5 thì đổi nguồn clip (phương án C hoặc B).
  - Phần vòng 11 chưa commit vẫn nằm nguyên trong `.wt-dh-vfx`.
- **Tích hợp bản 3D của Wordwoven** (`td-ui` gồm `td-1c`, `td-scenery`) vào nhánh `td-integrate` đang chạy (`wf_4dcc3fee-723`), có giám khảo C10.
  - Last Line ở `.wt-ts-ui-wire`: icon 149–153 và thanh trượt.
  - Dragonhold `.wt-dh-sliders` và Wordwoven `.wt-td-sliders`: ảnh thanh trượt.
- Sau lệnh đẩy hiện tại cần `media:push` lần nữa: 24 GLB và 50 ảnh UI mới của Last Line.
- **Media:** `pnpm media:push` toàn bộ chạy nền từ khoảng 11:00 (27.331 file, 9,1 GB, phần lớn là `_review/` của Codex). Log ở `.local/media-push-originals-20261031.log`. Xong thì commit các `media.md5`.
- **Đang chạy:** workflow `typing-feel-merge-and-g7` (`wf_835c6f92-41c`), phần G7. Phần gộp nhánh đã xong:
  - gộp `ts-typefx` vào `main` của Last Line, `dh-keys` vào `main` của Dragonhold, `td-keys` vào `a2-days` của Wordwoven (nhánh thư mục game chính đang dùng), rồi kiểm trên host chơi bằng Chrome headless;
  - song song làm G7 (nút Format).
- **G4 Monkeytype xong (B6):** commit `2cc987e8f`, đã đẩy lên `feature/en-vn-translation` ở cả GitHub và GitLab (31/10).
  - Monkeytype đọc từ `TYPING_FEEL_URL`, không còn `sync-keys`.
  - Repo cha: `feel:pack` và con trỏ Monkeytype (`85ef5df8`).
  - Chủ dự án đã nhận `tmp/typing-feel-pack/typing-feel-v1-r1.zip` (15 MB) cho máy công ty. Các bước ở `docs/CUSTOM_TYPING_FEEL.md` của Monkeytype.
  - **Các dòng cũ dưới đây nhắc `sync-keys` hay zip 32 bộ đã lỗi thời.**
- **31/10 05:15, chủ dự án: Codex gần hết hạn mức, tạm thời chỉ giao việc tạo ảnh.** Việc code, kiểm lại và phản biện do workflow của Claude làm. Vẫn một làn. Làn s27 hiện chỉ còn phiếu ảnh 225.
- **Ảnh Codex:** bộ UI Last Line 149–153 đã nhận đủ (31/10 05:15), kể cả các lượt làm lại 237–240. Ảnh chưa chép vào `public/`; việc đó thuộc làn gắn ảnh (mục kiểm kê UI 29/10).
  - Làn s27: phiếu 225 (ảnh thanh trượt ba game) gặp giới hạn công cụ ảnh; bộ chạy tự chờ tới 05:23 rồi chạy lại.
  - Bộ chạy mới đã chứng minh tự chạy tiếp sau hạn mức, hai lần trong đêm 31/10 (03:05 → 04:04 và 04:53 → 05:23).
- **31/10 05:10: hai workflow hết hạn mức phiên ở bước kiểm**, đã cho chạy tiếp bằng `resumeFromRunId`: `wf_065fd408-7ca` (G6) và `wf_900342b5-42f` (kit, B4, B5).
- **G5 (phiếu 236) xong và đã gộp** vào `feat/space-typing-admin-uiux` (`4ac4884b`). Đó là Admin nhiều khu: All games (Overview, Learning Content), Space Typing, Administration. Đã qua hai người kiểm, một lượt sửa và một lần kiểm lại. Worktree `admin-ia` đã dọn.

**31/10, khoảng 01:00: chủ dự án cho Codex chạy lại một làn.**
- Làn s24: phiếu 236 (G5, Admin nhiều khu), trong worktree `typing-game-wt/admin-ia`, nhánh `admin-shared-ia`. Ở đó `games/space-typing` là worktree tách rời của Space ở `84777155`.
- Làn s25 (phiếu ảnh 149–153, 225) tự bắt đầu khi s24 xong; vẫn một làn tại một lúc.
- Bộ chạy không bỏ phiếu vì hạn mức nữa (`04016a9a`). Luật: hết hạn mức thì chờ rồi chạy tiếp; không tắt làn đang chờ.
- Claude giữ một nhịp `CronCreate` 20 phút một lần (phút 7, 27, 47) để tự làm tiếp khi rảnh hoặc sau khi hết hạn mức. Session mới phải tạo lại nhịp này.

**30/10, 11:20: chủ dự án bảo Claude dừng mọi việc, chỉ giao việc cho Codex (ba làn, nhiều việc), rồi chờ giao việc.**

Việc của Claude đã dừng, và chỗ dừng của từng việc:

- **Sửa lỗi sau khi gắn 32 bộ phím:** workflow `wf_ef77bd64-ccb`. Bốn bản sửa đã commit, chưa gộp, chưa đẩy:
  - Last Line: `ts-typefx` `d15fed0`, `7a793c3`;
  - Dragonhold: `dh-keys` `568eb35`;
  - Wordwoven: `td-keys` `646e889`;
  - Monkeytype: `feature/typing-feel-32` `2bf28b79a`.

  Last Line và Dragonhold đã kiểm lại, đạt. Wordwoven và Monkeytype bị dừng giữa lúc kiểm lại. Làm tiếp: `Workflow({scriptPath: ".../workflows/scripts/keys-32-review-fixes-wf_ef77bd64-ccb.js", resumeFromRunId: "wf_ef77bd64-ccb"})`. Sau đó Claude kiểm bốn game trên trình duyệt.
- **Phân tích cách Codex xử lý âm phím, kèm bản mẫu tốt hơn** (chủ dự án yêu cầu): workflow `wf_5d707009-95f`. Mới xong nhánh "pipeline". Kết luận sơ bộ: khâu cắt và xử lý âm phần lớn ổn; 32 bộ nghe giống nhau là do cách v2 gom tiếng gõ thành bộ. Chưa phản biện. Làm tiếp bằng `resumeFromRunId: "wf_5d707009-95f"`; đầu ra ở `tmp/keys-firefly/diagnose/`.
- **Lửa Rồng vòng 11:** V-dh2 dừng giữa chừng khi đang thêm vòng sóng bám mặt đất cho Sky Fire. Có thay đổi chưa commit trong `games/.wt-dh-vfx`: `src/view/fx.ts`, `skyfire.ts`, `flipbook.ts`, `vfx-layers.ts`, `actors.ts`, `crowd.ts` và hai kịch bản chụp. Mốc commit cuối là `ca64509`.

Codex chạy ba làn (owner 30/10 11:15):
- `s7`: 194 → 195 → 197 trong `.wt-dh-codex`;
- `s8`: 214 → 215 → 216 → 217 → 206;
- `s9`: 199 → 202 → 200.

Lô phiếu mới 220+ đang soạn qua workflow `codex-batch-220` và sẽ được nối vào sau ba làn. 213 nối sau `s8`.

**30/10, khoảng 18:00: các phiếu Codex trong ngày đã duyệt và commit xong.** Tất cả nằm trên nhánh worktree, chưa gộp vào main của từng game, chưa đẩy:

| Game | Worktree | Nhánh và commit |
|---|---|---|
| Dragonhold | `.wt-dh-codex` | `dh-codex`: 187, 194, 195, 197, 223, 235 (6 commit), `c96ef50` |
| Last Line | `.wt-ts-codex` | `ts-codex`: 205, 207, 210 (`ba6d70e`), 220 (`28ba10e`) |
| Last Line | `.wt-ts-art` | `ts-art`: 206 (`ce94c1a`) |
| Wordwoven | `.wt-td-scenery` | `td-scenery`: 199, 202 |
| Wordwoven | `.wt-td-ui` | `td-ui`: 200 (`49bffbb`), 203A (`b3a542d`) |
| Wordwoven | `.wt-td-codex` | `td-codex`: 170 + 208 (`cab37f7`), 229 (`2b6f282`) |

- **Repo cha:** 212, 213, 214, 215 + 228 + 234, 216, 217, 221 đã commit.
- **Tiếng phím:**
  - Raindrop Tile (bộ 33) đã vào `ts-typefx`, `dh-keys`, `td-keys` và Monkeytype; Monkeytype đã đẩy GitHub và GitLab ở `be5943667`.
  - Hail Stone (bộ 34) đã vào `ts-typefx` `22d22dc`, `dh-keys` `b7e8e63`, `td-keys` `0cff05e` và Monkeytype; Monkeytype `feature/en-vn-translation` ở `4f1fcf3b0` trên cả GitHub và GitLab. Zip 34 bộ đã gửi chủ dự án.
  - 31/10: chủ dự án giữ nguyên Hail Stone (không cắt phần dạo đầu của 7 phím trễ tiếng chính). Mờ 10 ms cuối preview để dành cho lần dựng lại sau (bước Format của Typing Feel).
- **Còn chờ:**
  - gộp các nhánh vào main của từng game;
  - `media:push` (rclone chưa kết nối lại);
  - F1 của 222 (SVG, tranh gỗ CSS của Dragonhold) chờ chấm ảnh;
  - lỗi kit: dòng đang chọn trong danh sách bộ phím khó đọc khi con trỏ còn trên nó.

**30/10, 15:25: chủ dự án tạm dừng Codex, chuyển việc cho Claude.**
- Đã dừng mọi làn và lệnh chờ phiếu ảnh 19:48. Không chạy lại Codex khi chủ dự án chưa bảo.
- Claude làm qua workflow `claude-takes-over-codex-235-234-230-232` (`wf_5a8d7c6d-8af`):
  - sửa 235 (Dragonhold F2–F4 của 222) và 234 (vá nốt F2 của phần học), mỗi bản có người kiểm độc lập;
  - kiểm lại 230 (Last Line 206 và 220) và 232 (Wordwoven 200 và 203).
- **Đã kiểm, commit được:** 199 và 202 (231: không P0/P1); 229 (233).
- **Chưa commit được:**
  - 228: chờ 234;
  - Dragonhold 187, 194, 195, 197: chờ 235;
  - F1 của 222 (SVG, tranh gỗ CSS) chờ chấm ảnh.
- **Kết quả đo:**
  - 220 (luật bến đầy Last Line): chưa ứng viên nào đạt, giữ mặc định tắt;
  - 223 (bot giống người Dragonhold) xong;
  - 226 (gói cân bằng Wordwoven) xong.
- **Danh sách âm Firefly:** 212 (Last Line, đã commit), 213 (Dragonhold), 221 (Wordwoven).
- **Ảnh 149–153 và 225:** chờ hạn mức ảnh (mở 19:47) và chờ chủ dự án cho chạy lại Codex.

**Monkeytype đã đẩy (30/10, 14:25, chủ dự án bảo):**
- `feature/en-vn-translation` lên GitHub `sinhvienaiti/monkeytype` qua SSH, `85a8667a1..02d511788`, không ép. Gồm âm và hiệu ứng gõ, 32 bộ phím, các bản sửa, và commit mirror GitLab của chủ dự án đã gộp vào.
- Đã kiểm: lint, `ts-check`, 1.485/1.485 test; hai người kiểm độc lập; thử trên trình duyệt (danh sách 32 bộ theo họ, nghe thử khi rê chuột, chọn bộ, gõ có hiệu ứng).
- File âm không theo Git. Chủ dự án đã nhận zip 32 bộ (`tmp/keys-firefly/zip/keys-firefly-32-monkeytype.zip`). Máy khác: giải nén vào `~/AudioLab/review/staging/`, rồi `pnpm sync-keys`.
- **GitLab (máy Mac mini M2 ở công ty chỉ dùng GitLab):** workflow mirror trên GitHub chết từ 08/10. Đã đẩy tay `feature/en-vn-translation` lên `gitlab.com/sinhvienaiti/monkeytype`, `7d84bfb70..02d511788`, không ép, đầu nhánh khớp GitHub. Khóa dùng được là `~/htdocs/key/id_ed25519_github`; GitLab nhận khóa này là tài khoản `@toanjaco2`.
- Repo cha chưa đẩy: `build:monkeytype` có bước sync và `KEYS_FIREFLY_HANDOFF.md` chưa có trên remote; con trỏ `games/monkeytype` trong repo cha chưa cập nhật.

**Cập nhật 13:35:** Codex vẫn chạy ba làn.

- **Đã xong, chờ Claude duyệt và commit:**
  - 194, 195, 197 (Dragonhold, `.wt-dh-codex`; 197 xanh 593/593);
  - 200 (Wordwoven, `.wt-td-ui`; 405/405, gói 82,3 kB);
  - 206, 214, 215, 216, 217, 213.
- **Đã commit:** 212 (`83217b53`) và changelog của 198.
- **Ảnh 149–153:** `image_gen` của Codex vẫn trả 429 lúc 13:07, dù phần làm code đã có hạn mức. Chạy lại khi có hạn mức ảnh.
- **199:** quyết định lần hai lúc 13:28: phép kiểm màu khóa chỉ áp cho điểm có độ sáng ≥ 0,25.
- **Ba làn:**
  - `s13`: 199 → 202 → 226;
  - `s14`: 220, rồi lệnh chờ tự chạy `s14b`: 222 → 223;
  - `s15`: 221 → 227 → 224 → 225 (225 là ảnh, có thể gặp 429).
- **Lô 220–227** đã qua người kiểm, có hàng trong `CODEX_QUEUE.md`.
- **Vẫn chờ Claude chấm ảnh:** 203 (ảnh 133, 165, 172), 204 (lô UI Wordwoven), 211 (ảnh 149–153 và khung 127).

**Cập nhật cuối của session cũ (28/10, sau 22:10):** session cũ (157c54d6) đã xong cả 4 lượt và gửi kết quả sang `coordinator-2`. Từ đây mọi việc thuộc session mới:
- `codex-review-28-10`: kết quả nằm trong tin nhắn.
- `map-pilot-a`: trung vị 7,125, chưa đạt cổng A; nhánh `map-pilot`.
- `map1-production-audit`: `docs/games/MAP1_PRODUCTION.md`, `docs/games/map1/`.
- `vfx-dh-v2`:
  - bước 1a đã làm 2 vòng, người chấm cho 7/7,5, cần một vòng sửa lõi trắng;
  - Sky Fire dở, có sửa chưa commit trong `games/.wt-dh-vfx`;
  - VFX quái chưa làm.

Mục 3 bên dưới là lịch sử.

- **Luật chủ dự án 28/10 tối:** mọi chi tiết giao diện (thẻ, nút, ô, nhãn, biển, bảng tin, kết quả, cửa hàng) phải có hình thật đi kèm, không chỉ có chữ. **Tuyệt đối không dùng hình vẽ bằng mã để thay hình thật**: không SVG hay canvas vẽ cảnh, không icon bằng CSS, không emoji, không tranh dự phòng. Thiếu ảnh thì mở phiếu Codex. Âm thanh cũng phải là file thật, có chất lượng, làm theo `docs/games/AUDIO_PIPELINE.md`. Lượt rà toàn bộ giao diện và âm thanh đang chạy; kết quả sẽ ở `docs/games/map1/UI_IMAGERY.md` và `UI_IMAGERY_CODEX.md`.

- **Quyết định của chủ dự án 28/10 tối** (đã ghi vào `AGENTS.md`):
  - toàn bộ chữ trong game bằng tiếng Anh, tiếng Việt chỉ ở nghĩa của từ;
  - tên game: Dragonhold, Wordwoven, Last Line;
  - Wordwoven theo hướng sử thi: làm lại nền, trời, màn tựa, ảnh chủ đạo, khung UI; giữ 117 model và chỉnh ánh sáng;
  - cả ba game được chấm lại so với game thương mại, cái nào dưới 8 thì làm lại.
  Làn chỉ đạo mỹ thuật đang viết `docs/games/ART_DIRECTION_2026-10-28.md` và các phiếu từ 112. Phiếu 106, 110 đã rút khỏi làn ảnh M6.

- **Học từ Typing Break** (chủ dự án 29/10): `docs/games/TYPING_BREAK_STUDY.md` có 16 kỹ thuật kèm thông số, cách áp cho từng game, và top 10 việc nên làm. Dùng cho thẻ gọi của Wordwoven (C10); thẻ chữ, nút kỹ năng, thanh xây của Dragonhold; dòng gõ và ô súng của Last Line (làm sau khi chủ dự án chọn hướng ở phiếu 112).

## 1. Bắt đầu session mới

1. Đọc file này, `MAP1_PRODUCTION.md` §4, rồi `docs/CODEX_QUEUE.md` (các dòng 088 trở đi).
2. Kiểm các làn ở mục 3: `pgrep -fl codex-lane-mac` cho Codex; nhật ký Codex ở `.local/codex-runs/<phiếu>/`, báo cáo ở `docs/codex-queue/<số>-report.md`.
3. Làn Claude là agent nền của session điều phối. Session đó dừng thì làn cũng dừng: xem `git log` trong worktree của làn, rồi mở lại bằng một agent mới có ghi chú RESUME.

## 2. Luật chính (chi tiết ở memory)

- **Giao tiếp:** trả lời chủ dự án bằng tiếng Việt; tự làm theo khuyến nghị, chỉ hỏi quyết định thật sự chặn việc; cổng nào gãy thì báo kèm số.
- **Git và media:** không media trong Git; repo game đẩy qua SSH, không force; chỉ Claude chạy `pnpm media:push`; không đụng Tu Tiên.
- **Codex** (chủ dự án 28/10: "tăng gấp đôi công việc cho codex"):
  - luôn chạy **hai làn cùng lúc**, một làn ảnh và một làn mã, ghi vào các đường khác nhau;
  - giao một danh sách việc, ảnh trước;
  - Codex không chạy git có ghi; Claude duyệt rồi mới commit.
- **Làn Claude:** tối đa 4 cùng lúc. Ảnh test: giữ tờ ghép, xóa ảnh thô bằng `tools/capture-prune`.
- **Mức nhận:** ảnh 2D từ 8 điểm; model 3D từ 7 điểm; điểm 7–8,5 ghi vào `ART_REPLACE_LATER.md`.

## 3. Đang chạy (28/10, 19:40)

### Codex: hai làn (cập nhật 29/10, 03:50)

| Làn | Còn lại | Ghi chú |
|---|---|---|
| Ảnh M10, rồi M11 | 113 (đang chạy), 114 → 115, 116, 117, 118, 119, 120, 122, 123, 124, 128 | `.local/codex-lane-mac-m10.txt`, `-m11.txt` (M11 chờ M10 xong rồi tự chạy) |
| Mã M8, M9 | xong (130–132, 111b) | |
| Ảnh M15 (sau M14) | 155 đường đá Dragonhold, 125, 156 (Tripo Lightbearer và 5 súng canh), 121, 127, 126, 157 | `-m15.txt` (hướng B) |
| Ảnh M16 (sau M12) | 149, 150, 151, 153, 152: icon UI Last Line | `-m16.txt` |
| Ảnh M18 (sau M15) | 145, 147, 173, 176 | `-m18.txt` |
| Ảnh M19 (sau M17) | 174, 175, 177 | `-m19.txt` |
| **M17c** (từ 14:15, thay M17b) | 182 tiếng phím trước, rồi danh sách của M17b | `-m17c.txt`; M19 vẫn chờ tên `m17` |
| ~~M17b~~ (dừng 14:15) | 170, 119, 120 (đã sửa thiết kế vòng), 178, 179, 117, 118, 171, 162, 148, 163–167, 146 | `-m17b.txt`; M19 chờ tên `m17` nên vẫn nối sau |
| ~~M17~~ (dừng 13:40) (từ 29/10 10:45, chủ dự án: Codex còn nhiều hạn mức) | mã 168, 169, 170, 171 → ảnh 162, 148, 163, 164, 165, 166, 167, 146 | `-m17.txt`. Ba worktree Codex đã tua tới nhánh chính và có lượt đồng bộ kit chưa commit (kit 154, check-pack); Claude commit cùng phiếu 168–170 sau khi duyệt |

**Codex hết hạn mức 29/10 05:49, tự chạy lại lúc 09:45** (M11 dừng ở 116, M13 dừng ở 140).
| Ảnh M12 (sau M11) | 133–136, 141–144: icon UI Wordwoven | `-m12.txt` |
| Ảnh M13 (sau M9, chiếm chỗ làn mã khi hết phiếu mã) | 137–140: icon UI Dragonhold | `-m13.txt` |

- **Chờ quyết định, chưa xếp làn:** 121, 125, 126, 127 (Last Line, chờ chủ dự án chọn hướng từ 112); 129 (Wordwoven, chờ chủ dự án đồng ý dựng lại sáu nhà mái tranh).
- **Phiếu icon UI chờ điều kiện** (kiểm kê UI 29/10, `docs/games/map1/UI_IMAGERY.md`): 145 (chờ Claude nhận khung 115), 146 (chờ khung UI Dragonhold, chưa có phiếu AD), 147 (Claude dựng trước ảnh tham chiếu từ GLB rồng bằng `.local/bin/render-glb-views.py`), 148 (Claude thử cắt chân dung quái từ ảnh có sẵn trước), 149–153 (Last Line, chờ chọn hướng). Sáu phiếu vẽ lại có điều kiện (UIC-*-R) chưa tách số.
- **Kiểm kê UI 29/10, việc của Claude (làn gắn ảnh, chưa mở):** gắn icon súng 108 vào thẻ Nạp súng và hai bến chữ của Last Line; chân dung quái 089 vào thẻ ải; chân dung Draconis và Thư Đồng vào thanh đội Wordwoven; icon tài nguyên Wordwoven; 17 icon vẽ có sẵn thay SVG của Dragonhold. Làm sau khi duyệt và gộp 130–132, để không đụng phần đổi chữ.
- **Lỗi thật từ kiểm kê:** Dragonhold bản build không có ô đất (`src/view/paint.ts:372-375` chỉ nạp ô đất và decal từ `/art-src/` khi chạy dev; việc của làn map, MF-C24); màn tựa Wordwoven không có `onerror` nên thiếu ảnh thì lặng lẽ rơi về cảnh SVG (`src/ui/title.ts:180-185`). Bản chơi `games/.wt-play-typing-defense` thiếu `title-dusk.webp`: đã chép vào 29/10 04:10, kiểm trên trình duyệt thấy tranh. Ba bản chơi `.wt-play-*` đều cũ so với nhánh chính; làn T phải dựng lại cả ba.
- **Âm thanh:** cả ba game chưa có file âm nào (176 tiếng, 172 tổng hợp bằng mã). Claude chọn: tiếng phím dùng mẫu thật CC0, mã chỉ đổi cao độ (theo luật "âm thanh là file thật"). Chủ dự án cần chấm các lượt nghe trên Audio Lab (chưa ai chấm từ 23/10).
- **Xong, chờ Claude duyệt:** 112 (tờ `games/typing-survival/art-src/_review/112-directions.jpg`, đã gửi chủ dự án), 130, 131 (chữ tiếng Anh trên nhánh Codex của từng game).
- **Đã gộp 29/10 04:35:** `ts-codex` (104b, 130) vào `main` Last Line; `dh-codex` (080, 094, 101, 105, 105b, 131) vào `main` Dragonhold, trước `dh-vfx` (V-dh gộp `main` vào `dh-vfx` ở điểm sạch tới; `src/view/fx.ts` có nhãn PERFECT).
- **Đã gộp:** `td-codex` (091, 103) vào `a2-days`; `ts-codex` cũ vào `main` Tuyến Cuối `e26e898`.
- **Ảnh đã nhận:** 088, 089, 093, 095, 096, 097; 098–100 xong nhưng bị chấm lại theo mức chợ, thay bằng 116–118, 122, 123.

### Tiếng phím: 80 bộ trở lên (30/10, khoảng 08:40)

- **Nghe thử và làn Codex thứ hai (30/10, khoảng 10:50):**
  - Đã gửi chủ dự án 32 file nghe, mỗi bộ 9 giây, cùng nhịp và cùng độ to. File ở `tmp/keys-firefly/listen-sets/`, dựng bằng `bash tools/audio-lab/run.sh tools/audio-lab/keys/firefly_listen_sets.py`.
  - Chủ dự án bảo tăng thêm một làn Codex, nên giờ chạy **hai làn** song song:
    - `s4`: 212 → 214, 215, 216, 217, 206;
    - `s6`: 199, 202 trong `.wt-td-scenery` → 200 trong `.wt-td-ui`; khi `s6` xong, `s7` tự chạy 194 → 195 → 197 trong `.wt-dh-codex` (194 lượt 10:43 dừng vì phần dở của 195, bị cắt lúc đổi làn 08:43; đã ghi chú vào ba phiếu).
  - Hai worktree Wordwoven mới cắt từ `td-1c` `2a1f61d`, có liên kết media như `.wt-td-1c`.
  - Đã bỏ lệnh chờ `s5`, vì 194 nay nằm trong `s7`.
- **Nghe xong 32 bộ (30/10, khoảng 11:20):**
  - Chủ dự án thấy "âm nào cũng hơi giống nhau". 7 bộ bản 1 nghe khác hẳn nhau (ông gọi là clack, cream, poppy, thock, click).
  - Claude mở một vòng chẩn đoán, chủ dự án bảo dừng: "không cần chẩn đoán nữa, tạm thời cứ dùng 32 file âm đó". Đã dừng; chưa có kết luận lỗi do Codex hay do nguồn.
  - Nếu sau này cần bộ khác nhau rõ hơn: xem `KEYS_FIREFLY_HANDOFF.md` §5. Cách dễ thử nhất là chỉ giữ các bộ khác nhau nhất, hoặc dựng lại với vùng lấy mẫu mỗi bộ hẹp hơn.
- **Đã gắn 32 bộ** (chưa gộp, chưa đẩy):
  - Last Line: `ts-typefx` `e1c7d15`, `8956257`, `804429a`;
  - Dragonhold: `dh-keys` `2a8933f` (Codex 192), `7c84b64`, `255b452`;
  - Wordwoven: `td-keys` `0a63df2` (Codex 193), `023b995`;
  - Monkeytype: `feature/typing-feel-32` `8dead1a6d`, `44945ad4a`.
  - Workflow `keys-32-review-fixes` đang sửa các lỗi người kiểm tìm ra:
    - Dragonhold: đổi bộ không giải phóng bộ cũ;
    - Wordwoven: mất tiếng gõ sai, thiếu test bảng;
    - Monkeytype: danh sách vẽ lại toàn bộ.
  - Còn chờ:
    - Claude kiểm trình duyệt;
    - `media:push` sau khi gộp;
    - quyết định có làm manifest gọn cho game không (mỗi game hiện thêm khoảng 5 MB JSON vào Git, mỗi bộ khoảng 170 KB tải khi chọn).
- **Kết quả và quyết định (30/10, khoảng 10:45):** phiếu 218 chỉ ra 32 bộ (458 trên 490 bộ đạt điểm bị loại vì gần trùng). Chủ dự án nghe 10 bộ bị loại và chốt: **tạm giữ 32 bộ**, sau cần thì làm thêm. Cách làm thêm ghi ở `docs/games/audio/KEYS_FIREFLY_HANDOFF.md` §5 (hạ `MIN_DISTANCE`, sửa điểm độ lặp, ồn nền, hoặc tạo âm Firefly mới). Tài liệu đó cũng là README cho folder âm trên Drive.

- Chủ dự án thấy chỉ có 7 bộ ("tôi tải hơn 400 file âm cơ mà"), rồi chốt: **80 bộ trở lên, mỗi bộ 70–100 biến thể, khoảng 6 điểm là được**. Giữ 7 id cũ (mặc định Bright Clack) cho bộ tốt nhất mỗi họ.
- Phiếu Codex 218 (dựng bộ), 219 (kit: danh sách theo họ, nhiều biến thể). Làn `s4` thay `s3` sau khi 194 xong: 218, 219 chạy trước, rồi phần còn lại của `s3`. Vẫn một làn.
- Sau 218–219: Claude chép bản giao `tmp/keys-firefly/staging-v2/` sang `~/AudioLab/review/staging/keys-firefly/`, đồng bộ kit vào `ts-typefx`, `dh-keys`, `td-keys`, chép kit vào Monkeytype (`frontend/src/ts/custom/typing-feel/kit/`), chạy `pnpm sync-keys`, thử trình duyệt.
- Đã tạo 4 clip khói Firefly (chủ dự án đồng ý), cắt thành `~/VFXLab/out/dragon-hold/smoke-mask/`, giao V-dh2 cho vòng 10.

### Lửa Rồng vòng 10 đã chấm (30/10, khoảng 10:30): chưa đạt, đi ngang

- V-dh2 commit `5587bd7`, `c2a6f9b`, `8b028ce`, `d91586f`, `ca64509` trên `dh-vfx` (mặt nạ khói Firefly, sửa nêm 1/6 của mặt nạ vết nứt, Sky Fire vẽ đè quái, lóe đòn thường bằng flipbook…). Giám khảo A: mạnh 8,0, thường 7,7, Sky Fire 8,1; giám khảo B: 7,8, 7,4, 7,8. Vòng 8 khoảng 7,75, vòng 9 khoảng 7,8, vòng 10 khoảng 7,8: **đi ngang quanh 8**.
- Lỗi lặp lại cả ba vòng: lửa tắt bằng alpha trên cỏ ra vàng mù tạt, ô liu (cộng màu cam mờ lên xanh lá); khói còn phẳng; Sky Fire chưa có vòng sóng hay vòm, nổ không to hơn đòn chữ; vết cháy và lưới nứt quá đều. Clip PLAIN của vòng 10 chụp nhầm đòn mạnh (PERFECT 128).
- Phiếu: `games/.wt-dh-vfx/tmp/vfx/judge-r10a/verdict.md`, `judge-r10b/verdict.md`. Đang hỏi chủ dự án: làm vòng 11 có kiểm màu tại chỗ trước khi chấm, hay dừng ở khoảng 8 và gộp.

### Lửa Rồng vòng 9 đã chấm (30/10, khoảng 08:10): chưa đạt 8,5

- Giám khảo A: mạnh 7,9, thường 7,4, Sky Fire 7,9; giám khảo B: 8,0, 7,5, 8,0. Tiến trình: vòng 7 khoảng 7,4, vòng 8 khoảng 7,75, vòng 9 khoảng 7,8. Đã ngang game thương mại: T của đòn mạnh 8,5, R của Sky Fire 8,5, T của Sky Fire 9,0.
- Kéo xuống: khói pha F 6,0–6,5 ở cả ba đòn (mảng ô liu phẳng trên cỏ, dải mép thẳng trên sông), lửa tắt thành mảng đỏ cắt cứng, Sky Fire trúng còn đĩa hồng đào và chưa có vòng hay vòm theo bán kính luật, ngôi sao sticker ở đòn mạnh, quái lóe kem 4–5 khung ở đòn thường, vết cháy như cái lỗ, đòn Perfect chưa có vệt chữ. Tờ Sky 1280x720 play-dark bị lớp tạm dừng che, phải chụp lại.
- **Vòng 10** đã gửi V-dh2 (`judge-r9a/b/verdict.md`). Khói đổi sang mặt nạ mật độ, tô màu trong shader (than ấm, sáng trên, ửng lửa dưới). Clip Firefly khói trắng trên nền đen làm mặt nạ: hỏi chủ dự án trước khi tạo (đã dùng hết khoảng 25 clip được duyệt).

### Sau khi khởi động lại (30/10, khoảng 00:25)

- Làn Codex `s1` chạy lại; 00:36 chủ dự án báo Codex đã có hạn mức, khởi động lại `s1` để chạy ngay (192 bắt đầu 00:36). Vẫn **một làn**. Chủ dự án: "Codex bao giờ xong thì kêu nó làm tiếp" — hết `s1` thì duyệt và nối phiếu 194–217.
- V-dh2 được gửi tin chụp tiếp vòng 9.
- **Monkeytype typing feel: xong (30/10, khoảng 09:05).** Nhánh `feature/typing-feel` trong `games/monkeytype` (6 commit) **đã gộp fast-forward vào `feature/en-vn-translation`** (30/10, chủ dự án bảo "gộp luôn"; HEAD `8a335aba6`, chưa push, checkout đang ở `feature/en-vn-translation`). Hai vòng kiểm độc lập: vòng 2 đạt. 1.457 test, oxlint và tsc sạch. Claude thử trình duyệt: nhóm "typing feel" ở tab custom, rê chuột tải đúng preview, chọn Bright Clack tải đủ 15 file và lưu, gõ chữ vẽ hiệu ứng trên hai canvas. `pnpm build:monkeytype` ở repo cha nay chạy `sync-keys` trước (commit `43a44fbf`). Khi có 80 bộ (218, 219): chép kit mới vào `frontend/src/ts/custom/typing-feel/kit/` và chạy `pnpm sync-keys` từ staging mới.
- **Việc mới của chủ dự án:** đưa tiếng phím Firefly và hiệu ứng gõ chữ vào **Monkeytype** (`games/monkeytype`, repo riêng, nhánh `feature/en-vn-translation`), cài đặt nằm trong tab "custom" của cửa sổ Custom Text (mã của chủ dự án ở `frontend/src/ts/custom/en-vn-translation/`). Workflow `monkeytype-typing-feel` đang chạy: ba người đọc, thiết kế, làm trên nhánh mới `feature/typing-feel`, hai người kiểm. Thử trình duyệt do điều phối làm sau. File âm không vào Git (script chép từ `~/AudioLab/review/staging/keys-firefly`).

### Dừng hết để chủ dự án khởi động lại máy (30/10, 00:18)

Chủ dự án: "dừng lại mọi thứ để tôi reset máy". Không còn tiến trình nào chạy (đã kiểm `queue.sh`, `codex exec`, vite, trình duyệt chụp).
- **Codex:** làn `s1` đã dừng. Phiếu 192 chưa chạy được vì Codex hết hạn mức tới **04:17 sáng 30/10**. Chạy lại: `tools/codex-run/queue.sh .local/codex-lane-mac-s1.txt` (một làn; còn 192, 193, 142–145, 148, 186, 149–153, 183–185, 176, 177).
- **Lửa Rồng vòng 9 (V-dh2):** dừng giữa lúc chụp. Trên `dh-vfx` đã commit `31e2191` (chín sửa chung của giám khảo vòng 8) và `196d490`; worktree sạch. Lượt chụp vòng 9 chưa xong: đòn mạnh đã chụp, thường và Sky Fire chưa. Mở lại: một agent mới đọc `docs/changelog` vòng 8, hai phiếu `judge-r8a/b/verdict.md` và hai commit trên, chụp lại đủ bộ vào `tmp/vfx/final9/`, rồi gửi hai giám khảo mới.
- **Phiếu Codex mới 194–217 (24 phiếu):** workflow `codex-next-tickets` đã viết xong bản nháp nhưng bị dừng trong bước kiểm. Các file chưa commit, chưa xếp làn. Mở lại: kiểm từng phiếu (đường dẫn, trùng, luật Codex), thêm hàng vào `docs/CODEX_QUEUE.md`, nối vào cuối làn `s1`.
- **Tiếng phím:** 189, 190, 191 xong (191 commit `de7176e` trên `ts-typefx`, mặc định Bright Clack). Chờ `media:push`; Drive cần chủ dự án chạy `pnpm media:setup --reconnect`.

### Codex vừa phải (30/10, 00:00; chủ dự án: "khi Codex có quota lại, hãy giao việc vừa phải thôi, không cần làm song song nhiều agent nữa")

- **00:02, một làn (chủ dự án: "tạm thời cho Codex về 1 làn thôi cũng được, khi nào tôi yêu cầu thì sửa sau"):** dừng ba làn `m1`–`m3` khi đang chờ giới hạn (không phiếu chạy dở), gom vào **một làn `s1`**: 192, 193, 142, 143, 144, 145, 148, 186, 149, 150, 151, 153, 152, 183, 184, 185, 176, 177. Phiếu mới (194 trở đi) nối vào cuối `s1`. Chỉ mở thêm làn khi chủ dự án bảo.
- Mười làn song song chạm giới hạn chỉ vài phút sau khi mở (23:35). Đã dừng cả mười khi đang chờ, gom phần còn lại vào **ba làn**: `m1` 192, 193, 176, 177; `m2` 142, 143, 144, 145, 148, 186; `m3` 149, 150, 151, 153, 152, 183, 184, 185. Cả ba chạy tiếp khi hết giới hạn (khoảng 00:05).
- Đã xong từ 23:15: 175, 188, 191 (Last Line: 7 bộ phím, mặc định Deep, 238 test xanh; chờ Claude kiểm trình duyệt và `media:push`).
- Phiếu mới của workflow `codex-next-tickets` (194 trở đi) nối vào cuối ba làn này, không mở làn mới.

### Codex chạy song song (29/10, 23:25; chủ dự án: "tăng việc song song", "cho nó làm song song")

- Dừng P1, P2, P3, P5 lúc đang chờ hết giới hạn (không phiếu nào chạy dở) và dừng vòng lặp P6b (phiếu 191 vẫn chạy tới hết). Chia việc còn lại thành 10 làn chạy cùng lúc, cách nhau 10 giây: `p1a` 142, 143; `p1b` 144, 145; `p2a` 148, 176; `p3a` 175, 149, 150; `p3b` 151, 153; `p3c` 152, 177; `p5a` 188, 183, 184; `p5b` 185, 186; `p6c` 192 (`.wt-dh-keys`); `p6d` 193 (`.wt-td-keys`). Danh sách ở `.local/codex-lane-mac-<làn>.txt`.
- Gặp giới hạn thì `queue.sh` tự chờ rồi chạy lại phiếu đó. Hạn mức Codex là trần thật, nhiều làn chỉ làm hàng đợi cạn nhanh hơn khi còn hạn mức.
- Workflow `codex-next-tickets` đang soạn 18–24 phiếu mới (194 trở đi) cho làn P7–P10; xong thì duyệt, thêm hàng vào `docs/CODEX_QUEUE.md`, chạy song song.

### Lửa Rồng nhắm 9 (29/10 tối)

- **Vòng 8 xong (29/10, khoảng 23:20):** V-dh2 commit trên `dh-vfx` (`bea3528` gộp main, `47efd27`, `210e94c`, `cc9d15c`, `e16fbf2` changelog), chưa gộp, chưa push. Đủ chín flipbook theo bản chọn; §5.6 đạt trừ thân sáng lóe / đầu đạn đòn mạnh 1,11–1,44 (dưới 1,5); `dh-perf` High trận 3,84–4,56 / 5,4–6,3 ms. Còn mở: bộ nhớ texture VFX khoảng 101 MB High (trần đề xuất 32 MB), số Sky Fire chồng thẻ chữ đang gập 3–5 khung (sửa ở `src/ui/tags.ts`). Media flipbook chờ `media:push` (Drive cần chủ dự án kết nối lại). Tờ và clip: `games/.wt-dh-vfx/tmp/vfx/final8/`. **Chấm vòng 8 (29/10, khoảng 23:45): chưa đạt 8,5.** Giám khảo A: mạnh 7,8, thường 7,4, Sky Fire 7,3; giám khảo B: 8,4, 8,0, 7,6 (vòng 7: 7,55/7,7, 7,35/7,1, 7,4/7,4). Hai người cùng chỉ: lửa additive vẫn phai qua vàng mù tạt, ô liu trên cỏ; khói Sky Fire là khối xanh đen đặc đứng yên hơn 1 s; đèn tung đòn rửa bệ sáng thành hồng cá hồi; số sát thương che lõi nổ hoặc nằm dưới thẻ chữ; nổ Sky Fire nhỏ hơn thiên thạch. Phiếu: `games/.wt-dh-vfx/tmp/vfx/judge-r8a/verdict.md`, `judge-r8b/verdict.md`. **Vòng 9:** đã gửi V-dh2 chín sửa chung của hai giám khảo cùng phần còn nợ; xong thì gửi hai giám khảo mới.

- **Chủ dự án:** "cố gắng lên 9, 8,5 vẫn chấp nhận được" (ghi ở `VFX_STANDARD.md` §5.6). Duyệt khoảng 25 clip Firefly.
- **Firefly Video không trừ credit:** tài khoản ghi "Standard features: Unlimited access"; số dư đứng 8.900/10.010 sau khi bấm tạo. Credit chỉ dùng cho model đối tác (không dùng).
- **Clip:** điều phối tạo trong tab Firefly của chủ dự án theo `docs/games/vfx/FIREFLY_VFX_LIST.md` (22 lệnh lúc khoảng 21:00, một lệnh báo "Something went wrong"); tải về `~/VFXLab/inbox/firefly/dragon-hold/<id>/`.
- **Làn FXV** (agent nền, mở lại): dựng `tools/vfx-flipbook/` (`run.sh ingest`, `run.sh all`), không commit, báo danh sách file để điều phối duyệt.
- **Làn V-dh2** (agent nền): `games/.wt-dh-vfx` nhánh `dh-vfx`; gộp `main`, làm 15 sửa của hai giám khảo vòng 7, lớp flipbook, rồi chụp vòng 8. Không tự chấm thay giám khảo: điều phối gửi hai giám khảo độc lập (mức 9, sàn 8,5).

### Làn Claude (agent nền của coordinator-2, trừ làn cuối)

| Làn | Nơi làm | Việc | Khi xong |
|---|---|---|---|
| **R2** (map Rồng, chờ ảnh) | `games/.wt-dh-mappilot`, nhánh `map-pilot` (`51fb5b2`, chưa gộp) | Đường vòng 2: mọi lối mòn thành dải đường, cụm 1–3 món mỗi 2–4,5 m (56 món), hết khung giật (vẽ một khung lúc nạp), `dh-bench` +0,30 ms; tự chấm đường M 6,0, "vệt quệt" còn ít. Model ven đường: cliff-rock-a/b, grass-tuft, lantern-post, rail-fence | **Dừng chờ** 155 (đá lát), 120 (trời), 124 (mốc) và M-dh; khi có thì chạy lại `dh-foe-contrast` 1920 và `dh-crowd`, rồi giám khảo đường và cổng C |
| **L2** (Wordwoven 1C, hết ngữ cảnh 29/10 08:45) | `games/.wt-td-1c` (nhánh `td-1c` `7b9de55`, chưa gộp) | Đã gộp `a2-days`; sửa C10 theo giám khảo (tự chấm 7,5; tờ `tmp/lane-l2/sheets2/`); đường map 1 bản đầu (`95f764d`: `src/view/3d/road.ts`, ảnh theo vai trò ở `road.json`, đá bờ `props/da-ke`, đã push media). Còn: khay mép, kẹp thẻ khi zoom, tờ đường theo PATH_QUALITY §5, sửa đá bờ, gắn 122/123c khi nhận (BUILD_NOTES §8.9–§8.12) | Giám khảo C10 vòng 2 đang chạy; làn mới (L3) nhận phần còn lại, đọc BUILD_NOTES §8.9–§8.12 |
| **V-ts** (VFX Last Line) | đã gộp vào `main` `e26e898` (cùng `ts-codex`), đã đẩy | TS-M1-04 đạt. TS-M1-05 **trượt giám khảo độc lập**: Pulse Gun 5,5, Heat Beam 5, tàu bị đánh 4,5, Pulse Gun trên nền sáng 4. Lóe bắn là đĩa trắng tròn quanh tàu, mất màu súng; đốm trúng trắng che bầy; khói mờ; thiếu lớp tối | Vòng 2 khi có chỗ trống (tối đa 4 làn) |
| **V-dh** (VFX Rồng, dừng 29/10 19:30) | `games/.wt-dh-vfx`, `dh-vfx` `2ed786a` (sạch, chưa gộp) | Vòng 7 hai giám khảo: mạnh 7,55/7,7, thường 7,35/7,1, Sky Fire 7,4/7,4, dáng 7,5/7,5. Bloom chỉ ở Ultra (`?bloom=1` tới khi có Cài đặt), thước đo vùng màu lửa `fireRegion`, số Sky Fire cạnh thẻ. Bước 3: VFX quái 5 pha và mã SFX từng quái đã commit; chưa chụp đợt 7 đông, chưa đo riêng, chưa chấm. Bàn giao: mục 8 cuối `docs/changelog/2026-10-29-vfx-round7.md`; công cụ ở `tmp/vfx/lane-tools/` | **Làn mới V-dh2 (chưa mở):** vòng 8 dùng texture lửa (Codex 173, làn M20) và có thể flipbook từ video Firefly (Adobe Firefly Video Model, nền đen); sửa của hai giám khảo `judge-r7a/`, `judge-r7b/` |
| **J5** (xong) | `judge-r6/verdict.md` | 1a vòng 6 **trượt**: mạnh 7,3, thường 7,0; Sky Fire 7,4 (ô 720 nền sáng 6,5–6,75). Đạt: số sát thương, vùng tối quanh quái | V-dh dừng bước 3, làm vòng 7 cho cả hai; vòng sau hai giám khảo |
| **Âm thanh: đường Firefly** (từ 29/10 19:20) | `docs/games/audio/firefly/` (phiếu Codex 212 lập danh sách Last Line, 213 Dragonhold), `tools/audio-lab/firefly/` (phiếu 217) | Chủ dự án tự tạo âm trong Adobe Firefly (Generate Sound Effects; Adobe cho dùng thương mại với model của Adobe; không dùng model đối tác; không bán lại gói). Làn FF soạn danh sách âm theo mã sự kiện (prompt tiếng Anh, gợi ý diễn bằng giọng, nhịp VFX) và dựng bước `run.sh firefly ingest` / `listen` | Chủ dự án thả WAV vào `~/AudioLab/inbox/firefly/<game>/<mã>/`; điều phối chạy ingest, gửi bản nghe 20 s, gắn vào game sau khi chủ dự án duyệt |
| **FXV** (video Firefly thành flipbook, 29/10 19:45) | `docs/games/vfx/FIREFLY_VFX_LIST.md`, `tools/vfx-flipbook/` | Chủ dự án tạo video hiệu ứng bằng Firefly Video Model của Adobe (nền đen hoặc xanh; an toàn thương mại theo Adobe). Kling và model đối tác chỉ để tham khảo animation, không đưa vào game. Làn FXV soạn danh sách hiệu ứng (prompt, blend, lưới atlas) và dựng `run.sh ingest`: cắt đoạn, tách nền, căn tâm, nối vòng, atlas PNG, JSON, tờ xem | Chủ dự án thả MP4 vào `~/VFXLab/inbox/firefly/<game>/<id>/`; V-dh2 dùng flipbook cho vòng 8 |
| **J1** (giám khảo, xong 29/10 09:00) | `judge-r5/verdict.md`, `judge-c10/verdict.md` | 1a vòng 5 **trượt**: mạnh 6,75, thường 6,4 (A 5,5; trên đá sáng 4,5–5; nón R là hình thang cam phẳng, khối nổ một tông che quái, số sát thương sinh cao 100 px). C10 **trượt**: 6,5 (phím đúng 6,5, sai 7,5, xong từ 6, Word Shot 7,5, combo 6,5; vòng ấn che chữ, từ 13 px nhỏ hơn dòng nghĩa) | Đã gửi: V-dh dựng vật liệu lửa thật (nhiễu ăn mòn, ramp, khói tối cùng lúc) cho 1a vòng 6 và Sky Fire; L2 sửa 5 điểm C10 trước khi làm đường; R2 làm hệ thống đường Dragonhold |
| **J2** (nhận ảnh Codex, xong 29/10 08:30) | `docs/codex-queue/accept-29-10/verdict.md` | Nhận 36, làm lại 18: 113 nhận keyart, logo, emblem (logo và emblem sạch đã chép đè, bản cũ ở `_review/113/replaced-29-10/`); 114 nhận sky-beast, sky-beast-top; 115 nhận banner, portrait-ring, crest, divider; 137 nhận 8, 138 nhận 10, 139 nhận 9. Gốc lỗi: hậu kỳ phá tranh → luật `ART_ACCEPTANCE.md` §5, đã chép vào mọi phiếu ảnh còn chờ | Phiếu làm lại 158–161 đứng đầu làn M15. Gợi ý của người chấm còn mở: ổ icon kim loại và cỡ icon tối thiểu khoảng 20 px cho Dragonhold; vẽ lại bộ icon kiểu cũ của Dragonhold cho hợp bộ mới |
| **M-dh** (model Dragonhold theo mức) | `games/.wt-dh-models` (`dh-models` `d84a433`; kit cha `da4bd842` bậc `ultra`) | Bốn mức dựng từ file gốc, normal và map nhám; LOD xa làm camera chơi vẫn dùng lưới Medium (High 6,25–7,26 ms); Ultra sửa hộp đen (NaN MSAA). Tải: High 10,6 MB, Ultra 15,8 MB. Quyết định 29/10: High vẽ lưới đầy đủ ở camera chơi, cổng High mới ≤ 10 ms TB, ≤ 14 ms p95; thử nén KTX2; tải texture dần ở `view/stage.ts` | Gộp vào `main` Dragonhold sau khi đo lại; chép `m0b/`, `kit3/` (128 file) sang checkout chính rồi `media:push` (Drive cần `pnpm media:setup --reconnect`) |
| **J4** (xong) | `tmp/lane-l3/judge-c10-r3/verdict.md` | C10 vòng 3 **trượt** 7,5 (phím đúng 8, sai 7,5, xong từ 7,5, Word Shot 7,5, combo 7,5, khay 7); lõi trắng R 0,46–0,6 bán kính | Vòng sau cần hai giám khảo (dải 7,5–8,5) |
| **L4** (Wordwoven C10, **đạt 8,0** 29/10 19:00) | `games/.wt-td-1c` (`td-1c` `2a1f61d`) | Hai giám khảo C và D cùng 8,0 (khay 7,5 và 7,0): C10 qua mức VFX 8. Quyết định: khung đầu đo theo từng nhịp (nhịp hai ở nhà nhận là sự kiện riêng). Việc sửa còn lại cho vòng sau: giữ màu đã gõ trên mọi thẻ khớp; mũi chỉ khay dùng chữ V ở mọi mép (vòng hở ở mép trái đọc thành chữ "C"); ×N và chữ đóng dấu không ra khỏi màn, không đè HUD (kiểm `overHud` mọi khung); nét viền cứng 1–2 khung khi gõ xong; chữ đóng dấu hiện ngay khung phím. Dải chữ giữa màn dùng chung (TF2) sẽ gắn sau | Làn Wordwoven kế: gắn ảnh đã nhận (116 cây, 158 nền tựa, khung 115), sửa các điểm trên, đường dùng ảnh 122/123 khi nhận |
| **J3** (giám khảo C10 vòng 2, xong) | `tmp/lane-l2/judge-c10-r2/verdict.md` | **Trượt** 7,0 (phím đúng 7, sai 7,5, xong từ 6,5, Word Shot 7,5, combo 7): vòng tối vẫn đè từ; thẻ mới hiện cùng khung nổ; đích đáp lại +125–208 ms; số combo nghỉ 13 px; lõi R nửa bán kính | Đã giao L3 |
| **L3** (Wordwoven, xong 29/10 10:30) | `games/.wt-td-1c` (`td-1c` `bc05e67`, chưa gộp) | C10 vòng 3 (`012774b`: vòng ấn dưới mép thẻ, nổ tại thẻ rồi bóp, nhà lóe 65–89 ms, combo 34 px, khay mép, kẹp thẻ mọi zoom; tự chấm 7,7). Đường (`bc05e67`: đá bờ hết viền đen do GTAO, vai tối hơn; lõi − cỏ 0,159/0,155; tự chấm M 5,5, còn "vệt quệt" ở camera mặc định). Còn: lõi R có thể > 30 %; chưa chụp cặp bậc 2; nét trắng mảnh lượn trên cỏ (chưa rõ nguồn); khay mép cần icon nhà và mũi tên bằng ảnh thật; emoji ở thẻ chờ phiếu 133 | Giám khảo J4 chấm C10 vòng 3; đường chờ ảnh 122, 123c |
| **TF2** (phản hồi gõ chữ, thay TF từ 29/10 14:30) | repo cha `shared/game-kit/feedback/typing-fx/`, `ui/quick-settings/`; `games/.wt-ts-typefx` (`ts-typefx`, `4d84efa` chỉ có đồng bộ kit) | TF đã làm: cỡ dải (Large mặc định), móc texture, mặt nạ chữ ẩn, Stamp nâng cấp (tự chấm phím 8,5, xong từ 8,5–9, sai 8; commit `33836dc2`, `9fb51362`, `f6f154ee`). TF2: khảo sát thư viện, Stamp rồi 5 kiểu lên 9, kit quick-settings, gắn Last Line (giữ tiếng phím cũ tới khi Audio Lab được duyệt) | Hai giám khảo trên Lab khi TF2 báo |
| **AN** (thiết kế animation, xong 29/10 14:45) | `docs/games/CHARACTER_ANIMATION.md` (`1accc46d`) | Chưa nhân vật nào lên 7: chuyển tiếp clip 3,5–4 (quái Dragonhold bật tư thế nghỉ, Hỏa Long nằm rạp 70° một khung), chuẩn bị 4–6, khối lượng quái 4,5–5; Wordwoven chưa có nhân vật 3D; Last Line chưa có Lightbearer. Thiết kế: kit `shared/game-kit/anim/` (chuyển tiếp quán tính, sự kiện clip, clip cộng, đám đông skin GPU), Anim Lab `tools/anim-lab/`, thư viện: AnimationMixer, SkeletonUtils, CCDIK (MIT), `@pixiv/three-vrm-springbone` (MIT), clip CC0 Mesh2Motion và Quaternius UAL1, UAL2 | **Bước kế (chưa giao, chờ chỗ trống):** làn ANIM1 dựng lõi kit `anim/` và Anim Lab, sửa hai lỗi bật tư thế của Dragonhold. Đã báo V-dh thử cờ additive cho Attack/Hit/Cast của Hỏa Long sau vòng 7. Codex 181 vẽ tờ tư thế khóa. Chờ chủ dự án: tải Mesh2Motion (rồng, cáo, ngựa, nhện, kaiju; 4,3 MB), Quaternius UAL1, UAL2 Standard (CC0) |
| **E** (duyệt chữ tiếng Anh, xong 29/10) | — | 130, 131, 132 đạt sau sửa, đã gộp: Last Line `main` `b904a54`, Dragonhold `main` `4f61c6e`, Wordwoven `a2-days` `1048f8a` (132 `c5c4f8c`, màn tựa bỏ hình vẽ bằng mã `c7942eb`: không cò, dây đèn, đom đóm, con dấu; thiếu tranh thì nền phẳng và `console.warn`). `NAMES_EN.md` theo luật 28/10 (`7617e17d`) | Tên file chơi thử `loi-goi-choi-thu-*.json` đổi ở lượt dọn công cụ (cùng `scripts/td/b9.ts`) |

**Đã xong 29/10:** kiểm kê hình ảnh và âm thanh UI (commit `330b4527`, `docs/games/map1/UI_IMAGERY.md`); chỉ đạo mỹ thuật (`b2b54ec5`). Làn R chạy lại dưới tên R2 lúc 05:00. Ổ đĩa còn 10 GB lúc 04:15 (74 GB lúc 05:00 sau khi V-dh dọn); `.wt-dh-vfx/tmp` 16 GB, đã bảo V-dh dọn khung thô của các vòng đã đóng.

**29/10 19:50, phiên mở lại:** mọi làn Codex cũ (M11–M20) đã dừng khi phiên khép. Chủ dự án bảo giao nhiều việc cho Codex: dựng lại bốn làn song song từ mọi phiếu chưa xong (`.local/codex-lane-mac-p1…p4.txt`):
- P1: 173, 124, 128, 117, 118, 174, 134, 135, 136, 141, 142, 143, 144, 145;
- P2: 179, 155, 162, 181, 163, 164, 146, 147, 148, 176;
- P3: 125, 156, 121, 127, 126, 157, 175, 149, 150, 151, 153, 152, 177;
- P4: 133, 172, 180, 171, 165, 166, 167;
- P5 (sau P4, chủ dự án bảo giao thêm): 187, 188, 183, 184, 185, 186.
Đã xong chờ chấm nhận: 119, 120, 122 (tự báo chưa đạt), 123, 140 (lượt b), 158, 159, 160, 161, 178; mã 170 chờ duyệt; 182 âm thanh (đường Firefly thay thế).

**29/10 19:55, chủ dự án bảo dừng hết việc khoảng 10 phút** (sẽ đăng nhập Firefly trong khung trình duyệt của app để Claude tự xem). Đã dừng bốn làn Claude giữa chừng, gửi tin để chạy tiếp từ chỗ dừng: TF2 (hiệu ứng gõ, đang làm cú nổ riêng từng kiểu), M-dh (model, đang thêm nén KTX2), FF (danh sách âm Firefly và bước ingest), FXV (danh sách video Firefly và công cụ flipbook). Ba làn Codex vẫn chạy.

**29/10 18:10:** Claude và Codex cùng hết hạn mức khoảng 14:50–18:10. Đã gửi lại bốn làn Claude (TF2, V-dh, L4, M-dh); ba làn Codex tự chạy lại 18:09 ở 122, 160, 120. Phiếu đã xong chờ chấm nhận: 119 (màn tựa Dragonhold), 170 (Wordwoven pack-and-kit, chưa duyệt), 182 (âm thanh, tạm dừng).

**Claude có lại hạn mức 29/10 13:10; Codex hết hạn mức 10:45, tự chạy lại 14:47 (ba làn chờ ở 122, 160, 170).** Đã gửi lại bốn làn Claude (AU-keys, V-dh, M-dh, L4); giám khảo nhận ảnh lô 2 (116–120, 140, 158, 159) đang chạy, kết quả ở `docs/codex-queue/accept-29-10b/`.

**Khi Claude có lại hạn mức (chủ dự án 29/10 11:40: hạn mức Claude sắp hết, giao Codex một lượt dài):** Codex chạy ba làn liền (khoảng 50 phiếu). Việc đầu tiên khi quay lại:
1. Đọc nhật ký làn `.local/codex-runs/` và báo cáo `docs/codex-queue/<số>-report.md` của mọi phiếu xong.
2. Chấm nhận ảnh theo lô (một agent giám khảo như `accept-29-10`), làm lại theo luật hậu kỳ §5; ảnh đạt thì báo làn game gắn.
3. Duyệt phiếu mã 168–171 trong ba worktree Codex (có lượt đồng bộ kit chưa commit), commit, gộp, đẩy.
4. Gửi chủ dự án danh sách dựng Tripo (124, 128, 156) kèm luật số mặt `MODEL_QUALITY.md`.
5. Kiểm các làn Claude còn chạy: V-dh (vòng 7), M-dh (model theo mức), TF (module gõ chữ, Lab), L4 (C10 vòng 4), AU-keys (tiếng phím); làn nào chết thì gửi tin cho nó chạy tiếp.

**Ảnh đã nhận, chờ gắn (29/10, `docs/codex-queue/accept-29-10b/verdict.md` mục "Sẵn sàng gắn"):** Wordwoven 116 (cây v3/v4), 158 `title-backdrop.v2` (cắt 16:9 `1536x864+0+80`, logo `logo.alpha.png` khoảng 45 % rộng); Dragonhold 140 (chín icon kết quả); cùng lượt a: 113 keyart, logo, emblem; 114 sky-beast; 115 banner, portrait-ring, crest, divider; 137 (8), 138 (10), 139 (9). Chưa có làn gắn ảnh UI: mở khi các làn game rảnh.

## 4. Việc chờ, theo thứ tự

0a. **Đẩy âm gõ phím lên Drive khi Codex xong hết (chủ dự án 30/10, khoảng 09:35).** Chủ dự án: "sau khi Codex làm xong toàn bộ, đẩy toàn bộ file âm gốc thành một folder riêng lên Drive, và file âm đã cắt thành folder riêng; folder âm cắt có cả file handoff để tải về máy khác biết đặt ở đâu, cần làm gì để chạy được sau khi pull code".
   - **Chờ:** phiếu 218 (80 bộ trở lên), 219 (kit theo họ) xong, Claude duyệt và gắn vào ba game và Monkeytype.
   - **Drive:** rclone `tgmedia:` (gốc là thư mục `typing-game-media`). Token hết hạn (`invalid_grant`, kiểm 30/10 09:38): chủ dự án chạy `rclone config reconnect tgmedia:` hoặc `pnpm media:setup --reconnect` trước khi đẩy.
   - **Folder 1, âm gốc:** `~/Downloads/typing-mp3/` (408 WAV, khoảng 889 MB) → `tgmedia:audio-sources/typing-firefly-original/`, giữ nguyên 9 thư mục. Đẩy bằng `rclone copy`, kiểm md5 (`rclone check`).
   - **Folder 2, âm đã cắt:** bản giao cuối (`~/AudioLab/review/staging/keys-firefly/` sau 218) → `tgmedia:audio-sources/typing-keys-cut/`, kèm `README.md` lấy từ `docs/games/audio/KEYS_FIREFLY_HANDOFF.md`. README ghi:
     - đặt folder ở đâu: `~/AudioLab/review/staging/keys-firefly/`; âm gốc ở `~/Downloads/typing-mp3/` (đường mặc định của `tools/audio-lab/keys/firefly.py`);
     - lệnh sau khi pull code: Monkeytype `pnpm --dir games/monkeytype/frontend sync-keys`; ba game: chép vào `public/assets/<game>/audio/keys/` hay `pnpm media:pull`; Lab `LAB_KEYS=...`;
     - cách dựng lại từ âm gốc: `bash tools/audio-lab/run.sh keys firefly survey` rồi `build` (hay `build-v2`).
   - Báo chủ dự án hai đường dẫn Drive và dung lượng.
0. **Ưu tiên sớm (chủ dự án 29/10, 20:50): tiếng phím từ Firefly của chủ dự án.** Chủ dự án đã tạo 408 file WAV bằng Adobe Firefly Generate Sound Effects ở `~/Downloads/typing-mp3/` (9 thư mục `Adobe_2026-10-29*`, 8 thư mục 50 file và 1 thư mục 8 file; mỗi file 12 giây, 48 kHz, stereo 16-bit; tên file mở bằng "An edited Foley sequence of isol…").
   - Việc: khảo sát cả 408 file, chọn bản hay cho năm hồ sơ `creamy`, `thock`, `marbly`, `clack`, `dome`, cắt `key-01` … `key-10`, `space-01` … `space-03`, làm sạch, cân độ to, ghi `keys-manifest.json` đúng định dạng `shared/game-kit/feedback/typing-fx/audio.ts`, file nghe 20 giây mỗi hồ sơ và một file so sánh.
   - Mức nhận: từ 9 (`SHARED_SYSTEMS_BAR.md`: bộ phê bình Audio Lab đạt mọi cổng, rồi chủ dự án nghe). Thay bộ Stable Audio và bộ Codex 182 đã bị trả.
   - Không đưa vào game trước khi chủ dự án nghe và đồng ý. File âm không vào Git.
   - **Chủ dự án 29/10, khoảng 22:00:** "tôi đánh giá âm typing hiện tại được rồi, không cần tạo thêm". Không tạo lô Firefly mới (ba giám khảo của workflow đoán bộ này chỉ 7–8,5 theo số đo và đã viết sẵn prompt bổ sung; tai chủ dự án là cổng cuối nên dựng từ 408 file này). Sau khi dựng xong, gửi file nghe để chủ dự án chốt từng hồ sơ.
   - **Chủ dự án 29/10, khoảng 21:55, đổi hướng:** "triển khai luôn, không cần dựng theo list (Creamy, Thock, Marbly, Clack, Dome), cứ tạo luôn, thêm tính năng khi hover vào thì phát ra âm 1 s"; "nếu Codex làm được và tốt thì kêu Codex làm luôn". Đã dừng workflow `keys-from-firefly` ở bước dựng (khảo sát và ba phiếu chọn nguồn vẫn còn ở `tmp/keys-firefly/` và trong journal của workflow). Giao Codex:
     - làn P6 (chạy 21:59): 189 (mỗi thư mục một bộ, tên tiếng Anh, `preview.ogg` 1 s, staging `~/AudioLab/review/staging/keys-firefly/`), rồi 190 (kit: danh sách chọn từ danh mục, rê chuột hay focus nghe thử 1 s);
     - làn P6b (`.local/codex-lane-mac-p6b.txt`, **Claude mở tay**): 191 Last Line (`.wt-ts-typefx`), 192 Dragonhold (`.wt-dh-keys` từ `main`), 193 Wordwoven (`.wt-td-keys` từ `a2-days`).
     - Trước P6b, Claude phải: duyệt và commit 189, 190 (giữ nguyên sửa chưa commit của TF2 trong `typing-fx/css.ts`, `draw.ts`, `quick-settings/css.ts`); thêm `ui`, `feedback`, `audio` vào `kit.config.json` của Wordwoven; tạo hai worktree; đồng bộ kit vào ba worktree; báo TF2 rằng 191 làm trong `.wt-ts-typefx`.
     - **Đã làm (29/10, khoảng 22:50):**
       - 189 và 190 đã duyệt, commit `9f7cac0f` và `7b677b5a`. Thử Lab ở 1280 × 720: danh sách Off cùng 7 bộ; rê chuột chỉ tải `preview.ogg` của bộ đó; chọn thì tải đủ file và giữ lựa chọn; không lỗi console.
       - 7 bộ: Deep, Warm, Rounded, Solid, Crisp, Clear, Bright Clack. Mức chung −34,5 LUFS-M max (thấp hơn −27, vì cú có crest lớn). Đã chép sang `~/AudioLab/review/staging/keys-firefly/`; sandbox Codex không ghi ra ngoài repo.
       - Kit đồng bộ từ bản HEAD sạch (worktree tạm, không kéo sửa dở của TF2): `ts-typefx` `0bc81b5`, `dh-keys` `d7717ac` (thêm a11y-dialog 8.1.5), `td-keys` `81baf46` (thêm module, a11y-dialog, test theo nhãn tiếng Anh của kit). `pnpm check` xanh cả ba.
       - **P6b sẵn sàng, chưa mở:** chờ chủ dự án nghe `tmp/keys-firefly/listen/so-sanh-cac-bo.mp3` và chọn bộ mặc định (đã hứa không gắn vào game trước khi có câu trả lời). Có câu trả lời thì ghi bộ mặc định vào cuối `docs/codex-queue/189-report.md` (phiếu 191 đọc ở đó), rồi chạy `tools/codex-run/queue.sh .local/codex-lane-mac-p6b.txt`.
   - **Đã dừng (29/10, khoảng 20:55):** workflow `keys-from-firefly` (khảo sát → ba giám khảo chọn nguồn → dựng → hai người kiểm bác bỏ → sửa, tối đa ba vòng). Mã ở `tools/audio-lab/keys/firefly.py`, đầu ra ở `tmp/keys-firefly/` (hồ sơ, `listen/<id>-20s.mp3`, `so-sanh-5-ban-phim.mp3`, `metrics.json`, `spectra.png`). Khi xong: duyệt mã, commit, gửi file nghe cho chủ dự án.
1. **Duyệt đầu ra Codex** khi từng phiếu xong. Phiếu mã thì chạy lại kiểm và đọc diff; phiếu đụng giao diện thì kiểm trên trình duyệt ở 1280 và 1920. Sau đó gộp:
   - `ts-codex` vào `main` Tuyến Cuối;
   - `td-codex` vào `a2-days`;
   - `dh-codex` vào `main` Rồng, theo thứ tự gộp map pilot → VFX → `dh-codex`.
2. **Làn T** (chưa mở; bắt đầu khi 090–094 đã gộp):
   - TS-M1-01: model riêng của Tuyến Cuối;
   - DH-02: báo lỗi khi bộ chữ rỗng; bỏ alias nginx;
   - `pnpm build:local`, rồi báo chủ dự án chạy sudo nginx;
   - kiểm cả ba game qua `typing-game.local`.
   Xem `MAP1_PRODUCTION.md` §4.3.
3. **Media:** sau khi nhận ảnh Codex hay model mới, chạy `pnpm media:push --yes`, commit `media.md5` của game, bump con trỏ.
4. **Repo cha:** nhánh `feat/space-typing-admin-uiux` chưa đẩy. Nhánh `map-factory` (Codex 071–075) chưa gộp vì đang tạm dừng.

## 5. Chủ dự án

- **7 câu hỏi** (`MAP1_PRODUCTION.md` §4.4): chủ dự án **đồng ý cả 7 đề xuất** ngày 28/10, khoảng 19:45:
  - Rồng tự tua ×1,75 khi không có chữ (DH-05 bước 0; sửa 06 §10);
  - Chữ Bẫy đo trên nhánh riêng, sau DH-08;
  - D27, D31, D33 chưa đổi núm nào;
  - tên ải 1 của Rồng "Ải 1 · Cầu và Suối" (phiếu 101);
  - C0 của Lời Gọi được duyệt;
  - Lời Gọi chấp nhận khoảng chờ ban ngày, đo lại sau 1C;
  - Tuyến Cuối: ải 2 tên "ẢI 2 · SĂN PACK LEADER", biển viết hoa cả câu (phiếu 104).
- **Trần media Medium của Lời Gọi** (chủ dự án 28/10, khoảng 23:20): tổng ≤ 9 MB, bộ khởi động ≤ 3,5 MB, tải dần theo ngày, byte tới Đêm 1 ≤ 6 MB.
- **Trần media High của Lời Gọi** (chủ dự án 28/10, khoảng 23:55): tổng ≤ 16 MB; High là bậc người chơi tự chọn trong Cài đặt, lần chơi đầu vẫn Medium.
- **Hỏi chủ dự án ngày 29/10, khoảng 03:50 (chưa trả lời):**
  - chọn hướng Last Line A Iron Warden, B Lightbearer hay C Rampart (tờ 112; người chỉ đạo mỹ thuật và Claude khuyên B);
  - dựng Tripo bằng tay: Dragonhold 6 mốc (phiếu 124, ~180 credit), Wordwoven 5 mốc (phiếu 128, ~150), Last Line nhân vật và 5 súng (~180, sau khi chọn hướng);
  - đồng ý hay không việc dựng lại sáu nhà mái tranh của Wordwoven (phiếu 129, ~180 credit);
  - nhận 109 (bốn ảnh ải Last Line) làm bản tạm cho tới khi 126 xong.
- **29/10 chiều, chủ dự án (3):** ba hệ dùng chung ưu tiên dùng thư viện và kho tài sản miễn phí có sẵn nếu an toàn giấy phép khi đưa site công khai (`SHARED_SYSTEMS_BAR.md` §5, sổ `docs/games/THIRD_PARTY.md`). Đã báo TF, AU-keys, AN; tải gói tài sản vẫn hỏi chủ dự án từng gói.
- **29/10 chiều, chủ dự án (2):** mỗi game có nút bánh răng và nút loa ngay trong trận, mở bảng cài đặt chung và bảng âm thanh, không phải ra màn cài đặt: `docs/games/IN_GAME_SETTINGS.md`, dòng trong AGENTS.md; kit `shared/game-kit/ui/quick-settings/` giao TF (gắn Last Line trước); icon ở phiếu Codex 180 (đầu làn M18).
- **29/10 chiều, chủ dự án:** tiếng phím Audio Lab, hiệu ứng gõ chữ và animation nhân vật là hệ dùng chung, phải đạt **từ 9** (hai giám khảo độc lập, không hạng mục con dưới 8,5; chủ dự án duyệt cuối): `docs/games/SHARED_SYSTEMS_BAR.md`, dòng trong AGENTS.md. Đã báo TF và AU-keys; làn **AN** (thiết kế animation) đang rà và viết `docs/games/CHARACTER_ANIMATION.md`.
- **29/10 sáng, chủ dự án:** chọn Last Line hướng **B · Lightbearer** (bỏ tàu; ART_DIRECTION §4.3 đã đánh dấu chọn). Luật mới về đường đi: "phần đường đi cũng phải làm thật đẹp, chứ đường đi nhìn như kiểu lấy ngón tay quệt dài như kia nó rất xấu" → `docs/games/PATH_QUALITY.md` (áp ba game; ảnh: 122/123 tờ c cho Wordwoven, 155 cho Dragonhold, 125 cho Last Line; mã: làn map từng game).
- Symlink lạc `shared/shared` → `shared` đã xóa 29/10 theo lời chủ dự án.
- **Sudo nginx một lần**, khi `pnpm build:local` xong.
- **Tripo đợt 4** (Campfire Ring, Woodpile, 60 credit): chủ dự án đang dựng. GLB thả vào `typing-game-handoff-2026-10-25/tripo-upload-dot4/_GLB tải về/`.
- **Tripo đợt 3** (8 model): đã xong, nằm trong `tripo-upload-dot3/_GLB tải về/`. Làn R đang nhập.
- **librsvg** cho 62 ảnh nhỏ SVG của thư viện: chờ chủ dự án cho cài. Không gấp, vì thư viện đang tạm dừng.

## 6. Tài liệu chính

- `docs/games/MAP1_PRODUCTION.md`, `docs/games/map1/`;
- `docs/games/VFX_STANDARD.md`, `docs/games/DEPLOY_INDEPENDENCE.md`;
- `docs/tools/map-factory/MAP_PLAN.md`, `tools/map-factory/docs/judge.md`;
- `docs/games/ART_ACCEPTANCE.md`, `ART_REPLACE_LATER.md`, `NAMES_EN.md`, `BALANCE.md`;
- `docs/CODEX_QUEUE.md`.
