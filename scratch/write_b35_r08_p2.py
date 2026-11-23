import json

items = [
    ("073603", "outspaning", "verb", "/ˈaʊtˌspænɪŋ/", "đang tháo ách cho bò; nghỉ xả trại"),
    ("073604", "outspanned", "verb", "/ˈaʊtˌspænd/", "đã tháo ách cho bò; nghỉ xả trại"),
    ("073605", "outspanning", "verb", "/ˈaʊtˌspænɪŋ/", "đang tháo ách bò; đang nghỉ xả trại"),
    ("073606", "outspans", "verb", "/ˈaʊtˌspænz/", "tháo ách cho bò ngựa; hạ trại nghỉ"),
    ("073607", "ovoli", "noun", "/ˈoʊvəˌlaɪ/", "gờ chỉ phào hình trứng (kiến trúc)"),
    ("073608", "ovolos", "noun", "/ˈoʊvəˌloʊz/", "gờ chỉ phào hình trứng (kiến trúc)"),
    ("073609", "oxidisers", "noun", "/ˈɒksɪˌdaɪzərz/", "chất oxy hóa (cách viết Anh)"),
    ("073610", "peglegs", "noun", "/ˈpɛɡˌlɛɡz/", "chân gỗ giả; người đi chân gỗ"),
    ("073611", "pengos", "noun", "/ˈpɛŋɡoʊz/", "đồng tiền pengő cũ của Hungary"),
    ("073612", "periplanetas", "noun", "/ˌpɛrɪpləˈniːtəz/", "chi Gián Mỹ lớn (Periplaneta)"),
    ("073613", "pithecanthropi", "noun", "/ˌpɪθɪˈkænθrəpaɪ/", "người vượn cổ Java Pithecanthropus"),
    ("073614", "pithecanthropuses", "noun", "/ˌpɪθɪˈkænθrəpəsɪz/", "người vượn cổ Java Pithecanthropus"),
    ("073615", "profitablenesses", "noun", "/ˈprɒfɪtəbəlnəsɪz/", "tính sinh lợi mang lại lợi nhuận"),
    ("073616", "prunos", "noun", "/ˈpruːnoʊz/", "rượu trái cây lên men tự chế (lóng)"),
    ("073617", "qabalahs", "noun", "/kəˈbɑːləz/", "học thuyết mật giáo Kabbalah"),
    ("073618", "ramees", "noun", "/ˈræmiz/", "cây gai xanh lấy sợi (ramie)"),
    ("073619", "reflectivenesses", "noun", "/rɪˈflɛktɪvnəsɪz/", "tính trầm tư sâu sắc hay suy ngẫm"),
    ("073620", "resuscitators", "noun", "/rɪˈsʌsɪˌteɪtərz/", "thiết bị hồi sức cấp cứu thở oxy"),
    ("073621", "runnels", "noun", "/ˈrʌnəlz/", "dòng suối nhỏ; rãnh thoát nước nhỏ"),
    ("073622", "ruritanias", "noun", "/ˌrʊərɪˈteɪniəz/", "vương quốc giả tưởng Ruritania"),
    ("073623", "sahuaros", "noun", "/səˈwɑːroʊz/", "xương rồng khổng lồ saguaro sa mạc"),
    ("073624", "sakkaras", "noun", "/səˈkɑːrəz/", "di chỉ Saqqara cổ đại ở Ai Cập"),
    ("073625", "sallets", "noun", "/ˈsælɪts/", "mũ sắt trùm gáy thế kỷ 15 (sallet)"),
    ("073626", "sansevierias", "noun", "/ˌsænsɪˈvɪəriəz/", "cây lưỡi hổ đuôi công Sansevieria"),
    ("073627", "seiches", "noun", "/seɪʃɪz/", "sóng dừng dao động mặt hồ seiche"),
    ("073628", "shiahs", "noun", "/ˈʃiːəz/", "người Hồi giáo dòng Shiite (Shia)"),
    ("073629", "spirants", "noun", "/ˈspaɪrənts/", "phụ âm xát (ngữ âm học)"),
    ("073630", "strongrooms", "noun", "/ˈstrɒŋˌruːmz/", "phòng két kiên cố cất giữ tài sản"),
    ("073631", "tantrisms", "noun", "/ˈtæntrɪzəmz/", "Mật tông (Ấn Độ giáo và Phật giáo)"),
    ("073632", "thalictrums", "noun", "/θəˈlɪktrəmz/", "cây đường tùng hương thảo"),
    ("073633", "tranylcypromines", "noun", "/ˌtrænəlˈsaɪprəmiːnz/", "thuốc ức chế MAO tranylcypromine"),
    ("073634", "trasimenos", "noun", "/ˌtrɑːsɪˈmeɪnoʊz/", "hồ và trận Trasimene ở Ý cổ đại"),
    ("073635", "zeugmas", "noun", "/ˈzjuːɡməz/", "phép tu từ phối hợp nghĩa zeugma"),
    ("073636", "albulas", "noun", "/ˈælbjʊləz/", "chi Cá mòi đường xương (Albula)"),
    ("073637", "amobarbitals", "noun", "/ˌæmoʊˈbɑːrbɪˌtɑːlz/", "thuốc ngủ barbiturat amobarbital"),
    ("073638", "amphioxi", "noun", "/ˌæmfiˈɒksaɪ/", "con lưỡng tiêm biển (cá lưỡng tiêm)"),
    ("073639", "amphioxuses", "noun", "/ˌæmfiˈɒksəsɪz/", "con lưỡng tiêm biển (amphioxus)"),
    ("073640", "amphipodas", "noun", "/æmˈfɪpədəz/", "bộ Chân hai bên (bọ nhảy biển)"),
    ("073641", "amygdaloids", "noun", "/əˈmɪɡdəˌlɔɪdz/", "đá hốc hạnh nhân; hạch hạnh nhân"),
    ("073642", "araxeses", "noun", "/əˈræksiːzɪz/", "sông Aras (Araxes) vùng Kavkaz"),
    ("073643", "backblasts", "noun", "/ˈbækˌblæsts/", "luồng phụt ngược đuôi tên lửa RPG"),
    ("073644", "carpetbags", "noun", "/ˈkɑːrpɪtˌbæɡz/", "túi xách du lịch may bằng vải thảm"),
    ("073645", "chlorofluorocarbons", "noun", "/ˌklɔːroʊflʊəroʊˈkɑːrbənz/", "hợp chất khí CFC (gây thủng ozon)"),
    ("073646", "commensalisms", "noun", "/kəˈmɛnsəˌlɪzəmz/", "quan hệ hội sinh (sinh thái học)"),
    ("073647", "contumelies", "noun", "/kənˈtjuːməliz/", "lời lăng mạ sỉ nhục xấc xược"),
    ("073648", "costermongers", "noun", "/ˈkɒstərˌmʌŋɡərz/", "người bán rong rau quả xe đẩy (Anh)"),
    ("073649", "cryptococcoses", "noun", "/ˌkrɪptoʊkɒˈkoʊsiːz/", "bệnh nhiễm nấm Cryptococcus não"),
    ("073650", "cynewulfs", "noun", "/ˈkɪnəˌwʊlfs/", "thi sĩ Anh cổ đại Cynewulf"),
    ("073651", "dalos", "noun", "/ˈdɑːloʊz/", "cây khoai môn nước (tên Fiji)"),
    ("073652", "dardanuses", "noun", "/ˈdɑːrdənəsɪz/", "thủy tổ thành Troy Dardanus Hy Lạp"),
    ("073653", "deviltries", "noun", "/ˈdɛvəltriz/", "trò quỷ quái tinh ranh ác độc"),
    ("073654", "dissimilations", "noun", "/dɪˌsɪmɪˈleɪʃənz/", "sự dị hóa âm vị khác nhau (ngữ âm)"),
    ("073655", "dolichocephalics", "noun", "/ˌdɒlɪkoʊsɪˈfælɪks/", "người có hộp sọ dài hẹp"),
    ("073656", "douras", "noun", "/ˈdʊərəz/", "cây lúa miến cao lương dura"),
    ("073657", "endodontists", "noun", "/ˌɛndoʊˈdɒntɪsts/", "bác sĩ chuyên khoa nội nha tủy răng"),
    ("073658", "endolymphs", "noun", "/ˈɛndoʊˌlɪmfs/", "nội dịch trong ốc tai tai trong"),
    ("073659", "epigeneses", "noun", "/ˌɛpɪˈdʒɛnɪˌsiːz/", "thuyết phát sinh phôi dần (sinh)"),
    ("073660", "eriogonums", "noun", "/ˌɛriˈɒɡənəmz/", "cây kiều mạch hoang chi Eriogonum"),
    ("073661", "fingerspellings", "noun", "/ˈfɪŋɡərˌspɛlɪŋz/", "cách đánh vần chữ cái bằng ngón tay"),
    ("073662", "flagellants", "noun", "/ˈflædʒələnts/", "tín đồ tự hành xác bằng roi"),
    ("073663", "fleabanes", "noun", "/ˈfliːˌbeɪnz/", "cây cúc đuổi bọ chét fleabane"),
    ("073664", "folderols", "noun", "/ˈfɒldəˌrɒlz/", "chuyện nhảm nhí phù phiếm vớ vẩn"),
    ("073665", "foreparts", "noun", "/ˈfɔːrˌpɑːrts/", "phần phía trước; thời kỳ đầu"),
    ("073666", "genistas", "noun", "/dʒɪˈnɪstəz/", "cây bụi hoa vàng kim tước (broom)"),
    ("073667", "hellenes", "noun", "/ˈhɛliːnz/", "người dân Hy Lạp cổ đại (Hellene)"),
    ("073668", "hoggets", "noun", "/ˈhɒɡɪts/", "cừu tơ một tuổi mới xén lông (Anh)"),
    ("073669", "hootches", "noun", "/ˈhuːtʃɪz/", "rượu nấu lậu; túp lều sơ sài (lóng)"),
    ("073670", "hyperlipidaemias", "noun", "/ˌhaɪpərlɪpɪˈdiːmiəz/", "chứng tăng mỡ máu rối loạn lipid"),
    ("073671", "hypertonias", "noun", "/ˌhaɪpərˈtoʊniəz/", "tình trạng tăng trương lực cơ co"),
    ("073672", "ichthyosauri", "noun", "/ˌɪkθioʊˈsɔːraɪ/", "thằn lằn cá biển tiền sử"),
    ("073673", "immunochemistries", "noun", "/ɪˌmjʊnoʊˈkɛmɪstriz/", "ngành hóa miễn dịch học"),
    ("073674", "insectivores", "noun", "/ɪnˈsɛktɪˌvɔːrz/", "động vật ăn sâu bọ côn trùng"),
    ("073675", "interpenetrated", "verb", "/ˌɪntərˈpɛnɪˌtreɪtɪd/", "đã thâm nhập đan xen vào nhau"),
    ("073676", "interpenetrates", "verb", "/ˌɪntərˈpɛnɪˌtreɪts/", "thâm nhập đan xen vào lẫn nhau"),
    ("073677", "interpenetrating", "verb", "/ˌɪntərˈpɛnɪˌtreɪtɪŋ/", "đang thâm nhập đan xen vào nhau"),
    ("073678", "introituses", "noun", "/ɪnˈtrɔɪtəsɪz/", "lỗ vào ống cơ quan (giải phẫu)"),
    ("073679", "justifiers", "noun", "/ˈdʒʌstɪˌfaɪərz/", "người biện minh; kỹ thuật căn lề"),
    ("073680", "kinkajous", "noun", "/ˈkɪŋkəˌdʒuːz/", "thú ăn quả gấu trúc kinkajou Nam Mỹ"),
    ("073681", "ligustrums", "noun", "/lɪˈɡʌstrəmz/", "cây nhót trắng hàng rào Ligustrum"),
    ("073682", "limens", "noun", "/ˈlaɪmɛnz/", "ngưỡng cảm giác tối thiểu (tâm lý)"),
    ("073683", "limina", "noun", "/ˈlɪmɪnə/", "ngưỡng cảm giác tối thiểu (tâm lý)"),
    ("073684", "lorgnettes", "noun", "/lɔːrnˈjɛts/", "kính mắt có tay cầm gấp (cổ điển)"),
    ("073685", "lowlanders", "noun", "/ˈloʊləndərz/", "người vùng đất thấp (Scotland)"),
    ("073686", "lymphadenitides", "noun", "/lɪmfˌædɪnɪˈtaɪdiːz/", "bệnh viêm hạch bạch huyết (y học)"),
    ("073687", "melanoses", "noun", "/ˌmɛləˈnoʊsiːz/", "tình trạng tăng sắc tố đen melanin"),
    ("073688", "mentums", "noun", "/ˈmɛntəmz/", "phần cằm; tấm môi dưới côn trùng"),
    ("073689", "methocarbamols", "noun", "/ˌmɛθoʊˈkɑːrbəˌmɒlz/", "thuốc giãn cơ vân methocarbamol"),
    ("073690", "millibars", "noun", "/ˈmɪlɪˌbɑːrz/", "đơn vị áp suất milibar (mbar)"),
    ("073691", "mintmarks", "noun", "/ˈmɪntˌmɑːrks/", "ký hiệu xưởng đúc trên đồng xu"),
    ("073692", "misquotations", "noun", "/ˌmɪskwoʊˈteɪʃənz/", "sự trích dẫn sai lệch nguyên văn"),
    ("073693", "modioli", "noun", "/moʊˈdaɪəˌlaɪ/", "trụ xoắn ốc tai (giải phẫu học)"),
    ("073694", "modioluses", "noun", "/moʊˈdaɪələsɪz/", "trụ xoắn ốc tai (giải phẫu học)"),
    ("073695", "moreens", "noun", "/məˈriːnz/", "vải len bông dệt gân sóng làm rèm"),
    ("073696", "mythologists", "noun", "/mɪˈθɒlədʒɪsts/", "nhà nghiên cứu thần thoại học"),
    ("073697", "nephrolithiases", "noun", "/ˌnɛfroʊlɪˈθaɪəsiːz/", "bệnh sỏi thận đường tiết niệu"),
    ("073698", "nomograms", "noun", "/ˈnɒməˌɡræmz/", "toán đồ đồ thị tính toán nhanh"),
    ("073699", "osteolyses", "noun", "/ˌɒstiˈɒlɪˌsiːz/", "hiện tượng tiêu hủy mô xương"),
    ("073700", "outaouaises", "noun", "/ˈuːtəˌweɪz/", "sông Ottawa (Outaouais Canada)"),
    ("073701", "overpopulates", "verb", "/ˌoʊvərˈpɒpjʊˌleɪts/", "làm dân số tăng quá tải mật độ"),
    ("073702", "overpopulating", "verb", "/ˌoʊvərˈpɒpjʊˌleɪtɪŋ/", "đang làm dân số tăng quá tải"),
]

with open("scratch/b35_r08_raw_p2.json") as f:
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

with open("scratch/b35_r08_p2.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r08_p2.json OK")
