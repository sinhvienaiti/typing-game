import json

# Manual word-by-word cognitive review for Batch 21 Round 8 Part 1 (records 3500-3599, IDs 200k.003502 to 200k.003601)
reviewed_entries = [
    # 3500: land mine
    {"ipa": "/lænd maɪn/", "vi": "quả mìn chôn dưới đất sát thương", "pos": "phrase"},
    # 3501: light minute
    {"ipa": "/laɪt ˈmɪnɪt/", "vi": "phút ánh sáng đo cự ly vũ trụ", "pos": "phrase"},
    # 3502: line of defense
    {"ipa": "/laɪn ʌv dɪˈfɛns/", "vi": "tuyến phòng thủ; lá chắn phòng ngự", "pos": "phrase"},
    # 3503: line organization
    {"ipa": "/laɪn ˌɔːrɡənəˈzeɪʃən/", "vi": "cơ cấu tổ chức theo tuyến trực tiếp", "pos": "phrase"},
    # 3504: market cross
    {"ipa": "/ˈmɑːrkɪt krɔːs/", "vi": "cây thánh giá dựng ở giữa chợ quê", "pos": "phrase"},
    # 3505: material body
    {"ipa": "/məˈtɪriəl ˈbɑːdi/", "vi": "vật thể vật chất; thân xác hữu hình", "pos": "phrase"},
    # 3506: modern english
    {"ipa": "/ˈmɑːdərn ˈɪŋɡlɪʃ/", "vi": "tiếng Anh thời kỳ hiện đại ngày nay", "pos": "phrase"},
    # 3507: money plant
    {"ipa": "/ˈmʌni plænt/", "vi": "cây kim tiền; cây bạc tài lộc", "pos": "phrase"},
    # 3508: new york minute
    {"ipa": "/nuː jɔːrk ˈmɪnɪt/", "vi": "trong tích tắc; chỉ trong chớp mắt", "pos": "phrase"},
    # 3509: oil production
    {"ipa": "/ɔɪl prəˈdʌkʃən/", "vi": "sản lượng khai thác dầu khí mỏ", "pos": "phrase"},
    # 3510: on faith
    {"ipa": "/ɑːn feɪθ/", "vi": "tin cậy hoàn toàn; nhờ vào đức tin", "pos": "phrase"},
    # 3511: out or keeping
    {"ipa": "/aʊt ɔːr ˈkiːpɪŋ/", "vi": "không hòa hợp; không tương xứng", "pos": "phrase"},
    # 3512: paper gold
    {"ipa": "/ˈpeɪpər ɡoʊld/", "vi": "vàng giấy; quyền rút vốn đặc biệt", "pos": "phrase"},
    # 3513: pay claim
    {"ipa": "/peɪ kleɪm/", "vi": "yêu sách đòi tăng mức lương thưởng", "pos": "phrase"},
    # 3514: peace march
    {"ipa": "/piːs mɑːrtʃ/", "vi": "cuộc tuần hành vì nền hòa bình", "pos": "phrase"},
    # 3515: peace process
    {"ipa": "/piːs ˈprɑːsɛs/", "vi": "tiến trình đàm phán hòa giải hòa", "pos": "phrase"},
    # 3516: period piece
    {"ipa": "/ˈpɪriəd piːs/", "vi": "phim cổ trang; tác phẩm thời kỳ cổ", "pos": "phrase"},
    # 3517: person of color
    {"ipa": "/ˈpɜːrsən ʌv ˈkʌlər/", "vi": "người da màu phi da trắng sắc tộc", "pos": "phrase"},
    # 3518: phone message
    {"ipa": "/foʊn ˈmɛsɪdʒ/", "vi": "tin nhắn điện thoại; lời nhắn thoại", "pos": "phrase"},
    # 3519: piece of land
    {"ipa": "/piːs ʌv lænd/", "vi": "mảnh đất; thửa đất sở hữu riêng", "pos": "phrase"},
    # 3520: plant family
    {"ipa": "/plænt ˈfæməli/", "vi": "họ thực vật trong phân loại học", "pos": "phrase"},
    # 3521: political campaign
    {"ipa": "/pəˈlɪtɪkəl kæmˈpeɪn/", "vi": "chiến dịch vận động tranh cử ghế", "pos": "phrase"},
    # 3522: press release
    {"ipa": "/prɛs rɪˈliːs/", "vi": "bản thông cáo báo chí chính thức", "pos": "phrase"},
    # 3523: primary school
    {"ipa": "/ˈpraɪmɛri skuːl/", "vi": "trường tiểu học; trường cấp một", "pos": "phrase"},
    # 3524: private parts
    {"ipa": "/ˈpraɪvət pɑːrts/", "vi": "vùng kín nhạy cảm; bộ phận sinh dục", "pos": "phrase"},
    # 3525: private practice
    {"ipa": "/ˈpraɪvət ˈpræktɪs/", "vi": "hành nghề tư nhân; mở phòng mạch tư", "pos": "phrase"},
    # 3526: product research
    {"ipa": "/ˈprɑːdʌkt riˈsɜːrtʃ/", "vi": "nghiên cứu phát triển dòng sản phẩm", "pos": "phrase"},
    # 3527: property tax
    {"ipa": "/ˈprɑːpərti tæks/", "vi": "thuế tài sản bất động sản nhà đất", "pos": "phrase"},
    # 3528: public speaking
    {"ipa": "/ˈpʌblɪk ˈspiːkɪŋ/", "vi": "kỹ năng thuyết trình trước đám đông", "pos": "phrase"},
    # 3529: pull in
    {"ipa": "/pʊl ɪn/", "vi": "tàu vào ga đỗ; tấp xe vào lề đường", "pos": "phrase"},
    # 3530: push on
    {"ipa": "/pʊʃ ɑːn/", "vi": "tiếp tục dấn bước; bền bỉ tiến lên", "pos": "phrase"},
    # 3531: religious right
    {"ipa": "/rɪˈlɪdʒəs raɪt/", "vi": "phe cánh hữu tôn giáo bảo thủ Mỹ", "pos": "phrase"},
    # 3532: rich person
    {"ipa": "/rɪtʃ ˈpɜːrsən/", "vi": "người giàu có; bậc đại gia tài sản", "pos": "phrase"},
    # 3533: ride off
    {"ipa": "/raɪd ɔːf/", "vi": "phi ngựa đi mất; phóng xe rời đi", "pos": "phrase"},
    # 3534: rule book
    {"ipa": "/ruːl bʊk/", "vi": "cuốn sách tập hợp điều lệ quy tắc", "pos": "phrase"},
    # 3535: rule of law
    {"ipa": "/ruːl ʌv lɔː/", "vi": "thượng tôn pháp luật; pháp quyền", "pos": "phrase"},
    # 3536: scale up
    {"ipa": "/skeɪl ʌp/", "vi": "mở rộng quy mô hoạt động sản xuất", "pos": "phrase"},
    # 3537: school teacher
    {"ipa": "/skuːl ˈtiːtʃər/", "vi": "thầy cô giáo giảng dạy trường học", "pos": "phrase"},
    # 3538: score out
    {"ipa": "/skɔːr aʊt/", "vi": "dùng bút gạch bỏ dòng chữ sai phạm", "pos": "phrase"},
    # 3539: screen off
    {"ipa": "/skriːn ɔːf/", "vi": "dựng vách bình phong ngăn phòng lại", "pos": "phrase"},
    # 3540: sea star
    {"ipa": "/siː stɑːr/", "vi": "con sao biển năm cánh dưới đáy biển", "pos": "phrase"},
    # 3541: secret service
    {"ipa": "/ˈsiːkrət ˈsɜːrvɪs/", "vi": "sở mật vụ bảo vệ tổng thống Mỹ", "pos": "phrase"},
    # 3542: sell short
    {"ipa": "/sɛl ʃɔːrt/", "vi": "bán khống; coi thường đánh giá thấp", "pos": "phrase"},
    # 3543: separate out
    {"ipa": "/ˈsɛpəreɪt aʊt/", "vi": "chắt lọc tách riêng từng thành phần", "pos": "phrase"},
    # 3544: serve well
    {"ipa": "/sɜːrv wɛl/", "vi": "phục vụ đắc lực; phát huy tác dụng", "pos": "phrase"},
    # 3545: simple interest
    {"ipa": "/ˈsɪmpəl ˈɪntrəst/", "vi": "tiền lãi đơn không nhập vốn", "pos": "phrase"},
    # 3546: site visit
    {"ipa": "/saɪt ˈvɪzɪt/", "vi": "chuyến khảo sát thực địa công trình", "pos": "phrase"},
    # 3547: skin care
    {"ipa": "/skɪn kɛr/", "vi": "liệu trình chăm sóc dưỡng da mặt", "pos": "phrase"},
    # 3548: social contract
    {"ipa": "/ˈsoʊʃəl ˈkɑːntrækt/", "vi": "học thuyết khế ước xã hội triết học", "pos": "phrase"},
    # 3549: social insurance
    {"ipa": "/ˈsoʊʃəl ɪnˈʃʊrəns/", "vi": "chế độ bảo hiểm xã hội trợ cấp", "pos": "phrase"},
    # 3550: social secretary
    {"ipa": "/ˈsoʊʃəl ˈsɛkrətɛri/", "vi": "thư ký phụ trách giao tế xã hội", "pos": "phrase"},
    # 3551: social unit
    {"ipa": "/ˈsoʊʃəl ˈjuːnɪt/", "vi": "tế bào đơn vị tổ chức trong xã hội", "pos": "phrase"},
    # 3552: source language
    {"ipa": "/sɔːrs ˈlæŋɡwɪdʒ/", "vi": "ngôn ngữ gốc trong biên phiên dịch", "pos": "phrase"},
    # 3553: special forces
    {"ipa": "/ˈspɛʃəl ˈfɔːrsɪz/", "vi": "lực lượng binh chủng đặc nhiệm", "pos": "phrase"},
    # 3554: speech day
    {"ipa": "/spiːtʃ deɪ/", "vi": "ngày lễ bế giảng trao phần thưởng", "pos": "phrase"},
    # 3555: sports car
    {"ipa": "/spɔːrts kɑːr/", "vi": "chiếc siêu xe thể thao tốc độ cao", "pos": "phrase"},
    # 3556: spring water
    {"ipa": "/sprɪŋ ˈwɔːtər/", "vi": "dòng nước suối nguồn ngọt mát", "pos": "phrase"},
    # 3557: stage director
    {"ipa": "/steɪdʒ dəˈrɛktər/", "vi": "đạo diễn dàn dựng sân khấu kịch", "pos": "phrase"},
    # 3558: stand oil
    {"ipa": "/stænd ɔɪl/", "vi": "dầu lanh cô đặc dùng pha sơn dầu vẽ", "pos": "phrase"},
    # 3559: step by step
    {"ipa": "/stɛp baɪ stɛp/", "vi": "từng bước một chậm rãi; dần dà từng", "pos": "phrase"},
    # 3560: step forward
    {"ipa": "/stɛp ˈfɔːrwərd/", "vi": "tiến lên phía trước; bước ra nhận", "pos": "phrase"},
    # 3561: stock car
    {"ipa": "/stɑːk kɑːr/", "vi": "xe đua nguyên bản trong giải đua", "pos": "phrase"},
    # 3562: subject matter
    {"ipa": "/ˈsʌbdʒɪkt ˈmætər/", "vi": "chủ đề cốt lõi của tác phẩm nghệ", "pos": "phrase"},
    # 3563: take flight
    {"ipa": "/teɪk flaɪt/", "vi": "cất cánh bay lên; vội vã tháo chạy", "pos": "phrase"},
    # 3564: test bed
    {"ipa": "/tɛst bɛd/", "vi": "bệ thử nghiệm kỹ thuật động cơ", "pos": "phrase"},
    # 3565: test paper
    {"ipa": "/tɛst ˈpeɪpər/", "vi": "tờ giấy thi; giấy quỳ tím thử hóa", "pos": "phrase"},
    # 3566: the hill
    {"ipa": "/ðə hɪl/", "vi": "Đồi Capitol trụ sở Quốc hội Mỹ", "pos": "phrase"},
    # 3567: think twice
    {"ipa": "/θɪŋk twaɪs/", "vi": "cân nhắc đắn đo suy nghĩ kỹ càng", "pos": "phrase"},
    # 3568: throw out
    {"ipa": "/θroʊ aʊt/", "vi": "ném vứt ra ngoài; bác bỏ dự luật", "pos": "phrase"},
    # 3569: throw up
    {"ipa": "/θroʊ ʌp/", "vi": "nôn mửa thức ăn; xây vội bức tường", "pos": "phrase"},
    # 3570: touch system
    {"ipa": "/tʌtʃ ˈsɪstəm/", "vi": "phương pháp gõ phím mười ngón", "pos": "phrase"},
    # 3571: travel plan
    {"ipa": "/ˈtrævəl plæn/", "vi": "lịch trình chuyến du lịch nghỉ ngơi", "pos": "phrase"},
    # 3572: united states army
    {"ipa": "/juːˈnaɪtɪd steɪts ˈɑːrmi/", "vi": "Lục quân Hợp chúng quốc Hoa Kỳ", "pos": "phrase"},
    # 3573: war dance
    {"ipa": "/wɔːr dæns/", "vi": "điệu múa xung trận mừng chiến thắng", "pos": "phrase"},
    # 3574: working rule
    {"ipa": "/ˈwɜːrkɪŋ ruːl/", "vi": "nội quy quy tắc làm việc chuẩn mực", "pos": "phrase"},
    # 3575: generals
    {"ipa": "/ˈdʒɛnərəlz/", "vi": "các vị tướng lĩnh; các đại tướng", "pos": "noun"},
    # 3576: acting out
    {"ipa": "/ˈæktɪŋ aʊt/", "vi": "hành vi bột phát mất kiểm soát", "pos": "phrase"},
    # 3577: action potential
    {"ipa": "/ˈækʃən pəˈtɛnʃəl/", "vi": "điện thế hoạt động màng tế bào", "pos": "phrase"},
    # 3578: air letter
    {"ipa": "/ɛr ˈlɛtər/", "vi": "thư gửi đường bưu chính hàng không", "pos": "phrase"},
    # 3579: air unit
    {"ipa": "/ɛr ˈjuːnɪt/", "vi": "đơn vị phi đội không quân tác chiến", "pos": "phrase"},
    # 3580: american dream
    {"ipa": "/əˈmɛrɪkən driːm/", "vi": "Giấc mơ Mỹ về cuộc sống thịnh vượng", "pos": "phrase"},
    # 3581: american indian
    {"ipa": "/əˈmɛrɪkən ˈɪndiən/", "vi": "người bản địa châu Mỹ; người da đỏ", "pos": "phrase"},
    # 3582: as follows
    {"ipa": "/æz ˈfɑːloʊz/", "vi": "như sau đây; như liệt kê dưới này", "pos": "phrase"},
    # 3583: ball club
    {"ipa": "/bɔːl klʌb/", "vi": "câu lạc bộ bóng chày chuyên nghiệp", "pos": "phrase"},
    # 3584: band together
    {"ipa": "/bænd təˈɡɛðər/", "vi": "liên minh kết đoàn lại với nhau", "pos": "phrase"},
    # 3585: bar girl
    {"ipa": "/bɑːr ɡɜːrl/", "vi": "nữ nhân viên tiếp rượu quán bar", "pos": "phrase"},
    # 3586: bed ground
    {"ipa": "/bɛd ɡraʊnd/", "vi": "bãi đất cho đàn gia súc ngủ qua đêm", "pos": "phrase"},
    # 3587: black africa
    {"ipa": "/blæk ˈæfrɪkə/", "vi": "vùng châu Phi hạ Sahara lục địa đen", "pos": "phrase"},
    # 3588: black operation
    {"ipa": "/blæk ˌɑːpəˈreɪʃən/", "vi": "chiến dịch tình báo ngầm tối mật", "pos": "phrase"},
    # 3589: blue blood
    {"ipa": "/bluː blʌd/", "vi": "dòng dõi quý tộc dòng máu hoàng gia", "pos": "phrase"},
    # 3590: body image
    {"ipa": "/ˈbɑːdi ˈɪmɪdʒ/", "vi": "hình ảnh cảm nhận về vóc dáng mình", "pos": "phrase"},
    # 3591: brain death
    {"ipa": "/breɪn dɛθ/", "vi": "trạng thái chết não mất tri giác", "pos": "phrase"},
    # 3592: capital cost
    {"ipa": "/ˈkæpɪtl kɔːst/", "vi": "chi phí đầu tư vốn tài sản ban đầu", "pos": "phrase"},
    # 3593: card player
    {"ipa": "/kɑːrd ˈpleɪər/", "vi": "tay chơi bài tây; người đánh bài", "pos": "phrase"},
    # 3594: centre bit
    {"ipa": "/ˈsɛntər bɪt/", "vi": "mũi khoan có chốt định tâm khoan gỗ", "pos": "phrase"},
    # 3595: christian name
    {"ipa": "/ˈkrɪstʃən neɪm/", "vi": "tên thánh khi rửa tội; tên chính", "pos": "phrase"},
    # 3596: city block
    {"ipa": "/ˈsɪti blɑːk/", "vi": "khu phố bao quanh bởi bốn con đường", "pos": "phrase"},
    # 3597: color line
    {"ipa": "/ˈkʌlər laɪn/", "vi": "hàng rào ranh giới phân biệt màu da", "pos": "phrase"},
    # 3598: commercial law
    {"ipa": "/kəˈmɜːrʃəl lɔː/", "vi": "ngành luật thương mại doanh nghiệp", "pos": "phrase"},
    # 3599: common box
    {"ipa": "/ˈkɑːmən bɑːks/", "vi": "cây hoàng dương lá thường xanh bóng", "pos": "phrase"},
]

with open('scratch/b21_r08_raw_p1.json') as f:
    raw_data = json.load(f)

assert len(raw_data) == 100
assert len(reviewed_entries) == 100

output = []
for i, item in enumerate(raw_data):
    rev = reviewed_entries[i]
    assert rev["ipa"].startswith("/") and rev["ipa"].endswith("/") and rev["ipa"].count("/") == 2
    assert len(rev["vi"]) <= 35, f"vi too long: {rev['vi']} ({len(rev['vi'])} chars)"
    assert rev["pos"] in ["noun", "verb", "adj", "adv", "phrase", "intj", "prep", "conj", "pron", "det", "num"]
    
    new_item = {
        "id": item["id"],
        "hw": item["hw"],
        "pos": rev["pos"],
        "ipa": rev["ipa"],
        "vi": rev["vi"],
        "cefr": item["cefr"],
        "tier": item["tier"],
        "status": "reviewed",
        "notes": item["notes"]
    }
    output.append(new_item)

with open('scratch/b21_r08_p1.json', 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("b21_r08_p1.json created successfully and validated!")
