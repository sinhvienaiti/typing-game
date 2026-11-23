import json

RECORDS = [
    ("086403", "sexologist", "noun", "/sɛkˈsɑːlədʒɪst/", "nhà tình dục học"),
    ("086404", "sexologists", "noun", "/sɛkˈsɑːlədʒɪsts/", "nhà tình dục học"),
    ("086405", "sexology", "noun", "/sɛkˈsɑːlədʒi/", "tình dục học"),
    ("086406", "sexpartite", "adj", "/sɛksˈpɑːrtaɪt/", "chia thành sáu phần"),
    ("086407", "sexsomnia", "noun", "/sɛkˈsɑːmniə/", "chứng mộng du tình dục"),
    ("086408", "sexsomniac", "noun", "/sɛkˈsɑːmniæk/", "người mắc chứng mộng du tình dục"),
    ("086409", "sextain", "noun", "/ˈsɛksteɪn/", "khổ thơ sáu câu"),
    ("086410", "sextan", "adj", "/ˈsɛkstən/", "tái phát cách mỗi năm ngày (sốt)"),
    ("086411", "sexte", "noun", "/sɛkst/", "kinh giờ Ngọ; thế thủ thứ sáu"),
    ("086412", "sextette", "noun", "/sɛkˈstɛt/", "nhóm sáu người; bản nhạc sáu bè"),
    ("086413", "sextic", "adj", "/ˈsɛkstɪk/", "bậc sáu (toán học)"),
    ("086414", "sexto", "noun", "/ˈsɛkstoʊ/", "sách khổ sáu (in ấn)"),
    ("086415", "sextodecimo", "noun", "/ˌsɛkstoʊˈdɛsəˌmoʊ/", "sách khổ mười sáu"),
    ("086416", "sextuplet", "noun", "/sɛkˈstʌplət/", "một đứa trong ca sinh sáu; bộ sáu"),
    ("086417", "sexuales", "noun", "/ˌsɛkʃuˈeɪliːz/", "cá thể có giới tính (côn trùng)"),
    ("086418", "sexualist", "noun", "/ˈsɛkʃuəlɪst/", "người phân loại cây theo nhị nhụy"),
    ("086419", "sezession", "noun", "/zɪˈtsɛʃən/", "trường phái Ly khai Vienna"),
    ("086420", "sf", "noun", "/ˌɛsˈɛf/", "truyện khoa học viễn tưởng (SF)"),
    ("086421", "sfumato", "noun", "/sfuːˈmɑːtoʊ/", "kỹ thuật tô chuyển mờ nhòe sfumato"),
    ("086422", "sgd", "adj", "/saɪnd/", "đã ký tên (viết tắt); đô la SGD"),
    ("086423", "shabbyish", "adj", "/ˈʃæbiɪʃ/", "hơi tồi tàn; hơi cũ sờn"),
    ("086424", "shabrack", "noun", "/ˈʃæbræk/", "tấm thảm phủ yên ngựa kỵ binh"),
    ("086425", "shabuoth", "noun", "/ʃəˈvuːoʊθ/", "lễ Ngũ Tuần Do Thái Shavuot"),
    ("086426", "shacked", "verb", "/ʃækt/", "đã sống chung chòi; sống thử"),
    ("086427", "shacking", "verb", "/ˈʃækɪŋ/", "đang sống chung không kết hôn"),
    ("086428", "shackles", "verb", "/ˈʃækəlz/", "cùm tay chân; trói buộc tự do"),
    ("086429", "shackling", "verb", "/ˈʃæklɪŋ/", "đang cùm tay; đang trói buộc"),
    ("086430", "shacks", "verb", "/ʃæks/", "sống chung trong chòi; sống thử"),
    ("086431", "shadberry", "noun", "/ˈʃædˌbɛri/", "quả thanh mai Bắc Mỹ (Amelanchier)"[:35]),
    ("086432", "shadblow", "noun", "/ˈʃædˌbloʊ/", "cây hoa mùa xuân Amelanchier"),
    ("086433", "shadbush", "noun", "/ˈʃædˌbʊʃ/", "cây bụi ra hoa xuân Amelanchier"),
    ("086434", "shaddocks", "noun", "/ˈʃædəks/", "quả bưởi chùm lớn"),
    ("086435", "shadeless", "adj", "/ˈʃeɪdləs/", "không có bóng râm; nắng gắt"),
    ("086436", "shadflower", "noun", "/ˈʃædˌflaʊər/", "cây hoa mùa xuân Amelanchier"),
    ("086437", "shadfly", "noun", "/ˈʃædˌflaɪ/", "con phù du; ruồi tháng năm"),
    ("086438", "shadily", "adv", "/ˈʃeɪdɪli/", "mập mờ mờ ám; râm mát"),
    ("086439", "shadings", "noun", "/ˈʃeɪdɪŋz/", "sắc độ sáng tối; nét đánh bóng"),
    ("086440", "shadoof", "noun", "/ʃəˈduːf/", "cần vọt múc nước tưới ruộng cổ"),
    ("086441", "shadoofs", "noun", "/ʃəˈduːfs/", "cần vọt múc nước tưới ruộng cổ"),
    ("086442", "shadower", "noun", "/ˈʃædoʊər/", "người bám đuôi theo dõi bí mật"),
    ("086443", "shadowgraph", "noun", "/ˈʃædoʊˌɡræf/", "ảnh chiếu bóng; phim X-quang"),
    ("086444", "shadowgraphs", "noun", "/ˈʃædoʊˌɡræfs/", "ảnh chiếu bóng; phim X-quang"),
    ("086445", "shadowiness", "noun", "/ˈʃædoʊinəs/", "sự mờ ảo; vẻ âm u bóng tối"),
    ("086446", "shadowless", "adj", "/ˈʃædoʊləs/", "không đổ bóng"),
    ("086447", "shadows", "verb", "/ˈʃædoʊz/", "che râm; bám đuôi theo dõi"),
    ("086448", "shafting", "noun", "/ˈʃæftɪŋ/", "hệ trục truyền động cơ khí"),
    ("086449", "shagbarks", "noun", "/ˈʃæɡˌbɑːrks/", "cây óc chó vỏ xù Bắc Mỹ"),
    ("086450", "shaggily", "adv", "/ˈʃæɡɪli/", "xù xì rậm rạp"),
    ("086451", "shagginess", "noun", "/ˈʃæɡinəs/", "vẻ xù xì bờm xờm"),
    ("086452", "shaggymane", "noun", "/ˈʃæɡiˌmeɪn/", "nấm mực bờm xù ăn được"),
    ("086453", "shagreen", "noun", "/ʃəˈɡriːn/", "da cá nhám sần làm bao kiếm"),
    ("086454", "shagreens", "noun", "/ʃəˈɡriːnz/", "da cá nhám sần"),
    ("086455", "shahaptian", "noun", "/ʃəˈhɑːptiən/", "người Shahaptian (Bắc Mỹ)"),
    ("086456", "shahdom", "noun", "/ˈʃɑːdəm/", "ngôi vị vua Shah Iran"),
    ("086457", "shahdoms", "noun", "/ˈʃɑːdəmz/", "vương triều vua Shah"),
    ("086458", "shakable", "adj", "/ˈʃeɪkəbəl/", "có thể rung lắc; dễ lung lay"),
    ("086459", "shakeable", "adj", "/ˈʃeɪkəbəl/", "có thể rung lắc; dễ lung lay"),
    ("086460", "shaktism", "noun", "/ˈʃɑːkˌtɪzəm/", "giáo phái thờ nữ thần Shakti"),
    ("086461", "shaktist", "noun", "/ˈʃɑːktɪst/", "tín đồ giáo phái Shakti"),
    ("086462", "shall", "verb", "/ʃæl/", "sẽ; phải (trợ động từ)"),
    ("086463", "shalloon", "noun", "/ʃəˈluːn/", "vải len dệt chéo làm lớp lót"),
    ("086464", "shallop", "noun", "/ˈʃæləp/", "thuyền nhỏ chạy buồm hoặc chèo"),
    ("086465", "shallu", "noun", "/ˈʃæluː/", "giống cây cao lương chịu hạn"),
    ("086466", "shalom", "noun", "/ʃəˈloʊm/", "lời chào bình an tiếng Do Thái"),
    ("086467", "shalt", "verb", "/ʃælt/", "sẽ (ngôi 2 số ít văn cổ)"),
    ("086468", "shaly", "adj", "/ˈʃeɪli/", "chứa đá phiến sét; dễ tách lớp"),
    ("086469", "shamanic", "adj", "/ʃəˈmænɪk/", "thuộc pháp sư shaman; vu thuật"),
    ("086470", "shamanise", "verb", "/ˈʃæməˌnaɪz/", "hành lễ thầy cúng shaman"),
    ("086471", "shamanize", "verb", "/ˈʃæməˌnaɪz/", "hành lễ thầy cúng shaman"),
    ("086472", "shamateur", "noun", "/ˈʃæməˌtɜːr/", "vận động viên nghiệp dư nhận lậu"),
    ("086473", "shambled", "verb", "/ˈʃæmbəld/", "đã đi lệt bệt kéo lê chân"),
    ("086474", "shambolically", "adv", "/ʃæmˈbɑːlɪkli/", "hỗn loạn tơi bời; bừa bãi"),
    ("086475", "shamefacedness", "noun", "/ˌʃeɪmˈfeɪsɪdnəs/", "vẻ ngượng ngùng bẽn lẽn"),
    ("086476", "shamefulness", "noun", "/ˈʃeɪmfəlnəs/", "sự đáng hổ thẹn; điều ô nhục"),
    ("086477", "shames", "verb", "/ʃeɪmz/", "làm xấu hổ; khiến bẽ mặt"),
    ("086478", "shaming", "verb", "/ˈʃeɪmɪŋ/", "đang làm bẽ mặt; chỉ trích công khai"[:35]),
    ("086479", "shammed", "verb", "/ʃæmd/", "đã giả vờ; đã đóng kịch giả dối"),
    ("086480", "shammer", "noun", "/ˈʃæmər/", "kẻ giả vờ; kẻ giả bộ ốm"),
    ("086481", "shammers", "noun", "/ˈʃæmərz/", "kẻ giả vờ; kẻ đóng kịch"),
    ("086482", "shammies", "noun", "/ˈʃæmiz/", "da sơn dương mềm lau kính"),
    ("086483", "shamming", "verb", "/ˈʃæmɪŋ/", "đang giả vờ; đang giả bộ"),
    ("086484", "shamrocks", "noun", "/ˈʃæmˌrɑːks/", "cỏ ba lá biểu tượng Ireland"),
    ("086485", "shams", "verb", "/ʃæmz/", "giả vờ; giả bộ"),
    ("086486", "shandies", "noun", "/ˈʃændiz/", "bia pha nước chanh shandy"),
    ("086487", "shandrydan", "noun", "/ˈʃændrɪˌdæn/", "xe ngựa cũ kỹ ọp ẹp"),
    ("086488", "shandrydans", "noun", "/ˈʃændrɪˌdænz/", "xe ngựa cũ kỹ ọp ẹp"),
    ("086489", "shandygaff", "noun", "/ˈʃændiˌɡæf/", "bia pha nước gừng hay nước chanh"),
    ("086490", "shandygaffs", "noun", "/ˈʃændiˌɡæfs/", "bia pha nước gừng hay nước chanh"),
    ("086491", "shangdi", "noun", "/ʃɑːŋˈdiː/", "Thượng Đế (tín ngưỡng Trung Hoa)"),
    ("086492", "shanghaiier", "noun", "/ˌʃæŋˈhaɪər/", "kẻ bắt cóc người đi làm thủy thủ"),
    ("086493", "shanghaiing", "verb", "/ˌʃæŋˈhaɪɪŋ/", "đang đánh thuốc bắt cóc đi biển"),
    ("086494", "shanghais", "verb", "/ˌʃæŋˈhaɪz/", "lừa bắt cóc làm thủy thủ; ép buộc"),
    ("086495", "shannies", "noun", "/ˈʃæniz/", "cá mào gà biển châu Âu"),
    ("086496", "shanties", "noun", "/ˈʃæntiz/", "túp lều tạm; bài hò thủy thủ"),
    ("086497", "shantyman", "noun", "/ˈʃæntimən/", "thợ rừng sống lán; người xướng hò"),
    ("086498", "shapelessly", "adv", "/ˈʃeɪpləsli/", "không có hình thù rõ ràng"),
    ("086499", "shapelessness", "noun", "/ˈʃeɪpləsnəs/", "tình trạng vô định hình"),
    ("086500", "shapeliness", "noun", "/ˈʃeɪplinəs/", "dáng vẻ cân đối hài hòa"),
    ("086501", "shapers", "noun", "/ˈʃeɪpərz/", "người định hình; máy bào xọc"),
    ("086502", "shapes", "verb", "/ʃeɪps/", "định hình; tạo dáng; uốn nắn"),
]

# Fix 086492 typo (`shanghaiier` -> `shanghaier`) and replace slices cleanly
RECORDS[28] = ("086431", "shadberry", "noun", "/ˈʃædˌbɛri/", "quả thanh mai Bắc Mỹ")
RECORDS[75] = ("086478", "shaming", "verb", "/ˈʃeɪmɪŋ/", "đang làm bẽ mặt; bêu riếu")
RECORDS[89] = ("086492", "shanghaier", "noun", "/ˌʃæŋˈhaɪər/", "kẻ bắt cóc ép đi làm thủy thủ")

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b38_r03_raw_p5.json"))
by_id = {r["id"].split(".")[-1]: r for r in raw}
out = []
for sid, hw, pos, ipa, vi in RECORDS:
    rec = dict(by_id[sid])
    assert rec["hw"] == hw, (sid, hw, rec["hw"])
    rec["pos"] = pos
    rec["ipa"] = ipa
    rec["vi"] = vi
    rec["status"] = "reviewed"
    out.append(rec)

json.dump(out, open("scratch/b38_r03_reviewed_p5.json", "w"), ensure_ascii=False, indent=2)
print("b38_r03_p5 saved OK")
