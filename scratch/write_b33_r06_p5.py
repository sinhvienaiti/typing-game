import json

items = [
  {"id": "lex.en.200k.062903", "hw": "infix notation", "pos": "phrase", "ipa": "/ˈɪnfɪks noʊˈteɪʃən/", "vi": "ký pháp trung tố toán học"},
  {"id": "lex.en.200k.062904", "hw": "lamina arcus vertebrae", "pos": "phrase", "ipa": "/ˈlæmənə ˈɑːrkəs ˈvɜːrtəbriː/", "vi": "mảnh cung đốt sống cột sống"},
  {"id": "lex.en.200k.062905", "hw": "leo szilard", "pos": "phrase", "ipa": "/ˈliːoʊ ˈsɪlɑːrd/", "vi": "nhà vật lý hạt nhân Leo Szilard"},
  {"id": "lex.en.200k.062906", "hw": "magna charta", "pos": "phrase", "ipa": "/ˈmæɡnə ˈkɑːrtə/", "vi": "Đại Hiến chương Tự do Anh 1215"},
  {"id": "lex.en.200k.062907", "hw": "malathion poisoning", "pos": "phrase", "ipa": "/ˌmæləˈθaɪɑːn ˈpɔɪzənɪŋ/", "vi": "ngộ độc thuốc trừ sâu malathion"},
  {"id": "lex.en.200k.062908", "hw": "malus sylvestris", "pos": "phrase", "ipa": "/ˈmeɪləs sɪlˈvɛstrɪs/", "vi": "cây táo dại bản địa châu Âu"},
  {"id": "lex.en.200k.062909", "hw": "medicago sativa", "pos": "phrase", "ipa": "/ˌmɛdɪˈkeɪɡoʊ səˈtaɪvə/", "vi": "cây cỏ linh lăng giàu dinh dưỡng"},
  {"id": "lex.en.200k.062910", "hw": "mouse eared chickweed", "pos": "phrase", "ipa": "/maʊs ɪərd ˈtʃɪkwiːd/", "vi": "cây cỏ tai chuột hoa trắng nhỏ"},
  {"id": "lex.en.200k.062911", "hw": "musculus sphincter pylori", "pos": "phrase", "ipa": "/ˈmʌskjʊləs ˈsfɪŋktər paɪˈlɔːri/", "vi": "cơ vòng thắt môn vị dạ dày"},
  {"id": "lex.en.200k.062912", "hw": "nasal meatus", "pos": "phrase", "ipa": "/ˈneɪzəl miˈeɪtəs/", "vi": "khe mũi; ngách dẫn khí xoang mũi"},
  {"id": "lex.en.200k.062913", "hw": "neuroleptic agent", "pos": "phrase", "ipa": "/ˌnjʊrəˈlɛptɪk ˈeɪdʒənt/", "vi": "hoạt chất thuốc an thần kinh"},
  {"id": "lex.en.200k.062914", "hw": "neuroleptic drug", "pos": "phrase", "ipa": "/ˌnjʊrəˈlɛptɪk drʌɡ/", "vi": "thuốc chống loạn thần an thần kinh"},
  {"id": "lex.en.200k.062915", "hw": "pink fritillary", "pos": "phrase", "ipa": "/pɪŋk ˈfrɪtəˌlɛri/", "vi": "cây hoa chuông hồng Bắc Mỹ"},
  {"id": "lex.en.200k.062916", "hw": "plott hound", "pos": "phrase", "ipa": "/plɑːt haʊnd/", "vi": "giống chó săn vằn Plott của Mỹ"},
  {"id": "lex.en.200k.062917", "hw": "primary dysmenorrhea", "pos": "phrase", "ipa": "/ˈpraɪˌmɛri ˌdɪsmɛnəˈriːə/", "vi": "đau bụng kinh nguyên phát thường"},
  {"id": "lex.en.200k.062918", "hw": "redfin pickerel", "pos": "phrase", "ipa": "/ˈrɛdfɪn ˈpɪkərəl/", "vi": "cá chó nước ngọt vây đỏ Bắc Mỹ"},
  {"id": "lex.en.200k.062919", "hw": "saint eustatius", "pos": "phrase", "ipa": "/seɪnt juːˈsteɪʃəs/", "vi": "đảo Sint Eustatius vùng Caribê"},
  {"id": "lex.en.200k.062920", "hw": "salix fragilis", "pos": "phrase", "ipa": "/ˈseɪlɪks ˈfrædʒəlɪs/", "vi": "cây liễu cành giòn dễ gãy châu Âu"},
  {"id": "lex.en.200k.062921", "hw": "scut work", "pos": "phrase", "ipa": "/skʌt wɜːrk/", "vi": "công việc vặt vãnh nặng nhọc nhàm"},
  {"id": "lex.en.200k.062922", "hw": "secondary dysmenorrhea", "pos": "phrase", "ipa": "/ˈsɛkəndɛri ˌdɪsmɛnəˈriːə/", "vi": "đau bụng kinh thứ phát do bệnh lý"},
  {"id": "lex.en.200k.062923", "hw": "showy orchis", "pos": "phrase", "ipa": "/ˈʃoʊi ˈɔːrkɪs/", "vi": "hoa lan nhỏ cánh tím trắng Bắc Mỹ"},
  {"id": "lex.en.200k.062924", "hw": "silene vulgaris", "pos": "phrase", "ipa": "/saɪˈliːni vʌlˈɡɛrɪs/", "vi": "cây hoa túi phồng châu Âu"},
  {"id": "lex.en.200k.062925", "hw": "sitz bath", "pos": "phrase", "ipa": "/sɪts bæθ/", "vi": "chậu ngâm mông nước ấm trị bệnh"},
  {"id": "lex.en.200k.062926", "hw": "spectacled caiman", "pos": "phrase", "ipa": "/ˈspɛktəkəld ˈkeɪmən/", "vi": "cá sấu caiman đeo kính Nam Mỹ"},
  {"id": "lex.en.200k.062927", "hw": "stalked puffball", "pos": "phrase", "ipa": "/stɔːkt ˈpʌfbɔːl/", "vi": "nấm túi bào tử có cuống dài"},
  {"id": "lex.en.200k.062928", "hw": "suborder lari", "pos": "phrase", "ipa": "/sʌbˈɔːrdər ˈlɛraɪ/", "vi": "phân bộ chim Mòng biển và Nhàn"},
  {"id": "lex.en.200k.062929", "hw": "tallapoosa river", "pos": "phrase", "ipa": "/ˌtæləˈpuːsə ˈrɪvər/", "vi": "sông Tallapoosa ở đông nam Hoa Kỳ"},
  {"id": "lex.en.200k.062930", "hw": "thorstein veblen", "pos": "phrase", "ipa": "/ˈθɔːrstaɪn ˈvɛblən/", "vi": "nhà kinh tế học Mỹ Thorstein Veblen"},
  {"id": "lex.en.200k.062931", "hw": "uralic language", "pos": "phrase", "ipa": "/jʊˈrælɪk ˈlæŋɡwɪdʒ/", "vi": "ngôn ngữ thuộc ngữ hệ Ural"},
  {"id": "lex.en.200k.062932", "hw": "white fringed orchis", "pos": "phrase", "ipa": "/waɪt frɪndʒd ˈɔːrkɪs/", "vi": "hoa lan cánh tua màu trắng Bắc Mỹ"},
  {"id": "lex.en.200k.062933", "hw": "white fritillary", "pos": "phrase", "ipa": "/waɪt ˈfrɪtəˌlɛri/", "vi": "cây hoa chuông trắng California"},
  {"id": "lex.en.200k.062934", "hw": "aflatoxins", "pos": "noun", "ipa": "/ˌæfləˈtɑːksɪnz/", "vi": "độc tố nấm mốc hại gan aflatoxin"},
  {"id": "lex.en.200k.062935", "hw": "agamas", "pos": "noun", "ipa": "/əˈɡɑːməz/", "vi": "thằn lằn đầu to châu Phi agama"},
  {"id": "lex.en.200k.062936", "hw": "armfuls", "pos": "noun", "ipa": "/ˈɑːrmfʊlz/", "vi": "lượng đồ vật ôm đầy một vòng tay"},
  {"id": "lex.en.200k.062937", "hw": "ashlars", "pos": "noun", "ipa": "/ˈæʃlərz/", "vi": "khối đá xây đẽo gọt vuông vức"},
  {"id": "lex.en.200k.062938", "hw": "beachcombers", "pos": "noun", "ipa": "/ˈbiːtʃˌkoʊmərz/", "vi": "người đi nhặt đồ trôi dạt bãi biển"},
  {"id": "lex.en.200k.062939", "hw": "bellhops", "pos": "noun", "ipa": "/ˈbɛlhɑːps/", "vi": "nhân viên khuân hành lý khách sạn"},
  {"id": "lex.en.200k.062940", "hw": "bizets", "pos": "noun", "ipa": "/biˈzeɪz/", "vi": "nhà soạn nhạc Carmen Georges Bizet"},
  {"id": "lex.en.200k.062941", "hw": "blackhearts", "pos": "noun", "ipa": "/ˈblækhɑːrts/", "vi": "kẻ lòng dạ đen tối; bệnh thối đen"},
  {"id": "lex.en.200k.062942", "hw": "bufos", "pos": "noun", "ipa": "/ˈbjuːfoʊz/", "vi": "cóc đất điển hình thuộc chi Bufo"},
  {"id": "lex.en.200k.062943", "hw": "bukharins", "pos": "noun", "ipa": "/buˈxɑːrɪnz/", "vi": "nhà lý luận Xô Viết Bukharin"},
  {"id": "lex.en.200k.062944", "hw": "chaits", "pos": "noun", "ipa": "/tʃaɪts/", "vi": "tháng Chait đầu năm lịch Ấn Độ"},
  {"id": "lex.en.200k.062945", "hw": "chelas", "pos": "noun", "ipa": "/ˈtʃeɪləz/", "vi": "đệ tử tâm linh; môn sinh (Ấn Độ)"},
  {"id": "lex.en.200k.062946", "hw": "claviers", "pos": "noun", "ipa": "/ˈklæviərz/", "vi": "đàn phím cổ; bàn phím đàn dương cầm"},
  {"id": "lex.en.200k.062947", "hw": "colimas", "pos": "noun", "ipa": "/kəˈliːməz/", "vi": "bang và núi lửa Colima ở Mexico"},
  {"id": "lex.en.200k.062948", "hw": "cooties", "pos": "noun", "ipa": "/ˈkuːtiz/", "vi": "con rận; trò trẻ em trêu nhiễm bẩn"},
  {"id": "lex.en.200k.062949", "hw": "damars", "pos": "noun", "ipa": "/ˈdæmərz/", "vi": "nhựa cây dầu cánh làm sơn bóng"},
  {"id": "lex.en.200k.062950", "hw": "demographers", "pos": "noun", "ipa": "/dɪˈmɑːɡrəfərz/", "vi": "nhà nghiên cứu dân số nhân khẩu học"},
  {"id": "lex.en.200k.062951", "hw": "draftees", "pos": "noun", "ipa": "/ˌdræfˈtiːz/", "vi": "tân binh được gọi nhập ngũ bắt buộc"},
  {"id": "lex.en.200k.062952", "hw": "dugongs", "pos": "noun", "ipa": "/ˈduːɡɔːŋz/", "vi": "cá cúi bò biển ăn cỏ vùng nhiệt đới"},
  {"id": "lex.en.200k.062953", "hw": "dulcineas", "pos": "noun", "ipa": "/ˌdʌlsɪˈniːəz/", "vi": "người tình trong mộng lý tưởng hóa"},
  {"id": "lex.en.200k.062954", "hw": "electromagneticses", "pos": "noun", "ipa": "/ɪˌlɛktroʊmæɡˈnɛtɪksɪz/", "vi": "môn điện từ học; hiện tượng điện từ"},
  {"id": "lex.en.200k.062955", "hw": "encaustics", "pos": "noun", "ipa": "/ɛnˈkɔːstɪks/", "vi": "kỹ thuật vẽ tranh sáp ong nóng"},
  {"id": "lex.en.200k.062956", "hw": "endonucleases", "pos": "noun", "ipa": "/ˌɛndoʊˈnuːkliˌeɪsɪz/", "vi": "enzym cắt liên kết axit nucleic"},
  {"id": "lex.en.200k.062957", "hw": "ephedras", "pos": "noun", "ipa": "/ɪˈfɛdrəz/", "vi": "cây ma hoàng thảo dược làm thuốc"},
  {"id": "lex.en.200k.062958", "hw": "ethnologists", "pos": "noun", "ipa": "/ɛθˈnɑːlədʒɪsts/", "vi": "nhà dân tộc học nghiên cứu văn hóa"},
  {"id": "lex.en.200k.062959", "hw": "fledges", "pos": "verb", "ipa": "/ˈflɛdʒɪz/", "vi": "nuôi chim non đủ lông bay; mọc lông"},
  {"id": "lex.en.200k.062960", "hw": "fledging", "pos": "verb", "ipa": "/ˈflɛdʒɪŋ/", "vi": "đang nuôi chim mọc lông; ra ràng"},
  {"id": "lex.en.200k.062961", "hw": "flowerpots", "pos": "noun", "ipa": "/ˈflaʊərpɑːts/", "vi": "chậu đất nung hoặc nhựa trồng hoa"},
  {"id": "lex.en.200k.062962", "hw": "foxtails", "pos": "noun", "ipa": "/ˈfɑːksteɪlz/", "vi": "cỏ đuôi cáo bông xù; lông đuôi cáo"},
  {"id": "lex.en.200k.062963", "hw": "frauleins", "pos": "noun", "ipa": "/ˈfrɔɪlaɪnz/", "vi": "cô gái trẻ chưa chồng (tiếng Đức)"},
  {"id": "lex.en.200k.062964", "hw": "fullerenes", "pos": "noun", "ipa": "/ˈfʊləriːnz/", "vi": "phân tử cacbon hình cầu rỗng"},
  {"id": "lex.en.200k.062965", "hw": "gamecocks", "pos": "noun", "ipa": "/ˈɡeɪmkɑːks/", "vi": "gà trống chọi nuôi để thi đấu"},
  {"id": "lex.en.200k.062966", "hw": "gessos", "pos": "noun", "ipa": "/ˈdʒɛsoʊz/", "vi": "lớp sơn lót thạch cao vẽ tranh"},
  {"id": "lex.en.200k.062967", "hw": "gonnes", "pos": "noun", "ipa": "/ɡɑːnz/", "vi": "nhà cách mạng Ireland Maud Gonne"},
  {"id": "lex.en.200k.062968", "hw": "goosenecks", "pos": "noun", "ipa": "/ˈɡuːsnɛks/", "vi": "ống cổ ngỗng uốn cong đàn hồi"},
  {"id": "lex.en.200k.062969", "hw": "harmattans", "pos": "noun", "ipa": "/ˌhɑːrməˈtænz/", "vi": "gió mùa khô bụi sa mạc Tây Phi"},
  {"id": "lex.en.200k.062970", "hw": "hieroglyphs", "pos": "noun", "ipa": "/ˈhaɪərəɡlɪfs/", "vi": "chữ tượng hình Ai Cập cổ đại"},
  {"id": "lex.en.200k.062971", "hw": "hydromorphones", "pos": "noun", "ipa": "/ˌhaɪdrəˈmɔːrfoʊnz/", "vi": "thuốc giảm đau mạnh hydromorphone"},
  {"id": "lex.en.200k.062972", "hw": "ingrates", "pos": "noun", "ipa": "/ˈɪnɡreɪts/", "vi": "kẻ vô ơn bạc nghĩa bội bạc"},
  {"id": "lex.en.200k.062973", "hw": "interbreeds", "pos": "verb", "ipa": "/ˌɪntərˈbriːdz/", "vi": "lai giống khác loài với nhau"},
  {"id": "lex.en.200k.062974", "hw": "jessamines", "pos": "noun", "ipa": "/ˈdʒɛsəmɪnz/", "vi": "cây hoa nhài thơm; dây lài vàng"},
  {"id": "lex.en.200k.062975", "hw": "jingoes", "pos": "noun", "ipa": "/ˈdʒɪŋɡoʊz/", "vi": "kẻ yêu nước cuồng chiến hiếu thắng"},
  {"id": "lex.en.200k.062976", "hw": "jingos", "pos": "noun", "ipa": "/ˈdʒɪŋɡoʊz/", "vi": "kẻ yêu nước cuồng chiến hiếu thắng"},
  {"id": "lex.en.200k.062977", "hw": "joffres", "pos": "noun", "ipa": "/ˈʒɔːfrəz/", "vi": "thống chế Pháp Joseph Joffre"},
  {"id": "lex.en.200k.062978", "hw": "khalifs", "pos": "noun", "ipa": "/ˈkeɪlɪfs/", "vi": "vua kế vị lãnh tụ Hồi giáo khalip"},
  {"id": "lex.en.200k.062979", "hw": "kilotons", "pos": "noun", "ipa": "/ˈkɪlətʌnz/", "vi": "đơn vị sức nổ một nghìn tấn TNT"},
  {"id": "lex.en.200k.062980", "hw": "kindergartners", "pos": "noun", "ipa": "/ˈkɪndərˌɡɑːrtnərz/", "vi": "học sinh lứa tuổi mẫu giáo"},
  {"id": "lex.en.200k.062981", "hw": "kolns", "pos": "noun", "ipa": "/kɜːlnz/", "vi": "thành phố Köln (Cologne) nước Đức"},
  {"id": "lex.en.200k.062982", "hw": "lasixes", "pos": "noun", "ipa": "/ˈleɪsɪksɪz/", "vi": "thuốc lợi tiểu furosemide Lasix"},
  {"id": "lex.en.200k.062983", "hw": "lepta", "pos": "noun", "ipa": "/ˈlɛptə/", "vi": "hạt cơ bản lepton; tiền xu Hy Lạp"},
  {"id": "lex.en.200k.062984", "hw": "leptons", "pos": "noun", "ipa": "/ˈlɛptɑːnz/", "vi": "hạt cơ bản lepton; xu lepton Hy Lạp"},
  {"id": "lex.en.200k.062985", "hw": "lodestones", "pos": "noun", "ipa": "/ˈloʊdstoʊnz/", "vi": "đá nam châm từ tính tự nhiên"},
  {"id": "lex.en.200k.062986", "hw": "macacas", "pos": "noun", "ipa": "/məˈkeɪkəz/", "vi": "giống khỉ vàng châu Á chi Macaca"},
  {"id": "lex.en.200k.062987", "hw": "mallei", "pos": "noun", "ipa": "/ˈmæliaɪ/", "vi": "xương búa trong tai giữa truyền âm"},
  {"id": "lex.en.200k.062988", "hw": "malleuses", "pos": "noun", "ipa": "/ˈmæliəsɪz/", "vi": "các xương búa nhỏ trong tai giữa"},
  {"id": "lex.en.200k.062989", "hw": "merls", "pos": "noun", "ipa": "/mɜːrlz/", "vi": "chim hoét đen hót hay vùng châu Âu"},
  {"id": "lex.en.200k.062990", "hw": "nestorians", "pos": "noun", "ipa": "/nɛˈstɔːriənz/", "vi": "tín đồ giáo phái Cơ Đốc Nestorius"},
  {"id": "lex.en.200k.062991", "hw": "nightdresses", "pos": "noun", "ipa": "/ˈnaɪtdrɛsɪz/", "vi": "váy áo ngủ dài mềm của phụ nữ"},
  {"id": "lex.en.200k.062992", "hw": "nisans", "pos": "noun", "ipa": "/ˈniːsɑːnz/", "vi": "tháng Nisan mở đầu năm lịch Do Thái"},
  {"id": "lex.en.200k.062993", "hw": "noradrenalines", "pos": "noun", "ipa": "/ˌnɔːrəˈdrɛnəlɪnz/", "vi": "hoóc môn thần kinh noradrenaline"},
  {"id": "lex.en.200k.062994", "hw": "oncorhynchuses", "pos": "noun", "ipa": "/ˌɑːŋkəˈrɪŋkəsɪz/", "vi": "cá hồi Thái Bình Dương Oncorhynchus"},
  {"id": "lex.en.200k.062995", "hw": "oriyas", "pos": "noun", "ipa": "/oʊˈriːəz/", "vi": "người dân và tiếng Oriya Ấn Độ"},
  {"id": "lex.en.200k.062996", "hw": "orthopedists", "pos": "noun", "ipa": "/ˌɔːrθəˈpiːdɪsts/", "vi": "bác sĩ chuyên khoa chỉnh hình xương"},
  {"id": "lex.en.200k.062997", "hw": "pacesetters", "pos": "noun", "ipa": "/ˈpeɪsˌsɛtərz/", "vi": "người dẫn tốc độ; người tiên phong"},
  {"id": "lex.en.200k.062998", "hw": "panadols", "pos": "noun", "ipa": "/ˈpænədɔːlz/", "vi": "thuốc giảm đau hạ sốt Panadol"},
  {"id": "lex.en.200k.062999", "hw": "panicums", "pos": "noun", "ipa": "/ˈpænɪkəmz/", "vi": "cỏ kê và cỏ làm thức ăn chi Panicum"},
  {"id": "lex.en.200k.063000", "hw": "parthias", "pos": "noun", "ipa": "/ˈpɑːrθiəz/", "vi": "đế chế cổ đại Parthia vùng Ba Tư"},
  {"id": "lex.en.200k.063001", "hw": "pastises", "pos": "noun", "ipa": "/pæˈstiːsɪz/", "vi": "rượu hồi khai vị Pháp pastis"},
  {"id": "lex.en.200k.063002", "hw": "petards", "pos": "noun", "ipa": "/pɪˈtɑːrdz/", "vi": "pháo bộc phá phá cổng thành xưa"}
]

with open('scratch/b33_r06_raw_p5.json') as f:
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

with open('scratch/b33_r06_p5.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)
print("Saved scratch/b33_r06_p5.json OK")
