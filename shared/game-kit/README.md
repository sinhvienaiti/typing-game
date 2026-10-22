# Bộ kit chung cho game (`shared/game-kit`)

Kit là **nguồn chuẩn** của mã dùng chung cho các game mới tách từ Space Typing:
Rồng Giữ Ải (`dragon-hold`), Lời Gọi (`typing-defense`), Tuyến Cuối (`typing-survival`).
Kit chỉ có TypeScript và test, không có ảnh, âm thanh hay model.

Kế hoạch đầy đủ: `docs/games/SPLIT_PLAN.md` §4.

## Quy tắc quan trọng

- **Không bao giờ sửa tay `src/kit/` trong một game.** Mọi file ở đó được chép từ đây
  và kiểm sha256. Sửa tay thì `pnpm check` của game sẽ đỏ.
- Muốn đổi kit: sửa ở `shared/game-kit`, chạy test, rồi chép lại vào từng game.
- Kit chép **từ** Space. Space giữ bản gốc, không đổi ở giai đoạn này.
- Sửa lỗi ở một bên (kit hoặc Space) thì ghi một dòng vào `DRIFT.md`.
- Mã trong một module chỉ import trong kit bằng đường dẫn tương đối
  (ví dụ `../platform/rng`), để chạy được cả ở đây lẫn ở `src/kit/` của game.

## Các module

| Thư mục | Nội dung | Nguồn |
|---|---|---|
| `platform/` | RNG có seed, vòng khung hình, lưu trữ an toàn, trạng thái canvas | Space `src/platform/*` (không đổi) |
| `input/` | Bảng phím, chuẩn hoá chữ gõ (`typingText`, `normalizeWord`) | Space `src/scene3d/keys.ts`, `src/logic.ts` |
| `vocab/` | Nạp từ vựng, chọn từ theo độ dài, lọc từ nhạy cảm | Space `src/vocabulary.ts`, `src/scene3d/words.ts` |
| `learning/` | Gửi sự kiện học về portal (`gameId` bắt buộc), hàng đợi khi chạy riêng | Space `src/learning/shared.ts`, `shared/learning/message-contract.mjs` |
| `speech/` | Đọc từ bằng giọng máy, cài đặt hẹp `{ enabled, rate, volume }` | Space `src/speech.ts` |
| `audio/` | Bộ trộn nhiều bus, nhận bảng âm của từng game | Space `src/scene3d/sfx.ts`, `src/audio/mix.ts` |
| `ui/` | Màu ngữ nghĩa, biến CSS, font chữ trận, khung học cơ bản | Mới |
| `tools/` | `cdp-run.mjs` (chạy kịch bản trình duyệt), plugin Vite phục vụ `/vocabulary/`, `/typing-texts/` | Space `scripts/visual/cdp-run.mjs`, `scripts/dev/vite.worktree.config.ts` |
| `typing/` | Bộ định tuyến gõ, chữ, chọn từ, chấm điểm | Space `src/td/typing/*` (làn Kit B) |
| `three/` | Nạp model, vật liệu, hạt, sân khấu 3D | Space `render3d/*`, `scene3d/*` (làn Kit B) |
| `feedback/` | Phản hồi gõ theo hồ sơ game | Space `src/feedback/*` ở thẻ `survival-s0` (a292d1ac, làn Kit B) |

Mỗi module có `index.ts` xuất API công khai và test `*.test.ts` nằm cạnh.

## Lệnh

Chạy ở repo cha (`/Users/toandx/htdocs/typing-game`):

| Lệnh | Làm gì |
|---|---|
| `pnpm kit:test` | Chạy test của kit |
| `pnpm kit:sync --target games/<id>` | Chép các module khai trong `games/<id>/kit.config.json` vào `games/<id>/src/kit/`, ghi `kit-manifest.json`, `verify-kit.mjs` và `README.md` |
| `pnpm kit:sync --target games/<id> --allow-missing` | Như trên, bỏ qua module chưa có (chưa có `index.ts`). `kit:check` vẫn đỏ tới khi chép đủ |
| `pnpm kit:check` | Kiểm mọi game có `kit.config.json` (bỏ qua thư mục bắt đầu bằng `.`, như worktree): không ai sửa tay, đúng bản kit hiện tại hoặc bản ghim. Lỗi thì thoát mã 1 |
| `pnpm kit:drift` | So từng file kit với bản gốc ghi ở dòng `// Source:` đầu file, in tóm tắt. Chỉ để biết, luôn thoát mã 0 |

Test của lệnh chép: `node --test scripts/sync-game-kit.test.mjs`.

Khi chép, lệnh:

- Bỏ test: `*.test.ts`, `*.spec.ts`, `*.test-helper.ts`, thư mục `__tests__`, `__fixtures__`.
- Từ chối file media (ảnh, âm, video, model, font) trong kit.
- Từ chối khi một module import module khác (`../<module>/...`) mà game chưa khai. Hiện tại: `vocab` cần `input`; `learning` cần `platform`, `vocab`; `speech` cần `platform`; `typing` cần `platform`.
- Xoá file thừa trong `src/kit/`, chỉ ghi file đổi nội dung.
- Ghi vào `kit-manifest.json`: phiên bản kit, `parentCommit` (commit cuối của repo cha có đổi `shared/game-kit`), `parentDirty` (kit có thay đổi chưa commit), danh sách module, sha256 từng file.

Chạy riêng trong kit:

```bash
pnpm --dir shared/game-kit install
pnpm --dir shared/game-kit exec vitest run
pnpm --dir shared/game-kit exec tsc -p tsconfig.json --noEmit
```

## Cấu hình của game

`games/<id>/kit.config.json`:

```json
{ "modules": ["platform", "input", "vocab", "learning", "speech", "audio", "ui", "typing", "three", "feedback"] }
```

Có thể ghim một bản cũ bằng `"pinned": { "commit": "<sha>", "reason": "<lý do>" }`.
Khi đó `kit:sync` chép kit ở đúng commit đó (đọc từ Git), còn `kit:check` so với commit đó, không đòi bản mới nhất.
Thiếu lý do thì lệnh báo lỗi.

Game chạy `node src/kit/verify-kit.mjs` trong lệnh `check` của mình.
Script này tự đứng một mình, nên vẫn chạy khi repo game được clone riêng.
Test của game có thể gọi `verifyKit()` mà nó xuất ra: trả về danh sách lỗi, rỗng là đúng.

Kit chỉ dùng trong `vite.config.ts` và script Node: `tools/` (cần `vite`, `node:fs`). Mã chạy trong trình duyệt không import `tools/`.
