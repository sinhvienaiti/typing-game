import json

items = [
    ("067203", "tdts", "noun", "/ˌtiː diː ˈtiːz/", "Thời gian Động lực học Trái Đất"),
    ("067204", "terminable interest", "phrase", "/ˈtɜːrmɪnəbəl ˈɪntrəst/", "quyền lợi tài sản có thời hạn"),
    ("067205", "testudos", "noun", "/tɛˈstjuːdoʊz/", "đội hình mai rùa La Mã; chi rùa cạn"),
    ("067206", "theodolites", "noun", "/θiˈɒdəˌlaɪts/", "máy kinh vĩ đo góc trắc địa"),
    ("067207", "tolbooths", "noun", "/ˈtoʊlˌbuːðz/", "trạm thu phí cầu đường; nhà tù cổ"),
    ("067208", "tollgates", "noun", "/ˈtoʊlˌɡeɪts/", "cổng barie trạm thu phí giao thông"),
    ("067209", "trichloroethylenes", "noun", "/traɪˌklɔːroʊˈɛθɪliːnz/", "dung môi công nghiệp tricloetylen"),
    ("067210", "tugela falls", "phrase", "/tuːˈɡeɪlə fɔːlz/", "thác nước cao Tugela ở Nam Phi"),
    ("067211", "unlovelier", "adj", "/ʌnˈlʌvliər/", "kém duyên xấu xí hơn; đáng ghét hơn"),
    ("067212", "unloveliest", "adj", "/ʌnˈlʌvliɪst/", "kém duyên xấu xí nhất"),
    ("067213", "uralics", "noun", "/jʊəˈrælɪks/", "ngữ hệ Ural vùng Bắc Á và Đông Âu"),
    ("067214", "vaginismuses", "noun", "/ˌvædʒɪˈnɪzməsɪz/", "chứng co thắt cơ âm đạo vô thức"),
    ("067215", "vascularizations", "noun", "/ˌvæskjələraɪˈzeɪʃənz/", "sự hình thành mạng mạch máu mới"),
    ("067216", "velvet osier", "phrase", "/ˈvɛlvɪt ˈoʊʒər/", "cây liễu nhung mềm Bắc Mỹ"),
    ("067217", "venus maidenhair", "phrase", "/ˈviːnəs ˈmeɪdənˌhɛər/", "cây dương xỉ tóc thần Vệ Nữ"),
    ("067218", "victorianas", "noun", "/vɪkˌtɔːriˈɑːnəz/", "đồ cổ và văn hóa thời Victoria"),
    ("067219", "walhallas", "noun", "/wɑːlˈhɑːləz/", "đại sảnh tử sĩ thần thoại Valhalla"),
    ("067220", "weedkillers", "noun", "/ˈwiːdˌkɪlərz/", "thuốc diệt cỏ dại nông nghiệp"),
    ("067221", "weimaraners", "noun", "/ˈvaɪmərɑːnərz/", "giống chó săn lông xám Weimaraner"),
    ("067222", "whiteflies", "noun", "/ˈwaɪtˌflaɪz/", "bọ phấn trắng chích hút hại cây"),
    ("067223", "witticisms", "noun", "/ˈwɪtɪˌsɪzəmz/", "câu nói dí dỏm hóm hỉnh thông minh"),
    ("067224", "wobblers", "noun", "/ˈwɒblərz/", "mồi câu rung lắc; ngựa mất thăng"),
    ("067225", "zeaxanthins", "noun", "/ˌziːəˈzænθɪnz/", "sắc tố carotenoit bảo vệ mắt"),
    ("067226", "affiants", "noun", "/əˈfaɪənts/", "người lập bản khai hữu thệ pháp lý"),
    ("067227", "altruists", "noun", "/ˈæltruːɪsts/", "người sống vị tha vì lợi ích chung"),
    ("067228", "antinomians", "noun", "/ˌæntɪˈnoʊmiənz/", "người theo thuyết bài luật đạo đức"),
    ("067229", "axillas", "noun", "/ækˈsɪləz/", "hõm nách dưới khớp vai; nách lá"),
    ("067230", "babkas", "noun", "/ˈbɑːbkəz/", "bánh mì xoắn ngọt sô cô la babka"),
    ("067231", "balladeers", "noun", "/ˌbæləˈdɪərz/", "ca sĩ chuyên hát nhạc ballad kể"),
    ("067232", "bardeens", "noun", "/bɑːrˈdiːnz/", "nhà vật lý Nobel John Bardeen"),
    ("067233", "birdbaths", "noun", "/ˈbɜːrdˌbæθs/", "chậu nông đặt sân vườn cho chim tắm"),
    ("067234", "bluecoats", "noun", "/ˈbluːˌkoʊts/", "lính phe Liên bang Nội chiến Mỹ"),
    ("067235", "bronchospasms", "noun", "/ˈbrɒŋkoʊˌspæzəmz/", "cơn co thắt cơ trơn phế quản"),
    ("067236", "brucellas", "noun", "/bruːˈsɛləz/", "vi khuẩn Brucella gây sốt sảy thai"),
    ("067237", "bruited", "verb", "/ˈbruːtɪd/", "đã đồn thổi lan truyền tin rộng rãi"),
    ("067238", "canids", "noun", "/ˈkeɪnɪdz/", "động vật ăn thịt thuộc họ Chó"),
    ("067239", "chalcopyrites", "noun", "/ˌkælkəˈpaɪraɪts/", "quặng đồng sunfua chalcopyrit"),
    ("067240", "chondrites", "noun", "/ˈkɒndraɪts/", "thiên thạch đá nguyên thủy chondrit"),
    ("067241", "codlings", "noun", "/ˈkɒdlɪŋz/", "cá tuyết con; giống táo nấu bánh"),
    ("067242", "collimators", "noun", "/ˈkɒlɪˌmeɪtərz/", "ống chuẩn trực hội tụ tia song song"),
    ("067243", "counterterrorists", "noun", "/ˌkaʊntərˈtɛrərɪsts/", "lực lượng chuyên trách chống khủng"),
    ("067244", "crecies", "noun", "/kreɪˈsiz/", "trận đánh Crécy năm 1346 ở Pháp"),
    ("067245", "croquettes", "noun", "/kroʊˈkɛts/", "bánh khoai thịt nghiền tẩm bột rán"),
    ("067246", "dacites", "noun", "/ˈdeɪsaɪts/", "đá núi lửa phun trào dacit"),
    ("067247", "distributers", "noun", "/dɪˈstrɪbjʊtərz/", "nhà phân phối hàng; bộ chia điện"),
    ("067248", "dyspeptics", "noun", "/dɪsˈpɛptɪks/", "người hay khó tiêu; kẻ bi quan"),
    ("067249", "exocets", "noun", "/ˈɛksoʊˌsɛts/", "tên lửa chống hạm Exocet của Pháp"),
    ("067250", "faciae", "noun", "/ˈfeɪʃiː/", "màng cân bao cơ; bảng mặt trước"),
    ("067251", "facias", "noun", "/ˈfeɪʃəz/", "bảng hiệu mặt tiền; bảng táp lô xe"),
    ("067252", "filiations", "noun", "/ˌfɪliˈeɪʃənz/", "quan hệ phụ tử huyết thống pháp lý"),
    ("067253", "gavottes", "noun", "/ɡəˈvɒts/", "điệu múa cổ điển Pháp nhịp vừa"),
    ("067254", "genevans", "noun", "/dʒɪˈniːvənz/", "người dân thành phố Geneva Thụy Sĩ"),
    ("067255", "gonds", "noun", "/ɡɒndz/", "người dân tộc Gond ở miền trung Ấn"),
    ("067256", "holographs", "noun", "/ˈhɒləˌɡræfs/", "di chúc hoặc văn bản tự viết tay"),
    ("067257", "hostas", "noun", "/ˈhɒstəz/", "cây ngọc trâm trồng cảnh râm mát"),
    ("067258", "icecaps", "noun", "/ˈaɪsˌkæps/", "chỏm băng vĩnh cửu phủ hai cực"),
    ("067259", "ilions", "noun", "/ˈɪliənz/", "thành cổ Troy Ilion trong sử thi"),
    ("067260", "infliximabs", "noun", "/ɪnˈflɪksɪˌmæbz/", "kháng thể đơn dòng trị tự miễn"),
    ("067261", "innovativenesses", "noun", "/ˈɪnəveɪtɪvnəsɪz/", "tính sáng tạo đổi mới không ngừng"),
    ("067262", "isofluranes", "noun", "/ˌaɪsoʊˈflʊəreɪnz/", "thuốc gây mê đường hô hấp isofluran"),
    ("067263", "izanagis", "noun", "/ˌiːzəˈnɑːɡiz/", "nam thần sáng thế Nhật Bản Izanagi"),
    ("067264", "jazzmans", "noun", "/ˈdʒæzmənz/", "nhạc công biểu diễn nhạc jazz"),
    ("067265", "juglanses", "noun", "/ˈdʒuːɡlænsɪz/", "cây óc chó thuộc chi Juglans"),
    ("067266", "kislevs", "noun", "/ˈkɪslɛvz/", "tháng thứ chín Kislev lịch Do Thái"),
    ("067267", "leafhoppers", "noun", "/ˈliːfˌhɒpərz/", "rầy xanh nhảy chích hút nhựa lá"),
    ("067268", "lifos", "noun", "/ˈlaɪfoʊz/", "nguyên lý nhập sau xuất trước LIFO"),
    ("067269", "lisente", "noun", "/lɪˈsɛnteɪ/", "đơn vị tiền xu sente của Lesotho"),
    ("067270", "listente", "noun", "/lɪˈsɛnteɪ/", "tiền xu sente Lesotho (biến thể)"),
    ("067271", "lungfishes", "noun", "/ˈlʌŋˌfɪʃɪz/", "cá phổi hô hấp được bằng không khí"),
    ("067272", "mandelstams", "noun", "/ˈmændəlstɑːmz/", "nhà thơ Nga Osip Mandelstam"),
    ("067273", "matabeles", "noun", "/ˌmætəˈbiːliz/", "người dân tộc Matabele Zimbabwe"),
    ("067274", "myalgias", "noun", "/maɪˈældʒəz/", "tình trạng đau nhức cơ bắp"),
    ("067275", "myelofibrosises", "noun", "/ˌmaɪəloʊfaɪˈbroʊsɪsɪz/", "bệnh xơ hóa tủy xương tạo máu"),
    ("067276", "ninetieths", "noun", "/ˈnaɪntiəθs/", "phân số một phần chín mươi"),
    ("067277", "notochords", "noun", "/ˈnoʊtəˌkɔːrdz/", "dây sống nâng đỡ phôi động vật"),
    ("067278", "oboists", "noun", "/ˈoʊboʊɪsts/", "nghệ sĩ thổi kèn gỗ ô-boa"),
    ("067279", "omertas", "noun", "/oʊˈmɛərtəz/", "luật im lặng ngầm omertà của mafia"),
    ("067280", "oxygenases", "noun", "/ˈɒksɪdʒəˌneɪsɪz/", "enzym xúc tác gắn phân tử oxy"),
    ("067281", "packhorses", "noun", "/ˈpækˌhɔːrsɪz/", "ngựa thồ chở hàng hóa đường núi"),
    ("067282", "paleoecologies", "noun", "/ˌpeɪlioʊɪˈkɒlədʒiz/", "ngành cổ sinh thái học tiền sử"),
    ("067283", "paraphilias", "noun", "/ˌpærəˈfɪliəz/", "lệch lạc hứng thú tình dục (y học)"),
    ("067284", "perceivers", "noun", "/pərˈsiːvərz/", "người nhận thức cảm thụ bằng giác"),
    ("067285", "pergamums", "noun", "/ˈpɜːrɡəməmz/", "thành cổ Pergamon ở Tiểu Á"),
    ("067286", "peristyles", "noun", "/ˈpɛrɪˌstaɪlz/", "hành lang hàng cột bao quanh đền"),
    ("067287", "philodendra", "noun", "/ˌfɪləˈdɛndrə/", "cây trầu bà lá xẻ họ Ráy"),
    ("067288", "philodendrons", "noun", "/ˌfɪləˈdɛndrənz/", "cây kiểng lá trầu bà Philodendron"),
    ("067289", "platonists", "noun", "/ˈpleɪtənɪsts/", "học giả theo triết học Platon"),
    ("067290", "pluggers", "noun", "/ˈplʌɡərz/", "người kiên trì chịu khó; người PR"),
    ("067291", "polemicists", "noun", "/pəˈlɛmɪsɪsts/", "nhà bút chiến tranh luận sắc bén"),
    ("067292", "rangpurs", "noun", "/ˈræŋˌpʊərz/", "quả chanh đỏ rangpur lai quýt"),
    ("067293", "refashioned", "verb", "/riːˈfæʃənd/", "đã cải tạo thiết kế tạo dáng lại"),
    ("067294", "refashioning", "verb", "/riːˈfæʃənɪŋ/", "đang tái thiết kế làm mới lại"),
    ("067295", "refashions", "verb", "/riːˈfæʃənz/", "tạo dáng mới sửa sang cải tạo lại"),
    ("067296", "rockslides", "noun", "/ˈrɒkˌslaɪdz/", "vụ lở đá sạt lở vách núi đá"),
    ("067297", "savoyards", "noun", "/ˌsævɔɪˈɑːrdz/", "người vùng Savoy; nghệ sĩ nhạc kịch"),
    ("067298", "scallywags", "noun", "/ˈskæliˌwæɡz/", "kẻ ranh mãnh; kẻ cơ hội chính trị"),
    ("067299", "scattergoods", "noun", "/ˈskætərˌɡʊdz/", "kẻ phá gia chi tử tiêu xài hoang"),
    ("067300", "scaups", "noun", "/skɔːps/", "loài vịt biển lặn kiếm ăn mỏ xanh"),
    ("067301", "schmaltzier", "adj", "/ˈʃmɔːltsiər/", "sến súa ủy mị quá mức hơn"),
    ("067302", "schmaltziest", "adj", "/ˈʃmɔːltsiɪst/", "sến súa ủy mị quá mức nhất"),
]

with open("scratch/b34_r05_raw_p3.json") as f:
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

with open("scratch/b34_r05_p3.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r05_p3.json OK")
