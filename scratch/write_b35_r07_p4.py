import json

items = [
    ("073303", "plications", "noun", "/plaɪˈkeɪʃənz/", "sự gấp nếp; nếp gấp (địa chất)"),
    ("073304", "procrusteses", "noun", "/proʊˈkrʌstiːzɪz/", "tên cướp Procrustes (Hy Lạp cổ)"),
    ("073305", "pyropes", "noun", "/ˈpaɪroʊps/", "đá quý ngọc hồng lựu đỏ pyrop"),
    ("073306", "raddles", "noun", "/ˈrædəlz/", "phẩm sơn đỏ đánh dấu; thanh đan rào"),
    ("073307", "raddling", "verb", "/ˈrædlɪŋ/", "đang bện rào; đang quệt phấn son đỏ"),
    ("073308", "razorbills", "noun", "/ˈreɪzərˌbɪlz/", "chim biển anca mỏ dao Bắc Cực"),
    ("073309", "reimpositions", "noun", "/ˌriːɪmpəˈzɪʃənz/", "sự tái áp đặt thuế hoặc quy định"),
    ("073310", "revisers", "noun", "/rɪˈvaɪzərz/", "người hiệu đính rà soát bản thảo"),
    ("073311", "rigamaroles", "noun", "/ˈrɪɡəməˌroʊlz/", "chuyện dài dòng lôi thôi (biến thể)"),
    ("073312", "salicornias", "noun", "/ˌsælɪˈkɔːrniəz/", "cây măng tây biển (chi Salicornia)"),
    ("073313", "salpingectomies", "noun", "/ˌsælpɪnˈdʒɛktəmiz/", "phẫu thuật cắt bỏ vòi trứng"),
    ("073314", "salsolas", "noun", "/sælˈsoʊləz/", "cây cỏ muối bồng lăn chi Salsola"),
    ("073315", "saquinavirs", "noun", "/səˈkwɪnəvɪərz/", "thuốc kháng HIV saquinavir"),
    ("073316", "sendups", "noun", "/ˈsɛndˌʌps/", "tác phẩm hài châm biếm nhại lại"),
    ("073317", "snowcaps", "noun", "/ˈsnoʊˌkæps/", "chỏm tuyết phủ vĩnh cửu đỉnh núi"),
    ("073318", "solvated", "verb", "/ˈsɒlveɪtɪd/", "đã solvat hóa (bao quanh phân tử)"),
    ("073319", "solvates", "noun", "/ˈsɒlveɪts/", "hợp chất solvat (dung môi gắn kết)"),
    ("073320", "solvating", "verb", "/ˈsɒlveɪtɪŋ/", "đang gây solvat hóa trong dung dịch"),
    ("073321", "stolons", "noun", "/ˈstoʊlɒnz/", "thân bò lan trên mặt đất (ngó cây)"),
    ("073322", "tallins", "noun", "/ˈtɑːlɪnz/", "thủ đô Tallinn của Estonia"),
    ("073323", "technophobias", "noun", "/ˌtɛknoʊˈfoʊbiəz/", "hội chứng sợ hoặc ác cảm công nghệ"),
    ("073324", "telencephalons", "noun", "/ˌtɛlɛnˈsɛfəlɒnz/", "đoan não (phần trước đại não)"),
    ("073325", "terebinths", "noun", "/ˈtɛrəbɪnθs/", "cây nhựa thơm Địa Trung Hải"),
    ("073326", "threadfins", "noun", "/ˈθrɛdˌfɪnz/", "cá nhụ bốn râu (họ Cá nhụ)"),
    ("073327", "thunnuses", "noun", "/ˈθʌnəsɪz/", "chi Cá ngừ đại dương (Thunnus)"),
    ("073328", "tormenters", "noun", "/tɔːrˈmɛntərz/", "kẻ hành hạ giày vò; tấm màn cánh"),
    ("073329", "tovariches", "noun", "/təˈvɑːrɪtʃɪz/", "đồng chí, bạn hữu (tiếng Nga cũ)"),
    ("073330", "triclinia", "noun", "/traɪˈklɪniə/", "phòng ăn có ba trường kỷ La Mã cổ"),
    ("073331", "trimurtis", "noun", "/trɪˈmʊərtiz/", "Tam vị nhất thể Trimurti Ấn Độ"),
    ("073332", "trismuses", "noun", "/ˈtrɪzməsɪz/", "chứng cứng khít hàm (uốn ván)"),
    ("073333", "tyrannicides", "noun", "/tɪˈrænɪˌsaɪdz/", "hành vi hoặc kẻ ám sát bạo chúa"),
    ("073334", "utns", "noun", "/ˌjuː tiː ˈɛnz/", "tổ chức UTN (Umma Tameer-e-Nau)"),
    ("073335", "vinifications", "noun", "/ˌvɪnɪfɪˈkeɪʃənz/", "quy trình lên men làm rượu vang"),
    ("073336", "viticulturists", "noun", "/ˌvɪtɪˈkʌltʃərɪsts/", "chuyên gia nghề trồng nho làm vang"),
    ("073337", "wanglers", "noun", "/ˈwæŋɡlərz/", "kẻ xoay xở khôn lỏi luồn lách"),
    ("073338", "weissbiers", "noun", "/ˈvaɪsˌbɪərz/", "bia lúa mì trắng kiểu Đức"),
    ("073339", "wildcatters", "noun", "/ˈwaɪldˌkætərz/", "người khoan dò dầu mỏ mạo hiểm"),
    ("073340", "winterberries", "noun", "/ˈwɪntərˌbɛriz/", "cây nhựa ruồi quả đỏ mùa đông"),
    ("073341", "zahariases", "noun", "/zəˈhɑːriəsɪz/", "nữ vận động viên Babe Didrikson"),
    ("073342", "abilas", "noun", "/əˈbiːləz/", "mũi Abila (một trong hai trụ cổ)"),
    ("073343", "abstractionisms", "noun", "/æbˈstrækʃəˌnɪzəmz/", "chủ nghĩa trừu tượng (nghệ thuật)"),
    ("073344", "acrises", "noun", "/ˈækrɪsɪz/", "chi Ếch dế nhỏ Bắc Mỹ (Acris)"),
    ("073345", "aegilopses", "noun", "/iːˈdʒɪlɒpsɪz/", "cỏ dê hoang họ hàng lúa mì; u góc"),
    ("073346", "affrighted", "verb", "/əˈfraɪtɪd/", "đã làm hoảng sợ kinh hãi (từ cổ)"),
    ("073347", "affrighting", "verb", "/əˈfraɪtɪŋ/", "đang làm hoảng sợ kinh hãi (từ cổ)"),
    ("073348", "affrights", "noun", "/əˈfraɪts/", "nỗi khiếp sợ; làm kinh hãi (cổ)"),
    ("073349", "afrls", "noun", "/ˌeɪ ɛf ɑːr ˈɛlz/", "Phòng Nghiên cứu Không quân (AFRL)"),
    ("073350", "akhenatons", "noun", "/ˌɑːkəˈnɑːtənz/", "Pharaon Ai Cập cổ Akhenaten"),
    ("073351", "angevines", "noun", "/ˈændʒɪˌvaɪnz/", "người xứ Anjou; vương triều Anjou"),
    ("073352", "antifeminisms", "noun", "/ˌæntiˈfɛmɪˌnɪzəmz/", "chủ nghĩa chống lại nữ quyền"),
    ("073353", "appellatives", "noun", "/əˈpɛlətɪvz/", "danh xưng gọi tên; danh từ chung"),
    ("073354", "araceaes", "noun", "/əˈreɪʃiˌiːz/", "họ Ráy (khoai môn, hồng môn)"),
    ("073355", "aristolochias", "noun", "/ˌærɪstəˈloʊkiəz/", "cây hoa bình vôi mộc hương Nam Mỹ"),
    ("073356", "ashkhabads", "noun", "/ˌɑːʃkəˈbɑːdz/", "thủ đô Ashgabat (tên cũ Ashkhabad)"),
    ("073357", "bannerets", "noun", "/ˌbænəˈrɛts/", "hiệp sĩ mang cờ hiệu phong tước xưa"),
    ("073358", "beriths", "noun", "/ˈbɪərɪθs/", "lễ cắt bao quy đầu Do Thái (Brit)"),
    ("073359", "bettongs", "noun", "/ˈbɛtɒŋz/", "chuột túi nhỏ bettong ở Úc"),
    ("073360", "blepharospasms", "noun", "/ˈblɛfərəˌspæzəmz/", "chứng co giật nháy mí mắt liên tục"),
    ("073361", "blowsier", "adj", "/ˈblaʊziər/", "lôi thôi xộc xệch đỏ mặt hơn"),
    ("073362", "blowsiest", "adj", "/ˈblaʊziɪst/", "lôi thôi xộc xệch đỏ mặt nhất"),
    ("073363", "bottlecaps", "noun", "/ˈbɒtəlˌkæps/", "nắp chai kim loại hoặc nhựa"),
    ("073364", "brachyuras", "noun", "/ˌbrækɪˈjʊərəz/", "phân thứ bộ Cua thật (đuôi ngắn)"),
    ("073365", "brickfields", "noun", "/ˈbrɪkˌfiːldz/", "bãi đất nặn và lò nung gạch"),
    ("073366", "butterflyfishes", "noun", "/ˈbʌtərflaɪˌfɪʃɪz/", "cá bướm rạn san hô màu rực rỡ"),
    ("073367", "carhops", "noun", "/ˈkɑːrˌhɒps/", "bồi bàn phục vụ tận xe (Mỹ)"),
    ("073368", "centauries", "noun", "/ˈsɛntɔːriz/", "cây cỏ bách thảo chi Centaurium"),
    ("073369", "cicutas", "noun", "/sɪˈkjuːtəz/", "cây cần độc chết người (Cicuta)"),
    ("073370", "circularizations", "noun", "/ˌsɜːrkjʊləraɪˈzeɪʃənz/", "sự gửi thông báo hàng loạt"),
    ("073371", "clothos", "noun", "/ˈkloʊθoʊz/", "nữ thần định mệnh Clotho Hy Lạp"),
    ("073372", "coccinellidaes", "noun", "/ˌkɒksɪnɪˈlɪdiːz/", "họ Bọ rùa ăn rệp (cánh cứng)"),
    ("073373", "columbites", "noun", "/kəˈlʌmbaɪts/", "quặng khoáng vật columbite"),
    ("073374", "comfits", "noun", "/ˈkʌmfɪts/", "kẹo bọc đường nhân hạt (từ cổ)"),
    ("073375", "concentricities", "noun", "/ˌkɒnsɛnˈtrɪsɪtiz/", "tính đồng tâm cùng chung tâm điểm"),
    ("073376", "coniums", "noun", "/ˈkoʊniəmz/", "cây độc cần Địa Trung Hải Conium"),
    ("073377", "coprinuses", "noun", "/kəˈpraɪnəsɪz/", "chi Nấm mực tự tan Coprinus"),
    ("073378", "cordierites", "noun", "/ˈkɔːrdiəˌraɪts/", "khoáng vật đá iolit cordierite"),
    ("073379", "cordylines", "noun", "/kɔːrˈdɪlɪnz/", "cây huyết dụ phất dụ chi Cordyline"),
    ("073380", "crocodyli", "noun", "/ˌkrɒkəˈdaɪlaɪ/", "chi Cá sấu thực thụ (Crocodylus)"),
    ("073381", "cybercafes", "noun", "/ˈsaɪbərkæˌfeɪz/", "quán cà phê kết hợp máy tính mạng"),
    ("073382", "cyclobenzaprines", "noun", "/ˌsaɪkloʊˈbɛnzəˌpriːnz/", "thuốc giãn cơ cyclobenzaprine"),
    ("073383", "cyprinids", "noun", "/ˈsɪprɪnɪdz/", "loài cá thuộc họ Cá chép"),
    ("073384", "declivities", "noun", "/dɪˈklɪvɪtiz/", "triền dốc thoai thoải đi xuống"),
    ("073385", "deixises", "noun", "/ˈdaɪksɪsɪz/", "phép trực chỉ ngữ dụng học (deixis)"),
    ("073386", "differentias", "noun", "/ˌdɪfəˈrɛnʃəz/", "đặc điểm khu biệt loài (logic học)"),
    ("073387", "divaricated", "verb", "/daɪˈværɪˌkeɪtɪd/", "đã phân chẽ đôi rẽ nhánh tỏa rộng"),
    ("073388", "divaricates", "verb", "/daɪˈværɪˌkeɪts/", "phân chẽ đôi rẽ nhánh rộng ra"),
    ("073389", "divaricating", "verb", "/daɪˈværɪˌkeɪtɪŋ/", "đang phân chẽ đôi rẽ nhánh rộng"),
    ("073390", "elasmobranches", "noun", "/ɪˈlæzməˌbræŋks/", "phân lớp Cá sụn mang bản (cá mập)"),
    ("073391", "electrocardiographs", "noun", "/ɪˌlɛktroʊˈkɑːrdiəˌɡræfs/", "máy đo ghi điện tâm đồ (ECG)"),
    ("073392", "embolectomies", "noun", "/ˌɛmbəˈlɛktəmiz/", "phẫu thuật lấy cục nghẽn mạch"),
    ("073393", "epicenes", "noun", "/ˈɛpɪˌsiːnz/", "từ dùng chung hai giống; lưỡng tính"),
    ("073394", "ethologists", "noun", "/iːˈθɒlədʒɪsts/", "nhà nghiên cứu tập tính động vật"),
    ("073395", "exhibitioners", "noun", "/ˌɛksɪˈbɪʃənərz/", "sinh viên nhận học bổng đại học Anh"),
    ("073396", "exorcized", "verb", "/ˈɛksɔːrˌsaɪzd/", "đã trừ tà xua đuổi tà ma (biến thể)"),
    ("073397", "exorcizes", "verb", "/ˈɛksɔːrˌsaɪzɪz/", "trừ tà xua đuổi ma quỷ (biến thể)"),
    ("073398", "exorcizing", "verb", "/ˈɛksɔːrˌsaɪzɪŋ/", "đang trừ tà xua đuổi ma quỷ"),
    ("073399", "flecainides", "noun", "/flɪˈkeɪˌnaɪdz/", "thuốc chống loạn nhịp flecainide"),
    ("073400", "forcemeats", "noun", "/ˈfɔːrsˌmiːts/", "thịt cá băm nhuyễn tẩm gia vị nhồi"),
    ("073401", "fosburies", "noun", "/ˈfɒzbəriz/", "vận động viên nhảy cao Dick Fosbury"),
    ("073402", "gammopathies", "noun", "/ɡæˈmɒpəθiz/", "bệnh lý tăng bất thường globulin"),
]

with open("scratch/b35_r07_raw_p4.json") as f:
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

with open("scratch/b35_r07_p4.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r07_p4.json OK")
