# Phiếu 433n: báo cáo (Claude làm thay Codex vì Codex hết lượt)

18/11/2026. Gắn 3 tài nguyên owner đã duyệt vào chiêu mưa kiếm Kim. Làm 3 vòng: sửa → chụp Alt+1 và Alt+2 (`?ground=%23353a40`) lúc kiếm lớn chạm đất và +0,3 / +0,8 / +1,5 s → xem ảnh.

## Đã sửa
- **Kiếm lớn không đế** (`metal-ult-rain.ts`, `metal-ult-energy-a.ts`): chỉ kiếm lớn nạp `ult-metal-sword.nobase.v2.glb`, dùng hình và vật liệu gốc của file đó. Hào quang C và vệt D giữ nguyên. GLB mới chung hệ toạ độ với v1, nên mình chuẩn hoá nó bằng khung bao của v1. Lưỡi kiếm giữ đúng cỡ và độ cắm như cũ, mũi kiếm vẫn ngập dưới đất. Kiếm nhỏ vẫn dùng v1, phần đế của chúng bị chôn 20 %.
- **Kiểm tra đá theo ghi chú owner:** `grep` chỉ thấy v1 được nạp ở `metal-ult-rain.ts`, chỗ này đã đổi cho kiếm lớn. Bản `metal-ult-3d.ts` cũ cũng nạp v1, nhưng chế độ `layered` không dùng bản đó. Không có file nào nạp `ult-metal-clean`. Cũng không có lớp đá riêng nào, dù là flipbook mảnh vụn hay mesh. Ảnh chụp lúc chạm đất ở cả hai góc không còn thấy khối đá.
- **Sóng vàng A** (`art-src/lab/vfx/metal-ult/impact-wave-a.png`): lấy từ ảnh tĩnh đã duyệt, nền đen được cắt thành alpha. Lớp này là mặt phẳng nằm trên đất trong không gian thế giới, cộng sáng, đặt giữa điểm kiếm lớn chạm đất. Nó phóng đều từ 0,3× lên 1× trong 0,35 s rồi mờ dần trong 0,6 s. Đường kính cuối khoảng 1,4 × bán kính trận, tức khoảng 11 m.
- **Nứt dung nham B** (`impact-crack-b.png` phủ thường, `impact-crack-b-glow.png` cộng sáng; cả hai lấy từ cùng một ảnh): lớp nứt nằm phẳng dưới chỗ chạm. Ánh dung nham sáng trong 0,8 s, sau đó nguội dần trong 1,2 s: màu chuyển sang đỏ tối rồi tắt. Đường nứt sẫm lại và còn đến khoảng 2,6 s.
- **Thứ tự lớp:** nứt (8,2 / 8,4) < sóng (8,6) < bụi Explosion01 (10).
- **Bụi nổ theo ghi chú owner:** thu đều còn 65 % (26 → 17 m, tâm hạ từ 10 xuống 6,5 m), độ đậm còn 0,6 lần (0,85 → 0,51).
- Không lớp nào được vẽ bằng code. Code chỉ đặt vị trí, xoay, phóng đều, nhuộm màu và làm mờ.

## Số đo (vòng 3)
- Vùng trắng **0,0001 %**, ngưỡng ≤ 6 %. p95 **6,0 ms**; dùng tối đa 212 draw call. Kiểm kiểu **0 lỗi**.
- Vòng 1: sóng A quá mờ (độ đậm 0,8, tint mặc định). Vòng 2 và 3: tăng tint sóng lên (2,6; 1,85; 0,9) và ánh nứt lên (2,4; 1,45; 0,55).

## Tệp
- Gửi owner: `typing-game-review/owner-review/2026-11-18/tu-tien/metal-rain-n.jpg` và `.mp4` (6,875 s, có âm). Đã thêm dòng vào `ABOUT.md`.
- Driver: `games/.wt-ic-lab-all/src/lab/metal-ult-rain-n-review.mjs`.
- Đã xoá khung thô. Chrome headless đã đóng và đã xoá profile tạm. Server 3148 vẫn chạy. Không commit.

## Owner xem
- Sóng A ở 0,35–0,95 s phần lớn nằm dưới bụi nổ, vì bụi phủ lên trên theo đúng thứ tự yêu cầu. Nó thấy rõ nhất ở khoảng 0,1–0,3 s đầu.
- Ở Alt+2, chỗ chạm cách người chơi khoảng 9 m nên nứt bị quái che nhiều.
