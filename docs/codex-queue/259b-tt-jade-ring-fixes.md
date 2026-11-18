# Phiếu 259b · Tu Tiên · Code: vòng ngọc, bổ sung phần phiếu 259 sửa sau và mở tham số để Claude chỉnh cho giống ảnh đã duyệt

**Loại việc:** code (`gpt-6.1-sol`, mức `xhigh`). Phiếu ngắn theo luật làm gọn (05/11). Không cần phản biện: theo luật làm gọn 05/11 (skill `agent-orchestration`, "Working lean" mục 6), phiếu code ngắn, chỉ phần nhìn, không đụng sim, canon hay cân bằng thì Claude soát là đủ; lần dừng trước của Codex là đúng theo phiếu cũ. Claude bỏ điều kiện này lúc 01:38 ngày 05/11. Làm ngay.

**Báo cáo:** `docs/codex-queue/259b-report.md`.

**Bối cảnh:**
- Mã 259 (worktree `games/.wt-immortality-cultivation-codex`, nhánh `codex/jade-ring-material`, chưa commit) làm theo phiếu **trước** lần sửa lúc 20:32.
- Claude kiểm trong trình duyệt (05/11, khoảng 00:05): đạt Kiểm 6, 7 và 11; trượt Kiểm 8, 9 và 10. Chi tiết ở `docs/codex-queue/259-report.md`, mục "Claude kiểm" (Claude thêm khi gộp).
- Nhìn bằng mắt:
  - Hỏa: ngọc trắng đúng ý.
  - Kim: đĩa phẳng, hơi xám, mất nét chạm và độ bóng của ảnh đã duyệt `art-src/weapons/clearwind-src3q.v4-try1.png`. Độ sáng đo được 0,825 → 0,808.

## Việc
1. **Làm nốt phần phiếu 259 hiện tại mà mã còn thiếu.** Đọc lại `docs/codex-queue/259-tt-jade-ring-material.md` bản hiện tại: §2, §4, §5 và Kiểm 8.
   - trần 0,95 dùng trọng số Rec. 709, không phải 601;
   - ánh sáng mép khi tan (`swRingDe`) giữ ngoài trần;
   - nhánh đọc trọng số `uSwRingOn > 1.5`;
   - `__lab.ringCap()`;
   - `MASK=1` và `ring-parity.mjs` ghi `ringCap`;
   - test kiểm ba dòng trần.
2. **Chặn tràn ra mép.** Ở tam giác gần như nghiêng hẳn, `fwidth` làm mép mềm của phép thử vòng giãn rất rộng, nên trọng số nhỏ tràn ra ngoài vòng: 18–23 điểm ảnh ngoài mặt nạ khi bloom 0.
   - Kẹp bề rộng mềm `swAr`, `swAz` ở tối đa 1,5 lần bề rộng một texel của ô vòng.
   - Ghi trong báo cáo công thức đã dùng.
3. **Mở tham số để Claude chỉnh nét trong lab** (Codex không tự chỉnh nét):
   - uniform kèm cờ lab: `jadeAlbedo` (hệ số độ sáng nền ngọc, mặc định giữ số hiện tại), `jadeRough` (độ nhám), `jadeNormal` (độ nổi của normal map trong vùng ngọc, mặc định 1), `jadeSheen` (lớp bóng mặt trên, kiểu clearcoat giả, mặc định 0), `jadeGlow` (đã có);
   - đặt qua `?jadeAlbedo=…` và qua `__lab.jadeRing({ albedo, rough, normal, sheen, glow })`; `__lab.jadeRing()` không đối số trả về giá trị đang dùng;
   - `jadeSheen > 0` cộng một vệt phản chiếu hẹp theo GGX với độ nhám 0,12, chỉ trong mặt nạ ngọc, đi qua bộ giới hạn headroom có sẵn;
   - mọi tham số ở mặc định cho ảnh **trùng từng điểm ảnh** với mã 259 hiện tại, trừ thay đổi của mục 1 và 2.

### Được ghi
Đúng các file phiếu 259 đã cho ghi, trong cùng worktree, cộng `docs/codex-queue/259b-report.md`.

### Cấm
Như phiếu 259: lệnh git ghi; file khác; Vitest hay Vite thiếu cờ `--no-cache --configLoader runner`; cổng mạng.

## Kiểm bắt buộc
1. tsc không lỗi; Vitest đủ, mọi test qua.
2. Build tạm như phiếu 259, grep `jadeRingGlow\|ring-parity\|jadeSheen` không ra gì; xóa thư mục build.
3. Test mới cho mục 2: phép kẹp mềm trên bộ số tổng hợp có góc nghiêng 85°, trọng số ngoài vòng bằng 0.
4. `git status --short`: chỉ các file được ghi.

## Claude làm sau
- Chỉnh `jadeAlbedo`, `jadeRough`, `jadeNormal` và `jadeSheen` trong lab, so với ảnh đã duyệt ở cận cảnh và camera chơi, cho tới khi đạt Kiểm 9: L ≥ cũ + 0,04 và tỉ số IQR ≤ 0,75.
- Ghi bộ số làm mặc định (một commit nhỏ), chạy lại Kiểm 8, gửi anh tấm so.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
