import json

items = [
    ("070803", "ghostwritten", "verb", "/ˈɡoʊstˌrɪtən/", "được viết thuê đứng tên (quá khứ)"),
    ("070804", "ghostwrote", "verb", "/ˈɡoʊstˌroʊt/", "đã viết thuê đứng tên người khác"),
    ("070805", "glyburides", "noun", "/ˈɡlaɪbjʊˌraɪdz/", "thuốc trị tiểu đường glyburide"),
    ("070806", "gnatcatchers", "noun", "/ˈnætˌkætʃərz/", "chim đớp muỗi gnatcatcher"),
    ("070807", "goldenseals", "noun", "/ˈɡoʊldənˌsiːlz/", "cây thảo dược goldenseal Bắc Mỹ"),
    ("070808", "gondis", "noun", "/ˈɡɒndiz/", "tiếng và người Gondi ở Ấn Độ"),
    ("070809", "greenshanks", "noun", "/ˈɡriːnˌʃæŋks/", "chim choắt chân xanh greenshank"),
    ("070810", "guenons", "noun", "/ɡəˈnɒnz/", "khỉ đuôi dài châu Phi guenon"),
    ("070811", "guttersnipes", "noun", "/ˈɡʌtərˌsnaɪps/", "trẻ bụi đời lang thang đường phố"),
    ("070812", "hammerlocks", "noun", "/ˈhæmərˌlɒks/", "đòn bẻ khóa tay ra sau lưng (vật)"),
    ("070813", "hartebeests", "noun", "/ˈhɑːrtɪˌbiːsts/", "linh dương sừng cong hartebeest"),
    ("070814", "hualapais", "noun", "/wɑːˈlɑːpaɪz/", "người bộ tộc Hualapai ở Arizona"),
    ("070815", "insurabilities", "noun", "/ɪnˌʃʊərəˈbɪlɪtiz/", "khả năng đủ điều kiện bảo hiểm"),
    ("070816", "isoproterenols", "noun", "/ˌaɪsoʊprəˈtɛrənɒlz/", "thuốc giãn phế quản isoproterenol"),
    ("070817", "jdams", "noun", "/ˈdʒeɪdæmz/", "bộ dẫn đường bom JDAM (Mỹ)"),
    ("070818", "keflexes", "noun", "/ˈkɛflɛksɪz/", "thuốc kháng sinh Keflex (Mỹ)"),
    ("070819", "kingbirds", "noun", "/ˈkɪŋˌbɜːrdz/", "chim bạo quân châu Mỹ kingbird"),
    ("070820", "larghettos", "noun", "/lɑːrˈɡɛtoʊz/", "đoạn nhạc tốc độ hơi chậm (nhạc)"),
    ("070821", "lindanes", "noun", "/ˈlɪndeɪnz/", "thuốc trừ sâu và trị ghẻ lindane"),
    ("070822", "luxurias", "noun", "/lʌkˈʃʊəriəz/", "thói dâm dục (bảy tội trọng)"),
    ("070823", "maghs", "noun", "/mɑːɡz/", "tháng Magh lịch Hindu (tháng 1–2)"),
    ("070824", "mantraps", "noun", "/ˈmænˌtræps/", "bẫy kẹp thú lớn đặt bắt kẻ trộm"),
    ("070825", "medawars", "noun", "/ˈmɛdəwɑːrz/", "nhà sinh học Nobel Peter Medawar"),
    ("070826", "mihrabs", "noun", "/ˈmiːrɑːbz/", "hốc tường mihrab hướng về Mecca"),
    ("070827", "millenaries", "noun", "/mɪˈlɛnəriz/", "lễ kỷ niệm một nghìn năm"),
    ("070828", "mirier", "adj", "/ˈmaɪriər/", "lầy lội bùn lầy hơn; sa lầy hơn"),
    ("070829", "miriest", "adj", "/ˈmaɪriɪst/", "lầy lội bùn lầy nhất; sa lầy nhất"),
    ("070830", "monodies", "noun", "/ˈmɒnədiz/", "khúc hát đơn ca ai oán; độc xướng"),
    ("070831", "monsteras", "noun", "/mɒnˈstɛrəz/", "cây trầu bà lá xẻ Monstera"),
    ("070832", "moonshiners", "noun", "/ˈmuːnˌʃaɪnərz/", "người nấu rượu lậu chui"),
    ("070833", "motmots", "noun", "/ˈmɒtˌmɒts/", "chim bói cá rừng motmot Nam Mỹ"),
    ("070834", "moulmeins", "noun", "/muːlˈmeɪnz/", "thành phố cảng Mawlamyine Myanmar"),
    ("070835", "mutilators", "noun", "/ˈmjuːtɪˌleɪtərz/", "kẻ làm biến dạng cắt xén tàn phá"),
    ("070836", "mygs", "noun", "/ˈmɪriəˌɡræmz/", "đơn vị khối lượng 10 kg (myg)"),
    ("070837", "newsbreaks", "noun", "/ˈnjuːzˌbreɪks/", "bản tin nhanh phát xen kẽ"),
    ("070838", "nitrofurantoins", "noun", "/ˌnaɪtroʊfjʊˈræntɔɪnz/", "thuốc kháng sinh nitrofurantoin"),
    ("070839", "oceanicas", "noun", "/ˌoʊʃiˈænɪkəz/", "khu vực châu Đại Dương (Oceanica)"),
    ("070840", "overbidding", "verb", "/ˌoʊvərˈbɪdɪŋ/", "đang trả giá quá cao hơn mức thực"),
    ("070841", "overbids", "noun", "/ˈoʊvərˌbɪdz/", "mức giá trả cao quá giá trị"),
    ("070842", "overgrowing", "verb", "/ˌoʊvərˈɡroʊɪŋ/", "đang mọc trùm lấn át xung quanh"),
    ("070843", "overgrows", "verb", "/ˌoʊvərˈɡroʊz/", "mọc trùm phủ kín xung quanh"),
    ("070844", "paleobotanies", "noun", "/ˌpeɪlioʊˈbɒtəniz/", "ngành cổ thực vật học"),
    ("070845", "paleogeographies", "noun", "/ˌpeɪlioʊdʒiˈɒɡrəfiz/", "ngành cổ địa lý học"),
    ("070846", "parapsychologists", "noun", "/ˌpærəsaɪˈkɒlədʒɪsts/", "nhà nghiên cứu cận tâm lý học"),
    ("070847", "parimutuels", "noun", "/ˌpærɪˈmjuːtʃuəlz/", "hình thức cá cược chia tiền tổng"),
    ("070848", "pennisetums", "noun", "/ˌpɛnɪˈsiːtəmz/", "cây cỏ voi cỏ kê chi Pennisetum"),
    ("070849", "pensionaries", "noun", "/ˈpɛnʃənɛriz/", "người hưởng trợ cấp; quan Hà Lan cũ"),
    ("070850", "phrenologists", "noun", "/frɪˈnɒlədʒɪsts/", "người theo thuyết xem tướng sọ não"),
    ("070851", "piezoelectricities", "noun", "/piˌeɪzoʊɪlɛkˈtrɪsɪtiz/", "hiện tượng áp điện (vật lý)"),
    ("070852", "piluses", "noun", "/ˈpaɪləsɪz/", "lông nhung vi khuẩn; sợi lông"),
    ("070853", "pimientos", "noun", "/pɪˈmjɛntoʊz/", "ớt ngọt đỏ Tây Ban Nha pimiento"),
    ("070854", "pogges", "noun", "/pɒɡz/", "cá bọ cạp biển giáp (pogge)"),
    ("070855", "polymyxins", "noun", "/ˌpɒlɪˈmɪksɪnz/", "kháng sinh polymyxin trị vi khuẩn"),
    ("070856", "praesidiums", "noun", "/prɪˈsɪdiəmz/", "đoàn chủ tịch thường trực (Liên Xô)"),
    ("070857", "preussens", "noun", "/ˈprɔɪsənz/", "xứ Phổ lịch sử ở Đức (Preußen)"),
    ("070858", "proctologies", "noun", "/prɒkˈtɒlədʒiz/", "chuyên khoa hậu môn trực tràng"),
    ("070859", "propenes", "noun", "/ˈproʊpiːnz/", "khí propylen / propen (C3H6)"),
    ("070860", "pullets", "noun", "/ˈpʊlɪts/", "gà mái tơ non dưới một năm tuổi"),
    ("070861", "pyrexias", "noun", "/paɪˈrɛksiəz/", "tình trạng sốt cao (thuật ngữ y)"),
    ("070862", "radiotelegraphs", "noun", "/ˌreɪdioʊˈtɛlɪˌɡræfs/", "máy điện báo truyền tin vô tuyến"),
    ("070863", "reatas", "noun", "/riˈɑːtəz/", "dây thòng lọng bện da bắt gia súc"),
    ("070864", "requiescats", "noun", "/ˌrɛkwiˈɛskæts/", "lời cầu chúc an nghỉ cho người mất"),
    ("070865", "resorcinols", "noun", "/rɪˈzɔːrsɪˌnɒlz/", "hợp chất sát trùng da resorcinol"),
    ("070866", "roundelays", "noun", "/ˈraʊndəˌleɪz/", "bài ca ngắn có điệp khúc lặp lại"),
    ("070867", "rushier", "adj", "/ˈrʌʃiər/", "nhiều cói lác hơn; mọc đầy cỏ lác"),
    ("070868", "rushiest", "adj", "/ˈrʌʃiɪst/", "nhiều cói lác nhất; đầy cỏ lác nhất"),
    ("070869", "sarpedons", "noun", "/sɑːrˈpiːdənz/", "anh hùng Sarpedon thần thoại Hy Lạp"),
    ("070870", "schoolfriends", "noun", "/ˈskuːlˌfrɛndz/", "bạn học cùng trường thời đi học"),
    ("070871", "schoolmarms", "noun", "/ˈskuːlˌmɑːrmz/", "cô giáo nghiêm khắc kiểu cũ (Mỹ)"),
    ("070872", "scissions", "noun", "/ˈsɪʒənz/", "sự chia rẽ phân tách; sự cắt đứt"),
    ("070873", "scragging", "verb", "/ˈskræɡɪŋ/", "đang bóp cổ xiết cổ; xử lý thô bạo"),
    ("070874", "scrags", "noun", "/skræɡz/", "người gầy trơ xương; miếng thịt gân"),
    ("070875", "shahadahs", "noun", "/ʃəˈhɑːdəz/", "lời tuyên tín Shahada Hồi giáo"),
    ("070876", "slangier", "adj", "/ˈslæŋiər/", "nhiều tiếng lóng bình dân hơn"),
    ("070877", "slangiest", "adj", "/ˈslæŋiɪst/", "nhiều tiếng lóng bình dân nhất"),
    ("070878", "solfeggi", "noun", "/sɒlˈfɛdʒi/", "bài tập thanh nhạc xướng âm"),
    ("070879", "solfeggios", "noun", "/sɒlˈfɛdʒioʊz/", "bài tập thanh nhạc xướng âm"),
    ("070880", "spallanzanis", "noun", "/ˌspɑːlɑːnˈtsɑːniz/", "nhà sinh học Ý Lazzaro Spallanzani"),
    ("070881", "sunbathers", "noun", "/ˈsʌnˌbeɪðərz/", "người đang phơi mình tắm nắng"),
    ("070882", "tetherballs", "noun", "/ˈtɛðərˌbɔːlz/", "trò bóng cột dây đánh quanh trụ"),
    ("070883", "tinners", "noun", "/ˈtɪnərz/", "thợ mỏ thiếc; thợ đóng đồ hộp thiếc"),
    ("070884", "totalisators", "noun", "/ˈtoʊtəˌlaɪzətərz/", "hệ thống máy tính tiền cá cược"),
    ("070885", "tractarians", "noun", "/trækˈtɛəriənz/", "tín đồ phong trào Anh giáo Oxford"),
    ("070886", "turnstones", "noun", "/ˈtɜːrnˌstoʊnz/", "chim dẽ khoang chuyên lật sỏi đá"),
    ("070887", "valmies", "noun", "/ˈvælmiz/", "trận chiến Valmy năm 1792 ở Pháp"),
    ("070888", "varicoceles", "noun", "/ˈværɪkoʊˌsiːlz/", "chứng giãn tĩnh mạch thừng tinh"),
    ("070889", "vermes", "noun", "/ˈvɜːrmiːz/", "thùy nhộng tiểu não; các loài giun"),
    ("070890", "vermises", "noun", "/ˈvɜːrmɪsɪz/", "thùy nhộng tiểu não"),
    ("070891", "xerodermas", "noun", "/ˌzɪərəˈdɜːrməz/", "bệnh khô da nứt nẻ (y học)"),
    ("070892", "zarqas", "noun", "/ˈzɑːrkəz/", "thành phố Zarqa ở Jordan"),
    ("070893", "adalias", "noun", "/əˈdeɪliəz/", "cảng Antalya cổ (Adalia)"),
    ("070894", "agranulocytoses", "noun", "/eɪˌɡrænjʊloʊsaɪˈtoʊsiːz/", "chứng giảm nặng bạch cầu hạt"),
    ("070895", "anolises", "noun", "/əˈnoʊlɪsɪz/", "thằn lằn anolis đổi màu châu Mỹ"),
    ("070896", "basophils", "noun", "/ˈbeɪsəˌfɪlz/", "bạch cầu ái kiềm trong máu"),
    ("070897", "bermudans", "noun", "/bɜːrˈmjuːdənz/", "người dân quần đảo Bermuda"),
    ("070898", "biochips", "noun", "/ˈbaɪoʊˌtʃɪps/", "vi mạch sinh học phân tích gen"),
    ("070899", "bitartrates", "noun", "/baɪˈtɑːrtreɪts/", "muối bitartrat (axit tartaric)"),
    ("070900", "bloaters", "noun", "/ˈbloʊtərz/", "cá trích muối hun khói nguyên con"),
    ("070901", "bromated", "verb", "/ˈbroʊmeɪtɪd/", "đã xử lý phản ứng bằng brom"),
    ("070902", "bromates", "verb", "/ˈbroʊmeɪts/", "xử lý hoặc kết hợp với brom"),
]

with open("scratch/b35_r02_raw_p4.json") as f:
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

with open("scratch/b35_r02_p4.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r02_p4.json OK")
