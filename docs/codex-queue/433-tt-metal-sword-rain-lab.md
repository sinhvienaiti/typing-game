# Phiếu 433: Tuyệt kỹ Kim dựng lại — trận pháp trên trời rồi mưa kiếm rơi (bản lab đầu)


Phản biện: PASS (Sonnet, 17/11)
**Owner miễn luật hạn mức (nguyên văn 16/11):** "tôi đã nói cứ cho codex làm đi, tôi sẽ reset codex sau"; 17/11: "cho codex làm việc đi, nó vẫn còn kìa".

## Bối cảnh
Owner 17/11 chê bản vành kiếm mọc từ đất: "tại sao cứ phải đi từ mặt đất… hệ kim, tạo ra 1 vòng trận pháp, sau đó triệu hồi mưa kiếm rơi xuống không phải đẹp sao". Thiết kế: `docs/games/tu-tien/ULT_CHOREOGRAPHY.md` dòng Kim. Bảng phân cảnh 2D đang vẽ (phiếu 431); bản lab này dùng để owner thấy chuyển động, sẽ chỉnh theo phân cảnh sau.

## Việc (worktree `games/.wt-ic-lab-all`, file mới `src/lab/metal-ult-rain.ts`, nối vào chỗ tung Kim trong `src/lab/metal-ult-layered.ts` thay cho vành kiếm mọc đất; giữ vành cũ bật được bằng `?metalUlt=ring`)
1. **Tụ lực (0–0,6 s):** vòng trận pháp hiện trên không trung, cao 9–12 m phía trên đám quái, nằm ngang, xoay chậm, sáng dần. Dùng ảnh có sẵn `games/.wt-ic-lab-all/art-src/lab/vfx/metal/metal-caster-seal.*` (atlas/khung tĩnh xoay bằng code); không vẽ hình bằng code.
2. **Mưa kiếm (0,6–2,4 s):** 3 đợt kiếm rơi thẳng xuống từ vòng trận, mỗi đợt 12–20 thanh, mũi hướng xuống, có vệt sáng ngắn phía sau (ribbon hoặc thẻ kéo dài, mỗi kênh ≤ 0,9). Mô hình: `art-src/lab/vfx/metal-ult/models3d/tripo/ult-metal-sword.tripo.v1.glb` (InstancedMesh, vật liệu thép bạc + vàng PBR). Rơi nhanh có gia tốc, nhắm vào vị trí quái (seed cố định) cộng vài thanh rơi lệch.
3. **Trúng (mỗi thanh):** cắm xuống đất nghiêng nhẹ, lóe tia ở điểm chạm (dùng `metal-impact-v2` có sẵn), quái trúng giật lùi + số sát thương (dùng đường sát thương có sẵn của chiêu).
4. **Điểm nhấn (2,4 s):** một thanh kiếm lớn (cùng mô hình, ×3) rơi xuống giữa trận, nổ `metal-big-burst-v2`.
5. **Dư âm (2,4–4 s):** các thanh kiếm tan thành bụi vàng (dissolve shader) rồi biến mất; vòng trận mờ dần.
Âm thanh: dùng thư viện âm Kim có sẵn (`metal-ult-sound.ts`): tiếng kiếm rít khi rơi, va chạm, nổ cuối.

## Nghiệm thu
- Kiểm kiểu strict 0 lỗi; probe CPU: số kiếm mỗi đợt, đợt đúng giờ, mọi kiếm được trả về pool sau 4 s, xoá/tung lại 5 lần không rò; vành cũ bật bằng `?metalUlt=ring`.
- Để lệnh chụp cho Claude: góc trên và sau lưng ở 0,4 s / 1,2 s / 2,4 s / 3,2 s; p95 `stress.html` 100 quái ≤ 16,7 ms.
- Chỉ sửa trong worktree `src/lab/metal-ult-*` (file mới + chỗ nối), không đụng file khác. Không commit, không media vào Git, không đổi nhánh.

## Giao nộp
`docs/codex-queue/433-report.md`.
