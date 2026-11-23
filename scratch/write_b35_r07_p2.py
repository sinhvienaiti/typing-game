import json

items = [
    ("073103", "butterburs", "noun", "/ˈbʌtərˌbɜːrz/", "cây cúc bơ lá to chi Petasites"),
    ("073104", "calyptras", "noun", "/kəˈlɪptrəz/", "chóp mũ rêu; bao nắp chồi hoa"),
    ("073105", "carpinuses", "noun", "/kɑːrˈpaɪnəsɪz/", "cây trăn thuộc chi Carpinus"),
    ("073106", "castillejas", "noun", "/ˌkæstɪˈleɪəz/", "cây chổi vẽ Ấn Độ Castilleja"),
    ("073107", "cathexes", "noun", "/kəˈθɛksiːz/", "sự dồn tâm lực cảm xúc (tâm lý)"),
    ("073108", "cathexises", "noun", "/kəˈθɛksɪsɪz/", "sự dồn tâm lực cảm xúc (tâm lý)"),
    ("073109", "cellularities", "noun", "/ˌsɛljʊˈlærɪtiz/", "mật độ tế bào trong mô (sinh học)"),
    ("073110", "circumambulated", "verb", "/ˌsɜːrkəmˈæmbjʊˌleɪtɪd/", "đã đi vòng quanh (hành hương lễ)"),
    ("073111", "circumambulates", "verb", "/ˌsɜːrkəmˈæmbjʊˌleɪts/", "đi vòng quanh (hành hương lễ)"),
    ("073112", "circumambulating", "verb", "/ˌsɜːrkəmˈæmbjʊˌleɪtɪŋ/", "đang đi vòng quanh (hành hương lễ)"),
    ("073113", "clabbered", "verb", "/ˈklæbərd/", "đã đông chua vón cục (sữa)"),
    ("073114", "clabbering", "verb", "/ˈklæbərɪŋ/", "đang đông chua vón cục (sữa)"),
    ("073115", "clabbers", "noun", "/ˈklæbərz/", "sữa đông chua tự nhiên; bùn sệt"),
    ("073116", "clonuses", "noun", "/ˈkloʊnəsɪz/", "chứng giật rung cơ nhịp nhàng"),
    ("073117", "compartmentalisations", "noun", "/kəmˌpɑːrtmɛntəlaɪˈzeɪʃənz/", "sự phân chia thành ngăn riêng (Anh)"),
    ("073118", "conoids", "noun", "/ˈkoʊnɔɪdz/", "mặt khối nón bậc hai (toán học)"),
    ("073119", "coxsackieviruses", "noun", "/kɒkˈsækiˌvaɪrəsɪz/", "vi-rút đường ruột Coxsackie"),
    ("073120", "ctenophoras", "noun", "/tɪˈnɒfərəz/", "ngành Sứa lược (động vật biển)"),
    ("073121", "culverins", "noun", "/ˈkʌlvərɪnz/", "khẩu pháo đồng nòng dài cổ đại"),
    ("073122", "cyanamids", "noun", "/saɪˈænəmɪdz/", "hợp chất hóa học xyanamit"),
    ("073123", "cytisuses", "noun", "/ˈsɪtɪsəsɪz/", "cây kim tước hoa vàng chi Cytisus"),
    ("073124", "decerebrated", "verb", "/diːˈsɛrɪˌbreɪtɪd/", "đã cắt bỏ đại não (thực nghiệm)"),
    ("073125", "decerebrates", "verb", "/diːˈsɛrɪˌbreɪts/", "cắt bỏ đại não; làm mất lý trí"),
    ("073126", "decerebrating", "verb", "/diːˈsɛrɪˌbreɪtɪŋ/", "đang cắt bỏ đại não (thực nghiệm)"),
    ("073127", "dendrologies", "noun", "/dɛnˈdrɒlədʒiz/", "ngành lâm mộc học nghiên cứu gỗ"),
    ("073128", "desyrels", "noun", "/ˈdɛzərɛlz/", "thuốc chống trầm cảm Desyrel"),
    ("073129", "epentheses", "noun", "/ɪˈpɛnθɪˌsiːz/", "hiện tượng chêm âm vào giữa từ"),
    ("073130", "epicycles", "noun", "/ˈɛpɪˌsaɪkəlz/", "ngoại luân (vòng tròn thiên văn cổ)"),
    ("073131", "euglenas", "noun", "/juːˈɡliːnəz/", "trùng roi xanh quang hợp Euglena"),
    ("073132", "eyespots", "noun", "/ˈaɪˌspɒts/", "điểm mắt cảm quang; đốm mắt cánh"),
    ("073133", "famotidines", "noun", "/fəˈmoʊtɪdiːnz/", "thuốc giảm axit dạ dày famotidine"),
    ("073134", "fauvists", "noun", "/ˈfoʊvɪsts/", "họa sĩ trường phái Dã thú (Pháp)"),
    ("073135", "fictionalizations", "noun", "/ˌfɪkʃənəlaɪˈzeɪʃənz/", "sự tiểu thuyết hóa hư cấu sự kiện"),
    ("073136", "fondus", "noun", "/ˈfɒndjuːz/", "động tác chùng gối ba lê; lẩu"),
    ("073137", "footwalls", "noun", "/ˈfʊtˌwɔːlz/", "vách đá nằm dưới đứt gãy (địa chất)"),
    ("073138", "freshets", "noun", "/ˈfrɛʃɪts/", "nước lũ băng tan; dòng nước ngọt"),
    ("073139", "galbanums", "noun", "/ˈɡælbənəmz/", "nhựa thơm thực vật galbanum"),
    ("073140", "gismos", "noun", "/ˈɡɪzmoʊz/", "thiết bị nhỏ lặt vãnh (biến thể)"),
    ("073141", "gramineaes", "noun", "/ɡrəˈmɪniˌiːz/", "họ Hòa thảo (họ Cỏ, lúa mì, tre)"),
    ("073142", "guaiacs", "noun", "/ˈɡwaɪæks/", "gỗ cứng nhựa thơm guaiac"),
    ("073143", "haemostases", "noun", "/ˌhiːməˈsteɪsiːz/", "quá trình cầm máu đông máu (Anh)"),
    ("073144", "halmas", "noun", "/ˈhælməz/", "trò chơi cờ nhảy halma bàn 16x16"),
    ("073145", "humuli", "noun", "/ˈhjuːmjʊˌlaɪ/", "chi Cây hoa bia ủ bia (Humulus)"),
    ("073146", "hydrocrackings", "noun", "/ˌhaɪdroʊˈkrækɪŋz/", "quá trình bẻ gãy hyđrô lọc dầu"),
    ("073147", "hyperaldosteronisms", "noun", "/ˌhaɪpərælˈdɒstəroʊˌnɪzəmz/", "hội chứng cường aldosterone"),
    ("073148", "ichneumonidaes", "noun", "/ɪkˌnjuːˈmɒnɪˌdiːz/", "họ Ong cự ký sinh sâu bọ"),
    ("073149", "idahoans", "noun", "/aɪˈdeɪhoʊənz/", "người dân bang Idaho của Mỹ"),
    ("073150", "jitterinesses", "noun", "/ˈdʒɪtərinəsɪz/", "tính bồn chồn lo lắng hồi hộp"),
    ("073151", "kylikes", "noun", "/ˈkaɪlɪˌkiːz/", "chén uống rượu cạn có quai Hy Lạp"),
    ("073152", "kylixes", "noun", "/ˈkaɪlɪksɪz/", "chén uống rượu cạn có quai Hy Lạp"),
    ("073153", "ladyloves", "noun", "/ˈleɪdɪˌlʌvz/", "người yêu nữ; bạn gái thân (từ cũ)"),
    ("073154", "latrodectuses", "noun", "/ˌlætroʊˈdɛktəsɪz/", "chi Nhện góa phụ đen độc"),
    ("073155", "lepidiums", "noun", "/lɪˈpɪdiəmz/", "cây cải xoong tiêu cạn Lepidium"),
    ("073156", "lipmanns", "noun", "/ˈlɪpmənz/", "nhà sinh hóa Fritz Lipmann"),
    ("073157", "lithotomies", "noun", "/lɪˈθɒtəmiz/", "phẫu thuật mổ lấy sỏi bàng quang"),
    ("073158", "matricarias", "noun", "/ˌmætrɪˈkɛəriəz/", "hoa cúc La Mã nhỏ Matricaria"),
    ("073159", "medflies", "noun", "/ˈmɛdˌflaɪz/", "ruồi đục quả Địa Trung Hải"),
    ("073160", "metastabilities", "noun", "/ˌmɛtəstəˈbɪlɪtiz/", "trạng thái siêu bền giả ổn định"),
    ("073161", "methaqualones", "noun", "/ˌmɛθəˈkweɪloʊnz/", "thuốc an thần gây ngủ methaqualone"),
    ("073162", "miliarias", "noun", "/ˌmɪliˈɛəriəz/", "bệnh rôm sảy tắc tuyến mồ hôi"),
    ("073163", "milliwatts", "noun", "/ˈmɪlɪˌwɒts/", "đơn vị công suất miliwatt (10^-3 W)"),
    ("073164", "monopolisations", "noun", "/məˌnɒpəlaɪˈzeɪʃənz/", "sự độc quyền thâu tóm thị trường"),
    ("073165", "morions", "noun", "/ˈmɔːriənz/", "mũ sắt đỉnh mào xưa; thạch anh đen"),
    ("073166", "moschuses", "noun", "/ˈmɒskəsɪz/", "chi Hươu xạ châu Á (Moschus)"),
    ("073167", "motorbuses", "noun", "/ˈmoʊtərˌbʌsɪz/", "xe ô tô buýt chở khách (từ cũ)"),
    ("073168", "mouflons", "noun", "/ˈmuːflɒnz/", "cừu rừng sừng xoắn Địa Trung Hải"),
    ("073169", "nectaries", "noun", "/ˈnɛktəriz/", "tuyến tiết mật ngọt của hoa lá"),
    ("073170", "newaris", "noun", "/nəˈwɑːriz/", "người và tiếng Newar ở Nepal"),
    ("073171", "notropides", "noun", "/noʊˈtrɒpɪdiːz/", "chi Cá tuế ánh bạc Bắc Mỹ Notropis"),
    ("073172", "organicisms", "noun", "/ɔːrˈɡænɪˌsɪzəmz/", "thuyết cơ thể hữu cơ (triết, sinh)"),
    ("073173", "ovalbumins", "noun", "/oʊˈvælbjʊmɪnz/", "protein lòng trắng trứng ovalbumin"),
    ("073174", "pachucos", "noun", "/pəˈtʃuːkoʊz/", "thanh niên gốc Mexico thập niên 40"),
    ("073175", "paleopathologies", "noun", "/ˌpeɪlioʊpəˈθɒlədʒiz/", "ngành cổ bệnh học (xương hóa thạch)"),
    ("073176", "pandions", "noun", "/ˈpændiənz/", "chi Chim ó cá săn cá (Pandion)"),
    ("073177", "pavonias", "noun", "/pəˈvoʊniəz/", "cây bụi hoa cẩm quỳ Pavonia"),
    ("073178", "pipefishes", "noun", "/ˈpaɪpˌfɪʃɪz/", "cá chìa vôi thân mảnh họ Cá ngựa"),
    ("073179", "pleonasms", "noun", "/ˈpliːəˌnæzəmz/", "lỗi lặp từ dư thừa rườm rà"),
    ("073180", "poilus", "noun", "/pwɑːˈluːz/", "người lính bộ binh Pháp Thế chiến I"),
    ("073181", "pontoses", "noun", "/ˈpɒntɒsɪz/", "thần biển cổ đại Pontus Hy Lạp"),
    ("073182", "princedoms", "noun", "/ˈprɪnsdəmz/", "thân vương quốc; ngôi vị thân vương"),
    ("073183", "proctitises", "noun", "/prɒkˈtaɪtɪsɪz/", "bệnh viêm niêm mạc trực tràng"),
    ("073184", "provisioners", "noun", "/prəˈvɪʒənərz/", "nhà cung cấp thực phẩm quân nhu"),
    ("073185", "pushtuns", "noun", "/ˈpʌʃtuːnz/", "người dân tộc Pashtun (Afghanistan)"),
    ("073186", "radiolarias", "noun", "/ˌreɪdioʊˈlɛəriəz/", "nhóm Trùng tia đơn bào biển"),
    ("073187", "rathskellers", "noun", "/ˈrɑːtsˌkɛlərz/", "quán rượu nhà hàng hầm kiểu Đức"),
    ("073188", "redhorses", "noun", "/ˈrɛdˌhɔːrsɪz/", "cá vây đỏ (họ Cá mút Bắc Mỹ)"),
    ("073189", "sagittarias", "noun", "/ˌsædʒɪˈtɛəriəz/", "chi Cây rau mác từ cô (Sagittaria)"),
    ("073190", "salpae", "noun", "/ˈsælpiː/", "động vật biển thân trong suốt salp"),
    ("073191", "salpas", "noun", "/ˈsælpəz/", "động vật biển thân trong suốt salp"),
    ("073192", "sequelae", "noun", "/sɪˈkwiːliː/", "di chứng bệnh lý còn để lại"),
    ("073193", "sequelas", "noun", "/sɪˈkwiːləz/", "di chứng bệnh lý còn để lại"),
    ("073194", "serails", "noun", "/sɛˈreɪlz/", "cung điện hậu cung Thổ Nhĩ Kỳ"),
    ("073195", "shitlists", "noun", "/ˈʃɪtˌlɪsts/", "danh sách đen bị ghét (từ lóng)"),
    ("073196", "slummier", "adj", "/ˈslʌmiər/", "nhếch nhác tồi tàn kiểu ổ chuột hơn"),
    ("073197", "slummiest", "adj", "/ˈslʌmiɪst/", "tồi tàn nhếch nhác nhất"),
    ("073198", "sociometries", "noun", "/ˌsoʊsiˈɒmɪtriz/", "ngành trắc lượng xã hội học"),
    ("073199", "sporoboluses", "noun", "/spɔːˈrɒbələsɪz/", "cỏ đuôi phụng thuộc chi Sporobolus"),
    ("073200", "stonechats", "noun", "/ˈstoʊnˌtʃæts/", "chim sẻ đá châu Âu hót lách cách"),
    ("073201", "sturmabteilungs", "noun", "/ˈʃtʊərmɑːpˌtaɪlʊŋz/", "Đội quân bão táp SA (Đức Quốc xã)"),
    ("073202", "styraxes", "noun", "/ˈstaɪræksɪz/", "cây bồ đề nhựa thơm chi Styrax"),
]

with open("scratch/b35_r07_raw_p2.json") as f:
    raw = json.load(f)

assert len(items) == 100
assert len(raw) == 100
allowed_pos = {"noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det", "phrase"}
out = []
for r, (rid, hw, pos, ipa, vi) in zip(raw, items):
    assert r["id"].endswith("." + rid), f"ID mismatch: {r['id']} != {rid}"
    assert r["hw"] == hw, f"HW mismatch: {r['hw']} != {hw}"
    assert pos in allowed_pos, f"Bad POS: {pos}"
    assert len(vi) <= 35, f"VI too long ({len(vi)}): {hw} -> {vi}"
    assert ipa.startswith("/") and ipa.endswith("/") and ipa.count("/") == 2, f"Bad IPA: {hw} -> {ipa}"
    assert not ipa[1:-1].startswith(" ") and not ipa[1:-1].endswith(" "), f"Space in IPA: {hw} -> {ipa}"
    out.append({**r, "pos": pos, "ipa": ipa, "vi": vi, "status": "reviewed"})

with open("scratch/b35_r07_p2.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r07_p2.json OK")
