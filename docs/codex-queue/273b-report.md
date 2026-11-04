# Báo cáo phiếu 273b · A.A theo hạng cho lửa phím 1

**Trạng thái: đã làm đúng công thức và tạo đủ đầu ra; CHƯA ĐẠT Kiểm 2.** Từ tick 9 sang 10, diện tích sáng tăng **2,4846%**, vượt ngưỡng nhiễu 2%. Không đổi lời giải, shader hoặc ngưỡng kiểm để ép đạt. Hồ sơ hiện ghi `CPU_preview_checks_failed`; công cụ xem trước thoát mã 1 có chủ ý khi kiểm này thất bại.

## 1. Đã làm

- [impact_masks.py](../../tools/vfx-masks/impact_masks.py): thêm `--survival-rank` đi cùng `--force`, tính hạng trung bình từ điểm life/EDT chưa lượng tử hóa; mở rộng mép mềm theo điểm vỏ gần nhất, làm mềm σ 0,6. Chỉ thay A.A; kiểm RGB trước ghi và sau đọc lại.
- [preview-masked.ts](../../tools/vfx-masks/preview-masked.ts): dựng đủ 43 tick bằng các hàm CPU thật của game; tạo tấm tick cũ, MP4, chuỗi diện tích và kiểm tự động. Khung thô ở bộ nhớ, không tạo hàng loạt PNG.
- [README.md](../../tools/vfx-masks/README.md): lệnh chạy, công thức, bản sao, cấu trúc video và kết quả kiểm hiện tại.
- Trong `games/immortality-cultivation/art-src/lab/vfx/fire/impact-k1-r2/`: cập nhật đúng `fire-impact-k1-r2-v1a.a4.maskA.png` và `fire-impact-k1-r2-v1a.a4.masks.json`; trước đó đã sao lưu nguyên bản thành `…a4.maskA.v1.png` và `…a4.masks.v1.json`. Bản sao không bị ghi đè khi chạy tiếp.

Đầu ra trong [273-out](../../.local/codex-runs/273-out/): [preview-ticks.png](../../.local/codex-runs/273-out/preview-ticks.png), [channels-k00-k23.png](../../.local/codex-runs/273-out/channels-k00-k23.png), [preview.mp4](../../.local/codex-runs/273-out/preview.mp4), [preview-area.json](../../.local/codex-runs/273-out/preview-area.json), hồ sơ/số đo và log có tiền tố `273b-`. Đã xem hai tấm PNG và [khung 12 từ video](../../.local/codex-runs/273-out/273b-video-frame12.jpg).

## 2. Kiểm bắt buộc

| Kiểm | Kết quả |
| --- | --- |
| 1 · RGB mới trùng maskA.v1 mọi điểm | **Đạt**; toàn bộ 10.616.832 byte RGB trùng. |
| 2 · Đơn điệu 9–42, nhiễu tối đa 2% | **Chưa đạt** tại 9→10: 10.384→10.642 điểm, tăng 2,4846%; bản sRGB 8 bit tăng 2,6207%. Từ 10 tới 42 không có lần tăng nào khác. |
| 2 · Tick 12 trong 0,50–0,80 | **Đạt: 0,683744** (7.100 điểm). |
| 2 · Tick 18 trong 0,10–0,30 | **Đạt: 0,191641** (1.990 điểm). |
| 2 · Tick 42 bằng 0 | **Đạt: 0**; tick 40–42 đều 0. |
| 3 · Gốc > mũi | **Đạt 24/24 ô**, đo lại trên PNG đã ghi. |
| 4 · Video | **Đạt**: H.264, yuv420p, 768×768, 60 fps, **430/430 khung**, 7,166667 s, **497.217 byte** <5 MB; ffprobe đọc đủ và ffmpeg giải mã toàn bộ không lỗi. |
| 5 · Phạm vi ghi | **Đạt theo chênh lệch với mốc ban đầu**: chỉ thêm dòng trạng thái của báo cáo; trạng thái submodule Tu Tiên giữ nguyên. |

Kiểm độc lập dùng `scipy.stats.rankdata(method="average")−1` và `logical_and.accumulate` để tính tuổi, thay vì thuật toán xếp hạng và đếm tuổi của công cụ chính: **A.A của 24/24 ô khớp công thức từng byte**, không có điểm lệch. Viền 2 px giữ 0. Chi tiết từng ô ở [273b-independent-verification.json](../../.local/codex-runs/273-out/273b-independent-verification.json); tổng hợp ở [273b-final-verification.json](../../.local/codex-runs/273-out/273b-final-verification.json).

## 3. Chuỗi diện tích

Độ sáng Rec.709 tuyến tính >0,1 sau kẹp HDR, trước mã hóa sRGB, không tính nhãn; chuẩn hóa theo 10.384 điểm của tick 9. Toàn bộ tick 0–42 đã in trong [273b-preview.log](../../.local/codex-runs/273-out/273b-preview.log), gồm cả số điểm và số sau mã hóa PNG. Chuỗi kiểm từ 9 tới 42 (tick:tỉ lệ):

```text
9:1.000000  10:1.024846  11:0.860555  12:0.683744  13:0.564522  14:0.489696
15:0.396764  16:0.322997  17:0.246148  18:0.191641  19:0.161113  20:0.150616
21:0.138771  22:0.127311  23:0.118163  24:0.106799  25:0.100250  26:0.088790
27:0.078005  28:0.067893  29:0.059707  30:0.052099  31:0.046610  32:0.043529
33:0.038713  34:0.034958  35:0.032165  36:0.024364  37:0.016371  38:0.007993
39:0.004815  40:0.000000  41:0.000000  42:0.000000
```

Tại tick 9, `ctl=[1,-0.08,0.08,0]`, vFrame=3,6; tại tick 10, `ctl=[1,0.081405,0.08,0.25]`, vFrame=4. Bộ ghép thật đồng thời đổi khung và bắt đầu trộn ramp. **Chưa tách riêng đóng góp của hai thay đổi này**; không quy lỗi cho lượng tử hóa hay tự kết luận phải sửa shader. Kết quả độc lập đã xác nhận phần A.A đúng lời giải; Claude cần quyết định cách xử lý chỗ tăng còn lại.

## 4. Bảo toàn và Git

So toàn bộ thư mục art-src với mốc trước: **56 tệp cũ, chỉ hai tệp được phép đổi; thêm đúng hai bản v1**. RGBA, maskB, atlas, clip, mọi ảnh/prompt khác giữ nguyên cả MD5 và mtime. Hai bản v1 khớp MD5 của hai tệp cũ. [273b-art-verification.json](../../.local/codex-runs/273-out/273b-art-verification.json) ghi toàn bộ danh sách; [273b-art-files-ls.txt](../../.local/codex-runs/273-out/273b-art-files-ls.txt) là `ls -la` sáu tệp liên quan.

| Tệp | Byte | MD5 |
| --- | ---: | --- |
| `fire-impact-k1-r2-v1a.a4.maskA.v1.png` | 801965 | `d900551e350f09352bc4265ea75b0b9a` |
| `fire-impact-k1-r2-v1a.a4.masks.v1.json` | 42918 | `f5f7da25fdb7c7eb071f273e12ba678c` |
| `fire-impact-k1-r2-v1a.a4.maskA.png` | 866764 | `01ca37174e6881c031bda65ecb6ab1b5` |
| `fire-impact-k1-r2-v1a.a4.masks.json` | 66515 | `55b4dcf621cf527e3588091c1e624570` |

Repo cha có nhiều thay đổi từ trước, nên không thể báo `git status --short` sạch ngoài phạm vi một cách trung thực. Đã lưu trạng thái trước/sau với `--untracked-files=all`; ba công cụ đã là untracked trước khi sửa. So sánh ở [273b-git-comparison.json](../../.local/codex-runs/273-out/273b-git-comparison.json):

```text
Thêm: ?? docs/codex-queue/273b-report.md
Bớt: (không có)
```

## 5. Cách chạy và bàn giao

Chạy Python đúng mẫu uv offline của phiếu, với `--force --survival-rank`; trả mã 0. Chạy Node bằng loader tsx có sẵn của game, `--force`; tạo đủ đầu ra rồi trả mã 1 do Kiểm 2. Không có lỗi hạn mức hay yêu cầu chờ. Bản sao cache uv riêng trong 273-out đã xóa; cache gốc không đổi.

Không sửa shader/màu than, mã game, manifest, script/test hoặc docs Tu Tiên; không nối lab, không chạy build/bộ test game, không mở cổng/trình duyệt, không chạy Git ghi. Không tạo ảnh AI/âm thanh. Không chuyển tệp sang typing-game-review vì ngoài đường ghi của phiếu; Claude chuyển khi cần.

**Anh cần xem preview.mp4, tấm tick và bước 9→10 chưa đạt.** Đoạn cuối vẫn trắng vàng theo ramp 258; đổi thành than đỏ là phiếu shader riêng do Claude chốt. Đầu ra được giữ đầy đủ để tiếp tục, chưa đánh dấu nghiệm thu.
