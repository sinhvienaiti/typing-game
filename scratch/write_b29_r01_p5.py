import json

# Manual cognitive QA review for Batch 29 Round 1 Part 5 (IDs 040402 to 040501)
reviewed_items = [
    {"id": "lex.en.200k.040402", "hw": "bassists", "pos": "noun", "ipa": "/ˈbeɪsɪsts/", "vi": "người chơi ghi-ta bass", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040403", "hw": "blockers", "pos": "noun", "ipa": "/ˈblɑːkərz/", "vi": "chất ức chế; cầu thủ cản phá", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040404", "hw": "blowouts", "pos": "noun", "ipa": "/ˈbloʊaʊts/", "vi": "sự nổ lốp xe; trận thắng áp đảo", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040405", "hw": "brisker", "pos": "adj", "ipa": "/ˈbrɪskər/", "vi": "nhanh nhẹn hơn; sảng khoái hơn", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040406", "hw": "briskest", "pos": "adj", "ipa": "/ˈbrɪskɪst/", "vi": "nhanh nhẹn nhất; nhộn nhịp nhất", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040407", "hw": "bubblier", "pos": "adj", "ipa": "/ˈbʌbliər/", "vi": "sủi nhiều bọt hơn; sôi nổi hơn", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040408", "hw": "bubbliest", "pos": "adj", "ipa": "/ˈbʌbliɪst/", "vi": "sủi bọt nhiều nhất; sôi nổi nhất", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040409", "hw": "bummers", "pos": "noun", "ipa": "/ˈbʌmərz/", "vi": "điều thất vọng; trải nghiệm tồi tệ", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040410", "hw": "caspers", "pos": "noun", "ipa": "/ˈkæspərz/", "vi": "thành phố Casper; bóng ma vui vẻ", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040411", "hw": "cauliflowers", "pos": "noun", "ipa": "/ˈkɑːliflaʊərz/", "vi": "các cây súp lơ trắng; bông cải", "cefr": "A2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040412", "hw": "chainsaws", "pos": "noun", "ipa": "/ˈtʃeɪnsɔːz/", "vi": "cưa máy cầm tay; máy cưa xích", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040413", "hw": "cheetahs", "pos": "noun", "ipa": "/ˈtʃiːtəz/", "vi": "loài báo săn gê-pa châu Phi", "cefr": "A2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040414", "hw": "cretes", "pos": "noun", "ipa": "/kriːts/", "vi": "đảo Crete; nền văn minh Crete", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040415", "hw": "cupids", "pos": "noun", "ipa": "/ˈkjuːpɪdz/", "vi": "thần tình yêu Cupid có cánh", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040416", "hw": "detoured", "pos": "verb", "ipa": "/ˈdiːtʊrd/", "vi": "đã đi đường vòng tránh xe", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040417", "hw": "detouring", "pos": "verb", "ipa": "/ˈdiːtʊrɪŋ/", "vi": "đang đi đường tránh xe vòng", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040418", "hw": "detours", "pos": "noun", "ipa": "/ˈdiːtʊrz/", "vi": "tuyến đường vòng; lối đi tránh", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040419", "hw": "dgs", "pos": "noun", "ipa": "/ˌdiːˈdʒiːz/", "vi": "đơn vị đêxigam; mười centigam", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040420", "hw": "dhakas", "pos": "noun", "ipa": "/ˈdɑːkəz/", "vi": "thủ đô Dhaka Bangladesh", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040421", "hw": "enlarges", "pos": "verb", "ipa": "/ɪnˈlɑːrdʒɪz/", "vi": "mở rộng phạm vi; phóng to ảnh", "cefr": "B1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040422", "hw": "enlarging", "pos": "verb", "ipa": "/ɪnˈlɑːrdʒɪŋ/", "vi": "đang mở rộng; đang phóng to ảnh", "cefr": "B1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040423", "hw": "equestrians", "pos": "noun", "ipa": "/ɪˈkwɛstriənz/", "vi": "kỵ sĩ cưỡi ngựa điêu luyện", "cefr": "C1", "tier": "sports", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040424", "hw": "expanses", "pos": "noun", "ipa": "/ɪkˈspænsɪz/", "vi": "dải đất mênh mông; vùng rộng lớn", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040425", "hw": "fanfares", "pos": "noun", "ipa": "/ˈfænfeərz/", "vi": "tiếng kèn hiệu; sự rùm beng", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040426", "hw": "flasks", "pos": "noun", "ipa": "/flæsks/", "vi": "bình giữ nhiệt; bình thí nghiệm", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040427", "hw": "fremonts", "pos": "noun", "ipa": "/ˈfriːmɑːnts/", "vi": "thành phố Fremont; nhà thám hiểm", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040428", "hw": "frostier", "pos": "adj", "ipa": "/ˈfrɔːstiər/", "vi": "lạnh buốt hơn; lạnh lùng hơn", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040429", "hw": "frostiest", "pos": "adj", "ipa": "/ˈfrɔːstiɪst/", "vi": "lạnh cóng nhất; giá lạnh nhất", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040430", "hw": "galileos", "pos": "noun", "ipa": "/ˌɡælɪˈleɪoʊz/", "vi": "nhà bác học Galileo Galilei", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040431", "hw": "germs", "pos": "noun", "ipa": "/dʒɜːrmz/", "vi": "vi trùng mầm bệnh; mầm mống", "cefr": "B1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040432", "hw": "givers", "pos": "noun", "ipa": "/ˈɡɪvərz/", "vi": "người cho tặng; nhà hảo tâm", "cefr": "B1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040433", "hw": "gnomes", "pos": "noun", "ipa": "/noʊmz/", "vi": "chú lùn giữ của; ngạn ngữ ngắn", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040434", "hw": "hadeses", "pos": "noun", "ipa": "/ˈheɪdiːzɪz/", "vi": "âm phủ; địa ngục Hades La Mã", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040435", "hw": "heartaches", "pos": "noun", "ipa": "/ˈhɑːrteɪks/", "vi": "nỗi đau lòng xót xa; đau khổ", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040436", "hw": "hertfordshires", "pos": "noun", "ipa": "/ˈhɑːrtfərdʃɪərz/", "vi": "hạt Hertfordshire nước Anh", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040437", "hw": "homeowners", "pos": "noun", "ipa": "/ˈhoʊmoʊnərz/", "vi": "chủ sở hữu nhà riêng", "cefr": "B1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040438", "hw": "insurgents", "pos": "noun", "ipa": "/ɪnˈsɜːrdʒənts/", "vi": "quân nổi dậy vũ trang; phiến quân", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040439", "hw": "janitors", "pos": "noun", "ipa": "/ˈdʒænɪtərz/", "vi": "người lao công; nhân viên tạp vụ", "cefr": "B1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040440", "hw": "langes", "pos": "noun", "ipa": "/ˈlæŋz/", "vi": "nhiếp ảnh gia Lange; dòng họ Lange", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040441", "hw": "legislators", "pos": "noun", "ipa": "/ˈlɛdʒɪsleɪtərz/", "vi": "nhà lập pháp; nghị sĩ quốc hội", "cefr": "C1", "tier": "academic", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040442", "hw": "limousines", "pos": "noun", "ipa": "/ˈlɪməziːnz/", "vi": "xe ô tô sang trọng limousine", "cefr": "B1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040443", "hw": "lindens", "pos": "noun", "ipa": "/ˈlɪndənz/", "vi": "cây đoạn lá hình tim linden", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040444", "hw": "lithuanians", "pos": "noun", "ipa": "/ˌlɪθjuˈeɪniənz/", "vi": "người dân Litva; người Lithuania", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040445", "hw": "mccormicks", "pos": "noun", "ipa": "/məˈkɔːrmɪks/", "vi": "gia tộc phát minh McCormick", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040446", "hw": "meteorites", "pos": "noun", "ipa": "/ˈmiːtiəraɪts/", "vi": "thiên thạch rơi xuống mặt đất", "cefr": "B2", "tier": "science", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040447", "hw": "milnes", "pos": "noun", "ipa": "/mɪlnz/", "vi": "nhà văn A. A. Milne sáng tác Pooh", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040448", "hw": "mrnas", "pos": "noun", "ipa": "/ˌɛmɑːrɛnˈeɪz/", "vi": "các phân tử ARN thông tin", "cefr": "C1", "tier": "science", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040449", "hw": "nehrus", "pos": "noun", "ipa": "/ˈneɪruːz/", "vi": "thủ tướng Nehru; gia tộc Nehru", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040450", "hw": "obliques", "pos": "noun", "ipa": "/əˈbliːks/", "vi": "cơ xiên bụng; đường xiên chéo", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040451", "hw": "obscurities", "pos": "noun", "ipa": "/əbˈskjʊrətiz/", "vi": "sự vô danh; điều tối nghĩa khó hiểu", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040452", "hw": "odessas", "pos": "noun", "ipa": "/oʊˈdɛsəz/", "vi": "thành phố cảng Odessa", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040453", "hw": "okinawas", "pos": "noun", "ipa": "/ˌoʊkɪˈnɑːwəz/", "vi": "quần đảo Okinawa Nhật Bản", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040454", "hw": "onslaughts", "pos": "noun", "ipa": "/ˈɑːnslɔːts/", "vi": "cuộc tấn công mãnh liệt; đợt ập đến", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040455", "hw": "opals", "pos": "noun", "ipa": "/ˈoʊpəlz/", "vi": "ngọc mắt mèo; đá quý opan ngũ sắc", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040456", "hw": "partridges", "pos": "noun", "ipa": "/ˈpɑːrtrɪdʒɪz/", "vi": "chim đa đa; chim gà gô đồng cỏ", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040457", "hw": "polkaed", "pos": "verb", "ipa": "/ˈpoʊlkəd/", "vi": "đã nhảy điệu vanh xơ polka", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040458", "hw": "polkaing", "pos": "verb", "ipa": "/ˈpoʊlkəɪŋ/", "vi": "đang khiêu vũ điệu polka", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040459", "hw": "polkas", "pos": "noun", "ipa": "/ˈpoʊlkəz/", "vi": "điệu nhảy sôi động polka", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040460", "hw": "rattlings", "pos": "noun", "ipa": "/ˈrætlɪŋz/", "vi": "tiếng kêu lạch cạch lách cách", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040461", "hw": "realisations", "pos": "noun", "ipa": "/ˌriːəlaɪˈzeɪʃənz/", "vi": "sự nhận thức rõ; sự thực hiện hóa", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040462", "hw": "recurrences", "pos": "noun", "ipa": "/rɪˈkɜːrənsɪz/", "vi": "sự tái phát bệnh; sự tái diễn lại", "cefr": "C1", "tier": "medical", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040463", "hw": "rockwells", "pos": "noun", "ipa": "/ˈrɑːkwɛlz/", "vi": "họa sĩ Norman Rockwell minh họa", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040464", "hw": "rodents", "pos": "noun", "ipa": "/ˈroʊdənts/", "vi": "động vật gặm nhấm; chuột bọ", "cefr": "B2", "tier": "science", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040465", "hw": "rudders", "pos": "noun", "ipa": "/ˈrʌdərz/", "vi": "bánh lái thuyền; bánh lái máy bay", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040466", "hw": "rungs", "pos": "noun", "ipa": "/rʌŋz/", "vi": "bậc thang gỗ; nấc thang danh vọng", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040467", "hw": "salahs", "pos": "noun", "ipa": "/səˈlɑːz/", "vi": "lễ cầu nguyện Salah Hồi giáo", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040468", "hw": "seamen", "pos": "noun", "ipa": "/ˈsiːmən/", "vi": "thủy thủ tàu biển; lính hải quân", "cefr": "B1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040469", "hw": "sensibilities", "pos": "noun", "ipa": "/ˌsɛnsəˈbɪlətiz/", "vi": "óc cảm thụ nghệ thuật; sự nhạy cảm", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040470", "hw": "sevillas", "pos": "noun", "ipa": "/seɪˈviːjəz/", "vi": "thành phố Sevilla Tây Ban Nha", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040471", "hw": "skiers", "pos": "noun", "ipa": "/ˈskiːərz/", "vi": "vận động viên trượt tuyết mùa đông", "cefr": "B1", "tier": "sports", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040472", "hw": "skyscrapers", "pos": "noun", "ipa": "/ˈskaɪskreɪpərz/", "vi": "tòa nhà chọc trời cao tầng", "cefr": "A2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040473", "hw": "stauncher", "pos": "adj", "ipa": "/ˈstɔːntʃər/", "vi": "trung thành hơn; kiên định hơn", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040474", "hw": "staunchest", "pos": "adj", "ipa": "/ˈstɔːntʃɪst/", "vi": "kiên định nhất; tận tụy nhất", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040475", "hw": "stuttgarts", "pos": "noun", "ipa": "/ˈʃtʊtɡɑːrts/", "vi": "thành phố Stuttgart công nghiệp Đức", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040476", "hw": "swooped", "pos": "verb", "ipa": "/swuːpt/", "vi": "đã sà xuống vồ mồi; ập tới bắt", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040477", "hw": "swooping", "pos": "verb", "ipa": "/ˈswuːpɪŋ/", "vi": "đang nhào sà xuống; đang vồ mồi", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040478", "hw": "swoops", "pos": "noun", "ipa": "/swuːps/", "vi": "cú sà xuống bắt mồi; đòn ập tới", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040479", "hw": "tallahassees", "pos": "noun", "ipa": "/ˌtæləˈhæsiz/", "vi": "thủ phủ Tallahassee bang Florida", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040480", "hw": "terences", "pos": "noun", "ipa": "/ˈtɛrənsɪz/", "vi": "nhà viết kịch Terence La Mã", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040481", "hw": "tias", "pos": "noun", "ipa": "/ˈtiːəz/", "vi": "cơn thiếu máu não thoáng qua", "cefr": "C2", "tier": "medical", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040482", "hw": "tunisians", "pos": "noun", "ipa": "/tuːˈnɪʒənz/", "vi": "người dân Tunisia Bắc Phi", "cefr": "B1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040483", "hw": "ugandans", "pos": "noun", "ipa": "/juːˈɡændənz/", "vi": "người dân Uganda Đông Phi", "cefr": "B1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040484", "hw": "unworthier", "pos": "adj", "ipa": "/ʌnˈwɜːrðiər/", "vi": "kém xứng đáng hơn; đê tiện hơn", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040485", "hw": "unworthiest", "pos": "adj", "ipa": "/ʌnˈwɜːrðiɪst/", "vi": "kém xứng đáng nhất; tồi tệ nhất", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040486", "hw": "vocations", "pos": "noun", "ipa": "/voʊˈkeɪʃənz/", "vi": "thiên hướng nghề nghiệp; sứ mệnh", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040487", "hw": "winslows", "pos": "noun", "ipa": "/ˈwɪnzloʊz/", "vi": "họa sĩ Winslow Homer; vùng Winslow", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040488", "hw": "zus", "pos": "noun", "ipa": "/zuːz/", "vi": "quái điểu Zu trong thần thoại Sumer", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040489", "hw": "abraham stoker", "pos": "phrase", "ipa": "", "vi": "nhà văn Bram Stoker tác giả Dracula", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040490", "hw": "absorbent material", "pos": "phrase", "ipa": "", "vi": "vật liệu thấm hút chất lỏng", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040491", "hw": "accounts receivable", "pos": "phrase", "ipa": "", "vi": "các khoản công nợ phải thu", "cefr": "B2", "tier": "business", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040492", "hw": "aerial tramway", "pos": "phrase", "ipa": "", "vi": "tuyến cáp treo trên không", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040493", "hw": "agate line", "pos": "phrase", "ipa": "", "vi": "dòng agate đo cột báo chí", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040494", "hw": "alkyl group", "pos": "phrase", "ipa": "", "vi": "gốc hidrocacbon ankyl hóa học", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040495", "hw": "ambulatory plague", "pos": "phrase", "ipa": "", "vi": "dịch hạch thể nhẹ đi lại được", "cefr": "C2", "tier": "medical", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040496", "hw": "american mistletoe", "pos": "phrase", "ipa": "", "vi": "cây tầm gửi Bắc Mỹ hoa trắng", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040497", "hw": "ammonium carbonate", "pos": "phrase", "ipa": "", "vi": "amoni cacbonat; muối làm nở bột", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040498", "hw": "amyloid plaque", "pos": "phrase", "ipa": "", "vi": "mảng xơ amyloid ở não", "cefr": "C2", "tier": "medical", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040499", "hw": "andrei markov", "pos": "phrase", "ipa": "", "vi": "nhà toán học Andrei Markov", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040500", "hw": "aster family", "pos": "phrase", "ipa": "", "vi": "họ thực vật hoa Cúc hướng dương", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040501", "hw": "atlantic manta", "pos": "phrase", "ipa": "", "vi": "cá nạng hải Đại Tây Dương khổng lồ", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""}
]

# Validation
ALLOWED_POS = {"noun", "verb", "adj", "adv", "intj", "prep", "conj", "pron", "det", "num", "phrase"}
with open('scratch/b29_r01_raw_p5.json', 'r', encoding='utf-8') as f:
    raw_items = json.load(f)

assert len(reviewed_items) == 100, f"Expected 100 items, got {len(reviewed_items)}"
for r, rev in zip(raw_items, reviewed_items):
    assert r["id"] == rev["id"], f"ID mismatch: {r['id']} vs {rev['id']}"
    assert r["hw"] == rev["hw"], f"HW mismatch: {r['hw']} vs {rev['hw']}"
    assert rev["pos"] in ALLOWED_POS, f"Invalid POS for {rev['id']}: {rev['pos']}"
    assert 0 < len(rev["vi"]) <= 35, f"Invalid VI length ({len(rev['vi'])}) for {rev['id']}: {rev['vi']}"
    assert rev["status"] == "reviewed", f"Status must be reviewed: {rev['id']}"
    if " " not in rev["hw"]:
        assert rev["ipa"].startswith("/") and rev["ipa"].endswith("/") and rev["ipa"].count("/") == 2, f"Invalid single-word IPA: {rev['id']}: {rev['ipa']}"

with open('scratch/b29_r01_p5.json', 'w', encoding='utf-8') as f:
    json.dump(reviewed_items, f, ensure_ascii=False, indent=2)

print("Batch 29 Round 1 Part 5 validated and written successfully. Total items:", len(reviewed_items))
