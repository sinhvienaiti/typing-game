import json

items = [
    ("069903", "sudras", "noun", "/ˈsuːdrəz/", "đẳng cấp lao động Shudra Ấn Độ"),
    ("069904", "supinations", "noun", "/ˌsuːpɪˈneɪʃənz/", "động tác xoay ngửa lòng bàn tay"),
    ("069905", "synopticses", "noun", "/sɪˈnɒptɪksɪz/", "ba sách Phúc Âm Nhất Lãm Tân Ước"),
    ("069906", "tailgaters", "noun", "/ˈteɪlˌɡeɪtərz/", "tài xế bám sát đuôi xe trước quá"),
    ("069907", "tarquinii", "noun", "/tɑːrˈkwɪniaɪ/", "vua La Mã Tarquinius; thành cổ"),
    ("069908", "telamones", "noun", "/ˌtɛləˈmoʊniːz/", "cột đá tạc tượng nam giới đỡ mái"),
    ("069909", "telamons", "noun", "/ˈtɛləmənz/", "tượng nam giới dùng làm cột đỡ"),
    ("069910", "terpsichores", "noun", "/tɜːrpˈsɪkəriz/", "nữ thần vũ đạo Terpsichore Hy Lạp"),
    ("069911", "turbinates", "noun", "/ˈtɜːrbɪnəts/", "xương xoăn mũi bên trong hốc mũi"),
    ("069912", "turgors", "noun", "/ˈtɜːrɡərz/", "áp suất trương căng tế bào thực vật"),
    ("069913", "ultracentrifugations", "noun", "/ˌʌltrəsɛntrɪfjʊˈɡeɪʃənz/", "phương pháp siêu ly tâm tách hạt"),
    ("069914", "urticas", "noun", "/ˈɜːrtɪkəz/", "cây tầm ma có lông ngứa chi Urtica"),
    ("069915", "vaporisers", "noun", "/ˈveɪpəˌraɪzərz/", "máy xông hơi ẩm; thiết bị hóa hơi"),
    ("069916", "vicunas", "noun", "/vɪˈkuːnjəz/", "lạc đà vicuña Andes; len lông mịn"),
    ("069917", "yanans", "noun", "/ˈjɑːnənz/", "ngữ hệ Yanan bản địa California"),
    ("069918", "ancestresses", "noun", "/ˈænsɛstrɪsɪz/", "nữ tổ tiên; bà tổ dòng họ"),
    ("069919", "anoles", "noun", "/əˈnoʊliz/", "thằn lằn anole đổi màu châu Mỹ"),
    ("069920", "arkansans", "noun", "/ɑːrˈkænzənz/", "người dân bang Arkansas của Mỹ"),
    ("069921", "armillarias", "noun", "/ˌɑːrmɪˈlɛəriəz/", "nấm mật ong mọc cụm trên gốc gỗ"),
    ("069922", "atheromas", "noun", "/ˌæθəˈroʊməz/", "mảng xơ vữa bám thành động mạch"),
    ("069923", "atheromata", "noun", "/ˌæθəˈroʊmətə/", "mảng xơ vữa mỡ gây hẹp mạch máu"),
    ("069924", "bandboxes", "noun", "/ˈbændˌbɒksɪz/", "hộp trụ nhẹ đựng mũ hoặc cổ áo"),
    ("069925", "barbettes", "noun", "/bɑːrˈbɛts/", "bệ thép bọc giáp đỡ tháp pháo tàu"),
    ("069926", "bartholdis", "noun", "/bɑːrˈtɒldiz/", "nhà điêu khắc Tượng Nữ thần Tự do"),
    ("069927", "bipedalisms", "noun", "/baɪˈpiːdəˌlɪzəmz/", "dáng đi đứng thẳng bằng hai chân"),
    ("069928", "blacktails", "noun", "/ˈblækˌteɪlz/", "hươu đuôi đen vùng tây Bắc Mỹ"),
    ("069929", "boundednesses", "noun", "/ˈbaʊndɪdnəsɪz/", "tính bị chặn có giới hạn (toán)"),
    ("069930", "caryas", "noun", "/ˈkɛəriəz/", "cây mạy châu hồ đào thuộc chi Carya"),
    ("069931", "chalonses", "noun", "/ʃɑːˈlɒnzɪz/", "trận đánh Châlons năm 451 ở Pháp"),
    ("069932", "chiggers", "noun", "/ˈtʃɪɡərz/", "ấu trùng ve đỏ; bọ chét cát"),
    ("069933", "clarinettists", "noun", "/ˌklærɪˈnɛtɪsts/", "nghệ sĩ thổi kèn clarinet (Anh)"),
    ("069934", "clasts", "noun", "/klæsts/", "mảnh vụn đá vỡ trong đá trầm tích"),
    ("069935", "cloudberries", "noun", "/ˈklaʊdˌbɛriz/", "quả mâm xôi vàng vùng đầm Bắc Cực"),
    ("069936", "coqueted", "verb", "/koʊˈkɛtɪd/", "đã tán tỉnh lả lơi (biến thể)"),
    ("069937", "coqueting", "verb", "/koʊˈkɛtɪŋ/", "đang tán tỉnh làm duyên (biến thể)"),
    ("069938", "coquets", "verb", "/koʊˈkɛts/", "tán tỉnh lả lơi đưa đẩy (biến thể)"),
    ("069939", "cordias", "noun", "/ˈkɔːrdiəz/", "cây cùm rụm lá nhám chi Cordia"),
    ("069940", "coryli", "noun", "/ˈkɒrɪlaɪ/", "cây phỉ lấy hạt thuộc chi Corylus"),
    ("069941", "countersank", "verb", "/ˈkaʊntərˌsæŋk/", "đã khoét vát loe miệng lỗ bắt vít"),
    ("069942", "countersinking", "verb", "/ˈkaʊntərˌsɪŋkɪŋ/", "đang khoét vát miệng lỗ bắt vít"),
    ("069943", "countersinks", "noun", "/ˈkaʊntərˌsɪŋks/", "lỗ vát chìm đầu ốc; mũi khoan vát"),
    ("069944", "countersunk", "verb", "/ˈkaʊntərˌsʌŋk/", "đã khoét vát loe lỗ (quá khứ phân)"),
    ("069945", "cupfuls", "noun", "/ˈkʌpˌfʊlz/", "lượng chất lỏng bột đầy một cốc"),
    ("069946", "demurrers", "noun", "/dɪˈmɜːrərz/", "đơn kháng nghị bác bỏ kiện pháp lý"),
    ("069947", "derrises", "noun", "/ˈdɛrɪsɪz/", "cây dây mật thuốc cá chi Derris"),
    ("069948", "dustups", "noun", "/ˈdʌstˌʌps/", "cuộc cãi vã ẩu đả ầm ĩ (khẩu ngữ)"),
    ("069949", "eggars", "noun", "/ˈɛɡərz/", "ngài đêm dày lông họ Lasiocampidae"),
    ("069950", "endplates", "noun", "/ˈɛndˌpleɪts/", "tấm tận cùng nối thần kinh cơ"),
    ("069951", "escaroles", "noun", "/ˈɛskəˌroʊlz/", "rau diếp xoăn lá rộng ăn sống"),
    ("069952", "eveningwears", "noun", "/ˈiːvnɪŋˌwɛərz/", "trang phục dạ hội trang trọng tối"),
    ("069953", "flagyls", "noun", "/ˈflædʒəlz/", "thuốc kháng sinh diệt khuẩn Flagyl"),
    ("069954", "framboises", "noun", "/frɑːmˈbwɑːzɪz/", "rượu mùi quả mâm xôi framboise"),
    ("069955", "gondwanalands", "noun", "/ɡɒndˈwɑːnəˌlændz/", "siêu lục địa cổ phía nam Gondwana"),
    ("069956", "grisailles", "noun", "/ɡrɪˈzaɪz/", "tranh hoặc kính vẽ đơn sắc tông xám"),
    ("069957", "heterozygotes", "noun", "/ˌhɛtəroʊˈzaɪɡoʊts/", "cá thể mang hai alen dị hợp tử"),
    ("069958", "hydrocolloids", "noun", "/ˌhaɪdroʊˈkɒlɔɪdz/", "chất keo tạo gel giữ nước"),
    ("069959", "hydroxymethyls", "noun", "/haɪˌdrɒksiˈmɛθəlz/", "nhóm chức hóa học hydroxymethyl"),
    ("069960", "hypoglossals", "noun", "/ˌhaɪpəˈɡlɒsəlz/", "dây thần kinh hạ thiệt vận động"),
    ("069961", "intuitionisms", "noun", "/ˌɪntjʊˈɪʃənˌɪzəmz/", "thuyết trực giác luận triết toán"),
    ("069962", "irredentisms", "noun", "/ˌɪrɪˈdɛntɪzəmz/", "chủ nghĩa đòi lại vùng đất cũ"),
    ("069963", "jaywalkers", "noun", "/ˈdʒeɪˌwɔːkərz/", "người đi bộ băng qua đường ẩu sai"),
    ("069964", "knotholes", "noun", "/ˈnɒtˌhoʊlz/", "lỗ hổng trên ván gỗ do mắt cây rơi"),
    ("069965", "lateralities", "noun", "/ˌlætəˈrælɪtiz/", "tính thuận một bên tay mắt não"),
    ("069966", "livenesses", "noun", "/ˈlaɪvnəsɪz/", "tính sống động trực tiếp âm thanh"),
    ("069967", "maenads", "noun", "/ˈmiːnædz/", "nữ tín đồ cuồng nhiệt thần Dionysus"),
    ("069968", "melphalans", "noun", "/ˈmɛlfələnz/", "thuốc hóa trị ung thư melphalan"),
    ("069969", "millionairesses", "noun", "/ˌmɪljəˈnɛərɪsɪz/", "nữ triệu phú sở hữu tài sản lớn"),
    ("069970", "missioners", "noun", "/ˈmɪʃənərz/", "nhà truyền giáo đi rao giảng đạo"),
    ("069971", "mitomycins", "noun", "/ˌmaɪtoʊˈmaɪsɪnz/", "thuốc kháng sinh trị u mitomycin"),
    ("069972", "moleches", "noun", "/ˈmoʊlɛks/", "thần cổ đại Moloch vùng Canaan"),
    ("069973", "moshavim", "noun", "/ˌmoʊʃɑːˈviːm/", "làng nông nghiệp hợp tác Israel"),
    ("069974", "moshavs", "noun", "/ˈmoʊʃɑːvz/", "làng hợp tác xã nông dân Israel"),
    ("069975", "ninjitsus", "noun", "/nɪnˈdʒɪtsuːz/", "võ thuật ẩn thân nhẫn thuật Nhật"),
    ("069976", "norrishes", "noun", "/ˈnɒrɪʃɪz/", "nhà hóa học Nobel Ronald Norrish"),
    ("069977", "numens", "noun", "/ˈnjuːmənz/", "thần linh bản mệnh nơi chốn"),
    ("069978", "nyalas", "noun", "/njɑːˈlɑːz/", "linh dương sừng xoắn nyala châu Phi"),
    ("069979", "obscurantists", "noun", "/ɒbˈskjʊərəntɪsts/", "người phản đối khai sáng; kẻ làm mờ"),
    ("069980", "ocelluses", "noun", "/oʊˈsɛləsɪz/", "mắt đơn cảm sáng ở côn trùng"),
    ("069981", "oenotheras", "noun", "/ˌiːnoʊˈθɪərəz/", "hoa anh thảo chiều chi Oenothera"),
    ("069982", "orchidaceaes", "noun", "/ˌɔːrkɪˈdeɪʃiz/", "họ Phong lan thực vật có hoa đẹp"),
    ("069983", "otologies", "noun", "/oʊˈtɒlədʒiz/", "chuyên khoa tai học nghiên cứu bệnh"),
    ("069984", "parers", "noun", "/ˈpɛərərz/", "dao gọt vỏ củ quả; thợ gọt mép"),
    ("069985", "paruses", "noun", "/ˈpɛərəsɪz/", "chim bạc má thuộc chi Parus"),
    ("069986", "peepshows", "noun", "/ˈpiːpˌʃoʊz/", "hộp kính xem tranh ảnh; màn diễn"),
    ("069987", "phencyclidines", "noun", "/fɛnˈsaɪklɪdiːnz/", "chất gây ảo giác phân ly PCP"),
    ("069988", "piperazines", "noun", "/pɪˈpɛrəˌziːnz/", "thuốc tẩy giun đũa kim piperazin"),
    ("069989", "ploughshares", "noun", "/ˈplaʊˌʃɛərz/", "lưỡi cày lật đất trồng trọt"),
    ("069990", "plumbagos", "noun", "/plʌmˈbeɪɡoʊz/", "cây đuôi công bạch hoa xà; than chì"),
    ("069991", "pochards", "noun", "/ˈpoʊtʃərdz/", "vịt lặn đầu nâu đỏ ăn thực vật"),
    ("069992", "pointillists", "noun", "/ˈpwæntɪlɪsts/", "họa sĩ theo trường phái chấm màu"),
    ("069993", "reflations", "noun", "/riːˈfleɪʃənz/", "chính sách tái kích thích lạm phát"),
    ("069994", "reified", "verb", "/ˈriːəˌfaɪd/", "đã cụ thể hóa khái niệm trừu tượng"),
    ("069995", "reifies", "verb", "/ˈriːəˌfaɪz/", "cụ thể hóa ý niệm thành thực thể"),
    ("069996", "reifying", "verb", "/ˈriːəˌfaɪɪŋ/", "đang cụ thể hóa thành thực thể"),
    ("069997", "remises", "noun", "/rəˈmiːzɪz/", "xe ngựa cho thuê; đòn đâm nối tiếp"),
    ("069998", "revetments", "noun", "/rɪˈvɛtmənts/", "tường kè đá chắn đất chống xói lở"),
    ("069999", "saltboxes", "noun", "/ˈsɔːltˌbɒksɪz/", "nhà mái dốc sau kiểu Mỹ; hộp muối"),
    ("070000", "scotchmans", "noun", "/ˈskɒtʃmənz/", "người Scotland (cách gọi cũ)"),
    ("070001", "scotomas", "noun", "/skəˈtoʊməz/", "ám điểm vùng mù trong thị trường"),
    ("070002", "scotomata", "noun", "/skəˈtoʊmətə/", "điểm mù khuất sáng trên võng mạc"),
]

with open("scratch/b34_r10_raw_p5.json") as f:
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

with open("scratch/b34_r10_p5.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r10_p5.json OK")
