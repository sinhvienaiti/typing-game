import json

items = [
  {"id": "lex.en.200k.063503", "hw": "friggs", "pos": "noun", "ipa": "/frɪɡz/", "vi": "nữ thần hôn nhân Bắc Âu Frigg"},
  {"id": "lex.en.200k.063504", "hw": "grannies", "pos": "noun", "ipa": "/ˈɡrænɪz/", "vi": "bà ngoại; bà nội (thân mật)"},
  {"id": "lex.en.200k.063505", "hw": "hasidims", "pos": "noun", "ipa": "/həˈsiːdɪmz/", "vi": "tín đồ Do Thái giáo chính thống"},
  {"id": "lex.en.200k.063506", "hw": "haylofts", "pos": "noun", "ipa": "/ˈheɪlɔːfts/", "vi": "gác xép chứa cỏ khô trong chuồng"},
  {"id": "lex.en.200k.063507", "hw": "helicons", "pos": "noun", "ipa": "/ˈhɛlɪkɑːnz/", "vi": "kèn đồng trầm cỡ lớn đeo vai"},
  {"id": "lex.en.200k.063508", "hw": "hellhounds", "pos": "noun", "ipa": "/ˈhɛlhaʊndz/", "vi": "chó săn địa ngục; kẻ tàn bạo độc ác"},
  {"id": "lex.en.200k.063509", "hw": "hematocrits", "pos": "noun", "ipa": "/hɪˈmætəkrɪts/", "vi": "tỷ lệ thể tích hồng cầu trong máu"},
  {"id": "lex.en.200k.063510", "hw": "heths", "pos": "noun", "ipa": "/hɛθs/", "vi": "chữ cái Do Thái và Phoenicia Heth"},
  {"id": "lex.en.200k.063511", "hw": "hexagrams", "pos": "noun", "ipa": "/ˈhɛksəɡræmz/", "vi": "hình sao sáu cánh; quẻ Kinh Dịch"},
  {"id": "lex.en.200k.063512", "hw": "hydroplaned", "pos": "verb", "ipa": "/ˈhaɪdroʊpleɪnd/", "vi": "đã trượt bánh trên nước; lướt nước"},
  {"id": "lex.en.200k.063513", "hw": "hydroplanes", "pos": "noun", "ipa": "/ˈhaɪdroʊpleɪnz/", "vi": "thủy phi cơ; tàu cánh lướt mặt nước"},
  {"id": "lex.en.200k.063514", "hw": "hydroplaning", "pos": "verb", "ipa": "/ˈhaɪdroʊˌpleɪnɪŋ/", "vi": "đang trượt bánh trên mặt nước mưa"},
  {"id": "lex.en.200k.063515", "hw": "hyperlipidemias", "pos": "noun", "ipa": "/ˌhaɪpərˌlɪpɪˈdiːmiəz/", "vi": "chứng rối loạn tăng mỡ máu cao"},
  {"id": "lex.en.200k.063516", "hw": "icefalls", "pos": "noun", "ipa": "/ˈaɪsfɔːlz/", "vi": "thác băng nứt gãy trên sông băng"},
  {"id": "lex.en.200k.063517", "hw": "inannas", "pos": "noun", "ipa": "/ɪˈnænəz/", "vi": "nữ thần tình yêu chiến tranh Inanna"},
  {"id": "lex.en.200k.063518", "hw": "ironsideses", "pos": "noun", "ipa": "/ˈaɪərnsaɪdzɪz/", "vi": "kỵ binh Sườn Sắt thời Cromwell"},
  {"id": "lex.en.200k.063519", "hw": "jras", "pos": "noun", "ipa": "/ˌdʒeɪˌɑːrˈeɪz/", "vi": "nhóm cực đoan Hồng quân Nhật Bản"},
  {"id": "lex.en.200k.063520", "hw": "kahluas", "pos": "noun", "ipa": "/kəˈluːəz/", "vi": "rượu mùi cà phê Mexico Kahlúa"},
  {"id": "lex.en.200k.063521", "hw": "kamasutras", "pos": "noun", "ipa": "/ˌkɑːməˈsuːtrəz/", "vi": "sách cổ Ấn Độ Kama Sutra"},
  {"id": "lex.en.200k.063522", "hw": "kutuzovs", "pos": "noun", "ipa": "/kuˈtuːzəfs/", "vi": "nguyên soái Nga Mikhail Kutuzov"},
  {"id": "lex.en.200k.063523", "hw": "larousses", "pos": "noun", "ipa": "/ləˈruːsɪz/", "vi": "nhà xuất bản từ điển Pháp Larousse"},
  {"id": "lex.en.200k.063524", "hw": "lomes", "pos": "noun", "ipa": "/loʊˈmeɪz/", "vi": "thủ đô cảng Lomé của nước Togo"},
  {"id": "lex.en.200k.063525", "hw": "maisonettes", "pos": "noun", "ipa": "/ˌmeɪzəˈnɛts/", "vi": "căn hộ thông hai tầng có lối riêng"},
  {"id": "lex.en.200k.063526", "hw": "marchers", "pos": "noun", "ipa": "/ˈmɑːrtʃərz/", "vi": "người diễu hành; người vùng biên ải"},
  {"id": "lex.en.200k.063527", "hw": "meetinghouses", "pos": "noun", "ipa": "/ˈmiːtɪŋhaʊzɪz/", "vi": "nhà hội họp cộng đồng; giáo đường"},
  {"id": "lex.en.200k.063528", "hw": "menuhins", "pos": "noun", "ipa": "/ˈmɛnjʊɪnz/", "vi": "nghệ sĩ vĩ cầm thiên tài Menuhin"},
  {"id": "lex.en.200k.063529", "hw": "meteoroids", "pos": "noun", "ipa": "/ˈmiːtiərɔɪdz/", "vi": "thiên thạch nhỏ bay trong vũ trụ"},
  {"id": "lex.en.200k.063530", "hw": "mnemosynes", "pos": "noun", "ipa": "/nɪˈmɑːsəniːz/", "vi": "nữ thần ký ức Hy Lạp cổ Mnemosyne"},
  {"id": "lex.en.200k.063531", "hw": "naturopaths", "pos": "noun", "ipa": "/ˈneɪtʃərəˌpæθs/", "vi": "thầy thuốc trị liệu tự nhiên"},
  {"id": "lex.en.200k.063532", "hw": "occitans", "pos": "noun", "ipa": "/ˈɑːksɪtənz/", "vi": "người và tiếng Occitan ở nam Pháp"},
  {"id": "lex.en.200k.063533", "hw": "oligosaccharides", "pos": "noun", "ipa": "/ˌɑːlɪɡoʊˈsækəˌraɪdz/", "vi": "chuỗi đường ngắn oligosaccharide"},
  {"id": "lex.en.200k.063534", "hw": "omdurmans", "pos": "noun", "ipa": "/ˌɑːmdərˈmɑːnz/", "vi": "thành phố lớn Omdurman của Sudan"},
  {"id": "lex.en.200k.063535", "hw": "organophosphates", "pos": "noun", "ipa": "/ɔːrˌɡænoʊˈfɑːsfeɪts/", "vi": "hóa chất lân hữu cơ trừ sâu độc"},
  {"id": "lex.en.200k.063536", "hw": "outstations", "pos": "noun", "ipa": "/ˈaʊtˌsteɪʃənz/", "vi": "trạm công tác hẻo lánh ở vùng xa"},
  {"id": "lex.en.200k.063537", "hw": "phylloxerae", "pos": "noun", "ipa": "/ˌfɪlɑːkˈsɪriː/", "vi": "rệp hút nhựa hại rễ cây nho"},
  {"id": "lex.en.200k.063538", "hw": "phylloxeras", "pos": "noun", "ipa": "/ˌfɪlɑːkˈsɪrəz/", "vi": "các loài rệp hại rễ lá cây nho"},
  {"id": "lex.en.200k.063539", "hw": "pitons", "pos": "noun", "ipa": "/ˈpiːtɑːnz/", "vi": "móc sắt đóng vách đá để leo núi"},
  {"id": "lex.en.200k.063540", "hw": "pitots", "pos": "noun", "ipa": "/piˈtoʊz/", "vi": "ống đo tốc độ dòng chảy khí Pitot"},
  {"id": "lex.en.200k.063541", "hw": "poulets", "pos": "noun", "ipa": "/puˈleɪz/", "vi": "món gà kiểu Pháp; thư tình gấp gọn"},
  {"id": "lex.en.200k.063542", "hw": "priapisms", "pos": "noun", "ipa": "/ˈpraɪəˌpɪzəmz/", "vi": "chứng cương dương kéo dài gây đau"},
  {"id": "lex.en.200k.063543", "hw": "pronations", "pos": "noun", "ipa": "/proʊˈneɪʃənz/", "vi": "động tác xoay sấp bàn tay hoặc chân"},
  {"id": "lex.en.200k.063544", "hw": "ragis", "pos": "noun", "ipa": "/ˈrɑːɡiz/", "vi": "cây kê ngón tay châu Phi Ấn Độ"},
  {"id": "lex.en.200k.063545", "hw": "reconfirmed", "pos": "verb", "ipa": "/ˌriːkənˈfɜːrmd/", "vi": "đã tái xác nhận lại lần nữa"},
  {"id": "lex.en.200k.063546", "hw": "reconfirming", "pos": "verb", "ipa": "/ˌriːkənˈfɜːrmɪŋ/", "vi": "đang tái xác nhận lại thông tin"},
  {"id": "lex.en.200k.063547", "hw": "reconfirms", "pos": "verb", "ipa": "/ˌriːkənˈfɜːrmz/", "vi": "tái xác nhận lại chắc chắn thêm"},
  {"id": "lex.en.200k.063548", "hw": "reconnoitered", "pos": "verb", "ipa": "/ˌrɛkəˈnɔɪtərd/", "vi": "đã trinh sát thám thính địa hình"},
  {"id": "lex.en.200k.063549", "hw": "reconnoiters", "pos": "verb", "ipa": "/ˌrɛkəˈnɔɪtərz/", "vi": "trinh sát do thám thăm dò địa bàn"},
  {"id": "lex.en.200k.063550", "hw": "rhuses", "pos": "noun", "ipa": "/ˈruːsɪz/", "vi": "chi cây sơn độc và sumac gia vị"},
  {"id": "lex.en.200k.063551", "hw": "rohypnols", "pos": "noun", "ipa": "/roʊˈhɪpnɔːlz/", "vi": "thuốc ngủ gây mê mạnh Rohypnol"},
  {"id": "lex.en.200k.063552", "hw": "rombergs", "pos": "noun", "ipa": "/ˈrɑːmbɜːrɡz/", "vi": "bác sĩ thần kinh học Đức Romberg"},
  {"id": "lex.en.200k.063553", "hw": "runups", "pos": "noun", "ipa": "/ˈrʌnʌps/", "vi": "đà tăng vọt nhanh trước sự kiện"},
  {"id": "lex.en.200k.063554", "hw": "schlepped", "pos": "verb", "ipa": "/ʃlɛpt/", "vi": "đã khuân vác nặng nhọc; lết đi"},
  {"id": "lex.en.200k.063555", "hw": "schlepping", "pos": "verb", "ipa": "/ˈʃlɛpɪŋ/", "vi": "đang khuân vác lê lết đi đường xa"},
  {"id": "lex.en.200k.063556", "hw": "seljuks", "pos": "noun", "ipa": "/sɛlˈdʒuːks/", "vi": "triều đại Thổ Nhĩ Kỳ cổ Seljuk"},
  {"id": "lex.en.200k.063557", "hw": "sideswiped", "pos": "verb", "ipa": "/ˈsaɪdswaɪpt/", "vi": "đã quẹt va chạm sườn xe; công kích"},
  {"id": "lex.en.200k.063558", "hw": "sideswipes", "pos": "noun", "ipa": "/ˈsaɪdswaɪps/", "vi": "cú quẹt ngang sườn; lời đả kích xéo"},
  {"id": "lex.en.200k.063559", "hw": "sideswiping", "pos": "verb", "ipa": "/ˈsaɪdswaɪpɪŋ/", "vi": "đang quẹt ngang sườn xe; nói móc"},
  {"id": "lex.en.200k.063560", "hw": "siroccos", "pos": "noun", "ipa": "/səˈrɑːkoʊz/", "vi": "gió nóng khô bụi từ sa mạc Sahara"},
  {"id": "lex.en.200k.063561", "hw": "slapshots", "pos": "noun", "ipa": "/ˈslæpʃɑːts/", "vi": "cú vung gậy đánh mạnh khúc côn cầu"},
  {"id": "lex.en.200k.063562", "hw": "specialnesses", "pos": "noun", "ipa": "/ˈspɛʃəlnəsɪz/", "vi": "nét đặc biệt riêng biệt hiếm có"},
  {"id": "lex.en.200k.063563", "hw": "stationmasters", "pos": "noun", "ipa": "/ˈsteɪʃənˌmæstərz/", "vi": "trưởng ga phụ trách nhà ga tàu hỏa"},
  {"id": "lex.en.200k.063564", "hw": "steelworkers", "pos": "noun", "ipa": "/ˈstiːlˌwɜːrkərz/", "vi": "công nhân luyện thép nhà máy thép"},
  {"id": "lex.en.200k.063565", "hw": "stipendiaries", "pos": "noun", "ipa": "/staɪˈpɛndiˌɛriz/", "vi": "thẩm phán chuyên trách ăn lương"},
  {"id": "lex.en.200k.063566", "hw": "stomatitises", "pos": "noun", "ipa": "/ˌstoʊməˈtaɪtɪsɪz/", "vi": "chứng viêm loét niêm mạc miệng"},
  {"id": "lex.en.200k.063567", "hw": "supplicants", "pos": "noun", "ipa": "/ˈsʌplɪkənts/", "vi": "người khẩn cầu tha thiết; tín đồ"},
  {"id": "lex.en.200k.063568", "hw": "symphyses", "pos": "noun", "ipa": "/ˈsɪmfəsiːz/", "vi": "khớp sụn giữa hai xương; khớp mu"},
  {"id": "lex.en.200k.063569", "hw": "syphilitics", "pos": "noun", "ipa": "/ˌsɪfəˈlɪtɪks/", "vi": "bệnh nhân mắc bệnh giang mai"},
  {"id": "lex.en.200k.063570", "hw": "temblors", "pos": "noun", "ipa": "/ˈtɛmblərz/", "vi": "trận động đất rung chuyển địa chấn"},
  {"id": "lex.en.200k.063571", "hw": "terpenes", "pos": "noun", "ipa": "/ˈtɜːrpiːnz/", "vi": "hợp chất hương thơm tự nhiên terpen"},
  {"id": "lex.en.200k.063572", "hw": "tinkerers", "pos": "noun", "ipa": "/ˈtɪŋkərərz/", "vi": "người thích mày mò sửa chữa đồ vặt"},
  {"id": "lex.en.200k.063573", "hw": "trameled", "pos": "verb", "ipa": "/ˈtræməld/", "vi": "đã cản trở kìm hãm; đã vướng lưới"},
  {"id": "lex.en.200k.063574", "hw": "trameling", "pos": "verb", "ipa": "/ˈtræməlɪŋ/", "vi": "đang gây cản trở hạn chế; vướng bẫy"},
  {"id": "lex.en.200k.063575", "hw": "tramelled", "pos": "verb", "ipa": "/ˈtræməld/", "vi": "đã kìm hãm trói buộc tự do (Anh)"},
  {"id": "lex.en.200k.063576", "hw": "tramelling", "pos": "verb", "ipa": "/ˈtræməlɪŋ/", "vi": "đang cản trở trói buộc (viết Anh)"},
  {"id": "lex.en.200k.063577", "hw": "tramels", "pos": "verb", "ipa": "/ˈtræməlz/", "vi": "cản trở hạn chế; trói buộc tự do"},
  {"id": "lex.en.200k.063578", "hw": "trammeled", "pos": "verb", "ipa": "/ˈtræməld/", "vi": "đã cản trở hạn chế quyền tự do"},
  {"id": "lex.en.200k.063579", "hw": "trammeling", "pos": "verb", "ipa": "/ˈtræməlɪŋ/", "vi": "đang kìm hãm hạn chế tự do"},
  {"id": "lex.en.200k.063580", "hw": "transferrins", "pos": "noun", "ipa": "/trænsˈfɛrɪnz/", "vi": "protein vận chuyển sắt trong huyết"},
  {"id": "lex.en.200k.063581", "hw": "utopianisms", "pos": "noun", "ipa": "/juːˈtoʊpiəˌnɪzəmz/", "vi": "tư tưởng xã hội không tưởng hoàn mỹ"},
  {"id": "lex.en.200k.063582", "hw": "verwoerds", "pos": "noun", "ipa": "/fərˈvʊərtz/", "vi": "thủ tướng Nam Phi Hendrik Verwoerd"},
  {"id": "lex.en.200k.063583", "hw": "videocassettes", "pos": "noun", "ipa": "/ˈvɪdioʊkəˌsɛts/", "vi": "băng từ video ghi hình hộp nhựa"},
  {"id": "lex.en.200k.063584", "hw": "waxworks", "pos": "noun", "ipa": "/ˈwækswɜːrks/", "vi": "tượng sáp trưng bày; bảo tàng sáp"},
  {"id": "lex.en.200k.063585", "hw": "wickliffes", "pos": "noun", "ipa": "/ˈwɪklɪfs/", "vi": "nhà cải cách Anh John Wycliffe"},
  {"id": "lex.en.200k.063586", "hw": "workmates", "pos": "noun", "ipa": "/ˈwɜːrkmeɪts/", "vi": "đồng nghiệp làm việc cùng cơ quan"},
  {"id": "lex.en.200k.063587", "hw": "allium cepa", "pos": "phrase", "ipa": "/ˈæliəm ˈsiːpə/", "vi": "cây hành tây củ gia vị phổ biến"},
  {"id": "lex.en.200k.063588", "hw": "antiarrhythmic drug", "pos": "phrase", "ipa": "/ˌæntiəˈrɪðmɪk drʌɡ/", "vi": "thuốc điều hòa chống loạn nhịp tim"},
  {"id": "lex.en.200k.063589", "hw": "antiarrhythmic medication", "pos": "phrase", "ipa": "/ˌæntiəˈrɪðmɪk ˌmɛdɪˈkeɪʃən/", "vi": "thuốc chữa chứng rối loạn nhịp tim"},
  {"id": "lex.en.200k.063590", "hw": "antipersonnel bomb", "pos": "phrase", "ipa": "/ˌæntipɜːrsəˈnɛl bɑːm/", "vi": "bom bi sát thương gây hại bộ binh"},
  {"id": "lex.en.200k.063591", "hw": "antipodal opposition", "pos": "phrase", "ipa": "/ænˈtɪpədəl ˌɑːpəˈzɪʃən/", "vi": "sự đối lập hoàn toàn ở hai thái cực"},
  {"id": "lex.en.200k.063592", "hw": "avogadro number", "pos": "phrase", "ipa": "/ˌɑːvəˈɡɑːdroʊ ˈnʌmbər/", "vi": "hằng số hạt Avogadro trong một mol"},
  {"id": "lex.en.200k.063593", "hw": "baroness karen blixen", "pos": "phrase", "ipa": "/ˈbærənəs ˈkærən ˈblɪksən/", "vi": "nữ văn sĩ Đan Mạch Karen Blixen"},
  {"id": "lex.en.200k.063594", "hw": "bayberry wax", "pos": "phrase", "ipa": "/ˈbeɪˌbɛri wæks/", "vi": "sáp quả thanh mai làm nến thơm"},
  {"id": "lex.en.200k.063595", "hw": "bedlington terrier", "pos": "phrase", "ipa": "/ˈbɛdlɪŋtən ˈtɛriər/", "vi": "chó sục Bedlington lông xù như cừu"},
  {"id": "lex.en.200k.063596", "hw": "berberis vulgaris", "pos": "phrase", "ipa": "/ˈbɜːrbərɪs vʌlˈɡɛrɪs/", "vi": "cây hoàng liên gai châu Âu quả đỏ"},
  {"id": "lex.en.200k.063597", "hw": "binary numeration system", "pos": "phrase", "ipa": "/ˈbaɪˌnɛri ˌnuːməˈreɪʃən ˈsɪstəm/", "vi": "hệ thống đếm cơ số hai nhị phân"},
  {"id": "lex.en.200k.063598", "hw": "boron trifluoride", "pos": "phrase", "ipa": "/ˈbɔːrɑːn traɪˈflʊraɪd/", "vi": "khí hóa học xúc tác bo triflorua"},
  {"id": "lex.en.200k.063599", "hw": "bronislaw kasper malinowski", "pos": "phrase", "ipa": "/ˈbrɔːnɪslɑːf ˈkɑːspər ˌmɑːlɪˈnɔːfski/", "vi": "nhà nhân học Ba Lan Malinowski"},
  {"id": "lex.en.200k.063600", "hw": "cervix uteri", "pos": "phrase", "ipa": "/ˈsɜːrvɪks ˈjuːtəraɪ/", "vi": "cổ tử cung nối thân tử cung âm đạo"},
  {"id": "lex.en.200k.063601", "hw": "clammy chickweed", "pos": "phrase", "ipa": "/ˈklæmi ˈtʃɪkwiːd/", "vi": "cây cỏ tai chuột thân dính nhớt"},
  {"id": "lex.en.200k.063602", "hw": "dail eireann", "pos": "phrase", "ipa": "/dɔɪl ˈɛərən/", "vi": "Hạ viện trong quốc hội Ireland"}
]

with open('scratch/b33_r08_raw_p1.json') as f:
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

with open('scratch/b33_r08_p1.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)
print("Saved scratch/b33_r08_p1.json OK")
