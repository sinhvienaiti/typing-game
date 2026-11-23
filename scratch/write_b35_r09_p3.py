import json

items = [
    ("074203", "narwals", "noun", "/ˈnɑːrwəlz/", "kỳ lân biển một ngà (cách viết)"),
    ("074204", "neuroblasts", "noun", "/ˈnjʊəroʊˌblæsts/", "nguyên bào thần kinh phôi thai"),
    ("074205", "noctuids", "noun", "/ˈnɒktʃuɪdz/", "bướm đêm họ Ngài đêm (Noctuidae)"),
    ("074206", "norvascs", "noun", "/ˈnɔːrvæsks/", "thuốc hạ huyết áp Norvasc"),
    ("074207", "notturnos", "noun", "/nɒtˈtʊərnoʊz/", "khúc nhạc dạ khúc trữ tình Ý"),
    ("074208", "nypas", "noun", "/ˈnaɪpəz/", "cây dừa nước (chi Nypa)"),
    ("074209", "orlons", "noun", "/ˈɔːrlɒnz/", "sợi tổng hợp acrylic Orlon"),
    ("074210", "oryctolaguses", "noun", "/ˌɒrɪkˈtɒləɡəsɪz/", "chi Thỏ châu Âu (Oryctolagus)"),
    ("074211", "panoches", "noun", "/pəˈnoʊtʃiz/", "kẹo đường nâu hồ đào panoche"),
    ("074212", "pennyweights", "noun", "/ˈpɛniˌweɪts/", "đơn vị đo vàng (~1,555 gam)"),
    ("074213", "peroneuses", "noun", "/ˌpɛrəˈniːəsɪz/", "cơ mác ở cẳng chân ngoài"),
    ("074214", "phacelias", "noun", "/fəˈsiːliəz/", "cây hoa chuông tím chi Phacelia"),
    ("074215", "pleomorphisms", "noun", "/ˌpliːoʊˈmɔːrfɪzəmz/", "hiện tượng đa hình tế bào sinh học"),
    ("074216", "podicepses", "noun", "/ˈpɒdɪsɛpsɪz/", "chi Chim lặn cổ đỏ Podiceps"),
    ("074217", "polyarteritises", "noun", "/ˌpɒliɑːrtəˈraɪtɪsɪz/", "bệnh viêm nút đa động mạch"),
    ("074218", "potpies", "noun", "/ˈpɒtˌpaɪz/", "bánh nướng nhân thịt hầm trong thố"),
    ("074219", "praenomens", "noun", "/priːˈnoʊmɛnz/", "tên cá nhân đứng đầu tên La Mã cổ"),
    ("074220", "praenomina", "noun", "/priːˈnɒmɪnə/", "tên cá nhân đứng đầu tên La Mã cổ"),
    ("074221", "prefigurations", "noun", "/ˌpriːfɪɡjʊˈreɪʃənz/", "điềm báo trước; hình mẫu tiên báo"),
    ("074222", "puffinuses", "noun", "/ˈpʌfɪnəsɪz/", "chi Chim hải âu lướt sóng Puffinus"),
    ("074223", "reclusivenesses", "noun", "/rɪˈkluːsɪvnəsɪz/", "tính ẩn dật khép kín ít giao du"),
    ("074224", "resuspensions", "noun", "/ˌriːsəˈspɛnʃənz/", "sự hòa huyền phù lơ lửng trở lại"),
    ("074225", "ruckled", "verb", "/ˈrʌkəld/", "đã nhăn nhúm nhàu; đã thở khò khè"),
    ("074226", "ruckles", "verb", "/ˈrʌkəlz/", "nhăn nhúm lại; thở rít khò khè"),
    ("074227", "ruckling", "verb", "/ˈrʌklɪŋ/", "đang nhăn nhúm; đang thở khò khè"),
    ("074228", "saimiris", "noun", "/saɪˈmɪəriz/", "chi Khỉ sóc Nam Mỹ (Saimiri)"),
    ("074229", "sandblasters", "noun", "/ˈsændˌblæstərz/", "máy phun cát làm sạch bề mặt"),
    ("074230", "sarawakians", "noun", "/ˌsærəˈwɑːkiənz/", "người dân bang Sarawak (Malaysia)"),
    ("074231", "seconders", "noun", "/ˈsɛkəndərz/", "người tán thành ủng hộ kiến nghị"),
    ("074232", "sensualisms", "noun", "/ˈsɛnʃuəˌlɪzəmz/", "thuyết khoái lạc; thuyết cảm giác"),
    ("074233", "shindies", "noun", "/ˈʃɪndiz/", "cuộc cãi lộn ầm ĩ; tiệc náo nhiệt"),
    ("074234", "shirtfronts", "noun", "/ˈʃɜːrtˌfrʌnts/", "phần thân ngực phía trước áo sơ mi"),
    ("074235", "sizzed", "verb", "/sɪzd/", "đã phát tiếng xèo xèo (từ hiếm)"),
    ("074236", "sizzes", "verb", "/ˈsɪzɪz/", "phát tiếng xèo xèo; làm xì (hiếm)"),
    ("074237", "sizzing", "verb", "/ˈsɪzɪŋ/", "đang phát tiếng xèo xèo"),
    ("074238", "snakewoods", "noun", "/ˈsneɪkˌwʊdz/", "cây gỗ vân da rắn (hoặc mã tiền)"),
    ("074239", "stellites", "noun", "/ˈstɛlaɪts/", "hợp kim siêu cứng chịu mài stellite"),
    ("074240", "summersaults", "noun", "/ˈsʌmərˌsɔːlts/", "cú nhào lộn vòng người (biến thể)"),
    ("074241", "superfectas", "noun", "/ˌsuːpərˈfɛktəz/", "cược chọn đúng bốn ngựa về nhất"),
    ("074242", "synthesists", "noun", "/ˈsɪnθɪsɪsts/", "nhà tổng hợp; người chơi đàn synth"),
    ("074243", "tebets", "noun", "/ˈtɛvɛts/", "tháng mười lịch Do Thái (Tevet)"),
    ("074244", "thalwegs", "noun", "/ˈtɑːlˌvɛɡz/", "đường sâu nhất lòng sông thung lũng"),
    ("074245", "thenars", "noun", "/ˈθiːnɑːrz/", "mô cái (gò thịt gốc ngón cái tay)"),
    ("074246", "thoracenteses", "noun", "/ˌθɔːrəsɛnˈtiːsiːz/", "thủ thuật chọc dò dịch màng phổi"),
    ("074247", "toxicodendrons", "noun", "/ˌtɒksɪkoʊˈdɛndrɒnz/", "chi Cây sơn độc (thường xuân độc)"),
    ("074248", "ululations", "noun", "/ˌjuːljʊˈleɪʃənz/", "tiếng hú tru dài; tiếng khóc than"),
    ("074249", "unci", "noun", "/ˈʌnsaɪ/", "móc giải phẫu; móc thùy thái dương"),
    ("074250", "uncuses", "noun", "/ˈʌŋkəsɪz/", "cấu trúc hình móc (thùy não, bọ)"),
    ("074251", "unilateralists", "noun", "/ˌjuːnɪˈlætərəlɪsts/", "người theo chủ nghĩa đơn phương"),
    ("074252", "uppps", "noun", "/ˌjuː piː piː ˈpiːz/", "phẫu thuật chỉnh họng ngủ ngáy UPPP"),
    ("074253", "wauled", "verb", "/wɔːld/", "đã rên rỉ kêu gào thảm thiết (mèo)"),
    ("074254", "wauling", "verb", "/ˈwɔːlɪŋ/", "đang kêu gào thảm thiết (mèo, trẻ)"),
    ("074255", "wauls", "verb", "/wɔːlz/", "kêu gào thảm thiết; rên rỉ (mèo)"),
    ("074256", "weakfishes", "noun", "/ˈwiːkˌfɪʃɪz/", "cá đù đốm biển Bắc Mỹ"),
    ("074257", "yentas", "noun", "/ˈjɛntəz/", "người đàn bà hay ngồi lê đôi mách"),
    ("074258", "agrimonies", "noun", "/ˈæɡrɪˌmoʊniz/", "cây long nha thảo hoa vàng"),
    ("074259", "almoravids", "noun", "/ælˈmɒrəvɪdz/", "triều đại Hồi giáo Almoravid"),
    ("074260", "anergies", "noun", "/ˈænərdʒiz/", "tình trạng mất đáp ứng miễn dịch"),
    ("074261", "antiphonaries", "noun", "/ænˈtɪfəˌnɛriz/", "sách thánh ca hát đối đáp Công giáo"),
    ("074262", "arsines", "noun", "/ˈɑːrsiːnz/", "khí độc asen hiđrua (AsH3)"),
    ("074263", "atherogeneses", "noun", "/ˌæθəroʊˈdʒɛnɪsiːz/", "quá trình hình thành xơ vữa mạch"),
    ("074264", "baptisias", "noun", "/bæpˈtɪʒəz/", "cây đậu chàm dại Bắc Mỹ Baptisia"),
    ("074265", "blastomeres", "noun", "/ˈblæstəˌmɪərz/", "phôi bào (tế bào phân cắt phôi sớm)"),
    ("074266", "borderers", "noun", "/ˈbɔːrdərərz/", "cư dân sống dọc vùng biên giới"),
    ("074267", "bovidaes", "noun", "/ˈboʊvɪˌdiːz/", "họ Trâu bò (bò, cừu, linh dương)"),
    ("074268", "bramblings", "noun", "/ˈbræmblɪŋz/", "chim sẻ núi ngực cam phương bắc"),
    ("074269", "brownshirts", "noun", "/ˈbraʊnˌʃɜːrts/", "đội quân áo nâu SA phát xít Đức"),
    ("074270", "brummagems", "noun", "/ˈbrʌmədʒəmz/", "hàng giả rẻ tiền (từ cổ Birmingham)"),
    ("074271", "caesalpinias", "noun", "/ˌsɛzəlˈpɪniəz/", "chi Cây tô mộc kim phượng"),
    ("074272", "carduuses", "noun", "/ˈkɑːrdjʊəsɪz/", "cây kế hoang thuộc chi Carduus"),
    ("074273", "catharanthuses", "noun", "/ˌkæθəˈrænθəsɪz/", "cây hoa dừa cạn chi Catharanthus"),
    ("074274", "cementites", "noun", "/sɪˈmɛntaɪts/", "pha cacbit sắt cứng xementit (Fe3C)"),
    ("074275", "chlorophyceaes", "noun", "/ˌklɔːrəˈfaɪʃiˌiːz/", "lớp Tảo lục đơn bào đa bào"),
    ("074276", "chukkers", "noun", "/ˈtʃʌkərz/", "hiệp đấu trong môn mã cầu polo"),
    ("074277", "clepsydrae", "noun", "/ˈklɛpsɪˌdriː/", "đồng hồ nước cổ đại đo thời gian"),
    ("074278", "clepsydras", "noun", "/ˈklɛpsɪdrəz/", "đồng hồ nước cổ đại đo thời gian"),
    ("074279", "clofibrates", "noun", "/kloʊˈfaɪbreɪts/", "thuốc hạ mỡ máu clofibrate"),
    ("074280", "cornetists", "noun", "/ˈkɔːrnɪtɪsts/", "nhạc công thổi kèn đồng cornet"),
    ("074281", "cosmids", "noun", "/ˈkɒzmɪdz/", "vector nhân bản cosmid (sinh học)"),
    ("074282", "cowfishes", "noun", "/ˈkaʊˌfɪʃɪz/", "cá nóc sừng bò (cá bò hòm có sừng)"),
    ("074283", "cymenes", "noun", "/ˈsaɪmiːnz/", "hợp chất thơm tự nhiên ximen"),
    ("074284", "didanosines", "noun", "/daɪˈdænəsiːnz/", "thuốc kháng HIV didanosine (ddI)"),
    ("074285", "digitalized", "verb", "/ˈdɪdʒɪtəˌlaɪzd/", "đã số hóa; dùng thuốc trợ tim"),
    ("074286", "digitalizes", "verb", "/ˈdɪdʒɪtəˌlaɪzɪz/", "số hóa; dùng thuốc trợ tim digital"),
    ("074287", "digitalizing", "verb", "/ˈdɪdʒɪtəˌlaɪzɪŋ/", "đang số hóa; đang dùng trợ tim"),
    ("074288", "dogfighters", "noun", "/ˈdɒɡˌfaɪtərz/", "phi công không chiến; chủ chọi chó"),
    ("074289", "encephaloceles", "noun", "/ɛnˈsɛfəloʊˌsiːlz/", "dị tật thoát vị não qua khuyết sọ"),
    ("074290", "entelechies", "noun", "/ɛnˈtɛlɪkiz/", "nguyên lý hoàn thiện hiện thực hóa"),
    ("074291", "eohippi", "noun", "/ˌiːoʊˈhɪpaɪ/", "ngựa thủy tổ tiền sử Eohippus"),
    ("074292", "esotropias", "noun", "/ˌɛsoʊˈtroʊpiəz/", "tật lác mắt vào trong (lé trong)"),
    ("074293", "execrated", "verb", "/ˈɛksɪˌkreɪtɪd/", "đã nguyền rủa ghê tởm lên án"),
    ("074294", "execrates", "verb", "/ˈɛksɪˌkreɪts/", "nguyền rủa căm ghét ghê tởm"),
    ("074295", "execrating", "verb", "/ˈɛksɪˌkreɪtɪŋ/", "đang nguyền rủa căm ghét ghê tởm"),
    ("074296", "ferules", "noun", "/ˈfɛruːlz/", "thước gỗ phạt đòn học sinh (cũ)"),
    ("074297", "fireplugs", "noun", "/ˈfaɪərˌplʌɡz/", "trụ cấp nước cứu hỏa ngoài đường"),
    ("074298", "fructidors", "noun", "/ˈfrʌktɪdɔːrz/", "tháng Quả (tháng 12 lịch Pháp 1793)"),
    ("074299", "goidelics", "noun", "/ɡɔɪˈdɛlɪks/", "nhóm ngôn ngữ Celt Goidel (Ireland)"),
    ("074300", "groaners", "noun", "/ˈɡroʊnərz/", "người rên rỉ than vãn; chuyện nhạt"),
    ("074301", "gyrocompasses", "noun", "/ˈdʒaɪroʊˌkʌmpəsɪz/", "la bàn con quay hồi chuyển"),
    ("074302", "halcions", "noun", "/ˈhælsiɒnz/", "thuốc ngủ an thần Halcion"),
]

with open("scratch/b35_r09_raw_p3.json") as f:
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

with open("scratch/b35_r09_p3.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r09_p3.json OK")
