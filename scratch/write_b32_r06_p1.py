import json

records = [
    {"id": "lex.en.200k.057502", "hw": "crisscrossing", "pos": "verb", "ipa": "/ˈkrɪskrɔːsɪŋ/", "vi": "đang đan chéo; đi lại chằng chịt"},
    {"id": "lex.en.200k.057503", "hw": "cultivators", "pos": "noun", "ipa": "/ˈkʌltɪveɪtɚz/", "vi": "người canh tác; máy xới đất"},
    {"id": "lex.en.200k.057504", "hw": "curlews", "pos": "noun", "ipa": "/ˈkɜːrljuːz/", "vi": "loài chim choắt mỏ cong"},
    {"id": "lex.en.200k.057505", "hw": "digoxins", "pos": "noun", "ipa": "/dɪˈdʒɑːksɪnz/", "vi": "thuốc trợ tim digoxin"},
    {"id": "lex.en.200k.057506", "hw": "dilettantes", "pos": "noun", "ipa": "/ˌdɪləˈtɑːntiz/", "vi": "những kẻ tài tử chơi bời nửa mùa"},
    {"id": "lex.en.200k.057507", "hw": "disenfranchises", "pos": "verb", "ipa": "/ˌdɪsɪnˈfræntʃaɪzɪz/", "vi": "tước quyền bầu cử công dân"},
    {"id": "lex.en.200k.057508", "hw": "disenfranchising", "pos": "verb", "ipa": "/ˌdɪsɪnˈfræntʃaɪzɪŋ/", "vi": "đang tước quyền bầu cử công dân"},
    {"id": "lex.en.200k.057509", "hw": "dogshits", "pos": "noun", "ipa": "/ˈdɔːɡʃɪts/", "vi": "bãi cứt chó; chuyện rác rưởi nhảm"},
    {"id": "lex.en.200k.057510", "hw": "dreamworlds", "pos": "noun", "ipa": "/ˈdriːmwɜːrldz/", "vi": "những thế giới cõi mộng ảo ảnh"},
    {"id": "lex.en.200k.057511", "hw": "duodena", "pos": "noun", "ipa": "/ˌduːəˈdiːnə/", "vi": "các đoạn tá tràng của ruột non"},
    {"id": "lex.en.200k.057512", "hw": "duona", "pos": "noun", "ipa": "/ˈduːoʊnə/", "vi": "bộ đôi song ca; tá tràng"},
    {"id": "lex.en.200k.057513", "hw": "duonas", "pos": "noun", "ipa": "/ˈduːoʊnəz/", "vi": "các bộ đôi song tấu âm nhạc"},
    {"id": "lex.en.200k.057514", "hw": "dushanbes", "pos": "noun", "ipa": "/duːˈʃɑːnbeɪz/", "vi": "thành phố thủ đô Dushanbe"},
    {"id": "lex.en.200k.057515", "hw": "echocardiographies", "pos": "noun", "ipa": "/ˌɛkoʊˌkɑːrdiˈɑːɡrəfiz/", "vi": "kỹ thuật siêu âm tim chẩn đoán"},
    {"id": "lex.en.200k.057516", "hw": "fatheads", "pos": "noun", "ipa": "/ˈfæthɛdz/", "vi": "những kẻ đần độn ngốc nghếch"},
    {"id": "lex.en.200k.057517", "hw": "finises", "pos": "noun", "ipa": "/ˈfɪnɪsɪz/", "vi": "phần kết thúc; đoạn kết truyện"},
    {"id": "lex.en.200k.057518", "hw": "fountainheads", "pos": "noun", "ipa": "/ˈfaʊntnhɛdz/", "vi": "cội nguồn phát sinh dồi dào"},
    {"id": "lex.en.200k.057519", "hw": "founts", "pos": "noun", "ipa": "/faʊnts/", "vi": "các phông chữ; suối nguồn dồi dào"},
    {"id": "lex.en.200k.057520", "hw": "frumpier", "pos": "adj", "ipa": "/ˈfrʌmpiər/", "vi": "lôi thôi nhếch nhác hơn"},
    {"id": "lex.en.200k.057521", "hw": "frumpiest", "pos": "adj", "ipa": "/ˈfrʌmpiɪst/", "vi": "lôi thôi nhếch nhác nhất"},
    {"id": "lex.en.200k.057522", "hw": "gambas", "pos": "noun", "ipa": "/ˈɡæmbəz/", "vi": "cây đàn viol gam-ba; món tôm gambas"},
    {"id": "lex.en.200k.057523", "hw": "giottos", "pos": "noun", "ipa": "/ˈdʒɑːtoʊz/", "vi": "danh họa thiên tài Giotto nước Ý"},
    {"id": "lex.en.200k.057524", "hw": "gliomas", "pos": "noun", "ipa": "/ɡlaɪˈoʊməz/", "vi": "các khối u thần kinh đệm não"},
    {"id": "lex.en.200k.057525", "hw": "gliomata", "pos": "noun", "ipa": "/ɡlaɪˈoʊmətə/", "vi": "u thần kinh đệm trong não"},
    {"id": "lex.en.200k.057526", "hw": "groveled", "pos": "verb", "ipa": "/ˈɡrɑːvəld/", "vi": "đã phủ phục; khúm núm quỳ lạy"},
    {"id": "lex.en.200k.057527", "hw": "haemoglobins", "pos": "noun", "ipa": "/ˌhiːməˈɡloʊbɪnz/", "vi": "huyết sắc tố hemoglobin"},
    {"id": "lex.en.200k.057528", "hw": "harmonisations", "pos": "noun", "ipa": "/ˌhɑːrmənaɪˈzeɪʃənz/", "vi": "sự hòa âm phối khí; sự hài hòa"},
    {"id": "lex.en.200k.057529", "hw": "hullabaloos", "pos": "noun", "ipa": "/ˌhʌləbəˈluːz/", "vi": "sự ồn ào la ó hỗn loạn huyên náo"},
    {"id": "lex.en.200k.057530", "hw": "husses", "pos": "noun", "ipa": "/ˈhʌsɪz/", "vi": "nhà cải cách tôn giáo Jan Hus"},
    {"id": "lex.en.200k.057531", "hw": "imprimaturs", "pos": "noun", "ipa": "/ˌɪmprɪˈmɑːtɚz/", "vi": "giấy chuẩn y xuất bản của giáo hội"},
    {"id": "lex.en.200k.057532", "hw": "incans", "pos": "noun", "ipa": "/ˈɪŋkənz/", "vi": "người dân đế chế Inca cổ đại"},
    {"id": "lex.en.200k.057533", "hw": "kafirs", "pos": "noun", "ipa": "/ˈkæfɚz/", "vi": "từ miệt thị người da đen Nam Phi"},
    {"id": "lex.en.200k.057534", "hw": "kinglier", "pos": "adj", "ipa": "/ˈkɪŋliər/", "vi": "mang phong thái bậc đế vương hơn"},
    {"id": "lex.en.200k.057535", "hw": "kingliest", "pos": "adj", "ipa": "/ˈkɪŋliɪst/", "vi": "mang phong thái đế vương nhất"},
    {"id": "lex.en.200k.057536", "hw": "lampreys", "pos": "noun", "ipa": "/ˈlæmpriz/", "vi": "loài cá mút đá ký sinh không hàm"},
    {"id": "lex.en.200k.057537", "hw": "laypeople", "pos": "noun", "ipa": "/ˈleɪpiːpəl/", "vi": "người không chuyên; người thế tục"},
    {"id": "lex.en.200k.057538", "hw": "laypersons", "pos": "noun", "ipa": "/ˈleɪpɜːrsənz/", "vi": "người không có chuyên môn cụ thể"},
    {"id": "lex.en.200k.057539", "hw": "maharajahs", "pos": "noun", "ipa": "/ˌmɑːhəˈrɑːdʒəz/", "vi": "các vị đại vương quân chủ Ấn Độ"},
    {"id": "lex.en.200k.057540", "hw": "mainsails", "pos": "noun", "ipa": "/ˈmeɪnseɪlz/", "vi": "cánh buồm chính của thuyền buồm"},
    {"id": "lex.en.200k.057541", "hw": "maldons", "pos": "noun", "ipa": "/ˈmɔːldənz/", "vi": "trận chiến lịch sử Maldon nước Anh"},
    {"id": "lex.en.200k.057542", "hw": "mannerisms", "pos": "noun", "ipa": "/ˈmænərɪzəmz/", "vi": "thói quen riêng biệt; điệu bộ riêng"},
    {"id": "lex.en.200k.057543", "hw": "mckims", "pos": "noun", "ipa": "/məˈkɪmz/", "vi": "kiến trúc sư Mỹ Charles McKim"},
    {"id": "lex.en.200k.057544", "hw": "meissners", "pos": "noun", "ipa": "/ˈmaɪsnɚz/", "vi": "thể cảm giác Meissner dưới da"},
    {"id": "lex.en.200k.057545", "hw": "melanges", "pos": "noun", "ipa": "/meɪˈlɑːnʒɪz/", "vi": "mớ hỗn hợp tạp nham pha trộn"},
    {"id": "lex.en.200k.057546", "hw": "menages", "pos": "noun", "ipa": "/meɪˈnɑːʒɪz/", "vi": "hộ gia đình; việc nội trợ gia đình"},
    {"id": "lex.en.200k.057547", "hw": "mishmashes", "pos": "noun", "ipa": "/ˈmɪʃmæʃɪz/", "vi": "mớ hỗn độn chắp vá lung tung"},
    {"id": "lex.en.200k.057548", "hw": "mollusks", "pos": "noun", "ipa": "/ˈmɑːləsks/", "vi": "các loài động vật thân mềm"},
    {"id": "lex.en.200k.057549", "hw": "moneymakers", "pos": "noun", "ipa": "/ˈmʌnimeɪkɚz/", "vi": "người hoặc thứ kiếm ra nhiều tiền"},
    {"id": "lex.en.200k.057550", "hw": "morphemes", "pos": "noun", "ipa": "/ˈmɔːrfiːmz/", "vi": "các hình vị ngữ nghĩa nhỏ nhất"},
    {"id": "lex.en.200k.057551", "hw": "narwhals", "pos": "noun", "ipa": "/ˈnɑːrwɑːlz/", "vi": "loài kỳ lân biển có sừng ngà dài"},
    {"id": "lex.en.200k.057552", "hw": "neckers", "pos": "noun", "ipa": "/ˈnɛkɚz/", "vi": "những kẻ hay ôm hôn âu yếm cổ nhau"},
    {"id": "lex.en.200k.057553", "hw": "obfuscated", "pos": "verb", "ipa": "/ˈɑːbfəskeɪtɪd/", "vi": "đã làm rối rắm; đã làm cho khó hiểu"},
    {"id": "lex.en.200k.057554", "hw": "obfuscates", "pos": "verb", "ipa": "/ˈɑːbfəskeɪts/", "vi": "làm rối rắm; làm cho tối nghĩa"},
    {"id": "lex.en.200k.057555", "hw": "obfuscating", "pos": "verb", "ipa": "/ˈɑːbfəskeɪtɪŋ/", "vi": "đang làm rối rắm; làm mờ mịt"},
    {"id": "lex.en.200k.057556", "hw": "outtakes", "pos": "noun", "ipa": "/ˈaʊtteɪks/", "vi": "các đoạn phim cảnh quay bị cắt bỏ"},
    {"id": "lex.en.200k.057557", "hw": "overpayments", "pos": "noun", "ipa": "/ˈoʊvɚpeɪmənts/", "vi": "khoản tiền thanh toán vượt mức"},
    {"id": "lex.en.200k.057558", "hw": "overtones", "pos": "noun", "ipa": "/ˈoʊvɚtoʊnz/", "vi": "họa âm bậc cao; ngụ ý kín đáo ẩn ý"},
    {"id": "lex.en.200k.057559", "hw": "pantsuits", "pos": "noun", "ipa": "/ˈpæntsuːts/", "vi": "bộ comple âu phục quần dài nữ"},
    {"id": "lex.en.200k.057560", "hw": "parasympathetics", "pos": "noun", "ipa": "/ˌpærəsɪmpəˈθɛtɪks/", "vi": "hệ thần kinh phó giao cảm cơ thể"},
    {"id": "lex.en.200k.057561", "hw": "pels", "pos": "noun", "ipa": "/pɛlz/", "vi": "các điểm ảnh pixel trên màn hình"},
    {"id": "lex.en.200k.057562", "hw": "persepolises", "pos": "noun", "ipa": "/pɚˈsɛpəlɪsɪz/", "vi": "kinh thành cổ Persepolis Ba Tư"},
    {"id": "lex.en.200k.057563", "hw": "pipettes", "pos": "noun", "ipa": "/paɪˈpɛts/", "vi": "ống hút nhỏ giọt pipet thí nghiệm"},
    {"id": "lex.en.200k.057564", "hw": "plexiglases", "pos": "noun", "ipa": "/ˈplɛksɪɡlæsɪz/", "vi": "tấm nhựa kính acrylic trong suốt"},
    {"id": "lex.en.200k.057565", "hw": "poppets", "pos": "noun", "ipa": "/ˈpɑːpɪts/", "vi": "búp bê phù phép; cục cưng; van nấm"},
    {"id": "lex.en.200k.057566", "hw": "portholes", "pos": "noun", "ipa": "/ˈpɔːrthoʊlz/", "vi": "các cửa sổ tròn đón gió mạn tàu"},
    {"id": "lex.en.200k.057567", "hw": "refiners", "pos": "noun", "ipa": "/rɪˈfaɪnɚz/", "vi": "nhà máy lọc dầu; người tinh luyện"},
    {"id": "lex.en.200k.057568", "hw": "ringmasters", "pos": "noun", "ipa": "/ˈrɪŋmæstɚz/", "vi": "người dẫn điều khiển rạp xiếc"},
    {"id": "lex.en.200k.057569", "hw": "sandburgs", "pos": "noun", "ipa": "/ˈsændbɜːrɡz/", "vi": "nhà thơ đoạt giải Carl Sandburg"},
    {"id": "lex.en.200k.057570", "hw": "schemers", "pos": "noun", "ipa": "/ˈskiːmɚz/", "vi": "những kẻ mưu mô xảo quyệt gian manh"},
    {"id": "lex.en.200k.057571", "hw": "setas", "pos": "noun", "ipa": "/ˈsiːtəz/", "vi": "các sợi lông cứng của sâu bọ nấm"},
    {"id": "lex.en.200k.057572", "hw": "sextants", "pos": "noun", "ipa": "/ˈsɛkstənts/", "vi": "kính lục phân đo góc hàng hải"},
    {"id": "lex.en.200k.057573", "hw": "signifiers", "pos": "noun", "ipa": "/ˈsɪɡnɪfaɪɚz/", "vi": "cái biểu đạt trong ký hiệu học"},
    {"id": "lex.en.200k.057574", "hw": "skydivers", "pos": "noun", "ipa": "/ˈskaɪdaɪvɚz/", "vi": "vận động viên nhảy dù tự do"},
    {"id": "lex.en.200k.057575", "hw": "smashers", "pos": "noun", "ipa": "/ˈsmæʃɚz/", "vi": "người đập vỡ; thứ vô cùng nổi bật"},
    {"id": "lex.en.200k.057576", "hw": "soupier", "pos": "adj", "ipa": "/ˈsuːpiər/", "vi": "sệt quánh như súp hơn; mù mịt hơn"},
    {"id": "lex.en.200k.057577", "hw": "soupiest", "pos": "adj", "ipa": "/ˈsuːpiɪst/", "vi": "sệt quánh như súp nhất; mù mịt nhất"},
    {"id": "lex.en.200k.057578", "hw": "splashier", "pos": "adj", "ipa": "/ˈsplæʃiər/", "vi": "bắn tóe nước nhiều hơn; rực rỡ hơn"},
    {"id": "lex.en.200k.057579", "hw": "splashiest", "pos": "adj", "ipa": "/ˈsplæʃiɪst/", "vi": "tóe nước nhiều nhất; rực rỡ nhất"},
    {"id": "lex.en.200k.057580", "hw": "subtotalled", "pos": "verb", "ipa": "/ˈsʌbˌtoʊtəld/", "vi": "đã cộng tổng tạm tính từng phần"},
    {"id": "lex.en.200k.057581", "hw": "subtotalling", "pos": "verb", "ipa": "/ˈsʌbˌtoʊtəlɪŋ/", "vi": "đang cộng tổng phụ tạm tính"},
    {"id": "lex.en.200k.057582", "hw": "subtotals", "pos": "noun", "ipa": "/ˈsʌbˌtoʊtəlz/", "vi": "các con số tổng phụ từng phần"},
    {"id": "lex.en.200k.057583", "hw": "suntans", "pos": "noun", "ipa": "/ˈsʌntænz/", "vi": "làn da rám nắng khỏe khoắn mùa hè"},
    {"id": "lex.en.200k.057584", "hw": "szechuans", "pos": "noun", "ipa": "/ˈsɛtʃwɑːnz/", "vi": "tỉnh Tứ Xuyên và ẩm thực Tứ Xuyên"},
    {"id": "lex.en.200k.057585", "hw": "taichis", "pos": "noun", "ipa": "/taɪˈtʃiːz/", "vi": "môn võ thái cực quyền dưỡng sinh"},
    {"id": "lex.en.200k.057586", "hw": "tailpipes", "pos": "noun", "ipa": "/ˈteɪlpaɪps/", "vi": "ống xả khói đuôi xe hơi cơ giới"},
    {"id": "lex.en.200k.057587", "hw": "terrapins", "pos": "noun", "ipa": "/ˈtɛrəpɪnz/", "vi": "loài rùa nước ngọt đầm lầy nhỏ"},
    {"id": "lex.en.200k.057588", "hw": "underlaid", "pos": "verb", "ipa": "/ˌʌndɚˈleɪd/", "vi": "đã lót phía dưới; đệm bên dưới"},
    {"id": "lex.en.200k.057589", "hw": "underlays", "pos": "noun", "ipa": "/ˈʌndɚleɪz/", "vi": "các lớp thảm lót đệm bên dưới"},
    {"id": "lex.en.200k.057590", "hw": "undershirts", "pos": "noun", "ipa": "/ˈʌndɚʃɜːrts/", "vi": "áo may ô lót bên trong nam giới"},
    {"id": "lex.en.200k.057591", "hw": "valis", "pos": "noun", "ipa": "/ˈvɑːliz/", "vi": "vị tổng đốc tỉnh thời Ottoman"},
    {"id": "lex.en.200k.057592", "hw": "vancomycins", "pos": "noun", "ipa": "/ˌvæŋkəˈmaɪsɪnz/", "vi": "thuốc kháng sinh mạnh vancomycin"},
    {"id": "lex.en.200k.057593", "hw": "velds", "pos": "noun", "ipa": "/vɛlts/", "vi": "thảo nguyên đồng cỏ ở Nam Phi"},
    {"id": "lex.en.200k.057594", "hw": "venerated", "pos": "verb", "ipa": "/ˈvɛnəreɪtɪd/", "vi": "đã sùng kính; đã tôn kính"},
    {"id": "lex.en.200k.057595", "hw": "venerates", "pos": "verb", "ipa": "/ˈvɛnəreɪts/", "vi": "tôn sùng; tôn kính kính cẩn"},
    {"id": "lex.en.200k.057596", "hw": "viols", "pos": "noun", "ipa": "/ˈvaɪəlz/", "vi": "các cây đàn viol nhiều dây cổ xưa"},
    {"id": "lex.en.200k.057597", "hw": "wigwams", "pos": "noun", "ipa": "/ˈwɪɡwɑːmz/", "vi": "túp lều vòm da thú của thổ dân"},
    {"id": "lex.en.200k.057598", "hw": "wroclaws", "pos": "noun", "ipa": "/ˈvrɔːtswɑːfz/", "vi": "thành phố cổ Wrocław ở Ba Lan"},
    {"id": "lex.en.200k.057599", "hw": "acute anterior poliomyelitis", "pos": "phrase", "ipa": "", "vi": "bệnh bại liệt cấp tính trẻ em"},
    {"id": "lex.en.200k.057600", "hw": "adsorbent material", "pos": "phrase", "ipa": "", "vi": "vật liệu chất hấp phụ bề mặt"},
    {"id": "lex.en.200k.057601", "hw": "amanita verna", "pos": "phrase", "ipa": "", "vi": "loài nấm độc tán xuân cực độc"}
]

# Validation
with open('scratch/b32_r06_raw_p1.json') as f:
    raw = json.load(f)

assert len(records) == 100, f"Expected 100 records, got {len(records)}"
for i, (r, raw_r) in enumerate(zip(records, raw)):
    assert r['id'] == raw_r['id'], f"Mismatch id at {i}: {r['id']} vs {raw_r['id']}"
    assert r['hw'] == raw_r['hw'], f"Mismatch hw at {i}: {r['hw']} vs {raw_r['hw']}"
    assert len(r['vi']) <= 35, f"Length violation at {i} ({r['hw']}): len={len(r['vi'])}: {r['vi']}"
    assert r['pos'] in ['noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'], f"Invalid pos at {i}: {r['pos']}"
    if ' ' not in r['hw']:
        assert r['ipa'].startswith('/') and r['ipa'].endswith('/') and r['ipa'].count('/') == 2, f"Invalid ipa at {i}: {r['ipa']}"

# Merge with raw
final_p1 = []
for r, raw_r in zip(records, raw):
    item = dict(raw_r)
    item['pos'] = r['pos']
    item['ipa'] = r['ipa']
    item['vi'] = r['vi']
    item['status'] = 'reviewed'
    final_p1.append(item)

with open('scratch/b32_r06_p1.json', 'w') as f:
    json.dump(final_p1, f, ensure_ascii=False, indent=2)
print("Part 1 validated and written successfully.")
