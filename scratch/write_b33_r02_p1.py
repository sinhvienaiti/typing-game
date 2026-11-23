import json

items = [
  {"id": "lex.en.200k.060503", "hw": "alcideses", "pos": "noun", "ipa": "/ælˈsaɪdiːzɪz/", "vi": "tên khác của anh hùng Hercules"},
  {"id": "lex.en.200k.060504", "hw": "allergists", "pos": "noun", "ipa": "/ˈælərdʒɪsts/", "vi": "bác sĩ chuyên khoa dị ứng"},
  {"id": "lex.en.200k.060505", "hw": "anthropoids", "pos": "noun", "ipa": "/ˈænθrəpɔɪdz/", "vi": "loài linh trưởng dạng vượn người"},
  {"id": "lex.en.200k.060506", "hw": "arcanums", "pos": "noun", "ipa": "/ɑːrˈkeɪnəmz/", "vi": "điều bí ẩn huyền bí; bí kíp"},
  {"id": "lex.en.200k.060507", "hw": "armagnacs", "pos": "noun", "ipa": "/ˈɑːrmənjæks/", "vi": "rượu mạnh brandy vùng Armagnac"},
  {"id": "lex.en.200k.060508", "hw": "backscattered", "pos": "verb", "ipa": "/ˈbækskætərd/", "vi": "đã tán xạ ngược bức xạ"},
  {"id": "lex.en.200k.060509", "hw": "backscatters", "pos": "verb", "ipa": "/ˈbækskætərz/", "vi": "tán xạ ngược sóng hoặc hạt"},
  {"id": "lex.en.200k.060510", "hw": "barbiturates", "pos": "noun", "ipa": "/bɑːrˈbɪtʃərəts/", "vi": "thuốc ngủ an thần barbiturat"},
  {"id": "lex.en.200k.060511", "hw": "barranquillas", "pos": "noun", "ipa": "/ˌbærəŋˈkiːjəz/", "vi": "thành phố cảng Barranquilla"},
  {"id": "lex.en.200k.060512", "hw": "beadworks", "pos": "noun", "ipa": "/ˈbiːdwɜːrks/", "vi": "đồ thủ công trang trí kết cườm"},
  {"id": "lex.en.200k.060513", "hw": "blowholes", "pos": "noun", "ipa": "/ˈbloʊhoʊlz/", "vi": "lỗ phun nước cá voi; lỗ thông hơi"},
  {"id": "lex.en.200k.060514", "hw": "borodins", "pos": "noun", "ipa": "/bɔːrəˈdiːnz/", "vi": "nhà soạn nhạc Nga Borodin"},
  {"id": "lex.en.200k.060515", "hw": "bougainvilleas", "pos": "noun", "ipa": "/ˌbuːɡənˈvɪliəz/", "vi": "dây leo hoa giấy rực rỡ"},
  {"id": "lex.en.200k.060516", "hw": "bourdons", "pos": "noun", "ipa": "/ˈbʊərdənz/", "vi": "ống âm trầm đàn đại phong cầm"},
  {"id": "lex.en.200k.060517", "hw": "bugandas", "pos": "noun", "ipa": "/buːˈɡændəz/", "vi": "vương quốc Buganda ở Uganda"},
  {"id": "lex.en.200k.060518", "hw": "bunions", "pos": "noun", "ipa": "/ˈbʌnjənz/", "vi": "chỗ sưng khớp ngón chân cái"},
  {"id": "lex.en.200k.060519", "hw": "businesspersons", "pos": "noun", "ipa": "/ˈbɪznəsˌpɜːrsənz/", "vi": "doanh nhân; người làm kinh doanh"},
  {"id": "lex.en.200k.060520", "hw": "campeches", "pos": "noun", "ipa": "/kæmˈpeɪtʃiz/", "vi": "bang thành phố Campeche Mexico"},
  {"id": "lex.en.200k.060521", "hw": "carobs", "pos": "noun", "ipa": "/ˈkærəbz/", "vi": "quả cây minh quyết carob ngọt"},
  {"id": "lex.en.200k.060522", "hw": "celebeses", "pos": "noun", "ipa": "/ˌsɛləˈbiːsɪz/", "vi": "đảo Sulawesi Celebes Indonesia"},
  {"id": "lex.en.200k.060523", "hw": "charioteers", "pos": "noun", "ipa": "/ˌtʃæriəˈtɪərz/", "vi": "người điều khiển xe ngựa chiến"},
  {"id": "lex.en.200k.060524", "hw": "chortled", "pos": "verb", "ipa": "/ˈtʃɔːrtld/", "vi": "đã cười khúc khích khoái chí"},
  {"id": "lex.en.200k.060525", "hw": "chortling", "pos": "verb", "ipa": "/ˈtʃɔːrtlɪŋ/", "vi": "đang cười khúc khích vui sướng"},
  {"id": "lex.en.200k.060526", "hw": "chukchis", "pos": "noun", "ipa": "/ˈtʃʊktʃiz/", "vi": "dân tộc Chukchi vùng viễn đông"},
  {"id": "lex.en.200k.060527", "hw": "cloches", "pos": "noun", "ipa": "/kloʊʃɪz/", "vi": "chụp thủy tinh che cây; mũ chuông"},
  {"id": "lex.en.200k.060528", "hw": "confectioners", "pos": "noun", "ipa": "/kənˈfɛkʃənərz/", "vi": "thợ làm bánh kẹo; chủ tiệm kẹo"},
  {"id": "lex.en.200k.060529", "hw": "creons", "pos": "noun", "ipa": "/ˈkriːɑːnz/", "vi": "vua Creon trong thần thoại Hy Lạp"},
  {"id": "lex.en.200k.060530", "hw": "demonetisations", "pos": "noun", "ipa": "/diːˌmɑːnɪtaɪˈzeɪʃənz/", "vi": "sự bãi bỏ giá trị lưu hành tiền"},
  {"id": "lex.en.200k.060531", "hw": "dictaphones", "pos": "noun", "ipa": "/ˈdɪktəfoʊnz/", "vi": "máy ghi âm đọc chính tả văn phòng"},
  {"id": "lex.en.200k.060532", "hw": "discotheques", "pos": "noun", "ipa": "/ˈdɪskətɛks/", "vi": "vũ trường hộp đêm nhảy disco"},
  {"id": "lex.en.200k.060533", "hw": "dynes", "pos": "noun", "ipa": "/daɪnz/", "vi": "đơn vị đo lực dyne trong vật lý"},
  {"id": "lex.en.200k.060534", "hw": "eiders", "pos": "noun", "ipa": "/ˈaɪdərz/", "vi": "vịt biển eider lấy lông làm đệm"},
  {"id": "lex.en.200k.060535", "hw": "emulsifiers", "pos": "noun", "ipa": "/ɪˈmʌlsɪfaɪərz/", "vi": "chất nhũ hóa làm mịn hỗn hợp"},
  {"id": "lex.en.200k.060536", "hw": "feelers", "pos": "noun", "ipa": "/ˈfiːlərz/", "vi": "râu xúc giác côn trùng; lời dò hỏi"},
  {"id": "lex.en.200k.060537", "hw": "felises", "pos": "noun", "ipa": "/ˈfiːlɪsɪz/", "vi": "chi mèo nhỏ thuộc họ Mèo Felis"},
  {"id": "lex.en.200k.060538", "hw": "firebombed", "pos": "verb", "ipa": "/ˈfaɪərbɑːmd/", "vi": "đã ném bom cháy; đánh bom xăng"},
  {"id": "lex.en.200k.060539", "hw": "firebombing", "pos": "verb", "ipa": "/ˈfaɪərbɑːmɪŋ/", "vi": "đang ném bom cháy thiêu rụi"},
  {"id": "lex.en.200k.060540", "hw": "firebombs", "pos": "noun", "ipa": "/ˈfaɪərbɑːmz/", "vi": "quả bom cháy; bom xăng tự chế"},
  {"id": "lex.en.200k.060541", "hw": "flories", "pos": "noun", "ipa": "/ˈflɔːriz/", "vi": "bác sĩ giải Nobel Howard Florey"},
  {"id": "lex.en.200k.060542", "hw": "foraminiferas", "pos": "noun", "ipa": "/fəˌræməˈnɪfərəz/", "vi": "động vật đơn bào trùng lỗ biển"},
  {"id": "lex.en.200k.060543", "hw": "functionalists", "pos": "noun", "ipa": "/ˈfʌŋkʃənəlɪsts/", "vi": "nhà nghiên cứu thuyết chức năng"},
  {"id": "lex.en.200k.060544", "hw": "gaudis", "pos": "noun", "ipa": "/ˈɡaʊdiz/", "vi": "kiến trúc sư tài hoa Antoni Gaudí"},
  {"id": "lex.en.200k.060545", "hw": "geophysicists", "pos": "noun", "ipa": "/ˌdʒiːoʊˈfɪzɪsɪsts/", "vi": "nhà địa vật lý nghiên cứu Trái Đất"},
  {"id": "lex.en.200k.060546", "hw": "gherkins", "pos": "noun", "ipa": "/ˈɡɜːrkɪnz/", "vi": "dưa chuột bao tử muối dưa chua"},
  {"id": "lex.en.200k.060547", "hw": "glaswegians", "pos": "noun", "ipa": "/ɡlæsˈwiːdʒənz/", "vi": "người dân thành phố Glasgow"},
  {"id": "lex.en.200k.060548", "hw": "grammarians", "pos": "noun", "ipa": "/ɡrəˈmɛriənz/", "vi": "nhà ngôn ngữ chuyên ngữ pháp"},
  {"id": "lex.en.200k.060549", "hw": "gushers", "pos": "noun", "ipa": "/ˈɡʌʃərz/", "vi": "giếng dầu phun trào; người bốc đồng"},
  {"id": "lex.en.200k.060550", "hw": "herdsmen", "pos": "noun", "ipa": "/ˈhɜːrdzmən/", "vi": "người chăn thả gia súc trên đồng"},
  {"id": "lex.en.200k.060551", "hw": "hestias", "pos": "noun", "ipa": "/ˈhɛstiəz/", "vi": "nữ thần bếp lửa Hestia Hy Lạp"},
  {"id": "lex.en.200k.060552", "hw": "immunohistochemistries", "pos": "noun", "ipa": "/ɪˌmjuːnoʊˌhɪstoʊˈkɛmɪstriz/", "vi": "kỹ thuật nhuộm hóa mô miễn dịch"},
  {"id": "lex.en.200k.060553", "hw": "indexers", "pos": "noun", "ipa": "/ˈɪndɛksərz/", "vi": "người lập bảng mục lục tra cứu"},
  {"id": "lex.en.200k.060554", "hw": "intrusted", "pos": "verb", "ipa": "/ɪnˈtrʌstɪd/", "vi": "đã giao phó; đã tin tưởng ủy thác"},
  {"id": "lex.en.200k.060555", "hw": "intrusting", "pos": "verb", "ipa": "/ɪnˈtrʌstɪŋ/", "vi": "đang giao phó trách nhiệm ủy thác"},
  {"id": "lex.en.200k.060556", "hw": "intrusts", "pos": "verb", "ipa": "/ɪnˈtrʌsts/", "vi": "giao phó nhiệm vụ; ủy thác tài sản"},
  {"id": "lex.en.200k.060557", "hw": "invitees", "pos": "noun", "ipa": "/ˌɪnvaɪˈtiːz/", "vi": "khách được mời tham dự sự kiện"},
  {"id": "lex.en.200k.060558", "hw": "jiggers", "pos": "noun", "ipa": "/ˈdʒɪɡərz/", "vi": "ly đong rượu pha chế; bọ chét cát"},
  {"id": "lex.en.200k.060559", "hw": "jirgas", "pos": "noun", "ipa": "/ˈdʒɪərɡəz/", "vi": "hội đồng bô lão truyền thống"},
  {"id": "lex.en.200k.060560", "hw": "jolsons", "pos": "noun", "ipa": "/ˈdʒoʊlsənz/", "vi": "ca sĩ diễn viên Mỹ Al Jolson"},
  {"id": "lex.en.200k.060561", "hw": "ketoacidoses", "pos": "noun", "ipa": "/ˌkiːtoʊˌæsɪˈdoʊsiːz/", "vi": "biến chứng nhiễm toan ceton máu"},
  {"id": "lex.en.200k.060562", "hw": "kines", "pos": "noun", "ipa": "/kaɪnz/", "vi": "đàn bò cái (từ cổ văn chương)"},
  {"id": "lex.en.200k.060563", "hw": "lancastrians", "pos": "noun", "ipa": "/læŋˈkæstriənz/", "vi": "người ủng hộ nhà Lancaster Anh"},
  {"id": "lex.en.200k.060564", "hw": "lapps", "pos": "noun", "ipa": "/læps/", "vi": "người dân tộc Sámi vùng Lapland"},
  {"id": "lex.en.200k.060565", "hw": "lavoisiers", "pos": "noun", "ipa": "/ləˈvwɑːzieɪz/", "vi": "nhà hóa học Antoine Lavoisier"},
  {"id": "lex.en.200k.060566", "hw": "lilliputs", "pos": "noun", "ipa": "/ˈlɪlɪpʌts/", "vi": "xứ sở người tí hon Lilliput"},
  {"id": "lex.en.200k.060567", "hw": "lotharios", "pos": "noun", "ipa": "/loʊˈθɛrioʊz/", "vi": "gã đào hoa sở khanh trăng hoa"},
  {"id": "lex.en.200k.060568", "hw": "manzonis", "pos": "noun", "ipa": "/mɑːnˈzoʊniz/", "vi": "nhà văn Ý Alessandro Manzoni"},
  {"id": "lex.en.200k.060569", "hw": "mexicanos", "pos": "noun", "ipa": "/ˌmɛksɪˈkɑːnoʊz/", "vi": "người dân gốc Mexico Tây Ban Nha"},
  {"id": "lex.en.200k.060570", "hw": "niebuhrs", "pos": "noun", "ipa": "/ˈniːbʊərz/", "vi": "nhà thần học Reinhold Niebuhr"},
  {"id": "lex.en.200k.060571", "hw": "novenae", "pos": "noun", "ipa": "/noʊˈviːniː/", "vi": "chuỗi tuần cửu nhật cầu nguyện"},
  {"id": "lex.en.200k.060572", "hw": "novenas", "pos": "noun", "ipa": "/noʊˈviːnəz/", "vi": "kinh cầu nguyện chín ngày Công giáo"},
  {"id": "lex.en.200k.060573", "hw": "osteosarcomas", "pos": "noun", "ipa": "/ˌɑːstioʊsɑːrˈkoʊməz/", "vi": "bệnh ung thư u xương ác tính"},
  {"id": "lex.en.200k.060574", "hw": "overachievers", "pos": "noun", "ipa": "/ˌoʊvərəˈtʃiːvərz/", "vi": "người đạt thành tích xuất sắc"},
  {"id": "lex.en.200k.060575", "hw": "overbites", "pos": "noun", "ipa": "/ˈoʊvərbaɪts/", "vi": "tật khớp cắn sâu hàm trên nhô"},
  {"id": "lex.en.200k.060576", "hw": "palaeontologists", "pos": "noun", "ipa": "/ˌpeɪliənˈtɑːlədʒɪsts/", "vi": "nhà cổ sinh vật học hóa thạch"},
  {"id": "lex.en.200k.060577", "hw": "panopticons", "pos": "noun", "ipa": "/pæˈnɑːptɪkɑːnz/", "vi": "nhà tù tròn giám sát toàn cảnh"},
  {"id": "lex.en.200k.060578", "hw": "paparazzi", "pos": "noun", "ipa": "/ˌpɑːpəˈrɑːtsi/", "vi": "cánh thợ săn ảnh người nổi tiếng"},
  {"id": "lex.en.200k.060579", "hw": "phots", "pos": "noun", "ipa": "/fɑːts/", "vi": "đơn vị đo độ rọi ánh sáng phot"},
  {"id": "lex.en.200k.060580", "hw": "pibs", "pos": "noun", "ipa": "/pɪbz/", "vi": "đơn vị tin học pebibyte; byte"},
  {"id": "lex.en.200k.060581", "hw": "pinafores", "pos": "noun", "ipa": "/ˈpɪnəfɔːrz/", "vi": "váy yếm bé gái; tạp dề có quai"},
  {"id": "lex.en.200k.060582", "hw": "plunked", "pos": "verb", "ipa": "/plʌŋkt/", "vi": "đã thả rơi tõm; gảy đàn vang"},
  {"id": "lex.en.200k.060583", "hw": "plunking", "pos": "verb", "ipa": "/ˈplʌŋkɪŋ/", "vi": "đang thả rơi tõm; gảy dây đàn"},
  {"id": "lex.en.200k.060584", "hw": "plunks", "pos": "noun", "ipa": "/plʌŋks/", "vi": "tiếng rơi tõm; tiếng gảy dây đàn"},
  {"id": "lex.en.200k.060585", "hw": "preconceptions", "pos": "noun", "ipa": "/ˌpriːkənˈsɛpʃənz/", "vi": "định kiến sẵn có; thành kiến trước"},
  {"id": "lex.en.200k.060586", "hw": "printmakers", "pos": "noun", "ipa": "/ˈprɪntmeɪkərz/", "vi": "nghệ sĩ làm tranh khắc in ấn"},
  {"id": "lex.en.200k.060587", "hw": "purkinjes", "pos": "noun", "ipa": "/ˈpɜːrkɪndʒiz/", "vi": "nhà sinh lý học Jan Purkinje"},
  {"id": "lex.en.200k.060588", "hw": "recurves", "pos": "verb", "ipa": "/rɪˈkɜːrvz/", "vi": "uốn cong ngược về phía sau"},
  {"id": "lex.en.200k.060589", "hw": "recurving", "pos": "verb", "ipa": "/rɪˈkɜːrvɪŋ/", "vi": "đang uốn cong ngược trở lại"},
  {"id": "lex.en.200k.060590", "hw": "remediated", "pos": "verb", "ipa": "/rɪˈmiːdieɪtɪd/", "vi": "đã khắc phục sửa chữa môi trường"},
  {"id": "lex.en.200k.060591", "hw": "remediates", "pos": "verb", "ipa": "/rɪˈmiːdieɪts/", "vi": "khắc phục sửa chữa; cải tạo đất"},
  {"id": "lex.en.200k.060592", "hw": "remediating", "pos": "verb", "ipa": "/rɪˈmiːdieɪtɪŋ/", "vi": "đang khắc phục xử lý khắc phục"},
  {"id": "lex.en.200k.060593", "hw": "resedas", "pos": "noun", "ipa": "/rɪˈsiːdəz/", "vi": "hoa mộc tê thơm màu vàng nhạt"},
  {"id": "lex.en.200k.060594", "hw": "rogaines", "pos": "noun", "ipa": "/ˈroʊɡeɪnz/", "vi": "thuốc bôi mọc tóc Rogaine"},
  {"id": "lex.en.200k.060595", "hw": "rydbergs", "pos": "noun", "ipa": "/ˈrɪdbɜːrɡz/", "vi": "đơn vị năng lượng hằng số Rydberg"},
  {"id": "lex.en.200k.060596", "hw": "safars", "pos": "noun", "ipa": "/ˈsʌfərz/", "vi": "tháng thứ hai lịch Hồi giáo Safar"},
  {"id": "lex.en.200k.060597", "hw": "sandlots", "pos": "noun", "ipa": "/ˈsændlɑːts/", "vi": "bãi đất cát trống cho trẻ chơi"},
  {"id": "lex.en.200k.060598", "hw": "sarsaparillas", "pos": "noun", "ipa": "/ˌsærsəpəˈrɪləz/", "vi": "cây thổ phục linh làm đồ uống"},
  {"id": "lex.en.200k.060599", "hw": "schiaparellis", "pos": "noun", "ipa": "/ˌskjɑːpəˈrɛliz/", "vi": "nhà thiên văn học Schiaparelli Ý"},
  {"id": "lex.en.200k.060600", "hw": "seductresses", "pos": "noun", "ipa": "/sɪˈdʌktrəsɪz/", "vi": "người đàn bà quyến rũ mê hoặc"},
  {"id": "lex.en.200k.060601", "hw": "senhors", "pos": "noun", "ipa": "/sɛnˈjɔːrz/", "vi": "tước hiệu quý ông Bồ Đào Nha"},
  {"id": "lex.en.200k.060602", "hw": "siltier", "pos": "adj", "ipa": "/ˈsɪltiər/", "vi": "nhiều phù sa bùn cát lắng hơn"}
]

with open('scratch/b33_r02_raw_p1.json') as f:
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

with open('scratch/b33_r02_p1.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

print("Batch 33 Round 2 Part 1 validated and written successfully.")
