# Làn Codex 3 · Ảnh: ấn trên đất cho Hỏa và 12 hệ còn lại (danh sách việc, làm lần lượt)

Anh (06/11 22:05): "Duyệt ấn Hỏa". Trước đó anh đã duyệt bộ 7 ấn Kim (phiếu 323, 324, 324b) và 2 mẫu ấn Hỏa (phiếu 327). Đây là danh sách của **làn 3**. Làm **lần lượt từng hệ**; xong một hệ thì tự kiểm theo mục "Đạt khi", ghi một đoạn vào báo cáo, rồi mới sang hệ kế tiếp.

**Model `gpt-6.1-sol`, mức `high`.** Báo cáo duy nhất: `docs/codex-queue/lane3-report.md` (tiếng Việt, ngắn): mỗi hệ một bảng điểm và tên tấm ghép.

## Ranh giới với hai làn kia (bắt buộc)
- Làn 1 sửa mã trong `games/.wt-ic-swarm-sim`; làn 2 ghi atlas vào `art-src/lab/vfx/`. Không đụng hai chỗ đó.
- **Chỉ thêm file mới** (`cp -n`) vào `S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`, đúng tên ở dưới. Không sửa, không xoá file có sẵn. Không lệnh git ghi, không mở cổng mạng, không dùng ảnh ngoài repo.

## Cách vẽ mỗi ảnh (giống phiếu 323, 324, 327)
- **Mốc dáng** (anh đã duyệt, gửi kèm mọi lần gọi `image_gen`), bản đã chọn của bộ Kim:
  - `S/metal-sigil-hex.v1-try2.png`, `S/metal-sigil-line.v1-try1.png`, `S/metal-sigil-arcs.v1-try2.png`, `S/metal-sigil-arrow.v1-try2.png`;
  - `S/metal-sigil-spiral.v1-try2.png`, `S/metal-crack-star.v1-try1.png`, `S/metal-rift-groove.v1-try3.png`.

  Mỗi ảnh gửi đúng mốc cùng dáng của nó.
- **Mốc chất liệu của hệ** (anh đã duyệt): `S/<hệ>-crescent-sym.v1-try1.png` và `S/<hệ>-ground-mark.v1-try1.jpg` (hoặc bản `-clean` nếu có). Chỉ lấy chất liệu, màu và ánh sáng; **dáng giữ đúng mốc Kim**.
- Prompt như phiếu 324 (mở file đó đọc), thay câu chất liệu thép bằng câu chất liệu của hệ, rút từ mốc chất liệu. **Hỏa:** dùng đúng câu chất liệu của phiếu 327. **Ám:** chỉ đen và đỏ thẫm, không tím, không tía; nét sáng đỏ thẫm có viền khói đen.
- Nhìn thẳng từ trên xuống, nền đen thuần, không chữ, lề trống, khổ 16:9.
- Ghi `.prompt.txt` cùng tên cho mỗi ảnh (công cụ, ảnh tham chiếu, prompt nguyên văn, khổ thật).
- **Tự chấm** như phiếu 324, gồm "cùng dáng với mốc Kim". Dưới 8 thì vẽ lại một lần (`-try2`) và chọn bản cao hơn.

## Danh sách việc
| # | Hệ | Ảnh cần vẽ (tên tệp trong `S/`, đuôi `.v1-try1.png`) |
|---|---|---|
| 1 | fire | `fire-sigil-arcs`, `fire-sigil-arrow`, `fire-sigil-spiral`, `fire-crack-star`, `fire-rift-groove` (`fire-sigil-hex`, `fire-sigil-line` đã có) |
| 2 | water | `water-sigil-hex`, `-line`, `-arcs`, `-arrow`, `-spiral`, `water-crack-star`, `water-rift-groove` |
| 3 | thunder | 7 ảnh như trên |
| 4 | wind | 7 ảnh |
| 5 | ice | 7 ảnh |
| 6 | earth | 7 ảnh |
| 7 | wood | 7 ảnh |
| 8 | light | 7 ảnh |
| 9 | dark | 7 ảnh (màu theo luật Ám ở trên) |
| 10 | poison | 7 ảnh |
| 11 | blood | 7 ảnh |
| 12 | void | 7 ảnh |
| 13 | star | 7 ảnh |

## Đạt khi (mỗi hệ)
- Có đủ ảnh của hệ đó, mỗi ảnh tự chấm ≥ 8 (sau tối đa một lần vẽ lại). Ảnh nào vẫn dưới 8 thì ghi rõ và vẫn sang hệ kế tiếp.
- Có tấm ghép `S/<hệ>-sigils-set-sheet.jpg`: 7 bản đã chọn, lưới 4 cột, kèm tên ngắn tiếng Anh, nền đen. Mở bằng `view_image` để kiểm đúng ô.
- Đo hộp nét ở ngưỡng sáng 5 % (như phiếu 324b): không ảnh nào chạm mép; rãnh cao không quá 10 % khung; xoắn ốc chiếm khoảng 70 % chiều cao.

## Hết hạn mức
Giữ file, ghi báo cáo phần đã xong (hệ nào xong, hệ nào chưa). Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
