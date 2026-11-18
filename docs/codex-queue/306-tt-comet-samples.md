# Phiếu 306 · Tu Tiên · Ảnh 2D: 2 mẫu sao băng rơi chéo (Hỏa, Thủy), 2 lần gọi `image_gen`

Anh (06/11 09:30) chê sao băng nghiêng D62: thân rơi đang dùng lưỡi liềm kiếm khí. Lưỡi liềm chỉ hợp với chiêu phóng ra từ kiếm; chiêu rơi từ trời phải có dáng riêng. Phiếu này vẽ **2 mẫu** cho anh duyệt trước khi làm đủ 14 hệ (luật: xem mẫu trước khi làm cả đợt). Phiếu ảnh ngắn, prompt đã chốt.

**Model `gpt-6.1-sol`, mức `high`. Đúng 2 lần gọi `image_gen`, không gọi thêm, không tự sửa lại.** Báo cáo: `docs/codex-queue/306-report.md` (tiếng Việt, ngắn).

## Đường dẫn
`D = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`. **Được ghi:** chỉ thêm file mới vào `D` (`cp -n`) và báo cáo. **Cấm:** mọi lệnh git ghi; sửa hay xóa file có sẵn; mở cổng mạng; ảnh ngoài làm tham chiếu.

## Cách làm mỗi ảnh
1. Mở ảnh tham chiếu của hệ bằng `view_image`. Đó là ảnh anh đã duyệt; chỉ lấy chất liệu, ánh sáng, độ phát sáng và độ hoàn thiện, **không lấy dáng lưỡi liềm**.
2. Gọi `image_gen` tạo mới, khổ ngang, kèm ảnh đó, **nền đen** (không bật nền trong suốt). Prompt dán nguyên văn, thay `<MATTER>` bằng cột chất liệu.
3. Chép bằng `cp -n` thành `D/<tên ra>.png`.
4. Ghi `D/<tên ra>.prompt.txt`: công cụ, ảnh tham chiếu, prompt đã gửi, khổ thật.

```text
Use the attached image only as the reference for material, light, glow and finish; do not copy its crescent shape. A meteor of <MATTER> falling diagonally from the upper left toward the lower right, about 20 degrees from vertical: a dense blazing rounded head with a white-hot core and a bright shimmering rim, followed by a long tapering tail of the same matter that streams back up toward the upper left, thins and breaks into sparks, embers and glints, with soft halos around the head. Seen from a high three-quarter game camera about 55 degrees down. Premium Chinese donghua xianxia skill effect, mythic and radiant, translucent energy, anime-mythic, not realistic. The whole meteor inside the frame with a wide empty border, solid pure black background, no ground, no crescent, no sword, no text.
```

| Tên ra | Ảnh tham chiếu | `<MATTER>` |
|---|---|---|
| `fire-comet.v1-try1` | `D/fire-crescent-sym.v1-try1.png` | dense white-gold, amber and vermilion flame with embers and sparks |
| `water-comet.v1-try1` | `D/water-crescent-sym.v1-try1.png` | clear deep-blue spirit water with a bright white pressure edge, thin foam and caustic light |

## Xong khi
Có đủ 2 bộ `.png` và `.prompt.txt`. Báo cáo ghi khổ thật, số lần gọi (phải là 2), và một câu mỗi ảnh: đầu sao băng có rõ không, đuôi có thon dần không, có dáng lưỡi liềm hay chữ lọt vào không.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
