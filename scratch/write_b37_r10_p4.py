import json

RECORDS = [
    ("084803", "sanitising", "verb", "/ˈsænɪˌtaɪzɪŋ/", "đang khử trùng; đang sát khuẩn"),
    ("084804", "sanitizable", "adj", "/ˈsænɪˌtaɪzəbəl/", "có thể khử trùng được"),
    ("084805", "sanitorium", "noun", "/ˌsænɪˈtɔːriəm/", "viện điều dưỡng"),
    ("084806", "sank", "verb", "/sæŋk/", "đã chìm; đã sụt xuống"),
    ("084807", "sannup", "noun", "/ˈsænəp/", "đàn ông bản địa Mỹ đã lập gia đình"[:35]),
    ("084808", "sans", "prep", "/sænz/", "không có; thiếu"),
    ("084809", "sanscrit", "noun", "/ˈsænskrɪt/", "tiếng Phạn cổ"),
    ("084810", "sansculotte", "noun", "/ˌsænzˈkuːlɑːt/", "nhà cách mạng bình dân Pháp xưa"),
    ("084811", "sansculottism", "noun", "/ˌsænzkjʊˈlɑːtɪzəm/", "chủ trương cách mạng dân nghèo Pháp"[:35]),
    ("084812", "sanserif", "noun", "/sænˈsɛrɪf/", "phông chữ không chân"),
    ("084813", "sanskritic", "adj", "/sænˈskrɪtɪk/", "thuộc tiếng Phạn; ảnh hưởng Phạn"),
    ("084814", "sanskritist", "noun", "/ˈsænskrɪtɪst/", "học giả nghiên cứu tiếng Phạn"),
    ("084815", "santal", "noun", "/ˈsæntəl/", "cây gỗ đàn hương"),
    ("084816", "santalaceae", "noun", "/ˌsæntəˈleɪsiːˌiː/", "họ Đàn hương (Santalaceae)"),
    ("084817", "santalaceous", "adj", "/ˌsæntəˈleɪʃəs/", "thuộc họ Đàn hương"),
    ("084818", "santalales", "noun", "/ˌsæntəˈleɪliːz/", "bộ Đàn hương (Santalales)"),
    ("084819", "santims", "noun", "/ˈsæntɪmz/", "đồng xu santims của Latvia"),
    ("084820", "santol", "noun", "/ˈsæntoʊl/", "cây sấu đỏ nhiệt đới santol"),
    ("084821", "santolina", "noun", "/ˌsæntəˈlaɪnə/", "chi cây oải hương bông Santolina"),
    ("084822", "santonica", "noun", "/sænˈtɑːnɪkə/", "cây ngải tẩy giun santonica"),
    ("084823", "santonin", "noun", "/ˈsæntənɪn/", "hoạt chất tẩy giun santonin"),
    ("084824", "sanvitalia", "noun", "/ˌsænvɪˈteɪliə/", "chi hoa cúc leo Sanvitalia"),
    ("084825", "saola", "noun", "/ˈsaʊlə/", "sao la (kỳ lân châu Á)"),
    ("084826", "saolas", "noun", "/ˈsaʊləz/", "sao la (kỳ lân châu Á)"),
    ("084827", "sapajou", "noun", "/ˈsæpəˌdʒuː/", "khỉ thầy tu Nam Mỹ"),
    ("084828", "sapful", "adj", "/ˈsæpfəl/", "tràn đầy nhựa sống; đầy sinh lực"),
    ("084829", "saphar", "noun", "/ˈsɑːfɑːr/", "tháng thứ hai lịch Hồi giáo"),
    ("084830", "saphead", "noun", "/ˈsæpˌhɛd/", "kẻ khờ dại; người ngốc nghếch"),
    ("084831", "saphena", "noun", "/səˈfiːnə/", "tĩnh mạch hiển ở chân"),
    ("084832", "saphenous", "adj", "/səˈfiːnəs/", "thuộc tĩnh mạch hiển ở chân"),
    ("084833", "sapidity", "noun", "/səˈpɪdɪti/", "vị đậm đà thơm ngon; sự thú vị"),
    ("084834", "sapidness", "noun", "/ˈsæpɪdnəs/", "vị đậm đà thơm ngon"),
    ("084835", "sapiently", "adv", "/ˈseɪpiəntli/", "khôn ngoan; tỏ vẻ thông thái"),
    ("084836", "sapindaceous", "adj", "/ˌsæpɪnˈdeɪʃəs/", "thuộc họ Bồ hòn (Sapindaceae)"),
    ("084837", "sapindales", "noun", "/ˌsæpɪnˈdeɪliːz/", "bộ Bồ hòn (Sapindales)"),
    ("084838", "sapindus", "noun", "/səˈpɪndəs/", "chi cây Bồ hòn (Sapindus)"),
    ("084839", "sapiosexual", "adj", "/ˌseɪpioʊˈsɛkʃuəl/", "bị hấp dẫn bởi trí thông minh"),
    ("084840", "sapless", "adj", "/ˈsæpləs/", "khô héo; cạn kiệt nhựa sống"),
    ("084841", "saponaceous", "adj", "/ˌsæpəˈneɪʃəs/", "giống xà phòng; khéo nịnh bợ"),
    ("084842", "saponifiable", "adj", "/səˈpɑːnəˌfaɪəbəl/", "có thể xà phòng hóa được"),
    ("084843", "saponifier", "noun", "/səˈpɑːnəˌfaɪər/", "chất xà phòng hóa"),
    ("084844", "saponify", "verb", "/səˈpɑːnəˌfaɪ/", "xà phòng hóa"),
    ("084845", "saponins", "noun", "/ˈsæpənɪnz/", "hợp chất saponin tạo bọt"),
    ("084846", "sapor", "noun", "/ˈseɪpər/", "hương vị; tính chất gây vị"),
    ("084847", "saporific", "adj", "/ˌsæpəˈrɪfɪk/", "tạo ra hương vị"),
    ("084848", "saporous", "adj", "/ˈsæpərəs/", "có vị đậm đà; thơm ngon"),
    ("084849", "sapota", "noun", "/səˈpoʊtə/", "cây hồng xiêm; quả sapôchê"),
    ("084850", "sapotaceae", "noun", "/ˌsæpəˈteɪsiːˌiː/", "họ Hồng xiêm (Sapotaceae)"),
    ("084851", "sappanwood", "noun", "/ˈsæpənˌwʊd/", "cây tô mộc; gỗ vang nhuộm đỏ"),
    ("084852", "sapped", "verb", "/sæpt/", "đã làm suy yếu; đã đào hào ngầm"),
    ("084853", "sapphirine", "adj", "/ˈsæfəˌraɪn/", "xanh ngọc bích như đá saphia"),
    ("084854", "sapphism", "noun", "/ˈsæfˌɪzəm/", "tình yêu đồng tính nữ"),
    ("084855", "sappiness", "noun", "/ˈsæpinəs/", "sự tràn đầy nhựa; tính sến sẩm"),
    ("084856", "sapping", "verb", "/ˈsæpɪŋ/", "đang làm suy yếu; đang đào hào"),
    ("084857", "sapraemia", "noun", "/sæˈpriːmiə/", "nhiễm độc máu do mô hoại tử"),
    ("084858", "sapremia", "noun", "/sæˈpriːmiə/", "nhiễm độc máu do mô hoại tử"),
    ("084859", "saproaemia", "noun", "/sæˈpriːmiə/", "nhiễm độc máu do vi khuẩn thối"),
    ("084860", "saprobe", "noun", "/ˈsæproʊb/", "sinh vật hoại sinh"),
    ("084861", "saprobic", "adj", "/sæˈproʊbɪk/", "hoại sinh; sống trên chất thối rữa"[:35]),
    ("084862", "saprobionts", "noun", "/ˌsæprəˈbaɪɑːnts/", "sinh vật hoại sinh"),
    ("084863", "saprogenic", "adj", "/ˌsæprəˈdʒɛnɪk/", "gây thối rữa; sinh ra từ phân hủy"),
    ("084864", "saprogenous", "adj", "/sæˈprɑːdʒənəs/", "gây thối rữa; mọc trên chất mục"),
    ("084865", "saprolegniales", "noun", "/ˌsæprəlɛɡniˈeɪliːz/", "bộ Nấm thủy sinh Saprolegniales"),
    ("084866", "sapropel", "noun", "/ˈsæprəˌpɛl/", "bùn hữu cơ đáy hồ"),
    ("084867", "sapropelic", "adj", "/ˌsæprəˈpɛlɪk/", "thuộc bùn hữu cơ sapropel"),
    ("084868", "saprophagous", "adj", "/sæˈprɑːfəɡəs/", "ăn chất hữu cơ phân hủy"),
    ("084869", "saprophile", "noun", "/ˈsæprəˌfaɪl/", "vi sinh vật ưa chất thối rữa"),
    ("084870", "saprophytes", "noun", "/ˈsæprəˌfaɪts/", "thực vật hoặc nấm hoại sinh"),
    ("084871", "saprophytism", "noun", "/ˌsæprəˈfaɪˌtɪzəm/", "lối sống hoại sinh"),
    ("084872", "saproplankton", "noun", "/ˌsæprəˈplæŋktən/", "sinh vật nổi hoại sinh"),
    ("084873", "saprotrophic", "adj", "/ˌsæprəˈtrɑːfɪk/", "dinh dưỡng hoại sinh"),
    ("084874", "saprozoic", "adj", "/ˌsæprəˈzoʊɪk/", "ăn chất hữu cơ phân hủy (động vật)"[:35]),
    ("084875", "saps", "verb", "/sæps/", "làm suy kiệt; đào hào ngầm"),
    ("084876", "sapsago", "noun", "/ˌsæpsəˈɡoʊ/", "phô mai xanh thảo mộc Thụy Sĩ"),
    ("084877", "saqqarah", "noun", "/səˈkɑːrə/", "khu lăng mộ cổ Saqqara (Ai Cập)"),
    ("084878", "sarafem", "noun", "/ˈsɛrəˌfɛm/", "thuốc chống trầm cảm Sarafem"),
    ("084879", "sarape", "noun", "/səˈrɑːpi/", "áo choàng sọc kiểu Mexico"),
    ("084880", "sarcelle", "noun", "/sɑːrˈsɛl/", "vịt mòng két (thực phẩm)"),
    ("084881", "sarcenchyma", "noun", "/sɑːrˈkɛŋkɪmə/", "mô mềm nhiều hạt của bọt biển"),
    ("084882", "sarcenet", "noun", "/ˈsɑːrsənɪt/", "vải lụa dệt mỏng mịn"),
    ("084883", "sarcobasis", "noun", "/sɑːrˈkɑːbəsɪs/", "đế quả nạc"),
    ("084884", "sarcobatus", "noun", "/ˌsɑːrkəˈbeɪtəs/", "chi cây bụi đất mặn Sarcobatus"),
    ("084885", "sarcocarp", "noun", "/ˈsɑːrkəˌkɑːrp/", "vỏ quả giữa nhiều thịt; cùi quả"),
    ("084886", "sarcocephalus", "noun", "/ˌsɑːrkoʊˈsɛfələs/", "chi cây gáo châu Phi"),
    ("084887", "sarcochilus", "noun", "/ˌsɑːrkəˈkaɪləs/", "chi phong lan Úc Sarcochilus"),
    ("084888", "sarcocystidean", "noun", "/ˌsɑːrkəsɪˈstɪdiən/", "trùng bào tử ký sinh cơ"),
    ("084889", "sarcocystieian", "noun", "/ˌsɑːrkəsɪˈstiːən/", "trùng bào tử ký sinh cơ"),
    ("084890", "sarcode", "noun", "/ˈsɑːrkoʊd/", "chất nguyên sinh động vật đơn bào"[:35]),
    ("084891", "sarcoderm", "noun", "/ˈsɑːrkəˌdɜːrm/", "lớp vỏ hạt nạc giữa"),
    ("084892", "sarcodes", "noun", "/sɑːrˈkoʊdiːz/", "chi cây tuyết đỏ Sarcodes"),
    ("084893", "sarcodic", "adj", "/sɑːrˈkɑːdɪk/", "thuộc chất nguyên sinh động vật"),
    ("084894", "sarcodina", "noun", "/ˌsɑːrkəˈdaɪnə/", "ngành Trùng chân giả (Sarcodina)"),
    ("084895", "sarcodine", "noun", "/ˈsɑːrkəˌdaɪn/", "trùng chân giả"),
    ("084896", "sarcodinian", "noun", "/ˌsɑːrkəˈdɪniən/", "động vật nguyên sinh chân giả"),
    ("084897", "sarcolemmal", "adj", "/ˌsɑːrkəˈlɛməl/", "thuộc màng sợi cơ"),
    ("084898", "sarcolemmic", "adj", "/ˌsɑːrkəˈlɛmɪk/", "thuộc màng sợi cơ"),
    ("084899", "sarcolemmik", "adj", "/ˌsɑːrkəˈlɛmɪk/", "thuộc màng sợi cơ"),
    ("084900", "sarcolemnous", "adj", "/ˌsɑːrkəˈlɛmnəs/", "thuộc màng sợi cơ"),
    ("084901", "sarcoline", "adj", "/ˈsɑːrkəˌlaɪn/", "có màu hồng thịt"),
    ("084902", "sarcological", "adj", "/ˌsɑːrkəˈlɑːdʒɪkəl/", "thuộc giải phẫu mô mềm"),
]

# Replace all 5 slice lines cleanly <= 35 chars
RECORDS[4] = ("084807", "sannup", "noun", "/ˈsænəp/", "đàn ông Mỹ bản địa có vợ")
RECORDS[8] = ("084811", "sansculottism", "noun", "/ˌsænzkjʊˈlɑːtɪzəm/", "chủ trương dân nghèo cách mạng Pháp"[:35])
RECORDS[8] = ("084811", "sansculottism", "noun", "/ˌsænzkjʊˈlɑːtɪzəm/", "tinh thần dân nghèo cách mạng Pháp")
RECORDS[58] = ("084861", "saprobic", "adj", "/sæˈproʊbɪk/", "hoại sinh; ưa chất hữu cơ phân hủy")
RECORDS[71] = ("084874", "saprozoic", "adj", "/ˌsæprəˈzoʊɪk/", "ăn chất hữu cơ phân hủy")
RECORDS[87] = ("084890", "sarcode", "noun", "/ˈsɑːrkoʊd/", "chất nguyên sinh đơn bào")

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b37_r10_raw_p4.json"))
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

json.dump(out, open("scratch/b37_r10_reviewed_p4.json", "w"), ensure_ascii=False, indent=2)
print("b37_r10_p4 saved OK")
