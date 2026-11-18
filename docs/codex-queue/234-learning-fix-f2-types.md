# Phiếu 234 · Repo cha · Vá nốt 227-F2: mẫu học trả ra iframe phải đúng kiểu, không mang câu trả lời lồng bên trong (P1-233-01)

**Nguồn:**
- `docs/codex-queue/233-report.md` §3, phát hiện **P1-233-01**: "F2 còn thiếu".
- Bản sửa 228 chỉ lọc các trường dư ở cấp đầu (`shared/learning/query.mjs:278`–`:283`), chưa kiểm kiểu giá trị.
- Ca hỏng mà 233 tái tạo được:
  - dựng hồ sơ hợp lệ bằng `applyLearningEvents`;
  - thay `recentSamples[0].gameId` bằng `{userAnswer:"PRIVATE_NESTED_USER_ANSWER",expectedAnswer:"PRIVATE_NESTED_EXPECTED_ANSWER"}`;
  - `parseLearningProfileBackup(JSON.stringify(profile))` vẫn nhận hồ sơ đó;
  - lookup hay query qua `ParentLearningBridge.handleMessage` trả ra nguyên hai câu trả lời.
  - Cả năm trường mẫu đều bị, mỗi trường qua hai đường tin: 10/10 đỏ.
- Bằng chứng: `233/parent-probe.mjs`, `233/parent-variants-final.log`.
- Phiếu gốc `215-portal-learning-lookup.md` (hợp đồng tin), `228-parent-fix-227-findings.md`.

**Không trùng:** 228 đã sửa F3, F4, F5 đúng (233 xác nhận). Phiếu này chỉ vá F2. Không đổi chính sách `recentMistakes` hay `recentAnswers`.

**Báo cáo:** `docs/codex-queue/234-report.md` (tiếng Việt) và thư mục `docs/codex-queue/234/`. Model `gpt-6.1-sol`, mức `high`.

## Chỉ chạy khi

1. Có `233-report.md` và `228-report.md`.
2. Nhánh `feat/space-typing-admin-uiux`.
3. `git status --short -uall -- shared/learning portal`:
   - chỉ có các đường của 214, 215 và 228 (đối chiếu ba báo cáo). Đó là file đã biết.
   - Có đường lạ thì dừng, ghi vào báo cáo.

## Nơi làm

- Repo cha, chạy từ gốc.
- Chỉ được sửa:
  - `shared/learning/query.mjs`, `profile-backup.mjs`, `core.d.mts`, `query.d.mts` nếu cần, và test của chúng;
  - `portal/src/learning/bridge.ts` và `portal/tests/learning-bridge.test.mjs` nếu cần;
  - changelog mới `docs/changelog/2026-10-30-learning-sample-types.md`;
  - báo cáo và `234/`.
- Git chỉ đọc. Không dev server, trình duyệt, mạng.
- Test trước, mã sau. Chú thích tiếng Anh, ngắn.

## Việc

1. **Test đỏ trước.** Dựng lại đúng các ca của 233: object hay array trong từng trường của mẫu, qua cả lookup và query, với cả hồ sơ nhập từ sao lưu lẫn hồ sơ đã lưu. Lưu đầu ra đỏ.
2. **Đường trả dữ liệu:**
   - dựng mỗi mẫu chỉ từ năm trường của hợp đồng, mỗi trường phải đúng kiểu nguyên thủy mà `core.d.mts` khai báo (chuỗi, số…);
   - mẫu có trường sai kiểu thì **bỏ cả mẫu**, không ép kiểu, không cắt chuỗi;
   - việc này bảo vệ cả hồ sơ đã lưu từ trước.
3. **Nhập sao lưu:** `parseLearningProfileBackup` kiểm kiểu `recentSamples` theo cùng luật. Mẫu sai kiểu thì bỏ, và ghi số mẫu bị bỏ vào kết quả nếu hàm đã có chỗ báo cáo; không thì chỉ bỏ.
4. **Đột biến:** tắt riêng từng bước 2 và 3 thì test mới phải đỏ.

## Kiểm (bắt buộc)

- Test của `shared/learning` và `portal/tests`: số trước và sau. Chạy lại `233/parent-probe.mjs` nếu chạy được, ghi số.
- `git diff --check` sạch trên các file đã sửa.
- `git status --short -uall` sau khi làm, lưu `234/status-after.txt`. Phần chênh chỉ nằm trong vùng ở mục "Nơi làm".

## Báo cáo

- Ca đỏ, bản sửa (tệp:dòng), ca xanh, đột biến, số test.
- Kết luận: F2 đã đóng hay chưa.
