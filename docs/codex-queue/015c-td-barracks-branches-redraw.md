# Phiếu 015c · Lời Gọi · vẽ lại 2 ảnh nhánh Trại Lính theo tháp hai tầng

**Bối cảnh:** lượt chấm lại theo luật 7 điểm (26/10/2026) xếp hai ảnh nguồn Tripo này ở mức **Tạo lại, P2**. Chi tiết và lý do ở `docs/games/ART_FIX_QUEUE.md` §3:
- V34 `branches/barracks-khien-dong.png`: 6,5 điểm;
- V35 `branches/barracks-giao-dai.png`: 5,5 điểm.

Cả hai vẽ theo nhà dài thấp cũ (`buildings/barracks.png`). Trại Lính đang dùng là **tháp hai tầng**: ảnh `buildings/barracks-v2.png`, model `art-src/3d/buildings/barracks.glb`, 9,5 điểm. Cùng bề ngang chân, hai nhánh chỉ cao khoảng nửa tháp, nên lên nhánh thì nhà thấp đi và mất tháp. Ảnh so: `docs/games/ART_FIX_QUEUE.md` §3.

**Thư mục làm việc:** gốc repo. Chỉ được ghi vào:
- `games/typing-defense/art-src/branches/` (ảnh, `.prompt.txt`);
- `games/typing-defense/art-src/README-015c.md`;
- `games/typing-defense/art-src/_review/015c-*.jpg`.

Không chạy git, không sửa mã, không dùng `tools/art-normalize`. Không đụng Tu Tiên.

## Luật (đọc `docs/games/ART_ACCEPTANCE.md`)

- Mỗi ảnh **tạo lại một lần**. Chỉ được thử thêm một lần nữa nếu lần đầu hỏng rõ: sai đề, hai vật, cắt mất thân.
- Tự chấm theo thang 10 điểm, ghi điểm và mức vào README.
- Từ 7 điểm là nhận. Lỗi nền, khung, lề không phải lý do tạo lại.

## Việc

1. **Không ghi đè:** đổi tên bản cũ thành `barracks-khien-dong.v1.png`, `barracks-giao-dai.v1.png`; prompt cũ thành `.v1.prompt.txt`.
2. **Prompt:**
   - ghép như phiếu 005b làm, theo `games/typing-defense/docs/art-requests/td/02-tripo-buildings-props-vs.md`, mục V34, V35 (STYLE, phần riêng, nền BG-G, 1024×1024);
   - đính kèm `games/typing-defense/art-src/buildings/barracks-v2.png` làm ảnh mẫu dáng;
   - thêm một dòng nói rõ: *the same two-storey watchtower barracks as the attached reference (same footprint, same height, the raised watch floor and the tall hipped roof), upgraded*;
   - giữ nét nhánh của phiếu 005b và của bản `.v1`:
     - **Khiên Đồng:** chân tường đá vôi; rào ốp khiên gỗ viền đồng; khiên đồng tròn trên mỗi cánh cổng; mái ngói đất nung;
     - **Giáo Dài:** rào cọc dài và cao hơn; giá giáo bó chặt thành một khối cạnh cổng; sàn tập ván nâng; không mũi giáo rời, không dây mảnh.
3. **Kiểm bằng mắt:** đặt ảnh mới cạnh `barracks-v2.png` cùng bề ngang chân. Nhánh phải cao gần bằng tháp và đọc ngay là Trại Lính đã nâng cấp. Ghép một ảnh xem nhanh `_review/015c-branches.jpg` (ImageMagick `/opt/homebrew/bin/magick`, font `/System/Library/Fonts/Supplemental/Arial.ttf`): v2 | bản mới | bản .v1.
4. **README-015c.md:** bảng ảnh, số lượt sinh, điểm, mức, thiếu gì.

**Xong khi:** hai ảnh mới có điểm từ 7, hoặc README ghi bản tốt hơn kèm điểm. Claude duyệt trước khi gửi Tripo.
