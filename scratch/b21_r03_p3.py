import json

# Manual word-by-word cognitive review for Batch 21 Round 3 Part 3 (records 1200-1299, IDs 200k.001202 to 200k.001301)
reviewed_entries = [
    # 1200: go board
    {"ipa": "/ɡoʊ bɔːrd/", "vi": "bàn cờ vây", "pos": "phrase"},
    # 1201: government office
    {"ipa": "/ˈɡʌvərmənt ˈɔːfɪs/", "vi": "cơ quan công quyền; công sở", "pos": "phrase"},
    # 1202: hard news
    {"ipa": "/hɑːrd nuːz/", "vi": "tin tức thời sự chính thống", "pos": "phrase"},
    # 1203: hold on
    {"ipa": "/hoʊld ɑːn/", "vi": "giữ máy chờ; nắm chặt kiên trì", "pos": "phrase"},
    # 1204: love child
    {"ipa": "/lʌv tʃaɪld/", "vi": "con ngoài giá thú; con riêng sinh", "pos": "phrase"},
    # 1205: old age
    {"ipa": "/oʊld eɪdʒ/", "vi": "tuổi già xế chiều; cảnh tuổi già", "pos": "phrase"},
    # 1206: old line state
    {"ipa": "/oʊld laɪn steɪt/", "vi": "biệt danh bang Maryland của Mỹ", "pos": "phrase"},
    # 1207: open order
    {"ipa": "/ˈoʊpən ˈɔːrdər/", "vi": "đội hình dãn cách; lệnh mở", "pos": "phrase"},
    # 1208: play along
    {"ipa": "/pleɪ əˈlɔːŋ/", "vi": "giả vờ hùa theo; diễn kịch cùng", "pos": "phrase"},
    # 1209: public office
    {"ipa": "/ˈpʌblɪk ˈɔːfɪs/", "vi": "chức vụ công; vị trí công quyền", "pos": "phrase"},
    # 1210: side by side
    {"ipa": "/saɪd baɪ saɪd/", "vi": "kề vai sát cánh; cạnh nhau", "pos": "phrase"},
    # 1211: social system
    {"ipa": "/ˈsoʊʃəl ˈsɪstəm/", "vi": "hệ thống cơ cấu xã hội", "pos": "phrase"},
    # 1212: stay in place
    {"ipa": "/steɪ ɪn pleɪs/", "vi": "giữ nguyên tại chỗ; không xê dịch", "pos": "phrase"},
    # 1213: time period
    {"ipa": "/taɪm ˈpɪriəd/", "vi": "khoảng thời gian; niên đại thời kỳ", "pos": "phrase"},
    # 1214: view as
    {"ipa": "/vjuː æz/", "vi": "coi như là; xem xét như", "pos": "phrase"},
    # 1215: work song
    {"ipa": "/wɜːrk sɔːŋ/", "vi": "bài ca lao động tập thể", "pos": "phrase"},
    # 1216: work study
    {"ipa": "/wɜːrk ˈstʌdi/", "vi": "nghiên cứu định mức thao tác", "pos": "phrase"},
    # 1217: young person
    {"ipa": "/jʌŋ ˈpɜːrsən/", "vi": "thanh niên trẻ; người trẻ tuổi", "pos": "phrase"},
    # 1218: greats
    {"ipa": "/ɡreɪts/", "vi": "các bậc vĩ nhân; người kiệt xuất", "pos": "noun"},
    # 1219: as needed
    {"ipa": "/æz ˈniːdɪd/", "vi": "khi cần thiết; theo nhu cầu", "pos": "phrase"},
    # 1220: at any cost
    {"ipa": "/æt ˈɛni kɔːst/", "vi": "bằng mọi giá; bất chấp phí tổn", "pos": "phrase"},
    # 1221: at present
    {"ipa": "/æt ˈprɛzənt/", "vi": "vào thời điểm hiện tại; bây giờ", "pos": "phrase"},
    # 1222: break with
    {"ipa": "/breɪk wɪð/", "vi": "đoạn tuyệt với; từ bỏ thói quen cũ", "pos": "phrase"},
    # 1223: bring through
    {"ipa": "/brɪŋ θruː/", "vi": "cứu sống qua cơn nguy kịch", "pos": "phrase"},
    # 1224: business office
    {"ipa": "/ˈbɪznəs ˈɔːfɪs/", "vi": "văn phòng làm việc của doanh nghiệp", "pos": "phrase"},
    # 1225: change of mind
    {"ipa": "/tʃeɪndʒ ʌv maɪnd/", "vi": "sự thay đổi ý định; đổi ý kiến", "pos": "phrase"},
    # 1226: clear off
    {"ipa": "/klɪr ɔːf/", "vi": "dọn dẹp sạch; xéo đi chỗ khác", "pos": "phrase"},
    # 1227: come near
    {"ipa": "/kʌm nɪr/", "vi": "tiến lại gần; suýt chạm tới", "pos": "phrase"},
    # 1228: common time
    {"ipa": "/ˈkɑːmən taɪm/", "vi": "nhịp bốn bốn trong âm nhạc", "pos": "phrase"},
    # 1229: control system
    {"ipa": "/kənˈtroʊl ˈsɪstəm/", "vi": "hệ thống kiểm soát và điều khiển", "pos": "phrase"},
    # 1230: fight back
    {"ipa": "/faɪt bæk/", "vi": "phản kháng đánh trả; kìm nén lệ", "pos": "phrase"},
    # 1231: force back
    {"ipa": "/fɔːrs bæk/", "vi": "đẩy lùi quân địch; đẩy lui", "pos": "phrase"},
    # 1232: front man
    {"ipa": "/frʌnt mæn/", "vi": "hát chính; kẻ đứng mũi chịu sào", "pos": "phrase"},
    # 1233: home front
    {"ipa": "/hoʊm frʌnt/", "vi": "hậu phương thời chiến", "pos": "phrase"},
    # 1234: lead time
    {"ipa": "/liːd taɪm/", "vi": "thời gian chờ hoàn thiện đơn hàng", "pos": "phrase"},
    # 1235: lead up
    {"ipa": "/liːd ʌp/", "vi": "dẫn dắt câu chuyện tới; mở đường", "pos": "phrase"},
    # 1236: light show
    {"ipa": "/laɪt ʃoʊ/", "vi": "chương trình trình diễn ánh sáng", "pos": "phrase"},
    # 1237: local call
    {"ipa": "/ˈloʊkəl kɔːl/", "vi": "cuộc điện thoại nội hạt", "pos": "phrase"},
    # 1238: period of time
    {"ipa": "/ˈpɪriəd ʌv taɪm/", "vi": "khoảng thời gian; một chu kỳ", "pos": "phrase"},
    # 1239: right of action
    {"ipa": "/raɪt ʌv ˈækʃən/", "vi": "quyền khởi kiện tại tòa án", "pos": "phrase"},
    # 1240: running back
    {"ipa": "/ˈrʌnɪŋ bæk/", "vi": "vị trí hậu vệ chạy bóng bầu dục", "pos": "phrase"},
    # 1241: second class
    {"ipa": "/ˈsɛkənd klæs/", "vi": "vé hạng nhì; công dân hạng hai", "pos": "phrase"},
    # 1242: service area
    {"ipa": "/ˈsɜːrvɪs ˈɛriə/", "vi": "trạm dừng nghỉ đường cao tốc", "pos": "phrase"},
    # 1243: third house
    {"ipa": "/θɜːrd haʊs/", "vi": "nhóm vận động hành lang nghị viện", "pos": "phrase"},
    # 1244: war party
    {"ipa": "/wɔːr ˈpɑːrti/", "vi": "toán chiến binh viễn chinh", "pos": "phrase"},
    # 1245: white book
    {"ipa": "/waɪt bʊk/", "vi": "sách trắng chính phủ ban hành", "pos": "phrase"},
    # 1246: white hope
    {"ipa": "/waɪt hoʊp/", "vi": "ngôi sao nhiều kỳ vọng; hy vọng lớn", "pos": "phrase"},
    # 1247: working party
    {"ipa": "/ˈwɜːrkɪŋ ˈpɑːrti/", "vi": "ủy ban công tác đặc trách", "pos": "phrase"},
    # 1248: air group
    {"ipa": "/ɛr ɡruːp/", "vi": "liên đoàn không quân hải quân", "pos": "phrase"},
    # 1249: answer for
    {"ipa": "/ˈænsər fɔːr/", "vi": "chịu trách nhiệm cho; bảo lãnh cho", "pos": "phrase"},
    # 1250: bad guy
    {"ipa": "/bæd ɡaɪ/", "vi": "kẻ phản diện; tên ác ôn gian xảo", "pos": "phrase"},
    # 1251: big deal
    {"ipa": "/bɪɡ diːl/", "vi": "việc quan trọng to tát; món hời lớn", "pos": "phrase"},
    # 1252: book of job
    {"ipa": "/bʊk ʌv dʒoʊb/", "vi": "Sách Gióp trong Cựu Ước Kinh Thánh", "pos": "phrase"},
    # 1253: break up
    {"ipa": "/breɪk ʌp/", "vi": "chia tay đôi lứa; tan rã tan vỡ", "pos": "phrase"},
    # 1254: bring home
    {"ipa": "/brɪŋ hoʊm/", "vi": "đem lại thu nhập; làm cho thấm thía", "pos": "phrase"},
    # 1255: by design
    {"ipa": "/baɪ dɪˈzaɪn/", "vi": "chủ ý sắp đặt; có chủ đích từ trước", "pos": "phrase"},
    # 1256: case history
    {"ipa": "/keɪs ˈhɪstəri/", "vi": "hồ sơ bệnh án; tiểu sử vụ việc", "pos": "phrase"},
    # 1257: close set
    {"ipa": "/kloʊs sɛt/", "vi": "mọc sát nhau; xếp khít cạnh nhau", "pos": "phrase"},
    # 1258: college man
    {"ipa": "/ˈkɑːlɪdʒ mæn/", "vi": "nam sinh viên đại học", "pos": "phrase"},
    # 1259: common people
    {"ipa": "/ˈkɑːmən ˈpiːpəl/", "vi": "dân chúng bình dân; thường dân", "pos": "phrase"},
    # 1260: couple up
    {"ipa": "/ˈkʌpəl ʌp/", "vi": "kết đôi cặp uyên ương; móc nối toa", "pos": "phrase"},
    # 1261: cut off
    {"ipa": "/kʌt ɔːf/", "vi": "bị cắt tiếp tế; bị cô lập chia cắt", "pos": "phrase"},
    # 1262: date back
    {"ipa": "/deɪt bæk/", "vi": "bắt nguồn từ xưa; có từ thời kỳ", "pos": "phrase"},
    # 1263: field day
    {"ipa": "/fiːld deɪ/", "vi": "ngày hội lớn; dịp làm ăn thắng lợi", "pos": "phrase"},
    # 1264: field work
    {"ipa": "/fiːld wɜːrk/", "vi": "công tác đi thực địa điều tra", "pos": "phrase"},
    # 1265: first period
    {"ipa": "/fɜːrst ˈpɪriəd/", "vi": "hiệp thi đấu đầu tiên; tiết học đầu", "pos": "phrase"},
    # 1266: for any price
    {"ipa": "/fɔːr ˈɛni praɪs/", "vi": "bằng bất cứ giá nào", "pos": "phrase"},
    # 1267: for certain
    {"ipa": "/fɔːr ˈsɜːrtən/", "vi": "chắc chắn rõ ràng không nghi ngờ", "pos": "phrase"},
    # 1268: get hold
    {"ipa": "/ɡɛt hoʊld/", "vi": "nắm bắt được; liên lạc tìm ra được", "pos": "phrase"},
    # 1269: higher up
    {"ipa": "/ˈhaɪər ʌp/", "vi": "ở vị trí cao hơn; quan chức cấp cao", "pos": "phrase"},
    # 1270: hold out
    {"ipa": "/hoʊld aʊt/", "vi": "chìa tay ra; kiên cường cầm cự", "pos": "phrase"},
    # 1271: hold up
    {"ipa": "/hoʊld ʌp/", "vi": "cản trở; vụ cướp có vũ trang", "pos": "phrase"},
    # 1272: inside out
    {"ipa": "/ˈɪnˌsaɪd aʊt/", "vi": "lộn trái mặt áo; hiểu rõ ngọn ngành", "pos": "phrase"},
    # 1273: large person
    {"ipa": "/lɑːrdʒ ˈpɜːrsən/", "vi": "người vóc dáng to lớn đồ sộ", "pos": "phrase"},
    # 1274: last word
    {"ipa": "/læst wɜːrd/", "vi": "lời phán quyết cuối cùng; tinh túy", "pos": "phrase"},
    # 1275: live body
    {"ipa": "/lɪv ˈbɑːdi/", "vi": "cơ thể sinh vật sống", "pos": "phrase"},
    # 1276: living thing
    {"ipa": "/ˈlɪvɪŋ θɪŋ/", "vi": "sinh vật sống; sinh linh nhân gian", "pos": "phrase"},
    # 1277: love song
    {"ipa": "/lʌv sɔːŋ/", "vi": "bản tình ca; bài hát về tình yêu", "pos": "phrase"},
    # 1278: making known
    {"ipa": "/ˈmeɪkɪŋ noʊn/", "vi": "sự công bố; việc tiết lộ ra", "pos": "phrase"},
    # 1279: order book
    {"ipa": "/ˈɔːrdər bʊk/", "vi": "sổ theo dõi đơn đặt hàng", "pos": "phrase"},
    # 1280: out of view
    {"ipa": "/aʊt ʌv vjuː/", "vi": "khuất khỏi tầm mắt; ngoài tầm nhìn", "pos": "phrase"},
    # 1281: rest day
    {"ipa": "/rɛst deɪ/", "vi": "ngày nghỉ ngơi phục hồi", "pos": "phrase"},
    # 1282: right field
    {"ipa": "/raɪt fiːld/", "vi": "khu sân ngoài bên phải bóng chày", "pos": "phrase"},
    # 1283: service book
    {"ipa": "/ˈsɜːrvɪs bʊk/", "vi": "sách kinh phụng vụ giáo hội", "pos": "phrase"},
    # 1284: small talk
    {"ipa": "/smɔːl tɔːk/", "vi": "chuyện phiếm; trò chuyện xã giao", "pos": "phrase"},
    # 1285: stay put
    {"ipa": "/steɪ pʊt/", "vi": "ở yên bất động tại chỗ", "pos": "phrase"},
    # 1286: support level
    {"ipa": "/səˈpɔːrt ˈlɛvəl/", "vi": "ngưỡng hỗ trợ giá chứng khoán", "pos": "phrase"},
    # 1287: take the field
    {"ipa": "/teɪk ðə fiːld/", "vi": "ra sân thi đấu; xuất quân ra trận", "pos": "phrase"},
    # 1288: take the road
    {"ipa": "/teɪk ðə roʊd/", "vi": "lên đường lưu diễn; khởi hành đi", "pos": "phrase"},
    # 1289: under fire
    {"ipa": "/ˈʌndər ˈfaɪər/", "vi": "bị trúng đạn; bị chỉ trích gay gắt", "pos": "phrase"},
    # 1290: water level
    {"ipa": "/ˈwɔːtər ˈlɛvəl/", "vi": "mực nước thủy triều; ống thủy chuẩn", "pos": "phrase"},
    # 1291: work force
    {"ipa": "/wɜːrk fɔːrs/", "vi": "lực lượng lao động xã hội", "pos": "phrase"},
    # 1292: art school
    {"ipa": "/ɑːrt skuːl/", "vi": "trường nghệ thuật hội họa", "pos": "phrase"},
    # 1293: body of water
    {"ipa": "/ˈbɑːdi ʌv ˈwɔːtər/", "vi": "thủy vực; vùng nước mênh mông", "pos": "phrase"},
    # 1294: break out
    {"ipa": "/breɪk aʊt/", "vi": "bùng phát chiến tranh; vượt ngục", "pos": "phrase"},
    # 1295: bring around
    {"ipa": "/brɪŋ əˈraʊnd/", "vi": "thuyết phục thay đổi ý; hồi tỉnh", "pos": "phrase"},
    # 1296: common good
    {"ipa": "/ˈkɑːmən ɡʊd/", "vi": "lợi ích công cộng; ích lợi chung", "pos": "phrase"},
    # 1297: court order
    {"ipa": "/kɔːrt ˈɔːrdər/", "vi": "lệnh quyết định của tòa án", "pos": "phrase"},
    # 1298: cut down
    {"ipa": "/kʌt daʊn/", "vi": "chặt đốn cây; cắt giảm chi tiêu", "pos": "phrase"},
    # 1299: cut through
    {"ipa": "/kʌt θruː/", "vi": "đi lối tắt xuyên qua; nhìn thấu bản", "pos": "phrase"},
]

with open('scratch/b21_r03_raw_p3.json') as f:
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

with open('scratch/b21_r03_p3.json', 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("b21_r03_p3.json created successfully and validated!")
