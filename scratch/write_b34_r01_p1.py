import json

items = [
  {"id": "lex.en.200k.065003", "hw": "sickbeds", "pos": "noun", "ipa": "/ˈsɪkbɛdz/", "vi": "giường nằm của người bệnh ốm yếu"},
  {"id": "lex.en.200k.065004", "hw": "silexes", "pos": "noun", "ipa": "/ˈsaɪlɛksɪz/", "vi": "đá lửa thạch anh bột silic mịn"},
  {"id": "lex.en.200k.065005", "hw": "squirters", "pos": "noun", "ipa": "/ˈskwɜːrtərz/", "vi": "súng phun nước; vòi phun tia nước"},
  {"id": "lex.en.200k.065006", "hw": "stabiles", "pos": "noun", "ipa": "/ˈstæbiːlz/", "vi": "tác phẩm điêu khắc trừu tượng tĩnh"},
  {"id": "lex.en.200k.065007", "hw": "substrings", "pos": "noun", "ipa": "/ˈsʌbstrɪŋz/", "vi": "chuỗi ký tự con trích từ chuỗi gốc"},
  {"id": "lex.en.200k.065008", "hw": "sugarplums", "pos": "noun", "ipa": "/ˈʃʊɡərˌplʌmz/", "vi": "kẹo đường nhỏ tròn; món ngọt hảo"},
  {"id": "lex.en.200k.065009", "hw": "sugis", "pos": "noun", "ipa": "/ˈsuːɡiz/", "vi": "cây liễu sam tuyết tùng Nhật Bản"},
  {"id": "lex.en.200k.065010", "hw": "surplices", "pos": "noun", "ipa": "/ˈsɜːrpləsɪz/", "vi": "áo lễ trắng rộng tay của giáo sĩ"},
  {"id": "lex.en.200k.065011", "hw": "suzerains", "pos": "noun", "ipa": "/ˈsuːzərənz/", "vi": "nước tông chủ; lãnh chúa tối cao"},
  {"id": "lex.en.200k.065012", "hw": "temujins", "pos": "noun", "ipa": "/ˈtɛmuːdʒɪnz/", "vi": "tên khai sinh của Thành Cát Tư Hãn"},
  {"id": "lex.en.200k.065013", "hw": "toltecs", "pos": "noun", "ipa": "/ˈtɑːltɛks/", "vi": "người và nền văn minh cổ Toltec"},
  {"id": "lex.en.200k.065014", "hw": "torricellis", "pos": "noun", "ipa": "/ˌtɔːrɪˈtʃɛliz/", "vi": "nhà vật lý Ý Torricelli đo áp suất"},
  {"id": "lex.en.200k.065015", "hw": "transgressors", "pos": "noun", "ipa": "/trænzˈɡrɛsərz/", "vi": "kẻ phạm pháp vi phạm luật đạo đức"},
  {"id": "lex.en.200k.065016", "hw": "transposons", "pos": "noun", "ipa": "/trænzˈpoʊzɑːnz/", "vi": "đoạn gen nhảy di chuyển trên ADN"},
  {"id": "lex.en.200k.065017", "hw": "trimers", "pos": "noun", "ipa": "/ˈtraɪmərz/", "vi": "phân tử tam hợp kết hợp ba đơn vị"},
  {"id": "lex.en.200k.065018", "hw": "tyrannuses", "pos": "noun", "ipa": "/tɪˈrænəsɪz/", "vi": "chi chim đớp ruồi bạo chúa Tyrannus"},
  {"id": "lex.en.200k.065019", "hw": "ungulates", "pos": "noun", "ipa": "/ˈʌŋɡjəlɪts/", "vi": "động vật có vú có móng guốc ăn cỏ"},
  {"id": "lex.en.200k.065020", "hw": "unmakes", "pos": "verb", "ipa": "/ʌnˈmeɪks/", "vi": "tháo dỡ hủy bỏ cấu trúc đã tạo"},
  {"id": "lex.en.200k.065021", "hw": "unmaking", "pos": "verb", "ipa": "/ʌnˈmeɪkɪŋ/", "vi": "đang phá hủy xóa bỏ làm sụp đổ"},
  {"id": "lex.en.200k.065022", "hw": "valses", "pos": "noun", "ipa": "/vɑːlsɪz/", "vi": "điệu khiêu vũ nhạc van-xơ nhịp ba"},
  {"id": "lex.en.200k.065023", "hw": "vidars", "pos": "noun", "ipa": "/ˈviːdɑːrz/", "vi": "thần báo thù thầm lặng Bắc Âu"},
  {"id": "lex.en.200k.065024", "hw": "washbasins", "pos": "noun", "ipa": "/ˈwɑːʃˌbeɪsənz/", "vi": "bồn chậu rửa mặt gắn vòi nước"},
  {"id": "lex.en.200k.065025", "hw": "watusis", "pos": "noun", "ipa": "/wɑːˈtuːsiz/", "vi": "người Tutsi và giống bò sừng dài"},
  {"id": "lex.en.200k.065026", "hw": "whackers", "pos": "noun", "ipa": "/ˈwækərz/", "vi": "vật to lớn khác thường; người đập"},
  {"id": "lex.en.200k.065027", "hw": "whomped", "pos": "verb", "ipa": "/wɑːmpt/", "vi": "đã đánh bại áp đảo; đã vỗ mạnh"},
  {"id": "lex.en.200k.065028", "hw": "whomping", "pos": "verb", "ipa": "/ˈwɑːmpɪŋ/", "vi": "đang đập mạnh; đánh bại áp đảo"},
  {"id": "lex.en.200k.065029", "hw": "whomps", "pos": "verb", "ipa": "/wɑːmps/", "vi": "đập mạnh tay; thắng áp đảo (lóng)"},
  {"id": "lex.en.200k.065030", "hw": "windbags", "pos": "noun", "ipa": "/ˈwɪndbæɡz/", "vi": "kẻ ba hoa rỗng tuếch nói dông dài"},
  {"id": "lex.en.200k.065031", "hw": "wolofs", "pos": "noun", "ipa": "/ˈwoʊlɑːfs/", "vi": "dân tộc và ngôn ngữ Wolof Tây Phi"},
  {"id": "lex.en.200k.065032", "hw": "zantacs", "pos": "noun", "ipa": "/ˈzæntæks/", "vi": "thuốc trị loét dạ dày Zantac"},
  {"id": "lex.en.200k.065033", "hw": "zeemans", "pos": "noun", "ipa": "/ˈzeɪmɑːnz/", "vi": "nhà vật lý Nobel Hà Lan Zeeman"},
  {"id": "lex.en.200k.065034", "hw": "zombas", "pos": "noun", "ipa": "/ˈzɑːmbəz/", "vi": "cố đô Zomba của quốc gia Malawi"},
  {"id": "lex.en.200k.065035", "hw": "andre derain", "pos": "phrase", "ipa": "/ɑːnˈdreɪ dəˈræn/", "vi": "danh họa Dã thú Pháp André Derain"},
  {"id": "lex.en.200k.065036", "hw": "antiemetic drug", "pos": "phrase", "ipa": "/ˌæntiɪˈmɛtɪk drʌɡ/", "vi": "thuốc chống buồn nôn và ói mửa"},
  {"id": "lex.en.200k.065037", "hw": "assortative mating", "pos": "phrase", "ipa": "/əˈsɔːrtətɪv ˈmeɪtɪŋ/", "vi": "giao phối chọn lọc theo kiểu hình"},
  {"id": "lex.en.200k.065038", "hw": "battle of wagram", "pos": "phrase", "ipa": "/ˈbætəl əv ˈvɑːɡrɑːm/", "vi": "trận chiến Wagram năm 1809 của Áo"},
  {"id": "lex.en.200k.065039", "hw": "betula pubescens", "pos": "phrase", "ipa": "/ˈbɛtʃʊlə pjuːˈbɛsənz/", "vi": "cây bạch dương vỏ trắng phủ lông"},
  {"id": "lex.en.200k.065040", "hw": "connive at", "pos": "phrase", "ipa": "/kəˈnaɪv æt/", "vi": "làm ngơ dung túng cho việc sai trái"},
  {"id": "lex.en.200k.065041", "hw": "decapod crustacean", "pos": "phrase", "ipa": "/ˈdɛkəˌpɑːd krʌˈsteɪʃən/", "vi": "động vật giáp xác mười chân"},
  {"id": "lex.en.200k.065042", "hw": "diabetes insipidus", "pos": "phrase", "ipa": "/ˌdaɪəˈbiːtiːz ɪnˈsɪpədəs/", "vi": "bệnh đái tháo nhạt rối loạn thận"},
  {"id": "lex.en.200k.065043", "hw": "dogtooth violet", "pos": "phrase", "ipa": "/ˈdɔːɡtuːθ ˈvaɪəlɪt/", "vi": "hoa loa kèn răng chó cánh uốn ngược"},
  {"id": "lex.en.200k.065044", "hw": "european dogtooth", "pos": "phrase", "ipa": "/ˌjʊrəˈpiːən ˈdɔːɡtuːθ/", "vi": "hoa bách hợp răng chó châu Âu"},
  {"id": "lex.en.200k.065045", "hw": "family carabidae", "pos": "phrase", "ipa": "/ˈfæməli kəˈræbədiː/", "vi": "họ bọ cánh cứng chân chạy săn mồi"},
  {"id": "lex.en.200k.065046", "hw": "genus corynebacterium", "pos": "phrase", "ipa": "/ˈdʒiːnəs kəˌraɪnibækˈtɪriəm/", "vi": "chi vi khuẩn que Corynebacterium"},
  {"id": "lex.en.200k.065047", "hw": "genus eimeria", "pos": "phrase", "ipa": "/ˈdʒiːnəs aɪˈmɪriə/", "vi": "chi trùng cầu ký sinh đường ruột"},
  {"id": "lex.en.200k.065048", "hw": "genus grampus", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈɡræmpəs/", "vi": "chi cá heo xám đầu tròn Grampus"},
  {"id": "lex.en.200k.065049", "hw": "genus hakea", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈheɪkiə/", "vi": "chi cây bụi hoa kim Hakea nước Úc"},
  {"id": "lex.en.200k.065050", "hw": "genus heliothis", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˌhiːliˈɑːθɪs/", "vi": "chi bướm đêm sâu đục nụ bông"},
  {"id": "lex.en.200k.065051", "hw": "genus iguanodon", "pos": "phrase", "ipa": "/ˈdʒiːnəs ɪˈɡwɑːnədɑːn/", "vi": "chi khủng long ăn cỏ Iguanodon"},
  {"id": "lex.en.200k.065052", "hw": "genus kobus", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈkoʊbəs/", "vi": "chi linh dương nước châu Phi Kobus"},
  {"id": "lex.en.200k.065053", "hw": "genus lycopodium", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˌlaɪkəˈpoʊdiəm/", "vi": "chi thực vật thông đất Thạch tùng"},
  {"id": "lex.en.200k.065054", "hw": "genus nepenthes", "pos": "phrase", "ipa": "/ˈdʒiːnəs nɪˈpɛnθiːz/", "vi": "chi cây nắp ấm bắt côn trùng"},
  {"id": "lex.en.200k.065055", "hw": "genus panax", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈpænæks/", "vi": "chi thực vật nhân sâm quý Panax"},
  {"id": "lex.en.200k.065056", "hw": "genus pavo", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈpeɪvoʊ/", "vi": "chi chim công đuôi xòe lộng lẫy"},
  {"id": "lex.en.200k.065057", "hw": "genus potentilla", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˌpoʊtənˈtɪlə/", "vi": "chi cây hoa ngũ trảo hoa vàng"},
  {"id": "lex.en.200k.065058", "hw": "handsaw fish", "pos": "phrase", "ipa": "/ˈhændsɔː fɪʃ/", "vi": "cá kiếm mũi nhọn vây lưng biển sâu"},
  {"id": "lex.en.200k.065059", "hw": "horsefly weed", "pos": "phrase", "ipa": "/ˈhɔːrsflaɪ wiːd/", "vi": "cây chàm dại hoa vàng Bắc Mỹ"},
  {"id": "lex.en.200k.065060", "hw": "ichneumon fly", "pos": "phrase", "ipa": "/ɪkˈnjuːmən flaɪ/", "vi": "ong cự ký sinh đẻ trứng vào sâu"},
  {"id": "lex.en.200k.065061", "hw": "ileal artery", "pos": "phrase", "ipa": "/ˈɪliəl ˈɑːrtəri/", "vi": "động mạch hồi tràng cấp máu ruột"},
  {"id": "lex.en.200k.065062", "hw": "iris cristata", "pos": "phrase", "ipa": "/ˈaɪrɪs krɪˈsteɪtə/", "vi": "hoa diên vĩ lùn có mào Bắc Mỹ"},
  {"id": "lex.en.200k.065063", "hw": "isak dinesen", "pos": "phrase", "ipa": "/ˈiːzɑːk dɪˈneɪzən/", "vi": "bút danh nữ văn sĩ Karen Blixen"},
  {"id": "lex.en.200k.065064", "hw": "john uhler", "pos": "phrase", "ipa": "/dʒɑːn ˈjuːlər/", "vi": "nam diễn viên Mỹ Jack Lemmon"},
  {"id": "lex.en.200k.065065", "hw": "killdeer plover", "pos": "phrase", "ipa": "/ˈkɪldɪər ˈplʌvər/", "vi": "chim choi choi hai vòng cổ Bắc Mỹ"},
  {"id": "lex.en.200k.065066", "hw": "larus marinus", "pos": "phrase", "ipa": "/ˈlɛrəs məˈraɪnəs/", "vi": "mòng biển lớn lưng đen Đại Tây"},
  {"id": "lex.en.200k.065067", "hw": "lautaro youth movement", "pos": "phrase", "ipa": "/laʊˈtɑːroʊ juːθ ˈmuːvmənt/", "vi": "nhóm thanh niên nổi dậy Lautaro"},
  {"id": "lex.en.200k.065068", "hw": "musculus adductor brevis", "pos": "phrase", "ipa": "/ˈmʌskjʊləs əˈdʌktər ˈbrɛvɪs/", "vi": "cơ khép ngắn vùng đùi trong"},
  {"id": "lex.en.200k.065069", "hw": "musculus tibialis", "pos": "phrase", "ipa": "/ˈmʌskjʊləs ˌtɪbiˈeɪlɪs/", "vi": "cơ chày dọc xương ống chân"},
  {"id": "lex.en.200k.065070", "hw": "mynah bird", "pos": "phrase", "ipa": "/ˈmaɪnə bɜːrd/", "vi": "chim sáo nâu; chim nhồng biết nói"},
  {"id": "lex.en.200k.065071", "hw": "neisseria gonorrhoeae", "pos": "phrase", "ipa": "/naɪˈsɪriə ˌɡɑːnəˈriːiː/", "vi": "song cầu khuẩn gây bệnh lậu"},
  {"id": "lex.en.200k.065072", "hw": "nerium oleander", "pos": "phrase", "ipa": "/ˈnɪriəm ˌoʊliˈændər/", "vi": "cây hoa trúc đào lá dài có độc tố"},
  {"id": "lex.en.200k.065073", "hw": "nicolo amati", "pos": "phrase", "ipa": "/ˈniːkoʊloʊ əˈmɑːti/", "vi": "nghệ nhân làm đàn vĩ cầm Ý Amati"},
  {"id": "lex.en.200k.065074", "hw": "nicotiana glauca", "pos": "phrase", "ipa": "/nɪˌkoʊʃiˈeɪnə ˈɡlɔːkə/", "vi": "cây thuốc lá thân gỗ hoa vàng"},
  {"id": "lex.en.200k.065075", "hw": "nrem sleep", "pos": "phrase", "ipa": "/ˈɛnˌrɛm sliːp/", "vi": "giấc ngủ sâu không chuyển động mắt"},
  {"id": "lex.en.200k.065076", "hw": "ortolan bunting", "pos": "phrase", "ipa": "/ˈɔːrtələn ˈbʌntɪŋ/", "vi": "chim sẻ đồng Ortolan ẩm thực Pháp"},
  {"id": "lex.en.200k.065077", "hw": "petrolatum gauze", "pos": "phrase", "ipa": "/ˌpɛtrəˈleɪtəm ɡɔːz/", "vi": "gạc y tế tẩm vaseline chống dính"},
  {"id": "lex.en.200k.065078", "hw": "prussic acid", "pos": "phrase", "ipa": "/ˈprʌsɪk ˈæsɪd/", "vi": "axit xianhidric cực độc HCN"},
  {"id": "lex.en.200k.065079", "hw": "quadriceps femoris", "pos": "phrase", "ipa": "/ˈkwɑːdrəsɛps ˈfɛmərɪs/", "vi": "khối cơ tứ đầu mặt trước đùi"},
  {"id": "lex.en.200k.065080", "hw": "queen triggerfish", "pos": "phrase", "ipa": "/kwiːn ˈtrɪɡərfɪʃ/", "vi": "cá bò da hoàng hậu rạn san hô"},
  {"id": "lex.en.200k.065081", "hw": "scilla verna", "pos": "phrase", "ipa": "/ˈsɪlə ˈvɜːrnə/", "vi": "hoa chuông xanh mùa xuân Scilla"},
  {"id": "lex.en.200k.065082", "hw": "senna alata", "pos": "phrase", "ipa": "/ˈsɛnə əˈleɪtə/", "vi": "cây muồng trâu hoa vàng trị nấm da"},
  {"id": "lex.en.200k.065083", "hw": "st mihiel", "pos": "phrase", "ipa": "/sænt miˈjɛl/", "vi": "trận St. Mihiel Thế chiến thứ nhất"},
  {"id": "lex.en.200k.065084", "hw": "staghorn sumac", "pos": "phrase", "ipa": "/ˈstæɡhɔːrn ˈsuːmæk/", "vi": "cây sơn lá kép lông nhung Bắc Mỹ"},
  {"id": "lex.en.200k.065085", "hw": "stratum lucidum", "pos": "phrase", "ipa": "/ˈstreɪtəm ˈluːsɪdəm/", "vi": "lớp sừng trong suốt của biểu bì da"},
  {"id": "lex.en.200k.065086", "hw": "submandibular salivary gland", "pos": "phrase", "ipa": "/ˌsʌbmænˈdɪbjələr ˈsælɪˌvɛri ɡlænd/", "vi": "tuyến nước bọt nằm dưới xương hàm"},
  {"id": "lex.en.200k.065087", "hw": "ulmus laevis", "pos": "phrase", "ipa": "/ˈʌlməs ˈliːvɪs/", "vi": "cây du trắng cánh quả rìa châu Âu"},
  {"id": "lex.en.200k.065088", "hw": "western wood pewee", "pos": "phrase", "ipa": "/ˈwɛstərn wʊd ˈpiːwi/", "vi": "chim đớp ruồi gỗ miền tây Bắc Mỹ"},
  {"id": "lex.en.200k.065089", "hw": "white dogtooth violet", "pos": "phrase", "ipa": "/waɪt ˈdɔːɡtuːθ ˈvaɪəlɪt/", "vi": "hoa bách hợp răng chó trắng Bắc Mỹ"},
  {"id": "lex.en.200k.065090", "hw": "wood pewee", "pos": "phrase", "ipa": "/wʊd ˈpiːwi/", "vi": "chim đớp ruồi nhỏ sống trong rừng"},
  {"id": "lex.en.200k.065091", "hw": "alarmisms", "pos": "noun", "ipa": "/əˈlɑːrmɪzəmz/", "vi": "thái độ thổi phồng gây hoang mang"},
  {"id": "lex.en.200k.065092", "hw": "allegrettos", "pos": "noun", "ipa": "/ˌælɪˈɡrɛtoʊz/", "vi": "chương nhạc tiết tấu hơi nhanh vui"},
  {"id": "lex.en.200k.065093", "hw": "amenorrheas", "pos": "noun", "ipa": "/eɪˌmɛnəˈriːəz/", "vi": "chứng vô kinh không có kinh nguyệt"},
  {"id": "lex.en.200k.065094", "hw": "antineoplastics", "pos": "noun", "ipa": "/ˌæntiniːoʊˈplæstɪks/", "vi": "nhóm thuốc hóa trị chống ung thư"},
  {"id": "lex.en.200k.065095", "hw": "appros", "pos": "noun", "ipa": "/ˈæproʊz/", "vi": "hình thức mua hàng xem thử (Anh)"},
  {"id": "lex.en.200k.065096", "hw": "arabists", "pos": "noun", "ipa": "/ˈærəbɪsts/", "vi": "học giả chuyên ngành Ả Rập học"},
  {"id": "lex.en.200k.065097", "hw": "attilios", "pos": "noun", "ipa": "/əˈtiːlioʊz/", "vi": "chòm râu nhỏ giữa dưới môi dưới"},
  {"id": "lex.en.200k.065098", "hw": "basias", "pos": "noun", "ipa": "/ˈbɑːzrəz/", "vi": "thành phố cảng lớn Basra ở Iraq"},
  {"id": "lex.en.200k.065099", "hw": "beantowns", "pos": "noun", "ipa": "/ˈbiːntaʊnz/", "vi": "biệt danh thành phố Boston Hoa Kỳ"},
  {"id": "lex.en.200k.065100", "hw": "billfolds", "pos": "noun", "ipa": "/ˈbɪlfoʊldz/", "vi": "ví da gấp đôi đựng tiền giấy tờ"},
  {"id": "lex.en.200k.065101", "hw": "bonefishes", "pos": "noun", "ipa": "/ˈboʊnfɪʃɪz/", "vi": "cá mòi đường biển cạn nhiều xương"},
  {"id": "lex.en.200k.065102", "hw": "booles", "pos": "noun", "ipa": "/buːlz/", "vi": "nhà toán học đại số George Boole"}
]

with open('scratch/b34_r01_raw_p1.json') as f:
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

with open('scratch/b34_r01_p1.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r01_p1.json OK")
