# Làn 3 · Ấn trên đất theo hệ

`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`.

Chỉ thêm ảnh/prompt/tấm ghép mới trong S; không sửa ảnh cũ, không tích hợp runtime, không chạy build/test hay lệnh Git ghi. Dùng `image_gen` tích hợp, mỗi lần kèm đúng mốc dáng Kim và hai mốc chất liệu của hệ. PNG giữ nguyên đầu ra, chép bằng `cp -n`, đối chiếu SHA-256; prompt ghi nguyên văn, tham chiếu và khổ thật. Điểm dưới đây là **tự chấm nguồn**, lấy mặt yếu nhất, chưa phải chấm mù/nghiệm thu runtime.

## 1 · Hỏa — đủ 7 ảnh

Thêm 5 PNG `fire-{sigil-arcs,sigil-arrow,sigil-spiral,crack-star,rift-groove}.v1-try1.png`, mỗi ảnh kèm `.prompt.txt`; dùng lại hex/line đã duyệt ở phiếu 327. Cả 5 ảnh mới 1672 × 941 px, 5 lần gọi, không cần vẽ lại.

| Ảnh chọn (đều try1) | Dáng | Đẹp, sang | Thẳng/nền/không chữ | Mặt nạ/lề | Cùng dáng Kim | Chung | Hộp nét 5% (rộng×cao+x+y) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| hex (327) | 9 | 8,5 | 8 | 8,5 | 9 | 8 | `758×813+458+47` |
| line (327) | 8,5 | 8,5 | 8 | 8 | 9 | 8 | `1641×197+16+365` |
| arcs | 8,5 | 8,5 | 8 | 8 | 9 | 8 | `860×870+393+24` |
| arrow | 8,5 | 8,5 | 8 | 8 | 9 | 8 | `1591×174+47+377` |
| spiral | 8,5 | 8,5 | 8 | 8 | 9 | 8 | `656×689+506+100` |
| crack | 8,5 | 8,5 | 8 | 8 | 9 | 8 | `1178×837+245+39` |
| groove | 8,5 | 8,5 | 8 | 9 | 9 | 8 | `1520×79+76+423` |

Đo ImageMagick `-colorspace Gray -threshold 5%`, lấy `%@`, như phiếu 324b. Không hộp nét nào chạm mép; rãnh cao **8,40% ≤10%**, xoắn ốc **73,22% ≈70%** (lề trên 100 px, dưới 152 px). Giữ bốn cung và tâm trống; mũi tên có ba vệt; nứt sao giữ tám nhánh cùng lỗ tâm; rãnh không phù văn. Lửa cam đỏ, lõi trắng vàng đúng câu phiếu 327. Nền nhìn đen nhưng góc dưới phải còn `(0,1,0)`, rãnh góc trên trái `(1,1,1)`; không tự làm sạch. Hoa văn trên crack kế thừa mốc Kim.

Tấm ghép: **`S/fire-sigils-set-sheet.jpg`**, đã mở bằng `view_image`, đúng 4 cột × 2 hàng: Hex · Line · Guard Arcs · Dash Arrow / Galaxy Spiral · Star Crack · Sword Rift · ô trống. Anh xem độ đồng bộ, lề line khá hẹp và lượng lửa quanh nét.

## 2 · Thủy — đủ 7 ảnh

Thêm `water-{sigil-hex,sigil-line,sigil-arcs,sigil-arrow,sigil-spiral,crack-star,rift-groove}.v1-try1.png` và 7 prompt; 7 lần gọi, không vẽ lại, đều 1672 × 941 px. Tham chiếu chất liệu: crescent và `water-ground-mark-clean.v1-try1.jpg`.

| Ảnh chọn (try1) | Dáng | Đẹp, sang | Thẳng/nền/không chữ | Mặt nạ/lề | Cùng dáng Kim | Chung | Hộp nét 5% |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| hex | 9 | 8,5 | 8 | 8,5 | 9 | 8 | `758×801+458+54` |
| line | 8,5 | 8,5 | 8 | 8 | 9 | 8 | `1640×198+14+361` |
| arcs | 8,5 | 8,5 | 8 | 8 | 9 | 8 | `842×877+398+21` |
| arrow | 8,5 | 8,5 | 8 | 8 | 9 | 8 | `1597×176+40+377` |
| spiral | 8,5 | 8,5 | 8 | 8,5 | 9 | 8 | `628×669+520+109` |
| crack | 8,5 | 8,5 | 8 | 8,5 | 9 | 8 | `1155×820+253+47` |
| groove | 8,5 | 8,5 | 8 | 9 | 9 | 8 | `1524×75+75+427` |

Không chạm mép; rãnh **7,97% ≤10%**, xoắn ốc **71,09% ≈70%**. Nét lam trong có gợn nước, lõi trắng, bọt/giọt mảnh; hình học và khoảng đen bám mốc Kim. Tấm **`S/water-sigils-set-sheet.jpg`** đã mở kiểm đủ bảy ô, đúng thứ tự như Hỏa. Anh xem line còn lề trái 14 px, arcs còn lề trên 21 px; hoa văn crack giữ theo mốc. Góc ảnh còn sai khác 1/255, chưa đen tuyệt đối; không hậu kỳ.

## 3 · Lôi — đủ 7 ảnh

Thêm đủ `thunder-{sigil-hex,sigil-line,sigil-arcs,sigil-arrow,sigil-spiral,crack-star,rift-groove}.v1-try1.png` và prompt; 7 lần gọi, không vẽ lại, đều 1672 × 941 px. Dùng crescent và ground-mark-clean của Lôi.

| Ảnh chọn (try1) | Dáng | Đẹp, sang | Thẳng/nền/không chữ | Mặt nạ/lề | Cùng dáng Kim | Chung | Hộp nét 5% |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| hex | 9 | 8,5 | 8 | 8,5 | 9 | 8 | `765×807+455+52` |
| line | 8,5 | 8,5 | 8 | 8 | 9 | 8 | `1645×197+12+364` |
| arcs | 8,5 | 8,5 | 8 | 8 | 9 | 8 | `850×882+397+19` |
| arrow | 8,5 | 8,5 | 8 | 8 | 9 | 8 | `1581×179+60+376` |
| spiral | 8,5 | 8,5 | 8 | 8,5 | 9 | 8 | `638×670+516+110` |
| crack | 8,5 | 8,5 | 8 | 8,5 | 9 | 8 | `1165×825+251+47` |
| groove | 8,5 | 8,5 | 8 | 9 | 9 | 8 | `1522×76+75+425` |

Không chạm mép; rãnh **8,08% ≤10%**, xoắn ốc **71,20% ≈70%**. Lõi trắng, plasma tím và tia điện bám nét; các khe ngắt/tâm trống vẫn rõ, rãnh không phù văn. Đã mở **`S/thunder-sigils-set-sheet.jpg`**, đúng 4×2 và thứ tự bảy dáng. Anh xem quầng điện, line lề trái 12 px và arcs lề trên 19 px. Nền còn sai khác 1/255 tại góc như các bộ trước, giữ nguyên.

## 4 · Phong — đủ 7 ảnh

Thêm 7 `wind-<dáng>.v1-try1.png` và prompt, cùng bảy tên dáng ở bảng trên; 7 lần gọi, không vẽ lại, đều 1672 × 941 px. Dùng crescent và ground-mark-clean của Phong.

| Ảnh chọn (try1) | Dáng | Đẹp, sang | Thẳng/nền/không chữ | Mặt nạ/lề | Cùng dáng Kim | Chung | Hộp nét 5% |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| hex | 9 | 8,5 | 8 | 8,5 | 9 | 8 | `754×796+459+57` |
| line | 8,5 | 8,5 | 8 | 8 | 9 | 8 | `1636×190+16+368` |
| arcs | 8,5 | 8,5 | 8 | 8 | 9 | 8 | `842×877+405+22` |
| arrow | 8,5 | 8,5 | 8 | 8 | 9 | 8 | `1596×176+42+376` |
| spiral | 8,5 | 8,5 | 8 | 8,5 | 9 | 8 | `621×654+524+117` |
| crack | 8,5 | 8,5 | 8 | 8,5 | 9 | 8 | `1177×824+246+47` |
| groove | 8,5 | 8,5 | 8 | 9 | 9 | 8 | `1526×68+73+430` |

Không chạm mép; rãnh **7,23%**, xoắn ốc **69,50%**, đều đạt tỷ lệ. Khí trắng ngọc/xanh bạc hà, dải khí mềm và hạt sáng mảnh, giữ đúng topology Kim. Đã mở **`S/wind-sigils-set-sheet.jpg`**, đủ bảy ô đúng thứ tự. Anh xem mức xanh và dải khí; line lề trái 16 px, arcs lề trên 22 px. Nền còn lệch 1/255 ở góc; giữ nguyên.

## 5 · Băng — đủ 7 ảnh

Thêm 7 `ice-<dáng>.v1-try1.png` và prompt (bảy dáng như trên), 7 lần gọi, không vẽ lại, đều 1672 × 941 px. Dùng crescent và ground-mark-clean của Băng.

| Ảnh chọn (try1) | Dáng | Đẹp, sang | Thẳng/nền/không chữ | Mặt nạ/lề | Cùng dáng Kim | Chung | Hộp nét 5% |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| hex | 9 | 8,5 | 8 | 8,5 | 9 | 8 | `766×808+455+50` |
| line | 8,5 | 8,5 | 8 | 8 | 9 | 8 | `1638×191+15+367` |
| arcs | 8,5 | 8,5 | 8 | 8 | 9 | 8 | `822×882+413+17` |
| arrow | 8,5 | 8,5 | 8 | 8 | 9 | 8 | `1590×173+45+379` |
| spiral | 8,5 | 8,5 | 8 | 8,5 | 9 | 8 | `642×673+514+109` |
| crack | 8,5 | 8,5 | 8 | 8,5 | 9 | 8 | `1172×824+247+49` |
| groove | 8,5 | 8,5 | 8 | 9 | 9 | 8 | `1519×77+77+426` |

Không chạm mép; rãnh **8,18%**, xoắn ốc **71,52%**, đạt tỷ lệ. Tinh thể lam nhạt có vân sương, cạnh sáng và hạt băng; giữ đúng hình Kim. Đã mở **`S/ice-sigils-set-sheet.jpg`**, đủ bảy ô đúng thứ tự. Anh xem khác biệt Băng/Thủy ở mặt tinh thể và hạt băng; line lề trái 15 px, arcs lề trên 17 px. Góc nền còn sai khác 1/255, giữ nguyên.

## 6 · Thổ — đủ 7 ảnh

Thêm 7 `earth-<dáng>.v1-try1.png` và prompt (bảy dáng như trên), 7 lần gọi, không vẽ lại, đều 1672 × 941 px. Dùng crescent và ground-mark của Thổ.

| Ảnh chọn (try1) | Dáng | Đẹp, sang | Thẳng/nền/không chữ | Mặt nạ/lề | Cùng dáng Kim | Chung | Hộp nét 5% |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| hex | 9 | 8,5 | 8 | 8,5 | 9 | 8 | `746×794+463+57` |
| line | 8,5 | 8,5 | 8 | 8 | 9 | 8 | `1642×190+14+367` |
| arcs | 8,5 | 8,5 | 8 | 8 | 9 | 8 | `823×871+415+24` |
| arrow | 8,5 | 8,5 | 8 | 8 | 9 | 8 | `1594×171+43+379` |
| spiral | 8,5 | 8,5 | 8 | 8,5 | 9 | 8 | `626×656+523+116` |
| crack | 8,5 | 8 | 8 | 8,5 | 9 | 8 | `1171×820+247+48` |
| groove | 8,5 | 8 | 8 | 9 | 9 | 8 | `1523×71+75+428` |

Không chạm mép; rãnh **7,55%**, xoắn ốc **69,71%**, đạt tỷ lệ. Khoáng nâu vàng/hổ phách, vân khoáng thấy rõ nhất trên spiral/line; crack/groove thiên về ánh vàng hơn hạt khoáng. Đã mở **`S/earth-sigils-set-sheet.jpg`**, đủ bảy ô đúng thứ tự. Anh xem chất Thổ ở hai dạng nứt; line lề trái 14 px, arcs lề trên 24 px. Nền còn lệch 1/255 tại góc, giữ nguyên.

## 7 · Mộc — đủ 7 ảnh

Thêm 7 `wood-<dáng>.v1-try1.png` và prompt, 7 lần gọi, không vẽ lại, đều 1672 × 941 px. Dùng crescent và ground-mark của Mộc.

| Ảnh chọn (try1) | Dáng | Đẹp, sang | Thẳng/nền/không chữ | Mặt nạ/lề | Cùng dáng Kim | Chung | Hộp nét 5% |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| hex | 9 | 8,5 | 8 | 8,5 | 8,5 | 8 | `754×800+459+54` |
| line | 8,5 | 8,5 | 8 | 8 | 8,5 | 8 | `1640×190+14+365` |
| arcs | 8,5 | 8,5 | 8 | 8 | 8,5 | 8 | `826×865+414+24` |
| arrow | 8,5 | 8,5 | 8 | 8 | 9 | 8 | `1597×175+41+377` |
| spiral | 8,5 | 8,5 | 8 | 8,5 | 8,5 | 8 | `628×657+521+115` |
| crack | 8,5 | 8,5 | 8 | 8,5 | 8,5 | 8 | `1168×832+247+39` |
| groove | 8 | 8,5 | 8 | 9 | 8 | 8 | `1511×72+81+427` |

Không chạm mép; rãnh **7,65%**, xoắn ốc **69,82%**, đạt tỷ lệ. Dây leo xanh vàng, lá/hoa nhỏ và hạt phấn theo mốc; hoa làm thay đổi chi tiết phụ nhưng cấu trúc chính vẫn bám Kim. Rãnh còn đọc hơi giống sợi dây leo, điểm dáng 8. Đã mở **`S/wood-sigils-set-sheet.jpg`**, đúng bảy ô. Anh xem lượng hoa lá và rãnh; line lề trái 14 px. Góc nền còn lệch 1/255, giữ nguyên.

## 8 · Quang — đủ 7 ảnh

Thêm 7 `light-<dáng>.v1-try1.png` và prompt, 7 lần gọi, không vẽ lại, đều 1672 × 941 px. Dùng crescent và ground-mark-clean của Quang.

| Ảnh chọn (try1) | Dáng | Đẹp, sang | Thẳng/nền/không chữ | Mặt nạ/lề | Cùng dáng Kim | Chung | Hộp nét 5% |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| hex | 9 | 8,5 | 8 | 8,5 | 9 | 8 | `770×824+452+41` |
| line | 8,5 | 8,5 | 8 | 8 | 9 | 8 | `1644×199+12+364` |
| arcs | 8,5 | 8,5 | 8 | 8 | 9 | 8 | `832×884+411+18` |
| arrow | 8,5 | 8,5 | 8 | 8 | 9 | 8 | `1599×184+40+371` |
| spiral | 8,5 | 8,5 | 8 | 8,5 | 9 | 8 | `643×662+514+113` |
| crack | 8,5 | 8,5 | 8 | 8 | 9 | 8 | `1195×859+235+35` |
| groove | 8,5 | 8,5 | 8 | 9 | 9 | 8 | `1524×79+74+426` |

Không chạm mép; rãnh **8,40%**, xoắn ốc **70,35%**, đạt tỷ lệ. Ánh trắng ngà/vàng champagne, sợi sáng và quầng ngọc trai; giữ hình học Kim. Đã mở **`S/light-sigils-set-sheet.jpg`**, đúng bảy ô. Anh xem độ khác biệt với Thổ ở chất ánh sáng; line lề trái 12 px, arcs lề trên 18 px. Nền còn lệch 1/255 ở góc, giữ nguyên.

## 9 · Ám — đủ 7 ảnh

Thêm 7 `dark-<dáng>.v1-try1.png` và prompt, 7 lần gọi, không vẽ lại, đều 1672 × 941 px. Mỗi lần gửi crescent và ground-mark-clean, prompt ưu tiên luật đen/đỏ thẫm của phiếu hơn màu tím trong ground-mark.

| Ảnh chọn (try1) | Dáng | Đẹp, sang | Thẳng/nền/không chữ | Mặt nạ/lề | Cùng dáng Kim | Chung | Hộp nét 5% |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| hex | 9 | 8,5 | 8 | 8,5 | 9 | 8 | `738×791+466+59` |
| line | 8,5 | 8,5 | 8 | 8 | 9 | 8 | `1631×181+18+372` |
| arcs | 8,5 | 8,5 | 8 | 8 | 9 | 8 | `835×862+400+29` |
| arrow | 8,5 | 8,5 | 8 | 8,5 | 9 | 8 | `1578×160+52+387` |
| spiral | 8,5 | 8,5 | 8 | 8,5 | 9 | 8 | `620×659+527+116` |
| crack | 8,5 | 8,5 | 8 | 8,5 | 9 | 8 | `1159×823+253+46` |
| groove | 8,5 | 8 | 8 | 9 | 9 | 8 | `1516×67+79+429` |

Không chạm mép; rãnh **7,12%**, xoắn ốc **70,03%**, đạt tỷ lệ. Nét đỏ thẫm và khói tối bám viền, giữ topology Kim; rãnh hơi tối. Đã mở **`S/dark-sigils-set-sheet.jpg`**, đúng bảy ô. Kiểm pixel tím/tía (`V>10%, S>30%, B>G+8%, B>0,6R`): sáu ảnh 0; hex có 9/152.590 pixel màu vượt ngưỡng, nhiễu lẻ không thành mảng tím thấy được. Không khẳng định sạch màu tuyệt đối. Anh xem khả năng đọc nét đỏ/khói trên nền đen. Góc nền còn lệch 1/255, giữ nguyên.

## 10 · Độc — đủ 7 ảnh

Thêm 7 `poison-<dáng>.v1-try1.png` và prompt, 7 lần gọi, không vẽ lại, đều 1672 × 941 px. Dùng crescent và ground-mark của Độc.

| Ảnh chọn (try1) | Dáng | Đẹp, sang | Thẳng/nền/không chữ | Mặt nạ/lề | Cùng dáng Kim | Chung | Hộp nét 5% |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| hex | 9 | 8,5 | 8 | 8,5 | 9 | 8 | `746×799+464+54` |
| line | 8,5 | 8,5 | 8 | 8 | 9 | 8 | `1644×190+14+367` |
| arcs | 8,5 | 8,5 | 8 | 8 | 9 | 8 | `826×867+410+25` |
| arrow | 8,5 | 8,5 | 8 | 8 | 9 | 8 | `1597×181+42+374` |
| spiral | 8,5 | 8,5 | 8 | 8,5 | 9 | 8 | `620×655+525+117` |
| crack | 8,5 | 8,5 | 8 | 8 | 9 | 8 | `1177×852+245+29` |
| groove | 8,5 | 8 | 8 | 9 | 9 | 8 | `1525×69+75+431` |

Không chạm mép; rãnh **7,33%**, xoắn ốc **69,61%**, đạt tỷ lệ. Xanh acid có bọt nhỏ và viền hơi tím theo đúng mốc; giữ hình Kim, rãnh không phù văn. Đã mở **`S/poison-sigils-set-sheet.jpg`**, đủ bảy ô đúng thứ tự. Anh xem cân bằng xanh/tím; line lề trái 14 px, nứt sao lề trên 29 px. Nền còn lệch 1/255 tại góc, giữ nguyên.

## 11 · Huyết — đủ 7 ảnh

Thêm 7 `blood-<dáng>.v1-try1.png` và prompt, 7 lần gọi, không vẽ lại, đều 1672 × 941 px. Dùng crescent và ground-mark của Huyết.

| Ảnh chọn (try1) | Dáng | Đẹp, sang | Thẳng/nền/không chữ | Mặt nạ/lề | Cùng dáng Kim | Chung | Hộp nét 5% |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| hex | 9 | 8,5 | 8 | 8,5 | 9 | 8 | `746×794+463+57` |
| line | 8,5 | 8,5 | 8 | 8 | 9 | 8 | `1635×188+18+366` |
| arcs | 8,5 | 8,5 | 8 | 8 | 9 | 8 | `825×874+415+21` |
| arrow | 8,5 | 8,5 | 8 | 8 | 9 | 8 | `1592×169+45+381` |
| spiral | 8,5 | 8,5 | 8 | 8,5 | 9 | 8 | `625×653+522+117` |
| crack | 8,5 | 8,5 | 8 | 8,5 | 9 | 8 | `1170×826+247+45` |
| groove | 8,5 | 8 | 8 | 9 | 9 | 8 | `1529×70+73+429` |

Không chạm mép; rãnh **7,44%**, xoắn ốc **69,39%**, đạt tỷ lệ. Ruby/đỏ thắm bóng, sợi năng lượng và giọt đỏ bám sát nét; sáng và lỏng hơn bộ Ám. Đã mở **`S/blood-sigils-set-sheet.jpg`**, đúng bảy ô. Anh xem giọt đỏ và độ sáng; line lề trái 18 px, arcs lề trên 21 px. Nền còn lệch 1/255 ở góc, giữ nguyên.

## 12 · Hư Không — đủ 7 ảnh

Thêm 7 `void-<dáng>.v1-try1.png` và prompt, 7 lần gọi, không vẽ lại, đều 1672 × 941 px. Dùng crescent và ground-mark của Hư Không.

| Ảnh chọn (try1) | Dáng | Đẹp, sang | Thẳng/nền/không chữ | Mặt nạ/lề | Cùng dáng Kim | Chung | Hộp nét 5% |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| hex | 9 | 8,5 | 8 | 8,5 | 9 | 8 | `746×796+463+57` |
| line | 8,5 | 8,5 | 8 | 8 | 9 | 8 | `1640×188+15+368` |
| arcs | 8,5 | 8,5 | 8 | 8 | 9 | 8 | `808×861+421+29` |
| arrow | 8,5 | 8,5 | 8 | 8 | 9 | 8 | `1594×169+43+382` |
| spiral | 8,5 | 8,5 | 8 | 8,5 | 9 | 8 | `624×654+524+117` |
| crack | 8,5 | 8 | 8 | 8,5 | 9 | 8 | `1156×834+255+36` |
| groove | 8,5 | 8 | 8 | 9 | 9 | 8 | `1521×70+76+429` |

Không chạm mép; rãnh **7,44%**, xoắn ốc **69,50%**, đạt tỷ lệ. Chàm/tím có kênh tối và sợi tinh vân; hai dạng nứt còn gần cảm giác điện tím của Lôi hơn các dáng rộng. Đã mở **`S/void-sigils-set-sheet.jpg`**, đúng bảy ô. Anh xem độ phân biệt Hư Không/Lôi; line lề trái 15 px. Nền còn lệch 1/255 ở góc, giữ nguyên.

## 13 · Tinh Tú — đủ 7 ảnh

Thêm 7 `star-<dáng>.v1-try1.png` và prompt, 7 lần gọi, không vẽ lại, đều 1672 × 941 px. Dùng crescent và ground-mark của Tinh Tú.

| Ảnh chọn (try1) | Dáng | Đẹp, sang | Thẳng/nền/không chữ | Mặt nạ/lề | Cùng dáng Kim | Chung | Hộp nét 5% |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| hex | 9 | 8,5 | 8 | 8,5 | 9 | 8 | `757×800+458+54` |
| line | 8,5 | 8,5 | 8 | 8 | 9 | 8 | `1640×190+15+367` |
| arcs | 8,5 | 8,5 | 8 | 8 | 9 | 8 | `820×874+418+22` |
| arrow | 8,5 | 8,5 | 8 | 8 | 9 | 8 | `1591×181+47+372` |
| spiral | 8,5 | 8,5 | 8 | 8,5 | 9 | 8 | `654×671+508+106` |
| crack | 8,5 | 8,5 | 8 | 8 | 9 | 8 | `1169×867+251+22` |
| groove | 8,5 | 8,5 | 8 | 9 | 9 | 8 | `1523×72+76+430` |

Không chạm mép; rãnh **7,65%**, xoắn ốc **71,31%**, đạt tỷ lệ. Chất sao chàm/lam tím với điểm trắng vàng, giữ topology Kim và khoảng đen. Đã mở **`S/star-sigils-set-sheet.jpg`**, đủ bảy ô đúng thứ tự. Anh xem hạt sao và độ phân biệt với Hư Không; line lề trái 15 px, crack lề trên 22 px. Nền còn lệch 1/255 ở góc, giữ nguyên.

## Kết quả làn 3

Đã làm lần lượt đủ **13 hệ**, thêm **89 PNG + 89 prompt + 13 tấm ghép** trong S, dùng lại hai ảnh Hỏa đã có; tổng bộ chọn **91 ảnh**. Đúng **89 lần `image_gen`**, không vẽ lại vì không ảnh nào tự chấm dưới 8; không gặp hạn mức. Tất cả tấm ghép đã mở bằng `view_image`. Không bỏ hệ/hạng mục nào; không hậu kỳ làm sạch nền hoặc tích hợp runtime vì ngoài phạm vi.

Anh cần xem 13 tấm ghép; chú ý các lề line/arcs hẹp, nền chưa đen tuyệt đối, lượng hoa lá/rãnh Mộc, chất Thổ ở hai dạng nứt, độ phân biệt Hư Không/Lôi và nhiễu màu lẻ của hex Ám. Đây là kết quả tự chấm ảnh nguồn theo phiếu, không thay nghiệm thu của anh hoặc chấm mù runtime.
