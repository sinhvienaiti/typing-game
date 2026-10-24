# Tu Tiên Thủ Ải (tên tạm)

Thư mục này đánh giá một game mới cho portal: **giữ ải chống thú triều trong thế giới tu tiên**, kỹ năng phát ra khi gõ (sau này nói) đúng từ tiếng Anh, chơi một mình hoặc theo đội 2–3 người (Thất Tinh 7 ghế là mở rộng, bot bù ghế). Tham chiếu nguyên tắc từ Quỷ Cốc Bát Hoang (Tale of Immortal), không chép tên, UI, hình hay cốt truyện.

**Trạng thái: đánh giá và đề xuất, chưa triển khai.** Chưa có mã, chưa có repo `games/tu-tien`. Mọi con số là số thử.

## Đọc theo thứ tự

1. [`DANH_GIA_2026-10-24.md`](DANH_GIA_2026-10-24.md): kết luận, đánh giá Codex V2.2, vòng chơi, bảng hệ thống, solo và đội, lộ trình mốc, rủi ro, **quyết định cần anh**. Chỗ nào khác các tệp phân tích thì tệp này thắng.
2. `00-canon.md` (chưa có): nguồn chân lý duy nhất (từ điển, bảng số, mốc). Viết ở mốc M0 sau khi anh trả lời mục 8 của tệp đánh giá.
3. Các tệp phân tích (đầu vào, có mâu thuẫn với nhau; đã giải ở Phụ lục A của tệp đánh giá):

| Tệp | Mảng |
|---|---|
| [`analysis/01-tu-luyen-canh-gioi.md`](analysis/01-tu-luyen-canh-gioi.md) | Tu luyện, cảnh giới, đột phá, mini-game tĩnh tọa, tiến trình |
| [`analysis/02-thuoc-tinh-he-linh-can.md`](analysis/02-thuoc-tinh-he-linh-can.md) | Chỉ số, ngũ hành, khắc chế, chí mạng, trần chỉ số |
| [`analysis/03-ky-nang-chien-dau.md`](analysis/03-ky-nang-chien-dau.md) | Kỹ năng, combat, trường phái, boss phá thế |
| [`analysis/04-vat-pham-kinh-te-shop.md`](analysis/04-vat-pham-kinh-te-shop.md) | Tiền tệ, đồ rơi, đan phù, pháp bảo, cửa hàng |
| [`analysis/05-che-do-chong-thu-trieu.md`](analysis/05-che-do-chong-thu-trieu.md) | Chế độ lõi: ải, trận pháp, đợt, thú, Thú Vương |
| [`analysis/06-solo-to-doi-online.md`](analysis/06-solo-to-doi-online.md) | Solo, đội, bot, online trên Cloudflare Free |
| [`analysis/07-hoc-tieng-anh-my-thuat-am-thanh-san-xuat.md`](analysis/07-hoc-tieng-anh-my-thuat-am-thanh-san-xuat.md) | Học tiếng Anh, mỹ thuật, âm thanh, phạm vi sản xuất |
| [`analysis/08-phan-bien.md`](analysis/08-phan-bien.md) | Phản biện tổng hợp 01–07 |

## Nguồn

- **Đề xuất Codex V2.2**: bản chụp đã commit ở [`source/CODEX_V2_2_2026-10-24.md`](source/CODEX_V2_2_2026-10-24.md). Đây là bản các tệp đánh giá đã đọc. Bản làm việc vẫn nằm ở gốc repo (`TU_TIEN_TYPING_SYSTEMS_AND_5_COMBAT_OPTIONS_V2_2026-10-24.md`, không vào Git) và có thể đã đổi sau ngày 24/10.
- **Bản quay QCBH của chủ dự án** (4:20, tu luyện và chiến đấu) ở gốc repo: `QCBH __ Diệt Không Vô Ảnh Kiếm #2_ Kết tinh chi lộ - 鬼谷八荒 Tale of Immortal - YouTube - Google Chrome 2026-10-24 17-02-08.mp4`. Tệp này không vào Git (`.gitignore` chặn `*.mp4`).
- **Khung hình trích từ video** (mỗi 4 s, cùng các khung dày cho mini-game tu luyện và trận boss) chỉ nằm trong thư mục tạm của phiên làm việc, **không commit**. Các tệp phân tích trích khung theo tên `t<giây>`, `med_NN`, `boss_NN`.
- Tài liệu dự án dùng làm nền: [`docs/games/SPLIT_PLAN.md`](../SPLIT_PLAN.md), [`docs/games/BALANCE.md`](../BALANCE.md), [`docs/games/AUDIO_PIPELINE.md`](../AUDIO_PIPELINE.md), [`tools/audio-lab/DECISIONS.md`](../../../tools/audio-lab/DECISIONS.md) (Q1, Q6), [`docs/games/dragon-lane/`](../dragon-lane/DESIGN.md) (Rồng Giữ Ải).

## Ký hiệu nguồn trong các tệp

[video] bản quay của chủ dự án · [Codex §x] tài liệu V2.2 · [web: url] trang đã đọc · [trí nhớ] chưa xác minh · [repo: đường dẫn] mã hoặc tài liệu trong dự án.
