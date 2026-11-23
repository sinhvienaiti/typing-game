import json

items = [
  {"id": "lex.en.200k.064403", "hw": "interweaving", "pos": "verb", "ipa": "/ˌɪntərˈwiːvɪŋ/", "vi": "đang đan xen bện lồng ghép vào"},
  {"id": "lex.en.200k.064404", "hw": "isocyanates", "pos": "noun", "ipa": "/ˌaɪsoʊˈsaɪəneɪts/", "vi": "hóa chất sản xuất nhựa isocyanat"},
  {"id": "lex.en.200k.064405", "hw": "keloids", "pos": "noun", "ipa": "/ˈkiːlɔɪdz/", "vi": "sẹo lồi phì đại trên vùng da tổn"},
  {"id": "lex.en.200k.064406", "hw": "keras", "pos": "noun", "ipa": "/ˈkɪrəz/", "vi": "người và ngôn ngữ Kera ở Trung Phi"},
  {"id": "lex.en.200k.064407", "hw": "koines", "pos": "noun", "ipa": "/ˈkɔɪneɪz/", "vi": "tiếng Hy Lạp phổ thông cổ Koine"},
  {"id": "lex.en.200k.064408", "hw": "levelers", "pos": "noun", "ipa": "/ˈlɛvələrz/", "vi": "người theo chủ nghĩa bình quân"},
  {"id": "lex.en.200k.064409", "hw": "macrocosms", "pos": "noun", "ipa": "/ˈmækrəˌkɑːzmz/", "vi": "vũ trụ vĩ mô; hệ thống quy mô lớn"},
  {"id": "lex.en.200k.064410", "hw": "manikins", "pos": "noun", "ipa": "/ˈmænəkɪnz/", "vi": "ma-nơ-canh; mô hình giải phẫu nhỏ"},
  {"id": "lex.en.200k.064411", "hw": "mastoids", "pos": "noun", "ipa": "/ˈmæstɔɪdz/", "vi": "mỏm xương chũm sau vành tai"},
  {"id": "lex.en.200k.064412", "hw": "matzahs", "pos": "noun", "ipa": "/ˈmɑːtsəz/", "vi": "bánh mì dẹt không men lễ Vượt Qua"},
  {"id": "lex.en.200k.064413", "hw": "miscellaneas", "pos": "noun", "ipa": "/ˌmɪsəˈleɪniəz/", "vi": "tuyển tập bài viết tạp văn hỗn hợp"},
  {"id": "lex.en.200k.064414", "hw": "mujahedins", "pos": "noun", "ipa": "/muːˌdʒɑːhɪˈdiːnz/", "vi": "chiến binh thánh chiến Hồi giáo"},
  {"id": "lex.en.200k.064415", "hw": "narcoses", "pos": "noun", "ipa": "/nɑːrˈkoʊsiːz/", "vi": "trạng thái mê man mất ý thức sâu"},
  {"id": "lex.en.200k.064416", "hw": "neosporins", "pos": "noun", "ipa": "/ˌniːoʊˈspɔːrɪnz/", "vi": "thuốc mỡ kháng sinh bôi ngoài da"},
  {"id": "lex.en.200k.064417", "hw": "nipas", "pos": "noun", "ipa": "/ˈniːpəz/", "vi": "cây dừa nước mọc vùng đầm lầy lợ"},
  {"id": "lex.en.200k.064418", "hw": "novocaines", "pos": "noun", "ipa": "/ˈnoʊvəˌkeɪnz/", "vi": "thuốc gây tê cục bộ nha khoa"},
  {"id": "lex.en.200k.064419", "hw": "obturators", "pos": "noun", "ipa": "/ˈɑːbtjʊˌreɪtərz/", "vi": "vật bịt lỗ; màng bịt cơ bịt hông"},
  {"id": "lex.en.200k.064420", "hw": "oireachtases", "pos": "noun", "ipa": "/ˈɛrəxtəsɪz/", "vi": "Quốc hội lập pháp Cộng hòa Ireland"},
  {"id": "lex.en.200k.064421", "hw": "ossuaries", "pos": "noun", "ipa": "/ˈɑːʃuˌɛriz/", "vi": "tiểu sành cốt; hầm chứa hài cốt"},
  {"id": "lex.en.200k.064422", "hw": "ostwalds", "pos": "noun", "ipa": "/ˈɔːstvældz/", "vi": "nhà hóa học Nobel Wilhelm Ostwald"},
  {"id": "lex.en.200k.064423", "hw": "pamlicos", "pos": "noun", "ipa": "/ˈpæmlɪkoʊz/", "vi": "bộ tộc bản địa Pamlico bang Mỹ"},
  {"id": "lex.en.200k.064424", "hw": "perlises", "pos": "noun", "ipa": "/ˈpɜːrlɪsɪz/", "vi": "bang nhỏ Perlis cực bắc Malaysia"},
  {"id": "lex.en.200k.064425", "hw": "pharmacologists", "pos": "noun", "ipa": "/ˌfɑːrməˈkɑːlədʒɪsts/", "vi": "nhà dược lý học nghiên cứu thuốc"},
  {"id": "lex.en.200k.064426", "hw": "photolithographies", "pos": "noun", "ipa": "/ˌfoʊtoʊlɪˈθɑːɡrəfiz/", "vi": "kỹ thuật quang khắc mạch bán dẫn"},
  {"id": "lex.en.200k.064427", "hw": "phototherapies", "pos": "noun", "ipa": "/ˌfoʊtoʊˈθɛrəpiz/", "vi": "liệu pháp quang trị liệu bằng sáng"},
  {"id": "lex.en.200k.064428", "hw": "pinschers", "pos": "noun", "ipa": "/ˈpɪnʃərz/", "vi": "giống chó săn Đức lông ngắn nhanh"},
  {"id": "lex.en.200k.064429", "hw": "porphyrins", "pos": "noun", "ipa": "/ˈpɔːrfərɪnz/", "vi": "hợp chất vòng hữu cơ tạo hồng cầu"},
  {"id": "lex.en.200k.064430", "hw": "postboxes", "pos": "noun", "ipa": "/ˈpoʊstbɑːksɪz/", "vi": "thùng bỏ thư bưu điện công cộng"},
  {"id": "lex.en.200k.064431", "hw": "prevarications", "pos": "noun", "ipa": "/prɪˌvɛrəˈkeɪʃənz/", "vi": "lời nói quanh co lấp lửng né tránh"},
  {"id": "lex.en.200k.064432", "hw": "prigged", "pos": "verb", "ipa": "/prɪɡd/", "vi": "đã ăn cắp vặt; đã tỏ vẻ hợm hĩnh"},
  {"id": "lex.en.200k.064433", "hw": "prigging", "pos": "verb", "ipa": "/ˈprɪɡɪŋ/", "vi": "đang ăn cắp vặt; tỏ vẻ hợm hĩnh"},
  {"id": "lex.en.200k.064434", "hw": "prigs", "pos": "noun", "ipa": "/prɪɡz/", "vi": "kẻ hợm hĩnh tự cho mình đạo đức"},
  {"id": "lex.en.200k.064435", "hw": "protuberances", "pos": "noun", "ipa": "/proʊˈtuːbərənsɪz/", "vi": "chỗ lồi u nhô ra trên bề mặt"},
  {"id": "lex.en.200k.064436", "hw": "quinones", "pos": "noun", "ipa": "/kwɪˈnoʊnz/", "vi": "hợp chất hữu cơ vòng thơm quinon"},
  {"id": "lex.en.200k.064437", "hw": "roundels", "pos": "noun", "ipa": "/ˈraʊndəlz/", "vi": "biểu tượng hình tròn; thể thơ ngắn"},
  {"id": "lex.en.200k.064438", "hw": "rutabagas", "pos": "noun", "ipa": "/ˌruːtəˈbeɪɡəz/", "vi": "củ cải vàng Thụy Điển ăn củ"},
  {"id": "lex.en.200k.064439", "hw": "saltines", "pos": "noun", "ipa": "/ˌsɔːlˈtiːnz/", "vi": "bánh quy giòn vị mặn hình vuông"},
  {"id": "lex.en.200k.064440", "hw": "screwups", "pos": "noun", "ipa": "/ˈskruːʌps/", "vi": "lỗi ngớ ngẩn làm hỏng bét (lóng)"},
  {"id": "lex.en.200k.064441", "hw": "secondi", "pos": "noun", "ipa": "/sɛˈkɑːndi/", "vi": "nhạc công hay phần bè thứ hai"},
  {"id": "lex.en.200k.064442", "hw": "secondos", "pos": "noun", "ipa": "/sɛˈkɑːndoʊz/", "vi": "các phần bè hòa âm thứ hai"},
  {"id": "lex.en.200k.064443", "hw": "seleuci", "pos": "noun", "ipa": "/səˈluːsaɪ/", "vi": "vua sáng lập đế chế Seleucid cổ"},
  {"id": "lex.en.200k.064444", "hw": "sherberts", "pos": "noun", "ipa": "/ˈʃɜːrbərts/", "vi": "kem trái cây mát lạnh (biến thể)"},
  {"id": "lex.en.200k.064445", "hw": "snowbanks", "pos": "noun", "ipa": "/ˈsnoʊbæŋks/", "vi": "đụn tuyết chất cao ven đường đi"},
  {"id": "lex.en.200k.064446", "hw": "snowdrifts", "pos": "noun", "ipa": "/ˈsnoʊdrɪfts/", "vi": "đống tuyết lớn do gió thổi dồn lại"},
  {"id": "lex.en.200k.064447", "hw": "splicers", "pos": "noun", "ipa": "/ˈsplaɪsərz/", "vi": "máy hàn nối cáp quang; thợ nối dây"},
  {"id": "lex.en.200k.064448", "hw": "stagers", "pos": "noun", "ipa": "/ˈsteɪdʒərz/", "vi": "người dàn dựng kịch; cựu binh dày"},
  {"id": "lex.en.200k.064449", "hw": "stanchions", "pos": "noun", "ipa": "/ˈstæntʃənz/", "vi": "cột trụ chống đứng boong tàu rào"},
  {"id": "lex.en.200k.064450", "hw": "steamrolled", "pos": "verb", "ipa": "/ˈstiːmroʊld/", "vi": "đã cán bằng xe lu; đã áp đảo bẹp"},
  {"id": "lex.en.200k.064451", "hw": "steamrolling", "pos": "verb", "ipa": "/ˈstiːmˌroʊlɪŋ/", "vi": "đang lu phẳng; đang ép buộc áp đảo"},
  {"id": "lex.en.200k.064452", "hw": "steamrolls", "pos": "verb", "ipa": "/ˈstiːmroʊlz/", "vi": "cán phẳng đường; lấn át áp đảo"},
  {"id": "lex.en.200k.064453", "hw": "superclasses", "pos": "noun", "ipa": "/ˈsuːpərˌklæsɪz/", "vi": "liên lớp sinh học; lớp cha (code)"},
  {"id": "lex.en.200k.064454", "hw": "swizzles", "pos": "noun", "ipa": "/ˈswɪzəlz/", "vi": "ly cocktail đá bào khuấy; trò bịp"},
  {"id": "lex.en.200k.064455", "hw": "taconites", "pos": "noun", "ipa": "/ˈtækənaɪts/", "vi": "loại đá chứa quặng sắt taconite"},
  {"id": "lex.en.200k.064456", "hw": "tailpieces", "pos": "noun", "ipa": "/ˈteɪlpiːsɪz/", "vi": "bộ giữ dây đàn; phần đuôi nối dài"},
  {"id": "lex.en.200k.064457", "hw": "tamms", "pos": "noun", "ipa": "/tɑːmz/", "vi": "nhà vật lý hạt nhân Nga Igor Tamm"},
  {"id": "lex.en.200k.064458", "hw": "tefillins", "pos": "noun", "ipa": "/təˈfɪlɪnz/", "vi": "hộp da đeo tay đầu cầu nguyện"},
  {"id": "lex.en.200k.064459", "hw": "theropods", "pos": "noun", "ipa": "/ˈθɪrəpɑːdz/", "vi": "khủng long chân thú đi hai chân"},
  {"id": "lex.en.200k.064460", "hw": "thimerosals", "pos": "noun", "ipa": "/θaɪˈmɛrəsɔːlz/", "vi": "chất bảo quản vắc-xin thủy ngân"},
  {"id": "lex.en.200k.064461", "hw": "thunderers", "pos": "noun", "ipa": "/ˈθʌndərərz/", "vi": "thần Sấm sét; người gầm thét oai"},
  {"id": "lex.en.200k.064462", "hw": "titres", "pos": "noun", "ipa": "/ˈtaɪtərz/", "vi": "nồng độ chuẩn độ dung dịch (Anh)"},
  {"id": "lex.en.200k.064463", "hw": "trhs", "pos": "noun", "ipa": "/ˌtiːˌɑːrˈeɪtʃɪz/", "vi": "hoóc môn kích thích tuyến yên TRH"},
  {"id": "lex.en.200k.064464", "hw": "trivets", "pos": "noun", "ipa": "/ˈtrɪvɪts/", "vi": "kiềng ba chân; đế lót nồi thức ăn"},
  {"id": "lex.en.200k.064465", "hw": "trochanters", "pos": "noun", "ipa": "/troʊˈkæntərz/", "vi": "mấu chuyển đầu trên xương đùi"},
  {"id": "lex.en.200k.064466", "hw": "underselling", "pos": "verb", "ipa": "/ˌʌndərˈsɛlɪŋ/", "vi": "đang bán phá giá rẻ hơn đối thủ"},
  {"id": "lex.en.200k.064467", "hw": "undersells", "pos": "verb", "ipa": "/ˌʌndərˈsɛlz/", "vi": "bán rẻ phá giá hơn đối thủ"},
  {"id": "lex.en.200k.064468", "hw": "uranias", "pos": "noun", "ipa": "/jʊˈreɪniəz/", "vi": "nàng thơ thiên văn học Urania"},
  {"id": "lex.en.200k.064469", "hw": "variolas", "pos": "noun", "ipa": "/vəˈraɪələz/", "vi": "bệnh truyền nhiễm đậu mùa nặng"},
  {"id": "lex.en.200k.064470", "hw": "vasodilators", "pos": "noun", "ipa": "/ˌveɪzoʊdaɪˈleɪtərz/", "vi": "thuốc làm giãn nở lòng mạch máu"},
  {"id": "lex.en.200k.064471", "hw": "viceroyalties", "pos": "noun", "ipa": "/vaɪsˈrɔɪəltiz/", "vi": "chức vụ và lãnh địa phó vương"},
  {"id": "lex.en.200k.064472", "hw": "wahabis", "pos": "noun", "ipa": "/wəˈhɑːbiz/", "vi": "tín đồ phong trào Hồi giáo Wahhabi"},
  {"id": "lex.en.200k.064473", "hw": "wahhabis", "pos": "noun", "ipa": "/wəˈhɑːbiz/", "vi": "tín đồ phong trào Wahhabi Hồi giáo"},
  {"id": "lex.en.200k.064474", "hw": "wardrooms", "pos": "noun", "ipa": "/ˈwɔːrdruːmz/", "vi": "phòng sinh hoạt sĩ quan tàu chiến"},
  {"id": "lex.en.200k.064475", "hw": "waterwheels", "pos": "noun", "ipa": "/ˈwɔːtərwiːlz/", "vi": "bánh xe guồng nước chạy cối xay"},
  {"id": "lex.en.200k.064476", "hw": "whelked", "pos": "verb", "ipa": "/wɛlkt/", "vi": "đã mò bắt ốc xoắn biển vùng cạn"},
  {"id": "lex.en.200k.064477", "hw": "whelks", "pos": "noun", "ipa": "/wɛlks/", "vi": "ốc xoắn biển thịt ngon ăn được"},
  {"id": "lex.en.200k.064478", "hw": "whitewoods", "pos": "noun", "ipa": "/ˈwaɪtwʊdz/", "vi": "cây gỗ dẻo màu sáng nhạt whitewood"},
  {"id": "lex.en.200k.064479", "hw": "whitlows", "pos": "noun", "ipa": "/ˈwɪtloʊz/", "vi": "bệnh chín mé mưng mủ đầu ngón tay"},
  {"id": "lex.en.200k.064480", "hw": "yarmulkes", "pos": "noun", "ipa": "/ˈjɑːrməlkəz/", "vi": "mũ tròn nhỏ đội đỉnh đầu Do Thái"},
  {"id": "lex.en.200k.064481", "hw": "antispasmodic agent", "pos": "phrase", "ipa": "/ˌæntispæzˈmɑːdɪk ˈeɪdʒənt/", "vi": "thuốc chống co thắt cơ trơn ruột"},
  {"id": "lex.en.200k.064482", "hw": "belaying pin", "pos": "phrase", "ipa": "/bɪˈleɪɪŋ pɪn/", "vi": "chốt gỗ kim loại buộc dây buồm tàu"},
  {"id": "lex.en.200k.064483", "hw": "bluestem wheatgrass", "pos": "phrase", "ipa": "/ˈbluːstɛm ˈwiːtɡræs/", "vi": "cỏ lúa mì thân xanh thảo nguyên"},
  {"id": "lex.en.200k.064484", "hw": "cape dagga", "pos": "phrase", "ipa": "/keɪp ˈdæɡə/", "vi": "cây tai sư tử hoa cam Nam Phi"},
  {"id": "lex.en.200k.064485", "hw": "castanea sativa", "pos": "phrase", "ipa": "/kæˈsteɪniə səˈtaɪvə/", "vi": "cây hạt dẻ ngọt châu Âu ăn hạt"},
  {"id": "lex.en.200k.064486", "hw": "cedar waxwing", "pos": "phrase", "ipa": "/ˈsiːdər ˈwækswɪŋ/", "vi": "chim cánh sáp ăn quả Bắc Mỹ"},
  {"id": "lex.en.200k.064487", "hw": "cornhusker state", "pos": "phrase", "ipa": "/ˈkɔːrnˌhʌskər steɪt/", "vi": "biệt danh bang nông nghiệp Nebraska"},
  {"id": "lex.en.200k.064488", "hw": "corpuscular radiation", "pos": "phrase", "ipa": "/kɔːrˈpʌskjələr ˌreɪdiˈeɪʃən/", "vi": "bức xạ dòng hạt vật chất năng cao"},
  {"id": "lex.en.200k.064489", "hw": "corpuscular theory", "pos": "phrase", "ipa": "/kɔːrˈpʌskjələr ˈθiːəri/", "vi": "thuyết hạt ánh sáng của Newton"},
  {"id": "lex.en.200k.064490", "hw": "el caudillo", "pos": "phrase", "ipa": "/ɛl kaʊˈdiːjoʊ/", "vi": "danh hiệu lãnh tụ độc tài Franco"},
  {"id": "lex.en.200k.064491", "hw": "ethelred the unready", "pos": "phrase", "ipa": "/ˈɛθəlrɛd ði ʌnˈrɛdi/", "vi": "vua Anh cổ đại Ethelred Thiếu Cố"},
  {"id": "lex.en.200k.064492", "hw": "euphorbia litchi", "pos": "phrase", "ipa": "/juːˈfɔːrbiə ˈlaɪtʃi/", "vi": "cây vải thiều (tên khoa học cũ)"},
  {"id": "lex.en.200k.064493", "hw": "flagellate protozoan", "pos": "phrase", "ipa": "/ˈflædʒəlɪt ˌproʊtəˈzoʊən/", "vi": "động vật đơn bào bơi bằng roi"},
  {"id": "lex.en.200k.064494", "hw": "genus curcuma", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈkɜːrkjəmə/", "vi": "chi cây nghệ vàng làm gia vị thuốc"},
  {"id": "lex.en.200k.064495", "hw": "genus cyperus", "pos": "phrase", "ipa": "/ˈdʒiːnəs saɪˈpɪrəs/", "vi": "chi cây cói lác thảo mộc Cyperus"},
  {"id": "lex.en.200k.064496", "hw": "genus lonicera", "pos": "phrase", "ipa": "/ˈdʒiːnəs loʊˈnɪsərə/", "vi": "chi dây hoa kim ngân thơm Lonicera"},
  {"id": "lex.en.200k.064497", "hw": "genus lupinus", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈluːpənəs/", "vi": "chi cây hoa lupin đậu cánh bướm"},
  {"id": "lex.en.200k.064498", "hw": "genus rumex", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈruːmɛks/", "vi": "chi cây chút chít chua vùng ôn đới"},
  {"id": "lex.en.200k.064499", "hw": "genus sclerotinia", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˌsklɛrəˈtɪniə/", "vi": "chi nấm mốc trắng hại cây trồng"},
  {"id": "lex.en.200k.064500", "hw": "genus termes", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈtɜːrmiːz/", "vi": "chi côn trùng mối gỗ ăn xenlulo"},
  {"id": "lex.en.200k.064501", "hw": "germ plasm", "pos": "phrase", "ipa": "/dʒɜːrm ˈplæzəm/", "vi": "chất mầm tế bào di truyền giống"},
  {"id": "lex.en.200k.064502", "hw": "giuseppe balsamo", "pos": "phrase", "ipa": "/dʒuˈzɛpɛ ˈbɑːlsəmoʊ/", "vi": "nhà giả kim phiêu lưu Cagliostro"}
]

with open('scratch/b33_r09_raw_p5.json') as f:
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

with open('scratch/b33_r09_p5.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)
print("Saved scratch/b33_r09_p5.json OK")
