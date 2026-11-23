import json

# Manual word-by-word cognitive review for Batch 21 Round 7 Part 1 (records 3000-3099, IDs 200k.003002 to 200k.003101)
reviewed_entries = [
    # 3000: wear down
    {"ipa": "/wɛr daʊn/", "vi": "làm cho hao mòn; làm kiệt quệ ý chí", "pos": "phrase"},
    # 3001: wear off
    {"ipa": "/wɛr ɔːf/", "vi": "mất dần tác dụng; phai nhạt dần", "pos": "phrase"},
    # 3002: white sale
    {"ipa": "/waɪt seɪl/", "vi": "đợt hạ giá ga gối khăn trải giường", "pos": "phrase"},
    # 3003: working capital
    {"ipa": "/ˈwɜːrkɪŋ ˈkæpɪtl/", "vi": "nguồn vốn lưu động kinh doanh", "pos": "phrase"},
    # 3004: world organization
    {"ipa": "/wɜːrld ˌɔːrɡənəˈzeɪʃən/", "vi": "tổ chức liên kết toàn cầu quốc tế", "pos": "phrase"},
    # 3005: fullest
    {"ipa": "/ˈfʊlɪst/", "vi": "đầy đủ nhất; trọn vẹn chi tiết nhất", "pos": "adj"},
    # 3006: livest
    {"ipa": "/ˈlaɪvɪst/", "vi": "sống động nhất; sôi nổi nhiệt nhất", "pos": "adj"},
    # 3007: makings
    {"ipa": "/ˈmeɪkɪŋz/", "vi": "tố chất tài năng; vật liệu chế tạo", "pos": "noun"},
    # 3008: reads
    {"ipa": "/riːdz/", "vi": "những cuốn sách hay rất đáng đọc", "pos": "noun"},
    # 3009: art paper
    {"ipa": "/ɑːrt ˈpeɪpər/", "vi": "giấy tráng bóng in tranh mỹ thuật", "pos": "phrase"},
    # 3010: australian state
    {"ipa": "/ɔːˈstreɪliən steɪt/", "vi": "tiểu bang của liên bang Úc", "pos": "phrase"},
    # 3011: baby oil
    {"ipa": "/ˈbeɪbi ɔɪl/", "vi": "dầu thoa mát-xa dưỡng da em bé", "pos": "phrase"},
    # 3012: be sick
    {"ipa": "/biː sɪk/", "vi": "bị ốm đau; nôn mửa khó chịu", "pos": "phrase"},
    # 3013: bed check
    {"ipa": "/bɛd tʃɛk/", "vi": "điểm danh phòng ngủ đêm trại lính", "pos": "phrase"},
    # 3014: big sister
    {"ipa": "/bɪɡ ˈsɪstər/", "vi": "chị gái ruột; người bảo trợ nữ", "pos": "phrase"},
    # 3015: bill of rights
    {"ipa": "/bɪl ʌv raɪts/", "vi": "tuyên ngôn nhân quyền hiến định", "pos": "phrase"},
    # 3016: black ice
    {"ipa": "/blæk aɪs/", "vi": "lớp băng đen trơn trượt trên mặt lộ", "pos": "phrase"},
    # 3017: block out
    {"ipa": "/blɑːk aʊt/", "vi": "chắn ánh sáng; phác họa đường nét", "pos": "phrase"},
    # 3018: block up
    {"ipa": "/blɑːk ʌp/", "vi": "bịt kín lối đi; làm tắc nghẽn dòng", "pos": "phrase"},
    # 3019: body weight
    {"ipa": "/ˈbɑːdi weɪt/", "vi": "trọng lượng thể trọng của cơ thể", "pos": "phrase"},
    # 3020: building code
    {"ipa": "/ˈbɪldɪŋ koʊd/", "vi": "bộ quy chuẩn kỹ thuật xây dựng nhà", "pos": "phrase"},
    # 3021: catch it
    {"ipa": "/kætʃ ɪt/", "vi": "bị la mắng tơi bời; chịu đòn phạt", "pos": "phrase"},
    # 3022: catch on
    {"ipa": "/kætʃ ɑːn/", "vi": "trở nên thịnh hành; hiểu ra vấn đề", "pos": "phrase"},
    # 3023: cause to sleep
    {"ipa": "/kɔːz tuː sliːp/", "vi": "ru cho ngủ yên; gây buồn ngủ say", "pos": "phrase"},
    # 3024: central america
    {"ipa": "/ˈsɛntrəl əˈmɛrɪkə/", "vi": "khu vực eo đất Trung Mỹ châu Mỹ", "pos": "phrase"},
    # 3025: christmas day
    {"ipa": "/ˈkrɪsməs deɪ/", "vi": "ngày lễ Giáng sinh 25 tháng 12", "pos": "phrase"},
    # 3026: church member
    {"ipa": "/tʃɜːrtʃ ˈmɛmbər/", "vi": "tín hữu thành viên giáo xứ giáo hội", "pos": "phrase"},
    # 3027: common ground
    {"ipa": "/ˈkɑːmən ɡraʊnd/", "vi": "điểm tương đồng; tiếng nói chung", "pos": "phrase"},
    # 3028: computer business
    {"ipa": "/kəmˈpjuːtər ˈbɪznəs/", "vi": "ngành kinh doanh máy tính tin học", "pos": "phrase"},
    # 3029: computer system
    {"ipa": "/kəmˈpjuːtər ˈsɪstəm/", "vi": "hệ thống máy vi tính điện tử", "pos": "phrase"},
    # 3030: course credit
    {"ipa": "/kɔːrs ˈkrɛdɪt/", "vi": "tín chỉ học phần tích lũy đại học", "pos": "phrase"},
    # 3031: double talk
    {"ipa": "/ˈdʌbəl tɔːk/", "vi": "lời nói quanh co cố ý đánh lận", "pos": "phrase"},
    # 3032: drive line system
    {"ipa": "/draɪv laɪn ˈsɪstəm/", "vi": "hệ thống truyền động trục xe ô tô", "pos": "phrase"},
    # 3033: drop line
    {"ipa": "/drɑːp laɪn/", "vi": "dòng tiêu đề thụt lề; dây câu cá", "pos": "phrase"},
    # 3034: drop open
    {"ipa": "/drɑːp ˈoʊpən/", "vi": "há hốc mồm kinh ngạc; bật mở toang", "pos": "phrase"},
    # 3035: economic process
    {"ipa": "/ˌɛkəˈnɑːmɪk ˈprɑːsɛs/", "vi": "tiến trình phát triển kinh tế vĩ mô", "pos": "phrase"},
    # 3036: european plan
    {"ipa": "/ˌjʊrəˈpiːən plæn/", "vi": "giá phòng không gồm bữa ăn tiền", "pos": "phrase"},
    # 3037: extra point
    {"ipa": "/ˈɛkstrə pɔɪnt/", "vi": "điểm thưởng sút phạt bóng bầu dục", "pos": "phrase"},
    # 3038: family unit
    {"ipa": "/ˈfæməli ˈjuːnɪt/", "vi": "tế bào gia đình; hộ gia đình chuẩn", "pos": "phrase"},
    # 3039: film director
    {"ipa": "/fɪlm dəˈrɛktər/", "vi": "đạo diễn phim điện ảnh nghệ thuật", "pos": "phrase"},
    # 3040: final decision
    {"ipa": "/ˈfaɪnəl dɪˈsɪʒən/", "vi": "quyết định sau cùng; chung cuộc", "pos": "phrase"},
    # 3041: finish off
    {"ipa": "/ˈfɪnɪʃ ɔːf/", "vi": "kết liễu đối thủ; ăn sạch nốt phần", "pos": "phrase"},
    # 3042: floor show
    {"ipa": "/flɔːr ʃoʊ/", "vi": "chương trình biểu diễn quán bar đêm", "pos": "phrase"},
    # 3043: football field
    {"ipa": "/ˈfʊtˌbɔːl fiːld/", "vi": "sân bóng bầu dục; sân cỏ bóng đá", "pos": "phrase"},
    # 3044: front door
    {"ipa": "/frʌnt dɔːr/", "vi": "cửa chính phía trước căn nhà", "pos": "phrase"},
    # 3045: get worse
    {"ipa": "/ɡɛt wɜːrs/", "vi": "trở nên tồi tệ hơn; diễn biến xấu", "pos": "phrase"},
    # 3046: go fish
    {"ipa": "/ɡoʊ fɪʃ/", "vi": "trò chơi bài câu cá Go Fish cho trẻ", "pos": "phrase"},
    # 3047: government income
    {"ipa": "/ˈɡʌvərnmənt ˈɪnkʌm/", "vi": "nguồn thu ngân sách nhà nước", "pos": "phrase"},
    # 3048: grow over
    {"ipa": "/ɡroʊ ˈoʊvər/", "vi": "mọc bò lan phủ kín mặt đất cây cối", "pos": "phrase"},
    # 3049: had crime
    {"ipa": "/hæd kraɪm/", "vi": "tội phạm theo luật hình sự Hồi giáo", "pos": "phrase"},
    # 3050: half track
    {"ipa": "/hæf træk/", "vi": "xe bọc thép bán xích quân sự", "pos": "phrase"},
    # 3051: hard sell
    {"ipa": "/hɑːrd sɛl/", "vi": "chiêu bán hàng chèo kéo ép mua", "pos": "phrase"},
    # 3052: in camera
    {"ipa": "/ɪn ˈkæmərə/", "vi": "xử kín trong phòng thẩm phán riêng", "pos": "phrase"},
    # 3053: international date line
    {"ipa": "/ˌɪntərˈnæʃənəl deɪt laɪn/", "vi": "đường đổi ngày quốc tế kinh tuyến", "pos": "phrase"},
    # 3054: john rock
    {"ipa": "/dʒɑːn rɑːk/", "vi": "bác sĩ sản khoa John Rock của Mỹ", "pos": "phrase"},
    # 3055: light sleep
    {"ipa": "/laɪt sliːp/", "vi": "giấc ngủ nông chập chờn dễ tỉnh", "pos": "phrase"},
    # 3056: long beach
    {"ipa": "/lɔːŋ biːtʃ/", "vi": "thành phố cảng Long Beach ở Mỹ", "pos": "phrase"},
    # 3057: luck through
    {"ipa": "/lʌk θruː/", "vi": "vượt qua gian nan nhờ may mắn số đỏ", "pos": "phrase"},
    # 3058: major fast day
    {"ipa": "/ˈmeɪdʒər fæst deɪ/", "vi": "ngày đại lễ ăn chay trọng Do Thái", "pos": "phrase"},
    # 3059: make grow
    {"ipa": "/meɪk ɡroʊ/", "vi": "vun đắp phát triển; làm tăng vọt", "pos": "phrase"},
    # 3060: may fish
    {"ipa": "/meɪ fɪʃ/", "vi": "loài cá sọc đen nhỏ sống ven bờ", "pos": "phrase"},
    # 3061: medical center
    {"ipa": "/ˈmɛdɪkəl ˈsɛntər/", "vi": "trung tâm y tế khám chữa bệnh lớn", "pos": "phrase"},
    # 3062: member bank
    {"ipa": "/ˈmɛmbər bæŋk/", "vi": "ngân hàng thành viên của hệ thống", "pos": "phrase"},
    # 3063: middle east
    {"ipa": "/ˈmɪdəl iːst/", "vi": "khu vực Trung Đông nhiều dầu mỏ", "pos": "phrase"},
    # 3064: movie industry
    {"ipa": "/ˈmuːvi ˈɪndəstri/", "vi": "ngành công nghiệp phim ảnh điện ảnh", "pos": "phrase"},
    # 3065: movie star
    {"ipa": "/ˈmuːvi stɑːr/", "vi": "ngôi sao điện ảnh; minh tinh bạc", "pos": "phrase"},
    # 3066: name calling
    {"ipa": "/neɪm ˈkɔːlɪŋ/", "vi": "thói chửi bới lăng mạ sỉ nhục", "pos": "phrase"},
    # 3067: natural action
    {"ipa": "/ˈnætʃərəl ˈækʃən/", "vi": "tác động của quy luật tự nhiên", "pos": "phrase"},
    # 3068: news conference
    {"ipa": "/nuːz ˈkɑːnfərəns/", "vi": "buổi họp báo công bố thông tin tức", "pos": "phrase"},
    # 3069: old master
    {"ipa": "/oʊld ˈmæstər/", "vi": "danh họa bậc thầy thời xưa châu Âu", "pos": "phrase"},
    # 3070: on camera
    {"ipa": "/ɑːn ˈkæmərə/", "vi": "xuất hiện trước ống kính máy quay", "pos": "phrase"},
    # 3071: on trial
    {"ipa": "/ɑːn ˈtraɪəl/", "vi": "đang bị xét xử; đang thử nghiệm", "pos": "phrase"},
    # 3072: organization man
    {"ipa": "/ˌɔːrɡənəˈzeɪʃən mæn/", "vi": "kẻ tuân phục mù quáng vì tổ chức", "pos": "phrase"},
    # 3073: peace of mind
    {"ipa": "/piːs ʌv maɪnd/", "vi": "sự an tâm thanh thản trong tâm hồn", "pos": "phrase"},
    # 3074: personal relationship
    {"ipa": "/ˈpɜːrsənəl rɪˈleɪʃənʃɪp/", "vi": "mối quan hệ cá nhân riêng tư", "pos": "phrase"},
    # 3075: peter out
    {"ipa": "/ˈpiːtər aʊt/", "vi": "lụi tàn dần rồi tắt hẳn; cạn dần", "pos": "phrase"},
    # 3076: playing card
    {"ipa": "/ˈpleɪɪŋ kɑːrd/", "vi": "lá bài tây 52 lá chơi bài giải trí", "pos": "phrase"},
    # 3077: pop in
    {"ipa": "/pɑːp ɪn/", "vi": "tạt vào ghé thăm chốc lát qua nhà", "pos": "phrase"},
    # 3078: question mark
    {"ipa": "/ˈkwɛstʃən mɑːrk/", "vi": "dấu chấm hỏi câu; mối hoài nghi lớn", "pos": "phrase"},
    # 3079: radio news
    {"ipa": "/ˈreɪdioʊ nuːz/", "vi": "bản tin phát thanh trên sóng đài", "pos": "phrase"},
    # 3080: red sea
    {"ipa": "/rɛd siː/", "vi": "vùng Biển Đỏ Hồng Hải giữa Phi và Á", "pos": "phrase"},
    # 3081: rock bit
    {"ipa": "/rɑːk bɪt/", "vi": "mũi khoan đá cứng giếng khoan dầu", "pos": "phrase"},
    # 3082: role player
    {"ipa": "/roʊl ˈpleɪər/", "vi": "cầu thủ sắm vai phụ chuyên biệt", "pos": "phrase"},
    # 3083: sales talk
    {"ipa": "/seɪlz tɔːk/", "vi": "lời chào mời mua hàng khéo léo ngọt", "pos": "phrase"},
    # 3084: security director
    {"ipa": "/sɪˈkjʊrəti dəˈrɛktər/", "vi": "giám đốc phụ trách công tác an ninh", "pos": "phrase"},
    # 3085: set gun
    {"ipa": "/sɛt ɡʌn/", "vi": "khẩu súng bẫy thú nối dây kích hỏa", "pos": "phrase"},
    # 3086: sex drive
    {"ipa": "/sɛks draɪv/", "vi": "nhu cầu ham muốn tình dục sinh lý", "pos": "phrase"},
    # 3087: shop at
    {"ipa": "/ʃɑːp æt/", "vi": "thường xuyên mua sắm tại cửa hàng", "pos": "phrase"},
    # 3088: short sleep
    {"ipa": "/ʃɔːrt sliːp/", "vi": "giấc chợp mắt ngắn ngủi nghỉ trưa", "pos": "phrase"},
    # 3089: sit back
    {"ipa": "/sɪt bæk/", "vi": "ngả lưng thư giãn; ngồi chờ đợi", "pos": "phrase"},
    # 3090: sleep late
    {"ipa": "/sliːp leɪt/", "vi": "ngủ nướng dậy muộn vào buổi sáng", "pos": "phrase"},
    # 3091: social station
    {"ipa": "/ˈsoʊʃəl ˈsteɪʃən/", "vi": "địa vị xã hội; tầng lớp xã hội", "pos": "phrase"},
    # 3092: sound film
    {"ipa": "/saʊnd fɪlm/", "vi": "bộ phim điện ảnh có âm thanh tiếng", "pos": "phrase"},
    # 3093: street sign
    {"ipa": "/striːt saɪn/", "vi": "biển tên phố; biển chỉ dẫn đường đi", "pos": "phrase"},
    # 3094: sun god
    {"ipa": "/sʌn ɡɑːd/", "vi": "thần mặt trời thái dương thần linh", "pos": "phrase"},
    # 3095: sunday best
    {"ipa": "/ˈsʌndeɪ bɛst/", "vi": "bộ đồ tươm tất diện đi lễ nhà thờ", "pos": "phrase"},
    # 3096: table saw
    {"ipa": "/ˈteɪbəl sɔː/", "vi": "máy cưa đĩa bàn gia công mộc gỗ", "pos": "phrase"},
    # 3097: touch down
    {"ipa": "/tʌtʃ daʊn/", "vi": "hạ cánh đáp đất; ghi điểm chạm gôn", "pos": "phrase"},
    # 3098: touch off
    {"ipa": "/tʌtʃ ɔːf/", "vi": "châm ngòi nổ; khơi mào xung đột lớn", "pos": "phrase"},
    # 3099: train of thought
    {"ipa": "/treɪn ʌv θɔːt/", "vi": "mạch suy nghĩ tuôn trào liền mạch", "pos": "phrase"},
]

with open('scratch/b21_r07_raw_p1.json') as f:
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

with open('scratch/b21_r07_p1.json', 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("b21_r07_p1.json created successfully and validated!")
