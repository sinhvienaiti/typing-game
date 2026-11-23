import json

items = [
    ("071903", "epilobiums", "noun", "/ˌɛpɪˈloʊbiəmz/", "cây liễu thảo chi Epilobium"),
    ("071904", "ereshkigals", "noun", "/ɛˌrɛʃkɪˈɡɑːlz/", "nữ thần âm phủ Ereshkigal"),
    ("071905", "erinyeses", "noun", "/ɪˈrɪniˌiːzɪz/", "nữ thần báo thù Erinyes Hy Lạp"),
    ("071906", "eumenideses", "noun", "/juːˈmɛnɪˌdiːzɪz/", "nữ thần nhân từ Eumenides Hy Lạp"),
    ("071907", "exfiltrated", "verb", "/ˈɛksfɪlˌtreɪtɪd/", "đã rút quân bí mật; rò rỉ dữ liệu"),
    ("071908", "exfiltrates", "verb", "/ˈɛksfɪlˌtreɪts/", "rút bí mật khỏi vùng địch; tuồn tin"),
    ("071909", "exfiltrating", "verb", "/ˈɛksfɪlˌtreɪtɪŋ/", "đang rút bí mật; đang tuồn dữ liệu"),
    ("071910", "fishwives", "noun", "/ˈfɪʃˌwaɪvz/", "bà bán cá chợ; bà chửi bới đanh đá"),
    ("071911", "flaminiuses", "noun", "/fləˈmɪniəsɪz/", "tướng La Mã Gaius Flaminius"),
    ("071912", "gateposts", "noun", "/ˈɡeɪtˌpoʊsts/", "trụ cột hai bên cổng ra vào"),
    ("071913", "gigues", "noun", "/ʒiːɡz/", "điệu nhảy gigue vui nhộn cổ điển"),
    ("071914", "glumes", "noun", "/ɡluːmz/", "vỏ mày bọc bông lúa hòa thảo"),
    ("071915", "googolplexes", "noun", "/ˈɡuːɡɒlˌplɛksɪz/", "số cực lớn googolplex (10^googol)"),
    ("071916", "goujons", "noun", "/ˈɡuːʒɒnz/", "cá bống trắng; thanh chốt lắp ráp"),
    ("071917", "guerdons", "noun", "/ˈɡɜːrdənz/", "phần thưởng xứng đáng (văn chương)"),
    ("071918", "habitudes", "noun", "/ˈhæbɪˌtjuːdz/", "thói quen cố hữu; nếp sinh hoạt"),
    ("071919", "hamamelises", "noun", "/ˌhæməˈmiːlɪsɪz/", "cây phỉ Mỹ (witch hazel Hamamelis)"),
    ("071920", "handwheels", "noun", "/ˈhændˌwiːlz/", "tay vặn hình bánh xe điều chỉnh"),
    ("071921", "hemerocallises", "noun", "/ˌhɛməroʊˈkælɪsɪz/", "hoa hiên (hoa huyên) Hemerocallis"),
    ("071922", "horizontalities", "noun", "/ˌhɒrɪzɒnˈtælɪtiz/", "tính nằm ngang theo phương ngang"),
    ("071923", "hydrozoas", "noun", "/ˌhaɪdrəˈzoʊəz/", "lớp Thủy tức ngành Ruột khoang"),
    ("071924", "imurans", "noun", "/ɪmˈjʊərənz/", "thuốc ức chế miễn dịch Imuran"),
    ("071925", "jewisons", "noun", "/ˈdʒuːɪsənz/", "đạo diễn Canada Norman Jewison"),
    ("071926", "ketorolacs", "noun", "/ˌkiːtoʊˈroʊlæks/", "thuốc giảm đau ketorolac"),
    ("071927", "lemnas", "noun", "/ˈlɛmnəz/", "cây bèo tấm nổi mặt nước (Lemna)"),
    ("071928", "luxembourgers", "noun", "/ˈlʌksəmˌbɜːrɡərz/", "người dân Công quốc Luxembourg"),
    ("071929", "maghas", "noun", "/ˈmɑːɡəz/", "tháng Magha lịch Ấn Độ giáo"),
    ("071930", "malapropisms", "noun", "/ˈmæləprɒˌpɪzəmz/", "lỗi dùng nhầm từ phát âm gần nhau"),
    ("071931", "manubria", "noun", "/məˈnjuːbriə/", "cán xương ức; cán xương búa tai"),
    ("071932", "manubriums", "noun", "/məˈnjuːbriəmz/", "cán xương ức; cán xương búa tai"),
    ("071933", "meclizines", "noun", "/ˈmɛklɪˌziːnz/", "thuốc chống say tàu xe meclizine"),
    ("071934", "mentations", "noun", "/mɛnˈteɪʃənz/", "hoạt động tâm trí tư duy ý thức"),
    ("071935", "meperidines", "noun", "/məˈpɛrɪdiːnz/", "thuốc giảm đau gây nghiện pethidin"),
    ("071936", "moneybags", "noun", "/ˈmʌniˌbæɡz/", "người giàu có lắm tiền; túi tiền"),
    ("071937", "morceaus", "noun", "/mɔːrˈsoʊz/", "đoạn nhạc ngắn; tiểu phẩm (Pháp)"),
    ("071938", "morceaux", "noun", "/mɔːrˈsoʊ/", "đoạn nhạc ngắn; trích đoạn văn"),
    ("071939", "myses", "noun", "/ˈmaɪsiːz/", "chi Tép biển nhỏ Mysis"),
    ("071940", "nevelsons", "noun", "/ˈnɛvəlsənz/", "nhà điêu khắc Mỹ Louise Nevelson"),
    ("071941", "numerologists", "noun", "/ˌnjuːməˈrɒlədʒɪsts/", "nhà thần số học nghiên cứu con số"),
    ("071942", "oesterreiches", "noun", "/ˈɜːstəˌraɪks/", "nước Cộng hòa Áo (tiếng Đức)"),
    ("071943", "oxonians", "noun", "/ɒkˈsoʊniənz/", "người hoặc sinh viên Đại học Oxford"),
    ("071944", "oxytetracyclines", "noun", "/ˌɒksɪtɛtrəˈsaɪkliːnz/", "thuốc kháng sinh oxytetracycline"),
    ("071945", "pentaerythritols", "noun", "/ˌpɛntəɛˈrɪθrɪtɒlz/", "hợp chất rượu bốn chức hóa học"),
    ("071946", "philistias", "noun", "/fɪˈlɪstiəz/", "vùng đất cổ Philistia bờ Canaan"),
    ("071947", "phytologists", "noun", "/faɪˈtɒlədʒɪsts/", "nhà thực vật học (thuật ngữ cũ)"),
    ("071948", "pitheads", "noun", "/ˈpɪtˌhɛdz/", "miệng giếng vào hầm mỏ than"),
    ("071949", "radiolarians", "noun", "/ˌreɪdioʊˈlɛəriənz/", "trùng tia sinh vật đơn bào biển"),
    ("071950", "ranunculaceaes", "noun", "/rəˌnʌŋkjʊˈleɪʃiˌiːz/", "họ Mao lương thực vật"),
    ("071951", "realgars", "noun", "/riˈælɡɑːrz/", "khoáng vật đá thạch hoàng realga"),
    ("071952", "rhumbs", "noun", "/rʌmz/", "hướng phương vị la bàn (hàng hải)"),
    ("071953", "roadworthinesses", "noun", "/ˈroʊdˌwɜːrðinəsɪz/", "tình trạng đủ an toàn lưu hành xe"),
    ("071954", "runtier", "adj", "/ˈrʌntiər/", "còi cọc nhỏ thó bé hơn"),
    ("071955", "runtiest", "adj", "/ˈrʌntiɪst/", "còi cọc nhỏ thó bé nhất"),
    ("071956", "sandflies", "noun", "/ˈsændˌflaɪz/", "ruồi cát hút máu truyền bệnh"),
    ("071957", "schussed", "verb", "/ʃʊst/", "đã trượt tuyết lao thẳng xuống dốc"),
    ("071958", "schusses", "verb", "/ˈʃʊsɪz/", "trượt tuyết lao thẳng xuống dốc"),
    ("071959", "schussing", "verb", "/ˈʃʊsɪŋ/", "đang trượt tuyết lao thẳng dốc"),
    ("071960", "seigniories", "noun", "/ˈseɪnjəriz/", "lãnh địa và quyền lực lãnh chúa"),
    ("071961", "shrinkwraped", "verb", "/ˈʃrɪŋkˌræpt/", "đã bọc kín bằng màng co nhiệt"),
    ("071962", "shrinkwraping", "verb", "/ˈʃrɪŋkˌræpɪŋ/", "đang bọc kín bằng màng co nhiệt"),
    ("071963", "shrinkwraps", "verb", "/ˈʃrɪŋkˌræps/", "bọc kín sản phẩm bằng màng co nhiệt"),
    ("071964", "signalers", "noun", "/ˈsɪɡnələrz/", "người phát tín hiệu báo hiệu (Mỹ)"),
    ("071965", "slivovitzes", "noun", "/ˈslɪvəˌvɪtsɪz/", "rượu mạnh chưng từ mận Đông Âu"),
    ("071966", "socinuses", "noun", "/soʊˈsaɪnəsɪz/", "nhà thần học Ý Fausto Sozzini"),
    ("071967", "spirogyras", "noun", "/ˌspaɪrəˈdʒaɪrəz/", "tảo xoắn nước ngọt sợi mảnh"),
    ("071968", "subbases", "noun", "/ˈsʌbˌbeɪsɪz/", "lớp nền đường; cơ sở con tô-pô"),
    ("071969", "tankages", "noun", "/ˈtæŋkɪdʒɪz/", "bột phụ phẩm lò mổ; dung tích bồn"),
    ("071970", "teaselled", "verb", "/ˈtiːzəld/", "đã chải xù lông bề mặt len dạ (Anh)"),
    ("071971", "teaselling", "verb", "/ˈtiːzəlɪŋ/", "đang chải xù lông len dạ (Anh)"),
    ("071972", "teasels", "noun", "/ˈtiːzəlz/", "cây kế chải len; bàn chải xù len"),
    ("071973", "tetrazzinis", "noun", "/ˌtɛtrəˈziːniz/", "món mì Ý sốt kem gà nấm Tetrazzini"),
    ("071974", "thaumaturgies", "noun", "/ˈθɔːməˌtɜːrdʒiz/", "phép thuật làm phép lạ kỳ diệu"),
    ("071975", "thermograms", "noun", "/ˈθɜːrməˌɡræmz/", "ảnh nhiệt; biểu đồ ghi nhiệt độ"),
    ("071976", "thioridazines", "noun", "/ˌθaɪəˈrɪdəziːnz/", "thuốc an thần kinh thioridazine"),
    ("071977", "tocsins", "noun", "/ˈtɒksɪnz/", "tiếng chuông báo động khẩn cấp"),
    ("071978", "tonometers", "noun", "/toʊˈnɒmɪtərz/", "máy đo nhãn áp mắt; máy đo áp lực"),
    ("071979", "triacetates", "noun", "/traɪˈæsɪˌteɪts/", "sợi hoặc muối hóa học triaxetat"),
    ("071980", "usufructuaries", "noun", "/ˌjuːzjʊˈfrʌktʃuɛriz/", "người hưởng quyền hoa lợi (luật)"),
    ("071981", "vaishnavisms", "noun", "/ˈvaɪʃnəˌvɪzəmz/", "tông phái thờ thần Vishnu (Ấn Độ)"),
    ("071982", "virilizations", "noun", "/ˌvɪrəlaɪˈzeɪʃənz/", "hiện tượng nam tính hóa (y học)"),
    ("071983", "vouvrays", "noun", "/ˈvuːvreɪz/", "rượu vang trắng vùng Vouvray Pháp"),
    ("071984", "warlpiris", "noun", "/ˈwɔːlpɪriz/", "dân tộc và tiếng Warlpiri (Úc)"),
    ("071985", "weighers", "noun", "/ˈweɪərz/", "người cân đong hoặc cân kiểm tra"),
    ("071986", "whatchamacallits", "noun", "/ˈwʌtʃəməˌkɔːlɪts/", "cái gì ấy nhỉ (khẩu ngữ)"),
    ("071987", "whydahs", "noun", "/ˈwɪdəz/", "chim đuôi dài châu Phi whydah"),
    ("071988", "yardmasters", "noun", "/ˈjɑːrdˌmæstərz/", "trưởng ga điều phối đường sắt"),
    ("071989", "yumans", "noun", "/ˈjuːmənz/", "người và ngữ hệ Yuman bản địa Mỹ"),
    ("071990", "ablauts", "noun", "/ˈɑːblaʊts/", "hiện tượng biến âm nguyên âm gốc"),
    ("071991", "absorptivities", "noun", "/ˌæbsɔːrpˈtɪvɪtiz/", "hệ số hấp thụ bức xạ (vật lý)"),
    ("071992", "aiais", "noun", "/ˌeɪ aɪ ˈeɪz/", "tổ chức Hồi giáo AIAI ở Somalia"),
    ("071993", "anaerobes", "noun", "/ˈænəˌroʊbz/", "vi sinh vật kỵ khí (sống không O2)"),
    ("071994", "arabises", "noun", "/ˈærəbɪsɪz/", "cây cải đá thuộc chi Arabis"),
    ("071995", "araneuses", "noun", "/əˈreɪnjəsɪz/", "nhện chăng lưới bánh xe Araneus"),
    ("071996", "arctans", "noun", "/ˈɑːrktænz/", "hàm lượng giác ngược arctang"),
    ("071997", "arctostaphyloses", "noun", "/ˌɑːrktoʊˈstæfɪˌloʊsɪz/", "cây bụi quả gấu chi Arctostaphylos"),
    ("071998", "asperities", "noun", "/æˈspɛrɪtiz/", "độ nhám gồ ghề; thái độ gay gắt"),
    ("071999", "associateships", "noun", "/əˈsoʊʃiətʃɪps/", "chức vụ cộng sự hoặc hội viên"),
    ("072000", "autostradas", "noun", "/ˌɔːtoʊˈstrɑːdəz/", "đường cao tốc ở Ý (autostrada)"),
    ("072001", "backgroundings", "noun", "/ˈbækˌɡraʊndɪŋz/", "cuộc họp báo cung cấp thông tin nền"),
    ("072002", "balaenopteras", "noun", "/ˌbælɪˈnɒptərəz/", "chi Cá voi xanh và cá voi vây"),
]

with open("scratch/b35_r04_raw_p5.json") as f:
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

with open("scratch/b35_r04_p5.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r04_p5.json OK")
