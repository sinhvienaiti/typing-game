import json

raw_items = json.load(open("scratch/b22_r01_raw_p1.json"))

reviews = [
    # 00: fish oil
    {"pos": "phrase", "ipa": "/fɪʃ ɔɪl/", "vi": "dầu cá; mỡ cá"},
    # 01: french foreign office
    {"pos": "phrase", "ipa": "/frɛntʃ ˈfɔːrən ˈɔːfɪs/", "vi": "Bộ Ngoại giao Pháp"},
    # 02: full dress
    {"pos": "phrase", "ipa": "/fʊl drɛs/", "vi": "lễ phục; trang phục dạ tiệc"},
    # 03: garden party
    {"pos": "phrase", "ipa": "/ˈɡɑːrdn ˈpɑːrti/", "vi": "tiệc sân vườn; tiệc ngoài trời"},
    # 04: gold coast
    {"pos": "phrase", "ipa": "/ɡoʊld koʊst/", "vi": "Bờ Biển Vàng; duyên hải thịnh vượng"},
    # 05: great britain
    {"pos": "phrase", "ipa": "/ɡreɪt ˈbrɪtn/", "vi": "Vương quốc Anh; đảo Anh"},
    # 06: heart and soul
    {"pos": "phrase", "ipa": "/hɑːrt ænd soʊl/", "vi": "hết lòng; toàn tâm toàn ý"},
    # 07: helping hand
    {"pos": "phrase", "ipa": "/ˈhɛlpɪŋ hænd/", "vi": "sự giúp đỡ; bàn tay tương trợ"},
    # 08: high tea
    {"pos": "phrase", "ipa": "/haɪ tiː/", "vi": "tiệc trà chiều kèm đồ ăn"},
    # 09: hospital ship
    {"pos": "phrase", "ipa": "/ˈhɑːspɪtl ʃɪp/", "vi": "tàu bệnh viện; tàu cứu thương"},
    # 10: hot weather
    {"pos": "phrase", "ipa": "/hɑːt ˈwɛðər/", "vi": "thời tiết nóng bức; trời oi ả"},
    # 11: human language technology
    {"pos": "phrase", "ipa": "/ˈhjuːmən ˈlæŋɡwɪdʒ tɛkˈnɑːlədʒi/", "vi": "công nghệ ngôn ngữ người"},
    # 12: jack london
    {"pos": "phrase", "ipa": "/dʒæk ˈlʌndən/", "vi": "nhà văn Jack London"},
    # 13: join forces
    {"pos": "phrase", "ipa": "/dʒɔɪn ˈfɔːrsɪz/", "vi": "hợp lực; chung tay hiệp sức"},
    # 14: jump on
    {"pos": "phrase", "ipa": "/dʒʌmp ɑːn/", "vi": "nhảy lên; mắng mỏ gay gắt"},
    # 15: kick down
    {"pos": "phrase", "ipa": "/kɪk daʊn/", "vi": "đạp đổ; đá văng; phá tung"},
    # 16: kick off
    {"pos": "phrase", "ipa": "/kɪk ɔːf/", "vi": "bắt đầu; khai mạc; phát bóng"},
    # 17: labor party
    {"pos": "phrase", "ipa": "/ˈleɪbər ˈpɑːrti/", "vi": "Đảng Lao động"},
    # 18: last quarter
    {"pos": "phrase", "ipa": "/læst ˈkwɔːrtər/", "vi": "trăng hạ huyền; quý cuối năm"},
    # 19: lead glass
    {"pos": "phrase", "ipa": "/lɛd ɡlæs/", "vi": "thủy tinh pha chì; pha lê chì"},
    # 20: lead tree
    {"pos": "phrase", "ipa": "/lɛd triː/", "vi": "cây keo dậu; cây bọ chét"},
    # 21: length of service
    {"pos": "phrase", "ipa": "/lɛŋkθ əv ˈsɜːrvɪs/", "vi": "thâm niên công tác; thời gian làm"},
    # 22: let fly
    {"pos": "phrase", "ipa": "/lɛt flaɪ/", "vi": "bắn; phóng; trút giận"},
    # 23: letter box
    {"pos": "phrase", "ipa": "/ˈlɛtər bɑːks/", "vi": "hòm thư; thùng thư"},
    # 24: long plane
    {"pos": "phrase", "ipa": "/lɔːŋ pleɪn/", "vi": "cái bào dài; bào ghép gỗ"},
    # 25: machine language
    {"pos": "phrase", "ipa": "/məˈʃiːn ˈlæŋɡwɪdʒ/", "vi": "ngôn ngữ máy"},
    # 26: mass meeting
    {"pos": "phrase", "ipa": "/mæs ˈmiːtɪŋ/", "vi": "cuộc mít tinh lớn; đại hội lớn"},
    # 27: mental process
    {"pos": "phrase", "ipa": "/ˈmɛntl ˈprɑːsɛs/", "vi": "quá trình tư duy; tiến trình tâm lý"},
    # 28: mexico city
    {"pos": "phrase", "ipa": "/ˈmɛksɪkoʊ ˈsɪti/", "vi": "thành phố Mexico City"},
    # 29: modern dance
    {"pos": "phrase", "ipa": "/ˈmɑːdərn dæns/", "vi": "múa hiện đại; vũ đạo hiện đại"},
    # 30: moon about
    {"pos": "phrase", "ipa": "/muːn əˈbaʊt/", "vi": "thẫn thờ; tha thẩn; bần thần"},
    # 31: mountain state
    {"pos": "phrase", "ipa": "/ˈmaʊntn steɪt/", "vi": "biệt danh bang Tây Virginia"},
    # 32: movie camera
    {"pos": "phrase", "ipa": "/ˈmuːvi ˈkæmərə/", "vi": "máy quay phim"},
    # 33: new forest
    {"pos": "phrase", "ipa": "/njuː ˈfɔːrɪst/", "vi": "vườn quốc gia New Forest"},
    # 34: new moon
    {"pos": "phrase", "ipa": "/njuː muːn/", "vi": "trăng non; trăng đầu tháng"},
    # 35: off her guard
    {"pos": "phrase", "ipa": "/ɔːf hɜːr ɡɑːrd/", "vi": "mất cảnh giác; sơ hở; lơ là"},
    # 36: oil color
    {"pos": "phrase", "ipa": "/ɔɪl ˈkʌlər/", "vi": "màu sơn dầu; màu vẽ tranh dầu"},
    # 37: old guard
    {"pos": "phrase", "ipa": "/oʊld ɡɑːrd/", "vi": "phe bảo thủ; phái cựu trào"},
    # 38: operating system
    {"pos": "phrase", "ipa": "/ˈɑːpəreɪtɪŋ ˈsɪstəm/", "vi": "hệ điều hành"},
    # 39: operation code
    {"pos": "phrase", "ipa": "/ˌɑːpəˈreɪʃn koʊd/", "vi": "mã thao tác; mã lệnh máy tính"},
    # 40: pain unit
    {"pos": "phrase", "ipa": "/peɪn ˈjuːnɪt/", "vi": "đơn vị đo mức độ đau"},
    # 41: pair off
    {"pos": "phrase", "ipa": "/pɛr ɔːf/", "vi": "ghép đôi; chia thành từng cặp"},
    # 42: party boss
    {"pos": "phrase", "ipa": "/ˈpɑːrti bɔːs/", "vi": "trùm đảng phái; trùm chính trị"},
    # 43: piece of material
    {"pos": "phrase", "ipa": "/piːs əv məˈtɪriəl/", "vi": "mảnh vải; tấm vật liệu"},
    # 44: political action committee
    {"pos": "phrase", "ipa": "/pəˈlɪtɪkl ˈækʃn kəˈmɪti/", "vi": "ủy ban hành động chính trị"},
    # 45: press agency
    {"pos": "phrase", "ipa": "/prɛs ˈeɪdʒənsi/", "vi": "hãng thông tấn; cơ quan báo chí"},
    # 46: public violence
    {"pos": "phrase", "ipa": "/ˈpʌblɪk ˈvaɪələns/", "vi": "bạo lực công cộng; bạo loạn"},
    # 47: pull up short
    {"pos": "phrase", "ipa": "/pʊl ʌp ʃɔːrt/", "vi": "dừng phắt lại; khựng lại đột ngột"},
    # 48: reading teacher
    {"pos": "phrase", "ipa": "/ˈriːdɪŋ ˈtiːtʃər/", "vi": "giáo viên dạy đọc"},
    # 49: road surface
    {"pos": "phrase", "ipa": "/roʊd ˈsɜːrfɪs/", "vi": "mặt đường; bề mặt đường xá"},
    # 50: safety island
    {"pos": "phrase", "ipa": "/ˈseɪfti ˈaɪlənd/", "vi": "đảo an toàn cho người đi bộ"},
    # 51: saturday night special
    {"pos": "phrase", "ipa": "/ˈsætərdeɪ naɪt ˈspɛʃl/", "vi": "súng lục nhỏ rẻ tiền"},
    # 52: school of medicine
    {"pos": "phrase", "ipa": "/skuːl əv ˈmɛdsn/", "vi": "trường y khoa; đại học y"},
    # 53: screen test
    {"pos": "phrase", "ipa": "/skriːn tɛst/", "vi": "buổi thử vai; cuộc quay phim thử"},
    # 54: sea floor
    {"pos": "phrase", "ipa": "/siː flɔːr/", "vi": "đáy biển; đáy đại dương"},
    # 55: secret code
    {"pos": "phrase", "ipa": "/ˈsiːkrət koʊd/", "vi": "mật mã; mật hiệu"},
    # 56: secret writing
    {"pos": "phrase", "ipa": "/ˈsiːkrət ˈraɪtɪŋ/", "vi": "mật mã học; chữ viết tàng hình"},
    # 57: side horse
    {"pos": "phrase", "ipa": "/saɪd hɔːrs/", "vi": "ngựa gỗ thể dục; ngựa tay quay"},
    # 58: silver age
    {"pos": "phrase", "ipa": "/ˈsɪlvər eɪdʒ/", "vi": "thời đại bạc; thời kỳ thịnh vượng"},
    # 59: social function
    {"pos": "phrase", "ipa": "/ˈsoʊʃl ˈfʌŋkʃn/", "vi": "sự kiện xã hội; chức năng xã hội"},
    # 60: solid state
    {"pos": "phrase", "ipa": "/ˈsɑːlɪd steɪt/", "vi": "thể rắn; trạng thái rắn; bán dẫn"},
    # 61: sound camera
    {"pos": "phrase", "ipa": "/saʊnd ˈkæmərə/", "vi": "máy quay phim thu âm đồng bộ"},
    # 62: south american nation
    {"pos": "phrase", "ipa": "/saʊθ əˈmɛrɪkən ˈneɪʃn/", "vi": "quốc gia Nam Mỹ"},
    # 63: south china sea
    {"pos": "phrase", "ipa": "/saʊθ ˈtʃaɪnə siː/", "vi": "Biển Đông"},
    # 64: stage direct
    {"pos": "phrase", "ipa": "/steɪdʒ dəˈrɛkt/", "vi": "đạo diễn sân khấu; dàn dựng kịch"},
    # 65: stone age
    {"pos": "phrase", "ipa": "/stoʊn eɪdʒ/", "vi": "thời kỳ đồ đá; thời đại đồ đá"},
    # 66: sweet oil
    {"pos": "phrase", "ipa": "/swiːt ɔɪl/", "vi": "dầu ô liu ngọt; dầu hạt cải"},
    # 67: take shape
    {"pos": "phrase", "ipa": "/teɪk ʃeɪp/", "vi": "hình thành; định hình; rõ nét"},
    # 68: target program
    {"pos": "phrase", "ipa": "/ˈtɑːrɡɪt ˈproʊɡræm/", "vi": "chương trình đích"},
    # 69: television room
    {"pos": "phrase", "ipa": "/ˈtɛləvɪʒn ruːm/", "vi": "phòng xem tivi; phòng truyền hình"},
    # 70: time limit
    {"pos": "phrase", "ipa": "/taɪm ˈlɪmɪt/", "vi": "giới hạn thời gian; hạn định"},
    # 71: true cat
    {"pos": "phrase", "ipa": "/truː kæt/", "vi": "mèo thực thụ; động vật họ mèo"},
    # 72: tv channel
    {"pos": "phrase", "ipa": "/ˌtiːˈviː ˈtʃænl/", "vi": "kênh truyền hình; đài truyền hình"},
    # 73: two hundred
    {"pos": "phrase", "ipa": "/tuː ˈhʌndrəd/", "vi": "hai trăm"},
    # 74: type metal
    {"pos": "phrase", "ipa": "/taɪp ˈmɛtl/", "vi": "hợp kim đúc chữ in"},
    # 75: united nations day
    {"pos": "phrase", "ipa": "/juːˈnaɪtɪd ˈneɪʃnz deɪ/", "vi": "Ngày Liên Hợp Quốc"},
    # 76: wall unit
    {"pos": "phrase", "ipa": "/wɔːl ˈjuːnɪt/", "vi": "tủ tường; kệ tủ áp tường"},
    # 77: weapons system
    {"pos": "phrase", "ipa": "/ˈwɛpənz ˈsɪstəm/", "vi": "hệ thống vũ khí"},
    # 78: wedding march
    {"pos": "phrase", "ipa": "/ˈwɛdɪŋ mɑːrtʃ/", "vi": "hành khúc đám cưới; nhạc rước dâu"},
    # 79: west african
    {"pos": "phrase", "ipa": "/wɛst ˈæfrɪkən/", "vi": "thuộc Tây Phi; người Tây Phi"},
    # 80: white horse
    {"pos": "phrase", "ipa": "/waɪt hɔːrs/", "vi": "ngựa trắng; sóng bạc đầu"},
    # 81: white magic
    {"pos": "phrase", "ipa": "/waɪt ˈmædʒɪk/", "vi": "bạch ma thuật; phép thuật trừ tà"},
    # 82: william green
    {"pos": "phrase", "ipa": "/ˈwɪljəm ɡriːn/", "vi": "William Green"},
    # 83: word of mouth
    {"pos": "phrase", "ipa": "/wɜːrd əv maʊθ/", "vi": "sự truyền miệng; lời truyền miệng"},
    # 84: ages
    {"pos": "noun", "ipa": "/ˈeɪdʒɪz/", "vi": "các thời đại; thời gian rất lâu"},
    # 85: deals
    {"pos": "noun", "ipa": "/diːlz/", "vi": "các thỏa thuận; các thương vụ"},
    # 86: redded
    {"pos": "verb", "ipa": "/ˈrɛdɪd/", "vi": "đã làm đỏ; đã nhuộm đỏ"},
    # 87: redder
    {"pos": "adj", "ipa": "/ˈrɛdər/", "vi": "đỏ hơn; sắc đỏ hơn"},
    # 88: reddest
    {"pos": "adj", "ipa": "/ˈrɛdɪst/", "vi": "đỏ nhất; thắm đỏ nhất"},
    # 89: reds
    {"pos": "noun", "ipa": "/rɛdz/", "vi": "các sắc đỏ; phe đỏ cánh tả"},
    # 90: thirds
    {"pos": "noun", "ipa": "/θɜːrdz/", "vi": "các phần ba; vị trí thứ ba"},
    # 91: adult education
    {"pos": "phrase", "ipa": "/əˈdʌlt ˌɛdʒuˈkeɪʃn/", "vi": "giáo dục người lớn; bổ túc văn hóa"},
    # 92: american standard version
    {"pos": "phrase", "ipa": "/əˈmɛrɪkən ˈstændərd ˈvɜːrʒn/", "vi": "Kinh Thánh bản chuẩn Hoa Kỳ"},
    # 93: ask for trouble
    {"pos": "phrase", "ipa": "/æsk fɔːr ˈtrʌbl/", "vi": "chuốc lấy rắc rối; rước họa"},
    # 94: background level
    {"pos": "phrase", "ipa": "/ˈbækɡraʊnd ˈlɛvl/", "vi": "mức nền; mức bức xạ nền"},
    # 95: bear down
    {"pos": "phrase", "ipa": "/bɛr daʊn/", "vi": "đè nén; rặn đẻ; dốc toàn lực"},
    # 96: bear down on
    {"pos": "phrase", "ipa": "/bɛr daʊn ɑːn/", "vi": "lao nhanh về phía; ập tới gần"},
    # 97: bear off
    {"pos": "phrase", "ipa": "/bɛr ɔːf/", "vi": "chuyển hướng lái; giành thắng lợi"},
    # 98: birth control
    {"pos": "phrase", "ipa": "/bɜːrθ kənˈtroʊl/", "vi": "biện pháp tránh thai; kế hoạch hóa"},
    # 99: black magic
    {"pos": "phrase", "ipa": "/blæk ˈmædʒɪk/", "vi": "tà thuật; ma thuật đen"}
]

assert len(reviews) == 100
assert len(raw_items) == 100

out_items = []
for i in range(100):
    item = dict(raw_items[i])
    rev = reviews[i]
    item["pos"] = rev["pos"]
    item["ipa"] = rev["ipa"]
    item["vi"] = rev["vi"]
    item["status"] = "reviewed"
    
    assert len(item["vi"]) <= 35, f"vi too long at {i}: {item['vi']}"
    assert len(item["vi"]) > 0
    assert item["ipa"].startswith("/") and item["ipa"].endswith("/") and item["ipa"].count("/") == 2
    out_items.append(item)

json.dump(out_items, open("scratch/b22_r01_p1.json", "w"), ensure_ascii=False, indent=2)
print("Part 1 reviewed successfully: 100 items saved to scratch/b22_r01_p1.json")
