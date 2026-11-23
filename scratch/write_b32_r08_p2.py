import json

items = [
  {"id": "lex.en.200k.058602", "hw": "ad valorem tax", "pos": "phrase", "ipa": "/æd vəˈlɔːrəm tæks/", "vi": "thuế theo giá trị hàng hóa"},
  {"id": "lex.en.200k.058603", "hw": "adenosine monophosphate", "pos": "phrase", "ipa": "/əˈdɛnəsiːn ˌmɑːnoʊˈfɑːsfeɪt/", "vi": "chất adenosine monophosphate"},
  {"id": "lex.en.200k.058604", "hw": "african bowstring hemp", "pos": "phrase", "ipa": "/ˈæfrɪkən ˈboʊstrɪŋ hɛmp/", "vi": "cây lưỡi hổ gai châu Phi"},
  {"id": "lex.en.200k.058605", "hw": "angara river", "pos": "phrase", "ipa": "/æŋˈɡɑːrə ˈrɪvər/", "vi": "sông Angara ở Nga"},
  {"id": "lex.en.200k.058606", "hw": "antiepileptic drug", "pos": "phrase", "ipa": "/ˌæntiːˌɛpəˈlɛptɪk drʌɡ/", "vi": "thuốc chống động kinh"},
  {"id": "lex.en.200k.058607", "hw": "austenitic steel", "pos": "phrase", "ipa": "/ɔːstəˈnɪtɪk stiːl/", "vi": "thép không gỉ austenit"},
  {"id": "lex.en.200k.058608", "hw": "bahasa melayu", "pos": "phrase", "ipa": "/bəˈhɑːsə məˈlaɪuː/", "vi": "tiếng Mã Lai"},
  {"id": "lex.en.200k.058609", "hw": "ballyhoo artist", "pos": "phrase", "ipa": "/ˈbælihuː ˈɑːrtɪst/", "vi": "kẻ quảng cáo thổi phồng"},
  {"id": "lex.en.200k.058610", "hw": "battle of omdurman", "pos": "phrase", "ipa": "/ˈbætl əv ˌɑːmdʊərˈmɑːn/", "vi": "trận đánh Omdurman"},
  {"id": "lex.en.200k.058611", "hw": "bowstring hemp", "pos": "phrase", "ipa": "/ˈboʊstrɪŋ hɛmp/", "vi": "cây lưỡi hổ; sợi cây lưỡi hổ"},
  {"id": "lex.en.200k.058612", "hw": "calamine lotion", "pos": "phrase", "ipa": "/ˈkæləmaɪn ˈloʊʃən/", "vi": "dung dịch dưỡng dịu da calamine"},
  {"id": "lex.en.200k.058613", "hw": "cardiac tamponade", "pos": "phrase", "ipa": "/ˈkɑːrdiæk ˌtæmpənˈeɪd/", "vi": "chèn ép màng ngoài tim cấp"},
  {"id": "lex.en.200k.058614", "hw": "crabapple jelly", "pos": "phrase", "ipa": "/ˈkræbæpl ˈdʒɛli/", "vi": "thạch làm từ táo dại"},
  {"id": "lex.en.200k.058615", "hw": "decoction mashing", "pos": "phrase", "ipa": "/dɪˈkɑːkʃən ˈmæʃɪŋ/", "vi": "phương pháp nấu đường hóa bia"},
  {"id": "lex.en.200k.058616", "hw": "diaphragmatic hernia", "pos": "phrase", "ipa": "/ˌdaɪəfræɡˈmætɪk ˈhɜːrniə/", "vi": "thoát vị cơ hoành"},
  {"id": "lex.en.200k.058617", "hw": "direct antonym", "pos": "phrase", "ipa": "/dəˈrɛkt ˈæntənɪm/", "vi": "từ trái nghĩa trực tiếp"},
  {"id": "lex.en.200k.058618", "hw": "dmitri mendeleev", "pos": "phrase", "ipa": "/dˈmiːtri ˌmɛndəlˈeɪəf/", "vi": "nhà hóa học Dmitri Mendeleev"},
  {"id": "lex.en.200k.058619", "hw": "endotracheal tube", "pos": "phrase", "ipa": "/ˌɛndoʊˈtreɪkiəl tuːb/", "vi": "ống đặt nội khí quản"},
  {"id": "lex.en.200k.058620", "hw": "epiphytic plant", "pos": "phrase", "ipa": "/ˌɛpəˈfɪtɪk plænt/", "vi": "loài thực vật biểu sinh"},
  {"id": "lex.en.200k.058621", "hw": "ethylene tetrachloride", "pos": "phrase", "ipa": "/ˈɛθəliːn ˌtɛtrəˈklɔːraɪd/", "vi": "chất tetrachloroethylene"},
  {"id": "lex.en.200k.058622", "hw": "genus casuarina", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˌkæzjʊəˈraɪnə/", "vi": "chi thực vật phi lao"},
  {"id": "lex.en.200k.058623", "hw": "genus ribes", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈraɪbiːz/", "vi": "chi thực vật lý chua"},
  {"id": "lex.en.200k.058624", "hw": "grand marnier", "pos": "phrase", "ipa": "/ɡrɑːnd mɑːrnˈjeɪ/", "vi": "rượu mùi cam Grand Marnier"},
  {"id": "lex.en.200k.058625", "hw": "harlow shapley", "pos": "phrase", "ipa": "/ˈhɑːrloʊ ˈʃæpli/", "vi": "nhà thiên văn Harlow Shapley"},
  {"id": "lex.en.200k.058626", "hw": "hunger marcher", "pos": "phrase", "ipa": "/ˈhʌŋɡər ˈmɑːrtʃər/", "vi": "người tuần hành chống nghèo đói"},
  {"id": "lex.en.200k.058627", "hw": "hydroplane racing", "pos": "phrase", "ipa": "/ˈhaɪdroʊpleɪn ˈreɪsɪŋ/", "vi": "môn đua ca nô lướt sóng nước"},
  {"id": "lex.en.200k.058628", "hw": "indirect antonym", "pos": "phrase", "ipa": "/ˌɪndəˈrɛkt ˈæntənɪm/", "vi": "từ trái nghĩa gián tiếp"},
  {"id": "lex.en.200k.058629", "hw": "iris versicolor", "pos": "phrase", "ipa": "/ˈaɪrɪs ˌvɜːrsɪˈkʌlər/", "vi": "hoa diên vĩ nhiều màu"},
  {"id": "lex.en.200k.058630", "hw": "john wickliffe", "pos": "phrase", "ipa": "/dʒɑːn ˈwɪklɪf/", "vi": "nhà cải cách John Wycliffe"},
  {"id": "lex.en.200k.058631", "hw": "josiah spode", "pos": "phrase", "ipa": "/dʒoʊˈzaɪə spoʊd/", "vi": "nhà sản xuất gốm Josiah Spode"},
  {"id": "lex.en.200k.058632", "hw": "la spezia", "pos": "phrase", "ipa": "/lɑː ˈspɛtsjɑː/", "vi": "thành phố cảng La Spezia"},
  {"id": "lex.en.200k.058633", "hw": "luteal phase", "pos": "phrase", "ipa": "/ˈluːtiəl feɪz/", "vi": "pha hoàng thể trong chu kỳ"},
  {"id": "lex.en.200k.058634", "hw": "lynx caracal", "pos": "phrase", "ipa": "/lɪŋks ˈkærəkæl/", "vi": "linh miêu tai đen caracal"},
  {"id": "lex.en.200k.058635", "hw": "lysergic acid", "pos": "phrase", "ipa": "/laɪˈsɜːrdʒɪk ˈæsɪd/", "vi": "hợp chất axit lysergic"},
  {"id": "lex.en.200k.058636", "hw": "max bruch", "pos": "phrase", "ipa": "/mæks brʊx/", "vi": "nhà soạn nhạc Max Bruch"},
  {"id": "lex.en.200k.058637", "hw": "norman mattoon thomas", "pos": "phrase", "ipa": "/ˈnɔːrmən məˈtuːn ˈtɑːməs/", "vi": "chính khách Norman Thomas"},
  {"id": "lex.en.200k.058638", "hw": "old ironsides", "pos": "phrase", "ipa": "/oʊld ˈaɪərnsaɪdz/", "vi": "chiến hạm Old Ironsides"},
  {"id": "lex.en.200k.058639", "hw": "organophosphate nerve agent", "pos": "phrase", "ipa": "/ɔːrˌɡænoʊˈfɑːsfeɪt nɜːrv ˈeɪdʒənt/", "vi": "chất độc thần kinh lân hữu cơ"},
  {"id": "lex.en.200k.058640", "hw": "orthostatic hypotension", "pos": "phrase", "ipa": "/ˌɔːrθəˈstætɪk ˌhaɪpoʊˈtɛnʃən/", "vi": "tụt huyết áp tư thế đứng"},
  {"id": "lex.en.200k.058641", "hw": "pierre larousse", "pos": "phrase", "ipa": "/pjɛər ləˈruːs/", "vi": "nhà từ điển Pierre Larousse"},
  {"id": "lex.en.200k.058642", "hw": "pipa pipa", "pos": "phrase", "ipa": "/ˈpiːpə ˈpiːpə/", "vi": "loài cóc tổ ong pipa pipa"},
  {"id": "lex.en.200k.058643", "hw": "pitot head", "pos": "phrase", "ipa": "/ˈpiːtoʊ hɛd/", "vi": "đầu ống đo áp suất pitot"},
  {"id": "lex.en.200k.058644", "hw": "pitot tube", "pos": "phrase", "ipa": "/ˈpiːtoʊ tuːb/", "vi": "ống đo vận tốc dòng khí pitot"},
  {"id": "lex.en.200k.058645", "hw": "quonset hut", "pos": "phrase", "ipa": "/ˈkwɑːnsɪt hʌt/", "vi": "nhà vòm tiền chế Quonset"},
  {"id": "lex.en.200k.058646", "hw": "regular dodecahedron", "pos": "phrase", "ipa": "/ˈrɛɡjələr ˌdoʊdɛkəˈhiːdrən/", "vi": "khối mười hai mặt đều"},
  {"id": "lex.en.200k.058647", "hw": "rembrandt van rijn", "pos": "phrase", "ipa": "/ˈrɛmbrænt væn raɪn/", "vi": "danh họa Rembrandt van Rijn"},
  {"id": "lex.en.200k.058648", "hw": "salix discolor", "pos": "phrase", "ipa": "/ˈseɪlɪks ˈdɪskʌlər/", "vi": "cây liễu nụ pussy willow"},
  {"id": "lex.en.200k.058649", "hw": "tartar emetic", "pos": "phrase", "ipa": "/ˈtɑːrtər ɪˈmɛtɪk/", "vi": "muối gây nôn tartar emetic"},
  {"id": "lex.en.200k.058650", "hw": "thales of miletus", "pos": "phrase", "ipa": "/ˈθeɪliːz əv maɪˈliːtəs/", "vi": "triết gia Thales xứ Miletus"},
  {"id": "lex.en.200k.058651", "hw": "titus livius", "pos": "phrase", "ipa": "/ˈtaɪtəs ˈlɪviəs/", "vi": "sử gia La Mã Titus Livius"},
  {"id": "lex.en.200k.058652", "hw": "trammel net", "pos": "phrase", "ipa": "/ˈtræməl nɛt/", "vi": "lưới bén ba màng; lưới rập"},
  {"id": "lex.en.200k.058653", "hw": "verrazano narrows", "pos": "phrase", "ipa": "/ˌvɛrəˈzɑːnoʊ ˈnæroʊz/", "vi": "eo biển Verrazano Narrows"},
  {"id": "lex.en.200k.058654", "hw": "affaires", "pos": "noun", "ipa": "/əfˈɛrz/", "vi": "chuyện tình vụng trộm; biến cố"},
  {"id": "lex.en.200k.058655", "hw": "aldosterones", "pos": "noun", "ipa": "/ældˈɑːstəroʊnz/", "vi": "hoóc-môn aldosterone"},
  {"id": "lex.en.200k.058656", "hw": "amperes", "pos": "noun", "ipa": "/ˈæmpˌɜːrz/", "vi": "đơn vị cường độ dòng điện ampe"},
  {"id": "lex.en.200k.058657", "hw": "aphises", "pos": "noun", "ipa": "/ˈeɪfɪsɪz/", "vi": "rệp vừng; rệp hại cây trồng"},
  {"id": "lex.en.200k.058658", "hw": "apias", "pos": "noun", "ipa": "/ˈɑːpiəz/", "vi": "thành phố cảng Apia"},
  {"id": "lex.en.200k.058659", "hw": "apoplexies", "pos": "noun", "ipa": "/ˈæpəplˌɛksiz/", "vi": "chứng đột quỵ não; cơn thịnh nộ"},
  {"id": "lex.en.200k.058660", "hw": "ariuses", "pos": "noun", "ipa": "/ərˈaɪəsɪz/", "vi": "nhà thần học Arius"},
  {"id": "lex.en.200k.058661", "hw": "bannocks", "pos": "noun", "ipa": "/bˈænəks/", "vi": "bánh mì nướng dẹt Scotland"},
  {"id": "lex.en.200k.058662", "hw": "beatifications", "pos": "noun", "ipa": "/biːˌætɪfɪkˈeɪʃənz/", "vi": "lễ phong chân phước"},
  {"id": "lex.en.200k.058663", "hw": "bellises", "pos": "noun", "ipa": "/bˈɛlɪsɪz/", "vi": "chi hoa cúc dại bellis"},
  {"id": "lex.en.200k.058664", "hw": "berkshireses", "pos": "noun", "ipa": "/bˈɜːrkʃɪrzɪz/", "vi": "vùng đồi Berkshires"},
  {"id": "lex.en.200k.058665", "hw": "brules", "pos": "noun", "ipa": "/bruːlˈeɪz/", "vi": "người bản địa Mỹ bộ tộc Brulé"},
  {"id": "lex.en.200k.058666", "hw": "bulimics", "pos": "noun", "ipa": "/bjuːlˈɪmɪks/", "vi": "người mắc chứng cuồng ăn ói"},
  {"id": "lex.en.200k.058667", "hw": "caimans", "pos": "noun", "ipa": "/kˈeɪmənz/", "vi": "loài cá sấu caiman Nam Mỹ"},
  {"id": "lex.en.200k.058668", "hw": "catalases", "pos": "noun", "ipa": "/kˈætəleɪsɪz/", "vi": "men enzym catalase"},
  {"id": "lex.en.200k.058669", "hw": "chambermaids", "pos": "noun", "ipa": "/tʃˈeɪmbɚmˌeɪdz/", "vi": "nữ phục vụ phòng khách sạn"},
  {"id": "lex.en.200k.058670", "hw": "clopped", "pos": "verb", "ipa": "/klˈɑːpt/", "vi": "bước lộc cộc; gõ móng lộp cộp"},
  {"id": "lex.en.200k.058671", "hw": "clops", "pos": "noun", "ipa": "/klˈɑːps/", "vi": "tiếng vó ngựa cộp cộp"},
  {"id": "lex.en.200k.058672", "hw": "complainers", "pos": "noun", "ipa": "/kˈɑmplˌeɪnɚz/", "vi": "người hay than phiền càu nhàu"},
  {"id": "lex.en.200k.058673", "hw": "counterclaimed", "pos": "verb", "ipa": "/kˈaʊntɚkleɪmd/", "vi": "đưa ra yêu cầu phản tố"},
  {"id": "lex.en.200k.058674", "hw": "counterclaiming", "pos": "verb", "ipa": "/kˈaʊntɚkleɪmɪŋ/", "vi": "đang phản tố trong vụ kiện"},
  {"id": "lex.en.200k.058675", "hw": "counterclaims", "pos": "noun", "ipa": "/kˈaʊntɚklˌeɪmz/", "vi": "yêu cầu phản tố; đơn phản kiện"},
  {"id": "lex.en.200k.058676", "hw": "curmudgeons", "pos": "noun", "ipa": "/kɚmˈʌdʒɪnz/", "vi": "lão già gắt gỏng bẳn tính"},
  {"id": "lex.en.200k.058677", "hw": "dnipropetrovsks", "pos": "noun", "ipa": "/dnˌɪproʊpətrˈɑːvskz/", "vi": "thành phố Dnipro ở Ukraina"},
  {"id": "lex.en.200k.058678", "hw": "durbars", "pos": "noun", "ipa": "/dˈɜːrbɑːrz/", "vi": "buổi thiết triều Ấn Độ xưa"},
  {"id": "lex.en.200k.058679", "hw": "ecclesiastics", "pos": "noun", "ipa": "/ɪklˌiːziˈæstɪks/", "vi": "hàng chức sắc giáo sĩ tăng lữ"},
  {"id": "lex.en.200k.058680", "hw": "eddas", "pos": "noun", "ipa": "/ˈɛdəz/", "vi": "bộ trường ca thần thoại Bắc Âu"},
  {"id": "lex.en.200k.058681", "hw": "eibs", "pos": "noun", "ipa": "/ˌiːaɪbˈiːz/", "vi": "ngân hàng đầu tư châu Âu EIB"},
  {"id": "lex.en.200k.058682", "hw": "enchanters", "pos": "noun", "ipa": "/ɛntʃˈæntɚz/", "vi": "phù thủy yểm bùa; kẻ mê hoặc"},
  {"id": "lex.en.200k.058683", "hw": "endoscopes", "pos": "noun", "ipa": "/ˈɛndəskoʊps/", "vi": "ống soi quang học nội soi"},
  {"id": "lex.en.200k.058684", "hw": "epicuruses", "pos": "noun", "ipa": "/ˌɛpɪkjˈʊrəsɪz/", "vi": "triết gia Epicurus"},
  {"id": "lex.en.200k.058685", "hw": "footlockers", "pos": "noun", "ipa": "/fˈʊtlɑːkɚz/", "vi": "hòm đựng quân trang chân giường"},
  {"id": "lex.en.200k.058686", "hw": "freestones", "pos": "noun", "ipa": "/frˈiːstoʊnz/", "vi": "giống đào tách hạt; đá dễ chạm"},
  {"id": "lex.en.200k.058687", "hw": "gannets", "pos": "noun", "ipa": "/ɡˈænɪts/", "vi": "loài chim điên biển; kẻ phàm ăn"},
  {"id": "lex.en.200k.058688", "hw": "garnishments", "pos": "noun", "ipa": "/ɡˈɑːrnɪʃmənts/", "vi": "lệnh trích thu nhập; trang trí"},
  {"id": "lex.en.200k.058689", "hw": "gides", "pos": "noun", "ipa": "/ʒˈiːdz/", "vi": "nhà văn André Gide"},
  {"id": "lex.en.200k.058690", "hw": "golgothas", "pos": "noun", "ipa": "/ɡˈɑːlɡəθəz/", "vi": "đồi Sọ Golgotha; nơi khổ nạn"},
  {"id": "lex.en.200k.058691", "hw": "gravitons", "pos": "noun", "ipa": "/ɡrˈævɪtɑːnz/", "vi": "hạt giả định hấp dẫn graviton"},
  {"id": "lex.en.200k.058692", "hw": "grebes", "pos": "noun", "ipa": "/ɡrˈiːbz/", "vi": "chim lặn nước grebe"},
  {"id": "lex.en.200k.058693", "hw": "griegs", "pos": "noun", "ipa": "/ɡrˈiːɡz/", "vi": "nhạc sĩ Edvard Grieg"},
  {"id": "lex.en.200k.058694", "hw": "hanoverians", "pos": "noun", "ipa": "/hˌænoʊvˈɪriənz/", "vi": "người thuộc dòng họ Hanover"},
  {"id": "lex.en.200k.058695", "hw": "heliports", "pos": "noun", "ipa": "/hˈɛləpɔːrts/", "vi": "sân bay cất cánh trực thăng"},
  {"id": "lex.en.200k.058696", "hw": "hephaestuses", "pos": "noun", "ipa": "/hɪfˈiːstəsɪz/", "vi": "thần thợ rèn Hephaestus"},
  {"id": "lex.en.200k.058697", "hw": "huffier", "pos": "adj", "ipa": "/hˈʌfiɚ/", "vi": "dễ hờn dỗi hơn; bực bội hơn"},
  {"id": "lex.en.200k.058698", "hw": "huffiest", "pos": "adj", "ipa": "/hˈʌfiɪst/", "vi": "dễ hờn dỗi nhất; cáu kỉnh nhất"},
  {"id": "lex.en.200k.058699", "hw": "interregnums", "pos": "noun", "ipa": "/ˌɪntərˈɛɡnəmz/", "vi": "thời kỳ gián đoạn triều đại"},
  {"id": "lex.en.200k.058700", "hw": "intimations", "pos": "noun", "ipa": "/ˌɪntəmˈeɪʃənz/", "vi": "lời ám chỉ kín đáo; thông báo"},
  {"id": "lex.en.200k.058701", "hw": "iwws", "pos": "noun", "ipa": "/ˌaɪdʌbəljˌuːdˈʌbəljuːz/", "vi": "công đoàn lao động thế giới IWW"}
]

with open('scratch/b32_r08_raw_p2.json') as f:
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

with open('scratch/b32_r08_p2.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

print("Part 2 validated and written successfully.")
