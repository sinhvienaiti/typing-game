# Rồng Giữ Ải — 06. Các hệ còn thiếu: lưu, focus, cài đặt, màn ngoài trận, hướng dẫn, đo lường (23/10/2026)

> Tài liệu này bổ sung các hệ mà bản phản biện đầy đủ chỉ ra là còn thiếu. Số chuẩn và bảng phím: `00-canon.md`. Luật trận: 01–04. Hình: 05.
> Không có số cân bằng ở đây. Mọi mặc định đều đổi được trong cài đặt hoặc dữ liệu.

## 0. Tóm tắt

| # | Hệ | Một dòng |
|---|---|---|
| 1 | Lưu | 8 lớp JSON có phiên bản và hàm chuyển; hai khe A/B có mã kiểm; ảnh chụp đầu mỗi lần nghỉ để chơi tiếp; xuất, nhập; tối đa 4 hồ sơ |
| 2 | Focus, tạm dừng | Mất focus giữa đợt thì tự dừng, che chữ; "bấm để tiếp" lấy lại focus; sim đứng yên khi dừng |
| 3 | Cài đặt | Một màn, 30 khóa, có mặc định, nơi lưu, quan hệ với portal và với sự kiện học |
| 4 | Màn ngoài trận | 15 màn, sơ đồ đi, bố cục vỏ gỗ khắc, đi hết bằng bàn phím |
| 5 | Hướng dẫn người mới | Kịch bản phiên đầu, lời Bạch Long ải 1–6, gợi ý theo ngữ cảnh, Sổ Quái, Sổ Món, lịch giới thiệu tiền và màn |
| 6 | Thoại, phụ đề | Bạch Long và người kể có giọng đọc dựng sẵn; boss chỉ gầm và phụ đề; phát âm từ qua `shared/voice` |
| 7 | Đo lường cục bộ | Người chơi tự bật; tắt và khóa ở hồ sơ trẻ em; xuất file; không gửi ra ngoài |
| 8 | Thành tựu | 40 thành tựu, 14 gắn với học |
| 9 | Bản địa hóa | Bản đầu chỉ tiếng Việt; mọi chuỗi trong `strings.vi.json` |
| 10 | Chống nản | Tua nhanh × 2, chơi lại ải, bỏ qua ải cho hồ sơ trẻ em |
| 11 | Admin, ôn tập, lịch sử | Admin để sau; adapter Smart Review ở lát C4–6; lịch sử học của TD giữ nguyên |
| 12 | Giữ chỗ cho di động | Lớp lệnh tách khỏi chuột; mọi lệnh có nút; không dựa vào hover |

## 1. Lưu

### 1.1 Nơi lưu và lớp

- Lưu bằng `safe-storage` của kit (mọi đọc, ghi trong try/catch). Khóa có tiền tố `dh:v1:`. Origin là `dragon.typing-game.local`, nên xóa dữ liệu trang của host này là mất hết: có nhắc xuất bản sao (mục 1.5).
- Độ thuộc từ **không** lưu ở đây. Nó nằm ở hồ sơ học của portal. Game chỉ giữ bản sao đọc và hàng chờ sự kiện chưa gửi.

| Lớp | Khóa | Nội dung | Khi ghi | Cỡ |
|---|---|---|---|---|
| Máy | `dh:v1:device` | Bậc đồ họa, tỉ lệ render, kết quả dò máy | Khi đổi | < 1 KB |
| Danh sách hồ sơ | `dh:v1:meta` | Hồ sơ, hồ sơ đang dùng, phiên bản lược đồ | Khi đổi | < 2 KB |
| Hồ sơ | `dh:v1:p:<id>:profile` | Tên, màu áo Rồng, cờ trẻ em, mức khó mặc định, Cấp Từ (bản sao), ngày tạo | Khi đổi | < 1 KB |
| Hành trình | `…:journey` | Mỗi ải: sao, Dấu Thách, Huy hiệu Học, Vương Miện, kỷ lục, số lần thua; ải mới nhất | Kết ải | ~12 KB (520 ải nén theo bit) |
| Rồng | `…:dragons` | XP, Bậc Rồng, Cây Long Mạch, Long Ấn đã mở | Kết ải | < 2 KB |
| Làng | `…:village` | Vảy, Tri Thức, bậc Thư Viện, cấp món, trang bị đã có và cấp, trang bị đang đeo, Bộ Mang Theo đã lưu | Kết ải, khi mua | < 4 KB |
| Ngày | `…:daily` | Ải Ngày, việc ngày, chuỗi ngày, thưởng dồn | Kết ải | < 1 KB |
| Cài đặt | `…:settings` | Mục 3 | Khi đổi | < 2 KB |
| Ải dở | `…:run` | Ảnh chụp đầu lần nghỉ gần nhất (mục 1.3) | Đầu mỗi lần nghỉ | ≤ 30 KB |
| Học cục bộ | `…:learn-cache` | Bản sao độ thuộc và mẫu nhớ của bộ từ đang dùng; hàng chờ sự kiện chưa gửi | Mỗi 5 s trong trận | ≤ 60 KB |
| Đo lường | `…:telemetry` | Chỉ khi bật (mục 7) | Kết ải | ≤ 500 KB |
| Thành tựu | `…:achievements` | Mục 8 | Khi đạt | < 2 KB |

### 1.2 Lược đồ, phiên bản, hàm chuyển

```jsonc
// mỗi lớp
{ "v": 3, "savedAt": "2026-10-23T09:00:00Z", "crc": "8f3a…", "data": { … } }
```

- `v` là phiên bản của **lớp đó**. Mỗi lần đổi lược đồ: thêm `src/app/save/migrations/<lớp>/<từ>-<tới>.ts`, chạy nối tiếp từ bản cũ nhất.
- Mỗi hàm chuyển có test với file mẫu của mọi bản cũ (`tests/save-fixtures/`). Trường cũ chỉ bị xóa sau 2 bản.
- Đọc một lớp có `v` lớn hơn bản game hiểu (người chơi quay về bản cũ): không ghi đè, báo "bản lưu mới hơn game", chỉ đọc.

### 1.3 Ảnh chụp để chơi tiếp và "Thử lại từ đợt trước"

- Sim tất định và **đợt chỉ hết khi mọi quái đã chết** (01 §1.2). Vì vậy đầu mỗi lần nghỉ là một trạng thái sạch: không quái, không đạn. Ảnh chụp chỉ cần phần nhỏ:

| Trường | Ví dụ |
|---|---|
| Ải | `id`, mã băm dữ liệu ải, seed, k_E, mức khó, số đợt kế |
| Phe ta | Món đã đặt (ô, cấp, nhánh, chế độ Kích, máu nhà), Vàng, đồ tiêu hao |
| Rồng | Máu hai Rồng, Cấp Rồng, Long Ấn đã chọn, lượt chọn còn chờ, Long Nộ, hồi kỹ năng |
| Gõ, học | Chuỗi, danh sách id từ của bộ từ ải, từ đã gửi sự kiện có chấm (00 D14), trạng thái RNG |
| Khác | Số lần đã dùng "Thử lại từ đợt trước", Lông Phượng đã dùng chưa |

- **Chơi tiếp:** đóng tab hay trình duyệt lỗi giữa ải thì lần mở sau màn Tiêu đề hỏi "Chơi tiếp ải 47 từ đầu lần nghỉ trước đợt 4?". Có hoặc Bỏ. Bỏ thì tính như bỏ ải (giữ 30 % tiền, 01 §5).
- **Thử lại từ đợt trước** (01 §5) dùng đúng ảnh chụp này.
- Mã băm dữ liệu ải khác (game đã cập nhật ải đó) thì ảnh chụp hết hiệu lực; báo và mời chơi lại từ đầu.
- Ảnh chụp bị xóa khi ải kết thúc.

### 1.4 Khi bản lưu hỏng

- Mỗi lớp ghi luân phiên hai khe `…:A` và `…:B`, kèm `crc`. Khi đọc: lấy khe mới nhất có `crc` đúng.
- Cả hai khe hỏng: chỉ lớp đó về mặc định; các lớp khác giữ. Báo rõ lớp nào mất và gợi ý nhập bản sao gần nhất.
- Không bao giờ xóa cả hồ sơ vì một lớp hỏng.

### 1.5 Xuất, nhập, nhiều hồ sơ, đồng bộ

- **Xuất:** một file `dragon-hold-<hồ sơ>-<ngày>.json` gồm mọi lớp của hồ sơ (đo lường chỉ khi chọn). Cùng kiểu với `shared/learning/profile-backup.mjs`. Hồ sơ học của portal xuất ở portal.
- **Nhập:** kiểm phiên bản, chạy hàm chuyển, hỏi ghi đè hay tạo hồ sơ mới.
- **Nhắc xuất:** mỗi 20 ải hoặc 7 ngày, một dòng nhỏ ở màn Kết ải. Tắt được.
- **Nhiều hồ sơ:** tối đa 4. Tạo hồ sơ hỏi tên và một công tắc **"Hồ sơ trẻ em"**. Hồ sơ trẻ em: mức Dễ, nghĩa luôn hiện, tự dùng kỹ năng hỗ trợ, nhắc nghỉ 20 phút, lọc từ `mature` (01 §6.1), đo lường tắt và khóa, cho bỏ qua ải sau 3 lần thua (mục 10). Đổi cờ trẻ em cần giải một phép tính nhỏ ở cài đặt.
- Hồ sơ học của portal là một hồ sơ cho mỗi trình duyệt. Các hồ sơ game dùng chung hồ sơ học đó (ghi rõ trên màn chọn hồ sơ). Muốn tách việc học thì dùng hồ sơ trình duyệt riêng (Câu hỏi 2).
- **Đồng bộ đám mây:** bản đầu không có. Lược đồ giữ dạng JSON từng lớp để sau này nối với dịch vụ `/api/account` (cổng 3016) theo kiểu người chơi tự bật.

## 2. Focus và tạm dừng

Game chạy trong iframe của portal. Portal hiện không gọi `frame.focus()` khi nạp game, nên phím đầu tiên rơi vào trang portal. Space chỉ tự dừng khi mất focus nếu không ở chế độ gõ.

| # | Luật |
|---|---|
| 1 | Khi nạp, game gọi `window.focus()` và gửi tin `typing-game:request-focus` lên portal. Portal (việc ở repo cha, 01 §6.8) focus iframe khi nạp và khi nhận tin này |
| 2 | Chưa có focus thì Tiêu đề và Lều Chuẩn Bị hiện lớp mờ "Bấm hoặc gõ phím bất kỳ để bắt đầu" |
| 3 | `blur` hoặc `visibilitychange` (tab ẩn) **giữa đợt hoặc lúc nghỉ**: tự dừng, che chữ, hiện "Bấm hoặc gõ phím bất kỳ để tiếp" |
| 4 | Tiếp sau khi dừng giữa đợt: đếm 3-2-1 rồi chạy. Tiếp lúc nghỉ: không đếm |
| 5 | Khi dừng, **sim đứng yên hoàn toàn**: đồng hồ đợt, đồng hồ nghỉ, cửa sổ Cụm Ấn, hồi kỹ năng, ngòi Pháo Hiệu. Âm tạm ngưng, nhạc qua lọc thấp |
| 6 | Trong trận không có thẻ `input`. Mọi phím đi qua một router ở `window`, pha capture |
| 7 | Nút DOM (HUD, dải món, vòng menu, Thẻ Ôn, cài đặt) có `tabindex=-1` và chặn `mousedown` mặc định, nên bấm chuột không lấy focus khỏi router; Enter, Space không bấm lại nút cũ |
| 8 | Đợt không tự bắt đầu khi thẻ học (Thẻ Ôn, Long Ấn, thẻ ra mắt dạy) đang mở |
| 9 | Menu dừng (Esc): Tiếp tục · Cài đặt · Sổ Quái · Chơi lại ải · Bỏ ải (giữ 30 % tiền) |

- Kiểm bằng kịch bản `dh-focus` (05 §10): bấm HUD, bấm dải món, alt-tab, bấm thanh nav của portal rồi quay lại, ẩn tab 10 s.

## 3. Cài đặt

Một màn Cài đặt, 6 thẻ: Âm · Chữ và học · Trận · Hình · Điều khiển · Hồ sơ. Mỗi thẻ có nút "Đặt lại mặc định". Cài đặt lưu theo hồ sơ (`…:settings`), trừ cài đặt máy (`dh:v1:device`).

| Thẻ | Khóa | Mặc định | Phạm vi | Lấy từ portal | Ảnh hưởng sự kiện học |
|---|---|---|---|---|---|
| Âm | Âm lượng tổng, nhạc, hiệu ứng, thoại, phát âm | 80 / 60 / 80 / 80 / 100 | 0–100 | Nhạc: nghe tin `typing-game:shared-music`; portal đang phát nhạc thì nhạc game tự hạ về 0 | Không |
| Âm | Giọng phát âm, tốc độ đọc | Theo `shared/voice` | Theo portal | Có | Không |
| Âm | Phát âm tự động | Từ mới và từ yếu | Tắt · Chỉ từ mới · Từ mới và từ yếu · Mọi từ hạ (01 §6.4) | Không | Không (`replayUsed` chỉ khi bấm Tab) |
| Âm | Phụ đề thoại · phụ đề âm | Bật · Tắt | Bật, Tắt | Không | Không |
| Chữ và học | Luôn hiện IPA · luôn hiện nghĩa | Tắt · Tắt (trẻ em, Dễ: nghĩa Bật) | Bật, Tắt | Không | **Có**: `hintUsed` (01 §6.3) |
| Chữ và học | Cỡ thẻ chữ · cỡ khung học | 100 % · 100 % | 80–150 % | Không | Không |
| Chữ và học | Chế độ khay | Tắt | Bật, Tắt (05 §4.6) | Không | Không |
| Chữ và học | Thẻ Ôn lúc nghỉ | Bật | Bật, Tắt | Không | Không |
| Trận | Mức khó mặc định | Thường (trẻ em: Dễ) | Dễ · Thường · Khó (00 §4.10) | Không | Không |
| Trận | Chữ Chiêu | Bật | Bật, Tắt (Tắt: chỉ Alt + số) | Không | Không |
| Trận | Tự dùng kỹ năng hỗ trợ | Tắt (Dễ, trẻ em: Bật) | Bật, Tắt (01 §2.4) | Không | Không |
| Trận | Từ Kích mặc định | Tự (C1–3) · Chữ (C4+) | Tự, Chữ (03 §7.1) | Không | Không |
| Trận | Nhắc nghỉ | 30 phút (trẻ em 20) | Tắt, 20, 30, 45, 60 | Không | Không |
| Hình | Bậc đồ họa | Tự dò (đo 3 s ở màn nạp lần đầu) | Low · Medium · High · Ultra (05 §8) | Không | Không |
| Hình | Tỉ lệ render | 100 % | 50–100 % | Không | Không |
| Hình | Rung màn · cường độ lóe · tách màu · mật độ hạt | 70 % · 100 % · Bật · 100 % | 0–100 % | Không | Không |
| Hình | Giảm chuyển động | Theo `prefers-reduced-motion` của máy | Bật, Tắt | Không | Không |
| Hình | Số sát thương | Bật | Bật · Tắt · Chỉ số lớn | Không | Không |
| Hình | Hoa văn mù màu | Tắt | Bật, Tắt | Không | Không |
| Điều khiển | Đổi phím | Bảng 00 §6 | Mọi phím lệnh không phải chữ cái; không cho gán a–z | Không | Không |
| Điều khiển | Camera: độ nhạy · đảo dọc · đảo ngang | 1,0 · Tắt · Tắt | 0,5–2,0 | Không | Không |
| Hồ sơ | Đo lường cục bộ | Tắt (trẻ em: khóa Tắt) | Bật, Tắt (mục 7) | Không | Không |
| Hồ sơ | Nhắc xuất bản sao | Bật | Bật, Tắt | Không | Không |
| Hồ sơ | Ngôn ngữ giao diện | Tiếng Việt | Bản đầu chỉ một (mục 9) | Không | Không |

## 4. Màn ngoài trận

### 4.1 Danh sách

Vỏ chung: gỗ khắc, vỏ cây sẫm, viền rêu (05 §1.1); tiêu đề Cormorant Garamond 700, chữ thân Be Vietnam Pro. Mỗi màn có tranh nền từ Codex và một Rồng nhỏ (3D nhẹ hoặc tranh) ở góc.

| # | Màn | Mở từ | Nội dung chính | Bàn phím |
|---|---|---|---|---|
| 1 | Màn nạp | Mở game, đổi kit | Tranh vùng đất, một mẹo, thanh tiến; lần đầu dò bậc đồ họa | — |
| 2 | Tiêu đề | Sau nạp | Hỏa Long lượn trên Bệ Rồng, Bạch Long đứng. Tiếp tục (ải mới nhất hoặc ải dở) · Hành Trình · Làng Rồng · Ôn Ngày · Sổ · Cài đặt · Đổi hồ sơ | ↑↓ chọn, Enter |
| 3 | Chọn hồ sơ | Lần đầu, Tiêu đề | 4 ô hồ sơ; tạo (tên, cờ trẻ em), xóa (gõ tên để xác nhận), xuất, nhập | Mũi tên, Enter, Esc |
| 4 | Bài xếp lớp | Lần đầu, tùy chọn | 3 lựa chọn: Mới bắt đầu (cấp 1) · Biết ít · Biết khá (bài 4 phút, 04 §7.4) | 1 / 2 / 3, rồi gõ |
| 5 | Hành Trình | Tiêu đề | Tranh Đại Ngàn Sương; 26 chương, mỗi chương một con đường 20 nút theo loại ải; sao, dấu, khóa; thẻ "Chơi thêm" (Ải Ngày, Rừng Vô Tận, Tháp Rồng, Ác Mộng) | Mũi tên đi nút, Tab đổi chương, Enter mở Thẻ ải |
| 6 | Thẻ ải, Lều Chuẩn Bị | Nút ải | Bản đồ khung, đợt, luật, Dấu Thách, số từ mới, Học trước, Bộ Mang Theo, mức khó, Lời Thề và Vương Miện nếu đã mở (05 §4.5) | 00 §6 |
| 7 | Menu dừng | Esc trong trận | Mục 2, luật 9 | ↑↓, Enter, Esc |
| 8 | Kết ải (thắng) | Hết ải | Sao bay vào; Vảy, Tri Thức, XP; Dấu Thách; Huy hiệu Học; thẻ **Sổ Từ Ải**; nút Ôn trận (60–90 s); Tiếp · Chơi lại · Về bản đồ | Enter Tiếp, Tab đổi thẻ |
| 9 | Màn thua | Hỏa Long hết máu | Biểu đồ máu Hỏa Long theo thời gian, đợt thua, quái gây nhiều sát thương nhất; 1–2 gợi ý cụ thể (mục 5.3); Thử lại từ đợt trước (nếu còn) · Chơi lại · Hạ mức khó (sau 2 lần) · Về Lều Chuẩn Bị | Mũi tên, Enter |
| 10 | Làng Rồng | Tiêu đề | Tranh làng với 3 nơi: Hang Rồng (Bậc Rồng, Cây Long Mạch, Long Ấn đã mở) · Thư Viện Rồng (12 bậc, Sổ Từ, Thi lên cấp) · Xưởng Rồng (cấp món, trang bị cố định, so sánh trước và sau) | ← → chọn nơi, Enter |
| 11 | Sổ | Tiêu đề, menu dừng | Sổ Quái · Sổ Món · Sổ Từ · Sổ Trang Bị · Thành tựu (mục 5.4, 8) | Tab đổi sổ, mũi tên, Enter |
| 12 | Cài đặt, Đổi phím | Tiêu đề, menu dừng | Mục 3 | Tab đổi thẻ, mũi tên, Enter |
| 13 | Ôn Ngày | Tiêu đề | 3 phút ôn từ đến hạn của mọi game portal (04 §10) | Gõ, Enter |
| 14 | Tranh truyện chương | Đầu chương | 3–6 tấm, phụ đề, giọng kể, Esc bỏ qua (05 §6.7) | Enter tiếp, Esc bỏ |
| 15 | Hỏi chơi tiếp | Mở game khi có ải dở | Mục 1.3 | Enter Có, Esc Bỏ |

### 4.2 Sơ đồ đi

```text
Màn nạp → (Chọn hồ sơ lần đầu → Bài xếp lớp tùy chọn) → Tiêu đề
Tiêu đề ─┬─ Tiếp tục ───────────────┐
         ├─ Hành Trình → Thẻ ải ────┴→ Lều Chuẩn Bị → Trận ─┬→ Kết ải ─┬→ Tiếp → Lều Chuẩn Bị (ải sau)
         ├─ Làng Rồng (Hang · Thư Viện · Xưởng)              │          └→ Về bản đồ → Hành Trình
         ├─ Ôn Ngày                                          └→ Màn thua ─┬→ Thử lại từ đợt trước → Trận
         ├─ Sổ (Quái · Món · Từ · Trang Bị · Thành tựu)                    ├→ Chơi lại → Lều Chuẩn Bị
         ├─ Cài đặt                                                        └→ Về Lều Chuẩn Bị
         └─ Đổi hồ sơ
Trận ─ Esc → Menu dừng (Tiếp · Cài đặt · Sổ Quái · Chơi lại · Bỏ ải)
```

- Esc luôn lùi một bước. Không màn nào chỉ đi được bằng chuột.
- Kịch bản `dh-meta-screens`: mọi màn ở 1280 × 720 và 1920 × 1080; đi hết sơ đồ chỉ bằng bàn phím; mọi chuỗi tiếng Việt vừa khung; font tiêu đề đủ dấu.

## 5. Hướng dẫn người mới

### 5.1 Phiên đầu

1. Mở game: Chọn hồ sơ (tên, cờ trẻ em).
2. Hỏi "Bạn đã biết nhiều từ tiếng Anh chưa?": Mới bắt đầu (Cấp Từ 1, bỏ bài xếp lớp) · Biết ít · Biết khá (bài xếp lớp 4 phút). Có thể bỏ qua.
3. Tranh truyện mở đầu C1 (3 tấm, 30 s, Esc bỏ qua).
4. Ải 1. Bạch Long là người dẫn tới hết ải 10 (00 D21).

### 5.2 Lời Bạch Long ở ải 1–6

Mỗi câu ≤ 12 từ, có phụ đề, có giọng đọc (mục 6). Bước sau chỉ hiện khi bước trước xong. Ải 1 dạy luật gõ; quái ải 1 chỉ đánh Rồng từ đợt 3.

| Ải | Lời dẫn (lần lượt) | Điều kiện qua bước | Gợi ý nếu kẹt 10 s |
|---|---|---|---|
| 1 | "Gõ chữ trên đầu quái. Hỏa Long sẽ phun lửa." → "Chữ sáng gạch chân là chữ để bắt đầu." → "Nhìn xuống dưới: nghĩa và cách đọc." | Gõ xong 1 từ; gõ xong 3 từ; khung học đã hiện | Chữ đầu của quái gần nhất nhấp nháy nhẹ |
| 1 | Khi gõ sai 2 phím: "Gõ sai thì bấm Backspace để xóa." · Khi đang khóa mà quái khác tới gần: "Muốn đổi quái? Gõ chữ đầu của nó, hoặc bấm Esc." | Dùng Backspace 1 lần; đổi khóa 1 lần | — |
| 2 | "Có vàng rồi. Đặt Gai Chông lên ô sáng." → (lúc nghỉ) "Quái đi qua gai sẽ chậm lại." | Đặt 1 bẫy (nút "Bỏ qua" sau 20 s) | Ô gợi ý sáng mạnh; dòng "bấm 1 rồi Enter" |
| 3 | "Ô kỹ năng sáng rồi. Gõ chữ trên ô, hoặc Alt + 1." | Dùng Phun Lửa 1 lần | Mũi tên chỉ vào ô kỹ năng |
| 4 | "Một từ cho cả đàn kiến. Gõ một lần, cháy cả đàn." | Hạ 1 cụm bầy bằng từ cụm | Từ cụm sáng hơn |
| 5 | "Quái cầm cờ làm cả toán chạy nhanh. Gõ từ viền đồng để tắt cờ." | Gõ 1 Ấn Phá | Ấn Phá nhấp viền |
| 6 | "Vệ Binh chặn quái trên đường. Đặt ở chỗ cắm cờ." | Đặt 1 Vệ Binh Rêu | Điểm giữ sáng |

- Từ ải 7, mỗi hệ mới (04 §6.1) có một **thẻ dạy** 1 câu khi hệ đó xuất hiện lần đầu, không dừng trận (trừ ải 1–6).

### 5.3 Gợi ý theo ngữ cảnh và mẹo khi thua

- Tối đa 1 gợi ý mỗi đợt, 1 dòng, góc trên. Mỗi gợi ý hiện tối đa 2 lần mỗi hồ sơ. Tắt được trong cài đặt (thẻ Trận).

| Khi | Gợi ý |
|---|---|
| Hỏa Long xuống dưới 50 % lần đầu | "Máu thấp: Alt + 7 để uống Bình Máu." |
| Bấm 3 phím không khớp chữ đầu nào trong 2 s | "Chỉ gõ chữ đầu đang sáng trên quái." |
| Quái bay lọt vào Bệ Rồng 3 lần trong một ải | "Quái bay không bị chặn. Thử Lưới Phóng." |
| Hai lần nghỉ liền không đặt món nào, còn ≥ 150 Vàng | "Vàng không mang ra khỏi ải. Đặt thêm bẫy." |
| Long Nộ đầy chưa dùng sau 20 s | "Long Nộ đầy: Alt + 5." |
| Tướng địch có hào quang đi qua nửa đường | "Gõ từ viền đồng để tắt hào quang." |

- **Màn thua** chọn 1–2 gợi ý từ dữ liệu trận: loài gây nhiều sát thương nhất → món khắc chế nó (03 §0.3); đường lọt nhiều nhất → "đặt lính ở đường X"; độ chuẩn < 85 % → "gõ chậm lại, chuẩn mạnh hơn nhanh".
- **Quay lại sau ≥ 14 ngày:** thẻ "Lần trước" (ải đang ở, hệ đã mở gần nhất, 3 phím chính) và mời chơi Ôn Ngày trước.

### 5.4 Sổ Quái, Sổ Món

- **Sổ Quái:** mỗi loài, tướng, boss mở khi gặp lần đầu. Trang có model xoay, tên, "làm gì", "khắc chế" (mã và món cụ thể từ 03 §0.3), chương gặp, mẹo gõ (ví dụ "đánh khi mai mở"). Thẻ ra mắt 3 s trong trận (02 §1.5) ghi vào sổ, nên người chơi đọc lại được lúc nghỉ.
- **Sổ Món:** mỗi món đã mở: số theo cấp, vùng, hồi, mã khắc chế nó giải được, chuỗi bẫy gợi ý (03 §7.4).

### 5.5 Lịch giới thiệu tiền và màn

| Thứ | Lần đầu thấy | Cách dạy |
|---|---|---|
| Vàng | Ải 2 | Lời Bạch Long, dải món sáng |
| Sao | Kết ải 1 | Sao bay vào, một dòng "Giữ máu Hỏa Long để có 3 sao" |
| Vảy Rồng, Xưởng Rồng | Kết ải 3 (ô Vuốt mở) | Mũi tên dẫn vào Làng Rồng, mua Vuốt Đá |
| XP, Bậc Rồng, Hang Rồng | Kết ải 5 | Thẻ "Bậc Rồng tăng" |
| Tri Thức, Thư Viện Rồng | Ải 9 (Ải Ôn) | Thẻ "Học thì có Tri Thức" |
| Cây Long Mạch | C2 ải 21 | Thẻ ở Hang Rồng |
| Long Ấn | C2 ải 24 | Bảng chọn lúc nghỉ, phím 1 / 2 / 3 |
| Vương Miện, Ải Ngày | C3 | Thẻ ở Hành Trình |
| Lời Thề | Ải 201 | Thẻ ở Lều Chuẩn Bị |

## 6. Thoại, giọng, phụ đề

| Ai nói | Giọng | Phụ đề | Số câu bản đầu |
|---|---|---|---|
| Bạch Long (dẫn, gợi ý, mốc Chuỗi, thắng thua) | Giọng đọc tiếng Việt dựng sẵn bằng công cụ AI có gói thương mại (TD 24.9), file OGG qua `pnpm media:push`. Không đọc lúc chạy | Luôn có | ~120 |
| Người kể (tranh truyện) | Như trên, giọng khác | Luôn có | ~60 (C1–C6) |
| Boss | Không nói thành lời; gầm, tiếng chữ ký (02 §4.5) | Câu thoại hiện bằng chữ khi ra mắt | 20 |
| Phát âm từ tiếng Anh | `shared/voice` lúc chạy, như Space (01 §6.4) | IPA ở khung học | — |

- Câu thoại nằm trong `src/content/dialogue.vi.json`, có khóa, điều kiện, độ ưu tiên. Thoại nhường phát âm từ (05 §7.2).
- Thiếu file giọng thì chỉ hiện phụ đề, không lỗi.

## 7. Đo lường cục bộ

- **Người chơi tự bật** (cài đặt, thẻ Hồ sơ). Tắt sẵn. Hồ sơ trẻ em: tắt và khóa.
- **Không gửi ra ngoài.** Chỉ lưu trong `…:telemetry` (vòng 50 ải gần nhất, ≤ 500 KB). Nút "Xuất đo lường" ra file JSON để chủ dự án và AI đọc khi chỉnh cân bằng. Nút "Xóa".
- Không có chữ tự do, không tên người.

| Nhóm | Ghi gì |
|---|---|
| Ải | id, seed, mã băm, mức khó, E, k_E, kết quả, sao, thời lượng từng đợt, đợt thua |
| Máu | Máu Hỏa Long mỗi 5 s; nguồn sát thương lên Rồng theo loài |
| Gõ | Số từ, độ chuẩn, phân bố Chớp → Ẩu, nghẽn chữ đầu theo nguồn (00 §5), mất khóa vì nguồn khác |
| Phe ta | Món mua, đặt, nâng, bán mỗi lần nghỉ; phần sát thương và khống chế theo nguồn |
| Kỹ năng | Lần dùng mỗi kỹ năng, Tối Thượng đã chọn |
| Hướng dẫn | Thời gian mỗi bước 5.2, gợi ý đã hiện |
| Bỏ dở | Màn và giây lúc người chơi thoát |

## 8. Thành tựu (40, ghi cục bộ)

| Nhóm | Số | Ví dụ |
|---|---|---|
| Học | 14 | 10 từ mới đầu tiên · 100 / 500 / 1.000 / 3.000 từ đã nhớ (≥ 2 lần nhớ đúng) · chuỗi ôn 7 / 30 ngày · 50 Thẻ Ôn đúng · 20 Hỏi Nghĩa đúng · 20 Từ Nghe đúng · Huy hiệu Học 10 / 50 ải · lên Cấp Từ 10 |
| Gõ | 8 | Chuỗi 50 / 100 · 20 Chớp liên tiếp · một ải chuẩn 100 % · 10 Từ Ngắt kịp · 10 Cụm Ấn kịp · Long Hống cứu Hỏa Long dưới 10 % máu · 1.000 từ gõ xong |
| Hành Trình | 10 | Hết C1 · hết Hồi I, II, III · 3 sao cả một chương · 100 / 500 / 1.560 sao · hạ B20 · 52 Dấu Thách |
| Chiến thuật | 8 | 100 quái bị giam · đủ 6 chuỗi bẫy làm sẵn (03 §7.4) · thắng không lính chặn · một Bom nổ 10 con · Bùng Cháy 20 lần · hạ tướng trong 20 s đầu · 10 Vương Miện · thắng một Lời Thề +100 % |

- Hiện ở Sổ Thành Tựu. Hiện ở hồ sơ portal để sau (cần hợp đồng mới ở repo cha).

## 9. Bản địa hóa

- Bản đầu **chỉ tiếng Việt**. Mọi chuỗi giao diện nằm trong `src/content/strings.vi.json` theo khóa; test chặn chuỗi tiếng Việt viết cứng trong `src/ui`, `src/app`.
- Từ tiếng Anh trên quái là nội dung học, không phải chuỗi giao diện.
- Font: Be Vietnam Pro (chữ trận), Cormorant Garamond 700 (tiêu đề, kiểm đủ dấu trong `dh-prep-shop`), font IPA riêng (05 §4.4).
- Tiếng Anh cho giao diện: sau khi có người chơi ngoài nước; chỉ cần thêm `strings.en.json`.

## 10. Chống nản

| Luật | Chi tiết |
|---|---|
| Tua nhanh × 2 | Alt + → (bật, tắt). Chỉ khi đang nghỉ, hoặc khi không còn chữ sống và không quái nào trong Vùng Chữ. Sim chạy hai bước mỗi khung, vẫn tất định |
| Chơi lại ải | Menu dừng và Màn thua. Không mất gì ngoài Vàng của ải |
| Thử lại từ đợt trước | 1 lần mỗi lần chơi ải (01 §5), dùng ảnh chụp mục 1.3 |
| Gợi ý hạ mức khó | Sau 2 lần thua liền một ải (00 §4.10). Không ép |
| Bỏ qua ải | Hồ sơ trẻ em, hoặc bật "trợ năng: cho bỏ qua": sau 3 lần thua liền. Không bỏ được ải boss chương. Ải bỏ qua mở ải sau, 0 sao, quay lại được |
| Nhắc nghỉ | 30 phút (trẻ em 20), một dòng ở lần nghỉ kế tiếp, không dừng trận |

## 11. Admin, ôn tập, lịch sử học

- **Admin để sau.** Bản đầu soạn ải và dữ liệu bằng JSON trong repo game, có lược đồ (`src/content/schema`) và `stages:validate`. Chỗ nối sau này: Admin đọc cùng lược đồ, ghi ra `*.override.json` (04 §11.1), game không đổi.
- **Smart Review:** adapter `shared/learning/dragon-hold-review-dataset.mjs` ở lát C4–6 (DESIGN.md §9, M4). Trước đó sự kiện học vẫn vào hồ sơ chung, Mixed Review chỉ chưa trộn được.
- **Lịch sử học của TD:** sự kiện cũ mang `gameId` `space-typing` (TD đang nằm trong Space). Sau khi tách, TD gửi `typing-defense`. Không viết lại lịch sử: độ thuộc tính theo từ, nên không mất gì; thống kê theo game ghi rõ mốc đổi (`../SPLIT_PLAN.md` §7).

## 12. Giữ chỗ cho di động (chưa làm ở bản đầu)

- Lớp lệnh tách khỏi chuột và bàn phím: mọi việc là một **lệnh** (`useSkill(2)`, `placeItem(slot, item)`), chuột, phím, chạm chỉ là nguồn lệnh.
- Mọi lệnh có nút trên màn. Không thông tin nào chỉ hiện khi rê chuột (thẻ thông tin quái mở bằng chạm giữ).
- Gõ dùng sự kiện soạn chữ, để sau này nhận bàn phím ảo. Bố cục HUD có vùng an toàn.
- Xoay camera bằng hai ngón; đặt món bằng chạm ô.

## 13. Câu hỏi cho chủ dự án (đã có mặc định)

| # | Câu hỏi | Mặc định |
|---|---|---|
| 1 | Đồng bộ bản lưu qua tài khoản (`/api/account`) ở bản đầu? | Không. Xuất, nhập file; đồng bộ để sau, người chơi tự bật |
| 2 | Hồ sơ game dùng chung một hồ sơ học của portal? | Có. Muốn tách học (ví dụ cho con) thì dùng hồ sơ trình duyệt riêng; portal làm nhiều hồ sơ học sau |
| 3 | Giọng Bạch Long: giọng AI tiếng Việt dựng sẵn (có giấy phép thương mại)? | Có. Thu âm người thật để sau |
| 4 | Đo lường cục bộ tắt sẵn, người chơi tự bật? | Có |
| 5 | Cho hồ sơ trẻ em bỏ qua ải sau 3 lần thua (trừ boss chương)? | Có |
