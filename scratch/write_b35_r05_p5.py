import json

items = [
    ("072403", "ouranoses", "noun", "/ˈjʊərənəsɪz/", "thần bầu trời Uranus Hy Lạp cổ"),
    ("072404", "outfights", "verb", "/ˌaʊtˈfaɪts/", "đánh thắng, chiến đấu giỏi hơn"),
    ("072405", "outfought", "verb", "/ˌaʊtˈfɔːt/", "đã đánh thắng chiến đấu giỏi hơn"),
    ("072406", "overbears", "verb", "/ˌoʊvərˈbɛərz/", "áp đảo, lấn át; đè nặng lên"),
    ("072407", "paeonias", "noun", "/piːˈoʊniəz/", "chi Hoa mẫu đơn (Paeonia)"),
    ("072408", "paranthropuses", "noun", "/pæˈrænθrəpəsɪz/", "chi Vượn nhân hình Paranthropus"),
    ("072409", "parodists", "noun", "/ˈpærədɪsts/", "người làm thơ văn nhại châm biếm"),
    ("072410", "patzers", "noun", "/ˈpɑːtsərz/", "kỳ thủ cờ vua đánh dở (khẩu ngữ)"),
    ("072411", "pearlers", "noun", "/ˈpɜːrlərz/", "thợ lặn hoặc tàu mò ngọc trai"),
    ("072412", "peridia", "noun", "/pəˈrɪdiə/", "vỏ bọc quả thể của nấm (sinh học)"),
    ("072413", "peridiums", "noun", "/pəˈrɪdiəmz/", "vỏ bọc quả thể của nấm (sinh học)"),
    ("072414", "philippics", "noun", "/fɪˈlɪpɪks/", "bài diễn văn đả kích nảy lửa"),
    ("072415", "placentations", "noun", "/ˌplæsɛnˈteɪʃənz/", "sự tạo nhau thai; cách đính noãn"),
    ("072416", "poltroons", "noun", "/pɒlˈtruːnz/", "kẻ hèn nhát nhút nhát đáng khinh"),
    ("072417", "polyanthuses", "noun", "/ˌpɒliˈænθəsɪz/", "cây hoa anh thảo nhiều hoa"),
    ("072418", "powderpuffs", "noun", "/ˈpaʊdərˌpʌfs/", "bông phấn trang điểm; người yếu ớt"),
    ("072419", "prevues", "noun", "/ˈpriːvjuːz/", "buổi chiếu trước; đoạn giới thiệu"),
    ("072420", "primaquines", "noun", "/ˈpraɪməˌkwiːnz/", "thuốc điều trị sốt rét primaquin"),
    ("072421", "procuresses", "noun", "/prəˈkjʊərɪsɪz/", "nữ môi giới mại dâm (từ cũ)"),
    ("072422", "provitamins", "noun", "/proʊˈvaɪtəmɪnz/", "tiền chất vitamin chuyển hóa được"),
    ("072423", "pseudopods", "noun", "/ˈsuːdəˌpɒdz/", "chân giả của tế bào hay trùng amip"),
    ("072424", "rascalities", "noun", "/ræˈskælɪtiz/", "thói ranh ma láu cá xỏ lá"),
    ("072425", "recusancies", "noun", "/ˈrɛkjʊzənsiz/", "sự bất tuân không theo quốc giáo"),
    ("072426", "redtails", "noun", "/ˈrɛdˌteɪlz/", "diều hâu đuôi đỏ; chim đuôi đỏ"),
    ("072427", "rorquals", "noun", "/ˈrɔːrkwəlz/", "cá voi rãnh họng (họ Cá voi xanh)"),
    ("072428", "rubialeses", "noun", "/ˌruːbiˈeɪliːzɪz/", "bộ Cà phê (thực vật hạt kín)"),
    ("072429", "saltations", "noun", "/sælˈteɪʃənz/", "sự nhảy vọt; sự tiến hóa đột biến"),
    ("072430", "scaremongers", "noun", "/ˈskɛərˌmʌŋɡərz/", "kẻ gieo rắc tin đồn gây hoang mang"),
    ("072431", "smarms", "noun", "/smɑːrmz/", "lời nịnh hót giả tạo dẻo miệng"),
    ("072432", "smartas", "noun", "/ˈsmɑːrtəz/", "tín đồ Ấn Độ giáo phái Smarta"),
    ("072433", "sorbing", "verb", "/ˈsɔːrbɪŋ/", "đang hấp thụ hoặc hấp phụ (hóa)"),
    ("072434", "sorbs", "noun", "/sɔːrbz/", "quả thanh lương trà; cây thanh trà"),
    ("072435", "stachyses", "noun", "/ˈsteɪkɪsɪz/", "cây xô thơm đồng chi Stachys"),
    ("072436", "stagier", "adj", "/ˈsteɪdʒiər/", "kịch tính giả tạo sân khấu hơn"),
    ("072437", "stagiest", "adj", "/ˈsteɪdʒiɪst/", "kịch tính giả tạo sân khấu nhất"),
    ("072438", "streptocarpi", "noun", "/ˌstrɛptəˈkɑːrpaɪ/", "cây hoa anh thảo Cape (quả xoắn)"),
    ("072439", "sulfadiazines", "noun", "/ˌsʌlfəˈdaɪəziːnz/", "thuốc kháng sinh sulfadiazine"),
    ("072440", "surtouts", "noun", "/sɜːrˈtuːts/", "áo choàng dài ôm eo nam giới xưa"),
    ("072441", "sympathectomies", "noun", "/ˌsɪmpəˈθɛktəmiz/", "phẫu thuật cắt thần kinh giao cảm"),
    ("072442", "unoriginalities", "noun", "/ˌʌnərɪdʒɪˈnælɪtiz/", "tính thiếu sáng tạo rập khuôn"),
    ("072443", "utricles", "noun", "/ˈjuːtrɪkəlz/", "túi nhỏ (giải phẫu); quả bế có màng"),
    ("072444", "vertebratas", "noun", "/ˌvɜːrtɪˈbreɪtəz/", "phân ngành Động vật có xương sống"),
    ("072445", "victuallers", "noun", "/ˈvɪtələrz/", "người cung cấp lương thực; chủ quán"),
    ("072446", "volvoxes", "noun", "/ˈvɒlvɒksɪz/", "tảo lục hình cầu tập đoàn volvox"),
    ("072447", "wrynecks", "noun", "/ˈraɪˌnɛks/", "chim vẹo cổ; chứng vẹo cổ cơ"),
    ("072448", "zaireans", "noun", "/zaɪˈɪəriənz/", "người dân nước Zaire (Congo cũ)"),
    ("072449", "zoviraxes", "noun", "/zoʊˈvaɪræksɪz/", "thuốc kháng vi-rút Zovirax"),
    ("072450", "abutilons", "noun", "/əˈbjuːtɪˌlɒnz/", "cây cối xay hoa chuông lồng đèn"),
    ("072451", "aerolites", "noun", "/ˈɛərəˌlaɪts/", "thiên thạch đá rơi từ vũ trụ"),
    ("072452", "alkies", "noun", "/ˈælkiz/", "người nghiện rượu nặng (lóng)"),
    ("072453", "anaximeneses", "noun", "/ˌænækˈsɪmɪˌniːzɪz/", "triết gia Hy Lạp cổ Anaximenes"),
    ("072454", "anthozoas", "noun", "/ˌænθəˈzoʊəz/", "lớp San hô và hải quỳ (Anthozoa)"),
    ("072455", "apiarists", "noun", "/ˈeɪpiərɪsts/", "người nuôi ong chuyên nghiệp"),
    ("072456", "apophyses", "noun", "/əˈpɒfɪˌsiːz/", "mấu lồi xương; chỗ phình rêu nấm"),
    ("072457", "arcseconds", "noun", "/ˈɑːrkˌsɛkəndz/", "đơn vị góc giây cung (1/3600 độ)"),
    ("072458", "argiopes", "noun", "/ɑːrˈdʒaɪəpiz/", "nhện lưới chữ X chi Argiope"),
    ("072459", "arouets", "noun", "/ˌɑːruˈeɪz/", "tên họ thật của Voltaire (Arouet)"),
    ("072460", "athabascans", "noun", "/ˌæθəˈbæskənz/", "người và ngữ hệ Athabasca Bắc Mỹ"),
    ("072461", "atomisations", "noun", "/ˌætəmaɪˈzeɪʃənz/", "sự phun tơi thành hạt mịn (Anh)"),
    ("072462", "atropas", "noun", "/ˈætrəpəz/", "cà độc dược belladonna (Atropa)"),
    ("072463", "avalokiteshvaras", "noun", "/ˌɑːvəloʊkɪˈtɛʃvərəz/", "Quán Thế Âm Bồ Tát (Phật giáo)"),
    ("072464", "backbites", "verb", "/ˈbækˌbaɪts/", "nói xấu sau lưng, đặt điều bôi nhọ"),
    ("072465", "balanuses", "noun", "/ˈbælənəsɪz/", "chi Hà biển bám đá (Balanus)"),
    ("072466", "baykals", "noun", "/baɪˈkɑːlz/", "hồ Baikal sâu nhất thế giới ở Nga"),
    ("072467", "boatbuilders", "noun", "/ˈboʊtˌbɪldərz/", "thợ đóng và sửa chữa tàu thuyền"),
    ("072468", "boccis", "noun", "/ˈbɒtʃiz/", "trò ném bi sắt hoặc gỗ bocce Ý"),
    ("072469", "buyis", "noun", "/buːˈjiz/", "dân tộc và tiếng Bố Y (Trung Quốc)"),
    ("072470", "carcharodons", "noun", "/kɑːrˈkærəˌdɒnz/", "chi Cá mập trắng lớn Carcharodon"),
    ("072471", "cerambycidaes", "noun", "/ˌsɛræmˈbɪsɪˌdiːz/", "họ Xén tóc bọ râu dài"),
    ("072472", "cheatgrasses", "noun", "/ˈtʃiːtˌɡræsɪz/", "cỏ dại bromus xâm lấn vùng khô"),
    ("072473", "cinerarias", "noun", "/ˌsɪnəˈrɛəriəz/", "hoa cúc lá bạc cánh rực cineraria"),
    ("072474", "clapperboards", "noun", "/ˈklæpərˌbɔːrdz/", "bảng dập clapper đánh dấu cảnh phim"),
    ("072475", "collectivizes", "verb", "/kəˈlɛktɪˌvaɪzɪz/", "tập thể hóa đất đai tài sản"),
    ("072476", "collectivizing", "verb", "/kəˈlɛktɪˌvaɪzɪŋ/", "đang tập thể hóa đất đai tài sản"),
    ("072477", "debones", "verb", "/diːˈboʊnz/", "rút lọc bỏ xương ra khỏi thịt cá"),
    ("072478", "deboning", "verb", "/diːˈboʊnɪŋ/", "đang rút lọc bỏ xương thịt cá"),
    ("072479", "denominationalisms", "noun", "/dɪˌnɒmɪˈneɪʃənəˌlɪzəmz/", "chủ nghĩa bè phái giáo phái riêng"),
    ("072480", "desynchronizations", "noun", "/diːˌsɪŋkrənaɪˈzeɪʃənz/", "sự mất đồng bộ lệch pha nhịp"),
    ("072481", "ecdyses", "noun", "/ˈɛkdɪˌsiːz/", "quá trình lột xác ở chân khớp"),
    ("072482", "electroencephalographs", "noun", "/ɪˌlɛktroʊɛnˈsɛfələˌɡræfs/", "máy đo ghi điện não đồ (EEG)"),
    ("072483", "enlaced", "verb", "/ɪnˈleɪst/", "đã đan xen lồng bện quấn vào nhau"),
    ("072484", "enlacing", "verb", "/ɪnˈleɪsɪŋ/", "đang đan xen lồng bện quấn nhau"),
    ("072485", "felids", "noun", "/ˈfiːlɪdz/", "động vật họ Mèo (mèo, hổ, báo)"),
    ("072486", "fermatas", "noun", "/fɛərˈmɑːtəz/", "dấu ngân tự do kéo dài nốt nhạc"),
    ("072487", "flavones", "noun", "/ˈfleɪvoʊnz/", "hợp chất sắc tố thực vật flavon"),
    ("072488", "florilegia", "noun", "/ˌflɔːrɪˈliːdʒə/", "tuyển tập hợp tuyển văn thơ hay"),
    ("072489", "florilegiums", "noun", "/ˌflɔːrɪˈliːdʒəmz/", "tuyển tập hợp tuyển văn thơ hay"),
    ("072490", "flummoxed", "verb", "/ˈflʌməkst/", "đã làm bối rối hoang mang tột độ"),
    ("072491", "flummoxes", "verb", "/ˈflʌməksɪz/", "làm bối rối hoang mang khó hiểu"),
    ("072492", "flummoxing", "verb", "/ˈflʌməksɪŋ/", "đang làm bối rối hoang mang"),
    ("072493", "geminations", "noun", "/ˌdʒɛmɪˈneɪʃənz/", "sự gấp đôi âm tiết; sự lặp đôi từ"),
    ("072494", "gibraltarians", "noun", "/ˌdʒɪbrɔːlˈtɛəriənz/", "người dân vùng lãnh thổ Gibraltar"),
    ("072495", "granicuses", "noun", "/ɡrəˈnaɪkəsɪz/", "trận sông Granicus (Alexandros)"),
    ("072496", "grappellis", "noun", "/ɡrɑːˈpɛliz/", "nghệ sĩ vĩ cầm jazz S. Grappelli"),
    ("072497", "gummas", "noun", "/ˈɡʌməz/", "gôm giang mai (u hạt mềm dưới da)"),
    ("072498", "gummata", "noun", "/ˈɡʌmətə/", "gôm giang mai (u hạt mềm dưới da)"),
    ("072499", "hairstreaks", "noun", "/ˈhɛərˌstriːks/", "bướm xanh đuôi mảnh (họ Bướm xanh)"),
    ("072500", "haptoglobins", "noun", "/ˌhæptəˈɡloʊbɪnz/", "protein huyết tương haptoglobin"),
    ("072501", "harvestmans", "noun", "/ˈhɑːrvɪstmənz/", "nhện chân dài (bộ Opiliones)"),
    ("072502", "hatmakers", "noun", "/ˈhætˌmeɪkərz/", "thợ thiết kế và làm mũ đội đầu"),
]

with open("scratch/b35_r05_raw_p5.json") as f:
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

with open("scratch/b35_r05_p5.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r05_p5.json OK")
