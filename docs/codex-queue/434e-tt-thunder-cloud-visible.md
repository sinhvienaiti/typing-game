# Phiếu 434e — Lôi: hạ mây vừa đủ thấy ở góc chơi (full-access, tự nhìn)

Phản biện: PASS (Sonnet, 17/11, vòng 2)

## Bối cảnh
434d (`typing-game-review/owner-review/2026-11-17/tu-tien/thunder-codex-d.jpg`): mây đã cao, không che quái, nhưng ở camera chơi gần như không thấy mây. Owner 17/11 chọn "Hạ mây vừa đủ thấy": mây chiếm dải 15–25 % trên cùng khung ở góc chơi, vẫn không che quái; sét lớn đánh từ mây xuống thấy rõ. Quyền, server 3148, ffmpeg, prune, phạm vi sửa (`games/.wt-ic-lab-all/src/lab/thunder-ult-*`, `cloud-volume*`), probe và cách đo giữ như `docs/codex-queue/434d-tt-thunder-cloud-high.md`; được ghi `docs/codex-queue/434e-report.md`.

## Việc
1. Ở camera chơi 1280×720: mây (alpha ≥ 0,5) chiếm dải từ mép trên xuống 15–25 % chiều cao khung, phủ ≥ 60 % bề ngang; số quái bị mây phủ = 0. Đặt bằng vị trí/độ cao thế giới, không ép màn hình. Góc sau lưng giữ như 434d.
2. Sét lớn: thân sét nối liền từ đáy mây thấy được trên màn hình xuống điểm đánh (không đứt đoạn ở mép khung).
3. Giữ sét dây chuyền, ánh tím, dư điện của 434d.
4. **Thay vết đất ở điểm đánh sét lớn** (owner 17/11 chê: "vệt lôi bạn lại dùng cái vệt rõ xấu kia", ảnh: vết hình sao tím tối có chấm trắng dưới cụm quái ở khung 3,0 s). Bỏ decal hình sao đó (giữ file trong thư viện), thay bằng đúng ô dưới trái/dưới phải phân cảnh 431: 6–10 nhánh tia sét bò trên mặt đất tỏa ra từ điểm đánh, sáng rồi tắt trong 0,4–0,6 s, để lại vết cháy nứt mảnh màu xám than ấm (không tím đặc, không hình sao, không chấm trắng), mờ dần trong 1,5 s. Dùng `games/.wt-ic-lab-all/art-src/lab/vfx/thunder/thunder-scorch-crack-top.*` cho vết nứt cháy; in số nhánh và thời gian sáng/tắt trong báo cáo; nếu không có thì chỉ giữ nhánh tia sét và ánh sáng, ghi vào báo cáo để Claude tạo thành phần.
5. Đối chiếu phong cách: mọi lớp phải giống phân cảnh 431 (tím–trắng điện, sắc nét); không tự thêm lớp ngoài phân cảnh.
Tối đa 3 vòng; in dải mây (%), số quái bị phủ, vùng trắng.

## Nghiệm thu
Kiểm kiểu 0 lỗi; p95 ≤ 16,7 ms. Lưu `thunder-codex-e.jpg/.mp4` mới (giữ file cũ), dòng `ABOUT.md`. Xoá khung thô. Không commit.
