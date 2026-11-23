import json

items = [
    ("066803", "olms", "noun", "/oʊlmz/", "kỳ giông mù sống hang động châu Âu"),
    ("066804", "ondaatjes", "noun", "/ɒnˈdɑːtʃiz/", "nhà văn Canada Michael Ondaatje"),
    ("066805", "oophorectomies", "noun", "/ˌoʊəfəˈrɛktəmiz/", "ca phẫu thuật cắt bỏ buồng trứng"),
    ("066806", "palliums", "noun", "/ˈpæliəmz/", "vỏ đại não; dây choàng giáo hoàng"),
    ("066807", "pierises", "noun", "/ˈpaɪərɪsɪz/", "chi bướm phấn trắng; chi cây Pieris"),
    ("066808", "plantagos", "noun", "/plænˈteɪɡoʊz/", "cây mã đề thuộc chi Plantago"),
    ("066809", "platefuls", "noun", "/ˈpleɪtˌfʊlz/", "lượng thức ăn chất đầy một đĩa"),
    ("066810", "porkers", "noun", "/ˈpɔːrkərz/", "lợn nuôi vỗ béo lấy thịt"),
    ("066811", "postmistresses", "noun", "/ˈpoʊstˌmɪstrɪsɪz/", "nữ trưởng bưu cục"),
    ("066812", "puffballs", "noun", "/ˈpʌfˌbɔːlz/", "nấm bóng thổi phun bào tử"),
    ("066813", "pyxises", "noun", "/ˈpɪksɪsɪz/", "quả hộp mở nắp; hộp đựng Bánh Thánh"),
    ("066814", "quantics", "noun", "/ˈkwɒntɪks/", "đa thức thuần nhất (toán học cổ)"),
    ("066815", "quitclaims", "noun", "/ˈkwɪtˌkleɪmz/", "văn bản chuyển nhượng từ bỏ quyền"),
    ("066816", "rashts", "noun", "/rɑːʃts/", "thành phố Rasht ở miền bắc Iran"),
    ("066817", "redcaps", "noun", "/ˈrɛdˌkæps/", "nhân viên khuân vác; lính quân cảnh"),
    ("066818", "reticules", "noun", "/ˈrɛtɪˌkjuːlz/", "túi xách rút dây; lưới chữ thập"),
    ("066819", "rosebushes", "noun", "/ˈroʊzˌbʊʃɪz/", "bụi cây hoa hồng"),
    ("066820", "rubatos", "noun", "/ruːˈbɑːtoʊz/", "lối diễn tấu co giãn nhịp tự do"),
    ("066821", "scrapheaps", "noun", "/ˈskræpˌhiːps/", "đống sắt vụn phế liệu bỏ đi"),
    ("066822", "seedsmans", "noun", "/ˈsiːdzmənz/", "người buôn hạt giống; nông dân gieo"),
    ("066823", "strymons", "noun", "/ˈstraɪmɒnz/", "chi bướm Strymon; sông Struma"),
    ("066824", "stutterers", "noun", "/ˈstʌtərərz/", "người mắc tật nói lắp bắp"),
    ("066825", "submenus", "noun", "/ˈsʌbˌmɛnjuːz/", "trình đơn con trong giao diện"),
    ("066826", "superordinated", "verb", "/ˌsuːpərˈɔːrdɪneɪtɪd/", "đã xếp vào cấp bậc cao hơn"),
    ("066827", "superordinating", "verb", "/ˌsuːpərˈɔːrdɪneɪtɪŋ/", "đang xếp vào cấp bậc cao hơn"),
    ("066828", "systoles", "noun", "/ˈsɪstəliz/", "thì tâm thu tim co bóp tống máu"),
    ("066829", "taels", "noun", "/teɪlz/", "đơn vị lạng cân Á Đông cổ"),
    ("066830", "tostadas", "noun", "/toʊˈstɑːdəz/", "bánh ngô chiên giòn nhân Mexico"),
    ("066831", "trotskyites", "noun", "/ˈtrɒtskiˌaɪts/", "người theo chủ nghĩa Trotsky"),
    ("066832", "tsimshians", "noun", "/ˈsɪmʃiənz/", "người bản địa Tsimshian bờ Tây"),
    ("066833", "ugrics", "noun", "/ˈjuːɡrɪks/", "nhóm ngôn ngữ Ugric gồm Hungary"),
    ("066834", "underplayed", "verb", "/ˌʌndərˈpleɪd/", "đã diễn xuất tiết chế không phô"),
    ("066835", "underplaying", "verb", "/ˌʌndərˈpleɪɪŋ/", "đang diễn tiết chế; hạ thấp mức độ"),
    ("066836", "underplays", "verb", "/ˌʌndərˈpleɪz/", "diễn tiết chế; xem nhẹ giảm nhẹ"),
    ("066837", "urmias", "noun", "/ˈʊərmiəz/", "hồ nước mặn Urmia ở Iran"),
    ("066838", "vivariums", "noun", "/vaɪˈvɛəriəmz/", "hộp kính nuôi sinh vật cạn cảnh"),
    ("066839", "woodgrains", "noun", "/ˈwʊdˌɡreɪnz/", "đường vân thớ gỗ tự nhiên"),
    ("066840", "wynettes", "noun", "/wɪˈnɛts/", "ca sĩ đồng quê Mỹ Tammy Wynette"),
    ("066841", "xxies", "noun", "/ˈɛks ɛks ˈwaɪz/", "hội chứng thừa NST giới tính XXY"),
    ("066842", "accentual system", "phrase", "/ækˈsɛntʃuəl ˈsɪstəm/", "hệ thống trọng âm của ngôn ngữ"),
    ("066843", "acyl anhydrides", "phrase", "/ˈeɪsəl ænˈhaɪdraɪdz/", "hợp chất hữu cơ anhiđrit acyl"),
    ("066844", "agapanthus africanus", "phrase", "/ˌæɡəˈpænθəs ˌæfrɪˈkeɪnəs/", "cây hoa huệ sông Nile châu Phi"),
    ("066845", "amanita muscaria", "phrase", "/ˌæməˈnaɪtə mʌˈskɛəriə/", "nấm độc tán đỏ chấm trắng"),
    ("066846", "anaphoric pronoun", "phrase", "/ˌænəˈfɔːrɪk ˈproʊnaʊn/", "đại từ hồi chỉ quy chiếu từ trước"),
    ("066847", "asclepias albicans", "phrase", "/æˈskliːpiəs ˈælbɪkænz/", "cây bông tai sáp trắng sa mạc"),
    ("066848", "barbette carriage", "phrase", "/bɑːrˈbɛt ˈkærɪdʒ/", "bệ pháo xoay đặt trên thành lũy"),
    ("066849", "blacktail deer", "phrase", "/ˈblækˌteɪl dɪər/", "hươu đuôi đen vùng tây Bắc Mỹ"),
    ("066850", "blacktail prairie dog", "phrase", "/ˈblækˌteɪl ˈprɛəri dɒɡ/", "sóc chó đồng cỏ đuôi đen"),
    ("066851", "cascara buckthorn", "phrase", "/kæˈskɛərə ˈbʌkθɔːrn/", "cây táo gai vỏ làm thuốc xổ cascara"),
    ("066852", "centaurea americana", "phrase", "/sɛnˈtɔːriə əˌmɛrɪˈkeɪnə/", "hoa cúc rổ tím Bắc Mỹ"),
    ("066853", "central scotoma", "phrase", "/ˈsɛntrəl skəˈtoʊmə/", "ám điểm mù vùng thị giác trung tâm"),
    ("066854", "chequing account", "phrase", "/ˈtʃɛkɪŋ əˈkaʊnt/", "tài khoản thanh toán viết séc"),
    ("066855", "chigger flower", "phrase", "/ˈtʃɪɡər ˈflaʊər/", "cây bông tai hoa cam Bắc Mỹ"),
    ("066856", "chilean rimu", "phrase", "/tʃɪˈliːən ˈriːmuː/", "cây tùng quả mận bản địa Chile"),
    ("066857", "cinchona pubescens", "phrase", "/sɪŋˈkoʊnə pjuːˈbɛsənz/", "cây canh-ki-na đỏ chứa quinin"),
    ("066858", "cloze procedure", "phrase", "/kloʊz prəˈsiːdʒər/", "kỹ thuật kiểm tra điền từ khuyết"),
    ("066859", "cloze test", "phrase", "/kloʊz tɛst/", "bài kiểm tra điền từ vào chỗ trống"),
    ("066860", "countersink bit", "phrase", "/ˈkaʊntərˌsɪŋk bɪt/", "mũi khoan vát miệng lỗ bắt vít chìm"),
    ("066861", "david siqueiros", "phrase", "/dɑːˈviːd sɪˈkɛərəz/", "họa sĩ tranh tường Mexico Siqueiros"),
    ("066862", "derris root", "phrase", "/ˈdɛrɪs ruːt/", "rễ cây dây mật thuốc cá rotenon"),
    ("066863", "edgard lawrence doctorow", "phrase", "/ˈɛdɡərd ˈlɔːrəns ˈdɒktəroʊ/", "nhà văn Mỹ E. L. Doctorow"),
    ("066864", "eugenio pacelli", "phrase", "/eɪuːˈdʒɛnjoʊ pɑːˈtʃɛli/", "Giáo hoàng Piô XII Eugenio Pacelli"),
    ("066865", "family orchidaceae", "phrase", "/ˈfæməli ˌɔːrkɪˈdeɪʃiː/", "họ Phong lan Orchidaceae"),
    ("066866", "fiddlehead fern", "phrase", "/ˈfɪdəlˌhɛd fɜːrn/", "chồi lá dương xỉ cuộn non ăn được"),
    ("066867", "genus armillaria", "phrase", "/ˈdʒiːnəs ˌɑːrmɪˈlɛəriə/", "chi nấm mật ong Armillaria"),
    ("066868", "genus carya", "phrase", "/ˈdʒiːnəs ˈkɛəriə/", "chi cây mạy châu hồ đào Carya"),
    ("066869", "genus cordia", "phrase", "/ˈdʒiːnəs ˈkɔːrdiə/", "chi cây cùm rụm lá nhám Cordia"),
    ("066870", "genus corylus", "phrase", "/ˈdʒiːnəs ˈkɔːrɪləs/", "chi cây phỉ Corylus"),
    ("066871", "genus derris", "phrase", "/ˈdʒiːnəs ˈdɛrɪs/", "chi dây mật thuốc cá Derris"),
    ("066872", "genus oenothera", "phrase", "/ˈdʒiːnəs ˌiːnoʊˈθɪərə/", "chi hoa anh thảo chiều Oenothera"),
    ("066873", "genus parus", "phrase", "/ˈdʒiːnəs ˈpɛərəs/", "chi chim bạc má Parus"),
    ("066874", "genus plumbago", "phrase", "/ˈdʒiːnəs plʌmˈbeɪɡoʊ/", "chi cây đuôi công bạch hoa xà"),
    ("066875", "genus serratia", "phrase", "/ˈdʒiːnəs sɛˈreɪʃə/", "chi vi khuẩn đường ruột Serratia"),
    ("066876", "genus theobroma", "phrase", "/ˈdʒiːnəs ˌθiːəˈbroʊmə/", "chi cây ca cao Theobroma"),
    ("066877", "giovanni cimabue", "phrase", "/dʒoʊˈvɑːni tʃiːˈmɑːbweɪ/", "họa sĩ Phục Hưng Ý Cimabue"),
    ("066878", "glottal plosive", "phrase", "/ˈɡlɒtəl ˈploʊsɪv/", "âm tắc thanh hầu (ngữ âm học)"),
    ("066879", "hans zinsser", "phrase", "/hɑːnz ˈzɪnsər/", "nhà vi khuẩn học Mỹ Hans Zinsser"),
    ("066880", "hypoglossal nerve", "phrase", "/ˌhaɪpəˈɡlɒsəl nɜːrv/", "dây thần kinh hạ thiệt sọ XII"),
    ("066881", "jacques etienne montgolfier", "phrase", "/ʒɑːk eɪˈtjɛn mɒntˈɡɒlfiər/", "nhà phát minh khinh khí cầu Pháp"),
    ("066882", "lactuca sativa", "phrase", "/lækˈtjuːkə səˈtaɪvə/", "cây rau diếp xà lách ăn lá"),
    ("066883", "madia elegans", "phrase", "/ˈmeɪdiə ˈɛlɪɡænz/", "hoa cúc mắt nhung California"),
    ("066884", "margaret munnerlyn mitchell", "phrase", "/ˈmɑːrɡərɪt ˈmʌnərlɪn ˈmɪtʃəl/", "tác giả Cuốn theo chiều gió"),
    ("066885", "mountain nyala", "phrase", "/ˈmaʊntən njɑːˈlɑː/", "linh dương nyala núi Ethiopia"),
    ("066886", "mugo pine", "phrase", "/ˈmjuːɡoʊ paɪn/", "cây thông lùn núi mugo châu Âu"),
    ("066887", "phylum arthropoda", "phrase", "/ˈfaɪləm ɑːrˈθrɒpədə/", "ngành Chân khớp động vật chân đốt"),
    ("066888", "piriform area", "phrase", "/ˈpɪrɪfɔːrm ˈɛəriə/", "vùng vỏ não khứu giác hình lê"),
    ("066889", "pulseless disease", "phrase", "/ˈpʌlsləs dɪˈziːz/", "bệnh viêm tắc động mạch Takayasu"),
    ("066890", "reentrant polygon", "phrase", "/riːˈɛntrənt ˈpɒlɪɡɒn/", "đa giác lõm có góc trên 180 độ"),
    ("066891", "sambucus nigra", "phrase", "/sæmˈbjuːkəs ˈnaɪɡrə/", "cây cơm cháy quả đen châu Âu"),
    ("066892", "silene latifolia", "phrase", "/saɪˈliːni ˌlætɪˈfoʊliə/", "cây cẩm chướng dại hoa trắng"),
    ("066893", "variola vaccinia", "phrase", "/vəˈraɪələ vækˈsɪniə/", "vi rút đậu bò làm vắc-xin"),
    ("066894", "vladimir ilyich ulyanov", "phrase", "/vləˈdɪmɪər ˈɪljɪtʃ ʊlˈjɑːnɒf/", "V. I. Lenin tên thật Ulyanov"),
    ("066895", "walter william skeat", "phrase", "/ˈwɔːltər ˈwɪljəm skiːt/", "nhà ngữ văn học Anh W. W. Skeat"),
    ("066896", "yenisei river", "phrase", "/ˌjɛnɪˈseɪ ˈrɪvər/", "sông Yenisei chảy qua Siberia Nga"),
    ("066897", "acclimatised", "verb", "/əˈklaɪməˌtaɪzd/", "đã thích nghi khí hậu (Anh Anh)"),
    ("066898", "acclimatises", "verb", "/əˈklaɪməˌtaɪzɪz/", "thích nghi khí hậu môi trường mới"),
    ("066899", "acclimatising", "verb", "/əˈklaɪməˌtaɪzɪŋ/", "đang thích nghi khí hậu môi trường"),
    ("066900", "agaricuses", "noun", "/ˈæɡərɪkəsɪz/", "nấm tán thuộc chi Agaricus"),
    ("066901", "agrobacteria", "noun", "/ˌæɡroʊbækˈtɪriə/", "vi khuẩn đất gây u sần thực vật"),
    ("066902", "angiosperms", "noun", "/ˈændʒiəˌspɜːrmz/", "thực vật hạt kín có hoa và quả"),
]

with open("scratch/b34_r04_raw_p4.json") as f:
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

with open("scratch/b34_r04_p4.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r04_p4.json OK")
