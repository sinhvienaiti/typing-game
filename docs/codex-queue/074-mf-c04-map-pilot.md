# Phiếu 074 · Bản thử bản đồ Rồng L2-cau · MF-C04: Đo ảnh (`cli look`)

Kế hoạch: [`docs/tools/map-factory/MAP_PLAN.md`](../tools/map-factory/MAP_PLAN.md). Danh sách phiếu gốc: [`docs/tools/map-factory/TICKETS.md`](../tools/map-factory/TICKETS.md), mục MF-C04. Phiếu ghi "MF-xx" là mã trong kế hoạch; số hàng đợi tương ứng nằm trong `docs/CODEX_QUEUE.md`.

**Báo cáo:** `docs/codex-queue/074-report.md` **trong worktree** `/Users/toandx/htdocs/typing-game-wt/map-codex`.

## Luật chung: 1.2 Mọi phiếu mã Codex ở repo cha

- **Thư mục làm việc:** worktree `/Users/toandx/htdocs/typing-game-wt/map-codex`, nhánh `map-factory` (MAP_FACTORY §9.4).
- **Chỉ được ghi:** đúng các đường dẫn phiếu liệt kê, cộng file báo cáo.
- **Cấm:**
  - lệnh git có ghi (`add`, `commit`, `checkout`, `stash`, `reset`, `clean`…); `git status`, `git diff`, `git archive` được phép;
  - mạng, trình duyệt, dev server, server bất kỳ;
  - ghi dưới `games/**` (chỉ đọc; bộ đọc lấy nội dung game bằng `git archive` ở commit ghim);
  - cài gói npm hay pip; chỉ Node 24 có sẵn và `node_modules` của `shared/game-kit` (TypeScript 6.0.3, vitest);
  - đọc hay ghi Tu Tiên;
  - `Math.sin/cos/tan/atan2/pow/hypot/exp/log/cbrt/random`, `Date`, `performance`, `**` trong `shared/game-kit/map/` (ngoài `*.test.ts`); số lẻ ở đầu ra lõi (đơn vị cm, ‰, độ nguyên).
- **Kiểm chung, bắt buộc:**
  - **KC1 cây Git:** lưu `git status --short --untracked-files=all` lúc đầu; lúc cuối chỉ được **thêm hoặc sửa** đường dẫn cho phép; không dòng ` M`, ` D` mới ngoài phạm vi.
  - **KC2 lint tất định:** test lint của 027 đạt trên mọi file mới trong `map/`.
  - **KC3 test:** `pnpm --dir shared/game-kit exec vitest run map` và `node --test tools/map-factory/test/*.test.mjs` đạt; `tsc -p shared/game-kit/map/tsconfig.json` đạt.
  - **KC4 tất định:** chạy hai lần (hai tiến trình Node) cho cùng từng byte; in băm.
- **Quá một giờ:** dừng ở phần đã xong, ghi phần còn lại vào báo cáo.
- **Báo cáo:** tiếng Việt; file tạo hay sửa; kết quả từng kiểm kèm số in ra; thời gian chạy.

## MF-C04 · [codex-code] Đo ảnh (`cli look`)

**Cần trước:** MF-C03.

**Chỉ được ghi:** `tools/map-factory/lint/look.mjs`, `tools/map-factory/cli.mjs` (thêm lệnh `look`), `tools/map-factory/test/look.test.mjs`, `tools/map-factory/test/fixtures/look/*.json`.

**Việc:** trên ảnh 384×216 (từ PNG qua MF-C03 hoặc từ `.rgb`), tính đúng như script của Claude (Claude chép nguyên văn `stats.mjs`, `stats2.mjs`, `stats3.mjs` vào phiếu khi xếp):
- L = 0,2126r + 0,7152g + 0,0722b; HSV theo hàm `hsv` của script;
- `meanLuma`;
- `litGrass`: hue 65–160°, s > 0,3, L > 0,45: tỉ lệ, trung vị L, trung vị hue;
- `brightMeadow`: hue 65–160°, s > 0,3, L > 0,5;
- `veryDark`: V < 0,22;
- `darkTeal`: hue 170–235°, s > 0,2, L < 0,3;
- `warmAccent`: (hue < 22° hoặc > 340°), s > 0,45, V > 0,3, theo thứ tự lớp của `stats.mjs`;
- `violet`: hue 240–300°, s > 0,25, theo thứ tự lớp của `stats.mjs`;
- `soil`: hue 18–55°, 0,18 < s < 0,65, V > 0,45;
- `fineTexture`: trung bình |L − mờ hộp bán kính 2|;
- `largeContrast`: độ lệch chuẩn của mờ hộp bán kính 12;
- lưới luma 4 × 3.
- Dải ngưỡng đọc từ một file JSON (`captureBands`); in bảng ĐẠT/TRƯỢT từng dòng và JSON; thoát 1 nếu có dòng trượt.

**Kiểm (bắt buộc):** KC1, KC3, KC4, và:
1. Ảnh tổng hợp biết trước đáp án (màu đơn, bàn cờ, dải chuyển): mọi số khớp ±1e-6.
2. Không DOM, không gói ngoài.
3. Dải mẫu cho pine-river (từ kế hoạch §2.9 Q5) nằm trong fixture; ảnh tổng hợp "đạt hết" và "trượt 3 dòng" cho đúng kết quả.

**Xong khi:** ba kiểm đạt. Claude chạy lại trên file thô ảnh mẫu, spike, M0b (đã chép vào `tools/map-factory/.cache/look-anchors/`, bị bỏ qua bởi Git): ảnh mẫu 0,522 và 41,7 %, spike 0,422 và 20,6 % (±0,005).
