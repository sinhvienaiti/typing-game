import json

items = [
    ("066103", "great mullein", "phrase", "/ɡreɪt ˈmʌlɪn/", "cây nhung thảo hoa vàng lớn"),
    ("066104", "greater omentum", "phrase", "/ˈɡreɪtər oʊˈmɛntəm/", "mạc nối lớn trong khoang bụng"),
    ("066105", "kadai language", "phrase", "/kəˈdaɪ ˈlæŋɡwɪdʒ/", "ngữ hệ Kra-Dai ở Đông Nam Á"),
    ("066106", "kobus leche", "phrase", "/ˈkoʊbəs ˈleɪtʃi/", "linh dương đầm lầy châu Phi"),
    ("066107", "le gallienne", "phrase", "/lə ˌɡæliˈɛn/", "nữ diễn viên Mỹ Le Gallienne"),
    ("066108", "legal jointure", "phrase", "/ˈliːɡəl ˈdʒɔɪntʃər/", "tài sản bảo đảm cho góa phụ"),
    ("066109", "lepus americanus", "phrase", "/ˈliːpəs əˌmɛrɪˈkeɪnəs/", "thỏ rừng tuyết trắng Bắc Mỹ"),
    ("066110", "lesser omentum", "phrase", "/ˈlɛsər oʊˈmɛntəm/", "mạc nối nhỏ nối gan và dạ dày"),
    ("066111", "lobar pneumonia", "phrase", "/ˈloʊbər nuːˈmoʊniə/", "bệnh viêm phổi thùy cấp tính"),
    ("066112", "lonicera flava", "phrase", "/ləˈnɪsərə ˈfleɪvə/", "cây kim ngân hoa vàng Bắc Mỹ"),
    ("066113", "luchino visconti", "phrase", "/luːˈkiːnoʊ vɪsˈkɒnti/", "đạo diễn điện ảnh Ý Visconti"),
    ("066114", "lumbosacral plexus", "phrase", "/ˌlʌmboʊˈseɪkrəl ˈplɛksəs/", "đám rối thần kinh thắt lưng cùng"),
    ("066115", "lyonnaise sauce", "phrase", "/ˌlaɪəˈneɪz sɔːs/", "xốt hành tây rượu vang Lyonnaise"),
    ("066116", "madia oil", "phrase", "/ˈmeɪdiə ɔɪl/", "dầu thực vật ép từ hạt madia"),
    ("066117", "madia oil plant", "phrase", "/ˈmeɪdiə ɔɪl plænt/", "cây cúc lấy dầu hạt madia"),
    ("066118", "malignant hepatoma", "phrase", "/məˈlɪɡnənt ˌhɛpəˈtoʊmə/", "ung thư biểu mô tế bào gan"),
    ("066119", "marquise de montespan", "phrase", "/mɑːrˈkiːz də ˌmɒntəˈspɒn/", "Nữ hầu tước Pháp de Montespan"),
    ("066120", "mullein pink", "phrase", "/ˈmʌlɪn pɪŋk/", "cây cẩm chướng lông trắng đỏ"),
    ("066121", "musculus serratus anterior", "phrase", "/ˈmʌskjələs sɛˈreɪtəs ænˈtɪriər/", "cơ răng trước vùng mạn sườn"),
    ("066122", "musculus serratus posterior", "phrase", "/ˈmʌskjələs sɛˈreɪtəs pɒˈstɪriər/", "cơ răng sau ở vùng lưng"),
    ("066123", "nymphaea alba", "phrase", "/nɪmˈfiːə ˈælbə/", "hoa súng trắng châu Âu"),
    ("066124", "olde worlde", "phrase", "/ˌoʊldi ˈwɜːrldi/", "kiểu cổ kính giả tạo; hoài cổ"),
    ("066125", "os frontale", "phrase", "/ɒs frɒnˈteɪli/", "xương trán của hộp sọ"),
    ("066126", "palmate leaf", "phrase", "/ˈpælmeɪt liːf/", "lá xẻ thùy hình chân vịt"),
    ("066127", "picric acid", "phrase", "/ˈpɪkrɪk ˈæsɪd/", "axit picric dễ nổ màu vàng"),
    ("066128", "pinus contorta", "phrase", "/ˈpaɪnəs kənˈtɔːrtə/", "cây thông vặn lá xoắn Bắc Mỹ"),
    ("066129", "prunus persica", "phrase", "/ˈpruːnəs ˈpɜːrsɪkə/", "cây đào ăn quả họ Hoa hồng"),
    ("066130", "purple mullein", "phrase", "/ˈpɜːrpəl ˈmʌlɪn/", "cây nhung thảo hoa tím"),
    ("066131", "remoulade sauce", "phrase", "/ˌrɛməˈlɑːd sɔːs/", "xốt kem chua thảo mộc remoulade"),
    ("066132", "rosh hashana", "phrase", "/ˌrɒʃ həˈʃɑːnə/", "lễ Tết cổ truyền Do Thái"),
    ("066133", "sciurus niger", "phrase", "/saɪˈjʊərəs ˈnaɪdʒər/", "loài sóc cáo phương Đông Bắc Mỹ"),
    ("066134", "simon legree", "phrase", "/ˈsaɪmən ləˈɡriː/", "chủ nô tàn ác Simon Legree"),
    ("066135", "sir john tenniel", "phrase", "/sɜːr dʒɒn ˈtɛniəl/", "họa sĩ minh họa Anh John Tenniel"),
    ("066136", "solidago bicolor", "phrase", "/ˌsɒlɪˈdeɪɡoʊ baɪˈkʌlər/", "cây hoàng anh hoa trắng Bắc Mỹ"),
    ("066137", "sorbus americana", "phrase", "/ˈsɔːrbəs əˌmɛrɪˈkeɪnə/", "cây thanh lương trà châu Mỹ"),
    ("066138", "steak au poivre", "phrase", "/steɪk oʊ ˈpwɑːvrə/", "bít tết bò rắc hạt tiêu Pháp"),
    ("066139", "string quartette", "phrase", "/strɪŋ kwɔːrˈtɛt/", "nhóm tứ tấu nhạc cụ dây"),
    ("066140", "triticum durum", "phrase", "/ˈtrɪtɪkəm ˈdjʊərəm/", "lúa mì cứng làm mì Ý"),
    ("066141", "ulmus glabra", "phrase", "/ˈʌlməs ˈɡleɪbrə/", "cây du núi Wych châu Âu"),
    ("066142", "vaccinium pallidum", "phrase", "/vækˈsɪniəm ˈpælɪdəm/", "cây việt quất sườn núi Bắc Mỹ"),
    ("066143", "verd antique", "phrase", "/vɜːrd ænˈtiːk/", "đá cẩm thạch xanh vân trắng cổ"),
    ("066144", "white mullein", "phrase", "/waɪt ˈmʌlɪn/", "cây nhung thảo hoa trắng"),
    ("066145", "whited sepulcher", "phrase", "/ˈwaɪtɪd ˈsɛpəlkər/", "kẻ giả nhân giả nghĩa; mồ tô vôi"),
    ("066146", "adelies", "noun", "/ˈædəliz/", "chim cánh cụt Adélie Nam Cực"),
    ("066147", "alienists", "noun", "/ˈeɪliənɪsts/", "bác sĩ tâm thần pháp y (từ cũ)"),
    ("066148", "arboricultures", "noun", "/ˈɑːrbərɪˌkʌltʃərz/", "nghề trồng và chăm sóc cây gỗ"),
    ("066149", "asteraceaes", "noun", "/ˌæstəˈreɪʃiz/", "họ thực vật Cúc Asteraceae"),
    ("066150", "atenolols", "noun", "/əˈtɛnəˌlɒlz/", "thuốc chẹn beta trị huyết áp"),
    ("066151", "bagasses", "noun", "/bəˈɡæsɪz/", "bã mía sau khi ép lấy nước đường"),
    ("066152", "banquettes", "noun", "/bæŋˈkɛts/", "ghế băng bọc nệm kê sát tường"),
    ("066153", "birders", "noun", "/ˈbɜːrdərz/", "người quan sát chim hoang dã"),
    ("066154", "blackbodies", "noun", "/ˈblækˌbɒdiz/", "vật đen tuyệt đối (vật lý)"),
    ("066155", "brummells", "noun", "/ˈbrʌməlz/", "nhân vật sành điệu Beau Brummell"),
    ("066156", "cairngorms", "noun", "/ˈkɛərnˌɡɔːrmz/", "đá thạch anh khói vàng nâu"),
    ("066157", "cellblocks", "noun", "/ˈsɛlˌblɒks/", "khu dãy phòng giam trong nhà tù"),
    ("066158", "chenopodiums", "noun", "/ˌkiːnəˈpoʊdiəmz/", "cây rau muối chi Chenopodium"),
    ("066159", "chloramines", "noun", "/ˈklɔːrəˌmiːnz/", "hợp chất khử trùng nước cloramin"),
    ("066160", "cholangitides", "noun", "/koʊˌlændʒɪˈtaɪdɪz/", "bệnh viêm đường ống dẫn mật"),
    ("066161", "cholinesterases", "noun", "/ˌkoʊlɪˈnɛstəreɪsɪz/", "enzym phân hủy chất dẫn truyền"),
    ("066162", "cocains", "noun", "/koʊˈkeɪnz/", "chất kích thích gây nghiện cocain"),
    ("066163", "cognomens", "noun", "/kɒɡˈnoʊmənz/", "biệt danh; tên họ phụ La Mã cổ"),
    ("066164", "cognomina", "noun", "/kɒɡˈnɒmɪnə/", "tên hiệu phụ La Mã; biệt danh"),
    ("066165", "colobuses", "noun", "/ˈkɒləbəsɪz/", "khỉ colobus sống trên cây châu Phi"),
    ("066166", "countertenors", "noun", "/ˌkaʊntərˈtɛnərz/", "nam ca sĩ hát giọng phản nam cao"),
    ("066167", "czarinas", "noun", "/zɑːˈriːnəz/", "nữ hoàng hoặc hoàng hậu Nga hoàng"),
    ("066168", "deadeyes", "noun", "/ˈdɛdˌaɪz/", "con đội dây buồm; xạ thủ thiện xạ"),
    ("066169", "denouncements", "noun", "/dɪˈnaʊnsmənts/", "sự tố cáo lên án công khai"),
    ("066170", "dicers", "noun", "/ˈdaɪsərz/", "dụng cụ hoặc máy thái hạt lựu"),
    ("066171", "disulfirams", "noun", "/daɪˈsʌlfɪˌræmz/", "thuốc hỗ trợ cai nghiện rượu"),
    ("066172", "dovecotes", "noun", "/ˈdʌvˌkoʊts/", "chuồng mái cao nuôi chim bồ câu"),
    ("066173", "enalaprils", "noun", "/ɪˈnæləˌprɪlz/", "thuốc ức chế men chuyển enalapril"),
    ("066174", "eosinophilias", "noun", "/ˌiːəˌsɪnəˈfɪliəz/", "tình trạng tăng bạch cầu ái toan"),
    ("066175", "epees", "noun", "/eɪˈpeɪz/", "kiếm ba cạnh đấu thể thao épée"),
    ("066176", "epididymides", "noun", "/ˌɛpɪdɪˈdɪmɪdiːz/", "mào tinh hoàn dẫn tinh trùng"),
    ("066177", "fasciculi", "noun", "/fəˈsɪkjəˌlaɪ/", "bó sợi thần kinh hoặc bó sợi cơ"),
    ("066178", "fatalists", "noun", "/ˈfeɪtəlɪsts/", "người tin vào thuyết định mệnh"),
    ("066179", "fleecier", "adj", "/ˈfliːsiər/", "mềm xốp như lông cừu hơn"),
    ("066180", "fleeciest", "adj", "/ˈfliːsiɪst/", "mềm xốp như lông cừu nhất"),
    ("066181", "floricultures", "noun", "/ˈflɔːrɪˌkʌltʃərz/", "ngành nghề trồng hoa và cây cảnh"),
    ("066182", "fontanelles", "noun", "/ˌfɒntəˈnɛlz/", "thóp mềm trên đỉnh đầu trẻ sơ sinh"),
    ("066183", "ganapatis", "noun", "/ɡəˈnɑːpətiz/", "thần đầu voi Ganapati Ấn Độ"),
    ("066184", "gitanos", "noun", "/hɪˈtɑːnoʊz/", "người Digan sinh sống ở Tây Ban Nha"),
    ("066185", "goldonis", "noun", "/ɡoʊlˈdoʊniz/", "nhà soạn kịch Ý Carlo Goldoni"),
    ("066186", "gorgases", "noun", "/ˈɡɔːrɡəsɪz/", "bác sĩ quân y Mỹ William Gorgas"),
    ("066187", "hokas", "noun", "/ˈhoʊkəz/", "nhóm ngôn ngữ bản địa Hoka"),
    ("066188", "houseflies", "noun", "/ˈhaʊsˌflaɪz/", "ruồi nhà thường gặp"),
    ("066189", "hydroxychloroquines", "noun", "/haɪˌdrɒksiˈklɔːrəˌkwiːnz/", "thuốc trị sốt rét và tự miễn"),
    ("066190", "ibrds", "noun", "/aɪ biː ɑːr ˈdiːz/", "Ngân hàng Tái thiết và Phát triển"),
    ("066191", "issuses", "noun", "/ˈɪsəsɪz/", "trận đánh cổ đại Issus"),
    ("066192", "kaolinites", "noun", "/ˈkeɪəlɪˌnaɪts/", "khoáng vật đất sét kaolinit"),
    ("066193", "kbos", "noun", "/ˌkeɪ biː ˈoʊz/", "thiên thể vành đai Kuiper"),
    ("066194", "macers", "noun", "/ˈmeɪsərz/", "người vác chùy nghi lễ hoàng gia"),
    ("066195", "mantissas", "noun", "/mænˈtɪsəz/", "phần định trị số; phần thập phân"),
    ("066196", "marmoras", "noun", "/ˈmɑːrmərəz/", "biển Marmara ở Thổ Nhĩ Kỳ"),
    ("066197", "mediastina", "noun", "/ˌmiːdiəˈstaɪnə/", "khoang trung thất giữa hai lá phổi"),
    ("066198", "mediastinums", "noun", "/ˌmiːdiəˈstaɪnəmz/", "khoang trung thất trong lồng ngực"),
    ("066199", "misinformed", "verb", "/ˌmɪsɪnˈfɔːrmd/", "đã cung cấp thông tin sai lệch"),
    ("066200", "misinforming", "verb", "/ˌmɪsɪnˈfɔːrmɪŋ/", "đang cung cấp thông tin sai lệch"),
    ("066201", "misinforms", "verb", "/ˌmɪsɪnˈfɔːrmz/", "cung cấp thông tin sai sự thật"),
    ("066202", "moorcocks", "noun", "/ˈmʊərˌkɒks/", "gà gô đỏ trống vùng đồng hoang"),
]

with open("scratch/b34_r03_raw_p2.json") as f:
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

with open("scratch/b34_r03_p2.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r03_p2.json OK")
