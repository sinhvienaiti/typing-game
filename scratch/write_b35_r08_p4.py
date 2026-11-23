import json

items = [
    ("073803", "homaruses", "noun", "/ˈhɒmərəsɪz/", "chi Tôm hùm càng lớn (Homarus)"),
    ("073804", "humouses", "noun", "/ˈhʊməsɪz/", "món sốt đậu gà nghiền hummus"),
    ("073805", "hyphae", "noun", "/ˈhaɪfiː/", "sợi nấm (cấu tạo hệ sợi nấm)"),
    ("073806", "hyphas", "noun", "/ˈhaɪfəz/", "sợi nấm (cấu tạo hệ sợi nấm)"),
    ("073807", "ijssels", "noun", "/ˈaɪsəlz/", "sông IJssel ở Hà Lan"),
    ("073808", "ironists", "noun", "/ˈaɪrənɪsts/", "người hay dùng lối nói mỉa mai"),
    ("073809", "latinaes", "noun", "/ləˈtiːniːz/", "phân họ hoặc thuật ngữ Latinae"),
    ("073810", "lemnisci", "noun", "/lɛmˈnɪsaɪ/", "dải bó sợi cảm giác (thần kinh)"),
    ("073811", "lemniscuses", "noun", "/lɛmˈnɪskəsɪz/", "dải bó sợi cảm giác (thần kinh)"),
    ("073812", "ligules", "noun", "/ˈlɪɡjuːlz/", "lưỡi nhỏ bẹ lá; tràng hoa hình lưỡi"),
    ("073813", "limoniums", "noun", "/lɪˈmoʊniəmz/", "cây hoa oải hương biển Limonium"),
    ("073814", "lyciums", "noun", "/ˈlɪsiəmz/", "chi Cây câu kỷ tử (Lycium)"),
    ("073815", "lymphopenias", "noun", "/ˌlɪmfoʊˈpiːniəz/", "chứng giảm bạch cầu lympho máu"),
    ("073816", "maltsters", "noun", "/ˈmɔːltstərz/", "thợ ủ chế biến mạch nha nấu bia"),
    ("073817", "manihots", "noun", "/ˈmænɪˌhɒts/", "chi Cây sắn khoai mì (Manihot)"),
    ("073818", "misalliances", "noun", "/ˌmɪsəˈlaɪənsɪz/", "cuộc hôn nhân không môn đăng hộ đối"),
    ("073819", "misremembers", "verb", "/ˌmɪsrɪˈmɛmbərz/", "nhớ nhầm lẫn ký ức hoặc chi tiết"),
    ("073820", "monologists", "noun", "/ˈmɒnəˌlɒɡɪsts/", "diễn viên độc thoại trên sân khấu"),
    ("073821", "mudskippers", "noun", "/ˈmʌdˌskɪpərz/", "cá thòi lòi leo bãi bùn ngập mặn"),
    ("073822", "naziisms", "noun", "/ˈnɑːtsiˌɪzəmz/", "chủ nghĩa phát xít Đức Quốc xã"),
    ("073823", "nazimovas", "noun", "/nəˈzɪməvəz/", "nữ diễn viên Nga Alla Nazimova"),
    ("073824", "orpiments", "noun", "/ˈɔːrpɪmənts/", "khoáng vật thạch hoàng vàng asen"),
    ("073825", "outrided", "verb", "/ˌaʊtˈraɪdɪd/", "đã vượt qua cơn bão; cưỡi nhanh hơn"),
    ("073826", "outrides", "verb", "/ˌaʊtˈraɪdz/", "vượt qua sóng gió; cưỡi ngựa vượt"),
    ("073827", "outriding", "verb", "/ˌaʊtˈraɪdɪŋ/", "đang vượt qua sóng gió; cưỡi vượt"),
    ("073828", "parasitemias", "noun", "/ˌpærəsaɪˈtiːmiəz/", "tình trạng ký sinh trùng trong máu"),
    ("073829", "partheniums", "noun", "/pɑːrˈθiːniəmz/", "cây cúc dại chi Parthenium"),
    ("073830", "peploses", "noun", "/ˈpɛplɒsɪz/", "áo choàng dài Hy Lạp cổ peplos"),
    ("073831", "perfused", "verb", "/pərˈfjuːzd/", "đã tưới máu truyền dịch qua mô"),
    ("073832", "perfuses", "verb", "/pərˈfjuːzɪz/", "tưới máu truyền dịch qua cơ quan"),
    ("073833", "perfusing", "verb", "/pərˈfjuːzɪŋ/", "đang tưới máu truyền dịch qua mô"),
    ("073834", "pineta", "noun", "/paɪˈniːtə/", "rừng thông; vườn sưu tập cây thông"),
    ("073835", "pinetums", "noun", "/paɪˈniːtəmz/", "vườn ươm sưu tập các loài thông"),
    ("073836", "pizzazes", "noun", "/pɪˈzæzɪz/", "sự sôi nổi rực rỡ quyến rũ (Mỹ)"),
    ("073837", "platyhelmintheses", "noun", "/ˌplætɪhɛlˈmɪnθiːzɪz/", "ngành Giun dẹp (sán lá, sán dây)"),
    ("073838", "playlets", "noun", "/ˈpleɪlɪts/", "vở kịch ngắn một màn (từ ít dùng)"),
    ("073839", "polisteses", "noun", "/pɒˈlɪstiːzɪz/", "chi Ong bắp cày giấy (Polistes)"),
    ("073840", "polybutylenes", "noun", "/ˌpɒliˈbjuːtɪˌliːnz/", "nhựa dẻo tổng hợp polybutylen"),
    ("073841", "postbags", "noun", "/ˈpoʊstˌbæɡz/", "túi đựng thư bưu phẩm đưa thư"),
    ("073842", "pouters", "noun", "/ˈpaʊtərz/", "người hay bĩu môi hờn; bồ câu phồng"),
    ("073843", "quintuplets", "noun", "/kwɪnˈtʌplɪts/", "ca sinh năm; bộ năm giống nhau"),
    ("073844", "quizzers", "noun", "/ˈkwɪzərz/", "người ra đề đố; người soi mói"),
    ("073845", "rajpoots", "noun", "/ˈrɑːdʒpuːts/", "chiến binh đẳng cấp Rajput Ấn Độ"),
    ("073846", "reconcilers", "noun", "/ˈrɛkənˌsaɪlərz/", "người hòa giải hàn gắn mâu thuẫn"),
    ("073847", "reconnoitrings", "noun", "/ˌrɛkəˈnɔɪtərɪŋz/", "cuộc trinh sát do thám địa hình"),
    ("073848", "sabahans", "noun", "/səˈbɑːənz/", "người dân bang Sabah (Malaysia)"),
    ("073849", "sandglasses", "noun", "/ˈsændˌɡlæsɪz/", "đồng hồ cát đo thời gian"),
    ("073850", "sarabands", "noun", "/ˈsærəˌbændz/", "điệu múa cổ điển Pháp sarabande"),
    ("073851", "schnapses", "noun", "/ʃnæpsɪz/", "rượu mạnh chưng cất schnapps Đức"),
    ("073852", "scholiums", "noun", "/ˈskoʊliəmz/", "lời chú giải bên lề văn bản cổ"),
    ("073853", "scoffers", "noun", "/ˈskɒfərz/", "kẻ chế giễu nhạo báng; kẻ ăn ngấu"),
    ("073854", "semivowels", "noun", "/ˈsɛmiˌvaʊəlz/", "bán nguyên âm (như /w/, /j/)"),
    ("073855", "shipsides", "noun", "/ˈʃɪpˌsaɪdz/", "mạn tàu thủy; cầu cảng sát mạn tàu"),
    ("073856", "skidders", "noun", "/ˈskɪdərz/", "máy kéo gỗ trong rừng; vật trượt"),
    ("073857", "soupcons", "noun", "/suːpˈsɒnz/", "một chút xíu gia vị; nét thoảng qua"),
    ("073858", "sterilisers", "noun", "/ˈstɛrɪˌlaɪzərz/", "máy tiệt trùng khử khuẩn (Anh)"),
    ("073859", "surgeonfishes", "noun", "/ˈsɜːrdʒənˌfɪʃɪz/", "cá đuôi gai sắc (cá bác sĩ biển)"),
    ("073860", "tailstocks", "noun", "/ˈteɪlˌstɒks/", "ụ động giữ phôi trên máy tiện"),
    ("073861", "thaddaeuses", "noun", "/θəˈdiːəsɪz/", "Thánh Tông đồ Giu-đa Ta-đê-ô"),
    ("073862", "toadflaxes", "noun", "/ˈtoʊdˌflæksɪz/", "cây hoa mõm chó vàng hoang dã"),
    ("073863", "topicalizations", "noun", "/ˌtɒpɪkəlaɪˈzeɪʃənz/", "phép đề hóa chuyển lên chủ đề câu"),
    ("073864", "toyons", "noun", "/ˈtɔɪənz/", "cây bụi quả đỏ toyon (California)"),
    ("073865", "tramontanas", "noun", "/ˌtrɑːmənˈtɑːnəz/", "gió bắc lạnh buốt Địa Trung Hải"),
    ("073866", "unknots", "verb", "/ʌnˈnɒts/", "tháo gỡ nút thắt dây rối"),
    ("073867", "unknotting", "verb", "/ʌnˈnɒtɪŋ/", "đang tháo gỡ nút thắt dây"),
    ("073868", "usneas", "noun", "/ˈʌsniəz/", "địa y râu rồng mọc trên cây Usnea"),
    ("073869", "utnapishtims", "noun", "/ˌuːtnɑːˈpɪʃtɪmz/", "nhân vật Utnapishtim (Gilgamesh)"),
    ("073870", "veloutes", "noun", "/vɛˈluːts/", "xốt trắng nấu từ nước dùng velouté"),
    ("073871", "volvae", "noun", "/ˈvɒlviː/", "bao gốc hình chén ở chân cây nấm"),
    ("073872", "volvas", "noun", "/ˈvɒlvəz/", "bao gốc hình chén ở chân cây nấm"),
    ("073873", "washdays", "noun", "/ˈwɒʃˌdeɪz/", "ngày giặt giũ quần áo trong tuần"),
    ("073874", "weatherstripped", "verb", "/ˈwɛðərˌstrɪpt/", "đã lắp gioăng khe cửa chắn gió bụi"),
    ("073875", "weatherstrips", "noun", "/ˈwɛðərˌstrɪps/", "dải gioăng khe cửa chắn gió mưa"),
    ("073876", "wisconsinites", "noun", "/wɪˈskɒnsɪˌnaɪts/", "người dân bang Wisconsin của Mỹ"),
    ("073877", "acrididaes", "noun", "/əˈkrɪdɪˌdiːz/", "họ Châu chấu (bộ Cánh thẳng)"),
    ("073878", "adrenalectomies", "noun", "/əˌdriːnəˈlɛktəmiz/", "phẫu thuật cắt bỏ tuyến thượng thận"),
    ("073879", "anthuses", "noun", "/ˈænθəsɪz/", "chi Chim manh manh đồng cỏ Anthus"),
    ("073880", "apidaes", "noun", "/ˈeɪpɪˌdiːz/", "họ Ong (ong mật và ong nghệ)"),
    ("073881", "astilbes", "noun", "/əˈstɪlbiz/", "hoa lông chim rực rỡ chi Astilbe"),
    ("073882", "athapaskans", "noun", "/ˌæθəˈpæskənz/", "người và ngữ hệ Athabasca Bắc Mỹ"),
    ("073883", "auspexes", "noun", "/ˈɔːspɛksɪz/", "thầy chiêm tinh xem chim La Mã cổ"),
    ("073884", "bahreins", "noun", "/bɑːˈreɪnz/", "quốc đảo Bahrain ở vịnh Ba Tư"),
    ("073885", "basutos", "noun", "/bəˈsuːtoʊz/", "người và tiếng Basotho ở Lesotho"),
    ("073886", "blastoderms", "noun", "/ˈblæstəˌdɜːrmz/", "lớp bì phôi hình đĩa phôi sớm"),
    ("073887", "blueings", "noun", "/ˈbluːɪŋz/", "thuốc lơ xanh tẩy trắng quần áo"),
    ("073888", "boxfishes", "noun", "/ˈbɒksˌfɪʃɪz/", "cá nóc hòm thân hộp xương cứng"),
    ("073889", "brahuis", "noun", "/ˈbrɑːhuːiz/", "người và tiếng Brahui ở Pakistan"),
    ("073890", "caddoans", "noun", "/kəˈdoʊənz/", "ngữ hệ bản địa Caddo Bắc Mỹ"),
    ("073891", "calidrises", "noun", "/kəˈlɪdrɪsɪz/", "chi Chim dẽ choắt bãi bùn Calidris"),
    ("073892", "coronates", "verb", "/ˈkɒrəˌneɪts/", "đội vương miện phong vương (hiếm)"),
    ("073893", "coronating", "verb", "/ˈkɒrəˌneɪtɪŋ/", "đang đội vương miện đăng quang"),
    ("073894", "corselets", "noun", "/ˈkɔːrslɪts/", "áo giáp che thân; áo nịt ngực xưa"),
    ("073895", "coryzas", "noun", "/kəˈraɪzəz/", "chứng sổ mũi viêm mũi cấp tính"),
    ("073896", "cottuses", "noun", "/ˈkɒtəsɪz/", "chi Cá bống đầu to nước ngọt Cottus"),
    ("073897", "covariations", "noun", "/ˌkoʊvɛəriˈeɪʃənz/", "sự hiệp biến biến thiên cùng nhau"),
    ("073898", "decarbonized", "verb", "/diːˈkɑːrbəˌnaɪzd/", "đã khử cacbon hoặc muội than"),
    ("073899", "decarbonizes", "verb", "/diːˈkɑːrbəˌnaɪzɪz/", "khử cacbon; tẩy muội than động cơ"),
    ("073900", "decarbonizing", "verb", "/diːˈkɑːrbəˌnaɪzɪŋ/", "đang khử cacbon hoặc muội than"),
    ("073901", "dedifferentiations", "noun", "/diːˌdɪfərɛnʃiˈeɪʃənz/", "sự phản biệt hóa tế bào (sinh học)"),
    ("073902", "dejeuners", "noun", "/ˌdeɪʒɜːˈneɪz/", "bữa trưa; bữa điểm tâm (tiếng Pháp)"),
]

with open("scratch/b35_r08_raw_p4.json") as f:
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

with open("scratch/b35_r08_p4.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r08_p4.json OK")
