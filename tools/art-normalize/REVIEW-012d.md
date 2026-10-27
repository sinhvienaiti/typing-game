# Đối chiếu phản biện Phiếu 012d

Ngày 26/10/2026. Đã đọc đủ `merged.findings`, `merged.review012b_status`, `merged.notes` và bốn góc trong `.local/codex-runs/012c-review.json`, cùng các script kiểm ảnh và mutant của người phản biện. JSON có **2 lỗi lớn và 19 lỗi nhỏ**; đoạn notes của phản biện ghi 20 lỗi nhỏ là lệch một mục. Đây là hồ sơ sửa, **chưa thay phản biện lần 4 của Claude**.

## 1. Hai lỗi lớn

**Đường nối B1.** Bỏ đường cắt thẳng cố định, tìm đường sai số nhỏ nhất bằng quy hoạch động theo từng hàng. Giá mỗi điểm gồm sai số RGB giữa hai cột nguồn và bước nhảy qua dải 8 cột; bước ngang tối đa 4 px/hàng. Trộn smoothstep bán kính 3 px. Không resize mặc định; PNG lưu đủ path/radius/overlap/source_size trong tEXt `art-normalize-seam`.

Chốt có reference tự suy ra đường nối từ pixel, không tin metadata của ảnh được kiểm. Theo dải 64 hàng, đo RGB qua 2r+2 cột, so p99 phần trong và cặp cột nguồn tương ứng. Độ sáng dùng cùng phép đo trung bình trị tuyệt đối ở đường nối và phần trong; ghi thêm bước có dấu. Điều này tránh so trung bình trị tuyệt đối với trị tuyệt đối của trung bình, vốn có thể triệt tiêu khác nhau. Các ngưỡng nằm trong README và mã; không chọn ngưỡng riêng cho B1.

Sọc hàng dùng cửa sổ trượt trên cả hai dải overlap, kể cả chỗ cắt. Có reference thì trừ bước hàng ở đúng cột nguồn được chọn cho từng hàng, kể cả đường nối di chuyển. Cửa sổ chi tiết cũng so đúng cột nguồn; bỏ nội suy vị trí theo tỉ lệ hai khổ. Kiểm gương có thêm các dải 3/5/8/12 px với cặp đối chứng cùng khoảng cách.

**Test ghim hành vi.** Ngoài bộ cũ, `regression_012d.py` kiểm toàn bộ lòng vật, vành cách nền 4–10 px, ranh AA giữa hai màu sơn, sơn cùng sắc khóa gần nền, viền sơn tối đục và AA. Có unit test cho `key_residue`, `preserve_interior`, chữ ký/frame/coder, `--keep-size`, túi Tripo và khóa runner/report. Ca chi tiết giữa dải giữ nguyên cửa sổ ngoài: **0,789344 nội ảnh / 0,781482 so nguồn phải trượt**; ca **0,935299 / 0,925984 phải qua**.

Ca bắt buộc khác: cắt cứng, cắt cột sai nhất, sọc tại chỗ cắt, sọc một bên mức 9, gương hẹp, gương chỉ trượt `reference_mirror`, bù lệch rộng 30/60 px. Bù lệch 30 px đo residual 5,366667 >5; 60 px đo 8,566667 >5 và test đòi ≥8, tránh chỉ ghim ca sát ngưỡng. Fixture khoảng cách đối chứng cho giá trị giải tích 14 ở khoảng cách 2k+1. Túi có vành mềm phải qua; túi 10×10 có lõi sai đúng 64 px phải trượt. Cầu sơn trung tính nằm ngay ngoài ngưỡng màu phải giữ túi 63 px, ghim cả mutant nới ngưỡng 15% và 60%.

## 2. Mười chín lỗi nhỏ

| Mục phản biện | Xử lý và giới hạn |
|---|---|
| Sơn bão hòa trùng khóa bị xóa, chốt mù | Ghi rõ connected chọn túi ≥64 px, global chọn mọi ứng viên khóa. Runner đếm tổng/xóa/alpha 9–249 của khóa đậm cách nền sáng >5 px; số 0 khóa dư không còn được dùng làm bằng chứng giữ sơn. Test riêng kiểm bộ đếm. Màu thật trùng khóa vẫn cần duyệt nguồn. |
| D3 còn đốm xanh vừa | Thêm tùy chọn job `--no-key-hue`, bật cho D1/D3. Kẹp chênh khóa >50 trong lòng vật; đếm thay đổi màu hợp lệ riêng. Bảng vẫn báo chênh >40, nên không giấu phần 41–50. |
| D1/D3 có đốm khóa ở viền | Với no-key-hue, kẹp kênh khóa ở viền mềm trong dải bảo vệ sau matte. Đếm viền alpha 9–249, chênh >25; có test kẹp và bộ đếm. |
| Làm sáng viền sơn tối/hạ alpha | Bỏ bước thay viền bằng màu trung bình lân cận. Chỉ nhận mô hình pha khóa với residual bình phương trung bình ≤9. Chặn fit gần đục và sơn tối không khóa khi không phải ứng viên. Test giữ đúng RGB/alpha viền tối và khôi phục AA pha khóa. |
| Reference so sai cột | Ánh xạ theo path và dịch overlap thực; test nguồn có đuôi ít chi tiết phải qua chốt detail so nguồn, dù tỷ số nội ảnh thấp. |
| Bù lệch 30 px/gương ≤12 px lọt | Trừ đúng bước nguồn, không cộng cực đại nguồn vào ngưỡng. Thêm kiểm dải gương hẹp và ca reference_mirror độc lập. |
| API nhận tên nguồn bắt đầu `-` | Decorator ghi đường dẫn tuyệt đối đã kiểm trở lại đối số src/files. Test fit/pad/sheet với tên tương đối `-script`. |
| File bị tráo thành SVG | Mỗi lần đọc dùng coder PNG/JPEG/WebP đã kiểm. Test tráo nội dung sau kiểm và canary MSL; không gọi decoder cho chữ ký bị cấm. |
| File công bố 0600 | File mới và bản lưu dùng 0644. Sửa quyền các dẫn xuất lịch sử 012c/012b có tên trong hồ sơ, không sửa byte hay quyền nguồn. Test quyền file công bố và fsync phải xảy ra trước link. |
| Tín hiệu khi dọn để partial | Chặn TERM/HUP/INT lúc tạo tên tạm và trong finally dọn; thử gửi từng tín hiệu ngay trong unlink. Số partial còn lại giảm nhưng chưa hết: tín hiệu đến ngay sau os.link vẫn có thể để lại một `.normalize-*.partial` là hard link thứ hai của đích hoàn chỉnh (phản biện lần 4: 11/40 lượt SIGTERM). Đích vẫn đầy đủ. SIGKILL/mất điện ngoài bảo đảm này. |
| Import thay SIGHUP/nohup | Chỉ CLI/runner gọi install_signal_handlers, giữ SIG_IGN. Test import không đổi handler. |
| Pha một nhận symlink treo | Kiểm is_symlink và đường dẫn thực của cả tên cũ/bản lưu trước mọi đổi tên. Test runner 012d với symlink treo ở cuối danh sách, file đầu giữ nguyên hash và chưa có bản lưu. |
| Test khóa có thể dựng art thật | Khóa riêng, ART/STAGE riêng cho mọi runner và report, gồm 012b/012c/012d. Bỏ khóa cũng chỉ tới dữ liệu tổng hợp thiếu manifest, không chạm art thật. |
| Túi Tripo/vành mềm chưa ghim | Test trực tiếp neutral_residue với vành mềm và lõi đúng 64 px. Bảng Tripo ghi rõ giống byte 012b/012c, không gọi đổi nhãn là sửa pixel. |
| Chữ ký/frame/keep-size/report chưa ghim | GIF một frame, BMP, TIFF phải trượt trước decoder; WebP động phải trượt ở kiểm frame; forced coder/canary được kiểm. Keep-size so pixel với Lanczos + tile và kiểm mép. Test khóa bao gồm report. |
| Canvas Tripo theo độ phân giải/phóng to | Chọn canvas chuẩn gần nhất theo log tỉ lệ hộp vật; fit chặn phóng to. Báo scale thực và khổ trước/sau. |
| Highlight bush-blossom mất sắc | Ứng viên nền trung tính cần chênh kênh ≤6 cả trong flood ngoài. Test highlight lavender RGB (221,206,216) giữ RGBA nguyên vẹn. Manifest ghi số highlight màu gần nền và số bị xóa tại key từng Tripo. |
| Ví dụ xy trượt chốt | Ví dụ tạo texture xác định bằng example_xy.py, rồi chạy seamless/seam-check xy với reference. Ảnh bất kỳ vẫn phải được đo và xem; exit 0 của seam-check chỉ xác nhận phép đo chạy xong. |
| REVIEW/trỏ wrapper/shard/help | Hồ sơ này tóm tắt bằng chứng bền vững, ảnh bàn giao ở art-src; sửa kết luận quá mức trong REVIEW-012c. Wrapper cũ trỏ runner 012d, bỏ shard không dùng, help có mặc định và tiếng Việt. README job ghi rõ chuyển lô một lần và cách tiếp tục. |

## 3. Số đo ảnh và tính toàn vẹn

Số đo chốt sau công bố được ghi trong [README-normalize](../../games/dragon-hold/art-src/2d/README-normalize.md) và [manifest](../../games/dragon-hold/art-src/_review/normalize-metrics.json). Mỗi PNG có sidecar `.prompt.txt` ghi argv thực, lệnh hậu kỳ và prompt nguồn nguyên văn khi có; không dùng prompt bản khác thay cho `.v1` thiếu prompt riêng. Không gọi image_gen vì phiếu yêu cầu hậu kỳ xác định từ ảnh gốc đã có.

| B1, đo bằng chốt 012d | 012c | 012d |
|---|---|---|
| Khổ | 1351×1024 | 1351×1024 |
| Chi tiết cửa sổ / đúng cột nguồn | 0,981672 | 0,997420 |
| Residual sọc so đúng cột nguồn | 0,287654 | 0,103086 |
| Dải 384–447: RGB qua đường nối / p99 phần trong | 11,447917 / 9,161458 | 2,322917 / 9,161458 |
| Dải 448–511: RGB qua đường nối / p99 phần trong | 13,901042 / 13,156250 | 4,802083 / 13,156250 |
| Dải 384–447: bước sáng / p99 cùng phép đo | 11,960881 / 10,526806 | 2,244666 / 10,526806 |
| Số dải hàng trượt chốt đường nối | 9/16 | 0/16 |

Số liệu chứng minh vì sao chỉ đo mép lặp/chi tiết/sọc chưa đủ: cả ba tiêu chí này vẫn qua ở bản cũ, trong khi chốt tại đường nối trượt. Các phép đo đều dùng cùng mã cuối, không so hai con số sinh bởi hai phiên bản chốt khác nhau.

Kiểm phá trực tiếp trên pixel B1, ngoài ảnh tổng hợp trong test.sh:

| Ca B1 | Kết quả chốt tương ứng |
|---|---|
| Cắt cứng ở cột 121, không feather | Trượt 10/16 dải hàng ở cut_continuity. |
| Cắt cứng ở cột sai nhất 75 trong miền tìm cũ | Trượt 11/16 dải hàng ở cut_continuity. |
| Sọc +9 tại path thật, rộng 22 px, mỗi 60 hàng | Residual hàng so nguồn 7,238272 >5, trượt. |

Đây là kiểm riêng các thành phần cut_metrics/row_residual trên dữ liệu B1; không gọi đó là một lượt test.sh hoặc một mutant mã nguồn bổ sung.

Herb-hut: đếm trực tiếp pixel alpha 9–199 có min(R,B)−G >25 trên `icons/normalized/herb-hut.{256,64}.png`: **0 → 0 ở cả hai cỡ**, giữ kết quả đã sửa của 012c. Đã xem hoa chuông tím D2 ở nguyên cỡ trên trắng và D3 trên trắng/tối; không coi số sắc khóa vừa của D2/D4 là toàn bộ lỗi loang vì vật thật có các sắc đó.

Hai crop B1 nguyên cỡ, không upscale, hàng 0–599, gồm cả mép lặp và toàn vùng đường nối trong ô: [012c](../../games/dragon-hold/art-src/_review/b1-cut-before-012d.png), [012d](../../games/dragon-hold/art-src/_review/b1-cut-after-012d.png). [Ảnh xem mép](../../games/dragon-hold/art-src/_review/pine-river-far.seam.png) giữ kích thước pixel. Đã xem crop trước/sau: bản cũ có đường thẳng và vách núi gãy; bản mới không còn đường gãy thẳng đó. Đây là phạm vi quan sát, không phải phê duyệt mỹ thuật toàn bộ lô.

Trong lúc bổ sung test, dừng runner và giữ lại 23 ảnh 012d đã có biên bản/hash. Chỉ hai file test/harness đổi hash; toàn bộ mã xử lý ảnh và runner giữ nguyên. Từng ảnh/sidecar hoàn chỉnh được kiểm hash rồi dùng lại trong vùng dựng mới; ảnh chưa có biên bản không được dùng lại. Manifest ghi `validation_revision` gồm hash test trước/sau và lý do. Validation cuối chạy lại bằng bộ test mới; không lấy kết quả test cũ làm kết quả cuối.

Sau đó phát hiện lỗi chạy đồng thời có thể tái hiện: tool_hashes dùng rglob đi vào thư mục tạm rồi mới lọc, nên gặp FileNotFoundError khi test vừa dọn thư mục. Đổi runner 012c/012d và verify-code sang os.walk, loại thư mục tạm/cache ngay trước duyệt. Đã so AST các runner ngoài đúng hàm tool_hashes, xác nhận không đổi phần xử lý; kiểm lại hash mọi ảnh có biên bản. Manifest ghi riêng `scan_revision`. Không sửa normalize.py hoặc thuật toán ảnh để giữ các kết quả đó.

Lượt chốt cuối sửa đúng một màu trong fixture: pixel ranh RGB (160,82,40) là pha 50/50 chính xác giữa hai màu sơn (192,48,48) và (128,116,32). Chạy lại baseline, test.sh, verify-code và đủ 71 mutant bằng hash fixture cuối. Manifest ghi `final_test_revision`; cập nhật metadata/báo cáo của 012d, không thay bất kỳ PNG, ảnh gốc hay bản lưu 012c nào.

## 4. Chạy mutant

`mutation_012d.py` nhập định nghĩa của ba bộ docs-tests và bộ code của người phản biện, áp lên bản sao công cụ, chạy test.sh riêng. Các bộ này nằm trong `.tmp` của người phản biện, ngoài Git; clone mới không chạy lại được bảng dưới đây. Bản gốc phải đạt trước khi bắt đầu. Mẫu cũ hết hiệu lực được ghi riêng, không tính là bị bắt. Khi cùng hành vi đã chuyển hàm, ghi rõ retarget và giữ old/new trong kết quả.

Lượt thăm dò trước khi chốt fixture bị loại hoàn toàn: một test mới gọi nhầm chữ ký preserve_interior lịch sử; sau đó kỳ vọng no-key-hue đã lẫn ngưỡng báo cáo >40 với ngưỡng sửa >50. Các lỗi fixture đã sửa. Chỉ lượt có baseline đạt và hash mã tương ứng được dùng cho bảng kết quả cuối; không cộng các lượt bị ngắt.

**Kết quả chốt: 71 mẫu, 67 thoát khác 0, 1 còn sống, 3 không áp được.** Baseline test.sh đạt; mọi hash mã gốc của từng bản sao khớp manifest công bố. Không có timeout. Không cộng các lượt thăm dò bị ngắt.

**Còn sống:** `F8-no-exists-precheck` bỏ kiểm exists/is_symlink sớm trong publish_file. Bước os.link độc quyền vẫn từ chối tên đã có, kể cả symlink treo và đối thủ xuất hiện muộn. Đây là bước phòng vệ thừa về tính không ghi đè; không viết test phụ thuộc riêng việc gọi pre-check chỉ để tăng số mutant bị bắt. Mã thật vẫn giữ pre-check.

**Không áp được:** A5, M2, M3 sửa bước tô lại viền bằng màu trung bình lân cận, vốn đã bị xóa. Không tính ba mẫu này là bị bắt.

**Giới hạn diễn giải:** “bị bắt” trong bảng nghĩa là test.sh của bản sao trả mã khác 0. E2 trượt vì IndexError; E6/E7 có biên an toàn trượt ở phép kiểm khoảng cách giải tích. H4–H6 trượt bằng FileNotFoundError khi đi tiếp qua chốt bị bỏ vào mô phỏng cố ý không có file đầu ra. H7 đã dịch file a trong ART giả trước khi phát hiện bản lưu z sai; phép kiểm hash a sau đó nhận FileNotFoundError. H4–H7 chỉ ghim runner lịch sử rebuild_012c.py: khối chốt của regression_012d và ca bản lưu sai hash lúc đó chỉ nạp runner này, nên chúng không chứng minh runner 012d giữ chốt (mutant J-* tương ứng trên rebuild_012d.py còn sống; xem §6). Đây là kiểm dữ liệu tổng hợp, không phải playtest phá art thật. M6 retarget trượt ở ca texture phải qua vì cửa sổ ngoài 3 px quá nhạy; kiểm sọc tại path B1 thật được báo riêng ở §3. Không diễn giải toàn bộ 67 mẫu là 67 kiểm ảnh thực độc lập.

Những mẫu đánh dấu “chuyển vị trí” được áp lại theo hành vi gần nhất sau khi mã đổi hàm. B4/M5 thay cách chọn trạng thái cuối DP, không còn là phép min/max cột thẳng cũ; ca cắt thẳng sai nhất trên B1 thật được kiểm riêng. M6 chuyển cả bề rộng cửa sổ lẫn phạm vi về đúng ba cột ngoài, không chỉ thu cửa sổ trong khi vẫn quét toàn dải. D6 chuyển mức nới một đơn vị sang ngưỡng residual 5→6, không giữ công thức nguồn+3 cũ.

Lượt chốt đầy đủ dùng `regression_012d.py` SHA-256 `48a5e46142bf0a206ef3d7cfce77cdc7433b11b9f3152d72e07f8beea45ea1a7`. Cả 71 bộ hash mã gốc của bản sao khớp manifest cuối, từng trạng thái trong bảng đã đối chiếu với lượt này.

| Mẫu gốc | Kết quả | Áp lại |
|---|---|---|
| `A1-band-3-to-30px` | Trượt test | Mẫu gốc |
| `A2-edge-matte-everywhere` | Trượt test | Mẫu gốc |
| `A3-strong-key-zero-not-candidate` | Trượt test | Chuyển vị trí/hành vi |
| `A4-eligible-everywhere` | Trượt test | Mẫu gốc |
| `A5-fringe-recolour-everywhere` | Không áp được | Mẫu gốc |
| `A6-interior-test-colour-dist` | Trượt test | Mẫu gốc |
| `A7-band-3-to-8px` | Trượt test | Mẫu gốc |
| `A8-interior-high-x1.15` | Trượt test | Mẫu gốc |
| `B1-default-keep-size` | Trượt test | Mẫu gốc |
| `B2-keep-size-no-tile-triangle` | Trượt test | Mẫu gốc |
| `B3-blend-whole-overlap` | Trượt test | Chuyển vị trí/hành vi |
| `B4-no-cut-search` | Trượt test | Chuyển vị trí/hành vi |
| `C1-windows-edge-only` | Trượt test | Mẫu gốc |
| `C2-window-whole-band` | Trượt test | Mẫu gốc |
| `C3-reference-window-off` | Trượt test | Mẫu gốc |
| `C4-reference-window-keeps-intrinsic` | Trượt test | Mẫu gốc |
| `C5-detail-threshold-0.6` | Trượt test | Mẫu gốc |
| `C6-reference-window-threshold-0.6` | Trượt test | Mẫu gốc |
| `C7-detail-threshold-0.75` | Trượt test | Mẫu gốc |
| `C8-reference-window-threshold-0.75` | Trượt test | Mẫu gốc |
| `D1-row-streak-off-with-reference` | Trượt test | Chuyển vị trí/hành vi |
| `D2-row-streak-reference-plus30` | Trượt test | Chuyển vị trí/hành vi |
| `D3-row-streak-left-band-only` | Trượt test | Chuyển vị trí/hành vi |
| `D4-row-streak-threshold-30` | Trượt test | Mẫu gốc |
| `D5-row-streak-off` | Trượt test | Mẫu gốc |
| `D6-row-streak-reference-plus4` | Trượt test | Chuyển vị trí/hành vi |
| `E1-control-distance-2k` | Trượt test | Mẫu gốc |
| `E2-control-distance-2k+5` | Trượt test | Mẫu gốc |
| `E3-mirror-ratio-0.25` | Trượt test | Chuyển vị trí/hành vi |
| `E4-reference-mirror-off` | Trượt test | Mẫu gốc |
| `E5-reference-mirror-never-exempt` | Trượt test | Mẫu gốc |
| `E6-control-distance-2k+3` | Trượt test | Mẫu gốc |
| `E7-control-distance-2k+5-safe` | Trượt test | Mẫu gốc |
| `F1-link-to-replace` | Trượt test | Mẫu gốc |
| `F2-direct-write` | Trượt test | Mẫu gốc |
| `F3-no-signal-handlers` | Trượt test | Mẫu gốc |
| `F4-sighup-unhandled` | Trượt test | Mẫu gốc |
| `F5-no-fsync` | Trượt test | Mẫu gốc |
| `F6-partial-not-removed` | Trượt test | Chuyển vị trí/hành vi |
| `F7-icon-publish-early` | Trượt test | Mẫu gốc |
| `F8-no-exists-precheck` | Còn sống | Mẫu gốc |
| `G1-accept-gif` | Trượt test | Mẫu gốc |
| `G2-decoder-before-rejection` | Trượt test | Mẫu gốc |
| `G3-no-frame-check` | Trượt test | Mẫu gốc |
| `G4-no-forced-coder` | Trượt test | Mẫu gốc |
| `G5-bmp-tiff-accepted` | Trượt test | Mẫu gốc |
| `H1-tripo-rim-exclusion-off` | Trượt test | Mẫu gốc |
| `H2-tripo-gate-never-fails` | Trượt test | Mẫu gốc |
| `H3-tripo-rim-excludes-5px` | Trượt test | Mẫu gốc |
| `H4-decal-interior-check-off` | Trượt test | Mẫu gốc |
| `H5-rejected-012-must-fail-off` | Trượt test | Mẫu gốc |
| `H6-strong-key-far-off` | Trượt test | Mẫu gốc |
| `H7-two-phase-archive-check-off` | Trượt test | Mẫu gốc |
| `H8-runner-012c-lock-off` | Trượt test | Mẫu gốc |
| `H9-report-lock-off` | Trượt test | Mẫu gốc |
| `M1-wide-despill-band` | Trượt test | Mẫu gốc |
| `M2-no-fringe-reconstruct` | Không áp được | Mẫu gốc |
| `M3-fringe-always-mean` | Không áp được | Mẫu gốc |
| `M4-hard-cut-no-blend` | Trượt test | Chuyển vị trí/hành vi |
| `M5-worst-cut` | Trượt test | Chuyển vị trí/hành vi |
| `M6-row-streak-5px` | Trượt test | Chuyển vị trí/hành vi |
| `M7-edge-matte-loose` | Trượt test | Chuyển vị trí/hành vi |
| `P1-pocket-min-65` | Trượt test | Mẫu gốc |
| `P2-no-pockets-colour-bg` | Trượt test | Mẫu gốc |
| `P3-alpha-threshold-half-percent` | Trượt test | Mẫu gốc |
| `P4-dejavu-branch-broken` | Trượt test | Mẫu gốc |
| `P5-fallback-branch-broken` | Trượt test | Mẫu gốc |
| `P6-input-not-safe-path` | Trượt test | Mẫu gốc |
| `P7-keep-alpha-ignored` | Trượt test | Mẫu gốc |
| `P8-no-corner-warning` | Trượt test | Mẫu gốc |
| `P9-tiny-guard-2px` | Trượt test | Mẫu gốc |

Các nhóm được ghim rõ bởi ca mới: A2/A7 (toàn lòng/vành/ranh sơn), A6/A8 (cầu sơn trung tính), C1/C2/C5/C7/C8 (chi tiết giữa dải), D3/D4 (sọc nhỏ một bên), E1/E6/E7 (cùng khoảng cách), E4 (chỉ reference_mirror), G1–G5 (chữ ký/frame/coder), H1–H3 (vành mềm/lõi 64 px), H9 (khóa report), F5 (fsync trước link), M4/M5/M7 (feather/tìm đường/mô hình pha khóa).


## 5. Phạm vi bàn giao

Sau công bố: 164/164 hash nguồn, 461/461 hash lịch sử, 211/211 bản lưu 012c và 212/212 file bàn giao khớp. 106 PNG đều có sidecar. Tổng 887 dẫn xuất/lịch sử thuộc các phiếu này có quyền 0644; đã đổi quyền 211 bản lưu 012b từ 0600, không đổi nội dung. Sau cập nhật fixture cuối, kiểm lại không cần đổi thêm quyền nào. 32/32 Tripo có scale ≤1, qua chốt túi, không xóa các highlight màu gần nền tại bước key; không file Tripo nào giống byte 012b hoặc 012c.

Các số không nên bỏ qua khi duyệt ảnh: D3 còn 2/3 pixel sắc khóa vừa theo ngưỡng >40; tùy chọn job chỉ kẹp >50. Bộ đếm viền/số alpha 9–249 trong lòng D2/D4 có tăng sau khi bỏ bước tô sáng viền; bảng README giữ nguyên số, không gán toàn bộ thành lỗi hoặc tuyên bố đã sạch mọi viền. Cần xem nguyên cỡ, nhất là hoa tím, rêu và nét tối. Khóa bão hòa xa nền vẫn có điểm bị xóa/partial theo quy tắc đã công bố, có bộ đếm riêng.

Không sửa ảnh gốc, art-src/3d, Tu Tiên, game code/docs, tools/audio-lab, model hoặc âm thanh. Không chạy Git, build hay test game. Dựng lại B1, 8 decal, 40 icon; dựng lại 32 Tripo do thay quy tắc canvas/khóa trung tính. Giữ nội dung `.rejected-012`/`.rejected-012b`, lưu bản 012c bằng `.rejected-012c` và kiểm hash. Chủ dự án/Claude cần xem đường nối B1, viền tối decal, D2 tím, D3 và highlight Tripo ở 1:1, rồi phản biện lần 4 trước commit.

## 6. Claude sửa sau phản biện lần 4

Ngày 26/10/2026. Phản biện lần 4 (`.local/codex-runs/012d-review.json`) ghi 1 lỗi lớn và 14 lỗi nhỏ, đề nghị commit sau vài sửa nhỏ của Claude. Commit đầu giữ đúng công cụ Codex 012d, khớp `tool_sha256` của manifest công bố (41/41 file). Commit thứ hai là phần sửa dưới đây. Không dựng lại lô, không đổi ảnh nào trong art-src, không viết lại manifest; vì vậy hash mã hiện hành khác `tool_sha256` đã công bố, và đó là chủ đích.

| Mục phản biện | Claude sửa |
|---|---|
| Lỗi lớn: chốt `--reference` cho qua đường nối rách | `reference_metrics` ghi `inferred_path_max_jump` và thêm tiêu chí `path_continuity`: bước lớn nhất của đường nối suy ra giữa hai hàng ≤8 px. Đo được: B1 công bố 5, ví dụ xy 4/4, B1 rách theo từng hàng 174. |
| Test chưa ghim tính liền của DP | `regression_012d` thêm ba ca: đường nối metadata của seam-x.png nhảy ≤4 px giữa hai hàng; ô texture.png cắt theo argmin từng hàng của chính chi phí DP phải trượt `path_continuity`; nguồn có bướu sáng giữa overlap thì đường nối DP phải qua chốt, còn cắt thẳng giữa dải phải trượt `cut_continuity`. Ô thử được dựng độc lập với `minimum_path`. |
| Chốt runner 012d không được test | Khối chốt (nội thất decal, nội thất icon, bản sọc 012 phải trượt, phông mới phải qua, khóa đậm xa viền) và ca bản lưu sai hash ở pha một chạy cho cả `rebuild_012c.py` lẫn `rebuild_012d.py`. Vùng dựng giả có sẵn `records/` và hash giả, nên bỏ một chốt sẽ đi tới validation và trượt rõ tên, không còn trượt vì thiếu file đầu ra. |
| Thông báo khóa cũ | probe.sh, audit-probe.sh, normalize_dragon.py, finalize_dragon.py trỏ `rebuild-012d.sh`; report_012b.py trỏ `report-012d.sh`; runner 012b chặn thêm ticket `012d`. |
| Tài liệu | README: art thật bắt buộc `--reference`; seam-check không thấy mảnh vỡ ở mức nội dung nên phải xem đường nối ở 1:1; ngưỡng cắt ghi đúng max(1; p99); partial có thể còn sau link; thêm dòng tiêu chí liền đường nối. Hồ sơ này sửa §2 (partial giảm chứ chưa hết) và §4 (H4–H7 chỉ ghim runner 012c; bộ mutant nằm ngoài Git). README job ghi việc ghim lại test sau khi dựng. |
| example_xy.py | Kiểm WORK trước khi tạo thư mục; đường dẫn ngoài WORK không còn để lại thư mục rỗng. |
| README-normalize: câu “Các dòng True…” sai (bảng 0/32 dòng True) | Không sửa file đã công bố: hash của nó nằm trong `_review/normalize-verification.json` và snapshot của runner kế tiếp đòi đúng hash đó. `report_012d.py` chỉ in câu này khi bảng có dòng True. |

Kiểm sau sửa:

- `seam-check.sh` trên B1 công bố với `--reference pine-river-far.png`: `pass` true, đủ 8 tiêu chí đạt, `inferred_path_max_jump` 5, 0/16 dải trượt.
- Ví dụ xy trong README: `pass` true, bước đường nối lớn nhất 4 ở cả hai trục.
- `test.sh` mã thoát 0; `verify-code.sh` mã thoát 0.

Chạy lại mutant của người phản biện trên bản sao công cụ đã sửa (định nghĩa giữ nguyên trong `code-tests/mutate4.py`, mỗi mẫu một test.sh riêng). Trước sửa, cả tám mẫu đều còn sống.

| Mẫu | Kết quả sau sửa | Ca bắt |
|---|---|---|
| `S3-dp-free-jump` | Trượt test | Ô seam-x có reference trượt `path_continuity` (bước 27 px). |
| `S4-straight-cut-mid` | Trượt test | Ô bướu sáng: đường nối thành cắt thẳng giữa dải, trượt `cut_continuity`. |
| `J-H4-decal-interior-gate-off` | Trượt test | Khối chốt runner 012d đi tới validation. |
| `J-H5-rejected-012-must-fail-off` | Trượt test | Khối chốt runner 012d đi tới validation. |
| `J-H6-strong-key-far-off` | Trượt test | Khối chốt runner 012d đi tới validation. |
| `J-H7-phase1-archive-hash-off` | Trượt test | Runner 012d dịch a.png trước khi thấy bản lưu z sai hash. |
| `J-backdrop-gate-off` | Trượt test | Khối chốt runner 012d đi tới validation. |
| `J-icon-interior-gate-off` (thêm) | Trượt test | Runner 012d bỏ chốt icon, trượt ở chốt số bản ghi thay vì chốt nội thất. |

Các mẫu còn sống khác của phản biện lần 4 (cắt theo dải 64 hàng, các chốt key(), J-canvas-first, J-no-hue-job-list-empty, J-preserve-hue-allow-all…) không được chạy lại và chưa ghim; xem danh sách hoãn.

Hoãn cho chủ dự án hoặc phiếu sau; không mục nào chặn commit:

- Viền tối từ quầng bóng nền xanh trên decal, rõ nhất ở forest-litter.v1 (trở lại mức 012b). Đưa crop 012c/012d cho chủ dự án chọn; nếu cần viền sạch hơn, phiếu sau tách bóng khóa khỏi sơn và thêm chốt độ sáng viền.
- Vòng xanh khóa quanh đốm đã kẹp ở D3: 78 và 113 px có chênh khóa >25.
- B1: mây bị cắt chéo và ngọn thông lơ lửng tại đường nối. Chấp nhận như lỗi thẩm mỹ, hoặc sau này thêm chi phí cắt qua vật thể vào DP.
- Fixture cho các chốt của key(): viền tối, pixel không phải ứng viên, kẹp viền no-key-hue, không phóng to ở flat-bg.
- Dải cắt trượt 16–32 hàng thay dải 64 hàng cố định: đoạn gãy 49 hàng vẫn lọt, một dải của B1 đúng bằng ngưỡng.
- Gương hẹp ở chế độ `--reference`: ô đúng có đuôi ít chi tiết vẫn trượt `mirror`; test chỉ kiểm `criteria['detail']`.
- Làm chắc việc dọn partial khi tín hiệu đến ngay sau os.link trong publish_file.
- Kiểm thư mục symlink trong publish: đích mới phải resolve bên trong ART.
- Chuỗi trợ giúp argparse còn tiếng Anh trên Python 3.9; report-012c.sh/report-012d.sh chạy báo cáo cả khi gọi `--help`.
- mutation_012d.py nhận thư mục bộ mutant làm tham số.
