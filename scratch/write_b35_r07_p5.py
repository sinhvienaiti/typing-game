import json

items = [
    ("073403", "gasfields", "noun", "/ˈɡæsˌfiːldz/", "mỏ khai thác khí đốt tự nhiên"),
    ("073404", "gastronomes", "noun", "/ˈɡæstrəˌnoʊmz/", "người sành ăn uống ẩm thực"),
    ("073405", "glissaded", "verb", "/ɡlɪˈsɑːdɪd/", "đã trượt tuyết (hoặc trượt ba lê)"),
    ("073406", "glissades", "noun", "/ɡlɪˈsɑːdz/", "cú trượt tuyết; bước trượt ba lê"),
    ("073407", "glissading", "verb", "/ɡlɪˈsɑːdɪŋ/", "đang trượt tuyết; đang lướt ba lê"),
    ("073408", "glossitises", "noun", "/ɡlɒˈsaɪtɪsɪz/", "bệnh viêm sưng lưỡi (y học)"),
    ("073409", "hairlessnesses", "noun", "/ˈhɛərləsnəsɪz/", "tình trạng không có lông hoặc tóc"),
    ("073410", "helpmeets", "noun", "/ˈhɛlpˌmiːts/", "người bạn đời giúp đỡ đồng hành"),
    ("073411", "herbarts", "noun", "/ˈhɜːrbɑːrts/", "triết gia Đức Johann Herbart"),
    ("073412", "hohhots", "noun", "/ˈhoʊhɒts/", "thành phố Hohhot ở Nội Mông"),
    ("073413", "hotcakes", "noun", "/ˈhɒtˌkeɪks/", "bánh kếp nướng ăn nóng (Mỹ)"),
    ("073414", "hydropathies", "noun", "/haɪˈdrɒpəθiz/", "thủy liệu pháp chữa bệnh bằng nước"),
    ("073415", "hypophyses", "noun", "/haɪˈpɒfɪˌsiːz/", "tuyến yên (não thùy)"),
    ("073416", "individualisations", "noun", "/ˌɪndɪvɪdʒuəlaɪˈzeɪʃənz/", "sự cá nhân hóa (cách viết Anh)"),
    ("073417", "jongleurs", "noun", "/ʒɒŋˈɡlɜːrz/", "nghệ sĩ hát rong tạp kỹ trung cổ"),
    ("073418", "karabiners", "noun", "/ˌkærəˈbiːnərz/", "móc khóa leo núi carabiner (Anh)"),
    ("073419", "kendrews", "noun", "/ˈkɛndruːz/", "nhà hóa sinh Nobel John Kendrew"),
    ("073420", "kenoses", "noun", "/kɪˈnoʊsiːz/", "sự tự hạ mình (thần học Ki-tô)"),
    ("073421", "kurrajongs", "noun", "/ˈkʌrəˌdʒɒŋz/", "cây bóng mát kurrajong của Úc"),
    ("073422", "labiodentals", "noun", "/ˌleɪbioʊˈdɛntəlz/", "âm môi-răng (như /f/, /v/)"),
    ("073423", "laocoons", "noun", "/leɪˈɒkəˌwɒnz/", "tư tế Laocoön thành Troy cổ đại"),
    ("073424", "laurasias", "noun", "/lɔːˈreɪʒəz/", "siêu lục địa cổ phía bắc Laurasia"),
    ("073425", "laurelwoods", "noun", "/ˈlɔːrəlˌwʊdz/", "gỗ hoặc cây nguyệt quế laurelwood"),
    ("073426", "leflunomides", "noun", "/lɛˈfluːnəˌmaɪdz/", "thuốc trị viêm khớp leflunomide"),
    ("073427", "lefthanders", "noun", "/ˌlɛftˈhændərz/", "người thuận tay trái (hoặc cú đấm)"),
    ("073428", "leucaenas", "noun", "/luːˈsiːnəz/", "cây keo dậu bình linh chi Leucaena"),
    ("073429", "leverets", "noun", "/ˈlɛvərɪts/", "thỏ rừng con non dưới một năm"),
    ("073430", "liatrises", "noun", "/laɪˈeɪtrɪsɪz/", "hoa sao tím Liatris Bắc Mỹ"),
    ("073431", "lodgments", "noun", "/ˈlɒdʒmənts/", "chỗ ở trọ; sự đọng kẹt; nộp đơn"),
    ("073432", "lodines", "noun", "/ˈloʊdiːnz/", "thuốc kháng viêm giảm đau Lodine"),
    ("073433", "lutenists", "noun", "/ˈluːtənɪsts/", "nghệ sĩ chơi đàn luýt cổ điển"),
    ("073434", "manpads", "noun", "/ˈmænpædz/", "tên lửa phòng không vác vai MANPADS"),
    ("073435", "mansarts", "noun", "/mɑːnˈsɑːrz/", "kiến trúc sư Pháp François Mansart"),
    ("073436", "marocains", "noun", "/ˌmærəˈkeɪnz/", "vải lụa dệt nổi gân marocain"),
    ("073437", "mawlamyines", "noun", "/ˌmaʊləˈmjɑːɪnz/", "thành phố cảng Mawlamyine Myanmar"),
    ("073438", "mediants", "noun", "/ˈmiːdiənts/", "nốt bậc ba của âm giai (âm nhạc)"),
    ("073439", "melilotuses", "noun", "/ˌmɛlɪˈloʊtəsɪz/", "cây nhãn hương cỏ ba lá ngọt"),
    ("073440", "mephitides", "noun", "/mɪˈfaɪtɪˌdiːz/", "chi Chồn hôi Bắc Mỹ (Mephitis)"),
    ("073441", "mesocarps", "noun", "/ˈmɛzoʊˌkɑːrps/", "lớp vỏ quả giữa (cùi thịt quả)"),
    ("073442", "methyltestosterones", "noun", "/ˌmɛθəltɛˈstɒstəroʊnz/", "hoóc-môn nam methyltestosterone"),
    ("073443", "midveins", "noun", "/ˈmɪdˌveɪnz/", "gân chính nằm giữa phiến lá"),
    ("073444", "misplayed", "verb", "/ˌmɪsˈpleɪd/", "đã đánh lỗi, chơi sai chiến thuật"),
    ("073445", "misplaying", "verb", "/ˌmɪsˈpleɪɪŋ/", "đang đánh lỗi, chơi sai (thể thao)"),
    ("073446", "misplays", "noun", "/ˌmɪsˈpleɪz/", "pha xử lý lỗi; nước đi sai lầm"),
    ("073447", "monals", "noun", "/ˈmoʊnəlz/", "chim trĩ sặc sỡ Himalaya monal"),
    ("073448", "multicollinearities", "noun", "/ˌmʌltikəlɪniˈærɪtiz/", "hiện tượng đa cộng tuyến (thống kê)"),
    ("073449", "munchhausens", "noun", "/ˈmʌntʃˌhaʊzənz/", "Nam tước Münchhausen hay khoác lác"),
    ("073450", "namois", "noun", "/ˈnæmɔɪz/", "sông Namoi ở bang New South Wales"),
    ("073451", "naphthoquinones", "noun", "/ˌnæfθoʊkwɪˈnoʊnz/", "hợp chất hữu cơ naphthoquinone"),
    ("073452", "natalities", "noun", "/neɪˈtælɪtiz/", "tỷ suất sinh sản trong dân số"),
    ("073453", "naturalises", "verb", "/ˈnætʃərəˌlaɪzɪz/", "nhập quốc tịch; thích nghi tự nhiên"),
    ("073454", "naturalising", "verb", "/ˈnætʃərəˌlaɪzɪŋ/", "đang nhập quốc tịch (cách viết Anh)"),
    ("073455", "nebuchadrezzars", "noun", "/ˌnɛbjʊkədˈrɛzərz/", "vua Babylon cổ Nebuchadnezzar"),
    ("073456", "nesselrodes", "noun", "/ˈnɛsəlˌroʊdz/", "bánh kem mứt hạt dẻ Nesselrode"),
    ("073457", "nicads", "noun", "/ˈnaɪkædz/", "pin sạc niken-cadimi (NiCd)"),
    ("073458", "nosewheels", "noun", "/ˈnoʊzˌwiːlz/", "bánh đáp mũi phía trước máy bay"),
    ("073459", "osmanlis", "noun", "/ɒzˈmɑːnliz/", "người Thổ Nhĩ Kỳ đế quốc Ottoman"),
    ("073460", "parcellings", "noun", "/ˈpɑːrsəlɪŋz/", "sự chia lô; sự chia thành phần nhỏ"),
    ("073461", "piastres", "noun", "/piˈæstərz/", "đồng tiền piastre (Ai Cập, xưa)"),
    ("073462", "pisiforms", "noun", "/ˈpaɪzɪˌfɔːrmz/", "xương đậu ở cổ tay (giải phẫu)"),
    ("073463", "polygalas", "noun", "/pəˈlɪɡələz/", "cây viễn chí (chi Polygala)"),
    ("073464", "porbeagles", "noun", "/ˈpɔːrˌbiːɡəlz/", "cá nhám thu Đại Tây Dương"),
    ("073465", "professionalised", "verb", "/prəˈfɛʃənəˌlaɪzd/", "đã chuyên nghiệp hóa (Anh)"),
    ("073466", "professionalises", "verb", "/prəˈfɛʃənəˌlaɪzɪz/", "chuyên nghiệp hóa (cách viết Anh)"),
    ("073467", "professionalising", "verb", "/prəˈfɛʃənəˌlaɪzɪŋ/", "đang chuyên nghiệp hóa (Anh)"),
    ("073468", "prognathisms", "noun", "/ˈprɒɡnəˌθɪzəmz/", "tình trạng hàm nhô vẩu ra trước"),
    ("073469", "quincentennials", "noun", "/ˌkwɪnsɛnˈtɛniəlz/", "lễ kỷ niệm 500 năm (nửa thiên niên)"),
    ("073470", "rampions", "noun", "/ˈræmpiənz/", "cây rau chuông rễ củ rampion"),
    ("073471", "regifted", "verb", "/riːˈɡɪftɪd/", "đã đem món quà được tặng cho lại"),
    ("073472", "regifting", "verb", "/riːˈɡɪftɪŋ/", "đang tặng lại quà mình được cho"),
    ("073473", "regifts", "verb", "/riːˈɡɪfts/", "tặng lại món quà mình vừa nhận"),
    ("073474", "rosmarinuses", "noun", "/ˌrɒzməˈraɪnəsɪz/", "cây hương thảo (chi Rosmarinus)"),
    ("073475", "roughriders", "noun", "/ˈrʌfˌraɪdərz/", "người cưỡi thuần hóa ngựa bất kham"),
    ("073476", "russulas", "noun", "/ˈrʌsjʊləz/", "nấm xốp mũ sặc sỡ chi Russula"),
    ("073477", "sarcosines", "noun", "/ˈsɑːrkəˌsiːnz/", "axit amin sarcosine (hóa sinh)"),
    ("073478", "schleidens", "noun", "/ˈʃlaɪdənz/", "nhà thực vật Đức Matthias Schleiden"),
    ("073479", "scrophulariaceaes", "noun", "/ˌskrɒfjʊˌlɛəriˈeɪʃiˌiːz/", "họ Huyền sâm (hoa mõm sói)"),
    ("073480", "shaksperes", "noun", "/ˈʃeɪkspɪərz/", "đại văn hào William Shakespeare"),
    ("073481", "shovelheads", "noun", "/ˈʃʌvəlˌhɛdz/", "cá nhám búa đầu xẻng; cá trê dẹt"),
    ("073482", "sinapises", "noun", "/sɪˈneɪpɪsɪz/", "chi Cây cải mù tạt (Sinapis)"),
    ("073483", "socages", "noun", "/ˈsɒkɪdʒɪz/", "chế độ lĩnh canh đất phong kiến Anh"),
    ("073484", "sophoras", "noun", "/səˈfɔːrəz/", "cây hòe hoa vàng thuộc chi Sophora"),
    ("073485", "stocktakes", "noun", "/ˈstɒkˌteɪks/", "đợt kiểm kê hàng tồn kho (Anh)"),
    ("073486", "stonefaces", "noun", "/ˈstoʊnˌfeɪsɪz/", "cây sỏi sống Lithops Nam Phi"),
    ("073487", "stonewashed", "verb", "/ˈstoʊnˌwɒʃt/", "đã giặt mài bằng đá bọt (vải bò)"),
    ("073488", "stonewashes", "verb", "/ˈstoʊnˌwɒʃɪz/", "giặt mài bằng đá bọt cho phai mềm"),
    ("073489", "stonewashing", "verb", "/ˈstoʊnˌwɒʃɪŋ/", "đang giặt mài bằng đá bọt (vải)"),
    ("073490", "subeditors", "noun", "/sʌbˈɛdɪtərz/", "biên tập viên hiệu đính bản thảo"),
    ("073491", "supersessions", "noun", "/ˌsuːpərˈsɛʃənz/", "sự thay thế kế nhiệm chức vụ"),
    ("073492", "thuribles", "noun", "/ˈθjʊərɪbəlz/", "bình lư xông trầm hương có dây xích"),
    ("073493", "tortricidaes", "noun", "/ˌtɔːrˈtrɪsɪˌdiːz/", "họ Bướm ngài cuốn lá (Tortricidae)"),
    ("073494", "tournedoses", "noun", "/ˌtʊərnəˈdoʊzɪz/", "miếng thịt thăn bò cắt tròn dày"),
    ("073495", "trustors", "noun", "/ˈtrʌstɔːrz/", "người lập quỹ tín thác ủy thác"),
    ("073496", "uraninites", "noun", "/jʊˈrænɪˌnaɪts/", "quặng urani oxit uraninit"),
    ("073497", "viscums", "noun", "/ˈvɪskəmz/", "chi Cây tầm gửi ký sinh (Viscum)"),
    ("073498", "weewees", "noun", "/ˈwiːˌwiːz/", "nước tiểu (ngôn ngữ trẻ con, lóng)"),
    ("073499", "wilfulnesses", "noun", "/ˈwɪlfʊlnəsɪz/", "tính bướng bỉnh cố chấp (Anh)"),
    ("073500", "wireworks", "noun", "/ˈwaɪərˌwɜːrks/", "xưởng sản xuất dây thép; lưới thép"),
    ("073501", "yucatecs", "noun", "/ˌjuːkəˈtɛks/", "người và tiếng Maya Yucatec Mexico"),
    ("073502", "abomasums", "noun", "/ˌæboʊˈmeɪsəmz/", "dạ múi khế (ngăn thứ tư dạ dày bò)"),
]

with open("scratch/b35_r07_raw_p5.json") as f:
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

with open("scratch/b35_r07_p5.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r07_p5.json OK")
