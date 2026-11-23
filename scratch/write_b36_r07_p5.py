import json

rows = [
    ("078403", "prancing", "verb", "/ˈprænsɪŋ/", "nhảy tung tăng; đi nghênh ngang"),
    ("078404", "prancingly", "adv", "/ˈprænsɪŋli/", "với dáng điệu nhảy tung tăng"),
    ("078405", "prandially", "adv", "/ˈprændiəli/", "trong lúc hoặc liên quan bữa ăn"),
    ("078406", "pranged", "verb", "/præŋd/", "đã đâm va (xe, máy bay); ném bom"),
    ("078407", "pranging", "verb", "/ˈpræŋɪŋ/", "đâm va (xe, máy bay); ném bom"),
    ("078408", "prangs", "verb", "/præŋz/", "đâm va (xe, máy bay); ném bom"),
    ("078409", "pranker", "noun", "/ˈpræŋkər/", "người hay trêu chọc; người diện"),
    ("078410", "prankful", "adj", "/ˈpræŋkfəl/", "hay chơi khăm, nghịch ngợm"),
    ("078411", "prankishly", "adv", "/ˈpræŋkɪʃli/", "một cách tinh nghịch, trêu chọc"),
    ("078412", "prankishness", "noun", "/ˈpræŋkɪʃnəs/", "tính hay chơi khăm, nghịch ngợm"),
    ("078413", "praps", "adv", "/præps/", "có lẽ, biết đâu (khẩu ngữ perhaps)"),
    ("078414", "prase", "noun", "/preɪz/", "đá thạch anh xanh lục (prase)"),
    ("078415", "prated", "verb", "/ˈpreɪtɪd/", "đã nói lảm nhảm, ba hoa dài dòng"),
    ("078416", "prates", "verb", "/preɪts/", "nói lảm nhảm, ba hoa dài dòng"),
    ("078417", "pratfalls", "noun", "/ˈprætˌfɔːlz/", "cú ngã chổng vó; lỗi bẽ mặt"),
    ("078418", "praties", "noun", "/ˈpreɪtiz/", "củ khoai tây (tiếng lóng Ireland)"),
    ("078419", "pratincole", "noun", "/ˈprætɪŋkoʊl/", "chim nhạn đồng (họ Glareolidae)"),
    ("078420", "prating", "verb", "/ˈpreɪtɪŋ/", "nói lảm nhảm, ba hoa dài dòng"),
    ("078421", "pratingly", "adv", "/ˈpreɪtɪŋli/", "một cách ba hoa, lảm nhảm"),
    ("078422", "pratique", "noun", "/præˈtiːk/", "giấy phép cập cảng kiểm dịch"),
    ("078423", "prattled", "verb", "/ˈprætəld/", "đã nói huyên thuyên, líu lo"),
    ("078424", "prattler", "noun", "/ˈprætlər/", "người hay nói huyên thuyên"),
    ("078425", "prattles", "verb", "/ˈprætəlz/", "nói huyên thuyên, líu lo"),
    ("078426", "prattling", "verb", "/ˈprætlɪŋ/", "nói huyên thuyên, líu lo"),
    ("078427", "prattlingly", "adv", "/ˈprætlɪŋli/", "một cách huyên thuyên, bi bô"),
    ("078428", "prau", "noun", "/praʊ/", "thuyền buồm Đông Nam Á (prau)"),
    ("078429", "praunus", "noun", "/ˈprɔːnəs/", "chi tôm nhỏ biển châu Âu Praunus"),
    ("078430", "pravachol", "noun", "/ˈprævəkɒl/", "thuốc hạ mỡ máu Pravachol"),
    ("078431", "pravity", "noun", "/ˈprævɪti/", "tính đồi bại, sự hư hỏng (cổ)"),
    ("078432", "prawned", "verb", "/prɔːnd/", "đã đánh bắt tôm (tôm he, tôm càng)"),
    ("078433", "prawner", "noun", "/ˈprɔːnər/", "ngư dân hoặc tàu đánh bắt tôm"),
    ("078434", "prawning", "verb", "/ˈprɔːnɪŋ/", "đánh bắt tôm (tôm he, tôm càng)"),
    ("078435", "prawns", "verb", "/prɔːnz/", "đánh bắt tôm (tôm he, tôm càng)"),
    ("078436", "praxes", "noun", "/ˈpræksiːz/", "thực tiễn áp dụng lý thuyết"),
    ("078437", "praxises", "noun", "/ˈpræksɪsɪz/", "thực tiễn áp dụng lý thuyết"),
    ("078438", "prayerfully", "adv", "/ˈprɛrfəli/", "một cách thành kính, khẩn nguyện"),
    ("078439", "prayerfulness", "noun", "/ˈprɛrfəlnəs/", "lòng thành kính hay cầu nguyện"),
    ("078440", "prayerless", "adj", "/ˈprɛrləs/", "không cầu nguyện, thiếu mộ đạo"),
    ("078441", "prayerwheel", "noun", "/ˈprɛrˌwiːl/", "kinh luân cầu nguyện (Tây Tạng)"),
    ("078442", "prd", "noun", "/ˌpiːɑːrˈdiː/", "tài liệu yêu cầu sản phẩm (PRD)"),
    ("078443", "preabdomen", "noun", "/ˌpriːæbˈdoʊmən/", "phần trước bụng (côn trùng)"),
    ("078444", "preacceleration", "noun", "/ˌpriːækˌsɛləˈreɪʃən/", "sự tiền tăng tốc (hạt cơ bản)"),
    ("078445", "preaccentuator", "noun", "/ˌpriːækˈsɛntʃueɪtər/", "mạch tiền nhấn tần số (điện tử)"),
    ("078446", "preachership", "noun", "/ˈpriːtʃərʃɪp/", "chức vụ mục sư, người thuyết giáo"),
    ("078447", "preachification", "noun", "/ˌpriːtʃɪfɪˈkeɪʃən/", "lối giảng đạo dài dòng nhàm chán"),
    ("078448", "preachify", "verb", "/ˈpriːtʃɪfaɪ/", "thuyết giáo dài dòng lên mặt"),
    ("078449", "preachily", "adv", "/ˈpriːtʃɪli/", "theo giọng thuyết giáo lên mặt"),
    ("078450", "preachiness", "noun", "/ˈpriːtʃinəs/", "tính thích thuyết giáo lên mặt"),
    ("078451", "preachingly", "adv", "/ˈpriːtʃɪŋli/", "theo lối thuyết giáo, rao giảng"),
    ("078452", "preachman", "noun", "/ˈpriːtʃmən/", "người giảng đạo, mục sư (từ cũ)"),
    ("078453", "preachment", "noun", "/ˈpriːtʃmənt/", "bài thuyết giáo dài dòng tẻ nhạt"),
    ("078454", "preacquaint", "verb", "/ˌpriːəˈkweɪnt/", "cho hay trước, làm quen trước"),
    ("078455", "preacquaintance", "noun", "/ˌpriːəˈkweɪntəns/", "sự biết trước, sự quen từ trước"),
    ("078456", "preadaptation", "noun", "/ˌpriːədæpˈteɪʃən/", "sự tiền thích nghi (tiến hóa)"),
    ("078457", "preadaptive", "adj", "/ˌpriːəˈdæptɪv/", "mang tính tiền thích nghi"),
    ("078458", "preadmonish", "verb", "/ˌpriːədˈmɒnɪʃ/", "khuyên bảo trước, cảnh báo trước"),
    ("078459", "preadmonished", "verb", "/ˌpriːədˈmɒnɪʃt/", "đã khuyên bảo trước, cảnh báo"),
    ("078460", "preadmonishes", "verb", "/ˌpriːədˈmɒnɪʃɪz/", "khuyên bảo trước, cảnh báo trước"),
    ("078461", "preadmonishing", "verb", "/ˌpriːədˈmɒnɪʃɪŋ/", "khuyên bảo trước, cảnh báo trước"),
    ("078462", "preadmonition", "noun", "/ˌpriːædməˈnɪʃən/", "lời khuyên bảo trước, cảnh báo"),
    ("078463", "preadvise", "verb", "/ˌpriːədˈvaɪz/", "khuyên nhủ trước, báo trước"),
    ("078464", "preagricultural", "adj", "/ˌpriːæɡrɪˈkʌltʃərəl/", "thuộc thời kỳ tiền nông nghiệp"),
    ("078465", "preambled", "verb", "/ˈpriːˌæmbəld/", "đã viết lời mở đầu; đi dạo quanh"),
    ("078466", "preambles", "verb", "/ˈpriːˌæmbəlz/", "viết lời mở đầu; đi dạo quanh"),
    ("078467", "preambling", "verb", "/ˈpriːˌæmbəlɪŋ/", "viết lời mở đầu; đi dạo quanh"),
    ("078468", "preambulary", "adj", "/priˈæmbjələri/", "mang tính mở đầu, tựa dẫn"),
    ("078469", "preambule", "noun", "/ˈpriːˌæmbjuːl/", "lời nói đầu, phần mở đầu (cổ)"),
    ("078470", "preamplifier", "noun", "/ˌpriːˈæmplɪˌfaɪər/", "bộ tiền khuếch đại (âm thanh)"),
    ("078471", "preanal", "adj", "/ˌpriːˈeɪnəl/", "ở phía trước hậu môn (giải phẫu)"),
    ("078472", "preannounce", "verb", "/ˌpriːəˈnaʊns/", "công bố trước, loan báo trước"),
    ("078473", "preannouncement", "noun", "/ˌpriːəˈnaʊnsmənt/", "sự công bố trước, loan báo trước"),
    ("078474", "prearrange", "verb", "/ˌpriːəˈreɪndʒ/", "sắp xếp trước, thu xếp từ trước"),
    ("078475", "prearranged", "verb", "/ˌpriːəˈreɪndʒd/", "đã sắp xếp trước, thu xếp trước"),
    ("078476", "prearranges", "verb", "/ˌpriːəˈreɪndʒɪz/", "sắp xếp trước, thu xếp từ trước"),
    ("078477", "prearranging", "verb", "/ˌpriːəˈreɪndʒɪŋ/", "sắp xếp trước, thu xếp từ trước"),
    ("078478", "preassemble", "verb", "/ˌpriːəˈsɛmbəl/", "lắp ráp sẵn từ trước"),
    ("078479", "preaxial", "adj", "/ˌpriːˈæksiəl/", "ở phía trước trục chi (giải phẫu)"),
    ("078480", "prebendal", "adj", "/prɪˈbɛndəl/", "thuộc bổng lộc giáo sĩ (Anh giáo)"),
    ("078481", "prebiologic", "adj", "/ˌpriːˌbaɪəˈlɒdʒɪk/", "tiền sinh học (trước khi có sống)"),
    ("078482", "prebiological", "adj", "/ˌpriːˌbaɪəˈlɒdʒɪkəl/", "tiền sinh học (trước khi có sống)"),
    ("078483", "prebrachial", "adj", "/ˌpriːˈbreɪkiəl/", "ở phía trước cánh tay (giải phẫu)"),
    ("078484", "precancel", "verb", "/ˌpriːˈkænsəl/", "đóng dấu hủy trước lên tem thư"),
    ("078485", "precartilage", "noun", "/ˌpriːˈkɑːrtəlɪdʒ/", "mô tiền sụn (phôi học)"),
    ("078486", "precative", "adj", "/ˈprɛkətɪv/", "mang tính cầu xin, van nài"),
    ("078487", "precatory", "adj", "/ˈprɛkətɔːri/", "mang tính khẩn cầu, van nài"),
    ("078488", "precautional", "adj", "/prɪˈkɔːʃənəl/", "để phòng ngừa, dự phòng trước"),
    ("078489", "precautions", "noun", "/prɪˈkɔːʃənz/", "biện pháp phòng ngừa, đề phòng"),
    ("078490", "precautious", "adj", "/prɪˈkɔːʃəs/", "để phòng ngừa, thận trọng dự phòng"),
    ("078491", "precava", "noun", "/ˌpriːˈkeɪvə/", "tĩnh mạch chủ trên (giải phẫu)"),
    ("078492", "precaval", "adj", "/ˌpriːˈkeɪvəl/", "thuộc tĩnh mạch chủ trên"),
    ("078493", "preceded", "verb", "/prɪˈsiːdɪd/", "đã đi trước, xảy ra trước, dẫn đầu"),
    ("078494", "precedences", "noun", "/ˈprɛsɪdənsɪz/", "quyền ưu tiên; thứ tự trước sau"),
    ("078495", "precedency", "noun", "/ˈprɛsɪdənsi/", "quyền ưu tiên; thứ tự trước sau"),
    ("078496", "precedentedly", "adv", "/ˈprɛsɪdɛntɪdli/", "theo tiền lệ đã có từ trước"),
    ("078497", "precedes", "verb", "/prɪˈsiːdz/", "đi trước, xảy ra trước, dẫn đầu"),
    ("078498", "precent", "verb", "/prɪˈsɛnt/", "hát lĩnh xướng dẫn nhịp (nhà thờ)"),
    ("078499", "precentorial", "adj", "/ˌpriːsɛnˈtɔːriəl/", "thuộc người lĩnh xướng ca đoàn"),
    ("078500", "precentorship", "noun", "/prɪˈsɛntərʃɪp/", "chức vụ người lĩnh xướng ca đoàn"),
    ("078501", "precentral", "adj", "/ˌpriːˈsɛntrəl/", "ở phía trước rãnh trung tâm (não)"),
    ("078502", "precentric", "adj", "/ˌpriːˈsɛntrɪk/", "ở phía trước tâm (sinh học)"),
]

with open("scratch/b36_r07_raw_p5.json", "r", encoding="utf-8") as f:
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

with open("scratch/b36_r07_p5.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b36_r07_p5 saved OK")
