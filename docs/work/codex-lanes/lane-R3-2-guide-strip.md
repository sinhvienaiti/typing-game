# Vòng 3 · Bước 2 · Cột Lôi: đường dẫn lên trời thành dải sét đọc được (sau `tp2=1`)

Nút thắt số 2 trong `docs/work/consult/r2-step4-verdict.md`: đường dẫn lên trời mảnh như sợi chỉ (giây 0,83–0,97). Nét tím đều, chưa chuyển được sức căng từ người tung tới cú giáng. Luật: `path-to-8.md` §7.

**Chỉ làm điểm này:**
- Thay sợi mảnh của bước R2-2 bằng **dải có texture** từ art sét có sẵn trong `art-src/lab/vfx/thunder/`:
  - ưu tiên `thunder-ribbon-loop`, hoặc dải sét khác đã nạp được. **Không dùng** `thunder-slash-arc` hay `thunder-crescent-sym`, vì log lab báo hai atlas này lỗi nạp `drawImage`;
  - **đầu sáng chạy dọc** từ tay người tung lên trời, **đuôi thon dần**;
  - bề rộng đọc được ở góc chơi, khoảng 0,5–0,8 m ở thân, mảnh dần về đuôi;
  - thời lượng nằm gọn giữa phóng và giáng, giữ đúng thời điểm giáng hiện tại.
- Lõi sáng mảnh, quầng ≤ 0,9 mỗi kênh. Không tăng bloom chung.

**Ngân sách:** như bước 1, bỏ sợi cũ khi bật dải mới. **Mức `high`.** Worktree như trên.
- **Được ghi:** `src/lab/thunder-travel-r2.ts`, chỗ nối, test, báo cáo.

**Đạt khi:**
- test node: đầu chạy đúng hướng và đúng thời gian, đuôi thon, bỏ sợi cũ, `tp2` tắt thì không đổi;
- chạy riêng các file test có liên quan.
