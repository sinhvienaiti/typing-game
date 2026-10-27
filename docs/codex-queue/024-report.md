# Phiếu 024 · Rà nghĩa tiếng Việt trong kho từ vựng chung

Ngày thực hiện: 27/10/2026. Mốc dữ liệu đối chiếu: `2b6f4b65a82c2908d14bd536b2eff6e0377e25cb`. Khi bắt đầu, `shared/vocabulary` chưa có thay đổi cục bộ; đã lưu ảnh chụp nội dung 100 file cấp trong phiên làm việc trước khi sửa.

Đã sửa **38 mục trong 31 file** `shared/vocabulary/levels/*.json`, chỉ trường `vi`. Trong đó: **21 mục chính tả**, **15 mục gộp nghĩa lặp do viết hoa hoặc vị trí dấu**, **2 mục bỏ nghĩa không phù hợp**. Giữ nguyên 100 cấp, 18.000 mục, `id`, `en`, `ipa`, thứ tự, các trường khác và định dạng `stableJson`. Lệnh tạo lại chạy thành công; `index.json` và `lookup.json` giữ nguyên từng byte.

Không chạy trình duyệt, dev server, build hoặc test của game. Không sửa game, Tu Tiên, media, mã nguồn công cụ hay dùng lệnh Git có ghi.

## 1. Kết quả quét bằng máy trước khi sửa

Tách token bằng Unicode `\p{L}[\p{L}\p{M}]*`, chuẩn hóa NFC và chuyển chữ thường khi đếm; dấu cách, dấu câu, gạch nối và chữ số là ranh giới. Đơn vị đếm là âm tiết viết rời của tiếng Việt; tên riêng, từ ngoại ngữ viết liền và ký hiệu chữ được đếm như một token, không suy diễn số âm tiết theo phát âm.

| Phép quét | Kết quả trên nguyên bản |
| --- | --- |
| Phạm vi | 100 cấp; 18.000 mục |
| Lượt âm tiết/token | 118.984 |
| Loại âm tiết/token phân biệt | 5.377 |
| Loại hiếm, xuất hiện ≤ 2 lần | 2.032 loại: 1.485 loại xuất hiện 1 lần, 547 loại xuất hiện 2 lần |
| Tổng lượt token hiếm | 2.579 lượt, nằm trong 2.022 mục |
| Cờ cấu trúc/dấu thanh | 1.095 loại; 1.513 lượt; nằm trong 1.053 mục |
| Cụm hỏi/ngã sai theo danh sách đối chiếu | 9 kết quả khớp, thuộc 7 mục; có kết quả lồng nhau |
| Nghĩa trùng nguyên văn sau tách bằng dấu chấm phẩy | 0 mục |
| Nghĩa lặp chỉ khác viết hoa/vị trí dấu | 15 mục |
| Nghĩa ghép có đủ từng thành phần đứng riêng bên cạnh | 14 mục |
| Mục có một nghĩa nằm trọn trong nghĩa khác theo ranh giới từ | 1.970 mục; đây là tập ứng viên rộng, không phải số lỗi |
| Hợp các mục được máy gắn cờ hiếm/cấu trúc/hỏi-ngã/lặp/ghép | 2.179 mục, đã khử trùng theo id |
| Đã sửa | 38 mục; 21 chính tả + 15 lặp cách viết + 2 nghĩa |
| Cần Claude xem | 29 mục; giữ nguyên phần còn nghi ngờ |

Bộ kiểm cấu trúc dùng danh sách phụ âm đầu và vần viết sẵn; xét các trường hợp `qu`, `gi`, `c/k`, `ng/ngh`, `gh`, vần `yê`; tách dấu thanh bằng NFD nhưng giữ dấu tạo chữ `ă/â/ê/ô/ơ/ư`. Kiểm tối đa một dấu thanh, dấu phải nằm trên nguyên âm, vần kết thúc `c/ch/p/t` chỉ nhận sắc hoặc nặng, và kiểm vị trí dấu trong cụm nguyên âm. Chấp nhận cả hai lối đặt dấu truyền thống/hiện đại với `oa/oe/uy` khi phù hợp, không đổi toàn kho sang một kiểu dấu.

Trong 1.095 loại bị gắn cờ có 1.074 loại ngoài bảng cấu trúc, 135 loại bị cờ thanh ở vần tắc, 1 loại sai vị trí dấu (`gỉa`), 1 loại có nhiều dấu thanh (`đềcalít`, từ vay mượn viết liền). Các nhóm có giao nhau. Tên riêng, từ vay mượn, thuật ngữ và ký hiệu như `internet`, `golf`, `axit`, `CH3` tạo nhiều cờ giả: **cờ máy không đồng nghĩa lỗi chính tả**. Bộ kiểm là bước sàng lọc hữu hạn, không phải từ điển xác nhận mọi âm tiết đúng/sai. Cách dùng hiếm chưa chắc chắn được chuyển vào bảng cần xem; không tự sửa từ địa phương hoặc thuật ngữ chỉ vì hiếm.

Đối chiếu hỏi/ngã tạo các biến thể hoán đổi hai dấu trong danh sách cụm quen, kể cả nhiều chữ sai cùng lúc; giữ ranh giới từng nghĩa khi tìm cụm. Các ví dụ chuẩn gồm `buồn bã`, `nghỉ ngơi`, `suy nghĩ`, `sửa chữa`, `sữa bò`, `dỗ dành`, `chủ nghĩa`, `nhiễm sắc thể`, `lễ rửa tội`. Cả 7 mục có kết quả hỏi/ngã đều đã được sửa. Không thay hàng loạt `chửa`, `rữa` hoặc `nghỉ`: những chữ này vẫn đúng trong ngữ cảnh khác, chẳng hạn `pregnant` và `rotting`.

| id | Cụm máy bắt | Cụm đúng |
| --- | --- | --- |
| L001-009 | buồn bả | buồn bã |
| L024-115 | chổ ở | chỗ ở |
| L088-051 | chủ nghỉa | chủ nghĩa |
| L088-051 | nhân văn chủ nghỉa | nhân văn chủ nghĩa |
| L040-085 | lể rữa tội | lễ rửa tội |
| L040-085 | rữa tội | rửa tội |
| L052-101 | dể giận | dễ giận |
| L044-112 | nhiểm sắc thể | nhiễm sắc thể |
| L098-105 | một muổng | một muỗng |

Sau khi sửa, chạy lại cùng bộ quét: **0 kết quả cụm hỏi/ngã sai**, **0 mục lặp chỉ khác viết hoa/vị trí dấu**, **0 mục lặp nguyên văn**. Còn 13 mục ghép có các thành phần đứng riêng, do các nghĩa đó vẫn đúng; đây không phải kiểm tra còn lỗi. Các cờ từ vay mượn và các trường hợp chưa rõ vẫn được giữ.

## 2. Quyết định cho đủ 14 mục ghép

Đã quét lại toàn bộ kho, không dừng ở cấp 056. Hai mục cuối là **deceive — L061-080** và **leaky — L081-150**. Không xóa một nghĩa đúng chỉ vì nó là thành phần của nghĩa ghép. Với `beer`, bỏ cả nghĩa ghép `rượu bia` vì đó là tên chung của nhóm đồ uống, không phải tên chính xác của beer; vẫn giữ mọi nghĩa ghép đúng ở các mục khác.

| Cấp | id | en | vi ban đầu | Quyết định và lý do |
| --- | --- | --- | --- | --- |
| 005 | L005-179 | usually | thường thường; thường lệ; thường | Giữ nguyên: «thường», «thường lệ», «thường thường» đều diễn đạt tần suất/thói quen; từ láy không phải nghĩa trùng hệt. |
| 008 | L008-050 | cow | bò cái; bò; cái | Bỏ «cái»; giữ «bò cái» và «bò» vì cả hai chỉ đúng con vật. |
| 013 | L013-138 | beer | bia; rượu; rượu bia | Giữ «bia»; bỏ «rượu» và «rượu bia» vì không đồng nghĩa chính xác với beer. |
| 019 | L019-065 | stove | lò; bếp lò; bếp | Giữ nguyên: «lò», «bếp», «bếp lò» đều chỉ thiết bị nấu/sưởi phù hợp. |
| 024 | L024-105 | asthma | suyễn; hen; hen suyễn | Giữ nguyên: «hen», «suyễn», «hen suyễn» đều là tên bệnh. |
| 025 | L025-048 | beat | đánh; đập; đánh đập | Giữ nguyên: «đánh», «đập», «đánh đập» đều có nghĩa tương ứng. |
| 025 | L025-127 | bet | cá; cược; cá cược | Giữ nguyên: «cá» có nghĩa đánh cược (như «cá với nhau»), «cược» và «cá cược» cũng đúng. |
| 026 | L026-112 | reduce | giảm; bớt; giảm bớt | Giữ nguyên: «giảm», «bớt», «giảm bớt» đều là các động từ phù hợp. |
| 026 | L026-150 | shift | thay đổi; thay; đổi | Giữ nguyên: «thay», «đổi», «thay đổi» đều diễn đạt sự chuyển đổi. |
| 027 | L027-072 | blind | mù; đui mù; đui | Giữ nguyên: «mù», «đui», «đui mù» đều diễn đạt mất khả năng nhìn. |
| 049 | L049-143 | torso | thân; thân mình; mình | Giữ nguyên: «thân», «mình», «thân mình» đều chỉ phần thân cơ thể. |
| 056 | L056-178 | await | chờ đợi; chờ; đợi | Giữ nguyên: «chờ», «đợi», «chờ đợi» đều có nghĩa tương ứng. |
| 061 | L061-080 | deceive | lừa; lừa bịp; bịp | Giữ nguyên: «lừa», «bịp», «lừa bịp» đều có nghĩa đánh lừa. |
| 081 | L081-150 | leaky | rò rỉ; rò; rỉ | Giữ nguyên: «rò», «rỉ», «rò rỉ» đều có thể chỉ tình trạng để chất lỏng thoát qua khe. |

## 3. Mọi mục đã sửa

Với 13 mục lặp do vị trí dấu, giữ cách viết xuất hiện trước để không mở rộng thành việc chuẩn hóa toàn kho. Hai mục lặp do viết hoa được gộp theo ngữ cảnh, trong đó giữ `Trái Đất` cho tên hành tinh. Ngoài ra, hai lỗi `ôông` và `bột nhồ` sau khi sửa tạo nghĩa trùng, nên gộp ngay.

| Cấp | id | en | vi cũ | vi mới | Lý do |
| --- | --- | --- | --- | --- | --- |
| 001 | L001-009 | sad | buồn; buồn bả; buồn rầu | buồn; buồn bã; buồn rầu | Sửa dấu hỏi thành dấu ngã trong từ láy «buồn bã». |
| 008 | L008-050 | cow | bò cái; bò; cái | bò cái; bò | Bỏ «cái»: đứng riêng không chỉ con bò; giữ cả «bò cái» và «bò». |
| 008 | L008-105 | grandfather | ông; ôông | ông | «Ôông» thừa chữ ô; sửa thành «ông» rồi bỏ nghĩa trùng. |
| 011 | L011-037 | cargo | hàng hóa; hàng hoá | hàng hóa | Hai cách đặt dấu cùng một nghĩa; giữ cách xuất hiện trước, bỏ bản lặp. |
| 013 | L013-138 | beer | bia; rượu; rượu bia | bia | Beer là bia; «rượu» chỉ đồ uống khác, «rượu bia» chỉ chung một nhóm đồ uống. |
| 014 | L014-058 | lock | khóa; ổ khóa; khoá | khóa; ổ khóa | Hai cách đặt dấu cùng một nghĩa; giữ cách xuất hiện trước, bỏ bản lặp. |
| 015 | L015-092 | repair | sửa chữa; chửa; sửa | sửa chữa; chữa; sửa | Trong nghĩa repair, phải viết «chữa»; «chửa» là mang thai. |
| 018 | L018-031 | satisfy | thỏa mãn; thoả mãn | thỏa mãn | Hai cách đặt dấu cùng một nghĩa; giữ cách xuất hiện trước, bỏ bản lặp. |
| 021 | L021-094 | dough | bột; bột nhồ; bột nhào | bột; bột nhào | «Bột nhồ» hỏng vần so với «bột nhào»; sửa rồi bỏ nghĩa trùng. |
| 022 | L022-132 | coordinate | tọa độ; toạ độ; điều phối | tọa độ; điều phối | Hai cách đặt dấu cùng một nghĩa; giữ cách xuất hiện trước, bỏ bản lặp. |
| 023 | L023-057 | vendor | ngưởi bán hàng rong | người bán hàng rong | Sửa «ngưởi» thành «người» trong cụm chỉ người bán hàng. |
| 024 | L024-115 | dwelling | chổ ở | chỗ ở | Sửa dấu hỏi thành dấu ngã: «chỗ ở». |
| 028 | L028-037 | republic | cộng hòa; cộng hoà | cộng hòa | Hai cách đặt dấu cùng một nghĩa; giữ cách xuất hiện trước, bỏ bản lặp. |
| 031 | L031-080 | irrigation | thủy lợi; thuỷ lợi | thủy lợi | Hai cách đặt dấu cùng một nghĩa; giữ cách xuất hiện trước, bỏ bản lặp. |
| 039 | L039-102 | dissolve | hoà tan; hòa tan; cảnh mờ dần (điện ảnh) | hoà tan; cảnh mờ dần (điện ảnh) | Hai cách đặt dấu cùng một nghĩa; giữ cách xuất hiện trước, bỏ bản lặp. |
| 040 | L040-085 | baptism | lể rữa tội | lễ rửa tội | Sửa hai dấu thanh: «lể» → «lễ», «rữa» → «rửa». |
| 040 | L040-090 | roadside | rệ đường | vệ đường | Sửa phụ âm đầu: «rệ đường» → «vệ đường». |
| 044 | L044-112 | chromosome | chất sinh sắt; nhiểm sắc thể | chất sinh sắt; nhiễm sắc thể | Sửa «nhiểm» → «nhiễm»; nghĩa «chất sinh sắt» chuyển Claude xem. |
| 047 | L047-137 | soviet | xô viết; thuộc Liên Xô; Xô viết | xô viết; thuộc Liên Xô | Bỏ nghĩa lặp chỉ khác viết hoa; giữ cách viết còn lại theo ngữ cảnh. |
| 047 | L047-146 | relief | рhù điêu | phù điêu | Thay chữ р Cyrillic (U+0440) bằng p Latin (U+0070). |
| 049 | L049-001 | abandoned | phóng đãng; truỵ lạc; trụy lạc | phóng đãng; truỵ lạc | Hai cách đặt dấu cùng một nghĩa; giữ cách xuất hiện trước, bỏ bản lặp. |
| 051 | L051-018 | legitimate | hợp pháp; hợp pháp hoá; hợp pháp hóa | hợp pháp; hợp pháp hoá | Hai cách đặt dấu cùng một nghĩa; giữ cách xuất hiện trước, bỏ bản lặp. |
| 052 | L052-101 | passionate | đam mê; dể giận | đam mê; dễ giận | Sửa dấu hỏi thành dấu ngã: «dễ giận». |
| 053 | L053-166 | accommodation | phòng ở; chỗ ở; nhá ở | phòng ở; chỗ ở; nhà ở | Sửa dấu sắc thành dấu huyền: «nhá ở» → «nhà ở». |
| 057 | L057-171 | translator | thông dịch viên; dịch gỉa | thông dịch viên; dịch giả | Đưa dấu hỏi về đúng nguyên âm a: «gỉa» → «giả». |
| 068 | L068-012 | pulpit | tòa giảng; toà giảng; giảng đài | tòa giảng; giảng đài | Hai cách đặt dấu cùng một nghĩa; giữ cách xuất hiện trước, bỏ bản lặp. |
| 071 | L071-011 | fossil | hoá thạch; hóa thạch; thuộc hóa thạch | hoá thạch; thuộc hóa thạch | Hai cách đặt dấu cùng một nghĩa; giữ cách xuất hiện trước, bỏ bản lặp. |
| 071 | L071-030 | verdict | bản án; phán quyểt | bản án; phán quyết | Âm tiết kết thúc bằng t dùng sắc/nặng; sửa «quyểt» → «quyết». |
| 071 | L071-118 | nag | cằn nhằn; càu nhàu; ỷ eo | cằn nhằn; càu nhàu; ỉ eo | Sửa «ỷ eo» → «ỉ eo», chỉ sự càu nhàu. |
| 076 | L076-181 | screwdriver | chìa vít; tuộc vít; tuốc-nơ-vít | chìa vít; tuốc vít; tuốc-nơ-vít | Sửa phụ âm cuối trong tên dụng cụ: «tuộc vít» → «tuốc vít». |
| 077 | L077-130 | latent | ngầm; ngấm ngần; âm ỉ | ngầm; ngấm ngầm; âm ỉ | Sửa phụ âm cuối: «ngấm ngần» → «ngấm ngầm». |
| 079 | L079-119 | extraterrestrial | ngoài trái đất; ngoài Trái Đất; ngoài hành tinh | ngoài Trái Đất; ngoài hành tinh | Bỏ nghĩa lặp chỉ khác viết hoa; giữ cách viết còn lại theo ngữ cảnh. |
| 088 | L088-015 | diffuse | khuếch tán; lan toả; lan tỏa | khuếch tán; lan toả | Hai cách đặt dấu cùng một nghĩa; giữ cách xuất hiện trước, bỏ bản lặp. |
| 088 | L088-051 | humanism | chủ nghĩa nhân văn; chủ nghĩa nhân bản; nhân văn chủ nghỉa | chủ nghĩa nhân văn; chủ nghĩa nhân bản; nhân văn chủ nghĩa | Sửa «nghỉa» → «nghĩa» trong cụm «chủ nghĩa». |
| 094 | L094-164 | blackbird | hạch thước điẻu | hạch thước điểu | Sửa vần và dấu «điẻu» → «điểu»; cụm «hạch thước» chuyển Claude xem. |
| 098 | L098-035 | smut | muội than, mồ hóng; bệnh than đen (ở cây ngũ cốc); nấm than đen | muội than, bồ hóng; bệnh than đen (ở cây ngũ cốc); nấm than đen | Sửa phụ âm đầu: «mồ hóng» → «bồ hóng». |
| 098 | L098-105 | spoonful | một muổng | một muỗng | Sửa dấu hỏi thành dấu ngã: «muổng» → «muỗng». |
| 099 | L099-083 | quicksilver | thuỷ ngân; thủy ngân; hay thay đổi thất thường | thuỷ ngân; hay thay đổi thất thường | Hai cách đặt dấu cùng một nghĩa; giữ cách xuất hiện trước, bỏ bản lặp. |

## 4. Cần Claude xem

Các phần ghi trong bảng dưới đây **chưa sửa**. Riêng `chromosome` và `blackbird` đã sửa lỗi âm tiết chắc chắn ở phần khác của cùng mục; phần nghĩa đang nghi ngờ vẫn được giữ. Không suy đoán cách thay thế từ một chuỗi hỏng hoặc từ một thuật ngữ hiếm.

| Cấp | id | en | Phần chưa sửa | Cần đối chiếu |
| --- | --- | --- | --- | --- |
| 006 | L006-141 | cheese | phó mát | Có thể là biến thể tên gọi vay mượn của «pho mát»; chưa đủ căn cứ để sửa hoặc gộp. |
| 007 | L007-111 | nurse | bảo mỗ | Có thể là cách đọc Hán Việt cũ; chưa đủ căn cứ để coi là sai «bảo mẫu». |
| 023 | L023-086 | whiskey | uytky; huých-ki | Dạng phiên âm whiskey bất thường; cần chốt chuẩn phiên âm, giữ nguyên. |
| 028 | L028-177 | angle | gốc | Đứng đầu nghĩa angle; có thể sai «góc» nhưng còn tùy nghĩa động từ «bắt nguồn»; cần rà cả mục. |
| 033 | L033-057 | abandon | bộm | Không xác định được nghĩa đơn tương ứng abandon; cần đối chiếu nguồn trước khi bỏ. |
| 033 | L033-148 | circus | xiệc | Có thể là biến thể địa phương/cách ghi cũ của «xiếc»; chưa tự gộp. |
| 035 | L035-104 | pupil | ngươi | Cần xác nhận cách dùng độc lập nghĩa pupil hay nên là «con ngươi». |
| 036 | L036-127 | volcano | hoả diệm sơn; hoả diễm sơn | Cần đối chiếu hai cách đọc Hán Việt, chưa tự gộp. |
| 038 | L038-040 | nanny | nhũ ảo | Từ Hán Việt hiếm; cần xác nhận nghĩa nanny. |
| 039 | L039-048 | mummy | uây khyếm mẹ | Cụm hỏng cấu trúc và nghĩa; không suy đoán lời dịch thay thế. «Xác ướp» và «mẹ» vẫn giữ. |
| 041 | L041-027 | asbestos | miăng | Có thể là cách rút gọn/cách ghi cũ của amiăng; chưa đủ căn cứ để bỏ. |
| 044 | L044-112 | chromosome | chất sinh sắt | Nghĩa rất đáng ngờ với chromosome; chỉ sửa chắc chắn «nhiểm» → «nhiễm» ở nghĩa kế bên. |
| 051 | L051-016 | mop | bĩu môi | Mop có thể có nghĩa cổ liên quan nhăn mặt; cần tra nguồn trước khi kết luận sai. |
| 052 | L052-055 | rainbow | lẹm | Chưa xác nhận được nghĩa rainbow; cần đối chiếu từ địa phương/nguồn gốc. |
| 061 | L061-152 | viper | rắn vipe | Phiên âm hiếm của viper; chưa đổi sang tên loài cụ thể. |
| 062 | L062-035 | intimidate | trộ | Chưa xác nhận được nghĩa intimidate; cần rà từ địa phương/cách ghi cũ. |
| 063 | L063-024 | kelvin | kenvin | Có vẻ sai tên kelvin; cần chốt quy tắc viết tên đơn vị vay mượn. |
| 069 | L069-092 | jingle | xủng xoảng | Từ tượng thanh hiếm; cần xác nhận cách viết, chưa thay bằng «loảng xoảng». |
| 072 | L072-016 | pioneer | namviet | Chuỗi bất thường trong nghĩa pioneer; không đoán thành «tiên phong». |
| 073 | L073-055 | carbohydrate | hyđat-cacbon | Có thể thiếu r trong tên hợp chất; cần chốt cách phiên âm chuẩn. |
| 074 | L074-176 | hyperbolic | hypebolic | Dạng thuật ngữ toán học đáng ngờ; cần xác nhận hypécbol/hyperbolic và quy ước của kho. |
| 079 | L079-141 | placenta | thực giá noãn | Có thể là thuật ngữ thực vật học, không tự thay theo nghĩa nhau thai. |
| 080 | L080-050 | motley | tạp nhạp | Cần xác nhận biến thể «tạp nham»/cách dùng địa phương; giữ nguyên. |
| 084 | L084-068 | plummet | lập loòng | Cụm không rõ nghĩa với plummet; không đoán lời thay thế. |
| 085 | L085-081 | soot | lọ; nghẹ | Các nghĩa đơn lạ của soot; có thể là cách ghi cũ/từ địa phương, cần đối chiếu. |
| 088 | L088-057 | bushy | xum xuê | Cần chốt biến thể chính tả với «sum suê»; chưa sửa đồng loạt theo cảm tính. |
| 094 | L094-164 | blackbird | hạch thước | Đã sửa «điẻu» → «điểu»; phần «hạch thước» vẫn cần kiểm chứng tên chim. |
| 098 | L098-070 | stubble | tót | Nghĩa đơn hiếm của stubble; chưa xác nhận để bỏ. |
| 098 | L098-130 | preamble | biện ngôn | Nghĩa hiếm của preamble; cần đối chiếu xem có sai «biền ngôn» hay thuật ngữ cũ. |

## 5. Kết quả ba lệnh kiểm bắt buộc

### 5.1. Tạo lại và validateLevels

Lệnh: `node scripts/generate-vocabulary.mjs`. **Mã thoát 0.**

```text
Generated vocabulary index/lookup for 18000 entries across 100 levels.
```

### 5.2. Đọc lại đủ 100 file bằng Node

**Mã thoát 0.** Đối chiếu theo mốc Git cố định đã khớp dữ liệu lúc bắt đầu. Kiểm từng vị trí mục, đủ trường `id/en/ipa`, mọi trường ngoài `vi`, metadata cấp, danh sách file, số mục và `stableJson`; kiểm hai file sinh ra giữ nguyên từng byte.

```bash
node --input-type=module <<'NODE'
import fs from 'node:fs';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { stableJson } from './scripts/vocabulary-core.mjs';
const revision = '2b6f4b65a82c2908d14bd536b2eff6e0377e25cb';
const dir = 'shared/vocabulary/levels';
const files = fs.readdirSync(dir).filter(f => /^\d{3}\.json$/.test(f)).sort();
const originalFiles = execFileSync('git', ['ls-tree', '--name-only', revision + ':' + dir], {encoding:'utf8'})
 .trim().split('\n').filter(f => /^\d{3}\.json$/.test(f)).sort();
assert.equal(files.length, 100);
assert.deepEqual(files, originalFiles);
let total = 0, changed = 0;
for (const file of files) {
 const path = dir + '/' + file;
 const raw = fs.readFileSync(path, 'utf8');
 const before = JSON.parse(execFileSync('git', ['show', revision + ':' + path], {encoding:'utf8'}));
 const after = JSON.parse(raw);
 assert.equal(raw, stableJson(after), path + ': stableJson');
 assert.equal(after.entries.length, before.entries.length, path + ': số mục');
 for (let i = 0; i < after.entries.length; i++) {
  const a = after.entries[i], b = before.entries[i];
  for (const key of ['id', 'en', 'ipa']) {
   assert.equal(typeof a[key], 'string');
   assert.ok(a[key].trim());
   assert.equal(a[key], b[key], path + ':' + i + ':' + key);
  }
  assert.equal(typeof a.vi, 'string');
  assert.ok(a.vi.trim());
  if (a.vi !== b.vi) changed++;
  total++;
 }
 const omitVi = d => ({...d, entries:d.entries.map(({vi, ...rest}) => rest)});
 assert.deepEqual(omitVi(after), omitVi(before), path + ': chỉ vi được đổi');
}
for (const name of ['index.json', 'lookup.json']) {
 const path = 'shared/vocabulary/' + name;
 const before = execFileSync('git', ['show', revision + ':' + path]);
 assert.ok(fs.readFileSync(path).equals(before), path + ': phải giữ nguyên');
}
console.log('PASS: ' + files.length + ' file, ' + total + ' mục; ' + changed + ' mục đổi vi.');
console.log('PASS: id/en/ipa, số mục, thứ tự, các trường khác và stableJson giữ nguyên.');
console.log('PASS: index.json và lookup.json không đổi từng byte.');
NODE
```

Kết quả:

```text
PASS: 100 file, 18000 mục; 38 mục đổi vi.
PASS: id/en/ipa, số mục, thứ tự, các trường khác và stableJson giữ nguyên.
PASS: index.json và lookup.json không đổi từng byte.
```

### 5.3. git diff --stat và toàn bộ git diff -U0 -- shared/vocabulary

Cả ba lệnh đọc diff bên dưới đều thoát **0**. Trong phạm vi phiếu, diff dữ liệu chỉ có **31 file cấp, 38 dòng vi thay đổi**; không có thay đổi index/lookup.

**Lưu ý trạng thái dùng chung:** ngay trước khi làm, `git status --short` đã ghi nhận thay đổi ở `games/dragon-hold`, `games/typing-defense`, `games/typing-survival` và một tài liệu Tu Tiên chưa theo dõi. Không sửa hoặc hoàn tác các thay đổi đó. Vì vậy `git diff --stat` toàn repo vẫn hiển thị ba đường dẫn game của làn khác; không thể làm cho thống kê toàn repo chỉ còn dữ liệu của phiếu mà không đụng công việc của họ. Thống kê giới hạn `shared/vocabulary` ngay bên dưới xác nhận phạm vi riêng của phiếu. Báo cáo này là file mới chưa theo dõi, nên chưa nằm trong `git diff --stat`.

Lệnh đúng nguyên văn `git diff --stat`:

```text
 games/dragon-hold                 | 0
 games/typing-defense              | 0
 games/typing-survival             | 2 +-
 shared/vocabulary/levels/001.json | 2 +-
 shared/vocabulary/levels/008.json | 4 ++--
 shared/vocabulary/levels/011.json | 2 +-
 shared/vocabulary/levels/013.json | 2 +-
 shared/vocabulary/levels/014.json | 2 +-
 shared/vocabulary/levels/015.json | 2 +-
 shared/vocabulary/levels/018.json | 2 +-
 shared/vocabulary/levels/021.json | 2 +-
 shared/vocabulary/levels/022.json | 2 +-
 shared/vocabulary/levels/023.json | 2 +-
 shared/vocabulary/levels/024.json | 2 +-
 shared/vocabulary/levels/028.json | 2 +-
 shared/vocabulary/levels/031.json | 2 +-
 shared/vocabulary/levels/039.json | 2 +-
 shared/vocabulary/levels/040.json | 4 ++--
 shared/vocabulary/levels/044.json | 2 +-
 shared/vocabulary/levels/047.json | 4 ++--
 shared/vocabulary/levels/049.json | 2 +-
 shared/vocabulary/levels/051.json | 2 +-
 shared/vocabulary/levels/052.json | 2 +-
 shared/vocabulary/levels/053.json | 2 +-
 shared/vocabulary/levels/057.json | 2 +-
 shared/vocabulary/levels/068.json | 2 +-
 shared/vocabulary/levels/071.json | 6 +++---
 shared/vocabulary/levels/076.json | 2 +-
 shared/vocabulary/levels/077.json | 2 +-
 shared/vocabulary/levels/079.json | 2 +-
 shared/vocabulary/levels/088.json | 4 ++--
 shared/vocabulary/levels/094.json | 2 +-
 shared/vocabulary/levels/098.json | 4 ++--
 shared/vocabulary/levels/099.json | 2 +-
 34 files changed, 39 insertions(+), 39 deletions(-)
```

Lệnh `git diff --stat -- shared/vocabulary`:

```text
 shared/vocabulary/levels/001.json | 2 +-
 shared/vocabulary/levels/008.json | 4 ++--
 shared/vocabulary/levels/011.json | 2 +-
 shared/vocabulary/levels/013.json | 2 +-
 shared/vocabulary/levels/014.json | 2 +-
 shared/vocabulary/levels/015.json | 2 +-
 shared/vocabulary/levels/018.json | 2 +-
 shared/vocabulary/levels/021.json | 2 +-
 shared/vocabulary/levels/022.json | 2 +-
 shared/vocabulary/levels/023.json | 2 +-
 shared/vocabulary/levels/024.json | 2 +-
 shared/vocabulary/levels/028.json | 2 +-
 shared/vocabulary/levels/031.json | 2 +-
 shared/vocabulary/levels/039.json | 2 +-
 shared/vocabulary/levels/040.json | 4 ++--
 shared/vocabulary/levels/044.json | 2 +-
 shared/vocabulary/levels/047.json | 4 ++--
 shared/vocabulary/levels/049.json | 2 +-
 shared/vocabulary/levels/051.json | 2 +-
 shared/vocabulary/levels/052.json | 2 +-
 shared/vocabulary/levels/053.json | 2 +-
 shared/vocabulary/levels/057.json | 2 +-
 shared/vocabulary/levels/068.json | 2 +-
 shared/vocabulary/levels/071.json | 6 +++---
 shared/vocabulary/levels/076.json | 2 +-
 shared/vocabulary/levels/077.json | 2 +-
 shared/vocabulary/levels/079.json | 2 +-
 shared/vocabulary/levels/088.json | 4 ++--
 shared/vocabulary/levels/094.json | 2 +-
 shared/vocabulary/levels/098.json | 4 ++--
 shared/vocabulary/levels/099.json | 2 +-
 31 files changed, 38 insertions(+), 38 deletions(-)
```

Toàn bộ kết quả `git diff -U0 -- shared/vocabulary`, không cắt bớt:

```diff
diff --git a/shared/vocabulary/levels/001.json b/shared/vocabulary/levels/001.json
index 68bc9e81..be9c99cb 100644
--- a/shared/vocabulary/levels/001.json
+++ b/shared/vocabulary/levels/001.json
@@ -57 +57 @@
-      "vi": "buồn; buồn bả; buồn rầu",
+      "vi": "buồn; buồn bã; buồn rầu",
diff --git a/shared/vocabulary/levels/008.json b/shared/vocabulary/levels/008.json
index 014cea91..924c7caa 100644
--- a/shared/vocabulary/levels/008.json
+++ b/shared/vocabulary/levels/008.json
@@ -303 +303 @@
-      "vi": "bò cái; bò; cái",
+      "vi": "bò cái; bò",
@@ -633 +633 @@
-      "vi": "ông; ôông",
+      "vi": "ông",
diff --git a/shared/vocabulary/levels/011.json b/shared/vocabulary/levels/011.json
index 7e140c43..855b1982 100644
--- a/shared/vocabulary/levels/011.json
+++ b/shared/vocabulary/levels/011.json
@@ -225 +225 @@
-      "vi": "hàng hóa; hàng hoá",
+      "vi": "hàng hóa",
diff --git a/shared/vocabulary/levels/013.json b/shared/vocabulary/levels/013.json
index 11e1a352..d213c3b2 100644
--- a/shared/vocabulary/levels/013.json
+++ b/shared/vocabulary/levels/013.json
@@ -831 +831 @@
-      "vi": "bia; rượu; rượu bia",
+      "vi": "bia",
diff --git a/shared/vocabulary/levels/014.json b/shared/vocabulary/levels/014.json
index e83623d8..9f23eef9 100644
--- a/shared/vocabulary/levels/014.json
+++ b/shared/vocabulary/levels/014.json
@@ -351 +351 @@
-      "vi": "khóa; ổ khóa; khoá",
+      "vi": "khóa; ổ khóa",
diff --git a/shared/vocabulary/levels/015.json b/shared/vocabulary/levels/015.json
index dcc4a7b7..47747fe4 100644
--- a/shared/vocabulary/levels/015.json
+++ b/shared/vocabulary/levels/015.json
@@ -555 +555 @@
-      "vi": "sửa chữa; chửa; sửa",
+      "vi": "sửa chữa; chữa; sửa",
diff --git a/shared/vocabulary/levels/018.json b/shared/vocabulary/levels/018.json
index abadaf68..6b190d8c 100644
--- a/shared/vocabulary/levels/018.json
+++ b/shared/vocabulary/levels/018.json
@@ -189 +189 @@
-      "vi": "thỏa mãn; thoả mãn",
+      "vi": "thỏa mãn",
diff --git a/shared/vocabulary/levels/021.json b/shared/vocabulary/levels/021.json
index 9f46ccd5..c3bfb8af 100644
--- a/shared/vocabulary/levels/021.json
+++ b/shared/vocabulary/levels/021.json
@@ -567 +567 @@
-      "vi": "bột; bột nhồ; bột nhào",
+      "vi": "bột; bột nhào",
diff --git a/shared/vocabulary/levels/022.json b/shared/vocabulary/levels/022.json
index 510bd0bf..ba796d4e 100644
--- a/shared/vocabulary/levels/022.json
+++ b/shared/vocabulary/levels/022.json
@@ -795 +795 @@
-      "vi": "tọa độ; toạ độ; điều phối",
+      "vi": "tọa độ; điều phối",
diff --git a/shared/vocabulary/levels/023.json b/shared/vocabulary/levels/023.json
index 6fbeb381..2366fd51 100644
--- a/shared/vocabulary/levels/023.json
+++ b/shared/vocabulary/levels/023.json
@@ -345 +345 @@
-      "vi": "ngưởi bán hàng rong",
+      "vi": "người bán hàng rong",
diff --git a/shared/vocabulary/levels/024.json b/shared/vocabulary/levels/024.json
index 2c01f545..38860ba5 100644
--- a/shared/vocabulary/levels/024.json
+++ b/shared/vocabulary/levels/024.json
@@ -693 +693 @@
-      "vi": "chổ ở",
+      "vi": "chỗ ở",
diff --git a/shared/vocabulary/levels/028.json b/shared/vocabulary/levels/028.json
index 20991add..882f2d56 100644
--- a/shared/vocabulary/levels/028.json
+++ b/shared/vocabulary/levels/028.json
@@ -225 +225 @@
-      "vi": "cộng hòa; cộng hoà",
+      "vi": "cộng hòa",
diff --git a/shared/vocabulary/levels/031.json b/shared/vocabulary/levels/031.json
index d07662ff..6ccfc9ed 100644
--- a/shared/vocabulary/levels/031.json
+++ b/shared/vocabulary/levels/031.json
@@ -483 +483 @@
-      "vi": "thủy lợi; thuỷ lợi",
+      "vi": "thủy lợi",
diff --git a/shared/vocabulary/levels/039.json b/shared/vocabulary/levels/039.json
index bc014bb7..46d101d8 100644
--- a/shared/vocabulary/levels/039.json
+++ b/shared/vocabulary/levels/039.json
@@ -615 +615 @@
-      "vi": "hoà tan; hòa tan; cảnh mờ dần (điện ảnh)",
+      "vi": "hoà tan; cảnh mờ dần (điện ảnh)",
diff --git a/shared/vocabulary/levels/040.json b/shared/vocabulary/levels/040.json
index ff58cdeb..7cd85cb4 100644
--- a/shared/vocabulary/levels/040.json
+++ b/shared/vocabulary/levels/040.json
@@ -513 +513 @@
-      "vi": "lể rữa tội",
+      "vi": "lễ rửa tội",
@@ -543 +543 @@
-      "vi": "rệ đường",
+      "vi": "vệ đường",
diff --git a/shared/vocabulary/levels/044.json b/shared/vocabulary/levels/044.json
index c412649b..ede3fa3d 100644
--- a/shared/vocabulary/levels/044.json
+++ b/shared/vocabulary/levels/044.json
@@ -675 +675 @@
-      "vi": "chất sinh sắt; nhiểm sắc thể",
+      "vi": "chất sinh sắt; nhiễm sắc thể",
diff --git a/shared/vocabulary/levels/047.json b/shared/vocabulary/levels/047.json
index 95a93d8c..6646dee6 100644
--- a/shared/vocabulary/levels/047.json
+++ b/shared/vocabulary/levels/047.json
@@ -825 +825 @@
-      "vi": "xô viết; thuộc Liên Xô; Xô viết",
+      "vi": "xô viết; thuộc Liên Xô",
@@ -879 +879 @@
-      "vi": "рhù điêu",
+      "vi": "phù điêu",
diff --git a/shared/vocabulary/levels/049.json b/shared/vocabulary/levels/049.json
index 075d97f7..070509a3 100644
--- a/shared/vocabulary/levels/049.json
+++ b/shared/vocabulary/levels/049.json
@@ -9 +9 @@
-      "vi": "phóng đãng; truỵ lạc; trụy lạc",
+      "vi": "phóng đãng; truỵ lạc",
diff --git a/shared/vocabulary/levels/051.json b/shared/vocabulary/levels/051.json
index 99c9ffdc..06221b68 100644
--- a/shared/vocabulary/levels/051.json
+++ b/shared/vocabulary/levels/051.json
@@ -111 +111 @@
-      "vi": "hợp pháp; hợp pháp hoá; hợp pháp hóa",
+      "vi": "hợp pháp; hợp pháp hoá",
diff --git a/shared/vocabulary/levels/052.json b/shared/vocabulary/levels/052.json
index 934bb9fe..9086690a 100644
--- a/shared/vocabulary/levels/052.json
+++ b/shared/vocabulary/levels/052.json
@@ -609 +609 @@
-      "vi": "đam mê; dể giận",
+      "vi": "đam mê; dễ giận",
diff --git a/shared/vocabulary/levels/053.json b/shared/vocabulary/levels/053.json
index 12ed5ef5..e711f0fd 100644
--- a/shared/vocabulary/levels/053.json
+++ b/shared/vocabulary/levels/053.json
@@ -999 +999 @@
-      "vi": "phòng ở; chỗ ở; nhá ở",
+      "vi": "phòng ở; chỗ ở; nhà ở",
diff --git a/shared/vocabulary/levels/057.json b/shared/vocabulary/levels/057.json
index fa1e0b77..4c1f037e 100644
--- a/shared/vocabulary/levels/057.json
+++ b/shared/vocabulary/levels/057.json
@@ -1029 +1029 @@
-      "vi": "thông dịch viên; dịch gỉa",
+      "vi": "thông dịch viên; dịch giả",
diff --git a/shared/vocabulary/levels/068.json b/shared/vocabulary/levels/068.json
index b2757185..8631f47b 100644
--- a/shared/vocabulary/levels/068.json
+++ b/shared/vocabulary/levels/068.json
@@ -75 +75 @@
-      "vi": "tòa giảng; toà giảng; giảng đài",
+      "vi": "tòa giảng; giảng đài",
diff --git a/shared/vocabulary/levels/071.json b/shared/vocabulary/levels/071.json
index b370b109..2fd1e7d1 100644
--- a/shared/vocabulary/levels/071.json
+++ b/shared/vocabulary/levels/071.json
@@ -69 +69 @@
-      "vi": "hoá thạch; hóa thạch; thuộc hóa thạch",
+      "vi": "hoá thạch; thuộc hóa thạch",
@@ -183 +183 @@
-      "vi": "bản án; phán quyểt",
+      "vi": "bản án; phán quyết",
@@ -711 +711 @@
-      "vi": "cằn nhằn; càu nhàu; ỷ eo",
+      "vi": "cằn nhằn; càu nhàu; ỉ eo",
diff --git a/shared/vocabulary/levels/076.json b/shared/vocabulary/levels/076.json
index 4041af1e..4f66acf3 100644
--- a/shared/vocabulary/levels/076.json
+++ b/shared/vocabulary/levels/076.json
@@ -1089 +1089 @@
-      "vi": "chìa vít; tuộc vít; tuốc-nơ-vít",
+      "vi": "chìa vít; tuốc vít; tuốc-nơ-vít",
diff --git a/shared/vocabulary/levels/077.json b/shared/vocabulary/levels/077.json
index 57e6c573..588a5867 100644
--- a/shared/vocabulary/levels/077.json
+++ b/shared/vocabulary/levels/077.json
@@ -783 +783 @@
-      "vi": "ngầm; ngấm ngần; âm ỉ",
+      "vi": "ngầm; ngấm ngầm; âm ỉ",
diff --git a/shared/vocabulary/levels/079.json b/shared/vocabulary/levels/079.json
index 53f8e499..4c8cbe22 100644
--- a/shared/vocabulary/levels/079.json
+++ b/shared/vocabulary/levels/079.json
@@ -717 +717 @@
-      "vi": "ngoài trái đất; ngoài Trái Đất; ngoài hành tinh",
+      "vi": "ngoài Trái Đất; ngoài hành tinh",
diff --git a/shared/vocabulary/levels/088.json b/shared/vocabulary/levels/088.json
index 607daba0..74d92204 100644
--- a/shared/vocabulary/levels/088.json
+++ b/shared/vocabulary/levels/088.json
@@ -93 +93 @@
-      "vi": "khuếch tán; lan toả; lan tỏa",
+      "vi": "khuếch tán; lan toả",
@@ -309 +309 @@
-      "vi": "chủ nghĩa nhân văn; chủ nghĩa nhân bản; nhân văn chủ nghỉa",
+      "vi": "chủ nghĩa nhân văn; chủ nghĩa nhân bản; nhân văn chủ nghĩa",
diff --git a/shared/vocabulary/levels/094.json b/shared/vocabulary/levels/094.json
index 0b049b5d..94d9ee7b 100644
--- a/shared/vocabulary/levels/094.json
+++ b/shared/vocabulary/levels/094.json
@@ -987 +987 @@
-      "vi": "hạch thước điẻu",
+      "vi": "hạch thước điểu",
diff --git a/shared/vocabulary/levels/098.json b/shared/vocabulary/levels/098.json
index 3ee68dfa..42622f93 100644
--- a/shared/vocabulary/levels/098.json
+++ b/shared/vocabulary/levels/098.json
@@ -213 +213 @@
-      "vi": "muội than, mồ hóng; bệnh than đen (ở cây ngũ cốc); nấm than đen",
+      "vi": "muội than, bồ hóng; bệnh than đen (ở cây ngũ cốc); nấm than đen",
@@ -633 +633 @@
-      "vi": "một muổng",
+      "vi": "một muỗng",
diff --git a/shared/vocabulary/levels/099.json b/shared/vocabulary/levels/099.json
index f9aca53f..bde71c7a 100644
--- a/shared/vocabulary/levels/099.json
+++ b/shared/vocabulary/levels/099.json
@@ -501 +501 @@
-      "vi": "thuỷ ngân; thủy ngân; hay thay đổi thất thường",
+      "vi": "thuỷ ngân; hay thay đổi thất thường",
```

## Phụ lục A. Đầy đủ âm tiết/token hiếm trên nguyên bản

Danh sách gồm cả tiếng Việt, từ vay mượn, tên riêng và ký hiệu theo cách tách token đã mô tả. Mỗi loại chỉ xuất hiện một lần trong danh sách; con số tiêu đề nhóm là tần suất trên toàn kho trước khi sửa. Hiếm chỉ là tín hiệu để xem ngữ cảnh, không phải lý do tự sửa.

<details>
<summary>2.032 loại hiếm, chia theo tần suất 1 hoặc 2</summary>


### Xuất hiện 1 lần: 1485 loại

| STT trong nhóm | Âm tiết/token |
| --- | --- |
| 1–20 | `aah`, `abc`, `abs`, `ạch`, `actin`, `adonis`, `adrenalin`, `affirmed`, `ag`, `agon`, `aides`, `alabama`, `alaska`, `all`, `allegro`, `alps`, `altruistic`, `amen`, `amiăng`, `amin` |
| 21–40 | `amino`, `amoni`, `ampe`, `amyl`, `amyloid`, `anaconda`, `anchorage`, `anglo`, `anxet`, `apollo`, `aria`, `armenia`, `armeria`, `artie`, `asen`, `asperula`, `aspirin`, `ate`, `attica`, `avatar` |
| 41–60 | `axetic`, `ăngten`, `bả`, `bạ`, `baba`, `babel`, `babu`, `babylon`, `bach`, `backhand`, `balboa`, `banjô`, `báp`, `barbary`, `barbulata`, `barie`, `basel`, `basilica`, `bastille`, `bằm` |
| 61–80 | `bặm`, `bẫm`, `bần`, `bây`, `bậy`, `beagle`, `beat`, `béc`, `benzen`, `benzoin`, `beo`, `bẽo`, `bẹo`, `bép`, `berber`, `beri`, `berserker`, `beryl`, `bet`, `bễ` |
| 81–100 | `bệt`, `bêta`, `biếu`, `bigfoot`, `biker`, `bikini`, `bím`, `bina`, `bingo`, `bĩnh`, `bịnh`, `birdie`, `bison`, `bit`, `bitmut`, `bitum`, `bỉu`, `bĩu`, `bizon`, `blazer` |
| 101–120 | `blouse`, `bõ`, `board`, `bob`, `bobsled`, `boer`, `bogey`, `bohemia`, `bon`, `bonaparte`, `bõng`, `bọng`, `bonus`, `boongke`, `boothe`, `bop`, `bordeaux`, `boulder`, `bowls`, `boxer` |
| 121–140 | `bôm`, `bộm`, `bổn`, `bồng`, `bỗng`, `bợ`, `bợm`, `bơn`, `braille`, `branđi`, `brant`, `brazil`, `brent`, `brie`, `brill`, `bu`, `bụ`, `bụa`, `bục`, `buffet` |
| 141–160 | `bugle`, `bulgaria`, `bulldog`, `bún`, `bủng`, `bungee`, `bunting`, `buồi`, `buông`, `burgundy`, `burrito`, `burton`, `butte`, `butyl`, `bự`, `bươm`, `by`, `byte`, `byzantine`, `cabernet` |
| 161–180 | `cacbonic`, `cacbua`, `cad`, `caddie`, `cadence`, `cađimi`, `cafêin`, `caffein`, `cairn`, `california`, `calypso`, `camera`, `campuchia`, `candela`, `candida`, `canvê`, `canxi`, `cảo`, `cappuccino`, `cara` |
| 181–200 | `caramen`, `caraôkê`, `carbine`, `carnot`, `carolina`, `carte`, `cascade`, `castor`, `catmi`, `catwalk`, `caviar`, `cắc`, `cấn`, `câng`, `cầy`, `ch`, `chả`, `chác`, `chancery`, `chang` |
| 201–220 | `chảng`, `charades`, `chau`, `chằng`, `chặng`, `chây`, `chấy`, `chelat`, `chẽn`, `chẹn`, `chennai`, `chess`, `chét`, `chêm`, `chiền`, `chiện`, `chiếp`, `chimera`, `chino`, `chipotle` |
| 221–240 | `cholesterol`, `chong`, `chổ`, `chôm`, `chốn`, `chợp`, `chục`, `chũi`, `chum`, `chúm`, `chun`, `chuôi`, `chuồn`, `chừ`, `chững`, `cicero`, `cisco`, `cla`, `clare`, `clarinet` |
| 241–260 | `class`, `clementine`, `clo`, `clocks`, `cntt`, `coca`, `cocktail`, `cỏi`, `cola`, `collagen`, `collie`, `collins`, `colt`, `còm`, `compost`, `concord`, `condor`, `còng`, `contextual`, `cóp` |
| 261–280 | `copy`, `corset`, `cortisol`, `corvus`, `cos`, `cosin`, `coupé`, `cox`, `cỗ`, `cỗi`, `cội`, `côngtenơ`, `côngxoocxiom`, `cời`, `cracker`, `creeps`, `crescendo`, `crích`, `crown`, `crô` |
| 281–300 | `crôm`, `cun`, `cụp`, `cupcake`, `cupid`, `curb`, `curie`, `cựa`, `cyclooxygenase`, `dả`, `dada`, `dahl`, `dái`, `daman`, `dan`, `darling`, `dát`, `dáy`, `dằn`, `dậm` |
| 301–320 | `dấn`, `ddt`, `decagam`, `delaware`, `deli`, `delicious`, `deuce`, `devices`, `dề`, `dể`, `dế`, `diesel`, `diệc`, `diễm`, `diệm`, `diếp`, `diệp`, `digan`, `din`, `dingue` |
| 321–340 | `disco`, `diva`, `dodo`, `doi`, `dọi`, `don`, `dona`, `dong`, `donna`, `donut`, `dopamine`, `dorado`, `dorsi`, `dory`, `dos`, `dot`, `dông`, `dũa`, `dulcamara`, `dúm` |
| 341–360 | `dụm`, `duvet`, `dưng`, `dửng`, `dượng`, `đanh`, `đẫn`, `đẩu`, `đẫy`, `đẽ`, `đem`, `đèo`, `đềcalít`, `đênh`, `đễnh`, `đểu`, `đỉa`, `điẻu`, `đinamit`, `đĩnh` |
| 361–380 | `địt`, `đò`, `đoàng`, `đom`, `đóm`, `đong`, `đơ`, `đơm`, `đớp`, `đớt`, `đrô`, `đũng`, `đuých`, `eczema`, `edwardian`, `egg`, `einsteini`, `electron`, `elip`, `elves` |
| 381–400 | `emu`, `én`, `enzim`, `èo`, `éo`, `episcopal`, `epsilon`, `eri`, `espresso`, `estonia`, `estrogen`, `ethylic`, `etyl`, `etylen`, `euro`, `everglades`, `exchange`, `eyre`, `êmia`, `fawkes` |
| 401–420 | `fedora`, `feet`, `ferret`, `fif`, `filler`, `flanen`, `florida`, `florua`, `fomanđêhít`, `fractal`, `frăng`, `freelance`, `freelancer`, `fresco`, `frigate`, `frông`, `fructoza`, `fudge`, `funk`, `g` |
| 421–440 | `gá`, `gãi`, `gal`, `galê`, `gambit`, `gang`, `gangster`, `gao`, `gáp`, `gar`, `gàu`, `gắm`, `gắp`, `gấm`, `gelatin`, `genoa`, `gestapo`, `geum`, `ghe`, `ghềnh` |
| 441–460 | `ghêpa`, `ghì`, `ghìm`, `giạ`, `gỉa`, `giảo`, `giăm`, `giậm`, `giần`, `gíc`, `gie`, `giec`, `gièm`, `gien`, `giếm`, `giềng`, `giỏ`, `gioan`, `gioăng`, `gióng` |
| 461–480 | `giô`, `giội`, `giời`, `gipsi`, `giũa`, `glu`, `glucozơ`, `glutamat`, `gluten`, `go`, `goá`, `gopher`, `gổ`, `gôm`, `gột`, `gở`, `grad`, `gradien`, `graduale`, `graffiti` |
| 481–500 | `granola`, `greyhound`, `groves`, `gù`, `guacamole`, `gục`, `guinea`, `guinée`, `gulag`, `gulliver`, `gulo`, `guộc`, `guru`, `guy`, `gym`, `hacker`, `hackney`, `haiku`, `hajj`, `hám` |
| 501–520 | `hampshire`, `han`, `hán`, `harlequin`, `hatchback`, `hawaii`, `hays`, `hắng`, `hâu`, `hấu`, `hebrew`, `hebrides`, `heli`, `heller`, `hemoglobin`, `henri`, `herpes`, `hertz`, `hex`, `hê` |
| 521–540 | `hếch`, `hêli`, `hên`, `hi`, `hích`, `hiđrocacbon`, `hiđrô`, `hiềm`, `highlighter`, `hind`, `hindi`, `hoắm`, `hobbit`, `hoen`, `hoét`, `hogan`, `hoi`, `holographic`, `hom`, `homer` |
| 541–560 | `hong`, `hòng`, `hoóc`, `hook`, `hộc`, `hỗm`, `hông`, `hởi`, `hỡi`, `hớp`, `huề`, `huệ`, `hula`, `hũm`, `hummus`, `hun`, `hungary`, `huyện`, `hừ`, `hực` |
| 561–580 | `hừng`, `hydrocacbon`, `hyđat`, `hyđrô`, `hypebolic`, `ibuprofen`, `ịch`, `ictêri`, `ii`, `iii`, `illinois`, `imam`, `ỉn`, `inch`, `indonesia`, `inner`, `insơ`, `insulin`, `iođ`, `ionia` |
| 581–600 | `ionic`, `iot`, `iốt`, `irving`, `israel`, `ittêri`, `jalapeno`, `jasper`, `java`, `jean`, `jeep`, `jig`, `jihadi`, `jukebox`, `jumpsuit`, `jung`, `kangaroo`, `kansas`, `kappa`, `karate` |
| 601–620 | `kat`, `kebab`, `kẻng`, `kentucky`, `kenvin`, `kếp`, `kêrôsin`, `kha`, `khaki`, `kham`, `khàn`, `khàng`, `khè`, `khép`, `khế`, `khều`, `khiêng`, `khò`, `khoả`, `khui` |
| 621–640 | `khuông`, `khụy`, `khuya`, `khuyển`, `khước`, `khyếm`, `khz`, `kiêm`, `kiễng`, `kiều`, `kilôgam`, `kilt`, `kimono`, `kin`, `kinaza`, `kinky`, `kít`, `km`, `koala`, `kos` |
| 641–660 | `kosher`, `kremli`, `kremlin`, `kris`, `kyrgyzstan`, `l`, `lacrosse`, `lactoza`, `lager`, `lài`, `lambert`, `lantan`, `lảo`, `láp`, `largo`, `latex`, `latissimus`, `latte`, `lẫm`, `league` |
| 661–680 | `leave`, `léc`, `led`, `lém`, `lẹm`, `lẻn`, `lép`, `let`, `lev`, `lể`, `lênh`, `lì`, `libido`, `lied`, `liệng`, `limerick`, `limô`, `lin`, `lindy`, `ling` |
| 681–700 | `links`, `linsơ`, `lip`, `líp`, `lipid`, `lister`, `lithi`, `liti`, `loan`, `loảng`, `loanh`, `lóc`, `locus`, `loét`, `logan`, `loi`, `lói`, `lom`, `lọn`, `lõng` |
| 701–720 | `loòng`, `lổ`, `lôgô`, `lôn`, `lổn`, `lsd`, `lú`, `luẩn`, `lucifer`, `lug`, `lùm`, `lumen`, `lún`, `luộm`, `lupus`, `lux`, `luỹ`, `luýt`, `lympho`, `mả` |
| 721–740 | `mac`, `macarôni`, `macca`, `mace`, `macma`, `mactet`, `mademoiselle`, `magie`, `magiê`, `magnum`, `mahatma`, `make`, `mako`, `malta`, `manga`, `mangan`, `manhattan`, `manila`, `manocanh`, `mantle` |
| 741–760 | `mão`, `margarin`, `margarita`, `marijuana`, `marketing`, `maroc`, `mars`, `marshals`, `marshmallow`, `martini`, `masters`, `matit`, `matte`, `maxi`, `maxwell`, `mayday`, `mayonnaise`, `mắng`, `mẫm`, `mấy` |
| 761–780 | `mdma`, `mecca`, `medicago`, `medusa`, `melatonin`, `meme`, `merino`, `merlin`, `methadone`, `metyl`, `mễ`, `mếch`, `mêtric`, `mị`, `mia`, `miăng`, `mica`, `mickey`, `micrômét`, `miligam` |
| 781–800 | `mills`, `milo`, `mini`, `minivan`, `minnesota`, `minor`, `mít`, `mocfin`, `modem`, `mói`, `molly`, `molypden`, `móm`, `monedula`, `montana`, `monte`, `moor`, `moose`, `móp`, `moray` |
| 801–820 | `mormon`, `moron`, `mosaic`, `mozzarella`, `mỗ`, `môgôn`, `mồng`, `mống`, `mônôgram`, `mú`, `múc`, `muffin`, `mull`, `mulligan`, `mùn`, `mùng`, `muỗi`, `muồng`, `muổng`, `mustang` |
| 821–840 | `mustelid`, `mụt`, `mướt`, `mỳ`, `myrtle`, `myrtus`, `n`, `nã`, `nạc`, `nacho`, `nái`, `namviet`, `nán`, `nancy`, `nạng`, `nano`, `napoléon`, `nato`, `natri`, `navajo` |
| 841–860 | `nặn`, `nelson`, `néo`, `nẹp`, `nepal`, `neutrino`, `nevada`, `new`, `nể`, `nệ`, `nếm`, `nết`, `nếu`, `ngác`, `ngách`, `ngạch`, `ngàn`, `ngạn`, `ngàng`, `ngao` |
| 861–880 | `ngắc`, `ngăm`, `ngần`, `ngầu`, `nghẹ`, `nghén`, `nghệch`, `nghênh`, `nghêu`, `nghỉa`, `nghịu`, `ngỏ`, `ngõ`, `ngoai`, `ngoe`, `ngoé`, `ngóng`, `ngỗ`, `ngố`, `ngốn` |
| 881–900 | `ngộp`, `ngỡ`, `nguẩy`, `ngút`, `nguỵ`, `ngừ`, `ngươi`, `ngưởi`, `nhài`, `nhãi`, `nhạn`, `nhang`, `nhạp`, `nhăng`, `nhâm`, `nhẩm`, `nhậu`, `nhẫy`, `nhen`, `nhẹp` |
| 901–920 | `nhếch`, `nhền`, `nhiểm`, `nhiêu`, `nhoàm`, `nhoè`, `nhòm`, `nhõng`, `nhót`, `nhồ`, `nhồm`, `nhổn`, `nhột`, `nhụy`, `níc`, `ních`, `nicotin`, `nicôtin`, `niềng`, `niết` |
| 921–940 | `niêu`, `nikel`, `ninja`, `ninkhursag`, `nitrit`, `nỏ`, `nó`, `noãn`, `noi`, `noodle`, `nốc`, `nt`, `nu`, `nucleic`, `nucleotide`, `núng`, `nuối`, `nức`, `nực`, `nứng` |
| 941–960 | `nương`, `nướu`, `oat`, `oát`, `oằn`, `oặt`, `oc`, `octan`, `odyssey`, `ọe`, `oh`, `ói`, `omega`, `oóc`, `ooh`, `opan`, `or`, `origami`, `osimi`, `osmerus` |
| 961–980 | `ounce`, `overdrive`, `own`, `oxit`, `oxyt`, `ozon`, `ồ`, `ối`, `ôông`, `ôxit`, `ờ`, `ợ`, `ỡm`, `ớn`, `paisley`, `palađi`, `panen`, `panh`, `pao`, `paprika` |
| 981–1000 | `para`, `paris`, `partridge`, `pasha`, `pastel`, `patê`, `penicillin`, `penny`, `penthouse`, `peptide`, `peptit`, `peso`, `phạc`, `phalanx`, `phang`, `phào`, `phau`, `phay`, `phất`, `phẩy` |
| 1001–1020 | `phèn`, `phét`, `phệ`, `phia`, `phịch`, `philippines`, `phoebe`, `phoi`, `phoric`, `phọt`, `photpho`, `phôn`, `phộng`, `phốtpho`, `phờ`, `phrăng`, `phủi`, `píc`, `piccolo`, `piedmont` |
| 1021–1040 | `pinball`, `pinto`, `plat`, `platin`, `plutoni`, `poaz`, `podcast`, `polo`, `polyetylen`, `polymerase`, `pom`, `pôke`, `pôni`, `pơ`, `pretzel`, `progesterone`, `proton`, `prô`, `pu`, `pug` |
| 1041–1060 | `punt`, `purê`, `pyxidanthera`, `quách`, `quạng`, `quắc`, `quặn`, `quặt`, `quẩn`, `quẫn`, `quây`, `quẩy`, `quậy`, `quệ`, `quỉ`, `quờ`, `quyện`, `quyểt`, `rá`, `rad` |
| 1061–1080 | `radian`, `rađơn`, `ragu`, `rainier`, `rao`, `rão`, `rạo`, `rap`, `rapper`, `rapsody`, `rát`, `ráu`, `ravioli`, `rayon`, `reel`, `reggae`, `remote`, `reni`, `rep`, `requiem` |
| 1081–1100 | `resort`, `retriever`, `retro`, `rể`, `rệ`, `rệp`, `rệu`, `rí`, `ria`, `rích`, `riềng`, `right`, `risotto`, `riu`, `ríu`, `riviera`, `rna`, `rọc`, `roche`, `rocker` |
| 1101–1120 | `rodeo`, `rọi`, `ròm`, `róm`, `romaine`, `router`, `roux`, `rộ`, `rôman`, `rôto`, `rớt`, `rudd`, `rún`, `rune`, `rúng`, `ruy`, `rựa`, `rường`, `ry`, `sà` |
| 1121–1140 | `sá`, `sac`, `salmonella`, `salsa`, `sạm`, `samurai`, `sảnh`, `sạo`, `sạp`, `saphia`, `sari`, `sarracenia`, `saskatchewan`, `sạt`, `satan`, `savoury`, `sax`, `saxon`, `saxophone`, `sảy` |
| 1141–1160 | `sắn`, `sậm`, `scat`, `schooner`, `scots`, `scrabble`, `script`, `se`, `sedan`, `seine`, `selen`, `senna`, `sent`, `sequin`, `serenade`, `serotonin`, `serpent`, `service`, `setter`, `seychelles` |
| 1161–1180 | `sến`, `sếp`, `sếu`, `shaker`, `shamrock`, `shearer`, `sheikh`, `sherry`, `shiite`, `shilling`, `shire`, `shōgun`, `shoo`, `siemen`, `sigma`, `sikh`, `silicon`, `silicone`, `sillago`, `silô` |
| 1181–1200 | `sim`, `sin`, `síp`, `sịp`, `skin`, `slam`, `slovakia`, `snare`, `sỏ`, `soa`, `socola`, `sod`, `soda`, `sol`, `solanum`, `solo`, `somalia`, `someone`, `somerset`, `sonar` |
| 1201–1220 | `sonata`, `sòng`, `soóc`, `soong`, `soprano`, `sour`, `sôcôla`, `sởi`, `spa`, `spaghetti`, `spandex`, `spaniel`, `sparta`, `spat`, `spectacle`, `sprint`, `sterling`, `stomp`, `stops`, `sub` |
| 1221–1240 | `suite`, `sulfuric`, `sullivan`, `sụn`, `suôn`, `suông`, `súp`, `sus`, `sushi`, `sụt`, `swami`, `sweatshirt`, `sycamore`, `tab`, `taco`, `tàm`, `tamil`, `tammy`, `tanin`, `tantan` |
| 1241–1260 | `tanzania`, `táp`, `tarot`, `tartan`, `tartrat`, `tasmania`, `tat`, `táy`, `tằm`, `tăn`, `tắn`, `tấc`, `tâng`, `tậu`, `tấy`, `tchad`, `techno`, `teddy`, `telua`, `tennis` |
| 1261–1280 | `tenor`, `tẹo`, `tequila`, `tesla`, `testosterone`, `tề`, `tếch`, `tễnh`, `tệp`, `têu`, `tếu`, `thãi`, `thào`, `thằn`, `thẫm`, `thậm`, `thây`, `their`, `thẹo`, `theta` |
| 1281–1300 | `thềm`, `thết`, `thỉ`, `thiếp`, `thím`, `thín`, `thori`, `thoroughbred`, `thồ`, `thục`, `thụi`, `thụng`, `thuộm`, `thuổng`, `thuở`, `thửa`, `thược`, `tiếu`, `timothy`, `típ` |
| 1301–1320 | `toác`, `toại`, `toát`, `tod`, `toé`, `tonga`, `tonneau`, `toong`, `tortilla`, `tót`, `tote`, `toxin`, `tốp`, `tơn`, `trailer`, `trám`, `trance`, `transistor`, `trập`, `trấu` |
| 1321–1340 | `trầy`, `tre`, `trèo`, `trê`, `trề`, `trệt`, `triền`, `triện`, `trifle`, `trĩnh`, `triple`, `trĩu`, `trombon`, `trộ`, `trồi`, `trỗi`, `trôm`, `trùn`, `trũng`, `truỵ` |
| 1341–1360 | `trướng`, `trượng`, `tuabin`, `tuba`, `tuếch`, `tulip`, `tuốc`, `tuý`, `tuyn`, `tv`, `ua`, `ùa`, `uẩn`, `uây`, `uganda`, `ukulele`, `ulster`, `ùm`, `ùn`, `ủn` |
| 1361–1380 | `unisex`, `uột`, `uran`, `urani`, `urê`, `us`, `út`, `uých`, `uýt`, `uytky`, `uzbekistan`, `ừ`, `ứ`, `ứa`, `ực`, `ươm`, `ướm`, `vạc`, `vãi`, `vại` |
| 1381–1400 | `valentine`, `vàn`, `vảng`, `vanh`, `vanilla`, `vat`, `vát`, `vắc`, `vằm`, `vấp`, `vầy`, `vẩy`, `vấy`, `vecni`, `vén`, `venice`, `vèo`, `vẹo`, `vermouth`, `veronica` |
| 1401–1420 | `vest`, `via`, `vibraphone`, `viceroy`, `viking`, `vịn`, `viola`, `vipe`, `virut`, `vishnu`, `vitriol`, `víu`, `vonfam`, `voodoo`, `vọp`, `vốc`, `vôn`, `vồng`, `vờn`, `vùi` |
| 1421–1440 | `vượn`, `watt`, `weber`, `website`, `wheeler`, `wheeling`, `whiskey`, `wight`, `wilderness`, `won`, `xacxô`, `xài`, `xàm`, `xamurai`, `xắn`, `xắt`, `xẩu`, `xcutơ`, `xenlulo`, `xenon` |
| 1441–1460 | `xerox`, `xẹt`, `xếch`, `xiệc`, `ximôckinh`, `ximôkinh`, `xiom`, `xỉu`, `xki`, `xo`, `xó`, `xoan`, `xoe`, `xoè`, `xốc`, `xớt`, `xtăngxin`, `xteoit`, `xuê`, `xum` |
| 1461–1480 | `xúm`, `xủng`, `xúp`, `xuyến`, `xuyệt`, `xức`, `xửng`, `xyt`, `ỷ`, `yard`, `yay`, `yểng`, `yểu`, `yoga`, `yourself`, `zac`, `zan`, `zắc`, `zeppelin`, `zeta` |
| 1481–1485 | `zêrô`, `zibelin`, `zona`, `zucchini`, `рhù` |

### Xuất hiện 2 lần: 547 loại

| STT trong nhóm | Âm tiết/token |
| --- | --- |
| 1–20 | `aba`, `afghanistan`, `ải`, `aids`, `album`, `ale`, `alpha`, `amazon`, `amoniac`, `anna`, `antô`, `apache`, `argentina`, `argyle`, `ascot`, `át`, `axetat`, `axít`, `ẳng`, `ấy` |
| 21–40 | `baptist`, `bar`, `baroque`, `basque`, `bập`, `bẽ`, `bebop`, `bel`, `bẹn`, `berili`, `berlin`, `bey`, `blog`, `bologna`, `bõm`, `bọn`, `bongo`, `boogie`, `bourbon`, `bourgogne` |
| 41–60 | `bowling`, `bô`, `bở`, `bravo`, `bùi`, `bum`, `bun`, `bủn`, `búng`, `cạc`, `cacao`, `cacbonat`, `calo`, `cambridge`, `caramel`, `cardigan`, `cashmere`, `cayenne`, `cặc`, `celt` |
| 61–80 | `chài`, `chạng`, `chardonnay`, `charleston`, `charlotte`, `chẵn`, `chăng`, `chắp`, `chấu`, `cheddar`, `chếch`, `chích`, `chịch`, `chiếc`, `chình`, `choạng`, `chóc`, `chọi`, `chỏm`, `chồm` |
| 81–100 | `chớm`, `chờn`, `chùa`, `chùi`, `chùn`, `chửa`, `clarion`, `clorua`, `coban`, `coóc`, `cọp`, `corgi`, `côca`, `cớm`, `creole`, `crếp`, `croquet`, `cũi`, `cùm`, `cuốc` |
| 101–120 | `cuồn`, `cừ`, `cữ`, `dãn`, `day`, `dấy`, `de`, `denim`, `dì`, `dĩa`, `diềm`, `diên`, `dìm`, `dỏm`, `dỗi`, `dơi`, `dứa`, `dường`, `dượt`, `đác` |
| 121–140 | `đản`, `đao`, `đát`, `đăm`, `điôxít`, `đui`, `đụn`, `đuốc`, `đượm`, `en`, `ẻo`, `epoxy`, `este`, `eureka`, `ê`, `ế`, `ếch`, `fair`, `fan`, `fathom` |
| 141–160 | `fez`, `florence`, `foot`, `ft`, `gallon`, `galông`, `gamma`, `gạn`, `gáo`, `gảy`, `gáy`, `gâu`, `gi`, `giã`, `giăng`, `giẫm`, `giấm`, `gic`, `giẻ`, `giê` |
| 161–180 | `giò`, `giơ`, `glycol`, `gonđon`, `google`, `gothic`, `gơ`, `green`, `gu`, `guernsey`, `guồng`, `gừng`, `gươm`, `ha`, `hakim`, `hamburger`, `háng`, `hặc`, `hấn`, `hất` |
| 181–200 | `hé`, `héc`, `hem`, `hen`, `henna`, `henry`, `hickory`, `hipster`, `hòm`, `hõm`, `homerun`, `hóng`, `hớt`, `hu`, `hủi`, `hùm`, `huyệt`, `hửng`, `hydrat`, `hyđrôxít` |
| 201–220 | `internet`, `jersey`, `jive`, `kaki`, `keg`, `kèo`, `kệ`, `kềm`, `kg`, `khạc`, `khảm`, `khánh`, `khạo`, `khay`, `khất`, `kheo`, `khêu`, `khiên`, `khịt`, `khoá` |
| 221–240 | `khoắn`, `khoẻ`, `khoeo`, `khuy`, `kiếng`, `kình`, `kiwi`, `kraft`, `lambda`, `lán`, `lạng`, `lanka`, `lào`, `lasagna`, `latin`, `lăm`, `lẩm`, `lầu`, `lẽo`, `leone` |
| 241–260 | `levant`, `limousine`, `lòa`, `loang`, `loáng`, `loát`, `logistics`, `lọi`, `lỏn`, `louisiana`, `lôgic`, `lợm`, `luce`, `lủn`, `lụy`, `lượm`, `mác`, `macro`, `mam`, `manti` |
| 261–280 | `mao`, `mạp`, `marcel`, `marguerite`, `maria`, `mạt`, `maya`, `mẹo`, `methamphetamine`, `metro`, `mề`, `mền`, `mênh`, `mí`, `mích`, `milimét`, `mĩm`, `min`, `miu`, `mobile` |
| 281–300 | `mol`, `mỏm`, `mono`, `monoxit`, `mọt`, `mơn`, `mũm`, `mun`, `muồi`, `muscat`, `mưng`, `mương`, `nách`, `nạm`, `nành`, `napan`, `nãy`, `nặc`, `nấng`, `nấp` |
| 301–320 | `neanderthal`, `neon`, `nệm`, `nện`, `ngả`, `ngáy`, `nghẹn`, `nghếch`, `nghịt`, `ngò`, `ngó`, `ngoạm`, `ngoãn`, `ngoảnh`, `ngoặc`, `ngoắt`, `ngọng`, `ngợm`, `ngùng`, `nguôi` |
| 321–340 | `nguội`, `nhá`, `nhác`, `nhan`, `nheo`, `nhéo`, `nhích`, `nhọt`, `nhôm`, `nhộng`, `nhụa`, `nhuần`, `nhúc`, `nhùi`, `nhũng`, `nịch`, `niệu`, `niken`, `nít`, `nitrat` |
| 341–360 | `nitric`, `nom`, `nòng`, `nọt`, `nôi`, `nộm`, `nờ`, `nơtron`, `ò`, `of`, `ohio`, `on`, `opera`, `ốt`, `pa`, `par`, `pascal`, `patin`, `pepperoni`, `pê` |
| 361–380 | `phấp`, `phập`, `phết`, `phiệt`, `phỉnh`, `pho`, `photocopy`, `phồn`, `phốt`, `phùn`, `phường`, `pi`, `piano`, `pít`, `pita`, `platon`, `play`, `poker`, `propan`, `protein` |
| 381–400 | `psi`, `pueblo`, `punk`, `quăn`, `quăng`, `quí`, `rạ`, `radar`, `radio`, `rái`, `rand`, `ráo`, `rave`, `rẫy`, `rè`, `riff`, `rinh`, `rọ`, `rock`, `ron` |
| 401–420 | `rống`, `rộp`, `rờ`, `rụi`, `rùm`, `rước`, `rưởi`, `rương`, `sạc`, `sải`, `saskatoon`, `savoy`, `săng`, `sấp`, `sập`, `sẩy`, `sậy`, `sec`, `sê`, `sên` |
| 421–440 | `sền`, `sết`, `shiva`, `sierra`, `sình`, `sò`, `sofa`, `som`, `sờn`, `sri`, `stress`, `studio`, `sulfua`, `sumo`, `sunfat`, `suyễn`, `sứa`, `sướt`, `tã`, `tánh` |
| 441–460 | `taxi`, `tè`, `texas`, `thạc`, `thán`, `thắp`, `thêu`, `thía`, `thò`, `thoai`, `thóc`, `thòi`, `thong`, `thóp`, `thổn`, `thốt`, `thúi`, `thuôn`, `thúy`, `tiễn` |
| 461–480 | `tịnh`, `tivi`, `toạ`, `toan`, `tọc`, `tòi`, `tòng`, `topaz`, `torah`, `trác`, `trệch`, `trịch`, `trỏ`, `tróc`, `trọc`, `troy`, `trớ`, `trớn`, `tru`, `truffle` |
| 481–500 | `tủa`, `tụm`, `tuộc`, `túp`, `tụt`, `tuýt`, `tưng`, `tỵ`, `úa`, `uể`, `um`, `uổng`, `uỷ`, `vài`, `vạng`, `vani`, `vắt`, `véc`, `vẹt`, `vế` |
| 501–520 | `vênh`, `vích`, `victoria`, `video`, `vinyl`, `virginia`, `vodka`, `vón`, `vôtca`, `vợi`, `vớt`, `vun`, `vung`, `vựa`, `vừng`, `vựng`, `vươn`, `xăm`, `xập`, `xâu` |
| 521–540 | `xém`, `xẻo`, `xệ`, `xêm`, `xía`, `xịch`, `xiềng`, `xình`, `xỏ`, `xoàng`, `xoảng`, `xóm`, `xong`, `xoóc`, `xối`, `xốt`, `xờ`, `xun`, `xuýt`, `xuỵt` |
| 541–547 | `yểm`, `yết`, `yogi`, `z`, `zaire`, `zic`, `zom` |

</details>

## Phụ lục B. Đầy đủ cờ cấu trúc/dấu trên nguyên bản

Các nhóm dưới đây tách theo **tổ hợp cờ**, nên một token chỉ nằm trong một nhóm. Danh sách này bảo toàn cả cờ giả do ngoại ngữ/ký hiệu. Các ca cần quyết định ngôn ngữ cụ thể đã được nêu riêng ở mục 4; không coi toàn bộ danh sách là lỗi cần thay hàng loạt.

<details>
<summary>1.095 loại token bị gắn cờ; số × là tần suất trên toàn kho</summary>


### cấu trúc: 959 loại

| STT trong nhóm | Token và tần suất trong nguyên bản |
| --- | --- |
| 1–20 | `aah` × 1, `aba` × 2, `abs` × 1, `actin` × 1, `adonis` × 1, `adrenalin` × 1, `affirmed` × 1, `afghanistan` × 2, `ag` × 1, `agon` × 1, `aides` × 1, `aids` × 2, `alabama` × 1, `alaska` × 1, `album` × 2, `ale` × 2, `alen` × 3, `all` × 1, `allegro` × 1, `alpha` × 2 |
| 21–40 | `alps` × 1, `amazon` × 2, `amen` × 1, `amiăng` × 1, `amin` × 1, `amino` × 1, `amoni` × 1, `ampe` × 1, `amyl` × 1, `amyloid` × 1, `anaconda` × 1, `anchorage` × 1, `anglo` × 1, `anna` × 2, `antô` × 2, `apache` × 2, `apollo` × 1, `argentina` × 2, `argyle` × 2, `aria` × 1 |
| 41–60 | `armenia` × 1, `armeria` × 1, `artie` × 1, `asen` × 1, `asperula` × 1, `aspirin` × 1, `ate` × 1, `attica` × 1, `avatar` × 1, `axít` × 2, `ăngten` × 1, `baba` × 1, `babel` × 1, `babu` × 1, `babylon` × 1, `backhand` × 1, `balboa` × 1, `banjô` × 1, `bar` × 2, `barbary` × 1 |
| 61–80 | `barbulata` × 1, `barie` × 1, `baroque` × 2, `basel` × 1, `basilica` × 1, `basque` × 2, `bass` × 4, `bastille` × 1, `beagle` × 1, `bel` × 2, `benzen` × 1, `benzoin` × 1, `berber` × 1, `beri` × 1, `berili` × 2, `berlin` × 2, `berserker` × 1, `beryl` × 1, `bey` × 2, `bêta` × 1 |
| 81–100 | `biker` × 1, `bikini` × 1, `bina` × 1, `bingo` × 1, `birdie` × 1, `bison` × 1, `bitum` × 1, `bizon` × 1, `blazer` × 1, `blog` × 2, `blouse` × 1, `bluegrass` × 3, `blues` × 3, `board` × 1, `bob` × 1, `bobsled` × 1, `boer` × 1, `bogey` × 1, `bohemia` × 1, `bologna` × 2 |
| 101–120 | `bonaparte` × 1, `bongo` × 2, `bonus` × 1, `boogie` × 2, `boomerang` × 3, `boongke` × 1, `boothe` × 1, `bordeaux` × 1, `boulder` × 1, `bourbon` × 2, `bourgogne` × 2, `bowling` × 2, `bowls` × 1, `boxer` × 1, `braille` × 1, `branđi` × 1, `bravo` × 2, `brazil` × 1, `bridge` × 4, `brie` × 1 |
| 121–140 | `brill` × 1, `bugle` × 1, `bulgaria` × 1, `bulldog` × 1, `bungee` × 1, `bunting` × 1, `burgundy` × 1, `burrito` × 1, `burton` × 1, `butte` × 1, `butyl` × 1, `byte` × 1, `byzantine` × 1, `cacao` × 2, `cacbon` × 6, `cacbua` × 1, `cad` × 1, `caddie` × 1, `cadence` × 1, `cađimi` × 1 |
| 141–160 | `cafêin` × 1, `caffein` × 1, `cairn` × 1, `california` × 1, `calo` × 2, `calypso` × 1, `cambridge` × 2, `camera` × 1, `campuchia` × 1, `canada` × 3, `candela` × 1, `candida` × 1, `canvê` × 1, `canxi` × 1, `cappuccino` × 1, `cara` × 1, `caramel` × 2, `caramen` × 1, `caraôkê` × 1, `carbine` × 1 |
| 161–180 | `cardigan` × 2, `carolina` × 1, `carte` × 1, `cascade` × 1, `cashmere` × 2, `castor` × 1, `catmi` × 1, `catwalk` × 1, `caviar` × 1, `cayenne` × 2, `chancery` × 1, `charades` × 1, `chardonnay` × 2, `charleston` × 2, `charlotte` × 2, `cheddar` × 2, `chennai` × 1, `chess` × 1, `chesterfield` × 3, `chihuahua` × 3 |
| 181–200 | `chimera` × 1, `chino` × 1, `chinook` × 3, `chipotle` × 1, `cholesterol` × 1, `cicero` × 1, `cisco` × 1, `cla` × 1, `clare` × 1, `clarion` × 2, `class` × 1, `clementine` × 1, `clo` × 1, `clocks` × 1, `clorua` × 2, `coban` × 2, `coca` × 1, `cocktail` × 1, `cola` × 1, `collagen` × 1 |
| 201–220 | `collie` × 1, `collins` × 1, `colorado` × 4, `concord` × 1, `condor` × 1, `contextual` × 1, `copy` × 1, `corgi` × 2, `cortisol` × 1, `corvus` × 1, `cos` × 1, `cosin` × 1, `coupé` × 1, `cox` × 1, `côca` × 2, `côngtenơ` × 1, `côngxoocxiom` × 1, `cracker` × 1, `creeps` × 1, `creole` × 2 |
| 221–240 | `crescendo` × 1, `crếp` × 2, `crích` × 1, `crom` × 3, `crown` × 1, `crô` × 1, `crôm` × 1, `cupcake` × 1, `cupid` × 1, `curb` × 1, `curie` × 1, `cyclooxygenase` × 1, `dada` × 1, `dahl` × 1, `daman` × 1, `darling` × 1, `decagam` × 1, `delaware` × 1, `deli` × 1, `delicious` × 1 |
| 241–260 | `denim` × 2, `deuce` × 1, `devices` × 1, `diesel` × 1, `digan` × 1, `dingue` × 1, `disco` × 1, `diva` × 1, `dna` × 3, `dodo` × 1, `domino` × 3, `dona` × 1, `donna` × 1, `dopamine` × 1, `dorado` × 1, `dorsi` × 1, `dory` × 1, `dos` × 1, `dulcamara` × 1, `điẻu` × 1 |
| 261–280 | `điôxít` × 2, `đram` × 3, `đrô` × 1, `eczema` × 1, `edwardian` × 1, `egg` × 1, `einsteini` × 1, `electron` × 1, `elves` × 1, `emu` × 1, `entropy` × 3, `enzim` × 1, `enzym` × 3, `episcopal` × 1, `epoxy` × 2, `epsilon` × 1, `eri` × 1, `espresso` × 1, `este` × 2, `estonia` × 1 |
| 281–300 | `estrogen` × 1, `etyl` × 1, `etylen` × 1, `eureka` × 2, `euro` × 1, `everglades` × 1, `exchange` × 1, `eyre` × 1, `êmia` × 1, `fair` × 2, `fan` × 2, `fathom` × 2, `fawkes` × 1, `fax` × 4, `fedora` × 1, `fez` × 2, `fif` × 1, `filler` × 1, `flanen` × 1, `florence` × 2 |
| 301–320 | `florida` × 1, `florua` × 1, `fomanđêhít` × 1, `fractal` × 1, `frăng` × 1, `freelance` × 1, `freelancer` × 1, `fresco` × 1, `frigate` × 1, `frông` × 1, `fructoza` × 1, `fudge` × 1, `funk` × 1, `g` × 1, `gal` × 1, `galê` × 1, `gallon` × 2, `galông` × 2, `gamma` × 2, `gangster` × 1 |
| 321–340 | `gar` × 1, `gelatin` × 1, `genoa` × 1, `german` × 3, `gestapo` × 1, `geum` × 1, `ghêpa` × 1, `gíc` × 1, `giêsu` × 3, `gipsi` × 1, `glu` × 1, `glucozơ` × 1, `gluten` × 1, `glycol` × 2, `golf` × 16, `gonđon` × 2, `google` × 2, `gopher` × 1, `goth` × 3, `grad` × 1 |
| 341–360 | `gradien` × 1, `graduale` × 1, `graffiti` × 1, `granola` × 1, `green` × 2, `greyhound` × 1, `groves` × 1, `guacamole` × 1, `guernsey` × 2, `guinea` × 1, `guinée` × 1, `gulag` × 1, `gulliver` × 1, `gulo` × 1, `guru` × 1, `gym` × 1, `hacker` × 1, `hackney` × 1, `haiku` × 1, `hajj` × 1 |
| 361–380 | `hakim` × 2, `hamburger` × 2, `hampshire` × 1, `harlequin` × 1, `hatchback` × 1, `hawaii` × 1, `hays` × 1, `hebrew` × 1, `hebrides` × 1, `heli` × 1, `heller` × 1, `hemoglobin` × 1, `henna` × 2, `henri` × 1, `henry` × 2, `herpes` × 1, `hertz` × 1, `hex` × 1, `hêli` × 1, `hickory` × 2 |
| 381–400 | `hiđrocacbon` × 1, `hiđrô` × 1, `highlighter` × 1, `hind` × 1, `hindi` × 1, `hippie` × 4, `hipster` × 2, `hogan` × 1, `homer` × 1, `homerun` × 2, `hook` × 1, `hormone` × 4, `hula` × 1, `hummus` × 1, `hungary` × 1, `hydrocacbon` × 1, `hyđrô` × 1, `hyđrôxít` × 2, `ibuprofen` × 1, `ictêri` × 1 |
| 401–420 | `ii` × 1, `iii` × 1, `illinois` × 1, `imam` × 1, `indonesia` × 1, `inner` × 1, `insơ` × 1, `insulin` × 1, `iođ` × 1, `ion` × 4, `ionia` × 1, `iốt` × 1, `ireland` × 7, `irving` × 1, `israel` × 1, `ittêri` × 1, `jalapeno` × 1, `jasper` × 1, `java` × 1, `jazz` × 7 |
| 421–440 | `jean` × 1, `jeans` × 3, `jersey` × 2, `jig` × 1, `jihadi` × 1, `jive` × 2, `jukebox` × 1, `jung` × 1, `kaki` × 2, `kali` × 3, `kangaroo` × 1, `kansas` × 1, `kappa` × 1, `karate` × 1, `kayak` × 3, `kebab` × 1, `keg` × 2, `kentucky` × 1, `kenvin` × 1, `kêrôsin` × 1 |
| 441–460 | `kg` × 2, `khaki` × 1, `khyếm` × 1, `khz` × 1, `kilôgam` × 1, `kimono` × 1, `kinaza` × 1, `kinky` × 1, `kiwi` × 2, `km` × 1, `koala` × 1, `kos` × 1, `kosher` × 1, `kremli` × 1, `kremlin` × 1, `kris` × 1, `kyrgyzstan` × 1, `l` × 1, `lacrosse` × 1, `lactoza` × 1 |
| 461–480 | `lager` × 1, `lambda` × 2, `lanka` × 2, `lantan` × 1, `largo` × 1, `lasagna` × 2, `latex` × 1, `latin` × 2, `latissimus` × 1, `latte` × 1, `lb` × 3, `league` × 1, `leave` × 1, `led` × 1, `leone` × 2, `lev` × 1, `libido` × 1, `lied` × 1, `limerick` × 1, `limousine` × 2 |
| 481–500 | `limô` × 1, `lindy` × 1, `ling` × 1, `links` × 1, `linsơ` × 1, `lipid` × 1, `lira` × 3, `lister` × 1, `lithi` × 1, `liti` × 1, `locus` × 1, `logan` × 1, `logistics` × 2, `louisiana` × 2, `lôgô` × 1, `lsd` × 1, `luce` × 2, `lucifer` × 1, `lug` × 1, `lumen` × 1 |
| 501–520 | `lupus` × 1, `lux` × 1, `lympho` × 1, `macarôni` × 1, `macca` × 1, `mace` × 1, `macma` × 1, `macro` × 2, `mademoiselle` × 1, `madras` × 3, `magie` × 1, `magiê` × 1, `magnum` × 1, `mahatma` × 1, `make` × 1, `mako` × 1, `malta` × 1, `manga` × 1, `mangan` × 1, `manhattan` × 1 |
| 521–540 | `manila` × 1, `manocanh` × 1, `manti` × 2, `mantle` × 1, `marcel` × 2, `margarin` × 1, `margarita` × 1, `marguerite` × 2, `maria` × 2, `marijuana` × 1, `marketing` × 1, `mars` × 1, `marshals` × 1, `marshmallow` × 1, `martini` × 1, `masters` × 1, `matte` × 1, `maxi` × 1, `maxwell` × 1, `maya` × 2 |
| 541–560 | `mayday` × 1, `mayonnaise` × 1, `mdma` × 1, `mecca` × 1, `medicago` × 1, `medusa` × 1, `melatonin` × 1, `meme` × 1, `merino` × 1, `merlin` × 1, `methadone` × 1, `methamphetamine` × 2, `metro` × 2, `metyl` × 1, `mexico` × 3, `miăng` × 1, `mica` × 1, `mickey` × 1, `micrô` × 3, `micrômét` × 1 |
| 561–580 | `mil` × 3, `miligam` × 1, `milimét` × 2, `mills` × 1, `milo` × 1, `mini` × 1, `minivan` × 1, `minnesota` × 1, `minor` × 1, `mobile` × 2, `mocfin` × 1, `mocha` × 3, `modem` × 1, `mol` × 2, `molly` × 1, `molypden` × 1, `monedula` × 1, `mono` × 2, `montana` × 1, `monte` × 1 |
| 581–600 | `moor` × 1, `moose` × 1, `moray` × 1, `mormon` × 1, `moron` × 1, `morse` × 3, `mousse` × 3, `mozzarella` × 1, `môgôn` × 1, `mônôgram` × 1, `muffin` × 1, `mull` × 1, `muller` × 3, `mulligan` × 1, `mustang` × 1, `mustelid` × 1, `myrtle` × 1, `myrtus` × 1, `n` × 1, `nacho` × 1 |
| 601–620 | `nancy` × 1, `nano` × 1, `napan` × 2, `napoleon` × 3, `napoléon` × 1, `nato` × 1, `natri` × 1, `navajo` × 1, `neanderthal` × 2, `nelson` × 1, `neon` × 2, `nepal` × 1, `neutrino` × 1, `nevada` × 1, `new` × 1, `níc` × 1, `nicotin` × 1, `nicôtin` × 1, `nikel` × 1, `niken` × 2 |
| 621–640 | `ninja` × 1, `ninkhursag` × 1, `nitơ` × 4, `noodle` × 1, `nơtron` × 2, `nucleotide` × 1, `octan` × 1, `odyssey` × 1, `of` × 2, `oh` × 1, `ohio` × 2, `omega` × 1, `ooh` × 1, `opan` × 1, `opera` × 2, `or` × 1, `organ` × 3, `origami` × 1, `osimi` × 1, `osmerus` × 1 |
| 641–660 | `ottoman` × 3, `ounce` × 1, `overdrive` × 1, `own` × 1, `oxford` × 3, `oxy` × 4, `ozon` × 1, `ôông` × 1, `ôxy` × 3, `paisley` × 1, `palađi` × 1, `panama` × 3, `panen` × 1, `paprika` × 1, `par` × 2, `para` × 1, `paris` × 1, `partridge` × 1, `pascal` × 2, `pasha` × 1 |
| 661–680 | `pastel` × 1, `patê` × 1, `patin` × 2, `penicillin` × 1, `penny` × 1, `penthouse` × 1, `pepperoni` × 2, `peptide` × 1, `peso` × 1, `phalanx` × 1, `philippines` × 1, `phoebe` × 1, `photocopy` × 2, `photpho` × 1, `phốtpho` × 1, `phrăng` × 1, `piano` × 2, `píc` × 1, `piccolo` × 1, `pinball` × 1 |
| 681–700 | `ping` × 3, `pinto` × 1, `pita` × 2, `pizza` × 3, `platin` × 1, `platon` × 2, `play` × 2, `plutoni` × 1, `poaz` × 1, `poker` × 2, `polka` × 3, `polo` × 1, `polyester` × 3, `polyetylen` × 1, `polymerase` × 1, `pound` × 3, `pôke` × 1, `pôni` × 1, `pretzel` × 1, `progesterone` × 1 |
| 701–720 | `propan` × 2, `protein` × 2, `proton` × 1, `prô` × 1, `psi` × 2, `pudding` × 3, `pueblo` × 2, `pug` × 1, `punk` × 2, `purê` × 1, `pyxidanthera` × 1, `rad` × 1, `radar` × 2, `radian` × 1, `radio` × 2, `rađơn` × 1, `ragu` × 1, `rainier` × 1, `rand` × 2, `rapper` × 1 |
| 721–740 | `rapsody` × 1, `rave` × 2, `ravioli` × 1, `rayon` × 1, `reel` × 1, `reggae` × 1, `remote` × 1, `reni` × 1, `requiem` × 1, `retriever` × 1, `retro` × 1, `rhea` × 3, `riff` × 2, `risotto` × 1, `riviera` × 1, `rna` × 1, `roche` × 1, `rock` × 2, `rocker` × 1, `rodeo` × 1 |
| 741–760 | `romaine` × 1, `router` × 1, `roux` × 1, `rôman` × 1, `rôto` × 1, `rudd` × 1, `rune` × 1, `rupi` × 3, `salmonella` × 1, `salsa` × 1, `samba` × 3, `samurai` × 1, `saphia` × 1, `sari` × 1, `sarracenia` × 1, `saskatchewan` × 1, `saskatoon` × 2, `satan` × 1, `savoury` × 1, `savoy` × 2 |
| 761–780 | `sax` × 1, `saxon` × 1, `saxophone` × 1, `schooner` × 1, `scotland` × 20, `scots` × 1, `scrabble` × 1, `sedan` × 1, `see` × 3, `seine` × 1, `selen` × 1, `senna` × 1, `sequin` × 1, `serenade` × 1, `serotonin` × 1, `service` × 1, `servo` × 3, `setter` × 1, `seychelles` × 1, `shaker` × 1 |
| 781–800 | `shamrock` × 1, `shaw` × 3, `shearer` × 1, `sheikh` × 1, `sherry` × 1, `shiite` × 1, `shilling` × 1, `shire` × 1, `shiva` × 2, `shōgun` × 1, `shoo` × 1, `siemen` × 1, `sierra` × 2, `sigma` × 1, `sikh` × 1, `silicon` × 1, `silicone` × 1, `sillago` × 1, `silô` × 1, `skin` × 1 |
| 801–820 | `slam` × 1, `slovakia` × 1, `snare` × 1, `socola` × 1, `sod` × 1, `soda` × 1, `sofa` × 2, `sol` × 1, `solanum` × 1, `solo` × 1, `soma` × 3, `somalia` × 1, `someone` × 1, `sonar` × 1, `sonata` × 1, `soprano` × 1, `sour` × 1, `sôcôla` × 1, `spa` × 1, `spaghetti` × 1 |
| 821–840 | `spandex` × 1, `spaniel` × 1, `sparta` × 1, `spectacle` × 1, `sri` × 2, `sterling` × 1, `stops` × 1, `stress` × 2, `studio` × 2, `sub` × 1, `suite` × 1, `sulfua` × 2, `sullivan` × 1, `sumo` × 2, `sus` × 1, `sushi` × 1, `swami` × 1, `sycamore` × 1, `tab` × 1, `taco` × 1 |
| 841–860 | `tamil` × 1, `tammy` × 1, `tango` × 3, `tanin` × 1, `tantan` × 1, `tanzania` × 1, `tartan` × 1, `tasmania` × 1, `taxi` × 2, `tchad` × 1, `techno` × 1, `teddy` × 1, `teen` × 4, `telua` × 1, `tennis` × 1, `tenor` × 1, `tequila` × 1, `tesla` × 1, `testosterone` × 1, `texas` × 2 |
| 861–880 | `their` × 1, `theta` × 1, `thori` × 1, `thoroughbred` × 1, `timothy` × 1, `titan` × 3, `tivi` × 2, `tod` × 1, `tonga` × 1, `tonneau` × 1, `topaz` × 2, `torah` × 2, `tortilla` × 1, `tote` × 1, `toxin` × 1, `trailer` × 1, `trance` × 1, `transistor` × 1, `trifle` × 1, `triple` × 1 |
| 881–900 | `trombon` × 1, `troy` × 2, `truffle` × 2, `tuabin` × 1, `tuba` × 1, `tv` × 1, `uganda` × 1, `ukulele` × 1, `ulster` × 1, `unisex` × 1, `uran` × 1, `urani` × 1, `urê` × 1, `us` × 1, `uytky` × 1, `uzbekistan` × 1, `v` × 6, `valentine` × 1, `vani` × 2, `vanilla` × 1 |
| 901–920 | `vecni` × 1, `venice` × 1, `vermouth` × 1, `veronica` × 1, `vibraphone` × 1, `viceroy` × 1, `victoria` × 2, `video` × 2, `viking` × 1, `vinyl` × 2, `viola` × 1, `vipe` × 1, `virginia` × 2, `vishnu` × 1, `vitriol` × 1, `vodka` × 2, `vonfam` × 1, `voodoo` × 1, `vôtca` × 2, `wales` × 4 |
| 921–940 | `web` × 5, `weber` × 1, `website` × 1, `wheeler` × 1, `wheeling` × 1, `whiskey` × 1, `whiting` × 3, `wilderness` × 1, `won` × 1, `x` × 5, `xacxô` × 1, `xamurai` × 1, `xcutơ` × 1, `xenlulo` × 1, `xenon` × 1, `xerox` × 1, `ximôckinh` × 1, `ximôkinh` × 1, `xiom` × 1, `xki` × 1 |
| 941–959 | `xtăngxin` × 1, `xyanua` × 3, `yard` × 1, `yay` × 1, `yoga` × 1, `yogi` × 2, `yourself` × 1, `z` × 2, `zaire` × 2, `zan` × 1, `zắc` × 1, `zeppelin` × 1, `zeta` × 1, `zêrô` × 1, `zibelin` × 1, `zom` × 2, `zona` × 1, `zucchini` × 1, `рhù` × 1 |

### cấu trúc; thanh ở vần tắc: 114 loại

| STT trong nhóm | Token và tần suất trong nguyên bản |
| --- | --- |
| 1–20 | `abc` × 1, `acrylic` × 3, `altruistic` × 1, `amoniac` × 2, `anxet` × 1, `ascot` × 2, `axetat` × 2, `axetic` × 1, `axit` × 8, `baptist` × 2, `beat` × 1, `bebop` × 2, `bigfoot` × 1, `bitmut` × 1, `brant` × 1, `brent` × 1, `buffet` × 1, `cabernet` × 1, `cacbonat` × 2, `cacbonic` × 1 |
| 21–40 | `carnot` × 1, `celt` × 2, `ch` × 1, `chelat` × 1, `clarinet` × 1, `cntt` × 1, `colt` × 1, `compost` × 1, `corset` × 1, `cricket` × 6, `croquet` × 2, `ddt` × 1, `donut` × 1, `duvet` × 1, `đinamit` × 1, `elip` × 1, `ethylic` × 1, `feet` × 1, `ferret` × 1, `foot` × 2 |
| 41–60 | `ft` × 2, `gambit` × 1, `gic` × 2, `gilbert` × 3, `glutamat` × 1, `gothic` × 2, `hobbit` × 1, `holographic` × 1, `hydrat` × 2, `hyđat` × 1, `hypebolic` × 1, `inch` × 1, `internet` × 2, `ionic` × 1, `iot` × 1, `jeep` × 1, `jumpsuit` × 1, `kat` × 1, `kilt` × 1, `kraft` × 2 |
| 61–80 | `lambert` × 1, `levant` × 2, `logic` × 8, `lôgic` × 2, `mactet` × 1, `maroc` × 1, `matit` × 1, `mêtric` × 1, `monoxit` × 2, `mosaic` × 1, `muscat` × 2, `namviet` × 1, `nitrat` × 2, `nitric` × 2, `nitrit` × 1, `nt` × 1, `nucleic` × 1, `oxit` × 1, `oxyt` × 1, `ôxit` × 1 |
| 81–100 | `peptit` × 1, `peroxit` × 3, `phoric` × 1, `piedmont` × 1, `pint` × 3, `plat` × 1, `podcast` × 1, `punt` × 1, `quart` × 3, `resort` × 1, `right` × 1, `scat` × 1, `script` × 1, `sent` × 1, `serpent` × 1, `silic` × 3, `somerset` × 1, `sonnet` × 3, `spat` × 1, `sprint` × 1 |
| 101–114 | `stomp` × 1, `sulfuric` × 1, `sunfat` × 2, `sweatshirt` × 1, `tarot` × 1, `tartrat` × 1, `tulip` × 1, `vest` × 1, `virut` × 1, `watt` × 1, `wight` × 1, `xteoit` × 1, `zac` × 1, `zic` × 2 |

### thanh ở vần tắc: 20 loại

| STT trong nhóm | Token và tần suất trong nguyên bản |
| --- | --- |
| 1–20 | `bach` × 1, `bet` × 1, `bit` × 1, `bop` × 1, `but` × 3, `dot` × 1, `giec` × 1, `let` × 1, `lip` × 1, `mac` × 1, `oat` × 1, `oc` × 1, `quyểt` × 1, `rap` × 1, `rep` × 1, `sac` × 1, `sec` × 2, `tat` × 1, `vat` × 1, `xyt` × 1 |

### vị trí dấu: 1 loại

| STT trong nhóm | Token và tần suất trong nguyên bản |
| --- | --- |
| 1–1 | `gỉa` × 1 |

### cấu trúc; nhiều dấu thanh; thanh ở vần tắc: 1 loại

| STT trong nhóm | Token và tần suất trong nguyên bản |
| --- | --- |
| 1–1 | `đềcalít` × 1 |

</details>

## Phụ lục C. Lệnh quét để tái lập

Lệnh chỉ đọc dữ liệu nguyên bản ở mốc Git cố định, không ghi file. Chạy từ repo cha. In thống kê, các cụm hỏi/ngã, toàn bộ từ hiếm và toàn bộ cờ cấu trúc; không tải từ điển hoặc mở trình duyệt.

<details>
<summary>Mã Node dùng cho bộ quét</summary>

```bash
node --input-type=module <<'NODE'
import fs from 'node:fs';
import {execFileSync} from 'node:child_process';
const revision = '2b6f4b65a82c2908d14bd536b2eff6e0377e25cb'; // mốc trước khi sửa
const entries = Array.from({length:100}, (_, i) => {
 const file = String(i + 1).padStart(3, '0') + '.json';
 return JSON.parse(execFileSync('git', ['show', revision + ':shared/vocabulary/levels/' + file], {encoding:'utf8'})).entries;
}).flat();
const frequency = {}, contexts = {};
let tokenTotal = 0;
for (const e of entries) for (const w of e.vi.normalize('NFC').toLowerCase().match(/\p{L}[\p{L}\p{M}]*/gu) || []) {
 frequency[w] = (frequency[w] || 0) + 1;
 (contexts[w] ??= []).push(e.id);
 tokenTotal++;
}
const tones = /[\u0300\u0301\u0303\u0309\u0323]/gu;
const vowels = 'aăâeêioôơuưy';
const rimes = "a ac ach ai am an ang anh ao ap at au ay ă ăc ăm ăn ăng ăp ăt â âc âm ân âng âp ât âu ây e ec em en eng eo ep et ê êch êm ên ênh êp êt êu i ia ich iêc iêm iên iêng iêp iêt iêu im in inh ip it iu o oa oac oach oai oam oan oang oanh oao oap oat oay oăc oăm oăn oăng oăp oăt oc oe oen oeo oet oi om on ong ooc oong op ot ô ôc ôi ôm ôn ông ôp ôt ơ ơi ơm ơn ơp ơt u ua uân uâng uât uây uc uê uêch uên uênh uêt ui um un ung uôc uôi uôm uôn uông uôp uôt up ut uy uya uych uyên uyêt uyn uynh uyp uyt uyu ư ưa ưc ưi ưm ưn ưng ưu ươc ươi ươm ươn ương ươp ươt ươu ưt y yêm yên yêng yêt yêp yêu yt yp yn ych uơ";
function inspect(word){
 const stripped=word.normalize('NFD').replace(tones,'').normalize('NFC');
 const letters=Array.from(word);let marks=[];
 letters.forEach((l,i)=>{const t=l.normalize('NFD').match(tones)||[];t.forEach(m=>marks.push({i,t:m}));});
 const forms=['ngh','ch','gh','gi','kh','ng','nh','ph','qu','th','tr','b','c','d','đ','g','h','k','l','m','n','p','r','s','t','v','x',''].filter(o=>stripped.startsWith(o)&&new Set(rimes.split(' ')).has(stripped.slice(o.length)) && (!/^yê/.test(stripped.slice(o.length)) || o==='' || o==='qu') && (o!=='k' || /^[ieêy]/.test(stripped.slice(o.length))) && (o!=='c' || !/^[ieêy]/.test(stripped.slice(o.length))) && (!['gh','ngh'].includes(o) || /^[ieê]/.test(stripped.slice(o.length))) && (o!=='ng' || !/^[ieê]/.test(stripped.slice(o.length))) && (o!=='g' || !/^i[aouyăâôơư]/.test(stripped.slice(o.length))));
 const flags=[];
 if(!forms.length)flags.push('cấu trúc');
 if(marks.length>1)flags.push('nhiều dấu thanh');
 if(marks.some(m=>!vowels.includes(stripped[m.i]||'')))flags.push('dấu trên phụ âm');
 if(/[ct p]$/.test(stripped)||stripped.endsWith('ch')){if(!marks.length||marks.some(m=>!['\u0301','\u0323'].includes(m.t)))flags.push('thanh ở vần tắc');}
 if(forms.length&&marks.length===1){
 const positions=new Set();
 for(const onset of forms){let nucleus=stripped.slice(onset.length).replace(/(ch|nh|ng|[cmnpt])$/,''); const inds=Array.from(nucleus).map((c,i)=>vowels.includes(c)?i:-1).filter(i=>i>=0);
 let index;
 if(nucleus.includes('ê'))index=nucleus.indexOf('ê');
 else if(nucleus.includes('ơ'))index=nucleus.indexOf('ơ');
 else if(inds.length>=3)index=inds[1];
 else if(inds.length===2)index=nucleus.length===stripped.length-onset.length?inds[0]:inds[1];
 else index=inds[0];
 if(index!==undefined)positions.add(onset.length+index);
 if(['oa','oe','uy'].includes(nucleus)&&nucleus.length===stripped.length-onset.length)for(const i of inds)positions.add(onset.length+i);
 }
 if(!positions.has(marks[0].i))flags.push('vị trí dấu');
 }
 return {stripped,flags};
}
const invalid = Object.keys(frequency).map(w => ({w, n:frequency[w], ...inspect(w)})).filter(r => r.flags.length);
const rare = Object.keys(frequency).filter(w => frequency[w] <= 2).sort((a,b) => a.localeCompare(b,'vi'));
const index = new Map();
for (const e of entries) for (const part of e.vi.split(';')) {
 const words = part.normalize('NFC').toLowerCase().match(/\p{L}[\p{L}\p{M}]*/gu) || [];
 for (let n = 1; n <= 5; n++) for (let i = 0; i + n <= words.length; i++) {
  const key = words.slice(i, i+n).join(' ');
  const ids = index.get(key) || new Set(); ids.add(e.id); index.set(key, ids);
 }
}
const phrases = ["buồn bã","nghỉ ngơi","suy nghĩ","sửa chữa","sữa bò","sữa mẹ","dạy dỗ","dỗ dành","đổ vỡ","đổ bộ","vỡ nợ","vỡ vụn","rạn vỡ","nỗi buồn","nỗi đau","đau khổ","sợ hãi","sợ sệt","sẵn sàng","sẵn có","hỗ trợ","hỗn hợp","hỗn loạn","kỹ thuật","kỹ năng","kỷ luật","kỷ niệm","lý lẽ","có lẽ","lễ hội","lễ phép","lễ nghi","mạnh mẽ","lặng lẽ","rõ ràng","rực rỡ","rạng rỡ","đẹp đẽ","sạch sẽ","vui vẻ","vẻ đẹp","vẽ tranh","vẽ vời","bản vẽ","bản đồ","sửa đổi","sửa sang","sửa sai","sửa soạn","sữa chua","sữa tươi","nghĩ ngợi","ngẫm nghĩ","nghĩ suy","nghỉ phép","nghỉ hưu","nghỉ học","nghỉ dưỡng","nhà nghỉ","nghỉ lễ","nghỉ việc","nhiễm trùng","nhiễm khuẩn","lây nhiễm","ô nhiễm","truyền nhiễm","miễn dịch","bãi biển","bãi bỏ","bãi đậu","tranh cãi","cãi nhau","gỗ thông","đồ gỗ","cỗ xe","cỗ máy","cỗ bàn","chỗ ngồi","chỗ ở","chỗ trống","chỗ đứng","cửa sổ","cửa hàng","mở cửa","cởi mở","mở rộng","rộng rãi","thoải mái","người mẫu","mẫu vật","mẫu mã","mẫu số","hình mẫu","số lẻ","riêng lẻ","lẻ tẻ","lỡ làng","lỡ hẹn","lầm lỡ","lẫn lộn","pha lẫn","nhầm lẫn","hối hả","vội vã","ngã ba","ngã tư","té ngã","ngã xuống","ngả nghiêng","lãnh đạo","lãnh thổ","lãnh sự","nhẫn nại","kiên nhẫn","nhẫn tâm","tàn nhẫn","bền bỉ","bĩu môi","cười mỉm","mũm mĩm","phẫn nộ","phẫn uất","giận dữ","hung dữ","dữ liệu","dữ dội","giữ gìn","giữ lại","nghĩa vụ","ý nghĩa","định nghĩa","nghĩa là","ngữ nghĩa","nghĩa trang","chính nghĩa","quả quyết","quyết định","lễ lạt","gỗ sồi","mã số","mã hóa","mật mã","từ ngữ","ngôn ngữ","ngữ pháp","ngữ cảnh","bổ sung","bổ ích","bỗng nhiên","ngẫu nhiên","dũng cảm","can đảm","vững chắc","vững vàng","vững bền","nửa đêm","một nửa","nửa vời","nửa chừng","nữa rồi","nữa đâu","lần nữa","hơn nữa","mãi mãi","mải mê","mải miết","giả vờ","giả dối","giả tạo","giả định","giả thiết","giả thuyết","giả mạo","giả danh","giã từ","giã biệt","tác giả","độc giả","diễn giả","giả tưởng","giả trang","thính giả","khán giả","lỗ hổng","lỗ thủng","lỗ mãng","lỗ vốn","lỗ tai","lổn nhổn","khổng lồ","khuôn khổ","khung cảnh","hoàn cảnh","sĩ quan","sĩ diện","nghệ sĩ","bác sĩ","thi sĩ","võ sĩ","tu sĩ","chiến sĩ","liêm sỉ","sỉ nhục","sỉ vả","sỉ lẻ","nỗ lực","nổ tung","nổi tiếng","trôi nổi","nổi bật","bão tố","cơn bão","bảo vệ","bảo hiểm","bảo đảm","đảm bảo","dễ dàng","dễ chịu","dễ dãi","đáng lẽ","đãi ngộ","đãi tiệc","đãi khách","ngược đãi","đãi bôi","đãi cát","thừa thãi","dồi dào","rảnh rỗi","rỗi rãi","lỗi lầm","tội lỗi","cũ kỹ","cũ kĩ","cũ rích","nghèo khổ","khổ sở","khốn khổ","đau đớn","đẫm máu","ướt đẫm","khe khẽ","nhỏ nhẹ","nhõng nhẽo","rên rỉ","rỉ tai","rỉ sét","hoen gỉ","han gỉ","rơi vãi","vung vãi","vãi ra","vải vóc","lãng phí","lãng mạn","lãng quên","vãng lai","vãng cảnh","dã man","dã thú","hoang dã","dã ngoại","giãy giụa","giãy nảy","vẫy tay","vẫy vùng","xoay xở","giỡn chơi","đùa giỡn","gãy gập","gãy đổ","gãy xương","đổ lỗi","đỗ xe","đỗ đạt","đổ mồ hôi","đổ xuống","rác rưởi","bẩn thỉu","nhảm nhí","nham nhở","vất vả","vật vã","tả tơi","tã lót","tả thực","miêu tả","mô tả","diễn tả","chễm chệ","chểnh mảng","nghễnh ngãng","ủ rũ","rũ rượi","ủ ê","ngửi thấy","ngửi mùi","chữ cái","chữ viết","tập thể","cụ thể","lịch sử","sử dụng","xử lý","xử lí","xử sự","cư xử","tiểu sử","lịch lãm","hiểu biết","hiểu rõ","kiểm tra","kiểm soát","bãi cỏ","cỏ dại","đồng cỏ","cái giỏ","giỏ hàng","dở dang","dở hơi","bỏ dở","chở hàng","chuyên chở","ở đâu","bỡ ngỡ","ngỡ ngàng","bỡn cợt","hờn dỗi","giận dỗi","nhăn nhở","nhăn nhó","bãi rác","vỗ tay","vỗ về","vỏ cây","vỏ sò","vỏ bọc","võ thuật","võ đài","bảnh bao","khỏe mạnh","khỏe khoắn","khoẻ mạnh","nãy giờ","nảy sinh","nảy mầm","xảy ra","xảy đến","chữa lành","chữa bệnh","chữa trị","chửa đẻ","tử tế","tỉ mỉ","khoan đã","dĩ nhiên","sĩ số","sĩ tử","khinh bỉ","lăng nhục","hoan hỉ","hoan hỷ","an ủi","giũ bụi","cởi trói","gỡ bỏ","trở ngại","trở về","lở loét","hỗn xược","nũng nịu","đẫy đà","đãi đằng","dịch giả","chủ nghĩa","nhân văn chủ nghĩa","lễ rửa tội","rửa tội","dễ giận","nhiễm sắc thể","bảo mẫu","một muỗng","ỉ eo","người bán hàng rong","phán quyết","điểu","bồ hóng","ngấm ngầm","nhà ở"];
const pairFlags = [];
for (const p of phrases) {
 let candidates = [''];
 for (const c of p) {
  const n = c.normalize('NFD');
  const alt = /[\u0309\u0303]/u.test(n) ? n.replace(/[\u0309\u0303]/u, t => t === '\u0309' ? '\u0303' : '\u0309').normalize('NFC') : null;
  candidates = candidates.flatMap(s => alt ? [s+c,s+alt] : [s+c]);
 }
 for (const wrong of candidates.filter(s => s !== p)) for (const id of index.get(wrong) || []) pairFlags.push({id,wrong,correct:p});
}
const parts = e => e.vi.split(';').map(s => s.trim());
const exactDuplicates = entries.filter(e => new Set(parts(e)).size < parts(e).length);
const compound = entries.filter(e => {
 const p = parts(e).map(s => s.toLowerCase());
 return p.some(s => s.includes(' ') && s.split(/\s+/).every(w => p.includes(w)));
});
const contained = entries.filter(e => {
 const p = parts(e).map(s => s.toLowerCase());
 return p.some(s => p.some(t => s !== t && (' '+t+' ').includes(' '+s+' ')));
});
function spellingKey(s) {
 return s.toLowerCase().split(/\s+/).map(w => {
  const n = w.normalize('NFD');
  return n.replace(tones,'').normalize('NFC') + ':' + (n.match(tones) || []).sort().join('');
 }).join(' ');
}
const variants = entries.filter(e => {
 const p = parts(e).map(spellingKey); return new Set(p).size < p.length;
});
const forWords = words => new Set(words.flatMap(w => contexts[w]));
const union = new Set([...forWords(rare), ...forWords(invalid.map(r => r.w)), ...pairFlags.map(r => r.id), ...variants.map(e => e.id), ...compound.map(e => e.id)]);
console.log(JSON.stringify({entries:entries.length,tokenTotal,uniqueTokens:Object.keys(frequency).length,rareTypes:rare.length,rareOccurrences:rare.reduce((n,w)=>n+frequency[w],0),grammarTypes:invalid.length,grammarOccurrences:invalid.reduce((n,r)=>n+r.n,0),pairMatches:pairFlags.length,pairEntries:new Set(pairFlags.map(r=>r.id)).size,compound:compound.length,contained:contained.length,exactDuplicates:exactDuplicates.length,variants:variants.length,machineEntryUnion:union.size}, null, 2));
console.log('CẶP HỎI/NGÃ:', JSON.stringify(pairFlags));
console.log('ÂM TIẾT HIẾM:', rare.map(w=>w+':'+frequency[w]).join(', '));
console.log('CỜ CẤU TRÚC:', JSON.stringify(invalid));
NODE
```

</details>


## 6. Claude duyệt (27/10)

Đọc cả 38 dòng đổi: đều đúng. Có một chỗ chưa nhất quán: với cặp hai cách đặt dấu ("hòa/hoà", "thủy/thuỷ"), Codex giữ cách viết đứng trước, nên có mục giữ kiểu mới, có mục giữ kiểu cũ. Không đổi gì vì cả kho đang trộn hai kiểu ("hóa" 258 lần, "hoá" 167 lần; "hòa" 96 lần, "hoà" 217 lần). Muốn thống nhất cả kho thì làm thành một việc riêng.

Trong bảng "Cần Claude xem", Claude sửa thêm 12 mục chắc chắn:

| Mục | Cũ | Mới |
|---|---|---|
| nurse | bảo mỗ | (bỏ) |
| angle | gốc | góc |
| abandon | bộm | (bỏ) |
| circus | xiệc | (bỏ, đã có "xiếc") |
| pupil | ngươi | con ngươi |
| nanny | nhũ ảo | (bỏ) |
| mummy | uây khyếm mẹ | (bỏ) |
| chromosome | chất sinh sắt | (bỏ) |
| rainbow | lẹm | (bỏ) |
| pioneer | namviet | (bỏ) |
| plummet | lập loòng | (bỏ) |
| blackbird | hạch thước điểu | chim hoét đen |

Các mục còn lại trong bảng giữ nguyên: là biến thể, từ địa phương hay thuật ngữ cũ, chưa đủ căn cứ để sửa.

`node scripts/generate-vocabulary.mjs` đạt (18.000 mục, 100 cấp). Tổng cộng 50 mục đổi trong 37 file.
