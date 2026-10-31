# Phiếu 247 · Last Line · Đổi ý tưởng ba icon còn trượt của 242

**Nguồn:**
- **Luật chung của đợt: mục "Luật chung của đợt 242–246" trong `docs/codex-queue/242-ts-icons-real-size.md`** (khối SMALL-SIZE, Kiểm 1–10, giới hạn ảnh, cấm, nhận). Phiếu này chỉ ghi chỗ khác.
- Báo cáo `242-report.md`. Claude chấm 31/10 khoảng 17:05, trên tờ tự dựng: bản cũ cạnh bản mới, ở 1× trên mảnh cắt thật từ `button.png` và `panel-large.png`, kèm nhãn.
  - **Nhận (từ 8):** `next-stage.r2`, `bay-full.r2`, `kills.r2`, `stat-accuracy.r2`, `stat-words`, `keyboard.r2`, `clock.r2`, `hazard.r2`. **Không động tới tám ảnh này.**
  - **Chưa đạt:**
    - `stat-evenness.r2` 7: ống thuỷ dài và mảnh; ở 28 px thành một thanh ngang nhỏ, giống lỗi của bản 152.
    - `stat-new-word.r2` 7: mắt trên thẻ; ở 28 px thành một khuôn mặt hay rô-bốt nhỏ.
    - `rift.r2` 7,5: khe hẹp, chỉ dùng khoảng 40 % bề ngang ô; ở 24 px thành một hạt tím.
  - Ba ảnh này đều đã dùng hết lượt ở ý cũ, nên phiếu này là **ý mới**, tính lượt lại.

**Báo cáo:** `docs/codex-queue/247-report.md` (tiếng Việt) và thư mục `docs/codex-queue/247/`. Model `gpt-6.1-sol`, mức `high`.

## Việc

Thư mục `games/typing-survival/art-src/ui/icons/`. Lượt sinh `<tên>.r3-tryN.*` (tối đa 3 lượt mỗi ảnh). Bản chọn `<tên>.r3.png` cùng `.r3.256.png`, `.r3.128.png`, `.r3.64.png`, `.r3.prompt.txt`. Không ghi đè gì.

Ba ý mới đều là **khối gọn, gần vuông** (hộp bao không quá 1,25:1), để chiếm hết ô ở 24–28 px.

| Tên | Nhãn | Cỡ 720p / 1080p | Đang đọc thành | Ý mới (EN) | So với |
|---|---|---|---|---|---|
| `stat-evenness` | Steadiness | 28 / 40 | thanh ngang nhỏ | a metronome seen front-on: a tall solid wedge body with a thick upright pendulum arm and a bright cyan weight, standing still at the centre | `clock.r2`, `stat-wpm.v2`, `bay-full.r2` |
| `stat-new-word` | New-word read | 28 / 40 | khuôn mặt, rô-bốt | an open book seen from the front, thick pages, with one bright four-point spark star rising above the spine | `stat-words`, `learning-rule` |
| `rift` | Rift | 24 / 32 | hạt tím, viên thuốc | a round dark portal disc split by one jagged violet crack from top to bottom, violet light bursting out of the crack; the disc fills the frame | `surge`, `warning`, `hazard.r2` |

- `rift` giữ sắc tím: đó là màu của mối nguy rift trong game. Số M (sắc gần magenta) có thể vượt 0,2 %; ghi số, không đổi màu để ép số.
- **Kiểm riêng:** độ rộng thật của bóng hình (alpha > 128) ở cỡ 720p phải chiếm **≥ 70 %** bề ngang ô và **≥ 70 %** chiều cao ô. Ghi số. Ô so sánh `stat-new-word` cạnh `stat-words` và `learning-rule`, `stat-evenness` cạnh `clock.r2`, ở 28 px 1×.

## Chỉ được ghi

- `games/typing-survival/art-src/ui/icons/{stat-evenness,stat-new-word,rift}.r3-try*.*`, `.r3.*` (mới).
- `games/typing-survival/art-src/_review/247*`.
- `docs/codex-queue/247-report.md`, `docs/codex-queue/247/`.
