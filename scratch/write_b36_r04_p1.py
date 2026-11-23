import json

rows = [
    ("076503", "phytogeographical", "adj", "/ˌfaɪtoʊˌdʒiːəˈɡræfɪkəl/", "thuộc địa lý thực vật"),
    ("076504", "phytogeography", "noun", "/ˌfaɪtoʊdʒiˈɑːɡrəfi/", "địa lý học thực vật"),
    ("076505", "phytography", "noun", "/faɪˈtɒɡrəfi/", "thực vật học mô tả"),
    ("076506", "phytolaccaceae", "noun", "/ˌfaɪtoʊləˈkeɪsiː/", "họ Thương lục (Phytolaccaceae)"),
    ("076507", "phytolith", "noun", "/ˈfaɪtəlɪθ/", "thể khoáng thực vật (phytolith)"),
    ("076508", "phytology", "noun", "/faɪˈtɒlədʒi/", "thực vật học (cách gọi cũ)"),
    ("076509", "phytomastigina", "noun", "/ˌfaɪtoʊmæstɪˈdʒaɪnə/", "phân lớp Trùng roi thực vật"),
    ("076510", "phytonadione", "noun", "/ˌfaɪtoʊnəˈdaɪoʊn/", "vitamin K1 (phytonadion)"),
    ("076511", "phytophagic", "adj", "/ˌfaɪtəˈfeɪdʒɪk/", "ăn thực vật (động vật)"),
    ("076512", "phytophilous", "adj", "/faɪˈtɒfɪləs/", "ưa sống trên thực vật"),
    ("076513", "phytotoxin", "noun", "/ˌfaɪtoʊˈtɒksɪn/", "độc tố nguồn gốc thực vật"),
    ("076514", "phytozoa", "noun", "/ˌfaɪtəˈzoʊə/", "động vật hình cây (sinh vật)"),
    ("076515", "phytozoon", "noun", "/ˌfaɪtəˈzoʊɒn/", "động vật hình cây (sinh vật)"),
    ("076516", "piacular", "adj", "/paɪˈækjələr/", "để chuộc tội; có tội nặng"),
    ("076517", "piaffe", "noun", "/piˈæf/", "bước dậm tại chỗ (môn cưỡi ngựa)"),
    ("076518", "piaffer", "noun", "/piˈæfər/", "bước đi dậm chân tại chỗ (ngựa)"),
    ("076519", "pianette", "noun", "/ˌpiːəˈnɛt/", "đàn piano đứng cỡ nhỏ"),
    ("076520", "pianino", "noun", "/ˌpiːəˈniːnoʊ/", "đàn piano đứng cỡ nhỏ"),
    ("076521", "pianists", "noun", "/ˈpiːənɪsts/", "nghệ sĩ dương cầm (piano)"),
    ("076522", "piaster", "noun", "/piˈæstər/", "đồng bạc piastre (tiền tệ)"),
    ("076523", "pibgorn", "noun", "/ˈpɪbɡɔːrn/", "kèn sừng sậy Xứ Wales (pibgorn)"),
    ("076524", "pibit", "noun", "/ˈpɪbɪt/", "đơn vị dữ liệu pebibit (Pibit)"),
    ("076525", "picamar", "noun", "/ˈpɪkəmɑːr/", "chất đắng picamar (hắc ín gỗ)"),
    ("076526", "picaninny", "noun", "/ˈpɪkənɪni/", "từ miệt thị cũ chỉ trẻ da đen"),
    ("076527", "picariae", "noun", "/pɪˈkɛriiː/", "bộ Chim gõ kiến cũ (Picariae)"),
    ("076528", "picaroon", "noun", "/ˌpɪkəˈruːn/", "kẻ bất lương; tên cướp biển"),
    ("076529", "picayunish", "adj", "/ˌpɪkəˈjuːnɪʃ/", "tầm thường, nhỏ nhặt, keo kiệt"),
    ("076530", "piccaninny", "noun", "/ˈpɪkənɪni/", "từ miệt thị cũ chỉ trẻ da đen"),
    ("076531", "piccoloist", "noun", "/ˈpɪkəloʊɪst/", "nhạc công thổi sáo piccolo"),
    ("076532", "piccolos", "noun", "/ˈpɪkəloʊz/", "sáo nhỏ âm cao (piccolo)"),
    ("076533", "pice", "noun", "/paɪs/", "đồng xu nhỏ pice (Ấn Độ cũ)"),
    ("076534", "pichiciago", "noun", "/ˌpɪtʃiˈsjɑːɡoʊ/", "con ta-tu tiên hồng (Argentina)"),
    ("076535", "pichiciego", "noun", "/ˌpɪtʃiˈsjeɪɡoʊ/", "con ta-tu tiên hồng (Argentina)"),
    ("076536", "picidae", "noun", "/ˈpɪsɪdiː/", "họ Chim gõ kiến (Picidae)"),
    ("076537", "piciformes", "noun", "/ˌpɪsɪˈfɔːrmiːz/", "bộ Chim gõ kiến (Piciformes)"),
    ("076538", "pickaback", "adv", "/ˈpɪkəbæk/", "cõng trên lưng; chở lồng toa tàu"),
    ("076539", "pickaxed", "verb", "/ˈpɪkækst/", "đã đào bổ bằng cuốc chim"),
    ("076540", "pickaxes", "verb", "/ˈpɪkæksɪz/", "đào bổ bằng cuốc chim"),
    ("076541", "pickaxing", "verb", "/ˈpɪkæksɪŋ/", "đào bổ bằng cuốc chim"),
    ("076542", "picked", "verb", "/pɪkt/", "đã chọn lọc; đã hái; đã gảy đàn"),
    ("076543", "pickerelweed", "noun", "/ˈpɪkərəlˌwiːd/", "cây rau mác nước Bắc Mỹ"),
    ("076544", "pickeringia", "noun", "/ˌpɪkəˈrɪndʒiə/", "chi cây bụi gai chaparral Mỹ"),
    ("076545", "picketed", "verb", "/ˈpɪkɪtɪd/", "đã lập hàng rào; đứng biểu tình"),
    ("076546", "picketing", "verb", "/ˈpɪkɪtɪŋ/", "lập hàng rào; đứng biểu tình"),
    ("076547", "pickets", "noun", "/ˈpɪkɪts/", "cọc hàng rào; người đứng biểu tình"),
    ("076548", "pickleball", "noun", "/ˈpɪkəlˌbɔːl/", "môn thể thao vợt pickleball"),
    ("076549", "pickleballs", "noun", "/ˈpɪkəlˌbɔːlz/", "môn pickleball; bóng pickleball"),
    ("076550", "picklepuss", "noun", "/ˈpɪkəlˌpʊs/", "người mặt mày cau có ủ rũ"),
    ("076551", "pickles", "verb", "/ˈpɪkəlz/", "ngâm dấm muối chua (dưa góp)"),
    ("076552", "pickling", "verb", "/ˈpɪklɪŋ/", "ngâm dấm muối chua (dưa góp)"),
    ("076553", "picklock", "noun", "/ˈpɪklɒk/", "kẻ phá khóa; dụng cụ mở khóa"),
    ("076554", "picklocks", "noun", "/ˈpɪklɒks/", "kẻ phá khóa; dụng cụ mở khóa"),
    ("076555", "picknicker", "noun", "/ˈpɪknɪkər/", "người đi dã ngoại (picnic)"),
    ("076556", "picks", "verb", "/pɪks/", "chọn lọc; hái; gảy đàn"),
    ("076557", "pickthank", "noun", "/ˈpɪkθæŋk/", "kẻ nịnh hót xu nịnh (từ cổ)"),
    ("076558", "pickthanks", "noun", "/ˈpɪkθæŋks/", "kẻ nịnh hót xu nịnh (từ cổ)"),
    ("076559", "pickups", "noun", "/ˈpɪkʌps/", "xe bán tải; đầu thu âm; sự đón"),
    ("076560", "pickwikian", "adj", "/pɪkˈwɪkiən/", "hiểu theo nghĩa bóng riêng biệt"),
    ("076561", "picnicker", "noun", "/ˈpɪknɪkər/", "người đi dã ngoại (picnic)"),
    ("076562", "pico", "noun", "/ˈpiːkoʊ/", "tiền tố pico (10 mũ âm 12)"),
    ("076563", "picofarad", "noun", "/ˌpiːkoʊˈfærəd/", "đơn vị điện dung picôfara (pF)"),
    ("076564", "picoides", "noun", "/pɪˈkɔɪdiːz/", "chi chim gõ kiến ba ngón Picoides"),
    ("076565", "picometer", "noun", "/ˈpiːkoʊˌmiːtər/", "đơn vị đo độ dài picômét (pm)"),
    ("076566", "picometre", "noun", "/ˈpiːkoʊˌmiːtər/", "đơn vị đo độ dài picômét (pm)"),
    ("076567", "picotee", "noun", "/ˈpɪkətiː/", "hoa cẩm chướng viền cánh khác màu"),
    ("076568", "picovolt", "noun", "/ˈpiːkoʊˌvoʊlt/", "đơn vị điện áp picôvôn (pV)"),
    ("076569", "picquet", "noun", "/pɪˈkɛt/", "chốt canh gác; trò chơi bài piquet"),
    ("076570", "picrasma", "noun", "/pɪˈkræzmə/", "chi cây khổ mộc (Picrasma)"),
    ("076571", "picric", "adj", "/ˈpɪkrɪk/", "thuộc axit picric (thuốc nổ vàng)"),
    ("076572", "picris", "noun", "/ˈpaɪkrɪs/", "chi cây cúc đắng (Picris)"),
    ("076573", "pics", "noun", "/pɪks/", "hình ảnh; phim (khẩu ngữ)"),
    ("076574", "pictogram", "noun", "/ˈpɪktəɡræm/", "ký hiệu tượng hình; biểu đồ tranh"),
    ("076575", "pictograms", "noun", "/ˈpɪktəɡræmz/", "ký hiệu tượng hình; biểu đồ tranh"),
    ("076576", "pictographically", "adv", "/ˌpɪktəˈɡræfɪkli/", "bằng ký hiệu chữ tượng hình"),
    ("076577", "pictography", "noun", "/pɪkˈtɒɡrəfi/", "hệ thống chữ viết bằng hình vẽ"),
    ("076578", "pictoriality", "noun", "/pɪkˌtɔːriˈælɪti/", "tính chất giàu hình ảnh, sinh động"),
    ("076579", "pictural", "adj", "/ˈpɪktʃərəl/", "thuộc tranh vẽ; sinh động như tranh"),
    ("076580", "picturedrome", "noun", "/ˈpɪktʃərdroʊm/", "rạp chiếu phim (từ cũ Anh)"),
    ("076581", "pictures", "verb", "/ˈpɪktʃərz/", "vẽ tranh; hình dung; chụp ảnh"),
    ("076582", "picul", "noun", "/ˈpɪkəl/", "đơn vị tạ châu Á (picul, 60 kg)"),
    ("076583", "piculet", "noun", "/ˈpɪkjəlɪt/", "chim gõ kiến lùn (piculet)"),
    ("076584", "picumnus", "noun", "/pɪˈkʌmnəs/", "chi chim gõ kiến lùn (Picumnus)"),
    ("076585", "pidginization", "noun", "/ˌpɪdʒɪnaɪˈzeɪʃən/", "quá trình hình thành tiếng bồi"),
    ("076586", "pidginize", "verb", "/ˈpɪdʒɪnaɪz/", "biến đổi thành ngôn ngữ bồi"),
    ("076587", "pidlimdi", "noun", "/pɪdˈlɪmdi/", "tiếng Pidlimdi (ngôn ngữ Nigeria)"),
    ("076588", "pieced", "verb", "/piːst/", "đã ghép nối lại, vá chắp mảnh"),
    ("076589", "piecer", "noun", "/ˈpiːsər/", "thợ nối sợi đứt (trong xưởng dệt)"),
    ("076590", "pieces", "verb", "/ˈpiːsɪz/", "ghép nối lại, vá chắp từng mảnh"),
    ("076591", "piecewise", "adv", "/ˈpiːsˌwaɪz/", "từng mảnh; từng khúc một (toán)"),
    ("076592", "pieceworker", "noun", "/ˈpiːsˌwɜːrkər/", "công nhân ăn lương theo sản phẩm"),
    ("076593", "piecing", "verb", "/ˈpiːsɪŋ/", "ghép nối lại, vá chắp từng mảnh"),
    ("076594", "piecrust", "noun", "/ˈpaɪkrʌst/", "vỏ bánh nướng (bánh tart, pie)"),
    ("076595", "pieman", "noun", "/ˈpaɪmən/", "người bán bánh nướng nhân (pie)"),
    ("076596", "piemen", "noun", "/ˈpaɪmən/", "người bán bánh nướng nhân (pie)"),
    ("076597", "pieplant", "noun", "/ˈpaɪplænt/", "cây đại hoàng (làm nhân bánh Mỹ)"),
    ("076598", "pierage", "noun", "/ˈpɪrɪdʒ/", "phí cập bến, thuế cầu tàu"),
    ("076599", "piercer", "noun", "/ˈpɪrsər/", "mũi khoan, dùi đục lỗ"),
    ("076600", "pierces", "verb", "/ˈpɪrsɪz/", "đâm xuyên thủng, chọc thủng"),
    ("076601", "pierid", "noun", "/ˈpaɪərɪd/", "bướm cải trắng (họ Pieridae)"),
    ("076602", "pieridae", "noun", "/paɪˈɛrɪdiː/", "họ Bướm cải trắng (Pieridae)"),
]

with open("scratch/b36_r04_raw_p1.json", "r", encoding="utf-8") as f:
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

with open("scratch/b36_r04_p1.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b36_r04_p1 saved OK")
