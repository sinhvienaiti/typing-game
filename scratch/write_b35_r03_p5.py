import json

items = [
    ("071403", "dysurias", "noun", "/dɪsˈjʊəriəz/", "chứng tiểu buốt tiểu rắt khó khăn"),
    ("071404", "echinococcoses", "noun", "/ɪˌkaɪnoʊkɒˈkoʊsiːz/", "bệnh sán dây chó nang nước"),
    ("071405", "echolalias", "noun", "/ˌɛkoʊˈleɪliəz/", "chứng nhại lời vô thức (tâm thần)"),
    ("071406", "enoses", "noun", "/ɛˈnoʊsiːz/", "phong trào Enosis (sáp nhập Hy Lạp)"),
    ("071407", "epilogs", "noun", "/ˈɛpɪˌlɒɡz/", "phần kết thúc; lời bạt cuối sách"),
    ("071408", "fasciolas", "noun", "/fəˈsaɪələz/", "chi Sán lá gan lớn (Fasciola)"),
    ("071409", "federalisations", "noun", "/ˌfɛdərəlaɪˈzeɪʃənz/", "sự liên bang hóa thể chế (Anh)"),
    ("071410", "feluccas", "noun", "/fɛˈlʌkəz/", "thuyền buồm gỗ Địa Trung Hải"),
    ("071411", "fletcs", "noun", "/ˈflɛtɛks/", "trung tâm đào tạo cảnh sát FLETC"),
    ("071412", "folia", "noun", "/ˈfoʊliə/", "lá; phiến lá mỏng; thùy tiểu não"),
    ("071413", "foliums", "noun", "/ˈfoʊliəmz/", "phiến lá mỏng; đường cong folium"),
    ("071414", "fontanels", "noun", "/ˌfɒntəˈnɛlz/", "thóp mềm trên hộp sọ trẻ sơ sinh"),
    ("071415", "foreshocks", "noun", "/ˈfɔːrˌʃɒks/", "tiền chấn (động đất nhỏ báo trước)"),
    ("071416", "geographicses", "noun", "/ˌdʒiːəˈɡræfɪksɪz/", "môn địa lý học (cách gọi cũ)"),
    ("071417", "granters", "noun", "/ˈɡræntərz/", "người cấp phép hoặc chuyển nhượng"),
    ("071418", "gulos", "noun", "/ˈɡjuːloʊz/", "chi Chồn gulô vùng cực Bắc (Gulo)"),
    ("071419", "heucheras", "noun", "/ˈhjuːkərəz/", "cây chuông san hô lá đẹp Heuchera"),
    ("071420", "hinnied", "verb", "/ˈhɪnid/", "đã kêu hí (lừa hoặc ngựa)"),
    ("071421", "housemothers", "noun", "/ˈhaʊsˌmʌðərz/", "nữ quản lý ký túc xá sinh viên"),
    ("071422", "interlinguas", "noun", "/ˌɪntərˈlɪŋɡwəz/", "ngôn ngữ nhân tạo Interlingua"),
    ("071423", "iontophoreses", "noun", "/aɪˌɒntoʊfəˈriːsiːz/", "liệu pháp điện di dẫn thuốc qua da"),
    ("071424", "jellyrolls", "noun", "/ˈdʒɛliˌroʊlz/", "bánh bông lan cuộn nhân mứt quả"),
    ("071425", "kalifs", "noun", "/ˈkeɪlɪfs/", "vua Hồi giáo tối cao (Khalip)"),
    ("071426", "keelboats", "noun", "/ˈkiːlˌboʊts/", "thuyền đáy sống chở hàng trên sông"),
    ("071427", "lacunaria", "noun", "/ˌlækjuˈnɛəriə/", "ô hốc trần trang trí kiến trúc cổ"),
    ("071428", "lacunars", "noun", "/ləˈkjuːnərz/", "ô hốc trần trang trí kiến trúc cổ"),
    ("071429", "lavandulas", "noun", "/ləˈvændjʊləz/", "cây hoa oải hương chi Lavandula"),
    ("071430", "levirates", "noun", "/ˈlɛvɪrəts/", "tục hôn nhân nối dây với em chồng"),
    ("071431", "littorinas", "noun", "/ˌlɪtəˈraɪnəz/", "chi Ốc biển bờ đá Littorina"),
    ("071432", "macropi", "noun", "/məˈkroʊpaɪ/", "chi Chuột túi lớn Macropus"),
    ("071433", "michiganders", "noun", "/ˌmɪʃɪˈɡændərz/", "người dân bang Michigan của Mỹ"),
    ("071434", "misidentified", "verb", "/ˌmɪsaɪˈdɛntɪˌfaɪd/", "đã nhận dạng nhầm lẫn"),
    ("071435", "misidentifies", "verb", "/ˌmɪsaɪˈdɛntɪˌfaɪz/", "nhận dạng nhầm lẫn; nhận sai"),
    ("071436", "misidentifying", "verb", "/ˌmɪsaɪˈdɛntɪˌfaɪɪŋ/", "đang nhận dạng nhầm lẫn"),
    ("071437", "mortarboards", "noun", "/ˈmɔːrtərˌbɔːrdz/", "mũ vuông tốt nghiệp; bàn xoa hồ"),
    ("071438", "murmurations", "noun", "/ˌmɜːrməˈreɪʃənz/", "đàn chim sáo bay lượn; tiếng rì rầm"),
    ("071439", "myotonias", "noun", "/ˌmaɪəˈtoʊniəz/", "chứng loạn trương lực co cứng cơ"),
    ("071440", "myrtaceaes", "noun", "/mɜːrˈteɪʃiˌiːz/", "họ Sim (bạch đàn, ổi, tràm)"),
    ("071441", "myxomas", "noun", "/mɪkˈsoʊməz/", "u nhầy mô liên kết (lành tính)"),
    ("071442", "myxomata", "noun", "/mɪkˈsoʊmətə/", "u nhầy mô liên kết (y học)"),
    ("071443", "nanograms", "noun", "/ˈnænoʊˌɡræmz/", "đơn vị khối lượng nanôgam"),
    ("071444", "natrixes", "noun", "/ˈneɪtrɪksɪz/", "chi Rắn nước không độc (Natrix)"),
    ("071445", "nematodas", "noun", "/ˌnɛməˈtoʊdəz/", "ngành Giun tròn ký sinh hoặc đất"),
    ("071446", "nucleoproteins", "noun", "/ˌnjuːklioʊˈproʊtiːnz/", "phức hợp protein và axit nucleic"),
    ("071447", "nullifiers", "noun", "/ˈnʌlɪˌfaɪərz/", "người vô hiệu hóa hủy bỏ hiệu lực"),
    ("071448", "nyiragongos", "noun", "/ˌnɪərəˈɡɒŋɡoʊz/", "núi lửa Nyiragongo ở CHDC Congo"),
    ("071449", "ocimums", "noun", "/ˈɒsɪməmz/", "cây húng quế hương nhu chi Ocimum"),
    ("071450", "odocoileuses", "noun", "/ˌoʊdəˈkɔɪliəsɪz/", "chi Hươu đuôi trắng Mỹ Odocoileus"),
    ("071451", "oogeneses", "noun", "/ˌoʊəˈdʒɛnɪsiːz/", "quá trình tạo noãn tế bào trứng"),
    ("071452", "orthoclases", "noun", "/ˈɔːrθəˌkleɪsɪz/", "khoáng vật fenspat kali octoclas"),
    ("071453", "papilledemas", "noun", "/ˌpæpɪlɪˈdiːməz/", "chứng phù gai thị giác đáy mắt"),
    ("071454", "perutzes", "noun", "/ˈpɛrʊtsɪz/", "nhà sinh học Nobel Max Perutz"),
    ("071455", "pinsks", "noun", "/pɪnsks/", "thành phố Pinsk ở Belarus"),
    ("071456", "plantaes", "noun", "/ˈplæntiːz/", "giới Thực vật trong sinh học"),
    ("071457", "pneumococci", "noun", "/ˌnjuːməˈkɒkaɪ/", "vi khuẩn phế cầu gây viêm phổi"),
    ("071458", "polypodiums", "noun", "/ˌpɒlɪˈpoʊdiəmz/", "cây dương xỉ cạn chi Polypodium"),
    ("071459", "precessed", "verb", "/prɪˈsɛst/", "đã tiến động (trục quay con quay)"),
    ("071460", "precesses", "verb", "/prɪˈsɛsɪz/", "tiến động đảo trục quay (vật lý)"),
    ("071461", "precessing", "verb", "/prɪˈsɛsɪŋ/", "đang tiến động quay đảo trục"),
    ("071462", "prosthetists", "noun", "/ˈprɒsθɪtɪsts/", "chuyên gia chế tạo chân tay giả"),
    ("071463", "radioimmunoassays", "noun", "/ˌreɪdioʊɪˌmjuːnoʊˈæseɪz/", "xét nghiệm miễn dịch phóng xạ"),
    ("071464", "reelers", "noun", "/ˈriːlərz/", "người cuộn tơ; kẻ đi loạng choạng"),
    ("071465", "sannyasis", "noun", "/sənˈjɑːsiz/", "tu sĩ khổ hạnh xuất gia Ấn Độ giáo"),
    ("071466", "scalawags", "noun", "/ˈskælɪˌwæɡz/", "kẻ ranh ma láu cá; người Tái thiết"),
    ("071467", "schnozes", "noun", "/ˈʃnɒzɪz/", "cái mũi to (tiếng lóng Mỹ)"),
    ("071468", "scratchpads", "noun", "/ˈskrætʃˌpædz/", "sổ giấy nháp; bộ nhớ đệm nhanh"),
    ("071469", "shiksas", "noun", "/ˈʃɪksəz/", "phụ nữ không theo Do Thái (từ lóng)"),
    ("071470", "snoeks", "noun", "/snʊks/", "cá thu rắn biển nam bán cầu snoek"),
    ("071471", "socles", "noun", "/ˈsɒkəlz/", "bệ đế vuông đặt cột hoặc tượng"),
    ("071472", "solvabilities", "noun", "/ˌsɒlvəˈbɪlɪtiz/", "tính giải được; khả năng trả nợ"),
    ("071473", "soubrettes", "noun", "/suːˈbrɛts/", "vai hầu gái lanh lợi (kịch, opera)"),
    ("071474", "spireas", "noun", "/spaɪˈriːəz/", "cây bụi hoa mơ trân châu Spiraea"),
    ("071475", "squiffier", "adj", "/ˈskwɪfiər/", "say ngà ngà hơn; lệch nghiêng hơn"),
    ("071476", "squiffiest", "adj", "/ˈskwɪfiɪst/", "say ngà ngà nhất; lệch nghiêng nhất"),
    ("071477", "strengtheners", "noun", "/ˈstrɛŋθənərz/", "vật gia cố tăng lực; chất làm bền"),
    ("071478", "suprematisms", "noun", "/sʊˈprɛməˌtɪzəmz/", "trường phái hội họa Tối thượng"),
    ("071479", "tetanies", "noun", "/ˈtɛtəniz/", "cơn co giật cứng cơ do hạ canxi"),
    ("071480", "tipplers", "noun", "/ˈtɪplərz/", "người hay nhâm nhi uống rượu đều"),
    ("071481", "triumvirs", "noun", "/traɪˈʌmvɜːrz/", "thành viên chế độ tam hùng La Mã"),
    ("071482", "tulipas", "noun", "/ˈtjuːlɪpəz/", "chi Hoa tulip uất kim hương"),
    ("071483", "untermeyers", "noun", "/ˈʌntərˌmaɪərz/", "nhà thơ Mỹ Louis Untermeyer"),
    ("071484", "videodiscs", "noun", "/ˈvɪdioʊˌdɪsks/", "đĩa hình quang học thu phát video"),
    ("071485", "virgilias", "noun", "/vɜːrˈdʒɪliəz/", "cây hoa đậu thơm châu Phi Virgilia"),
    ("071486", "viscometers", "noun", "/vɪsˈkɒmɪtərz/", "nhớt kế đo độ nhớt chất lỏng"),
    ("071487", "washhouses", "noun", "/ˈwɒʃˌhaʊzɪz/", "nhà giặt giũ quần áo công cộng"),
    ("071488", "westernisations", "noun", "/ˌwɛstərnaɪˈzeɪʃənz/", "quá trình Tây phương hóa (Anh)"),
    ("071489", "wouks", "noun", "/wʊks/", "nhà văn Mỹ Herman Wouk"),
    ("071490", "accelerandos", "noun", "/ɑːkˌtʃɛləˈrɑːndoʊz/", "đoạn nhạc tăng tốc nhanh dần đều"),
    ("071491", "ambassadresses", "noun", "/æmˈbæsədrɪsɪz/", "nữ đại sứ; phu nhân đại sứ"),
    ("071492", "amboynas", "noun", "/æmˈbɔɪnəz/", "gỗ gụ vân mắt chim Amboyna quý"),
    ("071493", "ambystomas", "noun", "/ˌæmbɪˈstoʊməz/", "chi Kỳ giông nốt chuột Ambystoma"),
    ("071494", "ascendents", "noun", "/əˈsɛndənts/", "tổ tiên đời trước; thế đang lên"),
    ("071495", "aviatrixes", "noun", "/ˌeɪviˈeɪtrɪksɪz/", "nữ phi công lái máy bay (từ cũ)"),
    ("071496", "bearnaises", "noun", "/bɛərˈneɪzɪz/", "xốt bơ trứng ngải giấm Béarnaise"),
    ("071497", "behaviourisms", "noun", "/bɪˈheɪvjəˌrɪzəmz/", "thuyết tâm lý học hành vi (Anh)"),
    ("071498", "biometries", "noun", "/baɪˈɒmɪtriz/", "ngành sinh trắc học thống kê"),
    ("071499", "bizarrenesses", "noun", "/bɪˈzɑːrnəsɪz/", "tính chất kỳ quái quái dị lạ lùng"),
    ("071500", "bowerbirds", "noun", "/ˈbaʊərˌbɜːrdz/", "chim lều (xây chòi kết hoa dụ bạn)"),
    ("071501", "calkins", "noun", "/ˈkɔːlkɪnz/", "đinh móc chống trượt dưới móng ngựa"),
    ("071502", "caporettos", "noun", "/ˌkæpəˈrɛtoʊz/", "trận Caporetto năm 1917 ở Ý"),
]

with open("scratch/b35_r03_raw_p5.json") as f:
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

with open("scratch/b35_r03_p5.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r03_p5.json OK")
