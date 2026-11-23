import json

# Manual word-by-word cognitive review for Batch 21 Round 3 Part 2 (records 1100-1199, IDs 200k.001102 to 200k.001201)
reviewed_entries = [
    # 1100: account for
    {"ipa": "/əˈkaʊnt fɔːr/", "vi": "giải thích cho; chiếm tỷ lệ", "pos": "phrase"},
    # 1101: age of man
    {"ipa": "/eɪdʒ ʌv mæn/", "vi": "thời đại loài người; kỷ nhân loại", "pos": "phrase"},
    # 1102: bring back
    {"ipa": "/brɪŋ bæk/", "vi": "mang trả lại; gợi nhớ lại kỷ niệm", "pos": "phrase"},
    # 1103: business news
    {"ipa": "/ˈbɪznəs nuːz/", "vi": "tin tức kinh doanh; tin tài chính", "pos": "phrase"},
    # 1104: call to order
    {"ipa": "/kɔːl tuː ˈɔːrdər/", "vi": "tuyên bố khai mạc phiên họp", "pos": "phrase"},
    # 1105: car care
    {"ipa": "/kɑːr kɛr/", "vi": "dịch vụ chăm sóc xe hơi", "pos": "phrase"},
    # 1106: case law
    {"ipa": "/keɪs lɔː/", "vi": "án lệ pháp luật; luật án lệ", "pos": "phrase"},
    # 1107: come short
    {"ipa": "/kʌm ʃɔːrt/", "vi": "thiếu hụt; không đạt kỳ vọng", "pos": "phrase"},
    # 1108: come to light
    {"ipa": "/kʌm tuː laɪt/", "vi": "được phơi bày ra ánh sáng; lộ ra", "pos": "phrase"},
    # 1109: country music
    {"ipa": "/ˈkʌntri ˈmjuːzɪk/", "vi": "dòng nhạc đồng quê nước Mỹ", "pos": "phrase"},
    # 1110: date from
    {"ipa": "/deɪt frʌm/", "vi": "có niên đại từ; bắt nguồn từ", "pos": "phrase"},
    # 1111: easy going
    {"ipa": "/ˈiːzi ˈɡoʊɪŋ/", "vi": "dễ tính ung dung; tiến triển êm", "pos": "phrase"},
    # 1112: end matter
    {"ipa": "/ɛnd ˈmætər/", "vi": "phần phụ lục tài liệu cuối sách", "pos": "phrase"},
    # 1113: family history
    {"ipa": "/ˈfæməli ˈhɪstəri/", "vi": "tiền sử bệnh gia đình; gia phả", "pos": "phrase"},
    # 1114: family room
    {"ipa": "/ˈfæməli ruːm/", "vi": "phòng sinh hoạt chung gia đình", "pos": "phrase"},
    # 1115: force out
    {"ipa": "/fɔːrs aʊt/", "vi": "ép buộc thôi việc; loại cầu thủ ép", "pos": "phrase"},
    # 1116: free hand
    {"ipa": "/friː hænd/", "vi": "toàn quyền tự quyết hành động", "pos": "phrase"},
    # 1117: full general
    {"ipa": "/fʊl ˈdʒɛnərəl/", "vi": "đại tướng bốn sao lục quân", "pos": "phrase"},
    # 1118: given name
    {"ipa": "/ˈɡɪvən neɪm/", "vi": "tên chính; tên gọi khai sinh", "pos": "phrase"},
    # 1119: good word
    {"ipa": "/ɡʊd wɜːrd/", "vi": "lời khen ngợi; lời nói tốt tiến cử", "pos": "phrase"},
    # 1120: health care
    {"ipa": "/hɛlθ kɛr/", "vi": "chăm sóc sức khỏe y tế", "pos": "phrase"},
    # 1121: hear out
    {"ipa": "/hɪr aʊt/", "vi": "lắng nghe hết đầu đuôi câu chuyện", "pos": "phrase"},
    # 1122: house of york
    {"ipa": "/haʊs ʌv jɔːrk/", "vi": "vương tộc York nước Anh", "pos": "phrase"},
    # 1123: in common
    {"ipa": "/ɪn ˈkɑːmən/", "vi": "có điểm chung; cùng chia sẻ", "pos": "phrase"},
    # 1124: in other words
    {"ipa": "/ɪn ˈʌðər wɜːrdz/", "vi": "nói cách khác; hay nói đúng hơn", "pos": "phrase"},
    # 1125: in the lead
    {"ipa": "/ɪn ðə liːd/", "vi": "dẫn đầu cuộc đua; đứng ở vị trí đầu", "pos": "phrase"},
    # 1126: left hand
    {"ipa": "/lɛft hænd/", "vi": "bàn tay trái; phía bên tay trái", "pos": "phrase"},
    # 1127: live together
    {"ipa": "/lɪv təˈɡɛðər/", "vi": "sống chung với nhau; chung sống", "pos": "phrase"},
    # 1128: market day
    {"ipa": "/ˈmɑːrkɪt deɪ/", "vi": "ngày họp phiên chợ quê", "pos": "phrase"},
    # 1129: national service
    {"ipa": "/ˈnæʃənəl ˈsɜːrvɪs/", "vi": "chế độ nghĩa vụ quân sự quốc gia", "pos": "phrase"},
    # 1130: new town
    {"ipa": "/nuː taʊn/", "vi": "khu đô thị mới quy hoạch", "pos": "phrase"},
    # 1131: next friend
    {"ipa": "/nɛkst frɛnd/", "vi": "người đại diện tố tụng pháp lý", "pos": "phrase"},
    # 1132: night court
    {"ipa": "/naɪt kɔːrt/", "vi": "phiên tòa xét xử ban đêm", "pos": "phrase"},
    # 1133: old woman
    {"ipa": "/oʊld ˈwʊmən/", "vi": "bà lão; người phụ nữ cao tuổi", "pos": "phrase"},
    # 1134: one shot
    {"ipa": "/wʌn ʃɑːt/", "vi": "chỉ dùng một lần; phát đạn duy nhất", "pos": "phrase"},
    # 1135: played out
    {"ipa": "/pleɪd aʊt/", "vi": "kiệt sức mệt lử; hết thời", "pos": "phrase"},
    # 1136: police state
    {"ipa": "/pəˈliːs steɪt/", "vi": "chế độ nhà nước cảnh sát trị", "pos": "phrase"},
    # 1137: power line
    {"ipa": "/ˈpaʊər laɪn/", "vi": "đường dây tải điện", "pos": "phrase"},
    # 1138: power service
    {"ipa": "/ˈpaʊər ˈsɜːrvɪs/", "vi": "dịch vụ cấp điện sinh hoạt", "pos": "phrase"},
    # 1139: red man
    {"ipa": "/rɛd mæn/", "vi": "người thổ dân da đỏ châu Mỹ", "pos": "phrase"},
    # 1140: second coming
    {"ipa": "/ˈsɛkənd ˈkʌmɪŋ/", "vi": "sự tái lâm của Chúa Kitô", "pos": "phrase"},
    # 1141: second half
    {"ipa": "/ˈsɛkənd hæf/", "vi": "hiệp thi đấu thứ hai; nửa sau", "pos": "phrase"},
    # 1142: second hand
    {"ipa": "/ˈsɛkənd hænd/", "vi": "đồ dùng đã qua tay; kim giây", "pos": "phrase"},
    # 1143: service call
    {"ipa": "/ˈsɜːrvɪs kɔːl/", "vi": "chuyến đến nhà sửa chữa bảo dưỡng", "pos": "phrase"},
    # 1144: stop order
    {"ipa": "/stɑːp ˈɔːrdər/", "vi": "lệnh dừng giao dịch; lệnh cắt lỗ", "pos": "phrase"},
    # 1145: water line
    {"ipa": "/ˈwɔːtər laɪn/", "vi": "đường mớn nước thân tàu", "pos": "phrase"},
    # 1146: week after week
    {"ipa": "/wiːk ˈæftər wiːk/", "vi": "tuần này qua tuần khác liên miên", "pos": "phrase"},
    # 1147: white line
    {"ipa": "/waɪt laɪn/", "vi": "vạch sơn trắng kẻ đường xe", "pos": "phrase"},
    # 1148: work of art
    {"ipa": "/wɜːrk ʌv ɑːrt/", "vi": "tác phẩm nghệ thuật tuyệt mỹ", "pos": "phrase"},
    # 1149: working group
    {"ipa": "/ˈwɜːrkɪŋ ɡruːp/", "vi": "tổ công tác chuyên môn; nhóm dự án", "pos": "phrase"},
    # 1150: working person
    {"ipa": "/ˈwɜːrkɪŋ ˈpɜːrsən/", "vi": "người lao động; công nhân viên", "pos": "phrase"},
    # 1151: american party
    {"ipa": "/əˈmɛrɪkən ˈpɑːrti/", "vi": "Đảng Người Mỹ thế kỷ 19", "pos": "phrase"},
    # 1152: black music
    {"ipa": "/blæk ˈmjuːzɪk/", "vi": "nhạc của người da đen; nhạc da màu", "pos": "phrase"},
    # 1153: come of age
    {"ipa": "/kʌm ʌv eɪdʒ/", "vi": "bước vào tuổi trưởng thành", "pos": "phrase"},
    # 1154: food company
    {"ipa": "/fuːd ˈkʌmpəni/", "vi": "công ty chế biến thực phẩm", "pos": "phrase"},
    # 1155: high and low
    {"ipa": "/haɪ ænd loʊ/", "vi": "khắp mọi nơi chốn; đủ mọi tầng lớp", "pos": "phrase"},
    # 1156: hold in
    {"ipa": "/hoʊld ɪn/", "vi": "kìm nén cảm xúc; nhịn lại", "pos": "phrase"},
    # 1157: important person
    {"ipa": "/ɪmˈpɔːrtənt ˈpɜːrsən/", "vi": "nhân vật quan trọng; người có quyền", "pos": "phrase"},
    # 1158: in common with
    {"ipa": "/ɪn ˈkɑːmən wɪð/", "vi": "cũng tương tự như; giống như", "pos": "phrase"},
    # 1159: in private
    {"ipa": "/ɪn ˈpraɪvət/", "vi": "nơi kín đáo riêng tư; bí mật", "pos": "phrase"},
    # 1160: in return
    {"ipa": "/ɪn rɪˈtɜːrn/", "vi": "để đáp lại; đổi lại điều gì", "pos": "phrase"},
    # 1161: information system
    {"ipa": "/ˌɪnfərˈmeɪʃən ˈsɪstəm/", "vi": "hệ thống thông tin điện toán", "pos": "phrase"},
    # 1162: land up
    {"ipa": "/lænd ʌp/", "vi": "rốt cuộc kết cục rơi vào tình cảnh", "pos": "phrase"},
    # 1163: large number
    {"ipa": "/lɑːrdʒ ˈnʌmbər/", "vi": "số lượng đông đảo; con số lớn", "pos": "phrase"},
    # 1164: lead on
    {"ipa": "/liːd ɑːn/", "vi": "dẫn đường; gieo hy vọng hão huyền", "pos": "phrase"},
    # 1165: local government
    {"ipa": "/ˈloʊkəl ˈɡʌvərmənt/", "vi": "chính quyền địa phương các cấp", "pos": "phrase"},
    # 1166: new york state
    {"ipa": "/nuː jɔːrk steɪt/", "vi": "tiểu bang New York của Mỹ", "pos": "phrase"},
    # 1167: party line
    {"ipa": "/ˈpɑːrti laɪn/", "vi": "đường lối chính sách của đảng phái", "pos": "phrase"},
    # 1168: power law
    {"ipa": "/ˈpaʊər lɔː/", "vi": "định luật hàm lũy thừa trong toán", "pos": "phrase"},
    # 1169: running time
    {"ipa": "/ˈrʌnɪŋ taɪm/", "vi": "thời lượng phát sóng; độ dài phim", "pos": "phrase"},
    # 1170: service line
    {"ipa": "/ˈsɜːrvɪs laɪn/", "vi": "vạch giao bóng trên sân đấu", "pos": "phrase"},
    # 1171: sex up
    {"ipa": "/sɛks ʌp/", "vi": "làm cho khêu gợi; thổi phồng tin", "pos": "phrase"},
    # 1172: side order
    {"ipa": "/saɪd ˈɔːrdər/", "vi": "món ăn gọi thêm gọi kèm", "pos": "phrase"},
    # 1173: social group
    {"ipa": "/ˈsoʊʃəl ɡruːp/", "vi": "nhóm xã hội; cộng đồng xã hội", "pos": "phrase"},
    # 1174: states general
    {"ipa": "/steɪts ˈdʒɛnərəl/", "vi": "Hội nghị các đẳng cấp; quốc hội", "pos": "phrase"},
    # 1175: take it easy
    {"ipa": "/teɪk ɪt ˈiːzi/", "vi": "bình tĩnh thư giãn; đừng quá lo", "pos": "phrase"},
    # 1176: turn around
    {"ipa": "/tɜːrn əˈraʊnd/", "vi": "xoay chuyển tình thế; quay lại nhìn", "pos": "phrase"},
    # 1177: united states
    {"ipa": "/juːˈnaɪtɪd steɪts/", "vi": "Hợp chúng quốc Hoa Kỳ; nước Mỹ", "pos": "phrase"},
    # 1178: up to date
    {"ipa": "/ʌp tuː deɪt/", "vi": "cập nhật mới nhất; hợp thời đại", "pos": "phrase"},
    # 1179: war power
    {"ipa": "/wɔːr ˈpaʊər/", "vi": "quyền ban bố tình trạng chiến tranh", "pos": "phrase"},
    # 1180: says
    {"ipa": "/sɛz/", "vi": "quyền phát biểu; những lời nói ra", "pos": "noun"},
    # 1181: worlds
    {"ipa": "/wɜːrldz/", "vi": "các thế giới; những cõi đời", "pos": "noun"},
    # 1182: above all
    {"ipa": "/əˈbʌv ɔːl/", "vi": "quan trọng hơn hết; trên tất cả", "pos": "phrase"},
    # 1183: black and white
    {"ipa": "/blæk ænd waɪt/", "vi": "trắng đen rõ ràng; đen trắng", "pos": "phrase"},
    # 1184: break in
    {"ipa": "/breɪk ɪn/", "vi": "đột nhập trái phép; thuần hóa ngựa", "pos": "phrase"},
    # 1185: bring down
    {"ipa": "/brɪŋ daʊn/", "vi": "lật đổ chế độ; hạ gục; làm giảm giá", "pos": "phrase"},
    # 1186: bring off
    {"ipa": "/brɪŋ ɔːf/", "vi": "đạt được thành công ngoạn mục", "pos": "phrase"},
    # 1187: by rights
    {"ipa": "/baɪ raɪts/", "vi": "theo đúng lẽ công bằng; đáng ra", "pos": "phrase"},
    # 1188: center on
    {"ipa": "/ˈsɛntər ɑːn/", "vi": "xoay quanh tâm điểm; tập trung vào", "pos": "phrase"},
    # 1189: change course
    {"ipa": "/tʃeɪndʒ kɔːrs/", "vi": "thay đổi lộ trình; chuyển hướng đi", "pos": "phrase"},
    # 1190: change of course
    {"ipa": "/tʃeɪndʒ ʌv kɔːrs/", "vi": "sự thay đổi hướng đi; đổi lộ trình", "pos": "phrase"},
    # 1191: city room
    {"ipa": "/ˈsɪti ruːm/", "vi": "phòng biên tập tin tức tòa soạn báo", "pos": "phrase"},
    # 1192: city university
    {"ipa": "/ˈsɪti ˌjuːnɪˈvɜːrsɪti/", "vi": "trường đại học thuộc thành phố", "pos": "phrase"},
    # 1193: couple on
    {"ipa": "/ˈkʌpəl ɑːn/", "vi": "móc nối ghép toa xe lửa", "pos": "phrase"},
    # 1194: cut back
    {"ipa": "/kʌt bæk/", "vi": "cắt giảm chi tiêu ngân sách", "pos": "phrase"},
    # 1195: cut into
    {"ipa": "/kʌt ˈɪntuː/", "vi": "cắt lạm vào; ngắt lời chen ngang", "pos": "phrase"},
    # 1196: even chance
    {"ipa": "/ˈiːvən tʃæns/", "vi": "cơ hội ngang ngửa năm mươi năm mươi", "pos": "phrase"},
    # 1197: face the music
    {"ipa": "/feɪs ðə ˈmjuːzɪk/", "vi": "dũng cảm chấp nhận chịu trận", "pos": "phrase"},
    # 1198: first moment
    {"ipa": "/fɜːrst ˈmoʊmənt/", "vi": "mô-men quán tính cấp một trong toán", "pos": "phrase"},
    # 1199: food for thought
    {"ipa": "/fuːd fɔːr θɔːt/", "vi": "điều đáng suy ngẫm; điều trăn trở", "pos": "phrase"},
]

with open('scratch/b21_r03_raw_p2.json') as f:
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

with open('scratch/b21_r03_p2.json', 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("b21_r03_p2.json created successfully and validated!")
