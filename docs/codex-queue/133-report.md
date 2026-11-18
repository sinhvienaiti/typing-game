# Phiếu 133 · Wordwoven · Mười loại lời gọi

Ngày làm: 29/10/2026, repo cha trên macOS. **Đã tạo đủ 10 ảnh và 30 bản thu, giữ 11 lượt sinh cùng prompt. Chưa đóng phiếu: kiểm mở rộng trên bản thu phát hiện ngoại lệ alpha và sắc khóa, bảng dưới ghi nguyên số trượt. Chưa có chấm nhận của Claude.**

## 1. Nơi giao và phạm vi

- Bộ ảnh: [ui/calls/](../../games/typing-defense/art-src/ui/calls/): mỗi tên có `.png` 1024² sRGBA, `.256.png`, `.128.png`, `.64.png`, prompt bản chọn, prompt từng bản thu và mọi `.tryN.png`/`.tryN.prompt.txt`.
- [Tờ xem bốn hàng](../../games/typing-defense/art-src/_review/133-sheet.jpg).
- [10 ảnh trong một hàng ở đúng 18 px trên đế thẻ enough](../../games/typing-defense/art-src/_review/133-18px-cards.jpg), [bản phóng nearest để soi pixel](../../games/typing-defense/art-src/_review/133-18px-cards-zoom.jpg).
- [Đủ 18/20/24 px trên hai nền khung 115](../../games/typing-defense/art-src/_review/133-sizes.jpg).
- [Script và hồ sơ kiểm](../../games/typing-defense/art-src/_review/133/), [số đo cuối](../../games/typing-defense/art-src/_review/133/final-check/metrics.json), [kết quả kiểm tổng](../../games/typing-defense/art-src/_review/133/final-check/audit.json).

Chỉ thêm file trong các đường dẫn của phiếu. Không chạy lệnh Git, game, build, test suite, dev server hay trình duyệt. Không làm âm thanh, tích hợp mã hoặc chép vào `public/`; các việc đó ngoài phiếu. Không đọc/ghi Tu Tiên, `.wt-*` hoặc ghi game khác. Không xóa file nào, kể cả lượt không chọn. Không có capture trình duyệt hay raw frame cần prune.

## 2. Tham chiếu, prompt và lượt sinh

Sinh bằng công cụ tích hợp **`image_gen`**, một lời gọi cho mỗi ảnh/lượt, tổng **11 lượt**. Mỗi lượt đính kèm đúng ba ảnh: `ui/frames-epic/panel-large.v2.png`, `ui/title-epic/keyart.png` và `_refs/owner-epic-2026-10-28.webp`. Ảnh 115 thực tế ở **`frames-epic/`**, không phải đường dẫn `frames/` ghi trong phiếu; vì đã có ảnh nên không phải chờ.

Prompt bắt đầu nguyên văn STYLE-UI mới của AD và khối ICON trong tài liệu định dạng. Phần riêng sau đó ghi rõ ưu tiên mỹ thuật mới: khối có chiều sâu, chất liệu hoàn thiện, không viền mực/không tô phẳng theo khối cũ; một cụm vật, khoảng hở lớn, cạnh dài 70%, điểm sáng ngà/vàng. Kết thúc bằng dòng nền M nguyên văn. Không dùng chữ, số, dấu hỏi, logo hoặc khung trong ảnh; “word-arrow” là mũi tên ánh sáng, không có chữ.

Prompt chính xác nằm cạnh mọi lượt và bản chọn; `prompts.json` giữ lượt 1, `call-interrupt.try2.prompt.txt` giữ bản sửa lượt 2. Không gán prompt lượt 1 cho lượt 2.

| Tên | Thay đổi prompt / lựa chọn |
|---|---|
| `call-power` | Cung lưỡi liềm mở bên trái; tên vàng chạy ngang, dây tạo tam giác rỗng. Giữ try1. |
| `call-build` | Búa và đá thành khối chữ L chéo, đầu búa lớn và mặt đá sáng. Giữ try1. |
| `call-harvest` | Bó lúa xòe bên phải, liềm cong bên trái. Giữ try1. |
| `call-chop` | Đầu gỗ tròn nhìn thẳng, rìu cắm chéo. Giữ try1. |
| `call-mine` | Đầu cuốc chữ T rộng, quặng góc cạnh ở dưới phải. Giữ try1. |
| `call-quiz` | Giấy mở rộng, hai trục cuộn lớn và ấn đồng ở góc; thay dấu hỏi bằng nét mây để không tạo ký tự. Giữ try1. |
| `call-spell` | Lông nhọn chéo, ba khối lửa lớn bám vào lông, sáng nằm trong hình. Giữ try1. |
| `call-interrupt` | Try1: bàn tay bên trái và trống lớn bên phải; ở 18 px bàn tay còn chìm. Try2: yêu cầu tay chiếm 85% chiều cao, 75% diện tích, các ngón xòe với khe rộng, trống còn 25% chiều cao ở chân. Chọn try2; giữ nguyên try1. |
| `call-anchor` | Neo đứng với hai ngạnh rộng và chuỗi xích ngắn bên phải. Giữ try1. |
| `call-shield-break` | Vòm thấp rộng, khe nứt lớn xuyên giữa hai nửa. Giữ try1. |

11/11 PNG thử trùng MD5 nguồn công cụ, kiểm tại `final-check/audit.json`. File nguồn công cụ được ghi trong từng `.source.json`; mọi lượt thử giữ nguyên byte.

## 3. Hậu kỳ và tờ bản sinh | bản hậu kỳ

Nguồn công cụ vuông 1254²; bản thử giữ nguyên khổ đó. Bản giao tách nền M bằng bản sao nguyên trạng của bốn file `tools/art-normalize` nằm trong review, nên WORK của công cụ cũng nằm trong vùng được phép ghi. Lệnh chính:

```sh
export ART_MAGICK=/opt/homebrew/bin/magick
bash .../art-normalize/key-alpha.sh IN.tryN.png OUT.key.png \
  --bg '#FF00FF' --mode global --despill protect-interior --no-key-hue
```

Sau đó trim alpha, thu Lanczos fit 717×717, đặt giữa canvas trong suốt 1024² và xuất PNG32 sRGB. Không chỉnh sáng, gamma hay phủ màu, không làm phẳng hoặc xóa phần vẽ. Chốt alpha ngoài dải mép 3 px theo mặt nạ alpha 50%: chỉ đưa alpha lẻ về 0/255, giữ nguyên toàn bộ RGB và alpha trong dải mép. Số pixel alpha được chốt trên bản chọn: `{"call-power": 1868, "call-build": 3, "call-harvest": 265, "call-chop": 7, "call-mine": 13, "call-quiz": 2, "call-spell": 132, "call-interrupt": 36, "call-anchor": 10, "call-shield-break": 206}`. Có nhật ký từng chuyển đổi alpha trong `.alpha-clean.json`.

Mỗi bản thu đều thu **Lanczos trực tiếp từ bản 1024**, không nối chuỗi từ cỡ trung gian, không làm nét 64. Đã đối chiếu pixel: **30/30 bản thu trùng phép thu trực tiếp**. Chính kiểm mở rộng trên những bản thu này phát hiện ngoại lệ ở mục 5; không giấu bằng một bước sửa sau đó.

Mười tờ so cuối, cùng cỡ canvas 256², nền hậu kỳ lấy từ panel 115:

- [`call-power`](../../games/typing-defense/art-src/_review/133/call-power.compare-panel.jpg).
- [`call-build`](../../games/typing-defense/art-src/_review/133/call-build.compare-panel.jpg).
- [`call-harvest`](../../games/typing-defense/art-src/_review/133/call-harvest.compare-panel.jpg).
- [`call-chop`](../../games/typing-defense/art-src/_review/133/call-chop.compare-panel.jpg).
- [`call-mine`](../../games/typing-defense/art-src/_review/133/call-mine.compare-panel.jpg).
- [`call-quiz`](../../games/typing-defense/art-src/_review/133/call-quiz.compare-panel.jpg).
- [`call-spell`](../../games/typing-defense/art-src/_review/133/call-spell.compare-panel.jpg).
- [`call-interrupt`](../../games/typing-defense/art-src/_review/133/call-interrupt.compare-panel.jpg).
- [`call-anchor`](../../games/typing-defense/art-src/_review/133/call-anchor.compare-panel.jpg).
- [`call-shield-break`](../../games/typing-defense/art-src/_review/133/call-shield-break.compare-panel.jpg).

Các tờ `.before-after.jpg`, `.clean.before-after.jpg`, `.compare.jpg` khác là hồ sơ trung gian, có nền mẫu tạm; dùng **`.compare-panel.jpg`** khi duyệt cuối. Tự chấm ở mục 6 trên đúng bản hậu kỳ được giao, đã xem cả bản 1024 và cỡ sử dụng.

## 4. KA1 và khổ

Các thư mục đích chưa có file lúc bắt đầu. `md5-before.txt` rỗng (**0 file**); `md5-after.txt` dùng `md5 -r` cho toàn bộ calls, review/133, các tờ 133 và báo cáo, dự kiến **387 file**, trừ hai file tự tham chiếu `md5-after.txt`, `md5.diff.txt`. `md5-before.txt` vẫn được băm trong mốc sau. Đối chiếu bằng `md5.diff.txt`: chỉ thêm, không sửa/xóa file có trước phiếu.

`final-check/identify.txt` ghi đủ lệnh `identify -format '%f %wx%h %[channels]\n'` cho **40/40 file giao**: 10 bản 1024² và ba cỡ thu 256²/128²/64²; tất cả **srgba**. Cạnh dài alpha >16 của cả 10 bản gốc là **717/1024 = 70,0195%**; lệch tâm lớn nhất **0,04883%**, dưới 2%.

## 5. Kiểm số và ngoại lệ phải giữ lại

Hai nền cuối lấy trực tiếp từ `panel-large.v2.png`: chuẩn về canvas 1024², trung bình ROI ngọc `200x200+412+412` cho **#061e16**; ROI đá vôi `200x20+412+26` cho **#b8aa94**. Hồ sơ ứng viên dùng màu tạm của phiếu; hồ sơ **final-check** và tờ xem cuối dùng hai màu đo này.

Luma là Rec.709 trên sRGB chuẩn hóa 0–1; trung bình vật có trọng số alpha. Bảng ghi chênh luma với nền ngọc ở đúng 18/20/24 px. Nền đá vôi cũng được đo trong JSON. IoU dùng mặt nạ alpha >16, thu trực tiếp bằng Lanczos về 18 và 32 px, so đủ 45 cặp mỗi cỡ. Không có cặp sáng/tắt trong phiếu.

| Bản 1024 | Alpha lẻ ngoài mép 3 px | Sắc khóa / pixel alpha >0 (%) | Δ luma ngọc: 18 / 20 / 24 | IoU max 18 px · cặp | IoU max 32 px · cặp |
|---|---:|---:|---|---|---|
| `call-power` | 0 | 0.0597 | 0.4871 / 0.4850 / 0.4849 | 0.5536 · `call-shield-break` | 0.4057 · `call-shield-break` |
| `call-build` | 0 | 0.0376 | 0.4466 / 0.4465 / 0.4466 | 0.6452 · `call-shield-break` | 0.5973 · `call-interrupt` |
| `call-harvest` | 0 | 0.0724 | 0.4744 / 0.4743 / 0.4735 | 0.6838 · `call-interrupt` | 0.6465 · `call-interrupt` |
| `call-chop` | 0 | 0.0238 | 0.4052 / 0.4051 / 0.4048 | 0.6838 · `call-mine` | 0.6432 · `call-mine` |
| `call-mine` | 0 | 0.0316 | 0.4089 / 0.4081 / 0.4079 | 0.6838 · `call-chop` | 0.6578 · `call-interrupt` |
| `call-quiz` | 0 | 0.0211 | 0.5273 / 0.5279 / 0.5282 | 0.6824 · `call-chop` | 0.6295 · `call-mine` |
| `call-spell` | 0 | 0.0251 | 0.5254 / 0.5263 / 0.5267 | 0.6050 · `call-shield-break` | 0.5916 · `call-harvest` |
| `call-interrupt` | 0 | 0.0542 | 0.5119 / 0.5106 / 0.5090 | 0.6838 · `call-harvest` | 0.6578 · `call-mine` |
| `call-anchor` | 0 | 0.0697 | 0.3876 / 0.3849 / 0.3881 | 0.6903 · `call-shield-break` | 0.6074 · `call-shield-break` |
| `call-shield-break` | 0 | 0.1028 | 0.4610 / 0.4607 / 0.4617 | 0.6903 · `call-anchor` | 0.6168 · `call-quiz` |

**10/10 bản 1024 đạt** khổ, lề, alpha, sắc khóa ≤0,2%; tương phản cỡ dùng ≥0,25 trên ngọc; mọi cặp IoU ≤0,80 ở cả 18 và 32 px. Bản 18 px trên thẻ enough lấy mẫu từ đúng `tmp/ui-imagery/sheet-td-theme-1280.jpg`, vùng thẻ `82x28+869+243`; mở rộng phần nền trống ở chân thẻ để đặt 10 icon, không phóng icon. Không phải ảnh chụp runtime mới.

### Ngoại lệ trên bản thu — chưa đạt kiểm tổng

Áp dụng thêm cùng phép alpha/sắc khóa cho **mọi bản thu**, có **26/30** bản không qua ít nhất một ngưỡng. Mỗi ô là **pixel alpha lẻ ngoài mép 3 px / phần trăm sắc khóa**:

| Tên | 256 px | 128 px | 64 px |
|---|---:|---:|---:|
| `call-power` | 17 / 0.0455% | 4 / 0.2728% | 0 / 1.5682% |
| `call-build` | 0 / 0.0174% | 2 / 0.0000% | 0 / 0.0000% |
| `call-harvest` | 203 / 0.0357% | 83 / 0.0000% | 35 / 0.0684% |
| `call-chop` | 5 / 0.0000% | 3 / 0.0000% | 0 / 0.0000% |
| `call-mine` | 6 / 0.0332% | 2 / 0.0000% | 3 / 0.0000% |
| `call-quiz` | 2 / 0.0047% | 12 / 0.0000% | 9 / 0.0000% |
| `call-spell` | 76 / 0.0264% | 30 / 0.0244% | 15 / 0.0881% |
| `call-interrupt` | 5 / 0.0390% | 13 / 0.0418% | 4 / 0.0000% |
| `call-anchor` | 18 / 0.0295% | 15 / 0.0267% | 3 / 0.0000% |
| `call-shield-break` | 3 / 0.0188% | 3 / 0.0236% | 0 / 0.0870% |

Riêng cung tên có sắc khóa **0,2728% ở 128**, **1,5682% ở 64**. Ở 64, 13 pixel mang sắc khóa có alpha **24–29**, không phải phần sơn đục. `edge-details.json` giữ phân bố alpha và kiểm đối chiếu cách xác định mép bằng các ngưỡng 0%, 6,27451% và 50%; không chọn lại định nghĩa mép để đổi trượt thành đạt.

Theo **ART_ACCEPTANCE §5**, dừng việc ép các số này bằng cách bỏ nét nhỏ hoặc lấp khoảng rỗng: ở lúa, dây cung và lửa, đó có thể làm mất phần vẽ. Các bản thu giữ nguyên phép Lanczos và được đưa ra duyệt, không tự tuyên bố ngoại lệ đã được nhận. Bước làm sạch alpha sau thu có thể là hướng xử lý tiếp, nhưng cần đối chiếu tranh ở cỡ thật trước khi quyết, không được coi là miễn kiểm mặc nhiên.

Tôi đã xuất bản chọn trước khi mở rộng kiểm alpha sang toàn bộ bản thu; đây là thiếu sót quy trình của lượt này. Không ghi đè các file vừa giao vì phiếu cấm ghi đè file có sẵn. Không khẳng định các ngoại lệ là bất khả thi để sửa; báo rõ điểm còn thiếu để Claude quyết cách giữ tranh và chốt hậu kỳ. `final-check/audit.json` giữ **pass: false**.

## 6. KA5 — tự chấm mức chợ và đọc 18 px

Thứ tự Q: **Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp**. “Dùng tiếp” chỉ **1**, vì chưa qua toàn bộ kiểm trên bản thu. Ở 720p, chủ thể chính nhận ra nhưng các họa tiết đồng, chuỗi xích, hạt lúa và trống chỉ còn mảng màu, nên Đọc được chấm 1. M so mức hoàn thiện icon HUD thương mại trong ảnh chủ dự án, không so mức bộ cũ. Không coi tự chấm là nghiệm thu.

| Tên | M gốc | Q gốc | M 720p | Q 720p (18 px) | Tên Codex đọc ra ở 18 px |
|---|---:|---|---:|---|---|
| `call-power` | 8,5 | 9 = 2/2/2/2/1 | 8 | 8 = 2/1/2/2/1 | Bow and arrow · cung đang kéo tên sáng |
| `call-build` | 8,5 | 9 = 2/2/2/2/1 | 8 | 8 = 2/1/2/2/1 | Mason hammer · búa bổ đá |
| `call-harvest` | 8,5 | 9 = 2/2/2/2/1 | 8 | 8 = 2/1/2/2/1 | Rice and sickle · bó lúa với liềm |
| `call-chop` | 8,5 | 9 = 2/2/2/2/1 | 8 | 8 = 2/1/2/2/1 | Axe and log · rìu cắm gỗ tròn |
| `call-mine` | 8,5 | 9 = 2/2/2/2/1 | 8 | 8 = 2/1/2/2/1 | Pickaxe and gold · cuốc trên quặng vàng |
| `call-quiz` | 8,5 | 9 = 2/2/2/2/1 | 8 | 8 = 2/1/2/2/1 | Scroll · cuộn giấy có ấn |
| `call-spell` | 8,5 | 9 = 2/2/2/2/1 | 8 | 8 = 2/1/2/2/1 | Burning feather · lông chim cháy |
| `call-interrupt` | 8,5 | 9 = 2/2/2/2/1 | 8 | 8 = 2/1/2/2/1 | Stop hand · bàn tay giơ chặn, trống nhỏ ở chân |
| `call-anchor` | 8,5 | 9 = 2/2/2/2/1 | 8 | 8 = 2/1/2/2/1 | Anchor · mỏ neo |
| `call-shield-break` | 8,5 | 9 = 2/2/2/2/1 | 8 | 8 = 2/1/2/2/1 | Split dome · vòm khiên vỡ đôi |

**10/10 nhận ra vật chính ở 18 px trong lượt tự xem có biết brief**, không phải phép thử mù hay kết quả giám khảo độc lập. Chất liệu, bevel, màu ngọc–ngà–vàng và ánh sáng đứng cạnh được HUD mẫu ở mức M 8; các nét chạm rất dày ở bản lớn, và không trông đợi chúng còn đọc riêng ở 18 px. `call-interrupt` được sinh lại vì ưu tiên cử chỉ bàn tay thay vì chỉ đạt IoU.

## 7. Chạy lại và việc Claude cần xem

Không sinh ảnh lại khi chạy kiểm. Script từ chối ghi đè; dùng tên thư mục mới:

```sh
export ART_MAGICK=/opt/homebrew/bin/magick
PYTHONDONTWRITEBYTECODE=1 python3 \
  games/typing-defense/art-src/_review/133/run-final.py check recheck-owner-01
```

Lệnh trả **1** khi còn ngoại lệ; xem JSON thay vì coi mã chạy là đạt. `workflow.py` ghi nguồn/tách nền/chuẩn hóa, `finish-clean.py` chốt alpha master, `deliver.py` xuất bộ và ba bản thu, `run-final.py` áp màu panel và dựng tờ xem, `extra-sheets.py` dựng cỡ thật, `recheck-final.py` kiểm ảnh/nguồn/prompt, `audit-edge-details.py` giữ bằng chứng mép, `make-report.py` dựng báo cáo, `workflow.py audit` ghi mốc MD5 sau. Không chạy lại các bước xuất vào tên đã có.

**Còn lại:** Claude xem mười tờ bản sinh | hậu kỳ, tờ 18 px ở 100%, các ngoại lệ trên bản thu; chấm lại M/Q và quyết cách xử lý ngoại lệ alpha mà giữ tranh. **Chưa nhận, chưa chép `public/`, chưa đánh dấu xong điều kiện mọi kiểm 1–5.** Không sửa tài liệu thay ảnh khác vì ngoài đường dẫn cho phép.
