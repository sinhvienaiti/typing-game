# Phiếu 433k — Kim: hào quang C cho kiếm lớn (full-access, tự nhìn)

Phản biện: PASS (Sonnet, 18/11)

Nguồn hình: games/immortality-cultivation/art-src/lab/vfx/metal-ult/stills/giant-sword-aura.v1-try3.png

## Bối cảnh
Owner 18/11 chọn hào quang **C** (quầng hình thoi, sao hai đầu) của phiếu 448 (`typing-game-review/owner-review/2026-11-18/tu-tien/giant-sword-aura-448/giant-sword-aura-448.jpg`) cho kiếm lớn. Phiếu 433j đã gỡ viền lông nhọn và nhuộm phẳng, kiếm lớn hiện vật liệu gốc GLB. **Chỉ chạy sau khi 433j xong** (cùng file). Luật, quyền, server 3148, ffmpeg, prune, phạm vi sửa giữ như `docs/codex-queue/433j-tt-metal-bigger-swords-formation-back.md`; được ghi atlas/texture mới vào `games/.wt-ic-lab-all/art-src/lab/vfx/metal-ult/`, `docs/codex-queue/433k-report.md`, `ABOUT.md`. Tắt Chrome và xoá profile tạm khi xong.

## Việc
1. Cắt ảnh C: nền đen → alpha cộng sáng, giữ nguyên hình; ghi tâm khe kiếm vào `.json`.
2. Đặt C **phía sau** kiếm lớn: quad dựng đứng theo trục kiếm, quay mặt về camera quanh trục đó; khe giữa ảnh khớp thân kiếm; thu phóng đều sao cho chiều cao khe ≈ chiều cao thân kiếm.
3. Nhịp: hào quang hiện khi kiếm lớn bắt đầu rơi, sáng rõ lúc chạm đất, sáng nhịp nhẹ (chỉnh độ mờ) khi cắm, tan cùng kiếm.
4. Khôi phục chỉ tiêu tỷ số sáng kiếm lớn/nhỏ ≥ 1,5 (đo như 433i). Vùng trắng ≤ 6 %. Không thêm lớp nào khác.

## Vòng lặp
Tối đa 3 vòng sửa → chụp → mở ảnh → so với hàng ghép thử của C → sửa; camera chơi (Alt+1) và sau lưng (Alt+2), nền `?ground=%23353a40`, gồm khung lúc kiếm lớn chạm đất. In tỷ số sáng, vùng trắng, p95.

## Nghiệm thu
Kiểm kiểu 0 lỗi; p95 ≤ 16,7 ms. Lưu `metal-rain-k.jpg/.mp4` vào `typing-game-review/owner-review/2026-11-18/tu-tien/`, dòng `ABOUT.md`. Xoá khung thô. Không commit.
