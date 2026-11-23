import json

rows = [
    ("075003", "fascicules", "noun", "/ˈfæsɪkjuːlz/", "tập sách nhỏ; bó sợi (giải phẫu)"),
    ("075004", "fieldmice", "noun", "/ˈfiːldmaɪs/", "chuột đồng"),
    ("075005", "fieldmouses", "noun", "/ˈfiːldˌmaʊsɪz/", "chuột đồng"),
    ("075006", "flurbiprofens", "noun", "/flʊrˈbɪprəfənz/", "thuốc kháng viêm flurbiprofen"),
    ("075007", "francisellas", "noun", "/ˌfrænsɪˈsɛləz/", "vi khuẩn Francisella (gây bệnh)"),
    ("075008", "garganeys", "noun", "/ˈɡɑːrɡəniz/", "vịt mòng két mày trắng"),
    ("075009", "gearsticks", "noun", "/ˈɡɪrstɪks/", "cần gạt số xe ô tô"),
    ("075010", "grigris", "noun", "/ˈɡriːɡriz/", "bùa hộ mệnh châu Phi (grigri)"),
    ("075011", "guaiacums", "noun", "/ˈɡwaɪəkəmz/", "cây gỗ gaiac; nhựa gỗ gaiac"),
    ("075012", "hemicycles", "noun", "/ˈhɛmɪˌsaɪkəlz/", "hình bán nguyệt; giảng đường vòng"),
    ("075013", "hogfishes", "noun", "/ˈhɒɡˌfɪʃɪz/", "cá mó lợn (hogfish Đại Tây Dương)"),
    ("075014", "homographs", "noun", "/ˈhɒməɡræfs/", "từ đồng dạng khác nghĩa"),
    ("075015", "indapamides", "noun", "/ɪnˈdæpəmaɪdz/", "thuốc lợi tiểu indapamide"),
    ("075016", "kilocalories", "noun", "/ˈkɪləˌkæləriz/", "kilocalo (đơn vị năng lượng)"),
    ("075017", "komondors", "noun", "/ˈkɒməndɔːrz/", "chó chăn cừu lông bện Komondor"),
    ("075018", "labourites", "noun", "/ˈleɪbəraɪts/", "đảng viên Công đảng (Anh)"),
    ("075019", "leucotomies", "noun", "/luːˈkɒtəmiz/", "phẫu thuật cắt thùy trán não"),
    ("075020", "licensers", "noun", "/ˈlaɪsənsərz/", "người cấp giấy phép; kiểm duyệt"),
    ("075021", "logorrheas", "noun", "/ˌlɒɡəˈriːəz/", "chứng nói liên thanh (y học)"),
    ("075022", "louisianians", "noun", "/luˌiːziˈæniənz/", "người bang Louisiana (Mỹ)"),
    ("075023", "lueses", "noun", "/ˈluːɪsiːz/", "bệnh giang mai (y học cổ)"),
    ("075024", "lunkheads", "noun", "/ˈlʌŋkhɛdz/", "người đần độn chậm hiểu (khẩu ngữ)"),
    ("075025", "mackems", "noun", "/ˈmækəmz/", "người vùng Sunderland (Anh)"),
    ("075026", "malacologies", "noun", "/ˌmæləˈkɒlədʒiz/", "ngành nhuyễn thể học"),
    ("075027", "mastopexies", "noun", "/ˈmæstəˌpɛksiz/", "phẫu thuật nâng ngực (y học)"),
    ("075028", "merlons", "noun", "/ˈmɜːrlɒnz/", "đoạn tường chắn nhô trên lũy thành"),
    ("075029", "micrometeoroids", "noun", "/ˌmaɪkroʊˈmiːtiərɔɪdz/", "vi thiên thạch (bụi đá vũ trụ)"),
    ("075030", "misdeals", "noun", "/ˌmɪsˈdiːlz/", "lỗi chia bài sai"),
    ("075031", "moneyers", "noun", "/ˈmʌniərz/", "thợ đúc tiền (lịch sử)"),
    ("075032", "mustachios", "noun", "/məˈstɑːʃoʊz/", "ria mép rậm dài"),
    ("075033", "mustelidaes", "noun", "/mʌˈstɛlɪdiːz/", "họ Chồn (Mustelidae)"),
    ("075034", "needlefishes", "noun", "/ˈniːdəlˌfɪʃɪz/", "cá nhói (cá kìm mỏ dài)"),
    ("075035", "obligati", "noun", "/ˌɒblɪˈɡɑːti/", "bè nhạc bắt buộc (âm nhạc Ý)"),
    ("075036", "obligatos", "noun", "/ˌɒblɪˈɡɑːtoʊz/", "bè nhạc bắt buộc (âm nhạc Ý)"),
    ("075037", "obstinances", "noun", "/ˈɒbstɪnənsɪz/", "tính ngoan cố, bướng bỉnh"),
    ("075038", "oenophiles", "noun", "/ˈiːnəfaɪlz/", "người sành và yêu rượu vang"),
    ("075039", "passeriformeses", "noun", "/ˌpæsərɪˈfɔːrmiːzɪz/", "bộ Sẻ (Passeriformes)"),
    ("075040", "pavises", "noun", "/ˈpævɪsɪz/", "khiên cao che toàn thân (Trung Cổ)"),
    ("075041", "pignuts", "noun", "/ˈpɪɡnʌts/", "cây hồ đào đắng (pignut Bắc Mỹ)"),
    ("075042", "platysmas", "noun", "/pləˈtɪzməz/", "cơ bám da cổ (giải phẫu)"),
    ("075043", "prolificacies", "noun", "/prəˈlɪfɪkəsiz/", "sức sinh sản dồi dào; sự phong phú"),
    ("075044", "protoceratopses", "noun", "/ˌproʊtoʊˈsɛrətɒpsɪz/", "khủng long sừng Protoceratops"),
    ("075045", "proxemicses", "noun", "/prɒkˈsiːmɪksɪz/", "khoa học khoảng cách giao tiếp"),
    ("075046", "quantisations", "noun", "/ˌkwɒntaɪˈzeɪʃənz/", "sự lượng tử hóa"),
    ("075047", "radiolocations", "noun", "/ˌreɪdioʊloʊˈkeɪʃənz/", "sự định vị bằng sóng ra-đa"),
    ("075048", "radiophones", "noun", "/ˈreɪdioʊˌfoʊnz/", "máy điện thoại vô tuyến"),
    ("075049", "roarers", "noun", "/ˈrɔːrərz/", "người gào thét; ngựa thở khò khè"),
    ("075050", "rosebays", "noun", "/ˈroʊzbeɪz/", "cây đỗ quyên lớn; cây liễu lan"),
    ("075051", "sainfoins", "noun", "/ˈseɪnfɔɪnz/", "cây cỏ đậu hồng sainfoin (thức ăn)"),
    ("075052", "scombers", "noun", "/ˈskɒmbərz/", "chi cá thu Đại Tây Dương (Scomber)"),
    ("075053", "selars", "noun", "/ˈsiːlɑːrz/", "chi cá trác, cá chỉ vàng (Selar)"),
    ("075054", "servomechanisms", "noun", "/ˌsɜːrvoʊˈmɛkənɪzəmz/", "cơ cấu chấp hành servo"),
    ("075055", "sporotrichoses", "noun", "/ˌspɒroʊtrɪˈkoʊsiːz/", "bệnh nấm da sporotrichosis"),
    ("075056", "strappers", "noun", "/ˈstræpərz/", "người vạm vỡ; người buộc dây đai"),
    ("075057", "studbooks", "noun", "/ˈstʌdbʊks/", "sổ gia phả giống vật nuôi"),
    ("075058", "successfulnesses", "noun", "/səkˈsɛsfəlnəsɪz/", "sự thành công, thắng lợi"),
    ("075059", "sweetleafs", "noun", "/ˈswiːtliːfs/", "chi cây dung lá ngọt (Symplocos)"),
    ("075060", "syllabubs", "noun", "/ˈsɪləbʌbz/", "món kem sữa đánh rượu ngọt Anh"),
    ("075061", "tetrafluoroethylenes", "noun", "/ˌtɛtrəˌflʊəroʊˈɛθəliːnz/", "khí tetrafluoroetylen (chế Teflon)"),
    ("075062", "toonas", "noun", "/ˈtuːnəz/", "chi xoan mộc, hương xuân (Toona)"),
    ("075063", "topers", "noun", "/ˈtoʊpərz/", "kẻ nghiện rượu nặng, bợm nhậu"),
    ("075064", "transaminations", "noun", "/ˌtrænzˌæmɪˈneɪʃənz/", "phản ứng chuyển nhóm amin"),
    ("075065", "traubels", "noun", "/ˈtraʊbəlz/", "nữ ca sĩ opera Helen Traubel"),
    ("075066", "trepaned", "verb", "/trɪˈpænd/", "đã khoan mở sọ (phẫu thuật)"),
    ("075067", "trepaning", "verb", "/trɪˈpænɪŋ/", "khoan mở sọ (phẫu thuật)"),
    ("075068", "trepanned", "verb", "/trɪˈpænd/", "đã khoan mở sọ (phẫu thuật)"),
    ("075069", "trepanning", "verb", "/trɪˈpænɪŋ/", "khoan mở sọ (phẫu thuật)"),
    ("075070", "trepans", "noun", "/trɪˈpænz/", "mũi khoan sọ; phẫu thuật khoan sọ"),
    ("075071", "tsaritsas", "noun", "/zɑːˈrɪtsəz/", "hoàng hậu Nga (Sa hậu)"),
    ("075072", "tuckets", "noun", "/ˈtʌkɪts/", "khúc kèn hiệu báo tiến quân (cổ)"),
    ("075073", "twirped", "verb", "/twɜːrpt/", "đã ríu rít; đã cư xử ngớ ngẩn"),
    ("075074", "twirping", "verb", "/ˈtwɜːrpɪŋ/", "ríu rít; cư xử ngớ ngẩn"),
    ("075075", "twirps", "noun", "/twɜːrps/", "kẻ ngớ ngẩn đáng ghét (khẩu ngữ)"),
    ("075076", "ultramontanisms", "noun", "/ˌʌltrəˈmɒntənɪzəmz/", "chủ nghĩa quyền tối cao Giáo hoàng"),
    ("075077", "underrunned", "verb", "/ˌʌndərˈrʌnd/", "đã chạy xuyên dưới; trượt giá dưới"),
    ("075078", "underrunning", "verb", "/ˌʌndərˈrʌnɪŋ/", "chạy xuyên dưới; trượt giá dưới"),
    ("075079", "underruns", "verb", "/ˌʌndərˈrʌnz/", "chạy xuyên dưới; trượt giá dưới"),
    ("075080", "valuated", "verb", "/ˈvæljueɪtɪd/", "đã thẩm định giá trị"),
    ("075081", "valuates", "verb", "/ˈvæljueɪts/", "thẩm định giá trị"),
    ("075082", "valuating", "verb", "/ˈvæljueɪtɪŋ/", "thẩm định giá trị"),
    ("075083", "valuators", "noun", "/ˈvæljueɪtərz/", "người thẩm định giá tài sản"),
    ("075084", "wrigglers", "noun", "/ˈrɪɡlərz/", "người uốn éo; bọ gậy, ấu trùng muỗi"),
    ("075085", "xanthates", "noun", "/ˈzænθeɪts/", "muối xanthat (tuyển nổi quặng)"),
    ("075086", "yobbos", "noun", "/ˈjɒboʊz/", "kẻ côn đồ du côn (khẩu ngữ Anh)"),
    ("075087", "zworykins", "noun", "/ˈzwɔːrɪkɪnz/", "nhà phát minh TV V. Zworykin"),
    ("075088", "pediluvium", "noun", "/ˌpɛdɪˈluːviəm/", "bồn ngâm chân thuốc (y học)"),
    ("075089", "pedimental", "adj", "/ˈpɛdɪməntəl/", "thuộc trán tường (kiến trúc)"),
    ("075090", "pedimeter", "noun", "/pɪˈdɪmɪtər/", "máy đếm bước đi; dụng cụ đo cỡ trẻ"),
    ("075091", "pediocactus", "noun", "/ˌpɛdioʊˈkæktəs/", "chi xương rồng Pediocactus (Mỹ)"),
    ("075092", "pedioecetes", "noun", "/ˌpɛdiˈiːsɪtiːz/", "chi gà gô đồng cỏ đuôi nhọn"),
    ("075093", "pedionomus", "noun", "/ˌpɛdiˈɒnəməs/", "chim chạy đồng cỏ Úc (Pedionomus)"),
    ("075094", "pedipalpi", "noun", "/ˌpɛdɪˈpælpaɪ/", "bộ Bọ cạp roi; xúc giác chân"),
    ("075095", "pedipalpous", "adj", "/ˌpɛdɪˈpælpəs/", "có chân xúc giác (hình nhện)"),
    ("075096", "pedlary", "noun", "/ˈpɛdləri/", "nghề bán hàng rong; hàng bán rong"),
    ("075097", "pedobaptism", "noun", "/ˌpiːdoʊˈbæptɪzəm/", "lễ rửa tội cho trẻ sơ sinh"),
    ("075098", "pedobaptist", "noun", "/ˌpiːdoʊˈbæptɪst/", "người ủng hộ rửa tội trẻ sơ sinh"),
    ("075099", "pedodontist", "noun", "/ˌpiːdəˈdɒntɪst/", "nha sĩ nhi khoa"),
    ("075100", "pedogamic", "adj", "/ˌpiːdəˈɡæmɪk/", "thuộc ấu giao (sinh sản ở ấu trùng)"),
    ("075101", "pedogamous", "adj", "/pɪˈdɒɡəməs/", "ấu giao (sinh sản ở ấu trùng)"),
    ("075102", "pedogamy", "noun", "/pɪˈdɒɡəmi/", "hiện tượng ấu giao (sinh học)"),
]

with open("scratch/b36_r01_raw_p1.json", "r", encoding="utf-8") as f:
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

with open("scratch/b36_r01_p1.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b36_r01_p1 saved OK")
