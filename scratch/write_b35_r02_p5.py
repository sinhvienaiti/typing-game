import json

items = [
    ("070903", "bromating", "verb", "/ˈbroʊmeɪtɪŋ/", "đang xử lý phản ứng bằng brom"),
    ("070904", "budgerigars", "noun", "/ˈbʌdʒərɪˌɡɑːrz/", "vẹt cảnh Úc yến phụng budgie"),
    ("070905", "cardiums", "noun", "/ˈkɑːrdiəmz/", "chi Sò tim biển Cardium"),
    ("070906", "cataloguers", "noun", "/ˈkætəˌlɒɡərz/", "người biên mục lập danh mục sách"),
    ("070907", "centrefolds", "noun", "/ˈsɛntərˌfoʊldz/", "trang ảnh gập giữa tạp chí (Anh)"),
    ("070908", "chahtas", "noun", "/ˈtʃɑːtəz/", "dân tộc và tiếng Choctaw (Chahta)"),
    ("070909", "chittered", "verb", "/ˈtʃɪtərd/", "đã hót ríu rít; đã run cầm cập"),
    ("070910", "chittering", "verb", "/ˈtʃɪtərɪŋ/", "đang hót ríu rít; run cầm cập"),
    ("070911", "chitters", "verb", "/ˈtʃɪtərz/", "hót ríu rít; run lẩy bẩy"),
    ("070912", "cladisticses", "noun", "/kləˈdɪstɪksɪz/", "phương pháp phân loại nhánh học"),
    ("070913", "clavuses", "noun", "/ˈkleɪvəsɪz/", "mắt cá chai chân; cục u chai da"),
    ("070914", "coarctations", "noun", "/ˌkoʊɑːrkˈteɪʃənz/", "sự hẹp khít động mạch; sự co thắt"),
    ("070915", "cobbers", "noun", "/ˈkɒbərz/", "bạn thân chí cốt (tiếng lóng Úc)"),
    ("070916", "crosshatches", "noun", "/ˈkrɒsˌhætʃɪz/", "nét gạch bóng đan chéo nhau"),
    ("070917", "crosshatching", "verb", "/ˈkrɒsˌhætʃɪŋ/", "đang vẽ nét gạch bóng đan chéo"),
    ("070918", "cryptologists", "noun", "/krɪpˈtɒlədʒɪsts/", "nhà mật mã học và giải mã"),
    ("070919", "dalbergias", "noun", "/dælˈbɜːrdʒiəz/", "cây gỗ trắc cẩm lai chi Dalbergia"),
    ("070920", "decubiti", "noun", "/dɪˈkjuːbɪˌtaɪ/", "loét tỳ đè (do nằm lâu); tư thế nằm"),
    ("070921", "desponded", "verb", "/dɪˈspɒndɪd/", "đã chán nản ngã lòng tuyệt vọng"),
    ("070922", "desponding", "verb", "/dɪˈspɒndɪŋ/", "đang chán nản ngã lòng tuyệt vọng"),
    ("070923", "desponds", "verb", "/dɪˈspɒndz/", "chán nản ngã lòng tuyệt vọng"),
    ("070924", "desquamations", "noun", "/ˌdɛskwəˈmeɪʃənz/", "hiện tượng bong tróc vảy lớp da"),
    ("070925", "diencephalons", "noun", "/ˌdaɪɛnˈsɛfəlɒnz/", "não trung gian (gian não)"),
    ("070926", "diospyroses", "noun", "/ˌdaɪɒˈspɪrəsɪz/", "cây thị hồng mun chi Diospyros"),
    ("070927", "discussants", "noun", "/dɪˈskʌsənts/", "người tham gia thảo luận phản biện"),
    ("070928", "dishpans", "noun", "/ˈdɪʃˌpænz/", "chậu rửa chén bát (Mỹ)"),
    ("070929", "dockworkers", "noun", "/ˈdɒkˌwɜːrkərz/", "công nhân bốc xếp khuân vác cảng"),
    ("070930", "economizers", "noun", "/ɪˈkɒnəˌmaɪzərz/", "bộ tiết kiệm nhiệt; người tiết kiệm"),
    ("070931", "endarterectomies", "noun", "/ˌɛndɑːrtəˈrɛktəmiz/", "phẫu thuật bóc nội mạc động mạch"),
    ("070932", "excrescences", "noun", "/ɪkˈskrɛsənsɪz/", "mụn lồi dư thừa; u sùi phát triển"),
    ("070933", "footednesses", "noun", "/ˈfʊtɪdnəsɪz/", "tính thuận chân trái hoặc phải"),
    ("070934", "formicidaes", "noun", "/fɔːrˈmɪsɪdiːz/", "họ Kiến trong bộ Cánh màng"),
    ("070935", "gasbags", "noun", "/ˈɡæsˌbæɡz/", "kẻ nói dóc ba hoa; túi chứa khí"),
    ("070936", "geomancers", "noun", "/ˈdʒiːoʊˌmænsərz/", "thầy địa lý phong thủy; nhà bói đất"),
    ("070937", "geriatricians", "noun", "/ˌdʒɛriəˈtrɪʃənz/", "bác sĩ chuyên khoa lão khoa"),
    ("070938", "gibberellins", "noun", "/ˌdʒɪbəˈrɛlɪnz/", "hoóc-môn sinh trưởng thực vật GA"),
    ("070939", "glossae", "noun", "/ˈɡlɒsiː/", "lưỡi côn trùng; chú giải văn bản"),
    ("070940", "glossas", "noun", "/ˈɡlɒsəz/", "lưỡi (động vật); lời chú giải"),
    ("070941", "groschens", "noun", "/ˈɡroʊʃənz/", "đồng xu groschen (Áo và Đức cũ)"),
    ("070942", "hasids", "noun", "/ˈhæsɪdz/", "tín đồ Do Thái giáo Hasid"),
    ("070943", "hatbands", "noun", "/ˈhætˌbændz/", "dải ruy-băng quấn quanh vành mũ"),
    ("070944", "horseboxes", "noun", "/ˈhɔːrsˌbɒksɪz/", "toa xe chuyên chở ngựa (Anh)"),
    ("070945", "humectants", "noun", "/hjuːˈmɛktənts/", "chất giữ ẩm hút ẩm (mỹ phẩm)"),
    ("070946", "hydatids", "noun", "/ˈhaɪdətɪdz/", "nang sán nước echinococcus (y học)"),
    ("070947", "jillions", "noun", "/ˈdʒɪljənz/", "vô số kể; hàng tỷ tỷ (khẩu ngữ)"),
    ("070948", "kampucheans", "noun", "/ˌkæmpʊˈtʃiːənz/", "người dân Campuchia (tên cũ)"),
    ("070949", "kinetoscopes", "noun", "/kɪˈniːtəˌskoʊps/", "máy chiếu phim sớm Kinetoscope"),
    ("070950", "lavaliers", "noun", "/ˌlævəˈlɪərz/", "mặt dây chuyền; micro cài áo"),
    ("070951", "leopoldvilles", "noun", "/ˈliːəpoʊldˌvɪlz/", "Kinshasa (tên cũ Léopoldville)"),
    ("070952", "lepidopterans", "noun", "/ˌlɛpɪˈdɒptərənz/", "côn trùng bộ Cánh vảy (bướm ngài)"),
    ("070953", "liftgates", "noun", "/ˈlɪftˌɡeɪts/", "cửa cốp sau mở hất lên của ô tô"),
    ("070954", "loofas", "noun", "/ˈluːfəz/", "xơ mướp tự nhiên để tắm chà rửa"),
    ("070955", "mahonias", "noun", "/məˈhoʊniəz/", "cây bụi hoàng liên gai lá nhọn"),
    ("070956", "malefactors", "noun", "/ˈmælɪˌfæktərz/", "kẻ phạm tội ác; kẻ làm điều xấu"),
    ("070957", "mantlets", "noun", "/ˈmæntləts/", "lá chắn gỗ di động che đạn tên"),
    ("070958", "nidaroses", "noun", "/ˈnɪdərɒsɪz/", "thành phố Trondheim cổ (Nidaros)"),
    ("070959", "ornithopters", "noun", "/ɔːrˈnɪθɒptərz/", "máy bay vỗ cánh như chim"),
    ("070960", "orthophosphates", "noun", "/ˌɔːrθoʊˈfɒsfeɪts/", "muối hoặc este orthophotphat"),
    ("070961", "pedagogicses", "noun", "/ˌpɛdəˈɡɒdʒɪksɪz/", "ngành khoa học sư phạm giảng dạy"),
    ("070962", "pepcids", "noun", "/ˈpɛpsɪdz/", "thuốc kháng axit dạ dày Pepcid"),
    ("070963", "perambulations", "noun", "/pəˌræmbjʊˈleɪʃənz/", "cuộc đi dạo thị sát; sự đi tuần"),
    ("070964", "phalloplasties", "noun", "/ˈfæləˌplæstiz/", "phẫu thuật tạo hình dương vật"),
    ("070965", "phocas", "noun", "/ˈfoʊkəz/", "chi Hải cẩu thật sự (Phoca)"),
    ("070966", "plowshares", "noun", "/ˈplaʊˌʃɛərz/", "lưỡi cày lật đất nông nghiệp"),
    ("070967", "polynucleotides", "noun", "/ˌpɒlɪˈnjuːkliəˌtaɪdz/", "chuỗi phân tử polynucleotide"),
    ("070968", "potages", "noun", "/poʊˈtɑːʒɪz/", "món súp đặc hầm rau thịt (Pháp)"),
    ("070969", "puppises", "noun", "/ˈpʌpɪsɪz/", "chòm sao Thuyền Vĩ trên bầu trời"),
    ("070970", "randomisations", "noun", "/ˌrændəmaɪˈzeɪʃənz/", "sự ngẫu nhiên hóa thí nghiệm (Anh)"),
    ("070971", "rectorships", "noun", "/ˈrɛktərʃɪps/", "chức vụ hiệu trưởng; chức cha xứ"),
    ("070972", "rediffusions", "noun", "/ˌriːdɪˈfjuːʒənz/", "hệ thống tiếp sóng truyền lại"),
    ("070973", "revelers", "noun", "/ˈrɛvələrz/", "người tiệc tùng vui chơi ồn ào (Mỹ)"),
    ("070974", "revellers", "noun", "/ˈrɛvələrz/", "người tiệc tùng vui chơi ồn ào"),
    ("070975", "robinias", "noun", "/roʊˈbɪniəz/", "cây dương hòe thuộc chi Robinia"),
    ("070976", "saccharides", "noun", "/ˈsækəˌraɪdz/", "hợp chất đường bột saccarit"),
    ("070977", "secretins", "noun", "/sɪˈkriːtɪnz/", "hoóc-môn tiêu hóa secretin"),
    ("070978", "sexploitations", "noun", "/ˌsɛksplɔɪˈteɪʃənz/", "sự trục lợi thương mại từ tình dục"),
    ("070979", "shoreas", "noun", "/ˈʃɔːriəz/", "cây gỗ nhiệt đới chi Shorea"),
    ("070980", "sinusoids", "noun", "/ˈsaɪnəˌsɔɪdz/", "đồ thị hình sin; xoang mao mạch"),
    ("070981", "snakeroots", "noun", "/ˈsneɪkˌruːts/", "cây thảo dược rễ trị rắn cắn"),
    ("070982", "teniae", "noun", "/ˈtiːniˌiː/", "băng buộc đầu cổ Hy Lạp; sán dây"),
    ("070983", "tenias", "noun", "/ˈtiːniəz/", "băng buộc đầu cổ đại; sán dây"),
    ("070984", "thyroglobulins", "noun", "/ˌθaɪroʊˈɡlɒbjʊlɪnz/", "protein tuyến giáp thyroglobulin"),
    ("070985", "triiodothyronines", "noun", "/ˌtraɪaɪˌoʊdoʊˈθaɪrəniːnz/", "hoóc-môn tuyến giáp T3"),
    ("070986", "ullages", "noun", "/ˈʌlɪdʒɪz/", "phần vơi hụt chất lỏng trong thùng"),
    ("070987", "veeries", "noun", "/ˈvɪəriz/", "chim hoét nâu châu Mỹ veery"),
    ("070988", "vizcainos", "noun", "/vɪzˈkaɪnoʊz/", "nhà thám hiểm Sebastián Vizcaíno"),
    ("070989", "waterbucks", "noun", "/ˈwɔːtərˌbʌks/", "linh dương nước châu Phi waterbuck"),
    ("070990", "waterpowers", "noun", "/ˈwɔːtərˌpaʊərz/", "thủy năng; sức nước phát điện"),
    ("070991", "yevtushenkos", "noun", "/ˌjɛftʊˈʃɛŋkoʊz/", "nhà thơ Nga Yevgeny Yevtushenko"),
    ("070992", "zosteras", "noun", "/zɒˈstɪərəz/", "cỏ lươn biển thuộc chi Zostera"),
    ("070993", "aglaias", "noun", "/əˈɡlaɪəz/", "nữ thần duyên dáng Aglaia Hy Lạp"),
    ("070994", "aguacates", "noun", "/ˌɑːɡwəˈkɑːteɪz/", "quả bơ (tên tiếng Tây Ban Nha)"),
    ("070995", "alstroemerias", "noun", "/ˌælstrəˈmɪəriəz/", "hoa thủy tiên Peru (Alstroemeria)"),
    ("070996", "amenias", "noun", "/əˈmiːniəz/", "chứng vô kinh (mất kinh nguyệt)"),
    ("070997", "anovulations", "noun", "/ænˌɒvjʊˈleɪʃənz/", "tình trạng không rụng trứng"),
    ("070998", "appreciators", "noun", "/əˈpriːʃiˌeɪtərz/", "người biết trân trọng đánh giá cao"),
    ("070999", "athabaskans", "noun", "/ˌæθəˈbæskənz/", "người và ngữ hệ Athabaska Bắc Mỹ"),
    ("071000", "axiologies", "noun", "/ˌæksiˈɒlədʒiz/", "triết học giá trị luận (tiên đề)"),
    ("071001", "bestowers", "noun", "/bɪˈstoʊərz/", "người ban tặng trao cho ân huệ"),
    ("071002", "bonemeals", "noun", "/ˈboʊnˌmiːlz/", "bột xương nghiền làm phân bón"),
]

with open("scratch/b35_r02_raw_p5.json") as f:
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

with open("scratch/b35_r02_p5.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r02_p5.json OK")
