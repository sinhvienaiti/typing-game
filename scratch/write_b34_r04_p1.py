import json

items = [
    ("066503", "swage block", "phrase", "/sweɪdʒ blɒk/", "đế khuôn rèn uốn kim loại"),
    ("066504", "tin pyrites", "phrase", "/tɪn ˈpaɪraɪts/", "quặng stannit sunfua đồng thiếc"),
    ("066505", "toxic dumpsite", "phrase", "/ˈtɒksɪk ˈdʌmpˌsaɪt/", "bãi chôn lấp chất thải độc hại"),
    ("066506", "tyrannus tyrannus", "phrase", "/tɪˈrænəs tɪˈrænəs/", "chim bạo quân phương Đông Bắc Mỹ"),
    ("066507", "volcan de colima", "phrase", "/vɒlˈkɑːn deɪ koʊˈliːmə/", "núi lửa Colima ở tây Mexico"),
    ("066508", "white blood corpuscle", "phrase", "/waɪt blʌd ˈkɔːrpʌsəl/", "tế bào bạch cầu bảo vệ miễn dịch"),
    ("066509", "white corpuscle", "phrase", "/waɪt ˈkɔːrpʌsəl/", "tế bào bạch cầu trong máu"),
    ("066510", "wild cavy", "phrase", "/waɪld ˈkeɪvi/", "chuột lang hoang dã Nam Mỹ"),
    ("066511", "wisteria floribunda", "phrase", "/wɪˈstɪriə ˌflɔːrɪˈbʌndə/", "cây hoa tử đằng Nhật Bản"),
    ("066512", "yellow loosestrife", "phrase", "/ˈjɛloʊ ˈluːsˌstraɪf/", "cây trân châu hoa vàng"),
    ("066513", "zonk out", "phrase", "/zɒŋk aʊt/", "ngủ gục ngay; ngất lịm đi (lóng)"),
    ("066514", "acetabula", "noun", "/ˌæsɪˈtæbjələ/", "ổ cối khớp háng xương chậu"),
    ("066515", "acetabulums", "noun", "/ˌæsɪˈtæbjələmz/", "ổ cối khớp hông xương chậu"),
    ("066516", "afterimages", "noun", "/ˈæftərˌɪmɪdʒɪz/", "dư ảnh lưu lại trên võng mạc"),
    ("066517", "alectos", "noun", "/əˈlɛktoʊz/", "nữ thần báo thù Alecto Hy Lạp"),
    ("066518", "algrens", "noun", "/ˈælɡrənz/", "nhà văn Mỹ Nelson Algren"),
    ("066519", "amaranthuses", "noun", "/ˌæməˈrænθəsɪz/", "cây rau dền thuộc chi Amaranthus"),
    ("066520", "amnesics", "noun", "/æmˈniːzɪks/", "người mắc chứng mất trí nhớ"),
    ("066521", "ansers", "noun", "/ˈænsərz/", "chi ngỗng thật điển hình Anser"),
    ("066522", "araucarias", "noun", "/ˌɛərəˈkɛəriəz/", "cây bách tán thuộc chi Araucaria"),
    ("066523", "arteritises", "noun", "/ˌɑːrtəˈraɪtɪsɪz/", "bệnh viêm thành động mạch"),
    ("066524", "bedrests", "noun", "/ˈbɛdˌrɛsts/", "thời gian nằm nghỉ dưỡng tại giường"),
    ("066525", "biodefenses", "noun", "/ˌbaɪoʊdɪˈfɛnsɪz/", "hệ thống phòng thủ sinh học"),
    ("066526", "bluestems", "noun", "/ˈbluːˌstɛmz/", "cỏ thảo nguyên thân xanh Bắc Mỹ"),
    ("066527", "brachiopods", "noun", "/ˈbrækiəˌpɒdz/", "động vật tay cuộn có vỏ hai mảnh"),
    ("066528", "brigits", "noun", "/ˈbrɪdʒɪts/", "nữ thần Celtic Brigid của Ireland"),
    ("066529", "caloocans", "noun", "/ˌkɑːloʊˈoʊkənz/", "thành phố Caloocan ở Philippines"),
    ("066530", "carjacked", "verb", "/ˈkɑːrˌdʒækt/", "đã cướp xe ô tô có người lái"),
    ("066531", "carjacks", "verb", "/ˈkɑːrˌdʒæks/", "cướp xe ô tô đang có người trên xe"),
    ("066532", "catecholamines", "noun", "/ˌkætəˈkoʊləmiːnz/", "chất dẫn truyền catecholamin"),
    ("066533", "chanterelles", "noun", "/ˌʃæntəˈrɛlz/", "nấm mồng gà màu vàng ăn được"),
    ("066534", "chimaerae", "noun", "/kaɪˈmɪriː/", "quái vật Chimera; cá khiêm biển"),
    ("066535", "chimaeras", "noun", "/kaɪˈmɪrəz/", "sinh vật khảm; quái vật Chimera"),
    ("066536", "chintzier", "adj", "/ˈtʃɪntsiər/", "rẻ tiền lòe loẹt hơn; keo kiệt hơn"),
    ("066537", "chintziest", "adj", "/ˈtʃɪntsiɪst/", "rẻ tiền lòe loẹt nhất; keo kiệt"),
    ("066538", "dactyls", "noun", "/ˈdæktɪlz/", "bước thơ một âm nặng hai âm nhẹ"),
    ("066539", "devoirs", "noun", "/dəˈvwɑːrz/", "lời chào kính cẩn; bổn phận"),
    ("066540", "dishier", "adj", "/ˈdɪʃiər/", "quyến rũ đẹp trai hấp dẫn hơn"),
    ("066541", "dishiest", "adj", "/ˈdɪʃiɪst/", "quyến rũ đẹp trai hấp dẫn nhất"),
    ("066542", "donkins", "noun", "/ˈdɒŋkɪnz/", "kỹ sư hoặc nhà toán học Donkin"),
    ("066543", "dumbwaiters", "noun", "/ˈdʌmˌweɪtərz/", "thang tời nhỏ vận chuyển đồ ăn"),
    ("066544", "eavesdroppers", "noun", "/ˈiːvzˌdrɒpərz/", "kẻ nghe lén câu chuyện người khác"),
    ("066545", "elastases", "noun", "/ɪˈlæsˌteɪsɪz/", "enzym phân giải sợi đàn hồi elastin"),
    ("066546", "embayments", "noun", "/ɪmˈbeɪmənts/", "vịnh nhỏ hình thành trên bờ biển"),
    ("066547", "faunuses", "noun", "/ˈfɔːnəsɪz/", "thần rừng đồng quê Faunus La Mã"),
    ("066548", "flatfeet", "noun", "/ˈflætˌfiːt/", "bàn chân bẹt; cảnh sát đi bộ (lóng)"),
    ("066549", "gametophytes", "noun", "/ɡəˈmiːtəˌfaɪts/", "thể giao tử ở thực vật và tảo"),
    ("066550", "gingivae", "noun", "/dʒɪnˈdʒaɪviː/", "mô nướu lợi quanh chân răng"),
    ("066551", "gingivas", "noun", "/dʒɪnˈdʒaɪvəz/", "nướu lợi bao bọc quanh răng"),
    ("066552", "gingkoes", "noun", "/ˈɡɪŋkoʊz/", "cây bạch quả cổ đại lá quạt"),
    ("066553", "gingkos", "noun", "/ˈɡɪŋkoʊz/", "cây ngân hạnh bạch quả"),
    ("066554", "gnomons", "noun", "/ˈnoʊmɒnz/", "kim đồng hồ mặt trời chỉ bóng nắng"),
    ("066555", "godwits", "noun", "/ˈɡɒdwɪts/", "chim choắt mỏ dài sống vùng lầy"),
    ("066556", "hankies", "noun", "/ˈhæŋkiz/", "khăn mùi soa bỏ túi (thân mật)"),
    ("066557", "hemangiomas", "noun", "/hɪˌmændʒiˈoʊməz/", "u mạch máu lành tính trên da"),
    ("066558", "heyerdahls", "noun", "/ˈheɪərdɑːlz/", "nhà thám hiểm Na Uy Heyerdahl"),
    ("066559", "hirsutisms", "noun", "/ˈhɜːrsjʊˌtɪzəmz/", "chứng rậm lông tóc bất thường"),
    ("066560", "holoferneses", "noun", "/ˌhɒləˈfɜːrniːzɪz/", "tướng Holofernes trong Kinh Thánh"),
    ("066561", "icelanders", "noun", "/ˈaɪsˌlændərz/", "người dân đảo quốc Iceland"),
    ("066562", "independencies", "noun", "/ˌɪndɪˈpɛndənsiz/", "nền độc lập tự chủ hoàn toàn"),
    ("066563", "isopods", "noun", "/ˈaɪsəˌpɒdz/", "giáp xác chân đều như rận gỗ"),
    ("066564", "keratoconuses", "noun", "/ˌkɛrətoʊˈkoʊnəsɪz/", "bệnh giãn phình giác mạc hình nón"),
    ("066565", "klaipedas", "noun", "/ˈklaɪpɛdəz/", "thành phố cảng Klaipėda Litva"),
    ("066566", "kotexes", "noun", "/ˈkoʊtɛksɪz/", "băng vệ sinh thấm hút phụ nữ"),
    ("066567", "kyphoses", "noun", "/kaɪˈfoʊsiːz/", "chứng gù cong cột sống lưng trên"),
    ("066568", "lacheses", "noun", "/ˈlækɪsiːz/", "nữ thần số mệnh Lachesis; rắn độc"),
    ("066569", "laminectomies", "noun", "/ˌlæmɪˈnɛktəmiz/", "phẫu thuật cắt cung sau đốt sống"),
    ("066570", "lammases", "noun", "/ˈlæməsɪz/", "lễ hội thu hoạch lúa mì Lammas"),
    ("066571", "lamplighters", "noun", "/ˈlæmpˌlaɪtərz/", "người thắp đèn đường bằng ga xưa"),
    ("066572", "landrovers", "noun", "/ˈlændˌroʊvərz/", "xe ô tô dẫn động hai cầu địa hình"),
    ("066573", "leapers", "noun", "/ˈliːpərz/", "người hoặc loài vật bật nhảy xa"),
    ("066574", "loungewears", "noun", "/ˈlaʊndʒˌwɛərz/", "quần áo thoải mái mặc thư giãn"),
    ("066575", "louvers", "noun", "/ˈluːvərz/", "lá chớp thông gió cửa sổ"),
    ("066576", "maeterlincks", "noun", "/ˈmeɪtərlɪŋks/", "nhà văn Nobel Bỉ Maeterlinck"),
    ("066577", "menders", "noun", "/ˈmɛndərz/", "thợ vá quần áo; người sửa chữa"),
    ("066578", "mesospheres", "noun", "/ˈmɛzəˌsfɪərz/", "tầng trung lưu của khí quyển"),
    ("066579", "micrograms", "noun", "/ˈmaɪkrəˌɡræmz/", "đơn vị khối lượng micrôgam"),
    ("066580", "minocyclines", "noun", "/ˌmɪnəˈsaɪkliːnz/", "thuốc kháng sinh minocyclin"),
    ("066581", "mizens", "noun", "/ˈmɪzənz/", "cột buồm sau cùng trên tàu buồm"),
    ("066582", "mugworts", "noun", "/ˈmʌɡˌwɜːrts/", "cây ngải cứu làm gia vị và thuốc"),
    ("066583", "murrumbidgees", "noun", "/ˌmʌrəmˈbɪdʒiz/", "sông Murrumbidgee ở nước Úc"),
    ("066584", "neomycins", "noun", "/ˌniːəˈmaɪsɪnz/", "thuốc kháng sinh neomycin bôi da"),
    ("066585", "nepetas", "noun", "/ˈnɛpətəz/", "cây bạc hà mèo thuộc chi Nepeta"),
    ("066586", "nightsticks", "noun", "/ˈnaɪtˌstɪks/", "dùi cui tuần tra của cảnh sát"),
    ("066587", "nijs", "noun", "/ˌɛn aɪ ˈdʒeɪz/", "Viện Nghiên cứu Tư pháp Quốc gia Mỹ"),
    ("066588", "nonbelievers", "noun", "/ˌnɒnbɪˈliːvərz/", "người không tin theo tôn giáo"),
    ("066589", "nonstarters", "noun", "/nɒnˈstɑːrtərz/", "kế hoạch hay ý tưởng cầm chắc thua"),
    ("066590", "oozier", "adj", "/ˈuːziər/", "nhầy nhụa bùn hơn; rỉ nước hơn"),
    ("066591", "ooziest", "adj", "/ˈuːziɪst/", "nhầy nhụa bùn nhất; rỉ nước nhất"),
    ("066592", "orffs", "noun", "/ɔːrfs/", "nhà soạn nhạc Đức Carl Orff"),
    ("066593", "ostinatos", "noun", "/ˌɒstɪˈnɑːtoʊz/", "mô-típ nhạc lặp đi lặp lại"),
    ("066594", "oximeters", "noun", "/ɒkˈsɪmɪtərz/", "máy đo nồng độ oxy trong máu"),
    ("066595", "pabas", "noun", "/ˈpɑːbəz/", "axit PABA chống nắng vitamin Bx"),
    ("066596", "pelargoniums", "noun", "/ˌpɛlɑːrˈɡoʊniəmz/", "hoa phong lữ chi Pelargonium"),
    ("066597", "percepts", "noun", "/ˈpɜːrsɛpts/", "hình ảnh tri giác cảm nhận được"),
    ("066598", "photophobias", "noun", "/ˌfoʊtəˈfoʊbiəz/", "chứng chói mắt sợ ánh sáng mạnh"),
    ("066599", "piddled", "verb", "/ˈpɪdəld/", "đã làm việc qua loa lãng phí giờ"),
    ("066600", "piddles", "noun", "/ˈpɪdəlz/", "nước tiểu; việc làm qua loa (lóng)"),
    ("066601", "pillocks", "noun", "/ˈpɪləks/", "kẻ ngốc nghếch (khẩu ngữ Anh)"),
    ("066602", "pledgers", "noun", "/ˈplɛdʒərz/", "người cam kết đóng góp hoặc cầm cố"),
]

with open("scratch/b34_r04_raw_p1.json") as f:
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

with open("scratch/b34_r04_p1.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r04_p1.json OK")
