import json

items = [
    ("069503", "unchastest", "adj", "/ʌnˈtʃeɪstɪst/", "không trong trắng tiết hạnh nhất"),
    ("069504", "upstrokes", "noun", "/ˈʌpˌstroʊks/", "nét bút đưa hất lên từ dưới"),
    ("069505", "vacationers", "noun", "/veɪˈkeɪʃənərz/", "khách đi nghỉ mát du lịch (Mỹ)"),
    ("069506", "vanirs", "noun", "/ˈvɑːnɪərz/", "nhóm thần Vanir thần thoại Bắc Âu"),
    ("069507", "verrucas", "noun", "/vəˈruːkəz/", "mụn cóc lòng bàn chân do vi rút"),
    ("069508", "vestrises", "noun", "/ˈvɛstrɪsɪz/", "vũ công ba lê Pháp Vestris"),
    ("069509", "vuillards", "noun", "/ˈvwiːjɑːrz/", "họa sĩ Pháp Édouard Vuillard"),
    ("069510", "waterers", "noun", "/ˈwɔːtərərz/", "người tưới cây; bình vòi tưới nước"),
    ("069511", "waylaying", "verb", "/ˈweɪˌleɪɪŋ/", "đang mai phục chặn đánh dọc đường"),
    ("069512", "waylays", "verb", "/ˈweɪˌleɪz/", "mai phục chặn đón đường tấn công"),
    ("069513", "xyies", "noun", "/ˌɛks waɪ ˈwaɪz/", "hội chứng thừa nhiễm sắc thể XYY"),
    ("069514", "yardarms", "noun", "/ˈjɑːrdˌɑːrmz/", "hai đầu xà ngang treo buồm trên cột"),
    ("069515", "yedos", "noun", "/ˈjɛdoʊz/", "tên cổ của Tokyo thời Edo Nhật Bản"),
    ("069516", "alizarins", "noun", "/əˈlɪzərɪnz/", "thuốc nhuộm đỏ alizarin thiên nhiên"),
    ("069517", "allocutions", "noun", "/ˌæləˈkjuːʃənz/", "bài phát biểu tuyên cáo trang trọng"),
    ("069518", "amebas", "noun", "/əˈmiːbəz/", "trùng biến hình amip đơn bào"),
    ("069519", "annelids", "noun", "/ˈænəlɪdz/", "động vật giun đốt như giun đất đỉa"),
    ("069520", "anomias", "noun", "/əˈnoʊmiəz/", "chứng mất khả năng nhớ gọi tên vật"),
    ("069521", "anthroposophies", "noun", "/ˌænθrəˈpɒsəfiz/", "học thuyết nhân trí Rudolf Steiner"),
    ("069522", "antipopes", "noun", "/ˈæntiˌpoʊps/", "giáo hoàng đối lập tranh ngôi giáo"),
    ("069523", "argillites", "noun", "/ˈɑːrdʒəˌlaɪts/", "đá sét phiến hóa nhẹ kết cấu mịn"),
    ("069524", "arizonans", "noun", "/ˌærɪˈzoʊnənz/", "người dân bang Arizona của Mỹ"),
    ("069525", "ascenders", "noun", "/əˈsɛndərz/", "nét nhô trên chữ cái; dụng cụ leo"),
    ("069526", "autoantibodies", "noun", "/ˌɔːtoʊˈæntɪˌbɒdiz/", "tự kháng thể tấn công mô cơ thể"),
    ("069527", "barkeepers", "noun", "/ˈbɑːrˌkiːpərz/", "chủ quán rượu hoặc người pha chế"),
    ("069528", "bluejackets", "noun", "/ˈbluːˌdʒækɪts/", "thủy thủ hải quân mặc áo xanh xưa"),
    ("069529", "brunhilds", "noun", "/ˈbruːnhɪldz/", "nữ chiến thần Valkyrie Brünnhilde"),
    ("069530", "cathouses", "noun", "/ˈkætˌhaʊzɪz/", "nhà chứa mại dâm (từ lóng)"),
    ("069531", "centerfielders", "noun", "/ˈsɛntərˌfiːldərz/", "cầu thủ giữa sân ngoài bóng chày"),
    ("069532", "chessmen", "noun", "/ˈtʃɛsmən/", "quân cờ trên bàn cờ vua"),
    ("069533", "coatis", "noun", "/koʊˈɑːtiz/", "thú họ gấu mèo mũi dài Nam Mỹ"),
    ("069534", "commissures", "noun", "/ˈkɒmɪˌʃʊərz/", "mép nối giữa hai bán cầu não mắt"),
    ("069535", "conchologies", "noun", "/kɒŋˈkɒlədʒiz/", "ngành nghiên cứu sưu tầm vỏ ốc sò"),
    ("069536", "contrabasses", "noun", "/ˈkɒntrəˌbeɪsɪz/", "đàn đại hồ cầm lớn nhất dàn nhạc"),
    ("069537", "coonskins", "noun", "/ˈkuːnˌskɪnz/", "da lông gấu mèo hoặc mũ lông đuôi"),
    ("069538", "corers", "noun", "/ˈkɔːrərz/", "dụng cụ khoét bỏ lõi hạt táo dứa"),
    ("069539", "corkboards", "noun", "/ˈkɔːrkˌbɔːrdz/", "bảng gỗ bần mềm để ghim thông báo"),
    ("069540", "cumulated", "verb", "/ˈkjuːmjəˌleɪtɪd/", "đã tích lũy cộng dồn chồng chất"),
    ("069541", "cumulates", "verb", "/ˈkjuːmjəˌleɪts/", "tích lũy dồn lại từng bước"),
    ("069542", "cumulating", "verb", "/ˈkjuːmjəˌleɪtɪŋ/", "đang tích lũy chồng chất dồn lại"),
    ("069543", "deerstalkers", "noun", "/ˈdɪərˌstɔːkərz/", "mũ vải hai lưỡi trai thợ săn hươu"),
    ("069544", "dholes", "noun", "/doʊlz/", "chó sói đỏ hoang dã châu Á"),
    ("069545", "disproofs", "noun", "/dɪsˈpruːfs/", "bằng chứng hoặc lập luận bác bỏ"),
    ("069546", "drambuies", "noun", "/dræmˈbuːiz/", "rượu mùi mật ong thảo mộc Drambuie"),
    ("069547", "dufies", "noun", "/djuːˈfiz/", "họa sĩ Pháp Raoul Dufy"),
    ("069548", "eniwetoks", "noun", "/ˌɛnɪˈwiːtɒks/", "đảo san hô vòng Enewetak Thái Bình"),
    ("069549", "epaulettes", "noun", "/ˈɛpəˌlɛts/", "cầu vai quân hàm trên vai áo lính"),
    ("069550", "euterpes", "noun", "/juːˈtɜːrpiz/", "chi cọ açaí Euterpe; nàng thơ nhạc"),
    ("069551", "exogamies", "noun", "/ɛkˈsɒɡəmiz/", "tập tục kết hôn ngoài thị tộc"),
    ("069552", "fauves", "noun", "/foʊvz/", "họa sĩ trường phái Dã thú Pháp"),
    ("069553", "fellated", "verb", "/fəˈleɪtɪd/", "đã kích thích sinh dục bằng miệng"),
    ("069554", "fellates", "verb", "/fəˈleɪts/", "kích thích sinh dục bằng miệng"),
    ("069555", "fellating", "verb", "/fəˈleɪtɪŋ/", "đang kích thích sinh dục bằng miệng"),
    ("069556", "fluorspars", "noun", "/ˈflʊərˌspɑːrz/", "khoáng vật florit phát huỳnh quang"),
    ("069557", "furnivalls", "noun", "/ˈfɜːrnɪvɔːlz/", "học giả ngữ văn Anh Furnivall"),
    ("069558", "goalmouths", "noun", "/ˈɡoʊlˌmaʊðz/", "vùng trước khung thành bóng đá"),
    ("069559", "gueneveres", "noun", "/ˈɡwɛnɪˌvɪərz/", "hoàng hậu Guinevere truyền thuyết"),
    ("069560", "handclaps", "noun", "/ˈhændˌklæps/", "tiếng vỗ tay tán thưởng nhịp điệu"),
    ("069561", "haslets", "noun", "/ˈheɪslɪts/", "chả thịt phủ tạng lợn kiểu Anh"),
    ("069562", "heavers", "noun", "/ˈhiːvərz/", "công nhân bốc vác; thanh xà bẩy"),
    ("069563", "honeggers", "noun", "/ˈhɒnɪɡərz/", "nhà soạn nhạc Thụy Sĩ Honegger"),
    ("069564", "iapetuses", "noun", "/aɪˈæpɪtəsɪz/", "thần Titan Iapetus; vệ tinh Thổ"),
    ("069565", "ignitors", "noun", "/ɪɡˈnaɪtərz/", "bộ đánh lửa mồi nổ động cơ tên lửa"),
    ("069566", "jansenisms", "noun", "/ˈdʒænsənˌɪzəmz/", "giáo thuyết tiền định Jansenism"),
    ("069567", "kalkas", "noun", "/ˈkælkəz/", "người Mông Cổ Khalkha đa số"),
    ("069568", "kalmias", "noun", "/ˈkælmiəz/", "cây nguyệt quế núi thuộc chi Kalmia"),
    ("069569", "korunas", "noun", "/kəˈruːnəz/", "đơn vị tiền tệ koruna Cộng hòa Séc"),
    ("069570", "lactucas", "noun", "/ˈlæktjʊkəz/", "cây rau diếp xà lách chi Lactuca"),
    ("069571", "lahars", "noun", "/ˈlɑːhɑːrz/", "dòng bùn đá núi lửa phun trào lahar"),
    ("069572", "lobules", "noun", "/ˈlɒbjuːlz/", "tiểu thùy nhỏ cấu tạo tuyến cơ quan"),
    ("069573", "lungers", "noun", "/ˈlʌŋərz/", "người mắc bệnh lao phổi (lóng cũ)"),
    ("069574", "mafas", "noun", "/ˈmɑːfəz/", "người và tiếng Mafa ở Cameroon"),
    ("069575", "magnetohydrodynamicses", "noun", "/mæɡˌniːtoʊˌhaɪdroʊdaɪˈnæmɪksɪz/", "từ thủy động lực học chất plasma"),
    ("069576", "marantas", "noun", "/məˈræntəz/", "cây dong riềng cảnh chi Maranta"),
    ("069577", "mestizas", "noun", "/mɛˈstiːzəz/", "nữ người lai Tây Ban Nha và bản địa"),
    ("069578", "misgivings", "noun", "/mɪsˈɡɪvɪŋz/", "nỗi lo âu e ngại nghi ngờ bất an"),
    ("069579", "morones", "noun", "/məˈroʊniz/", "cá vược ôn đới thuộc chi Morone"),
    ("069580", "mukallas", "noun", "/mʊˈkɑːləz/", "thành phố cảng Al-Mukalla ở Yemen"),
    ("069581", "mussier", "adj", "/ˈmʌsiər/", "nhăn nhúm bừa bộn xộc xệch hơn"),
    ("069582", "mussiest", "adj", "/ˈmʌsiɪst/", "nhăn nhúm bừa bộn xộc xệch nhất"),
    ("069583", "myometriums", "noun", "/ˌmaɪoʊˈmiːtriəmz/", "lớp cơ trơn thành tử cung"),
    ("069584", "myrmidones", "noun", "/ˈmɜːrmɪˌdɒniːz/", "thuộc hạ răm rắp tuân lệnh mù quáng"),
    ("069585", "myrmidons", "noun", "/ˈmɜːrmɪdənz/", "lính đánh thuê; tay sai mù quáng"),
    ("069586", "neurosporas", "noun", "/njʊəˈrɒspərəz/", "nấm mốc đỏ bánh mì chi Neurospora"),
    ("069587", "ninurtas", "noun", "/nɪˈnʊərtəz/", "thần chiến tranh Ninurta Lưỡng Hà"),
    ("069588", "odesas", "noun", "/oʊˈdɛsəz/", "thành phố cảng Odessa ở Ukraine"),
    ("069589", "odetses", "noun", "/oʊˈdɛtsɪz/", "nhà viết kịch Mỹ Clifford Odets"),
    ("069590", "opsins", "noun", "/ˈɒpsɪnz/", "protein cảm quang opsin võng mạc"),
    ("069591", "ostreas", "noun", "/ˈɒstriəz/", "hàu biển dẹt thuộc chi Ostrea"),
    ("069592", "outturns", "noun", "/ˈaʊtˌtɜːrnz/", "tổng sản lượng đầu ra thực tế"),
    ("069593", "pennons", "noun", "/ˈpɛnənz/", "cờ hiệu đuôi nheo nhọn đầu giáo"),
    ("069594", "pentothals", "noun", "/ˈpɛntəˌθɔːlz/", "thuốc gây mê tĩnh mạch Pentothal"),
    ("069595", "petrifications", "noun", "/ˌpɛtrɪfɪˈkeɪʃənz/", "quá trình hóa đá thành hóa thạch"),
    ("069596", "phalaropes", "noun", "/ˈfæləˌroʊps/", "chim lội nhỏ phalarope xoay vòng"),
    ("069597", "pianolas", "noun", "/ˌpiːəˈnoʊləz/", "đàn piano tự động chạy cuộn giấy"),
    ("069598", "pilaus", "noun", "/pɪˈlaʊz/", "cơm rang thập cẩm gia vị pilau"),
    ("069599", "pisums", "noun", "/ˈpaɪsəmz/", "cây đậu Hà Lan thuộc chi Pisum"),
    ("069600", "polysemies", "noun", "/ˈpɒlɪˌsiːmiz/", "hiện tượng từ đa nghĩa ngôn ngữ"),
    ("069601", "popularizers", "noun", "/ˈpɒpjələˌraɪzərz/", "người truyền bá phổ cập kiến thức"),
    ("069602", "praetoriums", "noun", "/priːˈtɔːriəmz/", "sở chỉ huy lều tướng La Mã cổ đại"),
]

with open("scratch/b34_r10_raw_p1.json") as f:
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

with open("scratch/b34_r10_p1.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r10_p1.json OK")
