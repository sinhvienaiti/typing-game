# Làn 5 · Gắn âm Firefly vào lab

Đã gắn **65 việc / 65 take** trong `games/.wt-ic-lab-all` (`codex/lab-all`). Không đổi các take, mức và bảng mix cũ. **Chưa nghe**; anh nghe và quyết cuối.

| Bước | Kết quả |
| --- | --- |
| 1 · Kiểm kê | JSON thực tế có **657** việc, khác 659 trong phiếu; 179 id đã có, **478** chưa gắn. Bảng nhóm bên dưới phủ đủ 478. |
| 2 · Song Long | **19** việc: thả/lượn/gào/ngọc nổ/tan; gào và chuông thay phiên. Greybox bám **F49/F57** trong mã hiện tại, thay F47/F51 ở `why`; swarm bám packet được presenter chấp nhận và lifecycle thật. |
| 3 · Quái, xác nhận | **22** việc: Herd tier 0/1/2/4; greybox/swarm đọc species thật, kiểm serial; B chặn vào hộ kiếm. Dùng chung xô impact **40 ms**, death **50 ms** và voice cap cũ. Hook confirm-spirit có trên bus nhưng lab chưa sinh loài spirit. |
| 4 · Chiêu/cut-in | **19** việc ở release/world của k5/k7, wipe/shout/ấn dấu/thoát cut-in. **D60/D61/M và D6–D8 đã có âm riêng**, giữ nguyên; các tuyệt kỹ 8/9 cũng giữ nguyên. |
| 5 · UI | **5** việc: bấm/chọn, rút lựa chọn, mở/đóng panel H, hover nút. Bus UI khô, send = 0, đích −28/−30 LUFS-M. |

**413 việc còn lại** chưa gắn: chờ hình/tính năng/hook riêng, hoặc là lớp thay thế của sự kiện đã có âm được bảo vệ. Không tự thêm tính năng hay thay âm cũ. Captain, ape, kiếp nạn, nhặt thưởng, shop, kết quả, cooldown/gauge và các pha boss riêng chưa có cảnh lab phù hợp.

## Chỗ gọi và file đã sửa

- `src/lab/sound.ts`: `SPRINT_TAKES`, route các cue mới qua `playTake`, thêm lớp ở xô chết đông; giữ `LAB_TAKES`, bảng sự kiện và cách chọn hậu tố cũ.
- `src/lab/sound-tiers.ts`: thêm đúng **65** mục đo vào `FIREFLY_LEVELS`; giữ toàn bộ mục cũ, gain bus, limiter, cap và duck.
- `src/lab/skills-main.ts`: callback bus release/world/impact/death; callback Song Long greybox; frame swarm và callback sim; callback cut-in; nhánh `fx.block` thành công của B; phím W/E; click/hover nút panel; đổi WPM, typed charge, sword, element, mục 8/9, aura; toggle panel H.
- `src/lab/twin-pearl-greybox.ts`: callback âm ở `stepWorld` và `onEvent`, nối constructor tùy chọn; không đổi sim/timeline.
- `src/lab/cutin.ts`: callback ở mở, khung shout, ấn dấu lần đầu và kết thúc tự nhiên. Reset chỉ đặt lại chốt âm; không đổi hình/timing.
- `tests/lab/lane5-sounds.test.ts`: **17 test node**: WAV/prompt thật, mức và onset, tất cả 65 id tới được từ event, xô 100 quái, loài/serial, timeline swarm thật, cut-in một lần, UI khô và chỗ gọi.

## Đo và kiểm tra

Đo **360 take** bằng `ffmpeg ebur128=peak=true`, lấy M max (400 ms) và true peak; `silencedetect` −45 dB lấy đầu lặng, WAV lấy độ dài. Prompt của **65/65** take chứa đúng prompt công việc. Chọn prompt khớp hành động, loại take gần im/lỗi; ưu tiên thân/đuôi chiến đấu, đuôi UI ngắn. Các mẫu chạm rail đều rời từng mẫu (run tối đa 1), không có plateau kéo dài; gain mỗi take khô, gồm bus/master, giữ **≤ −1 dBTP**. Âm chính Song Long dùng T4/T5, tiếng quái T3, các lớp phụ thấp hơn tiếng chính; UI T1 khô. Take chuông F0 được đổi sang take 4 sau đối chiếu crest để giữ lực mà không vượt peak.

Số đo, prompt gốc, lý do từng việc và SHA-256: `games/.wt-ic-lab-all/.local/lane5-sounds/{measurements,picks,checks,inventory-before,inventory-after}.json`. WAV gốc và prompt trong `firefly-sprint-2026-11-05` không sửa. Tổng WAV chọn khoảng **34,1 MB**.

| Mốc | TypeScript | Vitest |
| --- | --- | --- |
| Trước sửa | Sạch | 114 file / **1.311** test |
| Sau Song Long | Sạch | 115 file / 1.314 test |
| Sau quái | Sạch | 115 file / 1.320 test |
| Sau chiêu/cut-in | Sạch | 115 file / 1.322 test |
| Bổ sung B + kiểm cut-in thật | Sạch | 115 file / 1.324 test |
| Sau UI | Sạch | 115 file / 1.326 test |
| Cuối cùng, kiểm phủ đủ cue + swarm thật | Sạch | 115 file / **1.328** test, 54,60 s |

Lệnh: `npx --no-install tsc --noEmit`; `npx --no-install vitest run --maxWorkers=4`. `git diff --check` sạch. Đối chiếu snapshot: `LAB_TAKES`, `SOUND_IDS`, toàn bộ mức Firefly cũ và bảng mix cũ giữ nguyên. Không build, mở cổng/trình duyệt, tạo âm hay chạy lệnh git ghi.

**Anh cần nghe:** hai lượt Song Long để nghe biến thể, bầy quái chết cùng lúc, B lúc bật hộ kiếm, k5/k7 với cut-in, rồi panel H/E/W. Kiểm lực/đuôi và lớp mới chồng âm cũ; số đo không xác nhận chất âm hay tổng mix nghe thực tế. Đây là bàn giao kỹ thuật, chưa phải nghiệm thu nghe.

<details>
<summary>Kiểm kê đủ 478 việc chưa gắn lúc bắt đầu, theo group</summary>

| Nhóm | Số việc | Sự kiện lab / phần còn thiếu | Gắn được hay chờ tính năng |
| --- | ---: | --- | --- |
| Fire layers (ticket 269: crackle, glint) | 7 | Giữ 122 sự kiện hệ đã nghe; chưa có hook riêng cho các loop/pillar/orb/wave/lớp dư này | Chờ tính năng/hook riêng |
| Metal layers (ticket 269: ring, glint) | 7 | Giữ 122 sự kiện hệ đã nghe; chưa có hook riêng cho các loop/pillar/orb/wave/lớp dư này | Chờ tính năng/hook riêng |
| cut-in (SOUND_AUDIT 3, CUTIN_AUDIT) | 5 | Wipe mở, khung shout, ấn dấu, thoát tự nhiên; chưa có tiêu đề boss | Gắn 5; chờ 0 |
| element blood | 7 | Giữ 122 sự kiện hệ đã nghe; chưa có hook riêng cho các loop/pillar/orb/wave/lớp dư này | Chờ tính năng/hook riêng |
| element blood x sabre | 1 | Lab hiện chỉ trang bị sword; chưa có sabre/spear | Chờ tính năng/hook riêng |
| element blood x spear | 1 | Lab hiện chỉ trang bị sword; chưa có sabre/spear | Chờ tính năng/hook riêng |
| element dark | 7 | Giữ 122 sự kiện hệ đã nghe; chưa có hook riêng cho các loop/pillar/orb/wave/lớp dư này | Chờ tính năng/hook riêng |
| element dark x sabre | 1 | Lab hiện chỉ trang bị sword; chưa có sabre/spear | Chờ tính năng/hook riêng |
| element dark x spear | 1 | Lab hiện chỉ trang bị sword; chưa có sabre/spear | Chờ tính năng/hook riêng |
| element earth | 7 | Giữ 122 sự kiện hệ đã nghe; chưa có hook riêng cho các loop/pillar/orb/wave/lớp dư này | Chờ tính năng/hook riêng |
| element earth x sabre | 1 | Lab hiện chỉ trang bị sword; chưa có sabre/spear | Chờ tính năng/hook riêng |
| element earth x spear | 1 | Lab hiện chỉ trang bị sword; chưa có sabre/spear | Chờ tính năng/hook riêng |
| element fire | 6 | Giữ 122 sự kiện hệ đã nghe; chưa có hook riêng cho các loop/pillar/orb/wave/lớp dư này | Chờ tính năng/hook riêng |
| element fire x sabre | 1 | Lab hiện chỉ trang bị sword; chưa có sabre/spear | Chờ tính năng/hook riêng |
| element fire x spear | 1 | Lab hiện chỉ trang bị sword; chưa có sabre/spear | Chờ tính năng/hook riêng |
| element fire x sword | 1 | Giữ 122 sự kiện hệ đã nghe; chưa có hook riêng cho các loop/pillar/orb/wave/lớp dư này | Chờ tính năng/hook riêng |
| element ice | 7 | Giữ 122 sự kiện hệ đã nghe; chưa có hook riêng cho các loop/pillar/orb/wave/lớp dư này | Chờ tính năng/hook riêng |
| element ice x sabre | 1 | Lab hiện chỉ trang bị sword; chưa có sabre/spear | Chờ tính năng/hook riêng |
| element ice x spear | 1 | Lab hiện chỉ trang bị sword; chưa có sabre/spear | Chờ tính năng/hook riêng |
| element light | 7 | Giữ 122 sự kiện hệ đã nghe; chưa có hook riêng cho các loop/pillar/orb/wave/lớp dư này | Chờ tính năng/hook riêng |
| element light x sabre | 1 | Lab hiện chỉ trang bị sword; chưa có sabre/spear | Chờ tính năng/hook riêng |
| element light x spear | 1 | Lab hiện chỉ trang bị sword; chưa có sabre/spear | Chờ tính năng/hook riêng |
| element metal | 8 | Giữ 122 sự kiện hệ đã nghe; chưa có hook riêng cho các loop/pillar/orb/wave/lớp dư này | Chờ tính năng/hook riêng |
| element metal x sabre | 1 | Lab hiện chỉ trang bị sword; chưa có sabre/spear | Chờ tính năng/hook riêng |
| element metal x spear | 1 | Lab hiện chỉ trang bị sword; chưa có sabre/spear | Chờ tính năng/hook riêng |
| element metal x sword | 1 | Giữ 122 sự kiện hệ đã nghe; chưa có hook riêng cho các loop/pillar/orb/wave/lớp dư này | Chờ tính năng/hook riêng |
| element poison | 7 | Giữ 122 sự kiện hệ đã nghe; chưa có hook riêng cho các loop/pillar/orb/wave/lớp dư này | Chờ tính năng/hook riêng |
| element poison x sabre | 1 | Lab hiện chỉ trang bị sword; chưa có sabre/spear | Chờ tính năng/hook riêng |
| element poison x spear | 1 | Lab hiện chỉ trang bị sword; chưa có sabre/spear | Chờ tính năng/hook riêng |
| element star | 7 | Giữ 122 sự kiện hệ đã nghe; chưa có hook riêng cho các loop/pillar/orb/wave/lớp dư này | Chờ tính năng/hook riêng |
| element star x sabre | 1 | Lab hiện chỉ trang bị sword; chưa có sabre/spear | Chờ tính năng/hook riêng |
| element star x spear | 1 | Lab hiện chỉ trang bị sword; chưa có sabre/spear | Chờ tính năng/hook riêng |
| element thunder | 7 | Giữ 122 sự kiện hệ đã nghe; chưa có hook riêng cho các loop/pillar/orb/wave/lớp dư này | Chờ tính năng/hook riêng |
| element thunder x sabre | 1 | Lab hiện chỉ trang bị sword; chưa có sabre/spear | Chờ tính năng/hook riêng |
| element thunder x spear | 1 | Lab hiện chỉ trang bị sword; chưa có sabre/spear | Chờ tính năng/hook riêng |
| element void | 7 | Giữ 122 sự kiện hệ đã nghe; chưa có hook riêng cho các loop/pillar/orb/wave/lớp dư này | Chờ tính năng/hook riêng |
| element void x sabre | 1 | Lab hiện chỉ trang bị sword; chưa có sabre/spear | Chờ tính năng/hook riêng |
| element void x spear | 1 | Lab hiện chỉ trang bị sword; chưa có sabre/spear | Chờ tính năng/hook riêng |
| element water | 7 | Giữ 122 sự kiện hệ đã nghe; chưa có hook riêng cho các loop/pillar/orb/wave/lớp dư này | Chờ tính năng/hook riêng |
| element water x sabre | 1 | Lab hiện chỉ trang bị sword; chưa có sabre/spear | Chờ tính năng/hook riêng |
| element water x spear | 1 | Lab hiện chỉ trang bị sword; chưa có sabre/spear | Chờ tính năng/hook riêng |
| element wind | 7 | Giữ 122 sự kiện hệ đã nghe; chưa có hook riêng cho các loop/pillar/orb/wave/lớp dư này | Chờ tính năng/hook riêng |
| element wind x sabre | 1 | Lab hiện chỉ trang bị sword; chưa có sabre/spear | Chờ tính năng/hook riêng |
| element wind x spear | 1 | Lab hiện chỉ trang bị sword; chưa có sabre/spear | Chờ tính năng/hook riêng |
| element wood | 7 | Giữ 122 sự kiện hệ đã nghe; chưa có hook riêng cho các loop/pillar/orb/wave/lớp dư này | Chờ tính năng/hook riêng |
| element wood x sabre | 1 | Lab hiện chỉ trang bị sword; chưa có sabre/spear | Chờ tính năng/hook riêng |
| element wood x spear | 1 | Lab hiện chỉ trang bị sword; chưa có sabre/spear | Chờ tính năng/hook riêng |
| five-phase affliction | 14 | FivePhase chỉ có recipe Fire; M/charge/impact đã có âm; chưa có hook riêng theo 14 hệ cho lớp này | Chờ tính năng/hook riêng |
| five-phase charge | 14 | FivePhase chỉ có recipe Fire; M/charge/impact đã có âm; chưa có hook riêng theo 14 hệ cho lớp này | Chờ tính năng/hook riêng |
| five-phase comet | 14 | FivePhase chỉ có recipe Fire; M/charge/impact đã có âm; chưa có hook riêng theo 14 hệ cho lớp này | Chờ tính năng/hook riêng |
| five-phase seal | 14 | FivePhase chỉ có recipe Fire; M/charge/impact đã có âm; chưa có hook riêng theo 14 hệ cho lớp này | Chờ tính năng/hook riêng |
| gap beast-ape | 7 | Lab không sinh Nham Viên | Chờ tính năng/hook riêng |
| gap beast-boar | 7 | Herd tier 2 trúng/chết; chưa có biểu diễn cào móng/lao/húc/trấn nút | Gắn 2; chờ 5 |
| gap beast-common | 3 | Tan mực ở xô chết; chuỗi tan ở xô đông; chưa có gào với canyon tail riêng | Gắn 2; chờ 1 |
| gap beast-crow | 6 | Greybox Hỏa Nha trúng/chết; chưa có hình/callback riêng cho tiếng gọi/bổ nhào | Gắn 2; chờ 4 |
| gap beast-rat | 7 | Herd tier 0 chết dùng swarm-kill-crunch; chưa có âm nền theo mật độ/ngoạm Trận Tâm | Chờ tính năng/hook riêng |
| gap beast-wolf | 6 | Herd tier 1, greybox Phong Lang trúng/chết; chưa có biểu diễn cắn/gào/chạy theo đàn | Gắn 3; chờ 3 |
| gap boss | 19 | Herd king/greybox V trúng/chết; chưa có hình/hook riêng cho các pha, hơi thở, lao/húc | Gắn 2; chờ 17 |
| gap captain | 5 | Lab không sinh Lang Đầu Đàn | Chờ tính năng/hook riêng |
| gap cutin | 4 | Wipe mở, khung shout, ấn dấu, thoát tự nhiên; chưa có tiêu đề boss | Gắn 3; chờ 1 |
| gap elite | 12 | Herd coi tier 2 là elite: chết; chưa có trait/seal/giáp vỡ/hồi phục riêng | Gắn 1; chờ 11 |
| gap enemy-cue | 12 | B gặp hộ kiếm: chặn thành công; không có hình báo đòn circle/cone/line, vỡ khiên, Trận Tâm | Gắn 1; chờ 11 |
| gap reward | 11 | Chưa có nhặt vật phẩm, thu hoạch, tally, sao, elixir/dao fruit trong lab | Chờ tính năng/hook riêng |
| gap tribulation | 10 | Chưa có cảnh kiếp nạn/đột phá trong lab | Chờ tính năng/hook riêng |
| gap ui | 11 | Panel H mở/đóng, bấm/chọn/rút lựa chọn; chưa có hồi chiêu, gauge, shop, xây/nâng/bán | Gắn 4; chờ 7 |
| gap world | 19 | Chưa có hình/hook wave, cổng, Trận Tâm/nút, thắng/thua và ambience sở hữu vòng đời | Chờ tính năng/hook riêng |
| gap2 dao skills | 2 | Hook tương ứng chưa có riêng trong lab; giữ các âm đã gắn | Chờ tính năng/hook riêng |
| gap2 element fire | 1 | Hook tương ứng chưa có riêng trong lab; giữ các âm đã gắn | Chờ tính năng/hook riêng |
| gap2 element metal | 1 | Lab chưa có hình/hook tương ứng của hệ thống này | Chờ tính năng/hook riêng |
| gap2 formation | 1 | Lab chưa có hình/hook tương ứng của hệ thống này | Chờ tính năng/hook riêng |
| gap2 hero | 1 | Lab chưa có hình/hook tương ứng của hệ thống này | Chờ tính năng/hook riêng |
| gap2 kiem skills | 1 | Hook tương ứng chưa có riêng trong lab; giữ các âm đã gắn | Chờ tính năng/hook riêng |
| gap2 mechanism | 3 | Lab chưa có hình/hook tương ứng của hệ thống này | Chờ tính năng/hook riêng |
| gap2 meditation | 4 | Lab không có cảnh Tĩnh Tu | Chờ tính năng/hook riêng |
| gap2 meta | 1 | Lab chưa có hình/hook tương ứng của hệ thống này | Chờ tính năng/hook riêng |
| gap2 skill charge | 2 | Hook tương ứng chưa có riêng trong lab; giữ các âm đã gắn | Chờ tính năng/hook riêng |
| gap2 skill marks | 1 | Hook tương ứng chưa có riêng trong lab; giữ các âm đã gắn | Chờ tính năng/hook riêng |
| gap2 summon travel | 1 | Hook tương ứng chưa có riêng trong lab; giữ các âm đã gắn | Chờ tính năng/hook riêng |
| gap2 ui | 5 | Hover nút panel; chưa có countdown, chia thẻ, thông báo riêng | Gắn 1; chờ 4 |
| gap2 weapon | 1 | Hook tương ứng chưa có riêng trong lab; giữ các âm đã gắn | Chờ tính năng/hook riêng |
| hit confirm and kills (ticket 269, audio.md 5.3) | 14 | Xô impact 40 ms: confirm/chạm boss; death 50 ms: swarm/elite/chuỗi; các lớp khác đã có âm cũ | Gắn 8; chờ 6 |
| melee combo-finisher | 14 | Nhánh melee riêng chưa có trong lab; sword swing/launch giữ bộ âm hiện tại | Chờ tính năng/hook riêng |
| melee flying-sword-launch | 1 | Nhánh melee riêng chưa có trong lab; sword swing/launch giữ bộ âm hiện tại | Chờ tính năng/hook riêng |
| melee sabre-swing | 14 | Lab hiện chỉ trang bị sword; chưa có sabre/spear | Chờ tính năng/hook riêng |
| melee spear-thrust | 14 | Lab hiện chỉ trang bị sword; chưa có sabre/spear | Chờ tính năng/hook riêng |
| melee sword-swing | 1 | Nhánh melee riêng chưa có trong lab; sword swing/launch giữ bộ âm hiện tại | Chờ tính năng/hook riêng |
| per-skill missing layers (SOUND_AUDIT 3) | 8 | B chạm hộ kiếm: guard-deflect; các lớp auto/k1/guard/dash/k4 khác giữ âm cũ | Gắn 1; chờ 7 |
| shared big layers | 11 | Không có sự kiện mới độc lập; các đòn lớn/cast/ấn đã có âm riêng, giữ nguyên | Chờ tính năng/hook riêng |
| twin-dragons (SOUND_AUDIT 4) | 19 | F0 thả; F3 lượn; F49 gào; F57 ngọc nổ; F78 tan; swarm đọc packet/cast/burst/end | Gắn 19; chờ 0 |
| ultimate and k5 (ticket 269, SOUND_AUDIT 3) | 11 | k5/k7 release; world open/climax/close sẵn có; không đổi tuyệt kỹ riêng của 8/9 | Gắn 11; chờ 0 |
| weapon sabre | 2 | Lab hiện chỉ trang bị sword; chưa có sabre/spear | Chờ tính năng/hook riêng |
| weapon spear | 2 | Lab hiện chỉ trang bị sword; chưa có sabre/spear | Chờ tính năng/hook riêng |

</details>

<details>
<summary>65 take đã gắn: số đo và một dòng lý do mỗi việc</summary>

Id dưới đây đều có tiền tố `tt-sfx-`; đường dẫn đầy đủ là `sound/<id>/<take>`. M/TP tính bằng LUFS-M/dBTP; đầu lặng/độ dài tính bằng giây. Đích đã gồm bus/master; true peak có quyền hạ gain thấp hơn đích.

| Id | Take | M / TP | Bỏ đầu / Dài | Đích M | Lý do chọn |
| --- | --- | --- | --- | ---: | --- |
| `twin-bell-giant` | take6.wav | -6.0 / -0.0 | 0.0147 / 6.00 | -11.5 | Prompt khớp chuông chính khi ngọc nổ; thân/đuôi hữu ích 5.60 s; không có plateau ở rail |
| `twin-dragon-roar-a` | take5.wav | -8.7 / -0.1 | 0.0165 / 3.00 | -13.5 | Prompt khớp gào trái; thân/đuôi hữu ích 2.87 s; không có plateau ở rail |
| `twin-dragon-roar-b` | take4.wav | -6.6 / -0.0 | 0.0401 / 3.00 | -13.5 | Prompt khớp gào phải; thân/đuôi hữu ích 2.75 s; không có plateau ở rail |
| `twin-bronze-bell-high` | take4.wav | -14.7 / -1.4 | 0.0144 / 3.00 | -13.5 | Take 4 có crest thấp hơn take 7 (13,3 thay vì 21,2 dB), thân đạt gần T4 mà vẫn giữ trần −1 dBTP; đuôi hữu ích 1,46 giây. |
| `twin-sword-crack` | take4.wav | -6.5 / 0.1 | 0.0000 / 1.50 | -21 | Prompt khớp lóe kiếm F0; thân/đuôi hữu ích 1.45 s; không có plateau ở rail |
| `twin-fire-whoosh-a` | take7.wav | -9.4 / -0.0 | 0.0057 / 2.00 | -21 | Prompt khớp lượn trái; thân/đuôi hữu ích 1.95 s; không có plateau ở rail |
| `twin-fire-whoosh-b` | take6.wav | -8.5 / -0.0 | 0.0000 / 2.00 | -21 | Prompt khớp lượn phải; thân/đuôi hữu ích 1.95 s; không có plateau ở rail |
| `twin-deep-boom` | take1.wav | -7.8 / -1.2 | 0.0000 / 4.00 | -22 | Prompt khớp thân nổ ngọc; thân/đuôi hữu ích 4.00 s; không có plateau ở rail |
| `twin-mountain-echo` | take1.wav | -6.4 / -0.0 | 0.0171 / 5.00 | -25 | Prompt khớp đuôi núi sau nổ ngọc; thân/đuôi hữu ích 4.48 s; không có plateau ở rail |
| `twin-ember-crackle` | take1.wav | -28.4 / -1.5 | 0.0000 / 4.00 | -26 | Prompt khớp than hồng khi tan; thân/đuôi hữu ích 4.00 s; không có plateau ở rail |
| `twin-glint-shimmer` | take4.wav | -12.1 / -1.8 | 0.1349 / 3.00 | -25 | Prompt khớp lóe quanh nổ ngọc; thân/đuôi hữu ích 2.42 s; không có plateau ở rail |
| `twin-sparkle-ticks` | take2.wav | -16.3 / -6.3 | 0.0576 / 3.00 | -28 | Prompt khớp tia nhỏ khi tan; thân/đuôi hữu ích 2.22 s; không có plateau ở rail |
| `twin-roar-rumble` | take3.wav | -9.3 / -0.0 | 0.0195 / 3.00 | -25 | Prompt khớp thân trầm dưới gào; thân/đuôi hữu ích 2.95 s; không có plateau ở rail |
| `twin-flame-flutter` | take4.wav | -7.7 / -0.0 | 0.0000 / 3.00 | -27 | Prompt khớp lửa lượn; thân/đuôi hữu ích 2.96 s; không có plateau ở rail |
| `twin-sub-hit` | take1.wav | -6.6 / -1.1 | 0.0127 / 1.50 | -26 | Prompt khớp lớp trầm ngắn F0; thân/đuôi hữu ích 1.45 s; không có plateau ở rail |
| `twin-dragon-roar-c` | take3.wav | -8.2 / -0.1 | 0.0295 / 3.00 | -13.5 | Prompt khớp gào trái thay phiên; thân/đuôi hữu ích 2.76 s; không có plateau ở rail |
| `twin-bell-giant-b` | take2.wav | -15.1 / -7.1 | 0.0000 / 8.00 | -11.5 | Prompt khớp chuông thay phiên khi ngọc nổ; thân/đuôi hữu ích 8.00 s; không có plateau ở rail |
| `twin-fire-breath` | take3.wav | -8.2 / -0.0 | 0.0051 / 3.00 | -25 | Prompt khớp hơi lửa thân rồng; thân/đuôi hữu ích 2.97 s; không có plateau ở rail |
| `twin-pearl-shimmer` | take2.wav | -11.6 / -1.7 | 0.0000 / 3.00 | -26 | Prompt khớp ngọc di chuyển; thân/đuôi hữu ích 2.45 s; không có plateau ở rail |
| `k5-release-instant` | take3.wav | -32.6 / -22.2 | 0.0000 / 4.00 | -21 | Prompt khớp đầu release k5; thân/đuôi hữu ích 3.98 s; không có plateau ở rail |
| `k5-release-tail` | take1.wav | -3.7 / 0.1 | 0.0147 / 5.00 | -25 | Prompt khớp đuôi release k5; thân/đuôi hữu ích 4.19 s; không có plateau ở rail |
| `k5-sky-split` | take1.wav | -6.3 / 0.0 | 0.0134 / 3.00 | -21 | Prompt khớp trời xé khi k5 thả; thân/đuôi hữu ích 2.86 s; không có plateau ở rail |
| `ult-release-instant` | take2.wav | -5.8 / 0.0 | 0.0000 / 5.00 | -21 | Prompt khớp release k7; thân/đuôi hữu ích 4.92 s; không có plateau ở rail |
| `ult-climax-boom` | take4.wav | -6.4 / 0.0 | 0.0213 / 5.00 | -14 | Prompt khớp world climax; thân/đuôi hữu ích 4.68 s; không có plateau ở rail |
| `ult-sword-rain` | take1.wav | -4.5 / 0.0 | 0.0161 / 5.00 | -25 | Prompt khớp mưa kiếm k5; thân/đuôi hữu ích 4.84 s; không có plateau ở rail |
| `ult-preverb-swell` | take1.wav | -7.0 / 0.0 | 0.0887 / 1.50 | -25 | Prompt khớp tụ trước release k5, dưới cut-in; thân/đuôi hữu ích 1.39 s; không có plateau ở rail |
| `world-open-punch` | take1.wav | -7.9 / 0.0 | 0.0000 / 3.00 | -21 | Prompt khớp world open; thân/đuôi hữu ích 2.97 s; không có plateau ở rail |
| `ult-close-tail` | take4.wav | -6.4 / -0.1 | 0.0315 / 6.00 | -25 | Prompt khớp world close k7; thân/đuôi hữu ích 5.80 s; không có plateau ở rail |
| `ult-heaven-drone` | take1.wav | -10.2 / -0.5 | 0.0000 / 4.00 | -25 | Prompt khớp nền world open; thân/đuôi hữu ích 4.00 s; không có plateau ở rail |
| `k7-sword-river` | take1.wav | -9.0 / -0.0 | 0.0000 / 4.00 | -25 | Prompt khớp sông kiếm k7 mở; thân/đuôi hữu ích 4.00 s; không có plateau ở rail |
| `cutin-ink-whoosh` | take6.wav | -17.0 / -2.3 | 0.0605 / 1.50 | -21 | Prompt khớp wipe mở; thân/đuôi hữu ích 1.43 s; không có plateau ở rail |
| `cutin-frame-hit` | take2.wav | -9.5 / 0.0 | 0.0191 / 1.50 | -21 | Prompt khớp cắt sang shout; thân/đuôi hữu ích 1.35 s; không có plateau ở rail |
| `cutin-bell-tail` | take4.wav | -22.1 / -15.7 | 0.0000 / 4.00 | -25 | Prompt khớp đuôi thoát; thân/đuôi hữu ích 3.99 s; không có plateau ở rail |
| `cutin-sword-swarm` | take1.wav | -7.9 / 0.0 | 0.2694 / 3.00 | -25 | Prompt khớp kiếm ở khung shout; thân/đuôi hữu ích 2.67 s; không có plateau ở rail |
| `cutin-power-burst` | take3.wav | -7.4 / 0.0 | 0.0000 / 2.00 | -21 | Prompt khớp bùng sáng khung shout; thân/đuôi hữu ích 1.80 s; không có plateau ở rail |
| `confirm-flesh` | take8.wav | -14.5 / 0.0 | 0.0197 / 1.00 | -24 | Prompt khớp confirm flesh đầu xô; thân/đuôi hữu ích 0.96 s; không có plateau ở rail |
| `confirm-stone` | take8.wav | -9.1 / 0.1 | 0.0149 / 1.00 | -24 | Prompt khớp confirm stone đầu xô; thân/đuôi hữu ích 0.97 s; không có plateau ở rail |
| `confirm-spirit` | take7.wav | -6.9 / 0.0 | 0.0000 / 1.00 | -24 | Prompt khớp hook impact-spirit sẵn có trên bus; thân/đuôi hữu ích 0.87 s; không có plateau ở rail |
| `mass-kill-burst` | take3.wav | -8.7 / 0.0 | 0.0000 / 2.00 | -18 | Prompt khớp xô đông, thay phiên; thân/đuôi hữu ích 2.00 s; không có plateau ở rail |
| `mass-kill-chain` | take4.wav | -7.5 / -0.0 | 0.0155 / 3.00 | -18 | Prompt khớp xô đông, thay phiên; thân/đuôi hữu ích 2.71 s; không có plateau ở rail |
| `swarm-kill-crunch` | take4.wav | -11.8 / 0.0 | 0.0135 / 1.00 | -18 | Prompt khớp chết Thạch Thử; thân/đuôi hữu ích 0.98 s; không có plateau ở rail |
| `elite-death-bronze` | take1.wav | -7.3 / -0.0 | 0.0000 / 4.00 | -18 | Prompt khớp elite chết, thay phiên; thân/đuôi hữu ích 4.00 s; không có plateau ở rail |
| `boss-hit-heavy` | take3.wav | -7.1 / 0.0 | 0.0118 / 2.00 | -18 | Prompt khớp chạm boss còn sống; thân/đuôi hữu ích 1.86 s; không có plateau ở rail |
| `beast-wolf-death` | take3.wav | -7.5 / -0.0 | 0.0178 / 2.00 | -18 | Prompt khớp Phong Lang chết; thân/đuôi hữu ích 1.93 s; không có plateau ở rail |
| `beast-crow-death` | take2.wav | -7.9 / 0.0 | 0.0123 / 1.50 | -18 | Prompt khớp Hỏa Nha chết; thân/đuôi hữu ích 1.46 s; không có plateau ở rail |
| `beast-boar-death` | take4.wav | -7.2 / 0.0 | 0.0070 / 2.50 | -23 | Prompt khớp Thiết Giáp Trư chết; thân/đuôi hữu ích 2.43 s; không có plateau ở rail |
| `beast-common-ink-dissolve` | take5.wav | -11.6 / -0.3 | 0.0000 / 1.50 | -28 | Prompt khớp tan mực đầu xô chết; thân/đuôi hữu ích 1.45 s; không có plateau ở rail |
| `boss-death` | take3.wav | -6.8 / -0.0 | 0.0088 / 6.00 | -18 | Prompt khớp boss chết; thân/đuôi hữu ích 5.79 s; không có plateau ở rail |
| `elite-death-roar` | take2.wav | -7.7 / -0.0 | 0.0214 / 3.00 | -18 | Prompt khớp elite chết, thay phiên; thân/đuôi hữu ích 2.92 s; không có plateau ở rail |
| `ui-confirm` | take5.wav | -22.2 / -3.6 | 0.0000 / 1.00 | -28 | Prompt khớp bấm/chọn; đuôi hữu ích 0.41 s ngắn để UI khô |
| `ui-back` | take4.wav | -19.8 / -0.5 | 0.1798 / 1.00 | -28 | Prompt khớp rút lựa chọn 8/9 về mục trống; đuôi hữu ích 0.59 s ngắn để UI khô |
| `beast-wolf-snarl` | take2.wav | -4.9 / 0.0 | 0.0498 / 1.50 | -23 | Prompt khớp Phong Lang trúng, thay phiên; thân/đuôi hữu ích 1.45 s; không có plateau ở rail |
| `beast-wolf-hurt` | take3.wav | -7.0 / -0.1 | 0.0107 / 1.00 | -23 | Prompt khớp Phong Lang trúng; thân/đuôi hữu ích 0.97 s; không có plateau ở rail |
| `beast-crow-hurt` | take2.wav | -11.7 / -4.5 | 0.0000 / 1.00 | -23 | Prompt khớp Hỏa Nha trúng; thân/đuôi hữu ích 1.00 s; không có plateau ở rail |
| `beast-boar-hurt` | take2.wav | -10.5 / 0.0 | 0.0240 / 1.00 | -23 | Prompt khớp Thiết Giáp Trư trúng; thân/đuôi hữu ích 0.80 s; không có plateau ở rail |
| `beast-common-dissolve-chain` | take1.wav | -8.7 / 0.0 | 0.0471 / 3.00 | -25 | Prompt khớp xô từ 3 xác trở lên; thân/đuôi hữu ích 2.70 s; không có plateau ở rail |
| `boss-death-dissolve` | take1.wav | -8.3 / 0.0 | 0.0188 / 5.00 | -25 | Prompt khớp boss tan mực; thân/đuôi hữu ích 4.71 s; không có plateau ở rail |
| `ui-panel-open` | take1.wav | -20.6 / -1.7 | 0.1210 / 1.00 | -28 | Prompt khớp mở panel H; đuôi hữu ích 0.75 s ngắn để UI khô |
| `ui-panel-close` | take4.wav | -22.8 / -10.4 | 0.1420 / 1.00 | -28 | Prompt khớp đóng panel H; đuôi hữu ích 0.70 s ngắn để UI khô |
| `cutin-seal-stamp` | take3.wav | -15.8 / -0.2 | 0.0152 / 1.50 | -21 | Prompt khớp dấu ấn hạ xuống; thân/đuôi hữu ích 1.45 s; không có plateau ở rail |
| `cutin-exit-whoosh` | take4.wav | -16.1 / -0.8 | 0.1010 / 1.50 | -21 | Prompt khớp wipe thoát; thân/đuôi hữu ích 1.17 s; không có plateau ở rail |
| `cutin-time-freeze` | take1.wav | -7.3 / -0.0 | 0.3082 / 1.50 | -21 | Prompt khớp giữ thế giới lúc mở; thân/đuôi hữu ích 1.17 s; không có plateau ở rail |
| `ui-cursor-move` | take4.wav | -28.5 / -2.2 | 0.0250 / 1.00 | -30 | Prompt khớp hover nút panel; đuôi hữu ích 0.03 s ngắn để UI khô |
| `guard-deflect` | take3.wav | -7.2 / 0.1 | 0.0256 / 1.50 | -23 | Prompt khớp lớp gạt kiếm ở cùng cú chặn; thân/đuôi hữu ích 1.34 s; không có plateau ở rail |
| `enemy-hit-hero-shield` | take3.wav | -8.0 / 0.0 | 0.0162 / 1.00 | -18 | Prompt khớp đạn B bị hộ kiếm chặn; thân/đuôi hữu ích 0.96 s; không có plateau ở rail |

</details>
