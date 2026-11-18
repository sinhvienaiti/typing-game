# BOARD · Tu Tiên (cập nhật 06/11/2026, 00:10)

**16/11/2026:** hàng việc Codex theo làn nằm ở `LANES.md`; `tools/codex-run/dispatch.sh` tự chạy phiếu kế tiếp khi một làn rảnh. Phần dưới là bảng cũ 06/11, chờ dọn.

Luật: tối đa 3 việc đang làm. Mỗi việc kết thúc bằng bản chơi (hoặc bước lab anh đã duyệt) cùng video trước/sau. Cách dùng: `README.md`.

**Lịch:** rà soát 23:00 mỗi ngày (cron chỉ sống trong phiên điều phối; chuyển phiên thì đặt lại). Định dạng: `review/README.md`.

**Firefly (11/11 23:5x, anh):** dùng `https://firefly.adobe.com/video-generate` (giao diện mới, báo giờ mở lại khi bị giới hạn). Giới hạn dùng thử ≈ 70 bản/ngày (11/11: 68 bản rồi chặn 22:03; 12/11: 72 bản rồi chặn 13:37). Mở lại 07:00 hôm sau. Bộ chạy đã sửa cho chu kỳ ngẫu nhiên 3–5 phút; trang cũ vẫn tạo được. Bộ chạy cần sửa cho giao diện mới trước lượt sau. **Model:** chỉ Fable 5.1 ở mọi phiên; effort theo việc.

## Đang làm (tối đa 3)
| Việc | Trạng thái | Kế tiếp | File |
|---|---|---|---|
| **Firefly tối 05/11 (ưu tiên 1)** | Anh duyệt danh sách (16:35, 8 hệ), thêm cột trụ và 6 hệ mới (16:58), duyệt 14 ảnh Gemini (17:08). Đang chạy: ChatGPT ảnh, video Firefly 2 làn (ảnh → video trước), âm Firefly | Anh duyệt → ảnh 2D (ChatGPT + Gemini) → anh chấm → ảnh → video, âm trước ~23:00 | `../games/tu-tien/skills/PRODUCTION_LIST_2026-11-05.md`, `tasks/skill-stills-0511.json`, `tasks/element-video-0511.json` |
| Song Long: bầy rồng khí (phím 2) | Anh duyệt hình (15:35) và cách gây sát thương (16:00): rồng lướt qua quái nào trúng quái đó, sim tự vạch đường 5 con qua đám quái đông, sóng xung kích lúc thả, nổ ngọc cả sân có trần. Lab `claude/dragon-swarm-lab` `6b9f26c` (1,3×, làm ấm, 106 test chuyển động) | Vòng ChatGPT → Gemini (đang chạy) → kế hoạch → phiếu Codex sim (đường, nhịp, sự kiện, test, cân bằng) → presenter view | `tasks/twin-dragons.md`, `consult/key2-qi-swarm-wiring-study.md` |
| Lô 1 Hỏa + cổng 7 | Nhánh `codex/fire-lot1-art` đã gộp main (`672f2e7`, 1028 test). Cổng 7 còn trượt nhẹ; 291 sửa khóa bóng Kim (số đèn điểm) | Agent đo cổng 7; đạt thì commit 291 và fast-forward `main` của game | `tasks/key1-fire.md` |
| Vòng ngọc Clear Wind | Dừng (lần 3 chưa đạt; số nghiệm thu tự mâu thuẫn) | Nghĩ lại mục tiêu + hỏi Gemini sau việc rồng | `tasks/jade-ring.md` |

## Hàng chờ Codex
297 làm ấm số sát thương (đang chạy 16:19). 293 đỗ tới mai: phản biện vòng 2 FAIL (vòng chờ ra ngoài sân), vòng 3 nghĩ lại nhịp (`tasks/twin-dragons.md`).

- **Việc mới anh duyệt 22:20 ("Duyệt cả 3", sau bản học video `skills/REF_VIDEO_LESSONS_2026-11-05.md`):** bộ đếm chuỗi từ D60 (`tasks/streak-counter.md`), chiêu duy trì D61 (`tasks/channel-skill.md`): đang hỏi Gemini (`consult/streak-channel-gemini.md`); sao băng nghiêng D62 (`tasks/slanted-meteor.md`): dựng từ clip có sẵn từ mai.

- **06/11 00:05 anh tự chấm; biến các mục lab thành kỹ năng dùng được** (`tasks/lab-castable-skills.md`): đợt 1 phím 8 (lab-element-kits đang làm), bảng 30 kỹ năng (lab-flipbooks đang soạn), rồi A, C, D, B, sau đó D62, D61, D60.

## Chờ anh
- Duyệt danh sách Firefly tối nay (3 câu hỏi cuối file).
- Tốc độ rồng 1,3× (đã áp, chưa xác nhận).

## Đỗ lại
- Đầu rồng sạch (`qi-dragon.v2-try1/2`): anh không muốn vẽ lại (15:35); chỉ lưu.
- Âm 285 (gộp tiếng, ép bus): chưa đạt cổng 3 LU; cần stem cao trào to hơn (thiết kế âm, cho anh nghe).
- Sửa cut-in (phiếu 268). Mặt nạ vẽ A5, A6, A8–A10; vết cháy Hỏa (lô 2 thay hình vẽ bằng mã: chờ chấm ứng viên).
- Cân bằng Song Long: sẽ đo lại theo thiết kế mới (bot Chuẩn thắng 15 %, phím 2 chiếm 45,99 % ở thiết kế cũ).

## Xong hôm nay (05/11)
- 09:22: 275 và 279 nhát chém kết phím 7 Hỏa bằng dải lửa thật (`bbb46d8`).
- 14:20–15:05: 286 commit, gộp main vào lô 1 (`672f2e7`), 287b giải xung đột.
- 15:00–15:45: rồng khí 3D v1→v4 (Tripo từ ảnh 3, vảy vẽ, ngọc, hết xoắn, hết giật; 288/289 test và sửa chuyển động; 290 làm ấm).
- Firefly: sprint âm, video W2, tiếng hô, flipbook (sáng sớm).

## Dừng lúc 14h 18/11 (lệnh owner: chỉ giữ 1 Codex ảnh, 1 agent Claude lab Metal, Claude điều phối)
- Thunder 434l (agent Claude Opus): đang làm gân mây đọc được (phủ ≥ 8 % dải), dừng trước vòng chụp đầu (script lỗi cú pháp, chưa chạy). Chưa có `thunder-art-l`, chưa có `434l-report.md`. Làm tiếp: sửa script, chụp, đo.
- Star plan (agent Claude Opus): đã có `docs/work/tasks/star-ult-plan.md` và phiếu `452-tt-star-constellation.md`; chưa kiểm hết bộ phiếu 452, chưa phản biện, chưa xếp làn.
- Light: owner chọn tia A2 mẫu B (light-ray-a2.v1-try2.png); chờ nối vào lab (agent lab duy nhất, sau Kim).
- Nữ chính: phiếu 436g (thân nền v4, làm trước thời trang) đã PASS, xếp làn ảnh sau 451; thời trang làm sau.
