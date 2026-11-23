import json

items = [
    ("066903", "archduchesses", "noun", "/ˌɑːrtʃˈdʌtʃɪsɪz/", "nữ đại công tước hoàng gia Áo"),
    ("066904", "atomisms", "noun", "/ˈætəˌmɪzəmz/", "thuyết nguyên tử cổ đại triết học"),
    ("066905", "baronetcies", "noun", "/ˈbærənɪtsiz/", "tước vị nam tước thế tập Anh"),
    ("066906", "basilei", "noun", "/ˈbæsɪleɪ/", "hoàng đế Byzantine Hy Lạp cổ"),
    ("066907", "basileis", "noun", "/ˈbæsɪleɪs/", "vua hoặc hoàng đế Hy Lạp cổ đại"),
    ("066908", "bedeviled", "verb", "/bɪˈdɛvəld/", "đã quấy rầy hành hạ; gây rắc rối"),
    ("066909", "bedeviling", "verb", "/bɪˈdɛvəlɪŋ/", "đang quấy rầy hành hạ; gây rối"),
    ("066910", "belorussias", "noun", "/ˌbɛloʊˈrʌʃəz/", "nước Belarus (cách gọi cũ)"),
    ("066911", "boucles", "noun", "/buːˈkleɪz/", "vải sợi xoắn xù bề mặt bouclé"),
    ("066912", "breadlines", "noun", "/ˈbrɛdˌlaɪnz/", "hàng người chờ nhận đồ ăn từ thiện"),
    ("066913", "brockets", "noun", "/ˈbrɒkɪts/", "hươu nhỏ Nam Mỹ sừng ngắn đơn"),
    ("066914", "buncoed", "verb", "/ˈbʌŋkoʊd/", "đã lừa đảo bịp bợm chiếm đoạt"),
    ("066915", "buncoing", "verb", "/ˈbʌŋkoʊɪŋ/", "đang lừa đảo bịp bợm (Mỹ)"),
    ("066916", "buncos", "noun", "/ˈbʌŋkoʊz/", "trò lừa đảo gian lận bịp bợm"),
    ("066917", "bunkos", "noun", "/ˈbʌŋkoʊz/", "trò lừa đảo bịp bợm đánh bạc"),
    ("066918", "caldrons", "noun", "/ˈkɔːldrənz/", "cái vạc lớn nấu sôi trên bếp lửa"),
    ("066919", "carbamates", "noun", "/ˈkɑːrbəˌmeɪts/", "hợp chất hữu cơ thuốc trừ sâu"),
    ("066920", "cardias", "noun", "/ˈkɑːrdiəz/", "lỗ tâm vị nối thực quản và dạ dày"),
    ("066921", "chromaticities", "noun", "/ˌkroʊməˈtɪsɪtiz/", "độ sắc độ thuần khiết của màu sắc"),
    ("066922", "cockades", "noun", "/kɒˈkeɪdz/", "huy hiệu nơ tròn gắn trên mũ"),
    ("066923", "cooperators", "noun", "/koʊˈɒpəˌreɪtərz/", "người hợp tác cùng làm việc chung"),
    ("066924", "copals", "noun", "/ˈkoʊpəlz/", "nhựa cây copal hóa thạch làm sơn"),
    ("066925", "copybooks", "noun", "/ˈkɒpiˌbʊks/", "vở tập viết chữ mẫu cho học sinh"),
    ("066926", "cordwoods", "noun", "/ˈkɔːrdˌwʊdz/", "củi xếp đống đo theo thước cord"),
    ("066927", "cotopaxis", "noun", "/ˌkoʊtoʊˈpæksiz/", "núi lửa Cotopaxi ở Ecuador"),
    ("066928", "cowries", "noun", "/ˈkaʊriz/", "vỏ ốc sứ bóng dùng làm tiền cổ"),
    ("066929", "determinists", "noun", "/dɪˈtɜːrmɪnɪsts/", "người theo thuyết tất định triết"),
    ("066930", "digitised", "verb", "/ˈdɪdʒɪˌtaɪzd/", "đã chuyển đổi sang dạng số hóa"),
    ("066931", "digitises", "verb", "/ˈdɪdʒɪˌtaɪzɪz/", "số hóa dữ liệu văn bản hình ảnh"),
    ("066932", "digitising", "verb", "/ˈdɪdʒɪˌtaɪzɪŋ/", "đang số hóa dữ liệu điện tử"),
    ("066933", "directivities", "noun", "/ˌdaɪrɛkˈtɪvɪtiz/", "tính định hướng phát sóng ăng-ten"),
    ("066934", "disfunctions", "noun", "/dɪsˈfʌŋkʃənz/", "sự rối loạn suy giảm chức năng"),
    ("066935", "disturbers", "noun", "/dɪˈstɜːrbərz/", "kẻ quấy rối gây mất trật tự"),
    ("066936", "doublethinks", "noun", "/ˈdʌbəlˌθɪŋks/", "lối tư duy nước đôi tự mâu thuẫn"),
    ("066937", "dragunovs", "noun", "/drəˈɡuːnɒfs/", "súng trường bắn tỉa Dragunov Nga"),
    ("066938", "effectivities", "noun", "/ˌɛfɛkˈtɪvɪtiz/", "tính hiệu lực; hiệu quả thực thi"),
    ("066939", "estragons", "noun", "/ˈɛstrəˌɡɒnz/", "cây ngải giấm tarragon làm gia vị"),
    ("066940", "exemplifications", "noun", "/ɪɡˌzɛmplɪfɪˈkeɪʃənz/", "sự minh họa bằng ví dụ điển hình"),
    ("066941", "extravasations", "noun", "/ɛkˌstrævəˈzeɪʃənz/", "hiện tượng dịch máu thoát ra ngoài"),
    ("066942", "florets", "noun", "/ˈflɒrɪts/", "bông hoa nhỏ li ti trên cụm hoa"),
    ("066943", "foredecks", "noun", "/ˈfɔːrˌdɛks/", "phần boong mũi phía trước con tàu"),
    ("066944", "forenoons", "noun", "/ˈfɔːrˌnuːnz/", "buổi sáng trước giờ trưa"),
    ("066945", "frangipanes", "noun", "/ˈfrændʒɪˌpænz/", "kem bánh hạnh nhân; cây hoa đại"),
    ("066946", "friers", "noun", "/ˈfraɪərz/", "gà non để rán; nồi chiên ngập dầu"),
    ("066947", "furans", "noun", "/ˈfjʊərænz/", "hợp chất vòng thơm dị tố furan"),
    ("066948", "gerberas", "noun", "/ˈdʒɜːrbərəz/", "hoa đồng tiền nhiều màu sặc sỡ"),
    ("066949", "glendowers", "noun", "/ɡlɛnˈdaʊərz/", "thủ lĩnh xứ Wales Owain Glyndŵr"),
    ("066950", "godels", "noun", "/ˈɡɜːdəlz/", "nhà toán học logic Kurt Gödel"),
    ("066951", "grosbeaks", "noun", "/ˈɡroʊsˌbiːks/", "chim sẻ mỏ dày cứng ăn hạt"),
    ("066952", "gyrations", "noun", "/dʒaɪˈreɪʃənz/", "chuyển động xoay tròn liên tục"),
    ("066953", "helsingforses", "noun", "/ˈhɛlsɪŋˌfɔːrsɪz/", "tên cổ của thủ đô Helsinki"),
    ("066954", "hexameters", "noun", "/hɛkˈsæmɪtərz/", "câu thơ lục nhịp sử thi cổ điển"),
    ("066955", "hinderances", "noun", "/ˈhɪndrənsɪz/", "vật cản trở gây khó khăn"),
    ("066956", "hypokalemias", "noun", "/ˌhaɪpoʊkəˈliːmiəz/", "tình trạng hạ kali trong máu"),
    ("066957", "imipramines", "noun", "/ɪˈmɪprəˌmiːnz/", "thuốc chống trầm cảm imipramin"),
    ("066958", "implausibilities", "noun", "/ɪmˌplɔːzəˈbɪlɪtiz/", "tính phi lý khó tin không hợp lý"),
    ("066959", "impressments", "noun", "/ɪmˈprɛsmənts/", "việc cưỡng bức bắt lính hải quân"),
    ("066960", "inconels", "noun", "/ˈɪnkəˌnɛlz/", "siêu hợp kim niken chịu nhiệt cao"),
    ("066961", "lascauxes", "noun", "/lɑːˈskoʊz/", "hang động tranh đá Lascaux Pháp"),
    ("066962", "lipomas", "noun", "/lɪˈpoʊməz/", "khối u mỡ lành tính dưới da"),
    ("066963", "lipomata", "noun", "/lɪˈpoʊmətə/", "u mỡ lành tính trong mô mềm"),
    ("066964", "lubavitches", "noun", "/luːˈbɑːvɪtʃɪz/", "phong trào Do Thái giáo Lubavitch"),
    ("066965", "lughs", "noun", "/luːz/", "thần ánh sáng Lugh trong thần thoại"),
    ("066966", "madagascans", "noun", "/ˌmædəˈɡæskənz/", "người dân đảo quốc Madagascar"),
    ("066967", "manzanillas", "noun", "/ˌmænzəˈniːəz/", "rượu vang khô Manzanilla; ô liu"),
    ("066968", "maois", "noun", "/ˌɛm eɪ oʊ ˈaɪz/", "thuốc chống trầm cảm ức chế MAO"),
    ("066969", "meatuses", "noun", "/miˈeɪtəsɪz/", "lỗ ống tự nhiên trong cơ thể"),
    ("066970", "mefloquines", "noun", "/ˈmɛfləˌkwiːnz/", "thuốc phòng trị sốt rét mefloquin"),
    ("066971", "megabits", "noun", "/ˈmɛɡəˌbɪts/", "đơn vị dữ liệu một triệu bit"),
    ("066972", "mortgagors", "noun", "/ˈmɔːrɡɪdʒərz/", "người thế chấp tài sản vay vốn"),
    ("066973", "msecs", "noun", "/ˈɛm sɛks/", "đơn vị thời gian mili giây"),
    ("066974", "muscas", "noun", "/ˈmʌskəz/", "chòm sao Con Ruồi; chi ruồi nhà"),
    ("066975", "nailers", "noun", "/ˈneɪlərz/", "máy bắn đinh; thợ đóng đinh"),
    ("066976", "narthexes", "noun", "/ˈnɑːrθɛksɪz/", "tiền sảnh lối vào chính nhà thờ"),
    ("066977", "nutrias", "noun", "/ˈnjuːtriəz/", "chuột hải ly lớn sống đầm lầy"),
    ("066978", "odonatas", "noun", "/ˌoʊdəˈneɪtəz/", "bộ Chuồn chuồn cánh màng"),
    ("066979", "originalisms", "noun", "/əˈrɪdʒənəˌlɪzəmz/", "thuyết hiểu hiến pháp nguyên bản"),
    ("066980", "ormandies", "noun", "/ˈɔːrməndiz/", "nhạc trưởng Mỹ Eugene Ormandy"),
    ("066981", "osteologies", "noun", "/ˌɒstiˈɒlədʒiz/", "ngành xương học nghiên cứu xương"),
    ("066982", "outriders", "noun", "/ˈaʊtˌraɪdərz/", "kỵ binh hộ tống dẫn đường xe ngựa"),
    ("066983", "outwearing", "verb", "/aʊtˈwɛərɪŋ/", "đang dùng bền hơn; kéo dài hơn"),
    ("066984", "outwears", "verb", "/aʊtˈwɛərz/", "dùng bền lâu hơn vật khác"),
    ("066985", "outworn", "verb", "/aʊtˈwɔːrn/", "đã dùng bền hơn; đã lỗi thời cũ"),
    ("066986", "ovules", "noun", "/ˈɒvjuːlz/", "noãn thực vật hình thành hạt"),
    ("066987", "paranoiacs", "noun", "/ˌpærəˈnɔɪæks/", "người mắc chứng hoang tưởng"),
    ("066988", "pareses", "noun", "/pəˈriːsiːz/", "chứng liệt nhẹ; bán liệt vận động"),
    ("066989", "pentodes", "noun", "/ˈpɛnˌtoʊdz/", "đèn điện tử chân không năm cực"),
    ("066990", "phaseoluses", "noun", "/fəˈsiːələsɪz/", "cây đậu cô ve thuộc chi Phaseolus"),
    ("066991", "phenylephrines", "noun", "/ˌfɛnəlˈɛfrɪnz/", "thuốc thông mũi phenylephrin"),
    ("066992", "pissers", "noun", "/ˈpɪsərz/", "người tiểu tiện; chuyện hài (lóng)"),
    ("066993", "prilosecs", "noun", "/ˈpraɪləˌsɛks/", "thuốc giảm axit dạ dày Prilosec"),
    ("066994", "procyons", "noun", "/ˈproʊsiɒnz/", "sao Thiên Cẩu Procyon; chi gấu mèo"),
    ("066995", "rhumbaed", "verb", "/ˈrʌmbəd/", "đã nhảy điệu khiêu vũ rumba"),
    ("066996", "rhumbaing", "verb", "/ˈrʌmbəɪŋ/", "đang nhảy điệu khiêu vũ rumba"),
    ("066997", "rhumbas", "noun", "/ˈrʌmbəz/", "điệu nhảy sôi động rumba Cuba"),
    ("066998", "ropeways", "noun", "/ˈroʊpˌweɪz/", "hệ thống cáp treo vận chuyển"),
    ("066999", "salmonids", "noun", "/ˈsælmənɪdz/", "cá thuộc họ Cá hồi"),
    ("067000", "sanitizations", "noun", "/ˌsænɪtaɪˈzeɪʃənz/", "quá trình khử trùng vệ sinh sạch"),
    ("067001", "scrapples", "noun", "/ˈskræpəlz/", "món chả thịt lợn bột ngô chiên"),
    ("067002", "soddies", "noun", "/ˈsɒdiz/", "nhà dựng bằng tảng đất thảo nguyên"),
]

with open("scratch/b34_r04_raw_p5.json") as f:
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

with open("scratch/b34_r04_p5.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r04_p5.json OK")
