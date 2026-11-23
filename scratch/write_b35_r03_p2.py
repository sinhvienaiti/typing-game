import json

items = [
    ("071103", "synoviums", "noun", "/sɪˈnoʊviəmz/", "màng hoạt dịch bao khớp xương"),
    ("071104", "tasses", "noun", "/ˈtæsɪz/", "mảnh giáp bảo vệ đùi (áo giáp)"),
    ("071105", "tenters", "noun", "/ˈtɛntərz/", "khung căng phơi vải; thợ coi máy"),
    ("071106", "thecae", "noun", "/ˈθiːsiː/", "túi bào tử; bao nang cơ quan"),
    ("071107", "thecas", "noun", "/ˈθiːkəz/", "túi bào tử; bao nang cơ quan"),
    ("071108", "tishris", "noun", "/ˈtɪʃriz/", "tháng đầu tiên lịch Do Thái"),
    ("071109", "tosks", "noun", "/tɒsks/", "nhóm người và phương ngữ Tosk"),
    ("071110", "transduced", "verb", "/trænzˈdjuːst/", "đã chuyển đổi năng lượng; tải nạp"),
    ("071111", "transduces", "verb", "/trænzˈdjuːsɪz/", "chuyển đổi tín hiệu; tải nạp gen"),
    ("071112", "upcasts", "noun", "/ˈʌpˌkæsts/", "giếng thông gió thoát khí lên (mỏ)"),
    ("071113", "vaccinators", "noun", "/ˈvæksɪˌneɪtərz/", "nhân viên tiêm chủng vắc-xin"),
    ("071114", "vinblastines", "noun", "/vɪnˈblæstiːnz/", "thuốc hóa trị ung thư vinblastine"),
    ("071115", "viremias", "noun", "/vaɪˈriːmiəz/", "tình trạng có vi-rút trong máu"),
    ("071116", "warrigals", "noun", "/ˈwɒrɪɡəlz/", "chó dingo hoang Úc; người hoang dã"),
    ("071117", "wavebands", "noun", "/ˈweɪvˌbændz/", "dải băng tần sóng vô tuyến"),
    ("071118", "whipsawed", "verb", "/ˈwɪpˌsɔːd/", "đã lừa hai đầu; đã cưa hai người"),
    ("071119", "whipsawn", "verb", "/ˈwɪpˌsɔːn/", "bị lừa thiệt hai đầu (quá khứ phân)"),
    ("071120", "whipsaws", "noun", "/ˈwɪpˌsɔːz/", "cưa xẻ dài hai người kéo; bẫy giá"),
    ("071121", "yardbirds", "noun", "/ˈjɑːrdˌbɜːrdz/", "tù nhân; tân binh (lóng Mỹ)"),
    ("071122", "ablates", "verb", "/əˈbleɪts/", "cắt bỏ mô; bào mòn bốc hơi"),
    ("071123", "ablating", "verb", "/əˈbleɪtɪŋ/", "đang cắt bỏ mô; đang bào mòn"),
    ("071124", "acanthoses", "noun", "/ˌækænˈθoʊsiːz/", "chứng dày gai thượng bì da"),
    ("071125", "adventisms", "noun", "/ˈædvɛntˌɪzəmz/", "giáo phái Cơ Đốc Phục Lâm"),
    ("071126", "akhas", "noun", "/ˈɑːkɑːz/", "dân tộc và tiếng Hà Nhì Akha"),
    ("071127", "alceses", "noun", "/ˈælsɪˌsiːz/", "chi Nai sừng tấm châu Âu (Alces)"),
    ("071128", "americanisations", "noun", "/əˌmɛrɪkənaɪˈzeɪʃənz/", "sự Mỹ hóa theo văn hóa Mỹ (Anh)"),
    ("071129", "androgynes", "noun", "/ˈændrəˌdʒaɪnz/", "người mang nét lưỡng tính nam nữ"),
    ("071130", "antepenultimates", "noun", "/ˌæntɪpɪˈnʌltɪmɪts/", "âm tiết thứ ba kể từ cuối từ"),
    ("071131", "araucas", "noun", "/əˈraʊkəz/", "sông Arauca ở Nam Mỹ"),
    ("071132", "arsenicals", "noun", "/ɑːrˈsɛnɪkəlz/", "hợp chất hoặc thuốc chứa asen"),
    ("071133", "asamas", "noun", "/əˈsɑːməz/", "núi lửa Asama ở Nhật Bản"),
    ("071134", "auriculas", "noun", "/ɔːˈrɪkjʊləz/", "hoa anh thảo tai gấu châu Âu"),
    ("071135", "autolyses", "noun", "/ɔːˈtɒlɪˌsiːz/", "hiện tượng tự phân hủy tế bào"),
    ("071136", "bartholins", "noun", "/ˈbɑːrtəlɪnz/", "tuyến Bartholin; bác sĩ Bartholin"),
    ("071137", "bryozoas", "noun", "/ˌbraɪəˈzoʊəz/", "ngành Động vật hình rêu (tảo rêu)"),
    ("071138", "buddleias", "noun", "/bʌdˈliːəz/", "cây tử đinh hương mùa hè hút bướm"),
    ("071139", "butterfishes", "noun", "/ˈbʌtərˌfɪʃɪz/", "cá bơ thân dẹt trơn bóng"),
    ("071140", "callunas", "noun", "/kəˈluːnəz/", "cây thạch nam hồng chi Calluna"),
    ("071141", "catafalques", "noun", "/ˈkætəˌfælks/", "đài kê quan tài trong lễ tang lớn"),
    ("071142", "catlings", "noun", "/ˈkætlɪŋz/", "dao phẫu thuật hai lưỡi; dây đàn"),
    ("071143", "chaeroneas", "noun", "/ˌkɛrəˈniːəz/", "trận chiến Chaeronea ở Hy Lạp cổ"),
    ("071144", "clawhammers", "noun", "/ˈklɔːˌhæmərz/", "búa sừng dê nhổ đinh"),
    ("071145", "commissionaires", "noun", "/kəˌmɪʃəˈnɛərz/", "nhân viên gác cổng mặc đồng phục"),
    ("071146", "convolutes", "verb", "/ˈkɒnvəˌluːts/", "cuộn xoắn lại chồng lên nhau"),
    ("071147", "convoluting", "verb", "/ˈkɒnvəˌluːtɪŋ/", "đang cuộn xoắn lại; phức tạp hóa"),
    ("071148", "cornelians", "noun", "/kɔːrˈniːliənz/", "đá mã não đỏ carnelian (Anh)"),
    ("071149", "creatins", "noun", "/ˈkriːətɪnz/", "hợp chất creatine tạo năng lượng"),
    ("071150", "creeses", "noun", "/ˈkriːsɪz/", "dao găm lưỡi lượn sóng Mã Lai"),
    ("071151", "deckles", "noun", "/ˈdɛkəlz/", "khung khuôn xeo giấy; mép giấy xù"),
    ("071152", "desensitisations", "noun", "/diːˌsɛnsɪtaɪˈzeɪʃənz/", "sự giảm mẫn cảm (cách viết Anh)"),
    ("071153", "dextrins", "noun", "/ˈdɛkstrɪnz/", "chất hồ tinh bột thủy phân dextrin"),
    ("071154", "diverticuloses", "noun", "/ˌdaɪvɜːrtɪkjʊˈloʊsiːz/", "bệnh túi thừa niêm mạc đại tràng"),
    ("071155", "doodads", "noun", "/ˈduːdædz/", "đồ vật nhỏ lặt vặt (khẩu ngữ)"),
    ("071156", "dulses", "noun", "/ˈdʌlsɪz/", "rong biển đỏ ăn được dulse"),
    ("071157", "dynasts", "noun", "/ˈdaɪnæsts/", "quốc vương; người cai trị triều đại"),
    ("071158", "eluted", "verb", "/ɪˈluːtɪd/", "đã rửa giải tách chất (hóa học)"),
    ("071159", "elutes", "verb", "/ɪˈluːts/", "rửa giải tách chất (sắc ký)"),
    ("071160", "eluting", "verb", "/ɪˈluːtɪŋ/", "đang rửa giải tách chất (sắc ký)"),
    ("071161", "endometritides", "noun", "/ˌɛndoʊmɪˈtraɪtɪdiːz/", "bệnh viêm nội mạc tử cung"),
    ("071162", "epimetheuses", "noun", "/ˌɛpɪˈmiːθiəsɪz/", "thần Epimetheus (em Prometheus)"),
    ("071163", "escadrilles", "noun", "/ˌɛskəˈdrɪlz/", "phi đội không quân hoặc hải đội nhỏ"),
    ("071164", "felidaes", "noun", "/ˈfiːlɪˌdiːz/", "họ Mèo trong bộ Ăn thịt"),
    ("071165", "fettuccinis", "noun", "/ˌfɛtəˈtʃiːniz/", "mì sợi dẹt Ý fettuccine"),
    ("071166", "fimbriae", "noun", "/ˈfɪmbriˌiː/", "tua diềm lông; tua vòi tử cung"),
    ("071167", "fimbrias", "noun", "/ˈfɪmbriəz/", "tua diềm; lông tua vi khuẩn"),
    ("071168", "flageolets", "noun", "/ˌflædʒəˈlɛts/", "sáo nhỏ flageolet; đậu xanh Pháp"),
    ("071169", "flummeries", "noun", "/ˈflʌməriz/", "lời nịnh hót nhảm; bánh bột yến"),
    ("071170", "gambusias", "noun", "/ɡæmˈbjuːʒəz/", "cá bảy màu diệt lăng quăng (muỗi)"),
    ("071171", "giardiases", "noun", "/ˌdʒiːɑːrˈdaɪəsiːz/", "bệnh nhiễm ký sinh trùng Giardia"),
    ("071172", "greaseballs", "noun", "/ˈɡriːsˌbɔːlz/", "từ lóng cũ xúc phạm; kẻ tóc bóng"),
    ("071173", "guvnors", "noun", "/ˈɡʌvnərz/", "ông chủ, sếp, thủ trưởng (lóng Anh)"),
    ("071174", "hanukahs", "noun", "/ˈhɑːnəkəz/", "lễ hội ánh sáng Hanukkah Do Thái"),
    ("071175", "hemostats", "noun", "/ˈhiːməˌstæts/", "kẹp cầm máu phẫu thuật"),
    ("071176", "hindfoots", "noun", "/ˈhaɪndˌfʊts/", "phần sau bàn chân (gót cổ chân)"),
    ("071177", "hodeidas", "noun", "/hoʊˈdeɪdəz/", "thành phố cảng Al Hudaydah Yemen"),
    ("071178", "infundibula", "noun", "/ˌɪnfʌnˈdɪbjʊlə/", "cấu trúc hình phễu (giải phẫu)"),
    ("071179", "infundibulums", "noun", "/ˌɪnfʌnˈdɪbjʊləmz/", "cấu trúc hình phễu (giải phẫu)"),
    ("071180", "irtyshes", "noun", "/ɪərˈtɪʃɪz/", "sông Irtysh (chảy qua Nga, Trung)"),
    ("071181", "jamboses", "noun", "/ˈdʒæmboʊsɪz/", "chi Trâm mận roi Syzygium (Jambos)"),
    ("071182", "jiddas", "noun", "/ˈdʒɪdəz/", "thành phố cảng Jeddah Ả Rập Xê Út"),
    ("071183", "leiomyosarcomas", "noun", "/ˌlaɪoʊmaɪoʊsɑːrˈkoʊməz/", "u ác tính cơ trơn leiomyosarcoma"),
    ("071184", "lepomises", "noun", "/ˈlɛpəmɪsɪz/", "chi Cá thái dương Bắc Mỹ Lepomis"),
    ("071185", "litterateurs", "noun", "/ˌlɪtərəˈtɜːrz/", "nhà văn học giả giới văn chương"),
    ("071186", "lowans", "noun", "/ˈloʊənz/", "gà ấp đất Úc (malleefowl)"),
    ("071187", "lowboys", "noun", "/ˈloʊˌbɔɪz/", "tủ thấp có ngăn kéo; xe sàn thấp"),
    ("071188", "macouns", "noun", "/məˈkaʊnz/", "giống táo đỏ giòn ngọt Macoun"),
    ("071189", "microscopists", "noun", "/maɪˈkrɒskəpɪsts/", "nhà chuyên môn kính hiển vi"),
    ("071190", "overprices", "verb", "/ˌoʊvərˈpraɪsɪz/", "định giá bán cao quá mức"),
    ("071191", "overpricing", "verb", "/ˌoʊvərˈpraɪsɪŋ/", "đang định giá bán cao quá mức"),
    ("071192", "parvises", "noun", "/ˈpɑːrvɪsɪz/", "sân hiên trước cửa chính nhà thờ"),
    ("071193", "pashtus", "noun", "/ˈpʌʃtuːz/", "tiếng Pashto của người Pashtun"),
    ("071194", "pastilles", "noun", "/pæˈstiːlz/", "viên ngậm ho thảo dược; nén hương"),
    ("071195", "peans", "noun", "/ˈpiːənz/", "bài ca khải hoàn tụng ca; lông da"),
    ("071196", "peneplains", "noun", "/ˈpɛnɪˌpleɪnz/", "đồng bằng san bằng cổ (bán bình)"),
    ("071197", "permuted", "verb", "/pərˈmjuːtɪd/", "đã hoán vị sắp xếp lại thứ tự"),
    ("071198", "permutes", "verb", "/pərˈmjuːts/", "hoán vị thay đổi thứ tự sắp xếp"),
    ("071199", "permuting", "verb", "/pərˈmjuːtɪŋ/", "đang hoán vị đổi thứ tự sắp xếp"),
    ("071200", "pesantrens", "noun", "/pəˈsɑːntrɛnz/", "trường nội trú Hồi giáo Indonesia"),
    ("071201", "photocathodes", "noun", "/ˌfoʊtoʊˈkæθoʊdz/", "catôt quang điện phát xạ electron"),
    ("071202", "plasmins", "noun", "/ˈplæzmɪnz/", "enzym phân giải cục máu đông"),
]

with open("scratch/b35_r03_raw_p2.json") as f:
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

with open("scratch/b35_r03_p2.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r03_p2.json OK")
