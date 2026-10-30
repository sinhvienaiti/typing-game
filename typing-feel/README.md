# Typing Feel

Âm phím (và sau này hiệu ứng gõ) dùng chung cho mọi game. Game đọc lúc chạy từ `https://feel.typing-game.local/v1/`, không chép âm vào game. Thiết kế: `docs/games/TYPING_FEEL_SERVICE.md`.

- Thư mục tự đủ: chỉ dùng module có sẵn của Node, không cài gói nào. Test ranh giới chặn import ra ngoài thư mục, nên tách repo sau này chỉ là dời thư mục.
- Hợp đồng v1: `contract/typing-feel.v1.json` (URL, luật đường dẫn, regex id, trường của danh mục và của bộ âm, luật `<fp12>`, mặc định hiệu ứng). Trong v1 chỉ được thêm, không đổi tên, không bỏ.

## Lệnh (chạy ở repo cha)

| Lệnh | Việc |
|---|---|
| `pnpm feel:import ~/AudioLab/review/staging/keys-firefly` | Dựng bản seed `r1` từ staging: chép nguyên byte OGG (không mã hoá lại), manifest rút gọn, danh mục, `health.json`. Bỏ qua `keys-manifest.*.bak.json`. |
| `pnpm feel:test` | Test của thư mục này (staging giả trong thư mục tạm, không có media thật). |

- Chạy lại trên cùng staging: không ghi gì, JSON giữ đúng từng byte.
- **Không bao giờ ghi đè:** thư mục `sets/<id>/<fp12>/` đã có thì mọi file phải trùng sha256, khác là báo lỗi. Danh mục đã Publish một bản (`r1`) thì không bị ghi lại bằng nội dung khác: staging đổi thì chạy với `--revision r2`.
- `<fp12>` tính trên byte âm và manifest bộ trừ `name`: chỉ đổi tên thì giữ thư mục và URL (danh mục mang tên mới); đổi thời lượng, licence hay âm thì ra thư mục mới.
- Git bỏ qua mọi file media (âm, ảnh, model, video) ở bất cứ đâu trong thư mục này, và cả `art-src/`; test `tests/no-media.test.mjs` kiểm bằng `git check-ignore`.
- Sau G6, Admin (All games → Typing Feel) thay lệnh này; nó giữ nguyên các đường seed.

## Cái gì ở đâu

| Thứ | Ở đâu | Sao lưu |
|---|---|---|
| Danh mục `public/v1/keys/keys-manifest.json`, manifest bộ âm `public/v1/keys/sets/<id>/<fp12>/keys-manifest.json`, `public/v1/health.json` | thư mục này | **Git** |
| OGG của bộ âm `public/v1/keys/sets/**` | thư mục này (Git bỏ qua) | `typing-feel/media.md5` + **Drive** (nhóm runtime) |
| WAV gốc `art-src/**` | thư mục này (Git bỏ qua) | **Drive** (nhóm originals) |

- Clone mới: danh mục về cùng Git; OGG lấy bằng `pnpm media:pull`.
- Sao lưu OGG lên Drive: chủ dự án chạy `pnpm media:push`.
- Máy nhà: nginx phục vụ `feel.typing-game.local` (block trong `infra/nginx/*.conf`, cần `pnpm setup:play` một lần).
