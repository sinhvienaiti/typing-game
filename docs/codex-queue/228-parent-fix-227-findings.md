# Phiếu 228 · Repo cha · Sửa các phát hiện của kiểm lại 227 (phiếu 214, 215, 216)

**Nguồn:**
- `docs/codex-queue/227-report.md` §"Phát hiện, từ nặng tới nhẹ". Phiếu này sửa 227-F2, F3, F4, F5, F7.
- Phiếu gốc: `214-portal-english-names.md`, `215-portal-learning-lookup.md`, `216-nginx-game-aliases.md` và báo cáo của chúng.
- Chủ dự án 30/10: Codex chạy ba làn, giao nhiều việc. Claude duyệt trước khi commit.

**Không trùng:**
- 227-F1 (16 lỗi cũ của Audio Lab) và 227-F6 (nhãn nguồn release của 217) chờ Claude quyết. Không sửa.
- 227-F8 (log của 217): không sửa.

**Báo cáo:** `docs/codex-queue/228-report.md` (tiếng Việt) và thư mục `docs/codex-queue/228/`.

## Chỉ chạy khi

1. Có `227-report.md`, `214-report.md`, `215-report.md`, `216-report.md`.
2. `git branch --show-current` là `feat/space-typing-admin-uiux`. Nhánh khác thì ghi lại, không đổi nhánh.
3. Trạng thái của `portal`, `shared/learning`, `infra/nginx`, `scripts/validate-play-mode*`:
   - Chỉ được có file chưa commit mà báo cáo 214, 215, 216 liệt kê. Đó là file đã biết.
   - Có file lạ trong các vùng đó thì dừng, ghi vào báo cáo.
   - File chưa commit ở vùng khác của repo cha (media, docs, `shared/game-kit`, `tools/audio-lab`, `docs/codex-queue`) là việc khác, không phải điều kiện dừng.
4. Lưu đầu ra của các lệnh kiểm trạng thái vào `228/status-before.txt`.

## Nơi làm

- Repo cha `/Users/toandx/htdocs/typing-game`. Mọi lệnh chạy từ gốc repo.
- Chỉ được sửa:
  - đúng các file mà phiếu 214, 215, 216 được sửa (xem mục "Nơi làm" của từng phiếu): `portal/src/**`, `portal/tests/**`, `portal/public/games.json`; `shared/learning/{core,query,message-contract,profile-backup}.mjs`, các `.d.mts`, test của chúng; `infra/nginx/typing-game.local.{play,dev}.conf`, `scripts/validate-play-mode.mjs`, `scripts/validate-play-mode.test.mjs`;
  - một changelog mới `docs/changelog/2026-10-30-fix-227.md`;
  - báo cáo và `228/`.
- Git chỉ đọc. Không dev server, trình duyệt, mạng.
- Test trước, mã sau. Chú thích tiếng Anh, ngắn. Chữ người chơi thấy là tiếng Anh.

## Việc

Mỗi phát hiện làm theo cùng trình tự:
1. đọc mục của nó trong `227-report.md` (tệp, dòng, cách tái tạo);
2. viết test đỏ tái tạo đúng ca đó, chạy và lưu đầu ra đỏ;
3. sửa ít nhất có thể;
4. chạy lại test, xanh.

1. **227-F2 (nặng, 215):** `recentSamples` lấy từ bản sao lưu hồ sơ không được mang câu trả lời ra iframe. Chỉ chuyển các trường mà hợp đồng tin cho phép (xem `message-contract.mjs` và `215-portal-learning-lookup.md`). Thêm test: bản sao lưu có câu trả lời mà tin gửi ra không có.
2. **227-F3 (vừa, 215):** `query-failed` không được chuyển tiếp nội dung lỗi hay hồ sơ. Chỉ gửi mã lỗi đã định nghĩa.
3. **227-F4 (vừa, 215):** bỏ việc parse hai lần, để id hợp lệ sau chuẩn hóa NFKC không bị báo là lỗi kho. Test với ít nhất một id có dấu tổ hợp.
4. **227-F5 (vừa, 214):** kiểm tiền tố đường ảnh sau khi giải mã hết, để tổ hợp dấu phân cách đã mã hóa (ví dụ `%2F`, `%5C`, mã hóa hai lần) không vượt được kiểm. Test từng tổ hợp trong 227.
   - Nếu 227 ghi "cần Claude xác nhận" ca nào, chọn cách chặt hơn (từ chối) và ghi rõ trong báo cáo.
5. **227-F7 (nhẹ, 216):** bỏ khoảng trắng cuối dòng trong log đỏ cũ mà 227 nêu, nếu log đó nằm trong vùng được sửa. Không thì ghi lại, không sửa.

## Kiểm (bắt buộc; điều phối cho phép chạy build và toàn bộ test)

1. Test của portal (`portal/tests`), của `shared/learning` và `scripts/validate-play-mode.test.mjs`. Ghi số trước và sau.
2. Gói portal: chạy lệnh build mà 214 dùng, ghi byte trước và sau.
3. `node scripts/validate-play-mode.mjs` như 216, nếu chạy được không cần nginx thật.
4. Đột biến: tắt từng bản sửa F2–F5 thì test mới tương ứng phải đỏ. Ghi kết quả.
5. `git status --short -uall` sau khi làm, lưu vào `228/status-after.txt`. Phần chênh so với lúc đầu chỉ được nằm trong vùng ở mục "Nơi làm".

## Báo cáo

- Mỗi phát hiện: test đỏ, bản sửa (tệp:dòng), test xanh, đột biến.
- Số của mục Kiểm.
- Ca nào chọn cách chặt hơn.
- Việc còn cho Claude (F1, F6).
