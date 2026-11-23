import json

items = [
  {"id": "lex.en.200k.058802", "hw": "norfolk wherry", "pos": "phrase", "ipa": "/ˈnɔːrfək ˈwɛri/", "vi": "thuyền buồm chở hàng Norfolk"},
  {"id": "lex.en.200k.058803", "hw": "northern dewberry", "pos": "phrase", "ipa": "/ˈnɔːrðərn ˈduːbɛri/", "vi": "dâu mâm xôi gai phương Bắc"},
  {"id": "lex.en.200k.058804", "hw": "number cruncher", "pos": "phrase", "ipa": "/ˈnʌmbər ˌkrʌntʃər/", "vi": "chuyên gia tính toán số liệu"},
  {"id": "lex.en.200k.058805", "hw": "paul johannes tillich", "pos": "phrase", "ipa": "/pɔːl joʊˈhænəs ˈtɪlɪx/", "vi": "nhà thần học Paul Tillich"},
  {"id": "lex.en.200k.058806", "hw": "positive chemotaxis", "pos": "phrase", "ipa": "/ˈpɑːzətɪv ˌkiːmoʊˈtæksɪs/", "vi": "hướng hóa dương; tiến về hóa chất"},
  {"id": "lex.en.200k.058807", "hw": "queensland kauri", "pos": "phrase", "ipa": "/ˈkwiːnzlənd ˈkaʊri/", "vi": "cây thông kauri Queensland"},
  {"id": "lex.en.200k.058808", "hw": "quercus ilex", "pos": "phrase", "ipa": "/ˈkwɜːrkəs ˈaɪlɛks/", "vi": "loài sồi thường xanh holm oak"},
  {"id": "lex.en.200k.058809", "hw": "red kauri", "pos": "phrase", "ipa": "/rɛd ˈkaʊri/", "vi": "loài cây thông kauri đỏ"},
  {"id": "lex.en.200k.058810", "hw": "redbird cactus", "pos": "phrase", "ipa": "/ˈrɛdbɜːrd ˈkæktəs/", "vi": "cây xương rồng chim đỏ"},
  {"id": "lex.en.200k.058811", "hw": "sarah kemble siddons", "pos": "phrase", "ipa": "/ˈsɛərə ˈkɛmbəl ˈsɪdənz/", "vi": "nữ diễn viên kịch Sarah Siddons"},
  {"id": "lex.en.200k.058812", "hw": "shuttlecock fern", "pos": "phrase", "ipa": "/ˈʃʌtlkɑːk fɜːrn/", "vi": "dương xỉ đà điểu hình cầu lông"},
  {"id": "lex.en.200k.058813", "hw": "southern dewberry", "pos": "phrase", "ipa": "/ˈsʌðərn ˈduːbɛri/", "vi": "dâu mâm xôi gai phương Nam"},
  {"id": "lex.en.200k.058814", "hw": "spider nevus", "pos": "phrase", "ipa": "/ˈspaɪdər ˈniːvəs/", "vi": "nốt ruồi mạng nhện; u mạch máu"},
  {"id": "lex.en.200k.058815", "hw": "stagnant anoxia", "pos": "phrase", "ipa": "/ˈstæɡnənt ænˈɑːksiə/", "vi": "thiếu oxy do máu ứ trệ"},
  {"id": "lex.en.200k.058816", "hw": "stereophonic system", "pos": "phrase", "ipa": "/ˌstɛrioʊˈfɑːnɪk ˈsɪstəm/", "vi": "hệ thống âm thanh nổi hai kênh"},
  {"id": "lex.en.200k.058817", "hw": "stipendiary magistrate", "pos": "phrase", "ipa": "/stɪˈpɛndiɛri ˈmædʒɪstreɪt/", "vi": "thẩm phán sơ thẩm chuyên nghiệp"},
  {"id": "lex.en.200k.058818", "hw": "strix occidentalis", "pos": "phrase", "ipa": "/strɪks ˌɑːksɪdɛnˈteɪlɪs/", "vi": "loài cú đốm phương tây"},
  {"id": "lex.en.200k.058819", "hw": "thomas kyd", "pos": "phrase", "ipa": "/ˈtɑːməs kɪd/", "vi": "nhà viết kịch Thomas Kyd"},
  {"id": "lex.en.200k.058820", "hw": "varicella zoster virus", "pos": "phrase", "ipa": "/ˌværəˈsɛlə ˈzɑːstər ˈvaɪrəs/", "vi": "vi-rút gây bệnh thủy đậu zona"},
  {"id": "lex.en.200k.058821", "hw": "videocassette recorder", "pos": "phrase", "ipa": "/ˌvɪdioʊkəˈsɛt rɪˈkɔːrdər/", "vi": "đầu máy ghi phát băng video"},
  {"id": "lex.en.200k.058822", "hw": "viscount northcliffe", "pos": "phrase", "ipa": "/ˈvaɪkaʊnt ˈnɔːrθklɪf/", "vi": "Tử tước Northcliffe trùm báo chí"},
  {"id": "lex.en.200k.058823", "hw": "western dewberry", "pos": "phrase", "ipa": "/ˈwɛstərn ˈduːbɛri/", "vi": "loài dâu mâm xôi miền tây"},
  {"id": "lex.en.200k.058824", "hw": "william of ockham", "pos": "phrase", "ipa": "/ˈwɪljəm əv ˈɑːkəm/", "vi": "triết gia William xứ Ockham"},
  {"id": "lex.en.200k.058825", "hw": "abelards", "pos": "noun", "ipa": "/ˈæbəlɑːrdz/", "vi": "triết gia Pierre Abélard"},
  {"id": "lex.en.200k.058826", "hw": "alcibiadeses", "pos": "noun", "ipa": "/ˌælsɪbˈaɪədiːzɪz/", "vi": "tướng Alcibiades Hy Lạp cổ"},
  {"id": "lex.en.200k.058827", "hw": "ataturks", "pos": "noun", "ipa": "/ˈætətɜːrks/", "vi": "lãnh tụ Thổ Nhĩ Kỳ Atatürk"},
  {"id": "lex.en.200k.058828", "hw": "austerlitzes", "pos": "noun", "ipa": "/ˈɔːstərlɪtsɪz/", "vi": "trận đại chiến Austerlitz"},
  {"id": "lex.en.200k.058829", "hw": "awns", "pos": "noun", "ipa": "/ˈɔːnz/", "vi": "râu bông lúa; râu hạt ngũ cốc"},
  {"id": "lex.en.200k.058830", "hw": "backbenchers", "pos": "noun", "ipa": "/bˈækˌbɛntʃɚz/", "vi": "nghị sĩ thường hàng ghế sau"},
  {"id": "lex.en.200k.058831", "hw": "ballplayers", "pos": "noun", "ipa": "/bɔlplˈeɪɚz/", "vi": "cầu thủ bóng chày; vận động viên"},
  {"id": "lex.en.200k.058832", "hw": "bartlesvilles", "pos": "noun", "ipa": "/bˈɑːrtlzvɪlz/", "vi": "thành phố Bartlesville"},
  {"id": "lex.en.200k.058833", "hw": "boccaccios", "pos": "noun", "ipa": "/boʊkˈɑːtʃioʊz/", "vi": "nhà văn Giovanni Boccaccio"},
  {"id": "lex.en.200k.058834", "hw": "bonaires", "pos": "noun", "ipa": "/bɒnˈɛərz/", "vi": "đảo Bonaire ở biển Caribe"},
  {"id": "lex.en.200k.058835", "hw": "bookmans", "pos": "noun", "ipa": "/bˈʊkmənz/", "vi": "người mê sách vở; học giả chữ"},
  {"id": "lex.en.200k.058836", "hw": "brassards", "pos": "noun", "ipa": "/bræsˈɑːrdz/", "vi": "băng đeo tay áo; giáp cánh tay"},
  {"id": "lex.en.200k.058837", "hw": "brinier", "pos": "adj", "ipa": "/brˈaɪniɚ/", "vi": "mặn chát hơn; nhiều muối hơn"},
  {"id": "lex.en.200k.058838", "hw": "briniest", "pos": "adj", "ipa": "/brˈaɪniɪst/", "vi": "mặn chát nhất; nhiều muối nhất"},
  {"id": "lex.en.200k.058839", "hw": "brintons", "pos": "noun", "ipa": "/brˈɪntənz/", "vi": "học giả Brinton"},
  {"id": "lex.en.200k.058840", "hw": "carbuncles", "pos": "noun", "ipa": "/kˈɑːrbʌŋklz/", "vi": "ổ nhọt cụm; viên ngọc hồng lựu"},
  {"id": "lex.en.200k.058841", "hw": "casbahs", "pos": "noun", "ipa": "/kˈæzbɑːz/", "vi": "khu thành quách cổ casbah"},
  {"id": "lex.en.200k.058842", "hw": "chastisements", "pos": "noun", "ipa": "/tʃæstˈaɪzmənts/", "vi": "hình phạt trừng giới; sự khiển phạt"},
  {"id": "lex.en.200k.058843", "hw": "chickenshits", "pos": "noun", "ipa": "/tʃˈɪkənʃɪts/", "vi": "trò vớ vẩn hèn hạ; kẻ nhát gan"},
  {"id": "lex.en.200k.058844", "hw": "clemenceaus", "pos": "noun", "ipa": "/klɛmənzˈoʊz/", "vi": "thủ tướng Georges Clemenceau"},
  {"id": "lex.en.200k.058845", "hw": "dbmses", "pos": "noun", "ipa": "/dˌiːbiːɛmˈɛsɪz/", "vi": "hệ quản trị cơ sở dữ liệu"},
  {"id": "lex.en.200k.058846", "hw": "devrieses", "pos": "noun", "ipa": "/dəvrˈiːsɪz/", "vi": "nhà thực vật học Hugo de Vries"},
  {"id": "lex.en.200k.058847", "hw": "distaffs", "pos": "noun", "ipa": "/dˈɪstæfs/", "vi": "cọc kéo sợi; phái nữ nhà ngoại"},
  {"id": "lex.en.200k.058848", "hw": "duvaliers", "pos": "noun", "ipa": "/duvˈeɪljɚz/", "vi": "gia tộc độc tài Duvalier"},
  {"id": "lex.en.200k.058849", "hw": "elastomers", "pos": "noun", "ipa": "/ɪlˈæstəmɚz/", "vi": "chất polyme có tính đàn hồi cao"},
  {"id": "lex.en.200k.058850", "hw": "entangles", "pos": "verb", "ipa": "/ɪntˈæŋɡəlz/", "vi": "làm vướng víu; khiến vướng vào"},
  {"id": "lex.en.200k.058851", "hw": "entangling", "pos": "verb", "ipa": "/ɪntˈæŋlɪŋ/", "vi": "làm vướng víu; gây trói buộc"},
  {"id": "lex.en.200k.058852", "hw": "feriae", "pos": "noun", "ipa": "/fˈɛriiː/", "vi": "ngày làm việc thường phụng vụ"},
  {"id": "lex.en.200k.058853", "hw": "ferias", "pos": "noun", "ipa": "/fˈɛriəz/", "vi": "ngày thường trong tuần thánh"},
  {"id": "lex.en.200k.058854", "hw": "fibrinogens", "pos": "noun", "ipa": "/faɪbrˈɪnədʒənz/", "vi": "protein đông máu fibrinogen"},
  {"id": "lex.en.200k.058855", "hw": "funfairs", "pos": "noun", "ipa": "/fˈʌnfɛrz/", "vi": "hội chợ vui chơi ngoài trời"},
  {"id": "lex.en.200k.058856", "hw": "gcas", "pos": "noun", "ipa": "/dʒˌiːsiːˈeɪz/", "vi": "hệ radar hướng dẫn tiếp đất máy bay"},
  {"id": "lex.en.200k.058857", "hw": "gimlets", "pos": "noun", "ipa": "/ɡˈɪmlɪts/", "vi": "mũi khoan xoắn; cocktail rượu gin"},
  {"id": "lex.en.200k.058858", "hw": "goddaughters", "pos": "noun", "ipa": "/ɡˈɑːddɔːtɚz/", "vi": "con gái đỡ đầu"},
  {"id": "lex.en.200k.058859", "hw": "gravures", "pos": "noun", "ipa": "/ɡrəvjˈʊərz/", "vi": "kỹ thuật in ống đồng khắc lõm"},
  {"id": "lex.en.200k.058860", "hw": "gryphons", "pos": "noun", "ipa": "/ɡrˈɪfənz/", "vi": "quái thú đầu đại bàng mình sư tử"},
  {"id": "lex.en.200k.058861", "hw": "haplotypes", "pos": "noun", "ipa": "/hˈæploʊtaɪps/", "vi": "tập hợp gen liên kết haplotype"},
  {"id": "lex.en.200k.058862", "hw": "harpists", "pos": "noun", "ipa": "/hˈɑrpɪsts/", "vi": "nghệ sĩ chơi đàn hạc cầm"},
  {"id": "lex.en.200k.058863", "hw": "hirschfelds", "pos": "noun", "ipa": "/hˈɜːrʃfɛldz/", "vi": "họa sĩ biếm họa Hirschfeld"},
  {"id": "lex.en.200k.058864", "hw": "incongruities", "pos": "noun", "ipa": "/ˌɪnkəŋɡrˈuːətiz/", "vi": "sự bất hợp lý; nét khập khiễng"},
  {"id": "lex.en.200k.058865", "hw": "inheritors", "pos": "noun", "ipa": "/ɪnhˈɛrətɚz/", "vi": "người thừa kế di sản"},
  {"id": "lex.en.200k.058866", "hw": "langmuirs", "pos": "noun", "ipa": "/lˈæŋmjʊərz/", "vi": "nhà hóa học Irving Langmuir"},
  {"id": "lex.en.200k.058867", "hw": "lendls", "pos": "noun", "ipa": "/lˈɛndəlz/", "vi": "tay vợt huyền thoại Ivan Lendl"},
  {"id": "lex.en.200k.058868", "hw": "libations", "pos": "noun", "ipa": "/laɪbˈeɪʃənz/", "vi": "lễ rưới rượu cúng; chén rượu mời"},
  {"id": "lex.en.200k.058869", "hw": "llanos", "pos": "noun", "ipa": "/lˈɑnoʊz/", "vi": "thảo nguyên nhiệt đới llanos"},
  {"id": "lex.en.200k.058870", "hw": "loewes", "pos": "noun", "ipa": "/lˈoʊvz/", "vi": "nhà soạn nhạc Frederick Loewe"},
  {"id": "lex.en.200k.058871", "hw": "loggias", "pos": "noun", "ipa": "/lˈɑːdʒiəz/", "vi": "hành lang hiên nhà mở có vòm"},
  {"id": "lex.en.200k.058872", "hw": "loggie", "pos": "noun", "ipa": "/lˈɑːdʒi/", "vi": "hành lang có mái che hở cạnh"},
  {"id": "lex.en.200k.058873", "hw": "lupines", "pos": "noun", "ipa": "/lˈuːpɪnz/", "vi": "loài hoa lupin thuộc họ đậu"},
  {"id": "lex.en.200k.058874", "hw": "matzos", "pos": "noun", "ipa": "/mˈɑːtsoʊz/", "vi": "bánh tráng không men Do Thái"},
  {"id": "lex.en.200k.058875", "hw": "matzot", "pos": "noun", "ipa": "/mˈɑːtsoʊt/", "vi": "bánh không men lễ Vượt Qua"},
  {"id": "lex.en.200k.058876", "hw": "matzoth", "pos": "noun", "ipa": "/mˈɑːtsoʊθ/", "vi": "bánh không men truyền thống Do Thái"},
  {"id": "lex.en.200k.058877", "hw": "meltwaters", "pos": "noun", "ipa": "/mˈɛltwɔːtɚz/", "vi": "dòng nước tuyết băng tan"},
  {"id": "lex.en.200k.058878", "hw": "mezcals", "pos": "noun", "ipa": "/mɛzkˈælz/", "vi": "rượu chưng cất cây thùa mezcal"},
  {"id": "lex.en.200k.058879", "hw": "misanthropes", "pos": "noun", "ipa": "/mˈɪsənθroʊps/", "vi": "kẻ căm ghét loài người; ghét đời"},
  {"id": "lex.en.200k.058880", "hw": "misbehaviours", "pos": "noun", "ipa": "/ˌmɪsbɪhˈeɪvjɚz/", "vi": "hành vi cư xử sai trái; vô phép"},
  {"id": "lex.en.200k.058881", "hw": "morticians", "pos": "noun", "ipa": "/mɔːrtˈɪʃənz/", "vi": "người làm dịch vụ tang lễ mai táng"},
  {"id": "lex.en.200k.058882", "hw": "northeastwards", "pos": "adv", "ipa": "/nɔːrθˈiːstwərdz/", "vi": "về phía đông bắc; hướng đông bắc"},
  {"id": "lex.en.200k.058883", "hw": "opcws", "pos": "noun", "ipa": "/ˌoʊpiːsiːdˈʌbəljuːz/", "vi": "Tổ chức Cấm Vũ khí Hóa học"},
  {"id": "lex.en.200k.058884", "hw": "paganinis", "pos": "noun", "ipa": "/pˌæɡənˈiːniz/", "vi": "nghệ sĩ vĩ cầm Paganini"},
  {"id": "lex.en.200k.058885", "hw": "pahlavis", "pos": "noun", "ipa": "/pˈɑːhləviz/", "vi": "vương triều Pahlavi của Ba Tư"},
  {"id": "lex.en.200k.058886", "hw": "palfreys", "pos": "noun", "ipa": "/pˈɔːlfriz/", "vi": "ngựa cưỡi nhẹ thời trung cổ"},
  {"id": "lex.en.200k.058887", "hw": "pappas", "pos": "noun", "ipa": "/pˈæpəs/", "vi": "người cha; ông bố thân thương"},
  {"id": "lex.en.200k.058888", "hw": "paracelsi", "pos": "noun", "ipa": "/ˌpærəsˈɛlsaɪ/", "vi": "thầy thuốc Paracelsus"},
  {"id": "lex.en.200k.058889", "hw": "paranas", "pos": "noun", "ipa": "/pˌærənˈɑːz/", "vi": "sông Paraná ở Nam Mỹ"},
  {"id": "lex.en.200k.058890", "hw": "pawnshops", "pos": "noun", "ipa": "/pˈɔnʃˌɑps/", "vi": "hiệu cầm đồ; tiệm cầm đồ"},
  {"id": "lex.en.200k.058891", "hw": "pearies", "pos": "noun", "ipa": "/pˈɪəriz/", "vi": "nhà thám hiểm Robert Peary"},
  {"id": "lex.en.200k.058892", "hw": "phaetons", "pos": "noun", "ipa": "/fˈeɪətənz/", "vi": "xe ngựa bốn bánh mui trần nhẹ"},
  {"id": "lex.en.200k.058893", "hw": "pigeonholed", "pos": "verb", "ipa": "/pˈɪdʒənhˌoʊld/", "vi": "xếp vào một loại; phân định cứng"},
  {"id": "lex.en.200k.058894", "hw": "pimentos", "pos": "noun", "ipa": "/pɪmˈɛntoʊz/", "vi": "ớt ngọt pimento đỏ mọng"},
  {"id": "lex.en.200k.058895", "hw": "pimpernels", "pos": "noun", "ipa": "/pˈɪmpɚnəlz/", "vi": "cây hoa đỏ cỏ phụng nhãn"},
  {"id": "lex.en.200k.058896", "hw": "posies", "pos": "noun", "ipa": "/pˈoʊziz/", "vi": "bó hoa thơm nhỏ xinh cài áo"},
  {"id": "lex.en.200k.058897", "hw": "positivists", "pos": "noun", "ipa": "/pˈɑːzətɪvɪsts/", "vi": "người theo chủ nghĩa thực chứng"},
  {"id": "lex.en.200k.058898", "hw": "profundities", "pos": "noun", "ipa": "/prəfˈʌndətiz/", "vi": "sự sâu sắc; điều thâm sâu uyên bác"},
  {"id": "lex.en.200k.058899", "hw": "pusans", "pos": "noun", "ipa": "/pˈuːsænz/", "vi": "thành phố cảng Busan Hàn Quốc"},
  {"id": "lex.en.200k.058900", "hw": "puzzlers", "pos": "noun", "ipa": "/pˈʌzlɚz/", "vi": "câu đố hóc búa; việc nan giải"},
  {"id": "lex.en.200k.058901", "hw": "quickstepped", "pos": "verb", "ipa": "/kwˈɪkstɛpt/", "vi": "khiêu vũ bước nhanh quickstep"}
]

with open('scratch/b32_r08_raw_p4.json') as f:
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

with open('scratch/b32_r08_p4.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

print("Part 4 validated and written successfully.")
