import json

# Manual word-by-word cognitive review for Batch 21 Round 6 Part 4 (records 2800-2899, IDs 200k.002802 to 200k.002901)
reviewed_entries = [
    # 2800: degree day
    {"ipa": "/dɪˈɡriː deɪ/", "vi": "độ-ngày đo nhiệt năng tiêu thụ", "pos": "phrase"},
    # 2801: dream up
    {"ipa": "/driːm ʌp/", "vi": "nghĩ ra sáng kiến lạ; bịa đặt ra", "pos": "phrase"},
    # 2802: drink in
    {"ipa": "/drɪŋk ɪn/", "vi": "say sưa ngắm nhìn; đắm chìm thưởng", "pos": "phrase"},
    # 2803: drop away
    {"ipa": "/drɑːp əˈweɪ/", "vi": "giảm sút rõ rệt; rời rạc thưa dần", "pos": "phrase"},
    # 2804: face card
    {"ipa": "/feɪs kɑːrd/", "vi": "quân bài hình người tây J Q K", "pos": "phrase"},
    # 2805: fall behind
    {"ipa": "/fɔːl bɪˈhaɪnd/", "vi": "tụt lại phía sau; chậm trễ tiến độ", "pos": "phrase"},
    # 2806: finish out
    {"ipa": "/ˈfɪnɪʃ aʊt/", "vi": "hoàn thành nốt phần cuối nhiệm kỳ", "pos": "phrase"},
    # 2807: finish up
    {"ipa": "/ˈfɪnɪʃ ʌp/", "vi": "hoàn tất toàn bộ; kết thúc trọn", "pos": "phrase"},
    # 2808: forward market
    {"ipa": "/ˈfɔːrwərd ˈmɑːrkɪt/", "vi": "thị trường kỳ hạn hợp đồng hàng", "pos": "phrase"},
    # 2809: french leave
    {"ipa": "/frɛntʃ liːv/", "vi": "việc chuồn êm không xin phép từ giã", "pos": "phrase"},
    # 2810: full treatment
    {"ipa": "/fʊl ˈtriːtmənt/", "vi": "dịch vụ trọn gói chu đáo tận tình", "pos": "phrase"},
    # 2811: gas system
    {"ipa": "/ɡæs ˈsɪstəm/", "vi": "hệ thống đường ống dẫn khí đốt gas", "pos": "phrase"},
    # 2812: general officer
    {"ipa": "/ˈdʒɛnərəl ˈɔːfɪsər/", "vi": "sĩ quan cấp tướng trong quân đội", "pos": "phrase"},
    # 2813: green market
    {"ipa": "/ɡriːn ˈmɑːrkɪt/", "vi": "chợ nông sản rau củ quả tươi sạch", "pos": "phrase"},
    # 2814: head cold
    {"ipa": "/hɛd koʊld/", "vi": "chứng cảm lạnh sổ mũi nhức đầu", "pos": "phrase"},
    # 2815: health professional
    {"ipa": "/hɛlθ prəˈfɛʃənəl/", "vi": "chuyên gia y tế; nhân viên y tế", "pos": "phrase"},
    # 2816: hospital room
    {"ipa": "/ˈhɑːspɪtl ruːm/", "vi": "phòng bệnh nhân nội trú bệnh viện", "pos": "phrase"},
    # 2817: key west
    {"ipa": "/kiː wɛst/", "vi": "đảo Key West ở cực nam bang Florida", "pos": "phrase"},
    # 2818: line officer
    {"ipa": "/laɪn ˈɔːfɪsər/", "vi": "sĩ quan chỉ huy tác chiến mặt trận", "pos": "phrase"},
    # 2819: luck out
    {"ipa": "/lʌk aʊt/", "vi": "gặp vận may bất ngờ; số đỏ bất ngờ", "pos": "phrase"},
    # 2820: major key
    {"ipa": "/ˈmeɪdʒər kiː/", "vi": "giọng trưởng trong hệ thống âm nhạc", "pos": "phrase"},
    # 2821: man friday
    {"ipa": "/mæn ˈfraɪdeɪ/", "vi": "trợ thủ đắc lực; cánh tay phải thân", "pos": "phrase"},
    # 2822: middle term
    {"ipa": "/ˈmɪdəl tɜːrm/", "vi": "trung từ trong tam đoạn luận logic", "pos": "phrase"},
    # 2823: military position
    {"ipa": "/ˈmɪlətɛri pəˈzɪʃən/", "vi": "vị trí quân sự; cứ điểm phòng thủ", "pos": "phrase"},
    # 2824: north star state
    {"ipa": "/nɔːrθ stɑːr steɪt/", "vi": "biệt danh bang Minnesota Hoa Kỳ", "pos": "phrase"},
    # 2825: oil future
    {"ipa": "/ɔɪl ˈfjuːtʃər/", "vi": "hợp đồng dầu thô tương lai kỳ hạn", "pos": "phrase"},
    # 2826: police dog
    {"ipa": "/pəˈliːs dɔːɡ/", "vi": "chó nghiệp vụ cảnh sát phá án", "pos": "phrase"},
    # 2827: political science
    {"ipa": "/pəˈlɪtɪkəl ˈsaɪəns/", "vi": "ngành chính trị học viện nghiên cứu", "pos": "phrase"},
    # 2828: pressure group
    {"ipa": "/ˈprɛʃər ɡruːp/", "vi": "nhóm gây sức ép vận động hành lang", "pos": "phrase"},
    # 2829: pressure point
    {"ipa": "/ˈprɛʃər pɔɪnt/", "vi": "huyệt đạo bấm huyệt; điểm nhạy cảm", "pos": "phrase"},
    # 2830: reading program
    {"ipa": "/ˈriːdɪŋ ˈproʊɡræm/", "vi": "chương trình rèn luyện kỹ năng đọc", "pos": "phrase"},
    # 2831: record player
    {"ipa": "/ˈrɛkərd ˈpleɪər/", "vi": "máy quay đĩa than cổ điển phát nhạc", "pos": "phrase"},
    # 2832: red china
    {"ipa": "/rɛd ˈtʃaɪnə/", "vi": "Trung Quốc thời Chiến tranh Lạnh", "pos": "phrase"},
    # 2833: right brain
    {"ipa": "/raɪt breɪn/", "vi": "bán cầu não phải sáng tạo cảm xúc", "pos": "phrase"},
    # 2834: sea level
    {"ipa": "/siː ˈlɛvəl/", "vi": "mực nước biển chuẩn trắc địa", "pos": "phrase"},
    # 2835: side effect
    {"ipa": "/saɪd ɪˈfɛkt/", "vi": "tác dụng phụ không mong muốn", "pos": "phrase"},
    # 2836: sit in
    {"ipa": "/sɪt ɪn/", "vi": "biểu tình ngồi; dự thính lớp học", "pos": "phrase"},
    # 2837: social security number
    {"ipa": "/ˈsoʊʃəl sɪˈkjʊrəti ˈnʌmbər/", "vi": "mã số thẻ an sinh xã hội tại Mỹ", "pos": "phrase"},
    # 2838: source program
    {"ipa": "/sɔːrs ˈproʊɡræm/", "vi": "chương trình nguồn; tệp mã nguồn", "pos": "phrase"},
    # 2839: south australia
    {"ipa": "/saʊθ ɔːˈstreɪliə/", "vi": "tiểu bang Nam Úc trù phú", "pos": "phrase"},
    # 2840: south sea
    {"ipa": "/saʊθ siː/", "vi": "vùng biển Nam Thái Bình Dương ấm áp", "pos": "phrase"},
    # 2841: straight face
    {"ipa": "/streɪt feɪs/", "vi": "nét mặt tỉnh bơ không hề mỉm cười", "pos": "phrase"},
    # 2842: table talk
    {"ipa": "/ˈteɪbəl tɔːk/", "vi": "chuyện phiếm rôm rả trên bàn ăn", "pos": "phrase"},
    # 2843: take the floor
    {"ipa": "/teɪk ðə flɔːr/", "vi": "đứng lên phát biểu ý kiến tại nghị", "pos": "phrase"},
    # 2844: talking picture
    {"ipa": "/ˈtɔːkɪŋ ˈpɪktʃər/", "vi": "bộ phim điện ảnh có lồng tiếng động", "pos": "phrase"},
    # 2845: tax program
    {"ipa": "/tæks ˈproʊɡræm/", "vi": "chương trình phần mềm kê khai thuế", "pos": "phrase"},
    # 2846: test period
    {"ipa": "/tɛst ˈpɪriəd/", "vi": "giai đoạn thử nghiệm kiểm định chất", "pos": "phrase"},
    # 2847: touch up
    {"ipa": "/tʌtʃ ʌp/", "vi": "tút lại dung nhan; chấm sửa nét vẽ", "pos": "phrase"},
    # 2848: walk on air
    {"ipa": "/wɔːk ɑːn ɛr/", "vi": "vui sướng ngất ngây; lâng lâng hạnh", "pos": "phrase"},
    # 2849: whole note
    {"ipa": "/hoʊl noʊt/", "vi": "nốt tròn có giá trị bốn phách nhạc", "pos": "phrase"},
    # 2850: work to rule
    {"ipa": "/wɜːrk tuː ruːl/", "vi": "đình công làm việc theo đúng luật", "pos": "phrase"},
    # 2851: cared
    {"ipa": "/kɛrd/", "vi": "đã quan tâm chăm sóc; đã để ý", "pos": "verb"},
    # 2852: cares
    {"ipa": "/kɛrz/", "vi": "những nỗi lo âu; sự săn sóc", "pos": "noun"},
    # 2853: american capital
    {"ipa": "/əˈmɛrɪkən ˈkæpɪtl/", "vi": "thủ đô nước Mỹ; nguồn vốn Mỹ", "pos": "phrase"},
    # 2854: american football game
    {"ipa": "/əˈmɛrɪkən ˈfʊtˌbɔːl ɡeɪm/", "vi": "trận đấu bóng bầu dục kiểu nước Mỹ", "pos": "phrase"},
    # 2855: bank shot
    {"ipa": "/bæŋk ʃɑːt/", "vi": "cú đánh bi da đập băng dội vào lỗ", "pos": "phrase"},
    # 2856: black eye
    {"ipa": "/blæk aɪ/", "vi": "mắt thâm quầng tím; vết nhơ sỉ nhục", "pos": "phrase"},
    # 2857: blue baby
    {"ipa": "/bluː ˈbeɪbi/", "vi": "trẻ sơ sinh bị chứng tím tái da bẩm", "pos": "phrase"},
    # 2858: board meeting
    {"ipa": "/bɔːrd ˈmiːtɪŋ/", "vi": "cuộc họp hội đồng quản trị định kỳ", "pos": "phrase"},
    # 2859: bring forward
    {"ipa": "/brɪŋ ˈfɔːrwərd/", "vi": "đưa ra đề xuất thảo luận; chuyển số", "pos": "phrase"},
    # 2860: by machine
    {"ipa": "/baɪ məˈʃiːn/", "vi": "được gia công chế tạo bằng máy móc", "pos": "phrase"},
    # 2861: carry on
    {"ipa": "/ˈkæri ɑːn/", "vi": "tiếp tục duy trì; cư xử nhặng xị", "pos": "phrase"},
    # 2862: caught up
    {"ipa": "/kɔːt ʌp/", "vi": "bị cuốn vào vòng xoáy; bắt kịp theo", "pos": "phrase"},
    # 2863: chinese white
    {"ipa": "/ˌtʃaɪˈniːz waɪt/", "vi": "bột kẽm trắng dùng trong hội họa", "pos": "phrase"},
    # 2864: civil day
    {"ipa": "/ˈsɪvəl deɪ/", "vi": "ngày dương lịch tính từ nửa đêm", "pos": "phrase"},
    # 2865: civil right
    {"ipa": "/ˈsɪvəl raɪt/", "vi": "quyền dân sự; quyền công dân cơ bản", "pos": "phrase"},
    # 2866: civil year
    {"ipa": "/ˈsɪvəl jɪr/", "vi": "năm dương lịch theo lịch nhà nước", "pos": "phrase"},
    # 2867: club member
    {"ipa": "/klʌb ˈmɛmbər/", "vi": "thành viên câu lạc bộ chính thức", "pos": "phrase"},
    # 2868: coach house
    {"ipa": "/koʊtʃ haʊs/", "vi": "nhà để cỗ xe ngựa thời xưa quý tộc", "pos": "phrase"},
    # 2869: cold war
    {"ipa": "/koʊld wɔːr/", "vi": "thời kỳ Chiến tranh Lạnh căng thẳng", "pos": "phrase"},
    # 2870: common sense
    {"ipa": "/ˈkɑːmən sɛns/", "vi": "lẽ thường tình; lương tri phán đoán", "pos": "phrase"},
    # 2871: conference call
    {"ipa": "/ˈkɑːnfərəns kɔːl/", "vi": "cuộc đàm thoại hội nghị nhiều bên", "pos": "phrase"},
    # 2872: country store
    {"ipa": "/ˈkʌntri stɔːr/", "vi": "tiệm tạp hóa bách hóa vùng thôn quê", "pos": "phrase"},
    # 2873: court card
    {"ipa": "/kɔːrt kɑːrd/", "vi": "quân bài hình người hoàng gia J Q K", "pos": "phrase"},
    # 2874: credit system
    {"ipa": "/ˈkrɛdɪt ˈsɪstəm/", "vi": "hệ thống tín dụng mua trả góp", "pos": "phrase"},
    # 2875: cup final
    {"ipa": "/kʌp ˈfaɪnəl/", "vi": "trận chung kết tranh cúp vô địch", "pos": "phrase"},
    # 2876: cut rate
    {"ipa": "/kʌt reɪt/", "vi": "mức giá hạ sâu; bán giá chiết khấu", "pos": "phrase"},
    # 2877: dead center
    {"ipa": "/dɛd ˈsɛntər/", "vi": "chính giữa tâm; điểm chết piston", "pos": "phrase"},
    # 2878: deep south
    {"ipa": "/diːp saʊθ/", "vi": "vùng Viễn Nam của nước Mỹ", "pos": "phrase"},
    # 2879: doctor up
    {"ipa": "/ˈdɑːktər ʌp/", "vi": "ngụy tạo làm sai lệch; sửa tạm thời", "pos": "phrase"},
    # 2880: drink up
    {"ipa": "/drɪŋk ʌp/", "vi": "uống cạn ly; uống sạch không còn", "pos": "phrase"},
    # 2881: european community
    {"ipa": "/ˌjʊrəˈpiːən kəˈmjuːnəti/", "vi": "Cộng đồng Kinh tế các nước Châu Âu", "pos": "phrase"},
    # 2882: female person
    {"ipa": "/ˈfiːmeɪl ˈpɜːrsən/", "vi": "phụ nữ giới tính nữ; người nữ giới", "pos": "phrase"},
    # 2883: film industry
    {"ipa": "/fɪlm ˈɪndəstri/", "vi": "ngành công nghiệp sản xuất điện ảnh", "pos": "phrase"},
    # 2884: film star
    {"ipa": "/fɪlm stɑːr/", "vi": "minh tinh màn bạc; ngôi sao màn ảnh", "pos": "phrase"},
    # 2885: fire chief
    {"ipa": "/ˈfaɪər tʃiːf/", "vi": "chỉ huy cứu hỏa; trưởng đội cứu hỏa", "pos": "phrase"},
    # 2886: gas line
    {"ipa": "/ɡæs laɪn/", "vi": "đường ống dẫn gas; hàng mua xăng", "pos": "phrase"},
    # 2887: gas service
    {"ipa": "/ɡæs ˈsɜːrvɪs/", "vi": "dịch vụ cung ứng khí đốt dân dụng", "pos": "phrase"},
    # 2888: general store
    {"ipa": "/ˈdʒɛnərəl stɔːr/", "vi": "cửa tiệm bách hóa tổng hợp tạp hóa", "pos": "phrase"},
    # 2889: get in touch
    {"ipa": "/ɡɛt ɪn tʌtʃ/", "vi": "chủ động liên hệ; giữ liên lạc", "pos": "phrase"},
    # 2890: grow up
    {"ipa": "/ɡroʊ ʌp/", "vi": "trưởng thành lớn khôn; khôn lớn dần", "pos": "phrase"},
    # 2891: half note
    {"ipa": "/hæf noʊt/", "vi": "nốt trắng giá trị hai phách nhạc", "pos": "phrase"},
    # 2892: heart attack
    {"ipa": "/hɑːrt əˈtæk/", "vi": "cơn đau tim; nhồi máu cơ tim cấp", "pos": "phrase"},
    # 2893: high german
    {"ipa": "/haɪ ˈdʒɜːrmən/", "vi": "tiếng Đức chuẩn vùng Thượng Đức", "pos": "phrase"},
    # 2894: home secretary
    {"ipa": "/hoʊm ˈsɛkrətɛri/", "vi": "Bộ trưởng Nội vụ của nước Anh", "pos": "phrase"},
    # 2895: hot issue
    {"ipa": "/hɑːt ˈɪʃuː/", "vi": "vấn đề nóng hổi; cổ phiếu sốt giá", "pos": "phrase"},
    # 2896: human race
    {"ipa": "/ˈhjuːmən reɪs/", "vi": "toàn thể nhân loại; loài người", "pos": "phrase"},
    # 2897: ice water
    {"ipa": "/aɪs ˈwɔːtər/", "vi": "nước ướp đá lạnh giải khát", "pos": "phrase"},
    # 2898: in reality
    {"ipa": "/ɪn riˈæləti/", "vi": "trên thực tế khách quan; kỳ thực là", "pos": "phrase"},
    # 2899: law officer
    {"ipa": "/lɔː ˈɔːfɪsər/", "vi": "nhân viên chấp pháp thi hành án", "pos": "phrase"},
]

with open('scratch/b21_r06_raw_p4.json') as f:
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

with open('scratch/b21_r06_p4.json', 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("b21_r06_p4.json created successfully and validated!")
