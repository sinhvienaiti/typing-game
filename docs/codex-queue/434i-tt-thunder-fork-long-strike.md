# Phiếu 434i: Lôi, sét lan nhiều hướng và sét lớn kéo dài 3–4 s (full-access, tự nhìn)

Phản biện: PASS (Sonnet, 17/11, vòng 2)

## Bối cảnh
Owner duyệt bản 434h (`typing-game-review/owner-review/2026-11-17/tu-tien/thunder-codex-h.jpg`), trong đó sét nối giữa các quái dùng ảnh C. Ngày 17/11 owner yêu cầu thêm: "sét lan vào quái nên có nhiều tia ra nhiều hướng, sét đánh xuống nên lâu hơn, đánh khoảng 3 4 giây".

Giữ nguyên theo `docs/codex-queue/434h-tt-thunder-chain-use-c.md`:
- quyền chạy, server 3148, ffmpeg, prune;
- phạm vi sửa (`games/.wt-ic-lab-all/src/lab/thunder-ult-*`, `cloud-volume*`, tài nguyên trong `art-src/lab/vfx/thunder/`);
- cách đo.

Được ghi `docs/codex-queue/434i-report.md` và `ABOUT.md`. Khi xong phải tắt Chrome và xoá profile tạm.

## Việc
1. **Sét lan toả.** Mỗi khi một quái bị sét chạm, từ quái đó tỏa ra 2–4 tia sét C đi theo các hướng khác nhau. Góc giữa hai tia cạnh nhau ≥ 40°.
   - Mỗi tia chạm một quái gần, trong bán kính khoảng 6 m. Nếu không có quái thì tia tắt giữa chừng, đầu tia toé tia lửa nhỏ.
   - Sét lan ra như mạng nhện qua đàn quái, có thể lan 2–3 tầng.
   - Tổng số tia sáng cùng lúc ≤ 24.
   - Mỗi tia dùng một biến thể C khác nhau, lệch ngẫu nhiên có hạt giống.
2. **Sét lớn kéo dài 3–4 s.** Cột sét Ngũ Lôi đánh liên tục trong 3–4 s, không phải một nhát rồi thôi.
   - Thân cột chớp, giật và đổi hình liên tục: đổi khung hoặc đổi biến thể mỗi 0,06–0,12 s.
   - Có 2–3 nhịp bùng mạnh (lóe 2 khung). Vùng trắng toàn khung ≤ 6 % ở mọi khung.
   - Chân cột liên tục tỏa sét bò trên đất và tia lửa.
   - Quái quanh chân cột giật liên tục.
   - Âm thanh kéo dài theo, lặp hoặc nối lớp của âm Lôi có sẵn.
3. **Mốc thời gian (tính từ lúc kích chiêu, cố định):** mây tụ 0–0,6 s; sét lan 0,6–2,4 s; cột sét 2,4–6,0 s (3,6 s); mây tan và dư điện 6,0–7,0 s. Tổng 7,0 s.
4. **Giới hạn số tia:** mỗi quái bị chạm tỏa 2–4 tia (góc giữa hai tia cạnh nhau ≥ 40°); nếu tổng tia sáng cùng lúc sắp vượt 24 thì tầng sau giảm còn 2 tia mỗi quái, rồi bỏ quái xa nhất. Đạt khi: tầng 1 có ≥ 3 tia, ít nhất 2 tầng, mọi góc ≥ 40°, cùng lúc ≤ 24.
5. **Phạm vi thêm:** quái giật dùng hook hit/jolt sẵn có qua `skills-main.ts` theo cách 434f đã gọi (chỉ gọi hook đã có, không sửa `skills-main.ts` hay logic quái); âm kéo dài làm trong `thunder-ult-*` bằng cách phát lặp/nối lớp file âm Lôi có sẵn (không sửa file âm, không thêm file âm mới).

## Vòng lặp
- Tối đa 3 vòng: sửa → chụp → mở ảnh → so với phân cảnh và nhận xét của owner → sửa.
- Chụp ở các mốc: 1,2 s (sét lan), 2,0 s (sét lan tầng 2), 2,5 s (đầu cột sét), 4,2 s (giữa cột sét), 5,8 s (cuối cột sét), 6,5 s (dư âm).
- Chụp ở camera chơi (Alt+1) và góc sau lưng (Alt+2), nền `?ground=%23353a40`.
- Mỗi vòng in ra: số tia mỗi tầng, góc tỏa, thời lượng cột sét, vùng trắng lớn nhất, p95.

## Nghiệm thu
- Kiểm kiểu 0 lỗi; p95 ≤ 16,7 ms, đo trong lúc cột sét đang đánh.
- Lưu `thunder-codex-i.jpg` và clip `.mp4` dài 7 s (giữ file cũ), thêm một dòng vào `ABOUT.md`.
- Xoá khung thô. Không commit.
