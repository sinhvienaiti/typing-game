import json

rows = [
    ("074503", "clavicepses", "noun", "/ˈklævɪsɛpsɪz/", "nấm cựa gà (chi Claviceps)"),
    ("074504", "claxoned", "verb", "/ˈklæksənd/", "đã bấm còi xe; bóp còi báo động"),
    ("074505", "claxoning", "verb", "/ˈklæksənɪŋ/", "bấm còi xe; bóp còi báo động"),
    ("074506", "claxons", "noun", "/ˈklæksənz/", "còi báo động; còi xe ô tô"),
    ("074507", "cleantheses", "noun", "/kliˈænθɪsiːz/", "triết gia Khắc kỷ Cleanthes"),
    ("074508", "clegs", "noun", "/klɛɡz/", "ruồi trâu; ruồi hút máu"),
    ("074509", "cockcrows", "noun", "/ˈkɒkkroʊz/", "lúc gà gáy sáng; rạng đông"),
    ("074510", "corvees", "noun", "/kɔːrˈveɪz/", "lao dịch cưỡng bức; sưu dịch"),
    ("074511", "crowberries", "noun", "/ˈkroʊˌbɛriz/", "quả mọng quạ (Empetrum)"),
    ("074512", "cycloserines", "noun", "/ˌsaɪkloʊˈsɛriːnz/", "kháng sinh trị lao cycloserine"),
    ("074513", "diacetylmorphines", "noun", "/daɪˌæsɪtɪlˈmɔːrfiːnz/", "heroin; chất gây nghiện bạch phiến"),
    ("074514", "dowitchers", "noun", "/ˈdaʊɪtʃərz/", "chim choắt mỏ dài (Bắc Mỹ)"),
    ("074515", "durras", "noun", "/ˈdʊrəz/", "cây cao lương trắng (lúa miến)"),
    ("074516", "echinochloas", "noun", "/ɪˌkaɪnəˈkloʊəz/", "chi cỏ lồng vực (Echinochloa)"),
    ("074517", "elisabethvilles", "noun", "/ɪˈlɪzəbəθˌvɪlz/", "tp. Lubumbashi cũ (Elisabethville)"),
    ("074518", "empaneled", "verb", "/ɪmˈpænəld/", "đã lập danh sách bồi thẩm đoàn"),
    ("074519", "empaneling", "verb", "/ɪmˈpænəlɪŋ/", "lập danh sách bồi thẩm đoàn"),
    ("074520", "empanelled", "verb", "/ɪmˈpænəld/", "đã lập danh sách bồi thẩm đoàn"),
    ("074521", "empanelling", "verb", "/ɪmˈpænəlɪŋ/", "lập danh sách bồi thẩm đoàn"),
    ("074522", "empanels", "verb", "/ɪmˈpænəlz/", "lập danh sách bồi thẩm đoàn"),
    ("074523", "enjambments", "noun", "/ɪnˈdʒæmbmənts/", "phép vắt dòng (thơ ca)"),
    ("074524", "eschars", "noun", "/ˈɛskɑːrz/", "vảy hoại tử vết bỏng (y học)"),
    ("074525", "flashguns", "noun", "/ˈflæʃɡʌnz/", "đèn chớp máy ảnh; đèn flash"),
    ("074526", "flexerils", "noun", "/ˈflɛksərɪlz/", "thuốc giãn cơ Flexeril"),
    ("074527", "furcated", "verb", "/ˈfɜːrkeɪtɪd/", "đã chia nhánh; đã rẽ chạc"),
    ("074528", "furcates", "verb", "/ˈfɜːrkeɪts/", "chia nhánh; rẽ chạc"),
    ("074529", "furcating", "verb", "/ˈfɜːrkeɪtɪŋ/", "chia nhánh; rẽ chạc"),
    ("074530", "furculae", "noun", "/ˈfɜːrkjəliː/", "xương đòn chữ V ở chim (xương chạc)"),
    ("074531", "furculas", "noun", "/ˈfɜːrkjələz/", "xương đòn chữ V ở chim (xương chạc)"),
    ("074532", "grassfires", "noun", "/ˈɡræsˌfaɪərz/", "đám cháy đồng cỏ; cháy bãi cỏ"),
    ("074533", "handcars", "noun", "/ˈhændkɑːrz/", "xe goòng đẩy tay (đường sắt)"),
    ("074534", "harborages", "noun", "/ˈhɑːrbərɪdʒɪz/", "nơi trú ẩn; cảng neo đậu an toàn"),
    ("074535", "hayforks", "noun", "/ˈheɪfɔːrks/", "cái chĩa xúc rơm cỏ khô"),
    ("074536", "helves", "noun", "/hɛlvz/", "cán rìu; cán búa; chuôi dao"),
    ("074537", "hematemeses", "noun", "/ˌhiːməˈtɛmɪsiːz/", "chứng nôn ra máu (y học)"),
    ("074538", "huroks", "noun", "/ˈhjʊrɒks/", "nhà bầu sô Sol Hurok (Mỹ)"),
    ("074539", "hypodermises", "noun", "/ˌhaɪpəˈdɜːrmɪsɪz/", "lớp hạ bì (sinh học, thực vật)"),
    ("074540", "inulas", "noun", "/ˈɪnjələz/", "chi cây cúc thiên môn đông (Inula)"),
    ("074541", "jacinths", "noun", "/ˈdʒeɪsɪnθs/", "đá quý hyacinth; ngọc màu cam đỏ"),
    ("074542", "kadikoys", "noun", "/kɑːdɪˈkɔɪz/", "quận Kadikoy (Istanbul, Thổ Nhĩ Kỳ)"),
    ("074543", "kerbalas", "noun", "/ˈkɜːrbələz/", "thành phố thánh địa Karbala (Iraq)"),
    ("074544", "laelias", "noun", "/ˈliːliəz/", "chi phong lan Laelia (Nam Mỹ)"),
    ("074545", "leucocytes", "noun", "/ˈluːkəsaɪts/", "tế bào bạch cầu"),
    ("074546", "lighterages", "noun", "/ˈlaɪtərɪdʒɪz/", "phí vận chuyển hàng bằng xà lan"),
    ("074547", "limners", "noun", "/ˈlɪmnərz/", "họa sĩ vẽ chân dung (cổ); thợ vẽ"),
    ("074548", "loadstars", "noun", "/ˈloʊdstɑːrz/", "sao Bắc Đẩu; ngôi sao dẫn đường"),
    ("074549", "luiks", "noun", "/ˈlœyks/", "thành phố Liège (tên tiếng Hà Lan)"),
    ("074550", "luwians", "noun", "/ˈluːiənz/", "người Luwia cổ; tiếng Luwia"),
    ("074551", "lymantrias", "noun", "/laɪˈmæntriəz/", "chi bướm đêm tơ hại cây (Lymantria)"),
    ("074552", "malthusianisms", "noun", "/mælˈθuːʒənɪzəmz/", "học thuyết dân số Malthus"),
    ("074553", "mangabeys", "noun", "/ˈmæŋɡəbeɪz/", "khỉ mangabey (châu Phi)"),
    ("074554", "mlitts", "noun", "/ˌɛmˈlɪts/", "bằng Thạc sĩ Văn học (MLitt)"),
    ("074555", "mobulas", "noun", "/ˈmɒbjələz/", "cá đuối dơi (chi Mobula)"),
    ("074556", "nondisjunctions", "noun", "/ˌnɒndɪsˈdʒʌŋkʃənz/", "sự không phân ly NST (di truyền)"),
    ("074557", "nswcs", "noun", "/ˌɛnˌɛsˌdʌbəljuːˈsiːz/", "Trung tâm Chiến tranh Mặt biển HQ"),
    ("074558", "overcalls", "noun", "/ˈoʊvərkɔːlz/", "lần tố bài cao hơn (bài bridge)"),
    ("074559", "paramyxoviruses", "noun", "/ˌpærəˌmɪksoʊˈvaɪrəsɪz/", "virus á cúm Paramyxovirus"),
    ("074560", "pelisses", "noun", "/pəˈliːsɪz/", "áo choàng dài cổ lông (lịch sử)"),
    ("074561", "petechias", "noun", "/pəˈtiːkiəz/", "chấm xuất huyết dưới da (y học)"),
    ("074562", "peuls", "noun", "/pɜːlz/", "người Fulani (Tây Phi); tiếng Peul"),
    ("074563", "philters", "noun", "/ˈfɪltərz/", "bùa yêu; thuốc kích tình (cổ)"),
    ("074564", "polypectomies", "noun", "/ˌpɒlɪˈpɛktəmiz/", "phẫu thuật cắt bỏ polyp (y học)"),
    ("074565", "pomologies", "noun", "/pəˈmɒlədʒiz/", "ngành quả học; nghề trồng cây quả"),
    ("074566", "potsherds", "noun", "/ˈpɒtʃɜːrdz/", "mảnh gốm vỡ (khảo cổ học)"),
    ("074567", "pouffes", "noun", "/puːfs/", "ghế đôn tròn thấp; búi tóc phồng"),
    ("074568", "poyangs", "noun", "/pɔːˈjæŋz/", "hồ Bà Dương (Trung Quốc)"),
    ("074569", "psychotrias", "noun", "/saɪˈkɒtriəz/", "chi cây cà phê rừng (Psychotria)"),
    ("074570", "qadhafis", "noun", "/ɡəˈdɑːfiz/", "nhà lãnh đạo Gaddafi (Libya)"),
    ("074571", "quinacrines", "noun", "/ˈkwɪnəkriːnz/", "thuốc trị sốt rét quinacrine"),
    ("074572", "regimentalses", "noun", "/ˌrɛdʒɪˈmɛntəlzɪz/", "quân phục trung đoàn (từ cổ)"),
    ("074573", "rhadamanthuses", "noun", "/ˌrædəˈmænθəsɪz/", "thẩm phán âm phủ Rhadamanthus"),
    ("074574", "ruralities", "noun", "/rʊˈrælɪtiz/", "tính chất nông thôn; nét đồng quê"),
    ("074575", "saponarias", "noun", "/ˌsæpəˈnɛriəz/", "chi cây xà phòng (Saponaria)"),
    ("074576", "saxitoxins", "noun", "/ˌsæksɪˈtɒksɪnz/", "độc tố tảo biển saxitoxin"),
    ("074577", "scenarists", "noun", "/ˈsiːnərɪsts/", "nhà biên kịch; tác giả kịch bản"),
    ("074578", "shivahs", "noun", "/ˈʃɪvəz/", "nghi lễ để tang 7 ngày (Do Thái)"),
    ("074579", "shooflies", "noun", "/ˈʃuːflaɪz/", "ghế bập bênh; bánh mật shoofly"),
    ("074580", "spermophiluses", "noun", "/spɜːrˈmɒfɪləsɪz/", "chi sóc đất (Spermophilus)"),
    ("074581", "spicules", "noun", "/ˈspɪkjuːlz/", "gai xương; cột khí nóng Mặt Trời"),
    ("074582", "spiks", "noun", "/spɪks/", "từ miệt thị người gốc Latinh"),
    ("074583", "squillae", "noun", "/ˈskwɪliː/", "tôm tít (bề bề, chi Squilla)"),
    ("074584", "squillas", "noun", "/ˈskwɪləz/", "tôm tít (bề bề, chi Squilla)"),
    ("074585", "stemmas", "noun", "/ˈstɛməz/", "phả hệ văn bản cổ; mắt đơn sâu bọ"),
    ("074586", "suntraps", "noun", "/ˈsʌntræps/", "nơi khuất gió hứng nhiều nắng"),
    ("074587", "superstrates", "noun", "/ˈsuːpərstreɪts/", "ngôn ngữ thượng tầng (ngôn ngữ học)"),
    ("074588", "suricatas", "noun", "/ˌsʊrɪˈkɑːtəz/", "chồn đất meerkat (Nam Phi)"),
    ("074589", "tchotchkes", "noun", "/ˈtʃɒtʃkəz/", "đồ trang trí nhỏ; đồ lưu niệm rẻ"),
    ("074590", "thrombocytoses", "noun", "/ˌθrɒmboʊsaɪˈtoʊsiːz/", "chứng tăng tiểu cầu (y học)"),
    ("074591", "turcomans", "noun", "/ˈtɜːrkəmənz/", "người Turkmen; tiếng Turkmen"),
    ("074592", "vendues", "noun", "/vɛnˈduːz/", "cuộc bán đấu giá công khai"),
    ("074593", "whinchats", "noun", "/ˈwɪntʃæts/", "chim sẻ bụi ngực hung (whinchat)"),
    ("074594", "wooers", "noun", "/ˈwuːərz/", "người cầu hôn; kẻ tán tỉnh"),
    ("074595", "worrywarts", "noun", "/ˈwɜːriˌwɔːrts/", "người hay lo âu thái quá"),
    ("074596", "actinomycetes", "noun", "/ˌæktɪnoʊˈmaɪsiːts/", "xạ khuẩn (vi sinh vật)"),
    ("074597", "alcedos", "noun", "/ælˈsiːdoʊz/", "chi chim bói cá (Alcedo)"),
    ("074598", "amorphophalluses", "noun", "/əˌmɔːrfoʊˈfæləsɪz/", "chi khoai nưa, cây xác thối"),
    ("074599", "aspises", "noun", "/ˈæspɪsɪz/", "rắn hổ mang Ai Cập; khiên tròn cổ"),
    ("074600", "barratries", "noun", "/ˈbærətriz/", "gian lận hàng hải; tội xúi kiện"),
    ("074601", "battlewagons", "noun", "/ˈbætəlˌwæɡənz/", "thiết giáp hạm; tàu chiến lớn"),
    ("074602", "bitcheries", "noun", "/ˈbɪtʃəriz/", "thái độ cay nghiệt (từ lóng cũ)"),
]

with open("scratch/b35_r10_raw_p1.json", "r", encoding="utf-8") as f:
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

with open("scratch/b35_r10_p1.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b35_r10_p1 saved OK")
