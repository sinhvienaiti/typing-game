# Thử tải 100 quái + map + kỹ năng, ngân sách hiệu năng (13/11/2026)

**Anh:** lo "100 quái cùng lúc trên màn hình, với đồ hoạ map đẹp, kỹ năng đẹp, thì liệu nó sẽ khiến fps của game như nào, game không mượt thì cuối cùng vẫn là thất bại"; "cứ thử với loại máy mà yếu vừa rồi đến máy trung bình, máy trung bình thì chắc cứ lấy máy tôi làm chuẩn" (Mac mini M4); máy cao chưa định nghĩa.

**Đọc:** AGENTS.md (hiệu năng, chất lượng model, captures), `docs/games/MODEL_QUALITY.md`, `docs/games/VFX_STANDARD.md` §3.7, `docs/games/LESSONS_FROM_THREE_GAMES.md` §5, lab `games/.wt-ic-lab-all/src/lab/` (Ngũ Lôi, ~90 quái, Alt+1..4 đổi góc; "bước p95" là thời gian CPU của sim, không phải thời gian GPU), `docs/games/tu-tien/MAP1_WIDE.md` §13 (map một đường).

## Việc
1. **Chế độ thử tải** trong lab (tệp mới, ví dụ `src/lab/stress.ts`, bật bằng URL hoặc nút; không đổi hành vi `five-thunder.ts`): 100 quái sống cùng lúc đi map một đường (lẫn loài, có hoạt ảnh), greybox map một đường có trang trí (~200 vật nhỏ instanced hoặc vật CC0 sẵn có), Ngũ Lôi v32 tung vào bầy mỗi 6 s, bloom và tone mapping như game.
2. **Đo thời gian GPU thật** mỗi khung (`EXT_disjoint_timer_query_webgl2`, hoặc Chrome tracing nếu không có), thời gian CPU, draw call, tam giác, bộ nhớ texture; ở 1920×1080 và 1280×720; cả bốn góc; với: chỉ quái, chỉ map, đỉnh Ngũ Lôi, tất cả. Chạy trình duyệt qua `.local/bin/heavy.sh --gpu`, trên máy này, khi không có việc nặng khác (kiểm `pgrep -f "[c]odex exe[c] -m"`, chờ nếu có).
3. **Máy yếu vừa:** không có máy thật, nên suy ngân sách: nêu GPU giả định (ví dụ lớp Intel Iris Xe hoặc Apple M1) và hệ số hiệu năng tương đối so với máy này, có nguồn (tra web, ghi đã kiểm hay chưa); tính mỗi mức được tiêu bao nhiêu ms trên máy này để giữ 60 khung/s ở máy đó. Thử thêm render scale 0,67 và DPR 1 để thấy mức Thấp tiết kiệm bao nhiêu.
4. **Ba chi phí lớn nhất** và cách cắt không thấy khác (quái instanced, hoạt ảnh nướng vào texture, ảnh phẳng cho quái xa, trần phủ cộng sáng cho kỹ năng, ánh sáng và bóng nướng cho map, texture nén), kèm mức tiết kiệm đo được nếu thử nhanh được.
5. Viết `docs/games/tu-tien/PERF_BUDGET.md` (tiếng Việt có dấu): bảng đo, ngân sách theo hệ thống cho 60 khung/s ở máy trung bình (máy này) và máy yếu vừa, định nghĩa mức Thấp/Vừa/Cao (Cao để ngỏ: anh chưa định nghĩa), luật tự hạ chất lượng khi khung hình rớt, thứ tự tối ưu nên làm trước.

**Giới hạn:** không commit; không media trong Git; không đụng chỉnh Ngũ Lôi (phiên lab-element-kits đang làm cùng lab); captures ở `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/perf-stress/` có ABOUT.md, clip ngắn cảnh thử tải và biểu đồ ở `owner-review/2026-11-13/tu-tien/perf-stress/`; xoá khung thô của mình. Model Opus 5.5, effort medium. Báo cáo tiếng Việt ≤ 300 chữ: số chính, ba chi phí lớn nhất, đề xuất mức chất lượng, đường dẫn tài liệu.

## Kết quả (lab-flipbooks, 13/11 11:15)
Đủ năm việc. Cảnh: `games/.wt-ic-lab-all/stress.html` + `src/lab/stress.ts` (tệp mới; `?auto=1` tung Ngũ Lôi mỗi 6 s). Đo: `scripts/visual/scenarios/lab-perf-stress.mjs` (PART=grid|cuts|live|clip). Tài liệu: `docs/games/tu-tien/PERF_BUDGET.md`. Số liệu: `typing-game-review/captures/tu-tien/perf-stress/`; cho anh xem: `owner-review/2026-11-13/tu-tien/perf-stress/`. Máy anh, "tất cả" 1920×1080: GPU 11,0 ms trung vị, 17,8 p95; 1280×720: 6,0 / 11,3; CPU p95 ≤ 2,2. Không commit; không đụng Ngũ Lôi. Props mượn của Dragonhold chép vào `art-src/lab/models/stress-props/` (git bỏ qua).

## Vòng 2 · tối ưu giữ nguyên hình ảnh (anh, 13/11 11:4x)
Anh: "tối ưu ở đây là gì, không phải cứ giảm chất lượng hình ảnh, video là tối ưu, tôi muốn chất lượng hình ảnh nó phải tốt, trừ khi hình ảnh đó gây quá mức làm kém chất lượng thì lúc đó mới phải cân bằng lại… còn lại thì phải làm sao để game vẫn mượt, đẹp". Render scale và tắt bloom chỉ là mức Thấp cuối cùng cho máy yếu, không phải kế hoạch chính.
Làm trong cảnh thử tải (không đụng chỉnh Ngũ Lôi; với Ngũ Lôi chỉ đo và đề xuất), mỗi việc đo trước/sau và **chụp so sánh cùng khung để chứng minh hình không đổi** (hiệu ảnh, PSNR ≥ 40 dB hoặc giải thích chỗ khác):
1. **Lưới vừa khít cho thẻ hiệu ứng** (cột, tia, vụ nổ, vũng sáng): thay hình chữ nhật đầy bằng lưới bám theo phần có điểm ảnh sáng, để không vẽ vùng trong suốt. Đo giảm overdraw và ms ở đỉnh Ngũ Lôi.
2. **Bầy quái:** LOD theo cỡ trên màn (chỉ đổi mesh khi quái cao < N px, chứng minh không thấy khác ở 1080p), hoạt ảnh nướng vào texture cho bầy instanced. Đo ms và tam giác.
3. **Nạp sẵn shader và texture** khi vào trận (bỏ khựng lần đầu), **texture nén KTX2** cho flipbook và model (hình như cũ, bộ nhớ giảm).
4. **Nền:** tách đo đất / ánh sáng / hậu kỳ; nếu đất đắt, nướng ánh sáng và bóng vào texture (hình như cũ hoặc đẹp hơn).
5. **Ngũ Lôi:** chỉ đề xuất (không sửa): lớp nào chồng nhiều nhất, có thể gộp lớp nào mà không đổi hình.
Cập nhật `docs/games/tu-tien/PERF_BUDGET.md`: thay mục mức chất lượng bằng thứ tự "giữ hình trước, hạ hình sau cùng", bảng trước/sau từng việc, và còn bao nhiêu ms so với ngân sách. Không commit. Báo cáo ≤ 300 chữ.

## Kết quả vòng 2 (lab-flipbooks, 13/11 chiều)
Đủ năm việc, chi tiết `docs/games/tu-tien/PERF_BUDGET.md` mục 7, 9, 10. Công cụ: `src/lab/stress-opt.ts` (công tắc lúc chạy, vẽ thẳng vào render target số thực để chứng minh hình giống hệt từng bit, A/B xen kẽ), `lab-perf-stress.mjs` PART=opt. Kết quả: nạp sẵn 480 → 45–55 ms khựng lần đầu (hình như cũ); KTX2 77,7 dB so PNG, bộ nhớ ÷ 4; ánh sáng đất 1,1 ms là chi phí scene lớn nhất (đề xuất nướng); lưới vừa khít cho thẻ 0–0,4 % (bỏ); LOD −9…−14 % scene nhưng đổi bóng ở con gần (chỉ cho con < ~80 px); Ngũ Lôi: đỉnh 12–17 lớp chồng, ba lớp trận pháp phủ 25–45 % màn, đề xuất gộp. Ảnh: `owner-review/2026-11-13/tu-tien/perf-stress/round2-compare.jpg`. Ghi chú: cách đo vòng 1 (đồng bộ mỗi khung) bi quan; số vòng thật là chuẩn. Không commit, không sửa Ngũ Lôi.

## Vòng 3 · hai việc giữ hình + chọn video (15/11 17:4x)
Anh (15/11): cứ làm theo đề xuất. Từ `docs/games/tu-tien/PERF_BUDGET.md` §9:
1. **Nướng ánh sáng đất** (1,1 ms ở 1080p): nướng ánh sáng tĩnh và bóng tĩnh của sân vào texture (lightmap), giữ đèn điểm của đòn đánh và bóng thú. Chứng minh bằng ảnh trước/sau cùng khung (PSNR hoặc hiệu ảnh) và số ms, như vòng 2.
2. **Gộp ba lớp trận pháp Ngũ Lôi** (`formationShade` + `formation` + `formationRim`) thành một thẻ một shader, cùng thứ tự trộn, hình y hệt; đo trước/sau. Phiên lab-element-kits đang chuyển sang làm rồng, không sửa Ngũ Lôi lúc này: được sửa `five-thunder.ts` chỉ phần lớp trận, và báo cho phiên đó trong báo cáo.
3. **Chọn take và làm flipbook cho video Firefly mới** (khoảng 122 video tạo ngày 13/11 trong `games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/video/`, các thư mục có `take*.mp4` mới hơn 2026-11-13 00:00): dùng các script chọn take và làm flipbook đã có ở `.local/s2/` (xem `picks-i2v3.json`), ghi lựa chọn vào một tệp picks mới, làm flipbook cho các take được chọn, cập nhật manifest tương ứng; tấm khung chọn take gửi `owner-review/2026-11-15/tu-tien/firefly-picks/`. Không xoá take nào.
Không commit. Báo cáo ≤ 250 chữ.

## Kết quả vòng 3 (lab-flipbooks, 15/11)
1. Nướng ánh sáng đất: làm và đo (`src/lab/ground-bake.ts`); giữ phản xạ thì không nhanh hơn, bản lite nhanh hơn 0,5–0,7 ms nhưng mất ánh phản xạ trời (22–24 dB) nên bỏ. Thay vào đó: AO+roughness gộp một texture (giống hệt từng bit, −0,3 ms) và KTX2 cho map đất (56–58 dB, −0,5–0,7 ms): đề xuất đưa vào `look.ts`. Chi tiết `PERF_BUDGET.md` mục 11.
2. Lớp trận pháp Ngũ Lôi: 6 thẻ tốn 1,32 ms lúc tia rơi. Tỉa shader (noise khi cần, một lần đọc) giống hệt nhưng không nhanh hơn, đã gỡ khỏi `five-thunder.ts` (tệp như trước vòng 3). Gộp một shader để ngỏ (ước 0,6–0,9 ms) đến khi Ngũ Lôi chốt hình.
3. Video 13/11: 62 việc, 122 take kiểm máy + xem tấm; picks `.local/s2/picks-2026-11-13.json` (2 đổi theo mắt, `dark-comet-white` cả hai take lỗi: cần làm lại). Flipbook 61 việc: 53 thay tại chỗ (bản cũ `.old`/`.old2`), 8 mục mới (5 Lôi i2v5 `thunder-column-a/b/c-i2v5`, `thunder-energy-sharp-i2v5`, `thunder-stream-a-i2v5`; 2 dấu đất nghiêng `*-ground-mark-side-i2v3`; `yin-yang-void-mirror-manifest`), 10 mp4 1080p, ktx2 nén lại cả 61. Tấm: `owner-review/2026-11-15/tu-tien/firefly-picks/`.

## Kết quả vòng 4 (lab-flipbooks, 15/11 18:4x)
`src/lab/look.ts`: đất dùng AO+roughness gộp rồi KTX2 (`?groundTex=jpg|orm|ktx2`, mặc định ktx2; tệp ở `art-src/lab/lookdev/<id>/`, ghi chú `PACKED.md`). Gộp giống hệt 100 % ở góc 1 và 2b; KTX2 53,7–55,8 dB (vẽ thẳng), 48–51 dB (cả khung). Scene −14 % / −21 %, cả khung −8 % / −15 %. Vòng thật khi máy rảnh: trung bình nhanh hơn, p95 trong nhiễu giữa các lượt. `PERF_BUDGET.md` §10.7. Không sửa Ngũ Lôi, không commit; test lab 425/425.
