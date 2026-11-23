import json

items = [
    ("072303", "packinghouses", "noun", "/ˈpækɪŋˌhaʊzɪz/", "xưởng chế biến đóng gói thực phẩm"),
    ("072304", "paleoclimatologies", "noun", "/ˌpeɪlioʊklaɪməˈtɒlədʒiz/", "ngành cổ khí hậu học"),
    ("072305", "pearlites", "noun", "/ˈpɜːrˌlaɪts/", "thép peclit; đá trân châu peclit"),
    ("072306", "pipals", "noun", "/ˈpiːpəlz/", "cây bồ đề linh thiêng Ấn Độ"),
    ("072307", "prodromes", "noun", "/ˈproʊdroʊmz/", "tiền triệu chứng báo trước bệnh"),
    ("072308", "psychopomps", "noun", "/ˈsaɪkəˌpɒmps/", "thần dẫn hồn sang thế giới bên kia"),
    ("072309", "radiolyses", "noun", "/reɪdiˈɒlɪˌsiːz/", "sự phân hủy hóa học do bức xạ"),
    ("072310", "rayonses", "noun", "/ˈreɪɒnzɪz/", "vải hoặc tơ nhân tạo rayon"),
    ("072311", "remilitarizations", "noun", "/ˌriːmɪlɪtəraɪˈzeɪʃənz/", "sự tái vũ trang quân sự hóa lại"),
    ("072312", "rotifers", "noun", "/ˈroʊtɪfərz/", "động vật luân trùng thủy sinh"),
    ("072313", "rutaceaes", "noun", "/ruːˈteɪʃiˌiːz/", "họ Cam chanh thực vật (Rutaceae)"),
    ("072314", "sanitisations", "noun", "/ˌsænɪtaɪˈzeɪʃənz/", "công tác vệ sinh khử trùng (Anh)"),
    ("072315", "santalums", "noun", "/ˈsæntələmz/", "chi Cây đàn hương (Santalum)"),
    ("072316", "scheelites", "noun", "/ˈʃiːlaɪts/", "quặng vonfram canxi scheelit"),
    ("072317", "sexagenarians", "noun", "/ˌsɛksədʒəˈnɛəriənz/", "người ở độ tuổi lục tuần (60–69)"),
    ("072318", "shirtdresses", "noun", "/ˈʃɜːrtˌdrɛsɪz/", "đầm liền dáng áo sơ mi"),
    ("072319", "spelunkers", "noun", "/spɪˈlʌŋkərz/", "người thám hiểm hang động"),
    ("072320", "tangelos", "noun", "/ˈtændʒəˌloʊz/", "quả lai quýt bưởi tangelo"),
    ("072321", "thromboplastins", "noun", "/ˌθrɒmboʊˈplæstɪnz/", "yếu tố đông máu thromboplastin"),
    ("072322", "tidelands", "noun", "/ˈtaɪdˌlændz/", "vùng đất bãi bồi ngập thủy triều"),
    ("072323", "toyohashis", "noun", "/ˌtoʊjoʊˈhɑːʃiz/", "thành phố Toyohashi ở Nhật Bản"),
    ("072324", "triazines", "noun", "/ˈtraɪəˌziːnz/", "hợp chất dị vòng triazin (hóa học)"),
    ("072325", "trichophytons", "noun", "/trɪˈkɒfɪˌtɒnz/", "nấm ngoài da chi Trichophyton"),
    ("072326", "unbends", "verb", "/ʌnˈbɛndz/", "duỗi thẳng ra; trở nên thân mật"),
    ("072327", "valerianas", "noun", "/vəˌlɪəriˈɑːnəz/", "cây nữ lang an thần chi Valeriana"),
    ("072328", "varanuses", "noun", "/ˈværənəsɪz/", "chi Kỳ đà khổng lồ (Varanus)"),
    ("072329", "villeins", "noun", "/ˈvɪlɪnz/", "nông nô lệ thuộc lãnh địa trung cổ"),
    ("072330", "vlamincks", "noun", "/vlɑːˈmæŋks/", "họa sĩ Pháp Maurice de Vlaminck"),
    ("072331", "vomituses", "noun", "/ˈvɒmɪtəsɪz/", "chất nôn ói ra từ dạ dày"),
    ("072332", "acipensers", "noun", "/ˌæsɪˈpɛnsərz/", "chi Cá tầm cổ (Acipenser)"),
    ("072333", "alpinisms", "noun", "/ˈælpɪˌnɪzəmz/", "môn leo núi cao vách băng"),
    ("072334", "angiosarcomas", "noun", "/ˌændʒioʊsɑːrˈkoʊməz/", "ung thư ác tính tế bào mạch máu"),
    ("072335", "ataraxes", "noun", "/ˈætəˌræksɪz/", "thuốc kháng histamin an thần Atarax"),
    ("072336", "autogiros", "noun", "/ˈɔːtoʊˌdʒaɪroʊz/", "máy bay cánh quay tự động autogyro"),
    ("072337", "aviated", "verb", "/ˈeɪviˌeɪtɪd/", "đã điều khiển lái máy bay"),
    ("072338", "aviates", "verb", "/ˈeɪviˌeɪts/", "lái máy bay điều khiển phi cơ"),
    ("072339", "aviating", "verb", "/ˈeɪviˌeɪtɪŋ/", "đang lái điều khiển máy bay"),
    ("072340", "backstays", "noun", "/ˈbækˌsteɪz/", "dây néo chéo giữ cột buồm về sau"),
    ("072341", "bandoneons", "noun", "/bænˈdoʊniənz/", "đàn xếp bandoneon nhạc tango"),
    ("072342", "bedwetters", "noun", "/ˈbɛdˌwɛtərz/", "người hay đái dầm khi ngủ"),
    ("072343", "boulevardiers", "noun", "/ˌbuːləvɑːrˈdjɛərz/", "người sành điệu hay dạo phố Paris"),
    ("072344", "bramas", "noun", "/ˈbrɑːməz/", "chi Cá vền biển sâu (Brama)"),
    ("072345", "bryophytes", "noun", "/ˈbraɪəˌfaɪts/", "ngành Rêu thực vật không mạch"),
    ("072346", "chadars", "noun", "/ˈtʃɑːdərz/", "khăn choàng trùm người phụ nữ Nam Á"),
    ("072347", "chassidims", "noun", "/ˈxɑːsɪdɪmz/", "tín đồ Do Thái giáo Hasid"),
    ("072348", "chokecherries", "noun", "/ˈtʃoʊkˌtʃɛriz/", "quả anh đào dại vị chát Bắc Mỹ"),
    ("072349", "congenerics", "noun", "/ˌkɒndʒəˈnɛrɪks/", "loài sinh vật cùng thuộc một chi"),
    ("072350", "conversos", "noun", "/kɒnˈvɜːrsoʊz/", "người Do Thái cải đạo Công giáo cổ"),
    ("072351", "corrigendas", "noun", "/ˌkɒrɪˈdʒɛndəz/", "bảng đính chính lỗi in trong sách"),
    ("072352", "cryptanalysts", "noun", "/krɪpˈtænəlɪsts/", "chuyên gia phân tích giải mật mã"),
    ("072353", "crystallites", "noun", "/ˈkrɪstəˌlaɪts/", "vi tinh thể trong khoáng vật"),
    ("072354", "currawongs", "noun", "/ˈkʌrəˌwɒŋz/", "chim đen mỏ khỏe currawong của Úc"),
    ("072355", "cuspids", "noun", "/ˈkʌspɪdz/", "răng nanh (nha khoa); đỉnh van tim"),
    ("072356", "dacoities", "noun", "/dəˈkɔɪtiz/", "vụ cướp bóc có vũ trang theo băng"),
    ("072357", "decrescendos", "noun", "/ˌdeɪkrəˈʃɛndoʊz/", "đoạn nhạc giảm âm lượng nhỏ dần"),
    ("072358", "desmodiums", "noun", "/dɛzˈmoʊdiəmz/", "cây tràng quả thuộc chi Desmodium"),
    ("072359", "didelphides", "noun", "/daɪˈdɛlfɪdiːz/", "chi Thú có túi opossum Didelphis"),
    ("072360", "digitarias", "noun", "/ˌdɪdʒɪˈtɛəriəz/", "cỏ chân vịt túc hình chi Digitaria"),
    ("072361", "dipterans", "noun", "/ˈdɪptərənz/", "côn trùng bộ Hai cánh (ruồi, muỗi)"),
    ("072362", "doxazosins", "noun", "/dɒkˈsæzəsɪnz/", "thuốc hạ huyết áp doxazosin"),
    ("072363", "echiums", "noun", "/ˈɛkiəmz/", "cây hoa vòi voi rắn chi Echium"),
    ("072364", "elints", "noun", "/ˈiːlɪnts/", "tình báo tín hiệu điện tử (ELINT)"),
    ("072365", "elodeas", "noun", "/ɪˈloʊdiəz/", "cây rong thủy sinh Elodea (cỏ nước)"),
    ("072366", "encrustations", "noun", "/ˌɛnkrʌˈsteɪʃənz/", "lớp vỏ cứng đóng cặn; sự khảm đá"),
    ("072367", "enjoyers", "noun", "/ɪnˈdʒɔɪərz/", "người tận hưởng thưởng thức"),
    ("072368", "enterotoxins", "noun", "/ˌɛntəroʊˈtɒksɪnz/", "độc tố đường ruột gây ngộ độc"),
    ("072369", "falangists", "noun", "/fəˈlændʒɪsts/", "đảng viên phái Falange Tây Ban Nha"),
    ("072370", "flatboats", "noun", "/ˈflætˌboʊts/", "thuyền đáy bằng chở hàng trên sông"),
    ("072371", "forepersons", "noun", "/ˈfɔːrˌpɜːrsənz/", "quản đốc; trưởng ban bồi thẩm đoàn"),
    ("072372", "fugacities", "noun", "/fjuːˈɡæsɪtiz/", "tính chóng tàn; hoạt áp nhiệt động"),
    ("072373", "funduluses", "noun", "/ˈfʌndjʊləsɪz/", "cá tuế killifish chi Fundulus"),
    ("072374", "gerontocracies", "noun", "/ˌdʒɛrənˈtɒkrəsiz/", "chế độ cai trị bởi người cao tuổi"),
    ("072375", "greisens", "noun", "/ˈɡraɪzənz/", "đá biến chất greisen chứa thiếc"),
    ("072376", "gwydions", "noun", "/ˈɡwɪdiənz/", "pháp sư Gwydion thần thoại Wales"),
    ("072377", "hexapods", "noun", "/ˈhɛksəˌpɒdz/", "động vật sáu chân (côn trùng)"),
    ("072378", "hieracia", "noun", "/ˌhaɪəˈreɪʃə/", "chi Cỏ diếp dại mắt chim Hieracium"),
    ("072379", "hominoids", "noun", "/ˈhɒmɪˌnɔɪdz/", "siêu họ Linh trưởng dạng người"),
    ("072380", "hyperboreans", "noun", "/ˌhaɪpərˈbɔːriənz/", "người vùng cực bắc huyền thoại"),
    ("072381", "hypopigmentations", "noun", "/ˌhaɪpoʊpɪɡmɛnˈteɪʃənz/", "tình trạng giảm mất sắc tố da"),
    ("072382", "hypopneas", "noun", "/haɪˈpɒpniəz/", "chứng thở nông giảm thông khí ngủ"),
    ("072383", "iconologies", "noun", "/ˌaɪkəˈnɒlədʒiz/", "ngành biểu tượng học nghệ thuật"),
    ("072384", "idiolects", "noun", "/ˈɪdiəˌlɛkts/", "ngữ hệ cá nhân đặc trưng từng người"),
    ("072385", "imprecations", "noun", "/ˌɪmprɪˈkeɪʃənz/", "lời nguyền rủa trù ẻo độc địa"),
    ("072386", "interrelatednesses", "noun", "/ˌɪntərɪˈleɪtɪdnəsɪz/", "tính liên kết tương quan lẫn nhau"),
    ("072387", "klopstocks", "noun", "/ˈklɒpstɒks/", "thi sĩ Đức Friedrich Klopstock"),
    ("072388", "landlers", "noun", "/ˈlɛndlərz/", "điệu nhảy dân gian Áo-Đức Ländler"),
    ("072389", "lobstermans", "noun", "/ˈlɒbstərmənz/", "ngư dân chuyên đánh bắt tôm hùm"),
    ("072390", "loxias", "noun", "/ˈlɒksiəz/", "chi Chim mỏ chéo (Loxia)"),
    ("072391", "manoeuvered", "verb", "/məˈnuːvərd/", "đã điều động; đã xoay xở khéo (Anh)"),
    ("072392", "manoeuvering", "verb", "/məˈnuːvərɪŋ/", "đang điều động; đang xoay xở khéo"),
    ("072393", "manoeuvers", "verb", "/məˈnuːvərz/", "điều động khéo; xoay xở vượt qua"),
    ("072394", "maruts", "noun", "/ˈmɑːrʊts/", "chư thần bão tố Marut Ấn Độ cổ"),
    ("072395", "mujahadeens", "noun", "/ˌmuːdʒəhɑːˈdiːnz/", "chiến binh thánh chiến Mujahideen"),
    ("072396", "nautches", "noun", "/nɔːtʃɪz/", "điệu múa truyền thống Ấn Độ nautch"),
    ("072397", "negociated", "verb", "/nɪˈɡoʊʃiˌeɪtɪd/", "đã đàm phán thương lượng (biến thể)"),
    ("072398", "negociates", "verb", "/nɪˈɡoʊʃiˌeɪts/", "đàm phán thương lượng; vượt qua"),
    ("072399", "negociating", "verb", "/nɪˈɡoʊʃiˌeɪtɪŋ/", "đang đàm phán thương lượng"),
    ("072400", "nominalists", "noun", "/ˈnɒmɪnəlɪsts/", "triết gia theo thuyết duy danh"),
    ("072401", "obstruents", "noun", "/ɒbˈstruːənts/", "âm tắc xát cản hơi (ngữ âm học)"),
    ("072402", "oersteds", "noun", "/ˈɜːrstɛdz/", "đơn vị từ trường oersted (Oe)"),
]

with open("scratch/b35_r05_raw_p4.json") as f:
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

with open("scratch/b35_r05_p4.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r05_p4.json OK")
