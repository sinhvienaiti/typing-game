# 31/10/2026 · Kit: bảng Settings và Sound trong trận, đợt da mới

## Yêu cầu

Lượt chấm thứ hai (31/10, khoảng 16:00): giám khảo chấm bảng Settings/Sound của Dragonhold và Wordwoven **6,5**; giám
khảo Last Line ghi cùng các chỗ hở của kit. Đợt này chỉ sửa kit (`shared/game-kit/ui/quick-settings/`), dựng móc cho
ảnh mới của phiếu Codex 244 và 245. Mỗi tuỳ chọn mới đều không bắt buộc: game chưa đặt thì trông như cũ. Chưa chép vào
game nào; Last Line nhận bản kit này sau.

## Đã làm

| Việc | Cách làm | Game dùng thế nào |
|---|---|---|
| 1. Phần đầy của thanh trượt | `<input type="range">` gốc nằm trong `.kit-qs__slider` cùng hai lớp ảnh `aria-hidden`: rãnh rỗng (`.kit-qs__groove`) và phần đầy (`.kit-qs__fill`). Kit đặt `--kit-qs-v` (0..1) trên `.kit-qs__slider` mỗi lần giá trị đổi; phần đầy bị cắt (`clip-path`) đúng tâm núm. Hai lớp vẽ ba mảnh bằng `border-image` như rãnh hiện tại của game, đầu rãnh giữ tỉ lệ. Rãnh riêng của ô trượt bị xoá khi lớp này bật | `skin.sliderFill`, `skin.sliderEmpty` (một trong hai là bật). Thiếu cái nào thì dùng `sliderTrack`; phần đầy lấy từ `sliderTrack` thì qua `--kit-qs-fill-filter` (mặc định `brightness(1.3) saturate(1.35)`), phần rỗng qua `--kit-qs-empty-filter`. Cắt: `--kit-qs-groove-slice` (ví dụ `0 64`), `--kit-qs-groove-cap` (ví dụ `calc(10px * var(--kit-qs-s))`); núm `--kit-qs-knob`, rãnh cao `--kit-qs-groove-h` |
| 2. Mọi rãnh dài bằng nhau | Nút Mute ra khỏi cột rãnh, vào cột cố định `.kit-qs__aside` sau con số. Bảng có hàng trượt kèm nút thì **mọi** hàng trượt của bảng đó giữ cột này (ô trống ở hàng không có nút); con số rộng cố định 2,4em; hàng trượt không xuống dòng | `--kit-qs-aside-w` (mặc định `calc(100px * var(--kit-qs-s))`). Nút vẫn là `.kit-qs__btn[data-toggle="muted"]`, `aria-pressed`, trong `.kit-qs__row[data-row="master"]`, nên `watchMute` của hai game chạy y như cũ |
| 3. Danh sách âm phím không còn kiểu listbox web | Mỗi dòng vẽ tấm ảnh chín mảnh ở `::before`; khung bo tròn và nền phẳng bị bỏ; dòng đang chọn mang tấm active; rê chuột làm sáng tấm; dòng tắt xám đi; nhãn vẫn có dấu ba chấm (`overflow: clip`) | `skin.listRow`, `skin.listRowActive` kiểu `QuickNineSlice { url?, slice, edge? }`. Thiếu `url` là ảnh `button` (`buttonActive` cho tấm active); không có ảnh active nào thì tấm thường sáng lên (`--kit-qs-list-active-filter`). Chỉnh: `--kit-qs-list-inset`, `--kit-qs-list-pad`; chữ dòng chọn `--kit-qs-active-text`. Danh sách ở Lab (ngoài bảng có da) giữ nguyên |
| 4. Icon trên mọi hàng | `icon` của hàng nhận tên bất kỳ (`QuickIconKey`); hàng mặc định của kit đều có tên: `vol-keyboard-volume` (Keyboard volume, đúng tên phiếu 244), `fx-style`, `fx-strength`, `fx-size`, `gfx-quality`, `gfx-motion`, `learn-meaning`, `learn-ipa` (`QUICK_ROW_ICON_NAMES`, để riêng khỏi `QUICK_ICON_NAMES` mà game map ra file, nên không sinh yêu cầu 404). Ô icon tự giữ rộng `--kit-qs-icon-size` khi trống, có `data-icon` | Hàng riêng của game đặt `icon: "game-pace"` v.v. và đưa URL qua `icons` / `setIcons` |
| 5. Close là nút icon | Ảnh ở góc trên phải bảng, 32 px ở 720p, tên đọc "Close", gợi ý "Close (Esc)"; ra khỏi lớp `.kit-qs__btn` khi là icon (không dính tấm nút của game); ảnh lỗi thì về nút chữ | `skin.close`; cỡ `--kit-qs-close-size`, dời lên góc khung bằng `--kit-qs-close-x` / `--kit-qs-close-y` |
| 6. Focus là quầng sáng | Khi có da: nút, chip, dòng danh sách, núm, nút icon góc và Close hiện focus bằng `--kit-qs-glow-filter` (drop-shadow ôm theo alpha của ảnh) thay viền phẳng 2 px. Không có da thì giữ viền như cũ | Màu `--kit-qs-glow` (mặc định `--kit-qs-focus`); đổi cả công thức qua `--kit-qs-glow-filter` |
| 7. Font tựa bảng | `.kit-qs__title` đọc `--kit-qs-title-font`, không đặt thì theo font của bảng (`inherit`) | Đặt `--kit-qs-title-font` trên lớp `.kit-qs` |
| Thêm | `skin.buttonActive`: nút đang nhấn hay đang bật mang tấm này (chữ `--kit-qs-active-text`); cũng là tấm active dự phòng của danh sách | Hai game đang vẽ tấm này bằng CSS riêng (`--dh-qs-button-active`, `--td-qs-button-active`); có thể chuyển sang trường này |

Mọi biến và mặc định: `QUICK_SETTINGS_VARS` trong `css.ts`. README của kit có thêm năm dòng ở mục `ui/quick-settings/`.

## Kiểm

- `pnpm kit:test`: trước 62 file, 997 test; sau **63 file, 1026 test**, đều qua. 29 test mới ở
  `ui/quick-settings/quick-panels-skin.test.ts` (mỗi tuỳ chọn mới, cả đường dự phòng và trường hợp không đặt); thử đột
  biến (bỏ lớp `kit-qs--skin-list`, ẩn lớp phần đầy) thì 3 test đỏ, đã trả lại.
- `pnpm --dir shared/game-kit typecheck`: 0 lỗi. Một file thử ghép đúng cách `quick.ts` của Dragonhold và Wordwoven
  dùng kit hiện nay: 0 lỗi kiểu, nên lúc đồng bộ không phải sửa mã game vì kiểu.
- Chrome không giao diện, trang thử riêng (kit gói bằng esbuild, CSS thật của hai game, ảnh thật trong
  `public/assets`), 1280 × 720 và 1920 × 1080. Tờ ghép và số đo: `games/dragon-hold/tmp/kit-qs/contact-dh-kit-qs.jpg`,
  `games/typing-defense/tmp/kit-qs/contact-td-kit-qs.jpg`, `numbers-kit-qs.json` cùng thư mục; ảnh thô đã xoá bằng
  `tools/capture-prune/prune.mjs`.
  - Rãnh mọi hàng bằng nhau: Dragonhold 107,5 px (cột 90 px), Wordwoven 139 px (cột 98 px) ở 720p; kit trơn 179,5 px.
  - Phần đầy dừng đúng tâm núm ở 0, 25, 50, 65, 80, 100 % (thử bằng màu lệch tông rồi bằng `--kit-qs-empty-filter`).
  - Tấm danh sách, dấu ba chấm với tên dài, quầng focus trên dòng, trên Mute, trên Close; font tựa theo biến, không
    đặt thì theo font của bảng; ô icon trống giữ chỗ, nhãn thẳng hàng.

## Việc còn lại (bước Games, chưa làm ở đây)

- Đồng bộ kit vào Dragonhold (`main`) và Wordwoven (`a2-days`), rồi trong CSS của game:
  - đặt `--kit-qs-aside-w` theo bề rộng nút Unmute của game (Dragonhold `calc(90px * var(--kit-qs-s))`, Wordwoven
    `calc(38px + 60px * var(--kit-qs-s))`), `--kit-qs-knob: calc(32px * var(--kit-qs-s))`,
    `--kit-qs-groove-slice: 0 64`, `--kit-qs-groove-cap: calc(10px * var(--kit-qs-s))`;
  - đổi luật hàng tắt tiếng từ `.kit-qs__range` sang `.kit-qs__slider` (khi bật lớp phần đầy, lọc trên ô trượt chỉ
    còn làm mờ núm);
  - quy tắc `.kit-qs__control .kit-qs__range { flex-basis: 6em }` của Dragonhold không còn tác dụng, bỏ được.
- Trước khi có ảnh 244/245: Dragonhold có thể bật phần đầy bằng `sliderEmpty` = rãnh 241 với
  `--kit-qs-empty-filter: brightness(0.45) saturate(0.5)`; Wordwoven có thể bật tấm danh sách bằng ảnh nút
  (`listRow: { slice: [170, 260], edge: [12, 18] }`). Ảnh nút của Dragonhold có lề trong suốt lớn nên tấm mỏng; nên
  chờ `list-row` của phiếu 245.
- Cái giá của cột Mute: rãnh các hàng khác ngắn đi khoảng một nửa ở 720p (Dragonhold từ khoảng 205 px, tính theo CSS cũ, xuống 107,5 px đo được). Nếu
  giám khảo thấy rãnh ngắn, cách còn lại là đưa Mute vào ô icon của hàng Master (cái loa bấm được); cách đó đổi nút chữ
  thành nút icon nên `watchMute` của hai game phải sửa.
- Last Line nhận bản kit này sau khi workflow đang chạy ở đó xong.

## Đồng bộ vào game (bước Games, 31/10)

Kit `18722b41` đã chép vào Dragonhold (`main`, `e52cfac`) và Wordwoven (`a2-days`, `e5e22de`); Last Line chưa. Mỗi game
có changelog riêng `docs/changelog/2026-10-31-kit-quick-panels.md`. Không sửa kit ở bước này.

- Cả hai game: phần đầy chạy trên rãnh đã nhận (`sliderEmpty` = rãnh; phần rỗng xám tối, phần đầy sáng có quầng), cột
  Mute theo bề rộng "Unmute", bảng Sound rộng 640 px (rãnh 720p: Dragonhold 187,5 px, Wordwoven 219 px), tấm đang bật
  qua `buttonActive`, danh sách âm phím trên tấm nút (dòng chọn trên tấm active), quầng focus theo màu game, font tựa
  của game, icon Keyboard volume dùng tạm `vol-keyboard`.
- Danh sách âm phím lớn theo bảng trong CSS của game (dòng, tiêu đề họ, icon nghe thử và mép tấm nhân `--kit-qs-s`):
  kit vẽ 34 px ở mọi cỡ, nên ở 1080p chữ lấp kín tấm. Nếu Last Line cũng cần, nên đưa việc này vào kit.
- Dragonhold thêm: nút và chip là tấm 162 chín mảnh cao 32 px (lề trong suốt đẩy ra ngoài bằng `border-image-outset`),
  danh sách cao 7,5 dòng để bảng Sound vừa khung ở 720p.
- Kiểm trên host chơi (1280 × 720 và 1920 × 1080, màn tựa và trong trận): phần đầy đo bằng điểm ảnh khớp giá trị ở 0,
  50, 100 % (lệch ≤ 0,5 px), mọi rãnh bằng nhau, 0 ảnh hỏng, 0 yêu cầu lỗi, 0 ngoại lệ, Tab ở trong bảng, Esc đóng, một
  phím một tiếng trên bộ Typing Feel vừa chọn.


## Lượt sửa (giám khảo 31/10, tối)

Giám khảo chấm bảng của Dragonhold và Wordwoven sau bước Games và ghi 11 mục; 6 mục thuộc kit, sửa ở `b8a224d0`, rồi
chép lại vào hai game (`--check` OK cho cả hai). Last Line vẫn chưa nhận bản kit này.

| Mục | Kit làm gì | Game dùng thế nào |
|---|---|---|
| Núm bị rãnh và phần đầy vẽ đè khi đứng yên | Lớp rãnh và phần đầy `z-index: 0`, ô trượt `position: relative; z-index: 1`: núm luôn trên ảnh, không cần hover hay focus | Không phải làm gì |
| Settings ở màn tựa có Resume và Quit to title | `QuickContext` (`"title"` \| `"play"`): tuỳ chọn `context` (giá trị hoặc hàm, đọc mỗi lần `open()` và `refresh()`), `setContext()`, `context`; ở `"title"` hàng `button` có `action` `"resume"`/`"quit"` ẩn, hàng nút trống cũng ẩn, nút riêng của game vẫn hiện; focus đang ở nút bị ẩn thì sang Close; gốc lớp có `data-context` | Dragonhold `context: () => (run ? "play" : "title")`; Wordwoven `QuickHooks.context`, `main.ts` truyền `titleUp` |
| Danh sách âm phím cắt cứng, dòng chọn nằm ở mép dưới | Mép trên/dưới mờ 10 px × `--kit-qs-s` (`mask-image`) chỉ khi còn dòng phía đó (`data-more-above`/`-below`); `scroll-snap-type: y proximity`, dòng và tiêu đề họ bám đầu; mở bảng thì dòng chọn ra giữa; mũi tên cuộn ít nhất và dừng đúng chỗ bám | Không phải làm gì |
| Tab đi qua mọi nút nghe thử | Chỉ nút Listen của dòng đang focus (hoặc đang chọn) có `tabindex="0"`; Tab từ danh sách tới Keyboard volume trong tối đa 2 lần | Không phải làm gì |
| Rê chuột trên dòng danh sách không thấy | `--kit-qs-list-hover-filter`, mặc định sáng 1,3 kèm quầng `--kit-qs-glow` | Dragonhold đặt quầng than hồng; Wordwoven dùng mặc định |
| Chữ thân là sans web | `--kit-qs-button-font` (nút, chip, nút chữ ở góc, dòng âm phím), `--kit-qs-label-font` (nhãn, tiêu đề mục, tiêu đề họ), `--kit-qs-note-font` (ghi chú, mặc định font trận) | Dragonhold Cormorant Garamond 700, Wordwoven Baloo 2 600 |

5 mục còn lại là CSS và skin của game (khung không lặp, hàng cao đều, Story mode một dòng, gắn cặp phần đầy/rỗng 244 đã
nhận, rê chuột trên nút của Wordwoven); chi tiết trong changelog của từng game.

Kiểm:

- `pnpm kit:test`: **64 file, 1038 test** (trước 63 file, 1026), đều qua; 12 test mới ở
  `ui/quick-settings/quick-panels-judge.test.ts`; ba test cũ của danh sách đổi từ "dòng chọn ở mép dưới" sang "ở giữa"
  như giám khảo yêu cầu.
- Hai game: Dragonhold 710 test qua (1 bỏ qua), Wordwoven 653; `pnpm build:dragon`, `pnpm build:td` OK; kiểm trên host
  chơi ở 1280 × 720 và 1920 × 1080 (núm trên ảnh ở 0/50/100, màn tựa ẩn hai nút, Tab tới Keyboard volume sau 2 lần,
  mép mờ, 0 yêu cầu lỗi, 0 ngoại lệ).
