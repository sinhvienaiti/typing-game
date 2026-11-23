import json

RECORDS = [
    ("088003", "solanine", "noun", "/ˈsɑːləˌniːn/", "chất độc solanin (trong khoai tây)"),
    ("088004", "solanopteris", "noun", "/ˌsɑːləˈnɑːptərɪs/", "chi dương xỉ củ Solanopteris"),
    ("088005", "solaria", "noun", "/soʊˈlɛriə/", "phòng tắm nắng kính; đồng hồ mặt"[:35]),
    ("088006", "solarisation", "noun", "/ˌsoʊlərəˈzeɪʃən/", "sự phơi nắng; hiệu ứng đảo ảnh"),
    ("088007", "solarise", "verb", "/ˈsoʊləˌraɪz/", "phơi nắng; đảo tông ảnh do sáng"),
    ("088008", "solarize", "verb", "/ˈsoʊləˌraɪz/", "phơi nắng; đảo tông ảnh do sáng"),
    ("088009", "solatia", "noun", "/soʊˈleɪʃə/", "tiền bồi thường tổn thất tinh thần"),
    ("088010", "solatium", "noun", "/soʊˈleɪʃəm/", "tiền bồi thường tổn thất tinh thần"),
    ("088011", "soldanella", "noun", "/ˌsɑːldəˈnɛlə/", "hoa chuông tuyết vùng núi tuyết"),
    ("088012", "solderability", "noun", "/ˌsɑːdərəˈbɪlɪti/", "tính dễ hàn; khả năng bám thiếc"),
    ("088013", "solderable", "adj", "/ˈsɑːdərəbəl/", "có thể hàn thiếc được"),
    ("088014", "soldered", "verb", "/ˈsɑːdərd/", "đã hàn thiếc; đã gắn kết chặt"),
    ("088015", "solderer", "noun", "/ˈsɑːdərər/", "thợ hàn; mỏ hàn thiếc"),
    ("088016", "solders", "verb", "/ˈsɑːdərz/", "hàn thiếc; gắn chặt lại"),
    ("088017", "soldiered", "verb", "/ˈsoʊldʒərd/", "đã đi lính; đã kiên trì vượt khó"),
    ("088018", "soldierfish", "noun", "/ˈsoʊldʒərˌfɪʃ/", "cá sơn đá mắt to họ Holocentridae"),
    ("088019", "soldierlike", "adj", "/ˈsoʊldʒərˌlaɪk/", "oai nghiêm dũng cảm như người lính"),
    ("088020", "soldiers", "verb", "/ˈsoʊldʒərz/", "làm lính; kiên trì chịu đựng"),
    ("088021", "soldiership", "noun", "/ˈsoʊldʒərˌʃɪp/", "kỹ năng quân sự; phẩm chất lính"),
    ("088022", "soldo", "noun", "/ˈsɑːldoʊ/", "đồng xu đồng cổ soldo của Ý"),
    ("088023", "solecist", "noun", "/ˈsɑːlɪsɪst/", "người hay dùng sai ngữ pháp"),
    ("088024", "solecistic", "adj", "/ˌsɑːlɪˈsɪstɪk/", "sai ngữ pháp; lỗi cách hành xử"),
    ("088025", "soleidae", "noun", "/soʊˈliːɪˌdiː/", "họ Cá bơn lưỡi trâu (Soleidae)"),
    ("088026", "soleirolia", "noun", "/ˌsɑːlɪˈroʊliə/", "cây cỏ mắt em bé (Soleirolia)"),
    ("088027", "soleless", "adj", "/ˈsoʊlləs/", "không có đế giày"),
    ("088028", "solemness", "noun", "/ˈsɑːləmnəs/", "vẻ trang nghiêm; sự nghiêm trang"),
    ("088029", "solemnised", "verb", "/ˈsɑːləmˌnaɪzd/", "đã cử hành long trọng (hôn lễ)"),
    ("088030", "solemnises", "verb", "/ˈsɑːləmˌnaɪzɪz/", "cử hành nghi lễ long trọng"),
    ("088031", "solemnising", "verb", "/ˈsɑːləmˌnaɪzɪŋ/", "đang cử hành nghi lễ long trọng"),
    ("088032", "solemnized", "verb", "/ˈsɑːləmˌnaɪzd/", "đã cử hành long trọng (hôn lễ)"),
    ("088033", "solemnizer", "noun", "/ˈsɑːləmˌnaɪzər/", "người chủ trì nghi lễ hôn phối"),
    ("088034", "solemnizes", "verb", "/ˈsɑːləmˌnaɪzɪz/", "cử hành nghi lễ long trọng"),
    ("088035", "solemnizing", "verb", "/ˈsɑːləmˌnaɪzɪŋ/", "đang cử hành nghi lễ long trọng"),
    ("088036", "solemnness", "noun", "/ˈsɑːləmnəs/", "sự trang nghiêm; tính long trọng"),
    ("088037", "solenette", "noun", "/ˌsɑːləˈnɛt/", "cá bơn vàng nhỏ châu Âu"),
    ("088038", "solenichthyes", "noun", "/ˌsoʊləˈnɪkθiˌiːz/", "bộ Cá chìa vôi và cá ngựa"),
    ("088039", "solenidae", "noun", "/səˈlɛnɪˌdiː/", "họ Ngao móng tay (Solenidae)"),
    ("088040", "solenogaster", "noun", "/səˌliːnoʊˈɡæstər/", "thân mềm không vỏ dạng giun biển"),
    ("088041", "solenogastres", "noun", "/səˌliːnoʊˈɡæstriːz/", "lớp Thân mềm không vỏ Solenogastres"[:35]),
    ("088042", "solenoidal", "adj", "/ˌsɑːləˈnɔɪdəl/", "dạng ống dây điện từ solenoid"),
    ("088043", "solenostemon", "noun", "/səˌlɛnəˈstiːmɑːn/", "chi cây tía tô cảnh lá gấm"),
    ("088044", "soles", "verb", "/soʊlz/", "đóng lại đế giày"),
    ("088045", "solfatara", "noun", "/ˌsɑːlfəˈtɑːrə/", "miệng núi lửa phun khí lưu huỳnh"),
    ("088046", "solicitant", "noun", "/səˈlɪsətənt/", "người khẩn cầu; người xin phép"),
    ("088047", "solicited", "verb", "/səˈlɪsɪtɪd/", "đã khẩn khoản xin; đã chèo kéo"),
    ("088048", "soliciting", "verb", "/səˈlɪsɪtɪŋ/", "đang xin tài trợ; đang chèo kéo"),
    ("088049", "solicitors", "noun", "/səˈlɪsɪtərz/", "luật sư tư vấn; nhân viên chào mời"),
    ("088050", "solicitorship", "noun", "/səˈlɪsɪtərˌʃɪp/", "chức vụ luật sư cố vấn pháp lý"),
    ("088051", "solicitousness", "noun", "/səˈlɪsətəsnəs/", "sự quan tâm lo lắng ân cần"),
    ("088052", "solicits", "verb", "/səˈlɪsɪts/", "kêu gọi đóng góp; chèo kéo mời"),
    ("088053", "solidarism", "noun", "/ˈsɑːlɪdəˌrɪzəm/", "chủ nghĩa liên đới xã hội"),
    ("088054", "solidarist", "noun", "/ˈsɑːlɪdərɪst/", "người theo chủ nghĩa liên đới"),
    ("088055", "solidary", "adj", "/ˈsɑːlɪˌdɛri/", "đoàn kết; liên đới trách nhiệm"),
    ("088056", "solidifiable", "adj", "/səˈlɪdəˌfaɪəbəl/", "có thể hóa rắn; đóng đặc được"),
    ("088057", "solidifies", "verb", "/səˈlɪdəˌfaɪz/", "hóa rắn; củng cố vững chắc"),
    ("088058", "solidungular", "adj", "/ˌsɑːlɪˈdʌŋɡjələr/", "có một móng guốc đơn (họ Ngựa)"),
    ("088059", "solidungulate", "adj", "/ˌsɑːlɪˈdʌŋɡjəlɪt/", "có một móng guốc đơn"),
    ("088060", "solifidian", "noun", "/ˌsɑːlɪˈfɪdiən/", "người theo thuyết duy tín cứu rỗi"),
    ("088061", "solifluction", "noun", "/ˌsɑːlɪˈflʌkʃən/", "hiện tượng trượt đất băng tan"),
    ("088062", "soliloquise", "verb", "/səˈlɪləˌkwaɪz/", "độc thoại một mình"),
    ("088063", "soliloquised", "verb", "/səˈlɪləˌkwaɪzd/", "đã độc thoại một mình"),
    ("088064", "soliloquises", "verb", "/səˈlɪləˌkwaɪzɪz/", "độc thoại một mình"),
    ("088065", "soliloquising", "verb", "/səˈlɪləˌkwaɪzɪŋ/", "đang độc thoại một mình"),
    ("088066", "soliloquist", "noun", "/səˈlɪləkwɪst/", "người hay nói một mình; độc thoại"),
    ("088067", "soliloquize", "verb", "/səˈlɪləˌkwaɪz/", "độc thoại; nói lẩm bẩm một mình"),
    ("088068", "soliloquized", "verb", "/səˈlɪləˌkwaɪzd/", "đã độc thoại; đã nói một mình"),
    ("088069", "soliloquizes", "verb", "/səˈlɪləˌkwaɪzɪz/", "độc thoại; nói một mình"),
    ("088070", "soliloquizing", "verb", "/səˈlɪləˌkwaɪzɪŋ/", "đang độc thoại; đang nói một mình"),
    ("088071", "soling", "verb", "/ˈsoʊlɪŋ/", "đang đóng đế giày"),
    ("088072", "soliped", "adj", "/ˈsɑːləˌpɛd/", "có một móng guốc đơn (như ngựa)"),
    ("088073", "solipsist", "noun", "/ˈsɑːləpsɪst/", "người theo thuyết duy ngã"),
    ("088074", "solipsistic", "adj", "/ˌsɑːləpˈsɪstɪk/", "thuộc thuyết duy ngã; chỉ biết mình"[:35]),
    ("088075", "solitariness", "noun", "/ˈsɑːləˌtɛrinəs/", "cảnh cô độc; sự sống tách biệt"),
    ("088076", "solitudes", "noun", "/ˈsɑːləˌtuːdz/", "cảnh cô đơn; nơi vắng vẻ hẻo lánh"),
    ("088077", "solitudinarian", "noun", "/ˌsɑːlɪˌtuːdɪˈnɛriən/", "người thích sống ẩn dật một mình"),
    ("088078", "solleret", "noun", "/ˈsɑːlərɪt/", "giày sắt bộ giáp hiệp sĩ xưa"),
    ("088079", "solmisation", "noun", "/ˌsɑːlmɪˈzeɪʃən/", "hệ thống xướng âm Đô Rê Mi"),
    ("088080", "solmizate", "verb", "/ˈsɑːlmɪˌzeɪt/", "hát xướng âm theo nốt nhạc"),
    ("088081", "solmization", "noun", "/ˌsɑːlmɪˈzeɪʃən/", "hệ thống xướng âm Đô Rê Mi"),
    ("088082", "solresol", "noun", "/ˈsoʊlrɛˌsɔːl/", "ngôn ngữ âm nhạc nhân tạo Solresol"),
    ("088083", "solstitial", "adj", "/sɑːlˈstɪʃəl/", "thuộc ngày hạ chí hoặc đông chí"),
    ("088084", "solubilization", "noun", "/ˌsɑːljəbələˈzeɪʃən/", "sự làm tăng độ hòa tan"),
    ("088085", "solubilize", "verb", "/ˈsɑːljəbəˌlaɪz/", "làm cho hòa tan được"),
    ("088086", "solubleness", "noun", "/ˈsɑːljəbəlnəs/", "tính hòa tan được"),
    ("088087", "solus", "adj", "/ˈsoʊləs/", "một mình trên sân khấu (kịch)"),
    ("088088", "solutionist", "noun", "/səˈluːʃənɪst/", "người chuyên giải câu đố hay vấn đề"[:35]),
    ("088089", "solventless", "adj", "/ˈsɑːlvəntləs/", "không chứa dung môi"),
    ("088090", "solves", "verb", "/sɑːlvz/", "giải quyết; giải mã; tìm đáp án"),
    ("088091", "solvolysis", "noun", "/sɑːlˈvɑːləsɪs/", "phản ứng phân ly bởi dung môi"),
    ("088092", "solvus", "noun", "/ˈsɑːlvəs/", "đường giới hạn độ hòa tan pha rắn"),
    ("088093", "somaesthesia", "noun", "/ˌsoʊməsˈθiːʒə/", "cảm giác thân thể xúc giác bản thể"),
    ("088094", "somaesthesis", "noun", "/ˌsoʊməsˈθiːsɪs/", "hệ cảm giác thân thể"),
    ("088095", "somataesthesis", "noun", "/ˌsoʊmətəsˈθiːsɪs/", "hệ cảm giác thân thể"),
    ("088096", "somateria", "noun", "/ˌsoʊməˈtɪriə/", "chi vịt biển Eider (Somateria)"),
    ("088097", "somatesthesia", "noun", "/ˌsoʊmətəsˈθiːʒə/", "cảm giác thân thể"),
    ("088098", "somatically", "adv", "/soʊˈmætɪkli/", "về mặt thể xác; thuộc tế bào thân"),
    ("088099", "somatogenetic", "adj", "/ˌsoʊmətoʊdʒəˈnɛtɪk/", "có nguồn gốc thực thể sinh lý"),
    ("088100", "somatogenic", "adj", "/ˌsoʊmətoʊˈdʒɛnɪk/", "có nguồn gốc thực thể sinh lý"),
    ("088101", "somatologic", "adj", "/ˌsoʊmətəˈlɑːdʒɪk/", "thuộc nhân chủng học hình thể"),
    ("088102", "somatologies", "noun", "/ˌsoʊməˈtɑːlədʒiz/", "nhân trắc hình thể học"),
]

# Cleanly shorten slices / >35 chars
RECORDS[2] = ("088005", "solaria", "noun", "/soʊˈlɛriə/", "phòng tắm nắng; đồng hồ mặt trời")
RECORDS[38] = ("088041", "solenogastres", "noun", "/səˌliːnoʊˈɡæstriːz/", "lớp Thân mềm không vỏ biển sâu")
RECORDS[71] = ("088074", "solipsistic", "adj", "/ˌsɑːləpˈsɪstɪk/", "duy ngã; chỉ biết mỗi bản thân")
RECORDS[85] = ("088088", "solutionist", "noun", "/səˈluːʃənɪst/", "người chuyên giải đố; tìm giải pháp"[:35])
RECORDS[85] = ("088088", "solutionist", "noun", "/səˈluːʃənɪst/", "người chuyên giải đố hay tìm cách")

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b38_r07_raw_p1.json"))
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

json.dump(out, open("scratch/b38_r07_reviewed_p1.json", "w"), ensure_ascii=False, indent=2)
print("b38_r07_p1 saved OK")
