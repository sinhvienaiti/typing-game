import json

items = [
  {"id": "lex.en.200k.060303", "hw": "coahuilas", "pos": "noun", "ipa": "/ˌkoʊɑːˈwiːləz/", "vi": "bang Coahuila ở miền bắc Mexico"},
  {"id": "lex.en.200k.060304", "hw": "crappers", "pos": "noun", "ipa": "/ˈkræpərz/", "vi": "nhà vệ sinh; bồn cầu xí bệt"},
  {"id": "lex.en.200k.060305", "hw": "crashers", "pos": "noun", "ipa": "/ˈkræʃərz/", "vi": "kẻ dự tiệc chui không được mời"},
  {"id": "lex.en.200k.060306", "hw": "culebras", "pos": "noun", "ipa": "/kʊˈlɛbrəz/", "vi": "đảo Culebra thuộc Puerto Rico"},
  {"id": "lex.en.200k.060307", "hw": "daces", "pos": "noun", "ipa": "/deɪsɪz/", "vi": "loài cá chép nhỏ vảy bạc nước ngọt"},
  {"id": "lex.en.200k.060308", "hw": "deadheads", "pos": "noun", "ipa": "/ˈdɛdhɛdz/", "vi": "người đi vé miễn phí; bông hoa héo"},
  {"id": "lex.en.200k.060309", "hw": "deists", "pos": "noun", "ipa": "/ˈdiːɪsts/", "vi": "người theo thuyết tự nhiên thần"},
  {"id": "lex.en.200k.060310", "hw": "depardieus", "pos": "noun", "ipa": "/dəpɑːrˈdjɜːz/", "vi": "tài tử điện ảnh Gérard Depardieu"},
  {"id": "lex.en.200k.060311", "hw": "depersonalizations", "pos": "noun", "ipa": "/diːˌpɜːrsənələˈzeɪʃənz/", "vi": "chứng giải thể nhân cách tâm thần"},
  {"id": "lex.en.200k.060312", "hw": "divots", "pos": "noun", "ipa": "/ˈdɪvəts/", "vi": "mảng cỏ tróc lên khi đánh gôn"},
  {"id": "lex.en.200k.060313", "hw": "drippier", "pos": "adj", "ipa": "/ˈdrɪpiər/", "vi": "nhỏ giọt nhiều hơn; ướt sũng hơn"},
  {"id": "lex.en.200k.060314", "hw": "drippiest", "pos": "adj", "ipa": "/ˈdrɪpiɪst/", "vi": "nhỏ giọt nhiều nhất; ướt đẫm nhất"},
  {"id": "lex.en.200k.060315", "hw": "dryades", "pos": "noun", "ipa": "/ˈdraɪədiːz/", "vi": "nữ thần rừng cây thần thoại Hy Lạp"},
  {"id": "lex.en.200k.060316", "hw": "duffers", "pos": "noun", "ipa": "/ˈdʌfərz/", "vi": "người chơi vụng về; lão già lẩm cẩm"},
  {"id": "lex.en.200k.060317", "hw": "dulcimers", "pos": "noun", "ipa": "/ˈdʌlsɪmərz/", "vi": "đàn tam thập lục; đàn dây gõ"},
  {"id": "lex.en.200k.060318", "hw": "durkheims", "pos": "noun", "ipa": "/ˈdɜːrkhaɪmz/", "vi": "nhà xã hội học Émile Durkheim"},
  {"id": "lex.en.200k.060319", "hw": "ernes", "pos": "noun", "ipa": "/ɜːrnz/", "vi": "chim đại bàng biển đuôi trắng"},
  {"id": "lex.en.200k.060320", "hw": "farmhands", "pos": "noun", "ipa": "/ˈfɑːrmhændz/", "vi": "người làm công thuê ở nông trại"},
  {"id": "lex.en.200k.060321", "hw": "fermats", "pos": "noun", "ipa": "/fɛərˈmɑːz/", "vi": "nhà toán học Pháp Pierre de Fermat"},
  {"id": "lex.en.200k.060322", "hw": "finials", "pos": "noun", "ipa": "/ˈfɪniəlz/", "vi": "chóp nhọn trang trí đỉnh mái nhà"},
  {"id": "lex.en.200k.060323", "hw": "floorboards", "pos": "noun", "ipa": "/ˈflɔːrbɔːrdz/", "vi": "tấm ván lát sàn nhà bằng gỗ"},
  {"id": "lex.en.200k.060324", "hw": "forebrains", "pos": "noun", "ipa": "/ˈfɔːrbreɪnz/", "vi": "vùng não trước của hệ thần kinh"},
  {"id": "lex.en.200k.060325", "hw": "framers", "pos": "noun", "ipa": "/ˈfreɪmərz/", "vi": "thợ đóng khung; nhà lập hiến"},
  {"id": "lex.en.200k.060326", "hw": "frapped", "pos": "verb", "ipa": "/fræpt/", "vi": "đã quấn dây chằng buộc thật chặt"},
  {"id": "lex.en.200k.060327", "hw": "frapping", "pos": "verb", "ipa": "/ˈfræpɪŋ/", "vi": "đang quấn dây chằng buộc chặt"},
  {"id": "lex.en.200k.060328", "hw": "fraps", "pos": "verb", "ipa": "/fræps/", "vi": "quấn dây thừng chằng buộc chặt"},
  {"id": "lex.en.200k.060329", "hw": "gadflies", "pos": "noun", "ipa": "/ˈɡædflaɪz/", "vi": "con ruồi trâu; kẻ hay châm chọc"},
  {"id": "lex.en.200k.060330", "hw": "galans", "pos": "noun", "ipa": "/ɡəˈlɑːnz/", "vi": "miệng núi lửa Galán ở Argentina"},
  {"id": "lex.en.200k.060331", "hw": "glias", "pos": "noun", "ipa": "/ˈɡliːəz/", "vi": "mô thần kinh đệm nâng đỡ nơ-ron"},
  {"id": "lex.en.200k.060332", "hw": "gobies", "pos": "noun", "ipa": "/ˈɡoʊbiz/", "vi": "loài cá bống nhỏ sống đáy nước"},
  {"id": "lex.en.200k.060333", "hw": "gumshoes", "pos": "noun", "ipa": "/ˈɡʌmʃuːz/", "vi": "giày đế cao su; thám tử tư"},
  {"id": "lex.en.200k.060334", "hw": "haemophilias", "pos": "noun", "ipa": "/ˌhiːməˈfɪliəz/", "vi": "bệnh máu khó đông di truyền"},
  {"id": "lex.en.200k.060335", "hw": "hayfields", "pos": "noun", "ipa": "/ˈheɪfiːldz/", "vi": "cánh đồng trồng cỏ làm cỏ khô"},
  {"id": "lex.en.200k.060336", "hw": "hebes", "pos": "noun", "ipa": "/ˈhiːbiːz/", "vi": "nữ thần tuổi trẻ Hebe Hy Lạp"},
  {"id": "lex.en.200k.060337", "hw": "hibachis", "pos": "noun", "ipa": "/hɪˈbɑːtʃiz/", "vi": "lò nướng than hồng kiểu Nhật Bản"},
  {"id": "lex.en.200k.060338", "hw": "hoagies", "pos": "noun", "ipa": "/ˈhoʊɡiz/", "vi": "ổ bánh mì dài kẹp thịt nguội rau"},
  {"id": "lex.en.200k.060339", "hw": "homburgs", "pos": "noun", "ipa": "/ˈhɑːmbɜːrɡz/", "vi": "mũ phớt dạ chóp lõm Homburg"},
  {"id": "lex.en.200k.060340", "hw": "inducers", "pos": "noun", "ipa": "/ɪnˈduːsərz/", "vi": "chất gây cảm ứng sinh hóa học"},
  {"id": "lex.en.200k.060341", "hw": "insteps", "pos": "noun", "ipa": "/ˈɪnstɛps/", "vi": "phần vòm mu bàn chân con người"},
  {"id": "lex.en.200k.060342", "hw": "jobcentres", "pos": "noun", "ipa": "/ˈdʒɑːbsɛntərz/", "vi": "trung tâm môi giới việc làm Anh"},
  {"id": "lex.en.200k.060343", "hw": "jockstraps", "pos": "noun", "ipa": "/ˈdʒɑːkstræps/", "vi": "đai quần lót bảo hộ thể thao nam"},
  {"id": "lex.en.200k.060344", "hw": "joppas", "pos": "noun", "ipa": "/ˈdʒɑːpəz/", "vi": "thành phố cảng cổ Joppa ở Israel"},
  {"id": "lex.en.200k.060345", "hw": "jottings", "pos": "noun", "ipa": "/ˈdʒɑːtɪŋz/", "vi": "mẩu ghi chép nhanh ngắn gọn"},
  {"id": "lex.en.200k.060346", "hw": "jynxes", "pos": "noun", "ipa": "/ˈdʒɪŋksɪz/", "vi": "loài chim vẹo cổ họ Gõ kiến"},
  {"id": "lex.en.200k.060347", "hw": "kerchiefs", "pos": "noun", "ipa": "/ˈkɜːrtʃɪfs/", "vi": "chiếc khăn vuông trùm đầu quàng cổ"},
  {"id": "lex.en.200k.060348", "hw": "kingfishes", "pos": "noun", "ipa": "/ˈkɪŋfɪʃɪz/", "vi": "loài cá thu vạch lớn câu thể thao"},
  {"id": "lex.en.200k.060349", "hw": "kingwoods", "pos": "noun", "ipa": "/ˈkɪŋwʊdz/", "vi": "gỗ cẩm lai tím quý hiếm Nam Mỹ"},
  {"id": "lex.en.200k.060350", "hw": "klutzes", "pos": "noun", "ipa": "/ˈklʌtsɪz/", "vi": "người hậu đậu vụng về lóng ngóng"},
  {"id": "lex.en.200k.060351", "hw": "knobbier", "pos": "adj", "ipa": "/ˈnɑːbiər/", "vi": "nhiều mấu u cục gồ ghề hơn"},
  {"id": "lex.en.200k.060352", "hw": "knobbiest", "pos": "adj", "ipa": "/ˈnɑːbiɪst/", "vi": "nhiều u bướu mấu sần sùi nhất"},
  {"id": "lex.en.200k.060353", "hw": "kwanzaas", "pos": "noun", "ipa": "/ˈkwɑːnzəz/", "vi": "lễ hội văn hóa người Mỹ gốc Phi"},
  {"id": "lex.en.200k.060354", "hw": "laerteses", "pos": "noun", "ipa": "/leɪˈɜːrtiːzɪz/", "vi": "nhân vật Laertes trong kịch Hamlet"},
  {"id": "lex.en.200k.060355", "hw": "larkspurs", "pos": "noun", "ipa": "/ˈlɑːrkspɜːrz/", "vi": "cây hoa phi yến chùm xanh tím"},
  {"id": "lex.en.200k.060356", "hw": "lassas", "pos": "noun", "ipa": "/ˈlɑːsəz/", "vi": "bệnh sốt xuất huyết vi-rút Lassa"},
  {"id": "lex.en.200k.060357", "hw": "linnets", "pos": "noun", "ipa": "/ˈlɪnɪts/", "vi": "loài chim sẻ hồng hót hay châu Âu"},
  {"id": "lex.en.200k.060358", "hw": "lordlier", "pos": "adj", "ipa": "/ˈlɔːrdliər/", "vi": "oai vệ quý phái hơn; kiêu kỳ hơn"},
  {"id": "lex.en.200k.060359", "hw": "lordliest", "pos": "adj", "ipa": "/ˈlɔːrdliɪst/", "vi": "oai vệ quý phái nhất; kiêu kỳ nhất"},
  {"id": "lex.en.200k.060360", "hw": "lowballed", "pos": "verb", "ipa": "/ˈloʊbɔːld/", "vi": "đã cố tình ép giá trả giá quá thấp"},
  {"id": "lex.en.200k.060361", "hw": "lowballing", "pos": "verb", "ipa": "/ˈloʊbɔːlɪŋ/", "vi": "đang cố tình trả giá thấp ép giá"},
  {"id": "lex.en.200k.060362", "hw": "lowballs", "pos": "verb", "ipa": "/ˈloʊbɔːlz/", "vi": "cố tình đưa mức giá thấp lừa khách"},
  {"id": "lex.en.200k.060363", "hw": "lutheranisms", "pos": "noun", "ipa": "/ˈluːθərənɪzəmz/", "vi": "giáo phái Tin Lành dòng Luther"},
  {"id": "lex.en.200k.060364", "hw": "masers", "pos": "noun", "ipa": "/ˈmeɪzərz/", "vi": "thiết bị khuếch đại bức xạ vi sóng"},
  {"id": "lex.en.200k.060365", "hw": "masouds", "pos": "noun", "ipa": "/məˈsuːdz/", "vi": "thủ lĩnh kháng chiến Ahmad Massoud"},
  {"id": "lex.en.200k.060366", "hw": "merchandisers", "pos": "noun", "ipa": "/ˈmɜːrtʃəndaɪzərz/", "vi": "chuyên viên trưng bày hàng bán lẻ"},
  {"id": "lex.en.200k.060367", "hw": "midgards", "pos": "noun", "ipa": "/ˈmɪdɡɑːrdz/", "vi": "cõi người trần Midgard Bắc Âu"},
  {"id": "lex.en.200k.060368", "hw": "monkfishes", "pos": "noun", "ipa": "/ˈmʌŋkfɪʃɪz/", "vi": "loài cá vây chân đầu to biển sâu"},
  {"id": "lex.en.200k.060369", "hw": "monteverdis", "pos": "noun", "ipa": "/ˌmɑːntəˈvɛərdiz/", "vi": "nhà soạn nhạc Ý Claudio Monteverdi"},
  {"id": "lex.en.200k.060370", "hw": "mouldered", "pos": "verb", "ipa": "/ˈmoʊldərd/", "vi": "đã mục rữa phân hủy thành tro bụi"},
  {"id": "lex.en.200k.060371", "hw": "mouldering", "pos": "verb", "ipa": "/ˈmoʊldərɪŋ/", "vi": "đang mục nát thối rữa dần dần"},
  {"id": "lex.en.200k.060372", "hw": "moulders", "pos": "verb", "ipa": "/ˈmoʊldərz/", "vi": "mục rữa thối nát theo thời gian"},
  {"id": "lex.en.200k.060373", "hw": "nootkas", "pos": "noun", "ipa": "/ˈnuːtkəz/", "vi": "thổ dân Nootka đảo Vancouver"},
  {"id": "lex.en.200k.060374", "hw": "nucleons", "pos": "noun", "ipa": "/ˈnuːkliɑːnz/", "vi": "hạt cấu tạo nhân nguyên tử nucleon"},
  {"id": "lex.en.200k.060375", "hw": "nungs", "pos": "noun", "ipa": "/nʊŋz/", "vi": "dân tộc Nùng; tiếng nói người Nùng"},
  {"id": "lex.en.200k.060376", "hw": "outcalled", "pos": "verb", "ipa": "/aʊtˈkɔːld/", "vi": "đã gọi to át tiếng; đã tố cao hơn"},
  {"id": "lex.en.200k.060377", "hw": "outcalling", "pos": "verb", "ipa": "/aʊtˈkɔːlɪŋ/", "vi": "đang gọi lớn hơn; đặt cược cao hơn"},
  {"id": "lex.en.200k.060378", "hw": "outcalls", "pos": "verb", "ipa": "/aʊtˈkɔːlz/", "vi": "gọi át tiếng; đặt cược cao hơn"},
  {"id": "lex.en.200k.060379", "hw": "papermakings", "pos": "noun", "ipa": "/ˈpeɪpərmeɪkɪŋz/", "vi": "ngành công nghiệp sản xuất giấy"},
  {"id": "lex.en.200k.060380", "hw": "pentathlons", "pos": "noun", "ipa": "/pɛnˈtæθlənz/", "vi": "môn thi đấu điền kinh năm môn"},
  {"id": "lex.en.200k.060381", "hw": "pharmacopoeias", "pos": "noun", "ipa": "/ˌfɑːrməkəˈpiːəz/", "vi": "bộ dược điển tiêu chuẩn quốc gia"},
  {"id": "lex.en.200k.060382", "hw": "phonebooks", "pos": "noun", "ipa": "/ˈfoʊnbʊks/", "vi": "cuốn niên giám danh bạ điện thoại"},
  {"id": "lex.en.200k.060383", "hw": "pillions", "pos": "noun", "ipa": "/ˈpɪljənz/", "vi": "yên phụ ngồi sau của xe gắn máy"},
  {"id": "lex.en.200k.060384", "hw": "plages", "pos": "noun", "ipa": "/plɑːʒɪz/", "vi": "bãi biển nghỉ mát sang trọng"},
  {"id": "lex.en.200k.060385", "hw": "poinsettias", "pos": "noun", "ipa": "/ˌpɔɪnˈsɛtiəz/", "vi": "cây hoa trạng nguyên đỏ Giáng sinh"},
  {"id": "lex.en.200k.060386", "hw": "prajapatis", "pos": "noun", "ipa": "/prəˈdʒɑːpətiz/", "vi": "thần sáng tạo muôn loài Ấn Độ giáo"},
  {"id": "lex.en.200k.060387", "hw": "quetzalcoatls", "pos": "noun", "ipa": "/ˌkɛtsɑːlkoʊˈɑːtlz/", "vi": "thần rắn lông vũ Quetzalcoatl"},
  {"id": "lex.en.200k.060388", "hw": "rabelaises", "pos": "noun", "ipa": "/ˌræbəˈleɪz/", "vi": "nhà văn trào phúng Pháp Rabelais"},
  {"id": "lex.en.200k.060389", "hw": "radians", "pos": "noun", "ipa": "/ˈreɪdiənz/", "vi": "đơn vị đo góc phẳng chuẩn radian"},
  {"id": "lex.en.200k.060390", "hw": "rangelands", "pos": "noun", "ipa": "/ˈreɪndʒlændz/", "vi": "vùng đồng cỏ rộng chăn thả gia súc"},
  {"id": "lex.en.200k.060391", "hw": "rastafaris", "pos": "noun", "ipa": "/ˌræstəˈfɑːriz/", "vi": "phong trào tôn giáo Rastafari"},
  {"id": "lex.en.200k.060392", "hw": "rattuses", "pos": "noun", "ipa": "/ˈrætəsɪz/", "vi": "chi chuột cống chuột nhà Rattus"},
  {"id": "lex.en.200k.060393", "hw": "rhombuses", "pos": "noun", "ipa": "/ˈrɑːmbəsɪz/", "vi": "hình thoi bốn cạnh bằng nhau"},
  {"id": "lex.en.200k.060394", "hw": "rolodexes", "pos": "noun", "ipa": "/ˈroʊlədɛksɪz/", "vi": "hộp thẻ xoay lưu danh bạ để bàn"},
  {"id": "lex.en.200k.060395", "hw": "saguaros", "pos": "noun", "ipa": "/səˈɡwɑːroʊz/", "vi": "cây xương rồng khổng lồ Saguaro"},
  {"id": "lex.en.200k.060396", "hw": "sbes", "pos": "noun", "ipa": "/ɛs biː iːz/", "vi": "hướng la bàn nam hơi lệch đông"},
  {"id": "lex.en.200k.060397", "hw": "scoutmasters", "pos": "noun", "ipa": "/ˈskaʊtmæstərz/", "vi": "huynh trưởng dẫn dắt đội Hướng đạo"},
  {"id": "lex.en.200k.060398", "hw": "scragglier", "pos": "adj", "ipa": "/ˈskræɡliər/", "vi": "lởm chởm xơ xác hơn; gầy guộc hơn"},
  {"id": "lex.en.200k.060399", "hw": "scraggliest", "pos": "adj", "ipa": "/ˈskræɡliɪst/", "vi": "mọc lởm chởm xơ xác nhất; gầy nhất"},
  {"id": "lex.en.200k.060400", "hw": "siddonses", "pos": "noun", "ipa": "/ˈsɪdənzɪz/", "vi": "nữ diễn viên bi kịch Sarah Siddons"},
  {"id": "lex.en.200k.060401", "hw": "significations", "pos": "noun", "ipa": "/ˌsɪɡnɪfɪˈkeɪʃənz/", "vi": "hàm ý biểu đạt; ý nghĩa chính xác"},
  {"id": "lex.en.200k.060402", "hw": "stegosauruses", "pos": "noun", "ipa": "/ˌstɛɡəˈsɔːrəsɪz/", "vi": "loài khủng long vây kiếm ăn cỏ"}
]

with open('scratch/b33_r01_raw_p4.json') as f:
    raw = json.load(f)

assert len(items) == 100
assert len(raw) == 100

for i, (item, r) in enumerate(zip(items, raw)):
    assert item['id'] == r['id'], f"Mismatch id at {i}: {item['id']} vs {r['id']}"
    assert item['hw'] == r['hw'], f"Mismatch hw at {i}: {item['hw']} vs {r['hw']}"
    assert len(item['vi']) <= 35, f"vi length > 35 at {i} ({item['hw']}): {len(item['vi'])}"
    assert item['pos'] in ['noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'], f"Invalid pos at {i}: {item['pos']}"
    if ' ' not in item['hw']:
        assert item['ipa'].startswith('/') and item['ipa'].endswith('/') and item['ipa'].count('/') == 2, f"Invalid ipa at {i}: {item['ipa']}"
    r['pos'] = item['pos']
    r['ipa'] = item['ipa']
    r['vi'] = item['vi']
    r['status'] = 'reviewed'

with open('scratch/b33_r01_p4.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

print("Batch 33 Round 1 Part 4 validated and written successfully.")
