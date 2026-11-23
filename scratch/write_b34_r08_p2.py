import json

items = [
    ("068603", "yamanis", "noun", "/ˈjɑːməniz/", "người dân nước Yemen (biến thể)"),
    ("068604", "adulterates", "verb", "/əˈdʌltəˌreɪts/", "pha tạp chất giả làm giảm phẩm"),
    ("068605", "alkalosises", "noun", "/ˌælkəˈloʊsɪsɪz/", "tình trạng nhiễm kiềm máu bệnh lý"),
    ("068606", "amahs", "noun", "/ˈɑːməz/", "vú em bảo mẫu ở châu Á (từ cũ)"),
    ("068607", "amoraim", "noun", "/əˈmɔːreɪɪm/", "học giả Kinh Talmud Amora Do Thái"),
    ("068608", "amoras", "noun", "/əˈmɔːrəz/", "nhà hiền triết Do Thái thời Talmud"),
    ("068609", "anamneses", "noun", "/ˌænæmˈniːsiːz/", "tiền sử bệnh án; hồi ức tâm linh"),
    ("068610", "anaximanders", "noun", "/əˌnæksɪˈmændərz/", "triết gia Hy Lạp cổ Anaximander"),
    ("068611", "anchorites", "noun", "/ˈæŋkəˌraɪts/", "ẩn sĩ tu khổ hạnh xa lánh trần tục"),
    ("068612", "apicultures", "noun", "/ˈeɪpɪˌkʌltʃərz/", "nghề nuôi ong lấy mật và sáp"),
    ("068613", "archpriests", "noun", "/ˌɑːrtʃˈpriːsts/", "tổng linh mục trưởng giáo khu"),
    ("068614", "asclepiases", "noun", "/æˈskliːpiəsɪz/", "cây bông tai thuộc chi Asclepias"),
    ("068615", "atelectasises", "noun", "/ˌætəˈlɛktəsɪsɪz/", "chứng xẹp phổi thiếu không khí"),
    ("068616", "autobuses", "noun", "/ˈɔːtoʊˌbʌsɪz/", "xe ô tô buýt chở khách công cộng"),
    ("068617", "aventurines", "noun", "/əˈvɛntʃərɪnz/", "đá thạch anh lấp lánh aventurin"),
    ("068618", "azollas", "noun", "/əˈzɒləz/", "bèo hoa dâu cộng sinh cố định đạm"),
    ("068619", "bauhinias", "noun", "/bɔːˈhɪniəz/", "cây hoa ban móng bò chi Bauhinia"),
    ("068620", "blowier", "adj", "/ˈbloʊiər/", "lộng gió hơn; hay khoác lác hơn"),
    ("068621", "blowiest", "adj", "/ˈbloʊiɪst/", "lộng gió nhất; hay khoác lác nhất"),
    ("068622", "bulrushes", "noun", "/ˈbʊlˌrʌʃɪz/", "cây thủy trúc hương bồ đầm lầy"),
    ("068623", "canvassers", "noun", "/ˈkænvəsərz/", "người vận động bầu cử hoặc tiếp thị"),
    ("068624", "casques", "noun", "/kæsks/", "mũ giáp sắt cổ; mào sừng chim mỏ"),
    ("068625", "catamounts", "noun", "/ˈkætəˌmaʊnts/", "báo sư tử puma hoang dã Bắc Mỹ"),
    ("068626", "cetaceas", "noun", "/sɪˈteɪʃəz/", "bộ Cá voi gồm cá voi cá heo"),
    ("068627", "chlorises", "noun", "/ˈklɔːrɪsɪz/", "cỏ chân gà thuộc chi Chloris"),
    ("068628", "cholestasises", "noun", "/ˌkoʊlɪˈsteɪsɪsɪz/", "tình trạng ứ mật tắc dòng mật gan"),
    ("068629", "clavichords", "noun", "/ˈklævɪˌkɔːrdz/", "đàn phím cổ điển clavico châu Âu"),
    ("068630", "coalfaces", "noun", "/ˈkoʊlˌfeɪsɪz/", "gương lò nơi trực tiếp khai thác"),
    ("068631", "columbaria", "noun", "/ˌkɒləmˈbɛəriə/", "nhà lưu giữ tro cốt; chuồng bồ câu"),
    ("068632", "communicants", "noun", "/kəˈmjuːnɪkənts/", "tín hữu rước lễ Tiệc Thánh"),
    ("068633", "connoisseurships", "noun", "/ˌkɒnəˈsɜːrʃɪps/", "sự sành sỏi am hiểu nghệ thuật"),
    ("068634", "coria", "noun", "/ˈkɔːriə/", "lớp chân bì dày dưới biểu bì da"),
    ("068635", "coriums", "noun", "/ˈkɔːriəmz/", "lớp bì nâng đỡ mô biểu bì da"),
    ("068636", "cutes", "noun", "/ˈkjuːtiːz/", "lớp chân bì cutis (số nhiều ít gặp)"),
    ("068637", "cutides", "noun", "/ˈkjuːtɪdiːz/", "lớp chân bì của da (giải phẫu)"),
    ("068638", "denazifications", "noun", "/diːˌnɑːtsɪfɪˈkeɪʃənz/", "quá trình phi quốc xã hóa nước Đức"),
    ("068639", "disaccharides", "noun", "/daɪˈsækəˌraɪdz/", "đường đôi như đường mía đường sữa"),
    ("068640", "distributaries", "noun", "/dɪˈstrɪbjʊˌtɛriz/", "nhánh phân lưu đổ ra cửa sông"),
    ("068641", "diureses", "noun", "/ˌdaɪjʊˈriːsiːz/", "hiện tượng tăng bài tiết nước tiểu"),
    ("068642", "dixiecratses", "noun", "/ˈdɪksiˌkrætsɪz/", "đảng ly khai miền Nam Mỹ Dixiecrat"),
    ("068643", "doxepins", "noun", "/ˈdɒksɪpɪnz/", "thuốc chống trầm cảm doxepin"),
    ("068644", "dracaenas", "noun", "/drəˈsiːnəz/", "cây huyết dụ phát tài chi Dracaena"),
    ("068645", "epicureanisms", "noun", "/ˌɛpɪˈkjʊəriənˌɪzəmz/", "triết lý hưởng lạc Epicurus"),
    ("068646", "equiseta", "noun", "/ˌɛkwɪˈsiːtə/", "cây cỏ tháp bút không hoa"),
    ("068647", "equisetums", "noun", "/ˌɛkwɪˈsiːtəmz/", "cây mộc tặc cỏ tháp bút đốt rỗng"),
    ("068648", "eudaimonias", "noun", "/ˌjuːdaɪˈmoʊniəz/", "hạnh phúc an lạc viên mãn triết học"),
    ("068649", "falanges", "noun", "/fəˈlɑːŋxeɪz/", "phong trào chính trị Falange"),
    ("068650", "familiarisations", "noun", "/fəˌmɪliəraɪˈzeɪʃənz/", "quá trình làm quen tìm hiểu kỹ"),
    ("068651", "flatcars", "noun", "/ˈflætˌkɑːrz/", "toa xe lửa mặt phẳng chở hàng nặng"),
    ("068652", "flophouses", "noun", "/ˈflɒpˌhaʊzɪz/", "nhà trọ bình dân rẻ tiền tồi tàn"),
    ("068653", "gaiters", "noun", "/ˈɡeɪtərz/", "xà cạp bọc cổ chân; ống quàng cổ"),
    ("068654", "gaolers", "noun", "/ˈdʒeɪlərz/", "người cai ngục quản lý tù nhân"),
    ("068655", "gavages", "noun", "/ɡəˈvɑːʒɪz/", "cho ăn bằng ống thông dạ dày"),
    ("068656", "gomels", "noun", "/ˈɡɒməlz/", "thành phố Gomel miền đông Belarus"),
    ("068657", "granduncles", "noun", "/ˌɡrændˈʌŋkəlz/", "ông bác hoặc ông chú ruột"),
    ("068658", "greynesses", "noun", "/ˈɡreɪnəsɪz/", "sắc xám xịt ảm đạm buồn tẻ"),
    ("068659", "gunwales", "noun", "/ˈɡʌnəlz/", "mép mé trên dọc hai bên mạn thuyền"),
    ("068660", "hangnails", "noun", "/ˈhæŋˌneɪlz/", "mảnh da xước măng rô quanh móng tay"),
    ("068661", "hausens", "noun", "/ˈhaʊzənz/", "cá tầm khổng lồ beluga biển Caspi"),
    ("068662", "hickocks", "noun", "/ˈhɪkɒks/", "tay súng miền Tây Wild Bill Hickok"),
    ("068663", "historiographers", "noun", "/hɪˌstɒriˈɒɡrəfərz/", "nhà biên soạn sử liệu học"),
    ("068664", "hogbacks", "noun", "/ˈhɒɡˌbæks/", "sống núi hẹp dốc đứng hai sườn"),
    ("068665", "holidaymakers", "noun", "/ˈhɒlɪdeɪˌmeɪkərz/", "du khách đi nghỉ mát du lịch (Anh)"),
    ("068666", "illuminances", "noun", "/ɪˈluːmɪnənsɪz/", "độ rọi ánh sáng chiếu trên bề mặt"),
    ("068667", "inflexions", "noun", "/ɪnˈflɛkʃənz/", "sự biến tố ngữ pháp; ngữ điệu uốn"),
    ("068668", "isocrateses", "noun", "/aɪˈsɒkrətiːzɪz/", "nhà hùng biện Hy Lạp cổ Isocrates"),
    ("068669", "jackboots", "noun", "/ˈdʒækˌbuːts/", "ủng da quân sự cao quá đầu gối"),
    ("068670", "klystrons", "noun", "/ˈklaɪstrɒnz/", "đèn điện tử phát vi sóng klystron"),
    ("068671", "kyats", "noun", "/kiˈɑːts/", "đơn vị tiền tệ kyat của Myanmar"),
    ("068672", "lepases", "noun", "/ˈliːpəsɪz/", "chi con hà cổ ngỗng biển Lepas"),
    ("068673", "lycanthropes", "noun", "/ˈlaɪkənˌθroʊpz/", "người sói biến hình (truyền thuyết)"),
    ("068674", "maracas", "noun", "/məˈrɑːkəz/", "nhạc cụ gõ lắc hạt maraca Mỹ Latin"),
    ("068675", "micmacs", "noun", "/ˈmɪkmæks/", "người bản địa Mi'kmaq đông Canada"),
    ("068676", "mineralocorticoids", "noun", "/ˌmɪnərəloʊˈkɔːrtɪkɔɪdz/", "hoóc-môn vỏ thượng thận giữ muối"),
    ("068677", "molarities", "noun", "/moʊˈlærɪtiz/", "nồng độ mol trên lít dung dịch"),
    ("068678", "monosaccharides", "noun", "/ˌmɒnoʊˈsækəˌraɪdz/", "đường đơn giản nhất như glucozơ"),
    ("068679", "muntjacs", "noun", "/ˈmʌntdʒæks/", "hươu mang; con hoẵng rừng châu Á"),
    ("068680", "mytilenes", "noun", "/ˌmɪtɪˈliːniz/", "thành phố cảng Mytilene đảo Lesbos"),
    ("068681", "neckbands", "noun", "/ˈnɛkˌbændz/", "dải băng viền cổ áo sơ mi"),
    ("068682", "nephthyses", "noun", "/ˈnɛfθɪsɪz/", "nữ thần bảo hộ Nephthys Ai Cập"),
    ("068683", "neurobiologists", "noun", "/ˌnjʊəroʊbaɪˈɒlədʒɪsts/", "nhà sinh học thần kinh học"),
    ("068684", "noisemakers", "noun", "/ˈnɔɪzˌmeɪkərz/", "dụng cụ tạo tiếng ồn tiệc lễ hội"),
    ("068685", "ntides", "noun", "/ˌɛn tiː aɪ ˈdiːz/", "Viện Kỹ thuật Quốc gia NTID"),
    ("068686", "nubbier", "adj", "/ˈnʌbiər/", "sần sùi nhiều mấu nổi hơn"),
    ("068687", "nubbiest", "adj", "/ˈnʌbiɪst/", "sần sùi nhiều mấu nổi nhất"),
    ("068688", "orizabas", "noun", "/ˌɔːrɪˈzɑːbəz/", "núi lửa cao nhất Mexico Orizaba"),
    ("068689", "oropharynxes", "noun", "/ˌɔːroʊˈfærɪŋksɪz/", "vùng hầu miệng sau khoang miệng"),
    ("068690", "osteitises", "noun", "/ˌɒstiˈaɪtɪsɪz/", "tình trạng viêm nhiễm mô xương"),
    ("068691", "overfeeds", "verb", "/ˌoʊvərˈfiːdz/", "cho ăn quá mức cần thiết"),
    ("068692", "partitives", "noun", "/ˈpɑːrtɪtɪvz/", "từ chỉ một phần trích xuất bộ phận"),
    ("068693", "pastorales", "noun", "/ˌpæstəˈrɑːliz/", "nhạc khúc mục đồng đồng quê"),
    ("068694", "paterfamiliases", "noun", "/ˌpeɪtərfəˈmɪliəsɪz/", "người gia trưởng nam quyền La Mã cổ"),
    ("068695", "payslips", "noun", "/ˈpeɪˌslɪps/", "phiếu kê chi tiết tiền lương tháng"),
    ("068696", "phaethons", "noun", "/ˈfeɪəθɒnz/", "thần Phaethon; sao chổi Phaethon"),
    ("068697", "phenergans", "noun", "/ˈfɛnərˌɡænz/", "thuốc kháng histamin Phenergan"),
    ("068698", "pitocins", "noun", "/pɪˈtoʊsɪnz/", "thuốc giục sinh tổng hợp Pitocin"),
    ("068699", "plastrons", "noun", "/ˈplæstrɒnz/", "yếm bụng rùa; giáp ngực đấu kiếm"),
    ("068700", "plataeas", "noun", "/pləˈtiːəz/", "trận đánh Plataea năm 479 TCN"),
    ("068701", "podgier", "adj", "/ˈpɒdʒiər/", "mũm mĩm béo tròn lùn hơn (Anh)"),
    ("068702", "podgiest", "adj", "/ˈpɒdʒiɪst/", "mũm mĩm béo tròn lùn nhất (Anh)"),
]

with open("scratch/b34_r08_raw_p2.json") as f:
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

with open("scratch/b34_r08_p2.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r08_p2.json OK")
