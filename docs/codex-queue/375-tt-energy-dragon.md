# Phiếu 375 · Tu Tiên · Linh kiện: rồng năng lượng vẽ bằng nét sáng, thân chia đốt

Anh (12/11 19:0x–19:2x) muốn làm rồng theo cách: một con rồng dài đẹp, rồi uốn theo nhiều đường, nhân số lượng theo góc quay để ra nhiều kỹ năng. Kế hoạch: `docs/work/tasks/energy-dragon-kit.md` bước 1. Theo luật linh kiện (AGENTS.md "Components first"): vẽ **các đốt rời của một con rồng** để code nối theo đường cong, không vẽ con rồng trọn cảnh.

**Model `gpt-6.1-sol`, mức `high`. Tối đa 10 lần `image_gen`**, `view_image` tối đa 12. Báo cáo `docs/codex-queue/375-report.md`.

## Đường dẫn
`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`. Chỉ thêm `S/energy-dragon-{head,body,tail,claw}.v1-try*.png`, một `.prompt.txt` cho mỗi ảnh (ghi đường dẫn tham chiếu), tấm ghép `S/energy-dragon-375-sheet.jpg`. Cấm git ghi, sửa file có sẵn, mã.

## Tham chiếu (`view_image`)
`S/azure-cloud-dragon.v1-try1.png` (hình rồng của dự án), `S/thunder-single-bolt-a.v4-try9.png` và `S/thunder-column-c.v1-try1.png` (chất nét sáng bạch kim đã duyệt). Không dùng ảnh ngoài repo.

## Bốn ảnh, nền đen thuần (để cộng sáng), nhìn ngang hơi từ trên, rồng **vẽ bằng nét sáng** (viền và gân sáng, lòng thân trong mờ, không thân đặc), bạch kim D65 (trắng ngà, vàng nhạt):
1. **head** 1024×1024: đầu rồng phương Đông nhìn nghiêng, sừng hươu, râu, bờm lửa năng lượng, miệng há, mắt sáng; cổ cắt phẳng ở mép phải.
2. **body** 2048×512: một đoạn thân **lặp liền theo trục x** (cột pixel đầu khớp cột cuối), vảy nét sáng, vây lưng, độ dày đều. Làm lặp liền bằng script: dịch nửa chiều dài, hoà chéo hoặc vá đường nối, rồi dịch về.
3. **tail** 1024×512: đuôi thon dần tan thành tia năng lượng; mép trái khớp với body.
4. **claw** 512×512: một chân rồng ba hoặc bốn móng, gốc chân sạch để gắn vào thân.
Lề ≥ 6 % trừ mép nối. Không chữ.

## Kiểm và tự chấm
Script: body lặp liền (hiệu cột đầu/cuối), mép nối head/tail khớp chiều cao thân, nền đen sạch, trắng thuần ≤ 6 %. Tấm ghép: head + 3 đoạn body + tail nối thành một con, và bản thu cao 120 px. Tự chấm theo mặt yếu nhất (đẹp, ghép liền, đọc ở cỡ nhỏ, hợp bạch kim); dưới 8 vẽ lại. Báo cáo ≤ 300 chữ.

Phản biện: PASS (Sonnet, 12/11; lỗi phản biện nêu đã sửa)
