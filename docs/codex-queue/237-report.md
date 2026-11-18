# Phiếu 237 · Last Line · Làm lại ba icon HUD của 149

Ngày 31/10/2026. **Đã chốt `keyboard.try2`, `bay-full.try3`, `streak.try2`; đủ 12 PNG và ba prompt bản chốt. Tự kiểm số đạt, đã xem ở 16/24 px trên cả hai nền. Chờ Claude chấm lại từ 8; chưa phải nghiệm thu.** Sinh bằng công cụ tích hợp `image_gen`, không gặp 429, không chuyển sang API/CLI.

## Bộ giao và tờ xem

Gốc: `games/typing-survival/art-src/ui/icons/`. Đúng ba tên `keyboard`, `bay-full`, `streak`, mỗi tên có `.png` (1024²), `.64.png`, `.128.png`, `.256.png`, `.prompt.txt`. Bốn bản sinh mới và prompt nguyên văn giữ cạnh nhau: `keyboard.try2.*`, `bay-full.try2.*`, `bay-full.try3.*`, `streak.try2.*`.

Trước khi thay, đã chép **đủ 15 file cũ** vào [237/prev](../../games/typing-survival/art-src/_review/237/prev/); byte backup khớp MD5 trước phiên. Bảy icon đã nhận và mọi try1 giữ nguyên.

**Tờ Claude cần chấm:** [237-sheet-delivery.jpg](../../games/typing-survival/art-src/_review/237-sheet-delivery.jpg). Ba icon mới đứng cạnh bảy icon đã nhận, cùng canvas 256 px; dưới có cỡ 1080p/720p trên `#14181f` và `#8c96a3`; hàng cuối đối chiếu bốn icon súng và HUD thương mại của chủ dự án, cùng cao 256 px. Đã xem tờ chốt: vật liệu, bevel và ánh sáng phù hợp bộ trắng ngà–vàng–lam.

Các tờ nhỏ có **cỡ thật 16/24 px trên hai nền**, kèm phóng nearest 8× để soi cấu trúc:

- [keyboard try2](../../games/typing-survival/art-src/_review/237/keyboard-try2-small.jpg).
- [bay-full try2, không chọn](../../games/typing-survival/art-src/_review/237/bay-full-try2-small.jpg).
- [bay-full try3 ở lấp 70%, mốc trung gian](../../games/typing-survival/art-src/_review/237/bay-full-try3-small.jpg).
- [bay-full try3 bản chốt 71,875%](../../games/typing-survival/art-src/_review/237/bay-full-try3-fill736-small.jpg).
- [streak try2](../../games/typing-survival/art-src/_review/237/streak-try2-small.jpg).

[Tờ cả bộ nhỏ](../../games/typing-survival/art-src/_review/237-small-delivery-4x.jpg), [trên hai bến 720p/1080p](../../games/typing-survival/art-src/_review/237-bay-delivery.jpg), [token bay-glass trên sàn thật](../../games/typing-survival/art-src/_review/237-bay-glass-delivery.jpg). Đây là mock trên capture có sẵn của phiếu 149, không phải phiên chơi/capture mới.

## Prompt và lựa chọn

Giữ nguyên khối STYLE-UI ở ART_DIRECTION §4.3 và khối ICON của 149; chỉ viết lại phần chủ thể, thêm vai trò ảnh `armour.png` làm tham chiếu vật liệu. Đã xem `gun-xung.norm.256.png`, tờ 121/127, tờ 149 và HUD thương mại; không sửa các nguồn đó. [Nhật ký sinh và prompt thực tế](237/generation-log.json).

| Icon | Sửa gì và vì sao |
| --- | --- |
| keyboard try2 · chọn | Bỏ thân ngang và hàng phím nhỏ; đúng bốn phím trống 2×2, một phím lam, khe chữ thập rộng. Hình gần vuông; ở 16 px vẫn tách bốn phím, ở 24 px rõ hơn. Không cần try3. |
| bay-full try2 · không chọn | Ba ô lam cạnh nhau trong ổ U dày, gần vuông và đọc được ở 16 px. Tuy nhiên IoU với keyboard try2 = **0,8157**, vượt 0,80; giữ nguyên hồ sơ, không dùng bản này. |
| bay-full try3 · chọn | Đổi thành ba đỉnh nhô rõ, ô giữa cao hơn, khe thoáng sâu, ổ U thấp và đáy thu gọn. Cỡ 16 px vẫn đếm được ba ô; 24 px giữ rõ ô giữa cao. Lượt này dùng hết hai lần sinh mới của bay-full. |
| streak try2 · chọn | Thay ba tia mảnh bằng hai chevron lam rất dày, viền trắng ngà và vàng, liên kết bằng khối cơ khí. 16 px còn hai đầu mũi và hai hõm V, không còn ba chấm. Bản sinh đặt hai chevron ngang, không lệch chéo như prompt; phù hợp ví dụ chevron của 237 và giữ dáng đọc rõ. Không cần try3. |

Bay-full try3 lúc lấp 69,922% có IoU với clock **0,8156**. Trước khi chốt, thử **thu đều toàn vật**, giữ tỷ lệ và tâm, ở các mức lề khác nhau; chọn cạnh dài **736/1024 = 71,875%**, vẫn trong 68–72%. IoU với clock còn **0,7968** và với keyboard **0,7925**. Không cắt phần vẽ, không bóp ngang/dọc hay dịch lệch tâm để đổi dáng; tăng kích cỡ cũng giúp đọc ở 16 px. Mốc 696 px của phép thử có lấp 67,969%, dưới 68%, chỉ là probe và không giao. [Probe lề](../../games/typing-survival/art-src/_review/237/margin-probe.json) dùng keyboard cũ làm đối chiếu phụ; bảng chốt đo lại cả bộ mới.

## Hậu kỳ không phá tranh

Bốn nguồn công cụ trả 1254², RGBA trong suốt thật. Chuẩn hóa về gốc 1024² bằng Lanczos, giữ tỷ lệ và tâm bbox alpha >16. Không tách nền khóa, không chỉnh RGB/độ sáng, không vẽ, phủ màu hoặc xóa chi tiết. Các bản 256/128/64 thu **trực tiếp từ gốc**, không làm nét 64.

Alpha vật nguồn thường 252–253 thay vì đục 255. Cùng cách 149: chỉ chuẩn hóa alpha ngoài dải 3 px quanh contour alpha 128, giữ alpha trong dải và giữ RGB; vì đây là kim loại/kính phát sáng đục, không phải kính nhìn xuyên. Sửa tương tự nhiễu alpha do Lanczos ở bản thu. Số pixel đổi trên bản chốt:

- `keyboard`: alpha đổi ở gốc **420899 pixel**, tổng ba bản thu **0 pixel**; RGB do bước alpha đổi **0 pixel**.
- `bay-full`: alpha đổi ở gốc **344895 pixel**, tổng ba bản thu **6 pixel**; RGB do bước alpha đổi **0 pixel**.
- `streak`: alpha đổi ở gốc **262744 pixel**, tổng ba bản thu **2 pixel**; RGB do bước alpha đổi **0 pixel**.

Đã xem ba tờ **bản sinh | bản hậu kỳ** cùng cỡ: [keyboard](../../games/typing-survival/art-src/_review/237/keyboard-try2-before-after.jpg), [bay-full](../../games/typing-survival/art-src/_review/237/bay-full-try3-fill736-before-after.jpg), [streak](../../games/typing-survival/art-src/_review/237/streak-try2-before-after.jpg). Không thấy mất khối, phai chất liệu hoặc bị cắt tranh.

## Kiểm số trên bản giao

12/12 PNG đúng khổ, sRGB RGBA 8 bit, `srgba`; [identify](../../games/typing-survival/art-src/_review/237/identify-delivery.txt). Alpha ngoài dải mép 3 px bằng 0 ở cả bốn file của mỗi icon. Sắc M: hue lệch ≤15° so với 300°, S>0,5, tính trên pixel alpha>0; ghi cực đại qua bốn file, giới hạn 0,2%. Không dùng nền khóa nhưng vẫn kiểm nhiễu M.

Luma theo đúng 149: `Y = 0,2126R + 0,7152G + 0,0722B` trên sRGB 0–1, trung bình vật có trọng số alpha; ΔY là trị tuyệt đối giữa vật và nền, không phải tỷ lệ WCAG. Mặt nạ IoU: alpha ≥128 sau Lanczos về 32². Tất cả **45/45 cặp** trong bộ mười icon ≤0,80, cực đại **0,7968**. Không có cặp sáng/tắt. Tỷ lệ dưới là cạnh dài/cạnh ngắn bbox alpha>16; cả keyboard và bay-full ≤1,30.

| Icon | Chọn | Tỷ lệ bbox | Lấp cạnh dài % | Alpha ngoài mép (4 file) | M tối đa % | ΔY than chì 16/24 | ΔY bay-glass 16/24 | IoU lớn nhất |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| keyboard | try2 | 1.0453 | 69.922 | 0 | 0.0188 | 0.4616 / 0.4608 | 0.4048 / 0.4039 | 0.7925 (bay-full) |
| bay-full | try3 | 1.1220 | 71.875 | 0 | 0.0214 | 0.4400 / 0.4405 | 0.4267 / 0.4271 | 0.7968 (clock) |
| streak | try2 | 1.2198 | 69.922 | 0 | 0.0372 | 0.4443 / 0.4466 | 0.4502 / 0.4525 | 0.6713 (clock) |

Độ lệch tâm bbox bản gốc lớn nhất **0,049%**, dưới 2%. Cả ba đạt ΔY≥0,25 trên than chì và token `--bay-glass = rgba(7,9,11,0.64)` ghép trên mảnh sàn capture cũ. Nền thép sáng vẫn có tờ kiểm; ΔY trung bình thấp (0,029–0,051), không tuyên bố nền này đạt ngưỡng. Các khe than chì/viền sáng vẫn giúp đọc dáng ở nền sáng.

Dữ liệu đủ: [kiểm gốc/bản thu, tương phản hai nền, 45 cặp IoU](../../games/typing-survival/art-src/_review/237/measurements-selected.json), [bến/token kính](../../games/typing-survival/art-src/_review/237/bay-measurements-delivery-1031.json). Tên file `*-1031` trong hồ sơ 237 là do tái dùng script dựng proof của 149; không ghi vào hồ sơ 149.

## KA5 · Tự chấm trên bản hậu kỳ

Q theo thứ tự Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp, mỗi tiêu chí 0–2. M so chất liệu và độ hoàn thiện với icon/HUD game thương mại, không thay việc Claude chấm nhận. Dùng tiếp = 2 vì kiểm số và hồ sơ đạt.

| Icon | Q gốc | Tổng | Q 16 px | Tổng | M gốc / 16 / 24 px | Cần xem kỹ |
| --- | --- | ---: | --- | ---: | --- | --- |
| keyboard | 2 / 2 / 2 / 2 / 2 | 10 | 2 / 1,5 / 2 / 1,5 / 2 | 9 | 8,5 / 8,2 / 8,4 | Bốn phím còn rõ; hình là cụm keypad theo hướng 237, không có hàng phím dài. |
| bay-full | 2 / 2 / 2 / 1,5 / 2 | 9,5 | 2 / 1,5 / 2 / 1,5 / 2 | 9 | 8,5 / 8,3 / 8,4 | Ba ô đọc được; các nắp bạc hơi lớn; IoU clock 0,7968 sát ngưỡng. |
| streak | 2 / 2 / 2 / 2 / 2 | 10 | 2 / 1,5 / 2 / 2 / 2 | 9,5 | 8,6 / 8,4 / 8,5 | Hai chevron giữ đầu mũi và hõm V; nét khắc phụ biến mất đúng dự kiến. |

## KA1 · Phạm vi và việc bỏ qua

MD5 trước phiên có **1631 file** trong ui/icons và hồ sơ 149. Sau giao, chỉ **15 file cũ được phép thay** khác MD5; cả 15 bản cũ ở prev khớp mốc đầu. **Không mất file, không đổi file cũ nào khác**; 35 file chốt của bảy icon đã nhận và mọi try1 giữ nguyên. Khác luật chỉ-thêm của 149 là ngoại lệ ghi đè đúng ba tên do 237 cho phép, có backup trước. [Mốc trước](../../games/typing-survival/art-src/_review/237/md5-before.txt), [sau](../../games/typing-survival/art-src/_review/237/md5-after.txt), [diff](../../games/typing-survival/art-src/_review/237/md5-diff.txt), [tổng kết](../../games/typing-survival/art-src/_review/237/md5-summary.json), [manifest 15 file giao](../../games/typing-survival/art-src/_review/237/installed-manifest.json). File thêm đồng thời trong cây icon không tự quy thành sản phẩm phiếu này.

Script cục bộ giữ trong `_review/237/`: `process.py`, `prepare-delivery.py`, `proofs.py`, `install.py`, `audit.py`. Không sửa công cụ chung. Script từ chối ghi đè hồ sơ đã có; install chỉ thay ba tên sau khi sao lưu toàn bộ. Hướng dẫn tái lập ở [237/README.md](237/README.md).

Không sinh try3 cho keyboard/streak vì try2 đã đạt tự kiểm. Không sửa bảy icon đã nhận, try1, mã game, tài liệu khác, Tu Tiên hay `.wt-*`; không chạy Git, build/test game, dev server hoặc trình duyệt. Không chép `public/` vì Claude là người gắn; không làm âm thanh vì ngoài phiếu. Không có capture/raw frame mới cần prune: bản sinh, proof và probe đều là hồ sơ kiểm cần giữ.

**Claude/chủ dự án cần xem:** tờ 237-sheet-delivery, ba tờ 16/24 px bản chốt và bay-full sát ngưỡng IoU. Chỉ nhận sau khi Claude chấm lại từ 8. Không có hạn mức hoặc thời gian chờ còn tồn đọng.
