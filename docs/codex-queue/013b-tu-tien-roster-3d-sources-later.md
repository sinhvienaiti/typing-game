# Phiếu 013b · Tu Tiên Thủ Ải · ảnh nguồn 3D cho 6 nhân vật sau MVP, linh thú, pháp khí

**Bối cảnh:** như phiếu 013. Chủ dự án duyệt cả 10 chân dung ngày 25/10 (canon D49). Phiếu này làm phần **sau MVP**:
- Phù nam, Phù nữ;
- Hỏa nam, Hỏa nữ;
- Ngự thú nam, Ngự thú nữ;
- 2 linh thú: linh lộc, linh cáo một đuôi;
- pháp khí cầm tay của họ.

Chạy **sau** phiếu 013 và theo đúng cách làm của 013. Đọc `art-src/README-013.md` trước để tránh lặp lỗi.

**Thư mục làm việc:** gốc repo `D:\typing-game`. Chỉ được ghi vào:
- `docs/games/tu-tien/art-requests/m0b/14-roster-3d-sources-later.md`;
- `games/immortality-cultivation/art-src/cultivators/`, `art-src/companions/`, `art-src/treasures/`;
- `games/immortality-cultivation/art-src/README-013b.md`;
- mục 6.1 của `docs/games/3D_REQUESTS.md`.

Không chạy git, không sửa mã hay canon.

## Nguồn

- **Như phiếu 013:** canon D47, D49, §21.2; mẫu `m0b/01-cultivators-bots.md`; file prompt `m0b/13-roster-3d-sources.md` vừa viết.
- **Chân dung đã duyệt:** `art-src/roster/{phu,hoa,ngu-thu}-{nam,nu}.png`.

## Việc

1. **Nhân vật:** 6 nhân vật × trước và sau, 1024×1536, tư thế A, nền `#E6E6E6`, bàn tay để trống.
   - Lưu `cultivators/<phai>-<nam|nu>.png` và `-back.png`.
   - Pháp khí là vật riêng, không cầm trong ảnh nguồn.
   - Ghi 3D: face limit 20000, tự rig Blender bằng bộ xương mẫu của phiếu 013, clip như 013.
2. **Linh thú:** linh lộc (`companions/linh-loc.png` ngang, `-front.png` trước) và linh cáo một đuôi (`companions/linh-cao.png`, `-front.png`).
   - Bốn chân, đứng thẳng, nền `#E6E6E6`.
   - Đúng như chân dung đã duyệt: lộc có chồi gạc ngắn; cáo đúng một đuôi.
   - Ghi 3D:
     - face limit 6000;
     - tự rig Blender: bốn chân nhỏ, dáng đi riêng; không dùng preset Tripo.
     - clip: Idle, Move, Follow, Cast_Assist, Hit.
3. **Pháp khí** (vật tĩnh, không rig, mỗi món 1–2 góc):
   - bút lông lớn (`treasures/but-phu.png`);
   - tập phù lục (`treasures/phu-luc.png`);
   - quạt xếp lửa, mở nửa (`treasures/quat-hoa.png`);
   - ấn hổ phách (`treasures/an-ho-phach.png`);
   - sáo trúc (`treasures/sao-truc.png`);
   - sáo ngọc (`treasures/sao-ngoc.png`).
   - Đính kèm chân dung của chủ nhân để giữ đúng hình.
4. **3D_REQUESTS:** thêm các dòng NV05–NV10, LT01–LT02 (linh thú), PB04–PB09 (pháp khí), ghi mốc "sau MVP".
5. **Kiểm và README:** như phiếu 013.
   - Không dùng `tools/art-normalize` trừ khi `CODEX_QUEUE.md` ghi phiếu 012 "Claude đã duyệt".
   - Ảnh xem nhanh: `art-src/_review/013b-sources.png`.

**Xong khi:**
- file prompt viết xong;
- 12 ảnh nhân vật, 4 ảnh linh thú, ảnh pháp khí có đủ, hoặc ghi lý do;
- `3D_REQUESTS.md` đã cập nhật;
- README đã có.
