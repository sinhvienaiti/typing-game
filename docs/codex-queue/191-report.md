# Phiếu 191 · Last Line · Gắn tiếng phím Firefly và nghe thử khi rê chuột

Ngày 29/10/2026 · Mac mini M4 · worktree `games/.wt-ts-typefx`, nhánh `ts-typefx`. **Đã gắn bảy bộ Firefly, Off và Relay; mặc định Deep. `pnpm check` xanh 238/238 test; 18/18 ván vàng giữ nguyên.** Báo cáo và chứng cứ nằm trong `docs/codex-queue/` của worktree này.

## Điều kiện đầu vào

- `git status --short -uall` trước khi sửa **0 mục**: [status-before.txt](191/status-before.txt).
- HEAD `0bc81b552119b552097f15c35faa8aa50ca9664a`: commit đồng bộ kit phiếu 190 có Claude Opus đồng tác giả, ghi đã qua `pnpm check`; manifest trỏ cha `7b677b5a76436176fb376785b2b6f330f422ab1c`, `parentDirty: false`, có `ui` và `feedback`.
- Đã kiểm API `loadKeyboardCatalog`, `KeyboardSoundPreview`, `KeyboardSoundChoices`, `keyboardSounds`; xác minh **81/81 file kit** đúng manifest. Không sửa hoặc đồng bộ lại kit.
- Staging 189 đã có ở `~/AudioLab/review/staging/keys-firefly/`. Phần “Bộ mặc định (điều phối, 29/10 23:15)” của báo cáo 189 ghi chủ dự án chưa chọn bộ, tạm dùng Deep. Hằng số dễ đổi: **`DEFAULT_KEYBOARD_SOUND = "deep"`**, `src/app/settings.ts`.

## Đã làm

| Đường dẫn | Thay đổi |
|---|---|
| `public/assets/typing-survival/audio/keys/` | Chép 98 OGG và 8 manifest JSON, không WAV |
| `.gitignore`, `media.md5` | Cho Git giữ đúng các manifest; thêm 98 MD5 âm, giữ các mục media cũ |
| `src/app/keyboard.ts` | Đọc danh mục bằng kit; Off, Relay rồi Firefly; sửa id save mất; tải bộ khởi động; mức Master × Keyboard; adapter một tiếng mỗi chữ |
| `src/app/settings.ts` | Deep mặc định; chỉ Relay bật synth phím của game; lựa chọn và mức âm giữ trong save `survival.settings.typingFx` |
| `src/app/quick.ts` | Bỏ danh sách pending; dùng lựa chọn từ danh mục và truyền đúng `TypeFx.sounds` cho thành phần nghe thử của kit |
| `src/app/main.ts`, `src/view/type-fx.ts` | Khôi phục bộ lúc mở trang, chờ tải trước sim, nối player chung và mức âm; giữ chặn gõ/tạm dừng của bảng |
| `src/app/input.ts` | Space phát nhóm `space-*`, không thay sim; kiểm IME, shortcut, repeat và trạng thái trận/bảng |
| `src/audio/theme-audio.ts` | Chuẩn bị context im lặng để giải mã; nhạc/âm trận chờ cử chỉ; Relay ngoài Effects |
| `tests/keyboard-sounds.test.ts` | 23 test tích hợp danh mục, media thật, player/preview kit với Web Audio giả, lưu và tải lại |
| `tests/quick-settings.test.ts`, `tests/survival-input.test.ts` | Cập nhật 7 test settings và thêm 1 test Space |
| `docs/audio/THEME_SOUND_LIST.md` | Ghi bảy id bộ, đường dẫn, nguồn, mức và luật phát |
| `docs/changelog/2026-10-29-keyboard-sounds.md` | Changelog tiếng Việt của lần cập nhật |

Chữ đúng phát một biến thể `key-*`; Space phát `space-*`; biến thể do kit xoay vòng xáo và không lặp sát nhau. Hoàn tất từ giữ tiếng nạp đạn sẵn có của game, không phát thêm sample bàn phím. Firefly và Off tắt synth Relay. Firefly đi vào destination chung theo Master × Keyboard volume, không chịu Effects; mute hoặc mức bằng 0 làm im tiếng phím.

Hover/focus và chọn bộ dùng đúng thành phần kit 190: **150 ms** chờ trước nghe, đoạn **1 s**, tắt dần **30 ms** khi rời/chuyển/đóng. Player tải gameplay chính là instance truyền cho preview. Bảng mở hoặc đếm 3-2-1 vẫn giữ `quick.blocking`, dừng trận và chặn chữ; Space cũng kiểm trạng thái này. Bộ lưu cũ mất về Deep; nếu Deep mất thì lấy bộ đầu còn lại, nếu cả danh mục thiếu thì Relay. Off lưu cũ được giữ.

## Media và cách đi vào gói

MB trong bảng là byte / 1.000.000. Mỗi bộ có 10 phím, 3 cách, 1 preview và 1 manifest.

| Thư mục | OGG | JSON | Tổng file | MB |
|---|---:|---:|---:|---:|
| `deep/` | 14 | 1 | 15 | 0,135934 |
| `warm/` | 14 | 1 | 15 | 0,135224 |
| `rounded/` | 14 | 1 | 15 | 0,123247 |
| `solid/` | 14 | 1 | 15 | 0,140683 |
| `crisp/` | 14 | 1 | 15 | 0,136207 |
| `clear/` | 14 | 1 | 15 | 0,134426 |
| `bright-clack/` | 14 | 1 | 15 | 0,137501 |
| Manifest gốc | 0 | 1 | 1 | 0,001505 |
| **Tổng** | **98** | **8** | **106** | **0,944727** |

- **98 OGG: 607.670 byte (0,607670 MB)**, bị Git bỏ qua; thêm đúng 98 dòng trong `media.md5`. WAV đã chép **0**, không mang dấu nội bộ `.firefly-builder.json` sang game.
- **8 JSON: 337.057 byte (0,337057 MB)**, mở lại từng tầng thư mục và đúng mẫu `keys/**/keys-manifest.json` trong `.gitignore`, theo `AUDIO_PIPELINE.md` §11. JSON đi qua Git, không trông chờ `media:push` vốn chỉ nhận đuôi media. Các tên WAV trong metadata manifest được giữ nguyên để lưu nguồn gốc; loader chỉ chọn 91 OGG sample.
- Vite sao chép `public/` vào `dist/`: đã kiểm **106/106** file trong build trùng byte với staging và bản game. Danh sách từng file, byte, MD5, SHA-256: [copied-files.json](191/copied-files.json). Kết quả kiểm: [verification.json](191/verification.json); chạy lại bằng `python3 docs/codex-queue/191/verify-assets.py` sau build.
- **Claude chạy `media:push`.** Âm đang ở worktree này; cấu hình media repo cha trỏ `games/typing-survival`. Khi nhận thay đổi, cần mang cả 98 OGG bị bỏ qua sang checkout đích hoặc dùng cấu hình media trỏ worktree trước khi đẩy. Không chỉ nhận phần diff Git rồi bỏ sót âm.

## Kiểm tra

Lệnh kiểm bắt buộc của phiếu: `pnpm check` (bao gồm test và build của đúng game này). Không chạy riêng suite/build của game khác.

| Kiểm | Kết quả |
|---|---|
| Manifest kit | 81/81 file đúng; `ui`, `feedback` và API 190 có đủ |
| File test | **24/24 qua** |
| Test | **238/238 qua**, 0 lỗi, 0 bỏ qua |
| Tiếng phím mới | **23/23 qua** |
| Input | **5/5 qua**, gồm 1 test Space mới |
| Quick settings | **7/7 qua**, cập nhật theo Firefly |
| Ván vàng S0 | **18/18 qua**, JSON golden không đổi |
| Thời gian bước S0 | Median **0,546 ms**, p95 1,207 ms; cổng median ≤1,5 ms đạt |
| Thời gian bước chapter | Median **0,863 ms**, p95 1,797 ms; cổng median ≤1,5 ms đạt |
| Typecheck và production build | Qua; Vite có cảnh báo chunk >500 kB, không lỗi |
| Đối chiếu media | **106/106** trùng staging và dist; 98/98 OGG đúng MD5/bị bỏ qua; 8/8 JSON không bị bỏ qua |
| Phạm vi bảo vệ | `src/kit`, `src/sim`, `src/content`, `tests/golden`: **0 diff** |

Không có test thời gian đỏ nên không cần chạy riêng ba lần. [Log cuối](191/check.txt), [lượt kiểm đầu](191/check-first.txt). Lượt đầu 236 test xanh; khi rà thêm, đã bỏ bộ hẹn giờ nghe mẫu có thể phát muộn sau đổi bộ, thêm trường hợp tải cũ gặp Warm, và tách chuẩn bị context khỏi phát nhạc để tải sample không tự bật tiếng. Lượt cuối có đủ 238 test ở bảng trên.

Các test đọc catalogue/OGG thật từ filesystem qua fetch giả, không gọi mạng; Web Audio giả kiểm file, player, số lần phát, routing, gain và thời lượng. Chứng minh tải đủ 13 sample mỗi bộ và phát đúng đường dẫn; chọn/lưu/tải lại giữ bộ; id cũ mất về mặc định; Off/Relay/Master mute/0/Keyboard volume 0 làm im player mẫu; tải cũ không đè Warm/Off; chờ hover 150 ms, phát 1 s, rời tắt 30 ms; chuẩn bị context không phát nhạc/âm trận. Không nhận các phép kiểm này là đã nghe hoặc render thật.

Status cuối và kiểm phạm vi: [status-after.txt](191/status-after.txt), [scope.json](191/scope.json). Chỉ có file phiếu, manifest và changelog nêu trên; không có file âm trong danh sách Git.

## Bỏ qua và việc chủ dự án/Claude cần xem

- Không mở dev server, trình duyệt hoặc mạng; chưa nghe thực tế hoặc kiểm render/focus/hover trên thiết bị. Claude cần nghe bảy bộ, thử rê nhanh, Tab/Enter/Space, đóng bảng và mute ở 1280×720/1920×1080, đồng thời xác nhận phím không vào trận khi bảng mở.
- Worktree không có ảnh loa phiếu 180; giữ nút chữ **Listen** của kit. Không tạo ảnh hoặc chép art từ game khác.
- Không đẩy media, không đồng bộ/sửa kit, không dùng lệnh Git có ghi, không đổi ván vàng, không chạm game khác hoặc Tu Tiên. Không tạo âm hay ảnh mới nên không có prompt mới.
