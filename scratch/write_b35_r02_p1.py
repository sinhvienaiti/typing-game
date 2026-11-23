import json

items = [
    ("070503", "uncrosses", "verb", "/ʌnˈkrɒsɪz/", "mở chéo; tách hai vật bắt chéo"),
    ("070504", "uncrossing", "verb", "/ʌnˈkrɒsɪŋ/", "đang mở chéo; đang tách bắt chéo"),
    ("070505", "unsaying", "verb", "/ʌnˈseɪɪŋ/", "đang rút lại lời đã nói"),
    ("070506", "unsays", "verb", "/ʌnˈsɛz/", "rút lại lời đã nói; nói ngược lại"),
    ("070507", "vesicas", "noun", "/vɪˈsaɪkəz/", "bọng màng mỏng; bàng quang (y học)"),
    ("070508", "wajdas", "noun", "/ˈvaɪdəz/", "đạo diễn Ba Lan Andrzej Wajda"),
    ("070509", "warrantees", "noun", "/ˌwɒrənˈtiːz/", "người được bảo hành hoặc bảo đảm"),
    ("070510", "abors", "noun", "/ˈɑːbɔːrz/", "người dân tộc và tiếng Abor Ấn Độ"),
    ("070511", "adsorbates", "noun", "/ædˈsɔːrbeɪts/", "chất bị hấp phụ lên bề mặt"),
    ("070512", "aegisthuses", "noun", "/iːˈdʒɪsθəsɪz/", "nhân vật Aegisthus (Hy Lạp cổ)"),
    ("070513", "andorrans", "noun", "/ænˈdɔːrənz/", "người dân Công quốc Andorra"),
    ("070514", "antheses", "noun", "/ænˈθiːsiːz/", "thời kỳ hoa nở rộ hoàn toàn"),
    ("070515", "antifeminists", "noun", "/ˌæntiˈfɛmɪnɪsts/", "người phản đối chủ nghĩa nữ quyền"),
    ("070516", "applecarts", "noun", "/ˈæpəlˌkɑːrts/", "xe đẩy bán táo; kế hoạch sẵn"),
    ("070517", "ashurbanipals", "noun", "/ˌɑːʃʊərˈbɑːnɪˌpɑːlz/", "vua Assyria Ashurbanipal cổ đại"),
    ("070518", "autoradiographies", "noun", "/ˌɔːtoʊreɪdiˈɒɡrəfiz/", "kỹ thuật chụp ảnh phóng xạ tự ghi"),
    ("070519", "baldrics", "noun", "/ˈbɔːldrɪks/", "dây đai đeo chéo vai cài kiếm"),
    ("070520", "bodonis", "noun", "/bəˈdoʊniz/", "phông chữ Bodoni; nhà in Ý Bodoni"),
    ("070521", "bursters", "noun", "/ˈbɜːrstərz/", "thuốc nổ phá đạn; máy tách giấy"),
    ("070522", "butenes", "noun", "/ˈbjuːtiːnz/", "hiđrocacbon anken buten (C4H8)"),
    ("070523", "carchariases", "noun", "/kɑːrˈkɛəriəsɪz/", "chi Cá mập cát Carcharias"),
    ("070524", "congruities", "noun", "/kənˈɡruːɪtiz/", "tính tương thích phù hợp hài hòa"),
    ("070525", "crotalarias", "noun", "/ˌkroʊtəˈlɛəriəz/", "cây lục lạc thuộc chi Crotalaria"),
    ("070526", "cymes", "noun", "/saɪmz/", "cụm hoa xim mọc phân nhánh"),
    ("070527", "devilfishes", "noun", "/ˈdɛvəlˌfɪʃɪz/", "cá đuối manta; bạch tuộc khổng lồ"),
    ("070528", "dialectologies", "noun", "/ˌdaɪəlɛkˈtɒlədʒiz/", "ngành phương ngữ học"),
    ("070529", "energisers", "noun", "/ˈɛnərdʒaɪzərz/", "người tiếp sức; máy kích điện (Anh)"),
    ("070530", "essentialities", "noun", "/ɪˌsɛnʃiˈælɪtiz/", "tính thiết yếu cốt lõi"),
    ("070531", "feverfews", "noun", "/ˈfiːvərˌfjuːz/", "cây cúc thơm chữa đau đầu"),
    ("070532", "fibrinolyses", "noun", "/ˌfaɪbrɪˈnɒlɪsiːz/", "quá trình tiêu sợi huyết"),
    ("070533", "flimflammed", "verb", "/ˈflɪmˌflæmd/", "đã lừa bịp phỉnh phờ (khẩu ngữ)"),
    ("070534", "flimflamming", "verb", "/ˈflɪmˌflæmɪŋ/", "đang lừa bịp phỉnh phờ (khẩu ngữ)"),
    ("070535", "flimflams", "noun", "/ˈflɪmˌflæmz/", "trò lừa bịp bợm; chuyện nói nhảm"),
    ("070536", "fluoroscopes", "noun", "/ˈflʊərəˌskoʊps/", "máy chiếu X-quang huỳnh quang"),
    ("070537", "freebooters", "noun", "/ˈfriːˌbuːtərz/", "hải tặc cướp biển; kẻ cướp bóc"),
    ("070538", "galiums", "noun", "/ˈɡeɪliəmz/", "cây sữa đông thuộc chi Galium"),
    ("070539", "garnisheed", "verb", "/ˌɡɑːrnɪˈʃiːd/", "đã sai áp khấu trừ lương trả nợ"),
    ("070540", "garnisheeing", "verb", "/ˌɡɑːrnɪˈʃiːɪŋ/", "đang sai áp khấu trừ lương trả nợ"),
    ("070541", "garnishees", "noun", "/ˌɡɑːrnɪˈʃiːz/", "người bị phong tỏa tiền trả nợ"),
    ("070542", "gerberts", "noun", "/ˈɡɜːrbərts/", "Giáo hoàng Sylvester II (Gerbert)"),
    ("070543", "gravidas", "noun", "/ˈɡrævɪdəz/", "sản phụ; phụ nữ đang mang thai"),
    ("070544", "groynes", "noun", "/ɡrɔɪnz/", "kè mỏ hàn chắn sóng giữ cát (Anh)"),
    ("070545", "guilloches", "noun", "/ɡɪˈloʊʃɪz/", "hoa văn đan xoắn guilloché"),
    ("070546", "gunnels", "noun", "/ˈɡʌnəlz/", "mạn trên thân thuyền; cá gunnel"),
    ("070547", "haematologists", "noun", "/ˌhiːməˈtɒlədʒɪsts/", "bác sĩ chuyên khoa huyết học (Anh)"),
    ("070548", "harelips", "noun", "/ˈhɛərˌlɪps/", "tật sứt môi bẩm sinh"),
    ("070549", "haricots", "noun", "/ˈhærɪˌkoʊz/", "đậu cô ve; hạt đậu trắng (Anh)"),
    ("070550", "hederas", "noun", "/ˈhɛdərəz/", "cây thường xuân thuộc chi Hedera"),
    ("070551", "helleboruses", "noun", "/ˈhɛlɪˌbɔːrəsɪz/", "cây hoa hồng Giáng sinh Helleborus"),
    ("070552", "hoteis", "noun", "/hoʊˈteɪz/", "Phật Di Lặc Bố Đại (Hotei Nhật)"),
    ("070553", "housebuilders", "noun", "/ˈhaʊsˌbɪldərz/", "nhà thầu hoặc thợ xây dựng nhà ở"),
    ("070554", "hymnbooks", "noun", "/ˈhɪmˌbʊks/", "sách thánh ca hát trong nhà thờ"),
    ("070555", "hyperboloids", "noun", "/haɪˈpɜːrbəˌlɔɪdz/", "mặt cong bậc hai hyperboloid"),
    ("070556", "idealisations", "noun", "/aɪˌdiːəlaɪˈzeɪʃənz/", "sự lý tưởng hóa (cách viết Anh)"),
    ("070557", "inoculants", "noun", "/ɪˈnɒkjʊlənts/", "chất cấy vi sinh; vắc-xin chủng"),
    ("070558", "internees", "noun", "/ˌɪntɜːrˈniːz/", "người bị giam giữ quản thúc"),
    ("070559", "katzenjammers", "noun", "/ˈkætsənˌdʒæmərz/", "cơn nôn nao sau say; tiếng ồn ào"),
    ("070560", "kieslowskis", "noun", "/kjɛʃˈlɒfskiz/", "đạo diễn Ba Lan Kieślowski"),
    ("070561", "lateens", "noun", "/ləˈtiːnz/", "cánh buồm tam giác buồm la-tinh"),
    ("070562", "locutions", "noun", "/loʊˈkjuːʃənz/", "lối diễn đạt; cụm từ đặc trưng"),
    ("070563", "loirs", "noun", "/lwɑːrz/", "chuột sóc lớn châu Âu (chi Glis)"),
    ("070564", "miniaturisations", "noun", "/ˌmɪnɪtʃəraɪˈzeɪʃənz/", "sự thu nhỏ kích thước (Anh)"),
    ("070565", "monegasques", "noun", "/ˌmɒnɪˈɡæsks/", "người dân Công quốc Monaco"),
    ("070566", "mugwumps", "noun", "/ˈmʌɡˌwʌmps/", "chính khách độc lập không theo đảng"),
    ("070567", "nanometres", "noun", "/ˈnænoʊˌmiːtərz/", "đơn vị độ dài nanômét (Anh)"),
    ("070568", "neurosyphilises", "noun", "/ˌnjʊəroʊˈsɪfɪlɪsɪz/", "bệnh giang mai thần kinh"),
    ("070569", "nevirapines", "noun", "/nəˈvɪrəpiːnz/", "thuốc kháng HIV nevirapine"),
    ("070570", "nightriders", "noun", "/ˈnaɪtˌraɪdərz/", "băng kỵ sĩ khủng bố ban đêm (Mỹ)"),
    ("070571", "noeses", "noun", "/noʊˈiːsiːz/", "hành vi nhận thức lý trí (triết)"),
    ("070572", "novelisations", "noun", "/ˌnɒvəlaɪˈzeɪʃənz/", "sự chuyển thể thành tiểu thuyết"),
    ("070573", "nubbins", "noun", "/ˈnʌbɪnz/", "bắp ngô lép nhỏ; mẩu thừa nhỏ"),
    ("070574", "odontologies", "noun", "/ˌoʊdɒnˈtɒlədʒiz/", "nha khoa học nghiên cứu về răng"),
    ("070575", "onegas", "noun", "/oʊˈnɛɡəz/", "hồ Onega ở vùng tây bắc Nga"),
    ("070576", "onsagers", "noun", "/ˈɒnˌsɑːɡərz/", "nhà hóa học Nobel Lars Onsager"),
    ("070577", "outlawries", "noun", "/ˈaʊtˌlɔːriz/", "tình trạng đặt ngoài vòng pháp luật"),
    ("070578", "paddlewheels", "noun", "/ˈpædəlˌwiːlz/", "bánh guồng đạp nước đẩy tàu thủy"),
    ("070579", "panglosses", "noun", "/ˈpænˌɡlɒsɪz/", "người lạc quan mù quáng vô lý"),
    ("070580", "passionflowers", "noun", "/ˈpæʃənˌflaʊərz/", "hoa lạc tiên (hoa chanh dây)"),
    ("070581", "pichis", "noun", "/ˈpiːtʃiz/", "tatu nhỏ pichi; cây thuốc Nam Mỹ"),
    ("070582", "piutes", "noun", "/ˈpaɪjuːts/", "người dân tộc Paiute bản địa Mỹ"),
    ("070583", "placekickers", "noun", "/ˈpleɪsˌkɪkərz/", "cầu thủ đá phạt bóng bầu dục Mỹ"),
    ("070584", "prognosticators", "noun", "/prɒɡˈnɒstɪˌkeɪtərz/", "người tiên đoán dự báo tương lai"),
    ("070585", "pyrethrums", "noun", "/paɪˈriːθrəmz/", "cây cúc trừ sâu pyrethrum"),
    ("070586", "rachets", "noun", "/ˈrætʃɪts/", "cơ cấu bánh cóc hãm một chiều"),
    ("070587", "ruttier", "adj", "/ˈrʌtiər/", "lồi lõm vết bánh xe hơn"),
    ("070588", "ruttiest", "adj", "/ˈrʌtiɪst/", "lồi lõm vết bánh xe nhất"),
    ("070589", "sagittas", "noun", "/səˈdʒɪtəz/", "chòm sao Thiên Tiễn; đường tên cung"),
    ("070590", "sailmakers", "noun", "/ˈseɪlˌmeɪkərz/", "thợ may vá và chế tạo buồm tàu"),
    ("070591", "schmalzes", "noun", "/ʃmɑːltsɪz/", "sự ủy mị sướt mướt quá mức"),
    ("070592", "scholiasts", "noun", "/ˈskoʊliˌæsts/", "học giả chú giải văn bản cổ điển"),
    ("070593", "serialisms", "noun", "/ˈsɪəriəˌlɪzəmz/", "kỹ thuật sáng tác nhạc mười hai âm"),
    ("070594", "simuliums", "noun", "/sɪˈmjuːliəmz/", "ruồi đen thuộc chi Simulium"),
    ("070595", "snackers", "noun", "/ˈsnækərz/", "người hay ăn vặt giữa bữa"),
    ("070596", "steelyards", "noun", "/ˈstiːlˌjɑːrdz/", "cân đòn móc treo có quả cân trượt"),
    ("070597", "styptics", "noun", "/ˈstɪptɪks/", "chất cầm máu se vết thương"),
    ("070598", "subprograms", "noun", "/ˈsʌbˌproʊɡræmz/", "chương trình con (lập trình)"),
    ("070599", "sweatboxes", "noun", "/ˈswɛtˌbɒksɪz/", "phòng nóng bức chật hẹp; buồng giam"),
    ("070600", "synchronisms", "noun", "/ˈsɪŋkrəˌnɪzəmz/", "sự đồng thời; trường phái hội họa"),
    ("070601", "tabuns", "noun", "/ˈtɑːbuːnz/", "chất độc thần kinh tabun (GA)"),
    ("070602", "tegus", "noun", "/ˈteɪɡuːz/", "thằn lằn lớn Nam Mỹ tegu"),
]

with open("scratch/b35_r02_raw_p1.json") as f:
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

with open("scratch/b35_r02_p1.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r02_p1.json OK")
