import json

items = [
    ("071203", "prescripts", "noun", "/ˈpriːskrɪpts/", "quy tắc; sắc lệnh; toa thuốc (cổ)"),
    ("071204", "previsions", "noun", "/priːˈvɪʒənz/", "sự tiên liệu thấy trước tương lai"),
    ("071205", "prokaryotes", "noun", "/proʊˈkæriˌoʊts/", "sinh vật nhân sơ (vi khuẩn)"),
    ("071206", "protists", "noun", "/ˈproʊtɪsts/", "sinh vật nguyên sinh đơn bào"),
    ("071207", "roadmans", "noun", "/ˈroʊdmənz/", "công nhân bảo trì đường; tay đua xe"),
    ("071208", "rolaidses", "noun", "/ˈroʊleɪdzɪz/", "thuốc kháng axit dạ dày Rolaids"),
    ("071209", "salerooms", "noun", "/ˈseɪlˌruːmz/", "phòng bán đấu giá; phòng bán hàng"),
    ("071210", "secessionisms", "noun", "/sɪˈsɛʃəˌnɪzəmz/", "chủ nghĩa ly khai đòi tách riêng"),
    ("071211", "segni", "noun", "/ˈsɛnji/", "dấu hiệu lặp lại segno (âm nhạc)"),
    ("071212", "segnos", "noun", "/ˈsɛnjoʊz/", "dấu hiệu lặp lại segno (âm nhạc)"),
    ("071213", "sheepherders", "noun", "/ˈʃiːpˌhɜːrdərz/", "người chăn thả đàn cừu"),
    ("071214", "skeps", "noun", "/skɛps/", "tổ ong bện rơm; rổ đan lớn"),
    ("071215", "smackers", "noun", "/ˈsmækərz/", "đồng đô la (lóng Mỹ); nụ hôn chụt"),
    ("071216", "socinians", "noun", "/soʊˈsɪniənz/", "tín đồ giáo phái Socinus"),
    ("071217", "soubriquets", "noun", "/ˈsuːbrɪˌkeɪz/", "biệt danh, tên gọi thân mật"),
    ("071218", "sternocleidomastoids", "noun", "/ˌstɜːrnoʊklaɪdoʊˈmæstɔɪdz/", "cơ ức-đòn-chũm ở cổ"),
    ("071219", "synchromeshes", "noun", "/ˈsɪŋkroʊˌmɛʃɪz/", "hộp số đồng tốc (ô tô)"),
    ("071220", "taegus", "noun", "/ˈteɪɡuːz/", "thành phố Daegu ở Hàn Quốc"),
    ("071221", "tappas", "noun", "/ˈtɑːpəz/", "vải vỏ cây dâu tằm Polynesia"),
    ("071222", "tartlets", "noun", "/ˈtɑːrtləts/", "bánh tart nhân ngọt hoặc mặn nhỏ"),
    ("071223", "tetrameters", "noun", "/tɛˈtræmɪtərz/", "câu thơ bốn nhịp (tứ bộ vi)"),
    ("071224", "theurgies", "noun", "/ˈθiːɜːrdʒiz/", "phép màu thần linh; ma thuật trắng"),
    ("071225", "thuggees", "noun", "/θʌˈɡiːz/", "tổ chức cướp sát hại du khách Ấn"),
    ("071226", "timolols", "noun", "/ˈtɪməˌlɒlz/", "thuốc chẹn beta timolol (nhỏ mắt)"),
    ("071227", "titbits", "noun", "/ˈtɪtbɪts/", "món ngon nhỏ; tin đồn thú vị (Anh)"),
    ("071228", "tombaughs", "noun", "/ˈtɒmˌbɔːz/", "nhà thiên văn học Clyde Tombaugh"),
    ("071229", "totaras", "noun", "/ˈtoʊtərəz/", "cây gỗ totara bản địa New Zealand"),
    ("071230", "transalpines", "noun", "/trænzˈælpaɪnz/", "người vùng bên kia dãy núi Alps"),
    ("071231", "trigas", "noun", "/ˈtraɪɡəz/", "xe ba ngựa La Mã cổ; chi cá biển"),
    ("071232", "urgas", "noun", "/ˈʊərɡəz/", "Ulaanbaatar (tên cũ Urga)"),
    ("071233", "verticilliums", "noun", "/ˌvɜːrtɪˈsɪliəmz/", "nấm bệnh héo cây chi Verticillium"),
    ("071234", "victualled", "verb", "/ˈvɪtəld/", "đã tiếp tế lương thực thực phẩm"),
    ("071235", "vomers", "noun", "/ˈvoʊmərz/", "xương lá mía vách ngăn mũi"),
    ("071236", "windflowers", "noun", "/ˈwɪndˌflaʊərz/", "hoa phong quỳ (chi Anemone)"),
    ("071237", "xenophaneses", "noun", "/zɪˈnɒfəˌniːzɪz/", "triết gia Hy Lạp cổ Xenophanes"),
    ("071238", "achaeas", "noun", "/əˈkiːəz/", "vùng Achaea cổ đại Hy Lạp"),
    ("071239", "alveoluses", "noun", "/ælˈviːələsɪz/", "phế nang phổi; huyệt ổ chân răng"),
    ("071240", "amoxils", "noun", "/əˈmɒksɪlz/", "thuốc kháng sinh Amoxil"),
    ("071241", "anabaptisms", "noun", "/ˌænəˈbæptɪzəmz/", "phong trào Cải cách Tái Tẩy Lễ"),
    ("071242", "anthuriums", "noun", "/ænˈθjʊəriəmz/", "cây hoa hồng môn (chi Anthurium)"),
    ("071243", "aralias", "noun", "/əˈreɪliəz/", "cây đơn châu chấu thuộc chi Aralia"),
    ("071244", "arthrodeses", "noun", "/ˌɑːrθrəˈdiːsiːz/", "phẫu thuật hàn dính cố định khớp"),
    ("071245", "autobiographers", "noun", "/ˌɔːtoʊbaɪˈɒɡrəfərz/", "tác giả viết tự truyện đời mình"),
    ("071246", "avalokitesvaras", "noun", "/ˌɑːvəloʊkɪˈtɛʃvərəz/", "Quán Thế Âm Bồ Tát (Phật giáo)"),
    ("071247", "barded", "verb", "/ˈbɑːrdɪd/", "đã trang bị giáp ngựa; đã bọc mỡ"),
    ("071248", "bardes", "verb", "/bɑːrdz/", "mặc giáp cho ngựa; bọc thịt mỡ"),
    ("071249", "barding", "verb", "/ˈbɑːrdɪŋ/", "đang mặc giáp ngựa; đang bọc mỡ"),
    ("071250", "bolivianos", "noun", "/bəˌlɪviˈɑːnoʊz/", "đồng tiền boliviano của Bolivia"),
    ("071251", "brailed", "verb", "/breɪld/", "đã kéo thu cánh buồm; đánh lưới"),
    ("071252", "brailing", "verb", "/ˈbreɪlɪŋ/", "đang thu gọn cánh buồm; đánh lưới"),
    ("071253", "brails", "noun", "/breɪlz/", "dây thu cánh buồm; vợt xúc cá lớn"),
    ("071254", "cardamons", "noun", "/ˈkɑːrdəmənz/", "cây hoặc hạt thảo quả (biến thể)"),
    ("071255", "cardrooms", "noun", "/ˈkɑːrdˌruːmz/", "phòng chơi bài trong câu lạc bộ"),
    ("071256", "chiasmi", "noun", "/kaɪˈæzmaɪ/", "phép đối chéo vế từ (tu từ học)"),
    ("071257", "chiasmuses", "noun", "/kaɪˈæzməsɪz/", "phép đối chéo vế từ (tu từ học)"),
    ("071258", "chiropteras", "noun", "/kaɪˈrɒptərəz/", "bộ Dơi (động vật có vú biết bay)"),
    ("071259", "chrysomelidaes", "noun", "/ˌkrɪsəmɪˈliːdiːz/", "họ Bọ ánh kim ăn lá (cánh cứng)"),
    ("071260", "cigarillos", "noun", "/ˌsɪɡəˈrɪloʊz/", "điếu xì gà nhỏ cuốn lá thuốc"),
    ("071261", "cinnamomums", "noun", "/ˌsɪnəˈmoʊməmz/", "chi Quế và long não (Cinnamomum)"),
    ("071262", "cirsiums", "noun", "/ˈsɜːrsiəmz/", "cây kế đại kế thuộc chi Cirsium"),
    ("071263", "clons", "noun", "/klɒnz/", "dòng tế bào hay sinh vật vô tính"),
    ("071264", "coattails", "noun", "/ˈkoʊtˌteɪlz/", "vạt đuôi áo dài; dựa hơi người khác"),
    ("071265", "cockscombs", "noun", "/ˈkɒksˌkoʊmz/", "mào gà; hoa mào gà; mũ anh hề"),
    ("071266", "coconspirators", "noun", "/ˌkoʊkənˈspɪrətərz/", "đồng phạm cùng tham gia âm mưu"),
    ("071267", "cyanocobalamins", "noun", "/saɪˌænoʊkoʊˈbæləmɪnz/", "vitamin B12 tổng hợp"),
    ("071268", "duellists", "noun", "/ˈdjuːəlɪsts/", "người tham gia đấu tay đôi (Anh)"),
    ("071269", "dunderheads", "noun", "/ˈdʌndərˌhɛdz/", "kẻ đần độn ngốc nghếch chậm hiểu"),
    ("071270", "effectuations", "noun", "/ɪˌfɛktʃuˈeɪʃənz/", "sự thực hiện hoàn thành hiệu quả"),
    ("071271", "enescos", "noun", "/əˈnɛskoʊz/", "nhạc sĩ Romania George Enescu"),
    ("071272", "entrepots", "noun", "/ˈɒntrəˌpoʊz/", "cảng trung chuyển kho ngoại quan"),
    ("071273", "ephahs", "noun", "/ˈiːfɑːz/", "đơn vị đo dung tích Do Thái cổ"),
    ("071274", "epilations", "noun", "/ˌɛpɪˈleɪʃənz/", "sự nhổ tẩy triệt lông tận gốc"),
    ("071275", "extremums", "noun", "/ɪkˈstriːməmz/", "điểm cực trị cực đại cực tiểu"),
    ("071276", "farfalles", "noun", "/fɑːrˈfɑːleɪz/", "mì nơ Ý farfalle hình cánh bướm"),
    ("071277", "ferrocyanides", "noun", "/ˌfɛroʊˈsaɪənaɪdz/", "muối phức chất feroxyanua"),
    ("071278", "fosamaxes", "noun", "/ˈfɒsəmæksɪz/", "thuốc trị loãng xương Fosamax"),
    ("071279", "gavias", "noun", "/ˈɡeɪviəz/", "chim lặn phương bắc chi Gavia"),
    ("071280", "gesticulations", "noun", "/dʒɛˌstɪkjʊˈleɪʃənz/", "điệu bộ khoa tay múa chân"),
    ("071281", "giraudouxes", "noun", "/ˌʒɪərəˈduːz/", "nhà văn kịch Pháp Jean Giraudoux"),
    ("071282", "goldcrests", "noun", "/ˈɡoʊldˌkrɛsts/", "chim mào vàng nhỏ châu Âu"),
    ("071283", "griseofulvins", "noun", "/ˌɡrɪzioʊˈfʌlvɪnz/", "thuốc kháng nấm griseofulvin"),
    ("071284", "gunrunners", "noun", "/ˈɡʌnˌrʌnərz/", "kẻ buôn lậu vũ khí súng đạn"),
    ("071285", "harpooners", "noun", "/hɑːrˈpuːnərz/", "người phóng lao săn cá voi"),
    ("071286", "hellbenders", "noun", "/ˈhɛlˌbɛndərz/", "kỳ giông khổng lồ Bắc Mỹ"),
    ("071287", "homels", "noun", "/ˈhoʊməlz/", "thành phố Gomel (Homiel) Belarus"),
    ("071288", "homogenates", "noun", "/hoʊˈmɒdʒɪˌneɪts/", "hỗn hợp đồng hóa mô tế bào"),
    ("071289", "homozygosities", "noun", "/ˌhoʊmoʊzaɪˈɡɒsɪtiz/", "tính đồng hợp tử (di truyền học)"),
    ("071290", "hyperacuses", "noun", "/ˌhaɪpərˈækjuːsɪz/", "chứng tăng nhạy cảm âm thanh"),
    ("071291", "hyperglycaemias", "noun", "/ˌhaɪpərɡlaɪˈsiːmiəz/", "tình trạng tăng đường huyết (Anh)"),
    ("071292", "imbedded", "verb", "/ɪmˈbɛdɪd/", "đã nhúng gắn chìm chặt vào trong"),
    ("071293", "imbeds", "verb", "/ɪmˈbɛdz/", "nhúng gắn chìm chặt vào trong"),
    ("071294", "kinetochores", "noun", "/kɪˈnɛtəˌkɔːrz/", "thể động bám thoi phân bào"),
    ("071295", "kitakyushus", "noun", "/ˌkiːtɑːkiˈuːʃuːz/", "thành phố Kitakyushu ở Nhật Bản"),
    ("071296", "lablabs", "noun", "/ˈlæblæbz/", "cây đậu ván ăn quả (Lablab)"),
    ("071297", "langsides", "noun", "/ˈlæŋsaɪdz/", "trận Langside năm 1568 ở Scotland"),
    ("071298", "latkes", "noun", "/ˈlɑːtkəz/", "bánh khoai tây bào chiên giòn"),
    ("071299", "leiomyomas", "noun", "/ˌlaɪoʊmaɪˈoʊməz/", "u xơ cơ trơn lành tính (tử cung)"),
    ("071300", "litases", "noun", "/ˈliːtɑːsɪz/", "đồng tiền litas cũ của Litva"),
    ("071301", "litu", "noun", "/ˈliːtuː/", "đơn vị tiền tệ cũ của Litva"),
    ("071302", "luxations", "noun", "/lʌkˈseɪʃənz/", "chấn thương trật sai khớp (y học)"),
]

with open("scratch/b35_r03_raw_p3.json") as f:
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

with open("scratch/b35_r03_p3.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r03_p3.json OK")
