# Thẻ spec âm (`specs/`)

Mỗi id âm của một game có một thẻ YAML: `specs/<game>/<id>.yaml`. Đây là lớp L0 của bộ phê bình và bước 1 của vòng làm âm ([`AUDIO_PIPELINE.md`](../../../docs/games/AUDIO_PIPELINE.md) §4.1, §5.1). Thẻ được **sinh** từ mã và danh sách âm của từng game. `games/**` chỉ được đọc, không bao giờ ghi.

## Lệnh

```bash
pnpm audio:specs generate            # sinh hoặc cập nhật mọi thẻ, giữ phần sửa tay, rồi kiểm
pnpm audio:specs generate --check    # không ghi; mã thoát 1 nếu thẻ lệch nguồn (dùng cho CI)
pnpm audio:specs validate            # kiểm theo schema/card.schema.json và luật riêng
pnpm audio:specs report              # số thẻ theo game và nhóm; mọi chỗ mã và danh sách âm lệch nhau
pnpm audio:specs report --json --out ~/AudioLab/work/_specs/report.json
pnpm audio:specs list --game typing-survival --category hit-small
pnpm audio:specs export --game dragon-hold   # chép sang ~/AudioLab/review/staging/<game>/art-src/audio/specs/
```

Thêm `--game <game>` để chỉ chạy một game. Chạy thẳng bằng venv cũng được (đặt chỗ ghi bytecode ra ngoài repo): `cd tools/audio-lab && PYTHONPYCACHEPREFIX=~/AudioLab/cache/pycache ~/AudioLab/.venv/bin/python -m specs validate`.

## Nguồn của từng game

| Game | Mã (catalog) | Danh sách âm | Ghi chú |
|---|---|---|---|
| `dragon-hold` | `src/audio/catalog.ts` (id, bus, ưu tiên, độ dài, `gainDb`), `mix.ts` (mức bus), `music-plan.ts` (lớp nhạc) | `docs/audio/M0_SOUND_LIST.md` | Catalog là nguồn chuẩn của độ dài |
| `typing-defense` | Không có bảng id. `readers/typing_defense.py` dò từng nhánh của `TypingAudio` (`EVIDENCE`) trong `src/view/audio-min.ts`, `music.ts` | `docs/audio/THEME_SOUND_LIST.md` | Độ dài lấy từ prompt |
| `typing-survival` | `src/audio/theme-audio.ts` (`SOUND_IDS`, `BUSES`, lời gọi `voice()`), `music.ts` | `docs/audio/THEME_SOUND_LIST.md` | Độ dài lấy từ prompt |

Thêm cả id do kế hoạch đề xuất (`hit.sub`, `hit.tail`, §6.3) và id chỉ nhắc trong văn bản (`kill.chime`), với `status: proposed` và `blocked_by: [sua-tai-lieu-game]`.

Mỗi bộ đọc kiểm lại các câu luật nó dựa vào (ví dụ "Đòn trúng nên có 3–6 biến thể"). Câu nào biến mất thì `report` ghi "Bộ đọc cần kiểm lại".

## Thẻ có gì

| Trường | Nội dung | Nguồn |
|---|---|---|
| `when`, `purpose` | Khi nào phát, cảm giác | Danh sách âm |
| `category` | Nhóm xếp hạng L2 (`key-ok`, `hit-small`, …, `fx-other` cho âm ngoài bảng) | §4.3.3 |
| `family` | 8 họ hiệu chỉnh, thêm `nhac` | §4.6 |
| `source_class` | Loại âm theo bảng nguồn | §3.2 |
| `playback` | `mode` (one-shot/loop), kênh, bus, ưu tiên, khoảng cách tối thiểu, trần phát | Mã, danh sách |
| `duration` | Đích, dung sai 20 % (nhạc: đúng ô nhịp, ±1 ms), khoảng của nhóm | Catalog hoặc prompt, §4.3.1 |
| `onset` | Thời gian lên, im lặng đầu tối đa. Lớp: `key`, `ui` (lên ≤ 3 ms), `impact` (trúng, bắn, nổ: ≤ 10 ms; cả `fx-other` thuộc họ `trung`, `ban`, `no`), `creature` (≤ 30 ms), `other` (thưởng, báo nguy, stinger, chết quái, khác: **không kiểm thời gian lên**, im lặng đầu ≤ 5 ms), `none` (vút, dâng), `loop` (không kiểm đầu tiếng). Test `test_cards_vs_plan.py` so mọi thẻ với bảng này | §4.3.1, lấy mức chặt hơn khi tài liệu game có giới hạn |
| `variants` | Số biến thể | Tài liệu game > §9 > §4.3.3 |
| `randomisation` | Cao độ, độ to khi phát, luật; cách mã đang làm | §5.3, mã |
| `frequency_role` | Dải chiếm, luật dải giọng 1–4 kHz | §6.4, §6.2 |
| `loudness` | Đích của file (tài liệu game), đề xuất của kế hoạch, mức bus, `gain_db` và `gain_basis`, `relative_db` (= `gain_db` + mức bus, tức mức so với bus trước master), mức nhường giọng, mức trong bản trộn. Lời Gọi và Tuyến Cuối chưa có mức riêng cho từng id nên `gain_db` = 0 | Mã, tài liệu game, §4.3.3 |
| `prompt` | Prompt của danh sách, đuôi chung, gốc prompt §5.2, `variants` (Claude viết, giữ khi sinh lại) | Danh sách, §5.2 |
| `pitches`, `parts`, `layer_plan` | Nốt cần làm; phần tách (đầu, vòng lặp, cuối); quan hệ lớp | Prompt, §6.3, §9 |
| `references` | Âm tham chiếu (trống lúc đầu) | Sửa tay |
| `source_plan` | Thứ tự nguồn, `now` (làm ngay khi chưa có mô hình), `later`, hồ sơ lô 1 | §3.2, §9, §10.1 |
| `licence` | Giấy phép được dùng, có điều kiện, bị cấm | §10.2 |
| `constraints` | Luật riêng của id và của game (văn hóa, chất liệu) | Tài liệu game, §8 |
| `board`, `critic` | Bối cảnh nghe, nhịp lặp; họ bẩn, trọng số lô 1, chấm trên bản lặp, nhãn AST nên có. `critic` còn chép sẵn các khóa mà `critic/spec.py` đọc (`group`, `loop`, `stereo`, `attack_max_ms`, `head_max_ms`, `rate_hz`, `bpm`, `bars`, `intent`, `refs`), tính lại sau mỗi lần sinh; `null` nghĩa là không kiểm. `group` theo `category`, trừ các id có khuôn riêng ở `taxonomy.CRITIC_GROUP_BY_ID` (`fire.impact.*` → `hit_fire`). `critic.clap` (nhãn, cặp chất liệu CLAP riêng cho id) chỉ sửa tay và phải ghi vào `manual_fields` (ví dụ `ui-pick`: phách gỗ cộng chuông đồng). `intent` luôn là chuỗi (prompt, hoặc `when` khi chưa có prompt) | §7, §4.4, §4.5 |
| `blocked_by` | Việc đang chặn (duyệt, tự ghi, Freesound…) | Bảng `BLOCKERS` trong `taxonomy.py` |
| `origin` | File nguồn, id có trong mã và danh sách không | Bộ đọc |

Tài liệu game thắng kế hoạch. Khi hai bên khác nhau, thẻ dùng số của tài liệu game và ghi số của kế hoạch ở trường `proposal` hoặc trong mục "Kế hoạch đề xuất khác tài liệu game" của `report`.

## Sửa tay

`generate` giữ:

- cả thẻ có `manual: true` ở gốc;
- mọi mục có `manual: true` (ví dụ đặt trong `duration:` để giữ cả mục);
- mọi đường dẫn ghi trong `manual_fields` (ví dụ `[duration.target_ms, constraints]`);
- luôn giữ `status`, `references`, `prompt.variants`, `notes`.

Comment YAML bị mất khi sinh lại. Ghi chú để ở `notes`.

## Dùng từ làn khác

```python
from specs import load_card, load_cards, taxonomy
card = load_card("typing-survival", "gun.xung")
taxonomy.CATEGORIES[card["category"]]["mix"]     # ngưỡng L2 của nhóm
```

## Kiểm thử

`pnpm audio:test` (hoặc `bash tools/audio-lab/run.sh test tools/audio-lab/specs`). Bài thử sinh thẻ từ game thật vào thư mục tạm, so mã băm file game trước và sau để chắc không ghi vào `games/**`.
