import json

items = [
  {"id": "lex.en.200k.060103", "hw": "wallace hume carothers", "pos": "phrase", "ipa": "/ˈwɑːləs hjuːm kəˈrʌðərz/", "vi": "nhà hóa học Wallace Carothers Mỹ"},
  {"id": "lex.en.200k.060104", "hw": "whitetail jackrabbit", "pos": "phrase", "ipa": "/ˈwaɪtteɪl ˈdʒækræbɪt/", "vi": "thỏ rừng đuôi trắng Bắc Mỹ"},
  {"id": "lex.en.200k.060105", "hw": "wilhelm ostwald", "pos": "phrase", "ipa": "/ˈvɪlhɛlm ˈɔːstvalt/", "vi": "nhà hóa học Nobel Wilhelm Ostwald"},
  {"id": "lex.en.200k.060106", "hw": "william wycherley", "pos": "phrase", "ipa": "/ˈwɪljəm ˈwɪtʃərli/", "vi": "nhà viết kịch William Wycherley"},
  {"id": "lex.en.200k.060107", "hw": "winnow out", "pos": "phrase", "ipa": "/ˈwɪnoʊ aʊt/", "vi": "sàng lọc loại bỏ; chọn lọc kỹ"},
  {"id": "lex.en.200k.060108", "hw": "yucca glauca", "pos": "phrase", "ipa": "/ˈjʌkə ˈɡlɔːkə/", "vi": "cây ngọc giá thảo nguyên Bắc Mỹ"},
  {"id": "lex.en.200k.060109", "hw": "adenomas", "pos": "noun", "ipa": "/ˌædɪˈnoʊməz/", "vi": "u tuyến lành tính biểu mô"},
  {"id": "lex.en.200k.060110", "hw": "adenomata", "pos": "noun", "ipa": "/ˌædɪˈnoʊmətə/", "vi": "các u tuyến biểu mô lành tính"},
  {"id": "lex.en.200k.060111", "hw": "adverbials", "pos": "noun", "ipa": "/ædˈvɜːrbiəlz/", "vi": "trạng từ; trạng ngữ trong câu"},
  {"id": "lex.en.200k.060112", "hw": "ailerons", "pos": "noun", "ipa": "/ˈeɪlərɑːnz/", "vi": "cánh liệng thăng bằng máy bay"},
  {"id": "lex.en.200k.060113", "hw": "alpenas", "pos": "noun", "ipa": "/ælˈpiːnəz/", "vi": "thành phố cảng Alpena Michigan"},
  {"id": "lex.en.200k.060114", "hw": "amanitas", "pos": "noun", "ipa": "/ˌæməˈnaɪtəz/", "vi": "chi nấm tán amanita kịch độc"},
  {"id": "lex.en.200k.060115", "hw": "argosies", "pos": "noun", "ipa": "/ˈɑːrɡəsiz/", "vi": "đoàn tàu buôn lớn chở kho báu"},
  {"id": "lex.en.200k.060116", "hw": "arsenides", "pos": "noun", "ipa": "/ˈɑːrsənaɪdz/", "vi": "hợp chất muối arsenua kim loại"},
  {"id": "lex.en.200k.060117", "hw": "atheneums", "pos": "noun", "ipa": "/ˌæθəˈniːəmz/", "vi": "viện văn hóa; phòng đọc sách công"},
  {"id": "lex.en.200k.060118", "hw": "bioluminescences", "pos": "noun", "ipa": "/ˌbaɪoʊˌluːmɪˈnɛsənsɪz/", "vi": "hiện tượng phát quang sinh học"},
  {"id": "lex.en.200k.060119", "hw": "boatyards", "pos": "noun", "ipa": "/ˈboʊtjɑːrdz/", "vi": "xưởng đóng sửa chữa tàu thuyền"},
  {"id": "lex.en.200k.060120", "hw": "bookends", "pos": "noun", "ipa": "/ˈbʊkɛndz/", "vi": "đồ chặn giữ sách; cái chặn sách"},
  {"id": "lex.en.200k.060121", "hw": "bromes", "pos": "noun", "ipa": "/broʊmz/", "vi": "loài cỏ đuôi chồn brome chăn nuôi"},
  {"id": "lex.en.200k.060122", "hw": "burghers", "pos": "noun", "ipa": "/ˈbɜːrɡərz/", "vi": "tầng lớp thị dân giàu có thành thị"},
  {"id": "lex.en.200k.060123", "hw": "busybodies", "pos": "noun", "ipa": "/ˈbɪzibɑːdiz/", "vi": "kẻ thích xía mũi vào chuyện khác"},
  {"id": "lex.en.200k.060124", "hw": "campanas", "pos": "noun", "ipa": "/kæmˈpɑːnəz/", "vi": "chuông lớn; hoa văn hình chuông"},
  {"id": "lex.en.200k.060125", "hw": "carolinians", "pos": "noun", "ipa": "/ˌkærəˈlɪniənz/", "vi": "người dân bang Bắc Nam Carolina Mỹ"},
  {"id": "lex.en.200k.060126", "hw": "chateaubriands", "pos": "noun", "ipa": "/ʃæˌtoʊbriːˈɑ̃ːz/", "vi": "miếng bít tết bò phi-lê dày nướng"},
  {"id": "lex.en.200k.060127", "hw": "cosponsored", "pos": "verb", "ipa": "/koʊˈspɑːnsərd/", "vi": "đã cùng đồng tài trợ; đồng bảo trợ"},
  {"id": "lex.en.200k.060128", "hw": "cosponsoring", "pos": "verb", "ipa": "/koʊˈspɑːnsərɪŋ/", "vi": "đang đồng tài trợ; cùng đứng tên"},
  {"id": "lex.en.200k.060129", "hw": "cosponsors", "pos": "verb", "ipa": "/koʊˈspɑːnsərz/", "vi": "đồng tài trợ; đồng bảo trợ dự luật"},
  {"id": "lex.en.200k.060130", "hw": "deltoids", "pos": "noun", "ipa": "/ˈdɛltɔɪdz/", "vi": "cơ delta; cơ bắp hình tam giác vai"},
  {"id": "lex.en.200k.060131", "hw": "depositors", "pos": "noun", "ipa": "/dɪˈpɑːzɪtərz/", "vi": "người gửi tiền tiết kiệm ngân hàng"},
  {"id": "lex.en.200k.060132", "hw": "draftier", "pos": "adj", "ipa": "/ˈdræftiər/", "vi": "nhiều gió lùa lạnh hơn"},
  {"id": "lex.en.200k.060133", "hw": "draftiest", "pos": "adj", "ipa": "/ˈdræftiɪst/", "vi": "nhiều luồng gió lùa lạnh nhất"},
  {"id": "lex.en.200k.060134", "hw": "entrenchments", "pos": "noun", "ipa": "/ɪnˈtrɛntʃmənts/", "vi": "chiến hào phòng thủ kiên cố"},
  {"id": "lex.en.200k.060135", "hw": "filmier", "pos": "adj", "ipa": "/ˈfɪlmiər/", "vi": "mỏng tang hơn; trong suốt hơn"},
  {"id": "lex.en.200k.060136", "hw": "filmiest", "pos": "adj", "ipa": "/ˈfɪlmiɪst/", "vi": "mỏng tang nhất; mờ ảo nhất"},
  {"id": "lex.en.200k.060137", "hw": "frenchwomans", "pos": "noun", "ipa": "/ˈfrɛntʃˌwɪmɪn/", "vi": "phụ nữ nước Pháp; quý cô Pháp"},
  {"id": "lex.en.200k.060138", "hw": "ftos", "pos": "noun", "ipa": "/ɛf tiː oʊz/", "vi": "tổ chức khủng bố nước ngoài FTO"},
  {"id": "lex.en.200k.060139", "hw": "ghqs", "pos": "noun", "ipa": "/dʒiː eɪtʃ kjuːz/", "vi": "tổng hành dinh chỉ huy tối cao"},
  {"id": "lex.en.200k.060140", "hw": "highballs", "pos": "noun", "ipa": "/ˈhaɪbɔːlz/", "vi": "ly rượu cocktail pha soda đá"},
  {"id": "lex.en.200k.060141", "hw": "historicisms", "pos": "noun", "ipa": "/hɪˈstɔːrɪsɪzəmz/", "vi": "thuyết lịch sử luận triết học"},
  {"id": "lex.en.200k.060142", "hw": "ingenues", "pos": "noun", "ipa": "/ˌæ̃ʒeɪˈnjuːz/", "vi": "vai thiếu nữ ngây thơ; cô gái trẻ"},
  {"id": "lex.en.200k.060143", "hw": "jacksonians", "pos": "noun", "ipa": "/dʒækˈsoʊniənz/", "vi": "người ủng hộ tổng thống Jackson"},
  {"id": "lex.en.200k.060144", "hw": "judaeas", "pos": "noun", "ipa": "/dʒuːˈdiːəz/", "vi": "vùng đất xứ Judea lịch sử Do Thái"},
  {"id": "lex.en.200k.060145", "hw": "kerenskies", "pos": "noun", "ipa": "/kəˈrɛnskiz/", "vi": "chính khách Alexander Kerensky Nga"},
  {"id": "lex.en.200k.060146", "hw": "knitters", "pos": "noun", "ipa": "/ˈnɪtərz/", "vi": "thợ đan len; máy dệt kim sợi len"},
  {"id": "lex.en.200k.060147", "hw": "kudus", "pos": "noun", "ipa": "/ˈkuːduːz/", "vi": "loài linh dương sừng xoắn Kudu Phi"},
  {"id": "lex.en.200k.060148", "hw": "laterites", "pos": "noun", "ipa": "/ˈlætəraɪts/", "vi": "đá ong đỏ giàu sắt nhôm"},
  {"id": "lex.en.200k.060149", "hw": "lilongwes", "pos": "noun", "ipa": "/lɪˈlɔːŋweɪz/", "vi": "thủ đô Lilongwe nước Malawi"},
  {"id": "lex.en.200k.060150", "hw": "limeys", "pos": "noun", "ipa": "/ˈlaɪmiz/", "vi": "từ lóng thủy thủ người Anh"},
  {"id": "lex.en.200k.060151", "hw": "lipitors", "pos": "noun", "ipa": "/ˈlɪpɪtɔːrz/", "vi": "thuốc hạ mỡ máu statin Lipitor"},
  {"id": "lex.en.200k.060152", "hw": "logicians", "pos": "noun", "ipa": "/loʊˈdʒɪʃənz/", "vi": "nhà nghiên cứu logic; nhà luận lý"},
  {"id": "lex.en.200k.060153", "hw": "louts", "pos": "noun", "ipa": "/laʊts/", "vi": "kẻ thô bỉ vụng về; kẻ cục cằn"},
  {"id": "lex.en.200k.060154", "hw": "lymphedemas", "pos": "noun", "ipa": "/ˌlɪmfəˈdiːməz/", "vi": "chứng phù mạch bạch huyết sưng to"},
  {"id": "lex.en.200k.060155", "hw": "maoisms", "pos": "noun", "ipa": "/ˈmaʊɪzəmz/", "vi": "tư tưởng chủ nghĩa Mao Trạch Đông"},
  {"id": "lex.en.200k.060156", "hw": "marcuses", "pos": "noun", "ipa": "/mɑːrˈkuːsəz/", "vi": "triết gia Herbert Marcuse"},
  {"id": "lex.en.200k.060157", "hw": "maupassants", "pos": "noun", "ipa": "/moʊpəˈsɑ̃ːz/", "vi": "đại văn hào Pháp Guy de Maupassant"},
  {"id": "lex.en.200k.060158", "hw": "mazatlans", "pos": "noun", "ipa": "/ˌmɑːzɑːtˈlɑːnz/", "vi": "thành phố biển nghỉ mát Mazatlán"},
  {"id": "lex.en.200k.060159", "hw": "megalopolises", "pos": "noun", "ipa": "/ˌmɛɡəˈlɑːpəlɪsɪz/", "vi": "siêu đô thị khổng lồ liên kết"},
  {"id": "lex.en.200k.060160", "hw": "metronidazoles", "pos": "noun", "ipa": "/ˌmɛtrəˈnaɪdəzoʊlz/", "vi": "thuốc kháng sinh metronidazole"},
  {"id": "lex.en.200k.060161", "hw": "micronutrients", "pos": "noun", "ipa": "/ˌmaɪkroʊˈnuːtriənts/", "vi": "chất dinh dưỡng vi lượng thiết yếu"},
  {"id": "lex.en.200k.060162", "hw": "molnars", "pos": "noun", "ipa": "/ˈmoʊlnɑːrz/", "vi": "nhà văn kịch nghệ Ferenc Molnár"},
  {"id": "lex.en.200k.060163", "hw": "myasthenias", "pos": "noun", "ipa": "/ˌmaɪəsˈθiːniəz/", "vi": "bệnh lý nhược cơ mỏi cơ mạn tính"},
  {"id": "lex.en.200k.060164", "hw": "nahuatls", "pos": "noun", "ipa": "/ˈnɑːwɑːtəlz/", "vi": "người Nahuatl bản địa Mexico"},
  {"id": "lex.en.200k.060165", "hw": "naltrexones", "pos": "noun", "ipa": "/nælˈtrɛksoʊnz/", "vi": "thuốc naltrexone cai nghiện ma túy"},
  {"id": "lex.en.200k.060166", "hw": "nitpicked", "pos": "verb", "ipa": "/ˈnɪtpɪkt/", "vi": "đã bới lông tìm vết; săm soi"},
  {"id": "lex.en.200k.060167", "hw": "nitpicks", "pos": "verb", "ipa": "/ˈnɪtpɪks/", "vi": "bới lông tìm vết; vạch lá tìm sâu"},
  {"id": "lex.en.200k.060168", "hw": "nonpayments", "pos": "noun", "ipa": "/nɑːnˈpeɪmənts/", "vi": "sự không thanh toán; quỵt nợ"},
  {"id": "lex.en.200k.060169", "hw": "northwestwards", "pos": "noun", "ipa": "/ˌnɔːrθˈwɛstwərdz/", "vi": "hướng tây bắc; vùng tây bắc"},
  {"id": "lex.en.200k.060170", "hw": "novitiates", "pos": "noun", "ipa": "/noʊˈvɪʃiɪts/", "vi": "giai đoạn tập tu dòng; nhà tập sự"},
  {"id": "lex.en.200k.060171", "hw": "occidents", "pos": "noun", "ipa": "/ˈɑːksɪdənts/", "vi": "các nước phương Tây; thế giới Tây"},
  {"id": "lex.en.200k.060172", "hw": "organelles", "pos": "noun", "ipa": "/ˌɔːrɡəˈnɛlz/", "vi": "các bào quan bên trong tế bào"},
  {"id": "lex.en.200k.060173", "hw": "osteomyelitides", "pos": "noun", "ipa": "/ˌɑːstioʊˌmaɪəˈlaɪtɪdiːz/", "vi": "chứng bệnh viêm tủy xương tủy mủ"},
  {"id": "lex.en.200k.060174", "hw": "outselling", "pos": "verb", "ipa": "/aʊtˈsɛlɪŋ/", "vi": "đang bán chạy hơn doanh số"},
  {"id": "lex.en.200k.060175", "hw": "outsells", "pos": "verb", "ipa": "/aʊtˈsɛlz/", "vi": "bán chạy hơn; vượt trội doanh số"},
  {"id": "lex.en.200k.060176", "hw": "overstayed", "pos": "verb", "ipa": "/ˌoʊvərˈsteɪd/", "vi": "đã ở lại quá hạn; lưu trú quá lâu"},
  {"id": "lex.en.200k.060177", "hw": "overstaying", "pos": "verb", "ipa": "/ˌoʊvərˈsteɪɪŋ/", "vi": "đang ở quá hạn visa; lưu trú lâu"},
  {"id": "lex.en.200k.060178", "hw": "overstays", "pos": "verb", "ipa": "/ˌoʊvərˈsteɪz/", "vi": "ở quá hạn lưu trú; nán lại quá lâu"},
  {"id": "lex.en.200k.060179", "hw": "oviducts", "pos": "noun", "ipa": "/ˈoʊvɪdʌkts/", "vi": "ống dẫn trứng; vòi dẫn trứng"},
  {"id": "lex.en.200k.060180", "hw": "oxtails", "pos": "noun", "ipa": "/ˈɑːksteɪlz/", "vi": "đuôi bò nấu súp lẩu hầm mềm"},
  {"id": "lex.en.200k.060181", "hw": "pacas", "pos": "noun", "ipa": "/ˈpɑːkəz/", "vi": "loài chuột paca lông đốm Nam Mỹ"},
  {"id": "lex.en.200k.060182", "hw": "padovas", "pos": "noun", "ipa": "/ˈpædʊəz/", "vi": "thành phố cổ Padova nước Ý"},
  {"id": "lex.en.200k.060183", "hw": "paiutes", "pos": "noun", "ipa": "/ˈpaɪjuːts/", "vi": "người da đỏ Paiute bản địa Mỹ"},
  {"id": "lex.en.200k.060184", "hw": "palanquins", "pos": "noun", "ipa": "/ˌpælənˈkiːnz/", "vi": "kiệu khiêng người; chiếc kiệu cổ"},
  {"id": "lex.en.200k.060185", "hw": "paternosters", "pos": "noun", "ipa": "/ˌpeɪtərˈnɑːstərz/", "vi": "kinh Lạy Cha; chuỗi hạt kinh"},
  {"id": "lex.en.200k.060186", "hw": "peaveys", "pos": "noun", "ipa": "/ˈpiːviz/", "vi": "cây đòn bẩy móc lăn xúc gỗ"},
  {"id": "lex.en.200k.060187", "hw": "pedants", "pos": "noun", "ipa": "/ˈpɛdənts/", "vi": "kẻ câu nệ chữ nghĩa; kẻ mọt sách"},
  {"id": "lex.en.200k.060188", "hw": "pharoses", "pos": "noun", "ipa": "/ˈfɛroʊsɪz/", "vi": "ngọn hải đăng dẫn đường ven biển"},
  {"id": "lex.en.200k.060189", "hw": "prednisolones", "pos": "noun", "ipa": "/ˌprɛdˈnɪsəloʊnz/", "vi": "thuốc steroid kháng viêm dị ứng"},
  {"id": "lex.en.200k.060190", "hw": "preschoolers", "pos": "noun", "ipa": "/ˈpriːskuːlərz/", "vi": "trẻ em lứa tuổi mẫu giáo mầm non"},
  {"id": "lex.en.200k.060191", "hw": "progestins", "pos": "noun", "ipa": "/proʊˈdʒɛstɪnz/", "vi": "hoóc-môn progestin tổng hợp"},
  {"id": "lex.en.200k.060192", "hw": "puseys", "pos": "noun", "ipa": "/ˈpjuːziz/", "vi": "nhà thần học Edward Pusey ở Anh"},
  {"id": "lex.en.200k.060193", "hw": "raconteurs", "pos": "noun", "ipa": "/ˌrækɑːnˈtɜːrz/", "vi": "người có tài kể chuyện lôi cuốn"},
  {"id": "lex.en.200k.060194", "hw": "recoded", "pos": "verb", "ipa": "/riːˈkoʊdɪd/", "vi": "đã tái lập trình; đã lập mã lại"},
  {"id": "lex.en.200k.060195", "hw": "recodes", "pos": "verb", "ipa": "/riːˈkoʊdz/", "vi": "mã hóa lại; tái lập trình dữ liệu"},
  {"id": "lex.en.200k.060196", "hw": "republished", "pos": "verb", "ipa": "/riːˈpʌblɪʃt/", "vi": "đã tái bản sách; đã xuất bản lại"},
  {"id": "lex.en.200k.060197", "hw": "republishes", "pos": "verb", "ipa": "/riːˈpʌblɪʃɪz/", "vi": "tái bản ấn phẩm; xuất bản lại sách"},
  {"id": "lex.en.200k.060198", "hw": "rhenishes", "pos": "noun", "ipa": "/ˈrɛnɪʃɪz/", "vi": "rượu vang trắng vùng sông Rhine Đức"},
  {"id": "lex.en.200k.060199", "hw": "sakharovs", "pos": "noun", "ipa": "/ˈsɑːkərɔːvz/", "vi": "nhà vật lý Nobel Hòa bình Sakharov"},
  {"id": "lex.en.200k.060200", "hw": "samosas", "pos": "noun", "ipa": "/səˈmoʊsəz/", "vi": "bánh gối chiên giòn samosa Ấn Độ"},
  {"id": "lex.en.200k.060201", "hw": "simulacrums", "pos": "noun", "ipa": "/ˌsɪmjʊˈleɪkrəmz/", "vi": "hình ảnh mô phỏng; bản sao ảo ảnh"},
  {"id": "lex.en.200k.060202", "hw": "smilers", "pos": "noun", "ipa": "/ˈsmaɪlərz/", "vi": "người luôn nở nụ cười tươi tắn"}
]

with open('scratch/b33_r01_raw_p2.json') as f:
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

with open('scratch/b33_r01_p2.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

print("Batch 33 Round 1 Part 2 validated and written successfully.")
