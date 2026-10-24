# Tu Tiên Thủ Ải (tên tạm)

Thư mục này đánh giá một game mới cho portal: **giữ ải chống thú triều trong thế giới tu tiên**, kỹ năng phát ra khi gõ (sau này nói) đúng từ tiếng Anh, chơi một mình hoặc theo đội 2–3 người (Thất Tinh 7 ghế là mở rộng, bot bù ghế). Tham chiếu nguyên tắc từ Quỷ Cốc Bát Hoang (Tale of Immortal), không chép tên, UI, hình hay cốt truyện.

**Trạng thái (25/10/2026): M0 xong phần viết, sắp dựng M0a.** Anh đã chọn làm (24–25/10) và chọn hướng hình **3D trước, có đo**. Đã có canon và kế hoạch M0a, đã qua một vòng phản biện ([`analysis/09-phan-bien-canon.md`](analysis/09-phan-bien-canon.md)) và đã sửa theo đó (canon D32–D46); chưa có mã. Mọi con số là số thử.

- **Repo:** `sinhvienaiti/immortality-cultivation`, submodule `games/immortality-cultivation` (mới có `README.md`). `gameId` `immortality-cultivation`, cổng dev 3008, host `tutien.typing-game.local`.
- **Tài liệu thiết kế** vẫn ở thư mục này (`docs/games/tu-tien/`), như `dragon-lane/` của Rồng Giữ Ải; chuyển vào repo game ở M1.

## Đọc theo thứ tự

1. [`00-canon.md`](00-canon.md): **nguồn chân lý duy nhất**: định danh, từ điển, sổ quyết định, luật, công thức, bảng số, bảng phím, cổng bot, ngân sách hiệu năng và bench HN0. Thắng mọi tệp khác.
2. [`M0A_PLAN.md`](M0A_PLAN.md): kế hoạch xây M0a (hộp xám) và bản thử Tĩnh Tu: khung repo, nối repo cha, làn có đường dẫn sở hữu riêng, thứ tự, nghiệm thu, cổng, cách đo GPU.
3. [`DANH_GIA_2026-10-24.md`](DANH_GIA_2026-10-24.md): kết luận, đánh giá Codex V2.2, vòng chơi, bảng hệ thống, solo và đội, lộ trình mốc, rủi ro, quyết định của anh (mục 8, đã trả lời 24–25/10). Lý do của canon; chỗ nào khác canon thì canon thắng.
4. Các tệp phân tích (đầu vào, có mâu thuẫn với nhau; đã giải ở Phụ lục A của tệp đánh giá và trong canon; `09` là phản biện canon, đã áp):

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
| [`analysis/09-phan-bien-canon.md`](analysis/09-phan-bien-canon.md) | Phản biện `00-canon.md` và `M0A_PLAN.md` (25/10); mọi mục đã áp vào hai tệp đó |

## Nguồn

- **Đề xuất Codex V2.2**: bản chụp đã commit ở [`source/CODEX_V2_2_2026-10-24.md`](source/CODEX_V2_2_2026-10-24.md). Đây là bản các tệp đánh giá đã đọc. Bản làm việc vẫn nằm ở gốc repo (`TU_TIEN_TYPING_SYSTEMS_AND_5_COMBAT_OPTIONS_V2_2026-10-24.md`, không vào Git) và có thể đã đổi sau ngày 24/10.
- **Bản quay QCBH của chủ dự án** (4:20, tu luyện và chiến đấu) ở gốc repo: `QCBH __ Diệt Không Vô Ảnh Kiếm #2_ Kết tinh chi lộ - 鬼谷八荒 Tale of Immortal - YouTube - Google Chrome 2026-10-24 17-02-08.mp4`. Tệp này không vào Git (`.gitignore` chặn `*.mp4`).
- **Khung hình trích từ video** (mỗi 4 s, cùng các khung dày cho mini-game tu luyện và trận boss) chỉ nằm trong thư mục tạm của phiên làm việc, **không commit**. Các tệp phân tích trích khung theo tên `t<giây>`, `med_NN`, `boss_NN`.
- Tài liệu dự án dùng làm nền: [`docs/games/SPLIT_PLAN.md`](../SPLIT_PLAN.md), [`docs/games/BALANCE.md`](../BALANCE.md), [`docs/games/AUDIO_PIPELINE.md`](../AUDIO_PIPELINE.md), [`tools/audio-lab/DECISIONS.md`](../../../tools/audio-lab/DECISIONS.md) (Q1, Q6), [`docs/games/dragon-lane/`](../dragon-lane/DESIGN.md) (Rồng Giữ Ải).

## Ký hiệu nguồn trong các tệp

[video] bản quay của chủ dự án · [Codex §x] tài liệu V2.2 · [web: url] trang đã đọc · [trí nhớ] chưa xác minh · [repo: đường dẫn] mã hoặc tài liệu trong dự án.
