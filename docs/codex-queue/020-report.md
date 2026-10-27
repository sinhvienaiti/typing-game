# Phiếu 020 · Báo cáo làm lại 9 ảnh 2D dưới 8 điểm

Ngày 27/10/2026. **Đã có 9 bản chọn từ 8,5–9 điểm theo Codex; đang chờ Claude chấm lại, chưa phải kết quả nhận cuối.** Dùng built-in `image_gen`: 12 ảnh tạo, 12 prompt nguyên văn ở cạnh từng `.tryN.png`; 9 bản hậu kỳ `.fix.png`. Không ảnh nào quá 2 lượt tạo. C22 sửa bằng công cụ, không tạo lại.

Đã đọc prompt cạnh từng ảnh, ART_FIX_QUEUE §3b, ART_ACCEPTANCE và mục phong cách 015b-priority. Đối chiếu rêu với grass-a/grass-b; chân dung với narrator/draconis và ảnh nhân vật; cây với hai v1 và v2 hiện tại; V35 đính kèm cả barracks-v2 và nhánh hiện tại ở lượt 1. Lượt 2 V35 thêm bản nháp sửa tỉ lệ làm mẫu chiều cao.

## 1. Bản chọn và tự chấm

Thứ tự năm tiêu chí: **Đúng đề / Đọc được trong game / Hợp bộ / Hình khối / Dùng được cho bước sau**, mỗi tiêu chí 0–2. Cỡ xem: chân dung 128 và 64 px; cây 160 px; rêu ghép 3×3, mỗi ô 128 px trên tờ nhanh. Điểm lẻ 0,5 dùng như các bản chấm trước.

| # | Mã | Cách (sửa / tạo lại) | Số lượt | File chọn | Điểm từng tiêu chí (5 × 0–2) | Tổng | Còn thiếu gì |
|---|---|---|---:|---|---|---:|---|
| 1 | T3 Rêu dưới tán | Tạo lại + sửa | 1 | [moss.fix.png](../../games/dragon-hold/art-src/ground/pine-river/moss.fix.png) | 2 / 1,5 / 1 / 2 / 2 | 8,5 | Mảng chéo còn nhận ra khi lặp; nét mềm hơn cỏ A. Rêu phẳng, không lá/cành; mép nối qua đủ kiểm. |
| 2 | C23 Draconis tối thượng | Tạo lại + sửa | 2 | [draconis-ult.fix.png](../../games/typing-defense/art-src/portraits/draconis-ult.fix.png) | 2 / 2 / 1,5 / 1,5 / 2 | 9 | Nét giáp và bàn tay còn nhiều chi tiết; mưa lông đi chéo xuống. Nền cam đào, sừng/mặt/tay nằm trong dải 3:1. |
| 3 | C9 Lam | Tạo lại + sửa | 2 | [lam.fix.png](../../games/typing-defense/art-src/portraits/lam.fix.png) | 2 / 2 / 1 / 2 / 2 | 9 | Lối tô còn dày hơn narrator; biểu cảm cười lớn, khung đầu–thân trên, tai và lửa đủ lề. |
| 4 | C10 Tre | Tạo lại + sửa | 1 | [tre.fix.png](../../games/typing-defense/art-src/portraits/tre.fix.png) | 2 / 1,5 / 1 / 2 / 2 | 8,5 | Chuồn chuồn nhỏ ở 64 px; lối tô còn dày. Búa đặt trên vai, đầu–thân trên rõ. |
| 5 | C25 Tre tối thượng | Tạo lại + sửa | 2 | [tre-ult.fix.png](../../games/typing-defense/art-src/portraits/tre-ult.fix.png) | 2 / 2 / 1 / 2 / 2 | 9 | Giàn và túi còn nhiều nét. Búa giơ cao, hai tay và mặt trọn dải; giàn nguyên, vệt dựng hướng lên. |
| 6 | C22 Đại Bàng Tinh | Sửa | 0 | [dai-bang-tinh.fix.png](../../games/typing-defense/art-src/portraits/dai-bang-tinh.fix.png) | 2 / 2 / 1 / 1,5 / 2 | 8,5 | Mặt đồng được làm trơn nên phẳng hơn lông; mép ngực phải cắt thẳng. Đã quay phải, chỉ đầu–ngực, có viền/vệt mực, không còn nét giống chữ. |
| 7 | S15-v2 Ô-liu v2 | Tạo lại + sửa | 1 | [olive-tree-v2.fix.png](../../games/typing-defense/art-src/scenery/coast/olive-tree-v2.fix.png) | 1,5 / 1,5 / 1,5 / 2 / 2 | 8,5 | Vẫn còn khá nhiều dấu lá/vỏ nhỏ; tán đã gom năm khối, thân nghiêng phải rõ, khác dáng v1. |
| 8 | S16-v2 Phi lao v2 | Tạo lại + sửa | 1 | [casuarina-v2.fix.png](../../games/typing-defense/art-src/scenery/coast/casuarina-v2.fix.png) | 1,5 / 1,5 / 1,5 / 2 / 2 | 8,5 | Tán còn nhiều nét nhỏ hơn mong muốn; thân uốn ngả phải và tán xuôi gió đọc rõ ở 160 px. |
| 9 | V35 Trại Lính, nhánh Giáo Dài | Tạo lại + sửa | 2 | [barracks-giao-dai.fix.png](../../games/typing-defense/art-src/branches/barracks-giao-dai.fix.png) | 1,5 / 1,5 / 2 / 1,5 / 2 | 8,5 | Mũi giáo còn thấy phân lớp và chi tiết công trình dày; bó giáo sát nhau, không khe xuyên nền. Chiều cao 97,87% mẫu, còn lệch nhẹ phối cảnh. Đã xóa hai đốm xanh nhỏ. |

### Điểm các lượt trước hậu kỳ

| Mã | Lượt 1 | Lượt 2 | Lý do sửa tiếp |
|---|---:|---:|---|
| T3 | 7,5 | — | 1254×1254; cần chuẩn 1024, hạ tương phản và xử lý mép. |
| C23 | 7,5 | 8,5 | Lượt 1 còn cam cháy, sừng bị dải cắt mất. Lượt 2 làm ngang 3:1, sau đó chuẩn hóa/dàn vào giữa 1536×1024. |
| C9 | 7,5 | 8 | Lượt 1 ngọn lửa chạm mép. Lượt 2 giữ trọn ngọn, hậu kỳ thêm lề và tách nền. |
| C10 | 8 | — | Đã đủ đề; hậu kỳ tách nền, thêm lề và chuẩn khổ. |
| C25 | 7 | 9 | Lượt 1 búa bị dải cắt mất; lượt 2 vẽ trực tiếp ngang 3:1, hậu kỳ đặt giữa 1536×1024. |
| C22 | Không tạo | — | Cắt và lật ảnh gốc, xóa cánh thừa ở góc, thay mặt đồng bằng mặt trơn có lỗ vuông, thêm viền/vệt mực, tách nền. |
| S15-v2 | 8 | — | Đủ thân nghiêng; thêm lề, chuẩn khổ dọc và alpha. |
| S16-v2 | 8 | — | Đủ thân ngả gió; thêm lề gốc và alpha. |
| V35 | 7,5 | 8,5 | Lượt 1 vẫn chỉ 76,84% chiều cao mẫu khi cùng bề ngang chân. Bản kéo tỉ lệ thử bị méo trống/huy hiệu nên **không chọn**; lượt 2 vẽ lại hình khối cao. Hậu kỳ chỉ fit đồng tỉ lệ, khóa BG-G và xóa 27 px xanh lạ. |

Ảnh đã từ 8 điểm chỉ hậu kỳ bằng công cụ; không tạo thêm sau khi đạt. Bản tạo nguyên gốc giữ tại `.tryN.png`; file giao chọn là `.fix.png`. Không thay tên ảnh đang dùng.

## 2. MD5 ảnh đang dùng

Đã ghi trước khi tạo ảnh: [md5-before.txt](../../games/typing-defense/art-src/_review/020/md5-before.txt). Cuối cùng: [md5-after.txt](../../games/typing-defense/art-src/_review/020/md5-after.txt). Đầu ra `md5 -r` trước:

```text
0c053f350973d4955312b2541a7533fa games/dragon-hold/art-src/ground/pine-river/moss.png
9bcdd6e9a1e9a636a6ff3967d2b3ce2e games/typing-defense/art-src/portraits/draconis-ult.png
97de44b84f01a79b835dc15c2146b718 games/typing-defense/art-src/portraits/lam.png
a3821930dc5529dd5d8dc4945e2aae46 games/typing-defense/art-src/portraits/tre.png
7d712c125ba0c3abf4abc16ebe9b1cc9 games/typing-defense/art-src/portraits/tre-ult.png
168440809dcf133e78670d1db5905548 games/typing-defense/art-src/portraits/dai-bang-tinh.png
88ff1a26b2b1036ee907a0aa73693476 games/typing-defense/art-src/scenery/coast/olive-tree-v2.png
a4cab3d0dd6c567752469a2ccf3ae49a games/typing-defense/art-src/scenery/coast/casuarina-v2.png
787b44a5975077b48848a15d019e75d9 games/typing-defense/art-src/branches/barracks-giao-dai.png
```

Đầu ra `md5 -r` sau:

```text
0c053f350973d4955312b2541a7533fa games/dragon-hold/art-src/ground/pine-river/moss.png
9bcdd6e9a1e9a636a6ff3967d2b3ce2e games/typing-defense/art-src/portraits/draconis-ult.png
97de44b84f01a79b835dc15c2146b718 games/typing-defense/art-src/portraits/lam.png
a3821930dc5529dd5d8dc4945e2aae46 games/typing-defense/art-src/portraits/tre.png
7d712c125ba0c3abf4abc16ebe9b1cc9 games/typing-defense/art-src/portraits/tre-ult.png
168440809dcf133e78670d1db5905548 games/typing-defense/art-src/portraits/dai-bang-tinh.png
88ff1a26b2b1036ee907a0aa73693476 games/typing-defense/art-src/scenery/coast/olive-tree-v2.png
a4cab3d0dd6c567752469a2ccf3ae49a games/typing-defense/art-src/scenery/coast/casuarina-v2.png
787b44a5975077b48848a15d019e75d9 games/typing-defense/art-src/branches/barracks-giao-dai.png
```

```sh
diff games/typing-defense/art-src/_review/020/md5-before.txt games/typing-defense/art-src/_review/020/md5-after.txt
```

Đầu ra rỗng; mã thoát **0**, 0 byte. Chín ảnh gốc không đổi. [Bản ghi diff](../../games/typing-defense/art-src/_review/020/md5-diff.txt).

## 3. Kiểm file mới và công việc đồng thời

Kết quả chụp tại lần kiểm: **170 file mới của phiếu 020**, gồm 12 PNG lượt tạo, 12 prompt, 9 `.fix.png`; phần còn lại là ảnh đối chiếu, số đo và script kiểm trong vùng `_review/020/`, cùng hai JPG tờ nhanh. Không có file của phiếu 020 ngoài các mẫu được phép. [Danh sách riêng phiếu 020](../../games/typing-defense/art-src/_review/020/owned-files.txt).

Lệnh toàn thư mục trả **243 file**. Trong đó **75 đường dẫn ngoài phạm vi phiếu 020** phát sinh từ công việc đồng thời: `_review/020b*`, `_review/020c*`, chân dung Mộc Tinh, nhánh Mỏ Vàng và ảnh UI barracks. Có hai file Mộc Tinh có sẵn được tiến trình khác cập nhật. Tôi không tạo, sửa hay xóa các đường dẫn này. Vì vậy không kết luận danh sách toàn workspace chỉ có phiếu 020; kiểm riêng phần được phiếu này tạo đạt. Lần kiểm toàn cục đầu đã dừng assertion vì các file đồng thời này, bản `audit-summary.json` giữ để đối chiếu; kết quả phân định cuối ở [audit-summary-final.json](../../games/typing-defense/art-src/_review/020/audit-summary-final.json).

Đầu ra tóm tắt kiểm cuối:

```json
{
  "original_nine_md5_equal": true,
  "global_find_newer_files": 243,
  "owned_new_files": 170,
  "concurrent_paths_in_find": 75,
  "generated_images": 12,
  "exact_prompt_files": 12,
  "selected_fix_files": 9,
  "owned_outside_whitelist": [],
  "missing_prompt": []
}
```

Lệnh đã dùng:

```sh
find games/dragon-hold/art-src games/typing-defense/art-src -newer games/typing-defense/art-src/_review/020/md5-before.txt -type f
```

Đầu ra nguyên văn tại thời điểm kiểm (không lọc file của tác vụ khác):

```text
games/dragon-hold/art-src/ground/pine-river/moss.try1.png
games/dragon-hold/art-src/ground/pine-river/moss.try1.prompt.txt
games/dragon-hold/art-src/ground/pine-river/moss.fix.png
games/dragon-hold/art-src/_review/020-dh.jpg
games/typing-defense/art-src/ui/buildings/normalized/barracks-v2.trim.256.png
games/typing-defense/art-src/ui/buildings/normalized/barracks-v2.trim.64.png
games/typing-defense/art-src/ui/buildings/barracks-v2.trim.png
games/typing-defense/art-src/scenery/coast/olive-tree-v2.try1.prompt.txt
games/typing-defense/art-src/scenery/coast/casuarina-v2.try1.png
games/typing-defense/art-src/scenery/coast/olive-tree-v2.try1.png
games/typing-defense/art-src/scenery/coast/casuarina-v2.try1.prompt.txt
games/typing-defense/art-src/scenery/coast/olive-tree-v2.fix.png
games/typing-defense/art-src/scenery/coast/casuarina-v2.fix.png
games/typing-defense/art-src/_review/020b-moc-tinh.jpg
games/typing-defense/art-src/_review/020/td-row1-try2.png
games/typing-defense/art-src/_review/020/td-row0-try2.png
games/typing-defense/art-src/_review/020/audit-summary.json
games/typing-defense/art-src/_review/020/seam-environment.sh
games/typing-defense/art-src/_review/020/v35-key.png
games/typing-defense/art-src/_review/020/draconis-ult.old-strip.png
games/typing-defense/art-src/_review/020/moss-candidate.png
games/typing-defense/art-src/_review/020/fix-candidates.py
games/typing-defense/art-src/_review/020/seam-soft-candidate.json
games/typing-defense/art-src/_review/020/td-row0-try1.png
games/typing-defense/art-src/_review/020/verify-final.py
games/typing-defense/art-src/_review/020/td-row1-try1.png
games/typing-defense/art-src/_review/020/make-review.py
games/typing-defense/art-src/_review/020/v35-equal-base.jpg
games/typing-defense/art-src/_review/020/c22-padded.png
games/typing-defense/art-src/_review/020/td-row7-old.png
games/typing-defense/art-src/_review/020/seam-final.json
games/typing-defense/art-src/_review/020/ultimate-strips.jpg
games/typing-defense/art-src/_review/020/td-row6-old.png
games/typing-defense/art-src/_review/020/finalize-candidates.py
games/typing-defense/art-src/_review/020/tre-candidate.png
games/typing-defense/art-src/_review/020/v35-candidate2.png
games/typing-defense/art-src/_review/020/t3-old-3x3.png
games/typing-defense/art-src/_review/020/moss-soft-candidate.png.seam.png
games/typing-defense/art-src/_review/020/candidates-a.jpg
games/typing-defense/art-src/_review/020/draconis-ult.try2-strip-label.png
games/typing-defense/art-src/_review/020/generation-plan.json
games/typing-defense/art-src/_review/020/olive-tree-v2-candidate.png
games/typing-defense/art-src/_review/020/casuarina-v2-candidate.png
games/typing-defense/art-src/_review/020/ultimate-vs-old-draconis.jpg
games/typing-defense/art-src/_review/020/td-row4-old.png
games/typing-defense/art-src/_review/020/c22-crop-inspect.png
games/typing-defense/art-src/_review/020/tre-ult.old-strip.png
games/typing-defense/art-src/_review/020/draconis-ult.old-strip-label.png
games/typing-defense/art-src/_review/020/ground-reference.jpg
games/typing-defense/art-src/_review/020/td-row3-selected.png
games/typing-defense/art-src/_review/020/tre-ult.try2-strip.png
games/typing-defense/art-src/_review/020/td-row4-selected.png
games/typing-defense/art-src/_review/020/t3-try1-3x3.png
games/typing-defense/art-src/_review/020/contrast-alpha-off.json
games/typing-defense/art-src/_review/020/seam-candidate.json
games/typing-defense/art-src/_review/020/td-row6-try2.png
games/typing-defense/art-src/_review/020/td-row7-try2.png
games/typing-defense/art-src/_review/020/new-files.json
games/typing-defense/art-src/_review/020/tre-ult.try1-strip-label.png
games/typing-defense/art-src/_review/020/owned-files.txt
games/typing-defense/art-src/_review/020/tre-ult.fix-strip-label.png
games/typing-defense/art-src/_review/020/td-row7-try1.png
games/typing-defense/art-src/_review/020/td-row6-try1.png
games/typing-defense/art-src/_review/020/v35-candidate.png
games/typing-defense/art-src/_review/020/t3-grass-a-3x3.png
games/typing-defense/art-src/_review/020/files-newer.txt
games/typing-defense/art-src/_review/020/audit-final.py
games/typing-defense/art-src/_review/020/files-newer-final.txt
games/typing-defense/art-src/_review/020/draconis-ult.try1-strip.png
games/typing-defense/art-src/_review/020/td-row5-old.png
games/typing-defense/art-src/_review/020/c22-candidate.png
games/typing-defense/art-src/_review/020/td-row5-selected.png
games/typing-defense/art-src/_review/020/td-row2-selected.png
games/typing-defense/art-src/_review/020/draconis-ult.fix-strip-label.png
games/typing-defense/art-src/_review/020/t3-selected-2x2.png
games/typing-defense/art-src/_review/020/td-row0-old.png
games/typing-defense/art-src/_review/020/moss-candidate.png.seam.png
games/typing-defense/art-src/_review/020/measure-v35.py
games/typing-defense/art-src/_review/020/draconis-ult-candidate.png
games/typing-defense/art-src/_review/020/v35-equal-base-0.png
games/typing-defense/art-src/_review/020/draconis-ult.fix-strip.png
games/typing-defense/art-src/_review/020/v35-green-cleanup.json
games/typing-defense/art-src/_review/020/draconis-ult.try1-strip-label.png
games/typing-defense/art-src/_review/020/coast-reference.jpg
games/typing-defense/art-src/_review/020/md5-after.txt
games/typing-defense/art-src/_review/020/td-row0-selected.png
games/typing-defense/art-src/_review/020/tre-ult.try1-strip.png
games/typing-defense/art-src/_review/020/td-row7-selected.png
games/typing-defense/art-src/_review/020/c22-key.png
games/typing-defense/art-src/_review/020/portraits-reference.jpg
games/typing-defense/art-src/_review/020/v35-equal-base-1.png
games/typing-defense/art-src/_review/020/td-row3-try1.png
games/typing-defense/art-src/_review/020/td-row2-try1.png
games/typing-defense/art-src/_review/020/audit-scoped.py
games/typing-defense/art-src/_review/020/v35-try2-key.png
games/typing-defense/art-src/_review/020/lam-candidate.png
games/typing-defense/art-src/_review/020/tre-key.png
games/typing-defense/art-src/_review/020/td-row6-selected.png
games/typing-defense/art-src/_review/020/td-row1-old.png
games/typing-defense/art-src/_review/020/td-row2-try2.png
games/typing-defense/art-src/_review/020/td-row3-try2.png
games/typing-defense/art-src/_review/020/td-row1-selected.png
games/typing-defense/art-src/_review/020/selected-measurements.json
games/typing-defense/art-src/_review/020/moss-overlap.png
games/typing-defense/art-src/_review/020/draconis-ult.try2-strip.png
games/typing-defense/art-src/_review/020/moss.fix.png.seam.png
games/typing-defense/art-src/_review/020/moss-seam-inspect.jpg
games/typing-defense/art-src/_review/020/tre-ult.old-strip-label.png
games/typing-defense/art-src/_review/020/td-row4-try1.png
games/typing-defense/art-src/_review/020/td-row5-try1.png
games/typing-defense/art-src/_review/020/moss-soft2-candidate.png
games/typing-defense/art-src/_review/020/v35-measure-candidate2.json
games/typing-defense/art-src/_review/020/td-row5.png
games/typing-defense/art-src/_review/020/td-row4.png
games/typing-defense/art-src/_review/020/moss-preseam.png
games/typing-defense/art-src/_review/020/tre-ult.try2-strip-label.png
games/typing-defense/art-src/_review/020/v35-measure-candidate.json
games/typing-defense/art-src/_review/020/audit-summary-final.json
games/typing-defense/art-src/_review/020/tre-ult-candidate.png
games/typing-defense/art-src/_review/020/td-row5-try2.png
games/typing-defense/art-src/_review/020/td-row4-try2.png
games/typing-defense/art-src/_review/020/tre-ult.fix-display-strip.png
games/typing-defense/art-src/_review/020/tre-ult.fix-strip.png
games/typing-defense/art-src/_review/020/td-row3-old.png
games/typing-defense/art-src/_review/020/v35-clean-candidate.png
games/typing-defense/art-src/_review/020/td-row6.png
games/typing-defense/art-src/_review/020/c22-clean.png
games/typing-defense/art-src/_review/020/t3-selected-3x3.png
games/typing-defense/art-src/_review/020/barracks-reference.jpg
games/typing-defense/art-src/_review/020/td-row7.png
games/typing-defense/art-src/_review/020/lam-key.png
games/typing-defense/art-src/_review/020/md5-diff.txt
games/typing-defense/art-src/_review/020/selected-measurements-final.json
games/typing-defense/art-src/_review/020/casuarina-v2-key.png
games/typing-defense/art-src/_review/020/moss-soft-candidate.png
games/typing-defense/art-src/_review/020/concurrent-files.txt
games/typing-defense/art-src/_review/020/td-row3.png
games/typing-defense/art-src/_review/020/td-row2-old.png
games/typing-defense/art-src/_review/020/td-row2.png
games/typing-defense/art-src/_review/020/olive-tree-v2-key.png
games/typing-defense/art-src/_review/020/draconis-ult.fix-display-strip.png
games/typing-defense/art-src/_review/020/finish-qa.py
games/typing-defense/art-src/_review/020/seam-soft2-candidate.json
games/typing-defense/art-src/_review/020/td-row0.png
games/typing-defense/art-src/_review/020/moss-soft2-candidate.png.seam.png
games/typing-defense/art-src/_review/020/td-row1.png
games/typing-defense/art-src/_review/020/t3-grass-a-3x3-comparison.jpg
games/typing-defense/art-src/_review/020c/verify-final.py
games/typing-defense/art-src/_review/020c/try2-64.jpg
games/typing-defense/art-src/_review/020c/try2-key.alpha.prompt.txt
games/typing-defense/art-src/_review/020c/normalization-all.txt
games/typing-defense/art-src/_review/020c/background-final.json
games/typing-defense/art-src/_review/020c/background.json
games/typing-defense/art-src/_review/020c/try3-key.alpha.png
games/typing-defense/art-src/_review/020c/identify-corners-final.txt
games/typing-defense/art-src/_review/020c/identify-corners.txt
games/typing-defense/art-src/_review/020c/try3-key.alpha.prompt.txt
games/typing-defense/art-src/_review/020c/brightness-all-tries.json
games/typing-defense/art-src/_review/020c/md5-result-final.json
games/typing-defense/art-src/_review/020c/md5-result.json
games/typing-defense/art-src/_review/020c/020c-v37-draft-try1.jpg
games/typing-defense/art-src/_review/020c/roi-comparison-final.jpg
games/typing-defense/art-src/_review/020c/020c-v37-final.jpg
games/typing-defense/art-src/_review/020c/md5-diff-final.txt
games/typing-defense/art-src/_review/020c/md5-before.txt
games/typing-defense/art-src/_review/020c/try1-128.jpg
games/typing-defense/art-src/_review/020c/try1-raw.prompt.txt
games/typing-defense/art-src/_review/020c/try3-64.jpg
games/typing-defense/art-src/_review/020c/md5-after.txt
games/typing-defense/art-src/_review/020c/try1-raw.png
games/typing-defense/art-src/_review/020c/normalization.txt
games/typing-defense/art-src/_review/020c/roi-spec.txt
games/typing-defense/art-src/_review/020c/md5-after-final.txt
games/typing-defense/art-src/_review/020c/verification-notes.txt
games/typing-defense/art-src/_review/020c/try1-64.jpg
games/typing-defense/art-src/_review/020c/roi-comparison.jpg
games/typing-defense/art-src/_review/020c/try2-raw.png
games/typing-defense/art-src/_review/020c/try2-raw.prompt.txt
games/typing-defense/art-src/_review/020c/verify.py
games/typing-defense/art-src/_review/020c/try2-128.jpg
games/typing-defense/art-src/_review/020c/roi-comparison-try1-fixed.jpg
games/typing-defense/art-src/_review/020c/try2-key.alpha.png
games/typing-defense/art-src/_review/020c/md5-diff.txt
games/typing-defense/art-src/_review/020c/brightness.json
games/typing-defense/art-src/_review/020c/try3-128.jpg
games/typing-defense/art-src/_review/020c/try1-key.alpha.png
games/typing-defense/art-src/_review/020c/roi-try1-direct.jpg
games/typing-defense/art-src/_review/020c/try1-key.alpha.prompt.txt
games/typing-defense/art-src/_review/020c/try3-raw.png
games/typing-defense/art-src/_review/020c/md5-diff-020c-only.txt
games/typing-defense/art-src/_review/020c/brightness-final.json
games/typing-defense/art-src/_review/020c/try3-raw.prompt.txt
games/typing-defense/art-src/_review/020b/moc-tinh.try1.128.prompt.txt
games/typing-defense/art-src/_review/020b/identify-corners.txt
games/typing-defense/art-src/_review/020b/md5-check.json
games/typing-defense/art-src/_review/020b/moc-tinh.try1.64.prompt.txt
games/typing-defense/art-src/_review/020b/md5-before.txt
games/typing-defense/art-src/_review/020b/md5-after.txt
games/typing-defense/art-src/_review/020b/normalization.txt
games/typing-defense/art-src/_review/020b/moc-tinh.try1.raw.prompt.txt
games/typing-defense/art-src/_review/020b/moc-tinh.try1.128.png
games/typing-defense/art-src/_review/020b/moc-tinh.try1.raw.png
games/typing-defense/art-src/_review/020b/md5-diff.txt
games/typing-defense/art-src/_review/020b/moc-tinh.try1.64.png
games/typing-defense/art-src/_review/020b/contact-sheet-command.txt
games/typing-defense/art-src/_review/020c-v37.jpg
games/typing-defense/art-src/_review/020-td.jpg
games/typing-defense/art-src/portraits/moc-tinh.png
games/typing-defense/art-src/portraits/lam.try1.prompt.txt
games/typing-defense/art-src/portraits/draconis-ult.try1.prompt.txt
games/typing-defense/art-src/portraits/tre-ult.try1.prompt.txt
games/typing-defense/art-src/portraits/tre-ult.try1.png
games/typing-defense/art-src/portraits/tre-ult.try2.png
games/typing-defense/art-src/portraits/moc-tinh.prompt.txt
games/typing-defense/art-src/portraits/dai-bang-tinh.fix.png
games/typing-defense/art-src/portraits/tre.try1.png
games/typing-defense/art-src/portraits/moc-tinh.try1.prompt.txt
games/typing-defense/art-src/portraits/moc-tinh.try1.png
games/typing-defense/art-src/portraits/tre.try1.prompt.txt
games/typing-defense/art-src/portraits/draconis-ult.fix.png
games/typing-defense/art-src/portraits/tre.fix.png
games/typing-defense/art-src/portraits/lam.fix.png
games/typing-defense/art-src/portraits/lam.try2.png
games/typing-defense/art-src/portraits/draconis-ult.try2.prompt.txt
games/typing-defense/art-src/portraits/tre-ult.fix.png
games/typing-defense/art-src/portraits/lam.try1.png
games/typing-defense/art-src/portraits/tre-ult.try2.prompt.txt
games/typing-defense/art-src/portraits/draconis-ult.try1.png
games/typing-defense/art-src/portraits/lam.try2.prompt.txt
games/typing-defense/art-src/portraits/draconis-ult.try2.png
games/typing-defense/art-src/branches/gold-mine-lo-duc-tien.png
games/typing-defense/art-src/branches/barracks-giao-dai.try1.prompt.txt
games/typing-defense/art-src/branches/gold-mine-lo-duc-tien.try3.prompt.txt
games/typing-defense/art-src/branches/gold-mine-lo-duc-tien.try1.prompt.txt
games/typing-defense/art-src/branches/gold-mine-lo-duc-tien.try2.prompt.txt
games/typing-defense/art-src/branches/barracks-giao-dai.try1.png
games/typing-defense/art-src/branches/barracks-giao-dai.try2.png
games/typing-defense/art-src/branches/gold-mine-lo-duc-tien.try2.png
games/typing-defense/art-src/branches/gold-mine-lo-duc-tien.try3.png
games/typing-defense/art-src/branches/gold-mine-lo-duc-tien.prompt.txt
games/typing-defense/art-src/branches/gold-mine-lo-duc-tien.try1.png
games/typing-defense/art-src/branches/barracks-giao-dai.fix.png
games/typing-defense/art-src/branches/barracks-giao-dai.try2.prompt.txt
```

## 4. T3: kích thước, mép nối và tương phản

`moss.fix.png`: **1024×1024**. Hậu kỳ: hạ tương phản, chồng mép bằng đường cắt tối thiểu cả hai trục, chuẩn hóa khổ bằng Lanczos với virtual-pixel tile, làm mềm toàn ảnh σ=1,25 px. Không dùng lật gương mép. Các bản trung gian và lần kiểm chưa đạt giữ trong `_review/020/`.

Đã chạy đúng script yêu cầu; đặt ảnh kiểm trong vùng được phép thay vì tạo sidecar ngoài whitelist:

```sh
export ART_MAGICK=/opt/homebrew/bin/magick
BASH_ENV="$PWD/games/typing-defense/art-src/_review/020/seam-environment.sh" bash tools/art-normalize/seam-check.sh games/dragon-hold/art-src/ground/pine-river/moss.fix.png games/typing-defense/art-src/_review/020/moss.fix.png.seam.png --axis xy
```

`seam-environment.sh` chỉ chuyển thư mục tạm của script sang `_review/020/normalize-work`, không sửa `tools/art-normalize`. Đích `<file>.seam.png` ở cạnh ảnh không nằm trong danh sách được ghi; ảnh kiểm vì vậy được lưu ở `_review/020/moss.fix.png.seam.png`.

| Trục | MAE mép (0–255) | MAE trung vị hai cột/hàng kề | Tỉ lệ mirror/control | Tỉ lệ chi tiết dải | Row step excess | Kết quả |
|---|---:|---:|---:|---:|---:|---|
| X | 1.059245 | 0.957682 | 1.031518 | 0.972723 | 4.707527 | Qua đủ 4 tiêu chí |
| Y | 0.925130 | 0.945638 | 0.800945 | 0.955450 | 4.513172 | Qua đủ 4 tiêu chí |

Kết quả chung `pass: true`. [JSON đầy đủ](../../games/typing-defense/art-src/_review/020/seam-final.json). Lần chưa làm mềm báo row_streak; σ=0,7 vẫn còn báo; σ=1,25 qua cả hai trục. MAE được đo lại trên chính file `.fix.png` đã chọn.

Độ chói chuẩn hóa khi tắt alpha trước khi đo: rêu **mean 0,434162; σ 0,037087**; cỏ A **mean 0,464320; σ 0,061339**. Rêu tối hơn nhẹ và có tương phản thấp hơn cỏ A; không còn khe tối/gò nổi như ảnh cũ. [Số đo](../../games/typing-defense/art-src/_review/020/contrast-alpha-off.json).

Đã tự xem ghép [2×2](../../games/typing-defense/art-src/_review/020/t3-selected-2x2.png), [3×3](../../games/typing-defense/art-src/_review/020/t3-selected-3x3.png) và [3×3 cạnh cỏ A](../../games/typing-defense/art-src/_review/020/t3-grass-a-3x3-comparison.jpg). Không thấy đường nối thẳng ở biên ô. Còn nhận ra nhịp mảng chéo khi lặp; đã trừ điểm đọc/hợp bộ.

## 5. C23 và C25: dải giữa 3:1

Hai file chọn đều **1536×1024**, cắt **1536×512 tại x=0, y=256**. Lượt 2 được tạo trực tiếp ở khoảng 3:1 (2048×683), chuẩn hóa về 1536×512, rồi thêm nền đồng màu ở trên/dưới để giữ khổ bộ. Không kéo méo nhân vật để nhét vào dải.

Đã đặt cả hai dải cạnh dải 3:1 của Draconis cũ tại [ultimate-vs-old-draconis.jpg](../../games/typing-defense/art-src/_review/020/ultimate-vs-old-draconis.jpg); toàn bộ lượt ở [ultimate-strips.jpg](../../games/typing-defense/art-src/_review/020/ultimate-strips.jpg). Đã tự xem: C23 giữ mặt, sừng, tay và mưa lông rơi; C25 giữ toàn đầu búa trên cao, hai bàn tay, búi tóc, gương mặt và giàn tre dựng nguyên.

## 6. V35: chiều cao ở cùng bề ngang chân

Đo hộp bao vật bằng ngưỡng tách nền: BG-G dùng sắc xanh khóa; mẫu barracks-v2 dùng nền xám trung tính. Bề ngang chân là bề ngang vật trong 45% dưới của hộp bao, gồm sàn/bàn trước; hai ảnh dùng cùng cách đo. Không lấy chiều cao canvas hoặc so ảnh ở hai tỉ lệ hiển thị khác nhau.

| Ảnh | Canvas | Hộp bao x,y,w,h | Bề ngang chân | Chiều cao vật | Chiều cao khi chân rộng 500 px | Tỉ lệ so mẫu |
|---|---|---|---:|---:|---:|---:|
| barracks-v2.png mẫu | 1102×1427 | 47,20,1029,1355 | 1029 px | 1355 px | 658,406 px | 100% |
| Nhánh cũ | 1024×1024 | 33,19,959,973 | 958 px | 973 px | 507,829 px | 77,13% |
| Lượt 1 | 1254×1254 | 36,24,1179,1192 | 1178 px | 1192 px | 505,942 px | 76,84% |
| **Bản chọn `.fix.png`** | **1024×1024** | **153,50,717,924** | **717 px** | **924 px** | **644,351 px** | **97,8653%** |

Đạt đích ≥95%. [Đối chiếu cùng bề ngang chân](../../games/typing-defense/art-src/_review/020/v35-equal-base.jpg). [Số đo](../../games/typing-defense/art-src/_review/020/v35-measure-candidate2.json). Bản nháp kéo tỉ lệ đạt 100,4% nhưng làm huy hiệu/trống méo nên không giao; bản chọn dùng vẽ lượt 2, hậu kỳ co **đồng tỉ lệ**.

BG-G bốn góc đúng `[0,255,0]`. Hai đốm xanh 14 và 13 px được thay bằng màu gỗ gần nhất; kiểm lại **0 thành phần xanh rời 1–16 px**. Các ô xanh lớn còn lại là khoảng hở cửa sổ/lan can thông nền, không phải đốm trên sàn. Mũi giáo xếp chạm/đè lên nhau trên nền gỗ kín, không khe xuyên nền xanh. [Bản ghi sửa đốm](../../games/typing-defense/art-src/_review/020/v35-green-cleanup.json), [kiểm cuối](../../games/typing-defense/art-src/_review/020/selected-measurements-final.json).

## 7. Tờ xem nhanh và phần chờ duyệt

- [020-dh.jpg](../../games/dragon-hold/art-src/_review/020-dh.jpg): ảnh cũ, lượt 1, bản chọn ghép 3×3; cỏ A ghép 3×3 để đối chiếu.
- [020-td.jpg](../../games/typing-defense/art-src/_review/020-td.jpg): mỗi hàng có ảnh cũ, mọi lượt tạo và bản chọn đúng cỡ; chân dung 128/64 px, cây 160 px. Font Arial đúng đường dẫn macOS được yêu cầu.
- Đã tự mở hai tờ nhanh, ghép 2×2/3×3, dải cắt và tờ so chiều cao; xem riêng C10/C22 ở 128/64 px.

Không bỏ qua ảnh nào trong chín ảnh. Không chạy Git, build hay bộ test game; không sửa mã, ART_*.md, IMAGE_AUDIT_*.md, Tu Tiên, Space hoặc handoff. Không gửi Tripo. Toàn bộ file có sẵn trước phiếu thuộc phạm vi chín ảnh được giữ nguyên; chỉ các bản hậu kỳ/tờ xem do phiếu này tạo được cập nhật trong lúc kiểm.

**Chờ Claude:** chấm lại cả chín bản `.fix.png`; T3, C10, C22, S15-v2, S16-v2 và V35 ở 8,5 cần người chấm thứ hai độc lập theo ART_ACCEPTANCE §4. Chưa có kết quả Claude trong phiên này; không tự ghi là đã nhận. Chủ dự án nên xem kỹ độ phẳng/nhịp lặp rêu, mặt đồng C22, mức gom lá của hai cây và bó giáo V35. Chỉ sau duyệt Claude mới thay ảnh đang dùng, cập nhật danh sách và bộ Tripo.
