import json

RECORDS = [
    ("087003", "silaging", "verb", "/ˈsaɪlɪdʒɪŋ/", "đang ủ chua thức ăn gia súc"),
    ("087004", "silencers", "noun", "/ˈsaɪlənsərz/", "ống giảm thanh; bộ tiêu âm"),
    ("087005", "silences", "verb", "/ˈsaɪlənsɪz/", "làm im lặng; bịt miệng; dập tắt"),
    ("087006", "silencing", "verb", "/ˈsaɪlənsɪŋ/", "đang làm im lặng; đang bịt miệng"),
    ("087007", "silhouetted", "verb", "/ˌsɪləˈwɛtɪd/", "đã hiện bóng đen nổi bật trên nền"[:35]),
    ("087008", "silhouettes", "verb", "/ˌsɪləˈwɛts/", "tạo bóng đen nổi bật trên nền"),
    ("087009", "silhouetting", "verb", "/ˌsɪləˈwɛtɪŋ/", "đang tạo bóng đen nổi bật"),
    ("087010", "silicated", "adj", "/ˈsɪlɪˌkeɪtɪd/", "tẩm silicat; kết hợp với silic"),
    ("087011", "silicic", "adj", "/səˈlɪsɪk/", "thuộc axit silicic; chứa silic"),
    ("087012", "siliciferous", "adj", "/ˌsɪlɪˈsɪfərəs/", "chứa silic đioxit; giàu silic"),
    ("087013", "silicification", "noun", "/səˌlɪsɪfɪˈkeɪʃən/", "quá trình hóa silic; hóa đá"),
    ("087014", "silicify", "verb", "/səˈlɪsɪˌfaɪ/", "hóa silic; tẩm silic đioxit"),
    ("087015", "silicious", "adj", "/səˈlɪʃəs/", "chứa silic; giống thạch anh"),
    ("087016", "silicium", "noun", "/səˈlɪʃiəm/", "nguyên tố hóa học silic"),
    ("087017", "silicle", "noun", "/ˈsɪlɪkəl/", "quả cải ngắn (thực vật)"),
    ("087018", "silicotic", "adj", "/ˌsɪlɪˈkɑːtɪk/", "mắc bệnh bụi phổi silic"),
    ("087019", "silicula", "noun", "/səˈlɪkjələ/", "quả cải ngắn"),
    ("087020", "silique", "noun", "/səˈliːk/", "quả cải dài (họ Cải)"),
    ("087021", "siliquose", "adj", "/ˈsɪlɪˌkwoʊs/", "có quả cải dài; dạng quả cải"),
    ("087022", "siliquous", "adj", "/ˈsɪlɪkwəs/", "có quả cải dài; dạng quả cải"),
    ("087023", "silkalene", "noun", "/ˈsɪlkəˌliːn/", "vải bông mỏng mịn ánh lụa"),
    ("087024", "silkaline", "noun", "/ˈsɪlkəˌliːn/", "vải bông mỏng mịn ánh lụa"),
    ("087025", "silkfish", "noun", "/ˈsɪlkˌfɪʃ/", "cá đao bạc; cá bơn nhỏ"),
    ("087026", "silkgrass", "noun", "/ˈsɪlkˌɡræs/", "cỏ tơ; cây dứa sợi tơ"),
    ("087027", "silklike", "adj", "/ˈsɪlkˌlaɪk/", "mềm mượt như tơ lụa"),
    ("087028", "silkman", "noun", "/ˈsɪlkmən/", "thương nhân buôn bán tơ lụa"),
    ("087029", "silkmen", "noun", "/ˈsɪlkmən/", "thương nhân buôn bán tơ lụa"),
    ("087030", "silkmoth", "noun", "/ˈsɪlkˌmɔːθ/", "ngài tằm; bướm tằm"),
    ("087031", "silkweed", "noun", "/ˈsɪlkˌwiːd/", "cây bông tai hạt có chùm lông tơ"),
    ("087032", "sillabub", "noun", "/ˈsɪləˌbʌb/", "món kem sữa đánh rượu ngọt"),
    ("087033", "sillaginidae", "noun", "/ˌsɪləˈdʒɪnɪˌdiː/", "họ Cá đục (Sillaginidae)"),
    ("087034", "sillago", "noun", "/ˈsɪləɡoʊ/", "chi Cá đục biển (Sillago)"),
    ("087035", "siller", "noun", "/ˈsɪlər/", "bạc; tiền bạc (tiếng Scotland)"),
    ("087036", "sillily", "adv", "/ˈsɪlɪli/", "ngớ ngẩn; khờ dại; dại dột"),
    ("087037", "sillinesses", "noun", "/ˈsɪlinəsɪz/", "sự ngớ ngẩn; trò dại dột"),
    ("087038", "siltation", "noun", "/sɪlˈteɪʃən/", "sự bồi lắng phù sa bùn cát"),
    ("087039", "silted", "verb", "/ˈsɪltɪd/", "đã bị bồi lắng bùn cát"),
    ("087040", "silting", "verb", "/ˈsɪltɪŋ/", "đang bị bồi lắng bùn cát"),
    ("087041", "silts", "verb", "/sɪlts/", "bồi lắng bùn cát; tắc nghẽn bùn"),
    ("087042", "silumin", "noun", "/ˈsɪljəmɪn/", "hợp kim nhôm silic (silumin)"),
    ("087043", "silurid", "noun", "/səˈljʊrɪd/", "cá nheo; cá da trơn họ Siluridae"),
    ("087044", "siluridae", "noun", "/səˈljʊrɪˌdiː/", "họ Cá nheo (Siluridae)"),
    ("087045", "siluriformes", "noun", "/səˌljʊrɪˈfɔːrmiːz/", "bộ Cá nheo; bộ Cá da trơn"),
    ("087046", "silurus", "noun", "/səˈljʊrəs/", "chi Cá nheo (Silurus)"),
    ("087047", "silverberry", "noun", "/ˈsɪlvərˌbɛri/", "cây nhót bạc Bắc Mỹ"),
    ("087048", "silverbush", "noun", "/ˈsɪlvərˌbʊʃ/", "cây bụi lá ánh bạc"),
    ("087049", "silvered", "verb", "/ˈsɪlvərd/", "đã mạ bạc; đã nhuốm màu hoa râm"),
    ("087050", "silveriness", "noun", "/ˈsɪlvərinəs/", "sắc ánh bạc; âm thanh trong trẻo"),
    ("087051", "silvering", "verb", "/ˈsɪlvərɪŋ/", "đang tráng bạc; đang nhuốm bạc"),
    ("087052", "silverish", "adj", "/ˈsɪlvərɪʃ/", "hơi có ánh bạc"),
    ("087053", "silverless", "adj", "/ˈsɪlvərləs/", "không có bạc; nghèo túng không tiền"[:35]),
    ("087054", "silverly", "adv", "/ˈsɪlvərli/", "óng ánh màu bạc; trong trẻo"),
    ("087055", "silvern", "adj", "/ˈsɪlvərn/", "bằng bạc; óng ánh màu bạc"),
    ("087056", "silverpoint", "noun", "/ˈsɪlvərˌpɔɪnt/", "kỹ thuật vẽ bằng bút đầu bạc"),
    ("087057", "silverrod", "noun", "/ˈsɪlvərˌrɑːd/", "cây hoàng hoa Solidago bicolor"),
    ("087058", "silvers", "verb", "/ˈsɪlvərz/", "mạ bạc; tráng bạc; hóa tóc bạc"),
    ("087059", "silverspot", "noun", "/ˈsɪlvərˌspɑːt/", "bướm đốm bạc cánh dưới"),
    ("087060", "silversword", "noun", "/ˈsɪlvərˌsɔːrd/", "cây kiếm bạc Hawaii quý hiếm"),
    ("087061", "silvervine", "noun", "/ˈsɪlvərˌvaɪn/", "cây dây leo kiwi bạc (mèo thích)"),
    ("087062", "silverweed", "noun", "/ˈsɪlvərˌwiːd/", "cây cỏ lá bạc Potentilla"),
    ("087063", "silverworker", "noun", "/ˈsɪlvərˌwɜːrkər/", "thợ chế tác đồ bạc"),
    ("087064", "silvester", "noun", "/sɪlˈvɛstər/", "tên họ Silvester; đêm Giao thừa"),
    ("087065", "silvex", "noun", "/ˈsɪlvɛks/", "thuốc diệt cỏ silvex"),
    ("087066", "silvics", "noun", "/ˈsɪlvɪks/", "sinh thái học rừng; lâm học"),
    ("087067", "silvicultural", "adj", "/ˌsɪlvɪˈkʌltʃərəl/", "thuộc lâm sinh học; trồng rừng"),
    ("087068", "silviculturist", "noun", "/ˌsɪlvɪˈkʌltʃərɪst/", "chuyên gia lâm sinh học"),
    ("087069", "silybum", "noun", "/ˈsɪlɪbəm/", "chi Kế sữa (Silybum)"),
    ("087070", "simal", "noun", "/ˈsiːməl/", "cây gạo hoa đỏ Ấn Độ"),
    ("087071", "simarouba", "noun", "/ˌsɪməˈruːbə/", "chi cây Thanh thất nhiệt đới Mỹ"),
    ("087072", "simaroubaceae", "noun", "/ˌsɪməruːˈbeɪsiːˌiː/", "họ Thanh thất (Simaroubaceae)"),
    ("087073", "simazine", "noun", "/ˈsɪməˌziːn/", "thuốc diệt cỏ simazine"),
    ("087074", "similarities", "noun", "/ˌsɪməˈlærɪtiz/", "điểm tương đồng; nét giống nhau"),
    ("087075", "similise", "verb", "/ˈsɪməˌlaɪz/", "dùng phép so sánh ví von"),
    ("087076", "similize", "verb", "/ˈsɪməˌlaɪz/", "dùng phép so sánh ví von"),
    ("087077", "simitar", "noun", "/ˈsɪmɪtər/", "thanh đao cong Trung Đông"),
    ("087078", "simmered", "verb", "/ˈsɪmərd/", "đã đun liu riu; đã âm ỉ giận"),
    ("087079", "simmers", "verb", "/ˈsɪmərz/", "đun sôi liu riu; âm ỉ bực tức"),
    ("087080", "simmpleness", "noun", "/ˈsɪmpəlnəs/", "tính giản dị; vẻ mộc mạc đơn sơ"),
    ("087081", "simoleon", "noun", "/sɪˈmoʊliən/", "đồng đô la (tiếng lóng Mỹ)"),
    ("087082", "simoniac", "noun", "/sɪˈmoʊniˌæk/", "kẻ buôn bán chức sắc thần quyền"),
    ("087083", "simoniacal", "adj", "/ˌsɪməˈnaɪəkəl/", "thuộc tội buôn bán chức thánh"),
    ("087084", "simonise", "verb", "/ˈsaɪməˌnaɪz/", "đánh bóng xe bằng sáp"),
    ("087085", "simoniz", "noun", "/ˈsaɪməˌnaɪz/", "sáp đánh bóng ô tô Simoniz"),
    ("087086", "simonize", "verb", "/ˈsaɪməˌnaɪz/", "đánh bóng xe bằng sáp"),
    ("087087", "simoon", "noun", "/sɪˈmuːn/", "gió cát nóng bỏng sa mạc Sahara"),
    ("087088", "simp", "noun", "/sɪmp/", "người si mê mù quáng (lóng); khờ"),
    ("087089", "simpered", "verb", "/ˈsɪmpərd/", "đã cười gượng gạo ngớ ngẩn"),
    ("087090", "simperer", "noun", "/ˈsɪmpərər/", "người hay cười cười ngớ ngẩn"),
    ("087091", "simpering", "verb", "/ˈsɪmpərɪŋ/", "đang cười ngượng nghịu lấy lòng"),
    ("087092", "simperingly", "adv", "/ˈsɪmpərɪŋli/", "với điệu cười ngượng ngập gượng gạo"[:35]),
    ("087093", "simpers", "verb", "/ˈsɪmpərz/", "cười ngượng nghịu ngớ ngẩn"),
    ("087094", "simpleminded", "adj", "/ˌsɪmpəlˈmaɪndɪd/", "ngây thơ cả tin; suy nghĩ đơn giản"[:35]),
    ("087095", "simplicial", "adj", "/sɪmˈplɪʃəl/", "thuộc đơn hình (toán học)"),
    ("087096", "simpliciter", "adv", "/sɪmˈplɪsɪtər/", "một cách vô điều kiện; đơn thuần"),
    ("087097", "simplified", "verb", "/ˈsɪmpləˌfaɪd/", "đã đơn giản hóa"),
    ("087098", "simplifier", "noun", "/ˈsɪmpləˌfaɪər/", "người đơn giản hóa vấn đề"),
    ("087099", "simplifiers", "noun", "/ˈsɪmpləˌfaɪərz/", "người đơn giản hóa vấn đề"),
    ("087100", "simplifies", "verb", "/ˈsɪmpləˌfaɪz/", "đơn giản hóa"),
    ("087101", "simplifying", "verb", "/ˈsɪmpləˌfaɪɪŋ/", "đang đơn giản hóa"),
    ("087102", "simplism", "noun", "/ˈsɪmplɪzəm/", "lối đơn giản hóa thái quá"),
]

# Remove slices cleanly <= 35 chars
RECORDS[4] = ("087007", "silhouetted", "verb", "/ˌsɪləˈwɛtɪd/", "đã hiện bóng đen nổi bật")
RECORDS[50] = ("087053", "silverless", "adj", "/ˈsɪlvərləs/", "không có bạc; nghèo túng")
RECORDS[89] = ("087092", "simperingly", "adv", "/ˈsɪmpərɪŋli/", "với điệu cười gượng ngớ ngẩn")
RECORDS[91] = ("087094", "simpleminded", "adj", "/ˌsɪmpəlˈmaɪndɪd/", "ngây thơ cả tin; đầu óc đơn giản")

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b38_r05_raw_p1.json"))
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

json.dump(out, open("scratch/b38_r05_reviewed_p1.json", "w"), ensure_ascii=False, indent=2)
print("b38_r05_p1 saved OK")
