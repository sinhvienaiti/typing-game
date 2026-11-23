import json

# Manual word-by-word cognitive review for Batch 21 Round 3 Part 4 (records 1300-1399, IDs 200k.001302 to 200k.001401)
reviewed_entries = [
    # 1300: day of rest
    {"ipa": "/deɪ ʌv rɛst/", "vi": "ngày nghỉ ngơi an tĩnh; ngày Sa-bát", "pos": "phrase"},
    # 1301: down town
    {"ipa": "/daʊn taʊn/", "vi": "trung tâm thành phố; phố xá sầm uất", "pos": "phrase"},
    # 1302: english people
    {"ipa": "/ˈɪŋɡlɪʃ ˈpiːpəl/", "vi": "người dân nước Anh", "pos": "phrase"},
    # 1303: face to face
    {"ipa": "/feɪs tuː feɪs/", "vi": "trực tiếp đối mặt; giáp mặt", "pos": "phrase"},
    # 1304: fight off
    {"ipa": "/faɪt ɔːf/", "vi": "đánh đuổi cản phá; chống chọi bệnh", "pos": "phrase"},
    # 1305: film over
    {"ipa": "/fɪlm ˈoʊvər/", "vi": "bị phủ màng mờ; mắt đờ đẫn", "pos": "phrase"},
    # 1306: form family
    {"ipa": "/fɔːrm ˈfæməli/", "vi": "họ hình thái thực vật", "pos": "phrase"},
    # 1307: game plan
    {"ipa": "/ɡeɪm plæn/", "vi": "kế hoạch chiến thuật hành động", "pos": "phrase"},
    # 1308: get hold of
    {"ipa": "/ɡɛt hoʊld ʌv/", "vi": "nắm bắt được; liên lạc tìm được ai", "pos": "phrase"},
    # 1309: great mother
    {"ipa": "/ɡreɪt ˈmʌðər/", "vi": "nữ thần mẹ thiên nhiên vĩ đại", "pos": "phrase"},
    # 1310: hand job
    {"ipa": "/ˈhænd dʒɑːb/", "vi": "kích thích tình dục bằng tay", "pos": "phrase"},
    # 1311: hand line
    {"ipa": "/hænd laɪn/", "vi": "dây câu cá bằng tay", "pos": "phrase"},
    # 1312: high street
    {"ipa": "/haɪ striːt/", "vi": "phố mua sắm chính của thị trấn", "pos": "phrase"},
    # 1313: home study
    {"ipa": "/hoʊm ˈstʌdi/", "vi": "khóa tự học tại nhà; thẩm tra nhà", "pos": "phrase"},
    # 1314: international system
    {"ipa": "/ˌɪntərˈnæʃənəl ˈsɪstəm/", "vi": "hệ đo lường quốc tế chuẩn", "pos": "phrase"},
    # 1315: job control
    {"ipa": "/dʒɑːb kənˈtroʊl/", "vi": "điều khiển quản lý tác vụ tin học", "pos": "phrase"},
    # 1316: large white
    {"ipa": "/lɑːrdʒ waɪt/", "vi": "loài bướm trắng lớn bắp cải", "pos": "phrase"},
    # 1317: light second
    {"ipa": "/laɪt ˈsɛkənd/", "vi": "giây ánh sáng trong thiên văn", "pos": "phrase"},
    # 1318: line single
    {"ipa": "/laɪn ˈsɪŋɡəl/", "vi": "cú đánh bóng căng ăn một điểm", "pos": "phrase"},
    # 1319: market place
    {"ipa": "/ˈmɑːrkɪt pleɪs/", "vi": "thương trường buôn bán; chợ phố", "pos": "phrase"},
    # 1320: most especially
    {"ipa": "/moʊst ɪˈspɛʃəli/", "vi": "đặc biệt hơn cả; trên hết mọi điều", "pos": "phrase"},
    # 1321: near thing
    {"ipa": "/nɪr θɪŋ/", "vi": "phen suýt chết; tình thế hiểm nghèo", "pos": "phrase"},
    # 1322: night watch
    {"ipa": "/naɪt wɑːtʃ/", "vi": "phiên gác đêm; lực lượng tuần đêm", "pos": "phrase"},
    # 1323: on average
    {"ipa": "/ɑːn ˈævərɪdʒ/", "vi": "tính trung bình; thông thường", "pos": "phrase"},
    # 1324: on the average
    {"ipa": "/ɑːn ðə ˈævərɪdʒ/", "vi": "tính theo mức bình quân", "pos": "phrase"},
    # 1325: past times
    {"ipa": "/pæst taɪmz/", "vi": "thời gian đã trôi qua; dĩ vãng", "pos": "phrase"},
    # 1326: press on
    {"ipa": "/prɛs ɑːn/", "vi": "kiên quyết tiến bước về phía trước", "pos": "phrase"},
    # 1327: saw set
    {"ipa": "/sɔː sɛt/", "vi": "kìm uốn chỉnh răng cưa xẻ gỗ", "pos": "phrase"},
    # 1328: second world war
    {"ipa": "/ˈsɛkənd wɜːrld wɔːr/", "vi": "Chiến tranh thế giới thứ hai", "pos": "phrase"},
    # 1329: small hours
    {"ipa": "/smɔːl ˈaʊərz/", "vi": "lúc canh khuya; nửa đêm về sáng", "pos": "phrase"},
    # 1330: social season
    {"ipa": "/ˈsoʊʃəl ˈsiːzən/", "vi": "mùa dạ hội tiệc tùng của giới quý", "pos": "phrase"},
    # 1331: social service
    {"ipa": "/ˈsoʊʃəl ˈsɜːrvɪs/", "vi": "dịch vụ trợ giúp xã hội; từ thiện", "pos": "phrase"},
    # 1332: south side
    {"ipa": "/saʊθ saɪd/", "vi": "phía mạn nam; khu bờ phía nam", "pos": "phrase"},
    # 1333: stay away
    {"ipa": "/steɪ əˈweɪ/", "vi": "ở xa ra; tránh xa không dính líu", "pos": "phrase"},
    # 1334: take issue
    {"ipa": "/teɪk ˈɪʃuː/", "vi": "bày tỏ bất đồng; phản bác quan điểm", "pos": "phrase"},
    # 1335: watch night
    {"ipa": "/wɑːtʃ naɪt/", "vi": "lễ canh thức đêm giao thừa", "pos": "phrase"},
    # 1336: white room
    {"ipa": "/waɪt ruːm/", "vi": "phòng thí nghiệm sạch vô trùng", "pos": "phrase"},
    # 1337: air power
    {"ipa": "/ɛr ˈpaʊər/", "vi": "sức mạnh không lực quân sự", "pos": "phrase"},
    # 1338: black book
    {"ipa": "/blæk bʊk/", "vi": "sổ đen ghi danh sách trừng phạt", "pos": "phrase"},
    # 1339: british people
    {"ipa": "/ˈbrɪtɪʃ ˈpiːpəl/", "vi": "người dân Vương quốc Anh", "pos": "phrase"},
    # 1340: business community
    {"ipa": "/ˈbɪznəs kəˈmjuːnəti/", "vi": "cộng đồng doanh nghiệp; giới làm ăn", "pos": "phrase"},
    # 1341: call girl
    {"ipa": "/kɔːl ɡɜːrl/", "vi": "gái gọi cao cấp; gái bán hoa", "pos": "phrase"},
    # 1342: city of light
    {"ipa": "/ˈsɪti ʌv laɪt/", "vi": "kinh đô ánh sáng Paris", "pos": "phrase"},
    # 1343: close support
    {"ipa": "/kloʊs səˈpɔːrt/", "vi": "chi viện trực tiếp tầm gần quân sự", "pos": "phrase"},
    # 1344: come across
    {"ipa": "/kʌm əˈkrɔːs/", "vi": "tình cờ gặp gỡ; tạo ấn tượng", "pos": "phrase"},
    # 1345: cool it
    {"ipa": "/kuːl ɪt/", "vi": "hãy bình tĩnh lại; bớt nóng nảy", "pos": "phrase"},
    # 1346: data system
    {"ipa": "/ˈdeɪtə ˈsɪstəm/", "vi": "hệ thống xử lý lưu trữ dữ liệu", "pos": "phrase"},
    # 1347: due care
    {"ipa": "/djuː kɛr/", "vi": "sự cẩn trọng đúng mức theo luật", "pos": "phrase"},
    # 1348: fight down
    {"ipa": "/faɪt daʊn/", "vi": "kìm nén cảm xúc; dập tắt nổi loạn", "pos": "phrase"},
    # 1349: free form
    {"ipa": "/friː fɔːrm/", "vi": "tự do phóng khoáng; không gò bó", "pos": "phrase"},
    # 1350: good sense
    {"ipa": "/ɡʊd sɛns/", "vi": "lương tri lành mạnh; óc phán đoán", "pos": "phrase"},
    # 1351: hold over
    {"ipa": "/hoʊld ˈoʊvər/", "vi": "hoãn lại; tiếp tục chiếu rạp thêm", "pos": "phrase"},
    # 1352: hot up
    {"ipa": "/hɑːt ʌp/", "vi": "trở nên sôi nổi gay cấn; hâm nóng", "pos": "phrase"},
    # 1353: in evidence
    {"ipa": "/ɪn ˈɛvədəns/", "vi": "hiện diện rõ ràng; dễ thấy ngay", "pos": "phrase"},
    # 1354: large order
    {"ipa": "/lɑːrdʒ ˈɔːrdər/", "vi": "đơn hàng lớn; nhiệm vụ cam go", "pos": "phrase"},
    # 1355: life force
    {"ipa": "/laɪf fɔːrs/", "vi": "nguồn sinh lực; năng lượng sống", "pos": "phrase"},
    # 1356: light company
    {"ipa": "/laɪt ˈkʌmpəni/", "vi": "công ty cấp điện thắp sáng", "pos": "phrase"},
    # 1357: line of control
    {"ipa": "/laɪn ʌv kənˈtroʊl/", "vi": "đường ranh giới kiểm soát thực tế", "pos": "phrase"},
    # 1358: look across
    {"ipa": "/lʊk əˈkrɔːs/", "vi": "nhìn sang phía đối diện; trông sang", "pos": "phrase"},
    # 1359: make sense
    {"ipa": "/meɪk sɛns/", "vi": "hợp tình hợp lý; có ý nghĩa rõ ràng", "pos": "phrase"},
    # 1360: man of action
    {"ipa": "/mæn ʌv ˈækʃən/", "vi": "con người của hành động quả quyết", "pos": "phrase"},
    # 1361: new york city
    {"ipa": "/nuː jɔːrk ˈsɪti/", "vi": "thành phố New York sầm uất", "pos": "phrase"},
    # 1362: news story
    {"ipa": "/nuːz ˈstɔːri/", "vi": "bản tin báo chí; phóng sự thời sự", "pos": "phrase"},
    # 1363: south american
    {"ipa": "/saʊθ əˈmɛrɪkən/", "vi": "thuộc về lục địa Nam Mỹ", "pos": "phrase"},
    # 1364: stand in
    {"ipa": "/stænd ɪn/", "vi": "đóng thế vai; làm người thay thế", "pos": "phrase"},
    # 1365: turn away
    {"ipa": "/tɜːrn əˈweɪ/", "vi": "quay mặt đi; từ chối tiếp nhận", "pos": "phrase"},
    # 1366: two weeks
    {"ipa": "/tuː wiːks/", "vi": "khoảng thời gian hai tuần lễ", "pos": "phrase"},
    # 1367: west end
    {"ipa": "/wɛst ɛnd/", "vi": "khu kịch nghệ West End Luân Đôn", "pos": "phrase"},
    # 1368: white matter
    {"ipa": "/waɪt ˈmætər/", "vi": "chất trắng trong hệ thần kinh não", "pos": "phrase"},
    # 1369: worked up
    {"ipa": "/wɜːrkt ʌp/", "vi": "bị kích động; hồi hộp lo âu", "pos": "phrase"},
    # 1370: besting
    {"ipa": "/ˈbɛstɪŋ/", "vi": "chiến thắng đối thủ; đánh bại", "pos": "verb"},
    # 1371: bests
    {"ipa": "/bɛsts/", "vi": "những nỗ lực tột bậc; kỷ lục tốt", "pos": "noun"},
    # 1372: age group
    {"ipa": "/eɪdʒ ɡruːp/", "vi": "nhóm lứa tuổi; độ tuổi chung", "pos": "phrase"},
    # 1373: average out
    {"ipa": "/ˈævərɪdʒ aʊt/", "vi": "tính ra mức bình quân chung", "pos": "phrase"},
    # 1374: black body
    {"ipa": "/blæk ˈbɑːdi/", "vi": "vật đen tuyệt đối trong vật lý", "pos": "phrase"},
    # 1375: black death
    {"ipa": "/blæk dɛθ/", "vi": "Đại dịch Cái Chết Đen thế kỷ 14", "pos": "phrase"},
    # 1376: black hand
    {"ipa": "/blæk hænd/", "vi": "tổ chức bí mật Bàn Tay Đen", "pos": "phrase"},
    # 1377: break into
    {"ipa": "/breɪk ˈɪntuː/", "vi": "đột nhập; bất chợt bật khóc cười", "pos": "phrase"},
    # 1378: close call
    {"ipa": "/kloʊs kɔːl/", "vi": "phen thoát chết trong gang tấc", "pos": "phrase"},
    # 1379: coming together
    {"ipa": "/ˈkʌmɪŋ təˈɡɛðər/", "vi": "sự quy tụ; sự đoàn tụ sum vầy", "pos": "phrase"},
    # 1380: common year
    {"ipa": "/ˈkɑːmən jɪr/", "vi": "năm thường có 365 ngày", "pos": "phrase"},
    # 1381: court of law
    {"ipa": "/kɔːrt ʌv lɔː/", "vi": "tòa án pháp luật tài phán", "pos": "phrase"},
    # 1382: data point
    {"ipa": "/ˈdeɪtə pɔɪnt/", "vi": "điểm số liệu cụ thể trong tập dữ", "pos": "phrase"},
    # 1383: drive in
    {"ipa": "/draɪv ɪn/", "vi": "rạp chiếu phim ngoài trời ngồi xe", "pos": "phrase"},
    # 1384: easy money
    {"ipa": "/ˈiːzi ˈmʌni/", "vi": "tiền kiếm dễ dàng; tiền phi pháp", "pos": "phrase"},
    # 1385: eat in
    {"ipa": "/iːt ɪn/", "vi": "dùng bữa ở nhà; ăn tại quán", "pos": "phrase"},
    # 1386: fall in
    {"ipa": "/fɔːl ɪn/", "vi": "sụp đổ sập xuống; tập hợp hàng ngũ", "pos": "phrase"},
    # 1387: free living
    {"ipa": "/friː ˈlɪvɪŋ/", "vi": "lối sống tự do phóng khoáng", "pos": "phrase"},
    # 1388: front end
    {"ipa": "/frʌnt ɛnd/", "vi": "giao diện người dùng; phần đầu xe", "pos": "phrase"},
    # 1389: game of chance
    {"ipa": "/ɡeɪm ʌv tʃæns/", "vi": "trò chơi đỏ đen may rủi; cờ bạc", "pos": "phrase"},
    # 1390: giving up
    {"ipa": "/ˈɡɪvɪŋ ʌp/", "vi": "sự từ bỏ buông xuôi; sự chịu thua", "pos": "phrase"},
    # 1391: hold back
    {"ipa": "/hoʊld bæk/", "vi": "ngăn cản kìm chế; giấu giếm lại", "pos": "phrase"},
    # 1392: in league
    {"ipa": "/ɪn liːɡ/", "vi": "câu kết mờ ám với; liên minh cùng", "pos": "phrase"},
    # 1393: law court
    {"ipa": "/lɔː kɔːrt/", "vi": "tòa án xét xử tranh chấp", "pos": "phrase"},
    # 1394: lead off
    {"ipa": "/liːd ɔːf/", "vi": "khởi xướng mở đầu bài diễn văn", "pos": "phrase"},
    # 1395: man and wife
    {"ipa": "/mæn ænd waɪf/", "vi": "hai vợ chồng kết nghĩa sắt son", "pos": "phrase"},
    # 1396: money market
    {"ipa": "/ˈmʌni ˈmɑːrkɪt/", "vi": "thị trường vốn tiền tệ tài chính", "pos": "phrase"},
    # 1397: no longer
    {"ipa": "/noʊ ˈlɔːŋɡər/", "vi": "không còn tiếp diễn nữa", "pos": "phrase"},
    # 1398: off the record
    {"ipa": "/ɔːf ðə ˈrɛkərd/", "vi": "không chính thức; chưa được công bố", "pos": "phrase"},
    # 1399: open university
    {"ipa": "/ˈoʊpən ˌjuːnɪˈvɜːrsɪti/", "vi": "trường đại học mở giáo dục", "pos": "phrase"},
]

with open('scratch/b21_r03_raw_p4.json') as f:
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

with open('scratch/b21_r03_p4.json', 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("b21_r03_p4.json created successfully and validated!")
