# Phiếu 379i · Tu Tiên · Cột hai tia dày: thân tia gãy gắt, lõi mảnh hơn

Codex chấm (379h): bản dày `v4-try3` thắng ba tiêu chí (nguồn chính 9,0, tia phụ 8,7, độ dày 8,7) nhưng nét sét 7,7: lõi trắng rộng làm thân tia trơn như dải năng lượng, nhịp uốn đều. Anh (13/11 14:2x): "bản dày hơn nhưng tia hơi mềm, nhìn thiếu lực, nó nên được sửa lại theo đề xuất của bạn để tốt hơn… tạm chấp nhận lần này để nó xong việc sấm sét đã". Kết quả phiếu này dùng làm cột chính rồi làm video.

**Model `gpt-6.1-sol`, mức `high`. Tối đa 4 lần `image_gen`** (dùng công cụ `image_gen` ở chế độ sửa ảnh, đưa ảnh gốc vào: 2 lần cho ảnh cột, 2 lần cho dải bốn khung), `view_image` tối đa 6. Báo cáo `docs/codex-queue/379i-report.md` (Codex tự viết).

## Đường dẫn
`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`. Chỉ thêm `S/thunder-energy-column.v5-try*.png`, `S/thunder-energy-column-frames.v5-try*.png`, một `.prompt.txt` cho mỗi ảnh (ghi ảnh gốc đã sửa), tấm ghép `S/thunder-energy-379i-sheet.jpg`. Giữ nguyên bản cũ. Cấm git ghi, sửa file có sẵn, mã.

## Ảnh gốc
`S/thunder-energy-column.v4-try3.png`, `S/thunder-energy-column-frames.v4-try3.png`. Tham chiếu nét: `S/thunder-single-bolt-a.v4-try9.png`.

## Sửa (giữ bề rộng tổng, độ dày quầng, chân, mây, tia phụ, màu)
- **Thân hai tia chính gãy gắt:** mỗi tia là chuỗi đoạn gần thẳng nối nhau ở góc gấp nhọn (khoảng 30–70°), độ dài các đoạn không đều (có đoạn dài, có đoạn ngắn giật), không còn uốn lượn theo nhịp đều.
- **Lõi trắng mảnh hơn:** lõi trắng thuần chỉ khoảng 1/3 bề dày tia, nằm trong quầng vàng nhạt dày (quầng giữ bề dày bản gốc), để tia vẫn dày mà có nét sắc.
- Vài gai điện nhỏ bật ra ở các góc gấp.
- Bốn khung sửa giống hệt, mỗi khung đường gãy khác nhau.

## Kiểm và tự chấm
Script (đạt khi mọi điều sau đúng): bề rộng thân bằng bản gốc ± 10 % (hàng 40/50/60 %, ngưỡng 50 % độ sáng lớn nhất của hàng, trung vị); lõi trắng (điểm ảnh > 90 % độ sáng lớn nhất của hàng) rộng ≤ 40 % bề dày tia (ngưỡng 50 %) trên ít nhất 2 trong 3 hàng; lề ≥ 6 %; chân cùng hàng (lệch ≤ 2 % chiều cao). Tấm ghép: `v3-try4` | `v4-try3` | bản mới cạnh nhau cùng cỡ, dải bốn khung, bản thu cao 120 px. Tự chấm theo bốn tiêu chí của `docs/codex-queue/379h-report.md` (nguồn chính, tia phụ, độ dày và độ hẹp thân, nét sét), điểm cuối là thấp nhất. Báo cáo ≤ 150 chữ.

Phản biện: PASS (Sonnet, 13/11; ghi rõ image_gen và ngưỡng lõi)
