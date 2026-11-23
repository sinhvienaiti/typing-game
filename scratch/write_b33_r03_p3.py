import json

items = [
  {"id": "lex.en.200k.061203", "hw": "assignations", "pos": "noun", "ipa": "/ˌæsɪɡˈneɪʃənz/", "vi": "cuộc hẹn hò bí mật; sự ấn định"},
  {"id": "lex.en.200k.061204", "hw": "attenuators", "pos": "noun", "ipa": "/əˈtɛnjueɪtərz/", "vi": "bộ suy giảm tín hiệu điện tử"},
  {"id": "lex.en.200k.061205", "hw": "beefsteaks", "pos": "noun", "ipa": "/ˈbiːfsteɪks/", "vi": "miếng thịt bò bít tết nướng"},
  {"id": "lex.en.200k.061206", "hw": "blasphemers", "pos": "noun", "ipa": "/blæsˈfiːmərz/", "vi": "kẻ báng bổ; người xúc phạm thần"},
  {"id": "lex.en.200k.061207", "hw": "buffetings", "pos": "noun", "ipa": "/ˈbʌfətɪŋz/", "vi": "những cú đấm quật đánh liên tiếp"},
  {"id": "lex.en.200k.061208", "hw": "bunas", "pos": "noun", "ipa": "/ˈbjuːnəz/", "vi": "cao su nhân tạo tổng hợp Buna"},
  {"id": "lex.en.200k.061209", "hw": "calorimetries", "pos": "noun", "ipa": "/ˌkæləˈrɪmətriːz/", "vi": "phép đo nhiệt lượng phản ứng"},
  {"id": "lex.en.200k.061210", "hw": "carboxylated", "pos": "verb", "ipa": "/kɑːrˈbɑːksəleɪtɪd/", "vi": "đã gắn thêm nhóm cacboxyl vào chất"},
  {"id": "lex.en.200k.061211", "hw": "carboxylates", "pos": "verb", "ipa": "/kɑːrˈbɑːksəleɪts/", "vi": "gắn nhóm cacboxyl vào hợp chất"},
  {"id": "lex.en.200k.061212", "hw": "carboxylating", "pos": "verb", "ipa": "/kɑːrˈbɑːksəleɪtɪŋ/", "vi": "đang gắn nhóm cacboxyl hóa học"},
  {"id": "lex.en.200k.061213", "hw": "carrells", "pos": "noun", "ipa": "/ˈkærəlz/", "vi": "bàn đọc sách có vách ngăn thư viện"},
  {"id": "lex.en.200k.061214", "hw": "catacombs", "pos": "noun", "ipa": "/ˈkætəkoʊmz/", "vi": "hầm mộ ngầm; đường hầm chôn cất cổ"},
  {"id": "lex.en.200k.061215", "hw": "cereuses", "pos": "noun", "ipa": "/ˈsɪriəsɪz/", "vi": "cây xương rồng hoa quỳnh nở đêm"},
  {"id": "lex.en.200k.061216", "hw": "chanukahs", "pos": "noun", "ipa": "/ˈhɑːnəkəz/", "vi": "lễ hội Ánh sáng Hanukkah Do Thái"},
  {"id": "lex.en.200k.061217", "hw": "chekovs", "pos": "noun", "ipa": "/ˈtʃɛkɔːfs/", "vi": "đại văn hào Nga Anton Chekhov"},
  {"id": "lex.en.200k.061218", "hw": "chloroquines", "pos": "noun", "ipa": "/ˈklɔːrəkwiːnz/", "vi": "thuốc điều trị sốt rét chloroquine"},
  {"id": "lex.en.200k.061219", "hw": "coadjutors", "pos": "noun", "ipa": "/koʊˈædʒətərz/", "vi": "giám mục phó kế vị; người phụ tá"},
  {"id": "lex.en.200k.061220", "hw": "consonances", "pos": "noun", "ipa": "/ˈkɑːnsənənsɪz/", "vi": "sự hòa hợp âm thanh; sự đồng điệu"},
  {"id": "lex.en.200k.061221", "hw": "corots", "pos": "noun", "ipa": "/kɔːˈroʊz/", "vi": "họa sĩ phong cảnh Pháp Corot"},
  {"id": "lex.en.200k.061222", "hw": "cubits", "pos": "noun", "ipa": "/ˈkjuːbɪts/", "vi": "đơn vị đo chiều dài cổ đại cubit"},
  {"id": "lex.en.200k.061223", "hw": "cyclopedias", "pos": "noun", "ipa": "/ˌsaɪkləˈpiːdiəz/", "vi": "bộ sách bách khoa toàn thư tra cứu"},
  {"id": "lex.en.200k.061224", "hw": "dards", "pos": "noun", "ipa": "/dɑːrdz/", "vi": "người dân hoặc ngữ chi Dard Nam Á"},
  {"id": "lex.en.200k.061225", "hw": "deathtraps", "pos": "noun", "ipa": "/ˈdɛθtræps/", "vi": "cái bẫy tử thần; nơi cực nguy hiểm"},
  {"id": "lex.en.200k.061226", "hw": "decarboxylases", "pos": "noun", "ipa": "/ˌdiːkɑːrˈbɑːksəleɪsɪz/", "vi": "men enzyme khử nhóm cacboxyl"},
  {"id": "lex.en.200k.061227", "hw": "decriminalisations", "pos": "noun", "ipa": "/diːˌkrɪmɪnəlaɪˈzeɪʃənz/", "vi": "sự xóa bỏ tội danh phi hình sự hóa"},
  {"id": "lex.en.200k.061228", "hw": "demiurges", "pos": "noun", "ipa": "/ˈdɛmiɜːrdʒɪz/", "vi": "đấng tạo hóa thế giới vật chất"},
  {"id": "lex.en.200k.061229", "hw": "diamines", "pos": "noun", "ipa": "/ˈdaɪəmiːnz/", "vi": "hợp chất hữu cơ chứa hai nhóm amin"},
  {"id": "lex.en.200k.061230", "hw": "diddleys", "pos": "noun", "ipa": "/ˈdɪdliz/", "vi": "nhạc sĩ rock Bo Diddley; tí tẹo"},
  {"id": "lex.en.200k.061231", "hw": "doubters", "pos": "noun", "ipa": "/ˈdaʊtərz/", "vi": "người hay nghi ngờ; kẻ hoài nghi"},
  {"id": "lex.en.200k.061232", "hw": "earwigs", "pos": "noun", "ipa": "/ˈɪərwɪɡz/", "vi": "con bọ kìm đuôi kẹp; sâu tai"},
  {"id": "lex.en.200k.061233", "hw": "ectoplasms", "pos": "noun", "ipa": "/ˈɛktəplæzəmz/", "vi": "lớp ngoại chất tế bào; linh chất"},
  {"id": "lex.en.200k.061234", "hw": "escargots", "pos": "noun", "ipa": "/ˌɛskɑːrˈɡoʊz/", "vi": "món ốc sên nướng bơ tỏi kiểu Pháp"},
  {"id": "lex.en.200k.061235", "hw": "falkners", "pos": "noun", "ipa": "/ˈfɔːknərz/", "vi": "đại văn hào Nobel William Faulkner"},
  {"id": "lex.en.200k.061236", "hw": "ferritins", "pos": "noun", "ipa": "/ˈfɛrətɪnz/", "vi": "protein dự trữ chất sắt ferritin"},
  {"id": "lex.en.200k.061237", "hw": "fitments", "pos": "noun", "ipa": "/ˈfɪtmənts/", "vi": "đồ nội thất gắn cố định; phụ kiện"},
  {"id": "lex.en.200k.061238", "hw": "forelands", "pos": "noun", "ipa": "/ˈfɔːrlændz/", "vi": "mũi đất nhô ra biển; vùng đất ven"},
  {"id": "lex.en.200k.061239", "hw": "gobblers", "pos": "noun", "ipa": "/ˈɡɑːblərz/", "vi": "gà tây trống; người ăn ngấu nghiến"},
  {"id": "lex.en.200k.061240", "hw": "groszes", "pos": "noun", "ipa": "/ˈɡroʊʃɪz/", "vi": "tiền xu nhỏ grosz của Ba Lan"},
  {"id": "lex.en.200k.061241", "hw": "groszy", "pos": "noun", "ipa": "/ˈɡroʊʃi/", "vi": "đồng tiền xu grosz đơn vị Ba Lan"},
  {"id": "lex.en.200k.061242", "hw": "hairballs", "pos": "noun", "ipa": "/ˈhɛərbɔːlz/", "vi": "búi lông vón cục trong dạ dày mèo"},
  {"id": "lex.en.200k.061243", "hw": "hooters", "pos": "noun", "ipa": "/ˈhuːtərz/", "vi": "còi hú xe hơi; chim cú kêu ban đêm"},
  {"id": "lex.en.200k.061244", "hw": "housmans", "pos": "noun", "ipa": "/ˈhaʊsmənz/", "vi": "nhà thơ học giả Anh A. E. Housman"},
  {"id": "lex.en.200k.061245", "hw": "hypoplasias", "pos": "noun", "ipa": "/ˌhaɪpoʊˈpleɪʒiəz/", "vi": "tình trạng cơ quan kém phát triển"},
  {"id": "lex.en.200k.061246", "hw": "improvers", "pos": "noun", "ipa": "/ɪmˈpruːvərz/", "vi": "chất cải thiện; người học nghề"},
  {"id": "lex.en.200k.061247", "hw": "injuns", "pos": "noun", "ipa": "/ˈɪndʒənz/", "vi": "tiếng lóng cũ chỉ người da đỏ Mỹ"},
  {"id": "lex.en.200k.061248", "hw": "iphigenias", "pos": "noun", "ipa": "/ˌɪfəˈdʒiːniəz/", "vi": "công chúa Iphigenia thần thoại"},
  {"id": "lex.en.200k.061249", "hw": "jetliners", "pos": "noun", "ipa": "/ˈdʒɛtlaɪnərz/", "vi": "máy bay phản lực chở khách cỡ lớn"},
  {"id": "lex.en.200k.061250", "hw": "jinjas", "pos": "noun", "ipa": "/ˈdʒɪndʒəz/", "vi": "thành phố Jinja bên hồ Victoria"},
  {"id": "lex.en.200k.061251", "hw": "jitterbugged", "pos": "verb", "ipa": "/ˈdʒɪtərbʌɡd/", "vi": "đã nhảy điệu jitterbug sôi động"},
  {"id": "lex.en.200k.061252", "hw": "jitterbugging", "pos": "verb", "ipa": "/ˈdʒɪtərbʌɡɪŋ/", "vi": "đang nhảy điệu swing jitterbug"},
  {"id": "lex.en.200k.061253", "hw": "jitterbugs", "pos": "noun", "ipa": "/ˈdʒɪtərbʌɡz/", "vi": "điệu nhảy jitterbug; người bồn chồn"},
  {"id": "lex.en.200k.061254", "hw": "jowls", "pos": "noun", "ipa": "/dʒaʊlz/", "vi": "phần má hàm dưới chảy xệ; nọng má"},
  {"id": "lex.en.200k.061255", "hw": "kickapoos", "pos": "noun", "ipa": "/ˈkɪkəpuːz/", "vi": "bộ tộc thổ dân da đỏ Kickapoo Mỹ"},
  {"id": "lex.en.200k.061256", "hw": "kimberlites", "pos": "noun", "ipa": "/ˈkɪmbərlaɪts/", "vi": "đá kimberlit thường chứa kim cương"},
  {"id": "lex.en.200k.061257", "hw": "knowers", "pos": "noun", "ipa": "/ˈnoʊərz/", "vi": "người am tường; người hiểu rõ"},
  {"id": "lex.en.200k.061258", "hw": "loges", "pos": "noun", "ipa": "/loʊʒɪz/", "vi": "lô ghế hạng sang trong rạp hát"},
  {"id": "lex.en.200k.061259", "hw": "logjams", "pos": "noun", "ipa": "/ˈlɑːɡdʒæmz/", "vi": "cảnh ùn tắc kẹt cứng; gỗ kẹt sông"},
  {"id": "lex.en.200k.061260", "hw": "magneticses", "pos": "noun", "ipa": "/mæɡˈnɛtɪksɪz/", "vi": "ngành vật lý nghiên cứu từ học"},
  {"id": "lex.en.200k.061261", "hw": "maillots", "pos": "noun", "ipa": "/maɪˈoʊz/", "vi": "đồ bơi liền một mảnh; áo cua-rơ"},
  {"id": "lex.en.200k.061262", "hw": "malars", "pos": "noun", "ipa": "/ˈmeɪlərz/", "vi": "xương gò má nằm dưới hốc mắt"},
  {"id": "lex.en.200k.061263", "hw": "martinets", "pos": "noun", "ipa": "/ˌmɑːrtəˈnɛts/", "vi": "người chỉ huy kỷ luật cực khắt khe"},
  {"id": "lex.en.200k.061264", "hw": "mbds", "pos": "noun", "ipa": "/ɛm biː diːz/", "vi": "rối loạn chức năng não tối thiểu"},
  {"id": "lex.en.200k.061265", "hw": "meadowlarks", "pos": "noun", "ipa": "/ˈmɛdoʊlɑːrks/", "vi": "chim sơn ca đồng cỏ ức vàng Mỹ"},
  {"id": "lex.en.200k.061266", "hw": "mechanisations", "pos": "noun", "ipa": "/ˌmɛkənaɪˈzeɪʃənz/", "vi": "sự cơ giới hóa bằng máy móc"},
  {"id": "lex.en.200k.061267", "hw": "miscasts", "pos": "verb", "ipa": "/ˌmɪsˈkæsts/", "vi": "phân vai diễn viên không hợp vai"},
  {"id": "lex.en.200k.061268", "hw": "misdirected", "pos": "verb", "ipa": "/ˌmɪsdəˈrɛktɪd/", "vi": "đã chỉ sai đường; điều hướng lệch"},
  {"id": "lex.en.200k.061269", "hw": "misdirecting", "pos": "verb", "ipa": "/ˌmɪsdəˈrɛktɪŋ/", "vi": "đang chỉ sai đường; đánh lạc hướng"},
  {"id": "lex.en.200k.061270", "hw": "misdirects", "pos": "verb", "ipa": "/ˌmɪsdəˈrɛkts/", "vi": "chỉ sai hướng; gửi nhầm địa chỉ"},
  {"id": "lex.en.200k.061271", "hw": "mohicans", "pos": "noun", "ipa": "/moʊˈhiːkənz/", "vi": "bộ tộc thổ dân da đỏ Mohican"},
  {"id": "lex.en.200k.061272", "hw": "monocytes", "pos": "noun", "ipa": "/ˈmɑːnəsaɪts/", "vi": "tế bào bạch cầu đơn nhân miễn dịch"},
  {"id": "lex.en.200k.061273", "hw": "motrins", "pos": "noun", "ipa": "/ˈmoʊtrɪnz/", "vi": "thuốc giảm đau chống viêm Motrin"},
  {"id": "lex.en.200k.061274", "hw": "nards", "pos": "noun", "ipa": "/nɑːrdz/", "vi": "dầu thơm cam tùng hương cổ đại"},
  {"id": "lex.en.200k.061275", "hw": "neoshos", "pos": "noun", "ipa": "/niˈoʊʃoʊz/", "vi": "dòng sông Neosho miền trung Mỹ"},
  {"id": "lex.en.200k.061276", "hw": "ninjutsus", "pos": "noun", "ipa": "/nɪnˈdʒʊtsuz/", "vi": "võ thuật nhẫn giả bí truyền Nhật"},
  {"id": "lex.en.200k.061277", "hw": "nystagmuses", "pos": "noun", "ipa": "/nɪˈstæɡməsɪz/", "vi": "tật rung giật nhãn cầu không chủ ý"},
  {"id": "lex.en.200k.061278", "hw": "outplayed", "pos": "verb", "ipa": "/aʊtˈpleɪd/", "vi": "đã thi đấu lấn lướt vượt trội hơn"},
  {"id": "lex.en.200k.061279", "hw": "outplaying", "pos": "verb", "ipa": "/aʊtˈpleɪɪŋ/", "vi": "đang chơi hay hơn hẳn đối thủ"},
  {"id": "lex.en.200k.061280", "hw": "outplays", "pos": "verb", "ipa": "/aʊtˈpleɪz/", "vi": "chơi hay hơn hẳn; áp đảo đối thủ"},
  {"id": "lex.en.200k.061281", "hw": "palladios", "pos": "noun", "ipa": "/pəˈlɑːdioʊz/", "vi": "kiến trúc sư Ý Andrea Palladio"},
  {"id": "lex.en.200k.061282", "hw": "pangaeas", "pos": "noun", "ipa": "/pænˈdʒiːəz/", "vi": "siêu lục địa cổ đại Pangaea"},
  {"id": "lex.en.200k.061283", "hw": "pendents", "pos": "noun", "ipa": "/ˈpɛndənts/", "vi": "mặt dây chuyền trang sức treo cổ"},
  {"id": "lex.en.200k.061284", "hw": "pickerels", "pos": "noun", "ipa": "/ˈpɪkərəlz/", "vi": "loài cá chó nhỏ ăn thịt nước ngọt"},
  {"id": "lex.en.200k.061285", "hw": "pinecones", "pos": "noun", "ipa": "/ˈpaɪnkoʊnz/", "vi": "quả nón thông rụng khô chứa hạt"},
  {"id": "lex.en.200k.061286", "hw": "popularised", "pos": "verb", "ipa": "/ˈpɑːpjələraɪzd/", "vi": "đã phổ biến đại chúng rộng rãi"},
  {"id": "lex.en.200k.061287", "hw": "popularises", "pos": "verb", "ipa": "/ˈpɑːpjələraɪzɪz/", "vi": "phổ biến rộng rãi tới đại chúng"},
  {"id": "lex.en.200k.061288", "hw": "popularising", "pos": "verb", "ipa": "/ˈpɑːpjələraɪzɪŋ/", "vi": "đang phổ biến hóa; truyền bá rộng"},
  {"id": "lex.en.200k.061289", "hw": "ppks", "pos": "noun", "ipa": "/piː piː keɪz/", "vi": "Đảng Công nhân người Kurd PKK"},
  {"id": "lex.en.200k.061290", "hw": "primitivisms", "pos": "noun", "ipa": "/ˈprɪmətɪvɪzəmz/", "vi": "trường phái nguyên thủy nghệ thuật"},
  {"id": "lex.en.200k.061291", "hw": "procrastinators", "pos": "noun", "ipa": "/prəˈkræstəneɪtərz/", "vi": "người hay trì hoãn chần chừ việc"},
  {"id": "lex.en.200k.061292", "hw": "proprioceptions", "pos": "noun", "ipa": "/ˌproʊprioʊˈsɛpʃənz/", "vi": "cảm giác nhận biết vị trí cơ thể"},
  {"id": "lex.en.200k.061293", "hw": "psyops", "pos": "noun", "ipa": "/ˈsaɪɑːps/", "vi": "chiến dịch tác chiến tâm lý chiến"},
  {"id": "lex.en.200k.061294", "hw": "pugilists", "pos": "noun", "ipa": "/ˈpjuːdʒəlɪsts/", "vi": "võ sĩ quyền Anh chuyên nghiệp"},
  {"id": "lex.en.200k.061295", "hw": "ransacks", "pos": "verb", "ipa": "/ˈrænsæks/", "vi": "lục soát tung; cướp phá tan hoang"},
  {"id": "lex.en.200k.061296", "hw": "redfishes", "pos": "noun", "ipa": "/ˈrɛdfɪʃɪz/", "vi": "cá hồng đỏ; cá lù đù biển đỏ"},
  {"id": "lex.en.200k.061297", "hw": "revitalisations", "pos": "noun", "ipa": "/riːˌvaɪtəlaɪˈzeɪʃənz/", "vi": "sự hồi sinh tái thiết phát triển"},
  {"id": "lex.en.200k.061298", "hw": "salonikas", "pos": "noun", "ipa": "/səˈlɑːnɪkəz/", "vi": "thành phố cảng Thessaloniki Hy Lạp"},
  {"id": "lex.en.200k.061299", "hw": "sandbanks", "pos": "noun", "ipa": "/ˈsændbæŋks/", "vi": "bãi cát ngầm bồi tụ ven sông biển"},
  {"id": "lex.en.200k.061300", "hw": "saroyans", "pos": "noun", "ipa": "/səˈrɔɪənz/", "vi": "nhà văn Mỹ William Saroyan"},
  {"id": "lex.en.200k.061301", "hw": "sashayed", "pos": "verb", "ipa": "/sæˈʃeɪd/", "vi": "đã bước đi uyển chuyển lả lướt"},
  {"id": "lex.en.200k.061302", "hw": "sashaying", "pos": "verb", "ipa": "/sæˈʃeɪɪŋ/", "vi": "đang bước đi lả lướt sang ngang"}
]

with open('scratch/b33_r03_raw_p3.json') as f:
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

with open('scratch/b33_r03_p3.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

print("Batch 33 Round 3 Part 3 validated and written successfully.")
