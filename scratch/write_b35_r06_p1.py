import json

items = [
    ("072503", "hawfinches", "noun", "/ˈhɔːˌfɪntʃɪz/", "chim sẻ mỏ to (chuyên cắn hạt)"),
    ("072504", "heartseases", "noun", "/ˈhɑːrtsˌiːzɪz/", "hoa păng-xê tam sắc; sự thanh thản"),
    ("072505", "hydrostaticses", "noun", "/ˌhaɪdrəˈstætɪksɪz/", "ngành thủy tĩnh học"),
    ("072506", "hyoscines", "noun", "/ˈhaɪəsiːnz/", "chất chống say tàu xe scopolamine"),
    ("072507", "hyperemias", "noun", "/ˌhaɪpəˈriːmiəz/", "tình trạng sung huyết cục bộ"),
    ("072508", "inkpots", "noun", "/ˈɪŋkˌpɒts/", "lọ nhỏ đựng mực viết"),
    ("072509", "jaggier", "adj", "/ˈdʒæɡiər/", "gồ ghề lởm chởm răng cưa hơn"),
    ("072510", "jaggiest", "adj", "/ˈdʒæɡiɪst/", "gồ ghề lởm chởm răng cưa nhất"),
    ("072511", "jeths", "noun", "/dʒɛθs/", "tháng Jeth lịch Ấn Độ (tháng 5–6)"),
    ("072512", "kataris", "noun", "/kəˈtɑːriz/", "người dân nước Qatar (biến thể)"),
    ("072513", "laundrymen", "noun", "/ˈlɔːndrɪˌmɛn/", "nhân viên nam làm nghề giặt ủi"),
    ("072514", "locknuts", "noun", "/ˈlɒkˌnʌts/", "đai ốc khóa chống tự tháo"),
    ("072515", "lunarias", "noun", "/luːˈnɛəriəz/", "cây đồng tiền bạc chi Lunaria"),
    ("072516", "maltmans", "noun", "/ˈmɔːltmənz/", "thợ ủ chế biến mạch nha nấu bia"),
    ("072517", "maltos", "noun", "/ˈmɑːltoʊz/", "người dân tộc và tiếng Malto Ấn Độ"),
    ("072518", "mangiferas", "noun", "/mæŋˈɡɪfərəz/", "chi Cây xoài thực vật (Mangifera)"),
    ("072519", "marrowbones", "noun", "/ˈmæroʊˌboʊnz/", "xương ống chứa tủy béo; đầu gối"),
    ("072520", "materialisations", "noun", "/məˌtɪəriəlaɪˈzeɪʃənz/", "sự hiện hình thành vật thể (Anh)"),
    ("072521", "mesmerists", "noun", "/ˈmɛzmərɪsts/", "người thực hành thôi miên cổ điển"),
    ("072522", "microevolutions", "noun", "/ˌmaɪkroʊɪvəˈluːʃənz/", "tiến hóa vi mô trong quần thể"),
    ("072523", "millenarianisms", "noun", "/ˌmɪlɪˈnɛəriəˌnɪzəmz/", "thuyết thiên niên kỷ cứu thế"),
    ("072524", "mioses", "noun", "/maɪˈoʊsiːz/", "chứng co đồng tử mắt; giảm phân"),
    ("072525", "monosomies", "noun", "/ˈmɒnəˌsoʊmiz/", "thể đơn nhiễm (mất một nhiễm sắc)"),
    ("072526", "neotomas", "noun", "/niˈɒtəməz/", "chuột bụi rậm Bắc Mỹ (pack rat)"),
    ("072527", "nervuses", "noun", "/ˈnɜːrvəsɪz/", "dây thần kinh; gân lá (sinh học)"),
    ("072528", "orangeades", "noun", "/ˌɒrɪndʒˈeɪdz/", "nước cam ép pha đường giải khát"),
    ("072529", "outgoes", "verb", "/ˌaʊtˈɡoʊz/", "chi phí tiêu dùng; vượt qua (từ cũ)"),
    ("072530", "parasails", "noun", "/ˈpærəˌseɪlz/", "dù lượn kéo sau ca nô trên biển"),
    ("072531", "pennia", "noun", "/ˈpɛniə/", "đơn vị tiền xu penni cũ Phần Lan"),
    ("072532", "pennis", "noun", "/ˈpɛniz/", "đồng xu penni cũ của Phần Lan"),
    ("072533", "phylacteries", "noun", "/fɪˈlæktəriz/", "hộp kinh đeo lễ Do Thái; bùa hộ"),
    ("072534", "poods", "noun", "/puːdz/", "đơn vị khối lượng pood Nga (~16 kg)"),
    ("072535", "prochlorperazines", "noun", "/proʊˌklɔːrˈpɛrəziːnz/", "thuốc chống nôn prochlorperazine"),
    ("072536", "pterises", "noun", "/ˈtɛrɪsɪz/", "chi Dương xỉ chân chim (Pteris)"),
    ("072537", "ptomaines", "noun", "/ˈtoʊmeɪnz/", "chất amin ptomain do thịt thối rữa"),
    ("072538", "pyrrhotites", "noun", "/ˈpɪrəˌtaɪts/", "khoáng vật sắt sunfua pyrrhotit"),
    ("072539", "raleghs", "noun", "/ˈrɑːliz/", "nhà thám hiểm Anh Walter Raleigh"),
    ("072540", "rastafarianisms", "noun", "/ˌræstəˈfɛəriəˌnɪzəmz/", "phong trào tín ngưỡng Rastafari"),
    ("072541", "retied", "verb", "/riːˈtaɪd/", "đã thắt buộc nút dây lại"),
    ("072542", "reties", "verb", "/riːˈtaɪz/", "thắt buộc lại nút dây hoặc cà vạt"),
    ("072543", "retying", "verb", "/riːˈtaɪɪŋ/", "đang thắt buộc nút dây lại"),
    ("072544", "rugelaches", "noun", "/ˈrʊɡəˌlɑːks/", "bánh sừng bò nhân nho hạt Do Thái"),
    ("072545", "salishans", "noun", "/ˈseɪlɪʃənz/", "người và ngữ hệ Salish Bắc Mỹ"),
    ("072546", "schizosaccharomyceses", "noun", "/ˌskɪzoʊsækərəˈmaɪsiːzɪz/", "chi Nấm men phân đôi sinh học"),
    ("072547", "serigraphs", "noun", "/ˈsɛrɪˌɡræfs/", "tranh in lưới nghệ thuật (in lụa)"),
    ("072548", "serkins", "noun", "/ˈsɜːrkɪnz/", "nghệ sĩ dương cầm Rudolf Serkin"),
    ("072549", "serosas", "noun", "/sɪˈroʊsəz/", "màng thanh mạc bao bọc nội tạng"),
    ("072550", "shelducks", "noun", "/ˈʃɛlˌdʌks/", "vịt khoang vằn Tadorna châu Âu"),
    ("072551", "silversideses", "noun", "/ˈsɪlvərˌsaɪdzɪz/", "cá suốt bạc nhỏ (họ Cá suốt)"),
    ("072552", "sinologists", "noun", "/saɪˈnɒlədʒɪsts/", "nhà Hán học nghiên cứu Trung Hoa"),
    ("072553", "slaveys", "noun", "/ˈslæviz/", "cô hầu gái làm lụng vất vả (Anh cũ)"),
    ("072554", "spikenards", "noun", "/ˈspaɪkˌnɑːrdz/", "cây cam tùng hương; dầu thơm nard"),
    ("072555", "squills", "noun", "/skwɪlz/", "cây hành biển dược liệu; tôm tít"),
    ("072556", "stonecrops", "noun", "/ˈstoʊnˌkrɒps/", "cây sen đá trường sinh Sedum"),
    ("072557", "strivers", "noun", "/ˈstraɪvərz/", "người phấn đấu nỗ lực không ngừng"),
    ("072558", "submucosae", "noun", "/ˌsʌbmjuːˈkoʊsiː/", "lớp mô dưới niêm mạc (giải phẫu)"),
    ("072559", "submucosas", "noun", "/ˌsʌbmjuːˈkoʊsəz/", "lớp mô dưới niêm mạc (giải phẫu)"),
    ("072560", "tagamets", "noun", "/ˈtæɡəmɛts/", "thuốc giảm axit dạ dày Tagamet"),
    ("072561", "thimblefuls", "noun", "/ˈθɪmbəlˌfʊlz/", "lượng rất ít ỏi bằng một đê khâu"),
    ("072562", "tocharians", "noun", "/toʊˈkɛəriənz/", "người và tiếng Thổ Hỏa La cổ đại"),
    ("072563", "transparences", "noun", "/trænˈspɛərənsɪz/", "tính trong suốt; phim dương bản"),
    ("072564", "triazolams", "noun", "/traɪˈæzəˌlæmz/", "thuốc ngủ benzodiazepin triazolam"),
    ("072565", "vicissitudes", "noun", "/vɪˈsɪsɪˌtjuːdz/", "những bước thăng trầm biến cố đời"),
    ("072566", "xizangs", "noun", "/ʃiːˈdzɑːŋz/", "khu tự trị Tây Tạng (tên Hán)"),
    ("072567", "zibs", "noun", "/ˈzɛbɪˌbaɪts/", "đơn vị dữ liệu zebibyte (ZiB)"),
    ("072568", "zoris", "noun", "/ˈzɔːriz/", "dép cói xỏ ngón truyền thống Nhật"),
    ("072569", "abatises", "noun", "/ˈæbətɪsɪz/", "hàng rào chướng ngại cành cây vót"),
    ("072570", "agios", "noun", "/ˈædʒioʊz/", "phí chênh lệch đổi ngoại tệ agio"),
    ("072571", "ammoniacs", "noun", "/əˈmoʊniæks/", "nhựa cây gum ammoniacum (hương)"),
    ("072572", "anaplasmoses", "noun", "/ˌænəplæzˈmoʊsiːz/", "bệnh ký sinh trùng máu gia súc"),
    ("072573", "anglicisations", "noun", "/ˌæŋɡlɪsaɪˈzeɪʃənz/", "sự Anh hóa ngôn ngữ văn hóa (Anh)"),
    ("072574", "anglicizations", "noun", "/ˌæŋɡlɪsaɪˈzeɪʃənz/", "sự Anh hóa ngôn ngữ hay tên gọi"),
    ("072575", "articulators", "noun", "/ɑːrˈtɪkjʊˌleɪtərz/", "cơ quan phát âm; giá khớp nha khoa"),
    ("072576", "arundos", "noun", "/əˈrʌndoʊz/", "cây sậy khổng lồ chi Arundo"),
    ("072577", "balanitides", "noun", "/ˌbælənɪˈtaɪdiːz/", "bệnh viêm quy đầu (y học)"),
    ("072578", "bowfins", "noun", "/ˈboʊˌfɪnz/", "cá vây cung nước ngọt Bắc Mỹ"),
    ("072579", "bumblers", "noun", "/ˈbʌmblərz/", "người vụng về lóng ngóng hay hỏng"),
    ("072580", "caravansaries", "noun", "/ˌkærəˈvænsəriz/", "trạm dừng chân đoàn lạc đà buôn"),
    ("072581", "cenobites", "noun", "/ˈsiːnəˌbaɪts/", "tu sĩ sống tu hành theo cộng đoàn"),
    ("072582", "chamaecyparises", "noun", "/ˌkæmɪˈsɪpərɪsɪz/", "cây hoàng đàn giả Chamaecyparis"),
    ("072583", "chandelled", "verb", "/ʃænˈdɛld/", "đã kéo vọt máy bay lên đổi hướng"),
    ("072584", "chandelles", "noun", "/ʃænˈdɛlz/", "động tác bay vọt xoay 180 độ"),
    ("072585", "chandelling", "verb", "/ʃænˈdɛlɪŋ/", "đang bay vọt đổi hướng 180 độ"),
    ("072586", "chimneypieces", "noun", "/ˈtʃɪmniˌpiːsɪz/", "khung bệ trang trí quanh lò sưởi"),
    ("072587", "cladograms", "noun", "/ˈklædəˌɡræmz/", "biểu đồ nhánh phát sinh chủng loại"),
    ("072588", "clawfoots", "noun", "/ˈklɔːˌfʊts/", "dị tật bàn chân lõm co quắp ngón"),
    ("072589", "cnidarians", "noun", "/naɪˈdɛəriənz/", "động vật ruột khoang thích ty bào"),
    ("072590", "coiffeurs", "noun", "/kwɑːˈfɜːrz/", "thợ làm đầu tạo mẫu tóc (nam)"),
    ("072591", "coltsfoots", "noun", "/ˈkoʊltsˌfʊts/", "cây khoản đông hoa vàng trị ho"),
    ("072592", "conventionalisms", "noun", "/kənˈvɛnʃənəˌlɪzəmz/", "lối suy nghĩ khuôn sáo ước lệ"),
    ("072593", "damselfishes", "noun", "/ˈdæmzəlˌfɪʃɪz/", "cá thia rạn san hô màu sặc sỡ"),
    ("072594", "decapodas", "noun", "/dɪˈkæpədəz/", "bộ Mười chân (tôm, cua, mực ống)"),
    ("072595", "decolletages", "noun", "/ˌdeɪkɒlˈtɑːʒɪz/", "đường cổ áo trễ sâu hở vai ngực"),
    ("072596", "degreased", "verb", "/diːˈɡriːst/", "đã tẩy sạch lớp dầu mỡ bám"),
    ("072597", "degreases", "verb", "/diːˈɡriːsɪz/", "tẩy sạch dầu mỡ trên bề mặt"),
    ("072598", "degreasing", "verb", "/diːˈɡriːsɪŋ/", "đang tẩy sạch lớp dầu mỡ"),
    ("072599", "dermatoses", "noun", "/ˌdɜːrməˈtoʊsiːz/", "bệnh lý ngoài da nói chung"),
    ("072600", "didriksons", "noun", "/ˈdɪdrɪksənz/", "nữ vận động viên Babe Didrikson"),
    ("072601", "disseminators", "noun", "/dɪˈsɛmɪˌneɪtərz/", "người hoặc vật truyền bá gieo rắc"),
    ("072602", "dkms", "noun", "/ˈdɛkəˌmiːtərz/", "đơn vị đo độ dài đề-ca-mét (10 m)"),
]

with open("scratch/b35_r06_raw_p1.json") as f:
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

with open("scratch/b35_r06_p1.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r06_p1.json OK")
