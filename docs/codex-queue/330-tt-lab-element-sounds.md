# Phiếu 330 · Tu Tiên · Âm thanh: đưa âm Firefly của 14 hệ vào các sự kiện âm của lab

Anh (06/11 21:45): "việc còn lại cứ giao codex xử lý lần lượt". Hôm nay Firefly làm xong 657 việc âm, trong đó mỗi hệ có khoảng 30 loại âm (`tt-sfx-<hệ>-<loại>`). Lab mới có âm riêng cho Hỏa; 13 hệ còn lại đang dùng chung âm mặc định. Phiếu này chép âm của từng hệ vào đúng sự kiện của lab.

**Model `gpt-6.1-sol`, mức `high`.** Báo cáo: `docs/codex-queue/330-report.md` (tiếng Việt, ngắn).

## Cách lab tìm âm (đọc `games/.wt-ic-lab-panel/src/lab/sound.ts`, dòng 1–25)
- Sự kiện: `cast`, `release-<slot>` rồi `release`, `flyby`, `impact-flesh`, `impact-stone`, `impact-spirit`, `death`, `world-open`, `world-climax`, `world-close`, `callout`.
- Có hệ thì lab thử `"<sự kiện>-<hệ>"` trước, không có mới quay về `"<sự kiện>"`. Hệ là hậu tố âm của bộ hệ (ví dụ `fire`, `metal`, …): lấy đúng danh sách hậu tố trong mã lab (`grep` các element kit), không đoán.
- File: `art-src/lab/audio/<event-id>/01.ogg…03.ogg`, liệt kê trong `art-src/lab/audio/manifest.json` (`{ "<event-id>": ["01.ogg", …] }`).

## Nguồn
- Danh sách việc âm: `docs/work/tasks/firefly-sprint-sound.json` (`jobs[].id`).
- File: `games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/sound/<id>/take1.wav … take4.wav` (việc 2 lượt có tới take8).

## Bảng ghép (mỗi hệ `<el>` trong 14 hệ)
| Sự kiện lab | Lấy từ việc âm |
|---|---|
| `cast-<el>` | `tt-sfx-<el>-cast` |
| `release-<el>` | `tt-sfx-<el>-flying-sword-launch` |
| `release-dash-<el>` | `tt-sfx-<el>-dash` |
| `flyby-<el>` | `tt-sfx-<el>-sword-swing` |
| `impact-flesh-<el>` | `tt-sfx-<el>-sword-hit` |
| `impact-stone-<el>` | `tt-sfx-<el>-hit-heavy` |
| `impact-spirit-<el>` | `tt-sfx-<el>-hit-light` |
| `world-open-<el>` | `tt-sfx-<el>-charge-long` |
| `world-climax-<el>` | `tt-sfx-<el>-big-burst` |
| `world-close-<el>` | `tt-sfx-<el>-tail` |

- Thiếu việc nguồn (một số hệ không có `cast`, `hit-heavy`, `hit-light`, `tail`) thì bỏ ô đó; lab tự quay về âm chung.
- **Thư mục sự kiện đã có thì không đụng** (ví dụ các thư mục `-fire` sẵn có): không ghi đè file, không sửa mục manifest của nó.

## Cách làm
1. Script mới `games/.wt-ic-lab-panel/scripts/audio/lab-element-sounds.mjs` (Node, gọi `ffmpeg`, không thêm gói):
   - lấy 3 take đầu có thật của việc nguồn;
   - đổi sang `.ogg` (Vorbis, `-q:a 5`, giữ tần số mẫu gốc, không cắt, không chuẩn hoá: mức âm do `sound-tiers.ts` lo);
   - ghi `01.ogg`–`03.ogg` vào thư mục sự kiện mới;
   - thêm mục vào `manifest.json`: đọc, gộp, ghi lại nguyên tử, giữ nguyên mọi mục cũ;
   - có `--dry-run` in bảng sẽ làm.
2. Chạy `--dry-run`, rồi chạy thật.
3. Thêm `art-src/lab/audio/SOURCES.json` cho mỗi thư mục mới (nếu file có định dạng sẵn thì theo đúng định dạng đó): việc nguồn, take, prompt lấy từ `take<N>.prompt.txt`.

## Được ghi và cấm
- **Được ghi:** script mới ở trên; thư mục sự kiện mới, `manifest.json` và `SOURCES.json` trong `games/immortality-cultivation/art-src/lab/audio/`; báo cáo.
- **Cấm:** sửa mã lab; ghi đè hay xoá file âm có sẵn; sửa file trong `firefly-sprint-2026-11-05/sound/`; lệnh git ghi; mở cổng mạng.

## Xong khi
- Báo cáo có bảng: hệ × sự kiện, ô nào đã gắn, ô nào bỏ vì thiếu nguồn, ô nào bỏ vì đã có sẵn.
- `node --check` script qua; `manifest.json` đọc được bằng `JSON.parse` và mọi file nó liệt kê đều có thật.

## Hết hạn mức
Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`); làm xong phiếu thì không ghi.
