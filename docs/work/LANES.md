# LANES · hàng việc Codex tự chạy tiếp (từ 16/11/2026)

Anh dặn 16/11: "tạo file md, list ra các công việc của các agent để sau khi làm xong nó tự biết việc làm tiếp, chứ sao cứ để tôi kiểm tra".

Cách chạy: `tools/codex-run/dispatch.sh` chạy nền (không tốn token). Cứ 3 phút nó xem làn nào rảnh rồi lấy dòng `[ ]` đầu tiên của làn đó, chạy phiếu, đánh `[~]`. Khi có `<n>-report.md` thì đánh `[x]`. Chỉ phiếu có dòng "Phản biện: PASS" mới chạy được (cổng `run.sh`).
Claude: đọc báo cáo mới, gửi anh, viết và phản biện phiếu kế tiếp **trước khi** hàng của làn cạn. Một làn không bao giờ được để trống.
Luật làn: 1 làn ảnh luôn chạy; 2 làn code không bao giờ sửa chung file (làn A = game `games/immortality-cultivation`, làn B = lab `games/.wt-ic-lab-all`). Codex dưới 15 % hạn mức: chỉ làn ảnh.

Mỗi làn ghi rõ ai làm (Codex hay agent Claude) ngay ở tiêu đề; khi báo anh cũng nói rõ như vậy (anh dặn 16/11).
Điều phối, đọc báo cáo, viết và phản biện phiếu: Claude (phiên này) + agent Claude Sonnet làm phản biện.
Định dạng dòng: `- [ ] <mã> | <đường dẫn phiếu> | <effort>`

## Làn ẢNH · Codex (image_gen)
- [x] 396 | docs/codex-queue/396-tt-ult-metal-reference-stills.md | high
- [x] 398 | docs/codex-queue/398-tt-ult-void-blood-star-stills.md | high
- [x] 399 | docs/codex-queue/399-tt-ult-water-fire-earth-stills.md | high
- [x] 401 | docs/codex-queue/401-tt-elite-boss-icons.md | high
- [x] 405 | docs/codex-queue/405-tt-ult-light-poison-wind-stills.md | high
- [x] 407 | docs/codex-queue/407-tt-pillar-meteor-judgement-stills.md | high
- [x] 410 | docs/codex-queue/410-tt-astral-kunpeng-stills.md | high
- [x] 411 | docs/codex-queue/411-tt-hand-seal-reference-sheet.md | high
- [x] 416 | docs/codex-queue/416-tt-cutin-band-stills.md | high
- [x] 417 | docs/codex-queue/417-tt-cutin-band-shapes.md | high
- [x] 418 | docs/codex-queue/418-tt-burst-stills-55deg.md | high
- [x] 425 | docs/codex-queue/425-tt-blood-crown-stills.md | high
- [x] 429 | docs/codex-queue/429-tt-tripo-source-stills.md | high
- [x] 430 | docs/codex-queue/430-tt-metal-single-sword-src.md | high
- [x] 431 | docs/codex-queue/431-tt-ult-storyboards-batch1.md | high
- [x] 431b | docs/codex-queue/431b-tt-ult-storyboards-batch2.md | high
- [x] 435 | docs/codex-queue/435-tt-metal-rain-component-stills.md | high
- [x] 436 | docs/codex-queue/436-tt-heroine-base-and-outfits.md | high
- [x] 437 | docs/codex-queue/437-tt-formation-topdown.md | high
- [x] 436b | docs/codex-queue/436b-tt-heroine-accessories-redo.md | high
- [x] 436c | docs/codex-queue/436c-tt-heroine-jade-crimson.md | high
- [x] 436d | docs/codex-queue/436d-tt-heroine-proportion-fashion.md | high
- [x] 436e | docs/codex-queue/436e-tt-heroine-body-mature-and-looks.md | high
- [x] 436f | docs/codex-queue/436f-tt-heroine-turnarounds.md | high
- [x] 440 | docs/codex-queue/440-tt-light-burst-stills.md | high
- [x] 442 | docs/codex-queue/442-tt-thunder-bolt-stills.md | high
- [x] 443 | docs/codex-queue/443-tt-sky-formation-directions.md | high
- [x] 444 | docs/codex-queue/444-tt-sword-trail-stills.md | high
- [x] 445 | docs/codex-queue/445-tt-void-blackhole-storyboard.md | high
- [x] 446 | docs/codex-queue/446-tt-energy-sword-stills.md | high
- [x] 448 | docs/codex-queue/448-tt-giant-sword-aura-stills.md | high
- [x] 449 | docs/codex-queue/449-tt-blackhole-rim-stills.md | high
- [x] 450 | docs/codex-queue/450-tt-giant-impact-stills.md | high
- [x] 451 | docs/codex-queue/451-tt-light-ray-a2-ref.md | high
- [x] 436g | docs/codex-queue/436g-tt-heroine-base-body-v4.md | high
- [x] 451b | docs/codex-queue/451b-tt-light-lens-wedge-ref.md | high
- [x] 436h | docs/codex-queue/436h-tt-heroine-base-body-v5-appeal.md | high
- [x] 451c | docs/codex-queue/451c-tt-light-relic-mirror.md | high
- [x] 451d | docs/codex-queue/451d-tt-light-relic-mirror-light-tone.md | high
- [x] 436i | docs/codex-queue/436i-tt-heroine-v5b-hands.md | high
- [x] 436j | docs/codex-queue/436j-tt-heroine-base-v6-allure.md | high
- [x] 436k | docs/codex-queue/436k-tt-heroine-hair-card-atlas.md | high
- [x] 452 | docs/codex-queue/452-tt-star-constellation.md | high
- [~] 452b | docs/codex-queue/452b-tt-star-meteor.md | high
- [ ] 452c | docs/codex-queue/452c-tt-star-diamond.md | high

## Làn A (game) · Codex
- [x] 394 | docs/codex-queue/394-tt-typing-ui-layout-build.md | ultra
- [x] 400 | docs/codex-queue/400-tt-word-lifecycle-fx.md | ultra
- [x] 394b | docs/codex-queue/394b-tt-typing-ui-fixes.md | ultra
- [x] 394c | docs/codex-queue/394c-tt-ultimate-word-allocation.md | xhigh
- [x] 406 | docs/codex-queue/406-tt-icons-forecast-wordfx.md | ultra
- [x] 409 | docs/codex-queue/409-tt-ui-english-pass.md | high
- [x] 406b | docs/codex-queue/406b-tt-wordfx-fall-and-callout.md | ultra
- [x] 413 | docs/codex-queue/413-tt-wordfx-polish.md | high
- [x] 414 | docs/codex-queue/414-tt-burst-atlas-margin-repack.md | high
- [x] 419 | docs/codex-queue/419-tt-burst-flipbooks-batch1.md | high
- [x] 420 | docs/codex-queue/420-tt-burst-flipbooks-batch2.md | high
- [x] 428 | docs/codex-queue/428-tt-blood-crown-v4-cut.md | high
- [x] 432 | docs/codex-queue/432-tt-poison-recut.md | high
- [x] 432b | docs/codex-queue/432b-tt-poison-v5-bottom.md | high
- [x] 438 | docs/codex-queue/438-tt-cloud-shader-3d.md | ultra

## Làn B (lab) · Codex
- [x] 395 | docs/codex-queue/395-tt-ult-wood-from-stills.md | ultra
- [x] 397 | docs/codex-queue/397-tt-hero-anim-lab-round1.md | ultra
- [x] 395b | docs/codex-queue/395b-tt-ult-wood-rework.md | ultra
- [x] 402 | docs/codex-queue/402-tt-ult-metal-from-stills.md | ultra
- [x] 403 | docs/codex-queue/403-tt-hero-anim-lab-round2.md | ultra
- [x] 408 | docs/codex-queue/408-tt-ult-void-from-stills.md | ultra
- [x] 412 | docs/codex-queue/412-tt-hand-seals-from-reference.md | ultra
- [x] 415 | docs/codex-queue/415-tt-hand-rig-finger-elbow-controls.md | ultra
- [x] 415b | docs/codex-queue/415b-tt-finger-curl.md | ultra
- [x] 421 | docs/codex-queue/421-tt-wire-burst-v2-lab.md | ultra
- [x] 422 | docs/codex-queue/422-tt-burst-v2-fixes.md | ultra
- [x] 422b | docs/codex-queue/422b-tt-burst-v2-hue-orient.md | ultra
- [x] 423 | docs/codex-queue/423-tt-burst-v2-revert-and-soften.md | high
- [x] 424 | docs/codex-queue/424-tt-burst-v3-thunder-blood.md | high
- [x] 427 | docs/codex-queue/427-tt-ult-void-3d-blender.md | ultra
- [x] 426 | docs/codex-queue/426-tt-ult-metal-3d-blender.md | ultra
- [x] 433 | docs/codex-queue/433-tt-metal-sword-rain-lab.md | ultra
- [x] 433b | docs/codex-queue/433b-tt-metal-sword-rain-fix.md | ultra
- [x] 433c | docs/codex-queue/433c-tt-metal-rain-scale-camera.md | ultra
- [x] 434 | docs/codex-queue/434-tt-thunder-chain-ult-lab.md | ultra
- [x] 433d | docs/codex-queue/433d-tt-metal-rain-use-stills.md | ultra
- [x] 434b | docs/codex-queue/434b-tt-thunder-chain-fix.md | ultra
- [x] 439 | docs/codex-queue/439-tt-light-ult-eyes-loop.md | ultra (full-access, owner 17/11; chạy tay)
- [x] 439b | docs/codex-queue/439b-tt-light-ult-glow.md | ultra (full-access, chạy tay)
- [x] 439c | docs/codex-queue/439c-tt-light-ult-center-beam.md | ultra (full-access, chạy tay)
- [x] 439d | docs/codex-queue/439d-tt-light-ult-power.md | ultra (full-access, chạy tay)
- [x] 434c | docs/codex-queue/434c-tt-thunder-zigzag-trunk.md | ultra (full-access, chạy tay)
- [x] 441 | docs/codex-queue/441-tt-light-prism-burst-wire.md | ultra (full-access, chạy tay)
- [x] 434d | docs/codex-queue/434d-tt-thunder-cloud-high.md | ultra (full-access, chạy tay)
- [x] 441b | docs/codex-queue/441b-tt-light-burst-huge.md | ultra (full-access, chạy tay)
- [x] 441c | docs/codex-queue/441c-tt-light-burst-fixes.md | ultra (full-access, chạy tay)
- [x] 434e | docs/codex-queue/434e-tt-thunder-cloud-visible.md | ultra (full-access, chạy tay)
- [x] 433e | docs/codex-queue/433e-tt-metal-sword-mix.md | ultra (full-access, chạy tay)
- [x] 434f | docs/codex-queue/434f-tt-thunder-use-five-thunder.md | ultra (full-access, chạy tay)
- [x] 434g | docs/codex-queue/434g-tt-thunder-chain-thick.md | ultra (full-access, chạy tay)
- [x] 434h | docs/codex-queue/434h-tt-thunder-chain-use-c.md | ultra (full-access, chạy tay)
- [x] 443b | docs/codex-queue/443b-tt-sky-formation-simple.md | ultra (full-access, chạy tay)
- [x] 434i | docs/codex-queue/434i-tt-thunder-fork-long-strike.md | ultra (full-access, chạy tay)
- [x] 434j | docs/codex-queue/434j-tt-thunder-wide-multi-strike.md | ultra (full-access, chạy tay)
- [x] 433f | docs/codex-queue/433f-tt-metal-rain-bigger-longer.md | ultra (full-access, chạy tay)
- [x] 433g | docs/codex-queue/433g-tt-metal-replace-code-vfx.md | ultra (full-access, chạy tay)
- [x] 433h | docs/codex-queue/433h-tt-metal-trail-d.md | ultra (full-access, chạy tay)
- [x] 433i | docs/codex-queue/433i-tt-metal-energy-sword.md | ultra (full-access, chạy tay)
- [x] 433j | docs/codex-queue/433j-tt-metal-bigger-swords-formation-back.md | ultra (full-access, chạy tay)
- [x] 433k | docs/codex-queue/433k-tt-metal-giant-aura-c.md | ultra (full-access, chạy tay)
- [x] 433l | docs/codex-queue/433l-tt-metal-seven-fixes.md | ultra (Claude Opus làm, Codex <15%)
- [x] 447 | docs/codex-queue/447-tt-void-blackhole-lab.md | ultra (full-access, chạy tay)
- [x] 447b | docs/codex-queue/447b-tt-void-blackhole-3d-core.md | ultra (full-access, chạy tay)
- [x] 453 | docs/codex-queue/453-tt-light-ult-art-swap.md | ultra (full-access, chạy tay)
- [~] 453b | docs/codex-queue/453b-tt-light-mirror-size.md | ultra (full-access, chạy tay)

## Cần Claude viết phiếu (chưa vào hàng)
- Codex còn 14 % (16/11 22:30): chỉ phiếu ảnh. 428 (cắt máu -v4) giữ [h] đến khi hạn mức reset; khi đó đổi [h] → [ ].
- 426/427 tạm giữ [h]: owner 16/11 "phần blender bạn xử lý đi, tránh để giao cho codex" — agent Claude dựng GLB Kim/Hư Không trong Blender trước, rồi sửa phiếu bỏ bước Blender và trả lại làn B cho Codex nối code.
- Làn A sau 394c: thẻ dự báo đợt đè đáy ngăn Shop ở 1920 lúc chuẩn bị (x 1510–1910, y 795–925); hiệu ứng chữ 400 cho sống động hơn (bay xa hơn 22 px, nảy vàng rõ hơn), hệ dùng chung chuẩn 9.
- Kim: nếu rễ 3D Blender của Mộc đạt, làm lưỡi kiếm 3D cho Kim theo cùng cách.
- Nối icon E1 Khiên ngọc (tinh anh) và B1 Vương miện (boss) vào chỗ cắm của 394b (owner chọn 16/11), làn A sau 394c.
- Dựng 6 tuyệt kỹ (Hư Không, Huyết, Tinh Tú, Thủy, Hỏa, Thổ) theo bản Codex gợi ý, làn B sau 403; mỗi phiếu xong → Claude Opus chỉnh bằng mắt.
- Dựng tuyệt kỹ Kim (làn B) sau khi chọn ảnh 396.
- Vá theo kết quả 394 (làn A): đo che màn thật, hiệu ứng chữ bay lên/rơi xuống và mờ dần (hệ dùng chung, chuẩn 9).
- Bài học 16/11: Codex dựng VFX "mù" (sandbox không mở được trình duyệt), Mộc trượt ảnh đích 2 lần. Từ nay mọi phiếu VFX của Codex xong → agent Claude Opus chụp, so ảnh đích và tự chỉnh hình (tối đa 5 vòng) trước khi gửi anh. Áp cho 402 (Kim).
- Hoạt ảnh 397: quay lại góc chính diện để thấy thủ ấn hai tay; vòng 2 theo 393-report §8.
- 17/11 chiều, Claude sắp hết hạn mức (owner: "làm nốt cho xong r dừng để giao việc cho codex"). Đang chạy: Codex 439 (Quang, full-access), 436c (2 bộ trang phục, làn ảnh). Agent Claude Kim A/B kiếm sáng và Lôi+mây để chạy nốt. Đã dừng agent thiết kế trận pháp trên trời. Việc tiếp khi có hạn mức: (1) trận pháp trên trời: owner chê "quá xấu… góc nhìn có vẻ sai", cần phân tích + 2–3 hướng (Gemini) rồi phiếu Codex full-access dựng 3–5 lớp vòng dày nhiều độ cao; (2) gửi owner A/B kiếm Kim, Lôi, 439, 436c.
- Việc tiếp nữ chính (owner duyệt 436e 17/11): phiếu ảnh bảng 3 góc chữ A cho base-body.v3 + từng bộ, giữ mặt chan-dung-A đồng nhất → giám khảo mù 8,5 → Tripo (Claude, không Codex) → rig Blender.
- Luật dọn máy (owner 17/11, máy lag và đầy ổ): mọi phiếu/agent chụp bằng Chrome headless phải tắt Chrome khi xong (kể cả khi lỗi) và xoá thư mục profile tạm của mình (`--user-data-dir`); không chạy quá 2 phiếu có Chrome cùng lúc. Sau mỗi lượt kiểm làn, Claude kiểm Chrome headless mồ côi (PPID 1 hoặc chạy > 2 giờ) và `/private/tmp/claude-501/s/prof*`, tắt/xoá.
- Dọn rác: owner 17/11 bỏ lịch tự động, sẽ tự nhắc. Khi được nhắc chạy `tools/cleanup/nightly.sh` (xem) rồi `--apply`.
