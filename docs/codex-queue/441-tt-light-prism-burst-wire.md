# Phiếu 441: Quang, đóng gói video nổ D và gắn vào điểm trúng (full-access, tự nhìn)

Phản biện: PASS (Sonnet, 17/11, vòng 2)

## Bối cảnh
Ngày 17/11 owner chọn video `games/immortality-cultivation/art-src/lab/vfx/light/firefly-raw/light-prism-burst.v1-try1.mp4` cho cú nổ kết của Quang. Video là Firefly 1:1, 5 s, nền đen, làm từ ảnh tĩnh D đã duyệt; câu của owner: "Bản 1". Video chưa tắt hẳn về đen ở cuối, nên phải cắt và làm mờ phần đuôi.

Bản hiện tại là 439d (`typing-game-review/owner-review/2026-11-17/tu-tien/light-ult-codex-d.jpg`): điểm nổ nhỏ và yếu, tia cuối như một cột trắng.

Owner cho chạy full-access để Codex tự chụp ("Cho full-access", 17/11). Quyền, server 3148, ffmpeg, prune, cách đo và probe giữ như `docs/codex-queue/439d-tt-light-ult-power.md`.

Phạm vi sửa:
- chỉ `src/lab/light-ult-*` và một script cắt mới `src/lab/light-ult-cut.mjs`, viết theo mẫu `metal-ult-cut.mjs`;
- tài nguyên mới vào `games/.wt-ic-lab-all/art-src/lab/vfx/light/`;
- được ghi thêm: `docs/games/tu-tien/skills/VFX_LIBRARY.md`, `typing-game-review/owner-review/2026-11-17/tu-tien/ABOUT.md` và `docs/codex-queue/441-report.md`.

Mọi đường dẫn `src/lab/...` và `art-src/...` tính từ gốc `games/.wt-ic-lab-all/`.

## Việc
1. **Đóng gói flipbook `light-prism-burst`.** Dùng cùng định dạng với các flipbook có sẵn trong thư mục (`.atlas.png` + `.json` + `.uastc.ktx2`, như `light-big-burst`).
   - Lấy khoảng 0–3 s, khoảng 24–32 khung.
   - Đen thành alpha (cộng sáng).
   - Làm mờ dần về 0 trong 25 % khung cuối.
   - Giữ lề.
   - Ghi chấm đáy (điểm chạm đất, khoảng 62 % chiều cao khung) vào `.json` để neo đúng chỗ.
2. **Gắn vào điểm trúng của tia hội tụ.** Tia hội tụ vẫn nằm giữa trục quạt như owner đã chốt.
   - Flipbook dựng đứng trong không gian thế giới, quay về camera theo trục đứng, chấm đáy đặt trên mặt đất tại điểm trúng.
   - Cỡ 5–7 m.
   - Thay flipbook `light-big-burst` cũ ở điểm trúng (giữ file cũ trong thư viện).
   - Giữ tia lửa, ánh sáng rọi và rung camera của 439d.
3. **Đầu tia hội tụ không còn là cột cụt.** Đầu tia thu nhỏ dần và chìm vào lõi nổ.
4. **Luật chung:** chỉ cú nổ được rực nhất (một điểm nhấn), vùng trắng toàn khung ≤ 6 %, không vòng hay đĩa dưới đất.

## Vòng lặp và đo
- Tối đa 4 vòng: sửa → chụp → mở ảnh → so với ô dưới trái của phân cảnh `games/immortality-cultivation/art-src/concept/ult-storyboards/light-storyboard.v1-try1.png` → sửa.
- Chụp ở camera chơi (Alt+1) và góc sau lưng (Alt+2), nền `?ground=%23353a40`.
- Giữ các số đo của 439d. Khung nổ là khung có độ sáng trung bình cao nhất trong vòng 120 px quanh điểm trúng, tìm trong 0,5 s sau lúc tia hội tụ chạm; in thời điểm của khung này. Ở khung nổ, độ phủ sáng trong vòng 120 px quanh điểm trúng phải ≥ 55 %.

## Nghiệm thu
- Kiểm kiểu 0 lỗi; p95 ≤ 16,7 ms.
- Lưu `light-ult-codex-e.jpg` và `.mp4` mới, giữ file cũ, thêm một dòng vào `ABOUT.md`.
- Ghi flipbook mới vào `docs/games/tu-tien/skills/VFX_LIBRARY.md`.
- Xoá khung thô. Không commit, không đưa media vào Git.

## Giao nộp
`docs/codex-queue/441-report.md`.
