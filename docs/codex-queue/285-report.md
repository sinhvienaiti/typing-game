# Phiếu 285 · Âm lab: gộp tiếng hàng loạt và ép bus

Ngày: **05/11/2026**. Worktree: `/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-sound-mix`, nhánh `codex/sound-mix-duck`, HEAD `bbb46d8e20c6d340df214ad10dbb889271d19dd5`.

**Kết quả: phần mã và kiểm hành vi đạt; chưa đạt cổng 4 về cao trào hơn đợt trúng ít nhất 3 LU. Chưa sẵn sàng gộp. NOT LISTENED.**

## Các tệp đã ghi

Đường dưới worktree:

| Tệp | Nội dung |
|---|---|
| `src/lab/sound.ts` | Hạn mức 120 ms, GainNode tăng mức take đầu, log gộp, gain ép bus riêng, dừng/nhả ép tiếng hô khi reset. |
| `src/lab/sound-tiers.ts` | Hạn mức 4/3/2, bước tăng 0,25 dB/trần +1,5 dB, trần true peak và đỉnh nguồn từ 269, hàm tạo đường ép và lấy gain nhỏ nhất. Không đổi bảng trim cũ. |
| `scripts/audio/lab-sound-tiers.mjs` | Lệnh `mix` trộn theo bus, gain gộp đúng thời điểm, thời lượng giữ ép theo mẫu giải mã/rate, nhánh vang và hush cũ; hỗ trợ bản ghi 269. Các lệnh measure/attack/trims/ir giữ nguyên. |
| `tests/lab/sound-duck-merge.test.ts` | 15 ca hành vi mới dùng đồng hồ và AudioContext giả. |
| `docs/changelog/2026-11-05-lab-sound-duck-merge.md` | Thay đổi, cách chạy, kiểm và phần chưa đạt. |

Tệp thứ sáu là báo cáo này ở repo cha. Không sửa test cũ, fixture, sim, canon, nội dung, kit hoặc art-src. Không chạy lệnh Git ghi, build, server, trình duyệt hoặc model AI. Áp dụng `agent-orchestration` và `game-sfx`, làm một làn theo phiếu giao ngay, không mở vòng phản biện.

## Hành vi đã làm

- `impact-*` dùng **một hạn mức chung** qua mọi vật liệu/nguyên tố; death/flyby có hạn mức riêng. Cửa sổ mở từ take đầu, hết sau 120 ms. Tối đa 4/3/2 nguồn; sự kiện dư không chọn thêm file, không tạo nguồn và không đẩy vòng biến thể/tốc độ.
- Mỗi sự kiện dư tăng take đầu 0,25 dB, tổng không quá +1,5 dB. Trần nhỏ hơn khi thiếu phần dư tới −1 dBTP của bậc: dùng max TP nguồn của đánh giá 269, gain thực đã trim, gain bus/master và biên an toàn khi pan stereo gộp kênh. Nguồn chưa có số đo không được tăng mức. Trần này áp cho đường khô từng take; **không thêm limiter tổng live**.
- `merge.count` ghi tổng số sự kiện dư; `merge.boosts` ghi gain và thời điểm. Offline không tăng ngược toàn bộ take từ đầu và không gộp lại bản ghi mới.
- Cao trào ép combat −6 dB với 20 ms/độ dài take/300 ms. Tiếng hô ép combat/world −4 dB với 30 ms/độ dài take/250 ms. Các đường ép lấy gain nhỏ nhất, gồm cả điểm giao trong attack/release. Voice giữ nguyên; world không chịu ép cao trào.
- Hush vẫn 8% với ramp 12/10 ms; send trước bus, IR/return và trim cũ giữ nguyên. Reset dừng tiếng hô và nhả ép từ mức hiện tại; cao trào còn chạy không bị nhả theo.

## Ngoại lệ đường dẫn offline

Bộ trộn thực của 269 là **`scripts/visual/mix-lab-sound.mjs`**, không nằm trong danh sách được ghi của phiếu 285. Đã để nguyên tệp đó. Phần offline mới nằm trong script 269 được phép ghi, với lệnh sau (chạy từ worktree):

```sh
node scripts/audio/lab-sound-tiers.mjs mix <takes.json> <out.wav> \
  --root=/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation \
  --duration=25
```

Có `--offset=<s>` và `--ir=<file>`. **Claude phải dùng lệnh này để trộn video 285; đường gọi cũ chưa biết luật mới.** Không sửa caller/capture script ngoài phạm vi.

## Kiểm bắt buộc

| Kiểm | Kết quả |
|---|---|
| `node node_modules/typescript/bin/tsc --noEmit -p .` | Thoát 0, không lỗi. |
| `VITEST_MAX_THREADS=4 node node_modules/vitest/vitest.mjs run --no-cache --configLoader runner --maxWorkers 4` | **90 tệp, 1.004/1.004 test**, 12,21 s ở lần cuối. |
| Test mới | **15/15 qua**. 20 impact/100 ms → 4 nguồn; boost tối đa +1,5 dB; kiểm cả trần thấp hơn do true peak. Death 3, flyby 2; đổi vật liệu/nguyên tố vẫn cùng hạn mức. |
| Đường ép giả | Combat đúng −6 dB tại 20 ms, hold đúng buffer.duration/playbackRate và hồi sau 300 ms. Voice −4 dB tại 30 ms, hồi 250 ms. Chồng cao trào vẫn −6 dB; kiểm cả giao ramp, callout kéo dài và reset giữa attack. |
| Parity live/record | Cùng chuỗi sự kiện cho đúng 9 nguồn/take (4+3+2), cùng gain, pan, rate và mốc boost; ghi đủ 51 sự kiện dư. |
| WAV offline, giữ 100–300 ms | Cao trào **−6,0001 dB**, tiếng hô **−3,9999 dB**, chồng nhau **−6,0001 dB** so với cùng take không ép; sai số dưới 0,2 dB. Dùng âm repo thật, trigger gain 0 để đo riêng phần bus. |
| Bản ghi mới → offline | 20 impact: **4 take, 16 sự kiện gộp**, không gộp lần hai. |
| Kịch bản đủ 269 | Đã trộn lại Kim/Hỏa và đo trước/sau; **cổng chênh 3 LU chưa đạt**, bảng dưới. |
| `git diff --check`, status | Không lỗi khoảng trắng; chỉ các tệp được phép và `?? node_modules` có sẵn. Báo cáo ở repo cha được kiểm riêng. |

## Bảng trước/sau của kịch bản đủ

Nguồn: `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/sound-tiers/raw-after-{metal,fire}/takes.json`, cùng `run.json`: 25 s, slot k1 ở 0,5 s, k5 ở 3 s, k7 ở 12 s. Đây là bản ghi **sau 269, trước 285**. Trước dùng bộ trộn 269; sau dùng lệnh `mix` mới trên cùng log/âm nguồn. Không dùng lại mức trước khi có trim 269.

Meter: `apad=pad_dur=1,ebur128=peak=true:framelog=verbose`. Cửa sổ **400 ms là EBU momentary M**, tương ứng yêu cầu “LUFS-S 400 ms” của phiếu; không dùng cửa sổ S 3 s. Đợt trúng lấy đỉnh ở 5,5–6,25 s. Cao trào bắt đầu 6,25 s; lấy đỉnh ở 6,65–9,5 s để toàn bộ cửa sổ 400 ms nằm sau cue cao trào. Giữ cả voice, release, world và vang trong bản trộn đủ.

| Nguyên tố | Bản | Đỉnh đợt trúng / thời điểm | Đỉnh cao trào / thời điểm | Cao trào − đợt trúng | Đạt ≥ 3 LU |
|---|---|---|---|---:|---|
| Kim | Trước | −7,8 LUFS / 6,200 s | −8,6 LUFS / 6,700 s | −0,8 LU | Không |
| Kim | Sau | −8,7 LUFS / 6,200 s | −9,5 LUFS / 6,700 s | **−0,8 LU** | **Không** |
| Hỏa | Trước | −8,1 LUFS / 6,100 s | −8,9 LUFS / 6,700 s | −0,8 LU | Không |
| Hỏa | Sau | −9,1 LUFS / 6,100 s | −9,3 LUFS / 6,700 s | **−0,2 LU** | **Không** |

| Nguyên tố | Take trước → sau | Số gộp thêm | Số lần ép | File thiếu | Đỉnh 400 ms toàn đoạn trước → sau | TP trước → sau |
|---|---:|---:|---:|---:|---|---|
| Kim | 166 → 147 | 19 | 5 | 0 | −7,5 → −8,7 LUFS | −1,0 → −1,0 dBTP |
| Hỏa | 170 → 154 | 16 | 5 | 0 | −7,8 → −8,3 LUFS | −1,0 → −1,0 dBTP |

Các số đếm không tính marker hush. Bản ghi 269 chỉ lưu take đã phát; **không chứa từng sự kiện mà xô 40/50 ms cũ đã bỏ**, nên số gộp ở bảng là gộp thêm trên log cũ, không phải tổng gộp của một lần chạy live mới. Không nhận đây là nghiệm thu bản ghi mới trong host. Cần Claude ghi lại cùng cảnh sau khi ghép mã để có phép đo cuối.

**Ba luật hiện chưa chứng minh hoặc đạt mục tiêu 3 LU.** Đỉnh lớn nằm trước cue cao trào, khi voice/world-open/release và đuôi trúng còn chồng nhau. Chỉ ép combat lúc cao trào không hạ được đỉnh đã xảy ra; world và nhánh vang chung phải giữ theo phiếu. Không tự tăng cao trào, đổi trim/âm nguồn, đổi nhánh vang hoặc tăng mức ép ngoài −6/−4 dB để làm bảng qua cổng.

## Phần bỏ qua và cần xem

1. Không sửa entry offline trong `scripts/visual/` hoặc các script quay, vì ngoài danh sách được ghi. Dùng lệnh mới ở trên cho lần quay 285.
2. Không mở server, quay video, chạy build hoặc nhận đã nghe âm. Video trước/sau giữa bầy và chủ dự án nghe duyệt thuộc bước Claude làm sau.
3. Không chỉnh thêm để ép đạt 3 LU: cần Claude/chủ dự án quyết định sau phép đo log mới; phiếu hiện buộc giữ trim, nhánh vang và đúng độ sâu ép. **Chưa đủ điều kiện gộp.**
4. Chỉ tạo WAV trộn kiểm trong thư mục tạm `/private/tmp`, xóa sau khi ghi số ở đây; không tạo/sửa file âm nguồn, ảnh, raw frame hoặc capture lâu dài. Không ghi vào thư mục review bên SSD ngoài phạm vi được phép, nên không có index review cần dựng lại.

Trạng thái cuối trong worktree: sửa `scripts/audio/lab-sound-tiers.mjs`, `src/lab/sound.ts`, `src/lab/sound-tiers.ts`; thêm test và changelog nêu trên; `node_modules` không thay đổi, đã có từ đầu. Không stage/commit/push/reset/clean/stash.
