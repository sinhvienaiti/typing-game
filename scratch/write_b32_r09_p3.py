import json

items = [
  {"id": "lex.en.200k.059203", "hw": "raymond lully", "pos": "phrase", "ipa": "/ˈreɪmənd ˈlʌli/", "vi": "học giả thần bí Raymond Lully"},
  {"id": "lex.en.200k.059204", "hw": "rock purslane", "pos": "phrase", "ipa": "/rɑːk ˈpɜːrsleɪn/", "vi": "cây rau sam đá Calandrinia"},
  {"id": "lex.en.200k.059205", "hw": "scarlet tanager", "pos": "phrase", "ipa": "/ˈskɑːrlət ˈtænədʒər/", "vi": "chim hồng y đỏ tươi cánh đen"},
  {"id": "lex.en.200k.059206", "hw": "substantia nigra", "pos": "phrase", "ipa": "/səbˈstænʃiə ˈnaɪɡrə/", "vi": "chất đen trong trung não"},
  {"id": "lex.en.200k.059207", "hw": "tomas de torquemada", "pos": "phrase", "ipa": "/toʊˈmɑːs deɪ ˌtɔːrkəˈmɑːdə/", "vi": "đại phán quan Tomás Torquemada"},
  {"id": "lex.en.200k.059208", "hw": "vena pectoralis", "pos": "phrase", "ipa": "/ˈviːnə ˌpɛktəˈreɪlɪs/", "vi": "tĩnh mạch vùng cơ ngực"},
  {"id": "lex.en.200k.059209", "hw": "vinca major", "pos": "phrase", "ipa": "/ˈvɪŋkə ˈmeɪdʒər/", "vi": "cây dừa cạn hoa tím lớn"},
  {"id": "lex.en.200k.059210", "hw": "vinca minor", "pos": "phrase", "ipa": "/ˈvɪŋkə ˈmaɪnər/", "vi": "cây dừa cạn dây hoa nhỏ"},
  {"id": "lex.en.200k.059211", "hw": "viscountess astor", "pos": "phrase", "ipa": "/ˌvaɪkaʊntəs ˈæstər/", "vi": "Nữ tử tước Nancy Astor"},
  {"id": "lex.en.200k.059212", "hw": "vladimir vladimirovich putin", "pos": "phrase", "ipa": "/ˈvlædɪmɪr vlæˈdɪmɪrəvɪtʃ ˈpuːtɪn/", "vi": "tổng thống Nga Vladimir Putin"},
  {"id": "lex.en.200k.059213", "hw": "william tindal", "pos": "phrase", "ipa": "/ˈwɪljəm ˈtɪndəl/", "vi": "nhà dịch Kinh Thánh Tyndale"},
  {"id": "lex.en.200k.059214", "hw": "wilms tumour", "pos": "phrase", "ipa": "/vɪlmz ˈtjuːmər/", "vi": "u nguyên bào thận Wilms ở trẻ"},
  {"id": "lex.en.200k.059215", "hw": "winter purslane", "pos": "phrase", "ipa": "/ˈwɪntər ˈpɜːrsleɪn/", "vi": "rau sam mùa đông claytonia"},
  {"id": "lex.en.200k.059216", "hw": "acetaldehydes", "pos": "noun", "ipa": "/ˌæsɪtˈældɪhaɪdz/", "vi": "hợp chất hữu cơ axetanđêhit"},
  {"id": "lex.en.200k.059217", "hw": "anodynes", "pos": "noun", "ipa": "/ˈænədaɪnz/", "vi": "thuốc giảm đau; lời xoa dịu"},
  {"id": "lex.en.200k.059218", "hw": "arapahos", "pos": "noun", "ipa": "/əˈræpəhoʊz/", "vi": "người bản địa da đỏ Arapaho"},
  {"id": "lex.en.200k.059219", "hw": "arthroplasties", "pos": "noun", "ipa": "/ˈɑːrθroʊˌplæstiz/", "vi": "phẫu thuật thay tạo hình khớp"},
  {"id": "lex.en.200k.059220", "hw": "bacteriophages", "pos": "noun", "ipa": "/bækˈtɪəriəfeɪdʒɪz/", "vi": "thực khuẩn thể diệt khuẩn"},
  {"id": "lex.en.200k.059221", "hw": "bakunins", "pos": "noun", "ipa": "/bəkˈuːnɪnz/", "vi": "nhà lý luận Mikhail Bakunin"},
  {"id": "lex.en.200k.059222", "hw": "bearcats", "pos": "noun", "ipa": "/bˈɛrkæts/", "vi": "loài cầy mực gấu binturong"},
  {"id": "lex.en.200k.059223", "hw": "bluebeards", "pos": "noun", "ipa": "/blˈuːbɪrdz/", "vi": "gã sát thê Lão Râu Xanh"},
  {"id": "lex.en.200k.059224", "hw": "boeufs", "pos": "noun", "ipa": "/bˈɜːfs/", "vi": "món thịt bò kiểu Pháp bœuf"},
  {"id": "lex.en.200k.059225", "hw": "brigantines", "pos": "noun", "ipa": "/brˈɪɡəntiːnz/", "vi": "loại thuyền hai cột buồm vuông"},
  {"id": "lex.en.200k.059226", "hw": "bugbears", "pos": "noun", "ipa": "/bˈʌɡbɛrz/", "vi": "nỗi ám ảnh; điều gây sợ hãi"},
  {"id": "lex.en.200k.059227", "hw": "cerebra", "pos": "noun", "ipa": "/sərˈiːbrə/", "vi": "các bán cầu đại não bộ não"},
  {"id": "lex.en.200k.059228", "hw": "cerebrums", "pos": "noun", "ipa": "/sərˈiːbrəmz/", "vi": "các bán cầu đại não người"},
  {"id": "lex.en.200k.059229", "hw": "cheapened", "pos": "verb", "ipa": "/tʃˈipənd/", "vi": "đã làm giảm giá trị; hạ phẩm"},
  {"id": "lex.en.200k.059230", "hw": "cheapening", "pos": "verb", "ipa": "/tʃˈipənɪŋ/", "vi": "đang làm giảm phẩm giá; hạ giá"},
  {"id": "lex.en.200k.059231", "hw": "cheapens", "pos": "verb", "ipa": "/tʃˈipənz/", "vi": "làm giảm phẩm giá; hạ giá thành"},
  {"id": "lex.en.200k.059232", "hw": "coffers", "pos": "noun", "ipa": "/kˈɑfɚz/", "vi": "rương báu; kho quỹ tài chính"},
  {"id": "lex.en.200k.059233", "hw": "corsages", "pos": "noun", "ipa": "/kɔːrsˈɑːʒɪz/", "vi": "hoa cài áo dạ hội của phụ nữ"},
  {"id": "lex.en.200k.059234", "hw": "counterexamples", "pos": "noun", "ipa": "/kˈaʊntɚrɪɡzˌæmpəlz/", "vi": "phản ví dụ bác bỏ luận điểm"},
  {"id": "lex.en.200k.059235", "hw": "cronuses", "pos": "noun", "ipa": "/krˈoʊnəsɪz/", "vi": "thần thời gian nông nghiệp Cronus"},
  {"id": "lex.en.200k.059236", "hw": "dahomeys", "pos": "noun", "ipa": "/dəhˈoʊmiz/", "vi": "vương quốc cổ Dahomey ở Tây Phi"},
  {"id": "lex.en.200k.059237", "hw": "daimons", "pos": "noun", "ipa": "/dˈeɪmɑːnz/", "vi": "linh hồn dẫn dắt; thần hộ mệnh"},
  {"id": "lex.en.200k.059238", "hw": "decommissioned", "pos": "verb", "ipa": "/dikəmˈɪʃənd/", "vi": "đã xuất biên chế; ngừng dùng"},
  {"id": "lex.en.200k.059239", "hw": "decommissioning", "pos": "verb", "ipa": "/dikəmˈɪʃənɪŋ/", "vi": "đang tháo dỡ; cho nghỉ hưu tàu"},
  {"id": "lex.en.200k.059240", "hw": "decommissions", "pos": "verb", "ipa": "/diːkəmˈɪʃənz/", "vi": "loại khỏi biên chế; tháo dỡ"},
  {"id": "lex.en.200k.059241", "hw": "discolored", "pos": "verb", "ipa": "/dɪskˈʌlɚd/", "vi": "đã làm đổi màu; đã hoen ố"},
  {"id": "lex.en.200k.059242", "hw": "discoloring", "pos": "verb", "ipa": "/dɪskˈʌlərɪŋ/", "vi": "làm phai màu ố; đổi sắc thái"},
  {"id": "lex.en.200k.059243", "hw": "discolors", "pos": "verb", "ipa": "/dɪskˈʌlɚz/", "vi": "làm biến màu; làm hoen ố"},
  {"id": "lex.en.200k.059244", "hw": "drubbings", "pos": "noun", "ipa": "/drˈʌbɪŋz/", "vi": "trận đòn roi; trận thua thảm bại"},
  {"id": "lex.en.200k.059245", "hw": "dumpers", "pos": "noun", "ipa": "/dˈʌmpɚz/", "vi": "xe tải ben tự đổ; kẻ ruồng bỏ"},
  {"id": "lex.en.200k.059246", "hw": "eclairs", "pos": "noun", "ipa": "/eɪklˈɛrz/", "vi": "bánh su kem dài éclair"},
  {"id": "lex.en.200k.059247", "hw": "ehrenbergs", "pos": "noun", "ipa": "/ˈɛərənbɜːrɡz/", "vi": "nhà sinh vật học Ehrenberg"},
  {"id": "lex.en.200k.059248", "hw": "emanations", "pos": "noun", "ipa": "/ˌɛmənˈeɪʃənz/", "vi": "sự tỏa ra; nguồn năng lượng phát"},
  {"id": "lex.en.200k.059249", "hw": "encumbrances", "pos": "noun", "ipa": "/ɪnkˈʌmbrənsɪz/", "vi": "gánh nặng; tài sản gán nợ chấp"},
  {"id": "lex.en.200k.059250", "hw": "equalisations", "pos": "noun", "ipa": "/ˌiːkwəlaɪzˈeɪʃənz/", "vi": "sự làm cân bằng; chỉnh âm tần"},
  {"id": "lex.en.200k.059251", "hw": "estheticses", "pos": "noun", "ipa": "/ɛsθˈɛtɪksɪz/", "vi": "môn mỹ học; chuẩn mực thẩm mỹ"},
  {"id": "lex.en.200k.059252", "hw": "euphonia", "pos": "noun", "ipa": "/juːfˈoʊniə/", "vi": "kèn đồng trầm euphonium"},
  {"id": "lex.en.200k.059253", "hw": "frgs", "pos": "noun", "ipa": "/ˌɛfɑːrdʒˈiːz/", "vi": "Cộng hòa Liên bang Tây Đức"},
  {"id": "lex.en.200k.059254", "hw": "geums", "pos": "noun", "ipa": "/dʒˈiːəmz/", "vi": "chi thực vật hoa thủy hoàng geum"},
  {"id": "lex.en.200k.059255", "hw": "gonorrhoeae", "pos": "noun", "ipa": "/ˌɡɑːnərˈiːiː/", "vi": "vi khuẩn song cầu lậu Neisseria"},
  {"id": "lex.en.200k.059256", "hw": "gonorrhoeas", "pos": "noun", "ipa": "/ˌɡɑːnərˈiːəz/", "vi": "các ca mắc bệnh lây truyền lậu"},
  {"id": "lex.en.200k.059257", "hw": "grabbier", "pos": "adj", "ipa": "/ɡrˈæbiɚ/", "vi": "hay chộp giật hơn; tham lam hơn"},
  {"id": "lex.en.200k.059258", "hw": "grabbiest", "pos": "adj", "ipa": "/ɡrˈæbiɪst/", "vi": "hay chộp giật nhất; hám lợi nhất"},
  {"id": "lex.en.200k.059259", "hw": "grandees", "pos": "noun", "ipa": "/ɡrændˈiːz/", "vi": "bậc đại quý tộc; nhân vật tai to"},
  {"id": "lex.en.200k.059260", "hw": "herculaneums", "pos": "noun", "ipa": "/hˌɜːrkjəlˈeɪniəmz/", "vi": "thành phố cổ Herculaneum La Mã"},
  {"id": "lex.en.200k.059261", "hw": "hollandses", "pos": "noun", "ipa": "/hˈɑːləndzɪz/", "vi": "rượu gin mạch nha Hollands Hà Lan"},
  {"id": "lex.en.200k.059262", "hw": "igniters", "pos": "noun", "ipa": "/ɪɡnˈaɪtɚz/", "vi": "ngòi nổ; bộ phận đánh lửa mồi"},
  {"id": "lex.en.200k.059263", "hw": "improbabilities", "pos": "noun", "ipa": "/ˌɪmprɑːbəbˈɪlətiz/", "vi": "khả năng khó xảy ra; điều phi lý"},
  {"id": "lex.en.200k.059264", "hw": "intercostals", "pos": "noun", "ipa": "/ˌɪntərkˈɑːstəlz/", "vi": "nhóm cơ liên sườn gian sườn"},
  {"id": "lex.en.200k.059265", "hw": "jasperses", "pos": "noun", "ipa": "/dʒˈæspɚzɪz/", "vi": "triết gia hiện sinh Karl Jaspers"},
  {"id": "lex.en.200k.059266", "hw": "jerkers", "pos": "noun", "ipa": "/dʒˈɜːrkɚz/", "vi": "người hay giật mạnh; đòn gạt giật"},
  {"id": "lex.en.200k.059267", "hw": "kasais", "pos": "noun", "ipa": "/kəsˈaɪz/", "vi": "dòng sông Kasai ở Trung Phi"},
  {"id": "lex.en.200k.059268", "hw": "kennewicks", "pos": "noun", "ipa": "/kˈɛnəwɪks/", "vi": "hài cốt Kennewick; thành phố"},
  {"id": "lex.en.200k.059269", "hw": "kordas", "pos": "noun", "ipa": "/kˈɔːrdəz/", "vi": "nhà làm phim Alexander Korda"},
  {"id": "lex.en.200k.059270", "hw": "kuras", "pos": "noun", "ipa": "/kˈʊrəz/", "vi": "dòng sông Kura vùng Kavkaz"},
  {"id": "lex.en.200k.059271", "hw": "ledes", "pos": "noun", "ipa": "/lˈiːdz/", "vi": "đoạn mở đầu bản tin bài báo"},
  {"id": "lex.en.200k.059272", "hw": "legionnaires", "pos": "noun", "ipa": "/lˈidʒənˌɛrz/", "vi": "lính quân đoàn lê dương Pháp"},
  {"id": "lex.en.200k.059273", "hw": "leishmaniases", "pos": "noun", "ipa": "/liːʃmənˈaɪəsiːz/", "vi": "bệnh truyền nhiễm leishmania da"},
  {"id": "lex.en.200k.059274", "hw": "liefer", "pos": "adv", "ipa": "/lˈifɚ/", "vi": "thà rằng; vui lòng sẵn sàng hơn"},
  {"id": "lex.en.200k.059275", "hw": "liefest", "pos": "adv", "ipa": "/lˈiːfɪst/", "vi": "thích nhất; vui lòng nhất"},
  {"id": "lex.en.200k.059276", "hw": "mendicants", "pos": "noun", "ipa": "/mˈɛndɪkənts/", "vi": "tu sĩ khất thực; người ăn xin"},
  {"id": "lex.en.200k.059277", "hw": "microglias", "pos": "noun", "ipa": "/maɪkrˈɑːɡliəz/", "vi": "tế bào vi đệm miễn dịch não"},
  {"id": "lex.en.200k.059278", "hw": "mileposts", "pos": "noun", "ipa": "/mˈaɪlpoʊsts/", "vi": "cột mốc dặm cây số; mốc thời gian"},
  {"id": "lex.en.200k.059279", "hw": "moseyed", "pos": "verb", "ipa": "/mˈoʊzid/", "vi": "đã tản bộ thong thả dạo chơi"},
  {"id": "lex.en.200k.059280", "hw": "moseying", "pos": "verb", "ipa": "/mˈoʊziɪŋ/", "vi": "đang tản bộ thong dong nhẹ nhàng"},
  {"id": "lex.en.200k.059281", "hw": "moseys", "pos": "verb", "ipa": "/mˈoʊziz/", "vi": "đi tản bộ thong thả dạo bước"},
  {"id": "lex.en.200k.059282", "hw": "mshes", "pos": "noun", "ipa": "/ˌɛmɛsˈeɪtʃɪz/", "vi": "hoóc-môn kích thích sắc tố da"},
  {"id": "lex.en.200k.059283", "hw": "myocardia", "pos": "noun", "ipa": "/ˌmaɪoʊkˈɑːrdiə/", "vi": "lớp cơ tim dày của thành tim"},
  {"id": "lex.en.200k.059284", "hw": "newsagents", "pos": "noun", "ipa": "/nˈuːzeɪdʒənts/", "vi": "chủ quầy bán báo tạp chí"},
  {"id": "lex.en.200k.059285", "hw": "oleanders", "pos": "noun", "ipa": "/ˈoʊliˌændɚz/", "vi": "cây hoa bụi trúc đào có độc"},
  {"id": "lex.en.200k.059286", "hw": "palavered", "pos": "verb", "ipa": "/pəlˈævɚd/", "vi": "đã bàn tán lôi thôi dài dòng"},
  {"id": "lex.en.200k.059287", "hw": "palavering", "pos": "verb", "ipa": "/pəlˈævərɪŋ/", "vi": "đang nói chuyện phiếm rườm rà"},
  {"id": "lex.en.200k.059288", "hw": "palavers", "pos": "noun", "ipa": "/pəlˈævɚz/", "vi": "chuyện bàn tán rườm rà; đàm phán"},
  {"id": "lex.en.200k.059289", "hw": "palings", "pos": "noun", "ipa": "/pˈeɪlɪŋz/", "vi": "cọc gỗ hàng rào nhọn đầu"},
  {"id": "lex.en.200k.059290", "hw": "parallelograms", "pos": "noun", "ipa": "/pˌærəlˈɛləɡrˌæmz/", "vi": "hình bình hành bốn cạnh đối song"},
  {"id": "lex.en.200k.059291", "hw": "peavies", "pos": "noun", "ipa": "/pˈiːviz/", "vi": "cần móc bẩy lăn cây gỗ xẻ"},
  {"id": "lex.en.200k.059292", "hw": "perchlorates", "pos": "noun", "ipa": "/pərklˈɔːreɪts/", "vi": "muối peclorat khử trùng tẩy"},
  {"id": "lex.en.200k.059293", "hw": "photometries", "pos": "noun", "ipa": "/foʊtˈɑːmətriːz/", "vi": "kỹ thuật đo quang thông trắc"},
  {"id": "lex.en.200k.059294", "hw": "phrygians", "pos": "noun", "ipa": "/frˈɪdʒiənz/", "vi": "người xứ Phrygia cổ Tiểu Á"},
  {"id": "lex.en.200k.059295", "hw": "piceas", "pos": "noun", "ipa": "/paɪsˈiːəz/", "vi": "chi thực vật cây vân sam picea"},
  {"id": "lex.en.200k.059296", "hw": "platers", "pos": "noun", "ipa": "/plˈeɪtɚz/", "vi": "thợ xi mạ; thợ tán đinh vỏ tàu"},
  {"id": "lex.en.200k.059297", "hw": "polskas", "pos": "noun", "ipa": "/pˈoʊlskəz/", "vi": "điệu múa xoay vòng polska Bắc Âu"},
  {"id": "lex.en.200k.059298", "hw": "polymaths", "pos": "noun", "ipa": "/pˈɑːlimæθs/", "vi": "người học rộng biết nhiều bách khoa"},
  {"id": "lex.en.200k.059299", "hw": "pontifexes", "pos": "noun", "ipa": "/pˈɑːntɪfɛksɪz/", "vi": "thành viên viện giáo tư tế La Mã"},
  {"id": "lex.en.200k.059300", "hw": "pontifices", "pos": "noun", "ipa": "/pɒntˈɪfɪsiːz/", "vi": "các đại tư tế giáo phẩm La Mã cổ"},
  {"id": "lex.en.200k.059301", "hw": "purines", "pos": "noun", "ipa": "/pjˈʊriːnz/", "vi": "hợp chất bazơ nitơ purin"},
  {"id": "lex.en.200k.059302", "hw": "revivalists", "pos": "noun", "ipa": "/rɪvˈaɪvəlɪsts/", "vi": "nhà truyền giáo phục hưng đức tin"}
]

with open('scratch/b32_r09_raw_p3.json') as f:
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

with open('scratch/b32_r09_p3.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

print("Part 3 validated and written successfully.")
