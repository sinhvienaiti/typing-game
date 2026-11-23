import json

raw_items = json.load(open("scratch/b22_r02_raw_p2.json"))

reviews = [
    # 00: majority opinion
    {"pos": "phrase", "ipa": "/məˈdʒɔːrəti əˈpɪnjən/", "vi": "ý kiến đa số; phán quyết đa số"},
    # 01: majority rule
    {"pos": "phrase", "ipa": "/məˈdʒɔːrəti ruːl/", "vi": "nguyên tắc đa số; biểu quyết đa số"},
    # 02: man of affairs
    {"pos": "phrase", "ipa": "/mæn əv əˈfɛrz/", "vi": "nhà kinh doanh; người thạo việc"},
    # 03: mass culture
    {"pos": "phrase", "ipa": "/mæs ˈkʌltʃər/", "vi": "văn hóa đại chúng"},
    # 04: measure out
    {"pos": "phrase", "ipa": "/ˈmɛʒər aʊt/", "vi": "đong đo; phân chia theo định lượng"},
    # 05: measure up
    {"pos": "phrase", "ipa": "/ˈmɛʒər ʌp/", "vi": "đáp ứng tiêu chuẩn; đạt yêu cầu"},
    # 06: memory picture
    {"pos": "phrase", "ipa": "/ˈmɛməri ˈpɪktʃər/", "vi": "hình ảnh trong ký ức; ký ức xưa"},
    # 07: national security agency
    {"pos": "phrase", "ipa": "/ˈnæʃnəl sɪˈkjʊrəti ˈeɪdʒənsi/", "vi": "Cơ quan An ninh Quốc gia Mỹ; NSA"},
    # 08: ordered series
    {"pos": "phrase", "ipa": "/ˈɔːrdərd ˈsɪriːz/", "vi": "chuỗi có thứ tự; dãy sắp thứ tự"},
    # 09: phase in
    {"pos": "phrase", "ipa": "/feɪz ɪn/", "vi": "triển khai từng bước; áp dụng dần"},
    # 10: photo finish
    {"pos": "phrase", "ipa": "/ˈfoʊtoʊ ˈfɪnɪʃ/", "vi": "kết quả về đích sát nút chụp ảnh"},
    # 11: public debt
    {"pos": "phrase", "ipa": "/ˈpʌblɪk dɛt/", "vi": "nợ công; nợ quốc gia"},
    # 12: purchase order
    {"pos": "phrase", "ipa": "/ˈpɜːrtʃəs ˈɔːrdər/", "vi": "đơn đặt mua hàng; lệnh mua hàng PO"},
    # 13: push forward
    {"pos": "phrase", "ipa": "/pʊʃ ˈfɔːrwərd/", "vi": "tiến mạnh lên; thúc đẩy nhanh"},
    # 14: range animal
    {"pos": "phrase", "ipa": "/reɪndʒ ˈænɪml/", "vi": "gia súc chăn thả trên đồng cỏ"},
    # 15: red wine
    {"pos": "phrase", "ipa": "/rɛd waɪn/", "vi": "rượu vang đỏ; rượu nho đỏ"},
    # 16: road map
    {"pos": "phrase", "ipa": "/roʊd mæp/", "vi": "bản đồ đường bộ; lộ trình thực hiện"},
    # 17: rose of china
    {"pos": "phrase", "ipa": "/roʊz əv ˈtʃaɪnə/", "vi": "hoa dâm bụt; hoa hồng nhung"},
    # 18: rose oil
    {"pos": "phrase", "ipa": "/roʊz ɔɪl/", "vi": "tinh dầu hoa hồng; dầu hoa hồng"},
    # 19: round window
    {"pos": "phrase", "ipa": "/raʊnd ˈwɪndoʊ/", "vi": "cửa sổ tròn hốc tai trong"},
    # 20: sales agreement
    {"pos": "phrase", "ipa": "/seɪlz əˈɡriːmənt/", "vi": "hợp đồng mua bán; thỏa thuận bán"},
    # 21: screen pass
    {"pos": "phrase", "ipa": "/skriːn pæs/", "vi": "đường chuyền sau màn chắn đồng đội"},
    # 22: sea bottom
    {"pos": "phrase", "ipa": "/siː ˈbɑːtəm/", "vi": "đáy biển; đáy đại dương"},
    # 23: secretary of defense
    {"pos": "phrase", "ipa": "/ˈsɛkrətɛri əv dɪˈfɛns/", "vi": "Bộ trưởng Bộ Quốc phòng Hoa Kỳ"},
    # 24: shooting star
    {"pos": "phrase", "ipa": "/ˈʃuːtɪŋ stɑːr/", "vi": "sao băng; vệt sao sa trên trời"},
    # 25: short iron
    {"pos": "phrase", "ipa": "/ʃɔːrt ˈaɪərn/", "vi": "gậy sắt ngắn trong đánh golf"},
    # 26: sister ship
    {"pos": "phrase", "ipa": "/ˈsɪstər ʃɪp/", "vi": "tàu cùng thiết kế; tàu chị em"},
    # 27: small beer
    {"pos": "phrase", "ipa": "/smɔːl bɪr/", "vi": "chuyện vặt vãnh; điều nhỏ nhặt"},
    # 28: soldiers of god
    {"pos": "phrase", "ipa": "/ˈsoʊldʒərz əv ɡɑːd/", "vi": "những chiến binh của Chúa"},
    # 29: specific heat
    {"pos": "phrase", "ipa": "/spəˈsɪfɪk hiːt/", "vi": "nhiệt dung riêng của chất"},
    # 30: split up
    {"pos": "phrase", "ipa": "/splɪt ʌp/", "vi": "chia tay; tan rã nhóm; chia tách"},
    # 31: spring gun
    {"pos": "phrase", "ipa": "/sprɪŋ ɡʌn/", "vi": "súng bẫy gài dây tự nổ"},
    # 32: standard cell
    {"pos": "phrase", "ipa": "/ˈstændərd sɛl/", "vi": "pin chuẩn; ô chuẩn thiết kế vi mạch"},
    # 33: state of affairs
    {"pos": "phrase", "ipa": "/steɪt əv əˈfɛrz/", "vi": "tình hình thực tế; cục diện sự việc"},
    # 34: street corner
    {"pos": "phrase", "ipa": "/striːt ˈkɔːrnər/", "vi": "góc phố; góc ngã tư đường"},
    # 35: strike back
    {"pos": "phrase", "ipa": "/straɪk bæk/", "vi": "đánh trả lại; phản công trả đũa"},
    # 36: strike off
    {"pos": "phrase", "ipa": "/straɪk ɔːf/", "vi": "xóa tên khỏi danh bạ; gạch bỏ"},
    # 37: student teacher
    {"pos": "phrase", "ipa": "/ˈstuːdnt ˈtiːtʃər/", "vi": "giáo sinh thực tập đứng lớp"},
    # 38: system command
    {"pos": "phrase", "ipa": "/ˈsɪstəm kəˈmænd/", "vi": "lệnh hệ điều hành; lệnh hệ thống"},
    # 39: target language
    {"pos": "phrase", "ipa": "/ˈtɑːrɡɪt ˈlæŋɡwɪdʒ/", "vi": "ngôn ngữ đích cần dịch"},
    # 40: target range
    {"pos": "phrase", "ipa": "/ˈtɑːrɡɪt reɪndʒ/", "vi": "trường bắn bia; bãi tập bắn súng"},
    # 41: television star
    {"pos": "phrase", "ipa": "/ˈtɛləvɪʒn stɑːr/", "vi": "ngôi sao truyền hình; sao màn ảnh"},
    # 42: tv dinner
    {"pos": "phrase", "ipa": "/ˌtiːˈviː ˈdɪnər/", "vi": "suất ăn tối đông lạnh đóng sẵn"},
    # 43: upper hand
    {"pos": "phrase", "ipa": "/ˈʌpər hænd/", "vi": "thế thượng phong; ưu thế áp đảo"},
    # 44: vice president
    {"pos": "phrase", "ipa": "/vaɪs ˈprɛzədənt/", "vi": "phó chủ tịch; phó tổng thống"},
    # 45: wake board
    {"pos": "phrase", "ipa": "/weɪk bɔːrd/", "vi": "ván lướt sóng có dây kéo ca nô"},
    # 46: weather eye
    {"pos": "phrase", "ipa": "/ˈwɛðər aɪ/", "vi": "sự cảnh giác đề phòng cẩn thận"},
    # 47: white beer
    {"pos": "phrase", "ipa": "/waɪt bɪr/", "vi": "bia trắng lúa mì"},
    # 48: wild west show
    {"pos": "phrase", "ipa": "/waɪld wɛst ʃoʊ/", "vi": "chương trình biểu diễn miền Tây cổ"},
    # 49: william ii
    {"pos": "phrase", "ipa": "/ˈwɪljəm ðə ˈsɛkənd/", "vi": "Vua William Đệ Nhị"},
    # 50: willing and able
    {"pos": "phrase", "ipa": "/ˈwɪlɪŋ ænd ˈeɪbl/", "vi": "sẵn lòng và có đủ năng lực làm"},
    # 51: world affairs
    {"pos": "phrase", "ipa": "/wɜːrld əˈfɛrz/", "vi": "các vấn đề thời sự thế giới"},
    # 52: brings
    {"pos": "verb", "ipa": "/brɪŋz/", "vi": "mang lại; đem đến; dẫn tới"},
    # 53: londons
    {"pos": "noun", "ipa": "/ˈlʌndənz/", "vi": "các đô thị tên London; họ London"},
    # 54: meets
    {"pos": "noun", "ipa": "/miːts/", "vi": "các cuộc thi đấu thể thao"},
    # 55: air mail
    {"pos": "phrase", "ipa": "/ɛr meɪl/", "vi": "thư gửi đường hàng không; bưu phẩm"},
    # 56: american labor party
    {"pos": "phrase", "ipa": "/əˈmɛrɪkən ˈleɪbər ˈpɑːrti/", "vi": "Đảng Lao động Hoa Kỳ"},
    # 57: animal oil
    {"pos": "phrase", "ipa": "/ˈænɪml ɔɪl/", "vi": "dầu động vật; mỡ động vật"},
    # 58: arms race
    {"pos": "phrase", "ipa": "/ɑːrmz reɪs/", "vi": "cuộc chạy đua vũ trang quân sự"},
    # 59: article of faith
    {"pos": "phrase", "ipa": "/ˈɑːrtɪkl əv feɪθ/", "vi": "tín điều cốt lõi; niềm tin sắt đá"},
    # 60: asian american
    {"pos": "phrase", "ipa": "/ˈeɪʒn əˈmɛrɪkən/", "vi": "người Mỹ gốc Á; công dân gốc Á"},
    # 61: bad debt
    {"pos": "phrase", "ipa": "/bæd dɛt/", "vi": "nợ xấu; khoản nợ khó đòi"},
    # 62: bear in mind
    {"pos": "phrase", "ipa": "/bɛr ɪn maɪnd/", "vi": "ghi nhớ kỹ; khắc sâu trong lòng"},
    # 63: black forest
    {"pos": "phrase", "ipa": "/blæk ˈfɔːrɪst/", "vi": "Rừng Đen dãy núi Đức"},
    # 64: blue stone
    {"pos": "phrase", "ipa": "/bluː stoʊn/", "vi": "đá xanh bazan; khoáng phèn xanh"},
    # 65: break apart
    {"pos": "phrase", "ipa": "/breɪk əˈpɑːrt/", "vi": "vỡ vụn ra; tháo rời từng mảnh"},
    # 66: bridge player
    {"pos": "phrase", "ipa": "/brɪdʒ ˈpleɪər/", "vi": "người chơi bài bridge"},
    # 67: business loan
    {"pos": "phrase", "ipa": "/ˈbɪznəs loʊn/", "vi": "khoản vay kinh doanh thương mại"},
    # 68: camp david
    {"pos": "phrase", "ipa": "/kæmp ˈdeɪvɪd/", "vi": "Trại David nơi nghỉ Tổng thống Mỹ"},
    # 69: camp meeting
    {"pos": "phrase", "ipa": "/kæmp ˈmiːtɪŋ/", "vi": "buổi truyền giảng ngoài trời"},
    # 70: cash bar
    {"pos": "phrase", "ipa": "/kæʃ bɑːr/", "vi": "quầy bar tự trả tiền nước tại tiệc"},
    # 71: civil defense
    {"pos": "phrase", "ipa": "/ˈsɪvl dɪˈfɛns/", "vi": "phòng thủ dân sự; cứu nạn phòng hộ"},
    # 72: command line
    {"pos": "phrase", "ipa": "/kəˈmænd laɪn/", "vi": "dòng lệnh điều khiển; giao diện CLI"},
    # 73: command post
    {"pos": "phrase", "ipa": "/kəˈmænd poʊst/", "vi": "sở chỉ huy tiền phương quân đội"},
    # 74: communication system
    {"pos": "phrase", "ipa": "/kəˌmjuːnɪˈkeɪʃn ˈsɪstəm/", "vi": "hệ thống thông tin liên lạc"},
    # 75: crowd together
    {"pos": "phrase", "ipa": "/kraʊd təˈɡɛðər/", "vi": "tụ tập chen chúc; túm tụm lại"},
    # 76: dance floor
    {"pos": "phrase", "ipa": "/dæns flɔːr/", "vi": "sàn nhảy; sàn khiêu vũ vũ trường"},
    # 77: dance master
    {"pos": "phrase", "ipa": "/dæns ˈmæstər/", "vi": "thầy dạy khiêu vũ; sư phụ dạy múa"},
    # 78: death duty
    {"pos": "phrase", "ipa": "/dɛθ ˈduːti/", "vi": "thuế tài sản để lại; thuế di sản"},
    # 79: demand note
    {"pos": "phrase", "ipa": "/dɪˈmænd noʊt/", "vi": "hối phiếu trả ngay khi có yêu cầu"},
    # 80: down payment
    {"pos": "phrase", "ipa": "/daʊn ˈpeɪmənt/", "vi": "tiền trả trước; khoản tiền cọc"},
    # 81: east china sea
    {"pos": "phrase", "ipa": "/iːst ˈtʃaɪnə siː/", "vi": "biển Hoa Đông"},
    # 82: eastern church
    {"pos": "phrase", "ipa": "/ˈiːstərn tʃɜːrtʃ/", "vi": "Giáo hội Đông phương Chính thống"},
    # 83: emotional state
    {"pos": "phrase", "ipa": "/ɪˈmoʊʃənl steɪt/", "vi": "trạng thái cảm xúc; tâm trạng"},
    # 84: engineering science
    {"pos": "phrase", "ipa": "/ˌɛndʒəˈnɪrɪŋ ˈsaɪəns/", "vi": "khoa học kỹ thuật công trình"},
    # 85: exercise set
    {"pos": "phrase", "ipa": "/ˈɛksərsaɪz sɛt/", "vi": "hiệp tập luyện; chuỗi bài tập gym"},
    # 86: eye condition
    {"pos": "phrase", "ipa": "/aɪ kənˈdɪʃn/", "vi": "bệnh lý về mắt; tình trạng thị lực"},
    # 87: fair catch
    {"pos": "phrase", "ipa": "/fɛr kætʃ/", "vi": "cú bắt bóng an toàn bóng bầu dục"},
    # 88: fair weather
    {"pos": "phrase", "ipa": "/fɛr ˈwɛðər/", "vi": "thời tiết thuận lợi nắng đẹp"},
    # 89: fan letter
    {"pos": "phrase", "ipa": "/fæn ˈlɛtər/", "vi": "thư người hâm mộ gửi thần tượng"},
    # 90: feature article
    {"pos": "phrase", "ipa": "/ˈfiːtʃər ˈɑːrtɪkl/", "vi": "bài viết chuyên đề; bài phóng sự"},
    # 91: field guide
    {"pos": "phrase", "ipa": "/fiːld ɡaɪd/", "vi": "sách hướng dẫn nhận dạng thực địa"},
    # 92: fill out
    {"pos": "phrase", "ipa": "/fɪl aʊt/", "vi": "điền vào biểu mẫu; trở nên đẫy đà"},
    # 93: fill up
    {"pos": "phrase", "ipa": "/fɪl ʌp/", "vi": "đổ đầy bình; chứa đầy tràn ngập"},
    # 94: fire iron
    {"pos": "phrase", "ipa": "/ˈfaɪər ˈaɪərn/", "vi": "bộ que cời than lò sưởi sắt"},
    # 95: flow away
    {"pos": "phrase", "ipa": "/floʊ əˈweɪ/", "vi": "chảy trôi đi xa; tiêu thoát dần"},
    # 96: for good measure
    {"pos": "phrase", "ipa": "/fɔːr ɡʊd ˈmɛʒər/", "vi": "thêm vào cho chắc; trọn vẹn hơn"},
    # 97: gas heat
    {"pos": "phrase", "ipa": "/ɡæs hiːt/", "vi": "hệ thống sưởi ấm bằng khí đốt gas"},
    # 98: glass eye
    {"pos": "phrase", "ipa": "/ɡlæs aɪ/", "vi": "mắt giả thủy tinh; mắt nhân tạo"},
    # 99: global organization
    {"pos": "phrase", "ipa": "/ˈɡloʊbl ˌɔːrɡənəˈzeɪʃn/", "vi": "tổ chức toàn cầu quy mô quốc tế"}
]

for r in reviews:
    r["ipa"] = r["ipa"].strip()

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

json.dump(out_items, open("scratch/b22_r02_p2.json", "w"), ensure_ascii=False, indent=2)
print("Round 2 Part 2 reviewed successfully: 100 items saved to scratch/b22_r02_p2.json")
