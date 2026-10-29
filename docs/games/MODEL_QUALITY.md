# Chất lượng model 3D: số mặt và vật liệu

Chủ dự án, 29/10/2026: quái và cây của Dragonhold nhìn như nhựa, chất lượng rất kém. Ý chủ dự án:
- không bao giờ dùng loại 2k mặt nữa;
- model sau này phải có nhiều mặt hơn, chấp nhận nặng hơn để đồ họa đẹp hơn;
- chỉ cân lại khi việc tăng mặt gây lag hay chậm rõ;
- model 3D đang có thì tạm thời giữ nguyên, không sửa.

Áp cho mọi game có model 3D: Dragonhold, Wordwoven, Last Line.

## 1. Vì sao quái và cây Dragonhold nhìn như nhựa (đo 29/10)

Lỗi nằm ở bước xử lý của ta, không nằm ở file gốc Tripo:

- **Cắt mặt quá tay.** Bước xử lý M0b (`games/dragon-hold/scripts/models/m0b-strip.mjs`, preset `scripts/models/presets/dragon-hold-m0b.json`) giảm tam giác rất mạnh:

  | Loại | File gốc Tripo | Trong game (High) | Mất |
  |---|---:|---:|---:|
  | Quái (Moss Grunt, Blight Wolf, Tusk Boar, Moss Archer) | 5.600–5.900 | 2.400 | khoảng 58 % |
  | Thorn Ant | 3.744 | 1.200 | 68 % |
  | Thông cao, thông tròn, cây tán tím | 9.500–9.900 | 900–1.600 | 84–91 % |
  | Bụi cây | 4.700–4.900 | 700–800 | khoảng 85 % |
  | Đá, gốc cây, khúc gỗ | 3.700–4.900 | 450–800 | 85–88 % |

- **Bỏ hết map chi tiết.** Bước đó xóa normal map, map metal-roughness, occlusion, emissive. Nó đặt roughness phẳng 0,9 cho mọi chỗ và hạ texture màu từ 2048 xuống 1024. Không có normal map và độ nhám thay đổi thì bề mặt mịn đều, đọc ra nhựa.

## 2. Luật từ nay (model mới, hoặc model được xử lý lại vì lý do khác)

1. **Không model nào người chơi thấy gần có dưới 2.000 tam giác.** Đây là sàn cứng.
2. **Sàn ở bậc High:**

   | Loại | Sàn High | Ghi chú |
   |---|---:|---|
   | Nhân vật chính, rồng, boss | 20.000 | |
   | Quái, lính, người làng | 6.000 | giữ nguyên file gốc nếu file gốc ≤ 20.000 |
   | Nhà, cầu, mốc lớn, cây lớn | 8.000 | giữ nguyên file gốc nếu ≤ 25.000 |
   | Bụi, đá, gốc cây, hàng rào, đèn | 2.500 | |
   | Cỏ, hoa, sỏi rải dày | 1.500 | dùng instancing |

   Bậc Medium được giảm, nhưng giữ ít nhất 50 % số mặt của High. Bậc Low chỉ giảm thêm cho vật ở xa (trên 40 m) qua LOD.
3. **Giữ vật liệu thật:**
   - giữ normal map và map roughness của file gốc;
   - texture màu 2048 ở High (nhân vật, rồng, boss, quái, nhà, mốc), 1024 ở Medium;
   - không đặt một roughness phẳng cho cả model;
   - shader tô màu của game được chồng lên, không thay bằng cách xóa map.
4. **Khi dựng trên Tripo** (chủ dự án dựng tay trên web):
   - không chọn mức 2k mặt hay low poly;
   - chọn mức mặt cao nhất của chế độ thường;
   - texture PBR có normal map, 2K trở lên.

   Phiếu ảnh nguồn Tripo của Codex ghi dòng này cho chủ dự án.

## 2b. Theo mức chất lượng (chủ dự án 29/10, sau khi biết lỗi do ta cắt)

"Việc bạn giảm là không sai, nhưng nên ở chế độ nào: Ultra thì phải tăng mạnh lên, Low thì để như bạn cắt giảm còn hợp lý, chứ chế độ nào cũng giảm thì không nên."

| Mức trong Cài đặt | Số mặt | Texture và map | Vật liệu |
|---|---|---|---|
| **Ultra** | 100 % file gốc Tripo | màu 2048, normal map, roughness map | vật liệu có ánh sáng dùng đủ map |
| **High** (mặc định) | theo sàn mục 2, tối đa bằng file gốc (quái gần như giữ nguyên; cây khoảng 8.000) | màu 2048, normal map | dùng normal map |
| **Medium** | khoảng 50 % của High | màu 1024, normal map | dùng normal map |
| **Low** | như bản cắt hiện nay được (ví dụ quái 2.400, cây 900–1.600) | màu 1024, không map | tô phẳng của game |

- Sàn 2.000 tam giác ở mục 2.1 áp cho Ultra, High và Medium; Low được giữ mức cắt hiện nay.
- Máy yếu tự chọn Medium hay Low; người chơi chọn được Ultra trong Cài đặt.

## 3. Hiệu năng: đồ họa trước, cân lại khi đo thấy chậm

- **Mặc định là giữ số mặt và map.** Chỉ cân lại khi đo trên máy Mac của dự án thấy vượt ngân sách:
  - p95 thời gian khung ở High 1080p vượt trần của game;
  - hoặc bench đám đông (Dragonhold `dh-bench`, `dh-crowd`; Wordwoven `td-scale`; Last Line bench bầy) trượt.
- **Cân theo thứ tự này**, dừng ngay khi đạt:
  1. instancing, gộp lưới theo vật liệu;
  2. LOD theo khoảng cách (vật xa dùng bản ít mặt);
  3. nén texture, atlas;
  4. bậc Medium và Low;
  5. cuối cùng mới giảm mặt bậc High, và không xuống dưới sàn ở mục 2 nếu chủ dự án chưa đồng ý.
- Mỗi lần cân phải ghi số đo trước và sau vào changelog của game.

## 4. Model đang có

- **Chủ dự án cho sửa ngày 29/10** (sau khi biết lỗi do bước xử lý của ta): Dragonhold dựng lại bốn mức theo mục 2b từ file gốc, làn model riêng. Wordwoven và Last Line kiểm theo mục 2b khi làn của game chạm tới model.
- **Cách sửa rẻ khi được phép:** xử lý lại từ file gốc Tripo đang có trong `art-src/3d/`. Nâng `triangles` trong preset lên sàn mục 2, và bỏ bước xóa map của `m0b-strip.mjs`. Cách này không tốn credit Tripo. Đo `dh-bench` và `dh-crowd` trước và sau.
- Wordwoven (preset `games/typing-defense/scripts/models/presets/typing-defense-static.json`, 10.000–15.000 tam giác) và Last Line cũng được kiểm theo luật này khi làn của game chạm tới model.
