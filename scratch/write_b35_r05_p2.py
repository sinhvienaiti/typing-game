import json

items = [
    ("072103", "tabulators", "noun", "/ˈtæbjʊˌleɪtərz/", "máy lập bảng thẻ đục lỗ; phím Tab"),
    ("072104", "teratologies", "noun", "/ˌtɛrəˈtɒlədʒiz/", "ngành quái thai học (dị tật thai)"),
    ("072105", "throstles", "noun", "/ˈθrɒsəlz/", "chim hoét ca hát (Anh); máy kéo sợi"),
    ("072106", "tobramycins", "noun", "/ˌtoʊbrəˈmaɪsɪnz/", "thuốc kháng sinh tobramycin"),
    ("072107", "truckled", "verb", "/ˈtrʌkəld/", "đã khúm núm nịnh bợ khuất phục"),
    ("072108", "truckles", "noun", "/ˈtrʌkəlz/", "giường đẩy gầm thấp; bánh xe nhỏ"),
    ("072109", "truenesses", "noun", "/ˈtruːnəsɪz/", "tính chân thực trung thực đúng đắn"),
    ("072110", "tungstates", "noun", "/ˈtʌŋsteɪts/", "muối hóa học tungstat (vonfram)"),
    ("072111", "turfans", "noun", "/tʊərˈfɑːnz/", "ốc đảo Turpan (Thổ Lỗ Phồn)"),
    ("072112", "ubermenschen", "noun", "/ˈuːbərˌmɛnʃən/", "hình mẫu Siêu nhân (Nietzsche)"),
    ("072113", "ubermensches", "noun", "/ˈuːbərˌmɛnʃɪz/", "hình mẫu Siêu nhân (Nietzsche)"),
    ("072114", "uncomfortablenesses", "noun", "/ʌnˈkʌmfərtəbəlnəsɪz/", "sự bất tiện khó chịu gượng gạo"),
    ("072115", "usherettes", "noun", "/ˌʌʃəˈrɛts/", "nữ nhân viên dẫn chỗ rạp phim"),
    ("072116", "utricularias", "noun", "/juːˌtrɪkjʊˈlɛəriəz/", "cây rong bẫy mồi (chi Bèo đất)"),
    ("072117", "wollastonites", "noun", "/wʊˈlæstəˌnaɪts/", "khoáng vật silicat wollastonit"),
    ("072118", "yellowlegses", "noun", "/ˈjɛloʊˌlɛɡzɪz/", "chim choắt chân vàng Bắc Mỹ"),
    ("072119", "zinnemanns", "noun", "/ˈzɪnəmənz/", "đạo diễn Mỹ Fred Zinnemann"),
    ("072120", "zoysias", "noun", "/ˈzɔɪziəz/", "cỏ nhung Nhật thảm cỏ Zoysia"),
    ("072121", "alcaeuses", "noun", "/ælˈsiːəsɪz/", "thi sĩ Hy Lạp cổ đại Alcaeus"),
    ("072122", "aldactones", "noun", "/ælˈdæktoʊnz/", "thuốc lợi tiểu giữ kali Aldactone"),
    ("072123", "amelanchiers", "noun", "/ˌæmɪˈlæŋkiərz/", "cây bụi hoa tháng Sáu Amelanchier"),
    ("072124", "beldams", "noun", "/ˈbɛldəmz/", "bà lão đanh đá xấu xí (từ cổ)"),
    ("072125", "bestrides", "verb", "/bɪˈstraɪdz/", "cưỡi vắt chân qua; đứng dạng chân"),
    ("072126", "bestriding", "verb", "/bɪˈstraɪdɪŋ/", "đang cưỡi vắt qua; đứng dạng chân"),
    ("072127", "betatrons", "noun", "/ˈbeɪtəˌtrɒnz/", "máy gia tốc hạt điện tử betatron"),
    ("072128", "blennies", "noun", "/ˈblɛniz/", "cá bống biển nhỏ trơn không vảy"),
    ("072129", "botflies", "noun", "/ˈbɒtˌflaɪz/", "ruồi trâu ký sinh gây dòi da"),
    ("072130", "bouffes", "noun", "/buːfs/", "vở nhạc kịch hài Pháp cổ điển"),
    ("072131", "brassicaceaes", "noun", "/ˌbræsɪˈkeɪʃiˌiːz/", "họ Cải (cải bắp, su hào, súp lơ)"),
    ("072132", "cachalots", "noun", "/ˈkæʃəˌlɒts/", "cá nhà táng đầu vuông khổng lồ"),
    ("072133", "carambolas", "noun", "/ˌkærəmˈboʊləz/", "quả khế năm múi (cây khế)"),
    ("072134", "cartloads", "noun", "/ˈkɑːrtˌloʊdz/", "lượng hàng chất đầy một xe đẩy"),
    ("072135", "chanties", "noun", "/ˈʃæntiz/", "bài hò kéo neo làm việc thủy thủ"),
    ("072136", "charadriuses", "noun", "/kəˈreɪdriəsɪz/", "chi Chim choi choi (Charadrius)"),
    ("072137", "christmastides", "noun", "/ˈkrɪsməsˌtaɪdz/", "mùa lễ hội Giáng sinh (12 ngày)"),
    ("072138", "citrins", "noun", "/ˈsɪtrɪnz/", "chất màu thực vật citrin; độc tố"),
    ("072139", "cogitations", "noun", "/ˌkɒdʒɪˈteɪʃənz/", "sự trầm tư suy ngẫm sâu sắc"),
    ("072140", "colorimetries", "noun", "/ˌkʌləˈrɪmɪtriz/", "phép đo so màu phân tích hóa học"),
    ("072141", "crammers", "noun", "/ˈkræmərz/", "lớp hoặc sách luyện thi cấp tốc"),
    ("072142", "crawdaddies", "noun", "/ˈkrɔːˌdædiz/", "tôm hùm đất nước ngọt (khẩu ngữ)"),
    ("072143", "crossbenchers", "noun", "/ˈkrɒsˌbɛntʃərz/", "nghị sĩ độc lập không theo đảng"),
    ("072144", "decadrons", "noun", "/ˈdɛkəˌdrɒnz/", "thuốc kháng viêm Decadron"),
    ("072145", "dissolvers", "noun", "/dɪˈzɒlvərz/", "máy khuấy hòa tan; người giải tán"),
    ("072146", "erythrinas", "noun", "/ˌɛrɪˈθraɪnəz/", "cây vông nem thuộc chi Erythrina"),
    ("072147", "flambes", "verb", "/flɑːmˈbeɪz/", "đốt rượu cháy bùng lửa (ẩm thực)"),
    ("072148", "fledgelings", "noun", "/ˈflɛdʒlɪŋz/", "chim non mới ra ràng; người non nớt"),
    ("072149", "fraises", "noun", "/freɪzɪz/", "cổ áo xếp nếp xưa; hàng cọc chông"),
    ("072150", "gingersnaps", "noun", "/ˈdʒɪndʒərˌsnæps/", "bánh quy gừng nướng giòn tan"),
    ("072151", "glipizides", "noun", "/ˈɡlɪpɪˌzaɪdz/", "thuốc hạ đường huyết glipizide"),
    ("072152", "gongoras", "noun", "/ˈɡɒŋɡərəz/", "thi sĩ Tây Ban Nha Luis de Góngora"),
    ("072153", "greylags", "noun", "/ˈɡreɪˌlæɡz/", "ngỗng xám hoang dã châu Âu"),
    ("072154", "gyrfalcons", "noun", "/ˈdʒɜːrˌfɒlkənz/", "chim ưng bắc cực lớn nhất"),
    ("072155", "habitants", "noun", "/ˈhæbɪtənts/", "cư dân; nông dân Pháp-Canada xưa"),
    ("072156", "hagglers", "noun", "/ˈhæɡlərz/", "người hay kỳ kèo mặc cả giá"),
    ("072157", "hemoglobinurias", "noun", "/ˌhiːməɡloʊbɪˈnjʊəriəz/", "chứng đái ra huyết sắc tố (y học)"),
    ("072158", "iambs", "noun", "/ˈaɪæmz/", "nhịp thơ iamb (nhẹ trước nhấn sau)"),
    ("072159", "idyls", "noun", "/ˈaɪdəlz/", "thơ mục đồng; cảnh bình yên quê"),
    ("072160", "imperviousnesses", "noun", "/ɪmˈpɜːrviəsnəsɪz/", "tính không thấm nước; sự bất động"),
    ("072161", "impolitenesses", "noun", "/ˌɪmpəˈlaɪtnəsɪz/", "thái độ bất lịch sự khiếm nhã"),
    ("072162", "indictions", "noun", "/ɪnˈdɪkʃənz/", "chu kỳ thuế mười lăm năm La Mã cổ"),
    ("072163", "kneelers", "noun", "/ˈniːlərz/", "ghế đệm quỳ cầu nguyện; người quỳ"),
    ("072164", "lactaids", "noun", "/ˈlækteɪdz/", "men tiêu hóa sữa Lactaid (Mỹ)"),
    ("072165", "leitmotivs", "noun", "/ˈlaɪtmoʊˌtiːfs/", "nét nhạc chủ đạo; chủ đề xuyên suốt"),
    ("072166", "leontiefs", "noun", "/liˈɒntiɛfs/", "nhà kinh tế học Wassily Leontief"),
    ("072167", "limekilns", "noun", "/ˈlaɪmˌkɪlnz/", "lò nung đá vôi tạo vôi sống"),
    ("072168", "liquidambars", "noun", "/ˌlɪkwɪdˈæmbɑːrz/", "cây sau sau phong hương lấy nhựa"),
    ("072169", "liverworts", "noun", "/ˈlɪvərˌwɜːrts/", "ngành Rêu tản; cây thảo mộc gan"),
    ("072170", "lubavitchers", "noun", "/luːˈbɑːvɪtʃərz/", "tín đồ nhánh Do Thái Lubavitch"),
    ("072171", "melanopluses", "noun", "/ˌmɛləˈnɒpləsɪz/", "chi Châu chấu cánh ngắn Bắc Mỹ"),
    ("072172", "metonyms", "noun", "/ˈmɛtənɪmz/", "từ hoán dụ thay thế tên gọi"),
    ("072173", "micropteruses", "noun", "/maɪˈkrɒptərəsɪz/", "chi Cá vược đen Bắc Mỹ Micropterus"),
    ("072174", "muscadets", "noun", "/ˈmʌskəˌdɛts/", "rượu vang trắng khô Pháp Muscadet"),
    ("072175", "muskats", "noun", "/ˈmʌskæts/", "nho thơm Muscat; rượu vang Muscat"),
    ("072176", "muumuus", "noun", "/ˈmuːmuːz/", "váy suông rộng truyền thống Hawaii"),
    ("072177", "myelomeningoceles", "noun", "/ˌmaɪəloʊmɪˈnɪŋɡoʊˌsiːlz/", "dị tật thoát vị tủy màng tủy"),
    ("072178", "myosotises", "noun", "/ˌmaɪəˈsoʊtɪsɪz/", "chi Hoa lưu ly (xin đừng quên tôi)"),
    ("072179", "nibelungenlieds", "noun", "/ˈniːbəlʊŋənˌliːdz/", "bản anh hùng ca Đức Nibelungenlied"),
    ("072180", "niggards", "noun", "/ˈnɪɡərdz/", "kẻ keo kiệt bủn xỉn hà tiện (cổ)"),
    ("072181", "noctilucae", "noun", "/ˌnɒktɪˈluːsiː/", "sinh vật đơn bào phát quang biển"),
    ("072182", "noctilucas", "noun", "/ˌnɒktɪˈluːkəz/", "sinh vật phát sáng biển đêm"),
    ("072183", "nosegays", "noun", "/ˈnoʊzˌɡeɪz/", "bó hoa nhỏ thơm cầm tay làm quà"),
    ("072184", "paronychias", "noun", "/ˌpærəˈnɪkiəz/", "bệnh viêm chín mé quanh móng tay"),
    ("072185", "partygoers", "noun", "/ˈpɑːrtiˌɡoʊərz/", "người hay đi dự tiệc tùng giao lưu"),
    ("072186", "patristicses", "noun", "/pəˈtrɪstɪksɪz/", "ngành nghiên cứu Giáo phụ Ki-tô"),
    ("072187", "pedologies", "noun", "/pɪˈdɒlədʒiz/", "thổ nhưỡng học (đất); khoa trẻ em"),
    ("072188", "pekans", "noun", "/ˈpiːkənz/", "chồn fisher châu Mỹ; hạt hồ đào"),
    ("072189", "philomaths", "noun", "/ˈfɪləˌmæθs/", "người hiếu học say mê tri thức"),
    ("072190", "planarias", "noun", "/pləˈnɛəriəz/", "chi Sán lông dẹp nước ngọt Planaria"),
    ("072191", "plicates", "verb", "/ˈplaɪkeɪts/", "gấp nếp xếp nếp song song"),
    ("072192", "plicating", "verb", "/ˈplaɪkeɪtɪŋ/", "đang gấp nếp xếp nếp song song"),
    ("072193", "postpositions", "noun", "/ˌpoʊstpəˈzɪʃənz/", "hậu giới từ đứng sau danh từ"),
    ("072194", "prehensions", "noun", "/prɪˈhɛnʃənz/", "sự nắm bắt cầm giữ; sự lĩnh hội"),
    ("072195", "quicksets", "noun", "/ˈkwɪkˌsɛts/", "cành giâm hàng rào sống (táo gai)"),
    ("072196", "quietists", "noun", "/ˈkwaɪɪtɪsts/", "tín đồ thuyết Tĩnh tâm tôn giáo"),
    ("072197", "raffinoses", "noun", "/ˈræfɪˌnoʊsɪz/", "đường ba phân tử raffinose"),
    ("072198", "salamandras", "noun", "/ˌsæləˈmændrəz/", "chi Kỳ giông lửa châu Âu"),
    ("072199", "salvagers", "noun", "/ˈsælvɪdʒərz/", "người trục vớt cứu hộ tài sản đắm"),
    ("072200", "sarcomeres", "noun", "/ˈsɑːrkəˌmɪərz/", "đơn vị co cơ cơ bản sarcomere"),
    ("072201", "sauerbratens", "noun", "/ˈsaʊərˌbrɑːtənz/", "món thịt bò ướp giấm hầm kiểu Đức"),
    ("072202", "scarabaeidaes", "noun", "/ˌskærəˈbiːɪˌdiːz/", "họ Bọ hung bọ cánh cứng phân"),
]

with open("scratch/b35_r05_raw_p2.json") as f:
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

with open("scratch/b35_r05_p2.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r05_p2.json OK")
