import json

items = [
    ("072003", "baronages", "noun", "/ˈbærənɪdʒɪz/", "giới nam tước; tước vị nam tước"),
    ("072004", "berlages", "noun", "/ˈbɛərlɑːɡəz/", "kiến trúc sư Hendrik Berlage"),
    ("072005", "bimetals", "noun", "/baɪˈmɛtəlz/", "vật liệu lưỡng kim ghép hai lớp"),
    ("072006", "birettas", "noun", "/bɪˈrɛtəz/", "mũ vuông chóp giáo sĩ Công giáo"),
    ("072007", "boskier", "adj", "/ˈbɒskiər/", "rậm rạp cây bụi hơn (văn chương)"),
    ("072008", "boskiest", "adj", "/ˈbɒskiɪst/", "rậm rạp cây bụi nhất (văn chương)"),
    ("072009", "brynhilds", "noun", "/ˈbrɪnhɪldz/", "nữ chiến binh Valkyrie Brynhild"),
    ("072010", "buffleheads", "noun", "/ˈbʌfəlˌhɛdz/", "vịt lặn đầu xù nhỏ Bắc Mỹ"),
    ("072011", "cardiograms", "noun", "/ˈkɑːrdiəˌɡræmz/", "điện tâm đồ ghi nhịp tim"),
    ("072012", "catalogers", "noun", "/ˈkætəˌlɒɡərz/", "nhân viên biên mục thư viện (Mỹ)"),
    ("072013", "cedruses", "noun", "/ˈsiːdrəsɪz/", "chi Cây tuyết tùng thật sự Cedrus"),
    ("072014", "charabancs", "noun", "/ˈʃærəˌbæŋks/", "xe ngựa hoặc xe buýt mở mui xưa"),
    ("072015", "childbeds", "noun", "/ˈtʃaɪldˌbɛdz/", "thời kỳ sinh đẻ; giường sinh con"),
    ("072016", "codefendants", "noun", "/ˌkoʊdɪˈfɛndənts/", "người đồng bị cáo trong vụ án"),
    ("072017", "corespondents", "noun", "/ˌkoʊrɪˈspɒndənts/", "người bị kiện đồng phạm ly hôn"),
    ("072018", "corncrakes", "noun", "/ˈkɔːrnˌkreɪks/", "chim gà nước đồng cỏ corncrake"),
    ("072019", "cosseted", "verb", "/ˈkɒsɪtɪd/", "đã chiều chuộng nâng niu quá mức"),
    ("072020", "cosseting", "verb", "/ˈkɒsɪtɪŋ/", "đang chiều chuộng nâng niu quá mức"),
    ("072021", "cushitics", "noun", "/kʊˈʃɪtɪks/", "nhóm ngôn ngữ Cushitic Đông Phi"),
    ("072022", "cyders", "noun", "/ˈsaɪdərz/", "rượu táo lên men (cách viết cũ)"),
    ("072023", "cymrics", "noun", "/ˈkɪmrɪks/", "tiếng xứ Wales (ngôn ngữ Celt)"),
    ("072024", "darners", "noun", "/ˈdɑːrnərz/", "người mạng vá quần áo; kim mạng"),
    ("072025", "decertified", "verb", "/diːˈsɜːrtɪˌfaɪd/", "đã hủy bỏ chứng nhận công nhận"),
    ("072026", "decertifies", "verb", "/diːˈsɜːrtɪˌfaɪz/", "hủy bỏ chứng nhận hợp lệ"),
    ("072027", "decertifying", "verb", "/diːˈsɜːrtɪˌfaɪɪŋ/", "đang hủy bỏ chứng nhận hợp lệ"),
    ("072028", "donars", "noun", "/ˈdoʊnɑːrz/", "thần sấm Donar (Thor tiếng Đức)"),
    ("072029", "drolleries", "noun", "/ˈdroʊləriz/", "trò khôi hài dí dỏm kỳ cục"),
    ("072030", "elvers", "noun", "/ˈɛlvərz/", "cá chình con non bơi ngược dòng"),
    ("072031", "excessivenesses", "noun", "/ɪkˈsɛsɪvnəsɪz/", "tính chất thái quá quá mức"),
    ("072032", "eyeshots", "noun", "/ˈaɪˌʃɒts/", "tầm nhìn xa của mắt (tầm mắt)"),
    ("072033", "ezechiels", "noun", "/ɪˈziːkiəlz/", "nhà tiên tri Ezekiel (biến thể)"),
    ("072034", "forams", "noun", "/ˈfɔːræmz/", "trùng lỗ vi sinh vật vỏ đá vôi"),
    ("072035", "gemboks", "noun", "/ˈɡɛmbɒks/", "linh dương sừng thẳng Nam Phi"),
    ("072036", "gemsboks", "noun", "/ˈɡɛmzˌbɒks/", "linh dương sừng kiếm Nam Phi"),
    ("072037", "genuflections", "noun", "/ˌdʒɛnjʊˈflɛkʃənz/", "động tác quỳ một gối tôn kính"),
    ("072038", "greybacks", "noun", "/ˈɡreɪˌbæks/", "lính Liên minh miền Nam Mỹ (cũ)"),
    ("072039", "gunstocks", "noun", "/ˈɡʌnˌstɒks/", "báng súng gỗ nâng đỡ nòng súng"),
    ("072040", "hamelns", "noun", "/ˈhɑːməlnz/", "thành phố Hamelin (Hamelns) ở Đức"),
    ("072041", "hemins", "noun", "/ˈhiːmɪnz/", "tinh thể hemin có trong máu"),
    ("072042", "hominidaes", "noun", "/hɒˈmɪnɪˌdiːz/", "họ Người (người và vượn lớn)"),
    ("072043", "hostlers", "noun", "/ˈɒslərz/", "người trông giữ ngựa tại quán trọ"),
    ("072044", "hubels", "noun", "/ˈhjuːbəlz/", "nhà thần kinh học David H. Hubel"),
    ("072045", "hydrolysed", "verb", "/ˈhaɪdrəˌlaɪzd/", "đã thủy phân bằng nước (Anh)"),
    ("072046", "hydrolyses", "verb", "/ˈhaɪdrəˌlaɪzɪz/", "thủy phân tách liên kết bằng nước"),
    ("072047", "hydrolysing", "verb", "/ˈhaɪdrəˌlaɪzɪŋ/", "đang thủy phân bằng nước (Anh)"),
    ("072048", "hyperbilirubinemias", "noun", "/ˌhaɪpərbɪlɪˌruːbɪˈniːmiəz/", "chứng tăng bilirubin trong máu"),
    ("072049", "hypercapnias", "noun", "/ˌhaɪpərˈkæpniəz/", "tình trạng tăng CO2 trong máu"),
    ("072050", "hypochondriases", "noun", "/ˌhaɪpoʊkɒnˈdraɪəsiːz/", "chứng nghi bệnh lo âu sức khỏe"),
    ("072051", "hypoparathyroidisms", "noun", "/ˌhaɪpoʊpærəˈθaɪrɔɪˌdɪzəmz/", "bệnh suy tuyến cận giáp (y học)"),
    ("072052", "inkles", "noun", "/ˈɪŋkəlz/", "dải ruy-băng dây vải lanh dệt hẹp"),
    ("072053", "intriguers", "noun", "/ɪnˈtriːɡərz/", "kẻ bày mưu tính kế ngầm"),
    ("072054", "klothos", "noun", "/ˈkloʊθoʊz/", "nữ thần định mệnh Clotho Hy Lạp"),
    ("072055", "krotos", "noun", "/ˈkroʊtoʊz/", "nhà hóa học Nobel Harold Kroto"),
    ("072056", "kwashiorkors", "noun", "/ˌkwɑːʃiˈɔːrkɔːrz/", "bệnh suy dinh dưỡng thiếu đạm phù"),
    ("072057", "lespedezas", "noun", "/ˌlɛspɪˈdiːzəz/", "cây đậu bụi cỏ ba lá Lespedeza"),
    ("072058", "litorals", "noun", "/ˈlɪtərəlz/", "vùng ven biển ven bờ (biến thể)"),
    ("072059", "llyrs", "noun", "/ˈlɪərz/", "thần biển Llyr xứ Wales cổ"),
    ("072060", "lucilias", "noun", "/luːˈsɪliəz/", "chi Ruồi nhặng xanh (Lucilia)"),
    ("072061", "malpighis", "noun", "/mɑːlˈpiːɡiz/", "nhà giải phẫu Ý Marcello Malpighi"),
    ("072062", "mediatrixes", "noun", "/ˌmiːdiˈeɪtrɪksɪz/", "nữ trung gian hòa giải mâu thuẫn"),
    ("072063", "megahits", "noun", "/ˈmɛɡəˌhɪts/", "tác phẩm thành công vang dội lớn"),
    ("072064", "megatheria", "noun", "/ˌmɛɡəˈθɪəriə/", "con lười đất khổng lồ tiền sử"),
    ("072065", "meniscectomies", "noun", "/ˌmɛnɪˈsɛktəmiz/", "phẫu thuật cắt sụn chêm khớp gối"),
    ("072066", "microtomes", "noun", "/ˈmaɪkrəˌtoʊmz/", "máy cắt lát siêu mỏng làm tiêu bản"),
    ("072067", "minibikes", "noun", "/ˈmɪniˌbaɪks/", "xe mô tô hai bánh cỡ nhỏ mini"),
    ("072068", "mohammedanisms", "noun", "/moʊˈhæmədəˌnɪzəmz/", "đạo Hồi (tên gọi cũ phương Tây)"),
    ("072069", "montanans", "noun", "/mɒnˈtænənz/", "người dân bang Montana của Mỹ"),
    ("072070", "mucoids", "noun", "/ˈmjuːkɔɪdz/", "chất nhầy mucoid giống dịch nhầy"),
    ("072071", "muscaris", "noun", "/mjʊˈskɛəriz/", "hoa lục bình nho chi Muscari"),
    ("072072", "naiases", "noun", "/ˈnaɪəsɪz/", "chi Rong mái chèo thủy sinh Najas"),
    ("072073", "nazifications", "noun", "/ˌnɑːtsɪfɪˈkeɪʃənz/", "quá trình Đức Quốc xã hóa chế độ"),
    ("072074", "necrolyses", "noun", "/nɛˈkrɒlɪˌsiːz/", "hiện tượng hoại tử bong tách mô"),
    ("072075", "nejds", "noun", "/nɛdʒdz/", "vùng cao nguyên Najd ở Ả Rập"),
    ("072076", "nocturias", "noun", "/nɒkˈtjʊəriəz/", "chứng tiểu đêm nhiều lần"),
    ("072077", "octrois", "noun", "/ɒkˈtrwɑːz/", "thuế cửa thành đánh vào hàng hóa"),
    ("072078", "odontoglossums", "noun", "/oʊˌdɒntoʊˈɡlɒsəmz/", "lan kiếm răng cưa Odontoglossum"),
    ("072079", "ophthalmias", "noun", "/ɒfˈθælmiəz/", "bệnh viêm mắt nặng (y học)"),
    ("072080", "peipings", "noun", "/ˈpeɪpɪŋz/", "Bắc Bình (tên cũ của Bắc Kinh)"),
    ("072081", "personations", "noun", "/ˌpɜːrsəˈneɪʃənz/", "sự đóng giả mạo danh; sự thể hiện"),
    ("072082", "pinnipeds", "noun", "/ˈpɪnɪˌpɛdz/", "động vật chân màng (hải cẩu, moóc)"),
    ("072083", "plasmacytomas", "noun", "/ˌplæzməsaɪˈtoʊməz/", "khối u tương bào ác tính (y học)"),
    ("072084", "potholders", "noun", "/ˈpɒtˌhoʊldərz/", "miếng vải lót tay nhấc nồi nóng"),
    ("072085", "protamines", "noun", "/ˈproʊtəmiːnz/", "protein kiềm đơn giản protamine"),
    ("072086", "rebinds", "verb", "/ˌriːˈbaɪndz/", "đóng lại gáy sách; buộc trói lại"),
    ("072087", "recitalists", "noun", "/rɪˈsaɪtəlɪsts/", "nghệ sĩ biểu diễn độc tấu nhạc"),
    ("072088", "religionists", "noun", "/rɪˈlɪdʒənɪsts/", "người sùng đạo hoặc cuồng tín"),
    ("072089", "rhizophoras", "noun", "/raɪˈzɒfərəz/", "cây đước rừng ngập mặn Rhizophora"),
    ("072090", "roomers", "noun", "/ˈruːmərz/", "người thuê phòng trọ ở riêng (Mỹ)"),
    ("072091", "saceurs", "noun", "/sæˈkjʊərz/", "Tư lệnh tối cao Đồng minh châu Âu"),
    ("072092", "serpenses", "noun", "/ˈsɜːrpɛnzɪz/", "chòm sao Cự Xà trên bầu trời"),
    ("072093", "sheeshas", "noun", "/ˈʃiːʃəz/", "bình hút thuốc shisha Trung Đông"),
    ("072094", "shirttails", "noun", "/ˈʃɜːrtˌteɪlz/", "vạt dưới đuôi áo sơ mi; tin phụ"),
    ("072095", "shunters", "noun", "/ˈʃʌntərz/", "đầu máy dồn toa; người đẩy ga (Anh)"),
    ("072096", "sideslipped", "verb", "/ˈsaɪdˌslɪpt/", "đã trượt ngang cánh sang bên"),
    ("072097", "sideslipping", "verb", "/ˈsaɪdˌslɪpɪŋ/", "đang trượt ngang sang bên"),
    ("072098", "sideslips", "noun", "/ˈsaɪdˌslɪps/", "cú trượt ngang (máy bay); trượt bên"),
    ("072099", "snorters", "noun", "/ˈsnɔːrtərz/", "người khịt mũi khinh bỉ; chuyện lớn"),
    ("072100", "subjectivists", "noun", "/səbˈdʒɛktɪvɪsts/", "người theo thuyết chủ quan luận"),
    ("072101", "surcoats", "noun", "/ˈsɜːrˌkoʊts/", "áo choàng ngoài mặc trùm áo giáp"),
    ("072102", "syndactylies", "noun", "/sɪnˈdæktɪliz/", "tật dính liền các ngón tay chân"),
]

with open("scratch/b35_r05_raw_p1.json") as f:
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

with open("scratch/b35_r05_p1.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r05_p1.json OK")
