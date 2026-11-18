# Phiếu 045 · Bộ gợi ý ghép GLB Tripo với ảnh nguồn

Ngày 28/10/2026 · repo cha trên Mac mini M4, Node v24.22.0, ImageMagick 7.1.2-34. Chỉ đọc media, không mạng, không dev server hoặc trình duyệt.

## Kết quả

Đã tạo đúng bốn file mới:

- `tools/tripo-match/match.mjs`: CLI Node ESM, chấm ba thành phần, ghép tham lam, bảng Markdown và JSON tùy chọn, MD5 trước/sau.
- `tools/tripo-match/test/match.test.mjs`: 18 test, gồm từng thành phần trên dữ liệu RAM, GLB tổng hợp JSON/BIN và ma trận ghép cố định.
- `tools/tripo-match/README.md`: cách chạy, công thức, hằng số, giới hạn và lệnh đo lại.
- `docs/codex-queue/045-report.md`: báo cáo này.

| Phép đo đợt 1 | Đúng / tổng | Độ đúng | Đích |
|---|---:|---:|---|
| Top-1 trước ghép | 38/55 | **69,09%** | Không đặt |
| Trong top-3 gốc | 51/55 | **92,73%** | ≥ 90%: đạt |
| Sau ghép một-một | 44/55 | **80,00%** | ≥ 80%: đạt |

Đủ 55 GLB, 57 model ứng viên; số tam giác của **55/55** khớp cột Tam giác trong đáp án. Không thiếu file đáp án và không có GLB chưa được ghi đáp án. Không dùng đáp án khi chấm hoặc ghép; hàm `evaluate` chỉ đối chiếu kết quả sau cùng. Đợt 2 có **86 GLB, 86 model ứng viên**, đã chạy hết, thoát 0; chưa có đáp án nên không công bố độ đúng cho đợt 2.

Bảng đáp án có 56 hàng model/file nhưng chỉ 55 hàng mang tên file `.glb`; mục `loigoi_oni-club` ghi lần thử Tripo CLI, không phải file tải về trong cây này. Giữ cả hai GLB mũ gatekeeper trong mẫu 55, dù một-một không thể cho cả hai cùng đúng. Không gộp bản trùng và không chấp nhận mã rainbow-scout thay rainbow-tank để nâng độ đúng.

## Các dòng sai

Liệt kê hợp của mọi dòng sai top-1, trượt top-3 hoặc sai sau ghép: **20 dòng**. Còn lại 35 dòng đúng cả ba phép đo. Dấu ✓ là ghép đúng; cột Trong top-3 đánh giá ba ứng viên gốc, không phải danh sách sau loại trừ. Nguyên nhân dưới đây là phân tích từ từ khớp, face và tỉ lệ đo, không phải kết quả xem render.

| File Tripo | Đáp án | Top-1 gốc | Trong top-3 | Sau ghép một-một | Nguyên nhân |
|---|---|---|---|---|---|
| `anime+chibi+girl+3d+model.glb` | `loigoi_ma-da` | `loigoi_dokkaebi` | Có | `loigoi_ma-da` ✓ | Tên Tripo không có từ chung với Ma Da; hình Dokkaebi gần hơn chút. Ghép loại trừ sửa được. |
| `bush+3d+model.glb` | `rong_bush-moss` | `rong_bush-blossom` | Có | `rong_bush-moss` ✓ | Cả hai bụi đều khớp bush; tỉ lệ ảnh 2D khác hộp 3D. Ghép loại trừ sửa được. |
| `cartoon+boy+3d+model.glb` | `loigoi_worker-base` | `loigoi_linh-khien` | Có | `loigoi_linh-khien` **sai** | Ba thân nhân vật cùng face 5000, tên boy không chỉ ra thân thợ; hình lính khiên gần hơn và được khóa trước. |
| `catapult+3d+model.glb` | `rong_net-launcher` | `loigoi_linh-giao-dai` | **Không** | `loigoi_worker-base` **sai** | Không có từ khớp Lưới Phóng; 4860 tam giác gần bậc 5000 hơn face 6000 thật. Đây là một ngoại lệ bậc đã ghi trong đáp án. |
| `crab-like+creature+3d+model.glb` | `rong_thorn-ant` | `rong_log` | **Không** | `rong_thorn-ant` ✓ | Crab không đồng nghĩa ant; hộp 3D 1,96 khác ảnh 1,27 nên nhóm đá/gỗ đứng trên. Ghép loại trừ vẫn sửa được. |
| `crystal+insect+3d+model.glb` | `tuyencuoi_rainbow-tank` | `rong_moss-warden` | Có | `tuyencuoi_rainbow-tank` ✓ | Nhãn Rainbow không chứa crystal/insect; hình moss-warden gần hơn. Đáp án ghi scout và tank dùng chung hình; vẫn chấm đúng mã tank. |
| `fantasy+animal+3d+model.glb` | `loigoi_kamaitachi` | `loigoi_trau` | Có | `loigoi_kamaitachi` ✓ | Animal quá chung, không khớp Chồn Liềm; buffalo có tỉ lệ gần hơn. Ghép loại trừ sửa được. |
| `leafy+forest+creature+3d+model.glb` | `rong_moss-archer` | `loigoi_tat-phuong` | Có | `rong_moss-archer` ✓ | Tên không nói archer; các nhân vật cùng bậc có hình gần nhau, leafy không có trong nhãn Yêu Rêu Cung. Ghép loại trừ sửa được. |
| `rock+cluster+3d+model.glb` | `rong_river-stones` | `rong_river-stones` | Có | `rong_rock-slab` **sai** | Đúng top-1 nhưng dòng steps khóa river-stones trước; ảnh phối cảnh và đồng nghĩa rock/stone không đủ phân biệt. |
| `rocky+stone+steps+3d+model.glb` | `rong_rock-slab` | `rong_river-stones` | Có | `rong_river-stones` **sai** | Rock và stone được gom; steps chưa khớp phiến. River-stones có điểm hình cao hơn và khóa mất ứng viên của dòng cluster. |
| `round+woven+racket+3d+model.glb` | `loigoi_helper-fan` | `loigoi_worker-kit-dong-rammer` | **Không** | `loigoi_worker-kit-dong-rammer` **sai** | Racket khác fan về nghĩa; tỉ lệ GLB 4,73 so với ảnh 0,83 khiến gậy dài đứng trên, rồi chiếm rammer. |
| `samurai+kid+3d+model.glb` | `loigoi_linh-giao-dai` | `loigoi_linh-giao-dai` | Có | `rong_net-launcher` **sai** | Đúng top-1 nhưng dòng character khóa lính giáo trước; ghép tham lam đẩy dòng này sang net-launcher. |
| `stylized+3d+character+model.glb` | `loigoi_linh-khien` | `loigoi_linh-giao-dai` | Có | `loigoi_linh-giao-dai` **sai** | Tên không có shield; hai lính cùng face 5000 và tỉ lệ sát nhau, lính giáo đứng trên. |
| `stylized+tree+3d+model.glb` | `rong_pine-round` | `rong_tree-violet` | Có | `rong_pine-round` ✓ | Tree chung cho nhiều cây; tree-violet khớp từ và hình nhỉnh hơn. Purple ở dòng khác khóa violet nên ghép sửa được. |
| `tree+creature+3d+model.glb` | `rong_moss-grunt` | `rong_tree-violet` | Có | `rong_moss-grunt` ✓ | Tree khớp cả cây trang trí; điểm chữ có thể vượt hình đúng dù face thấp hơn. Ghép loại trừ sửa được. |
| `viking+helmet+3d+model (1).glb` | `loigoi_worker-kit-gatekeeper-head` | `loigoi_worker-kit-scholar-head` | Có | `loigoi_helper-fan` **sai** | Hai GLB cùng một id thật; ràng buộc một-một chỉ cho dùng mũ một lần. Dòng này bị đẩy sang quạt, không có ngoại lệ để nâng số đo. |
| `viking+helmet+3d+model.glb` | `loigoi_worker-kit-gatekeeper-head` | `loigoi_worker-kit-scholar-head` | Có | `loigoi_worker-kit-gatekeeper-head` ✓ | Hat/helmet khớp nhiều mũ; hộp mũ scholar gần hơn ảnh gatekeeper. Ghép loại trừ chọn đúng bản này. |
| `wooden+battle+club+3d+model.glb` | `loigoi_dokkaebi-club` | `loigoi_oni-club` | Có | `loigoi_oni-club` **sai** | Nhãn chỉ ghi Gậy của Dokkaebi, không ghi gỗ; club khớp cả Oni. Hình chùy Oni gần hơn, ghép khóa nhầm. |
| `wooden+rope+whip+3d+model.glb` | `loigoi_worker-kit-dong-rammer` | `loigoi_worker-kit-dong-rammer` | Có | `loigoi_dokkaebi-club` **sai** | Đúng top-1 nhưng dòng racket khóa rammer trước; rope/whip không có trong nhãn Cây thông nòng nên không đủ điểm giữ ứng viên. |
| `wooden+toy+airplane+3d+model.glb` | `loigoi_chuon-chuon-tre` | `loigoi_tre-mallet` | **Không** | `loigoi_linh-giao-dai-spear` **sai** | Airplane không phải dragonfly/Chuồn Chuồn; tỉ lệ GLB 7,11 khác ảnh 2,63. Điểm vật liệu và hình ưu tiên đồ dài khác. |

Bốn dòng trượt top-3: `catapult`, `crab-like+creature`, `round+woven+racket`, `wooden+toy+airplane`. Ghép một-một cứu được dòng crab nhưng có thể làm hỏng top-1 đúng ở các dòng khác; không xem ghép tham lam là bảo đảm chất lượng.

## Hằng số và căn cứ

Các hằng số chung trong `CONFIG`, áp dụng giống nhau cho hai đợt:

| Hằng số | Giá trị | Lý do |
|---|---:|---|
| `minimumFaces` | 3000 | 20 GLB từ thư mục face 2000 có 2748–2966 tam giác, tức 1,374–1,483 lần face khai báo; so với sàn 3000 là 0,916–0,988667. Không phạt sai toàn nhóm. |
| `faceLow`, `faceHigh` | 0,55; 1,02 | 35 GLB còn lại nằm trong 0,7265–0,998 lần face. Khoảng rộng chấp nhận model được giảm lưới nhiều, còn bậc quá thấp/cao bị trừ mạnh. |
| `faceTarget` | 0,95 | Giá trị chung biểu diễn lưới thường sát dưới face đã đặt. |
| `faceReward`, `faceSlope`, `facePenalty` | 35; 35; 45 | Trong bậc: `35 - 35 × abs(log(r/0,95))`; ngoài bậc: `-45 - 35 × abs(log(r/0,95))`. Vẫn ưu tiên bậc gần đúng trong khoảng cho phép. |
| `shapeWeight`, `shapeScale` | 25; 0,4 | `25 × exp(-abs(log(g/i))/0,4)`, đối xứng theo log và nhẹ hơn tên vật khớp rõ. |
| `nameWeight` | 60 | Tỉ lệ trọng số từ truy vấn khớp với id/tên Anh/nhãn Việt. Từ vật liệu wood chỉ nặng 0,3, các từ khác 1. |

Không tìm bộ hằng số riêng theo GLB, id hay game. Lượt đầu với cùng CONFIG đạt 35/55 top-1, 51/55 top-3 và 39/55 một-một. Sau chuẩn hóa từ chung (màu, băng đô, pinecone, kính/cuốc/giỏ; phân biệt boar với piggy), lượt cuối đạt bảng trên. Các bổ sung là từ/cụm nghĩa dùng lại được, không có bảng ánh xạ đầy đủ tên Tripo sang model. Chưa có tập kiểm độc lập có nhãn; số đo trên tập hiệu chỉnh đợt 1 không bảo đảm độ đúng đợt 2.

Đọc và đo theo phiếu: nhập `inspectGlb` của 025, scene 0, nhân instance node; ảnh front/đơn được trim bằng lệnh ImageMagick đã chỉ định. Gom nhiều góc và biến thể theo id, chọn ảnh trước khi chấm; không chọn góc có điểm cao nhất. Rộng GLB là `max(X,Z)/Y`. Bộ ghép xét tất cả ứng viên, khóa cặp còn trống theo điểm giảm dần, luôn giữ top-3 gốc.

## Năm kiểm bắt buộc

| # | Lệnh / phép kiểm | Kết quả |
|---:|---|---|
| 1 | `node tools/tripo-match/match.mjs --upload typing-game-handoff-2026-10-25/tripo-upload`; đối chiếu đáp án bằng `evaluate` như README | **Đạt**, CLI thoát 0, 55 dòng, 0 lỗi/cảnh báo; top-1 38/55, top-3 51/55, một-một 44/55. Hai đích đều đạt. |
| 2 | `node tools/tripo-match/match.mjs --upload typing-game-handoff-2026-10-25/tripo-upload-dot2` | **Đạt**, thoát 0, bảng 86 GLB/86 ứng viên, 0 lỗi/cảnh báo, MD5 177 file không đổi. Kiểm thêm nhánh rỗng bằng `--glb tools/tripo-match/test`: in `0 GLB`, thoát 0. |
| 3 | `node --test tools/tripo-match/test` | **Không đạt nguyên văn**: Node v24.22.0 coi đường dẫn thư mục là module, báo `MODULE_NOT_FOUND`, thoát 1. Lệnh tương thích `node --test tools/tripo-match/test/*.test.mjs` **đạt 18/18**, thoát 0. Không thêm index/package vào thư mục test vì ngoài bốn file được phép. |
| 4 | Snapshot MD5 trước khi viết/chạy công cụ, so toàn cây hai upload sau khi chạy và test | **Đạt: 304/304 không đổi**, gồm 141 GLB và 163 PNG; 0 thêm, xóa, đổi. Riêng công cụ kiểm 120 file đợt 1 và 177 file đợt 2; 7 ảnh còn lại ngoài thư mục face vẫn được snapshot độc lập kiểm. |
| 5 | `git status --short`, đối chiếu mốc đầu; `git status --short --untracked-files=all -- tools/tripo-match docs/codex-queue/045-report.md` | **Phần của phiếu đạt:** đúng bốn file mới, không sửa/xóa file cũ. **Toàn repo không đạt nguyên văn điều kiện chỉ thêm bốn file** vì có thay đổi đồng thời của làn khác; ghi mốc và sai khác bên dưới. Không chạy Git có ghi để làm sạch chúng. |

Lệnh đo lại top-1/top-3/một-một, parser đáp án và bảng lỗi có sẵn trong README. Bộ test không chạy build hay test suite của bất kỳ game nào. `git diff --check` không báo lỗi; các file mới cũng được kiểm khoảng trắng riêng vì chưa được Git theo dõi.

### MD5 toàn phiên

Chụp từng đường dẫn và MD5 trước khi đọc metadata/ảnh; giữ bảng trong bộ nhớ công cụ phiên, không tạo snapshot cạnh media. Sau khi chạy, so lại cả tập đường dẫn lẫn MD5: 304 trước, 304 sau, 0 khác. SHA-256 của bảng MD5 chuẩn hóa sau khi xác nhận bằng nhau:

```text
d168ada56ee479f52288417c50c509b26f2c3621ac466c30461b42f54788b067
```

Chuẩn hóa: sắp đường dẫn, nối `đường_dẫn + NUL + md5 + LF`, SHA-256 UTF-8. Công cụ cũng tự băm trước/sau từng file đã đọc, từ chối kết quả nếu media đổi.

### Git đầu phiên

```text
 M docs/CODEX_QUEUE.md
 M games/dragon-hold
 M games/typing-defense
 M games/typing-survival
?? .claude/launch.json
?? TU_TIEN_TYPING_SYSTEMS_AND_5_COMBAT_OPTIONS_V2_2026-10-24.md
?? docs/codex-queue/045-tripo-glb-matcher.md
?? docs/tools/map-factory/
```

Trong các lần đối chiếu xuất hiện thêm thay đổi ngoài phạm vi của công việc đồng thời, gồm `docs/games/dragon-lane/03-our-side-shop-traps-support.md` và các file mới `docs/codex-queue/035-ts-first-frame.md`, `docs/codex-queue/036-td-fx-pipe.md`. Không đọc/sửa nội dung chúng trong phiếu này. Dòng thư mục `docs/tools/map-factory/` trong status ngắn là mục đã có từ đầu, không được coi là thay đổi của phiếu 045. Phần riêng 045 ở cuối phiên gồm đúng:

```text
?? docs/codex-queue/045-report.md
?? tools/tripo-match/README.md
?? tools/tripo-match/match.mjs
?? tools/tripo-match/test/match.test.mjs
```

## Việc bỏ qua và phần chủ dự án cần xem

- Không tạo/chỉnh ảnh, âm thanh hoặc GLB; phiếu chỉ viết công cụ. Không chép/xóa media, không chạm Tu Tiên, game code, game docs, audio-lab; không mạng hoặc trình duyệt; không commit/push/reset/clean/stash.
- Không tạo file JSON kết quả thật trong phiên vì không có đường dẫn `.json` nào trong bốn file được phép ghi. Chức năng `--out` đã có; test kiểm roundtrip JSON và chặn đầu ra vào media/ghi đè, nhưng chưa kiểm ghi JSON thật ra đĩa.
- Cần duyệt bằng mắt bảng sai, nhất là bốn dòng trượt top-3 và hai bản mũ trùng. Với đợt 2, nhiều nhà/kit cùng face và tên tải chung vẫn có thể bị tráo khi ghép. Công cụ không tự nhập model.
- Để chạy test trên Node hiện tại dùng glob trong README; kết quả lệnh thư mục bắt buộc được ghi là không đạt, không đánh dấu đã qua.


## Claude duyệt (28/10/2026)

- **Chạy lại test:** `node --test tools/tripo-match/test/*.test.mjs`, 18/18 đạt.
- **Độ đúng trên đợt 1** (55 file có đáp án): top-3 92,7 %, ghép một-một 80 %. Cả hai đạt đích. Công cụ chỉ là ý kiến thứ tư: đợt 2 vẫn ghép bằng ba người ghép độc lập xem ảnh render, cộng một người phân xử.
- **Đã dùng ngay** cho đợt 2: 86 GLB chủ dự án tải về lúc 00:07–00:15 ngày 28/10.
