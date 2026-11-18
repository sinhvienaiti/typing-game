# Phiếu 397: Hoạt ảnh nhân vật, đợt 1 trong lab (một chiêu kiếm trên rig `human`)


Phản biện: PASS (Sonnet, 16/11, vòng 2)
## Bối cảnh
Owner 16/11/2026 giao Codex làm hoạt ảnh nhân vật: "khi typing nhân vật sẽ có những animation nào… thủ ấn, cử động chân tay… mềm mượt đẹp và đa dạng". Nghiên cứu: `393-report.md` (đọc §3, §4, §5.1–5.2, §6, §8 dòng "Đợt 1", §9). Hoạt ảnh nhân vật là hệ dùng chung, chuẩn cuối 9; đợt này chỉ là lát thử kỹ thuật, không phải nghiệm thu.
Owner 16/11: "đảm bảo những nhân vật, quái đạt chất lượng rồi mới đưa vào làm 3d và rig" — vì vậy đợt này **chỉ dùng rig `human` có sẵn**, không làm model mới, không rig model Lam, không dùng Tripo.

## Thứ tự
Phiếu này nằm sau 395 trong cùng làn B (`docs/work/LANES.md`), nên chỉ chạy khi 395 đã xong; hai phiếu không chạy song song trên `skills-main.ts`. Đọc lại `skills-main.ts` hiện tại trước khi nối phím, giữ nguyên phần nối của 395.

## Việc (worktree `games/.wt-ic-lab-all`)
1. Trên rig `human` (66 khớp, đủ ngón): một clip **Kiếm A** đủ ba nhịp gồng → nhả → thu, hai thủ thế S0 và S1 (theo bảng thủ ấn §4), ba "xung chữ" nhỏ khi gõ từng chữ đúng (cộng dồn, không lặp đơn điệu), phản ứng gõ sai, huỷ và đổi đích. Idle hiện có giữ nguyên.
2. Làm clip bằng Blender có sẵn (`/Applications/Blender.app/Contents/MacOS/Blender --background --python …`) hoặc key pose bằng code trong lab; ghi rõ cách đã chọn. Không Mixamo, không auto-rig Tripo. Xuất GLB/clip vào `art-src/lab/anim/round1/`.
3. Nối vào lab: một phím mới (ghi trong báo cáo) để gõ thử một từ và xem nhân vật tụ lực theo từng chữ, chữ cuối phát chiêu ≤ 50 ms; dùng VFX và âm đã có để đối nhịp, không tạo look mới. Sự kiện clip (release, hit) phát cùng khung với VFX, âm, camera.
4. Lớp thủ tục theo §6.2: thở, nghiêng hông theo hướng đích, nhìn đích; chuyển trạng thái không bật, không trượt chân, không về bind pose.

## Nghiệm thu
- Kiểm kiểu sạch; probe đo độ trễ phím→phát chiêu (mục tiêu ≤ 50 ms) ở 60 Hz; kiểm không bind/trượt.
- Ảnh hoặc clip ngắn ở camera chơi và góc tay cận trong `typing-game-review/owner-review/2026-11-16/tu-tien/hero-anim-r1/` có `ABOUT.md`; nếu sandbox chặn trình duyệt, ghi rõ và để lệnh chụp cho Claude.
- Chỉ sửa trong `games/.wt-ic-lab-all`: file mới trong `src/lab/anim-r1-*.ts`, chỗ nối phím trong `src/lab/skills-main.ts`, `art-src/lab/anim/round1/`. Không đụng `ice-ult-*`, `wood-ult-*`, `src/view/`, `src/ui/`. Không commit, không media vào Git, không đổi nhánh.

## Giao nộp
`docs/codex-queue/397-report.md`: cách làm clip, phím lab, số đo, điểm yếu tự thấy.
