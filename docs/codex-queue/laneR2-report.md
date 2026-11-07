# Vòng 2 · Bước 1a · Cột Lôi
- Trong `games/.wt-ic-lab-all` (`codex/lab-all`): thêm `src/lab/thunder-caster-r2.ts`, nối `five-phase-clip.ts`, đăng ký `tp2` trong `ab-flags.ts`; bổ sung test ở `tests/lab/`.
- Chỉ `tp2=1` cùng B8 mới bật: ấn chân lộ trong 0,20 s rồi ăn mòn 0,30 s (hết ở R0+0,50 s); tối đa 24 sprite hút vào tay; vòng chân nở 0,15 s, mờ 0,25 s. B8 phóng ngay R0 và tụ lực chồng lên như cũ.
- Nhịp đèn dùng nguyên `FlashLights` tại hook release B8 cùng khung âm phóng; không thêm đèn, video, shader hay đổi clock/sát thương/trạng thái.
- Mã thêm: 121 dòng, không tính test; tối đa 3 draw call thêm qua pool; test kiểm buffer/vector/options tái dùng và AST đường cập nhật không cấp phát.
- Đã qua `npx --no-install tsc --noEmit`, `npx --no-install vitest run --maxWorkers=4`: 126 file, 1.564 test; B8 bật/tắt `tp2` có buffer giống nhau từng khung, release/hit giữ nguyên.
- Ba nguồn Lôi này chưa có KTX2 trong kho hiện đọc; không sửa media/manifest. Dùng chung texture sparkle với B8; hai atlas PNG thêm ước tính 42,64 MB (40,67 MiB), tính RGBA và mipmap, dưới 64 MB; chưa đo GPU thực.
- Bỏ qua bay/chạm/dư âm, sinh media, build, trình duyệt và cổng mạng theo ranh giới phiếu; chưa nghiệm thu hình hay hiệu năng GPU.
- Claude cần quay cùng camera chơi/seed/đồng hồ: B8 tắt/bật `tp2`, 1920×1080, DPR 1, High; một cast rồi tải chồng thực tế, nền sáng/tối, lạnh/ấm, giảm chuyển động; thêm cận người tung và bảng quanh R0 đến +0,50 s.
- Đo trung vị các lượt: Δp95 ≤ 1,0 ms và p95 ≤ 11,5 ms, draw call/texture thực, phím→phóng ≤ 50 ms; chấm mù pha người tung và toàn chiêu trước bước tiếp, chưa tuyên bố đạt 8,5.

## Vòng 2 · Bước 1b · Kịch bản TP
- Thêm `TP` trong `games/.wt-ic-lab-all/scripts/visual/scenarios/lab-pilot-ab.mjs`: giữ P1–P4; A=B8, B chỉ thêm `tp2=1`; khóa seed/camera, X/Y và khóa riêng; hai góc `play`/`caster` (35–50%), 12 khung (8 khung R0→+0,60 s), chặn vùng hiệu ứng đỉnh <0,5%.
- Thêm `games/.wt-ic-lab-all/scripts/visual/scenarios/lab-tp-perf.mjs`: 10 cast/lượt, 3 lượt/bản, 1080p DPR 1 High, bầy mặc định; CPU + đọc 1 pixel chờ GPU; JSON p50/p95/p99/max, draw call, trung vị và Δp95; kết luận ĐẠT/TRƯỢT đúng ngân sách.
- `node --check` cả hai file: ĐẠT. Chưa quay/đo GPU; không mở trình duyệt/cổng mạng, không chạy build/test hay sửa mã lab. Claude cần chạy hai lệnh từ Mac và xem video/bảng khung cùng `tp-perf.json` trước bước tiếp.
- Quay: `(cd /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all && URL=http://127.0.0.1:3146/skills-lab.html EFFECTS=TP SEED=711 ART_MAGICK=/opt/homebrew/bin/magick OUT_DIR="/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/r2-step1/tp-ab-$(date +%Y%m%d-%H%M%S)-$$" ../../.local/bin/heavy.sh --gpu node src/kit/tools/cdp-run.mjs scripts/visual/scenarios/lab-pilot-ab.mjs --width=1920 --height=1080 --dpr=1)`
- Đo: `(cd /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all && BASE=http://127.0.0.1:3146/skills-lab.html RUNS=3 OUT_DIR="/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/r2-step1/tp-perf-$(date +%Y%m%d-%H%M%S)-$$" ../../.local/bin/heavy.sh --perf node src/kit/tools/cdp-run.mjs scripts/visual/scenarios/lab-tp-perf.mjs --width=1920 --height=1080 --dpr=1 --headful)`
