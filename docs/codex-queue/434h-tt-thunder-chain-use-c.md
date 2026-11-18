# Phiếu 434h — Lôi: sét nối dùng đúng ảnh C owner đã chọn (full-access, tự nhìn)

Phản biện: PASS (Sonnet, 17/11)

## Bối cảnh
434g (`typing-game-review/owner-review/2026-11-17/tu-tien/thunder-codex-g.jpg`): sét nối dày nhưng là dải hồng trơn. Owner 17/11: "tại sao sấm sét giật quái bạn làm xấu quá vậy, đã dùng ảnh tham khảo để tạo chưa, chứ nhìn xấu quá"; "sửa lại". Owner đã chọn ảnh sét nối **C**: `games/immortality-cultivation/art-src/lab/vfx/thunder/stills-55/thunder-bolt-ff.v1-try3.png` (Firefly, nền đen, sét ngang tự nhiên nhiều nhánh khác nhau, hai đầu có chấm sáng). Quyền, server 3148, ffmpeg, prune, phạm vi sửa (`games/.wt-ic-lab-all/src/lab/thunder-ult-*`, `cloud-volume*`), cách đo giữ như `docs/codex-queue/434g-tt-thunder-chain-thick.md`; được ghi tài nguyên mới vào `games/.wt-ic-lab-all/art-src/lab/vfx/thunder/`, `docs/codex-queue/434h-report.md`, `ABOUT.md`. Tắt Chrome và xoá profile tạm khi xong.

## Việc
1. Cắt ảnh C thành texture cộng sáng (đen → alpha), đánh dấu hai chấm neo đầu/cuối (toạ độ trong `.json`). Thêm 2 biến thể bằng lật dọc/ngang để các bước không giống hệt nhau.
2. Mỗi bước sét nối = một quad 3D đặt giữa ngực hai quái, hai chấm neo trùng hai quái, xoay theo đoạn nối, quay mặt về camera theo trục đoạn nối; kéo giãn theo chiều dài, giữ tỉ lệ dày tối thiểu (thân ≥ 14 px ở camera chơi).
3. Nhịp: mỗi bước lóe sáng đủ ở khung đầu, chớp tắt 1–2 lần (độ sáng nhấp nháy), mờ trong 0,18–0,25 s; đổi biến thể và lệch nhẹ ngẫu nhiên có hạt giống.
4. Bỏ dải ribbon code của 434g (giữ code trong file nhưng không dùng). Giữ cột sét lớn Ngũ Lôi, mây, vết đất, zíc zắc; vùng trắng ≤ 6 %.

## Vòng lặp
Tối đa 3 vòng sửa → chụp → mở ảnh → so với ảnh C và nửa phải phân cảnh `games/immortality-cultivation/art-src/concept/ult-storyboards/ult-storyboard-samples-431.jpg` → sửa. Camera chơi (Alt+1) và sau lưng (Alt+2), nền `?ground=%23353a40`. In bề dày từng bước, vùng trắng, p95.

## Nghiệm thu
Kiểm kiểu 0 lỗi; p95 ≤ 16,7 ms. Lưu `thunder-codex-h.jpg/.mp4` mới (giữ file cũ), dòng `ABOUT.md`. Xoá khung thô. Không commit.
