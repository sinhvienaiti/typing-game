import json

items = [
  {"id": "lex.en.200k.063003", "hw": "polymorphs", "pos": "noun", "ipa": "/ˈpɑːlɪmɔːrfs/", "vi": "dạng đa hình; tinh thể đa hình"},
  {"id": "lex.en.200k.063004", "hw": "proscriptions", "pos": "noun", "ipa": "/proʊˈskrɪpʃənz/", "vi": "lệnh cấm đoán; sự lưu đày tịch thu"},
  {"id": "lex.en.200k.063005", "hw": "pufferfishes", "pos": "noun", "ipa": "/ˈpʌfərfɪʃɪz/", "vi": "cá nóc phồng thân có độc tố"},
  {"id": "lex.en.200k.063006", "hw": "radiographs", "pos": "noun", "ipa": "/ˈreɪdiəˌɡræfs/", "vi": "ảnh chụp X-quang y tế; máy X-quang"},
  {"id": "lex.en.200k.063007", "hw": "redrafts", "pos": "noun", "ipa": "/riːˈdræfts/", "vi": "bản thảo mới; hối phiếu tái lập"},
  {"id": "lex.en.200k.063008", "hw": "reproofed", "pos": "verb", "ipa": "/rɪˈpruːft/", "vi": "đã quở trách; đã khiển trách nhẹ"},
  {"id": "lex.en.200k.063009", "hw": "reproofing", "pos": "verb", "ipa": "/rɪˈpruːfɪŋ/", "vi": "đang quở trách; đang khiển trách"},
  {"id": "lex.en.200k.063010", "hw": "reproofs", "pos": "noun", "ipa": "/rɪˈpruːfs/", "vi": "lời quở trách; sự khiển trách"},
  {"id": "lex.en.200k.063011", "hw": "ruiners", "pos": "noun", "ipa": "/ˈruːənərz/", "vi": "kẻ phá hoại; kẻ hủy hoại sự nghiệp"},
  {"id": "lex.en.200k.063012", "hw": "shantytowns", "pos": "noun", "ipa": "/ˈʃæntitaʊnz/", "vi": "khu nhà ổ chuột dựng bằng ván tôn"},
  {"id": "lex.en.200k.063013", "hw": "shapleys", "pos": "noun", "ipa": "/ˈʃæpliz/", "vi": "nhà thiên văn học Mỹ Harlow Shapley"},
  {"id": "lex.en.200k.063014", "hw": "shigellas", "pos": "noun", "ipa": "/ʃɪˈɡɛləz/", "vi": "vi khuẩn Shigella gây bệnh kiết lỵ"},
  {"id": "lex.en.200k.063015", "hw": "simvastatins", "pos": "noun", "ipa": "/ˌsɪmvəˈstætɪnz/", "vi": "thuốc hạ mỡ máu simvastatin"},
  {"id": "lex.en.200k.063016", "hw": "singsonged", "pos": "verb", "ipa": "/ˈsɪŋsɔːŋd/", "vi": "đã nói hay ngâm nga giọng đều đều"},
  {"id": "lex.en.200k.063017", "hw": "singsonging", "pos": "verb", "ipa": "/ˈsɪŋsɔːŋɪŋ/", "vi": "đang nói đọc đều đều lên xuống"},
  {"id": "lex.en.200k.063018", "hw": "singsongs", "pos": "noun", "ipa": "/ˈsɪŋsɔːŋz/", "vi": "giọng nói đều đều; buổi hát vui"},
  {"id": "lex.en.200k.063019", "hw": "sothos", "pos": "noun", "ipa": "/ˈsuːtuːz/", "vi": "người và ngôn ngữ Sotho Nam Phi"},
  {"id": "lex.en.200k.063020", "hw": "spodes", "pos": "noun", "ipa": "/spoʊdz/", "vi": "đồ gốm sứ cao cấp Spode của Anh"},
  {"id": "lex.en.200k.063021", "hw": "sprats", "pos": "noun", "ipa": "/spræts/", "vi": "cá trích nhỏ biển Bắc châu Âu"},
  {"id": "lex.en.200k.063022", "hw": "sunshades", "pos": "noun", "ipa": "/ˈsʌnʃeɪdz/", "vi": "dù che nắng; mành rèm chắn nắng"},
  {"id": "lex.en.200k.063023", "hw": "theophrastuses", "pos": "noun", "ipa": "/ˌθiːəˈfræstəsɪz/", "vi": "triết gia Hy Lạp Theophrastus"},
  {"id": "lex.en.200k.063024", "hw": "thymidines", "pos": "noun", "ipa": "/ˈθaɪmədiːnz/", "vi": "nucleoside cấu tạo ADN thymidine"},
  {"id": "lex.en.200k.063025", "hw": "toadstools", "pos": "noun", "ipa": "/ˈtoʊdstuːlz/", "vi": "nấm tán mũ độc không ăn được"},
  {"id": "lex.en.200k.063026", "hw": "tolus", "pos": "noun", "ipa": "/ˈtoʊluːz/", "vi": "nhựa thơm cây tolu dùng trong dược"},
  {"id": "lex.en.200k.063027", "hw": "tragi", "pos": "noun", "ipa": "/ˈtreɪdʒaɪ/", "vi": "nắp bình tai ngoài; lông lỗ tai"},
  {"id": "lex.en.200k.063028", "hw": "traguses", "pos": "noun", "ipa": "/ˈtreɪɡəsɪz/", "vi": "các nắp gờ sụn trước lỗ tai ngoài"},
  {"id": "lex.en.200k.063029", "hw": "uvulas", "pos": "noun", "ipa": "/ˈjuːvjələz/", "vi": "lưỡi gà treo ở cuối vòm miệng"},
  {"id": "lex.en.200k.063030", "hw": "verrazanos", "pos": "noun", "ipa": "/ˌvɛrəˈzɑːnoʊz/", "vi": "nhà thám hiểm Giovanni Verrazzano"},
  {"id": "lex.en.200k.063031", "hw": "vexations", "pos": "noun", "ipa": "/vɛkˈseɪʃənz/", "vi": "nỗi bực mình; điều phiền toái"},
  {"id": "lex.en.200k.063032", "hw": "violists", "pos": "noun", "ipa": "/vaɪˈoʊlɪsts/", "vi": "nghệ sĩ biểu diễn đàn vĩ cầm trung"},
  {"id": "lex.en.200k.063033", "hw": "visualizers", "pos": "noun", "ipa": "/ˈvɪʒuəˌlaɪzərz/", "vi": "người hình dung; phần mềm mô phỏng"},
  {"id": "lex.en.200k.063034", "hw": "waterspouts", "pos": "noun", "ipa": "/ˈwɔːtərspaʊts/", "vi": "vòi rồng trên biển; ống thoát mái"},
  {"id": "lex.en.200k.063035", "hw": "adonis annua", "pos": "phrase", "ipa": "/əˈdɑːnɪs ˈænjuə/", "vi": "hoa mắt chim đỏ thắm Adonis annua"},
  {"id": "lex.en.200k.063036", "hw": "amerigo vespucci", "pos": "phrase", "ipa": "/ˌæməˈriːɡoʊ vɛˈspuːtʃi/", "vi": "nhà thám hiểm Amerigo Vespucci"},
  {"id": "lex.en.200k.063037", "hw": "ammonium carbamate", "pos": "phrase", "ipa": "/əˈmoʊniəm ˈkɑːrbəˌmeɪt/", "vi": "muối amoni cacbamat tổng hợp urê"},
  {"id": "lex.en.200k.063038", "hw": "australian lungfish", "pos": "phrase", "ipa": "/ɔːˈstreɪliən ˈlʌŋfɪʃ/", "vi": "cá phổi nước ngọt cổ đại của Úc"},
  {"id": "lex.en.200k.063039", "hw": "battle of crecy", "pos": "phrase", "ipa": "/ˈbætəl əv ˈkrɛsi/", "vi": "trận chiến Crécy năm 1346 ở Pháp"},
  {"id": "lex.en.200k.063040", "hw": "brigit nilsson", "pos": "phrase", "ipa": "/ˈbɪrɡɪt ˈnɪlsən/", "vi": "nữ ca sĩ opera Thụy Điển Nilsson"},
  {"id": "lex.en.200k.063041", "hw": "bufo marinus", "pos": "phrase", "ipa": "/ˈbjuːfoʊ məˈriːnəs/", "vi": "cóc mía khổng lồ có tuyến độc"},
  {"id": "lex.en.200k.063042", "hw": "citrus whitefly", "pos": "phrase", "ipa": "/ˈsɪtrəs ˈwaɪtflaɪ/", "vi": "bọ phấn trắng hại cây cam quýt"},
  {"id": "lex.en.200k.063043", "hw": "corvus corax", "pos": "phrase", "ipa": "/ˈkɔːrvəs ˈkɔːræks/", "vi": "loài quạ đen lớn Corvus corax"},
  {"id": "lex.en.200k.063044", "hw": "cycladic civilization", "pos": "phrase", "ipa": "/saɪˈklædɪk ˌsɪvələˈzeɪʃən/", "vi": "nền văn minh Cyclades thời Đồ Đồng"},
  {"id": "lex.en.200k.063045", "hw": "cycladic culture", "pos": "phrase", "ipa": "/saɪˈklædɪk ˈkʌltʃər/", "vi": "nền văn hóa cổ quần đảo Cyclades"},
  {"id": "lex.en.200k.063046", "hw": "docosahexaenoic acid", "pos": "phrase", "ipa": "/doʊˌkoʊsəˌhɛksəɪˈnoʊɪk ˈæsɪd/", "vi": "axit béo thiết yếu omega-3 DHA"},
  {"id": "lex.en.200k.063047", "hw": "eleuthera bark", "pos": "phrase", "ipa": "/ɪˈluːθərə bɑːrk/", "vi": "vỏ cây thơm cascarilla vùng Caribê"},
  {"id": "lex.en.200k.063048", "hw": "epidemic myalgia", "pos": "phrase", "ipa": "/ˌɛpɪˈdɛmɪk maɪˈældʒə/", "vi": "bệnh đau cơ thành dịch Bornholm"},
  {"id": "lex.en.200k.063049", "hw": "formica fusca", "pos": "phrase", "ipa": "/ˈfɔːrmɪkə ˈfʌskə/", "vi": "kiến đen mịn Bắc Bán Cầu Formica"},
  {"id": "lex.en.200k.063050", "hw": "genus hosta", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈhɑːstə/", "vi": "chi cây cảnh lá lớn hoa loa Hosta"},
  {"id": "lex.en.200k.063051", "hw": "genus juglans", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈdʒuːɡlænz/", "vi": "chi cây óc chó thân gỗ Juglans"},
  {"id": "lex.en.200k.063052", "hw": "genus philodendron", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˌfɪləˈdɛndrən/", "vi": "chi cây trầu bà lá xẻ Philodendron"},
  {"id": "lex.en.200k.063053", "hw": "genus thuja", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈθuːdʒə/", "vi": "chi cây trắc bách diệp thơm Thuja"},
  {"id": "lex.en.200k.063054", "hw": "george dibdin pitt", "pos": "phrase", "ipa": "/dʒɔːrdʒ ˈdɪbdɪn pɪt/", "vi": "nhà viết kịch Anh George Pitt"},
  {"id": "lex.en.200k.063055", "hw": "greater scaup", "pos": "phrase", "ipa": "/ˈɡreɪtər skɔːp/", "vi": "vịt biển lặn lớn đầu sẫm ánh xanh"},
  {"id": "lex.en.200k.063056", "hw": "hypoplastic anemia", "pos": "phrase", "ipa": "/ˌhaɪpəˈplæstɪk əˈniːmiə/", "vi": "thiếu máu giảm sản sinh tế bào tủy"},
  {"id": "lex.en.200k.063057", "hw": "hypovolemic shock", "pos": "phrase", "ipa": "/ˌhaɪpoʊvɑːˈliːmɪk ʃɑːk/", "vi": "sốc giảm thể tích máu tuần hoàn"},
  {"id": "lex.en.200k.063058", "hw": "intradermal injection", "pos": "phrase", "ipa": "/ˌɪntrəˈdɜːrməl ɪnˈdʒɛkʃən/", "vi": "mũi tiêm nông vào trong lớp bì da"},
  {"id": "lex.en.200k.063059", "hw": "intradermal test", "pos": "phrase", "ipa": "/ˌɪntrəˈdɜːrməl tɛst/", "vi": "xét nghiệm dị ứng tiêm trong da"},
  {"id": "lex.en.200k.063060", "hw": "iris virginica", "pos": "phrase", "ipa": "/ˈaɪrɪs vərˈdʒɪnɪkə/", "vi": "hoa diên vĩ tím xanh Virginia"},
  {"id": "lex.en.200k.063061", "hw": "james mckeen cattell", "pos": "phrase", "ipa": "/dʒeɪmz məˈkiːn kəˈtɛl/", "vi": "nhà tâm lý học Mỹ James Cattell"},
  {"id": "lex.en.200k.063062", "hw": "john bardeen", "pos": "phrase", "ipa": "/dʒɑːn bɑːrˈdiːn/", "vi": "nhà vật lý hai giải Nobel Bardeen"},
  {"id": "lex.en.200k.063063", "hw": "lesser scaup", "pos": "phrase", "ipa": "/ˈlɛsər skɔːp/", "vi": "vịt lặn đầu ánh tím nhỏ Bắc Mỹ"},
  {"id": "lex.en.200k.063064", "hw": "lesser scaup duck", "pos": "phrase", "ipa": "/ˈlɛsər skɔːp dʌk/", "vi": "loài vịt biển lặn đầu tím Bắc Mỹ"},
  {"id": "lex.en.200k.063065", "hw": "pantothenic acid", "pos": "phrase", "ipa": "/ˌpæntəˈθɛnɪk ˈæsɪd/", "vi": "vitamin B5 axit pantothenic"},
  {"id": "lex.en.200k.063066", "hw": "pilotless aircraft", "pos": "phrase", "ipa": "/ˈpaɪlətləs ˈɛərkræft/", "vi": "máy bay điều khiển không người lái"},
  {"id": "lex.en.200k.063067", "hw": "pyloric sphincter", "pos": "phrase", "ipa": "/paɪˈlɔːrɪk ˈsfɪŋktər/", "vi": "cơ vòng thắt mở môn vị dạ dày"},
  {"id": "lex.en.200k.063068", "hw": "pyloric stenosis", "pos": "phrase", "ipa": "/paɪˈlɔːrɪk stəˈnoʊsɪs/", "vi": "bệnh hẹp môn vị đường ra dạ dày"},
  {"id": "lex.en.200k.063069", "hw": "queensland lungfish", "pos": "phrase", "ipa": "/ˈkwiːnzlənd ˈlʌŋfɪʃ/", "vi": "cá phổi vùng Queensland của Úc"},
  {"id": "lex.en.200k.063070", "hw": "raffia vinifera", "pos": "phrase", "ipa": "/ˈræfiə vəˈnɪfərə/", "vi": "cây cọ sợi dệt Tây Phi Raffia"},
  {"id": "lex.en.200k.063071", "hw": "rangpur lime", "pos": "phrase", "ipa": "/ˈræŋpʊr laɪm/", "vi": "quả chanh vỏ cam chua Rangpur"},
  {"id": "lex.en.200k.063072", "hw": "scarlet fritillary", "pos": "phrase", "ipa": "/ˈskɑːrlɪt ˈfrɪtəˌlɛri/", "vi": "cây hoa chuông đỏ thắm California"},
  {"id": "lex.en.200k.063073", "hw": "scaup duck", "pos": "phrase", "ipa": "/skɔːp dʌk/", "vi": "vịt biển lặn mỏ xanh xám họ Vịt"},
  {"id": "lex.en.200k.063074", "hw": "severo ochoa", "pos": "phrase", "ipa": "/səˈvɛroʊ oʊˈtʃoʊə/", "vi": "nhà hóa sinh Nobel Severo Ochoa"},
  {"id": "lex.en.200k.063075", "hw": "south american staghorn", "pos": "phrase", "ipa": "/saʊθ əˈmɛrɪkən ˈstæɡhɔːrn/", "vi": "dương xỉ lá sừng hươu Nam Mỹ"},
  {"id": "lex.en.200k.063076", "hw": "staghorn coral", "pos": "phrase", "ipa": "/ˈstæɡhɔːrn ˈkɔːrəl/", "vi": "san hô nhánh giống gạc hươu rạn đá"},
  {"id": "lex.en.200k.063077", "hw": "staghorn moss", "pos": "phrase", "ipa": "/ˈstæɡhɔːrn mɔːs/", "vi": "cây thông đất thân bò hình gạc nai"},
  {"id": "lex.en.200k.063078", "hw": "status epilepticus", "pos": "phrase", "ipa": "/ˈsteɪtəs ˌɛpəˈlɛptɪkəs/", "vi": "cơn động kinh kéo dài nguy kịch"},
  {"id": "lex.en.200k.063079", "hw": "stemless daisy", "pos": "phrase", "ipa": "/ˈstɛmləs ˈdeɪzi/", "vi": "cây cúc lùn không thân hoa trắng"},
  {"id": "lex.en.200k.063080", "hw": "stemless golden weed", "pos": "phrase", "ipa": "/ˈstɛmləs ˈɡoʊldən wiːd/", "vi": "cỏ hoa vàng không thân vùng núi Mỹ"},
  {"id": "lex.en.200k.063081", "hw": "szechwan province", "pos": "phrase", "ipa": "/ˈsɛtʃwɑːn ˈprɑːvɪns/", "vi": "tỉnh Tứ Xuyên tây nam Trung Quốc"},
  {"id": "lex.en.200k.063082", "hw": "tombigbee river", "pos": "phrase", "ipa": "/tɑːmˈbɪɡbi ˈrɪvər/", "vi": "sông Tombigbee miền nam Hoa Kỳ"},
  {"id": "lex.en.200k.063083", "hw": "tuberculin skin test", "pos": "phrase", "ipa": "/tuːˈbɜːrkjəlɪn skɪn tɛst/", "vi": "xét nghiệm da tiêm lao tố Mantoux"},
  {"id": "lex.en.200k.063084", "hw": "tuberculin test", "pos": "phrase", "ipa": "/tuːˈbɜːrkjəlɪn tɛst/", "vi": "xét nghiệm sàng lọc vi khuẩn lao"},
  {"id": "lex.en.200k.063085", "hw": "twyla tharp", "pos": "phrase", "ipa": "/ˈtwaɪlə θɑːrp/", "vi": "biên đạo múa hiện đại Twyla Tharp"},
  {"id": "lex.en.200k.063086", "hw": "uranyl oxalate", "pos": "phrase", "ipa": "/ˈjʊrənɪl ˈɑːksəˌleɪt/", "vi": "hợp chất uranyl oxalat đo quang"},
  {"id": "lex.en.200k.063087", "hw": "veal parmigiana", "pos": "phrase", "ipa": "/viːl ˌpɑːrmɪˈdʒɑːnə/", "vi": "món thịt bê chiên phô mai sốt cà"},
  {"id": "lex.en.200k.063088", "hw": "vigna caracalla", "pos": "phrase", "ipa": "/ˈvɪɡnə ˌkærəˈkælə/", "vi": "dây leo đậu hoa xoắn ốc thơm ngát"},
  {"id": "lex.en.200k.063089", "hw": "vyacheslav mikhailovich molotov", "pos": "phrase", "ipa": "/vjɑːtʃɪˈslɑːf ˈmɔːlətɔːf/", "vi": "ngoại trưởng Xô Viết Molotov"},
  {"id": "lex.en.200k.063090", "hw": "algeries", "pos": "noun", "ipa": "/ˈældʒəriz/", "vi": "quốc gia Bắc Phi Algeria (tên cũ)"},
  {"id": "lex.en.200k.063091", "hw": "angioedemas", "pos": "noun", "ipa": "/ˌændʒioʊɪˈdiːməz/", "vi": "chứng phù mạch sưng dưới da dị ứng"},
  {"id": "lex.en.200k.063092", "hw": "angstroms", "pos": "noun", "ipa": "/ˈæŋstrəmz/", "vi": "đơn vị độ dài cực nhỏ angstrom"},
  {"id": "lex.en.200k.063093", "hw": "apollinaires", "pos": "noun", "ipa": "/əˌpɑːlɪˈnɛərz/", "vi": "nhà thơ tiên phong Pháp Apollinaire"},
  {"id": "lex.en.200k.063094", "hw": "aspinwalls", "pos": "noun", "ipa": "/ˈæspɪnwɔːlz/", "vi": "thành phố cảng Aspinwall (Colón)"},
  {"id": "lex.en.200k.063095", "hw": "backflows", "pos": "noun", "ipa": "/ˈbækfloʊz/", "vi": "dòng nước thải chảy trào ngược lại"},
  {"id": "lex.en.200k.063096", "hw": "backplates", "pos": "noun", "ipa": "/ˈbækpleɪts/", "vi": "tấm ốp bảo vệ mặt sau bo mạch giáp"},
  {"id": "lex.en.200k.063097", "hw": "backslid", "pos": "verb", "ipa": "/ˈbækslɪd/", "vi": "đã sa sút đạo đức; đã tái nghiện"},
  {"id": "lex.en.200k.063098", "hw": "backslidden", "pos": "verb", "ipa": "/ˈbækˌslɪdən/", "vi": "đã sa sút thoái hóa; đã bỏ đạo cũ"},
  {"id": "lex.en.200k.063099", "hw": "backslides", "pos": "verb", "ipa": "/ˈbækslaɪdz/", "vi": "sa sút trở lại thói xấu; tái phạm"},
  {"id": "lex.en.200k.063100", "hw": "baldricks", "pos": "noun", "ipa": "/ˈbɔːldrɪks/", "vi": "dây đeo chéo vai giữ kiếm hay kèn"},
  {"id": "lex.en.200k.063101", "hw": "beneficiations", "pos": "noun", "ipa": "/ˌbɛnɪfɪʃiˈeɪʃənz/", "vi": "quá trình tuyển tách làm giàu quặng"},
  {"id": "lex.en.200k.063102", "hw": "bidas", "pos": "noun", "ipa": "/ˈbiːdəz/", "vi": "thủ đô Doha Qatar (tên cũ Bida)"}
]

with open('scratch/b33_r07_raw_p1.json') as f:
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

with open('scratch/b33_r07_p1.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)
print("Saved scratch/b33_r07_p1.json OK")
