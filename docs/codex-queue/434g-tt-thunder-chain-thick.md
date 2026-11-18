# Phiếu 434g: Lôi, sét nối quái dày đều mọi bước (full-access, tự nhìn)

Phản biện: PASS (Sonnet, 17/11)

## Bối cảnh
Ở bản 434f (`typing-game-review/owner-review/2026-11-17/tu-tien/thunder-codex-f.jpg`), sét lớn đã dùng cột Ngũ Lôi và đạt ≥ 40 px. Sét nối quái thì chưa đạt: 6 trên 8 bước đạt ≥ 14 px, hai bước cuối còn mảnh, và nhìn ở camera chơi đoạn nối còn ngắn.

Ngày 17/11 owner chọn "Sửa sét nối dày đều". Câu này nghĩa là mọi bước phải dày như tia Ngũ Lôi và đủ dài để nối từ quái này sang quái kia.

Các điều sau giữ nguyên như `docs/codex-queue/434f-tt-thunder-use-five-thunder.md`:
- quyền chạy, server 3148, ffmpeg, prune;
- phạm vi sửa (`games/.wt-ic-lab-all/src/lab/thunder-ult-*`, `cloud-volume*`);
- import từ `five-thunder.ts`, không sửa file đó;
- cách đo và probe.

Được ghi `docs/codex-queue/434g-report.md` và `ABOUT.md`. Chạy xong phải tắt Chrome và xoá thư mục profile tạm của mình.

## Việc
1. **Mọi bước sét nối dày đều.** Ở camera chơi, thân tia ≥ 14 px ở mọi bước, kể cả hai bước cuối. Độ dày không được giảm dần theo bước.
2. **Tia phủ hết đoạn nối.** Mỗi tia kéo giãn từ ngực quái này tới ngực quái kế tiếp, phủ ≥ 90 % đoạn nối trên màn hình. Không để hở hai đầu.
3. **Giữ nguyên:**
   - nhịp zíc zắc;
   - cột sét lớn;
   - mây ở dải trên khung;
   - vết đất;
   - vùng trắng ≤ 6 %.

## Vòng lặp
- Tối đa 3 vòng.
- Chụp ở camera chơi (Alt+1) và góc sau lưng (Alt+2), nền `?ground=%23353a40`.
- In ra mỗi vòng:
  - bề dày từng bước sét nối;
  - % phủ đoạn nối;
  - vùng trắng;
  - p95.

## Nghiệm thu
- Kiểm kiểu 0 lỗi; p95 ≤ 16,7 ms.
- Lưu `thunder-codex-g.jpg` và `thunder-codex-g.mp4` mới, giữ file cũ, thêm dòng vào `ABOUT.md`.
- Xoá khung thô. Không commit.
