import json

items = [
    ("069703", "maledictions", "noun", "/ˌmælɪˈdɪkʃənz/", "lời nguyền rủa trù ẻo cay độc"),
    ("069704", "melasmas", "noun", "/məˈlæzməz/", "vết nám sạm mảng nâu trên da mặt"),
    ("069705", "mhos", "noun", "/moʊz/", "đơn vị độ dẫn điện mho (siemens)"),
    ("069706", "mithraisms", "noun", "/ˈmɪθreɪˌɪzəmz/", "tín ngưỡng thờ thần Mithras La Mã"),
    ("069707", "monogamists", "noun", "/məˈnɒɡəmɪsts/", "người theo chế độ một vợ một chồng"),
    ("069708", "montgolfiers", "noun", "/mɒntˈɡɒlfiərz/", "anh em phát minh khinh khí cầu Pháp"),
    ("069709", "muckrakers", "noun", "/ˈmʌkˌreɪkərz/", "nhà báo điều tra phanh phui bê bối"),
    ("069710", "mundanities", "noun", "/mʌnˈdænɪtiz/", "chuyện trần tục tầm thường"),
    ("069711", "muskallunge", "noun", "/ˈmʌskəˌlʌndʒ/", "cá chó khổng lồ Bắc Mỹ muskie"),
    ("069712", "muskellunges", "noun", "/ˈmʌskəˌlʌndʒɪz/", "cá chó nước ngọt lớn Bắc Mỹ"),
    ("069713", "natatoria", "noun", "/ˌneɪtəˈtɔːriə/", "bể bơi trong nhà có mái che"),
    ("069714", "natatoriums", "noun", "/ˌneɪtəˈtɔːriəmz/", "bể bơi công cộng trong nhà (Mỹ)"),
    ("069715", "neighbourlinesses", "noun", "/ˈneɪbərlinəsɪz/", "tình làng nghĩa xóm thân thiện"),
    ("069716", "neutralists", "noun", "/ˈnjuːtrəlɪsts/", "người theo đường lối trung lập"),
    ("069717", "nichromes", "noun", "/ˈnaɪˌkroʊmz/", "hợp kim niken-crom làm dây đốt nóng"),
    ("069718", "nortriptylines", "noun", "/nɔːrˈtrɪptɪˌliːnz/", "thuốc chống trầm cảm nortriptylin"),
    ("069719", "outrageousnesses", "noun", "/aʊtˈreɪdʒəsnəsɪz/", "tính thái quá quái gở gây phẫn nộ"),
    ("069720", "palases", "noun", "/pəˈlɑːsɪz/", "cây hoa rừng đỏ palas Ấn Độ"),
    ("069721", "parricides", "noun", "/ˈpærɪˌsaɪdz/", "tội giết cha mẹ; kẻ sát hại người"),
    ("069722", "pessaries", "noun", "/ˈpɛsəriz/", "vòng nâng âm đạo; thuốc đặt âm đạo"),
    ("069723", "physalises", "noun", "/ˈfaɪsəlɪsɪz/", "cây tầm bóp thù lù chi Physalis"),
    ("069724", "porcs", "noun", "/pɔːrks/", "thịt lợn thịt heo (từ mượn Pháp)"),
    ("069725", "prorated", "verb", "/proʊˈreɪtɪd/", "đã chia phân bổ theo tỷ lệ phần"),
    ("069726", "prorates", "verb", "/proʊˈreɪts/", "phân bổ tính theo tỷ lệ tương ứng"),
    ("069727", "prorating", "verb", "/proʊˈreɪtɪŋ/", "đang tính phân bổ theo tỷ lệ phần"),
    ("069728", "prothoraces", "noun", "/proʊˈθɔːrəsiːz/", "đốt ngực trước mang đôi chân đầu"),
    ("069729", "prothoraxes", "noun", "/proʊˈθɔːræksɪz/", "đốt ngực trước của côn trùng"),
    ("069730", "psilocins", "noun", "/ˈsaɪləsɪnz/", "chất gây ảo giác psilocin từ nấm"),
    ("069731", "psyllids", "noun", "/ˈsɪlɪdz/", "rầy chổng cánh nhỏ chích nhựa cây"),
    ("069732", "radiochemistries", "noun", "/ˌreɪdioʊˈkɛmɪstriz/", "ngành hóa học phóng xạ đồng vị"),
    ("069733", "rebozos", "noun", "/rəˈboʊzoʊz/", "khăn choàng vai dài phụ nữ Mexico"),
    ("069734", "retroflexes", "verb", "/ˈrɛtroʊˌflɛksɪz/", "uốn cong quặt ngược về phía sau"),
    ("069735", "retroflexing", "verb", "/ˈrɛtroʊˌflɛksɪŋ/", "đang uốn cong ngược về phía sau"),
    ("069736", "roughhoused", "verb", "/ˈrʌfˌhaʊzd/", "đã nô đùa xô đẩy ầm ĩ mạnh bạo"),
    ("069737", "roughhouses", "verb", "/ˈrʌfˌhaʊzɪz/", "nô đùa vật lộn ồn ào thô bạo"),
    ("069738", "roughhousing", "verb", "/ˈrʌfˌhaʊzɪŋ/", "đang nô đùa xô đẩy ồn ào mạnh"),
    ("069739", "sambres", "noun", "/ˈsɑːmbrəz/", "sông Sambre chảy qua Pháp và Bỉ"),
    ("069740", "scorekeepers", "noun", "/ˈskɔːrˌkiːpərz/", "người ghi điểm số trọng tài bàn"),
    ("069741", "scrummages", "noun", "/ˈskrʌmɪdʒɪz/", "pha tranh bóng xáp lá cà bầu dục"),
    ("069742", "shouters", "noun", "/ˈʃaʊtərz/", "người la hét to tiếng gào thét"),
    ("069743", "shrovetides", "noun", "/ˈʃroʊvˌtaɪdz/", "ba ngày trước Thứ Tư Lễ Tro Mùa"),
    ("069744", "siouans", "noun", "/ˈsuːənz/", "người bản địa và ngữ hệ Sioux"),
    ("069745", "skulds", "noun", "/skʊldz/", "nữ thần tương lai Skuld Bắc Âu"),
    ("069746", "spitzbergens", "noun", "/ˈspɪtsˌbɜːrɡənz/", "đảo Spitsbergen vùng Svalbard Na Uy"),
    ("069747", "squaluses", "noun", "/ˈskweɪləsɪz/", "cá nhám gai thuộc chi Squalus"),
    ("069748", "stammerers", "noun", "/ˈstæmərərz/", "người mắc tật nói lắp bắp ngọng"),
    ("069749", "stonefishes", "noun", "/ˈstoʊnˌfɪʃɪz/", "cá mặt quỷ ngụy trang cực độc biển"),
    ("069750", "stoups", "noun", "/stuːps/", "chậu đựng nước thánh cửa nhà thờ"),
    ("069751", "sundaneses", "noun", "/ˌsʌndəˈniːzɪz/", "người và tiếng Sunda ở Indonesia"),
    ("069752", "supernaturalisms", "noun", "/ˌsuːpərˈnætʃrəlˌɪzəmz/", "niềm tin vào thế lực siêu nhiên"),
    ("069753", "swaged", "verb", "/sweɪdʒd/", "đã rèn ép dập khuôn kim loại nguội"),
    ("069754", "swages", "noun", "/ˈsweɪdʒɪz/", "khuôn rèn tạo hình kim loại"),
    ("069755", "sweetbriars", "noun", "/ˈswiːtˌbraɪərz/", "cây tầm xuân lá thơm như táo"),
    ("069756", "tamburlaines", "noun", "/ˈtæmbərˌleɪnz/", "chinh tướng Timur Lenk vùng Trung Á"),
    ("069757", "taphouses", "noun", "/ˈtæpˌhaʊzɪz/", "quán bia quán rượu bán vòi rót"),
    ("069758", "tchads", "noun", "/tʃɑːdz/", "hồ Tchad; nước Cộng hòa Tchad"),
    ("069759", "tenderizers", "noun", "/ˈtɛndəˌraɪzərz/", "búa dần hoặc chất làm mềm thịt"),
    ("069760", "toolsheds", "noun", "/ˈtuːlˌʃɛdz/", "nhà kho lán chứa dụng cụ làm vườn"),
    ("069761", "torticollises", "noun", "/ˌtɔːrtɪˈkɒlɪsɪz/", "chứng vẹo cổ co cứng cơ ức đòn"),
    ("069762", "treponemas", "noun", "/ˌtrɛpəˈniːməz/", "xoắn khuẩn giang mai chi Treponema"),
    ("069763", "treponemata", "noun", "/ˌtrɛpəˈniːmətə/", "xoắn khuẩn mảnh thuộc chi Treponema"),
    ("069764", "twitterers", "noun", "/ˈtwɪtərərz/", "chim hót líu lo; người đăng Twitter"),
    ("069765", "twopences", "noun", "/ˈtʌpənsɪz/", "đồng xu hai xu cổ của nước Anh"),
    ("069766", "undocked", "verb", "/ʌnˈdɒkt/", "đã rời bến; đã tách ghép trạm tàu"),
    ("069767", "undocks", "verb", "/ʌnˈdɒks/", "rời bến cảng; tách ghép tàu vũ trụ"),
    ("069768", "urethritises", "noun", "/ˌjʊərɪˈθraɪtɪsɪz/", "bệnh viêm nhiễm đường niệu đạo"),
    ("069769", "urths", "noun", "/ɜːrθs/", "nữ thần số mệnh quá khứ Urth"),
    ("069770", "velocipedes", "noun", "/vəˈlɒsɪˌpiːdz/", "xe đạp thô sơ cổ điển thời đầu"),
    ("069771", "yahis", "noun", "/ˈjɑːhiz/", "bộ tộc bản địa Yahi California"),
    ("069772", "yawped", "verb", "/jɔːpt/", "đã kêu la oang oang ầm ĩ (Mỹ)"),
    ("069773", "yawping", "verb", "/ˈjɔːpɪŋ/", "đang gào kêu ầm ĩ inh tai nhức óc"),
    ("069774", "yawps", "verb", "/jɔːps/", "gào la oang oang ồn ào khó chịu"),
    ("069775", "zills", "noun", "/zɪlz/", "chũm chọe nhỏ đeo ngón tay múa"),
    ("069776", "abetments", "noun", "/əˈbɛtmənts/", "hành vi xúi giục tiếp tay phạm tội"),
    ("069777", "adenomyoses", "noun", "/ˌædənoʊmaɪˈoʊsiːz/", "bệnh lạc nội mạc trong cơ tử cung"),
    ("069778", "aegirs", "noun", "/ˈeɪɡɪərz/", "thần biển cả Aegir; sóng triều dâng"),
    ("069779", "amytals", "noun", "/ˈæmɪˌtɔːlz/", "thuốc ngủ an thần barbiturat Amytal"),
    ("069780", "annonas", "noun", "/əˈnoʊnəz/", "cây na mãng cầu thuộc chi Annona"),
    ("069781", "annotators", "noun", "/ˈænəˌteɪtərz/", "người chú giải gán nhãn dữ liệu"),
    ("069782", "anuras", "noun", "/əˈnjʊərəz/", "bộ Không đuôi gồm ếch nhái cóc"),
    ("069783", "apparatchiks", "noun", "/ˌæpəˈrætʃɪks/", "cán bộ máy móc quan liêu bộ máy"),
    ("069784", "arcsecs", "noun", "/ˈɑːrkˌsɛks/", "giây cung bằng 1/3600 độ góc"),
    ("069785", "ariettas", "noun", "/ˌɑːriˈɛtəz/", "khúc hát aria ngắn gọn nhẹ nhàng"),
    ("069786", "ariette", "noun", "/ˌɑːriˈɛt/", "đoạn hát đơn ngắn trong nhạc kịch"),
    ("069787", "arities", "noun", "/ˈærɪtiz/", "số lượng tham số của hàm toán học"),
    ("069788", "ascarises", "noun", "/ˈæskərɪsɪz/", "giun đũa ký sinh ruột chi Ascaris"),
    ("069789", "astrometries", "noun", "/əˈstrɒmɪtriz/", "trắc lượng học đo vị trí thiên thể"),
    ("069790", "atroposes", "noun", "/ˈætrəpɒsɪz/", "nữ thần số mệnh cắt chỉ Atropos"),
    ("069791", "baics", "noun", "/baɪks/", "tiếng dân tộc Bạch ở Vân Nam"),
    ("069792", "balaramas", "noun", "/ˌbɑːləˈrɑːməz/", "thần Balarama trong Ấn Độ giáo"),
    ("069793", "basenjis", "noun", "/bəˈsɛndʒiz/", "giống chó săn châu Phi không sủa"),
    ("069794", "bemas", "noun", "/ˈbiːməz/", "bục giảng cao trong giáo đường cổ"),
    ("069795", "blighters", "noun", "/ˈblaɪtərz/", "gã đáng ghét; anh chàng tội nghiệp"),
    ("069796", "boleti", "noun", "/boʊˈliːtaɪ/", "nấm thông lỗ xốp chi Boletus"),
    ("069797", "boletuses", "noun", "/boʊˈliːtəsɪz/", "nấm thông mũ dày ăn được Boletus"),
    ("069798", "bolides", "noun", "/ˈboʊlaɪdz/", "sao băng cầu lửa sáng rực phát nổ"),
    ("069799", "bonces", "noun", "/ˈbɒnsɪz/", "cái đầu (lóng Anh); viên bi to"),
    ("069800", "bronchopneumonias", "noun", "/ˌbrɒŋkoʊnjuːˈmoʊniəz/", "bệnh viêm phế quản phổi lan tỏa"),
    ("069801", "bulgier", "adj", "/ˈbʌldʒiər/", "phồng to phình lồi ra ngoài hơn"),
    ("069802", "bulgiest", "adj", "/ˈbʌldʒiɪst/", "phồng to phình lồi ra ngoài nhất"),
]

with open("scratch/b34_r10_raw_p3.json") as f:
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

with open("scratch/b34_r10_p3.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r10_p3.json OK")
