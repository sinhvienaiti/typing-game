import json

items = [
  {"id": "lex.en.200k.064903", "hw": "terbium metal", "pos": "phrase", "ipa": "/ˈtɜːrbiəm ˈmɛtəl/", "vi": "kim loại đất hiếm terbi (Tb)"},
  {"id": "lex.en.200k.064904", "hw": "tinea corporis", "pos": "phrase", "ipa": "/ˈtɪniə ˈkɔːrpərɪs/", "vi": "bệnh nấm hắc lào vùng da thân"},
  {"id": "lex.en.200k.064905", "hw": "tristan tzara", "pos": "phrase", "ipa": "/ˈtrɪstɑːn ˈtsɑːrə/", "vi": "nhà thơ tiên phong Đa-đa Tzara"},
  {"id": "lex.en.200k.064906", "hw": "van vleck", "pos": "phrase", "ipa": "/væn vlɛk/", "vi": "nhà vật lý Nobel John Van Vleck"},
  {"id": "lex.en.200k.064907", "hw": "vervet monkey", "pos": "phrase", "ipa": "/ˈvɜːrvɪt ˈmʌŋki/", "vi": "khỉ vervet mặt đen ở châu Phi"},
  {"id": "lex.en.200k.064908", "hw": "wild bill hickock", "pos": "phrase", "ipa": "/waɪld bɪl ˈhɪkɑːk/", "vi": "xạ thủ huyền thoại miền Tây Hickok"},
  {"id": "lex.en.200k.064909", "hw": "zea mays rugosa", "pos": "phrase", "ipa": "/ˈziːə meɪz ruːˈɡoʊsə/", "vi": "giống bắp ngô ngọt ăn tươi"},
  {"id": "lex.en.200k.064910", "hw": "acclimatisations", "pos": "noun", "ipa": "/əˌklaɪmətaɪˈzeɪʃənz/", "vi": "sự thích nghi khí hậu mới (Anh)"},
  {"id": "lex.en.200k.064911", "hw": "allocators", "pos": "noun", "ipa": "/ˈæləˌkeɪtərz/", "vi": "bộ cấp phát bộ nhớ; người phân bổ"},
  {"id": "lex.en.200k.064912", "hw": "anemometers", "pos": "noun", "ipa": "/ˌænəˈmɑːmətərz/", "vi": "máy phong kế đo tốc độ hướng gió"},
  {"id": "lex.en.200k.064913", "hw": "arcuses", "pos": "noun", "ipa": "/ˈɑːrkəsɪz/", "vi": "mây hình vòm cung; vòng cung giải"},
  {"id": "lex.en.200k.064914", "hw": "baedekers", "pos": "noun", "ipa": "/ˈbeɪdəkərz/", "vi": "cẩm nang sách hướng dẫn du lịch"},
  {"id": "lex.en.200k.064915", "hw": "bertoluccis", "pos": "noun", "ipa": "/ˌbɛrtəˈluːtʃiz/", "vi": "đạo diễn điện ảnh Ý Bertolucci"},
  {"id": "lex.en.200k.064916", "hw": "botas", "pos": "noun", "ipa": "/ˈboʊtəz/", "vi": "bình da đựng rượu truyền thống Tây"},
  {"id": "lex.en.200k.064917", "hw": "bottomlands", "pos": "noun", "ipa": "/ˈbɑːtəmˌlændz/", "vi": "vùng đất bãi bồi màu mỡ ven sông"},
  {"id": "lex.en.200k.064918", "hw": "careerists", "pos": "noun", "ipa": "/kəˈrɪərɪsts/", "vi": "kẻ hám danh cơ hội thăng tiến"},
  {"id": "lex.en.200k.064919", "hw": "carrageenans", "pos": "noun", "ipa": "/ˌkærəˈɡiːnənz/", "vi": "chất làm đặc chiết từ tảo biển đỏ"},
  {"id": "lex.en.200k.064920", "hw": "catechists", "pos": "noun", "ipa": "/ˈkætəˌkɪsts/", "vi": "giáo lý viên dạy giáo lý Công giáo"},
  {"id": "lex.en.200k.064921", "hw": "cephalosporins", "pos": "noun", "ipa": "/ˌsɛfələˈspɔːrɪnz/", "vi": "nhóm kháng sinh cephalosporin"},
  {"id": "lex.en.200k.064922", "hw": "cornuses", "pos": "noun", "ipa": "/ˈkɔːrnəsɪz/", "vi": "chi cây sơn thù du hoa bốn cánh"},
  {"id": "lex.en.200k.064923", "hw": "counterfeiters", "pos": "noun", "ipa": "/ˈkaʊntərˌfɪtərz/", "vi": "kẻ làm giả tiền giấy tờ hàng hóa"},
  {"id": "lex.en.200k.064924", "hw": "criollos", "pos": "noun", "ipa": "/kriˈoʊjoʊz/", "vi": "người gốc Tây sinh tại châu Mỹ"},
  {"id": "lex.en.200k.064925", "hw": "cyclopaedias", "pos": "noun", "ipa": "/ˌsaɪkləˈpiːdiəz/", "vi": "bộ sách bách khoa toàn thư (Anh)"},
  {"id": "lex.en.200k.064926", "hw": "czernies", "pos": "noun", "ipa": "/ˈtʃɛrniz/", "vi": "nhà soạn nhạc sư phạm đàn Czerny"},
  {"id": "lex.en.200k.064927", "hw": "delisted", "pos": "verb", "ipa": "/diːˈlɪstɪd/", "vi": "đã hủy niêm yết khỏi sàn danh sách"},
  {"id": "lex.en.200k.064928", "hw": "delisting", "pos": "verb", "ipa": "/diːˈlɪstɪŋ/", "vi": "đang rút hủy niêm yết cổ phiếu"},
  {"id": "lex.en.200k.064929", "hw": "delists", "pos": "verb", "ipa": "/diːˈlɪsts/", "vi": "hủy niêm yết xóa khỏi danh sách"},
  {"id": "lex.en.200k.064930", "hw": "demodulators", "pos": "noun", "ipa": "/diːˈmɑːdʒəˌleɪtərz/", "vi": "bộ giải điều chế tín hiệu radio"},
  {"id": "lex.en.200k.064931", "hw": "detractors", "pos": "noun", "ipa": "/dɪˈtræktərz/", "vi": "người gièm pha chê bai nói xấu"},
  {"id": "lex.en.200k.064932", "hw": "empedocleses", "pos": "noun", "ipa": "/ɛmˈpɛdəkliːzɪz/", "vi": "triết gia Hy Lạp cổ Empedocles"},
  {"id": "lex.en.200k.064933", "hw": "enfolded", "pos": "verb", "ipa": "/ɛnˈfoʊldɪd/", "vi": "đã ôm trọn vào lòng; đã bọc gói"},
  {"id": "lex.en.200k.064934", "hw": "enfolds", "pos": "verb", "ipa": "/ɛnˈfoʊldz/", "vi": "ôm ấp bao bọc lấy; gấp bọc lại"},
  {"id": "lex.en.200k.064935", "hw": "enkis", "pos": "noun", "ipa": "/ˈɛŋkiz/", "vi": "thần nước trí tuệ Sumer cổ đại Enki"},
  {"id": "lex.en.200k.064936", "hw": "enrollees", "pos": "noun", "ipa": "/ɛnˈroʊliːz/", "vi": "người ghi danh tham gia khóa học"},
  {"id": "lex.en.200k.064937", "hw": "entreaties", "pos": "noun", "ipa": "/ɛnˈtriːtiz/", "vi": "lời khẩn cầu tha thiết van nài"},
  {"id": "lex.en.200k.064938", "hw": "expositors", "pos": "noun", "ipa": "/ɪkˈspɑːzətərz/", "vi": "người giải thích chú giải kinh sách"},
  {"id": "lex.en.200k.064939", "hw": "fernier", "pos": "adj", "ipa": "/ˈfɜːrniər/", "vi": "rậm rạp nhiều cây dương xỉ hơn"},
  {"id": "lex.en.200k.064940", "hw": "ferniest", "pos": "adj", "ipa": "/ˈfɜːrniɪst/", "vi": "rậm rạp nhiều cây dương xỉ nhất"},
  {"id": "lex.en.200k.064941", "hw": "fices", "pos": "noun", "ipa": "/faɪsɪz/", "vi": "chó nhỏ lai tạp hay sủa dữ (Mỹ cổ)"},
  {"id": "lex.en.200k.064942", "hw": "fiords", "pos": "noun", "ipa": "/fjɔːrdz/", "vi": "vịnh hẹp sâu vách đá dựng ở Na Uy"},
  {"id": "lex.en.200k.064943", "hw": "fishhooks", "pos": "noun", "ipa": "/ˈfɪʃhʊks/", "vi": "lưỡi câu cá bằng thép có ngạnh"},
  {"id": "lex.en.200k.064944", "hw": "forebears", "pos": "noun", "ipa": "/ˈfɔːrbɛərz/", "vi": "tổ tiên ông cha đời trước dòng họ"},
  {"id": "lex.en.200k.064945", "hw": "francophiles", "pos": "noun", "ipa": "/ˈfræŋkəˌfaɪlz/", "vi": "người yêu mến văn hóa nước Pháp"},
  {"id": "lex.en.200k.064946", "hw": "fumigated", "pos": "verb", "ipa": "/ˈfjuːməˌɡeɪtɪd/", "vi": "đã xông khói hóa chất diệt trùng"},
  {"id": "lex.en.200k.064947", "hw": "fumigates", "pos": "verb", "ipa": "/ˈfjuːməˌɡeɪts/", "vi": "xông khói khử trùng diệt sâu bọ"},
  {"id": "lex.en.200k.064948", "hw": "fumigating", "pos": "verb", "ipa": "/ˈfjuːməˌɡeɪtɪŋ/", "vi": "đang xông hơi khử trùng diệt khuẩn"},
  {"id": "lex.en.200k.064949", "hw": "gaboneses", "pos": "noun", "ipa": "/ˌɡæbəˈniːzɪz/", "vi": "công dân quốc gia Trung Phi Gabon"},
  {"id": "lex.en.200k.064950", "hw": "gbits", "pos": "noun", "ipa": "/ˈɡɪɡəbɪts/", "vi": "đơn vị dữ liệu truyền tải gigabit"},
  {"id": "lex.en.200k.064951", "hw": "gesells", "pos": "noun", "ipa": "/ɡəˈzɛlz/", "vi": "nhà tâm lý trẻ em Arnold Gesell"},
  {"id": "lex.en.200k.064952", "hw": "glassworkses", "pos": "noun", "ipa": "/ˈɡlæswɜːrksɪz/", "vi": "xưởng nhà máy sản xuất thủy tinh"},
  {"id": "lex.en.200k.064953", "hw": "gulus", "pos": "noun", "ipa": "/ˈɡuːluːz/", "vi": "thành phố Gulu ở miền bắc Uganda"},
  {"id": "lex.en.200k.064954", "hw": "hadjes", "pos": "noun", "ipa": "/ˈhædʒɪz/", "vi": "cuộc hành hương đến thánh địa Mecca"},
  {"id": "lex.en.200k.064955", "hw": "hadjs", "pos": "noun", "ipa": "/ˈhædʒɪz/", "vi": "lễ hành hương Hajj của người Hồi"},
  {"id": "lex.en.200k.064956", "hw": "hellesponts", "pos": "noun", "ipa": "/ˈhɛləspɑːnts/", "vi": "eo biển cổ Hellespont Dardanelles"},
  {"id": "lex.en.200k.064957", "hw": "heterodyned", "pos": "verb", "ipa": "/ˈhɛtərəˌdaɪnd/", "vi": "đã trộn phách tạo tần số sóng mới"},
  {"id": "lex.en.200k.064958", "hw": "heterodynes", "pos": "verb", "ipa": "/ˈhɛtərəˌdaɪnz/", "vi": "trộn tần số tạo tín hiệu phách mới"},
  {"id": "lex.en.200k.064959", "hw": "heterodyning", "pos": "verb", "ipa": "/ˈhɛtərəˌdaɪnɪŋ/", "vi": "đang trộn hai tần số vô tuyến sóng"},
  {"id": "lex.en.200k.064960", "hw": "hieratics", "pos": "noun", "ipa": "/ˌhaɪəˈrætɪks/", "vi": "chữ viết thảo thầy tu Ai Cập cổ"},
  {"id": "lex.en.200k.064961", "hw": "hindemiths", "pos": "noun", "ipa": "/ˈhɪndəmɪθs/", "vi": "nhà soạn nhạc Đức Paul Hindemith"},
  {"id": "lex.en.200k.064962", "hw": "homophones", "pos": "noun", "ipa": "/ˈhɑːməfoʊnz/", "vi": "từ đồng âm khác chữ viết và nghĩa"},
  {"id": "lex.en.200k.064963", "hw": "hostelries", "pos": "noun", "ipa": "/ˈhɑːstəlriz/", "vi": "quán trọ nhà khách kiểu cổ ấm cúng"},
  {"id": "lex.en.200k.064964", "hw": "hotplates", "pos": "noun", "ipa": "/ˈhɑːtpleɪts/", "vi": "bếp điện bàn đun nóng di động nhỏ"},
  {"id": "lex.en.200k.064965", "hw": "interlayers", "pos": "noun", "ipa": "/ˈɪntərˌleɪərz/", "vi": "lớp đệm xen kẽ giữa hai lớp vật"},
  {"id": "lex.en.200k.064966", "hw": "iseults", "pos": "noun", "ipa": "/ɪˈsuːlts/", "vi": "công chúa Iseult truyền thuyết"},
  {"id": "lex.en.200k.064967", "hw": "iskcons", "pos": "noun", "ipa": "/ˈɪskɑːnz/", "vi": "tổ chức Ý thức Krishna ISKCON"},
  {"id": "lex.en.200k.064968", "hw": "juniperuses", "pos": "noun", "ipa": "/dʒuːˈnɪpərəsɪz/", "vi": "chi cây thông bách xù Juniperus"},
  {"id": "lex.en.200k.064969", "hw": "khanates", "pos": "noun", "ipa": "/ˈkɑːneɪts/", "vi": "hãn quốc thời đế quốc Mông Cổ"},
  {"id": "lex.en.200k.064970", "hw": "lemnoses", "pos": "noun", "ipa": "/ˈlɛmnɑːsɪz/", "vi": "đảo Lemnos phía bắc biển Aegean"},
  {"id": "lex.en.200k.064971", "hw": "linguinis", "pos": "noun", "ipa": "/lɪŋˈɡwiːniz/", "vi": "mì dẹt Ý linguine ăn kèm hải sản"},
  {"id": "lex.en.200k.064972", "hw": "moussakas", "pos": "noun", "ipa": "/ˌmuːsəˈkɑːz/", "vi": "món cà tím thịt băm đút lò Hy Lạp"},
  {"id": "lex.en.200k.064973", "hw": "neuropsychiatries", "pos": "noun", "ipa": "/ˌnjʊroʊsaɪˈkaɪətriz/", "vi": "ngành y học thần kinh tâm thần"},
  {"id": "lex.en.200k.064974", "hw": "nightshirts", "pos": "noun", "ipa": "/ˈnaɪtʃɜːrts/", "vi": "áo sơ mi dáng dài mặc ngủ đêm"},
  {"id": "lex.en.200k.064975", "hw": "nurnbergs", "pos": "noun", "ipa": "/ˈnjʊrəmbɜːrɡz/", "vi": "thành phố Nuremberg miền nam Đức"},
  {"id": "lex.en.200k.064976", "hw": "orcuses", "pos": "noun", "ipa": "/ˈɔːrkəsɪz/", "vi": "thần âm phủ La Mã cổ đại Orcus"},
  {"id": "lex.en.200k.064977", "hw": "otuses", "pos": "noun", "ipa": "/ˈoʊtəsɪz/", "vi": "chi chim cú mèo nhỏ tai chùm Otus"},
  {"id": "lex.en.200k.064978", "hw": "pallbearers", "pos": "noun", "ipa": "/ˈpɔːlˌbɛrərz/", "vi": "người khiêng linh cữu trong tang lễ"},
  {"id": "lex.en.200k.064979", "hw": "pandanuses", "pos": "noun", "ipa": "/pænˈdeɪnəsɪz/", "vi": "chi cây dứa gai lá dứa Pandanus"},
  {"id": "lex.en.200k.064980", "hw": "parvos", "pos": "noun", "ipa": "/ˈpɑːrvoʊz/", "vi": "virus gây bệnh đường ruột parvo"},
  {"id": "lex.en.200k.064981", "hw": "passels", "pos": "noun", "ipa": "/ˈpæsəlz/", "vi": "bầy nhóm đông; vô số nhiều thứ (Mỹ)"},
  {"id": "lex.en.200k.064982", "hw": "phalaenopses", "pos": "noun", "ipa": "/ˌfælɪˈnɑːpsiz/", "vi": "loài hoa phong lan hồ điệp đẹp"},
  {"id": "lex.en.200k.064983", "hw": "picoseconds", "pos": "noun", "ipa": "/ˈpɪkoʊˌsɛkəndz/", "vi": "đơn vị một phần nghìn tỷ giây"},
  {"id": "lex.en.200k.064984", "hw": "pipits", "pos": "noun", "ipa": "/ˈpɪpɪts/", "vi": "chim manh đồng cỏ ăn sâu bọ"},
  {"id": "lex.en.200k.064985", "hw": "pitchier", "pos": "adj", "ipa": "/ˈpɪtʃiər/", "vi": "đen sẫm như hắc ín hơn; nhiều nhựa"},
  {"id": "lex.en.200k.064986", "hw": "pitchiest", "pos": "adj", "ipa": "/ˈpɪtʃiɪst/", "vi": "đen đặc như nhựa đường tối nhất"},
  {"id": "lex.en.200k.064987", "hw": "plagiarists", "pos": "noun", "ipa": "/ˈpleɪdʒərɪsts/", "vi": "kẻ đạo văn sao chép tác phẩm người"},
  {"id": "lex.en.200k.064988", "hw": "plastids", "pos": "noun", "ipa": "/ˈplæstɪdz/", "vi": "bào quan lạp thể trong tế bào cây"},
  {"id": "lex.en.200k.064989", "hw": "plectrums", "pos": "noun", "ipa": "/ˈplɛktrəmz/", "vi": "miếng gảy phím đàn dây plectrum"},
  {"id": "lex.en.200k.064990", "hw": "poperies", "pos": "noun", "ipa": "/ˈpoʊpəriz/", "vi": "đạo giáo hoàng (từ cũ miệt thị)"},
  {"id": "lex.en.200k.064991", "hw": "pyrenes", "pos": "noun", "ipa": "/ˈpaɪriːnz/", "vi": "hiđrocacbon thơm pyrene; hạch quả"},
  {"id": "lex.en.200k.064992", "hw": "quapaws", "pos": "noun", "ipa": "/ˈkwɑːpɔːz/", "vi": "bộ tộc bản địa Mỹ Quapaw"},
  {"id": "lex.en.200k.064993", "hw": "railheads", "pos": "noun", "ipa": "/ˈreɪlhɛdz/", "vi": "ga đầu mối cuối tuyến đường sắt"},
  {"id": "lex.en.200k.064994", "hw": "reticulates", "pos": "verb", "ipa": "/rɪˈtɪkjəˌleɪts/", "vi": "tạo thành mạng lưới đan chéo nhau"},
  {"id": "lex.en.200k.064995", "hw": "reticulating", "pos": "verb", "ipa": "/rɪˈtɪkjəˌleɪtɪŋ/", "vi": "đang nối thành mạng lưới chằng chịt"},
  {"id": "lex.en.200k.064996", "hw": "rhodopsins", "pos": "noun", "ipa": "/roʊˈdɑːpsɪnz/", "vi": "sắc tố thị giác nhạy sáng võng mạc"},
  {"id": "lex.en.200k.064997", "hw": "salutatorians", "pos": "noun", "ipa": "/səˌluːtəˈtɔːriənz/", "vi": "á khoa đọc diễn văn khai mạc tốt"},
  {"id": "lex.en.200k.064998", "hw": "sampans", "pos": "noun", "ipa": "/ˈsæmpænz/", "vi": "thuyền nan tam bản đáy bằng châu Á"},
  {"id": "lex.en.200k.064999", "hw": "sazeracs", "pos": "noun", "ipa": "/ˈsæzəˌræks/", "vi": "cocktail rượu whisky New Orleans"},
  {"id": "lex.en.200k.065000", "hw": "seleses", "pos": "noun", "ipa": "/ˈsɛlɪsɪz/", "vi": "tay vợt huyền thoại Monica Seles"},
  {"id": "lex.en.200k.065001", "hw": "selvedges", "pos": "noun", "ipa": "/ˈsɛlvɪdʒɪz/", "vi": "biên dệt mép vải chống tưa sợi"},
  {"id": "lex.en.200k.065002", "hw": "serrati", "pos": "noun", "ipa": "/səˈreɪtaɪ/", "vi": "các cơ răng cưa ở thành ngực lưng"}
]

with open('scratch/b33_r10_raw_p5.json') as f:
    raw = json.load(f)

assert len(items) == 100
assert len(raw) == 100

for i, (item, r) in enumerate(zip(items, raw)):
    assert item['id'] == r['id'], f"Mismatch id at {i}: {item['id']} vs {r['id']}"
    assert item['hw'] == r['hw'], f"Mismatch hw at {i}: {item['hw']} vs {r['hw']}"
    assert len(item['vi']) <= 35, f"vi length > 35 at {i} ({item['hw']}): {len(item['vi'])}"
    assert item['pos'] in ['noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'], f"Invalid pos at {i}: {item['pos']}"
    assert item['ipa'].startswith('/') and item['ipa'].endswith('/') and item['ipa'].count('/') == 2, f"Invalid ipa at {i}: {item['ipa']}"
    assert not item['ipa'][1:-1].startswith(' ') and not item['ipa'][1:-1].endswith(' '), f"Space in ipa at {i}: {item['ipa']}"
    r['pos'] = item['pos']
    r['ipa'] = item['ipa']
    r['vi'] = item['vi']
    r['status'] = 'reviewed'

with open('scratch/b33_r10_p5.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)
print("Saved scratch/b33_r10_p5.json OK")
