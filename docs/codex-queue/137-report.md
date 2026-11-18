# Phiếu 137 · Dragonhold · HUD và trạng thái

Ngày 29/10/2026. Đã giao đủ 10 ảnh cùng ba bản thu, prompt, mọi lượt sinh và bằng chứng kiểm. **Chờ Claude chấm lại; chưa coi là đã nhận.** Không gắn vào `public/`.

## 1. File giao và nguồn mỹ thuật

Thư mục: `games/dragon-hold/art-src/ui/icons/`.

Mười tên: `wave-horn`, `chain`, `dragon-rage`, `armour`, `shield`, `phase-prep`, `phase-fight`, `phase-break`, `fast-forward`, `danger`.

Mỗi tên có `<tên>.png` 1024²; `.256.png`, `.128.png`, `.64.png`; `<tên>.prompt.txt`. Tổng cộng **40 PNG giao + 10 prompt chọn**. Mỗi bản thu dùng Lanczos trực tiếp từ bản 1024, không làm nét. File giao là sRGB RGBA 8 bit; ImageMagick tại máy ghi kênh `srgba 4.0` (srgba, bốn kênh).

Công cụ sinh: **image_gen tích hợp**, không dùng API ngoài. Nguồn sinh trả về 1254², giữ nguyên ở `.tryN.png`; bản chọn được tách nền và chuẩn hóa về 1024². Có 11 lượt sinh: chín ảnh một lượt, `danger` hai lượt; giữ cả 11 PNG và 11 prompt. Tổng cộng 72 file mới trong thư mục icon.

Đã đọc AD 28/10 §3, ART_ACCEPTANCE §2.2, định dạng 05-icons, UI_IMAGERY và UIC-DH-1; đã xem `skill-fire-breath.png`, `gold.png`, ảnh chủ dự án, ảnh trận chỉ định. Chưa có ảnh chọn 119 trong `ui/title-epic/` lúc kiểm. Dùng nguyên văn **STYLE-UI mới của AD**, không dùng khối sách tranh cũ. KIND ICON cụ thể hóa một vật hoàn chỉnh, dáng gọn, sáng tối lớn, không khung bọc, không chữ. Nền nguồn **M #FF00FF**.

## 2. Prompt và hậu kỳ từng lượt

Prompt tiếng Anh đầy đủ nằm cạnh mỗi ảnh; bản chọn khớp byte với prompt lượt chọn. STYLE-UI được giữ nguyên. Các quyết định riêng của lượt 1:

| Ảnh | Lượt 1 |
|---|---|
| wave-horn | Sừng ngà dáng lưỡi liềm, hai đai sắt, miệng loe có lòng tối; không dây đeo |
| chain | Đúng ba mắt xích, bố cục chéo, lỗ giữa rộng, mặt kim loại nóng và khe than hồng |
| dragon-rage | Mắt hổ phách có đồng tử dọc, vảy và ba khối lửa móc quanh mắt; không huy hiệu tròn |
| armour | Ba lớp giáp vảy, dáng cao nhọn; tách rõ khỏi khiên tròn |
| shield | Khiên granite và đồng, núm giữa lớn; hoa văn bảo hộ là phù điêu không thành chữ rune |
| phase-prep | Búa ngang bó ba cọc, đầu búa và mặt cọc lớn sáng |
| phase-fight | Hai lưỡi rộng thành chữ thập chéo, lửa giữa, khoảng âm giữa các nhánh |
| phase-break | Hai khúc củi, ngọn lửa gọn và dải khói kem uốn rõ; không sương mờ |
| fast-forward | Hai chevron riêng hướng phải, nằm cùng hàng, có khoảng trống giữa; không nền nút |
| danger | Dấu kim loại răng cưa với lõi men cam đỏ, mặt vàng sáng; lượt này quá mảnh trên cảnh trận |

**Lượt 2 chỉ có danger:** tăng bề ngang, yêu cầu thân zigzag đặc, mặt kim loại lớn sáng, giảm hoa văn; giữ lõi cam đỏ và mép sắt. Chọn lượt 2. Không sinh lượt 3.

Hậu kỳ xác định: `tools/art-normalize` tách M ở chế độ global, despill protect-interior, bật no-key-hue vì vật không chứa sắc khóa. WORK được chuyển vào `_review/137/work/`, không ghi thư mục tạm của công cụ ngoài phạm vi. Cắt theo alpha >16, giữ tỉ lệ, Lanczos cạnh dài 717 px rồi đặt giữa canvas 1024². Dọn đuôi alpha ≤4; kẹp những pixel bán trong suốt ngoài dải mép Chebyshev 3 px về 0/255. Không vẽ lại vật bằng mã.

Sau khi đo cỡ nhỏ, nâng trung độ RGB bằng gamma: wave-horn/shield/phase-break 1; chain 1,6; dragon-rage 1,2; armour 1,3; phase-prep 1,35; phase-fight 1,4; fast-forward 1,8; danger lượt 2 là 2,6. Alpha được giữ; đây là sửa ảnh bằng công cụ, không phải lượt sinh mới.

## 3. KA1 và khổ
KA1: trước **41 file**, sau **113 file** trong thư mục icon; diff **+72 / −0 dòng**. Toàn bộ 41 file có trước giữ nguyên MD5. `_review/137*` và báo cáo chưa có trước lượt này. Hai snapshot dùng `/sbin/md5 -r`; `md5-diff.txt` giữ diff đầy đủ.
KA1 mở rộng cho mọi file đích (icon, `_review/137*`, báo cáo): `md5-after-complete.txt`, `md5-diff-complete.txt`, `ka1-complete.json`; không tính chính ba manifest đang được tạo để tránh tự tham chiếu.

Bằng chứng trong `_review/137/`: `md5-before.txt`, `md5-after.txt`, `md5-diff.txt`, `ka1-summary.json`, `identify.txt`, `delivery-verification.json`. Identify đã chạy định dạng `%f %wx%h %[channels]\n` cho đủ 40 PNG. Cả 10 master khớp byte bản chọn, cả 30 bản thu khớp từng pixel với Lanczos tái tạo trực tiếp từ master. Không có bước sharpen.

## 4. Alpha, lề và dáng

Định nghĩa: hộp bao alpha >16; mặt nạ IoU alpha ≥128 tại 32²; dải mép là khoảng Chebyshev ≤3 px quanh biên mặt nạ alpha ≥128. Đếm sắc khóa trên mọi pixel alpha >0, hue 285–315°, S >0,5; mẫu số là toàn bộ pixel alpha >0. Alpha min/max của cả 10 ảnh đều **0/255**.

| Ảnh | Bbox x,y,w,h | Cạnh dài / canvas | Lệch tâm lớn nhất | Bán alpha ngoài mép | Sắc khóa còn, px / % | IoU lớn nhất ở 32 px, với |
|---|---|---:|---:|---:|---:|---|
| wave-horn | 153,184,717,656 | 70.020% | 0.049% | 0 | 63 / 0.0322% | 0.420, shield |
| chain | 153,160,717,704 | 70.020% | 0.049% | 0 | 205 / 0.1064% | 0.368, wave-horn |
| dragon-rage | 153,210,717,604 | 70.020% | 0.049% | 0 | 15 / 0.0068% | 0.535, phase-prep |
| armour | 308,153,408,717 | 70.020% | 0.049% | 0 | 83 / 0.0505% | 0.651, danger |
| shield | 156,153,711,717 | 70.020% | 0.049% | 0 | 104 / 0.0263% | 0.678, phase-prep |
| phase-prep | 153,163,717,697 | 70.020% | 0.049% | 0 | 297 / 0.1033% | 0.678, shield |
| phase-fight | 153,173,717,677 | 70.020% | 0.049% | 0 | 93 / 0.0436% | 0.464, phase-prep |
| phase-break | 331,153,362,717 | 70.020% | 0.049% | 0 | 50 / 0.0335% | 0.525, danger |
| fast-forward | 153,258,717,507 | 70.020% | 0.049% | 0 | 172 / 0.0875% | 0.457, shield |
| danger | 310,153,403,717 | 70.020% | 0.049% | 0 | 233 / 0.1739% | 0.651, armour |

Tất cả đạt: cạnh dài 68–72%, lệch tâm ≤2%, alpha ngoài mép 0, sắc khóa ≤0,2%, IoU ≤0,80. Riêng **armour–shield: IoU 12 px = 0.423; 32 px = 0.404**, dưới ngưỡng riêng 0,70. Ở 12 px giáp là vệt cao nhọn, khiên là đĩa tròn; chi tiết vảy/rune không còn là tín hiệu chính.

## 5. Đọc ở cỡ HUD và tương phản

Luma dùng Rec.709 trên kênh sRGB chuẩn hóa 0–1: `0,2126 R + 0,7152 G + 0,0722 B`. Bảng dưới đo **sau ghép thật** lên nền, trên dấu chân alpha >16, gồm ảnh hưởng của khử răng cưa. Mỗi ô ghi tối `#2b2118` / kem `#f1e3c4`. Cả 10 ảnh đều ≥0,25 trên nền tối ở cả hai cỡ.

| Ảnh | Cỡ 720p / 1080p | ΔY 720p tối / kem | ΔY 1080p tối / kem |
|---|---:|---:|---:|
| wave-horn | 16 / 24 | 0.266 / 0.277 | 0.297 / 0.306 |
| chain | 16 / 24 | 0.281 / 0.240 | 0.303 / 0.261 |
| dragon-rage | 16 / 24 | 0.272 / 0.265 | 0.298 / 0.288 |
| armour | 12 / 18 | 0.279 / 0.241 | 0.320 / 0.272 |
| shield | 12 / 18 | 0.272 / 0.332 | 0.288 / 0.345 |
| phase-prep | 16 / 24 | 0.284 / 0.269 | 0.308 / 0.294 |
| phase-fight | 16 / 24 | 0.275 / 0.186 | 0.324 / 0.218 |
| phase-break | 16 / 24 | 0.278 / 0.239 | 0.297 / 0.257 |
| fast-forward | 16 / 24 | 0.286 / 0.256 | 0.311 / 0.282 |
| danger | 24 / 36 | 0.449 / 0.136 | 0.488 / 0.148 |

**Danger trên cỏ:** lấy ô ảnh trận đầu tiên `640×360+4+54` trong đúng sheet chủ dự án chỉ định; phục hồi khổ 1280×720 và 1920×1080 bằng Lanczos. Đây là bản ghép từ tờ kiểm cũ, không phải ảnh chụp runtime mới. Vị trí trên cỏ: (888,418) tại 720p, (1332,627) tại 1080p. Đo nền **đúng dưới từng pixel của dấu chân alpha**; không lấy trung bình cả ô 40 px có màu nền khác.

| Cỡ màn / icon | Luma cỏ | Luma vật | ΔY vật–cỏ | ΔY sau ghép |
|---|---:|---:|---:|---:|
| 720p / 24 px | 0.3879 | 0.7165 | 0.3285 | 0.2536 |
| 1080p / 36 px | 0.3880 | 0.7164 | 0.3285 | 0.2757 |

Cả hai cỡ đạt ≥0,25 kể cả sau ghép. Giới hạn: kết quả này là tại vùng cỏ ô liu có bóng đã ghi tọa độ, **không bảo đảm mọi nền của sân**. Tờ thử nhiều điểm còn giữ các phép đo trượt ở vùng sáng; lượt 1 và các bản trước không được dùng làm bằng chứng cho bộ giao. Dấu vẫn mất tương phản trên vùng nền sáng gần cùng luma; Claude cần nhìn điều này khi gắn sprite.

## 6. Tờ xem và so mức chợ

- **Tờ bộ giao:** [137-sheet-selected.jpg](../../games/dragon-hold/art-src/_review/137-sheet-selected.jpg). Bốn hàng: canvas thu 256 px; cỡ 1080p trên hai nền; cỡ 720p trên hai nền; toàn bộ icon mới đặt cạnh bốn icon cũ và mảnh HUD ảnh chủ dự án, tất cả vật cùng cao 112 px. Hàng 2–3 giữ đúng pixel, không phóng lớn.
- [Mép 4× và giáp/khiên 12 px](../../games/dragon-hold/art-src/_review/137-detail-selected.jpg).
- Danger đúng cỡ: [720p](../../games/dragon-hold/art-src/_review/137/danger-proof-720.png), [1080p](../../games/dragon-hold/art-src/_review/137/danger-proof-1080.png).
- `137-sheet.jpg` là tờ đo đầu tiên, giữ nguyên để không ghi đè; `137-sheet-final.jpg` là bước sửa sáng trước khi thay danger. **Hai tờ này không phải bộ chọn cuối.**

So HUD thương mại của ảnh chủ dự án: **đứng cạnh được ở mức 8**, nhờ mép vật liệu hoàn thiện, diện sáng rõ, khối kim loại/đá có chiều sâu. Bộ cũ chỉ được dùng để so cỡ vật và nhận diện game; không dùng làm thước chấm. Bộ mới nhiều chi tiết vật liệu hơn icon hệ thống trong ảnh chủ dự án; ở cỡ rất nhỏ, dáng và mảng sáng làm nhiệm vụ nhận diện. Không sao chép vòng kỹ năng hay nội dung HUD tham chiếu vào icon mới.

## 7. KA5 tự chấm

Thứ tự năm tiêu chí: **Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp**, mỗi tiêu chí 0–2. Dùng tiếp =2 vì đủ các kiểm số bắt buộc; chưa thay thế bước Claude nhận. M là mức chợ riêng theo AD.

| Ảnh | Năm điểm gốc | Q gốc | Năm điểm 720p | Q 720p | M gốc / 720p |
|---|---|---:|---|---:|---:|
| wave-horn | 2 / 2 / 2 / 1,5 / 2 | 9,5 | 2 / 2 / 2 / 1 / 2 | 9 | 8,5 / 8 |
| chain | 2 / 2 / 2 / 1,5 / 2 | 9,5 | 2 / 1,5 / 2 / 1 / 2 | 8,5 | 8,5 / 8 |
| dragon-rage | 2 / 2 / 2 / 1,5 / 2 | 9,5 | 2 / 1,5 / 2 / 1 / 2 | 8,5 | 8,5 / 8 |
| armour | 2 / 2 / 2 / 1,5 / 2 | 9,5 | 2 / 1 / 2 / 1 / 2 | 8 | 8 / 8 |
| shield | 2 / 2 / 2 / 1,5 / 2 | 9,5 | 2 / 1,5 / 2 / 1 / 2 | 8,5 | 8,5 / 8 |
| phase-prep | 2 / 1,5 / 2 / 1,5 / 2 | 9 | 2 / 1 / 2 / 1 / 2 | 8 | 8 / 8 |
| phase-fight | 2 / 2 / 2 / 1,5 / 2 | 9,5 | 2 / 1,5 / 2 / 1 / 2 | 8,5 | 8,5 / 8 |
| phase-break | 2 / 2 / 2 / 1,5 / 2 | 9,5 | 2 / 1,5 / 2 / 1 / 2 | 8,5 | 8 / 8 |
| fast-forward | 2 / 2 / 2 / 1,5 / 2 | 9,5 | 2 / 2 / 2 / 1 / 2 | 9 | 8 / 8 |
| danger | 2 / 2 / 2 / 1,5 / 2 | 9,5 | 2 / 1,5 / 2 / 1 / 2 | 8,5 | 8 / 8 |

Điểm trừ: bề mặt khá giàu hoa văn ở gốc; ở 12–16 px một số vật chỉ còn dáng và mảng sáng. `phase-prep` cần người nhận nhìn riêng vì đầu búa/bó cọc ở 16 px gần nhau. `danger` cần nhìn lại trên vùng cỏ sáng khi gắn vào game.

## 8. Khác phiếu, phần bỏ qua và chạy lại

1. Tờ xem cuối dùng hậu tố `-selected`; tên `137-sheet.jpg` đã được tạo ở vòng đo đầu và được giữ nguyên theo luật không ghi đè. Báo cáo chỉ rõ tờ nào là bộ giao; các tờ thử không bị xóa.
2. Công cụ sinh trả 1254², nên giữ nguồn đúng byte trong `.try*`, hậu kỳ master về 1024². Không có tùy chọn size trong lời gọi image_gen tích hợp hiện dùng.
3. Lấy khung cảnh từ sheet đã cung cấp để kiểm danger; không mở browser, không chạy dev server. Không có capture trình duyệt hay raw frame mới cần prune.
4. `fast-forward` dùng hai chevron cùng hàng, cùng chiều cao, đúng nghĩa tua nhanh; “stacked” được diễn giải thành cặp chevron liên tiếp thay vì hai dấu chồng dọc.
5. Không tạo âm thanh vì phiếu chỉ yêu cầu ảnh. Không sửa mã game, tài liệu khác, công cụ, `public/`, game khác, Tu Tiên hay `.wt-*`; không chạy Git, build hay test suite game. Chỉ đọc các ảnh tham chiếu được yêu cầu của game khác.

Script dùng nằm trong `_review/137/`: `prepare.py`, `refine.py`, `finalize.py`, `verify.py`, `sheets.py`, `grass-proof.py`, `publish.py`, `verify-delivery.py`, `report.py`, `audit-complete.py`. Chạy từ repo cha, Python chuẩn + ImageMagick 7, `ART_MAGICK=/opt/homebrew/bin/magick`, font Arial hệ thống. Script tạo file mới độc quyền; không ghi đè báo cáo/số đo có sẵn. Các stage đã có được giữ nguyên. Có thể chạy `verify.py <thư-mục-icon> <tên-json-mới>` để đo lại bộ giao; `verify-delivery.py <tên-json-mới>` để kiểm lại các bản thu; `grass-proof.py -rerun` và `sheets.py <thư-mục-icon> -rerun` tạo bằng chứng mang hậu tố mới; `publish.py -rerun` và `audit-complete.py -rerun` tạo snapshot mới. Không dùng lại cùng hậu tố nếu file đã tồn tại. `generation-manifest.json` và `generation-danger-try2.json` giữ đường dẫn nguồn công cụ.

**Cần chủ dự án/Claude nhìn:** tờ `137-sheet-selected.jpg`, giáp/khiên ở 12 px, búa/bó cọc ở 16 px, dấu nguy hiểm ở cỡ thật trên cỏ và trên phần sáng. Claude chấm lại ≥8 rồi mới chép vào `public/` khi gắn.
