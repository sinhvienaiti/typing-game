# Phiếu 193 · Wordwoven · Settings, Sound và tiếng phím

Ngày 30/10/2026 · Mac mini M4. **Đã hoàn tất tích hợp và kiểm cục bộ; chưa nghiệm thu trong trình duyệt, chưa chạy build hoặc bộ test game theo house rules.** Báo cáo này thay báo cáo dừng vì worktree không sạch của lượt trước.

## Điều kiện đầu vào

Đúng worktree `games/.wt-td-keys`, nhánh `td-keys`; `a2-days` là tổ tiên của HEAD `81baf46`. Phiếu 189 đã được nhận ở commit repo cha `9f7cac0f` (“Codex 189, reviewed”); 190 ở `7b677b5a` (“reviewed in the Lab at 1280x720”). HEAD worktree đồng bộ kit đúng commit sau, có `ui`, `feedback`, `audio` và `a11y-dialog`.

Đã đọc toàn bộ phiếu 192, `IN_GAME_SETTINGS.md`, báo cáo 180/189/190, mẫu Last Line và Q6 của audio-lab. Tiếp tục phần dở theo chỉ dẫn chạy lại, giữ phần đúng; không yêu cầu status sạch hoặc giấu thay đổi. Bằng chứng: [scope.json](193/scope.json), [status khi tiếp tục](193/status-resume.txt).

## Phần giao

- `src/app/quick.ts`, `src/ui/quick.css`, `src/main.ts`: hai nút ảnh ở góc phải trên, có trên màn tựa và trong trận. Click/F1/F2 mở, chuyển hoặc đóng; Esc đóng. Khi bảng mở và đếm **3–2–1**, `blocking` giữ session dừng, chặn phím chữ và lệnh chiến thuật. Đóng từ trận đang chạy đếm ba nhịp 500 ms; từ màn tựa hoặc trạng thái đã dừng thì giữ trạng thái đó. Resume đóng bảng; Quit to title về tựa. Dời bảng dạy/sandbox xuống, thêm vùng tránh cho thẻ chữ. Chunk mới tải riêng.
- Sound có **Master/Mute, Music, Effects, Keyboard sound, Keyboard volume, Interface**. `src/view/audio-min.ts` tách Interface và Bamboo khỏi Effects; nhạc/hiệu ứng giữ đường cong mức cũ. Kéo slider phát mẫu đúng bus; mẫu Master không phụ thuộc Effects.
- Danh mục: **Off, Deep, Warm, Rounded, Solid, Crisp, Clear, Bright Clack, Bamboo (original)**. Các bộ Firefly dùng nguyên thành phần kit 190: hover/focus chờ **150 ms**, nghe **1 giây**, rời/chuyển/đóng tắt dần **30 ms**. Cùng instance `TypingSounds` tải và phát bộ trong trận.
- `src/app/input.ts`: chữ và Backspace ở C10 dùng `key-*`, khoảng cách giữa từ dùng `space-*`. Ô text, textarea và contenteditable dùng cùng bộ, không gửi chữ vào sim. Bỏ phím lặp, tổ hợp Ctrl/Alt/Meta và IME đang soạn. Bamboo giữ phản hồi cũ theo sự kiện từ, bổ sung tiếng cho khoảng cách và ô text.
- `src/app/prefs.ts`: lưu mức, Mute và bộ vào `td.settings`. **`DEFAULT_KEYBOARD_SOUND = "bright-clack"`**, theo quyết định chủ dự án ở báo cáo 189 ngày 30/10 00:10. Giữ lựa chọn đã lưu; bộ mất về bộ đầu còn dùng được; Off vẫn Off. Tiếng phím theo **Master × Keyboard volume**, độc lập Effects; Off/Mute/Master 0 im lặng.
- Settings chỉ có **Pace adapts to your typing** và **Story mode**, ghi rõ áp dụng ván mới; đây là các thiết lập có thật. Điều chỉnh expectation cũ trong `tests/td-settings.test.ts` theo schema save và mặc định mới.

## Media

`public/assets/typing-defense/audio/keys/`: **91 sample OGG, 7 preview OGG, 8 manifest**, nguyên byte từ `~/AudioLab/review/staging/keys-firefly/`; **0 WAV**. `.gitignore` cho qua `keys-manifest.json`; âm vẫn bị bỏ qua. Giữ nguồn/giấy phép trong manifest; không sinh âm mới, không sửa audio-lab.

`public/assets/typing-defense/ui/quick-settings/`: **8 icon phiếu 180, 2 ảnh khung/nút frames-epic**, đủ prompt chính xác cạnh PNG. Tám icon chép dở khác bản `selected/` hiện tại; đã chép lại đúng bản chọn cùng prompt. Không sinh/vẽ lại ảnh, không dùng CSS/SVG/emoji làm icon.

Đã thêm [README media](../../public/assets/typing-defense/README.md), [kiểm kê và đối chiếu nguồn](193/media-audit.json), [108 binary chờ tải](193/media-pending.md5). **108/108 binary bị Git bỏ qua**, 8 manifest hiện trong status. Không sửa `media.md5` trước khi tải: `scripts/media/lib/plan.mjs` coi đường dẫn cùng băm trong lock là đã tải và bỏ qua upload. Claude nhận media rồi chạy `media:push`; công cụ cập nhật lock sau khi thành công. Cần mang media trong worktree sang nơi Claude chạy lệnh đó.

## Kiểm đã chạy

| Kiểm | Kết quả |
|---|---|
| `node src/kit/verify-kit.mjs` | **69/69 file khớp**, không sửa kit |
| `node_modules/.bin/tsc --noEmit` | **0 lỗi**, exit 0 |
| `node --import tsx docs/codex-queue/193/verify.mjs` | **175 assertion qua**, không báo thiếu media |
| `node docs/codex-queue/193/audit-media.mjs` | Audio khớp staging; 10 PNG/10 prompt khớp nguồn; 0 WAV |
| `git diff --check` | Sạch |
| Golden JSON so với HEAD | **2/2 giống byte**, SHA-256 trong `scope.json` |

Script riêng dùng Happy DOM/WebAudio giả và fetch qua filesystem, không server, trình duyệt hoặc request mạng. Kiểm click/F1/F2/Esc trên tựa và trận; chặn chữ khi bảng mở/đếm ngược; tick/log/hash đứng yên; lưu mọi mức, mode, pace và Mute; focus/hover đúng preview; Warm phát đúng `key-*`/`space-*`; Off/Mute/Master 0; Bamboo độc lập Effects; giữ pause cũ; Quit và fallback bộ mất. Đối chứng **100 tick**, cùng lệnh cho cùng log/hash sau khoảng dừng trình bày. Đây là **175 assertion cục bộ, không phải số test của bộ game**.

Log: [typecheck](193/typecheck.txt), [kit](193/kit-check.txt), [hành vi](193/verification.json), [stderr](193/verification-errors.txt), [status cuối](193/status-final.txt). Không đổi `src/sim`, `src/content`, `src/typing`, `src/kit` hoặc golden. **Chưa chạy lại ván vàng**; fixture giữ nguyên không đồng nghĩa golden replay đã qua.

## Hàng ẩn, phần bỏ qua và việc cần xem

- **Voice ẩn:** không có luồng đọc từ/lời thoại. Chỗ dò `speechSynthesis.speaking` chỉ nhường nhạc, không phát giọng. Music/Effects/Interface có luồng thật nên giữ.
- Không thêm chất lượng Low–Ultra, giảm chuyển động, sáu kiểu typing effects, cỡ chữ hoặc công tắc nghĩa/IPA: chưa có thiết lập thực tương ứng. Giữ luật hiện nghĩa hiện hành.
- **Chưa có ảnh riêng cho track/thumb slider** trong art được giao; dùng range native của kit. Không tự vẽ ảnh thay. Claude cần quyết phần art này; chưa coi điều kiện hình của `IN_GAME_SETTINGS.md` §4 đã nghiệm thu đầy đủ.
- **Không chạy `pnpm check`, build, test suite game/golden hoặc trình duyệt**, đúng house rules và mục Cấm của 192. Chưa có số test game mới, số gzip, đo bố cục 1280×720/1920×1080 hoặc nghe thực. Claude cần kiểm chữ/nút/thẻ không đè nhau, focus/Tab, tương phản trên ảnh thật; nghe các bộ và mức phối trong trận; chạy kiểm phát hành trước khi gộp.
- Đếm vật lý `.ts/.css` dưới `src` trừ kit: HEAD **10.772 dòng**, sau phiếu **10.850 (+78)**. Baseline đã vượt trần lịch sử 10.500; không cắt mã làn khác để làm đẹp số. Ngân sách bundle chưa đo vì cấm build.

Không chạy lệnh Git có ghi; không sửa game/worktree khác, Tu Tiên hoặc mã/tài liệu làn khác. Không có capture trình duyệt cần dọn. `status-at-start.txt` và `media-copy.json` giữ hồ sơ lượt đầu; dùng các log mới liên kết ở trên để nhận lượt này.
