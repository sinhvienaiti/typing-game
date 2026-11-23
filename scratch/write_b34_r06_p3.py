import json

items = [
    ("067703", "sissed", "verb", "/sɪst/", "đã kêu xì xì; đã suỵt chó tấn công"),
    ("067704", "sisses", "verb", "/ˈsɪsɪz/", "kêu xì xì như hơi; suỵt chó"),
    ("067705", "sissing", "verb", "/ˈsɪsɪŋ/", "đang kêu xì xì; tiếng rít xì hơi"),
    ("067706", "snakier", "adj", "/ˈsneɪkiər/", "ngoằn ngoèo như rắn hơn; gian hơn"),
    ("067707", "snakiest", "adj", "/ˈsneɪkiɪst/", "ngoằn ngoèo nhất; quỷ quyệt nhất"),
    ("067708", "solidagos", "noun", "/ˌsɒlɪˈdeɪɡoʊz/", "cây cúc hoàng anh chi Solidago"),
    ("067709", "spiritisms", "noun", "/ˈspɪrɪˌtɪzəmz/", "thuyết duy linh giao tiếp vong hồn"),
    ("067710", "subventions", "noun", "/səbˈvɛnʃənz/", "khoản tiền trợ cấp từ nhà nước"),
    ("067711", "taenias", "noun", "/ˈtiːniəz/", "sán dây ký sinh; dải băng trang trí"),
    ("067712", "talebans", "noun", "/ˈtælɪˌbænz/", "lực lượng Hồi giáo Taliban"),
    ("067713", "terrassed", "verb", "/ˈtɛrəst/", "đã xây ruộng bậc thang; làm sân"),
    ("067714", "terrasses", "verb", "/ˈtɛrəsɪz/", "xây bậc thang; xếp tầng sân thượng"),
    ("067715", "terrassing", "verb", "/ˈtɛrəsɪŋ/", "đang đắp bậc thang (biến thể)"),
    ("067716", "thunderclouds", "noun", "/ˈθʌndərˌklaʊdz/", "đám mây tích điện giông bão đen"),
    ("067717", "tinbergens", "noun", "/ˈtɪnbɜːrɡənz/", "nhà khoa học Nobel Tinbergen"),
    ("067718", "tuberosities", "noun", "/ˌtjuːbəˈrɒsɪtiz/", "lồi củ gồ lên trên bề mặt xương"),
    ("067719", "tupis", "noun", "/ˈtuːpiz/", "người bản địa và tiếng Tupi Brazil"),
    ("067720", "typographers", "noun", "/taɪˈpɒɡrəfərz/", "nhà thiết kế sắp chữ in ấn"),
    ("067721", "umbels", "noun", "/ˈʌmbəlz/", "cụm hoa tán tỏa tròn như tán dù"),
    ("067722", "underpaying", "verb", "/ˌʌndərˈpeɪɪŋ/", "đang trả lương thấp bèo bọt hơn"),
    ("067723", "underpays", "verb", "/ˌʌndərˈpeɪz/", "trả lương thấp hơn công sức xứng"),
    ("067724", "uprised", "verb", "/ʌpˈraɪzd/", "đã nổi dậy đứng lên; vươn dậy"),
    ("067725", "uprises", "verb", "/ʌpˈraɪzɪz/", "nổi dậy phản kháng; dâng lên cao"),
    ("067726", "utus", "noun", "/ˈuːtuːz/", "thần mặt trời Utu Lưỡng Hà cổ"),
    ("067727", "valettas", "noun", "/vəˈlɛtəz/", "thủ đô Valletta của đảo quốc Malta"),
    ("067728", "volvuluses", "noun", "/ˈvɒlvjʊləsɪz/", "chứng xoắn ruột gây tắc ruột cấp"),
    ("067729", "wapitis", "noun", "/ˈwɒpɪtiz/", "nai sừng tấm lớn Bắc Mỹ wapiti"),
    ("067730", "weismanns", "noun", "/ˈvaɪsmənz/", "nhà sinh học tiến hóa A. Weismann"),
    ("067731", "wellpoints", "noun", "/ˈwɛlˌpɔɪnts/", "giếng ống lọc hút hạ mực nước ngầm"),
    ("067732", "wigglers", "noun", "/ˈwɪɡlərz/", "loăng quăng bọ gậy; người cựa quậy"),
    ("067733", "zombis", "noun", "/ˈzɒmbiz/", "xác sống; thây ma (biến thể)"),
    ("067734", "alfred eisenstaedt", "phrase", "/ˈælfrɪd ˈaɪzənˌstɛt/", "nhiếp ảnh gia Mỹ A. Eisenstaedt"),
    ("067735", "alnus rugosa", "phrase", "/ˈælnəs ruːˈɡoʊsə/", "cây tống quán sủ lốm đốm Bắc Mỹ"),
    ("067736", "american pulsatilla", "phrase", "/əˈmɛrɪkən ˌpʌlsəˈtɪlə/", "hoa chuông gió mùa xuân Bắc Mỹ"),
    ("067737", "antidiuretic drug", "phrase", "/ˌæntidaɪjʊˈrɛtɪk drʌɡ/", "thuốc chống bài niệu giữ nước"),
    ("067738", "antidiuretic hormone", "phrase", "/ˌæntidaɪjʊˈrɛtɪk ˈhɔːrmoʊn/", "hoóc-môn chống bài niệu ADH"),
    ("067739", "argillaceous rock", "phrase", "/ˌɑːrdʒɪˈleɪʃəs rɒk/", "đá trầm tích giàu khoáng vật sét"),
    ("067740", "armillary sphere", "phrase", "/ˈɑːrmɪˌlɛri sfɪər/", "hỗn thiên nghi mô phỏng bầu trời"),
    ("067741", "bollix up", "phrase", "/ˈbɒlɪks ʌp/", "làm hỏng bét; làm rối tung mọi việc"),
    ("067742", "cape froward", "phrase", "/keɪp ˈfroʊwərd/", "mũi cực nam Froward của Nam Mỹ"),
    ("067743", "centaurea nigra", "phrase", "/sɛnˈtɔːriə ˈnaɪɡrə/", "hoa cúc cánh mối đen đồng cỏ Âu"),
    ("067744", "chicle gum", "phrase", "/ˈtʃɪkəl ɡʌm/", "nhựa cây chicle làm kẹo cao su"),
    ("067745", "compos mentis", "phrase", "/ˈkɒmpɒs ˈmɛntɪs/", "tỉnh táo minh mẫn đủ năng lực luật"),
    ("067746", "comstock mealybug", "phrase", "/ˈkɒmstɒk ˈmiːlibʌɡ/", "rệp sáp Comstock hại cây ăn quả"),
    ("067747", "cucking stool", "phrase", "/ˈkʌkɪŋ stuːl/", "ghế nhúng nước trừng phạt thời xưa"),
    ("067748", "donald barthelme", "phrase", "/ˈdɒnəld ˈbɑːrθəlmi/", "nhà văn hậu hiện đại D. Barthelme"),
    ("067749", "fulmar petrel", "phrase", "/ˈfʊlmər ˈpɛtrəl/", "chim hải âu lớn fulmar biển lạnh"),
    ("067750", "genus aspidistra", "phrase", "/ˈdʒiːnəs ˌæspɪˈdɪstrə/", "chi cây tỏi rừng Aspidistra"),
    ("067751", "genus cotoneaster", "phrase", "/ˈdʒiːnəs kəˈtoʊniˌæstər/", "chi cây sơn tra đá Cotoneaster"),
    ("067752", "genus helichrysum", "phrase", "/ˈdʒiːnəs ˌhɛlɪˈkraɪzəm/", "chi hoa cúc bất tử Helichrysum"),
    ("067753", "genus lacerta", "phrase", "/ˈdʒiːnəs ləˈsɜːrtə/", "chi thằn lằn điển hình Lacerta"),
    ("067754", "genus pulsatilla", "phrase", "/ˈdʒiːnəs ˌpʌlsəˈtɪlə/", "chi hoa chuông gió Pulsatilla"),
    ("067755", "hadean aeon", "phrase", "/heɪˈdiːən ˈiːɒn/", "liên đại Hỏa Thành sơ khai Trái Đất"),
    ("067756", "hadean eon", "phrase", "/heɪˈdiːən ˈiːɒn/", "liên đại Hỏa Thành cổ xưa nhất"),
    ("067757", "herman hollerith", "phrase", "/ˈhɜːrmən ˈhɒlərɪθ/", "nhà phát minh thẻ đục lỗ Hollerith"),
    ("067758", "hollerith card", "phrase", "/ˈhɒlərɪθ kɑːrd/", "thẻ bìa đục lỗ dữ liệu Hollerith"),
    ("067759", "intermittent claudication", "phrase", "/ˌɪntərˈmɪtənt ˌklɔːdɪˈkeɪʃən/", "chứng đau cách hồi bắp chân khi đi"),
    ("067760", "inverse cotangent", "phrase", "/ɪnˈvɜːrs koʊˈtændʒənt/", "hàm lượng giác ngược arccotang"),
    ("067761", "jons jakob berzelius", "phrase", "/jɜːns ˈjɑːkɒb bərˈziːliəs/", "nhà hóa học Thụy Điển Berzelius"),
    ("067762", "katar peninsula", "phrase", "/ˈkɑːtər pəˈnɪnsjələ/", "bán đảo Qatar vùng Vịnh Ba Tư"),
    ("067763", "kazimir malevich", "phrase", "/ˈkæzɪmɪər ˈmælɪvɪtʃ/", "họa sĩ tiên phong Nga Malevich"),
    ("067764", "lobate foot", "phrase", "/ˈloʊbeɪt fʊt/", "chân chim có màng thùy bơi ở ngón"),
    ("067765", "malva sylvestris", "phrase", "/ˈmælvə sɪlˈvɛstrɪs/", "cây cẩm quỳ dại hoa tím châu Âu"),
    ("067766", "neck sweetbread", "phrase", "/nɛk ˈswiːtˌbrɛd/", "tuyến ức bê cừu dùng làm món ăn"),
    ("067767", "non compos mentis", "phrase", "/nɒn ˈkɒmpɒs ˈmɛntɪs/", "mất năng lực tinh thần trước luật"),
    ("067768", "nonsingular matrix", "phrase", "/nɒnˈsɪŋɡjələr ˈmeɪtrɪks/", "ma trận vuông khả nghịch định khác"),
    ("067769", "nonspecific urethritis", "phrase", "/ˌnɒnspəˈsɪfɪk ˌjʊərɪˈθraɪtɪs/", "bệnh viêm niệu đạo không đặc hiệu"),
    ("067770", "phencyclidine hydrochloride", "phrase", "/fɛnˈsaɪklɪdiːn ˌhaɪdrəˈklɔːraɪd/", "chất gây mê ảo giác PCP"),
    ("067771", "pinchas zukerman", "phrase", "/ˈpɪŋkəs ˈzʊkərmən/", "nghệ sĩ vĩ cầm Pinchas Zukerman"),
    ("067772", "platte river penstemon", "phrase", "/plæt ˈrɪvər ˈpɛnstəmən/", "cây hoa mõm rồng vùng sông Platte"),
    ("067773", "primula veris", "phrase", "/ˈprɪmjələ ˈvɪərɪs/", "hoa báo xuân vàng châu Âu"),
    ("067774", "pyriform area", "phrase", "/ˈpɪrɪfɔːrm ˈɛəriə/", "vùng vỏ não khứu giác hình quả lê"),
    ("067775", "rainbow lorikeet", "phrase", "/ˈreɪnboʊ ˈlɒrɪˌkiːt/", "loài vẹt lory cầu vồng sặc sỡ Úc"),
    ("067776", "rattail fish", "phrase", "/ˈrætˌteɪl fɪʃ/", "cá đuôi chuột sống dưới đáy biển"),
    ("067777", "reseda odorata", "phrase", "/rɪˈsiːdə ˌoʊdəˈrɑːtə/", "cây hoa mộc tê thơm reseda"),
    ("067778", "rudolf bultmann", "phrase", "/ˈruːdɒlf ˈbʊltmɑːn/", "nhà thần học Đức Rudolf Bultmann"),
    ("067779", "rudolf karl bultmann", "phrase", "/ˈruːdɒlf kɑːrl ˈbʊltmɑːn/", "học giả Tân Ước Rudolf K. Bultmann"),
    ("067780", "rutherford birchard hayes", "phrase", "/ˈrʌðərfərd ˈbɜːrtʃərd heɪz/", "Tổng thống Mỹ thứ 19 R. B. Hayes"),
    ("067781", "scintillating scotoma", "phrase", "/ˈsɪntɪˌleɪtɪŋ skəˈtoʊmə/", "ám điểm nhấp nháy báo cơn đau nửa"),
    ("067782", "spinocerebellar disorder", "phrase", "/ˌspaɪnoʊˌsɛrəˈbɛlər dɪsˈɔːrdər/", "rối loạn thoái hóa tủy tiểu não"),
    ("067783", "state of katar", "phrase", "/steɪt əv ˈkɑːtər/", "Nhà nước Qatar ở Trung Đông"),
    ("067784", "stomach sweetbread", "phrase", "/ˈstʌmək ˈswiːtˌbrɛd/", "tuyến tụy bê cừu làm món ăn"),
    ("067785", "streptomyces griseus", "phrase", "/ˌstrɛptəˈmaɪsiːz ˈɡrɪsiəs/", "xạ khuẩn tạo chất streptomycin"),
    ("067786", "throat sweetbread", "phrase", "/θroʊt ˈswiːtˌbrɛd/", "tuyến ức cổ bê dùng trong ẩm thực"),
    ("067787", "unformatted capacity", "phrase", "/ʌnˈfɔːrmætɪd kəˈpæsɪti/", "dung lượng thô trước khi định dạng"),
    ("067788", "varied lorikeet", "phrase", "/ˈvɛərid ˈlɒrɪˌkiːt/", "vẹt lory sọc nhiều màu bắc Úc"),
    ("067789", "vermiform appendix", "phrase", "/ˈvɜːrmɪˌfɔːrm əˈpɛndɪks/", "ruột thừa hình giun nối manh tràng"),
    ("067790", "vermiform process", "phrase", "/ˈvɜːrmɪˌfɔːrm ˈprɒsɛs/", "ruột thừa ở đoạn đầu ruột già"),
    ("067791", "welted thistle", "phrase", "/ˈwɛltɪd ˈθɪsəl/", "cây kế gai có cánh thân châu Âu"),
    ("067792", "whitebark pine", "phrase", "/ˈwaɪtbɑːrk paɪn/", "cây thông vỏ trắng vùng núi cao"),
    ("067793", "alleghenieses", "noun", "/ˌælɪˈɡeɪnizɪz/", "dãy núi Allegheny ở miền đông Mỹ"),
    ("067794", "almsgivings", "noun", "/ˈɑːmzˌɡɪvɪŋz/", "hành động bố thí tiền của từ thiện"),
    ("067795", "animalias", "noun", "/ˌænɪˈmeɪliəz/", "giới Động vật trong phân loại sinh"),
    ("067796", "anthelmintics", "noun", "/ˌænθɛlˈmɪntɪks/", "thuốc tẩy giun sán ký sinh"),
    ("067797", "antiarrhythmics", "noun", "/ˌæntiəˈrɪðmɪks/", "thuốc điều trị rối loạn nhịp tim"),
    ("067798", "antiguans", "noun", "/ænˈtiːɡənz/", "người dân đảo Antigua vùng Caribe"),
    ("067799", "antipodals", "noun", "/ænˈtɪpədəlz/", "điểm đối cực; tế bào đối cực noãn"),
    ("067800", "arils", "noun", "/ˈærɪlz/", "lớp áo hạt bao quanh hạt thực vật"),
    ("067801", "aureoles", "noun", "/ˈɔːrioʊlz/", "vầng hào quang sáng quanh mặt trời"),
    ("067802", "avogadros", "noun", "/ˌɑːvəˈɡɑːdroʊz/", "nhà khoa học Ý Amedeo Avogadro"),
]

with open("scratch/b34_r06_raw_p3.json") as f:
    raw = json.load(f)

assert len(items) == 100
assert len(raw) == 100
allowed_pos = {"noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det", "phrase"}

out = []
for r, (rid, hw, pos, ipa, vi) in zip(raw, items):
    assert r["id"].endswith("." + rid), f"ID mismatch: {r['id']} != {rid}"
    assert r["hw"] == hw, f"HW mismatch: {r['hw']} != {hw}"
    assert pos in allowed_pos, f"Bad POS {pos} for {hw}"
    assert len(vi) <= 35, f"VI too long ({len(vi)}): {hw} -> {vi}"
    assert ipa.startswith("/") and ipa.endswith("/") and ipa.count("/") == 2, f"Bad IPA: {hw} -> {ipa}"
    inner = ipa[1:-1]
    assert inner and not inner.startswith(" ") and not inner.endswith(" "), f"Empty/space IPA: {hw} -> {ipa}"
    rec = dict(r)
    rec["pos"] = pos
    rec["ipa"] = ipa
    rec["vi"] = vi
    rec["status"] = "reviewed"
    out.append(rec)

with open("scratch/b34_r06_p3.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r06_p3.json OK")
