import json

raw_items = json.load(open("scratch/b22_r01_raw_p2.json"))

reviews = [
    # 00: block vote
    {"pos": "phrase", "ipa": "/blɑːk voʊt/", "vi": "bỏ phiếu theo khối; phiếu khối"},
    # 01: body length
    {"pos": "phrase", "ipa": "/ˈbɑːdi lɛŋkθ/", "vi": "chiều dài thân; chiều dài cơ thể"},
    # 02: break of serve
    {"pos": "phrase", "ipa": "/breɪk əv sɜːrv/", "vi": "bẻ giao bóng; thắng ván đối phương"},
    # 03: break wind
    {"pos": "phrase", "ipa": "/breɪk wɪnd/", "vi": "xì hơi; đánh rắm; trung tiện"},
    # 04: breaking point
    {"pos": "phrase", "ipa": "/ˈbreɪkɪŋ pɔɪnt/", "vi": "giới hạn chịu đựng; điểm gãy"},
    # 05: bridge hand
    {"pos": "phrase", "ipa": "/brɪdʒ hænd/", "vi": "bộ bài bridge trên tay"},
    # 06: budget cut
    {"pos": "phrase", "ipa": "/ˈbʌdʒɪt kʌt/", "vi": "sự cắt giảm ngân sách"},
    # 07: capital letter
    {"pos": "phrase", "ipa": "/ˈkæpɪtl ˈlɛtər/", "vi": "chữ in hoa; chữ viết hoa"},
    # 08: charge unit
    {"pos": "phrase", "ipa": "/tʃɑːrdʒ ˈjuːnɪt/", "vi": "đơn vị điện tích"},
    # 09: christian science
    {"pos": "phrase", "ipa": "/ˈkrɪstʃən ˈsaɪəns/", "vi": "phái Khoa học Cơ Đốc giáo"},
    # 10: civil officer
    {"pos": "phrase", "ipa": "/ˈsɪvl ˈɔːfɪsər/", "vi": "viên chức dân sự; công chức"},
    # 11: coach station
    {"pos": "phrase", "ipa": "/koʊtʃ ˈsteɪʃn/", "vi": "bến xe khách; bến xe đường dài"},
    # 12: coast range
    {"pos": "phrase", "ipa": "/koʊst reɪndʒ/", "vi": "dãy núi duyên hải bờ Tây"},
    # 13: dry point
    {"pos": "phrase", "ipa": "/draɪ pɔɪnt/", "vi": "kỹ thuật khắc khô; mũi kim khắc"},
    # 14: earth color
    {"pos": "phrase", "ipa": "/ɜːrθ ˈkʌlər/", "vi": "màu đất tự nhiên; khoáng màu đất"},
    # 15: european economic community
    {"pos": "phrase", "ipa": "/ˌjʊərəˈpiːən ˌiːkəˈnɑːmɪk kəˈmjuːnəti/", "vi": "Cộng đồng Kinh tế châu Âu"},
    # 16: every quarter
    {"pos": "phrase", "ipa": "/ˈɛvri ˈkwɔːrtər/", "vi": "hằng quý; mỗi quý một lần"},
    # 17: family medicine
    {"pos": "phrase", "ipa": "/ˈfæməli ˈmɛdsn/", "vi": "y học gia đình"},
    # 18: federal agency
    {"pos": "phrase", "ipa": "/ˈfɛdərəl ˈeɪdʒənsi/", "vi": "cơ quan liên bang"},
    # 19: fly open
    {"pos": "phrase", "ipa": "/flaɪ ˈoʊpən/", "vi": "bật tung mở; mở toang ra"},
    # 20: free port
    {"pos": "phrase", "ipa": "/friː pɔːrt/", "vi": "cảng tự do; khu cảng miễn thuế"},
    # 21: gas gun
    {"pos": "phrase", "ipa": "/ɡæs ɡʌn/", "vi": "súng bắn hơi cay; súng bắn khí"},
    # 22: german capital
    {"pos": "phrase", "ipa": "/ˈdʒɜːrmən ˈkæpɪtl/", "vi": "thủ đô nước Đức; Berlin"},
    # 23: get the jump
    {"pos": "phrase", "ipa": "/ɡɛt ðə dʒʌmp/", "vi": "giành lợi thế sớm; ra tay trước"},
    # 24: great bear
    {"pos": "phrase", "ipa": "/ɡreɪt bɛr/", "vi": "chòm sao Đại Hùng"},
    # 25: great hundred
    {"pos": "phrase", "ipa": "/ɡreɪt ˈhʌndrəd/", "vi": "một trăm hai mươi; số 120"},
    # 26: growth stock
    {"pos": "phrase", "ipa": "/ɡroʊθ stɑːk/", "vi": "cổ phiếu tăng trưởng"},
    # 27: hard roll
    {"pos": "phrase", "ipa": "/hɑːrd roʊl/", "vi": "ổ bánh mì tròn vỏ cứng"},
    # 28: jump out
    {"pos": "phrase", "ipa": "/dʒʌmp aʊt/", "vi": "nhảy vọt ra; đập ngay vào mắt"},
    # 29: keep guard
    {"pos": "phrase", "ipa": "/kiːp ɡɑːrd/", "vi": "canh phòng; đứng gác cẩn mật"},
    # 30: kick around
    {"pos": "phrase", "ipa": "/kɪk əˈraʊnd/", "vi": "đối xử tệ; thảo luận; lang thang"},
    # 31: living stone
    {"pos": "phrase", "ipa": "/ˈlɪvɪŋ stoʊn/", "vi": "cây đá sống; cây ngọc sinh bì"},
    # 32: long hundred
    {"pos": "phrase", "ipa": "/lɔːŋ ˈhʌndrəd/", "vi": "một trăm hai mươi; số 120"},
    # 33: machine code
    {"pos": "phrase", "ipa": "/məˈʃiːn koʊd/", "vi": "mã máy; tập lệnh mã máy"},
    # 34: marketing research
    {"pos": "phrase", "ipa": "/ˈmɑːrkɪtɪŋ rɪˈsɜːrtʃ/", "vi": "nghiên cứu thị trường"},
    # 35: marriage bed
    {"pos": "phrase", "ipa": "/ˈmærɪdʒ bɛd/", "vi": "giường tân hôn; giường cưới"},
    # 36: mass production
    {"pos": "phrase", "ipa": "/mæs prəˈdʌkʃn/", "vi": "sản xuất hàng loạt; chế tạo quy mô"},
    # 37: mental energy
    {"pos": "phrase", "ipa": "/ˈmɛntl ˈɛnərdʒi/", "vi": "năng lượng tinh thần; trí lực"},
    # 38: middle distance
    {"pos": "phrase", "ipa": "/ˈmɪdl ˈdɪstəns/", "vi": "cự ly trung bình; trung cảnh"},
    # 39: north american nation
    {"pos": "phrase", "ipa": "/nɔːrθ əˈmɛrɪkən ˈneɪʃn/", "vi": "quốc gia Bắc Mỹ"},
    # 40: not surprised
    {"pos": "phrase", "ipa": "/nɑːt sərˈpraɪzd/", "vi": "không ngạc nhiên; đoán trước được"},
    # 41: nuclear family
    {"pos": "phrase", "ipa": "/ˈnuːkliər ˈfæməli/", "vi": "gia đình hạt nhân"},
    # 42: photo credit
    {"pos": "phrase", "ipa": "/ˈfoʊtoʊ ˈkrɛdɪt/", "vi": "ghi nhận nguồn ảnh; tác quyền ảnh"},
    # 43: place kick
    {"pos": "phrase", "ipa": "/pleɪs kɪk/", "vi": "cú sút bóng chết; quả đá bóng nằm"},
    # 44: poor fish
    {"pos": "phrase", "ipa": "/pʊr fɪʃ/", "vi": "kẻ tội nghiệp; người ngờ nghệch"},
    # 45: post horse
    {"pos": "phrase", "ipa": "/poʊst hɔːrs/", "vi": "ngựa trạm; ngựa trạm chuyển thư"},
    # 46: potential unit
    {"pos": "phrase", "ipa": "/pəˈtɛnʃl ˈjuːnɪt/", "vi": "đơn vị điện thế"},
    # 47: pressure unit
    {"pos": "phrase", "ipa": "/ˈprɛʃər ˈjuːnɪt/", "vi": "đơn vị áp suất"},
    # 48: professional organization
    {"pos": "phrase", "ipa": "/prəˈfɛʃənl ˌɔːrɡənəˈzeɪʃn/", "vi": "tổ chức nghề nghiệp"},
    # 49: rain down
    {"pos": "phrase", "ipa": "/reɪn daʊn/", "vi": "rơi như mưa; trút xuống dồn dập"},
    # 50: reference point
    {"pos": "phrase", "ipa": "/ˈrɛfrəns pɔɪnt/", "vi": "điểm tham chiếu; cột mốc quy chiếu"},
    # 51: reference system
    {"pos": "phrase", "ipa": "/ˈrɛfrəns ˈsɪstəm/", "vi": "hệ quy chiếu"},
    # 52: return on investment
    {"pos": "phrase", "ipa": "/rɪˈtɜːrn ɑːn ɪnˈvɛstmənt/", "vi": "tỷ suất hoàn vốn đầu tư; ROI"},
    # 53: road metal
    {"pos": "phrase", "ipa": "/roʊd ˈmɛtl/", "vi": "đá rải đường; đá dăm lát đường"},
    # 54: roll call
    {"pos": "phrase", "ipa": "/roʊl kɔːl/", "vi": "sự điểm danh; hồi còi điểm danh"},
    # 55: royal society
    {"pos": "phrase", "ipa": "/ˈrɔɪəl səˈsaɪəti/", "vi": "Hội Hoàng gia Anh"},
    # 56: science teacher
    {"pos": "phrase", "ipa": "/ˈsaɪəns ˈtiːtʃər/", "vi": "giáo viên khoa học"},
    # 57: sea fan
    {"pos": "phrase", "ipa": "/siː fæn/", "vi": "san hô hình quạt; quạt biển"},
    # 58: simple machine
    {"pos": "phrase", "ipa": "/ˈsɪmpl məˈʃiːn/", "vi": "máy cơ đơn giản"},
    # 59: sir david low
    {"pos": "phrase", "ipa": "/sɜːr ˈdeɪvɪd loʊ/", "vi": "họa sĩ David Low"},
    # 60: six nations
    {"pos": "phrase", "ipa": "/sɪks ˈneɪʃnz/", "vi": "Liên minh Sáu Bộ tộc; giải Sáu Nước"},
    # 61: social development commission
    {"pos": "phrase", "ipa": "/ˈsoʊʃl dɪˈvɛləpmənt kəˈmɪʃn/", "vi": "Ủy ban Phát triển Xã hội"},
    # 62: soft on
    {"pos": "phrase", "ipa": "/sɔːft ɑːn/", "vi": "nương tay với; say đắm mù quáng"},
    # 63: sound pressure level
    {"pos": "phrase", "ipa": "/saʊnd ˈprɛʃər ˈlɛvl/", "vi": "mức áp suất âm thanh; độ ồn"},
    # 64: standing press
    {"pos": "phrase", "ipa": "/ˈstændɪŋ prɛs/", "vi": "máy ép đứng; máy in đứng"},
    # 65: stick together
    {"pos": "phrase", "ipa": "/stɪk təˈɡɛðər/", "vi": "gắn bó bên nhau; đồng lòng gắn kết"},
    # 66: stone life face
    {"pos": "phrase", "ipa": "/stoʊn laɪf feɪs/", "vi": "cây đá sống Lithops"},
    # 67: stuck with
    {"pos": "phrase", "ipa": "/stʌk wɪð/", "vi": "mắc kẹt với; đành chịu gánh"},
    # 68: systems analysis
    {"pos": "phrase", "ipa": "/ˈsɪstəmz əˈnæləsɪs/", "vi": "phân tích hệ thống"},
    # 69: taking apart
    {"pos": "phrase", "ipa": "/ˈteɪkɪŋ əˈpɑːrt/", "vi": "việc tháo rời; mổ xẻ phân tích"},
    # 70: tea family
    {"pos": "phrase", "ipa": "/tiː ˈfæməli/", "vi": "họ chè Theaceae"},
    # 71: team sport
    {"pos": "phrase", "ipa": "/tiːm spɔːrt/", "vi": "môn thể thao đồng đội"},
    # 72: tough guy
    {"pos": "phrase", "ipa": "/tʌf ɡaɪ/", "vi": "kẻ cứng đầu; gã ngổ ngáo ngạo mạn"},
    # 73: train station
    {"pos": "phrase", "ipa": "/treɪn ˈsteɪʃn/", "vi": "nhà ga xe lửa; ga tàu hỏa"},
    # 74: trump card
    {"pos": "phrase", "ipa": "/trʌmp kɑːrd/", "vi": "quân bài tẩy; lá bài át chủ"},
    # 75: weight unit
    {"pos": "phrase", "ipa": "/weɪt ˈjuːnɪt/", "vi": "đơn vị đo khối lượng; đơn vị cân"},
    # 76: wild west
    {"pos": "phrase", "ipa": "/waɪld wɛst/", "vi": "miền Tây hoang dã Hoa Kỳ"},
    # 77: william james
    {"pos": "phrase", "ipa": "/ˈwɪljəm dʒeɪmz/", "vi": "nhà triết học William James"},
    # 78: wine making
    {"pos": "phrase", "ipa": "/waɪn ˈmeɪkɪŋ/", "vi": "nghề làm rượu vang; nghề ủ vang"},
    # 79: world trade organization
    {"pos": "phrase", "ipa": "/wɜːrld treɪd ˌɔːrɡənəˈzeɪʃn/", "vi": "Tổ chức Thương mại Thế giới; WTO"},
    # 80: arms industry
    {"pos": "phrase", "ipa": "/ɑːrmz ˈɪndəstri/", "vi": "ngành công nghiệp vũ khí"},
    # 81: australian capital
    {"pos": "phrase", "ipa": "/ɔːˈstreɪliən ˈkæpɪtl/", "vi": "thủ đô nước Úc; Canberra"},
    # 82: battle born state
    {"pos": "phrase", "ipa": "/ˈbætl bɔːrn steɪt/", "vi": "biệt danh bang Nevada"},
    # 83: beach ball
    {"pos": "phrase", "ipa": "/biːtʃ bɔːl/", "vi": "bóng bãi biển; bóng bơm hơi"},
    # 84: bill of exchange
    {"pos": "phrase", "ipa": "/bɪl əv ɪksˈtʃeɪndʒ/", "vi": "hối phiếu; hối phiếu thương mại"},
    # 85: black fly
    {"pos": "phrase", "ipa": "/blæk flaɪ/", "vi": "ruồi đen; bọ đen hại cây"},
    # 86: black september movement
    {"pos": "phrase", "ipa": "/blæk sɛpˈtɛmbər ˈmuːvmənt/ ", "vi": "Tổ chức Tháng Chín Đen"},
    # 87: blood cell
    {"pos": "phrase", "ipa": "/blʌd sɛl/", "vi": "tế bào máu; huyết cầu"},
    # 88: blue murder
    {"pos": "phrase", "ipa": "/bluː ˈmɜːrdər/", "vi": "tiếng la hét thất thanh inh ỏi"},
    # 89: box spring
    {"pos": "phrase", "ipa": "/bɑːks sprɪŋ/", "vi": "khung đệm lò xo"},
    # 90: capital of france
    {"pos": "phrase", "ipa": "/ˈkæpɪtl əv fræns/", "vi": "thủ đô nước Pháp; Paris"},
    # 91: capital ship
    {"pos": "phrase", "ipa": "/ˈkæpɪtl ʃɪp/", "vi": "tàu chiến chủ lực; soái hạm"},
    # 92: capital stock
    {"pos": "phrase", "ipa": "/ˈkæpɪtl stɑːk/", "vi": "vốn cổ phần; vốn điều lệ"},
    # 93: cash card
    {"pos": "phrase", "ipa": "/kæʃ kɑːrd/", "vi": "thẻ rút tiền mặt; thẻ ATM"},
    # 94: change taste
    {"pos": "phrase", "ipa": "/tʃeɪndʒ teɪst/", "vi": "đổi khẩu vị; thay đổi sở thích"},
    # 95: chief executive
    {"pos": "phrase", "ipa": "/tʃiːf ɪɡˈzɛkjətɪv/", "vi": "tổng thống; giám đốc điều hành"},
    # 96: christmas box
    {"pos": "phrase", "ipa": "/ˈkrɪsməs bɑːks/", "vi": "hộp quà Giáng sinh; tiền mừng lễ"},
    # 97: christmas card
    {"pos": "phrase", "ipa": "/ˈkrɪsməs kɑːrd/", "vi": "thiệp Giáng sinh; thiệp Noel"},
    # 98: coffee cup
    {"pos": "phrase", "ipa": "/ˈkɔːfi kʌp/", "vi": "tách cà phê; chén uống cà phê"},
    # 99: cold cash
    {"pos": "phrase", "ipa": "/koʊld kæʃ/", "vi": "tiền mặt trao tay; tiền tươi"}
]

# Quick fix for any trailing space in IPA:
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

json.dump(out_items, open("scratch/b22_r01_p2.json", "w"), ensure_ascii=False, indent=2)
print("Part 2 reviewed successfully: 100 items saved to scratch/b22_r01_p2.json")
