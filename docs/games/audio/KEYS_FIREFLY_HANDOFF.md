# Tiếng phím Firefly: nguồn, chỗ đặt file, cách chạy, cách làm thêm

Tài liệu này đi kèm folder âm đã cắt trên Drive (chép thành `README.md` trong folder đó). Đọc nó khi tải âm về máy khác, hoặc khi muốn làm thêm bộ.

## 1. Nguồn và các bản giao

| Bản | Gì | Ở đâu trên máy dự án |
|---|---|---|
| **Âm gốc** | 408 WAV chủ dự án tạo bằng Adobe Firefly Generate Sound Effects (model của Adobe), 9 thư mục `Adobe_2026-10-29*`, khoảng 889 MB | `~/Downloads/typing-mp3/` (đường mặc định của `tools/audio-lab/keys/firefly.py`) |
| **v1** (phiếu 189) | 7 bộ, mỗi bộ 10 phím và 3 phím cách | `~/AudioLab/review/staging/keys-firefly-v1/` |
| **v2** (phiếu 218, bản đang dùng) | 32 bộ thuộc 7 họ, mỗi bộ 70–80 phím và 8 phím cách, từ 6 điểm; khoảng 26 MB OGG | `~/AudioLab/review/staging/keys-firefly/` |

- Mỗi bộ là một thư mục `<id>/` gồm `key-01.ogg` … `key-NN.ogg`, `space-01.ogg` … `space-08.ogg`, `preview.ogg` (nghe thử 1 giây) và `keys-manifest.json`.
- Danh mục gốc `keys-manifest.json` liệt kê mọi bộ: `id`, `name`, `family`, `score`, `manifest`, `preview`, `order`.
- Bảy id cũ (`deep`, `warm`, `rounded`, `solid`, `crisp`, `clear`, `bright-clack`) là bộ tốt nhất của mỗi họ. Mặc định của mọi game là `bright-clack` (chủ dự án 30/10).
- File âm không vào Git. Git chỉ giữ code, test và các file JSON nhỏ.

## 2. Đặt file ở đâu trên máy mới

1. Tải folder âm đã cắt từ Drive, đặt vào `~/AudioLab/review/staging/keys-firefly/`. Kiểm: trong thư mục có `keys-manifest.json` và 32 thư mục con.
2. (Chỉ khi muốn dựng lại bộ âm) tải folder âm gốc, đặt vào `~/Downloads/typing-mp3/`, giữ nguyên 9 thư mục con.

## 3. Sau khi pull code: lệnh để có tiếng (Typing Feel, 31/10)

Từ 31/10 các game không còn giữ bản sao bộ âm. Mọi game đọc từ **Typing Feel**:
- thiết kế ở [`docs/games/TYPING_FEEL_SERVICE.md`](../TYPING_FEEL_SERVICE.md);
- dữ liệu ở `typing-feel/public/v1/keys/` của repo cha (danh mục r1, 34 bộ);
- host máy nhà là `https://feel.typing-game.local`.

| Nơi | Lệnh | Ghi chú |
|---|---|---|
| **Repo cha** | `pnpm media:pull` (lấy OGG của `typing-feel/` từ Drive), `pnpm setup:play` một lần | Danh mục và manifest bộ nằm trong Git. OGG nằm trong `typing-feel/media.md5` và trên Drive, sau khi Claude chạy `media:push`. Bộ mới đi vào bằng `pnpm feel:import <staging>` (tới G7 thì bằng nút Format trong Admin). |
| **Last Line, Dragonhold, Wordwoven** | không cần lệnh | `pnpm build:<game>` hay `pnpm dev:<game>:app` ở repo cha đặt `VITE_TYPING_FEEL_ORIGIN`. Chạy riêng trong repo game thì Typing Feel tắt, chỉ có Off và âm gốc của game. Dragonhold và Wordwoven đang chuyển (B4, B5). |
| **Monkeytype, máy nhà** | `pnpm build:monkeytype` | Đặt `TYPING_FEEL_URL=https://feel.typing-game.local`. |
| **Monkeytype, máy công ty (chỉ GitLab)** | `pnpm feel:pack` ở máy nhà, rồi `pnpm --dir frontend feel:mirror <zip>` ở máy công ty | Các bước ở `docs/CUSTOM_TYPING_FEEL.md` của Monkeytype. Lần đầu xoá `frontend/static/sounds/keys` cũ do `sync-keys` để lại. |
| **Typing Feedback Lab** | `LAB_KEYS="$HOME/AudioLab/review/staging/keys-firefly" shared/game-kit/node_modules/.bin/vite --config tools/typing-feedback-lab/vite.config.mjs` | Mở `http://127.0.0.1:4192/`. |

Host feel không trả lời thì game vẫn chạy: chỉ có Off và âm gốc của game, kèm dòng "Keyboard sounds unavailable". Bộ người chơi đã lưu được giữ nguyên.

## 4. Dựng lại bộ âm từ âm gốc

```bash
bash tools/audio-lab/run.sh keys firefly survey     # đo 408 file → tmp/keys-firefly/survey/
bash tools/audio-lab/run.sh keys firefly build-v2   # 32 bộ → tmp/keys-firefly/staging-v2/keys-firefly/
```

Sau đó chép `tmp/keys-firefly/staging-v2/keys-firefly/` sang `~/AudioLab/review/staging/keys-firefly/`. Bản v1 (7 bộ) dựng bằng `keys firefly build`.

## 5. Làm thêm bộ sau này (chủ dự án 30/10: "tạm giữ 32 bộ, sau nếu cần làm thêm thì triển khai tiếp")

**Vì sao chỉ có 32 bộ** (số trong `docs/codex-queue/218-report.md` và `218/selection.json`):

- Có 3.773 tâm âm sắc được thử.
- 529 bộ ứng viên dưới 6 điểm; 490 bộ đạt từ 6 điểm.
- 458 trong số 490 bộ đó bị loại vì gần trùng một bộ điểm cao hơn, còn lại 32.
- Ngưỡng gần trùng là `MIN_DISTANCE + 0.02` (hiện `0.50 + 0.02`) trong `tools/audio-lab/keys/firefly_v2.py`, hàm `propose`.

**Ba cách có thêm bộ từ âm gốc hiện có:**

1. **Hạ ngưỡng gần trùng.** Đổi `MIN_DISTANCE` trong `firefly_v2.py` rồi chạy lại `build-v2`.
   - Hạ ngưỡng thì có thêm bộ ngay từ 490 bộ đạt điểm; muốn khoảng 80 bộ thì thử dần từ khoảng 0,35.
   - Đổi lại: trong cùng một họ, nhiều bộ nghe gần nhau.
2. **Sửa điểm "độ lặp"** trong `score_set` của `firefly_v2.py`.
   - Hiện điểm lấy tương quan của **cặp giống nhau nhất** trong khoảng 80 biến thể, nên chỉ một cặp gần giống là kéo cả bộ xuống.
   - Đó là lý do chính các bộ dưới 6 bị loại: độ lặp 0,03–0,15, trong khi độ sạch, độ đều và đuôi tiếng ngang hoặc hơn bộ đạt.
   - Cách sửa: dùng phân vị 95 hay trung bình tương quan, hoặc bỏ hẳn cặp trùng rồi chấm. Sau đó chạy lại `build-v2`.
3. **Ồn nền** (phần thứ hai làm các bộ bị loại thấp điểm): lặng hóa khoảng nghỉ mạnh hơn trước khi chấm.

**Nghe thử bộ bị loại:** `bash tools/audio-lab/run.sh tools/audio-lab/keys/firefly_rejected_preview.py` dựng lại các bộ dưới 6 điểm và ghi 10 file nghe vào `tmp/keys-firefly/listen-rejected/`, kèm `scores.json` (điểm từng phần). Bản đã gửi chủ dự án 30/10 nằm sẵn ở đó.

**Muốn bộ khác hẳn,** không chỉ nhiều bộ hơn: tạo thêm âm trong Firefly với prompt khác hẳn về loại bàn phím, switch, keycap. Prompt nên:

- gõ chậm, khoảng 2 phím mỗi giây, có khoảng lặng giữa các phím;
- ghi âm khô, sát micro;
- tách riêng prompt phím cách cho từng bộ;
- bỏ chữ "Foley" và "edited sequence".

Prompt mẫu cho từng họ nằm trong ba phiếu giám khảo chọn nguồn của workflow `keys-from-firefly` (29/10), có tóm tắt ở `docs/HANDOFF_CURRENT.md`.

**Bộ mới tự hiện trong mọi game** vì danh sách đọc từ danh mục `keys-manifest.json`. Danh sách nhóm theo họ (kit phiếu 219). Không cần sửa code game, chỉ chép âm và danh mục mới.

## 6. Drive (chờ chủ dự án kết nối lại rclone)

- Âm gốc: `typing-game-media/audio-sources/typing-firefly-original/` (giữ 9 thư mục).
- Âm đã cắt: `typing-game-media/audio-sources/typing-keys-cut/`, có file này làm `README.md`.
- Trước khi đẩy: `rclone config reconnect tgmedia:` (token hết hạn 30/10).
