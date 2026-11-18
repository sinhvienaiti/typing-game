# Phiếu 362c — bốn loài v3

Đủ **8 ảnh**; image_gen **11/16 lượt**, view_image **9/20 lượt**. Chỉ dùng tham chiếu nội bộ.

**A = `games/immortality-cultivation/art-src`.**

- `A/beasts/{hoa-nha,nham-vien,thach-thu,thiet-giap-tru}.v3-{q,front}-final.png`.
- Tám bản gốc `.v3-{q,front}-final-raw.png`; tám `.v3-{q,front}-final.prompt.txt` ghi prompt, tham chiếu và hậu xử lý.
- `A/beasts/bestiary-362c-sheet.jpg`: boss v3 và bốn loài, hai góc, cùng bề ngang vật 300 px; ô canvas 66×66 px và đối chiếu gốc/chốt cùng cỡ.

**Kiểm script:** tất cả canvas 1024×1024, một khối 8-liên thông; nền đúng #00FF00, không còn pixel vật có G vượt max(R,B). Framecheck, shadowcheck đều PASS; chiều cao hai góc lệch **0%**.

| Loài | Cao Q/trước (px) | Rộng Q/trước (px) | Lề nhỏ nhất |
|---|---:|---:|---:|
| Hỏa Nha | 697/697 | 767/767 | 12,50% |
| Nham Viên | 713/713 | 798/735 | 11,04% |
| Thạch Thử | 660/660 | 807/726 | 10,55% |
| Thiết Giáp Trư | 571/571 | 800/733 | 10,94% |

Tự chấm theo góc yếu hơn:

| Loài | Đáng sợ 66 px | Cùng bộ boss | Dựng Tripo |
|---|---:|---:|---:|
| Hỏa Nha | 8,1 | 8,5 | 8,2 |
| Nham Viên | 8,3 | 8,6 | 8,4 |
| Thạch Thử | 8,0 | 8,3 | 8,2 |
| Thiết Giáp Trư | 8,4 | 8,6 | 8,4 |

Thạch Thử đã sửa răng cửa, chọn lại góc Q; bỏ thử nghiệm chính diện quá bè. Cần chủ dự án duyệt nét hung của Thạch Thử và mặt Hỏa Nha ở 66 px. Chưa nghiệm thu mù hoặc kiểm chứng model Tripo.

Giữ nguyên v2 và boss; không sửa mã, ghi Git, chạy build/test hoặc tạo 3D.
