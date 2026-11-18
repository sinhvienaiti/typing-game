# B8 · Mẫu năm pha Cột Lôi

Đã làm trong `games/.wt-ic-lab-all`, nhánh `codex/lab-all`, chỉ cho `pillar-thunder-single` theo `docs/games/VFX_STANDARD.md`:
- Thêm `src/lab/five-phase-clip.ts`: tụ lực chồng 0,20 s ở tay bằng `thunder-charge`, dùng riêng một giọng `ChargeFillFx` để không ngắt từ đang gõ; viền tím trắng và sparkle hút vào. Phóng ngay trong lệnh tung, lấy khung đỉnh của `thunder-release` (khung 19), đèn lóe và ribbon dựng đứng bay lên.
- Giữ cột trụ, ấn báo trước 0,20 s và đồng hồ trúng cũ. Tại cú trúng thêm `thunder-impact`, `thunder-ground-impact`; giữ phản ứng quái `heavy`, `stagger-stars-loop` và thời gian choáng 1 s trên đường trúng sẵn có. `thunder-hit-affliction` bám quái sống, theo vị trí và tàn khi hết choáng; chết thì dừng.
- Dư âm: giữ ấn đất 2 s như cũ, thêm sparkle lệch pha, thưa dần và erosion, hết trong 2,20 s sau cú trúng. Các lớp hào quang mới và ấn đất của mẫu có hệ số mỗi kênh ≤ 0,9. Lớp bám được cấp tuổi thật cho erosion của shader có sẵn, dù mỗi khung vẽ lại theo thân quái.
- Sửa `src/lab/clip-skills.ts` ở các điểm nối riêng Cột Lôi; `src/lab/skills-main.ts` nối tay/viền/đèn/camera và nạp trước khi mục Cột Lôi được chọn. `src/lab/ab-flags.ts` thêm **Thunder Pillar five phases**; `?fivephase=0` bỏ toàn bộ lớp mới, giữ bản cũ.
- Thêm `tests/lab/five-phase-clip.test.ts` (11 test), cập nhật `tests/lab/ab-flags.test.ts` cho cờ mới. Không đổi bảng chiêu, sát thương, thời gian trúng, hit-stop hoặc rung ở cú trúng; không sinh hình hay âm mới.

Kiểm tra: `npx --no-install tsc --noEmit` sạch; `npx --no-install vitest run --maxWorkers=4` qua **124 file / 1.509 test**; `git diff --check` sạch. Test Node xác nhận đủ thứ tự năm pha (tụ lực/phóng/bay chồng ngay ở thời điểm bấm), khung phóng đầu lấy đúng đỉnh và alpha 1, thời điểm trúng bằng bản cũ cả atlas lẫn video bị giữ đồng hồ, choáng/điện bám đúng hạn, dư âm còn sau 1,5 s và hết trước 2,5 s, cờ tắt không tải lớp mới, tái sử dụng pool/buffer/vector/options trong các khung đã ấm. Đây là xác nhận logic và dữ liệu dựng; chưa phải đo độ sáng pixel hoặc chấm hình trên màn hình.

Âm giữ nguyên, gồm `tt-sfx-pillar-thunder` và đường release/impact cũ. Có các nguồn Firefly hợp pha nhưng **chưa gắn**, trong `art-src/lab/firefly-sprint-2026-11-05/sound/` (mỗi mục có `take1.wav`–`take4.wav` và prompt):
- Tụ lực: `tt-sfx-el-thunder-charge`.
- Phóng: `tt-sfx-thunder-cast`.
- Bay/cột rơi: `tt-sfx-thunder-pillar`.
- Chạm mạnh: `tt-sfx-thunder-hit-heavy`.
- Dư âm và điện bám: `tt-sfx-thunder-tail`, `tt-sfx-el-thunder-affliction`.

Claude cần quay cho anh: chọn `pillar-thunder-single`, giữ cùng camera/chất lượng/bầy quái, quay bản mặc định và `fivephase=0`; thêm cặp `video=0` để kiểm atlas. Mỗi bản quay camera chơi và cận tay–kiếm/quái, gồm một cú vào quái còn sống đủ 1 s choáng, một cú giết, rồi chờ ít nhất 2,5 s sau cú trúng. Lấy khung phóng đầu, mốc báo đất, khung đỉnh trụ/chạm và mốc tàn 1,5/2,5 s; xem thẻ chữ, độ sáng và chuyển động ở tốc độ thường/nửa tốc độ. Kiểm thêm bấm nhanh nhiều lần và chuyển sang chiêu khác để thấy mẫu chỉ tác động Cột Lôi.

Chưa quay/chấm mù hoặc đo GPU, chữ ≥ 7:1, độ sáng pixel: ticket cấm trình duyệt và mở cổng. Chưa nhận đạt hình ảnh 8,5. Không build, không sửa media/âm/đường dẫn cấm và không chạy lệnh Git ghi.
