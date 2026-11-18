# Phiếu 433g — Kim thay K2, K3, K6 và K7 bằng art gốc

Ngày 17/11/2026. Đã thực hiện đúng ba vòng sửa → chụp → mở ảnh, tại server có sẵn `localhost:3148`, đối chiếu `metal-rain-f.jpg`. **Đạt cổng số: kiểm kiểu 0 lỗi, p95 mưa dày 8,80 ms, vùng trắng tối đa 0,00010851%, tỷ số sáng kiếm lớn/nhỏ thấp nhất 2,930×.** Chưa có chấm mù 8,5 hoặc owner chốt thẩm mỹ. Có điểm về phần đế trong model Tripo cần owner xem bên dưới.

## Các lớp đã thay

Đường dẫn nguồn tính từ `games/.wt-ic-lab-all/art-src/lab/vfx/`. Không sinh ảnh mới, không sửa file nguồn.

| Lớp | File đang dùng | Cách hiển thị và shader còn lại |
| --- | --- | --- |
| K2, hào quang kiếm lớn | `aura/aura-metal-feather-mantle.atlas.png` | Flipbook 24 khung, 12 fps, ô 1024×288. Xoay nguyên thẻ 90°; chiều dài 1,3× thân kiếm, ngang theo tỷ lệ gốc. Kiếm 9 m có hào quang dài 11,7 m, ngang 3,290625 m. `MeshBasicMaterial`, không shader tùy biến, không fresnel, không làm mờ hoặc uốn hình. |
| K3, kiếm nhỏ | Model Tripo cũ + `aura/qi-streak-1.png` | `MeshStandardMaterial` chuẩn, `emissive=(1; 0,7; 0,15)`, `emissiveIntensity=0,55` đồng nhất toàn thân; `emissiveMap=null`, `vertexColors=false`. Bỏ các map màu/normal/roughness/metalness ở kiếm năng lượng. Hai bản khí nối tiếp, mỗi bản dài 0,42× kiếm và ngang 0,0525× kiếm, đúng tỷ lệ 512:64. Chỉ xoay và thu phóng đều. Không core, flow, rim, gradient, noise hoặc shader tùy biến. |
| K6, tia từ trận | `metal-ult/rays.png` | Nguyên ảnh 512×512, 20 thẻ vuông cạnh 5,97 m; xoay và nhuộm màu. Shader chung chỉ đặt thẻ, lấy đúng một mẫu ảnh và đổi alpha theo thời gian. Nhánh `uArtOnly` trả kết quả trước mọi crop/blur/mask; không kéo ảnh thành tia dài. |
| K7, vệt đất | `metal/metal-ground-impact.atlas.png` | Ô 256×256, 32 khung, 12 fps, thẻ vuông 20,24×20,24 m nằm trên đất. Chạy lại các khung theo thời gian; cùng nhánh lấy nguyên ảnh `uArtOnly`, không mask tròn, blur, lọc kênh hoặc méo hình. |

Đã chụp và mở cả feather-mantle lẫn `aura-metal-windsilk.atlas.png`. Chọn feather-mantle vì đường lông vũ và khoảng trống quanh kiếm rõ hơn ở Alt+2; windsilk đọc như một dải thẳng và mất chi tiết khi thân kiếm sáng. Bản chọn cuối dùng mặc định, không cần cờ chọn hào quang. `?metalMantle=windsilk` chỉ phục vụ so sánh.

Kiếm lớn giữ vật liệu PBR của model và các map gốc, emissive vàng đồng nhất cường độ 0,85. Toàn bộ kiếm và hào quang mới tan bằng alpha theo thời gian; không dịch đỉnh theo noise hoặc dùng mask xói mòn. Vật liệu kiếm nhỏ và lớn đều đã xác minh tại runtime: `onBeforeCompile === THREE.Material.prototype.onBeforeCompile`.

Code cũ `SwordLookLayer`, các chuỗi shader fresnel/core/flow/rim, nhánh crop-blur và mask đất vẫn có trong nguồn. Không tạo lớp SwordLookLayer cũ; hook vật liệu kiếm cũ nằm trong nhánh `if (false)`. K6/K7 dùng nhánh art nguyên bản trước các nhánh cũ. **Không còn shader tạo hình chạy trên bốn lớp thay thế.** Cả chiêu vẫn còn shader trận A và K5 theo yêu cầu giữ nguyên; không nhận là đã xóa hết shader của chiêu.

## Phần giữ nguyên và số đo

Trận A cao 10 m, đường kính 22 m. Sáu đợt ở 0,60 / 1,28 / 1,90 / 2,46 / 2,96 / 3,40 s; số kiếm 12 / 14 / 16 / 18 / 20 / 22. Tổng 102 kiếm nhỏ + 1 kiếm lớn; tối đa 60 kiếm sống. Mưa kéo dài 4,088344 s; kiếm lớn sinh 4,10 s, chạm đất 4,90 s; trả đủ 103 ô và kết thúc 6,80 s. Các vị trí, camera, gia tốc, quãng rơi và âm thanh của 433f giữ nguyên.

Đo lại theo driver 433f: quãng rơi trung vị **39,69%** chiều cao khung, thời gian thấy rõ trung vị **0,767 s**, **102/103 kiếm (99,03%)** đạt cả 0,45 s và 18%. Kiếm lớn vẫn chỉ thấy rõ 0,417 s ở Alt+1, đúng hạn chế đã báo ở 433f. Bề ngang kiếm cắm 71,10%; lề trên trận A nhỏ nhất 6,87%.

| Vòng | Hào quang | Emissive nhỏ / lớn | Trắng tối đa (%) | Tỷ số sáng nhỏ nhất | p95 mưa dày (ms) |
| --- | --- | --- | ---: | ---: | ---: |
| 1 | Feather | 0,28 / 0,65 | 0,00010851 | 3,861× | 7,70 |
| 2 | Windsilk | 0,75 / 1,80 | 0 | 3,282× | 6,80 |
| 3, cuối | Feather | 0,55 / 0,85 | 0,00010851 | 2,930× | 8,80 |

Chrome headless, High mặc định, 1280×720, DPR 1, ANGLE Metal Renderer Apple M4; 100 quái (87 TargetField + 13 walker). Chọn 42 khung có kiếm rơi và số kiếm sống ≥80% đỉnh. Đo CPU rồi `readPixels` một pixel chờ GPU như `metal-ult-rain-review.mjs`: p95 tổng **8,80 ms**, CPU **2,80 ms**; p95 toàn khoảng chiêu **9,10 ms**. Đây không phải khoảng cách rAF. Tối đa 328 draw call, 1.808.005 tam giác. Không suy ra cải thiện hiệu năng từ chênh lệch với số đo lịch sử của f.

Vùng trắng tính khi cả ba kênh sRGB ≥242/255: tối đa một pixel trên 921.600 pixel ở các ảnh pha; toàn bộ 165 khung MP4 tối đa **0,00010851%** (một pixel). Tỷ số sáng đo riêng nhóm kiếm nhỏ và kiếm lớn vào RGBA half-float nền đen trước bloom/tone mapping, gồm thân và các thẻ khí/hào quang. Dùng các mẫu cả hai nhóm thực sự nằm trong khung; không lấy khung kiếm lớn còn trên mép trên làm tỷ số.

`node node_modules/typescript/bin/tsc --noEmit`: **0 lỗi**. Không chạy build hoặc bộ test của game. Không có exception hoặc lỗi tải tài nguyên mới của mưa kiếm. Còn các cảnh báo sẵn có ngoài phạm vi: nhiều KTX2Loader, `drawImage` với atlas metal-crescent-sym/metal-slash-arc.

## Tệp và dọn dẹp

Mã đã ghi, đúng phạm vi:
- `games/.wt-ic-lab-all/src/lab/metal-sword-look.ts`: lớp art mới, PBR chuẩn, thẻ giữ tỷ lệ và phép đo sáng không dùng shader cách ly.
- `games/.wt-ic-lab-all/src/lab/metal-ult-rain.ts`: nối nguồn K2/K3/K6/K7, tắt đường shader cũ, giữ lịch và quỹ đạo f.
- `games/.wt-ic-lab-all/src/lab/metal-ult-rain-g-review.mjs`: kịch bản ba vòng, hai góc, số đo và xuất clip.

Giao nộp:
- [metal-rain-g.jpg](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/metal-rain-g.jpg): năm mốc 1,05 / 2,35 / 3,90 / 4,916667 / 5,90 s, cả Alt+1 và Alt+2, nền `#353a40`.
- [metal-rain-g.mp4](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/metal-rain-g.mp4): H.264 + AAC, 1280×720, 24 fps, 165 khung, 6,875 s, 5.755.737 byte; từ kích chiêu đến khi kiếm tan hết, giữ âm Kim của f.
- [Tấm chuyển động](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/metal-rain-433g/motion-contact.jpg), [vòng 1](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/metal-rain-433g/round-1-feather-sheet.jpg), [vòng 2](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/metal-rain-433g/round-2-windsilk-sheet.jpg), [vòng 3](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/metal-rain-433g/round-3-feather-sheet.jpg), [nguồn hình](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/metal-rain-433g/source-sheet.jpg).

Đã mở ảnh giao nộp, các tấm ba vòng, ảnh 1280×720 và tấm chuyển động; so với bản f. Giữ nguyên toàn bộ media cũ. Đã thêm dòng `metal-rain-g` vào ABOUT của owner và ABOUT cho chủ đề/ba thư mục lượt. Đã xem trước rồi prune **195 khung thô, 257,151 MB** do phiên này tạo; giữ các tấm ghép. Đã xóa âm/video trung gian. Ba lần Chrome headless đều đã đóng bằng driver; profile tạm đã xóa, riêng profile lượt cuối đã kiểm tra không còn. Server 3148 (PID 243) vẫn chạy.

Không chạy `scripts/review-index.mjs`: công cụ ghi thêm các file chỉ mục ngoài phạm vi phiếu chỉ cho mã, media, báo cáo và ABOUT. Không commit, push, reset, clean hoặc stash; không sửa game chính hay file của agent khác.

## Điểm owner cần xem và phần bỏ qua

- **Phần đế có sẵn trong model Tripo hiện ra ở đầu dưới của kiếm khi bay**, rõ nhất ở Alt+2. Trước đây shader K1 cắt bỏ vùng local y<0; khi bỏ hook shader và dùng toàn bộ model với PBR chuẩn, vùng ấy hiện lại. Giữ nguyên hình học nguồn, không cắt/mask hoặc tạo hình thay thế. Đây là hạn chế hình ảnh cần owner xem, không tuyên bố đạt thẩm mỹ 8,5. Kiếm lớn cuối vẫn có áo lông vũ giữ đúng tỷ lệ.
- **K5 không làm**, chờ owner chọn ảnh ở phiếu 444; vệt crop-blur của K5 vẫn chạy. Trận A và shader riêng của trận giữ nguyên đúng phiếu.
- Không tạo ảnh hoặc âm mới vì đã có đủ nguồn được chỉ định. Không làm vòng thứ tư; chưa có chấm mù độc lập hay owner chốt hình/âm.

Tái kiểm trên server có sẵn (FINAL=1 xuất lại media):

```sh
ROUND=3 FINAL=1 ART_MAGICK=/opt/homebrew/bin/magick .local/bin/heavy.sh --perf node games/.wt-ic-lab-all/src/kit/tools/cdp-run.mjs games/.wt-ic-lab-all/src/lab/metal-ult-rain-g-review.mjs --width=1280 --height=720 --dpr=1
```

## Phụ lục số đo ba vòng

```json
{
  "cac_vong": [
    {
      "vong": 1,
      "tong_hop": {
        "height": 10,
        "diameter": 22,
        "widthPercent": 71.0985952173162,
        "rainDuration": 4.088344331988265,
        "waves": 6,
        "small": 102,
        "total": 103,
        "maxLive": 60,
        "white": 0.00010850694444444444,
        "p95": 7.699999928474426,
        "minGiantRatio": 3.8606542146898755,
        "fall": {
          "count": 103,
          "medianSeconds": 0.7666666666666674,
          "minSeconds": 0.41666666666666663,
          "medianTravel": 0.3969475703697208,
          "minTravel": 0.20125169362932965,
          "bothFraction": 0.9902912621359223,
          "giant": {
            "id": 102,
            "giant": true,
            "seconds": 0.41666666666666663,
            "firstY": 0.0023690372465155485,
            "impactY": 0.38486854007504523,
            "birth": 4.1,
            "impact": 4.9,
            "travel": 0.3824995028285297
          },
          "smallCount": 102
        }
      },
      "p95_toan_chieu_ms": 7.199999928474426,
      "cpu_p95_ms": 2.9000000953674316,
      "mau_mua_day": 42,
      "dat_cong_so": true
    },
    {
      "vong": 2,
      "tong_hop": {
        "height": 10,
        "diameter": 22,
        "widthPercent": 71.0985952173162,
        "rainDuration": 4.088344331988265,
        "waves": 6,
        "small": 102,
        "total": 103,
        "maxLive": 60,
        "white": 0,
        "p95": 6.799999952316284,
        "minGiantRatio": 3.282353726106018,
        "fall": {
          "count": 103,
          "medianSeconds": 0.7666666666666674,
          "minSeconds": 0.41666666666666663,
          "medianTravel": 0.3969475703697208,
          "minTravel": 0.20125169362932965,
          "bothFraction": 0.9902912621359223,
          "giant": {
            "id": 102,
            "giant": true,
            "seconds": 0.41666666666666663,
            "firstY": 0.0023690372465155485,
            "impactY": 0.38486854007504523,
            "birth": 4.1,
            "impact": 4.9,
            "travel": 0.3824995028285297
          },
          "smallCount": 102
        }
      },
      "p95_toan_chieu_ms": 6.600000023841858,
      "cpu_p95_ms": 2.3000000715255737,
      "mau_mua_day": 42,
      "dat_cong_so": true
    },
    {
      "vong": 3,
      "tong_hop": {
        "height": 10,
        "diameter": 22,
        "widthPercent": 71.0985952173162,
        "rainDuration": 4.088344331988265,
        "waves": 6,
        "small": 102,
        "total": 103,
        "maxLive": 60,
        "white": 0.00010850694444444444,
        "p95": 8.800000071525574,
        "minGiantRatio": 2.929628848127225,
        "fall": {
          "count": 103,
          "medianSeconds": 0.7666666666666674,
          "minSeconds": 0.41666666666666663,
          "medianTravel": 0.3969475703697208,
          "minTravel": 0.20125169362932965,
          "bothFraction": 0.9902912621359223,
          "giant": {
            "id": 102,
            "giant": true,
            "seconds": 0.41666666666666663,
            "firstY": 0.0023690372465155485,
            "impactY": 0.38486854007504523,
            "birth": 4.1,
            "impact": 4.9,
            "travel": 0.3824995028285297
          },
          "smallCount": 102
        }
      },
      "p95_toan_chieu_ms": 9.100000023841858,
      "cpu_p95_ms": 2.8000000715255737,
      "mau_mua_day": 42,
      "dat_cong_so": true
    }
  ],
  "vat_lieu_cuoi": {
    "look": "mix",
    "small": {
      "type": "MeshStandardMaterial",
      "emissive": [
        1,
        0.7,
        0.15
      ],
      "emissiveIntensity": 0.55,
      "emissiveMap": null,
      "vertexColors": false,
      "stockShader": true
    },
    "giant": {
      "type": "MeshStandardMaterial",
      "emissive": [
        1,
        0.7,
        0.15
      ],
      "emissiveIntensity": 0.85,
      "emissiveMap": null,
      "vertexColors": false,
      "stockShader": true
    },
    "aura": "http://127.0.0.1:3148/art-src/lab/vfx/aura/aura-metal-feather-mantle.atlas.png",
    "atlas": {
      "cols": 2,
      "rows": 12,
      "frames": 24,
      "fps": 12,
      "cell": [
        1024,
        288
      ]
    },
    "mantleHeightRatio": 1.3,
    "mantleWidthRatio": 0.36562500000000003,
    "streakRatio": 8,
    "streakLengthPerSword": 0.42,
    "streakCopies": 2,
    "active": 9
  },
  "am_thanh": {
    "first": 0,
    "last": 4.883333333333321,
    "count": 54
  },
  "su_kien_am": {
    "gather": 1,
    "grow": 7,
    "crack": 44,
    "break": 1,
    "tail": 1
  },
  "khung_clip_trang_toi_da_phan_tram": 0.00010850694444444444
}
```
