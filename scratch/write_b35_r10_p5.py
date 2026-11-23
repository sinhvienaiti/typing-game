import json

rows = [
    ("074903", "merlucciuses", "noun", "/mɜːrˈluːʃəsɪz/", "chi cá tuyết hake (Merluccius)"),
    ("074904", "metics", "noun", "/ˈmɛtɪks/", "kiều dân Hy Lạp cổ đại (metic)"),
    ("074905", "milvuses", "noun", "/ˈmɪlvəsɪz/", "chi diều hâu (Milvus)"),
    ("074906", "mongolics", "noun", "/mɒŋˈɡɒlɪks/", "người Mông Cổ; ngữ hệ Mông Cổ"),
    ("074907", "monosyllables", "noun", "/ˌmɒnəˈsɪləbəlz/", "từ đơn tiết (một âm tiết)"),
    ("074908", "muscidaes", "noun", "/ˈmʌsɪdiːz/", "họ ruồi nhà (Muscidae)"),
    ("074909", "myristicas", "noun", "/mɪˈrɪstɪkəz/", "chi cây nhục đậu khấu (Myristica)"),
    ("074910", "neckpieces", "noun", "/ˈnɛkˌpiːsɪz/", "vòng cổ; khăn lông choàng cổ"),
    ("074911", "nuptses", "noun", "/ˈnʊptsɪz/", "đỉnh núi Nuptse (dãy Himalaya)"),
    ("074912", "oligochaetes", "noun", "/ˌɒlɪɡəˈkiːts/", "lớp giun ít tơ (như giun đất)"),
    ("074913", "oraches", "noun", "/ˈɒrətʃɪz/", "cây rau muối tây (Atriplex)"),
    ("074914", "orderers", "noun", "/ˈɔːrdərərz/", "người đặt hàng; người sắp xếp"),
    ("074915", "pancreatectomies", "noun", "/ˌpæŋkriəˈtɛktəmiz/", "phẫu thuật cắt bỏ tuyến tụy"),
    ("074916", "passados", "noun", "/pəˈsɑːdoʊz/", "đòn đâm bước tới (đấu kiếm cổ)"),
    ("074917", "philtres", "noun", "/ˈfɪltərz/", "bùa yêu; thuốc kích tình (cổ)"),
    ("074918", "phoners", "noun", "/ˈfoʊnərz/", "người gọi điện; trạm điện thoại"),
    ("074919", "phosphocreatines", "noun", "/ˌfɒsfoʊˈkriːətiːnz/", "hợp chất cơ bắp phosphocreatin"),
    ("074920", "pileas", "noun", "/ˈpaɪliəz/", "chi cây lá gấm, bọ mắm (Pilea)"),
    ("074921", "promisors", "noun", "/ˈprɒmɪsərz/", "bên cam kết, người hứa (luật)"),
    ("074922", "psalteria", "noun", "/sɔːlˈtɪriə/", "dạ lá sách (nhai lại); đàn cổ"),
    ("074923", "psalteriums", "noun", "/sɔːlˈtɪriəmz/", "dạ lá sách (nhai lại); đàn cổ"),
    ("074924", "pseudococci", "noun", "/ˌsuːdəˈkɒksaɪ/", "chi rệp sáp phấn (Pseudococcus)"),
    ("074925", "rectoceles", "noun", "/ˈrɛktəˌsiːlz/", "chứng sa trực tràng (y học)"),
    ("074926", "refractorinesses", "noun", "/rɪˈfræktərinəsɪz/", "tính bướng bỉnh; tính chịu lửa"),
    ("074927", "salmonberries", "noun", "/ˈsæmənˌbɛriz/", "quả mâm xôi salmonberry (Bắc Mỹ)"),
    ("074928", "sarcophagas", "noun", "/sɑːrˈkɒfəɡəz/", "chi ruồi nhặng xám (Sarcophaga)"),
    ("074929", "scapegraces", "noun", "/ˈskeɪpˌɡreɪsɪz/", "kẻ vô lại; đứa trẻ nghịch ngợm"),
    ("074930", "scorpionfishes", "noun", "/ˈskɔːrpiənˌfɪʃɪz/", "cá mù làn; cá bò cạp biển"),
    ("074931", "secretors", "noun", "/sɪˈkriːtərz/", "người tiết kháng nguyên máu"),
    ("074932", "sonchuses", "noun", "/ˈsɒŋkəsɪz/", "chi cây diếp dại (Sonchus)"),
    ("074933", "sparkers", "noun", "/ˈspɑːrkərz/", "máy đánh điện; lưới chắn tia lửa"),
    ("074934", "spearpoints", "noun", "/ˈspɪrpɔɪnts/", "mũi giáo; đầu ngọn giáo"),
    ("074935", "sprags", "noun", "/spræɡz/", "cái chêm chặn bánh xe; thanh chống"),
    ("074936", "steatorrheas", "noun", "/ˌstiːətəˈriːəz/", "chứng đi ngoài phân mỡ (y học)"),
    ("074937", "synereses", "noun", "/sɪˈnɛrəsiːz/", "sự tách nước gel; gộp âm tiết"),
    ("074938", "tanginesses", "noun", "/ˈtæŋinəsɪz/", "vị chua gắt; mùi vị đậm đà"),
    ("074939", "tastebuds", "noun", "/ˈteɪstˌbʌdz/", "nụ vị giác (trên lưỡi)"),
    ("074940", "telopeas", "noun", "/təˈloʊpiəz/", "chi hoa chiến tranh Úc (Telopea)"),
    ("074941", "tephrosiae", "noun", "/tɪˈfroʊʒiiː/", "chi cây cốt khí (Tephrosia)"),
    ("074942", "thaumaturges", "noun", "/ˈθɔːməˌtɜːrdʒɪz/", "người làm phép lạ; ảo thuật gia"),
    ("074943", "tiebacks", "noun", "/ˈtaɪbæks/", "dây vén rèm cửa; thanh giằng tường"),
    ("074944", "timgads", "noun", "/ˈtɪmɡædz/", "thành phố La Mã cổ Timgad"),
    ("074945", "triatomas", "noun", "/ˌtraɪəˈtoʊməz/", "chi bọ xít hút máu (Triatoma)"),
    ("074946", "tungusics", "noun", "/tʊŋˈɡuːzɪks/", "người Tungus; ngữ hệ Tungus"),
    ("074947", "tupaias", "noun", "/tuːˈpaɪəz/", "chi đồi (chuột cây Tupaia)"),
    ("074948", "turbellarias", "noun", "/ˌtɜːrbəˈlɛriəz/", "lớp sán lông (Turbellaria)"),
    ("074949", "voluptuaries", "noun", "/vəˈlʌptʃuˌɛriz/", "người sống hưởng lạc xa hoa"),
    ("074950", "vulcanites", "noun", "/ˈvʌlkənaɪts/", "cao su cứng lưu hóa (ebonit)"),
    ("074951", "weltschmerzes", "noun", "/ˈvɛltˌʃmɛrtsɪz/", "nỗi sầu thế thái (triết học Đức)"),
    ("074952", "whizbangs", "noun", "/ˈwɪzbæŋz/", "pháo cao tốc (Thế chiến I); cái hay"),
    ("074953", "windcheaters", "noun", "/ˈwɪndˌtʃiːtərz/", "áo khoác chắn gió (áo gió)"),
    ("074954", "acaricides", "noun", "/əˈkærɪsaɪdz/", "thuốc diệt ve bét, nhện đỏ"),
    ("074955", "aldosteronisms", "noun", "/ælˈdɒstəroʊnɪzəmz/", "hội chứng cường aldosterone (y học)"),
    ("074956", "alocasias", "noun", "/ˌæləˈkeɪʒəz/", "chi cây môn ráy (Alocasia)"),
    ("074957", "alphabetizations", "noun", "/ˌælfəbɛtaɪˈzeɪʃənz/", "sự sắp xếp theo thứ tự chữ cái"),
    ("074958", "analysands", "noun", "/əˈnæləsændz/", "người được điều trị phân tâm học"),
    ("074959", "angiopathies", "noun", "/ˌændʒiˈɒpəθiz/", "bệnh lý mạch máu (y học)"),
    ("074960", "anglicisms", "noun", "/ˈæŋɡlɪsɪzəmz/", "cách nói kiểu Anh (trong ngôn ngữ)"),
    ("074961", "annwns", "noun", "/ˈænuːnz/", "âm phủ Annwn (thần thoại Xứ Wales)"),
    ("074962", "anorthites", "noun", "/əˈnɔːrθaɪts/", "khoáng vật fenspat anorthit"),
    ("074963", "arawakans", "noun", "/ˌærəˈwɑːkənz/", "người Arawak; ngữ hệ Arawak"),
    ("074964", "arrivers", "noun", "/əˈraɪvərz/", "người đến nơi; người thành đạt"),
    ("074965", "asangas", "noun", "/əˈsʌŋɡəz/", "luận sư Vô Trước (Asanga)"),
    ("074966", "asepses", "noun", "/eɪˈsɛpsiːz/", "trạng thái vô khuẩn, vô trùng"),
    ("074967", "ashtoreths", "noun", "/ˈæʃtəˌrɛθs/", "nữ thần Astarte (thần thoại cổ)"),
    ("074968", "asparaginases", "noun", "/æsˈpærədʒɪneɪsɪz/", "enzym asparaginase (trị ung thư)"),
    ("074969", "bargainers", "noun", "/ˈbɑːrɡɪnərz/", "người mặc cả, thương lượng"),
    ("074970", "baryteses", "noun", "/bəˈraɪtiːzɪz/", "khoáng vật barit (baryte)"),
    ("074971", "bedsitters", "noun", "/ˈbɛdsɪtərz/", "phòng trọ kiêm phòng khách (Anh)"),
    ("074972", "belemnites", "noun", "/bəˈlɛmnaɪts/", "hóa thạch mực cổ belemnit"),
    ("074973", "birdfeeders", "noun", "/ˈbɜːrdˌfiːdərz/", "máng cho chim ăn"),
    ("074974", "blintzes", "noun", "/ˈblɪntsɪz/", "bánh kếp cuộn nhân phô mai blintz"),
    ("074975", "bloodworms", "noun", "/ˈblʌdwɜːrmz/", "trùn chỉ đỏ (giun máu)"),
    ("074976", "blunderers", "noun", "/ˈblʌndərərz/", "người hay mắc lỗi ngớ ngẩn"),
    ("074977", "buglosses", "noun", "/ˈbjuːɡlɒsɪz/", "cây lưỡi bò (lưu ly dại)"),
    ("074978", "capricornuses", "noun", "/ˌkæprɪˈkɔːrnəsɪz/", "chòm sao Ma Kết; cung Ma Kết"),
    ("074979", "carnosaurs", "noun", "/ˈkɑːrnəˌsɔːrz/", "khủng long ăn thịt lớn (Carnosaur)"),
    ("074980", "catamites", "noun", "/ˈkætəmaɪts/", "bạn tình nam trẻ (Hy Lạp cổ đại)"),
    ("074981", "chalazions", "noun", "/kəˈleɪziɒnz/", "chắp mí mắt (nhãn khoa)"),
    ("074982", "cherrystones", "noun", "/ˈtʃɛriˌstoʊnz/", "sò nghêu vừa cherrystone"),
    ("074983", "chorines", "noun", "/kɔːˈriːnz/", "nữ diễn viên múa hát hợp xướng"),
    ("074984", "christianisations", "noun", "/ˌkrɪstʃənaɪˈzeɪʃənz/", "sự cải đạo sang Kitô giáo"),
    ("074985", "cives", "noun", "/saɪvz/", "cây hẹ tây; công dân (tiếng Latinh)"),
    ("074986", "cockaignes", "noun", "/kɒˈkeɪnz/", "xứ sở no đủ trong truyện dân gian"),
    ("074987", "comedos", "noun", "/kəˈmiːdoʊz/", "mụn đầu đen (mụn trứng cá)"),
    ("074988", "compeers", "noun", "/ˈkɒmpɪrz/", "bạn đồng cấp; người ngang hàng"),
    ("074989", "conceivabilities", "noun", "/kənˌsiːvəˈbɪlɪtiz/", "tính có thể hình dung được"),
    ("074990", "cortinariuses", "noun", "/ˌkɔːrtɪˈnɛriəsɪz/", "chi nấm tơ nhện Cortinarius"),
    ("074991", "corymbs", "noun", "/ˈkɒrɪmbz/", "cụm hoa ngù (thực vật học)"),
    ("074992", "cristobalites", "noun", "/krɪsˈtoʊbəlaɪts/", "khoáng vật thạch anh cristobalit"),
    ("074993", "cynocephaluses", "noun", "/ˌsaɪnoʊˈsɛfələsɪz/", "chi khỉ đầu chó; chồn bay"),
    ("074994", "danseurs", "noun", "/dɑːnˈsɜːrz/", "nam vũ công múa ba-lê"),
    ("074995", "dialyzers", "noun", "/ˈdaɪəlaɪzərz/", "máy lọc máu (máy thẩm phân)"),
    ("074996", "dracunculuses", "noun", "/drəˈkʌŋkjələsɪz/", "cây ráy rồng; giun Guinea"),
    ("074997", "drawees", "noun", "/drɔːˈiːz/", "người bị ký phát (hối phiếu)"),
    ("074998", "emberizas", "noun", "/ɛmˈbɛrɪzəz/", "chi chim sẻ đồng (Emberiza)"),
    ("074999", "endomorphs", "noun", "/ˈɛndəmɔːrfs/", "người tạng tròn mập (endomorph)"),
    ("075000", "epiglottitises", "noun", "/ˌɛpɪɡlɒˈtaɪtɪsɪz/", "bệnh viêm nắp thanh quản (y học)"),
    ("075001", "europans", "noun", "/jʊˈroʊpənz/", "dân châu Âu; dân vệ tinh Europa"),
    ("075002", "exchangeabilities", "noun", "/ɪksˌtʃeɪndʒəˈbɪlɪtiz/", "tính có thể trao đổi được"),
]

with open("scratch/b35_r10_raw_p5.json", "r", encoding="utf-8") as f:
    raw = json.load(f)

assert len(raw) == len(rows) == 100
out = []
for r, (rid, hw, pos, ipa, vi) in zip(raw, rows):
    assert r["id"].endswith("." + rid), f"ID mismatch: {r['id']} vs {rid}"
    assert r["hw"] == hw, f"HW mismatch: {r['hw']} vs {hw}"
    assert len(vi) <= 35, f"vi too long ({len(vi)}): {hw} -> {vi}"
    assert ipa.count("/") == 2 and not ipa[1:-1].startswith(" ") and not ipa[1:-1].endswith(" "), f"bad ipa: {hw} -> {ipa}"
    r["pos"] = pos
    r["ipa"] = ipa
    r["vi"] = vi
    r["status"] = "reviewed"
    out.append(r)

with open("scratch/b35_r10_p5.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b35_r10_p5 saved OK")
