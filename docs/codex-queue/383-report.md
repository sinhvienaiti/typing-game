# Phiếu 383 — hoàn tất nguồn ảnh

Đã tạo 6 ô 1024×1024 tại `games/immortality-cultivation/art-src/ground/thanh-thach/`, 8 decal RGBA 512×512 tại `games/immortality-cultivation/art-src/decals/thanh-thach/`. Mỗi ảnh có `.prompt.txt` ghi prompt nguyên văn, tham chiếu, hậu kỳ và tự chấm.

Tấm ghép: [ground-383-sheet.jpg](../../games/immortality-cultivation/art-src/ground/thanh-thach/ground-383-sheet.jpg): sáu mẫu lặp 3×3, tám decal trên ô 2, phối hành lang/sân/decal ở camera B 42°, cặp nguồn–hậu kỳ.

Kiểm bằng script: đúng kích thước; MAE mép 3,92–9,76/255, tỷ lệ so với pixel kề 0,81–1,27; cả hai trục đạt ngưỡng 2,5. Decal lề ≥8,4%, alpha mềm, không pixel tràn xanh >30 mức. Lá nâu xám; vết nước xám xanh lạnh.

Tự chấm theo mặt yếu nhất: sáu ô lần lượt **8,3 / 8,3 / 8,2 / 8,2 / 8,1 / 8,2**; tám decal **8,2 / 8,1 / 8,3 / 8,1 / 8,1 / 8,2 / 8,2 / 8,3**.

Dùng **14/20** lượt image_gen; không bỏ ảnh nào. Không sửa mã, file có sẵn, Git hay chạy build/test game. Chưa nhập runtime hoặc nghiệm thu 8,5; anh xem độ rõ trận văn và mức dịu của vết cháy.
