# Hình và âm cho từng chi tiết giao diện map 1

Ngày 29/10/2026. Người rà: agent rà hình UI (do điều phối giao).

**Phạm vi:**
- Rà map 1 của ba game: **Dragonhold** (trước là Rồng Giữ Ải), **Wordwoven** (trước là Lời Gọi) và **Last Line** (trước là Tuyến Cuối).
- Rà mọi màn: tìm chỗ chỉ có chữ, emoji, đĩa chữ cái, hình CSS, SVG hay canvas vẽ thay cho ảnh.
- Mỗi chỗ ghi ảnh cần gắn, ảnh có sẵn hay phải vẽ mới.
- Thêm phần âm thanh và phần chữ phải đổi sang tiếng Anh.
- Không sửa mã hay ảnh nào.

**Cây đã rà:**
- Dragonhold: `games/dragon-hold`, nhánh main, 9e619ec.
- Wordwoven: `games/typing-defense`, nhánh a2-days, 999958a. Chỉ rà HUD và menu DOM. Map 1 lên 3D ở nhánh td-1c.
- Last Line: `games/typing-survival`, nhánh main. Phiếu giao ghi 461b45c, nhưng main đã lên e26e898 (gộp 090, 092, 104 của Codex). Số dòng theo e26e898.

**Ba luật mới của chủ dự án (28/10 tối) áp vào bản này:**
- Mọi chữ người chơi đọc là tiếng Anh. Tiếng Việt chỉ còn ở nghĩa của từ đang học. Mỗi bảng có cột "Chữ".
- Ảnh được chấm theo game thương mại, không theo khối STYLE cũ. Ảnh tham chiếu của chủ dự án: `games/typing-defense/art-src/_refs/owner-epic-2026-10-28.webp`. Ảnh đó có icon kỹ năng tròn trong vòng kim loại, khung chân dung có huy hiệu, icon hệ thống nét trắng.
- **Chia việc với làn chỉ đạo mỹ thuật (AD):**
  - AD làm nền, màn tựa, ảnh chủ đạo, logo, khung UI. Phiếu của AD đánh số từ 112: 112, 113, 114, 115, 119, 120, 121.
  - Bản này chỉ đặt icon, chân dung nhỏ, dấu, tem và mảnh UI nhỏ.

## 0. Tóm tắt

### 0.1. Số đếm

Mỗi dòng trong bảng mục 2–4 là một phần tử.
- **Có đủ ảnh:** chỉ cần gắn ảnh có sẵn.
- **Có một phần:** có ảnh cho một phần, phần còn lại cần ảnh mới.
- **Cần mới:** chưa có ảnh nào dùng được. Gồm cả phần của AD.
- **Bỏ hay giữ:** bỏ hình vẽ bằng mã, hoặc giữ vì là đồng hồ đo, VFX hay chữ số.

| Game | Phần tử | Có đủ ảnh | Có một phần | Cần mới | Bỏ | Giữ | Có ảnh dùng ngay (đủ + một phần) | Cần ảnh mới (một phần + mới) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Dragonhold | 69 | 8 | 14 | 42 | 0 | 5 | 22 | 56 |
| Wordwoven | 68 | 13 | 15 | 35 | 5 | 0 | 28 | 50 |
| Last Line | 54 | 8 | 8 | 35 | 1 | 2 | 16 | 43 |
| **Cộng** | **191** | **29** | **37** | **112** | **6** | **7** | **66** | **149** |

**Ảnh mới cần vẽ:**
- Ngoài phần của AD: **201 ảnh trong 21 phiếu**. Dragonhold 64, Wordwoven 86, Last Line 51. Chi tiết ở `UI_IMAGERY_CODEX.md`.
- Thêm 6 phiếu vẽ lại có điều kiện (Dragonhold 2, Wordwoven 3, Last Line 1). Chúng chỉ chạy nếu AD chấm bộ icon cũ dưới 8 theo mức chợ.

### 0.2. Mười việc P1 lớn nhất

| # | Game | Chỗ | Đang hiện | Cách lấp | Ảnh |
|---|---|---|---|---|---|
| 1 | Last Line | 5 thẻ súng ở "Nạp súng" (`screens-journey.ts:91-97`) | chỉ có chữ | gắn icon súng | có: `art-src/ui/icons/*.norm.*` (108) |
| 2 | Last Line | 2 bến chữ trong trận (`hud.ts:164-173`, `span.sv-gun` ở 168) | tên súng, không hình | icon súng cạnh tên | có: 108 |
| 3 | Wordwoven | màn tựa (`title.ts:106-137`, 160, 180-185) | khi ảnh không tải: cảnh SVG và cò bay; khi tải: vẫn còn dây đèn SVG và đom đóm CSS | bỏ cảnh SVG, cò, dây đèn, đom đóm; chép ảnh vào bản chơi (mục 1) | có `title-dusk.webp` tạm; AD 113 thay |
| 4 | Wordwoven | icon loại lời gọi trên thẻ chữ (`cards.ts:27,33`; `td.css:159`) | emoji 🏹 🔨 🌾 🪓 ⛏️ 📖 🔥 ✋ ⚓ 🛡️ | 10 icon lời gọi | mới: UIC-WW-1 |
| 5 | Wordwoven | thanh đội (`team-bar.ts:26`) | đĩa đèn lồng CSS có chữ D, C, P, G | chân dung Draconis và ba Thư Đồng | có: `art-src/portraits/` |
| 6 | Wordwoven | ô tài nguyên (`hud.ts:42,57`) | chữ và số | icon Gold, Wood, Rice, Lives; Seeds vẽ mới | có 4, mới 1 |
| 7 | Dragonhold | 30 icon SVG trong HUD, Bộ Mang Theo, ô đặt (`skin.ts:132-184`) | SVG vẽ tay | 17 icon vẽ có sẵn; số còn lại vẽ mới | có 17, mới ở UIC-DH-1..3 |
| 8 | Dragonhold | chân dung Hỏa Long và Bạch Long (`hud.ts:274-282`) | SVG trong đĩa gradient CSS | chân dung vẽ | mới: UIC-DH-6 |
| 9 | Dragonhold | chip quái ở thẻ đợt, thẻ ra mắt quái (`wave-card.ts:254-261`, `debut-card.ts:84-121`) | bóng SVG `foeIcon` | chân dung quái | một phần: cắt từ `art-src/enemies/`; mới: UIC-DH-7 |
| 10 | Last Line | danh sách quái ở thẻ ải, thẻ ra mắt Brute (`screens-journey.ts:70-72`, `hud.ts:395-409`) | chỉ chữ | chân dung quái | có: `art-src/ui/foes/` (089) |

### 0.3. Vì sao `title-dusk.webp` không hiện (tóm tắt)

- **Nguyên nhân:** bản chơi ổn định `games/.wt-play-typing-defense` không có file ảnh.
  - Ảnh là media, bị git bỏ qua.
  - Worktree tạo bằng git không có ảnh đó. Không ai chép media sang.
- **Lỗi đi kèm:**
  - Vite trả `index.html` (200, text/html) cho đường ảnh thiếu.
  - Ảnh giải mã lỗi. `title.ts` không có `onerror`, không ghi log.
  - Cảnh SVG dự phòng có cò bay ở lại.
- **Nginx:** cấu hình nginx đang cài không có host của Wordwoven, nên chủ dự án không chơi qua nginx.
- Chi tiết ở mục 1.

### 0.4. Âm thanh (tóm tắt)

- Cả ba game chưa có một file âm nào. Mọi tiếng đều tổng hợp bằng mã:
  - Dragonhold: 87 mã tiếng; 2 lớp nhạc đang câm vì thiếu file;
  - Wordwoven: 43 tiếng, trong đó 13 tiếng chưa có mã trong danh sách;
  - Last Line: 46 mã tiếng.
- Audio Lab đã có ứng viên cho nhiều tiếng của lượt đầu. Chủ dự án chưa chấm ứng viên nào. Việc đầu tiên là chủ dự án nghe chấm.
- Một quyết định phải hỏi chủ dự án:
  - luật mới nói mọi âm phải là file thật;
  - tài liệu pipeline lại cho tiếng phím giữ tổng hợp.
- Chi tiết ở mục 7.

## Cách đọc bảng

**Cột:**
- **#:** mã phần tử. DH = Dragonhold, WW = Wordwoven, LL = Last Line.
- **Phần tử:** file:dòng (tính từ gốc repo game) và class.
- **Đang hiện:**
  - "SVG" là SVG viết trong mã;
  - "CSS" là hình làm bằng CSS;
  - "canvas" là vẽ bằng canvas;
  - "chữ" là chỉ có chữ.
- **Ảnh cần:** loại ảnh, rồi cỡ hiện trên màn ở 1280×720 / 1920×1080, tính bằng px CSS.
  - Ảnh giao cỡ gốc 1024, xuất 64/128/256 cho màn HiDPI.
- **Có sẵn:** đường dẫn ảnh dùng được hôm nay. "kiểu cũ" là ảnh vẽ theo khối STYLE cũ, chờ AD chấm lại.
- **Cần mới:** tên ảnh mới và phiếu dự kiến (UIC-…), hoặc "AD" nếu thuộc làn chỉ đạo mỹ thuật, hoặc "bỏ".
- **Ưu tiên:** P1 khi ở màn lần đầu chơi hay trong HUD trận; P2 khi ở chỗ khác.
- **Chữ:** "VI → EN" là chữ tiếng Việt phải đổi; "EN" là đã tiếng Anh; "—" là không có chữ.

**Viết tắt đường dẫn ảnh:**
- Dragonhold:
  - `N:` = `games/dragon-hold/art-src/icons/normalized/` (bản 64 và 256 RGBA);
  - `DI:` = `games/dragon-hold/art-src/ui/icons/`;
  - `DE:` = `games/dragon-hold/art-src/enemies/`.
- Wordwoven:
  - `WU:` = `games/typing-defense/art-src/ui/`;
  - `WP:` = `games/typing-defense/art-src/portraits/`.
  - Ảnh Wordwoven nền xanh G hoặc tím M, chưa có alpha. Phải tách nền khi gắn, trừ `archer.alpha` và `barracks.trim`.
- Last Line:
  - `LI:` = `games/typing-survival/art-src/ui/icons/`;
  - `LF:` = `.../ui/foes/`;
  - `LS:` = `.../ui/stages/`.

**Thang cỡ UI:**
- Dragonhold: `--ui` = 0,8 ở 720p và 1,2 ở 1080p (`src/kit/ui/tokens.ts:34`).
- Wordwoven: `--ui` = 0,8 / 1,2; `--hud` = 1 / 1,2 (`src/main.ts:325-327`).
- Last Line: `--ui` = 1 / 1,5 (`src/app/main.ts:569`).

## 1. `title-dusk.webp` của Wordwoven: vì sao không hiện

### 1.1. Đo ngày 29/10

| Nơi chạy | File có không | Trình duyệt nhận | Kết quả |
|---|---|---|---|
| Dev ở cây chính `games/typing-defense` (Vite 127.0.0.1:4151) | có, 335.236 B | 200 `image/webp` 335.236 B | Ảnh hiện. Kịch bản `td-theme` ở 1280×720 báo `painted: true`. Tờ: `games/typing-defense/tmp/ui-imagery/sheet-td-theme-1280.jpg` |
| `vite preview` của `dist` ở cây chính (build 28/10 22:18) | có | 200 `image/webp` | Ảnh hiện |
| Dev hay preview, đường ảnh **thiếu** | không | 200 `text/html`, 817–859 B (Vite trả `index.html`) | Ảnh giải mã lỗi. Không có `onerror`, nên cảnh SVG ở lại |
| Mẫu nginx play (`infra/nginx/typing-game.local.play.conf:167-194`) | theo `dist` | `root games/typing-defense/dist`; `/assets/typing-defense/` dùng `try_files … =404` | Đúng nếu `dist` có ảnh |
| Nginx đang cài (`/opt/homebrew/etc/nginx/servers/typing-game.local.conf`, 18/10) | — | Không có server `td.typing-game.local`; `/etc/hosts` cũng không có tên đó | Không vào được Wordwoven qua nginx |
| Bản chơi ổn định `games/.wt-play-typing-defense` (7d6adf4, detached) | **không** | `public/assets/typing-defense/` chỉ có `models/manifest.json`; không có `dist` | Đây là bản chủ dự án chơi (`docs/CLAUDE_PROCESS_2026-10-24.md:57`). Ảnh thiếu, nên hiện cảnh SVG và cò |
| `.wt-td-codex`, `.wt-td-vfx` | không | — | Như trên |
| `.wt-td-1c` | có | — | Ảnh hiện |

### 1.2. Nguyên nhân

1. **Ảnh không có trong bản chơi.**
   - `title-dusk.webp` là media, nằm trong `.gitignore` (`*.webp` và `public/assets/**`).
   - Worktree tạo bằng git không có nó. Media chỉ có khi chạy media pull hay chép tay. Bản chơi chưa được làm bước đó.
2. **Mã giấu lỗi.**
   - `src/ui/title.ts:180-185` chỉ có `onload`. Không có `onerror`, không có log.
   - Kịch bản `td-theme` cũng chấp nhận màn tựa không có ảnh (dòng 14 của kịch bản).
   - Vì vậy không ai thấy lỗi.
3. **Có ảnh vẫn còn hình vẽ bằng mã.**
   - Ảnh mờ dần vào trong 1,4 s. Trong lúc đó cảnh SVG nằm trên (`title.css:9-11`).
   - Dây đèn SVG (`title.ts:38-45,127-137`), 14 đom đóm CSS (`title.ts:160`), dấu "Văn Điền" và nét cọ CSS luôn nằm trên ảnh.

### 1.3. Cách sửa (chưa làm)

- **Bản chơi:** chủ dự án hay điều phối chép `public/assets/typing-defense/ui/` từ cây chính sang bản chơi. Hoặc chạy media pull cho bản đó. Hoặc dựng bản chơi từ cây đã có media.
- **Mã** (sửa sau khi AD 113 giao màn tựa mới), trong `src/ui/title.ts`:
  - bỏ cảnh SVG ở dòng 106-124, cò ở dòng 121, dây đèn, đom đóm, dấu "Văn Điền";
  - thêm `onerror`: ghi `console.warn` và để nền màu tối phẳng;
  - không vẽ tranh thay thế.
- **Kiểm:**
  - `td-theme` phải đòi `painted: true`;
  - bộ kiểm gói deploy (phiếu 111, `check-pack.mjs`) nên liệt kê mọi URL ảnh lúc chạy và báo lỗi khi `dist` thiếu file.
- **Nginx:** cài host `td.typing-game.local` và dòng `/etc/hosts`. Việc này nằm trong cổng G7 của `MAP1_PRODUCTION.md` (chủ dự án chạy sudo một lần).

## 2. Dragonhold (`games/dragon-hold`, main 9e619ec)

**Tình hình chung:**
- Giao diện không tải ảnh nào lúc chạy: không có `url(`, không có `<img>`.
- Mọi icon là SVG viết tay: 30 icon ở `src/ui/skin.ts:127-184`, 11 icon ở `tags.ts:473-488`, 1 icon ở `learning-frame.ts:181`.
- Mọi bảng là "gỗ khắc" bằng gradient CSS, có rêu CSS (`dh.css:67-118`).
- Trong khi đó 21 icon vẽ và bản chuẩn hóa 64/256 nằm yên trong `art-src`.
- `public/` chỉ có GLB. Bản build không có ảnh 2D nào.

**Màn chưa có:** màn tựa, menu chính, cài đặt, hồ sơ, chọn ải, thẻ ải, cửa hàng riêng, thanh máu boss.
- Bộ Mang Theo đóng vai cửa hàng.
- Thiếu màn tựa là chỗ hở lớn nhất. AD 119 vẽ ảnh, nhưng game còn cần màn để gắn ảnh. Điều phối quyết vì đang tạm dừng tính năng mới.

### 2.1. Khởi động và lần đầu chơi

| # | Phần tử | Đang hiện | Ảnh cần (720p / 1080p) | Có sẵn | Cần mới | Ưu tiên | Chữ |
|---|---|---|---|---|---|---|---|
| DH-01 | Màn tựa: chưa có. Dòng nạp `app.ts:205` `.dh-boot` | chữ "Rồng Giữ Ải · Bản thử…" | màn tựa có ảnh chủ đạo và logo, toàn màn | 096: chữ logo cũ thôi dùng; huy hiệu chấm 5,5 | AD 119; cần màn tựa trong mã | P1 | VI → EN |
| DH-02 | Biểu tượng tab `index.html:9` | rỗng (`data:,`) | favicon 32 / 64 | — | cắt từ huy hiệu 119 bằng công cụ | P2 | — |
| DH-03 | Lớp che lần đầu `app.ts:248-250,882` `.dh-veil.is-soft` | chữ trên hộp CSS | icon bàn phím 24 / 36 + bảng | — | `keyboard` (UIC-DH-2); bảng: AD | P1 | VI → EN |
| DH-04 | Thẻ tốc độ: bảng `pace-card.ts:24` `.dh-panel.dh-pacecard` | gỗ CSS, rêu CSS | bảng vẽ 9-slice, khoảng 330×420 / 500×630 | — | AD (chưa có phiếu khung Dragonhold) | P1 | — |
| DH-05 | Thẻ tốc độ: hàng `pace-card.ts:99-110` `.dh-key` | chữ "35 WPM" + phím CSS | huy hiệu tốc độ 20 / 30; mặt phím vẽ | — | `pace-*` ×4 (UIC-DH-6); `keycap` (UIC-DH-5) | P1 | VI → EN |
| DH-06 | Học trước `learning-frame.ts:404-467` `.dh-lpanel` | bảng CSS; "_" chỗ trống; "+5 Gold" chữ | bảng; icon loa 14 / 22; icon Gold 12 / 18; huy hiệu từ mới | Gold: `N:gold.64` | `speaker`, `new-word` (UIC-DH-2); bảng: AD | P1 | VI → EN |

### 2.2. HUD trận

| # | Phần tử | Đang hiện | Ảnh cần (720p / 1080p) | Có sẵn | Cần mới | Ưu tiên | Chữ |
|---|---|---|---|---|---|---|---|
| DH-07 | Bảng trận `hud.ts:234` `.dh-battle` | gỗ CSS | bảng HUD vẽ | — | AD | P1 | — |
| DH-08 | Ô Gold `hud.ts:236-242` | SVG `coin` | icon Gold 16 / 24 | `N:gold.64` (kiểu cũ) | — | P1 | EN |
| DH-09 | Ô Đợt `hud.ts:243-246` | chữ "Đợt" | icon tù và 16 / 24 | — | `wave-horn` (UIC-DH-1) | P1 | VI → EN |
| DH-10 | Ô Chuỗi `hud.ts:247-251` | chữ "Chuỗi ×1,08" | icon chuỗi lửa 16 / 24 | — | `chain` (UIC-DH-1) | P1 | VI → EN |
| DH-11 | Dòng pha `hud.ts:252,421-433` `.dh-phase` | chữ "Bày binh · ↵…" | icon pha 16 / 24 (bày binh, đánh, nghỉ) | — | `phase-prep`, `phase-fight`, `phase-break` (UIC-DH-1) | P1 | VI → EN |
| DH-12 | Nút tạm dừng `hud.ts:258-260` | SVG `pause` + phím Esc | icon 16 / 24 | — | `pause` (UIC-DH-2) | P1 | — |
| DH-13 | Nút về camera `hud.ts:264-266` | SVG `camera` | icon 16 / 24 | — | `camera-reset` (UIC-DH-2) | P1 | — |
| DH-14 | Bảng rồng `hud.ts:271` `.dh-dragons` | gỗ CSS | bảng HUD vẽ | — | AD | P1 | — |
| DH-15 | Chân dung Hỏa Long `hud.ts:274-275` `.dh-portrait` | SVG `dragon` trong đĩa gradient (`dh.css:349-359`) | chân dung bán thân trong vòng 46 / 70 | — (chỉ có huy hiệu 096) | `hoa-long`, `hoa-long-hurt` (UIC-DH-6); vòng: AD | P1 | — |
| DH-16 | Huy hiệu cấp `hud.ts:276,451` `.dh-level` | số trong đĩa CSS | đế huy hiệu 16 / 24 | — | `level-badge` (UIC-DH-5) | P1 | — |
| DH-17 | Bạch Long dẫn đường `hud.ts:279-282` | SVG `white-dragon` + chữ | chân dung 19 / 29 | — | `bach-long` (UIC-DH-6) | P1 | VI → EN |
| DH-18 | Chip Giáp `hud.ts:288-292` | SVG `armour` | icon 12 / 18 | `N:hard-scale.64` tạm được | `armour` (UIC-DH-1) | P1 | — |
| DH-19 | Chip Khiên `hud.ts:293-297` | SVG `shield` | icon 12 / 18 | — | `shield` (UIC-DH-1) | P1 | — |
| DH-20 | Thanh máu `hud.ts:300-305` (`dh.css:447-508`) | gradient CSS, sọc CSS | khung thanh vẽ; phần đầy giữ bằng mã | — | AD | P1 | VI → EN ("khiên") |
| DH-21 | Ô Fire Breath, Sky Fire `hud.ts:321-323` | SVG `breath`, `skyfire` | icon kỹ năng 21 / 31 trong ô 37 / 55 | `N:skill-fire-breath.64`, `N:skill-sky-fire.64` | — | P1 | — |
| DH-22 | Ô Dragon Roar `hud.ts:324-325` | SVG `roar` + chip "Từ Khẩn" | icon 21 / 31 | `N:015-skill-roar.64` (8,5, tạm nhận) | — | P1 | VI → EN |
| DH-23 | Ô đồ tiêu hao ×2 `hud.ts:327-329,474-484` | SVG `potion` (mọi món cùng một hình) | icon món 21 / 31 | `N:potion-small.64` | — | P1 | — |
| DH-24 | Đồng hồ Dragon Rage `hud.ts:331-336` (`dh.css:618-650`) | chữ + thanh gradient | icon 16 / 24; khung thanh | — | `dragon-rage` (UIC-DH-1); khung: AD | P1 | EN |
| DH-25 | Ô Inferno `hud.ts:337` | SVG `inferno` | icon 21 / 31 | `N:skill-ultimate.64` | — | P1 | — |
| DH-26 | Toast `hud.ts:344-376,509` | chữ | icon theo loại 16 / 24 | Gold, potion có | `deny` (UIC-DH-2) | P1 | VI → EN |
| DH-27 | Lớp hồi chiêu `dh.css:563` | conic-gradient | giữ: đồng hồ đo | — | — | — | — |

### 2.3. Thẻ đợt

| # | Phần tử | Đang hiện | Ảnh cần (720p / 1080p) | Có sẵn | Cần mới | Ưu tiên | Chữ |
|---|---|---|---|---|---|---|---|
| DH-28 | Bảng `wave-card.ts:141` | gỗ CSS | bảng vẽ | — | AD | P1 | — |
| DH-29 | Hàng đường `wave-card.ts:244-266` | chữ "Đường Cầu…"; SVG `wing` ở đường trời; chữ "Yên" | icon đường 16 / 24 | — | `lane-bridge`, `lane-stream`, `lane-sky` (UIC-DH-3) | P1 | VI → EN |
| DH-30 | Chip quái `wave-card.ts:254-261` | bóng SVG `foeIcon` (`skin.ts:172-184`) + SVG vương miện, cánh | chân dung tròn 22 / 34 (lớn hơn hôm nay) | tạm: `N:family-moss/beast/bug.64`, `N:enemy-general.64`; nguồn cắt: `DE:*.png` | 7 chân dung (UIC-DH-7) | P1 | VI → EN ("Tướng") |
| DH-31 | Chip báo `wave-card.ts:268-292` | SVG cánh "Quái bay ×n", SVG vương miện; chữ "Đợt nhẹ" | icon 14 / 20 | `N:enemy-general.64` | `lane-sky` dùng chung; đợt nhẹ dùng `phase-break` | P1 | VI → EN |
| DH-32 | Dải nhịp `wave-card.ts:296-313` | khối và chấm CSS | giữ: biểu đồ | — | — | — | VI → EN |
| DH-33 | Nút bắt đầu `wave-card.ts:154,359-360` | phím CSS + chữ | nút vẽ; mặt phím | — | nút: AD; `keycap` (UIC-DH-5) | P1 | VI → EN |
| DH-34 | Nút Gọi sớm `wave-card.ts:153,365-367` | phím + chữ "+N Gold · +N Dragon Rage" | icon gọi sớm 20 / 30 + Gold + Rage | `N:call-wave.64`, `N:gold.64` | `dragon-rage` | P1 | VI → EN |
| DH-35 | Băng rôn đợt `wave-card.ts:159-161,380-383` | chữ trên bảng CSS | băng rôn vẽ + icon tù và | — | băng rôn: AD; `wave-horn` | P1 | VI → EN |

### 2.4. Bộ Mang Theo (cửa hàng) và đặt bẫy

| # | Phần tử | Đang hiện | Ảnh cần (720p / 1080p) | Có sẵn | Cần mới | Ưu tiên | Chữ |
|---|---|---|---|---|---|---|---|
| DH-36 | Bảng Bộ Mang Theo `shop-strip.ts:172-176` | gỗ CSS, chữ "Bộ Mang Theo" | bảng vẽ | — | AD | P1 | VI → EN |
| DH-37 | 8 ô món `shop-strip.ts:235-255` | SVG món + SVG đồng xu | icon món 32 / 48 trong ô 46 / 70 (hôm nay icon 19 / 29) | `N:spikes`, `pine-bomb`, `net-launcher`, `moss-warden`, `herb-hut`, `potion-small`, `dragon-heart`, `hard-scale` (.64/.256), `N:gold.64` | — | P1 | EN |
| DH-38 | Nhãn ô (khóa, mới, lý do) `dh.css:1007-1140` | chữ trên viên CSS | icon khóa 12 / 18; huy hiệu mới | — | `lock`, `new-word` (UIC-DH-2) | P1 | VI → EN |
| DH-39 | Dòng thông tin `shop-strip.ts:177,288-298` | chữ | icon món đang trỏ 16 / 24 | như DH-37 | — | P1 | VI → EN |
| DH-40 | Dấu ô đã đặt `placement-ui.ts:404,600-603` | SVG món + 3 chấm CSS | icon món 27 / 41 + chấm cấp | icon món DH-37 | `pip-lit`, `pip-unlit` (UIC-DH-5) | P1 | — |
| DH-41 | Dấu ô trống `placement-ui.ts:600-603` (`dh.css:1170-1243`) | SVG `bar`, `rune`, `flag` trong đĩa CSS | biển ô 24 / 36 (Ô bẫy, Bệ nhà, Điểm giữ) | — | `slot-trap`, `slot-house`, `slot-hold` (UIC-DH-3) | P1 | — |
| DH-42 | Vòng tầm `placement-ui.ts:238-241,615-626` | đa giác SVG | giữ: lớp chỉ dẫn | — | — | — | — |
| DH-43 | Thẻ con trỏ `placement-ui.ts:244-246,629-661` | chữ "N Gold · Ô bẫy · Đường Cầu" | icon món, Gold, đường 16 / 24 | món, Gold | `lane-*` | P1 | VI → EN |
| DH-44 | Menu ô (bấm chuột) `placement-ui.ts:495-540` | phím + SVG món + "=" nâng, "-" bán | icon món; icon nâng và bán 16 / 24 | món | `upgrade`, `sell` (UIC-DH-2) | P1 | VI → EN |
| DH-45 | Dòng hướng dẫn `placement-ui.ts:249,672-676` | chữ + phím mũi tên CSS | mặt phím vẽ | — | `keycap` (UIC-DH-5) | P1 | VI → EN |

### 2.5. Chữ trên quái, thẻ ra mắt, cảnh trận

| # | Phần tử | Đang hiện | Ảnh cần (720p / 1080p) | Có sẵn | Cần mới | Ưu tiên | Chữ |
|---|---|---|---|---|---|---|---|
| DH-46 | Thân thẻ chữ `tags.ts:664-670,885-899` (CSS `tags.ts:495-501`) | hộp tối CSS, viền theo loại | đế thẻ 9-slice theo loại (quái, tướng, khẩn) | — | `tag-plate-*` (UIC-DH-5); đọc chữ là trên hết | P1 | — |
| DH-47 | Icon loại thẻ `tags.ts:455-488,890` | SVG `swarm`, `badge`, `seal`, `flag`, `roar` | icon 18 / 22 | `N:enemy-general.64`, `N:015-skill-roar.64` | `swarm`, `seal-lit`, `flag-pull` (UIC-DH-3) | P1 | — |
| DH-48 | Huy hiệu từ mới `tags.ts:892` | viên CSS chữ "MỚI" | icon lấp lánh + chữ "New" | — | `new-word` | P1 | VI → EN |
| DH-49 | Chấm Ấn Phá `tags.ts:893` | ký tự "◆" / "●" | chấm ấn sáng/tắt 10 / 14 | — | `seal-lit`, `seal-unlit` (UIC-DH-3) | P1 | — |
| DH-50 | Mũi tên chip mép `tags.ts:543` | tam giác viền CSS | mũi tên vẽ 10 / 14 | — | `edge-arrow` (UIC-DH-3) | P1 | — |
| DH-51 | Khung học `learning-frame.ts:214-339` | chấm CSS theo cấp, ký tự "✓", "MỚI", SVG loa | icon loa, dấu đúng, huy hiệu mới 14 / 22 | — | `speaker`, `check`, `new-word` | P1 | VI → EN |
| DH-52 | Thẻ ra mắt quái `debut-card.ts:84-121` (`dh.css:1347-1406`) | bóng SVG `foeIcon` 22 / 34, hoặc vương miện SVG | chân dung bán thân 77 / 115 | nguồn cắt: `DE:*`, `art-src/generals/moss-banner.png` | 7 chân dung (UIC-DH-7) | P1 | VI → EN |
| DH-53 | Dòng báo `app.ts:240,830` `.dh-notice` | chữ (IME; "Máu Hỏa Long thấp: ⌥7 uống Small Potion") | icon bàn phím, icon món | `N:potion-small.64` | `keyboard` | P1 | VI → EN |
| DH-54 | Nhãn tua nhanh `app.ts:243` `.dh-ff` | chữ "×2" | icon tua 16 / 24 | — | `fast-forward` (UIC-DH-1) | P1 | — |
| DH-55 | Dấu "!" báo đòn `view/telegraphs.ts:187-211,236-298` | đĩa đỏ vẽ canvas có "!" | icon nguy hiểm vẽ, sprite 3D | — | `danger` (UIC-DH-1) | P1 | — |
| DH-56 | Cờ tướng cắm xuống `view/banners.ts:80-127,246` | vải tro vẽ canvas, viền vàng, mắt | texture cờ vẽ 256×512 | — | `banner-cloth` (UIC-DH-7) | P1 | — |
| DH-57 | Nhãn "Cắm Cờ" `view/banners.ts:130-152,259` | chữ vẽ canvas | giữ chữ (đổi EN) + icon kỹ năng | `N:aura-attack.64` | — | P1 | VI → EN |
| DH-58 | Thanh máu quái, lính, nhà `view/hpbars.ts:1-25` | quad màu | giữ: đồng hồ đo | — | — | — | — |

### 2.6. Thẻ Ôn, tạm dừng, kết quả, chú thích

| # | Phần tử | Đang hiện | Ảnh cần (720p / 1080p) | Có sẵn | Cần mới | Ưu tiên | Chữ |
|---|---|---|---|---|---|---|---|
| DH-59 | Thẻ Ôn `learning-frame.ts:564,614-651` | bảng CSS; **emoji "🔊"** ở dòng 618; "Đúng! +10 Gold" | icon loa 18 / 26; Gold; bảng | `N:gold.64` | `speaker`; bảng: AD | P1 | VI → EN |
| DH-60 | Menu tạm dừng `app.ts:255-261,340-352` (`app.css:59-98`) | bảng CSS, 3 dòng chữ | bảng; icon tiếp tục, chơi lại, tốc độ 16 / 24 | — | bảng: AD; `retry` (UIC-DH-4); `phase-fight`, `pace-*` dùng chung | P1 | VI → EN |
| DH-61 | Lớp che khi mất tiêu điểm `app.ts:248-250,430` | chữ trên hộp CSS | icon bàn phím | — | `keyboard` | P1 | VI → EN |
| DH-62 | Đếm 3-2-1 `app.ts:252,836` | chữ số lớn | giữ: chữ số bằng font game | — | — | — | — |
| DH-63 | Giữ thắng `results.ts:262-266` (`dh.css:1410-1450`) | chữ "Giữ Ải thành công" | băng rôn thắng vẽ | — | AD | P1 | VI → EN |
| DH-64 | Nền kết quả `results.ts:227-229` (`dh.css:1455-1463`) | radial-gradient | nền vẽ thắng và thua | `art-src/backdrops/pine-river-far*.png` (5,5, AD thay) | AD (chưa có phiếu) | P1 | — |
| DH-65 | 3 sao `results.ts:236-240,295` | SVG `star` | sao sáng/tắt 37 / 55 | — | `star-lit`, `star-unlit` (UIC-DH-4) | P1 | — |
| DH-66 | 5 ô số `results.ts:276-304` | chữ "Gold còn", "Độ chuẩn"… | icon số 20 / 30 | `N:gold.64` | `stat-accuracy`, `stat-new-words`, `stat-words-seen` (UIC-DH-4) | P1 | VI → EN |
| DH-67 | Sổ Từ Ải `results.ts:245-249,306-331` | chữ, viên trạng thái CSS, SVG loa | icon trạng thái 14 / 20; loa | — | `status-learned`, `status-review`, `status-new`, `speaker` | P1 | VI → EN (nghĩa giữ VI) |
| DH-68 | Nút chơi lại, dễ hơn `results.ts:252-255,332-338` | phím + chữ | nút vẽ; icon chơi lại, dễ hơn 16 / 24 | — | nút: AD; `retry`, `easier` (UIC-DH-4) | P1 | VI → EN |
| DH-69 | Chú thích (`title=` gốc của trình duyệt): `hud.ts:242,260,266,277,282,289,294,310,452,469,483`; `wave-card.ts:151,255,273,281,290`; `placement-ui.ts:518,603`; `shop-strip.ts:287`; `results.ts:323` | chú thích trình duyệt, chỉ chữ | thẻ chú thích vẽ có icon món | icon món | thẻ: AD | P2 | VI → EN |

**Ghi chú Dragonhold:**
- **Mặt đất của bản build** cũng là hình tạm (ngoài UI, nhưng người chơi thấy):
  - `src/view/paint.ts:372-375` chỉ nạp ô đất và decal từ `/art-src/` khi chạy dev;
  - bản build chỉ có màu nền của shader.
  - Việc của làn map (MF-C24).
- **Bậc Low** (`?q=low`) vẫn là khối tạm: rồng và quái hình capsule, cây hình nón. Theo luật mới, Low phải dùng model thật bản nhẹ.
- **Màn kết quả có nút "Về cổng game"** ở nhánh `dh-codex` (105b), chưa gộp vào main.

## 3. Wordwoven (`games/typing-defense`, a2-days 999958a)

**Tình hình chung:**
- UI chỉ tải đúng một ảnh: `/assets/typing-defense/ui/title-dusk.webp`.
- Mọi chỗ khác là chữ, emoji, CSS, SVG hay canvas.
- `art-src` có sẵn, chưa dùng: 40 ảnh UI (nhà, tài nguyên, đèn lồng, nhịp, bùa, đồng xu) và 15 chân dung đã chọn.
- Map 2D (`view/debug-2d.ts`, `boss-2d.ts`) vẽ toàn bằng canvas. Trên td-1c, map 3D thay nó. Bản 2D còn lại làm bậc Low và đường lui.

**Màn chưa có:**
- lần đầu chơi và câu hỏi tốc độ (hồ sơ bắt đầu từ mặc định, `app/skill.ts:21`);
- chọn ải, thẻ ải, nạp quân hay cửa hàng riêng;
- thẻ đợt, thẻ ra mắt quái (quái mới chỉ được Bà Cú Mực giới thiệu bằng chữ, `tips.ts:19,23`);
- toast.

**Không rà:** bảng sandbox (`?sandbox=1`, `app/sandbox.ts`). Đó là công cụ dev, người chơi không thấy.

### 3.1. Khởi động và màn tựa

| # | Phần tử | Đang hiện | Ảnh cần (720p / 1080p) | Có sẵn | Cần mới | Ưu tiên | Chữ |
|---|---|---|---|---|---|---|---|
| WW-01 | Dòng nạp `index.html:14` `#tdHud .td-chip` | chữ "Lời Gọi · đang tải từ vựng…" | logo nhỏ 120 / 180 rộng | — | logo AD 113 | P1 | VI → EN |
| WW-02 | Biểu tượng tab `index.html:9` | rỗng (`data:,`) | favicon 32 / 64 | — | cắt từ huy hiệu 113 bằng công cụ | P2 | — |
| WW-03 | Nền màn tựa `title.ts:159,180-185` `.tt-art` (`title.css:8-11`) | ảnh `title-dusk.webp` khi tải được | ảnh chủ đạo sử thi, toàn màn | `WU:title-dusk.png` / webp (chấm 5/10 theo mức chợ) | AD 113 | P1 | — |
| WW-04 | Cảnh SVG dự phòng `title.ts:106-124` `svg.tt-scene` | SVG: trời, 16 sao, mặt trời, núi đá vôi, ruộng bậc, 3 nhà sàn, tre | — | — | **bỏ** | P1 | — |
| WW-05 | Cò bay `title.ts:121` `.tt-storks` (`title.css:22,75`) | nét SVG | — | — | **bỏ** | P1 | — |
| WW-06 | Dây đèn `title.ts:38-45,127-137` `svg.tt-garland .tt-lamp` | 8 đèn SVG gradient và nhòe, nằm trên cả ảnh | — | (`WU:lanterns/*` là icon HUD, không dùng ở đây) | **bỏ**; ảnh 113 tự có ánh sáng | P1 | — |
| WW-07 | Đom đóm `title.ts:160` `i.tt-fly` ×14 (`title.css:23`) | chấm sáng CSS | — | — | **bỏ** (nếu cần, làm hạt VFX theo chuẩn) | P1 | — |
| WW-08 | Tên game `title.ts:161` `h1.tt-name` (`title.css:26-27`, bộ lọc SVG `#tt-brush` ở `title.ts:134`) | chữ Baloo 2 + nhiễu SVG + nét cọ CSS | logo "Wordwoven" 420 / 630 rộng | — | logo AD 113 | P1 | VI → EN |
| WW-09 | Dấu "Văn Điền" `title.ts:161` `.tt-seal` (`title.css:28`) | ô radial-gradient CSS + chữ | — | — | **bỏ** (theme cũ); huy hiệu 113 thay | P1 | VI |
| WW-10 | Phụ đề, gợi ý phím `title.ts:162,164` | chữ | mặt phím vẽ | — | `keycap` (UIC-WW-7) | P1 | VI → EN |
| WW-11 | Bảng menu `title.ts:163` `nav.tt-menu.vd-sheet` (`theme.css:30-31,48`) | giấy CSS (nhiễu SVG data URI) | bảng lớn | — | AD 115 `panel-large` | P1 | — |
| WW-12 | 5 mục menu `title.ts:20-26,163` `.tt-entry` (`title.css:34-44`) | chữ; số trong vòng CSS; mục chọn là dấu son CSS | icon mục 24 / 36; nút đang chọn | — | `menu-start`, `menu-continue`, `menu-settings`, `menu-learn`, `menu-profile` (UIC-WW-5); nút: AD 115 `button-active` | P1 | VI → EN |
| WW-13 | Sao tốt nhất `title.ts:29` `.tt-stars` | ký tự "★☆" | sao sáng/tắt 16 / 20 | — | `star-lit`, `star-unlit` (UIC-WW-2) | P1 | — |

### 3.2. Cài đặt và hồ sơ gõ

| # | Phần tử | Đang hiện | Ảnh cần (720p / 1080p) | Có sẵn | Cần mới | Ưu tiên | Chữ |
|---|---|---|---|---|---|---|---|
| WW-14 | 3 hàng âm lượng `settings.ts:94-95` (`title.css:49-53`) | chữ + thanh "thanh tre" CSS + số | icon âm lượng 20 / 24; thanh trượt | — | `vol-master`, `vol-music`, `vol-effects` (UIC-WW-5) | P2 | VI → EN |
| WW-15 | Công tắc nhịp và chế độ `settings.ts:96-99` (`title.css:56-60`) | viên chữ "Bật/Tắt", "‹ Cân bằng ›" | icon chế độ 20 / 24 | — | `mode-relax`, `mode-learn`, `mode-balanced`, `mode-challenge` (UIC-WW-6) | P2 | VI → EN |
| WW-16 | Nút Xong `settings.ts:100` `button.vd-seal` (`theme.css:39-45`) | dấu son CSS | nút vẽ | — | AD 115 `button` | P2 | VI → EN |
| WW-17 | 5 số hồ sơ `profile.ts:30-39` (`title.css:65-71`) | chữ trong hộp CSS gạch | icon số 20 / 24 | — | `stat-speed`, `stat-accuracy`, `stat-new-word`, `stat-evenness` (UIC-WW-5); `mode-balanced` | P2 | VI → EN |

### 3.3. HUD trạng thái và dải chữ

| # | Phần tử | Đang hiện | Ảnh cần (720p / 1080p) | Có sẵn | Cần mới | Ưu tiên | Chữ |
|---|---|---|---|---|---|---|---|
| WW-18 | Dòng tên `hud.ts:55` `.td-title` | chữ "Lời Gọi · Bản đồ 1…" | logo nhỏ 90 / 110 rộng | — | logo AD 113 | P1 | VI → EN |
| WW-19 | Tạm dừng, tắt tiếng `hud.ts:56` `.td-x` | ký tự "Ⅱ"/"▶"; chữ "Âm" gạch ngang khi tắt | icon 16 / 20 | — | `pause`, `play`, `sound-on`, `sound-off` (UIC-WW-3) | P1 | VI → EN |
| WW-20 | 5 ô tài nguyên `hud.ts:42,57` `.td-stat` | nhãn chữ + số, không icon | icon 20 / 24 | `WU:resources/gold`, `wood`, `food` (Rice), `lives` (kiểu cũ, nền khóa) | `seeds` (UIC-WW-3) | P1 | VI → EN ("Mạng" → Lives) |
| WW-21 | Mất mạng `hud.ts:53` `.td-hit` | chữ "−3" | icon Lives nháy 20 / 24 | `WU:resources/lives` | — | P1 | — |
| WW-22 | Dòng pha `hud.ts:52,58` `.td-phase` | chữ "Ngày 2 · 0:41", "Đêm 2 · còn 12 quái" | icon ngày, đêm 20 / 24 | `WU:resources/wave` (số quái) | `day`, `night` (UIC-WW-3) | P1 | VI → EN |
| WW-23 | Dòng học `hud.ts:59` `.td-learn` | chữ "Knowledge", "Sổ ôn" | icon 16 / 20 | `WU:resources/knowledge` | `review-book` (UIC-WW-3) | P1 | VI → EN |
| WW-24 | Gọi đêm sớm `hud.ts:69-71` `.td-call` (`td.css:73-83`) | chữ trên dấu son CSS + thanh giờ CSS | icon gọi đêm 24 / 29 + Gold; khung thanh | `WU:resources/gold` | `night-call` (UIC-WW-3); khung: AD 115 | P1 | VI → EN |
| WW-25 | Dòng báo, thua `hud.ts:60-61` `.td-warn`; `main.ts:300-307` | chữ | icon cảnh báo 16 / 20 + icon tài nguyên | tài nguyên | `warning` (UIC-WW-3) | P1 | VI → EN |
| WW-26 | Bảng dải chữ `td.css:36-37` `.td-strip` | trục tre gradient CSS trên giấy CSS | dải vẽ | — | AD 115 `plate-long` | P1 | — |
| WW-27 | Từ, nghĩa, lý do từ chối `hud.ts:78-91`; `REASON` `hud.ts:25-34` | chữ | icon lý do 16 / 20 (thiếu Gold/Wood, khóa) | tài nguyên | `lock` (UIC-WW-4) | P1 | VI → EN (nghĩa giữ VI) |
| WW-28 | Chuỗi và 4 chấm `hud.ts:92-93` (`td.css:109-111`) | chữ "Chuỗi n" + chấm CSS | icon chuỗi 16 / 20; chấm vẽ | — | `chain` (UIC-WW-3); `pip-lit`, `pip-unlit` (UIC-WW-7) | P1 | VI → EN |

### 3.4. Thanh đội và nút hành động

| # | Phần tử | Đang hiện | Ảnh cần (720p / 1080p) | Có sẵn | Cần mới | Ưu tiên | Chữ |
|---|---|---|---|---|---|---|---|
| WW-29 | Đầu thanh `team-bar.ts:29` `.td-load` | chữ + viên CSS "Đang gọi n/N" | icon đang gọi 16 / 20 | — | `night-call` dùng chung | P1 | VI → EN |
| WW-30 | Chân dung `team-bar.ts:26` `button.td-agent` (`td.css:89-97`) | **đĩa chữ cái**: đèn lồng CSS màu nhân vật, chữ "D", "C", "P", "G" (`slice-1a.ts:151,154-156`) | chân dung trong vòng 54 / 65 | `WP:draconis.png`, `helper-cham-happy/-scared`, `helper-phay-*`, `helper-gach-*` (kiểu cũ, nền G) | vòng: AD 115 `portrait-ring` | P1 | — |
| WW-31 | Số thứ tự `team-bar.ts:26` `<i>` (`td.css:93-94`) | viên CSS + số | mặt phím nhỏ | — | `keycap` (UIC-WW-7) | P1 | — |
| WW-32 | Nơi được cử tới `team-bar.ts:22` `<em>` (`td.css:95`) | viên CSS: "Fort", **emoji "🏹", "🧨"**, chữ "L", "M", "R" (`slice-1a.ts:36,50,64,76,81,83`) | icon nhà 20 / 24 | `WU:buildings/keep`, `archer.alpha`, `cannon`, `barracks.trim`, `gold-mine`, `farm` | — | P1 | EN |
| WW-33 | Vòng nạp Tối Thượng `team-bar.ts:25` `.td-ult` (`td.css:99-101`) | vòng conic CSS | giữ phần đo; khung vòng vẽ | — | AD 115 `portrait-ring` | P1 | — |
| WW-34 | Ô khóa `team-bar.ts:20` `.is-locked` (`td.css:103`) | sọc CSS + chữ cái + "Fort n" | bóng chân dung + icon khóa | — | `lock` (UIC-WW-4) | P1 | VI → EN |
| WW-35 | Nút Xây, Thuê Villager, Tối Thượng, Tạm dừng `hud.ts:97-103` (`td.css:43,102`) | nút chữ + gợi ý phím; dấu son hay gradient hổ phách | icon nút 24 / 29 | — | `build`, `hire-villager`, `ultimate` (UIC-WW-4); `pause` | P1 | VI → EN |

### 3.5. Menu xây và thẻ nhà

| # | Phần tử | Đang hiện | Ảnh cần (720p / 1080p) | Có sẵn | Cần mới | Ưu tiên | Chữ |
|---|---|---|---|---|---|---|---|
| WW-36 | Đầu, chân menu `build-menu.ts:20,97` | chữ, "×" | icon đóng 16 / 20 | — | `close` (UIC-WW-3) | P1 | VI → EN |
| WW-37 | 5 hàng nhà `build-menu.ts:91-95` `.td-kind` (`td.css:113-115`) | chữ: số, tên, "70 Gold · 160 Wood", "Mở ở Ngày n"; không icon | icon nhà 28 / 34 + Gold, Wood | `WU:buildings/archer.alpha`, `cannon`, `barracks.trim`, `gold-mine`, `farm`; `WU:resources/gold`, `wood` | — | P1 | VI → EN |
| WW-38 | Dòng "làm gì" `build-menu.ts:25`; `tips.ts:29-35` | chữ | icon tài nguyên trong dòng | tài nguyên | `seeds` | P1 | VI → EN |
| WW-39 | Đầu thẻ nhà, công trường `build-menu.ts:52,64` | chữ "Cấp n", "Đang xây n % · chờ Builder" | icon nhà; chấm cấp; icon Builder | icon nhà | `level-pip-lit`, `level-pip-unlit` (UIC-WW-4); `builder` (UIC-WW-8) | P1 | VI → EN |
| WW-40 | Ruộng `build-menu.ts:41-45,57-58` | chữ "Chín 1 · Lớn 2 · Trống 1" + Seeds | icon trạng thái ruộng 20 / 24 | (`scenery/meadow/rice/*` là ô đất, không phải icon) | `rice-ripe`, `rice-growing`, `rice-empty` (UIC-WW-8); `seeds` | P1 | VI → EN |
| WW-41 | Thẻ Fort `build-menu.ts:28-38,59-60` | chữ đếm + nút thuê, bán, nâng; "Mở: Chấm" | icon Fort, Villager, Builder, bán, nâng; chân dung Chấm | `WU:buildings/keep`, `WP:helper-cham-happy` | `villager`, `builder` (UIC-WW-8); `sell`, `upgrade` (UIC-WW-4) | P1 | VI → EN |
| WW-42 | Lượt mạnh của tháp `build-menu.ts:61` | chữ "Lượt mạnh 3/5" | 5 đèn lồng 16 / 20 | `WU:lanterns/lantern-unlit`, `lantern-lit`, `lantern-blazing` (vẽ cho đúng chỗ này) | — | P1 | VI → EN |
| WW-43 | Nút gửi, hoàn tác, bán, nâng `build-menu.ts:55,65-70` | nút chữ, vài dấu son CSS | icon nút 16 / 20; chân dung nhân vật | chân dung | `send`, `undo`, `sell`, `upgrade` (UIC-WW-4) | P1 | VI → EN |

### 3.6. Thẻ gọi và thẻ chữ

| # | Phần tử | Đang hiện | Ảnh cần (720p / 1080p) | Có sẵn | Cần mới | Ưu tiên | Chữ |
|---|---|---|---|---|---|---|---|
| WW-44 | Đầu thẻ gọi `build-menu.ts:78-85`; `cards.ts:30-34` | emoji + tên, ví dụ "🌾 Gặt" | icon lời gọi 20 / 24 | — | 10 icon `call-*` (UIC-WW-1) | P1 | VI → EN |
| WW-45 | Thân thẻ chữ `cards.ts:89` `.td-card` (`td.css:151`) | "đèn lồng giấy" CSS: gradient, viền tre | đế thẻ 9-slice cao 34 / 37 | — | `card-plate`, `card-plate-review` (UIC-WW-7); chuyển cho AD nếu AD nhận | P1 | — |
| WW-46 | Icon loại `cards.ts:27,33,136` `data-icon` → `td.css:159` `::before` | **emoji "🏹 🔨 🌾 🪓 ⛏️ 📖 🔥 ✋", "⚓", "🛡️"** | icon lời gọi 18 / 24 | — | 10 icon `call-*` (UIC-WW-1) | P1 | — |
| WW-47 | Chấm và nghĩa `cards.ts:47,139` | ký tự "●○"; chữ | chấm vẽ 8 / 10 | — | `pip-lit`, `pip-unlit` | P1 | nghĩa giữ VI |
| WW-48 | Chấm nhân vật, đồng hồ, đồng hồ lời trực tiếp `td.css:171-181` | vòng CSS, thanh, vòng conic, viền đôi | chân dung nhỏ 16 / 20; giữ đồng hồ | chân dung `WP:` | — | P1 | — |
| WW-49 | Nhãn ôn `td.css:168` `.is-review::after` | viên CSS chữ "Ôn" | icon sổ ôn 14 / 18 | — | `review-book` | P1 | VI → EN |
| WW-50 | Tem hạng `cards.ts:24,93,118` `.td-stamp` (`td.css:183-187`) | chữ "Chớp / Hoàn hảo / Tốt / Vừa / Ẩu / Chuộc lại" trong dấu tròn CSS | tem hạng 36 / 44 (hình, không chữ; chữ EN đặt bằng font) | — | 6 `grade-*` (UIC-WW-2); đế dấu `stamp-seal` (UIC-WW-7) | P1 | VI → EN |

### 3.7. Boss, dạy, tạm dừng, kết quả, chú thích

| # | Phần tử | Đang hiện | Ảnh cần (720p / 1080p) | Có sẵn | Cần mới | Ưu tiên | Chữ |
|---|---|---|---|---|---|---|---|
| WW-51 | Thanh boss `hud.ts:195-218` `.td-boss` | chữ "Mộc Tinh", pha, "còn n m tới Fort"; không chân dung | chân dung boss 48 / 58 | `WP:moc-tinh.crop.png` (1024², kiểu cũ) | — | P1 | VI → EN |
| WW-52 | Máu boss `hud.ts:213-215` `.td-bar` (`td.css:122-132`) | thanh CSS, vạch 70 % và 50 % | khung thanh vẽ; vạch pha | — | AD 115; vạch dùng `pip-*` | P1 | VI → EN ("rút lui") |
| WW-53 | Lời boss `hud.ts:155-162,198` `.td-say` | chữ trong viên mực CSS | chân dung nhỏ 24 / 29 | `WP:moc-tinh.crop.png` | — | P1 | VI → EN |
| WW-54 | Khung dạy, lời Bà Cú Mực `hud.ts:187-192`; `tips.ts:15-26` (`td.css:135-141`) | chỉ chữ, không chân dung | chân dung người kể 40 / 48 | `WP:narrator.png` | — | P1 | VI → EN |
| WW-55 | Thẻ tạm dừng `sheets.ts:25,93` (`td.css:193-200`; `theme.css:48-50`) | giấy CSS, gạch cọ CSS, 3 nút chữ | bảng; icon tiếp tục, cài đặt, về màn đầu 20 / 24 | — | bảng: AD 115; `play`, `menu-settings`, `close` dùng chung | P1 | VI → EN |
| WW-56 | Đầu thẻ kết, câu truyện, gợi ý thua `sheets.ts:37-48,94-95` | chữ | huy hiệu thắng/thua | — | AD 115 `crest` | P1 | VI → EN |
| WW-57 | Sao và kỷ lục `sheets.ts:29,94` (`td.css:203-209`) | ký tự "★" ×3, hoạt cảnh dấu CSS | sao 28 / 34; dải kỷ lục | — | `star-lit`, `star-unlit`, `record-ribbon` (UIC-WW-2, -6) | P1 | VI → EN |
| WW-58 | Số, từ ôn, nút `sheets.ts:80-98` | chữ | icon số 20 / 24 | `WU:resources/lives`, `gold`, `knowledge`; `WU:loot/coin-*` | `stat-nights`, `stat-foes`, `stat-words` (UIC-WW-6); `grade-perfect` | P1 | VI → EN |
| WW-59 | Chú thích `title=`: `hud.ts:56,93`; `build-menu.ts:20`; `team-bar.ts:20,22,25,26,29` | chú thích trình duyệt | thẻ chú thích có icon | icon nhà, chân dung | AD 115 `tooltip` | P2 | VI → EN |

### 3.8. Map 2D (cảnh trận trên a2-days; bậc Low khi 1C xong)

| # | Phần tử | Đang hiện | Ảnh cần | Có sẵn | Cần mới | Ưu tiên | Chữ |
|---|---|---|---|---|---|---|---|
| WW-60 | Nhà `view/debug-2d.ts:486-537` | đĩa canvas + chữ "Fort", **emoji "🏹", "🧨"**, "L", "M"; vạch cấp; 5 đĩa lượt; cờ Path2D | 3D ở 1C; bậc Low: icon nhà 32 / 40 | `WU:buildings/*` | — | P1 | EN |
| WW-61 | Người làm `debug-2d.ts:51,531,540-552` | đĩa + **emoji "🌾 🪓 🔨 ⛏️"** | 3D ở 1C; Low: icon người làm 24 / 29 | — | `farmer`, `villager`, `builder`, `miner` (UIC-WW-8) | P1 | — |
| WW-62 | Thư Đồng, Draconis `debug-2d.ts:59,715-750` | **đĩa chữ cái** C, P, G; Draconis là tam giác có cánh Path2D | 3D ở 1C; Low: chân dung | `WP:draconis`, `helper-*` | — | P1 | — |
| WW-63 | Lính, quái `debug-2d.ts:632-702` | đĩa màu, ánh quái bay, cờ đuôi nheo, vòm, "★ ★", "×1,3" | 3D ở 1C; Low: chân dung quái 24 / 29 | nguồn cắt: `art-src/enemies/*` | 9 chân dung (UIC-WW-9); `soldier` (UIC-WW-8) | P1 | VI → EN |
| WW-64 | Mộc Tinh, Sapling `view/boss-2d.ts:241-256,310-400` | tán, mắt, chân rễ vẽ canvas (dòng 2 tự ghi "placeholder in ink") | 3D ở 1C; Low: chân dung | `WP:moc-tinh.crop` | `sapling` (UIC-WW-9) | P1 | — |
| WW-65 | Bong bóng lời gọi khi tối, mũi tên mép `debug-2d.ts:560-611` | roundRect canvas + emoji (dòng 602) + "●○" (604); tam giác | icon lời gọi + chấm; 3D chưa có bong bóng (C10) | — | `call-*`, `pip-*` | P1 | — |
| WW-66 | Chân dung Tối Thượng `view/fx-pipe.ts:149-189` | đầu rồng vẽ canvas trên thẻ giấy + "Tối Thượng!" | ảnh DOM, khoảng 420×280 / 630×420 | `WP:draconis-ult.png` (1536×1024 RGBA) | — | P1 | VI → EN |
| WW-67 | Số bay `debug-2d.ts:414,455,819-830`; `boss-2d.ts:237,295,390,395,426`; `fx-pipe.ts:132-144` | chữ canvas "+n", "−3 mạng", "Cháy ×1,25", "Tê n s", "Đứng sững!", "Vỡ vòm!", "✦", "★" | giữ chữ (VFX); icon trạng thái 16 / 20 | `WU:resources/lives` | `status-burn`, `status-stun` (UIC-WW-8) | P1 | VI → EN |
| WW-68 | Cảnh 2D `debug-2d.ts:229-458` | ruộng, làng, ao, hàng rào, mái, suối, đường, tre vẽ canvas | 3D ở 1C; Low: ô đất | `public/assets/typing-defense/ground/*.webp` (095, 097) | — | P1 | — |

## 4. Last Line (`games/typing-survival`, main e26e898)

**Tình hình chung:**
- Game không tải ảnh nào. Không có `<img>`, `url()` hay `TextureLoader` cho ảnh. Chỉ tải model Space và font.
- `public/` chỉ có `vocabulary/`. Không có `public/assets/typing-survival/`.
- `art-src/ui/title-horizon.png` chưa dùng.
- Ảnh đã nhận, chưa dùng:
  - 088: vỏ trạm, lớp xa, decal sàn;
  - 089: 6 chân dung quái;
  - 108: icon súng chuẩn hóa. Báo cáo 108 ghi chưa đạt hết KA3 và KA4; Claude chấm lại trước khi gắn;
  - 109: 4 ảnh ải, chờ Claude chấm lại.
- **Hướng mỹ thuật Last Line chưa chốt.** Phiếu 112 có ba hướng; chủ dự án có thể bỏ tàu vũ trụ.
  - Icon súng và chân dung quái có thể phải vẽ lại theo hướng mới.
  - Vẫn nên gắn ảnh có sẵn ngay. Việc gắn rẻ và lấp đúng ví dụ 2, 3 của chủ dự án. Đổi hướng thì chỉ thay file, giữ tên.

**Màn chưa có:**
- lần đầu chơi và câu hỏi tốc độ;
- cửa hàng (game không có tiền);
- nút kỹ năng (Nova thuộc S2);
- thanh boss (boss ở R3);
- chữ trên quái: chữ nằm ở bến, đúng thiết kế.

### 4.1. Khởi động và màn chính

| # | Phần tử | Đang hiện | Ảnh cần (720p / 1080p) | Có sẵn | Cần mới | Ưu tiên | Chữ |
|---|---|---|---|---|---|---|---|
| LL-01 | Dòng nạp `index.html:14` `.sv-loading` | chữ "TUYẾN CUỐI · đang tải…" | logo nhỏ 160 / 240 rộng | — | logo AD 121 | P1 | VI → EN |
| LL-02 | Báo không có WebGL `main.ts:108` `#svHud` | chữ | icon cảnh báo 24 / 36 | — | `warning` (UIC-LL-2) | P2 | VI → EN |
| LL-03 | Biểu tượng tab `index.html:9` | rỗng (`data:,`) | favicon 32 / 64 | — | cắt từ logo 121 | P2 | — |
| LL-04 | Thẻ điều khiển `screens.ts:65` `.sv-card.sv-panel.sv-title-card` (`survival.css:16-25,178`; `theme.css:96-99`) | tấm thép CSS: gradient chải, 4 đinh radial-gradient, vát cạnh | bảng 9-slice vẽ 520 / 780 rộng | — | AD (chưa có phiếu khung Last Line) | P1 | — |
| LL-05 | Nhãn trạm + chấm `screens.ts:66` `.sv-title-tag`, `.sv-dot` (`survival.css:179-180`) | chữ "TRẠM VC-7 · VÀNH CHÂN TRỜI" + chấm CSS nhấp nháy | huy hiệu trạm 20 / 30; bỏ chấm | — | `station-crest` (UIC-LL-2) | P1 | VI → EN |
| LL-06 | Tên game `screens.ts:67` `h1.sv-title-name` (`survival.css:181`) | chữ "TUYẾN CUỐI" 72 px, phát sáng CSS | logo "Last Line" 520 / 780 rộng | — | logo AD 121 | P1 | VI → EN |
| LL-07 | Phụ đề "LAST LINE" `screens.ts:68` | chữ | — | — | **bỏ** (logo mang tên) | P1 | EN |
| LL-08 | Vạch nguy hiểm `.sv-hazard` (`survival.css:26`; `theme.css:100`; `screens.ts:69,79,88,100,111,120,129`; `screens-journey.ts:53,63,86`) | sọc gradient CSS dưới mọi tiêu đề | dải vẽ, hoặc bỏ | — | AD | P1 | — |
| LL-09 | Menu 7 mục `main.ts:226-235`; thành phần `screens.ts:39-56` `.sv-item` (`survival.css:191-207`) | chữ + đèn LED CSS; giá trị giữa "◀ ▶" | icon mục 24 / 36; đèn; mũi tên | — | `menu-play`, `menu-journey`, `menu-mode`, `menu-armory`, `menu-settings`, `menu-profile` (UIC-LL-3); `led-on`, `led-off`, `arrow` (UIC-LL-5) | P1 | VI → EN |
| LL-10 | Dòng trạng thái `screens.ts:72`; `main.ts:283` | chữ "TÀU VANGUARD · HÌNH …" | ảnh tàu nhỏ 32 / 48 | — | Claude dựng ảnh từ GLB Vanguard và Draconis (không cần Codex) | P1 | VI → EN |
| LL-11 | Gợi ý phím `screens.ts:73` `.sv-hints kbd` (`survival.css:174`) | chữ trong phím CSS | mặt phím vẽ | — | `keycap`, `keycap-active` (UIC-LL-5) | P1 | VI → EN |
| LL-12 | Nền màn chính: cảnh 3D (`scene.ts:55-57,391-395`) + màn che CSS (`survival.css:169`) | hành lang vẽ bằng mã + shader hố đen + gradient | ảnh nền màn chính | `art-src/ui/title-horizon.png` (lệch kiểu, P3) | AD 121 `menu-bg` | P1 | — |

### 4.2. Cài đặt, hồ sơ, kho súng

| # | Phần tử | Đang hiện | Ảnh cần (720p / 1080p) | Có sẵn | Cần mới | Ưu tiên | Chữ |
|---|---|---|---|---|---|---|---|
| LL-13 | Bảng và 9 hàng `screens.ts:76-84`; `main.ts:236-249` | tấm CSS; chữ; thanh LED CSS; "Tàu: Vanguard/Draconis" chữ | icon hàng 20 / 30; ảnh tàu | — | 7 icon (UIC-LL-4); ảnh tàu như LL-10 | P2 | VI → EN |
| LL-14 | 4 ô hồ sơ `screens.ts:97-107` (`survival.css:268-271`); `results.ts:71-76` | chữ trong ô CSS | icon số 24 / 36 | — | `stat-wpm`, `stat-new-word`, `stat-evenness` (UIC-LL-4); `stat-accuracy` (UIC-LL-3) | P2 | VI → EN |
| LL-15 | 5 thẻ súng ở kho `screens.ts:90`; `main.ts:293` (`survival.css:211-215`) | chỉ chữ, viền trên màu súng | icon súng 64 / 96 | `LI:gun-xung`, `gun-tia`, `gun-tan`, `gun-ray`, `gun-phao-sao` `.norm.{64,128,256}` (108) | — | P2 | VI → EN |

### 4.3. Hành trình, thẻ ải

| # | Phần tử | Đang hiện | Ảnh cần (720p / 1080p) | Có sẵn | Cần mới | Ưu tiên | Chữ |
|---|---|---|---|---|---|---|---|
| LL-16 | Đầu Hành trình `screens-journey.ts:51-53` | chữ "CHƯƠNG 1 · HÀNH LANG VC-7" + sọc CSS | huy hiệu chương 32 / 48 | — | `chapter-crest` (UIC-LL-2); nền: AD 121 `journey-bg` | P1 | VI → EN |
| LL-17 | 4 hàng ải `journey.ts:120-126` → `screens-journey.ts:54` | chữ "Ải 1 · Ca trực đầu ★★☆"; ải khóa ghi "Qua ải n để mở"; không ảnh | ảnh nhỏ 96×54 / 144×81; sao; khóa | `LS:c1-s1…c1-s4.png` (109, chờ chấm) | `star-lit`, `star-unlit` (UIC-LL-3); `lock` (UIC-LL-1) | P1 | VI → EN |
| LL-18 | Tiêu đề thẻ ải `screens-journey.ts:62` | chữ "ẢI 1 · CA TRỰC ĐẦU" | băng ảnh ải 760×120 / 1140×180 | `LS:c1-s1.png` | — | P1 | VI → EN |
| LL-19 | Luật `screens-journey.ts:64-69` `dl.sv-brief-rules` | chữ: Mục tiêu, Hiểm họa, Luật học, Trang bị | icon luật 20 / 30 | — | `objective`, `hazard`, `learning-rule`, `equipment` (UIC-LL-2) | P1 | VI → EN |
| LL-20 | Danh sách quái `screens-journey.ts:70-72` `ul.sv-foes li` (`survival.css:225-231`) | chữ; "MỚI" là viên CSS; không chân dung | chân dung 40 / 60; huy hiệu mới | `LF:swarm`, `scout`, `brute` (089) | `new-badge` (UIC-LL-2) | P1 | VI → EN |
| LL-21 | Ghi chú dạy `screens-journey.ts:73` | chữ "Ải này dạy: quái Brute." | chân dung Brute 32 / 48 | `LF:brute.png` | — | P1 | VI → EN |
| LL-22 | Hàng nút `journey.ts:136-139` | chữ "Nạp súng", "Quay lại" | icon 20 / 30 | — | `load-guns`, `back` (UIC-LL-2) | P1 | VI → EN |
| LL-23 | Nền thẻ ải | cảnh 3D tối + màn che CSS | ảnh nền thẻ ải | — | AD 121 `briefing-bg` | P1 | — |

### 4.4. Nạp súng (ví dụ 2 của chủ dự án) và thẻ ải trước trận

| # | Phần tử | Đang hiện | Ảnh cần (720p / 1080p) | Có sẵn | Cần mới | Ưu tiên | Chữ |
|---|---|---|---|---|---|---|---|
| LL-24 | Nền "Nạp súng" `screens-journey.ts:83-86` `.sv-loadout` (`survival.css:167,220`) | tấm CSS trên cảnh màn chính mờ; **không có nền vẽ** | ảnh nền kho súng | — | AD 121 `loadout-bg` | P1 | VI → EN |
| LL-25 | 5 thẻ súng `screens-journey.ts:91-97` `section.sv-gun-card` (`survival.css:232-244`) | **chỉ chữ**: số trong phím, tên, nhãn CSS "BẾN n", mô tả, "khắc:", "kém:" | icon súng 72 / 108 ở đầu thẻ | `LI:*.norm.256` / `.norm.128` (108) | — | P1 | VI → EN |
| LL-26 | Dòng khắc, kém trong thẻ | chữ liệt kê quái | chân dung nhỏ 20 / 30 | `LF:swarm`, `scout`, `brute`, `pack-leader`, `shield-guard`, `splitter` | `shard` (UIC-LL-2) | P1 | VI → EN |
| LL-27 | Chip mối nguy `screens-journey.ts:101-103` `.sv-threats span` | chữ + "⚠" | chân dung nhỏ + icon cảnh báo 16 / 24 | `LF:*` | `warning` | P1 | VI → EN |
| LL-28 | Nút bắt đầu `screens-journey.ts:104-107` `.sv-start` | chữ "BẮT ĐẦU · CÒN ⚠" | nút vẽ + icon cảnh báo | — | nút: AD; `warning` | P1 | VI → EN |
| LL-29 | Thẻ ải trước trận `screens.ts:116-125` `.sv-intro`; `main.ts:301-307` | chữ "Trụ vững 2:30", "Pulse Gun · Heat Beam", "NHẤN PHÍM BẤT KỲ…" | ảnh ải 384×216 / 576×324 + 2 icon súng 48 / 72 | `LS:c1-s1.png`; `LI:*.norm.128` | — | P1 | VI → EN |

### 4.5. HUD trận (ví dụ 3 của chủ dự án)

| # | Phần tử | Đang hiện | Ảnh cần (720p / 1080p) | Có sẵn | Cần mới | Ưu tiên | Chữ |
|---|---|---|---|---|---|---|---|
| LL-30 | Giáp `hud.ts:130-134` `.sv-hp` (`survival.css:36-42`) | chữ "GIÁP" + thanh gradient CSS | icon giáp 20 / 30; khung thanh | — | `armour` (UIC-LL-1); khung: AD | P1 | VI → EN |
| LL-31 | Đồng hồ `hud.ts:135-139` `.sv-clock` | số LED chữ, "còn lại" | icon đồng hồ 20 / 30 | — | `clock` (UIC-LL-1) | P1 | VI → EN |
| LL-32 | Bảng mục tiêu `hud.ts:140-141,358-368` `.sv-goal` (ẩn ở c1-s1) | chữ | chân dung Pack Leader + icon mục tiêu | `LF:pack-leader` | `objective` | P2 | VI → EN |
| LL-33 | Số hạ `hud.ts:142-145,272-278` `.sv-kills` | chữ "×N", "hạ / 3 s", "Tổng N" | icon hạ 20 / 30 | — | `kills` (UIC-LL-1) | P1 | VI → EN |
| LL-34 | Băng rôn `hud.ts:146,239-243,269,363`; `main.ts:179,189,548` `.sv-banner` | chữ trên dải CSS viền sọc: "ẢI 1 · CA TRỰC ĐẦU", "ĐỈNH TRÀN n", "TIẾP TẾ +20 GIÁP", "VƯỢT ẢI!" | đế băng rôn; icon đợt tràn, tiếp tế 28 / 42 | — | đế: AD; `surge`, `repair-pod` (UIC-LL-1) | P1 | VI → EN |
| LL-35 | Thẻ ra mắt quái `hud.ts:56-61,395-409` `.sv-fresh` (`survival.css:71-72`) | chỉ chữ "MỚI · BRUTE · VỎ 4" | chân dung 48 / 72 + huy hiệu mới | `LF:brute.png` | — | P1 | VI → EN |
| LL-36 | Báo Rift `hud.ts:148,371-392` `.sv-warn` (không có ở c1-s1) | "⚠ Rift · n s" trên tấm cam CSS | icon Rift 24 / 36 | — | `rift` (UIC-LL-4) | P2 | VI → EN |
| LL-37 | Dòng báo nhập `hud.ts:149,245-248`; `main.ts:605`; `.sv-notice::before` "⌨ " (`survival.css:59-60`) | chữ + ký tự "⌨" | icon bàn phím 16 / 24 | — | `keyboard` (UIC-LL-1) | P1 | VI → EN |
| LL-38 | Tấm bến 1–2 `hud.ts:164-173` `section.sv-slot` (`survival.css:83-119`) | tấm CSS + sọc nạp gradient | khung bến vẽ; giữ phần nạp | — | AD | P1 | — |
| LL-39 | **Tên súng ở bến** `hud.ts:168` `span.sv-gun` (`survival.css:90`) | **chỉ chữ, không hình súng** | icon súng 40 / 60 ở đầu bến | `LI:*.norm.64` / `.norm.128` (108) | — | P1 | EN |
| LL-40 | Đèn băng đạn `hud.ts:169-172,323-336` `.sv-mags i` (`survival.css:93-98`) | ô CSS có mặt nạ gradient | ô đạn vẽ rỗng/đầy 10 / 15 | — | `mag-empty`, `mag-full` (UIC-LL-5) | P1 | — |
| LL-41 | Bến khóa 3–4 `hud.ts:156-161` `.sv-bay-lock` + `i.sv-lock` (`survival.css:108-110`) | **ổ khóa vẽ bằng CSS** + chữ "MỞ Ở MỐC" | icon khóa 24 / 36 | — | `lock` (UIC-LL-1) | P1 | VI → EN |
| LL-42 | Dòng chữ `strip.ts:86-92` `.sv-strip` (`survival.css:122-132,150`) | chữ trên tấm CSS | dải vẽ | — | AD | P1 | — |
| LL-43 | Dòng xong `strip.ts:90,170-200` `.sv-strip-done` | chữ "word · nghĩa ✓", "ĐẦY" | icon đúng, icon bến đầy 16 / 24 | — | `check`, `bay-full` (UIC-LL-1) | P1 | VI → EN (nghĩa giữ VI) |
| LL-44 | Chuỗi sạch, đếm Rift, vạch quái gần `strip.ts:93-97` | chữ "SẠCH ×N", "◀ Rift · n s"; thanh CSS | icon chuỗi 16 / 24; icon Rift | — | `streak` (UIC-LL-1); `rift` | P1 | VI → EN |
| LL-45 | Số sát thương `combat.ts:60-61` → `kit/feedback/numbers.ts:356-401` | atlas chữ số vẽ canvas; nhãn "HOÀN HẢO" (`profiles.ts:51`) | giữ: chữ số là VFX | — | — | — | VI → EN |
| LL-46 | Sân 3D `scene.ts:101-171,344-388` | sàn shader, tấm, trụ, đèn, lan can, vòm dựng bằng hình khối | vỏ trạm, lớp xa, decal sàn | `art-src/arena/hull-left`, `hull-right`, `far-structures`, `deck-decals` (088) | — (TS-M1-07, -08) | P1 | — |
| LL-47 | Shader hố đen `scene.ts:180-239` | shader | giữ shader; thêm lớp xa 088 | `far-structures.png` | — | — | — |

### 4.6. Tạm dừng, kết quả, chú thích

| # | Phần tử | Đang hiện | Ảnh cần (720p / 1080p) | Có sẵn | Cần mới | Ưu tiên | Chữ |
|---|---|---|---|---|---|---|---|
| LL-48 | Tạm dừng `screens.ts:108-115`; `main.ts:253-258` | tấm CSS, sọc, 3 dòng chữ | bảng; icon tiếp tục, chơi lại, menu 20 / 30 | — | bảng: AD; `menu-play`, `retry` (UIC-LL-3); `back` | P1 | VI → EN |
| LL-49 | Đầu kết quả `screens.ts:128-129` `.sv-end` | chữ | nền thắng/thua | — | AD 121 `results-win-bg`, `results-lose-bg` | P1 | VI → EN |
| LL-50 | Hàng sao `screens-journey.ts:118-121` `ul.sv-star-row` (`survival.css:255-258`) | ký tự "★ / ☆" | sao 28 / 42 | — | `star-lit`, `star-unlit` (UIC-LL-3) | P1 | — |
| LL-51 | Số kết quả `screens.ts:131`; `results.ts:13-23` `.sv-stats` | chữ trong ô CSS | icon số 24 / 36 | — | `stat-time`, `stat-accuracy` (UIC-LL-3); `kills`; `stat-wpm` | P1 | VI → EN |
| LL-52 | Từ đã học `screens.ts:135-136` `ul.sv-words` | chữ | icon từ mới | — | `new-badge`; `check` | P1 | VI → EN (nghĩa giữ VI) |
| LL-53 | Hàng nút cuối `main.ts:259-270` `.sv-row` | chữ "Ải 2 · Săn Pack Leader" | ảnh nhỏ ải kế 96×54 / 144×81 + icon | `LS:c1-s2.png` | `retry`, `next-stage` (UIC-LL-3) | P1 | VI → EN |
| LL-54 | Chú thích `title=` trên chip mối nguy `screens-journey.ts:102` | chú thích trình duyệt | thẻ chú thích có chân dung | `LF:*` | thẻ: AD | P2 | VI → EN |

## 5. Hình vẽ bằng mã người chơi thấy: gỡ hay thay

Luật mới: không hình nào người chơi thấy được vẽ bằng mã để thay ảnh thật. Shader và VFX đạt `VFX_STANDARD.md` thì giữ. Bảng dưới gom mọi chỗ đã thấy, kể cả chỗ không nằm trong UI.

### 5.1. Dragonhold

| Chỗ | Hình vẽ bằng mã | Thay bằng |
|---|---|---|
| `src/ui/skin.ts:127-184` | 30 icon SVG `ICONS` và bóng quái `foeIcon` | ảnh (mục 2); bóng quái thay bằng chân dung UIC-DH-7, tạm thời bằng `family-*` |
| `src/ui/tags.ts:473-488` | 11 icon SVG trên thẻ chữ | ảnh (DH-47) |
| `src/ui/learning-frame.ts:181,325,618` | SVG loa, ký tự "✓", emoji "🔊" | `speaker`, `check` |
| `src/app/pace-card.ts:52-57` | ký tự "⇧↵" làm icon | `keycap` |
| `src/ui/styles/dh.css:67-86` | bảng "gỗ khắc": vân lặp, ánh radial, vát | khung vẽ của AD |
| `dh.css:88-104` | 6 bụi rêu radial-gradient trên mép bảng | **bỏ ngay**; khung AD có mép riêng |
| `dh.css:107-118` | búi rêu góc dưới trái | **bỏ ngay** |
| `dh.css:138-151` | mặt phím gradient | `keycap` |
| `dh.css:169-200` | nút gỗ gradient | nút của AD |
| `dh.css:349-374` | đĩa chân dung, đĩa cấp | chân dung UIC-DH-6, `level-badge` |
| `dh.css:447-508,618-650` | thanh máu và Rage gradient, sọc khiên | khung thanh AD; phần đầy giữ |
| `dh.css:1170-1243` | đĩa ô đặt và chấm cấp | `slot-*`, `pip-*` |
| `dh.css:1455-1463` | nền kết quả radial | nền AD |
| `tags.ts:495-501,543` | hộp thẻ chữ, tam giác mép | `tag-plate-*`, `edge-arrow` |
| `tags.ts:893` | chấm "◆/●" | `seal-lit`, `seal-unlit` |
| `src/view/banners.ts:80-127` | vải cờ tướng vẽ canvas, mắt | `banner-cloth` |
| `src/view/telegraphs.ts:187-211` | đĩa "!" canvas | `danger` |
| `src/view/paint.ts:372-375` | bản build không có ô đất, chỉ có màu shader | gắn ô đất vào `public/` (làn map, MF-C24) |
| Bậc Low `?q=low` | rồng, quái capsule, cây nón | model thật bản nhẹ |

**Giữ:**
- `paint.ts`: ô đất thật, decal và nhiễu shader;
- `paths.ts`: chevron và bóng ô (shader);
- hạt sáng `fx.ts`;
- viền tối khi trúng, khi máu thấp (`app.css:186-238`);
- chữ số sát thương.

### 5.2. Wordwoven

| Chỗ | Hình vẽ bằng mã | Thay bằng |
|---|---|---|
| `src/ui/title.ts:31-124` | cảnh SVG dự phòng: trời, sao, núi, ruộng, nhà, tre | **bỏ**; lỗi ảnh thì để nền màu phẳng |
| `title.ts:121`; `title.css:22,75` | cò bay SVG | **bỏ** |
| `title.ts:38-45,127-137`; `title.css:14-18` | dây 8 đèn lồng SVG | **bỏ** |
| `title.ts:160`; `title.css:23` | 14 đom đóm CSS | **bỏ**, hoặc làm hạt VFX đạt chuẩn |
| `title.ts:134`; `title.css:26-28` | bộ lọc nhiễu SVG cho tên, dấu son CSS, nét cọ | logo và huy hiệu AD 113 |
| `theme.css:29-34,48-50`; `td.css:27` | giấy dó (nhiễu SVG data URI), mép cọ, gạch dưới h2 | khung AD 115 |
| `theme.css:39-45`; `td.css:43,200`; `title.css:42` | nút "dấu son" CSS | nút AD 115 |
| `td.css:36-37` | trục tre CSS của dải chữ | `plate-long` AD 115 |
| `td.css:89-103` | chân dung đèn lồng CSS có chữ cái, sọc ô khóa | chân dung `WP:` + `portrait-ring` |
| `td.css:151,168,180,183` | đèn lồng thẻ chữ, nhãn "Ôn", cuộn, dấu hạng | `card-plate`, `review-book`, `grade-*`, `stamp-seal` |
| `td.css:159` | emoji icon lời gọi | `call-*` |
| `td.css:203-209`; `sheets.ts:94` | sao "★" | `star-*` |
| `title.css:51-52` | thanh âm lượng thanh tre | thanh trượt vẽ, hoặc thanh phẳng |
| `src/view/fx-pipe.ts:149-189` | đầu rồng Tối Thượng vẽ canvas | `WP:draconis-ult.png` |
| `src/view/debug-2d.ts:229-750`; `boss-2d.ts:241-400` | toàn bộ map 2D: cảnh, nhà, người, quái, boss vẽ canvas, emoji, đĩa chữ cái | 3D ở 1C; bậc Low dùng ảnh nhà, chân dung, ô đất |
| `src/content/slice-1a.ts:36,50,64,76,81,83` | tên ngắn là emoji và chữ cái | icon nhà |

### 5.3. Last Line

| Chỗ | Hình vẽ bằng mã | Thay bằng |
|---|---|---|
| `src/view/theme.css:96-99`; `survival.css:16-25` | thép chải, 4 đinh, vát trên mọi bảng | khung 9-slice của AD, khai báo `url()` trong `theme.css` |
| `survival.css:26`; `theme.css:100` | vạch sọc nguy hiểm | dải vẽ, hoặc bỏ |
| `survival.css:55` | viền băng rôn bằng sọc | đế băng rôn |
| `survival.css:109-110` | ổ khóa CSS | `lock` |
| `survival.css:180,195,198` | chấm nhấp nháy, đèn LED tròn | `led-on`, `led-off`, hoặc bỏ |
| ký tự làm icon: "◀ ▶" (`screens.ts:44`, `hud.ts:386`), "★☆" (`screens-journey.ts:120`, `journey.ts:122`), "⚠" (`screens-journey.ts:102,106`, `hud.ts:377,380`), "⌨" (`survival.css:60`), "✓" (`strip.ts:172,179`) | ký tự | `arrow`, `star-*`, `warning`, `rift`, `keyboard`, `check` |
| `survival.css:181`; `screens.ts:67` | tên game là chữ phát sáng | logo AD 121 |
| `scene.ts:344-388` | trạm dựng bằng hình khối: tấm, trụ, đèn, lan can, ống, vòm | `hull-left/right` 088 (TS-M1-07: không dựng công trình bằng mã) |
| `scene.ts:101-171` | sàn shader: tấm, đinh, vạch, chevron | giữ làm nền sáng; thêm `deck-decals` 088 |

**Giữ:**
- tia lửa phím `.sv-strip-spark`;
- viền đỏ khi trúng `.sv-vignette`;
- atlas ánh sáng `fx.ts:19-76`;
- shader hố đen và màn sương Rift;
- chữ số sát thương;
- quái và tàu khối dự phòng: chỉ hiện khi thiếu GLB, là đường lui cho dev.

## 6. Chữ phải đổi sang tiếng Anh

- Mọi chữ người chơi đọc đổi sang tiếng Anh. Nghĩa của từ đang học giữ tiếng Việt.
- Đã có phiếu Codex cho lượt đổi chữ: **130** Last Line, **131** Dragonhold, **132** Wordwoven.
- Bảng dưới là các file có chuỗi tiếng Việt (đếm dòng có chuỗi mang dấu, bỏ chú thích và `src/kit`). Đếm này là số tối thiểu: chuỗi không dấu như "Ai" hay "Tau" không được đếm.

| Dragonhold (352 dòng) | Wordwoven (275 dòng) | Last Line (260 dòng) |
|---|---|---|
| `src/ui/hud.ts` 65 | `src/ui/hud.ts` 85 | `src/app/main.ts` 77 |
| `src/ui/placement-ui.ts` 38 | `src/ui/sheets.ts` 30 | `src/view/screens-journey.ts` 58 |
| `src/ui/shop-strip.ts` 35 | `src/ui/build-menu.ts` 28 | `src/app/results.ts` 31 |
| `src/ui/results.ts` 35 | `src/ui/tips.ts` 24 | `src/app/journey.ts` 20 |
| `src/ui/wave-card.ts` 28 | `src/main.ts` 17 | `src/view/screens.ts` 20 |
| `src/app/app.ts` 25 | `src/ui/title.ts` 16 | `src/content/guns.ts` 18 |
| `src/ui/learning-frame.ts` 17 | `src/app/sandbox.ts` 15 (dev) | `src/view/hud.ts` 12 |
| `src/ui/debut-card.ts` 16 | `src/view/words/cards.ts` 15 | `src/content/balance.ts` 6 |
| `src/app/typing-pace.ts` 16 | `src/ui/profile.ts` 13 | `src/content/stage-rules.ts` 5 |
| `src/ui/tags.ts` 12 | `src/ui/settings.ts` 10 | `src/content/chapter-1.ts` 4 |
| `src/app/pace-card.ts` 9 | `src/content/slice-1a.ts` 6 | `src/app/skill.ts` 3 |
| `src/audio/synth.ts` 7 | `src/ui/team-bar.ts` 3 | `index.html` 3 |
| `src/content/data/maps.ts` 4 | `src/app/prefs.ts` 3 | `src/view/strip.ts` 2 |
| `src/view/bench.ts` 3, `stage.ts` 2, `heroes.ts` 2, `banners.ts` 1 | `src/view/fx-pipe.ts` 3, `boss-2d.ts` 3 | `src/content/stage-s0.ts` 1 |
| `src/content/data/stages.ts` 1, `index.html` 2 | `index.html` 3, `src/ui/td.css` 1 | — |
| `src/ui/ui-preview.ts` 19, `src/audio/dev/harness.ts` 15 (dev) | — | — |

**Còn phải nhớ khi đổi chữ:**
- Chữ trong canvas cũng phải đổi:
  - Dragonhold: "Cắm Cờ" ở `banners.ts`;
  - Wordwoven: các số bay ở `debug-2d.ts` và `boss-2d.ts`;
  - Last Line: "HOÀN HẢO" trong kit `feedback/profiles.ts:51`. Đó là file kit, nên sửa ở `shared/game-kit` rồi đồng bộ.
- Tên trong dữ liệu như `nameVi` (Dragonhold) và tên ngắn trong `slice-1a.ts` (Wordwoven) phải đổi cùng.
- Nhãn `aria-label` cũng là chữ người chơi gặp qua trình đọc màn hình, ví dụ "Tốc độ gõ" ở `pace-card.ts`.

## 7. Âm thanh

### 7.1. Tình hình

- Không game nào có file âm.
  - `public/assets/<game>/audio/` và `art-src/audio/` không tồn tại ở cả ba game.
  - `~/AudioLab/review/staging/` rỗng.
- Dragonhold có bộ nạp file (`src/audio/bank.ts:85`, đọc `/assets/dragon-hold/audio/manifest.json`), nhưng chỉ bật khi `createAudio({files:true})`.
- Wordwoven chưa có bộ nạp file.
- Last Line tạo `SceneAudio` với `sounds: {}` (`src/audio/theme-audio.ts:101`): không có bảng file, không có đường lui.

**Nhóm tiếng:** theo `docs/games/AUDIO_PIPELINE.md` §3.2, gom thành bốn nhóm như điều phối yêu cầu.

| Nhóm | Loại trong §3.2 | Nguồn bậc 1 (bậc 2) |
|---|---|---|
| 1. Phím và UI | Phím đúng/sai; UI; Thưởng có cao độ; Thưởng xong từ (§4.3.3) | phím: tổng hợp (một mẫu thật CC0, mã đổi cao độ); UI: Kenney UI CC0 (tự ghi tre, giấy, gỗ); thưởng: mẫu VCSL qua bộ phát mẫu, dời ≤ 3 bán cung |
| 2. Tiếng ngắn | Va chạm, trúng; Súng, khạc, bắn; Điện, hồ quang; Báo nguy, stinger; Chết bầy, Chết lớn (§4.3.3) | trúng: Kenney Impact + thân Stable Audio 3; súng: Stable Audio 3 + lớp cơ khí Kenney + sub tổng hợp; điện: numpy và pedalboard dựng ra file; báo nguy: mẫu VSCO, VCSL + MIDI; chết: Stable Audio 3 |
| 3. Lửa, nổ, sinh vật, nền | Lửa, luồng lửa; Nổ, bẫy; Tiếng sinh vật; Nền lặp; Giọng người | lửa, nổ: Stable Audio 3 (Small-SFX); sinh vật: tiếng thú CC0 hạ 5–12 bán cung; nền: Stable Audio 3 + sửa mối nối (bản ghi CC0); giọng: chủ dự án và người nhà ghi, không AI |
| 4. Nhạc | Nhạc nhiều lớp; Nhạc cụ dân gian Việt | MIDI Claude viết, phát mẫu CC0 qua bộ phát mẫu (ACE-Step cho phác ý); sáo trúc, trống cơm: chủ dự án ghi (VCSL Dan Tranh, Slit Drum, Frame Drum) |

### 7.2. Dragonhold (87 mã; tài liệu `docs/audio/M0_SOUND_LIST.md` khớp `src/audio/catalog.ts`)

ME = `src/audio/map-events.ts`. Mọi tiếng đều tổng hợp ở `src/audio/synth.ts` và `beds.ts`, trừ hai dòng cuối.

| Mã | Gọi ở | Nguồn hôm nay | Loại §3.2 | Nguồn pipeline |
|---|---|---|---|---|
| `type.key`, `type.miss`, `type.back`, `type.switch` | ME:341, 351, 347, 344 | tổng hợp | Phím đúng/sai | giữ tổng hợp (§9 "ngoài lô") — cần chủ dự án quyết (mục 7.7) |
| `type.word`, `kill.chime`, `learn.new`, `learn.right`, `learn.wrong` | ME:271, 426, 273, 277; `app/app.ts:560,569` | tổng hợp | Thưởng có cao độ | VCSL qua bộ phát mẫu |
| `dragon.skill-ready`, `dragon.level`, `house.herb.pulse` | ME:431, 288, 314 | tổng hợp | Thưởng có cao độ (gần nhất) | VCSL đàn hạc, chuông |
| `ui.select` (chưa nơi nào gọi), `ui.confirm`, `ui.deny`, `ui.gold`, `dragon.potion`, `unit.warden.place`, `house.herb.place` | `audio/index.ts:259`; ME:295, 304, 278, 301, 291 | tổng hợp | UI | Kenney UI; `ui.gold` = Kenney RPG + VCSL Hand Chimes (§9 #27) |
| `fire.cast` | ME:272 | tổng hợp | Súng, khạc, bắn | §9 #1: Stable Audio 3, lớp gầm sau |
| `enemy.biped.shoot` | ME:236 | tổng hợp | Súng, khạc, bắn | Stable Audio 3 + Kenney |
| `fire.impact.a/b/c`, `impact.multi`, `enemy.{biped,quadruped,flyer,swarm}.hit`, `enemy.{biped,quadruped,flyer,swarm}.attack`, `enemy.quadruped.charge`, `general.g01.attack`, `unit.hit` | ME:382, 175, 388, 236, 369 | tổng hợp | Va chạm, trúng | §9 #2–4: Kenney + thân Stable Audio 3 |
| `enemy.{biped,quadruped,flyer,swarm}.death`, `unit.warden.down` | ME:412, 307 | tổng hợp | Chết bầy (bầy kiến), Chết lớn (còn lại) | Stable Audio 3 (§9 #15) |
| `warn.strike`, `warn.telegraph`, `general.g01.horn`, `general.g01.skill`, `general.g01.aura`, `wave.horn`, `wave.clear`, `stinger.victory`, `stinger.defeat`, `dragon.low`, `dragon.heartbeat` | ME:230, 246, 218, 247, 325, 187, 200, 204, 209, 106, 114 | tổng hợp | Báo nguy, stinger | mẫu nhạc cụ + MIDI; `wave.horn`, `general.g01.horn`: VSCO kèn co + VCSL trống khung (§9 #5, #6) |
| `dragon.breath`, `dragon.skyfire.cast`, `dragon.inferno` | ME:436 | tổng hợp | Lửa, luồng lửa | Stable Audio 3, tách đầu, vòng, cuối |
| `dragon.skyfire.impact`, `trap.{spikes,pine-bomb,net}.arm`, `trap.{spikes,net,pine-bomb}.trigger`, `general.aura.break` | ME:441, 291, 258, 325 | tổng hợp | Nổ, bẫy | Stable Audio 3; Pine Bomb: chủ dự án chọn Kenney Impact Plank v3 (3/5) |
| `dragon.hurt`, `dragon.roar`, `dragon.rage`, `dragon.down`, `enemy.{biped,quadruped,flyer,swarm}.spawn`, `enemy.{biped,quadruped,flyer}.windup`, `enemy.quadruped.howl` (chưa gắn sự kiện), `general.g01.death` | ME:365, 436, 281, 208, 221, 231, —, 398 | tổng hợp | Tiếng sinh vật | tiếng thú CC0 xếp lớp; Stable Audio 3 |
| `amb.forest`, `amb.river`, `amb.bird`, `enemy.{biped,quadruped,flyer,swarm}.march` | `audio/index.ts:161,162,166,158` | tổng hợp | Nền lặp | Stable Audio 3 vòng 6 s và 5 s (§9 #7–10) |
| nhạc `forest`, `wave` | `music.ts:140,154` | tổng hợp | Nhạc nhiều lớp | MIDI + VSCO, VCSL, vòng 22,857 s |
| nhạc `surge`, `general` | `music.ts:172-185` | **chỉ file, file thiếu: đang câm** | Nhạc nhiều lớp | như trên |

### 7.3. Wordwoven (30 mã trong `docs/audio/THEME_SOUND_LIST.md` + 13 tiếng chỉ có trong mã)

V = `src/view/audio-min.ts`. Mọi tiếng tổng hợp ở `src/view/folk.ts` và `music.ts`.

| Mã | Gọi ở | Nguồn hôm nay | Loại §3.2 | Nguồn pipeline |
|---|---|---|---|---|
| `key-right`, `key-wrong` | V:197, 196 | tổng hợp | Phím đúng/sai | giữ tổng hợp theo TK 24.6 — cần chủ dự án quyết |
| `ui-move`, `ui-pick`, `ui-off`, `ui-lamp` | V:128, 129, 132, 133 (`ui/title.ts:209-242`) | tổng hợp | UI | VCSL Slit Drum; mõ tre + Hand Chimes A5 (Q5); Kenney + foley |
| `call-build`, `call-mine`, `call-chop` | V:151, 156, 153 | tổng hợp | UI (gần nhất) | tự ghi hay Kenney; `call-chop`: Stable Audio 3 (chủ dự án chọn) |
| `call-harvest`, `word-hit`, `word-hit-bell`, `coin` | V:152, 200, 201, 235 | tổng hợp | Thưởng có cao độ | VCSL Hand Chimes; `word-hit`: VCSL Dan Tranh 7 file C4–C5 (§9 #21); `coin`: Kenney RPG + Hand Chimes (§9 #27) |
| `call-power`, `call-quiz`, `chain-callout` | V:150, 157, 202 | tổng hợp | Nhạc cụ dân gian Việt | trống cơm, sáo trúc chủ dự án ghi; VCSL Frame Drum; Faust flute |
| `wordshot-fire`, `arrow-fire` | V:227-230 | tổng hợp | Súng, khạc, bắn | §9 #23, #24: Stable Audio 3 (+ lớp giấy, hay cung ghi thật) |
| `blast` | V:231-233 | tổng hợp | Nổ, bẫy | §9 #26: VCSL Frame Drum/Timpani + Stable Audio 3 |
| `ink-puff` | V:234 | tổng hợp | Chết bầy | §9 #25: Stable Audio 3 |
| `leak`, `night-fall`, `dawn`, `defeat` | V:236, 205, 208, 217 | tổng hợp | Báo nguy, stinger | `leak`: VCSL Anvil kẻng (4/5); cồng: chủ dự án duyệt |
| `amb-villager-call` | V:116-120 | tổng hợp formant | Giọng người | chủ dự án và người nhà ghi 4 bản |
| `amb-dusk` | — | **chưa có** | Nền lặp | Stable Audio 3, vòng 60 s |
| `music-calm`, `music-tension` | `music.ts:74-94`; V:112 | tổng hợp | Nhạc nhiều lớp | MIDI + VCSL, vòng 45,714 s |
| `music-boss` | `music.ts:91` (chỉ trống) | tổng hợp một phần | Nhạc nhiều lớp | MIDI; ACE-Step |
| `music-stingers` (5 stinger) | — | **chưa có** | Nhạc nhiều lớp | ACE-Step hay MIDI |
| *(không mã)* đếm ngày 10 s cuối | V:110 | tổng hợp | UI | Kenney / foley |
| *(không mã)* boss báo, lặng, trồi, đổi pha, rút | V:163-170, 175-179 | tổng hợp | Báo nguy (4); Tiếng sinh vật (trồi, đổi pha) | mẫu + MIDI; Stable Audio 3 |
| *(không mã)* Rễ Trồi báo, Rễ Trồi đáp, đập Fort, hút sinh khí | V:171-174 | tổng hợp | Báo nguy (2); Va chạm, trúng (2) | như nhóm |
| *(không mã)* Ngắt, Neo, Phá Khiên | V:212-214 | tổng hợp | Va chạm, trúng | Kenney + Stable Audio 3 |
| *(không mã)* Thư Đồng hoảng | V:215 | tổng hợp | Báo nguy | mẫu + MIDI |

Trước khi Audio Lab làm 13 tiếng không mã, phải thêm mã cho chúng vào `THEME_SOUND_LIST.md`. Audio Lab chỉ có thẻ spec cho 30 mã.

### 7.4. Last Line (46 mã; `docs/audio/THEME_SOUND_LIST.md` khớp `SOUND_IDS` ở `src/audio/theme-audio.ts:40-72`)

TF = `view/typing-feel.ts`, CB = `view/combat.ts`, GF = `view/gunfx.ts`, SH = `view/shots.ts`, BM = `view/beams.ts`, MN = `app/main.ts`. Mọi tiếng đều tổng hợp.

| Mã | Gọi ở | Loại §3.2 | Nguồn pipeline |
|---|---|---|---|
| `key.ok`, `key.bad` | TF:120, 129 | Phím đúng/sai | giữ tổng hợp (§9) — cần chủ dự án quyết |
| `word.load`, `word.perfect`, `word.full` | TF:146 | Thưởng xong từ | §9 #17, #18: Stable Audio 3 + Kenney cơ khí |
| `streak.up`, `star.get` | TF:161, MN:186 | Thưởng có cao độ | VCSL |
| `ui.move`, `ui.select`, `ui.back` | MN:393-549 | UI | Kenney UI |
| `gun.xung`, `gun.xung.tail`, `gun.tan.fire`, `gun.ray.fire`, `gun.phao.launch`, `foe.shot` | SH:178, 181; GF:72, 76, 78; CB:235 | Súng, khạc, bắn | §9 #11: Kenney Metal + thân Stable Audio 3 + sub, 6 bản |
| `gun.tia.start`, `gun.tia.loop`, `gun.tia.end`, `gun.tia.pulse`, `gun.ray.charge`, `gun.ray.armed`, `hurt.drain` | CB:263, BM:184, CB:270, 294; GF:74; BM:165; CB:250 | Điện, hồ quang | numpy + pedalboard dựng ra file (§9 #19) |
| `hit.t1`, `hit.t2`, `hit.t4`, `hit.armour`, `shield.hit`, `shield.break`, `foe.shot.down`, `hurt.hull` | CB:198 → 303, 190; GF:84, 86; CB:240, 228 | Va chạm, trúng | §9 #12–14: Kenney Impact Metal + Stable Audio 3 |
| `gun.phao.burst` | GF:82 | Nổ, bẫy | Stable Audio 3 Small-SFX |
| `kill.swarm`, `foe.split`, `kill.elite`, `leader.down` | CB:366, GF:89, 96 | Chết bầy, Chết lớn | §9 #15, #16: Stable Audio 3 (+ hồ quang) |
| `hurt.breach`, `alarm.surge`, `end.win`, `end.lose`, `leader.horn`, `rift.warn`, `rift.open`, `support.repair` | CB:218; MN:619; CB:284; GF:91, 104, 107; CB:258 | Báo nguy, stinger | §9 #20: Stable Audio 3 + còi tổng hợp; còn lại mẫu + MIDI |
| `music.calm`, `music.surge` | MN:621 → `music.ts:38` | Nhạc nhiều lớp | MIDI + VCSL Anvil/Brake Drum, 20,000 s, −16 LUFS |

### 7.5. Đếm

| Game | Tổng | Tổng hợp | File thật | Chưa có | Phím và UI | Tiếng ngắn | Lửa, nổ, sinh vật, nền | Nhạc |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Dragonhold | 87 | 85 | 0 | 2 (lớp nhạc câm) | 19 | 33 | 31 | 4 |
| Wordwoven | 43 | 41 (1 một phần) | 0 | 2 | 14 | 18 | 4 | 7 |
| Last Line | 46 | 46 | 0 | 0 | 10 | 33 | 1 | 2 |
| **Cộng** | **176** | **172** | **0** | **4** | **43** | **84** | **36** | **13** |

**Chỗ lệch giữa tài liệu và mã:**
- Dragonhold: `ui.select` và `enemy.quadruped.howl` có mã nhưng không bao giờ phát.
- Wordwoven: tài liệu ghi `word-hit` là C5–C6; chủ dự án đã chọn C4–C5.
- Last Line: `gun.xung.loop`, `hit.sub`, `hit.tail` chỉ có trong tài liệu pipeline.

### 7.6. Audio Lab làm được gì

- **Chỗ chạy:**
  - mã ở `tools/audio-lab`;
  - dữ liệu nặng ở `~/AudioLab`: venv, trọng số, khoảng 1,9 GB thư viện CC0;
  - chạy qua `bash tools/audio-lab/run.sh`, không cần mạng.
- **Công cụ có sẵn:**
  - Stable Audio 3 Small-SFX và Small-Music (MLX), sinh ở 1, 2, 3 hay 10 s. Lượt chuẩn là 4 prompt × 6 seed = 24 ứng viên mỗi mã.
  - Bộ phát mẫu Python cho VCSL và VSCO-2-CE.
  - Bộ dựng lớp: thư viện + tổng hợp + mẫu.
  - Bộ trộn thử theo trận, có giọng đọc.
- **Chưa cài:** ACE-Step 1.5 (chờ chủ dự án nhận giấy phép, cần khoảng 10 GB), Surge XT.
- **Thẻ spec:** có cho mọi mã. Dragonhold 87, Wordwoven 30, Last Line 46.
- **Xử lý sau khi sinh:**
  - đổi về 48 kHz, lọc dưới 35 Hz, cắt đầu, mờ đuôi;
  - đo mối nối;
  - ghi WAV 24 bit kèm `SOURCES.json` và dòng giấy phép.
- **Độ to:**
  - tiếng ngắn −1 dBTP, LUFS-M tối đa −20;
  - nền LUFS-I −26;
  - nhạc theo tài liệu game: Dragonhold và Wordwoven −18, Last Line −16.
- **Bảng nghe** `pnpm audio:board` (127.0.0.1:3191):
  - nghe mù, cùng độ to;
  - 1–5 sao, chọn bản hay "Không bản nào đạt";
  - tối đa 10 mã và 20 phút mỗi lượt.
- **File đích:**
  - bản gốc `games/<g>/art-src/audio/masters/<id>/`;
  - bản chạy `public/assets/<g>/audio/…ogg` kèm `manifest.json`.
- **Giấy phép:**
  - chủ dự án đã đăng ký Stability Community License (cá nhân, 23/10);
  - chỉ dùng nguồn CC0, MIT, Apache, BSD;
  - cấm Freesound NC, Pixabay, BBC, âm của game khác.

### 7.7. Kế hoạch lô âm cho map 1

**Bước 0: chưa sinh gì mới.**
- Chủ dự án chấm các lượt nghe đã có trên bảng nghe:
  - lượt 1c: `1c-dh-1`, `1c-dh-2`, `1c-td`, `1c-ts-1`, `1c-ts-2`;
  - lượt 1 cũ: `1-dh-s2`, `1-dh-s3`, `1-ts-s1`, `1-ts-s4`, `1-td-s5`, `1-td-s6`.
- Các lượt này chứa phần lớn tiếng của lần chơi đầu. Chưa có dòng chấm nào sau 23/10.

**Việc mã trước khi file phát được** (pipeline §6.3; đây là mã, điều phối xếp làn):
- Dragonhold: bật `files:true`; harness có chế độ file; bộ giới hạn đọc độ dài file thật.
- Last Line: `SceneAudio` nhận bảng file, có đường lui; nhạc đi qua bus.
- Wordwoven: viết bộ nạp file.

**Thứ tự làm, tiếng nghe nhiều nhất trước:**

| Lượt | Dragonhold (L2-cau) | Wordwoven (Đồng Cỏ Thác Bạc) | Last Line (c1-s1) |
|---|---|---|---|
| A | `fire.cast`, `fire.impact.a/b/c`, `type.word`, `kill.chime` | `word-hit` (7 nốt Dan Tranh, không cần AI), `coin`, `call-chop`, `call-build`, `call-harvest` | `gun.xung`, `gun.xung.tail`, `hit.t1`, `hit.t2`, `kill.swarm`, `kill.elite`, `word.load`, `word.perfect` |
| B | `enemy.biped.*` và `enemy.swarm.*` (hit, death, march); `amb.forest`, `amb.river`, `wave.horn` | `ui-move`, `ui-pick`, `ui-off`, `ui-lamp` | `ui.move`, `ui.select`, `ui.back` |
| C | `ui.confirm`, `ui.deny`, `ui.gold`; bẫy arm và trigger | **nhạc đầu tiên `music-calm`** | **nhạc đầu tiên `music.calm`**, rồi `music.surge` |
| D | **nhạc đầu tiên `forest`**, rồi `wave` | `arrow-fire`, `wordshot-fire`, `ink-puff`, `blast`, `leak`, `night-fall`, `dawn`, `music-tension` | `gun.tia.*`, `foe.shot`, `hurt.hull`, `hurt.breach`, `hurt.drain`, `alarm.surge` |
| Sau | spawn, attack, `warn.strike`, `dragon.*`, `general.g01.*` (từ đợt 5), stinger, `learn.*`; rồi quadruped, flyer, lớp nhạc `surge`, `general` | `word-hit-bell`, `call-power` và `call-quiz` (cần trống cơm, sáo trúc), `chain-callout`, `defeat`, `amb-dusk`, `amb-villager-call` (ghi giọng), stinger, 13 tiếng boss và lời trực tiếp (cần mã trước) | `hit.t4`, `word.full`, `streak.up`, `foe.shot.down`, `support.repair`, `hit.armour`, `end.*`, `star.get`; rồi súng S1, khiên, Đầu Đàn, Rift |

**Được giữ tổng hợp nếu tài liệu thắng:**
- tiếng phím của cả ba game;
- họ tiếng điện của Last Line, nhưng chỉ khi dựng bằng numpy và pedalboard ra file.

**Quyết định của chủ dự án (chặn):**
- Luật 28/10 ở `AGENTS.md` nói "Sound is real audio files … not synthesized placeholders".
- Tài liệu pipeline và TK 24.6 của Wordwoven lại cho phím giữ tổng hợp.
- Đề xuất: dùng bậc 2 của §3.2. Mỗi phím là một mẫu thật CC0, mã chỉ đổi cao độ. Như vậy là file thật mà vẫn nhanh dưới 50 ms.

### 7.8. Chủ dự án phải nghe

- **Mỗi mã của map 1 ở bảng trên:** chọn bản trên bảng nghe. Mã có nhiều bản thì nghe thêm một lượt biến thể, khoảng 30 s mỗi mã.
- **Bảng phong cách mỗi game, trước lô của game đó:**
  - Dragonhold: `fire.cast`, `fire.impact.a`, `enemy.quadruped.howl`, `amb.forest`;
  - Last Line: `gun.xung`, `hit.t1`, `kill.swarm`, `word.load`;
  - Wordwoven: `word-hit`, `arrow-fire`, `ink-puff`, `coin`.
- **Mỗi lô, mỗi game:**
  - một đoạn dày 20 s;
  - một đoạn mỏi 3 phút;
  - phép thử E: 10 phút, có tiếng phím.
- **Phép thử F:** nghe trên điện thoại và laptop, một lần mỗi lô.
- **Phép thử C:** đoạn trộn khó nhất, để duyệt mức các tiếng khác lùi xuống dưới giọng đọc từ.
- **Riêng Wordwoven:**
  - duyệt nguồn chuông và cồng;
  - xem lại văn hóa của mọi lớp nhạc và mọi tiếng cồng (`night-fall`, `defeat`, tiếng pha boss, hút sinh khí).

## 8. Claude gắn ảnh có sẵn

**Luật chung cho mọi game:**
- Ảnh là media, không vào Git.
- Script chuẩn bị đọc `art-src`, xuất WebP vào `public/assets/<game>/ui/…` và ghi `manifest.json` nhỏ.
- Mã đọc URL từ một bảng duy nhất.
- Ảnh lỗi thì ghi `console.warn` và để trống. Không vẽ SVG thay. Kịch bản trình duyệt kiểm mọi ảnh đã tải.
- Tên file giữ nguyên khi AD hay Codex vẽ lại, nên đổi ảnh không cần sửa mã.
- Đây là việc làm đẹp, hợp giai đoạn tạm dừng tính năng mới.

### 8.1. Last Line (làm trước: lấp ví dụ 2 và 3 của chủ dự án, ít việc nhất)

1. Claude chấm lại 108 (KA3, KA4 chưa đạt hết) và 109 (chờ ≥ 8).
2. Tạo `public/assets/typing-survival/ui/{icons,foes,stages}/`:
   - từ `art-src/ui/icons/*.norm.{64,128,256}.png`;
   - từ `art-src/ui/foes/*.png` (xuất 64, 128);
   - từ `art-src/ui/stages/c1-s*.png` (xuất 768×432 và 192×108).
   - Theo AGENTS.md, biến `url()` đặt trong `src/view/theme.css`.
3. **Nạp súng:** `src/view/screens-journey.ts:91-97`, icon súng ở đầu thẻ (LL-25); chân dung trong dòng khắc, kém và chip mối nguy (LL-26, LL-27).
4. **Bến trận:** `src/view/hud.ts:164-173`, icon cạnh `span.sv-gun` ở dòng 168 (LL-39).
5. **Thẻ ải:** `screens-journey.ts:62,70-73`, băng ảnh ải và chân dung quái (LL-18, LL-20, LL-21).
6. **Thẻ ra mắt:** `hud.ts:395-409`, chân dung Brute (LL-35).
7. **Thẻ trước trận và Hành trình:**
   - `src/view/screens.ts:116-125`: ảnh ải và 2 icon súng (LL-29);
   - `src/app/journey.ts:120-126`: ảnh nhỏ ải (LL-17);
   - `src/app/main.ts:259-270`: ảnh ải kế (LL-53).
8. **Kho súng:** `screens.ts:90`, icon súng (LL-15).
9. **Sân 3D:** `src/view/scene.ts:344-388`, vỏ trạm, lớp xa, decal 088 (LL-46, LL-47). Đã có ở TS-M1-07 và -08.
10. **Dựng ảnh tàu:** Vanguard và Draconis từ GLB, cho LL-10 và LL-13.

### 8.2. Wordwoven

1. **Bản chơi:** chép `public/assets/typing-defense/ui/` từ cây chính sang bản chơi, hoặc chạy media pull (mục 1.3).
2. **Màn tựa** `src/ui/title.ts`:
   - bỏ cảnh SVG (106-124), cò (121), dây đèn (38-45, 127-137), đom đóm (160), dấu (161);
   - thêm `onerror`;
   - `title.css` bỏ quy tắc của các phần đó.
   - Kịch bản `td-theme` đòi `painted: true`.
3. **Tách nền:** ảnh `art-src/ui/buildings/*`, `ui/resources/*`, `ui/lanterns/*`, `portraits/*` nền G hoặc M. Tách bằng `tools/art-normalize`. Xuất 64, 128, 256 vào `public/assets/typing-defense/ui/{buildings,resources,lanterns,portraits}/`.
4. **Thanh đội:**
   - `src/ui/team-bar.ts:20-29`: chân dung thay chữ cái; `helper-*-scared` khi Thư Đồng hoảng;
   - `src/ui/td.css:89-103`: bỏ đèn lồng CSS (WW-30);
   - nơi được cử tới dùng icon nhà, thay emoji trong `src/content/slice-1a.ts:36,50,64,76,81,83` (WW-32).
5. **Tài nguyên:** `src/ui/hud.ts:42,53,57`, icon Gold, Wood, Rice (`food`), Lives (WW-20, WW-21); `knowledge`, `wave` (WW-22, WW-23).
6. **Menu xây và thẻ nhà:**
   - `src/ui/build-menu.ts:91-95`: icon nhà, icon giá (WW-37);
   - dòng 61: đèn lồng cho lượt mạnh (WW-42);
   - dòng 28-38: icon Fort, chân dung Chấm (WW-41).
7. **Boss và lời dạy:**
   - `hud.ts:195-218,155-162`: `moc-tinh.crop` (WW-51, WW-53);
   - `hud.ts:187-192`: `narrator` (WW-54).
8. **Tối Thượng:** `src/view/fx-pipe.ts:149-189`, `draconis-ult.png` thành lớp DOM, để chạy được cả trên map 3D (WW-66).
9. **Bậc Low 2D:** `src/view/debug-2d.ts:522` vẽ icon nhà thay emoji và chữ cái (WW-60), chân dung thay đĩa C, P, G (WW-62). Làm sau 1C hay cùng 1C; báo làn L.
10. Ảnh Wordwoven có sẵn đều kiểu cũ (sách tranh). Gắn bây giờ vẫn hơn emoji. Khi AD 115 có khung mới, AD chấm lại bộ icon (xem phiếu có điều kiện UIC-WW-R1–R3).

### 8.3. Dragonhold

1. **Script chuẩn bị** `scripts/ui-art/prepare.mjs` (mới): đọc `art-src/icons/normalized/<tên>.{64,256}.png`, xuất WebP vào `public/assets/dragon-hold/ui/icons/`.
2. **`src/ui/skin.ts:127-184`:** `ICONS` trả `<img>` theo bảng URL. Thay 17 icon có ảnh:
   - `coin` → `gold`;
   - `breath`, `skyfire`, `roar`, `inferno` → 4 `skill-*`;
   - `potion` → `potion-small`;
   - 5 món đặt (`spikes`, `pine-bomb`, `net-launcher`, `moss-warden`, `herb-hut`);
   - `dragon-heart`, `hard-scale`;
   - `crown` → `enemy-general`;
   - `foeIcon` tạm thay bằng `family-moss`, `family-beast`, `family-bug`.
3. **Chỗ dùng:**
   - `src/ui/hud.ts:236-242,321-337` (DH-08, DH-21–25);
   - `src/ui/shop-strip.ts:235-255` (DH-37, DH-39);
   - `src/ui/placement-ui.ts:404,495-540,600-603` (DH-40, DH-44);
   - `src/ui/wave-card.ts:254-292,365-367` (DH-30, DH-31, DH-34);
   - `src/ui/tags.ts:455-488` (DH-47);
   - `src/ui/results.ts:276-304` (DH-66).
   - Nút Cắm Cờ dùng `aura-attack` (DH-57).
4. **`src/ui/styles/dh.css:88-118`:** bỏ rêu CSS ngay. Bảng gỗ CSS giữ tới khi AD giao khung.
5. **Ô món** `dh.css:1007-1040`: tăng ô icon từ 24 lên khoảng 40 × `--ui`, để icon vẽ đọc được (DH-37).
6. **Chân dung quái tạm:** thử cắt từ `art-src/enemies/*.png` và `art-src/generals/moss-banner.png` bằng công cụ (DH-30, DH-52). Dưới 8 điểm thì chờ UIC-DH-7.
7. Bộ icon Dragonhold là kiểu cũ (sách tranh rừng thông). AD 119 đặt hướng sử thi. AD chấm lại; dưới 8 thì chạy UIC-DH-R1, R2.

## 9. Codex vẽ ảnh mới

Chi tiết từng phiếu ở `docs/games/map1/UI_IMAGERY_CODEX.md`.
- Phiếu chỉ gồm icon và mảnh UI nhỏ. Phong cách lấy khối STYLE mới của AD, không chép khối STYLE cũ.
- Mỗi phiếu 6–12 ảnh. Thứ tự: icon trước, rồi mảnh UI nhỏ, rồi minh họa nhỏ (chân dung).

| Lô | Phiếu | Game | Nội dung | Số ảnh | Ưu tiên |
|---|---|---|---|---:|---|
| 1 · Icon | UIC-LL-1 | Last Line | HUD trận: armour, clock, kills, surge, repair-pod, keyboard, check, bay-full, streak, lock | 10 | P1 |
| 1 · Icon | UIC-LL-2 | Last Line | Thẻ ải và nạp súng: objective, hazard, learning-rule, equipment, warning, new-badge, station-crest, chapter-crest, load-guns, back, shard | 11 | P1 |
| 1 · Icon | UIC-WW-1 | Wordwoven | 10 loại lời gọi | 10 | P1 |
| 1 · Icon | UIC-WW-2 | Wordwoven | 6 tem hạng, 2 sao | 8 | P1 |
| 1 · Icon | UIC-WW-3 | Wordwoven | HUD và hệ thống: seeds, day, night, night-call, review-book, chain, pause, play, sound-on, sound-off, close, warning | 12 | P1 |
| 1 · Icon | UIC-WW-4 | Wordwoven | Nút và thẻ nhà: build, hire-villager, ultimate, sell, upgrade, send, undo, lock, level-pip-lit, level-pip-unlit | 10 | P1 |
| 1 · Icon | UIC-DH-1 | Dragonhold | HUD và trạng thái: wave-horn, chain, dragon-rage, armour, shield, phase-prep, phase-fight, phase-break, fast-forward, danger | 10 | P1 |
| 1 · Icon | UIC-DH-2 | Dragonhold | Hệ thống và học: pause, camera-reset, keyboard, speaker, check, new-word, deny, lock, upgrade, sell | 10 | P1 |
| 1 · Icon | UIC-DH-3 | Dragonhold | Bản đồ và thẻ chữ: lane-bridge, lane-stream, lane-sky, slot-trap, slot-house, slot-hold, seal-lit, seal-unlit, flag-pull, swarm, edge-arrow | 11 | P1 |
| 1 · Icon | UIC-LL-3 | Last Line | Menu và kết quả: 6 icon menu, 2 sao, retry, next-stage, stat-time, stat-accuracy | 12 | P1 |
| 1 · Icon | UIC-DH-4 | Dragonhold | Kết quả: 2 sao, 3 số, retry, easier, 3 trạng thái từ | 10 | P1 |
| 1 · Icon | UIC-WW-5 | Wordwoven | Menu, âm lượng, hồ sơ: 5 icon menu, 3 âm lượng, 4 số hồ sơ | 12 | P1 (menu) / P2 |
| 1 · Icon | UIC-WW-6 | Wordwoven | Chế độ và số kết quả: 4 chế độ, stat-nights, stat-foes, stat-words, record-ribbon | 8 | P1 / P2 |
| 1 · Icon | UIC-LL-4 | Last Line | Cài đặt, hồ sơ, Rift | 11 | P2 |
| 2 · Mảnh UI | UIC-DH-5 | Dragonhold | keycap ×2, tag-plate ×3, level-badge, pip ×2 | 8 | P1 |
| 2 · Mảnh UI | UIC-WW-7 | Wordwoven | keycap, card-plate ×2, stamp-seal, pip ×2, agent-badge | 7 | P1 |
| 2 · Mảnh UI | UIC-LL-5 | Last Line | keycap ×2, led ×2, mag ×2, arrow | 7 | P1 |
| 3 · Minh họa | UIC-DH-6 | Dragonhold | hoa-long, hoa-long-hurt, bach-long, 4 huy hiệu tốc độ | 7 | P1 |
| 3 · Minh họa | UIC-DH-7 | Dragonhold | 7 chân dung quái và tướng, 1 vải cờ | 8 | P1 |
| 3 · Minh họa | UIC-WW-8 | Wordwoven | 5 người làng và lính, 3 trạng thái ruộng, 2 trạng thái | 10 | P1 |
| 3 · Minh họa | UIC-WW-9 | Wordwoven | 9 chân dung quái | 9 | P1 |

**Cộng:** 21 phiếu, 201 ảnh.
- Lô 1 có 145 ảnh, lô 2 có 22, lô 3 có 34.
- Một số tên trùng giữa các game (`lock`, `keycap`, `star-lit`…). Mỗi game vẽ bản riêng theo khối STYLE của game đó.

**Có điều kiện** (chỉ chạy nếu AD chấm bộ cũ dưới 8 theo mức chợ; 6 phiếu):
- **UIC-DH-R1, R2:** vẽ lại 21 icon Dragonhold (11 + 10).
- **UIC-WW-R1, R2, R3:** vẽ lại 6 nhà, 6 tài nguyên, 3 đèn lồng và 9 chân dung Wordwoven (8 + 7 + 9).
- **UIC-LL-R:** vẽ lại 5 súng và 6 quái Last Line theo hướng chủ dự án chọn ở 112 (11).

**Thứ tự chạy đề xuất:**
1. Last Line chờ chủ dự án chọn hướng ở 112. Khối STYLE Last Line đổi theo hướng đó.
2. Trong lúc chờ: Wordwoven trước (WW-1, WW-3, WW-2, WW-4), vì khối STYLE mới của nó đã có ở phiếu 113 và 115.
3. Sau đó Dragonhold (khối STYLE ở 119), rồi Last Line.

**Việc cho AD** (ngoài phạm vi bản này, chưa có phiếu):
- khung UI Dragonhold: bảng, nút, thanh, băng rôn, nền kết quả;
- khung UI Last Line: bảng, tấm bến, dải chữ, nút;
- đế thẻ chữ và đế tem hạng Wordwoven: 115 chưa có. Nếu AD nhận thì bỏ `card-plate` và `stamp-seal` khỏi UIC-WW-7;
- favicon cả ba game: Claude cắt từ huy hiệu hay logo bằng công cụ, không cần phiếu.

## 10. Bằng chứng

- **Tờ chụp đã có** (lượt kiểm 28/10):
  - `games/dragon-hold/tmp/map1-audit/sheets/sheet-01-first-time-flow-1920.jpg` và sheet 02–15;
  - `games/typing-defense/tmp/map1-audit/sheet-newplayer-1280x720.jpg`, `sheet-1280x720.jpg`, `sheet-1920x1080.jpg`;
  - `games/typing-survival/tmp/map1-audit/sheets/sheet-menus-a-1280x720.jpg`, `sheet-menus-b-1280x720.jpg`, `sheet-c1s1-fight-*.jpg`, `sheet-pause-end-1280x720.jpg`.
- **Chụp mới 29/10:** `games/typing-defense/tmp/ui-imagery/sheet-td-theme-1280.jpg`.
  - Gồm màn tựa, menu xây, ngày, đêm, tạm dừng, kết quả.
  - Kịch bản `td-theme`, Vite 4151, cây chính: `painted: true`, 0 lỗi console.
  - Ảnh thô đã xóa bằng `tools/capture-prune/prune.mjs`.
- **Đo tải ảnh:** curl tới Vite dev và `vite preview` trên 4151 (mục 1.1). Mọi server đã tắt.
