import json

items = [
    ("068303", "plasms", "noun", "/ˈplæzəmz/", "nguyên sinh chất; chất nền tế bào"),
    ("068304", "poaceaes", "noun", "/poʊˈeɪʃiz/", "họ Hòa thảo gồm lúa ngô tre cỏ"),
    ("068305", "professionalisations", "noun", "/prəˌfɛʃənəlaɪˈzeɪʃənz/", "quá trình chuyên nghiệp hóa ngành"),
    ("068306", "punctums", "noun", "/ˈpʌŋktəmz/", "điểm chi tiết nhỏ gây xúc động"),
    ("068307", "radomes", "noun", "/ˈreɪˌdoʊmz/", "vòm mái che bảo vệ ăng-ten rađa"),
    ("068308", "robitussins", "noun", "/ˌroʊbɪˈtʌsɪnz/", "thuốc siro trị ho Robitussin"),
    ("068309", "roustabouts", "noun", "/ˈraʊstəˌbaʊts/", "công nhân bốc vác hoặc giàn khoan"),
    ("068310", "salesladies", "noun", "/ˈseɪlzˌleɪdiz/", "nữ nhân viên bán hàng tại quầy"),
    ("068311", "salsifies", "noun", "/ˈsælsɪfiz/", "cây diếp củ rễ trắng ăn được"),
    ("068312", "saponifications", "noun", "/səˌpɒnɪfɪˈkeɪʃənz/", "phản ứng xà phòng hóa este dầu mỡ"),
    ("068313", "sawfishes", "noun", "/ˈsɔːˌfɪʃɪz/", "cá đao có mỏ dài hình lưỡi cưa"),
    ("068314", "schoolbooks", "noun", "/ˈskuːlˌbʊks/", "sách giáo khoa dùng ở trường học"),
    ("068315", "scoters", "noun", "/ˈskoʊtərz/", "vịt biển lặn lông sẫm scoter"),
    ("068316", "sculptresses", "noun", "/ˈskʌlptrɪsɪz/", "nữ nghệ sĩ điêu khắc tạc tượng"),
    ("068317", "sensitisations", "noun", "/ˌsɛnsɪtaɪˈzeɪʃənz/", "quá trình gây mẫn cảm dị ứng"),
    ("068318", "shirtier", "adj", "/ˈʃɜːrtiər/", "cáu kỉnh dễ bực bội hơn (lóng)"),
    ("068319", "shirtiest", "adj", "/ˈʃɜːrtiɪst/", "cáu kỉnh dễ bực bội nhất (lóng)"),
    ("068320", "sittas", "noun", "/ˈsɪtəz/", "chim trèo cây thuộc chi Sitta"),
    ("068321", "snoopers", "noun", "/ˈsnuːpərz/", "kẻ rình mò tọc mạch dò xét chuyện"),
    ("068322", "sodalities", "noun", "/soʊˈdælɪtiz/", "hội đoàn tông đồ hoặc huynh đệ"),
    ("068323", "spandrels", "noun", "/ˈspændrəlz/", "góc vòm tường; đặc điểm phụ kèm"),
    ("068324", "stiflers", "noun", "/ˈstaɪflərz/", "người kìm hãm bóp nghẹt tự do"),
    ("068325", "stogies", "noun", "/ˈstoʊɡiz/", "xì gà điếu dài giá rẻ bình dân"),
    ("068326", "sulfamethoxazoles", "noun", "/ˌsʌlfəməˈθɒksəzoʊlz/", "thuốc kháng sinh sulfamethoxazol"),
    ("068327", "sulfonamides", "noun", "/sʌlˈfɒnəˌmaɪdz/", "nhóm thuốc kháng khuẩn sulfonamid"),
    ("068328", "tabeses", "noun", "/ˈteɪbiːsiːz/", "chứng suy mòn gầy còm teo tủy"),
    ("068329", "tetrapods", "noun", "/ˈtɛtrəˌpɒdz/", "động vật có xương sống bốn chi"),
    ("068330", "theophanies", "noun", "/θiˈɒfəniz/", "sự hiển linh hiện hình của thần"),
    ("068331", "transfused", "verb", "/trænzˈfjuːzd/", "đã truyền máu hoặc truyền dịch"),
    ("068332", "transfuses", "verb", "/trænzˈfjuːzɪz/", "truyền máu hoặc dịch qua tĩnh mạch"),
    ("068333", "transfusing", "verb", "/trænzˈfjuːzɪŋ/", "đang truyền máu vào cơ thể"),
    ("068334", "treaters", "noun", "/ˈtriːtərz/", "người chiêu đãi; người điều trị"),
    ("068335", "trevithicks", "noun", "/trəˈvɪθɪks/", "kỹ sư đầu máy hơi nước Trevithick"),
    ("068336", "tussauds", "noun", "/tuːˈsoʊz/", "bảo tàng sáp hoặc bà Marie Tussaud"),
    ("068337", "tyramines", "noun", "/ˈtaɪrəˌmiːnz/", "hợp chất amin tyramin tăng huyết áp"),
    ("068338", "undergirded", "verb", "/ˌʌndərˈɡɜːrdɪd/", "đã chống đỡ củng cố nền tảng vững"),
    ("068339", "undergirds", "verb", "/ˌʌndərˈɡɜːrdz/", "nâng đỡ củng cố từ bên dưới"),
    ("068340", "undergirt", "verb", "/ˌʌndərˈɡɜːrt/", "đã chống đỡ củng cố vững chắc"),
    ("068341", "ussses", "noun", "/ˌjuː ɛs ɛs ˈiːz/", "Cơ quan Mật vụ Hoa Kỳ USSS"),
    ("068342", "vasoconstrictors", "noun", "/ˌveɪzoʊkənˈstrɪktərz/", "chất gây co thắt mạch máu"),
    ("068343", "veaus", "noun", "/voʊz/", "thịt bê non (từ mượn tiếng Pháp)"),
    ("068344", "wailers", "noun", "/ˈweɪlərz/", "người khóc than ai oán sầu thảm"),
    ("068345", "wangled", "verb", "/ˈwæŋɡəld/", "đã xoay xở đạt được bằng mẹo khéo"),
    ("068346", "wangles", "noun", "/ˈwæŋɡəlz/", "mánh khóe xoay xở khéo léo"),
    ("068347", "winkers", "noun", "/ˈwɪŋkərz/", "tấm che mắt ngựa; người nháy mắt"),
    ("068348", "xenografts", "noun", "/ˈzɛnəˌɡræfts/", "mô tạng cấy ghép từ loài khác"),
    ("068349", "aftereffects", "noun", "/ˈæftərɪˌfɛkts/", "di chứng hậu quả kéo dài về sau"),
    ("068350", "ambulations", "noun", "/ˌæmbjəˈleɪʃənz/", "khả năng đi lại sau phẫu thuật"),
    ("068351", "anaxagorases", "noun", "/ˌænækˈsæɡərəsɪz/", "triết gia Hy Lạp cổ Anaxagoras"),
    ("068352", "antipyretics", "noun", "/ˌæntipaɪˈrɛtɪks/", "thuốc hạ sốt giảm thân nhiệt"),
    ("068353", "antispasmodics", "noun", "/ˌæntispæzˈmɒdɪks/", "thuốc chống co thắt cơ trơn"),
    ("068354", "approvers", "noun", "/əˈpruːvərz/", "người phê duyệt ký chấp thuận"),
    ("068355", "aqualungs", "noun", "/ˈækwəˌlʌŋz/", "bình dưỡng khí thở lặn dưới nước"),
    ("068356", "austenites", "noun", "/ˈɔːstəˌnaɪts/", "pha tinh thể thép austenit"),
    ("068357", "avowing", "verb", "/əˈvaʊɪŋ/", "đang công khai tuyên bố thừa nhận"),
    ("068358", "avows", "verb", "/əˈvaʊz/", "tuyên bố công khai thẳng thắn"),
    ("068359", "biodegraded", "verb", "/ˌbaɪoʊdɪˈɡreɪdɪd/", "đã phân hủy sinh học tự nhiên"),
    ("068360", "biodegrades", "verb", "/ˌbaɪoʊdɪˈɡreɪdz/", "phân hủy sinh học nhờ vi sinh"),
    ("068361", "biodegrading", "verb", "/ˌbaɪoʊdɪˈɡreɪdɪŋ/", "đang phân hủy sinh học tự nhiên"),
    ("068362", "bisections", "noun", "/baɪˈsɛkʃənz/", "phép chia đôi thành hai phần đều"),
    ("068363", "borneans", "noun", "/ˈbɔːrniənz/", "cư dân sinh sống trên đảo Borneo"),
    ("068364", "camarillas", "noun", "/ˌkæməˈrɪləz/", "bè phái cố vấn lũng đoạn ngầm"),
    ("068365", "charwomen", "noun", "/ˈtʃɑːrˌwɪmən/", "nữ nhân viên dọn dẹp tạp vụ (Anh)"),
    ("068366", "chewers", "noun", "/ˈtʃuːərz/", "người nhai thức ăn hoặc nhai kẹo"),
    ("068367", "chieftainships", "noun", "/ˈtʃiːftənʃɪps/", "chức vị thủ lĩnh hoặc tù trưởng"),
    ("068368", "chloroses", "noun", "/klɔːˈroʊsiːz/", "bệnh vàng lá; thiếu máu da xanh"),
    ("068369", "circumscriptions", "noun", "/ˌsɜːrkəmˈskrɪpʃənz/", "sự khoanh vùng giới hạn; vòng chữ"),
    ("068370", "conceptualisms", "noun", "/kənˈsɛptʃʊəˌlɪzəmz/", "thuyết khái niệm luận triết học"),
    ("068371", "congeners", "noun", "/ˈkɒndʒənərz/", "sinh vật cùng chi; chất đồng loại"),
    ("068372", "controversialists", "noun", "/ˌkɒntrəˈvɜːrʃəlɪsts/", "người giỏi hoặc hay tranh luận"),
    ("068373", "cornhuskers", "noun", "/ˈkɔːrnˌhʌskərz/", "người bóc bẹ ngô; dân bang Nebraska"),
    ("068374", "crockets", "noun", "/ˈkrɒkɪts/", "họa tiết lá uốn cong kiến trúc"),
    ("068375", "curcumas", "noun", "/ˈkɜːrkjʊməz/", "cây nghệ thuộc chi Curcuma"),
    ("068376", "cyperuses", "noun", "/saɪˈpɪərəsɪz/", "cây cói lác thuộc chi Cyperus"),
    ("068377", "dagdas", "noun", "/ˈdɑːɡdəz/", "thần tối cao Dagda thần thoại"),
    ("068378", "daggas", "noun", "/ˈdɑːɡəz/", "cây sư tử tai; cần sa ở Nam Phi"),
    ("068379", "damselflies", "noun", "/ˈdæmzəlˌflaɪz/", "chuồn chuồn kim thân mảnh nhỏ"),
    ("068380", "deathblows", "noun", "/ˈdɛθˌbloʊz/", "đòn chí mạng gây sụp đổ hoàn toàn"),
    ("068381", "decriminalised", "verb", "/diːˈkrɪmɪnəˌlaɪzd/", "đã phi hình sự hóa hành vi"),
    ("068382", "decriminalises", "verb", "/diːˈkrɪmɪnəˌlaɪzɪz/", "phi hình sự hóa bỏ tội danh"),
    ("068383", "decriminalising", "verb", "/diːˈkrɪmɪnəˌlaɪzɪŋ/", "đang phi hình sự hóa hành vi"),
    ("068384", "defaulters", "noun", "/dɪˈfɔːltərz/", "người vỡ nợ quỵt nợ; kẻ vắng mặt"),
    ("068385", "demonisations", "noun", "/ˌdiːmənaɪˈzeɪʃənz/", "hành vi bôi nhọ thành ác quỷ"),
    ("068386", "dionysiae", "noun", "/ˌdaɪəˈnɪʒiː/", "lễ hội rượu vang thần Dionysus"),
    ("068387", "dragomans", "noun", "/ˈdræɡəmənz/", "thông dịch viên khu vực Trung Đông"),
    ("068388", "dunghills", "noun", "/ˈdʌŋˌhɪlz/", "đống phân chuồng ủ trên trang trại"),
    ("068389", "ebns", "noun", "/ˌiː biː ˈɛnz/", "hướng đông chếch bắc EBN (la bàn)"),
    ("068390", "electrotherapies", "noun", "/ɪˌlɛktroʊˈθɛrəpiz/", "liệu pháp điện vật lý trị liệu"),
    ("068391", "epistemes", "noun", "/ˌɛpɪˈstiːmz/", "hệ thống tri thức nền tảng thời đại"),
    ("068392", "eratos", "noun", "/ɛˈrɑːtoʊz/", "nàng thơ tình ca Erato Hy Lạp cổ"),
    ("068393", "escudos", "noun", "/ɛˈskuːdoʊz/", "đơn vị tiền tệ escudo Bồ Đào Nha"),
    ("068394", "felicitations", "noun", "/fəˌlɪsɪˈteɪʃənz/", "lời chúc mừng trân trọng chân thành"),
    ("068395", "flugelhorns", "noun", "/ˈfluːɡəlˌhɔːrnz/", "kèn đồng trầm ấm flugelhorn"),
    ("068396", "foundresses", "noun", "/ˈfaʊndrɪsɪz/", "nữ sáng lập viên tổ chức trường"),
    ("068397", "groovers", "noun", "/ˈɡruːvərz/", "máy xẻ rãnh gỗ; người sành điệu"),
    ("068398", "hypersomnias", "noun", "/ˌhaɪpərˈsɒmniəz/", "chứng ngủ nhiều quá mức ban ngày"),
    ("068399", "ichthyosaurs", "noun", "/ˈɪkθiəˌsɔːrz/", "bò sát biển ngư long tiền sử"),
    ("068400", "ichthyosauruses", "noun", "/ˌɪkθiəˈsɔːrəsɪz/", "loài bò sát ngư long giống cá heo"),
    ("068401", "imbecilities", "noun", "/ˌɪmbɪˈsɪlɪtiz/", "hành vi dại dột ngu ngốc; đần độn"),
    ("068402", "incudes", "noun", "/ɪŋˈkjuːdiːz/", "xương đe nằm trong tai giữa"),
]

with open("scratch/b34_r07_raw_p4.json") as f:
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

with open("scratch/b34_r07_p4.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r07_p4.json OK")
