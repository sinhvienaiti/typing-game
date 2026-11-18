# Phiếu 433l: Kim, sửa 7 lỗi kiếm trận owner nêu (full-access, tự nhìn)

Phản biện: PASS (Sonnet, 18/11, vòng 3)

Nguồn hình: games/.wt-ic-lab-all/art-src/lab/vfx/metal-ult/rays.png, games/.wt-ic-lab-all/art-src/lab/vfx/metal-ult/formation-simple-a.atlas.png, games/immortality-cultivation/art-src/lab/vfx/metal-ult/stills/energy-sword.v1-try1.png, games/immortality-cultivation/art-src/lab/vfx/metal-ult/stills/sword-trail.v1-try4.png, games/immortality-cultivation/art-src/third-party/smoke/unity-labs-vfx/flipbooks/DiscSmoke01_16x4.tga, games/immortality-cultivation/art-src/third-party/smoke/unity-labs-vfx/flipbooks/Explosion01-light-nofire_5x5.tga, games/.wt-ic-lab-all/art-src/lab/vfx/metal/metal-sparkle.atlas.png

## Bối cảnh
Owner xem bản 433k (`typing-game-review/owner-review/2026-11-18/tu-tien/metal-rain-k.jpg`) và nêu 7 lỗi, ngày 18/11:
1. Trận pháp vẫn không hợp với góc nhìn trong video.
2. Kiếm nhỏ quá to.
3. Kiếm rơi xuống là mất luôn. Đúng ra rơi xong khoảng 1 s phải còn một nhóm kiếm cắm dưới đất.
4. Hiệu ứng mặt đất khi kiếm nhỏ chạm đất nhìn ảo và xấu.
5. Toàn bộ VFX của skill vẫn như đồ chơi, chưa ra một kỹ năng hùng mạnh.
6. Kiếm cắm xuống đất bị dựng thẳng đứng, không hợp lý.
7. Kiếm bay ra quá xa so với kiếm trận.

Các phần giữ nguyên theo `docs/codex-queue/433k-tt-metal-giant-aura-c.md`:
- luật "chỉ đặt, xoay, thu phóng đều, nhuộm, chỉnh độ mờ, chạy flipbook";
- quyền chạy, server 3148, ffmpeg, prune;
- phạm vi sửa (`games/.wt-ic-lab-all/src/lab/metal-ult-*`, `metal-sword-look.ts`, tài nguyên mới trong `games/.wt-ic-lab-all/art-src/lab/vfx/metal-ult/`).

Được ghi `docs/codex-queue/433l-report.md` và `ABOUT.md` trong `typing-game-review/owner-review/2026-11-18/tu-tien/`. Khi xong, tắt Chrome và xoá profile tạm.

Giữ nguyên: trận A, hào quang C của kiếm lớn, kiếm năng lượng A, vệt D.

## Việc
1. **Trận đặt ngay trên vùng đánh, song song mặt đất (lỗi 1 và 7).**
   - Tâm trận nằm thẳng trên tâm vùng kiếm rơi. Trận nằm ngang, cao 12–16 m.
   - Kiếm rơi **thẳng đứng hoặc lệch ≤ 12°** từ dưới mặt trận xuống đất bên dưới.
   - Mọi điểm cắm nằm trong hình chiếu của trận xuống đất, bán kính ≤ 1,05 lần bán kính trận.
   - Ở camera chơi, trận phải đọc được là "ở trên cao, ngay trên vùng đánh": vùng sáng mờ in dưới đất thẳng dưới trận **là chính ảnh trận A** (`formation-simple-a`) đặt phẳng trên đất, nhuộm vàng tối, độ mờ ≤ 0,2; tia sáng rủ thẳng xuống dùng `rays.png` có sẵn. Không vẽ lớp nào bằng code. Trận phải **nằm trọn khung camera chơi, lề ≥ 4 %**; nếu 12–16 m làm ra khung thì hạ độ cao (tối thiểu 9 m); nếu ở 9 m vẫn ra khung thì giảm bán kính trận (tối thiểu 7 m) và thu vùng kiếm rơi theo; ghi số đã chọn.
   - Bỏ cách đặt trận lùi ra sau của 433j.
   - Quãng rơi vẫn đạt mức 433f: trung vị ≥ 0,45 s và ≥ 18 % chiều cao khung.
2. **Kiếm nhỏ nhỏ lại (lỗi 2).** Thân kiếm ở camera chơi cao 20–26 px (thu phóng đều cả kiếm và vệt). Kiếm lớn cao gấp ≥ 4 lần kiếm nhỏ.
3. **Nhóm kiếm cắm lại trên đất (lỗi 3).** Kiếm cắm giữ hiện rõ ít nhất 1,5 s sau khi chạm đất, rồi tan bằng độ mờ trong 0,5 s. Khi mưa dày nhất, cùng lúc phải thấy ≥ 25 kiếm cắm, giới hạn ≤ 60 kiếm đang hiển thị (tính cả kiếm đang bay, đang cắm và đang tan); để vừa ngân sách, lúc mưa dày nhất số kiếm đang bay ≤ 20, còn ≥ 25 là kiếm cắm.
4. **Kiếm cắm giữ góc rơi (lỗi 6).** Kiếm cắm nghiêng đúng hướng rơi, mũi ngập vào đất 15–25 %. Quad ảnh kiếm cố định theo góc cắm trong không gian thế giới, không quay theo camera, không dựng thẳng lại.
5. **Chạm đất thật hơn (lỗi 4).**
   - Bỏ hiệu ứng chạm đất hiện tại của kiếm nhỏ (giữ code, ngừng gọi).
   - Thay bằng: một chớp bụi xám nâu nhỏ, thấp, từ flipbook CC0 `DiscSmoke01_16x4` nhuộm màu đất, sống 0,4–0,6 s; một chùm tia lửa nhỏ `metal-sparkle`.
   - Không có đĩa sáng, không có vòng (bóng ảnh trận A in dưới đất ở mục 1 được miễn cả luật này lẫn luật 'không đĩa sáng' của 433k).
6. **Hùng mạnh hơn (lỗi 5).**
   - Mưa kiếm dồn nhịp: khi mưa dày nhất, camera rung nhẹ liên tục (`UltCameraPunch`, chỉ import).
   - Lúc kiếm lớn chạm đất:
     - một cú nổ bụi lớn `Explosion01-light-nofire_5x5` nhuộm vàng xám, phủ ≥ 25 % bề ngang khung;
     - camera rung mạnh hơn;
     - quái quanh điểm chạm hất văng hoặc giật (hook có sẵn);
     - âm Kim có sẵn nối lớp to hơn.
   - Cả cảnh tối nhẹ trong pha mưa (một lớp tối toàn màn hình một màu phẳng, không có hình dạng, độ mờ ≤ 0,25), để vàng nổi bật hơn.
   - Vùng trắng ≤ 6 %.

## Vòng lặp
- Tối đa 4 vòng: sửa → chụp → mở ảnh → đối chiếu **từng lỗi 1–7** → sửa.
- Chụp camera chơi (Alt+1) và sau lưng (Alt+2), nền `?ground=%23353a40`, ở các mốc: đợt 1, giữa mưa, mưa dày nhất, kiếm lớn chạm đất, +1,5 s.
- Mỗi vòng in ra:
  - chiều cao kiếm nhỏ và kiếm lớn (px);
  - lề nhỏ nhất của trận trong khung camera chơi, độ cao trận đã chọn;
  - khoảng cách xa nhất từ điểm cắm tới tâm trận, chia cho bán kính trận;
  - góc rơi lớn nhất;
  - số kiếm cắm cùng lúc;
  - góc cắm có bằng góc rơi không;
  - quãng rơi;
  - vùng trắng;
  - p95.
- Báo cáo có bảng 7 dòng, mỗi dòng ghi một lỗi là đã sửa hay chưa, kèm số đo.

## Nghiệm thu
- Kiểm kiểu 0 lỗi; p95 ≤ 16,7 ms.
- Lưu `metal-rain-l.jpg` và `.mp4` vào `typing-game-review/owner-review/2026-11-18/tu-tien/`, thêm một dòng vào `ABOUT.md`.
- Xoá khung thô. Không commit.
