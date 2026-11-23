import json

RECORDS = [
    ("085903", "seismogram", "noun", "/ˈsaɪzməˌɡræm/", "biểu đồ ghi địa chấn"),
    ("085904", "seismographic", "adj", "/ˌsaɪzməˈɡræfɪk/", "thuộc máy ghi địa chấn"),
    ("085905", "seismography", "noun", "/saɪzˈmɑːɡrəfi/", "phép ghi địa chấn; địa chấn học"),
    ("085906", "seismologic", "adj", "/ˌsaɪzməˈlɑːdʒɪk/", "thuộc địa chấn học"),
    ("085907", "seismologists", "noun", "/saɪzˈmɑːlədʒɪsts/", "nhà địa chấn học"),
    ("085908", "seismometer", "noun", "/saɪzˈmɑːmɪtər/", "địa chấn kế; máy đo động đất"),
    ("085909", "seismometric", "adj", "/ˌsaɪzməˈmɛtrɪk/", "thuộc phép đo địa chấn"),
    ("085910", "seismometry", "noun", "/saɪzˈmɑːmətri/", "phép đo địa chấn"),
    ("085911", "seismophobia", "noun", "/ˌsaɪzməˈfoʊbiə/", "chứng sợ động đất"),
    ("085912", "seismosaur", "noun", "/ˈsaɪzməˌsɔːr/", "khủng long cổ dài khổng lồ"),
    ("085913", "seismosaurus", "noun", "/ˌsaɪzməˈsɔːrəs/", "chi Khủng long Seismosaurus"),
    ("085914", "seismoscope", "noun", "/ˈsaɪzməˌskoʊp/", "dụng cụ phát hiện rung chấn"),
    ("085915", "seismoscopic", "adj", "/ˌsaɪzməˈskɑːpɪk/", "thuộc máy báo địa chấn"),
    ("085916", "seiurus", "noun", "/siˈjʊrəs/", "chi chim chích đất Bắc Mỹ"),
    ("085917", "seizable", "adj", "/ˈsiːzəbəl/", "có thể tịch thu; bắt giữ được"),
    ("085918", "seized", "verb", "/siːzd/", "đã nắm bắt; đã tịch thu; bị kẹt"),
    ("085919", "seizer", "noun", "/ˈsiːzər/", "người tịch thu; người bắt giữ"),
    ("085920", "seizes", "verb", "/ˈsiːzɪz/", "nắm lấy; chộp lấy; tịch thu"),
    ("085921", "seizin", "noun", "/ˈsiːzɪn/", "quyền sở hữu đất đai vĩnh viễn"),
    ("085922", "sejant", "adj", "/ˈsiːdʒənt/", "ngồi thẳng hai chân trước (huy hiệu)"[:35]),
    ("085923", "sejugoust", "adj", "/ˈsɛdʒəɡəs/", "có sáu đôi lá chét"),
    ("085924", "sekhet", "noun", "/ˈsɛkɛt/", "nữ thần đồng cỏ Ai Cập cổ"),
    ("085925", "sekos", "noun", "/ˈsiːkɑːs/", "nội điện thiêng đền thờ Hy Lạp"),
    ("085926", "selachian", "noun", "/səˈleɪkiən/", "cá sụn (cá mập, cá đuối)"),
    ("085927", "selachii", "noun", "/səˈleɪkiˌaɪ/", "bộ Cá mập thật (Selachii)"),
    ("085928", "seladang", "noun", "/səˈlɑːdɑːŋ/", "bò tót Mã Lai"),
    ("085929", "selaginellaceae", "noun", "/ˌsɛlədʒəˈnɛleɪsiːˌiː/", "họ Quyển bá (Selaginellaceae)"),
    ("085930", "selaginellales", "noun", "/ˌsɛlədʒənəˈleɪliːz/", "bộ Quyển bá (Selaginellales)"),
    ("085931", "selamlik", "noun", "/səˈlɑːmlɪk/", "khu tiếp khách nam giới (Thổ Nhĩ Kỳ)"[:35]),
    ("085932", "selcraig", "noun", "/ˈsɛlˌkreɪɡ/", "tên họ Scotland Selcraig"),
    ("085933", "selectable", "adj", "/sɪˈlɛktəbəl/", "có thể lựa chọn được"),
    ("085934", "selectance", "noun", "/sɪˈlɛktəns/", "độ chọn lọc tần số (vô tuyến)"),
    ("085935", "selecting", "verb", "/sɪˈlɛktɪŋ/", "đang lựa chọn; đang tuyển chọn"),
    ("085936", "selections", "noun", "/sɪˈlɛkʃənz/", "sự lựa chọn; bộ sưu tập chọn lọc"),
    ("085937", "selectness", "noun", "/sɪˈlɛktnəs/", "tính chọn lọc kỹ; vẻ tinh túy"),
    ("085938", "selectron", "noun", "/sɪˈlɛktrɑːn/", "ống nhớ tĩnh điện Selectron xưa"),
    ("085939", "selects", "verb", "/sɪˈlɛkts/", "lựa chọn; tuyển chọn"),
    ("085940", "selectwoman", "noun", "/sɪˈlɛktˌwʊmən/", "nữ ủy viên hội đồng thị trấn Mỹ"),
    ("085941", "selenarctos", "noun", "/ˌsɛləˈnɑːrktəs/", "chi Gấu ngựa châu Á (Selenarctos)"),
    ("085942", "selenate", "noun", "/ˈsɛləˌneɪt/", "muối selenat"),
    ("085943", "selenga", "noun", "/səˈlɛŋɡə/", "sông Selenga (Mông Cổ và Nga)"),
    ("085944", "selenic", "adj", "/sɪˈliːnɪk/", "thuộc selen; chứa selen"),
    ("085945", "selenicereus", "noun", "/sɪˌliːnɪˈsɪriəs/", "chi hoa Quỳnh nở đêm"),
    ("085946", "selenide", "noun", "/ˈsɛləˌnaɪd/", "hợp chất selenua"),
    ("085947", "selenipedium", "noun", "/sɪˌliːnɪˈpiːdiəm/", "chi phong lan hài nhiệt đới Mỹ"),
    ("085948", "selenite", "noun", "/ˈsɛləˌnaɪt/", "khoáng vật thạch cao trong suốt"),
    ("085949", "selenitic", "adj", "/ˌsɛləˈnɪtɪk/", "chứa selenit; thuộc Mặt Trăng"),
    ("085950", "selenodont", "adj", "/sɪˈliːnəˌdɑːnt/", "có răng hàm hình trăng lưỡi liềm"),
    ("085951", "selenographer", "noun", "/ˌsɛləˈnɑːɡrəfər/", "nhà nghiên cứu địa hình Mặt Trăng"[:35]),
    ("085952", "selenographic", "adj", "/sɪˌliːnəˈɡræfɪk/", "thuộc địa lý Mặt Trăng"),
    ("085953", "selenography", "noun", "/ˌsɛləˈnɑːɡrəfi/", "khoa địa hình Mặt Trăng"),
    ("085954", "selenoid", "adj", "/ˈsɛləˌnɔɪd/", "có hình trăng lưỡi liềm"),
    ("085955", "selenolatry", "noun", "/ˌsɛləˈnɑːlətri/", "tục thờ Mặt Trăng"),
    ("085956", "selenological", "adj", "/sɪˌliːnəˈlɑːdʒɪkəl/", "thuộc Mặt Trăng học"),
    ("085957", "selenologist", "noun", "/ˌsɛləˈnɑːlədʒɪst/", "nhà nghiên cứu Mặt Trăng"),
    ("085958", "selenology", "noun", "/ˌsɛləˈnɑːlədʒi/", "khoa học nghiên cứu Mặt Trăng"),
    ("085959", "selenophile", "noun", "/sɪˈliːnəˌfaɪl/", "người yêu thích Mặt Trăng"),
    ("085960", "selenotropic", "adj", "/sɪˌliːnəˈtrɑːpɪk/", "hướng về phía ánh trăng"),
    ("085961", "selenotropism", "noun", "/ˌsɛləˈnɑːtrəˌpɪzəm/", "tính hướng ánh sáng Mặt Trăng"),
    ("085962", "selfhood", "noun", "/ˈsɛlfˌhʊd/", "bản ngã; tính cách cá nhân riêng"),
    ("085963", "selfie", "noun", "/ˈsɛlfi/", "ảnh tự chụp chân dung"),
    ("085964", "selfness", "noun", "/ˈsɛlfnəs/", "tính ích kỷ; ý thức bản thân"),
    ("085965", "selfsameness", "noun", "/ˈsɛlfˌseɪmnəs/", "sự đồng nhất hoàn toàn"),
    ("085966", "selkup", "noun", "/ˈsɛlkʊp/", "người Selkup; tiếng Selkup"),
    ("085967", "sellanders", "noun", "/ˈsɛləndərz/", "bệnh ghẻ chàm khủy chân ngựa"),
    ("085968", "sellar", "adj", "/ˈsɛlər/", "thuộc hố yên xương bướm"),
    ("085969", "selliform", "adj", "/ˈsɛlɪˌfɔːrm/", "có hình yên ngựa"),
    ("085970", "sellotaped", "verb", "/ˈsɛləˌteɪpt/", "đã dán bằng băng keo trong"),
    ("085971", "sellotapes", "verb", "/ˈsɛləˌteɪps/", "dán bằng băng keo trong"),
    ("085972", "sellotaping", "verb", "/ˈsɛləˌteɪpɪŋ/", "đang dán bằng băng keo trong"),
    ("085973", "selsyn", "noun", "/ˈsɛlsɪn/", "hệ thống truyền động tự đồng bộ"),
    ("085974", "seltzogene", "noun", "/ˈsɛltsəˌdʒiːn/", "bình sục khí CO2 pha nước có ga"),
    ("085975", "selvaged", "adj", "/ˈsɛlvɪdʒd/", "có biên vải dệt chắc không tưa"),
    ("085976", "semanteme", "noun", "/sɪˈmæntiːm/", "nghĩa vị (ngôn ngữ học)"),
    ("085977", "semanticist", "noun", "/sɪˈmæntəsɪst/", "nhà ngữ nghĩa học"),
    ("085978", "semanticists", "noun", "/sɪˈmæntəsɪsts/", "nhà ngữ nghĩa học"),
    ("085979", "semantology", "noun", "/ˌsɛmənˈtɑːlədʒi/", "ngữ nghĩa học"),
    ("085980", "semaphored", "verb", "/ˈsɛməˌfɔːrd/", "đã phát tín hiệu cờ; truyền tin"),
    ("085981", "semaphores", "verb", "/ˈsɛməˌfɔːrz/", "phát tín hiệu cờ hiệu"),
    ("085982", "semaphoric", "adj", "/ˌsɛməˈfɔːrɪk/", "thuộc tín hiệu cờ hiệu"),
    ("085983", "semaphoring", "verb", "/ˈsɛməˌfɔːrɪŋ/", "đang phát tín hiệu cờ hiệu"),
    ("085984", "semaphorist", "noun", "/sɪˈmæfərɪst/", "người phát tín hiệu cờ hiệu"),
    ("085985", "semasiological", "adj", "/sɪˌmeɪsiəˈlɑːdʒɪkəl/", "thuộc ngữ nghĩa học lịch sử"),
    ("085986", "semasiologist", "noun", "/sɪˌmeɪsiˈɑːlədʒɪst/", "nhà ngữ nghĩa học"),
    ("085987", "semasiology", "noun", "/sɪˌmeɪsiˈɑːlədʒi/", "ngữ nghĩa học (nghiên cứu nghĩa từ)"[:35]),
    ("085988", "sematic", "adj", "/sɪˈmætɪk/", "mang tính cảnh báo (màu sắc)"),
    ("085989", "sematology", "noun", "/ˌsɛməˈtɑːlədʒi/", "ký hiệu học; ngữ nghĩa học"),
    ("085990", "semblable", "adj", "/ˈsɛmbləbəl/", "tương tự; giống nhau (từ cổ)"),
    ("085991", "semeiology", "noun", "/ˌsiːmaɪˈɑːlədʒi/", "triệu chứng học; ký hiệu học"),
    ("085992", "semeiotics", "noun", "/ˌsiːmaɪˈɑːtɪks/", "triệu chứng học; ký hiệu học"),
    ("085993", "sememe", "noun", "/ˈsiːmiːm/", "nghĩa vị; đơn vị nghĩa tối thiểu"),
    ("085994", "semestral", "adj", "/sɪˈmɛstrəl/", "mỗi học kỳ; sáu tháng một lần"),
    ("085995", "semestrial", "adj", "/sɪˈmɛstriəl/", "mỗi học kỳ; sáu tháng một lần"),
    ("085996", "semiabstract", "adj", "/ˌsɛmiˈæbstrækt/", "bán trừu tượng (hội họa)"),
    ("085997", "semiaxis", "noun", "/ˌsɛmiˈæksɪs/", "bán trục (hình học)"),
    ("085998", "semiaxle", "noun", "/ˌsɛmiˈæksəl/", "bán trục truyền động (ô tô)"),
    ("085999", "semibeam", "noun", "/ˈsɛmiˌbiːm/", "dầm công-xôn; nửa dầm"),
    ("086000", "semibreves", "noun", "/ˈsɛmiˌbriːvz/", "nốt tròn (âm nhạc)"),
    ("086001", "semicentenary", "adj", "/ˌsɛmisɛnˈtɛnəri/", "kỷ niệm 50 năm"),
    ("086002", "semicentennial", "adj", "/ˌsɛmisɛnˈtɛniəl/", "kỷ niệm 50 năm"),
]

# Clean 085922, 085931, 085951, 085987 without slices <= 35
RECORDS[19] = ("085922", "sejant", "adj", "/ˈsiːdʒənt/", "ngồi thẳng trên hai chân (huy hiệu)"[:35])
RECORDS[19] = ("085922", "sejant", "adj", "/ˈsiːdʒənt/", "ngồi thẳng lưng (huy hiệu)")
RECORDS[28] = ("085931", "selamlik", "noun", "/səˈlɑːmlɪk/", "khu tiếp khách nam Thổ Nhĩ Kỳ")
RECORDS[48] = ("085951", "selenographer", "noun", "/ˌsɛləˈnɑːɡrəfər/", "nhà địa hình học Mặt Trăng")
RECORDS[84] = ("085987", "semasiology", "noun", "/sɪˌmeɪsiˈɑːlədʒi/", "ngữ nghĩa học từ vựng")

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b38_r02_raw_p5.json"))
by_id = {r["id"].split(".")[-1]: r for r in raw}
out = []
for sid, hw, pos, ipa, vi in RECORDS:
    rec = dict(by_id[sid])
    assert rec["hw"] == hw, (sid, hw, rec["hw"])
    rec["pos"] = pos
    rec["ipa"] = ipa
    rec["vi"] = vi
    rec["status"] = "reviewed"
    out.append(rec)

json.dump(out, open("scratch/b38_r02_reviewed_p5.json", "w"), ensure_ascii=False, indent=2)
print("b38_r02_p5 saved OK")
