import json

raw_items = json.load(open("scratch/b22_r02_raw_p4.json"))

reviews = [
    # 00: brain doctor
    {"pos": "phrase", "ipa": "/breɪn ˈdɑːktər/", "vi": "bác sĩ thần kinh; chuyên gia não"},
    # 01: british west africa
    {"pos": "phrase", "ipa": "/ˈbrɪtɪʃ wɛst ˈæfrɪkə/", "vi": "Tây Phi thuộc Anh thuộc địa cũ"},
    # 02: california coffee
    {"pos": "phrase", "ipa": "/ˌkælɪˈfɔːrnjə ˈkɔːfi/", "vi": "cây cà phê dại California"},
    # 03: call loan
    {"pos": "phrase", "ipa": "/kɔːl loʊn/", "vi": "khoản vay hoàn trả theo yêu cầu"},
    # 04: central american nation
    {"pos": "phrase", "ipa": "/ˈsɛntrəl əˈmɛrɪkən ˈneɪʃn/", "vi": "quốc gia Trung Mỹ"},
    # 05: chair car
    {"pos": "phrase", "ipa": "/tʃɛr kɑːr/", "vi": "toa xe lửa hạng ghế bành ngồi"},
    # 06: channel island
    {"pos": "phrase", "ipa": "/ˈtʃænl ˈaɪlənd/", "vi": "quần đảo Eo biển Manche"},
    # 07: chicken out
    {"pos": "phrase", "ipa": "/ˈtʃɪkɪn aʊt/", "vi": "chùn bước; nhụt chí bỏ cuộc"},
    # 08: china stone
    {"pos": "phrase", "ipa": "/ˈtʃaɪnə stoʊn/", "vi": "đá tràng thạch làm sứ cao lanh"},
    # 09: civil marriage
    {"pos": "phrase", "ipa": "/ˈsɪvl ˈmærɪdʒ/", "vi": "kết hôn dân sự trước chính quyền"},
    # 10: color bar
    {"pos": "phrase", "ipa": "/ˈkʌlər bɑːr/", "vi": "rào cản phân biệt màu da"},
    # 11: confidence man
    {"pos": "phrase", "ipa": "/ˈkɑːnfədəns mæn/", "vi": "kẻ lừa đảo niềm tin; tay bịp bợm"},
    # 12: credit application
    {"pos": "phrase", "ipa": "/ˈkrɛdɪt ˌæplɪˈkeɪʃn/", "vi": "đơn xin cấp tín dụng; đơn vay"},
    # 13: criminal record
    {"pos": "phrase", "ipa": "/ˈkrɪmɪnl ˈrɛkərd/", "vi": "tiền án tiền sự; lý lịch tư pháp"},
    # 14: crowd control
    {"pos": "phrase", "ipa": "/kraʊd kənˈtroʊl/", "vi": "kiểm soát trật tự đám đông"},
    # 15: dance band
    {"pos": "phrase", "ipa": "/dæns bænd/", "vi": "ban nhạc khiêu vũ vũ trường"},
    # 16: dry land
    {"pos": "phrase", "ipa": "/draɪ lænd/", "vi": "đất liền; vùng đất khô cằn"},
    # 17: electric fire
    {"pos": "phrase", "ipa": "/ɪˈlɛktrɪk ˈfaɪər/", "vi": "lò sưởi điện; máy sưởi điện"},
    # 18: electric light
    {"pos": "phrase", "ipa": "/ɪˈlɛktrɪk laɪt/", "vi": "đèn điện chiếu sáng; ánh điện"},
    # 19: fall apart
    {"pos": "phrase", "ipa": "/fɔːl əˈpɑːrt/", "vi": "vỡ vụn; sụp đổ; suy sụp hoàn toàn"},
    # 20: fan dance
    {"pos": "phrase", "ipa": "/fæn dæns/", "vi": "điệu múa quạt truyền thống"},
    # 21: farm club
    {"pos": "phrase", "ipa": "/fɑːrm klʌb/", "vi": "đội bóng vệ tinh đào tạo trẻ"},
    # 22: fellow member
    {"pos": "phrase", "ipa": "/ˈfɛloʊ ˈmɛmbər/", "vi": "thành viên đồng cấp; đồng hội viên"},
    # 23: financial gain
    {"pos": "phrase", "ipa": "/faɪˈnænʃl ɡeɪn/", "vi": "lợi nhuận tài chính; mối lợi tiền"},
    # 24: foreign agent
    {"pos": "phrase", "ipa": "/ˈfɔːrən ˈeɪdʒənt/", "vi": "điệp viên nước ngoài; gián điệp"},
    # 25: free lunch
    {"pos": "phrase", "ipa": "/friː lʌntʃ/", "vi": "bữa ăn miễn phí; món lợi không công"},
    # 26: french window
    {"pos": "phrase", "ipa": "/frɛntʃ ˈwɪndoʊ/", "vi": "cửa sổ sát sàn kiểu Pháp"},
    # 27: gas engine
    {"pos": "phrase", "ipa": "/ɡæs ˈɛndʒɪn/", "vi": "động cơ đốt khí gas; máy nổ khí đốt"},
    # 28: german police dog
    {"pos": "phrase", "ipa": "/ˈdʒɜːrmən pəˈliːs dɔːɡ/", "vi": "chó chăn cừu Đức béc-giê"},
    # 29: gift tax
    {"pos": "phrase", "ipa": "/ɡɪft tæks/", "vi": "thuế quà tặng biếu; thuế biếu tặng"},
    # 30: giving birth
    {"pos": "phrase", "ipa": "/ˈɡɪvɪŋ bɜːrθ/", "vi": "việc sinh con; sự vượt cạn đẻ con"},
    # 31: heart failure
    {"pos": "phrase", "ipa": "/hɑːrt ˈfeɪljər/", "vi": "chứng suy tim tim mạch"},
    # 32: heat content
    {"pos": "phrase", "ipa": "/hiːt ˈkɑːntɛnt/", "vi": "nhiệt hàm entanpi nhiệt động học"},
    # 33: high finance
    {"pos": "phrase", "ipa": "/haɪ faɪˈnæns/", "vi": "tài chính cấp cao; giới tài phiệt"},
    # 34: horse sense
    {"pos": "phrase", "ipa": "/hɔːrs sɛns/", "vi": "lẽ thường tình; óc thực tế bén nhạy"},
    # 35: ice coffee
    {"pos": "phrase", "ipa": "/aɪs ˈkɔːfi/", "vi": "cà phê đá pha sẵn mát lạnh"},
    # 36: ill turn
    {"pos": "phrase", "ipa": "/ɪl tɜːrn/", "vi": "hành động làm hại; việc gây tổn hại"},
    # 37: kick turn
    {"pos": "phrase", "ipa": "/kɪk tɜːrn/", "vi": "cú đá xoay người trong trượt tuyết"},
    # 38: kitchen help
    {"pos": "phrase", "ipa": "/ˈkɪtʃɪn hɛlp/", "vi": "phụ bếp nhà hàng; người làm bếp"},
    # 39: lake district
    {"pos": "phrase", "ipa": "/leɪk ˈdɪstrɪkt/", "vi": "Khu thắng cảnh Lake District Anh"},
    # 40: launch area
    {"pos": "phrase", "ipa": "/lɔːntʃ ˈɛriə/", "vi": "khu vực bệ phóng tên lửa vũ trụ"},
    # 41: lay down
    {"pos": "phrase", "ipa": "/leɪ daʊn/", "vi": "đặt xuống; ban hành quy tắc luật"},
    # 42: lay off
    {"pos": "phrase", "ipa": "/leɪ ɔːf/", "vi": "sa thải hàng loạt; cho thôi việc"},
    # 43: lay over
    {"pos": "phrase", "ipa": "/leɪ ˈoʊvər/", "vi": "nghỉ quá cảnh chuyến bay; ghé lại"},
    # 44: long chain
    {"pos": "phrase", "ipa": "/lɔːŋ tʃeɪn/", "vi": "mạch phân tử dài; chuỗi dài polime"},
    # 45: long measure
    {"pos": "phrase", "ipa": "/lɔːŋ ˈmɛʒər/", "vi": "hệ đo độ dài; đơn vị đo chiều dài"},
    # 46: make pure
    {"pos": "phrase", "ipa": "/meɪk pjʊr/", "vi": "tinh chế làm sạch; thanh lọc"},
    # 47: marriage contract
    {"pos": "phrase", "ipa": "/ˈmærɪdʒ ˈkɑːntrækt/", "vi": "hôn ước hợp đồng tiền hôn nhân"},
    # 48: memory loss
    {"pos": "phrase", "ipa": "/ˈmɛməri lɔːs/", "vi": "mất trí nhớ; chứng suy giảm trí nhớ"},
    # 49: mental note
    {"pos": "phrase", "ipa": "/ˈmɛntl noʊt/", "vi": "ghi nhớ sâu trong đầu; tự nhắc nhở"},
    # 50: method of choice
    {"pos": "phrase", "ipa": "/ˈmɛθəd əv tʃɔɪs/", "vi": "phương pháp ưu tiên lựa chọn"},
    # 51: months
    {"pos": "noun", "ipa": "/mʌnθs/", "vi": "các tháng trong năm; nhiều tháng"},
    # 52: northern cross
    {"pos": "phrase", "ipa": "/ˈnɔːrðərn krɔːs/", "vi": "chòm sao Bắc Thập Tự Thiên Nga"},
    # 53: outsides
    {"pos": "noun", "ipa": "/ˈaʊtsaɪdz/", "vi": "các mặt bên ngoài; phần rìa ngoài"},
    # 54: patient role
    {"pos": "phrase", "ipa": "/ˈpeɪʃnt roʊl/", "vi": "vai trò người bệnh; vai bị động"},
    # 55: plant material
    {"pos": "phrase", "ipa": "/plænt məˈtɪriəl/", "vi": "nguyên liệu thực vật; mô thực vật"},
    # 56: plant product
    {"pos": "phrase", "ipa": "/plænt ˈprɑːdʌkt/", "vi": "nông sản; sản phẩm từ thực vật"},
    # 57: police boat
    {"pos": "phrase", "ipa": "/pəˈliːs boʊt/", "vi": "ca nô tuần tra cảnh sát đường sông"},
    # 58: public relations
    {"pos": "phrase", "ipa": "/ˈpʌblɪk rɪˈleɪʃnz/", "vi": "quan hệ công chúng; ngành PR"},
    # 59: religious text
    {"pos": "phrase", "ipa": "/rɪˈlɪdʒəs tɛkst/", "vi": "văn bản tôn giáo; kinh điển giáo lý"},
    # 60: river bottom
    {"pos": "phrase", "ipa": "/ˈrɪvər ˈbɑːtəm/", "vi": "lòng sông; đáy dòng sông phù sa"},
    # 61: robert brown
    {"pos": "phrase", "ipa": "/ˈrɑːbərt braʊn/", "vi": "nhà thực vật học Robert Brown"},
    # 62: rock bottom
    {"pos": "phrase", "ipa": "/rɑːk ˈbɑːtəm/", "vi": "đáy vực sâu; mức thấp nhất lịch sử"},
    # 63: roll film
    {"pos": "phrase", "ipa": "/roʊl fɪlm/", "vi": "cuộn phim máy ảnh chụp hình"},
    # 64: safety catch
    {"pos": "phrase", "ipa": "/ˈseɪfti kætʃ/", "vi": "chốt hãm an toàn; khóa an toàn súng"},
    # 65: sea animal
    {"pos": "phrase", "ipa": "/siː ˈænɪml/", "vi": "động vật biển; sinh vật đại dương"},
    # 66: selling race
    {"pos": "phrase", "ipa": "/ˈsɛlɪŋ reɪs/", "vi": "đua ngựa bán đấu giá ngựa thắng"},
    # 67: selves
    {"pos": "noun", "ipa": "/sɛlvz/", "vi": "những bản ngã; các cái tôi cá nhân"},
    # 68: senate race
    {"pos": "phrase", "ipa": "/ˈsɛnət reɪs/", "vi": "cuộc bầu cử đua vào Thượng viện Mỹ"},
    # 69: sense of balance
    {"pos": "phrase", "ipa": "/sɛns əv ˈbæləns/", "vi": "cảm giác thăng bằng cơ thể"},
    # 70: sexual practice
    {"pos": "phrase", "ipa": "/ˈsɛkʃuəl ˈpræktɪs/", "vi": "hành vi tình dục; quan hệ tình dục"},
    # 71: shooting range
    {"pos": "phrase", "ipa": "/ˈʃuːtɪŋ reɪndʒ/", "vi": "trường bắn súng đạn; bãi tập bắn"},
    # 72: skin cancer
    {"pos": "phrase", "ipa": "/skɪn ˈkænsər/", "vi": "bệnh ung thư da hắc tố ác tính"},
    # 73: smart card
    {"pos": "phrase", "ipa": "/smɑːrt kɑːrd/", "vi": "thẻ gắn vi mạch thông minh"},
    # 74: soft water
    {"pos": "phrase", "ipa": "/sɔːft ˈwɔːtər/", "vi": "nước mềm ít ion kim loại nặng"},
    # 75: star apple
    {"pos": "phrase", "ipa": "/stɑːr ˈæpl/", "vi": "quả vú sữa ngọt lịm"},
    # 76: sugar water
    {"pos": "phrase", "ipa": "/ˈʃʊɡər ˈwɔːtər/", "vi": "nước đường pha; nước sirô đường"},
    # 77: surface mine
    {"pos": "phrase", "ipa": "/ˈsɜːrfɪs maɪn/", "vi": "mỏ khoáng sản lộ thiên"},
    # 78: take lying down
    {"pos": "phrase", "ipa": "/teɪk ˈlaɪɪŋ daʊn/", "vi": "ngậm đắng nuốt cay chịu đựng"},
    # 79: target practice
    {"pos": "phrase", "ipa": "/ˈtɑːrɡɪt ˈpræktɪs/", "vi": "buổi tập bắn bia mục tiêu súng"},
    # 80: tax advantage
    {"pos": "phrase", "ipa": "/tæks ədˈvæntɪdʒ/", "vi": "lợi thế miễn giảm thuế đầu tư"},
    # 81: test driver
    {"pos": "phrase", "ipa": "/tɛst ˈdraɪvər/", "vi": "tài xế chuyên lái thử nghiệm xe"},
    # 82: test fly
    {"pos": "phrase", "ipa": "/tɛst flaɪ/", "vi": "bay thử nghiệm máy bay mới"},
    # 83: traffic island
    {"pos": "phrase", "ipa": "/ˈtræfɪk ˈaɪlənd/", "vi": "đảo phân làn giao thông đường bộ"},
    # 84: united mine workers
    {"pos": "phrase", "ipa": "/juːˈnaɪtɪd maɪn ˈwɜːrkərz/", "vi": "Nghiệp đoàn Thợ mỏ Hoa Kỳ UMW"},
    # 85: waste paper
    {"pos": "phrase", "ipa": "/weɪst ˈpeɪpər/", "vi": "giấy loại phế liệu; giấy vụn"},
    # 86: wear ship
    {"pos": "phrase", "ipa": "/wɛr ʃɪp/", "vi": "chuyển hướng xuôi gió tàu buồm"},
    # 87: web site
    {"pos": "phrase", "ipa": "/wɛb saɪt/", "vi": "trang thông tin điện tử; website"},
    # 88: wide area network
    {"pos": "phrase", "ipa": "/waɪd ˈɛriə ˈnɛtwɜːrk/", "vi": "mạng máy tính diện rộng WAN"},
    # 89: wild dog
    {"pos": "phrase", "ipa": "/waɪld dɔːɡ/", "vi": "chó hoang dại châu Phi"},
    # 90: word stress
    {"pos": "phrase", "ipa": "/wɜːrd strɛs/", "vi": "trọng âm của từ ngữ âm học"},
    # 91: zone fire
    {"pos": "phrase", "ipa": "/zoʊn ˈfaɪər/", "vi": "hỏa lực bắn bao phủ toàn khu vực"},
    # 92: costed
    {"pos": "verb", "ipa": "/ˈkɔːstɪd/", "vi": "đã định giá chi phí dự toán"},
    # 93: cuts
    {"pos": "noun", "ipa": "/kʌts/", "vi": "các vết cắt; các đợt cắt giảm"},
    # 94: mains
    {"pos": "noun", "ipa": "/meɪnz/", "vi": "mạng lưới điện nước chính tổng"},
    # 95: mothered
    {"pos": "verb", "ipa": "/ˈmʌðərd/", "vi": "đã bảo bọc chăm sóc như mẹ hiền"},
    # 96: mothering
    {"pos": "noun", "ipa": "/ˈmʌðərɪŋ/", "vi": "thiên chức làm mẹ; việc nuôi con"},
    # 97: mothers
    {"pos": "noun", "ipa": "/ˈmʌðərz/", "vi": "những người mẹ; các bà mẹ hiền"},
    # 98: towns
    {"pos": "noun", "ipa": "/taʊnz/", "vi": "các thị trấn; những đô thị nhỏ"},
    # 99: african american english
    {"pos": "phrase", "ipa": "/ˈæfrɪkən əˈmɛrɪkən ˈɪŋɡlɪʃ/", "vi": "tiếng Anh của người Mỹ da đen AAVE"}
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

json.dump(out_items, open("scratch/b22_r02_p4.json", "w"), ensure_ascii=False, indent=2)
print("Round 2 Part 4 reviewed successfully: 100 items saved to scratch/b22_r02_p4.json")
