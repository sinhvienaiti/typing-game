import json

items = [
  {"id": "lex.en.200k.065403", "hw": "depressor nerve", "pos": "phrase", "ipa": "/dɪˈprɛsər nɜːrv/", "vi": "dây thần kinh ức chế giảm áp"},
  {"id": "lex.en.200k.065404", "hw": "dilatation and curettage", "pos": "phrase", "ipa": "/ˌdɪləˈteɪʃən ənd ˌkjʊrəˈtɑːʒ/", "vi": "thủ thuật nong và nạo buồng tử cung"},
  {"id": "lex.en.200k.065405", "hw": "ductus deferens", "pos": "phrase", "ipa": "/ˈdʌktəs ˈdɛfərənz/", "vi": "ống dẫn tinh từ mào tinh hoàn"},
  {"id": "lex.en.200k.065406", "hw": "echinoderm family", "pos": "phrase", "ipa": "/ɪˈkaɪnədɜːrm ˈfæməli/", "vi": "họ động vật da gai sao biển nhím"},
  {"id": "lex.en.200k.065407", "hw": "echinoderm genus", "pos": "phrase", "ipa": "/ɪˈkaɪnədɜːrm ˈdʒiːnəs/", "vi": "chi động vật da gai ở đáy biển"},
  {"id": "lex.en.200k.065408", "hw": "emilia coccinea", "pos": "phrase", "ipa": "/ɪˈmɪliə kɑːkˈsɪniə/", "vi": "cây hoa cúc tua đỏ thắm chậu cảnh"},
  {"id": "lex.en.200k.065409", "hw": "emmy noether", "pos": "phrase", "ipa": "/ˈɛmi ˈnɜːrtər/", "vi": "nữ toán học vĩ đại Emmy Noether"},
  {"id": "lex.en.200k.065410", "hw": "ethmoid bone", "pos": "phrase", "ipa": "/ˈɛθmɔɪd boʊn/", "vi": "xương sàng giữa khoang mũi và não"},
  {"id": "lex.en.200k.065411", "hw": "fagus purpurea", "pos": "phrase", "ipa": "/ˈfeɪɡəs pərˈpjʊriə/", "vi": "cây dẻ gai lá màu tím đồng châu Âu"},
  {"id": "lex.en.200k.065412", "hw": "fetlock joint", "pos": "phrase", "ipa": "/ˈfɛtlɑːk dʒɔɪnt/", "vi": "khớp cổ chân dưới của ngựa"},
  {"id": "lex.en.200k.065413", "hw": "fulvic acid", "pos": "phrase", "ipa": "/ˈfʊlvɪk ˈæsɪd/", "vi": "axit hữu cơ đất mùn nông nghiệp"},
  {"id": "lex.en.200k.065414", "hw": "genus alyssum", "pos": "phrase", "ipa": "/ˈdʒiːnəs əˈlɪsəm/", "vi": "chi cây hoa nhỏ lá xám Alyssum"},
  {"id": "lex.en.200k.065415", "hw": "genus bankia", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈbæŋkiə/", "vi": "chi hà đục gỗ ngâm biển Bankia"},
  {"id": "lex.en.200k.065416", "hw": "genus crassula", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈkræsjʊlə/", "vi": "chi sen đá mọng nước Crassula"},
  {"id": "lex.en.200k.065417", "hw": "genus hyaena", "pos": "phrase", "ipa": "/ˈdʒiːnəs haɪˈiːnə/", "vi": "chi linh cẩu vằn ăn xác thối"},
  {"id": "lex.en.200k.065418", "hw": "genus picus", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈpaɪkəs/", "vi": "chi chim gõ kiến xanh lớn Picus"},
  {"id": "lex.en.200k.065419", "hw": "genus salvelinus", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˌsælvəˈlaɪnəs/", "vi": "chi cá hồi suối nước lạnh châu Bắc"},
  {"id": "lex.en.200k.065420", "hw": "genus tribulus", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈtrɪbjʊləs/", "vi": "chi cây bạch tật lê quả gai góc"},
  {"id": "lex.en.200k.065421", "hw": "genus typha", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈtaɪfə/", "vi": "chi cây hương bồ đầm lầy nến nước"},
  {"id": "lex.en.200k.065422", "hw": "genus xanthomonas", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˌzænθəˈmoʊnəs/", "vi": "chi vi khuẩn gây bệnh đốm lá cây"},
  {"id": "lex.en.200k.065423", "hw": "homeobox gene", "pos": "phrase", "ipa": "/ˈhoʊmioʊbɑːks dʒiːn/", "vi": "gen hộp điều hòa phát triển phôi"},
  {"id": "lex.en.200k.065424", "hw": "internal spermatic artery", "pos": "phrase", "ipa": "/ɪnˈtɜːrnəl spɜːrˈmætɪk ˈɑːrtəri/", "vi": "động mạch tinh hoàn trong cấp máu"},
  {"id": "lex.en.200k.065425", "hw": "john hanning speke", "pos": "phrase", "ipa": "/dʒɑːn ˈhænɪŋ spiːk/", "vi": "nhà thám hiểm tìm nguồn sông Nile"},
  {"id": "lex.en.200k.065426", "hw": "knut hamsun", "pos": "phrase", "ipa": "/knuːt ˈhɑːmsʊn/", "vi": "nhà văn Na Uy Nobel Knut Hamsun"},
  {"id": "lex.en.200k.065427", "hw": "loud hailer", "pos": "phrase", "ipa": "/ˈlaʊd ˈheɪlər/", "vi": "loa cầm tay phóng thanh khuếch đại"},
  {"id": "lex.en.200k.065428", "hw": "lupinus albus", "pos": "phrase", "ipa": "/ˈluːpɪnəs ˈælbəs/", "vi": "cây đậu lupin hoa trắng lấy hạt"},
  {"id": "lex.en.200k.065429", "hw": "maldive islands", "pos": "phrase", "ipa": "/ˈmɔːldaɪv ˈaɪləndz/", "vi": "quần đảo san hô Maldives Ấn Độ"},
  {"id": "lex.en.200k.065430", "hw": "middy blouse", "pos": "phrase", "ipa": "/ˈmɪdi blaʊz/", "vi": "áo cánh nữ cổ vuông kiểu thủy thủ"},
  {"id": "lex.en.200k.065431", "hw": "mounded over", "pos": "phrase", "ipa": "/ˈmaʊndɪd ˈoʊvər/", "vi": "đã đắp mô gò lên; đã lên da non"},
  {"id": "lex.en.200k.065432", "hw": "naja naja", "pos": "phrase", "ipa": "/ˈnɑːdʒə ˈnɑːdʒə/", "vi": "rắn hổ mang kính kịch độc Ấn Độ"},
  {"id": "lex.en.200k.065433", "hw": "philibert delorme", "pos": "phrase", "ipa": "/fiːliˈbɛər dəˈlɔːrm/", "vi": "kiến trúc sư Phục Hưng Pháp"},
  {"id": "lex.en.200k.065434", "hw": "prism spectroscope", "pos": "phrase", "ipa": "/ˈprɪzəm ˈspɛktrəˌskoʊp/", "vi": "máy quang phổ tán sắc lăng kính"},
  {"id": "lex.en.200k.065435", "hw": "quercus robur", "pos": "phrase", "ipa": "/ˈkwɜːrkəs ˈroʊbər/", "vi": "cây sồi Anh cổ thụ gỗ bền châu Âu"},
  {"id": "lex.en.200k.065436", "hw": "sauce espagnole", "pos": "phrase", "ipa": "/sɔːs ɛspɑːnˈjoʊl/", "vi": "nước xốt nâu nền tảng ẩm thực Pháp"},
  {"id": "lex.en.200k.065437", "hw": "scalene muscle", "pos": "phrase", "ipa": "/ˈskeɪliːn ˈmʌsəl/", "vi": "cơ bậc thang hai bên cổ nâng sườn"},
  {"id": "lex.en.200k.065438", "hw": "scalene triangle", "pos": "phrase", "ipa": "/ˈskeɪliːn ˈtraɪˌæŋɡəl/", "vi": "tam giác thường ba cạnh không đều"},
  {"id": "lex.en.200k.065439", "hw": "sequoia sempervirens", "pos": "phrase", "ipa": "/sɪˈkwɔɪə ˌsɛmpərˈvɪrənz/", "vi": "cây cù tùng đỏ khổng lồ California"},
  {"id": "lex.en.200k.065440", "hw": "spathe flower", "pos": "phrase", "ipa": "/speɪð ˈflaʊər/", "vi": "hoa mo như cây lan ý, môn trắng"},
  {"id": "lex.en.200k.065441", "hw": "spermatic cord", "pos": "phrase", "ipa": "/spɜːrˈmætɪk kɔːrd/", "vi": "thừng tinh chứa ống dẫn mạch máu"},
  {"id": "lex.en.200k.065442", "hw": "sweet alyssum", "pos": "phrase", "ipa": "/swiːt əˈlɪsəm/", "vi": "hoa nhỏ trắng thơm mọc thảm đất"},
  {"id": "lex.en.200k.065443", "hw": "tappet wrench", "pos": "phrase", "ipa": "/ˈtæpɪt rɛntʃ/", "vi": "cờ lê chuyên chỉnh khe hở xupáp"},
  {"id": "lex.en.200k.065444", "hw": "tenpin bowling", "pos": "phrase", "ipa": "/ˈtɛnpɪn ˈboʊlɪŋ/", "vi": "môn ném bóng bowling mười gỗ chuẩn"},
  {"id": "lex.en.200k.065445", "hw": "tilia japonica", "pos": "phrase", "ipa": "/ˈtɪliə dʒəˈpɑːnɪkə/", "vi": "cây đoạn hoa thơm bản địa Nhật Bản"},
  {"id": "lex.en.200k.065446", "hw": "tongue depressor", "pos": "phrase", "ipa": "/tʌŋ dɪˈprɛsər/", "vi": "que gỗ dẹt đè lưỡi khám cổ họng"},
  {"id": "lex.en.200k.065447", "hw": "undescended testicle", "pos": "phrase", "ipa": "/ˌʌndɪˈsɛndɪd ˈtɛstɪkəl/", "vi": "tật tinh hoàn ẩn chưa xuống bìu"},
  {"id": "lex.en.200k.065448", "hw": "viola odorata", "pos": "phrase", "ipa": "/vaɪˈoʊlə ˌoʊdəˈrɑːtə/", "vi": "hoa violet tím thơm làm nước hoa"},
  {"id": "lex.en.200k.065449", "hw": "viti levu", "pos": "phrase", "ipa": "/ˈviːti ˈleɪvuː/", "vi": "đảo lớn nhất Viti Levu ở Fiji"},
  {"id": "lex.en.200k.065450", "hw": "wych elm", "pos": "phrase", "ipa": "/wɪtʃ ɛlm/", "vi": "cây du núi vỏ nứt mọc rừng châu Âu"},
  {"id": "lex.en.200k.065451", "hw": "wych hazel", "pos": "phrase", "ipa": "/wɪtʃ ˈheɪzəl/", "vi": "cây kim mai hoa vàng Bắc Mỹ"},
  {"id": "lex.en.200k.065452", "hw": "wych hazel plant", "pos": "phrase", "ipa": "/wɪtʃ ˈheɪzəl plænt/", "vi": "cây thuốc kim mai Bắc Mỹ"},
  {"id": "lex.en.200k.065453", "hw": "abkhazes", "pos": "noun", "ipa": "/æbˈkɑːzɪz/", "vi": "người dân tộc vùng Abkhazia Kavkaz"},
  {"id": "lex.en.200k.065454", "hw": "acidophiluses", "pos": "noun", "ipa": "/ˌæsɪˈdɑːfələsɪz/", "vi": "vi khuẩn lợi khuẩn đường ruột sữa"},
  {"id": "lex.en.200k.065455", "hw": "alexanderses", "pos": "noun", "ipa": "/ˌælɪɡˈzændərzɪz/", "vi": "cây cần tây đen dại châu Âu"},
  {"id": "lex.en.200k.065456", "hw": "alkanes", "pos": "noun", "ipa": "/ˈælkeɪnz/", "vi": "hiđrocacbon mạch no đơn ankan"},
  {"id": "lex.en.200k.065457", "hw": "arsenates", "pos": "noun", "ipa": "/ˈɑːrsəneɪts/", "vi": "muối hóa học chứa gốc asenat độc"},
  {"id": "lex.en.200k.065458", "hw": "aspergilloses", "pos": "noun", "ipa": "/ˌæspərdʒəˈloʊsiːz/", "vi": "bệnh nhiễm nấm phổi Aspergillus"},
  {"id": "lex.en.200k.065459", "hw": "aspergillosises", "pos": "noun", "ipa": "/ˌæspərdʒəˈloʊsɪsɪz/", "vi": "các ca nhiễm nấm mốc Aspergillus"},
  {"id": "lex.en.200k.065460", "hw": "auscultations", "pos": "noun", "ipa": "/ˌɔːskəlˈteɪʃənz/", "vi": "phép nghe tim phổi bằng ống nghe"},
  {"id": "lex.en.200k.065461", "hw": "balochis", "pos": "noun", "ipa": "/bəˈloʊtʃiz/", "vi": "người dân và tiếng Balochi Pakistan"},
  {"id": "lex.en.200k.065462", "hw": "benzoins", "pos": "noun", "ipa": "/ˈbɛnzoʊɪnz/", "vi": "nhựa thơm cánh kiến trắng benzoin"},
  {"id": "lex.en.200k.065463", "hw": "bicuspids", "pos": "noun", "ipa": "/baɪˈkʌspɪdz/", "vi": "răng tiền hàm hai múi; van hai lá"},
  {"id": "lex.en.200k.065464", "hw": "bingles", "pos": "noun", "ipa": "/ˈbɪŋɡəlz/", "vi": "cú đánh bóng chạm chốt bóng chày"},
  {"id": "lex.en.200k.065465", "hw": "bioweapons", "pos": "noun", "ipa": "/ˈbaɪoʊˌwɛpənz/", "vi": "vũ khí sinh học vi khuẩn virus"},
  {"id": "lex.en.200k.065466", "hw": "bondholders", "pos": "noun", "ipa": "/ˈbɑːndˌhoʊldərz/", "vi": "người nắm giữ trái phiếu đầu tư"},
  {"id": "lex.en.200k.065467", "hw": "breadsticks", "pos": "noun", "ipa": "/ˈbrɛdstɪks/", "vi": "bánh mì que nướng giòn rụm"},
  {"id": "lex.en.200k.065468", "hw": "brinjals", "pos": "noun", "ipa": "/ˈbrɪndʒɑːlz/", "vi": "quả cà tím nấu ăn (tiếng Ấn Độ)"},
  {"id": "lex.en.200k.065469", "hw": "brocas", "pos": "noun", "ipa": "/ˈbroʊkəz/", "vi": "bác sĩ giải phẫu não Paul Broca"},
  {"id": "lex.en.200k.065470", "hw": "canopuses", "pos": "noun", "ipa": "/kəˈnoʊpəsɪz/", "vi": "ngôi sao sáng thứ hai bầu trời đêm"},
  {"id": "lex.en.200k.065471", "hw": "cassirers", "pos": "noun", "ipa": "/kəˈsɪrərz/", "vi": "triết gia Đức Ernst Cassirer"},
  {"id": "lex.en.200k.065472", "hw": "catharses", "pos": "noun", "ipa": "/kəˈθɑːrsiːz/", "vi": "sự thanh lọc cảm xúc; thuốc xổ"},
  {"id": "lex.en.200k.065473", "hw": "chasubles", "pos": "noun", "ipa": "/ˈtʃæzjəbəlz/", "vi": "áo lễ ngoài không tay của linh mục"},
  {"id": "lex.en.200k.065474", "hw": "chatelaines", "pos": "noun", "ipa": "/ˈʃætəˌleɪnz/", "vi": "dây xà tích đeo chìa khóa; bà chủ"},
  {"id": "lex.en.200k.065475", "hw": "cloudbursts", "pos": "noun", "ipa": "/ˈklaʊdbɜːrsts/", "vi": "trận mưa rào trút nước dữ dội"},
  {"id": "lex.en.200k.065476", "hw": "collegians", "pos": "noun", "ipa": "/kəˈliːdʒənz/", "vi": "sinh viên đang theo học đại học"},
  {"id": "lex.en.200k.065477", "hw": "cosmogonies", "pos": "noun", "ipa": "/kɑːzˈmɑːɡəniz/", "vi": "thuyết nguồn gốc hình thành vũ trụ"},
  {"id": "lex.en.200k.065478", "hw": "cytokineses", "pos": "noun", "ipa": "/ˌsaɪtoʊkəˈniːsiːz/", "vi": "quá trình phân chia tế bào chất"},
  {"id": "lex.en.200k.065479", "hw": "dabas", "pos": "noun", "ipa": "/ˈdɑːbəz/", "vi": "ngôn ngữ Chadic Daba miền bắc Cam"},
  {"id": "lex.en.200k.065480", "hw": "dangerousnesses", "pos": "noun", "ipa": "/ˈdeɪndʒərəsnəsɪz/", "vi": "mức độ tính chất hiểm nguy độc hại"},
  {"id": "lex.en.200k.065481", "hw": "danus", "pos": "noun", "ipa": "/ˈdɑːnuːz/", "vi": "nữ thần đất mẹ Danu thần thoại"},
  {"id": "lex.en.200k.065482", "hw": "diapasons", "pos": "noun", "ipa": "/ˌdaɪəˈpeɪzənz/", "vi": "âm vực hòa âm; ống sáo phong cầm"},
  {"id": "lex.en.200k.065483", "hw": "discourtesies", "pos": "noun", "ipa": "/dɪsˈkɜːrtəsiz/", "vi": "hành vi khiếm nhã thiếu lịch sự"},
  {"id": "lex.en.200k.065484", "hw": "dowdings", "pos": "noun", "ipa": "/ˈdaʊdɪŋz/", "vi": "tướng không quân Anh Hugh Dowding"},
  {"id": "lex.en.200k.065485", "hw": "doxologies", "pos": "noun", "ipa": "/dɑːkˈsɑːlədʒiz/", "vi": "bài thánh ca ngắn tôn vinh Chúa"},
  {"id": "lex.en.200k.065486", "hw": "emboli", "pos": "noun", "ipa": "/ˈɛmbəlaɪ/", "vi": "cục nghẽn mạch di chuyển trong máu"},
  {"id": "lex.en.200k.065487", "hw": "emboluses", "pos": "noun", "ipa": "/ˈɛmbələsɪz/", "vi": "các cục máu đông gây tắc mạch"},
  {"id": "lex.en.200k.065488", "hw": "enterobacteriaceaes", "pos": "noun", "ipa": "/ˌɛntəroʊbækˌtɪriˈeɪsiˌiːz/", "vi": "họ vi khuẩn đường ruột gram âm"},
  {"id": "lex.en.200k.065489", "hw": "esophagitises", "pos": "noun", "ipa": "/ɪˌsɑːfəˈdʒaɪtɪsɪz/", "vi": "bệnh viêm niêm mạc thực quản"},
  {"id": "lex.en.200k.065490", "hw": "fibrils", "pos": "noun", "ipa": "/ˈfaɪbrəlz/", "vi": "vi sợi mảnh cấu trúc cơ và tế bào"},
  {"id": "lex.en.200k.065491", "hw": "fluorouracils", "pos": "noun", "ipa": "/ˌflʊroʊˈjʊrəsɪlz/", "vi": "thuốc hóa trị ung thư fluorouracil"},
  {"id": "lex.en.200k.065492", "hw": "foliates", "pos": "verb", "ipa": "/ˈfoʊlieɪts/", "vi": "nảy lá; dát mỏng lá kim; đánh số"},
  {"id": "lex.en.200k.065493", "hw": "foliating", "pos": "verb", "ipa": "/ˈfoʊliˌeɪtɪŋ/", "vi": "đang nảy lá mới; đang dát lá mỏng"},
  {"id": "lex.en.200k.065494", "hw": "foxhounds", "pos": "noun", "ipa": "/ˈfɑːkshaʊndz/", "vi": "chó săn cáo nhanh nhẹn bền bỉ"},
  {"id": "lex.en.200k.065495", "hw": "galvanis", "pos": "noun", "ipa": "/ɡɑːlˈvɑːniz/", "vi": "nhà sinh học điện Ý Luigi Galvani"},
  {"id": "lex.en.200k.065496", "hw": "gondoliers", "pos": "noun", "ipa": "/ˌɡɑːndəˈlɪərz/", "vi": "người chèo thuyền gondola Venice Ý"},
  {"id": "lex.en.200k.065497", "hw": "granulocytes", "pos": "noun", "ipa": "/ˈɡrænjʊləˌsaɪts/", "vi": "tế bào bạch cầu hạt miễn dịch máu"},
  {"id": "lex.en.200k.065498", "hw": "gyrated", "pos": "verb", "ipa": "/ˈdʒaɪreɪtɪd/", "vi": "đã xoay tròn nhanh theo vòng xoắn"},
  {"id": "lex.en.200k.065499", "hw": "gyrates", "pos": "verb", "ipa": "/ˈdʒaɪreɪts/", "vi": "quay tròn nhanh theo hình xoắn ốc"},
  {"id": "lex.en.200k.065500", "hw": "gyrating", "pos": "verb", "ipa": "/ˈdʒaɪreɪtɪŋ/", "vi": "đang xoay tròn chuyển động xoắn ốc"},
  {"id": "lex.en.200k.065501", "hw": "halevies", "pos": "noun", "ipa": "/ˈhɑːləviz/", "vi": "nhà soạn nhạc opera Pháp Fromental"},
  {"id": "lex.en.200k.065502", "hw": "handshakings", "pos": "noun", "ipa": "/ˈhændˌʃeɪkɪŋz/", "vi": "cái bắt tay chào; giao thức bắt tay"}
]

with open('scratch/b34_r01_raw_p5.json') as f:
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

with open('scratch/b34_r01_p5.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r01_p5.json OK")
