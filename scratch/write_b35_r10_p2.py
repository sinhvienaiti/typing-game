import json

rows = [
    ("074603", "bloodmobiles", "noun", "/ˈblʌdmoʊˌbiːlz/", "xe thu gom máu di động"),
    ("074604", "bonesets", "noun", "/ˈboʊnsɛts/", "cây trạch lan nối xương (dược liệu)"),
    ("074605", "bribers", "noun", "/ˈbraɪbərz/", "người hối lộ; kẻ đút lót"),
    ("074606", "broadbills", "noun", "/ˈbrɔːdbɪlz/", "chim mỏ rộng; vịt mỏ thìa; cá kiếm"),
    ("074607", "brobdingnags", "noun", "/ˈbrɒbdɪŋnæɡz/", "xứ người khổng lồ Brobdingnag"),
    ("074608", "bubaluses", "noun", "/ˈbjuːbələsɪz/", "chi trâu châu Á (Bubalus)"),
    ("074609", "butanones", "noun", "/ˈbjuːtənoʊnz/", "dung môi butanon (MEK)"),
    ("074610", "caitiffs", "noun", "/ˈkeɪtɪfs/", "kẻ hèn hạ đê tiện (cổ)"),
    ("074611", "catharis", "noun", "/ˈkæθəraɪ/", "tín đồ giáo phái Cathar"),
    ("074612", "chelonians", "noun", "/kɪˈloʊniənz/", "loài rùa (bộ Rùa)"),
    ("074613", "compliancies", "noun", "/kəmˈplaɪənsiz/", "tính dễ phục tùng; sự tuân thủ"),
    ("074614", "conceptuses", "noun", "/kənˈsɛptəsɪz/", "phôi thai; bào thai (y học)"),
    ("074615", "countercoups", "noun", "/ˈkaʊntərˌkuːz/", "chấn thương đối lực; phản đảo chính"),
    ("074616", "cowcatchers", "noun", "/ˈkaʊˌkætʃərz/", "thanh gạt chướng ngại đầu tàu hỏa"),
    ("074617", "cracksmans", "noun", "/ˈkræksmənz/", "kẻ phá két sắt; đạo chích chuyên"),
    ("074618", "crepises", "noun", "/ˈkrɛpɪsiːz/", "chi cây diếp vàng (Crepis)"),
    ("074619", "cuneuses", "noun", "/ˈkjuːniəsɪz/", "thùy chêm vỏ não (cuneus)"),
    ("074620", "decagons", "noun", "/ˈdɛkəɡɒnz/", "hình mười cạnh; hình thập giác"),
    ("074621", "decalcifications", "noun", "/diːˌkælsɪfɪˈkeɪʃənz/", "sự khử canxi; mất canxi xương"),
    ("074622", "depersonalized", "verb", "/diːˈpɜːrsənəlaɪzd/", "đã phi nhân cách hóa; mất bản sắc"),
    ("074623", "depersonalizes", "verb", "/diːˈpɜːrsənəlaɪzɪz/", "phi nhân cách hóa; làm mất bản sắc"),
    ("074624", "depersonalizing", "verb", "/diːˈpɜːrsənəlaɪzɪŋ/", "phi nhân cách hóa; làm mất bản sắc"),
    ("074625", "dermacentors", "noun", "/ˌdɜːrməˈsɛntərz/", "chi ve chó Dermacentor"),
    ("074626", "despoilers", "noun", "/dɪˈspɔɪlərz/", "kẻ cướp bóc tàn phá"),
    ("074627", "dragonets", "noun", "/ˈdræɡənɪts/", "cá đàn lia (họ Callionymidae)"),
    ("074628", "duettes", "noun", "/duːˈɛts/", "bài song ca; bản song tấu (nữ)"),
    ("074629", "ectopias", "noun", "/ɛkˈtoʊpiəz/", "chứng lạc chỗ (y học)"),
    ("074630", "emplaced", "verb", "/ɪmˈpleɪst/", "đã đặt vào vị trí (pháo, quân)"),
    ("074631", "emplaces", "verb", "/ɪmˈpleɪsɪz/", "đặt vào vị trí (pháo, quân)"),
    ("074632", "emplacing", "verb", "/ɪmˈpleɪsɪŋ/", "đặt vào vị trí (pháo, quân)"),
    ("074633", "exenterations", "noun", "/ɛkˌsɛntəˈreɪʃənz/", "phẫu thuật nạo vét tạng (y học)"),
    ("074634", "exostoses", "noun", "/ˌɛksɒsˈtoʊsiːz/", "gai xương; u xương lành tính"),
    ("074635", "exotoxins", "noun", "/ˌɛksoʊˈtɒksɪnz/", "ngoại độc tố (vi khuẩn)"),
    ("074636", "filarias", "noun", "/fɪˈlɛriəz/", "giun chỉ ký sinh (Filaria)"),
    ("074637", "filariiae", "noun", "/fɪˈlɛriːiː/", "giun chỉ ký sinh (Filaria)"),
    ("074638", "fosterages", "noun", "/ˈfɒstərɪdʒɪz/", "chế độ gửi con nuôi (cổ)"),
    ("074639", "galantines", "noun", "/ˈɡælənˌtiːnz/", "món thịt cuộn nguội galantine"),
    ("074640", "glises", "noun", "/ˈɡlaɪsɪz/", "chi chuột sóc (Glis)"),
    ("074641", "hagiographers", "noun", "/ˌhæɡiˈɒɡrəfərz/", "người viết truyện thánh; ca tụng"),
    ("074642", "haliaeetuses", "noun", "/ˌhæliˈiːtəsɪz/", "chi đại bàng biển (Haliaeetus)"),
    ("074643", "handclasps", "noun", "/ˈhændklæsps/", "cái bắt tay chặt; sự nắm tay"),
    ("074644", "hasheeshes", "noun", "/hæˈʃiːʃɪz/", "nhựa cần sa; bột hashish"),
    ("074645", "hecatombs", "noun", "/ˈhɛkətoʊmz/", "lễ hiến tế lớn; vụ thảm sát lớn"),
    ("074646", "heleniums", "noun", "/hɪˈliːniəmz/", "chi cúc hắt xì (Helenium)"),
    ("074647", "hemolysins", "noun", "/hɪˈmɒlɪsɪnz/", "chất dung huyết (gây tan máu)"),
    ("074648", "highflyers", "noun", "/ˌhaɪˈflaɪərz/", "người tham vọng và thành đạt cao"),
    ("074649", "hornworts", "noun", "/ˈhɔːrnwɜːrts/", "rêu sừng; cây rong đuôi chó"),
    ("074650", "ictaluruses", "noun", "/ˌɪktəˈljʊrəsɪz/", "chi cá nheo Mỹ (Ictalurus)"),
    ("074651", "immunopathologies", "noun", "/ˌɪmjənoʊpəˈθɒlədʒiz/", "bệnh lý miễn dịch học"),
    ("074652", "inciters", "noun", "/ɪnˈsaɪtərz/", "kẻ xúi giục; kẻ kích động"),
    ("074653", "informercials", "noun", "/ˌɪnfəˈmɜːrʃəlz/", "quảng cáo dạng phóng sự (TV)"),
    ("074654", "keeshonden", "noun", "/ˈkeɪshɒndən/", "giống chó xù Hà Lan Keeshond"),
    ("074655", "keeshonds", "noun", "/ˈkeɪshɒndz/", "giống chó xù Hà Lan Keeshond"),
    ("074656", "khamsins", "noun", "/kæmˈsiːnz/", "gió nóng khô khamsin (Ai Cập)"),
    ("074657", "ladyfishes", "noun", "/ˈleɪdiˌfɪʃɪz/", "cá cháo lớn (ladyfish)"),
    ("074658", "ledums", "noun", "/ˈliːdəmz/", "chi cây đỗ quyên đầm lầy (Ledum)"),
    ("074659", "lemniscates", "noun", "/lɛmˈnɪskɪts/", "đường cong số tám lemniscat"),
    ("074660", "lempiras", "noun", "/lɛmˈpɪrəz/", "đồng tiền lempira (Honduras)"),
    ("074661", "longyis", "noun", "/ˈlɒŋjiz/", "váy quấn truyền thống longyi"),
    ("074662", "markkaa", "noun", "/ˈmɑːrkɑː/", "đơn vị tiền cũ markka (Phần Lan)"),
    ("074663", "mashriqs", "noun", "/mæʃˈriːks/", "vùng Đông Ả Rập (Mashriq)"),
    ("074664", "megalosauruses", "noun", "/ˌmɛɡələˈsɔːrəsɪz/", "khủng long bạo chúa Megalosaurus"),
    ("074665", "mumblers", "noun", "/ˈmʌmblərz/", "người nói lầm bầm không rõ tiếng"),
    ("074666", "muridaes", "noun", "/ˈmjʊrɪdiːz/", "họ Chuột (Muridae)"),
    ("074667", "nektons", "noun", "/ˈnɛktɒnz/", "sinh vật tự bơi (hải dương học)"),
    ("074668", "niblicks", "noun", "/ˈnɪblɪks/", "gậy golf đánh cát niblick"),
    ("074669", "nonevents", "noun", "/ˌnɒnɪˈvɛnts/", "sự kiện nhạt nhẽo, gây thất vọng"),
    ("074670", "nosepieces", "noun", "/ˈnoʊzpiːsɪz/", "gọng cầu mũi kính; mâm vật kính"),
    ("074671", "nosologies", "noun", "/nəˈsɒlədʒiz/", "bệnh học phân loại"),
    ("074672", "ophthalmoscopies", "noun", "/ˌɒfθælˈmɒskəpiz/", "thủ thuật soi đáy mắt (y học)"),
    ("074673", "orcinuses", "noun", "/ɔːrˈsaɪnəsɪz/", "chi cá voi sát thủ (Orcinus)"),
    ("074674", "ornithischians", "noun", "/ˌɔːrnɪˈθɪskiənz/", "khủng long hông chim"),
    ("074675", "osascos", "noun", "/oʊˈsɑːskoʊz/", "thành phố Osasco (Brazil)"),
    ("074676", "papules", "noun", "/ˈpæpjuːlz/", "nốt sẩn da (da liễu)"),
    ("074677", "paradiddles", "noun", "/ˈpærəˌdɪdəlz/", "kỹ thuật đánh trống paradiddle"),
    ("074678", "peepuls", "noun", "/ˈpiːpəlz/", "cây bồ đề (Ficus religiosa)"),
    ("074679", "perinatologies", "noun", "/ˌpɛrɪneɪˈtɒlədʒiz/", "khoa sản chu sinh (y học)"),
    ("074680", "phasmids", "noun", "/ˈfæzmɪdz/", "bọ que (bộ Phasmatodea)"),
    ("074681", "pipets", "noun", "/paɪˈpɛts/", "ống nhỏ giọt định mức pipet"),
    ("074682", "plagiocephalies", "noun", "/ˌpleɪdʒioʊˈsɛfəliz/", "dị tật đầu méo xiên (y học)"),
    ("074683", "pteridiums", "noun", "/təˈrɪdiəmz/", "chi dương xỉ diều hâu (Pteridium)"),
    ("074684", "pyrogens", "noun", "/ˈpaɪrədʒənz/", "chất gây sốt (y học)"),
    ("074685", "rattraps", "noun", "/ˈrætræps/", "bẫy chuột; nơi tồi tàn ngột ngạt"),
    ("074686", "recreants", "noun", "/ˈrɛkriənts/", "kẻ hèn nhát; kẻ phản bội (cổ)"),
    ("074687", "reseaus", "noun", "/reɪˈzoʊz/", "mạng lưới trạm; kẻ ô màn hình"),
    ("074688", "reseaux", "noun", "/reɪˈzoʊ/", "mạng lưới trạm; kẻ ô màn hình"),
    ("074689", "semiweeklies", "noun", "/ˌsɛmiˈwiːkliz/", "tuần san ra 2 kỳ mỗi tuần"),
    ("074690", "sesamums", "noun", "/ˈsɛsəməmz/", "chi cây vừng mè (Sesamum)"),
    ("074691", "shovellers", "noun", "/ˈʃʌvələrz/", "người xúc xẻng; vịt mỏ thìa"),
    ("074692", "smattered", "verb", "/ˈsmætərd/", "đã hiểu lơ mơ; đã bôi nhẹ lên"),
    ("074693", "smatters", "verb", "/ˈsmætərz/", "hiểu lơ mơ; nói lõm bõm; bôi nhẹ"),
    ("074694", "sporanoxes", "noun", "/spəˈrænɒksɪz/", "thuốc kháng nấm Sporanox"),
    ("074695", "stringybarks", "noun", "/ˈstrɪŋiˌbɑːrks/", "cây bạch đàn vỏ xơ (Úc)"),
    ("074696", "susianas", "noun", "/ˌsuːziˈɑːnəz/", "vùng cổ Susiana (Iran cổ đại)"),
    ("074697", "tabanidaes", "noun", "/təˈbænɪdiːz/", "họ ruồi trâu (Tabanidae)"),
    ("074698", "tercets", "noun", "/ˈtɜːrsɪts/", "khổ thơ ba câu (thơ ca)"),
    ("074699", "thingamabobs", "noun", "/ˈθɪŋəməˌbɒbz/", "cái món gì đó, cái thứ (khẩu ngữ)"),
    ("074700", "tompions", "noun", "/ˈtɒmpiənz/", "nút bịt nòng pháo; nút ống sáo"),
    ("074701", "totalisms", "noun", "/ˈtoʊtəlɪzəmz/", "chủ nghĩa toàn trị"),
    ("074702", "tranquillizers", "noun", "/ˈtræŋkwɪlaɪzərz/", "thuốc an thần; thuốc gây mê thú"),
]

with open("scratch/b35_r10_raw_p2.json", "r", encoding="utf-8") as f:
    raw = json.load(f)

assert len(raw) == len(rows) == 100
out = []
for r, (rid, hw, pos, ipa, vi) in zip(raw, rows):
    assert r["id"].endswith("." + rid), f"ID mismatch: {r['id']} vs {rid}"
    assert r["hw"] == hw, f"HW mismatch: {r['hw']} vs {hw}"
    assert len(vi) <= 35, f"vi too long ({len(vi)}): {hw} -> {vi}"
    assert ipa.count("/") == 2 and not ipa[1:-1].startswith(" ") and not ipa[1:-1].endswith(" "), f"bad ipa: {hw} -> {ipa}"
    r["pos"] = pos
    r["ipa"] = ipa
    r["vi"] = vi
    r["status"] = "reviewed"
    out.append(r)

with open("scratch/b35_r10_p2.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b35_r10_p2 saved OK")
