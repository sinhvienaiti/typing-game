# Danh sách dựng 3D bằng Tripo

**Chủ dự án, 01/11/2026 khoảng 03:50:**
- Claude dùng Firefly làm ảnh 2D rồi Tripo dựng 3D, **ưu tiên API** (khoảng 1.000 credit).
- "Chắc chắn xác nhận đầy đủ r hãy tạo vì credit có giới hạn rất ít."
- Face: "đừng có chơi số face ở mức cao nhất, nó chỉ nên được nâng cao hơn để đẹp hơn so với trước" (các đợt trước chỉ 2–4k).

## Cấu hình (đã kiểm bằng `--dry-run`, không tốn credit)

```
tripo generate image-to-model <ảnh nguồn> -p texture_quality=detailed -p pbr=true -p face_limit=<theo bảng> -o <thư mục tạm> --name <tên>
```

- Model `v3.1-20260211`, texture HD, PBR. Không dùng smart low-poly, không quad.
- Geometry để `standard`. Mức `detailed` tốn thêm 20 credit; chỉ cân nhắc cho nhân vật chính nếu lần thử đầu cần.
- Giá theo tài liệu Tripo: **40 credit một model**.
- Ví API hiện có **970 credit** (`tripo balance`). Ví web là ví riêng, dùng sau khi hết ví API.

## Chốt trước khi bấm dựng (mỗi model)

1. Ảnh nguồn đã được hai giám khảo mù cùng cho từ 8,5, kể cả điểm "hợp làm nguồn Tripo":
   - một khối liền, chân phẳng, góc ba phần tư nhìn từ trên khoảng 30°;
   - không có nền đất, bóng hay viền màu khóa.
2. Chạy `--dry-run` lại và đối chiếu: model, texture, PBR, `face_limit` đúng bảng.
3. Dựng **một model trước**, kiểm số tam giác, các map và vòng quay trong Blender, rồi mới dựng tiếp.
4. Ghi credit trước và sau vào bảng dưới.

## Danh sách

| # | Game | Model | Ảnh nguồn | Trạng thái nguồn | face_limit | Credit | Kết quả |
|---|---|---|---|---|---|---|---|
| 1 | Dragonhold | Cổng ải `hold-gate` | `games/dragon-hold/art-src/landmarks/hold-gate.png` (phiếu 124) | Đang chấm mù 8,5 | 50.000 | 40 | — |
| 2 | Dragonhold | Tường ải `hold-wall` | `landmarks/hold-wall.png` | Đang chấm | 30.000 | 40 | — |
| 3 | Dragonhold | Tháp canh `watchtower` | `landmarks/watchtower.png` | Đang chấm | 35.000 | 40 | — |
| 4 | Dragonhold | Tượng rồng `dragon-statue` | `landmarks/dragon-statue.png` | Đang chấm | 50.000 | 40 | — |
| 5 | Dragonhold | Vòm đổ `ruined-arch` | `landmarks/ruined-arch.png` | Đang chấm | 25.000 | 40 | — |
| 6 | Dragonhold | Chậu lửa `brazier` | `landmarks/brazier.png` | Đang chấm | 12.000 | 40 | — |
| 7 | Last Line | Nữ xạ thủ (Lightbearer) | Firefly, 4 góc khớp `results-lose-bg.png` (`QUALITY_RESCUE` §4.4) | Chưa có, Claude làm | 50.000 | 40 (multiview) | — |
| 8 | Last Line | Drone hỗ trợ | Firefly, 4 góc | Chưa có | 25.000 | 40 | — |
| 9–13 | Last Line | 5 súng cầm tay: Pulse, Heat Beam, Scatter, Rail, Star Mortar | Firefly, ba phần tư | Chưa có | 15.000 mỗi súng | 5 × 40 | — |

Tổng dự kiến 13 × 40 = **520 credit**. Còn khoảng 450 credit cho làm lại, hoặc nâng geometry `detailed` cho nhân vật.

Model dựng xong lưu ở `art-src/3d/` của từng game. Claude dọn và rig trong Blender, chấm trong bản chơi ở mức 8,5. Runtime giữ đúng sàn của MODEL_QUALITY, không cắt thêm.
