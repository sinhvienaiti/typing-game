# Làn Codex 1 · Gộp Song Long vào lab chung (giải 2 xung đột)

Anh (06/11 23:12): "sao phần side bar bên trái lại bị về như cũ r". Lab Song Long (`codex/key2-swarm-sim`) dựng từ bản game chính nên chưa có panel gọn, thanh chiêu, demo A/B, ấn Kim. Lab chung (`codex/lab-compact-panel`) thì có những thứ đó. Claude đã tạo worktree `games/.wt-ic-lab-all` (nhánh `codex/lab-all`, từ `codex/lab-compact-panel` `60e4657`) và chạy `git merge --no-commit --no-ff codex/key2-swarm-sim`. Merge dừng ở 2 file có xung đột.

**Model `gpt-6.1-sol`, mức `xhigh`.** Báo cáo: `docs/codex-queue/lane1c-report.md` (tiếng Việt, ngắn).

## Việc
1. **Giải xung đột trong `src/lab/skills-main.ts` và `src/lab/herd.ts`**, giữ **đủ cả hai phía**:
   - Phía lab chung:
     - panel gọn (bảng `SHORT`, `togglePanel`, khối `content`, phím H);
     - thanh chiêu (`SkillBar`, `refreshClipSlots`, phím I);
     - cảnh A/B (`AB_SCENE`, `HybridAB`, KTX2);
     - ấn vẽ tay (không nằm trong 2 file này nhưng không được làm hỏng);
     - âm và mọi phím 8, 9, M, K, C.
   - Phía Song Long:
     - tham số `?key2=swarm` và `?tier=`, adapter `src/lab/qi-dragon-swarm.ts`;
     - nút phím 2 khi bật swarm;
     - hai móc trong `herd.ts` (máu còn lại theo sim, giữ quái chết tới Reset).
   - Khi bật `?key2=swarm`: nhãn ngắn của phím 2 trong bảng `SHORT` là `Twin Dragons (swarm)`, và câu đầy đủ của phía Song Long làm tooltip.
2. Không sửa file nào khác, trừ khi bắt buộc để biên dịch (ghi rõ trong báo cáo).
3. **Không commit, không lệnh git ghi nào khác.** Để nguyên trạng thái merge; Claude sẽ `git add` và commit.

## Đạt khi
- Không còn dấu xung đột (`git diff --check` sạch; `grep -n "<<<<<<<\|>>>>>>>" src` rỗng).
- `npx tsc --noEmit` sạch.
- `npx vitest run --maxWorkers=4` toàn bộ qua. Ghi tổng số file và test (hai nhánh trước gộp: lab chung 46 file / 585 test, Song Long 93 file / 1.069 test).
- Báo cáo ghi các đoạn đã gộp và các tham số URL của lab chung sau gộp.

## Hết hạn mức
Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
