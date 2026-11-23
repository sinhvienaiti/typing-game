import json

items = [
    ("071603", "siderites", "noun", "/ˈsɪdəˌraɪts/", "quặng sắt siderit; thiên thạch sắt"),
    ("071604", "skegs", "noun", "/skɛɡz/", "vây ổn định đuôi ván lướt; ky phụ"),
    ("071605", "somites", "noun", "/ˈsoʊmaɪts/", "đốt phôi sinh học (trung bì)"),
    ("071606", "steatites", "noun", "/ˈstiːəˌtaɪts/", "đá xà phòng bột talc steatit"),
    ("071607", "subsidisations", "noun", "/ˌsʌbsɪdaɪˈzeɪʃənz/", "khoản tiền trợ cấp tài trợ (Anh)"),
    ("071608", "succoths", "noun", "/sʊˈkɒts/", "lễ Lều Tạm Sukkot của Do Thái"),
    ("071609", "swearwords", "noun", "/ˈswɛərˌwɜːrdz/", "từ chửi thề; lời nói tục tĩu"),
    ("071610", "thyrotropins", "noun", "/ˌθaɪroʊˈtroʊpɪnz/", "hoóc-môn kích thích tuyến giáp TSH"),
    ("071611", "totemisms", "noun", "/ˈtoʊtəˌmɪzəmz/", "tín ngưỡng vật tổ tô-tem"),
    ("071612", "trifoliatas", "noun", "/ˌtraɪfoʊliˈɑːtəz/", "cây cam ba lá chịu lạnh"),
    ("071613", "tursiopses", "noun", "/tɜːrˈsaɪɒpsɪz/", "chi Cá heo mũi chai (Tursiops)"),
    ("071614", "waltzers", "noun", "/ˈwɔːltsərz/", "người khiêu vũ điệu van-xơ"),
    ("071615", "whistlestoped", "verb", "/ˈwɪsəlˌstɒpt/", "đã vận động tranh cử bằng tàu hỏa"),
    ("071616", "whistlestoping", "verb", "/ˈwɪsəlˌstɒpɪŋ/", "đang đi vận động tranh cử dọc tuyến"),
    ("071617", "whistlestops", "verb", "/ˈwɪsəlˌstɒps/", "vận động tranh cử tại các thị trấn"),
    ("071618", "wilnos", "noun", "/ˈvɪlnoʊz/", "thành phố Vilnius (tên Ba Lan cũ)"),
    ("071619", "winesaps", "noun", "/ˈwaɪnˌsæps/", "giống táo đỏ giòn vị rượu Winesap"),
    ("071620", "wineskins", "noun", "/ˈwaɪnˌskɪnz/", "bầu da đựng rượu vang kiểu cổ"),
    ("071621", "yardies", "noun", "/ˈjɑːrdiz/", "thành viên băng đảng gốc Jamaica"),
    ("071622", "zingibers", "noun", "/ˈzɪndʒɪbərz/", "chi Cây gừng thực vật (Zingiber)"),
    ("071623", "airbrakes", "noun", "/ˈɛərˌbreɪks/", "phanh hơi khí nén (xe tải, tàu)"),
    ("071624", "alosas", "noun", "/əˈloʊsəz/", "chi Cá trích sông mòi dầu Alosa"),
    ("071625", "anlagen", "noun", "/ˈɑːnlɑːɡən/", "mầm sơ khai cơ quan phôi thai"),
    ("071626", "anlages", "noun", "/ˈɑːnlɑːɡɪz/", "mầm sơ khai cơ quan phôi thai"),
    ("071627", "aphasics", "noun", "/əˈfeɪzɪks/", "người mắc chứng mất ngôn ngữ"),
    ("071628", "arthropathies", "noun", "/ɑːrˈθrɒpəθiz/", "bệnh lý tổn thương khớp xương"),
    ("071629", "ascidians", "noun", "/əˈsɪdiənz/", "hải tiêu sống bám đáy biển"),
    ("071630", "astrodynamicses", "noun", "/ˌæstroʊdaɪˈnæmɪksɪz/", "ngành cơ học quỹ đạo thiên thể"),
    ("071631", "autofluorescences", "noun", "/ˌɔːtoʊflʊəˈrɛsənsɪz/", "hiện tượng tự phát huỳnh quang mô"),
    ("071632", "barcarolles", "noun", "/ˌbɑːrkəˈrɒlz/", "khúc hát chèo thuyền Venice"),
    ("071633", "basketfuls", "noun", "/ˈbæskɪtˌfʊlz/", "lượng chứa đầy một giỏ hay rổ"),
    ("071634", "beechnuts", "noun", "/ˈbiːtʃˌnʌts/", "hạt quả cây dẻ gai beech"),
    ("071635", "bjas", "noun", "/ˌbiː dʒeɪ ˈeɪz/", "Cục Hỗ trợ Tư pháp Mỹ (BJA)"),
    ("071636", "booklovers", "noun", "/ˈbʊkˌlʌvərz/", "người say mê yêu thích đọc sách"),
    ("071637", "cabmans", "noun", "/ˈkæbmənz/", "tài xế xe taxi hoặc xe ngựa (cũ)"),
    ("071638", "capetians", "noun", "/kəˈpiːʃənz/", "thành viên vương triều Capet Pháp"),
    ("071639", "carvedilols", "noun", "/kɑːrˈvɛdɪˌlɒlz/", "thuốc tim mạch hạ áp carvedilol"),
    ("071640", "corydalises", "noun", "/kəˈrɪdəlɪsɪz/", "cây hoa tử hoa địa đinh Corydalis"),
    ("071641", "curbstones", "noun", "/ˈkɜːrbˌstoʊnz/", "đá bó vỉa hè ngăn lề đường (Mỹ)"),
    ("071642", "daucuses", "noun", "/ˈdɔːkəsɪz/", "chi Cà rốt thực vật (Daucus)"),
    ("071643", "dendroctonuses", "noun", "/dɛnˈdrɒktənəsɪz/", "bọ cánh cứng đục vỏ cây thông"),
    ("071644", "drusens", "noun", "/ˈdruːzənz/", "cặn tinh thể drusen ở võng mạc mắt"),
    ("071645", "dryopterises", "noun", "/ˌdraɪɒpˈtɛrɪsɪz/", "chi Dương xỉ vảy gấm Dryopteris"),
    ("071646", "echinodermatas", "noun", "/ɪˌkaɪnoʊˈdɜːrmətəz/", "ngành Da gai (sao biển, cầu gai)"),
    ("071647", "electromyograms", "noun", "/ɪˌlɛktroʊˈmaɪəˌɡræmz/", "điện cơ đồ ghi hoạt động cơ"),
    ("071648", "empyemas", "noun", "/ˌɛmpaɪˈiːməz/", "tràn mủ khoang màng phổi (y học)"),
    ("071649", "esoxes", "noun", "/ˈɛsɒksɪz/", "chi Cá chó nước ngọt Esox"),
    ("071650", "eubacterias", "noun", "/ˌjuːbækˈtɪəriəz/", "nhóm Vi khuẩn thật sự (Eubacteria)"),
    ("071651", "fartleks", "noun", "/ˈfɑːrtˌlɛks/", "bài tập chạy biến tốc fartlek"),
    ("071652", "gearsets", "noun", "/ˈɡɪərˌsɛts/", "bộ cụm bánh răng truyền động"),
    ("071653", "gigots", "noun", "/ˈdʒɪɡəts/", "đùi cừu nướng; tay áo phồng vai"),
    ("071654", "greengages", "noun", "/ˈɡriːnˌɡeɪdʒɪz/", "mận xanh ngọt châu Âu greengage"),
    ("071655", "gucks", "noun", "/ɡʌks/", "chất nhầy nhớt bẩn dính (khẩu ngữ)"),
    ("071656", "haliotides", "noun", "/ˌhæliˈoʊtɪdiːz/", "chi Bào ngư biển (Haliotis)"),
    ("071657", "hemagglutinations", "noun", "/ˌhiːməˌɡluːtɪˈneɪʃənz/", "hiện tượng ngưng kết hồng cầu"),
    ("071658", "hexoses", "noun", "/ˈhɛksoʊsɪz/", "đường đơn sáu cacbon (hexose)"),
    ("071659", "hipbones", "noun", "/ˈhɪpˌboʊnz/", "xương chậu xương hông"),
    ("071660", "hirschsprungs", "noun", "/ˈhɪərʃˌsprʌŋz/", "bác sĩ Harald Hirschsprung"),
    ("071661", "hydroceles", "noun", "/ˈhaɪdrəˌsiːlz/", "tràn dịch màng tinh hoàn (y học)"),
    ("071662", "immortelles", "noun", "/ˌɪmɔːrˈtɛlz/", "hoa cúc bất tử giữ dáng khi khô"),
    ("071663", "indigenes", "noun", "/ˈɪndɪdʒiːnz/", "người dân bản địa; loài bản địa"),
    ("071664", "inspirited", "verb", "/ɪnˈspɪrɪtɪd/", "đã tiếp thêm sinh khí phấn chấn"),
    ("071665", "inspirits", "verb", "/ɪnˈspɪrɪts/", "truyền sinh khí cổ vũ phấn chấn"),
    ("071666", "invaginations", "noun", "/ɪnˌvædʒɪˈneɪʃənz/", "sự lồng vào; sự lõm vào trong"),
    ("071667", "kopecks", "noun", "/ˈkoʊpɛks/", "đồng xu kopeck (1/100 đồng rúp Nga)"),
    ("071668", "kopeks", "noun", "/ˈkoʊpɛks/", "đồng xu kopeck (1/100 đồng rúp)"),
    ("071669", "kummels", "noun", "/ˈkʊməlz/", "rượu mùi vị thì là Ba Tư kümmel"),
    ("071670", "kwangjus", "noun", "/ˈkwɑːŋdʒuːz/", "thành phố Gwangju của Hàn Quốc"),
    ("071671", "laconians", "noun", "/ləˈkoʊniənz/", "người xứ Laconia Hy Lạp (Sparta)"),
    ("071672", "lamaseries", "noun", "/ˈlɑːməˌsɛriz/", "tu viện của các Lạt Ma Tây Tạng"),
    ("071673", "lambkins", "noun", "/ˈlæmkɪnz/", "cừu con non đáng yêu"),
    ("071674", "laparoscopes", "noun", "/ləˈpærəˌskoʊps/", "ống kính nội soi ổ bụng"),
    ("071675", "lexemes", "noun", "/ˈlɛksiːmz/", "từ vị (đơn vị từ vựng ngôn ngữ)"),
    ("071676", "lobatas", "noun", "/loʊˈbeɪtəz/", "bộ Sứa lược thùy biển Lobata"),
    ("071677", "lunations", "noun", "/luːˈneɪʃənz/", "chu kỳ tuần trăng (29,5 ngày)"),
    ("071678", "macumbas", "noun", "/məˈkuːmbəz/", "tín ngưỡng dân gian Brazil Macumba"),
    ("071679", "maquiladoras", "noun", "/mɑːˌkiːləˈdɔːrəz/", "nhà máy gia công miễn thuế Mexico"),
    ("071680", "mergenthalers", "noun", "/ˈmɜːrɡənˌθɑːlərz/", "nhà sáng chế Ottmar Mergenthaler"),
    ("071681", "mesoblasts", "noun", "/ˈmɛzoʊˌblæsts/", "lá phôi giữa (trung bì phôi)"),
    ("071682", "mineralized", "verb", "/ˈmɪnərəˌlaɪzd/", "đã khoáng hóa thành đá hoặc muối"),
    ("071683", "mineralizes", "verb", "/ˈmɪnərəˌlaɪzɪz/", "khoáng hóa thành chất khoáng"),
    ("071684", "mineralizing", "verb", "/ˈmɪnərəˌlaɪzɪŋ/", "đang khoáng hóa thành chất khoáng"),
    ("071685", "misspeaking", "verb", "/mɪsˈspiːkɪŋ/", "đang lỡ lời nói hớ sai sót"),
    ("071686", "misspeaks", "verb", "/mɪsˈspiːks/", "lỡ lời nói hớ sai ý"),
    ("071687", "mucunas", "noun", "/mjʊˈkjuːnəz/", "cây đậu mèo ngứa thuộc chi Mucuna"),
    ("071688", "mummers", "noun", "/ˈmʌmərz/", "diễn viên kịch câm mặt nạ dân gian"),
    ("071689", "needlecrafts", "noun", "/ˈniːdəlˌkræfts/", "nghề thêu thùa đan móc thủ công"),
    ("071690", "nightwalkers", "noun", "/ˈnaɪtˌwɔːkərz/", "giun đất bò đêm; người đi đêm"),
    ("071691", "njords", "noun", "/njɔːrdz/", "thần biển Njörðr Bắc Âu"),
    ("071692", "offerers", "noun", "/ˈɒfərərz/", "người đề nghị; người dâng lễ vật"),
    ("071693", "oncidiums", "noun", "/ɒnˈsɪdiəmz/", "hoa lan vũ nữ thuộc chi Oncidium"),
    ("071694", "palaestras", "noun", "/pəˈlɛstrəz/", "trường đấu vật Hy Lạp La Mã cổ"),
    ("071695", "paltered", "verb", "/ˈpɔːltərd/", "đã nói lập lờ né tránh; mặc cả"),
    ("071696", "palters", "verb", "/ˈpɔːltərz/", "nói lập lờ thoái thác; mặc cả"),
    ("071697", "paygrades", "noun", "/ˈpeɪˌɡreɪdz/", "ngạch bậc lương công chức quân đội"),
    ("071698", "pentoxifyllines", "noun", "/pɛnˈtɒksɪˌfɪliːnz/", "thuốc tuần hoàn máu pentoxifylline"),
    ("071699", "pleurotuses", "noun", "/plʊˈrɒtəsɪz/", "chi Nấm bào ngư (nấm sò)"),
    ("071700", "pondweeds", "noun", "/ˈpɒndˌwiːdz/", "rong đuôi chồn nước ngọt (rong ao)"),
    ("071701", "porkpies", "noun", "/ˈpɔːrkˌpaɪz/", "bánh nhân thịt nguội; mũ vành hẹp"),
    ("071702", "prescriptivisms", "noun", "/prɪˈskrɪptɪˌvɪzəmz/", "chủ nghĩa chuẩn mực ngôn ngữ"),
]

with open("scratch/b35_r04_raw_p2.json") as f:
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

with open("scratch/b35_r04_p2.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r04_p2.json OK")
