import json

items = [
  {"id": "lex.en.200k.061103", "hw": "niameys", "pos": "noun", "ipa": "/niˈɑːmeɪz/", "vi": "thủ đô Niamey của nước Niger"},
  {"id": "lex.en.200k.061104", "hw": "nonpareils", "pos": "noun", "ipa": "/ˌnɑːnpəˈrɛlz/", "vi": "kẹo rắc đường màu; người vô song"},
  {"id": "lex.en.200k.061105", "hw": "northers", "pos": "noun", "ipa": "/ˈnɔːrðərz/", "vi": "cơn gió rét thổi mạnh từ hướng bắc"},
  {"id": "lex.en.200k.061106", "hw": "oglalas", "pos": "noun", "ipa": "/oʊˈɡlɑːləz/", "vi": "tộc người da đỏ Oglala Lakota"},
  {"id": "lex.en.200k.061107", "hw": "olmecs", "pos": "noun", "ipa": "/ˈɑːlmɛks/", "vi": "nền văn minh cổ đại Olmec Mexico"},
  {"id": "lex.en.200k.061108", "hw": "orogenies", "pos": "noun", "ipa": "/ɔːˈrɑːdʒəniz/", "vi": "quá trình tạo núi kiến tạo địa tầng"},
  {"id": "lex.en.200k.061109", "hw": "outscored", "pos": "verb", "ipa": "/aʊtˈskɔːrd/", "vi": "đã ghi điểm vượt trội hơn đối thủ"},
  {"id": "lex.en.200k.061110", "hw": "outscores", "pos": "verb", "ipa": "/aʊtˈskɔːrz/", "vi": "ghi nhiều điểm hơn đối thủ"},
  {"id": "lex.en.200k.061111", "hw": "outscoring", "pos": "verb", "ipa": "/aʊtˈskɔːrɪŋ/", "vi": "đang ghi điểm dẫn trước vượt trội"},
  {"id": "lex.en.200k.061112", "hw": "pedicels", "pos": "noun", "ipa": "/ˈpɛdɪsəlz/", "vi": "cuống nhỏ hoa; cuống chân sinh học"},
  {"id": "lex.en.200k.061113", "hw": "plautuses", "pos": "noun", "ipa": "/ˈplɔːtəsɪz/", "vi": "nhà viết hài kịch La Mã Plautus"},
  {"id": "lex.en.200k.061114", "hw": "porphyrias", "pos": "noun", "ipa": "/pɔːrˈfɪriəz/", "vi": "nhóm bệnh rối loạn chuyển hóa máu"},
  {"id": "lex.en.200k.061115", "hw": "reworded", "pos": "verb", "ipa": "/riːˈwɜːrdɪd/", "vi": "đã sửa câu chữ; đã diễn đạt lại ý"},
  {"id": "lex.en.200k.061116", "hw": "rewords", "pos": "verb", "ipa": "/riːˈwɜːrdz/", "vi": "viết lại câu từ; diễn đạt lại ý"},
  {"id": "lex.en.200k.061117", "hw": "rheologies", "pos": "noun", "ipa": "/riːˈɑːlədʒiz/", "vi": "ngành lưu biến học biến dạng chất"},
  {"id": "lex.en.200k.061118", "hw": "rheumatologists", "pos": "noun", "ipa": "/ˌruːməˈtɑːlədʒɪsts/", "vi": "bác sĩ chuyên khoa cơ xương khớp"},
  {"id": "lex.en.200k.061119", "hw": "rickenbackers", "pos": "noun", "ipa": "/ˈrɪkənbækərz/", "vi": "phi công chiến đấu Rickenbacker"},
  {"id": "lex.en.200k.061120", "hw": "rioters", "pos": "noun", "ipa": "/ˈraɪətərz/", "vi": "kẻ gây bạo loạn; người nổi loạn"},
  {"id": "lex.en.200k.061121", "hw": "riveters", "pos": "noun", "ipa": "/ˈrɪvətərz/", "vi": "thợ tán đinh; súng bắn đinh tán"},
  {"id": "lex.en.200k.061122", "hw": "ryas", "pos": "noun", "ipa": "/ˈriːəz/", "vi": "tấm thảm dệt lông xù rya Bắc Âu"},
  {"id": "lex.en.200k.061123", "hw": "sambars", "pos": "noun", "ipa": "/ˈsɑːmbɑːrz/", "vi": "nai rừng sambar; món súp sambar Ấn"},
  {"id": "lex.en.200k.061124", "hw": "schwanns", "pos": "noun", "ipa": "/ʃvɑːnz/", "vi": "nhà sinh lý học Đức Theodor Schwann"},
  {"id": "lex.en.200k.061125", "hw": "seurats", "pos": "noun", "ipa": "/sɜːˈrɑːz/", "vi": "họa sĩ Pháp Georges Seurat"},
  {"id": "lex.en.200k.061126", "hw": "sheldrakes", "pos": "noun", "ipa": "/ˈʃɛldreɪks/", "vi": "loài vịt khoang mỏ đỏ ven biển"},
  {"id": "lex.en.200k.061127", "hw": "skullcaps", "pos": "noun", "ipa": "/ˈskʌlkæps/", "vi": "mũ chỏm ôm sát đầu; cây hoàng cầm"},
  {"id": "lex.en.200k.061128", "hw": "slugfests", "pos": "noun", "ipa": "/ˈslʌɡfɛsts/", "vi": "trận đánh đấm ác liệt; màn cãi vã"},
  {"id": "lex.en.200k.061129", "hw": "stompers", "pos": "noun", "ipa": "/ˈstɑːmpərz/", "vi": "người giậm chân mạnh; giày ủng nặng"},
  {"id": "lex.en.200k.061130", "hw": "sunstones", "pos": "noun", "ipa": "/ˈsʌnstoʊnz/", "vi": "đá mặt trời lấp lánh ánh vàng"},
  {"id": "lex.en.200k.061131", "hw": "swashbucklers", "pos": "noun", "ipa": "/ˈswɑːʃbʌklərz/", "vi": "kiếm khách phiêu lưu mạo hiểm"},
  {"id": "lex.en.200k.061132", "hw": "sylvas", "pos": "noun", "ipa": "/ˈsɪlvəz/", "vi": "hệ cây cối rừng rậm một khu vực"},
  {"id": "lex.en.200k.061133", "hw": "tabards", "pos": "noun", "ipa": "/ˈtæbərdz/", "vi": "áo choàng ngắn không tay hiệp sĩ"},
  {"id": "lex.en.200k.061134", "hw": "tartrates", "pos": "noun", "ipa": "/ˈtɑːrtreɪts/", "vi": "muối tinh thể hóa học tartrat"},
  {"id": "lex.en.200k.061135", "hw": "vajras", "pos": "noun", "ipa": "/ˈvʌdʒrəz/", "vi": "chày kim cang pháp khí Mật tông"},
  {"id": "lex.en.200k.061136", "hw": "vandykes", "pos": "noun", "ipa": "/vænˈdaɪks/", "vi": "kiểu râu nhọn; danh họa Van Dyck"},
  {"id": "lex.en.200k.061137", "hw": "vindicators", "pos": "noun", "ipa": "/ˈvɪndɪkeɪtərz/", "vi": "người minh oan; người biện hộ"},
  {"id": "lex.en.200k.061138", "hw": "warplanes", "pos": "noun", "ipa": "/ˈwɔːrpleɪnz/", "vi": "máy bay chiến đấu quân sự"},
  {"id": "lex.en.200k.061139", "hw": "wartier", "pos": "adj", "ipa": "/ˈwɔːrtiər/", "vi": "nhiều mụn cóc sần sùi hơn"},
  {"id": "lex.en.200k.061140", "hw": "wartiest", "pos": "adj", "ipa": "/ˈwɔːrtiɪst/", "vi": "nhiều mụn cóc sần sùi nhất"},
  {"id": "lex.en.200k.061141", "hw": "wastebaskets", "pos": "noun", "ipa": "/ˈweɪstbæskɪts/", "vi": "thùng đựng rác văn phòng; sọt rác"},
  {"id": "lex.en.200k.061142", "hw": "wogs", "pos": "noun", "ipa": "/wɑːɡz/", "vi": "từ lăng mạ kỳ thị người da màu"},
  {"id": "lex.en.200k.061143", "hw": "yids", "pos": "noun", "ipa": "/jɪdz/", "vi": "từ lăng mạ miệt thị người Do Thái"},
  {"id": "lex.en.200k.061144", "hw": "zygomatics", "pos": "noun", "ipa": "/ˌzaɪɡəˈmætɪks/", "vi": "xương gò má; cơ gò má khuôn mặt"},
  {"id": "lex.en.200k.061145", "hw": "allegheny mountain spurge", "pos": "phrase", "ipa": "/ˌælɪˈɡeɪni ˈmaʊntn spɜːrdʒ/", "vi": "cây phú quý núi Allegheny Bắc Mỹ"},
  {"id": "lex.en.200k.061146", "hw": "allegheny spurge", "pos": "phrase", "ipa": "/ˌælɪˈɡeɪni spɜːrdʒ/", "vi": "cây phủ nền phú quý Allegheny"},
  {"id": "lex.en.200k.061147", "hw": "angina pectoris", "pos": "phrase", "ipa": "/ænˈdʒaɪnə ˈpɛktərɪs/", "vi": "cơn đau thắt ngực do thiếu máu tim"},
  {"id": "lex.en.200k.061148", "hw": "artemisia maritima", "pos": "phrase", "ipa": "/ˌɑːrtɪˈmiːʒə məˈrɪtɪmə/", "vi": "cây ngải cứu biển bờ biển châu Âu"},
  {"id": "lex.en.200k.061149", "hw": "banded krait", "pos": "phrase", "ipa": "/ˈbændɪd kreɪt/", "vi": "rắn cạp nong khoang đen vàng độc"},
  {"id": "lex.en.200k.061150", "hw": "battle of cowpens", "pos": "phrase", "ipa": "/ˈbætl əv ˈkaʊpɛnz/", "vi": "trận đánh Cowpens cách mạng Mỹ"},
  {"id": "lex.en.200k.061151", "hw": "billet doux", "pos": "phrase", "ipa": "/ˌbɪleɪ ˈduː/", "vi": "bức thư tình ngọt ngào lãng mạn"},
  {"id": "lex.en.200k.061152", "hw": "calamus australis", "pos": "phrase", "ipa": "/ˈkæləməs ɔːˈstreɪlɪs/", "vi": "cây mây gai leo rừng mưa Úc"},
  {"id": "lex.en.200k.061153", "hw": "carthusian order", "pos": "phrase", "ipa": "/kɑːrˈθuːʒən ˈɔːrdər/", "vi": "dòng tu ẩn tu khổ hạnh Carthusian"},
  {"id": "lex.en.200k.061154", "hw": "chainlink fence", "pos": "phrase", "ipa": "/ˈtʃeɪnlɪŋk fɛns/", "vi": "hàng rào lưới thép mắt cáo B40"},
  {"id": "lex.en.200k.061155", "hw": "crowfoot family", "pos": "phrase", "ipa": "/ˈkroʊfʊt ˈfæməli/", "vi": "họ thực vật Mao lương hoa vàng"},
  {"id": "lex.en.200k.061156", "hw": "crowfoot grass", "pos": "phrase", "ipa": "/ˈkroʊfʊt ɡræs/", "vi": "cỏ chân gà chân vịt mọc hoang"},
  {"id": "lex.en.200k.061157", "hw": "cypress spurge", "pos": "phrase", "ipa": "/ˈsaɪprəs spɜːrdʒ/", "vi": "cây cỏ sữa lá thông bách châu Âu"},
  {"id": "lex.en.200k.061158", "hw": "dilatory plea", "pos": "phrase", "ipa": "/ˈdɪlətɔːri pliː/", "vi": "lời bào chữa nhằm trì hoãn xét xử"},
  {"id": "lex.en.200k.061159", "hw": "eelgrass family", "pos": "phrase", "ipa": "/ˈiːlɡræs ˈfæməli/", "vi": "họ thực vật cỏ lươn biển"},
  {"id": "lex.en.200k.061160", "hw": "ernst cassirer", "pos": "phrase", "ipa": "/ɛrnst kəˈsɪrər/", "vi": "triết gia Đức Ernst Cassirer"},
  {"id": "lex.en.200k.061161", "hw": "filippo brunelleschi", "pos": "phrase", "ipa": "/fɪˈliːpoʊ ˌbruːnəˈlɛski/", "vi": "kiến trúc sư Ý Brunelleschi"},
  {"id": "lex.en.200k.061162", "hw": "genus benzoin", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈbɛnzoʊɪn/", "vi": "chi cây bồ đề nhựa cánh kiến"},
  {"id": "lex.en.200k.061163", "hw": "genus icterus", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈɪktərəs/", "vi": "chi chim vàng anh châu Mỹ Icterus"},
  {"id": "lex.en.200k.061164", "hw": "genus litchi", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈlaɪtʃi/", "vi": "chi thực vật cây vải thiều Litchi"},
  {"id": "lex.en.200k.061165", "hw": "genus nasturtium", "pos": "phrase", "ipa": "/ˈdʒiːnəs nəˈstɜːrʃəm/", "vi": "chi thực vật cải xoong nước"},
  {"id": "lex.en.200k.061166", "hw": "genus puccinia", "pos": "phrase", "ipa": "/ˈdʒiːnəs pʌkˈsɪniə/", "vi": "chi nấm gỉ sắt gây hại cây trồng"},
  {"id": "lex.en.200k.061167", "hw": "giacomo meyerbeer", "pos": "phrase", "ipa": "/dʒəˈkoʊmoʊ ˈmaɪərbɪər/", "vi": "nhà soạn nhạc opera Đức Meyerbeer"},
  {"id": "lex.en.200k.061168", "hw": "grand guignol", "pos": "phrase", "ipa": "/ɡrɑːnd ɡiːˈnjɔːl/", "vi": "kịch kinh dị máu me Grand Guignol"},
  {"id": "lex.en.200k.061169", "hw": "greaseproof paper", "pos": "phrase", "ipa": "/ˈɡriːspruːf ˈpeɪpər/", "vi": "giấy gói thực phẩm chống thấm dầu"},
  {"id": "lex.en.200k.061170", "hw": "john vanbrugh", "pos": "phrase", "ipa": "/dʒɑːn ˈvænbrə/", "vi": "kiến trúc sư kịch tác gia Vanbrugh"},
  {"id": "lex.en.200k.061171", "hw": "kriss kringle", "pos": "phrase", "ipa": "/krɪs ˈkrɪŋɡl/", "vi": "Ông già Noel tặng quà Giáng sinh"},
  {"id": "lex.en.200k.061172", "hw": "kunlun mountains", "pos": "phrase", "ipa": "/ˈkuːnluːn ˈmaʊntnz/", "vi": "dãy núi Côn Lôn hùng vĩ châu Á"},
  {"id": "lex.en.200k.061173", "hw": "lake balaton", "pos": "phrase", "ipa": "/leɪk ˈbɑːlətɑːn/", "vi": "hồ nước ngọt lớn Balaton Hungary"},
  {"id": "lex.en.200k.061174", "hw": "lauryl alcohol", "pos": "phrase", "ipa": "/ˈlɔːrəl ˈælkəhɔːl/", "vi": "cồn béo lauryl làm chất tẩy rửa"},
  {"id": "lex.en.200k.061175", "hw": "lech walesa", "pos": "phrase", "ipa": "/lɛk vəˈwɛnsə/", "vi": "cựu Tổng thống Ba Lan Lech Wałęsa"},
  {"id": "lex.en.200k.061176", "hw": "leopold stokowski", "pos": "phrase", "ipa": "/ˈliːəpoʊld stəˈkɑːfski/", "vi": "nhạc trưởng lừng danh Stokowski"},
  {"id": "lex.en.200k.061177", "hw": "lorenz oken", "pos": "phrase", "ipa": "/ˈlɔːrɛnts ˈoʊkən/", "vi": "nhà tự nhiên học Đức Lorenz Oken"},
  {"id": "lex.en.200k.061178", "hw": "malawi kwacha", "pos": "phrase", "ipa": "/məˈlɑːwi ˈkwɑːtʃə/", "vi": "đơn vị tiền tệ kwacha của Malawi"},
  {"id": "lex.en.200k.061179", "hw": "nadine gordimer", "pos": "phrase", "ipa": "/nəˈdiːn ˈɡɔːrdɪmər/", "vi": "nữ văn sĩ Nobel Nam Phi Gordimer"},
  {"id": "lex.en.200k.061180", "hw": "nonvolatile storage", "pos": "phrase", "ipa": "/ˌnɑːnˈvɑːlətl ˈstɔːrɪdʒ/", "vi": "bộ nhớ máy tính bất biến không mất"},
  {"id": "lex.en.200k.061181", "hw": "notational system", "pos": "phrase", "ipa": "/noʊˈteɪʃənəl ˈsɪstəm/", "vi": "hệ thống ký hiệu quy ước viết"},
  {"id": "lex.en.200k.061182", "hw": "occipital protuberance", "pos": "phrase", "ipa": "/ɑːkˈsɪpɪtl proʊˈtuːbərəns/", "vi": "ụ xương chẩm lồi phía sau gáy sọ"},
  {"id": "lex.en.200k.061183", "hw": "prunus avium", "pos": "phrase", "ipa": "/ˈpruːnəs ˈeɪviəm/", "vi": "cây anh đào dại ngọt châu Âu"},
  {"id": "lex.en.200k.061184", "hw": "regulus calendula", "pos": "phrase", "ipa": "/ˈrɛɡjʊləs kəˈlɛndjʊlə/", "vi": "chim tước mào đỏ châu Mỹ"},
  {"id": "lex.en.200k.061185", "hw": "sertoli cell", "pos": "phrase", "ipa": "/sərˈtoʊli sɛl/", "vi": "tế bào Sertoli nuôi tinh trùng"},
  {"id": "lex.en.200k.061186", "hw": "sheepshead porgy", "pos": "phrase", "ipa": "/ˈʃiːpshɛd ˈpɔːrɡi/", "vi": "cá tráp răng cừu vằn sọc đen trắng"},
  {"id": "lex.en.200k.061187", "hw": "slipper spurge", "pos": "phrase", "ipa": "/ˈslɪpər spɜːrdʒ/", "vi": "cây thuốc giấu tiểu hài thảo sáp"},
  {"id": "lex.en.200k.061188", "hw": "tall crowfoot", "pos": "phrase", "ipa": "/tɔːl ˈkroʊfʊt/", "vi": "cây mao lương cao đồng cỏ hoa vàng"},
  {"id": "lex.en.200k.061189", "hw": "tensor tympani", "pos": "phrase", "ipa": "/ˈtɛnsər ˈtɪmpənaɪ/", "vi": "cơ căng màng nhĩ giảm tiếng ồn"},
  {"id": "lex.en.200k.061190", "hw": "timur lenk", "pos": "phrase", "ipa": "/tɪˈmʊər lɛŋk/", "vi": "vua chinh phạt Thiếp Mộc Nhi Timur"},
  {"id": "lex.en.200k.061191", "hw": "tuatha de", "pos": "phrase", "ipa": "/ˈtuːəhə deɪ/", "vi": "thần tộc Tuatha Dé Danann Ireland"},
  {"id": "lex.en.200k.061192", "hw": "vigna radiata", "pos": "phrase", "ipa": "/ˈvɪɡnə ˌreɪdiˈeɪtə/", "vi": "cây đậu xanh hạt nhỏ làm giá đỗ"},
  {"id": "lex.en.200k.061193", "hw": "viola blanda", "pos": "phrase", "ipa": "/vaɪˈoʊlə ˈblændə/", "vi": "cây hoa tím trắng thơm dịu Bắc Mỹ"},
  {"id": "lex.en.200k.061194", "hw": "von rundstedt", "pos": "phrase", "ipa": "/fɔːn ˈrʊntʃtɛt/", "vi": "Thống chế Đức Gerd von Rundstedt"},
  {"id": "lex.en.200k.061195", "hw": "water crowfoot", "pos": "phrase", "ipa": "/ˈwɔːtər ˈkroʊfʊt/", "vi": "cây mao lương thủy sinh hoa trắng"},
  {"id": "lex.en.200k.061196", "hw": "wineglass heel", "pos": "phrase", "ipa": "/ˈwaɪnɡlæs hiːl/", "vi": "gót giày nữ uốn cong hình ly rượu"},
  {"id": "lex.en.200k.061197", "hw": "yack away", "pos": "phrase", "ipa": "/jæk əˈweɪ/", "vi": "nói huyên thuyên không dứt; tán gẫu"},
  {"id": "lex.en.200k.061198", "hw": "yves tanguy", "pos": "phrase", "ipa": "/iːv tɑ̃ːˈɡi/", "vi": "họa sĩ siêu thực Pháp Yves Tanguy"},
  {"id": "lex.en.200k.061199", "hw": "aminotransferases", "pos": "noun", "ipa": "/əˌmiːnoʊˈtrænsfəreɪsɪz/", "vi": "enzyme men chuyển hóa amin gan"},
  {"id": "lex.en.200k.061200", "hw": "aneurins", "pos": "noun", "ipa": "/əˈnjʊərɪnz/", "vi": "sinh tố vitamin B1 thiamin"},
  {"id": "lex.en.200k.061201", "hw": "antitoxins", "pos": "noun", "ipa": "/ˌæntiˈtɑːksɪnz/", "vi": "kháng thể kháng độc tố sinh học"},
  {"id": "lex.en.200k.061202", "hw": "apalachicolas", "pos": "noun", "ipa": "/ˌæpəlætʃɪˈkoʊləz/", "vi": "sông và vịnh Apalachicola Florida"}
]

with open('scratch/b33_r03_raw_p2.json') as f:
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

with open('scratch/b33_r03_p2.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

print("Batch 33 Round 3 Part 2 validated and written successfully.")
