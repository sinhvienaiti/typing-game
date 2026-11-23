import json

items = [
    ("068803", "jonquils", "noun", "/ˈdʒɒŋkwɪlz/", "hoa thủy tiên vàng thơm nồng"),
    ("068804", "katydids", "noun", "/ˈkeɪtiˌdɪdz/", "châu chấu lá xanh; con muỗm lá"),
    ("068805", "kilobytes", "noun", "/ˈkɪləˌbaɪts/", "đơn vị dữ liệu máy tính kilobyte"),
    ("068806", "kobuses", "noun", "/ˈkoʊbəsɪz/", "linh dương nước châu Phi chi Kobus"),
    ("068807", "libriums", "noun", "/ˈlɪbriəmz/", "thuốc an thần giải lo âu Librium"),
    ("068808", "lifeworks", "noun", "/ˈlaɪfˌwɜːrks/", "sự nghiệp sáng tác cả đời người"),
    ("068809", "livelongs", "noun", "/ˈlɪvˌlɒŋz/", "cây trường sinh sống đời chi Sedum"),
    ("068810", "loricae", "noun", "/ləˈraɪsiː/", "áo giáp La Mã; vỏ bọc sinh vật"),
    ("068811", "loricas", "noun", "/ˈlɒrɪkəz/", "vỏ giáp bảo vệ tế bào sinh vật"),
    ("068812", "lycopodiums", "noun", "/ˌlaɪkəˈpoʊdiəmz/", "cây thạch tùng mọc bò bào tử"),
    ("068813", "lysimachuses", "noun", "/laɪˈsɪməkəsɪz/", "tướng Hy Lạp cổ đại Lysimachus"),
    ("068814", "machinations", "noun", "/ˌmækɪˈneɪʃənz/", "mưu đồ thâm hiểm ngấm ngầm"),
    ("068815", "maunds", "noun", "/mɔːndz/", "đơn vị cân nặng cổ maund Ấn Độ"),
    ("068816", "mauriacs", "noun", "/ˌmɔːriˈæks/", "nhà văn Nobel Pháp F. Mauriac"),
    ("068817", "maximians", "noun", "/mækˈsɪmiənz/", "hoàng đế La Mã cổ đại Maximian"),
    ("068818", "metiers", "noun", "/ˈmɛtieɪz/", "nghề nghiệp hoặc lĩnh vực sở trường"),
    ("068819", "mockers", "noun", "/ˈmɒkərz/", "kẻ chế giễu nhạo báng người khác"),
    ("068820", "mollahs", "noun", "/ˈmɒləz/", "giáo sĩ học giả luật Hồi giáo"),
    ("068821", "monases", "noun", "/ˈmoʊnəsɪz/", "đơn thể nguyên thủy (triết học)"),
    ("068822", "muslimahs", "noun", "/ˈmʊzlɪməz/", "phụ nữ theo đạo Hồi (tiếng Ả Rập)"),
    ("068823", "mynahs", "noun", "/ˈmaɪnəz/", "chim sáo biết bắt chước tiếng người"),
    ("068824", "nepentheses", "noun", "/nɪˈpɛnθiːzɪz/", "cây nắp ấm bắt côn trùng"),
    ("068825", "nitrogenases", "noun", "/naɪˈtrɒdʒəˌneɪsɪz/", "enzym cố định nitơ ở vi khuẩn"),
    ("068826", "nominators", "noun", "/ˈnɒmɪˌneɪtərz/", "người tiến cử đề cử ứng viên"),
    ("068827", "nrems", "noun", "/ˈɛn rɛmz/", "giai đoạn ngủ không chuyển động mắt"),
    ("068828", "ocotillos", "noun", "/ˌoʊkəˈtiːoʊz/", "cây bụi gai hoa đỏ sa mạc ocotillo"),
    ("068829", "ophiuchi", "noun", "/ˌɒfiˈjuːkaɪ/", "chòm sao Xà Phu giữ rắn thiên cầu"),
    ("068830", "opposers", "noun", "/əˈpoʊzərz/", "người phản đối chống lại ý kiến"),
    ("068831", "oubliettes", "noun", "/ˌuːbliˈɛts/", "ngục tối sâu chỉ mở nắp trên trần"),
    ("068832", "overlies", "verb", "/ˌoʊvərˈlaɪz/", "nằm đè phủ lên phía bên trên"),
    ("068833", "oxidoreductases", "noun", "/ˌɒksɪdoʊrɪˈdʌkteɪsɪz/", "enzym xúc tác phản ứng oxy hóa khử"),
    ("068834", "palookas", "noun", "/pəˈluːkəz/", "võ sĩ quyền Anh kém; gã ngốc (lóng)"),
    ("068835", "panaxes", "noun", "/ˈpænæksɪz/", "cây nhân sâm thuộc chi Panax"),
    ("068836", "pavos", "noun", "/ˈpɑːvoʊz/", "chòm sao Khổng Tước thiên cầu nam"),
    ("068837", "peloponnesi", "noun", "/ˌpɛləpəˈniːsaɪ/", "bán đảo Peloponnese miền nam Hy Lạp"),
    ("068838", "pewees", "noun", "/ˈpiːwiz/", "chim đớp ruồi nhỏ pewee Bắc Mỹ"),
    ("068839", "phidiases", "noun", "/ˈfɪdiəsɪz/", "nhà điêu khắc Hy Lạp cổ Phidias"),
    ("068840", "plackets", "noun", "/ˈplækɪts/", "đường xẻ cài nút trên áo hoặc váy"),
    ("068841", "playschools", "noun", "/ˈpleɪˌskuːlz/", "trường nhà trẻ mẫu giáo vui chơi"),
    ("068842", "plunderers", "noun", "/ˈplʌndərərz/", "kẻ cướp bóc vơ vét của cải chiến"),
    ("068843", "polyphosphates", "noun", "/ˌpɒliˈfɒsfeɪts/", "muối polyphotphat phụ gia thực phẩm"),
    ("068844", "pompons", "noun", "/ˈpɒmpɒnz/", "quả cầu len trang trí mũ áo pompon"),
    ("068845", "potentillas", "noun", "/ˌpoʊtənˈtɪləz/", "cây hoa hồng năm cánh Potentilla"),
    ("068846", "quoins", "noun", "/kɔɪnz/", "đá xây góc tường; cái nêm chèn chữ"),
    ("068847", "rehoused", "verb", "/riːˈhaʊzd/", "đã bố trí tái định cư chỗ ở mới"),
    ("068848", "rehouses", "verb", "/riːˈhaʊzɪz/", "cấp nhà ở mới cho người chuyển dời"),
    ("068849", "rehousing", "verb", "/riːˈhaʊzɪŋ/", "đang cấp chỗ ở mới tái định cư"),
    ("068850", "resected", "verb", "/rɪˈsɛktɪd/", "đã phẫu thuật cắt bỏ một phần tạng"),
    ("068851", "resecting", "verb", "/rɪˈsɛktɪŋ/", "đang phẫu thuật cắt bỏ mô hay tạng"),
    ("068852", "resects", "verb", "/rɪˈsɛkts/", "cắt bỏ một phần cơ quan phẫu thuật"),
    ("068853", "roadsteads", "noun", "/ˈroʊdˌstɛdz/", "vũng neo đậu tàu ngoài khơi"),
    ("068854", "salades", "noun", "/səˈlɑːdz/", "mũ sắt chiến binh thế kỷ 15 sallet"),
    ("068855", "salmonelloses", "noun", "/ˌsælmənəˈloʊsiːz/", "bệnh nhiễm trùng khuẩn Salmonella"),
    ("068856", "shamashes", "noun", "/ˈʃɑːmɑːʃɪz/", "thần mặt trời và công lý Shamash"),
    ("068857", "steelmakers", "noun", "/ˈstiːlˌmeɪkərz/", "nhà sản xuất hoặc công nhân thép"),
    ("068858", "stirks", "noun", "/stɜːrks/", "bò tơ khoảng một tuổi (Scotland)"),
    ("068859", "supermoms", "noun", "/ˈsuːpərˌmɒmz/", "bà mẹ đảm đang giỏi việc nhà công"),
    ("068860", "synovitides", "noun", "/ˌsaɪnəvaɪˈtaɪdiːz/", "bệnh viêm màng hoạt dịch khớp"),
    ("068861", "tardigrades", "noun", "/ˈtɑːrdɪˌɡreɪdz/", "gấu nước vi sinh siêu bền cực đoan"),
    ("068862", "thills", "noun", "/θɪlz/", "hai càng gỗ cho ngựa kéo xe"),
    ("068863", "thingamajigs", "noun", "/ˈθɪŋəməˌdʒɪɡz/", "cái vật dụng quên tên (khẩu ngữ)"),
    ("068864", "triggerfishes", "noun", "/ˈtrɪɡərˌfɪʃɪz/", "cá bò da vây lưng dựng khóa"),
    ("068865", "trimarans", "noun", "/ˈtraɪməˌrænz/", "thuyền buồm ba thân song song"),
    ("068866", "troopships", "noun", "/ˈtruːpˌʃɪps/", "tàu thủy chuyên chở binh sĩ quân"),
    ("068867", "tuggers", "noun", "/ˈtʌɡərz/", "xe đầu kéo hàng; người kéo giật"),
    ("068868", "varlets", "noun", "/ˈvɑːrlɪts/", "tên vô lại; tiểu đồng hầu cận xưa"),
    ("068869", "visigoths", "noun", "/ˈvɪzɪˌɡɒθs/", "người Tây Goth Visigoth cổ đại"),
    ("068870", "wagrams", "noun", "/ˈvɑːɡrəmz/", "trận đánh Wagram năm 1809 ở Áo"),
    ("068871", "woodworms", "noun", "/ˈwʊdˌwɜːrmz/", "sâu mọt đục khoét phá gỗ"),
    ("068872", "albites", "noun", "/ˈælˌbaɪts/", "khoáng vật fenspat natri màu trắng"),
    ("068873", "apars", "noun", "/əˈpɑːrz/", "tatu ba đai Nam Mỹ cuộn thành bóng"),
    ("068874", "appaled", "verb", "/əˈpɔːld/", "đã làm kinh hãi kinh tởm (biến thể)"),
    ("068875", "appaling", "verb", "/əˈpɔːlɪŋ/", "đang gây kinh hãi (biến thể)"),
    ("068876", "aravas", "noun", "/ɑːˈrɑːvəz/", "thung lũng sa mạc Arava Israel"),
    ("068877", "arngs", "noun", "/ˌeɪ ɑːr ɛn ˈdʒiːz/", "Vệ binh Quốc gia Lục quân Mỹ ARNG"),
    ("068878", "arracks", "noun", "/ˈærəks/", "rượu mạnh chưng cất arrack châu Á"),
    ("068879", "astrologists", "noun", "/əˈstrɒlədʒɪsts/", "nhà chiêm tinh xem sao đoán vận"),
    ("068880", "authoresses", "noun", "/ˈɔːθərɪsɪz/", "nữ tác giả viết sách văn học"),
    ("068881", "balatas", "noun", "/bəˈlɑːtəz/", "cây và nhựa cao su cứng balata"),
    ("068882", "balloonists", "noun", "/bəˈluːnɪsts/", "phi công điều khiển khinh khí cầu"),
    ("068883", "barms", "noun", "/bɑːrmz/", "bọt men nổi lên khi ủ bia truyền"),
    ("068884", "bawds", "noun", "/bɔːdz/", "kẻ môi giới chứa mại dâm (từ cổ)"),
    ("068885", "blastoffs", "noun", "/ˈblæstˌɒfs/", "vụ phóng tên lửa rời bệ phóng"),
    ("068886", "buteos", "noun", "/ˈbjuːtioʊz/", "diều hâu cánh rộng thuộc chi Buteo"),
    ("068887", "cassiterites", "noun", "/kəˈsɪtəˌraɪts/", "quặng thiếc oxit chính cassiterit"),
    ("068888", "chiropodists", "noun", "/kɪˈrɒpədɪsts/", "chuyên viên chăm sóc bệnh bàn chân"),
    ("068889", "conservativisms", "noun", "/kənˈsɜːrvətɪˌvɪzəmz/", "tư tưởng chủ nghĩa bảo thủ truyền"),
    ("068890", "coxcombs", "noun", "/ˈkɒksˌkoʊmz/", "kẻ hợm hĩnh chưng diện; hoa mào gà"),
    ("068891", "cranched", "verb", "/kræntʃt/", "đã nhai rôm rốp; nghiến nát (cổ)"),
    ("068892", "cranches", "verb", "/ˈkræntʃɪz/", "nhai rôm rốp; nghiến giòn (từ cổ)"),
    ("068893", "cranching", "verb", "/ˈkræntʃɪŋ/", "đang nhai rôm rốp; nghiến (cổ)"),
    ("068894", "cuttles", "noun", "/ˈkʌtəlz/", "mực nang thân dẹt có mai cứng"),
    ("068895", "dewlaps", "noun", "/ˈdjuːˌlæps/", "yếm da thõng dưới cổ bò hoặc gà tây"),
    ("068896", "dinges", "noun", "/ˈdɪndʒɪz/", "vết lõm trầy nhỏ; vết bẩn ố nhẹ"),
    ("068897", "disquisitions", "noun", "/ˌdɪskwɪˈzɪʃənz/", "bài khảo luận chuyên đề học thuật"),
    ("068898", "eluls", "noun", "/ɛˈluːlz/", "tháng thứ mười hai Elul lịch Do"),
    ("068899", "embroiderers", "noun", "/ɪmˈbrɔɪdərərz/", "nghệ nhân thợ thêu tay hoặc thêu"),
    ("068900", "estriols", "noun", "/ˈɛstrioʊlz/", "hoóc-môn estrogen estriol thai kỳ"),
    ("068901", "fireweeds", "noun", "/ˈfaɪərˌwiːdz/", "cây liễu lan hoa hồng tím Bắc Mỹ"),
    ("068902", "gastrocnemii", "noun", "/ˌɡæstrɒkˈniːmiaɪ/", "cơ bụng chân tạo hình bắp chân"),
]

with open("scratch/b34_r08_raw_p4.json") as f:
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

with open("scratch/b34_r08_p4.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r08_p4.json OK")
