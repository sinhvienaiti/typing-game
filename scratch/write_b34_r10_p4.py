import json

items = [
    ("069803", "bushwhackers", "noun", "/ˈbʊʃˌwækərz/", "lính du kích phục kích trong rừng"),
    ("069804", "candlewoods", "noun", "/ˈkændəlˌwʊdz/", "cây gỗ nhiều nhựa dùng làm đuốc"),
    ("069805", "canvasbacks", "noun", "/ˈkænvəsˌbæks/", "vịt lưng trắng đầu hung Bắc Mỹ"),
    ("069806", "caricas", "noun", "/ˈkærɪkəz/", "cây đu đủ thuộc chi Carica"),
    ("069807", "cayuses", "noun", "/kaɪˈjuːsɪz/", "ngựa nhỏ hoang dã miền Tây Mỹ"),
    ("069808", "centaureas", "noun", "/sɛnˈtɔːriəz/", "hoa thanh cúc thuộc chi Centaurea"),
    ("069809", "chalcises", "noun", "/ˈkælsɪsɪz/", "ong ký sinh nhỏ thuộc chi Chalcis"),
    ("069810", "chironomidaes", "noun", "/ˌkaɪrəˈnɒmɪdiːz/", "họ muỗi lắc không đốt Chironomidae"),
    ("069811", "chlamydomonases", "noun", "/ˌklæmɪdəˈmoʊnəsɪz/", "tảo lục đơn bào hai roi roi bơi"),
    ("069812", "cimabues", "noun", "/tʃiːˈmɑːbweɪz/", "họa sĩ Phục Hưng Ý Cimabue"),
    ("069813", "clypei", "noun", "/ˈklɪpiaɪ/", "mảnh môi trên côn trùng; khiên tròn"),
    ("069814", "clypeuses", "noun", "/ˈklɪpiəsɪz/", "tấm giáp đầu miệng côn trùng"),
    ("069815", "cognisances", "noun", "/ˈkɒɡnɪzənsɪz/", "sự nhận thức; quyền xét xử"),
    ("069816", "cogwheels", "noun", "/ˈkɒɡˌwiːlz/", "bánh xe có răng ăn khớp truyền lực"),
    ("069817", "cohoshes", "noun", "/ˈkoʊhɒʃɪz/", "cây thiên ma thảo dược Bắc Mỹ"),
    ("069818", "cosmographies", "noun", "/kɒzˈmɒɡrəfiz/", "vũ trụ chí mô tả thiên văn địa lý"),
    ("069819", "counteractions", "noun", "/ˈkaʊntərˌækʃənz/", "hành động đối kháng vô hiệu hóa"),
    ("069820", "crossbeams", "noun", "/ˈkrɒsˌbiːmz/", "xà ngang đỡ mái nối hai cột tường"),
    ("069821", "cycloramas", "noun", "/ˌsaɪkləˈrɑːməz/", "tranh toàn cảnh 360 độ; phông cong"),
    ("069822", "defoliants", "noun", "/diːˈfoʊliənts/", "chất hóa học làm rụng lá cây"),
    ("069823", "dehumanisations", "noun", "/diːˌhjuːmənaɪˈzeɪʃənz/", "sự phi nhân tính hóa tàn nhẫn"),
    ("069824", "deodars", "noun", "/ˈdiːəˌdɑːrz/", "cây tuyết tùng Himalaya deodar"),
    ("069825", "deutschmarks", "noun", "/ˈdɔɪtʃˌmɑːrks/", "đồng tiền cũ Mark Đức (DM)"),
    ("069826", "didacticisms", "noun", "/daɪˈdæktɪˌsɪzəmz/", "lối văn nặng tính giáo huấn răn dạy"),
    ("069827", "dyspnoeas", "noun", "/dɪspˈniːəz/", "tình trạng khó thở hụt hơi (Anh)"),
    ("069828", "earplugs", "noun", "/ˈɪərˌplʌɡz/", "nút bịt tai chống ồn hoặc chắn nước"),
    ("069829", "emendations", "noun", "/ˌiːmɛnˈdeɪʃənz/", "sự hiệu đính sửa lỗi bản thảo"),
    ("069830", "euonymi", "noun", "/juːˈɒnɪmaɪ/", "cây đỗ trọng cảnh chi Euonymus"),
    ("069831", "fiddleheads", "noun", "/ˈfɪdəlˌhɛdz/", "chồi lá dương xỉ cuộn non ăn được"),
    ("069832", "flitches", "noun", "/ˈflɪtʃɪz/", "tảng thịt ba rọi muối xông khói"),
    ("069833", "forfended", "verb", "/fɔːrˈfɛndɪd/", "đã ngăn ngừa phòng tránh (từ cổ)"),
    ("069834", "forfending", "verb", "/fɔːrˈfɛndɪŋ/", "đang ngăn chặn bảo vệ tránh khỏi"),
    ("069835", "forfends", "verb", "/fɔːrˈfɛndz/", "ngăn ngừa bảo vệ khỏi điều xấu (cổ)"),
    ("069836", "fourpences", "noun", "/ˈfɔːrpənsɪz/", "đồng tiền xu bốn xu cổ nước Anh"),
    ("069837", "fusils", "noun", "/ˈfjuːzəlz/", "súng hỏa mai đá lửa nòng nhẹ xưa"),
    ("069838", "gaddis", "noun", "/ˈɡɑːdiz/", "ngai nệm Ấn Độ; dân tộc Gaddi"),
    ("069839", "gentianas", "noun", "/ˌdʒɛnʃiˈeɪnəz/", "hoa long đởm thảo chi Gentiana"),
    ("069840", "goethites", "noun", "/ˈɡɜːrˌtaɪts/", "khoáng vật quặng sắt oxit goethit"),
    ("069841", "grandnieces", "noun", "/ˈɡrændˌniːsɪz/", "cháu gái gọi bằng ông bà cô chú"),
    ("069842", "grevilleas", "noun", "/ɡrəˈvɪliəz/", "cây ngân hoa Úc thuộc chi Grevillea"),
    ("069843", "hemiplegics", "noun", "/ˌhɛmɪˈpliːdʒɪks/", "bệnh nhân bị liệt nửa thân người"),
    ("069844", "heteroses", "noun", "/ˌhɛtəˈroʊsiːz/", "hiện tượng ưu thế con lai F1"),
    ("069845", "honkeys", "noun", "/ˈhɒŋkiz/", "người da trắng (từ lóng miệt thị)"),
    ("069846", "hyraces", "noun", "/ˈhaɪrəsiːz/", "thú nhỏ đa man sống hốc đá châu Phi"),
    ("069847", "hyraxes", "noun", "/ˈhaɪræksɪz/", "con đa man giống chuột đá châu Phi"),
    ("069848", "inchworms", "noun", "/ˈɪntʃˌwɜːrmz/", "sâu đo bò uốn cong từng bước"),
    ("069849", "indiamans", "noun", "/ˈɪndiəmənz/", "tàu buồm lớn đi tuyến Đông Ấn xưa"),
    ("069850", "inhabitations", "noun", "/ɪnˌhæbɪˈteɪʃənz/", "sự cư trú sinh sống tại nơi nào"),
    ("069851", "interahamwes", "noun", "/ˌɪntərəˈhɑːmweɪz/", "dân quân Interahamwe ở Rwanda"),
    ("069852", "isotropies", "noun", "/aɪˈsɒtrəpiz/", "tính đẳng hướng đồng nhất mọi chiều"),
    ("069853", "javelinas", "noun", "/ˌhɑːvəˈliːnəz/", "lợn lòi peccary hoang dã Bắc Mỹ"),
    ("069854", "laagers", "noun", "/ˈlɑːɡərz/", "trại phòng thủ vòng tròn xe ngựa"),
    ("069855", "landsteiners", "noun", "/ˈlændˌstaɪnərz/", "nhà sinh học phát hiện nhóm máu"),
    ("069856", "manichaeisms", "noun", "/ˌmænɪˈkiːɪzəmz/", "đạo Mani nhị nguyên thiện ác cổ đại"),
    ("069857", "mazamas", "noun", "/məˈzɑːməz/", "hươu lùn Nam Mỹ thuộc chi Mazama"),
    ("069858", "mebendazoles", "noun", "/məˈbɛndəˌzoʊlz/", "thuốc tẩy giun phổ rộng mebendazol"),
    ("069859", "metalanguages", "noun", "/ˈmɛtəˌlæŋɡwɪdʒɪz/", "siêu ngôn ngữ dùng mô tả ngôn ngữ"),
    ("069860", "minesweepings", "noun", "/ˈmaɪnˌswiːpɪŋz/", "hoạt động rà phá gỡ thủy lôi mìn"),
    ("069861", "miniaturized", "verb", "/ˈmɪniətʃəˌraɪzd/", "đã thu nhỏ kích thước vi mạch"),
    ("069862", "miniaturizes", "verb", "/ˈmɪniətʃəˌraɪzɪz/", "thu nhỏ kích thước thiết bị"),
    ("069863", "miniaturizing", "verb", "/ˈmɪniətʃəˌraɪzɪŋ/", "đang thu nhỏ tối đa kích thước"),
    ("069864", "neandertals", "noun", "/niˈændərtɑːlz/", "người tiền sử Neanderthal cổ đại"),
    ("069865", "nonagenarians", "noun", "/ˌnɒnədʒəˈnɛəriənz/", "cụ già ở độ tuổi từ 90 đến 99"),
    ("069866", "norias", "noun", "/ˈnɔːriəz/", "guồng cọn nước quay lấy nước tưới"),
    ("069867", "nynorsks", "noun", "/ˈniːnɔːrsks/", "tiếng Na Uy chuẩn viết Nynorsk"),
    ("069868", "oldtimers", "noun", "/ˈoʊldˌtaɪmərz/", "người kỳ cựu lão thành gắn bó lâu"),
    ("069869", "olecranons", "noun", "/oʊˈlɛkrənɒnz/", "mỏm khuỷu nhô ra ở đầu xương trụ"),
    ("069870", "onrushes", "noun", "/ˈɒnˌrʌʃɪz/", "làn sóng lao tới ồ ạt dữ dội"),
    ("069871", "ophidians", "noun", "/oʊˈfɪdiənz/", "loài rắn bò sát không chân"),
    ("069872", "osteomalacias", "noun", "/ˌɒstioʊməˈleɪʃəz/", "bệnh nhuyễn mềm xương thiếu vitamin"),
    ("069873", "packrats", "noun", "/ˈpækˌræts/", "chuột rừng gom đồ; người tích trữ"),
    ("069874", "parsees", "noun", "/ˈpɑːrsiz/", "người theo Hỏa giáo Parsi ở Ấn Độ"),
    ("069875", "peaceniks", "noun", "/ˈpiːsnɪks/", "người hoạt động phản chiến hòa bình"),
    ("069876", "phenolphthaleins", "noun", "/ˌfiːnɒlˈθeɪliːnz/", "chất chỉ thị pH phenolphtalein"),
    ("069877", "pintados", "noun", "/pɪnˈtɑːdoʊz/", "cá thu chấm Tây Ban Nha; gà sao"),
    ("069878", "plesiosaurs", "noun", "/ˈpliːziəˌsɔːrz/", "bò sát biển cổ dài kỷ Jura"),
    ("069879", "polydactylies", "noun", "/ˌpɒliˈdæktɪliz/", "dị tật bẩm sinh thừa ngón tay chân"),
    ("069880", "popovers", "noun", "/ˈpɒpˌoʊvərz/", "bánh nướng trứng rỗng ruột phồng to"),
    ("069881", "postulants", "noun", "/ˈpɒstjʊlənts/", "người thỉnh sinh xin nhập dòng tu"),
    ("069882", "prazosins", "noun", "/ˈpreɪzəˌsɪnz/", "thuốc giãn mạch hạ áp prazosin"),
    ("069883", "presentisms", "noun", "/ˈprɛzənˌtɪzəmz/", "thuyết hiện tại luận triết học sử"),
    ("069884", "provoses", "noun", "/ˈproʊvoʊz/", "Quân đội Cộng hòa Ireland lâm thời"),
    ("069885", "psalteries", "noun", "/ˈsɔːltəriz/", "đàn gảy dây tam giác thời trung cổ"),
    ("069886", "ranees", "noun", "/ˈrɑːniz/", "nữ hoàng hoặc công chúa Ấn Độ xưa"),
    ("069887", "regularisations", "noun", "/ˌrɛɡjʊləraɪˈzeɪʃənz/", "sự chính quy hóa; hợp thức hóa"),
    ("069888", "renascences", "noun", "/rɪˈneɪsənsɪz/", "sự hồi sinh phục hưng văn hóa mới"),
    ("069889", "reprobations", "noun", "/ˌrɛprəˈbeɪʃənz/", "sự lên án kịch liệt; sự ruồng bỏ"),
    ("069890", "richlers", "noun", "/ˈrɪtʃlərz/", "nhà văn Canada Mordecai Richler"),
    ("069891", "rimus", "noun", "/ˈriːmuːz/", "cây gỗ thông rimu New Zealand"),
    ("069892", "rotogravures", "noun", "/ˌroʊtoʊɡrəˈvjʊərz/", "kỹ thuật in ống đồng tốc độ cao"),
    ("069893", "rustbelts", "noun", "/ˈrʌstˌbɛlts/", "vùng công nghiệp cũ Rust Belt"),
    ("069894", "salmagundis", "noun", "/ˌsælməˈɡʌndiz/", "món trộn thập cẩm truyền thống Anh"),
    ("069895", "shmucks", "noun", "/ʃmʌks/", "kẻ ngốc nghếch khờ dại (từ lóng)"),
    ("069896", "sircs", "noun", "/ˌɛs aɪ ɑːr ˈsiːz/", "Ủy ban Giám sát Tình báo Canada"),
    ("069897", "slanderers", "noun", "/ˈslɑːndərərz/", "kẻ đặt điều vu khống bôi nhọ người"),
    ("069898", "souchongs", "noun", "/ˈsuːˌʃɒŋz/", "trà đen lá lớn hun khói Lapsang"),
    ("069899", "spirographs", "noun", "/ˈspaɪrəˌɡræfs/", "phế dung kế ghi đồ thị hô hấp"),
    ("069900", "srbijas", "noun", "/ˈsɜːrbiəz/", "nước Cộng hòa Serbia (tên bản địa)"),
    ("069901", "standees", "noun", "/stænˈdiːz/", "hành khách đứng vì hết chỗ ngồi"),
    ("069902", "stockpots", "noun", "/ˈstɒkˌpɒts/", "nồi cao thành hầm nước dùng xương"),
]

with open("scratch/b34_r10_raw_p4.json") as f:
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

with open("scratch/b34_r10_p4.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r10_p4.json OK")
