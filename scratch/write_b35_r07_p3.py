import json

items = [
    ("073203", "suprematists", "noun", "/sʊˈprɛmətɪsts/", "họa sĩ trường phái Tối thượng"),
    ("073204", "swads", "noun", "/swɒdz/", "một nhóm tụ; củ cải Thụy Điển (Anh)"),
    ("073205", "tawses", "noun", "/ˈtɔːzɪz/", "dây da xẻ ngọn đánh đòn (Scotland)"),
    ("073206", "taxabilities", "noun", "/ˌtæksəˈbɪlɪtiz/", "tính chịu thuế theo quy định"),
    ("073207", "teguments", "noun", "/ˈtɛɡjʊmənts/", "lớp vỏ bọc ngoài (da, vỏ hạt)"),
    ("073208", "timbales", "noun", "/tæmˈbɑːlz/", "bánh đúc khuôn nhân thịt rau Pháp"),
    ("073209", "underspended", "verb", "/ˌʌndərˈspɛndɪd/", "đã chi tiêu thấp hơn dự toán"),
    ("073210", "underspending", "verb", "/ˌʌndərˈspɛndɪŋ/", "đang chi tiêu ít hơn dự toán"),
    ("073211", "underspends", "verb", "/ˌʌndərˈspɛndz/", "chi tiêu thấp hơn mức ngân sách"),
    ("073212", "verbascums", "noun", "/vɜːrˈbæskəmz/", "cây hoa thảo bản chi Verbascum"),
    ("073213", "verrazzanos", "noun", "/ˌvɛrəˈtsɑːnoʊz/", "nhà thám hiểm Giovanni Verrazzano"),
    ("073214", "vinicultures", "noun", "/ˈvɪnɪˌkʌltʃərz/", "nghề trồng nho làm rượu vang"),
    ("073215", "vivisectionists", "noun", "/ˌvɪvɪˈsɛkʃənɪsts/", "người thực hiện mổ xẻ sinh vật sống"),
    ("073216", "airmanships", "noun", "/ˈɛərmənʃɪps/", "kỹ năng điều khiển lái máy bay"),
    ("073217", "althaeas", "noun", "/ælˈθiːəz/", "cây thục quỳ hoa lớn chi Althaea"),
    ("073218", "annabas", "noun", "/əˈnɑːbəz/", "thành phố cảng Annaba ở Algeria"),
    ("073219", "antedated", "verb", "/ˌæntɪˈdeɪtɪd/", "đã ghi lùi ngày trước; có từ trước"),
    ("073220", "antedates", "verb", "/ˌæntɪˈdeɪts/", "ghi lùi ngày; có từ thời trước"),
    ("073221", "antedating", "verb", "/ˌæntɪˈdeɪtɪŋ/", "đang ghi lùi ngày; có trước đó"),
    ("073222", "arterioles", "noun", "/ɑːrˈtɪərioʊlz/", "tiểu động mạch dẫn máu vào mao mạch"),
    ("073223", "asahikawas", "noun", "/ˌɑːsɑːhiˈkɑːwəz/", "thành phố Asahikawa ở Hokkaido"),
    ("073224", "azadirachtas", "noun", "/ˌæzədɪˈræktəz/", "cây sầu đâu xoan Ấn Độ (neem)"),
    ("073225", "backstitched", "verb", "/ˈbækˌstɪtʃt/", "đã khâu mũi đột lùi chắc chắn"),
    ("073226", "backstitches", "noun", "/ˈbækˌstɪtʃɪz/", "mũi khâu đột lùi (may vá)"),
    ("073227", "backstitching", "verb", "/ˈbækˌstɪtʃɪŋ/", "đang khâu mũi đột lùi"),
    ("073228", "bactericides", "noun", "/bækˈtɪərɪˌsaɪdz/", "hóa chất hoặc thuốc diệt vi khuẩn"),
    ("073229", "bambusas", "noun", "/bæmˈbjuːzəz/", "chi Tre trúc thân gỗ (Bambusa)"),
    ("073230", "bicornes", "noun", "/ˈbaɪkɔːrnz/", "mũ hai sừng Napoléon (bicorne)"),
    ("073231", "birdbrains", "noun", "/ˈbɜːrdˌbreɪnz/", "kẻ đầu óc rỗng tuếch ngớ ngẩn"),
    ("073232", "boxfuls", "noun", "/ˈbɒksˌfʊlz/", "lượng chứa đầy một cái hộp"),
    ("073233", "braggers", "noun", "/ˈbræɡərz/", "kẻ hay khoác lác huênh hoang"),
    ("073234", "breughels", "noun", "/ˈbrɔɪɡəlz/", "danh họa Hà Lan Pieter Bruegel"),
    ("073235", "callipered", "verb", "/ˈkælɪpərd/", "đã đo bằng thước kẹp compa (Anh)"),
    ("073236", "callipering", "verb", "/ˈkælɪpərɪŋ/", "đang đo bằng thước kẹp compa (Anh)"),
    ("073237", "cardiomegalies", "noun", "/ˌkɑːrdioʊˈmɛɡəliz/", "chứng tim to phì đại cơ tim"),
    ("073238", "cheviotses", "noun", "/ˈtʃɛviətsɪz/", "dãy đồi Cheviot biên giới Anh-Scốt"),
    ("073239", "cinctures", "noun", "/ˈsɪŋktʃərz/", "dây thắt lưng áo choàng; vành cột"),
    ("073240", "cobwebbier", "adj", "/ˈkɒbˌwɛbiər/", "nhiều màng nhện hơn; mỏng manh hơn"),
    ("073241", "cobwebbiest", "adj", "/ˈkɒbˌwɛbiɪst/", "đầy mạng nhện nhất; mỏng manh nhất"),
    ("073242", "counterplays", "noun", "/ˈkaʊntərˌpleɪz/", "lối đánh phản công đối phó lại"),
    ("073243", "courantes", "noun", "/kʊˈrɑːnts/", "điệu múa cổ điển Pháp courante"),
    ("073244", "curanderas", "noun", "/ˌkʊərənˈdɛərəz/", "nữ thầy lang dân gian Mỹ Latinh"),
    ("073245", "cutworks", "noun", "/ˈkʌtˌwɜːrks/", "nghệ thuật thêu khoét lỗ ren nổi"),
    ("073246", "cyprinidaes", "noun", "/saɪˈprɪnɪˌdiːz/", "họ Cá chép nước ngọt (Cyprinidae)"),
    ("073247", "dandyisms", "noun", "/ˈdændiˌɪzəmz/", "lối sống chải chuốt công tử bột"),
    ("073248", "debasers", "noun", "/dɪˈbeɪsərz/", "kẻ hạ thấp phẩm giá hoặc giá trị"),
    ("073249", "defilades", "noun", "/ˌdɛfɪˈleɪdz/", "công sự che chắn khỏi hỏa lực địch"),
    ("073250", "dermatomes", "noun", "/ˈdɜːrməˌtoʊmz/", "máy lạng da; khoanh da thần kinh"),
    ("073251", "dishtowels", "noun", "/ˈdɪʃˌtaʊəlz/", "khăn vải lau khô chén bát (Mỹ)"),
    ("073252", "distraints", "noun", "/dɪˈstreɪnts/", "lệnh tịch biên giữ tài sản trả nợ"),
    ("073253", "dronabinols", "noun", "/droʊˈnæbɪˌnɒlz/", "hoạt chất dronabinol (THC y tế)"),
    ("073254", "durreses", "noun", "/ˈdʊrəsɪz/", "thành phố cảng Durrës ở Albania"),
    ("073255", "eighters", "noun", "/ˈeɪtərz/", "số tám; người thứ tám; lá bài tám"),
    ("073256", "enamines", "noun", "/ˈɛnəmiːnz/", "hợp chất hữu cơ enamin (hóa học)"),
    ("073257", "endocarps", "noun", "/ˈɛndoʊˌkɑːrps/", "lớp vỏ quả trong cứng (hạch quả)"),
    ("073258", "epididymitises", "noun", "/ˌɛpɪdɪdɪˈmaɪtɪsɪz/", "bệnh viêm mào tinh hoàn (y học)"),
    ("073259", "equidaes", "noun", "/ˈɛkwɪˌdiːz/", "họ Ngựa (ngựa, lừa, ngựa vằn)"),
    ("073260", "erivans", "noun", "/ɛrɪˈvɑːnz/", "thủ đô Yerevan của Armenia (cũ)"),
    ("073261", "flyspecks", "noun", "/ˈflaɪˌspɛks/", "chấm phân ruồi nhỏ; khuyết điểm nhỏ"),
    ("073262", "galactosemias", "noun", "/ɡəˌlæktəˈsiːmiəz/", "bệnh rối loạn chuyển hóa galactô"),
    ("073263", "gaultherias", "noun", "/ɡɔːlˈθɪəriəz/", "cây lộc đề xanh chi Gaultheria"),
    ("073264", "gynoecea", "noun", "/dʒaɪˈniːsiə/", "bộ nhụy gồm các lá noãn của hoa"),
    ("073265", "gynoecia", "noun", "/dʒaɪˈniːʃə/", "bộ nhụy gồm các lá noãn của hoa"),
    ("073266", "gynoeciums", "noun", "/dʒaɪˈniːsiəmz/", "bộ nhụy gồm các lá noãn của hoa"),
    ("073267", "hemianopias", "noun", "/ˌhɛmiəˈnoʊpiəz/", "chứng bán manh mất nửa thị trường"),
    ("073268", "humins", "noun", "/ˈhjuːmɪnz/", "chất hữu cơ đất không tan humin"),
    ("073269", "iliamnas", "noun", "/ˌɪliˈæmnəz/", "cây hoa dâm bụt núi chi Iliamna"),
    ("073270", "imbibitions", "noun", "/ˌɪmbɪˈbɪʃənz/", "sự hút trương nở nước; sự ngấm"),
    ("073271", "indumentums", "noun", "/ˌɪndjʊˈmɛntəmz/", "lớp lông tơ phủ trên thân lá chim"),
    ("073272", "invars", "noun", "/ˈɪnvɑːrz/", "hợp kim ít giãn nở nhiệt Invar"),
    ("073273", "jamberries", "noun", "/ˈdʒæmˌbɛriz/", "cây tầm bóp vàng (thù lù ăn quả)"),
    ("073274", "kartikeyas", "noun", "/ˌkɑːrtɪˈkeɪəz/", "thần chiến tranh Kartikeya Ấn Độ"),
    ("073275", "kettledrums", "noun", "/ˈkɛtəlˌdrʌmz/", "trống định âm timpani dàn nhạc"),
    ("073276", "knickknacks", "noun", "/ˈnɪkˌnæks/", "đồ trang trí lặt vặt bày kệ nhỏ"),
    ("073277", "knuckses", "noun", "/ˈnʌksɪz/", "tay đấm kim loại đeo ngón tay"),
    ("073278", "lactariuses", "noun", "/lækˈtɛəriəsɪz/", "nấm sữa tiết nhựa chi Lactarius"),
    ("073279", "larvicides", "noun", "/ˈlɑːrvɪˌsaɪdz/", "thuốc diệt ấu trùng côn trùng"),
    ("073280", "lauraceaes", "noun", "/lɔːˈreɪʃiˌiːz/", "họ Long não (quế, bơ, hồi)"),
    ("073281", "lisus", "noun", "/ˈliːsuːz/", "dân tộc và tiếng Lật Túc (Lisu)"),
    ("073282", "louisianans", "noun", "/luːˌiːziˈænənz/", "người dân bang Louisiana của Mỹ"),
    ("073283", "lymphocytoses", "noun", "/ˌlɪmfoʊsaɪˈtoʊsiːz/", "tình trạng tăng tế bào lympho máu"),
    ("073284", "mantineas", "noun", "/ˌmæntɪˈniːəz/", "thành cổ Mantinea ở Hy Lạp"),
    ("073285", "mesencephalons", "noun", "/ˌmɛzɛnˈsɛfəlɒnz/", "não giữa (trung não giải phẫu)"),
    ("073286", "methyldopas", "noun", "/ˌmɛθəlˈdoʊpəz/", "thuốc hạ huyết áp methyldopa"),
    ("073287", "micrococci", "noun", "/ˌmaɪkroʊˈkɒkaɪ/", "vi khuẩn cầu nhỏ chi Micrococcus"),
    ("073288", "mislaying", "verb", "/ˌmɪsˈleɪɪŋ/", "đang để thất lạc quên chỗ để"),
    ("073289", "mislays", "verb", "/ˌmɪsˈleɪz/", "để thất lạc quên khuấy mất chỗ để"),
    ("073290", "moldboards", "noun", "/ˈmoʊldˌbɔːrdz/", "tấm diệp cày cong lật úp luống đất"),
    ("073291", "mydriases", "noun", "/mɪˈdraɪəsiːz/", "tình trạng giãn đồng tử mắt (y học)"),
    ("073292", "neotenies", "noun", "/niˈɒtəniz/", "hiện tượng giữ đặc tính ấu trùng"),
    ("073293", "offprints", "noun", "/ˈɒfˌprɪnts/", "bản in trích riêng bài nghiên cứu"),
    ("073294", "ophthalmoplegias", "noun", "/ɒfˌθælmoʊˈpliːdʒəz/", "chứng liệt các cơ vận nhãn mắt"),
    ("073295", "otherworldlinesses", "noun", "/ˌʌðərˈwɜːrldlinəsɪz/", "tính siêu thoát không màng thế tục"),
    ("073296", "oxacillins", "noun", "/ˌɒksəˈsɪlɪnz/", "thuốc kháng sinh oxacillin"),
    ("073297", "oxazepams", "noun", "/ɒkˈsæzɪˌpæmz/", "thuốc an thần giải lo âu oxazepam"),
    ("073298", "palaemons", "noun", "/pəˈliːmɒnz/", "chi Tôm càng nhỏ Palaemon"),
    ("073299", "parcheesis", "noun", "/pɑːrˈtʃiːziz/", "trò chơi cờ xúc xắc Parcheesi"),
    ("073300", "phacoemulsifications", "noun", "/ˌfeɪkoʊɪmʌlsɪfɪˈkeɪʃənz/", "phẫu thuật tán nhuyễn thủy tinh thể"),
    ("073301", "physas", "noun", "/ˈfaɪsəz/", "ốc nước ngọt xoắn trái chi Physa"),
    ("073302", "pimozides", "noun", "/ˈpɪməˌzaɪdz/", "thuốc chống loạn thần pimozide"),
]

with open("scratch/b35_r07_raw_p3.json") as f:
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

with open("scratch/b35_r07_p3.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r07_p3.json OK")
