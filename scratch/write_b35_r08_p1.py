import json

items = [
    ("073503", "aeolics", "noun", "/iːˈɒlɪks/", "phương ngữ Hy Lạp cổ Aeolic"),
    ("073504", "altaces", "noun", "/ˈælteɪsɪz/", "thuốc hạ huyết áp Altace"),
    ("073505", "annamites", "noun", "/ˈænəˌmaɪts/", "người An Nam hoặc tiếng Việt (cũ)"),
    ("073506", "antiprotozoals", "noun", "/ˌæntɪproʊtəˈzoʊəlz/", "thuốc kháng động vật nguyên sinh"),
    ("073507", "apiaceaes", "noun", "/ˌeɪpiˈeɪʃiˌiːz/", "họ Hoa tán (cần tây, cà rốt)"),
    ("073508", "apocynaceaes", "noun", "/ˌæpəsɪˈneɪʃiˌiːz/", "họ Trúc đào (hoa sứ, dừa cạn)"),
    ("073509", "arrobas", "noun", "/əˈroʊbəz/", "đơn vị khối lượng arroba (~11,5 kg)"),
    ("073510", "arsenopyrites", "noun", "/ˌɑːrsənoʊˈpaɪraɪts/", "quặng asenopirit (FeAsS)"),
    ("073511", "ascariases", "noun", "/ˌæskəˈraɪəsiːz/", "bệnh nhiễm giun đũa đường ruột"),
    ("073512", "asdics", "noun", "/ˈæzdɪks/", "hệ thống dò tìm tàu ngầm ASDIC"),
    ("073513", "avicennias", "noun", "/ˌævɪˈsɛniəz/", "cây mắm rừng ngập mặn Avicennia"),
    ("073514", "beshrewed", "verb", "/bɪˈʃruːd/", "đã nguyền rủa nhẹ (từ cổ)"),
    ("073515", "beshrewing", "verb", "/bɪˈʃruːɪŋ/", "đang nguyền rủa nhẹ (từ cổ)"),
    ("073516", "beshrews", "verb", "/bɪˈʃruːz/", "nguyền rủa nhẹ (văn cổ)"),
    ("073517", "bioelectricities", "noun", "/ˌbaɪoʊɪlɛkˈtrɪsɪtiz/", "hiện tượng điện sinh học cơ thể"),
    ("073518", "birchbarks", "noun", "/ˈbɜːrtʃˌbɑːrks/", "vỏ cây bạch dương; xuồng vỏ cây"),
    ("073519", "blastomycoses", "noun", "/ˌblæstoʊmaɪˈkoʊsiːz/", "bệnh nhiễm nấm phổi Blastomyces"),
    ("073520", "blitzsteins", "noun", "/ˈblɪtsˌstaɪnz/", "nhà soạn nhạc Marc Blitzstein"),
    ("073521", "bollworms", "noun", "/ˈboʊlˌwɜːrmz/", "sâu đục quả cây bông vải"),
    ("073522", "boringnesses", "noun", "/ˈbɔːrɪŋnəsɪz/", "tính chất buồn tẻ nhạt nhẽo chán"),
    ("073523", "boutelouas", "noun", "/ˌbuːtɪˈluːəz/", "cỏ đồng cỏ Mỹ chi Bouteloua"),
    ("073524", "buxuses", "noun", "/ˈbʌksəsɪz/", "cây hoàng dương chi Buxus"),
    ("073525", "cabalists", "noun", "/ˈkæbəlɪsts/", "nhà nghiên cứu mật giáo Kabbalah"),
    ("073526", "caltrops", "noun", "/ˈkæltrəps/", "chông sắt bốn ngạnh; cây tật lê"),
    ("073527", "canareses", "noun", "/ˌkænəˈriːz/", "người và tiếng Kannada Ấn Độ"),
    ("073528", "catheterisations", "noun", "/ˌkæθɪtəraɪˈzeɪʃənz/", "thủ thuật đặt ống thông y tế (Anh)"),
    ("073529", "catostomuses", "noun", "/ˌkætəˈstoʊməsɪz/", "chi Cá mút nước ngọt Catostomus"),
    ("073530", "cavias", "noun", "/ˈkeɪviəz/", "chi Chuột lang nhà (Cavia)"),
    ("073531", "chenopodiaceaes", "noun", "/ˌkiːnoʊpoʊdiˈeɪʃiˌiːz/", "họ Rau muối (rau chân vịt, củ cải)"),
    ("073532", "cleomes", "noun", "/kliˈoʊmiz/", "cây màn màn hoa nhện chi Cleome"),
    ("073533", "closedowns", "noun", "/ˈkloʊzˌdaʊnz/", "sự đóng cửa ngừng hoạt động (Anh)"),
    ("073534", "colubers", "noun", "/ˈkɒljʊbərz/", "chi Rắn nước không độc Coluber"),
    ("073535", "containerships", "noun", "/kənˈteɪnərˌʃɪps/", "tàu thủy chuyên chở container"),
    ("073536", "coprophagias", "noun", "/ˌkɒprəˈfeɪdʒəz/", "tật ăn phân (sinh vật, tâm thần)"),
    ("073537", "cringles", "noun", "/ˈkrɪŋɡəlz/", "khoen tròn móc dây trên mép buồm"),
    ("073538", "crucifers", "noun", "/ˈkruːsɪfərz/", "cây họ Cải; người cầm thánh giá"),
    ("073539", "ctenophores", "noun", "/ˈtɛnəˌfɔːrz/", "sứa lược động vật biển trong suốt"),
    ("073540", "cybercultures", "noun", "/ˈsaɪbərˌkʌltʃərz/", "văn hóa không gian mạng internet"),
    ("073541", "dactylises", "noun", "/dækˈtɪlɪsɪz/", "cỏ gà mật Dactylis làm cỏ khô"),
    ("073542", "daugavpilses", "noun", "/ˈdaʊɡɑːvˌpɪlsɪz/", "thành phố Daugavpils ở Latvia"),
    ("073543", "decalcomanias", "noun", "/dɪˌkælkəˈmeɪniəz/", "tranh chuyển hình đề-can (decal)"),
    ("073544", "decantations", "noun", "/ˌdiːkænˈteɪʃənz/", "quá trình gạn rót tách cặn lắng"),
    ("073545", "decarbonised", "verb", "/diːˈkɑːrbəˌnaɪzd/", "đã khử cacbon hoặc muội than (Anh)"),
    ("073546", "decarbonises", "verb", "/diːˈkɑːrbəˌnaɪzɪz/", "khử cacbon hoặc muội than (Anh)"),
    ("073547", "decarbonising", "verb", "/diːˈkɑːrbəˌnaɪzɪŋ/", "đang khử cacbon hoặc muội (Anh)"),
    ("073548", "denticles", "noun", "/ˈdɛntɪkəlz/", "gai răng nhỏ; vảy da cá mập"),
    ("073549", "desipramines", "noun", "/dɛˈsɪprəmiːnz/", "thuốc chống trầm cảm desipramine"),
    ("073550", "dibbers", "noun", "/ˈdɪbərz/", "cây gậy chọc lỗ tra hạt trồng cây"),
    ("073551", "eccms", "noun", "/ˌiː siː siː ˈɛmz/", "biện pháp phản công điện tử ECCM"),
    ("073552", "ellipticities", "noun", "/ˌɛlɪpˈtɪsɪtiz/", "độ dẹt hình elip (hình học)"),
    ("073553", "enervates", "verb", "/ˈɛnərˌveɪts/", "làm kiệt sức suy nhược tinh thần"),
    ("073554", "ercillas", "noun", "/ɜːrˈsɪləz/", "cây leo hoa hồng bụi chi Ercilla"),
    ("073555", "evanesced", "verb", "/ˌɛvəˈnɛst/", "đã tan biến mờ dần vào hư không"),
    ("073556", "evanesces", "verb", "/ˌɛvəˈnɛsɪz/", "tan biến mờ dần đi mất hút"),
    ("073557", "evanescing", "verb", "/ˌɛvəˈnɛsɪŋ/", "đang tan biến mờ dần đi"),
    ("073558", "eyeshades", "noun", "/ˈaɪˌʃeɪdz/", "mũ lưỡi trai che mắt; miếng bịt mắt"),
    ("073559", "ferricyanides", "noun", "/ˌfɛrɪˈsaɪənaɪdz/", "muối hóa học ferrixyanua"),
    ("073560", "finbacks", "noun", "/ˈfɪnˌbæks/", "cá voi vây lưng lớn"),
    ("073561", "fluoridated", "verb", "/ˈflʊərɪˌdeɪtɪd/", "đã bổ sung flo vào nước máy"),
    ("073562", "fluoridates", "verb", "/ˈflʊərɪˌdeɪts/", "bổ sung florua vào nước uống"),
    ("073563", "fluoridating", "verb", "/ˈflʊərɪˌdeɪtɪŋ/", "đang bổ sung florua vào nước"),
    ("073564", "fulicas", "noun", "/ˈfjuːlɪkəz/", "chi Chim sâm cầm (Fulica)"),
    ("073565", "glebas", "noun", "/ˈɡliːbəz/", "khối mô sinh bào tử của nấm kín"),
    ("073566", "gorgonians", "noun", "/ɡɔːrˈɡoʊniənz/", "san hô sừng quạt biển gorgonian"),
    ("073567", "hackamores", "noun", "/ˈhækəˌmɔːrz/", "dây cương đầu ngựa không hàm thiếc"),
    ("073568", "homophonies", "noun", "/həˈmɒfəniz/", "nhạc chủ điệu; hiện tượng đồng âm"),
    ("073569", "homozygotes", "noun", "/ˌhoʊmoʊˈzaɪɡoʊts/", "cá thể mang hai alen đồng hợp tử"),
    ("073570", "hyphemas", "noun", "/haɪˈfiːməz/", "xuất huyết tiền phòng nhãn cầu"),
    ("073571", "intellections", "noun", "/ˌɪntəˈlɛkʃənz/", "hoạt động tư duy lý trí hiểu biết"),
    ("073572", "intercalated", "verb", "/ɪnˈtɜːrkəˌleɪtɪd/", "đã xen kẽ vào giữa; đã thêm nhuận"),
    ("073573", "intercalates", "verb", "/ɪnˈtɜːrkəˌleɪts/", "xen kẽ vào giữa; thêm ngày nhuận"),
    ("073574", "intercalating", "verb", "/ɪnˈtɜːrkəˌleɪtɪŋ/", "đang xen vào giữa; thêm ngày nhuận"),
    ("073575", "islamised", "verb", "/ˈɪzləˌmaɪzd/", "đã Hồi giáo hóa (cách viết Anh)"),
    ("073576", "islamises", "verb", "/ˈɪzləˌmaɪzɪz/", "Hồi giáo hóa (cách viết Anh)"),
    ("073577", "islamising", "verb", "/ˈɪzləˌmaɪzɪŋ/", "đang Hồi giáo hóa (cách viết Anh)"),
    ("073578", "klaproths", "noun", "/ˈklɑːprɒts/", "nhà hóa học Đức Martin Klaproth"),
    ("073579", "korbuts", "noun", "/ˈkɔːrbʊts/", "nữ VĐV thể dục Olga Korbut"),
    ("073580", "lamarckisms", "noun", "/ləˈmɑːrkɪzəmz/", "thuyết tiến hóa tập tính Lamarck"),
    ("073581", "lanugos", "noun", "/ləˈnuːɡoʊz/", "lông tơ mịn bao phủ thai nhi"),
    ("073582", "lapplands", "noun", "/ˈlæplændz/", "vùng Lapland ở bắc Scandinavia"),
    ("073583", "laryngospasms", "noun", "/ləˈrɪŋɡoʊˌspæzəmz/", "cơn co thắt thanh quản khó thở"),
    ("073584", "linarias", "noun", "/lɪˈnɛəriəz/", "cây hoa mõm sói nhỏ chi Linaria"),
    ("073585", "lycopersicums", "noun", "/ˌlaɪkoʊˈpɜːrsɪkəmz/", "chi Cà chua (tên cũ Lycopersicum)"),
    ("073586", "lycosas", "noun", "/laɪˈkoʊsəz/", "chi Nhện sói săn mồi Lycosa"),
    ("073587", "maillols", "noun", "/maɪˈɒlz/", "nhà điêu khắc Pháp Aristide Maillol"),
    ("073588", "maiolicas", "noun", "/məˈjɒlɪkəz/", "đồ gốm tráng men thiếc maiolica Ý"),
    ("073589", "malpighiaceaes", "noun", "/mælˌpɪɡiˈeɪʃiˌiːz/", "họ Sơ ri nhiệt đới Malpighiaceae"),
    ("073590", "mammillarias", "noun", "/ˌmæmɪˈlɛəriəz/", "xương rồng vú tròn chi Mammillaria"),
    ("073591", "marasmuses", "noun", "/məˈræzməsɪz/", "chứng suy dinh dưỡng teo đét nặng"),
    ("073592", "miltowns", "noun", "/ˈmɪlˌtaʊnz/", "thuốc an thần Miltown (Mỹ cũ)"),
    ("073593", "minelayers", "noun", "/ˈmaɪnˌleɪərz/", "tàu hải quân chuyên rải thủy lôi"),
    ("073594", "minicars", "noun", "/ˈmɪniˌkɑːrz/", "xe ô tô siêu nhỏ gọn minicar"),
    ("073595", "molalities", "noun", "/moʊˈlælɪtiz/", "nồng độ molan của dung dịch (hóa)"),
    ("073596", "myxedemas", "noun", "/ˌmɪksɪˈdiːməz/", "bệnh phù niêm do suy tuyến giáp"),
    ("073597", "nbws", "noun", "/ˌɛn biː ˈdʌbəljuːz/", "hướng bắc chếch tây (NbW)"),
    ("073598", "numskulls", "noun", "/ˈnʌmˌskʌlz/", "kẻ ngu dốt đần độn chậm hiểu"),
    ("073599", "onomasticses", "noun", "/ˌɒnəˈmæstɪksɪz/", "ngành danh xưng học nghiên cứu tên"),
    ("073600", "opacifications", "noun", "/oʊˌpæsɪfɪˈkeɪʃənz/", "hiện tượng hóa đục (thủy tinh thể)"),
    ("073601", "orchitides", "noun", "/ɔːrˈkaɪtɪˌdiːz/", "bệnh viêm tinh hoàn (y học)"),
    ("073602", "outspaned", "verb", "/ˈaʊtˌspænd/", "đã tháo ách cho bò; nghỉ xả trại"),
]

with open("scratch/b35_r08_raw_p1.json") as f:
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

with open("scratch/b35_r08_p1.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r08_p1.json OK")
