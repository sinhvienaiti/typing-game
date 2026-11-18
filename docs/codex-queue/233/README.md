# Bằng chứng phiếu 233

Đọc kết luận ở [233-report.md](../233-report.md). Mọi script chạy từ gốc repo cha; không chạy lại sau khi dọn nếu chưa dựng bản chép mới. Không dùng runner của 228/229 trực tiếp vì chúng có thể ghi vào mã gốc.

## Thứ tự đã dùng

1. Kiểm điều kiện chưa có đầu ra, nhánh và hai báo cáo; lưu status/hash vào `before.json`. Chép file Git và toàn bộ public theo mục “Dựng bản chép” của 224; kết quả `copy.json`. Portal chép portal/shared/scripts/nginx/package và nguồn `games/space-typing/src` cần cho import kiểu; thêm `play.sh` cho validator. Mọi bản chép nằm dưới hai đường tạm của 233.
2. `python3 docs/codex-queue/233/run.py parent portal-tests node --test portal/tests/*.test.mjs`
3. `python3 docs/codex-queue/233/run.py parent learning-tests node --test shared/learning/*.test.mjs`
4. `python3 docs/codex-queue/233/run.py td td-check pnpm check` và `td-golden pnpm td:golden:check`.
5. Portal build và validator: runner với chế độ `portal`, cwd luôn là cây sao chép. Argv cụ thể trong JSON cùng tên log.
6. `python3 docs/codex-queue/233/mutate.py parent` và `python3 docs/codex-queue/233/mutate.py td`: 4 + 6 đột biến, trả file bằng finally, kiểm hash và chạy xanh sau từng lần.
7. Probe repo cha: `run.py portal parent-variants-final node --test ../../docs/codex-queue/233/parent-probe.mjs`. Mã **1**, **43 xanh/10 đỏ** là kết quả có chủ đích ghi nhận F2 còn thiếu; không phải bộ hồi quy gốc đỏ.
8. Chép `td-variants.test.ts` vào `tree/tests/codex-233-variants.test.ts`, chạy `run.py td td-variants-final pnpm exec vitest run tests/codex-233-variants.test.ts`: **21 xanh**. Chỉ file probe trong bản chép được thêm, không sửa test sản phẩm.
9. `python3 docs/codex-queue/233/release.py`: production/bản nhà và kiểm âm tính bản nhà; inventory, byte/hash, quét host/prefix. `audit.py` kiểm phạm vi, F7, CLI và so gói với 229.
10. `portal-delta.py` build chín file trước 228 từ bản tái dựng đã khớp hash, đo +401 byte rồi trả nguyên byte; không sửa cây gốc. `finish.py` kiểm bảo toàn, xóa probe riêng trong bản chép, lưu status/hash cuối và xóa đúng hai cây tạm.

## Cách đọc log

Mỗi lệnh runner có `.log` và `.json` ghi argv, cwd, biến portal, mã thoát, thời gian. `mutated` phải đỏ; `restored` phải xanh. Các JSON tổng hợp `scope-review`, `integrity`, `cleanup`, `pack-comparison`, `portal-delta` là điểm bắt đầu đối chiếu.

Các log đầu `portal-build`, `validator-tests`, `parent-variants`, `td-variants` ghi lỗi dựng bản chép/probe đã được giải thích trong báo cáo. Dùng các lượt retry/final để lấy kết quả hiện hành. Không có dist, ảnh chụp hoặc âm thanh ở đây.
