import json

RECORDS = [
    ("088703", "spindles", "verb", "/ˈspɪndəlz/", "mọc vươn dài mảnh khảnh"),
    ("088704", "spindleshanks", "noun", "/ˈspɪndəlˌʃæŋks/", "người gầy nhom chân dài khẳng khiu"),
    ("088705", "spindling", "adj", "/ˈspɪndlɪŋ/", "cao lêu nghêu mảnh khảnh yếu ớt"),
    ("088706", "spined", "adj", "/spaɪnd/", "có gai nhọn; có xương sống"),
    ("088707", "spinelessly", "adv", "/ˈspaɪnləsli/", "nhu nhược thiếu bản lĩnh"),
    ("088708", "spinelet", "noun", "/ˈspaɪnlət/", "cái gai nhỏ li ti"),
    ("088709", "spinicerebrate", "adj", "/ˌspaɪnɪˈsɛrəbrət/", "có não bộ và tủy sống"),
    ("088710", "spiniferous", "adj", "/spaɪˈnɪfərəs/", "có gai nhọn; mọc đầy gai"),
    ("088711", "spiniform", "adj", "/ˈspaɪnɪˌfɔːrm/", "có hình dạng cái gai nhọn"),
    ("088712", "spininess", "noun", "/ˈspaɪninəs/", "tính nhiều gai góc; vẻ gai góc"),
    ("088713", "spinmeister", "noun", "/ˈspaɪnˌmaɪstər/", "bậc thầy xoay chuyển dư luận"),
    ("088714", "spinnability", "noun", "/ˌspɪnəˈbɪlɪti/", "khả năng kéo thành sợi mảnh"),
    ("088715", "spinnable", "adj", "/ˈspɪnəbəl/", "kéo thành sợi được; xoay chuyển được"[:35]),
    ("088716", "spinnbar", "adj", "/ˈʃpɪnbɑːr/", "có độ kéo sợi nhớt (sinh học)"),
    ("088717", "spinnbarkeit", "noun", "/ˈʃpɪnbɑːrˌkaɪt/", "độ dai kéo sợi của dịch nhầy"),
    ("088718", "spinneret", "noun", "/ˌspɪnəˈrɛt/", "tuyến nhả tơ (nhện, sâu tằm)"),
    ("088719", "spinnery", "noun", "/ˈspɪnəri/", "nhà máy kéo sợi; xưởng xe chỉ"),
    ("088720", "spinosely", "adv", "/ˈspaɪnəsli/", "đầy gai nhọn; sắc nhọn như gai"),
    ("088721", "spinosity", "noun", "/spaɪˈnɑːsɪti/", "tình trạng nhiều gai; tính gai góc"),
    ("088722", "spinozism", "noun", "/spɪˈnoʊˌzɪzəm/", "triết học nhất nguyên của Spinoza"),
    ("088723", "spinozist", "noun", "/spɪˈnoʊzɪst/", "người theo triết học Spinoza"),
    ("088724", "spinozistic", "adj", "/ˌspɪnoʊˈzɪstɪk/", "thuộc triết học Spinoza"),
    ("088725", "spinsthariscope", "noun", "/spɪnˈθærɪˌskoʊp/", "kính đếm nhấp nháy phóng xạ"),
    ("088726", "spinstress", "noun", "/ˈspɪnstrəs/", "nữ thợ quay tơ kéo sợi"),
    ("088727", "spinthariscope", "noun", "/spɪnˈθærɪˌskoʊp/", "kính phát hiện nhấp nháy phóng xạ"),
    ("088728", "spinula", "noun", "/ˈspɪnjələ/", "gai nhỏ; ngạnh nhỏ"),
    ("088729", "spinulation", "noun", "/ˌspɪnjəˈleɪʃən/", "hệ thống gai nhỏ bao phủ"),
    ("088730", "spinule", "noun", "/ˈspaɪnjuːl/", "gai nhỏ; ngạnh nhỏ li ti"),
    ("088731", "spinuleferous", "adj", "/ˌspɪnjəˈlɪfərəs/", "có nhiều gai nhỏ li ti"),
    ("088732", "spinulescent", "adj", "/ˌspɪnjəˈlɛsənt/", "hơi mọc gai nhỏ ở đầu"),
    ("088733", "spinulose", "adj", "/ˈspɪnjəˌloʊs/", "có nhiều gai nhỏ phủ bề mặt"),
    ("088734", "spinulosis", "noun", "/ˌspɪnjəˈloʊsɪs/", "bệnh dày sừng gai nang lông"),
    ("088735", "spinulous", "adj", "/ˈspɪnjələs/", "có nhiều gai nhỏ li ti"),
    ("088736", "spinus", "noun", "/ˈspaɪnəs/", "chi chim sẻ thông (Spinus)"),
    ("088737", "spiracular", "adj", "/spaɪˈrækjələr/", "thuộc lỗ thở côn trùng"),
    ("088738", "spiraculate", "adj", "/spaɪˈrækjəlɪt/", "có lỗ thở (côn trùng, cá đuối)"),
    ("088739", "spiralis", "noun", "/spaɪˈreɪlɪs/", "cơ hoặc dây chằng xoắn ốc"),
    ("088740", "spirality", "noun", "/spaɪˈrælɪti/", "tính chất xoáy trôn ốc"),
    ("088741", "spiralled", "verb", "/ˈspaɪrəld/", "đã xoắn ốc; đã tăng vọt mất kiểm soát"[:35]),
    ("088742", "spiralling", "verb", "/ˈspaɪrəlɪŋ/", "đang xoắn ốc; đang tăng vọt nhanh"),
    ("088743", "spirals", "verb", "/ˈspaɪrəlz/", "xoay vòng xoắn ốc; tăng vọt nhanh"),
    ("088744", "spiranthes", "noun", "/spaɪˈrænθiːz/", "chi phong lan xoắn (Spiranthes)"),
    ("088745", "spireme", "noun", "/ˈspaɪriːm/", "sợi nhiễm sắc xoắn khi phân bào"),
    ("088746", "spiriferous", "adj", "/spaɪˈrɪfərəs/", "có cấu trúc xoắn ốc"),
    ("088747", "spirilla", "noun", "/spaɪˈrɪlə/", "xoắn khuẩn hình lò xo"),
    ("088748", "spirillaceae", "noun", "/ˌspaɪrəˈleɪsiːˌiː/", "họ Xoắn khuẩn (Spirillaceae)"),
    ("088749", "spiriting", "verb", "/ˈspɪrɪtɪŋ/", "đang bí mật đưa đi; khích lệ"),
    ("088750", "spiritise", "verb", "/ˈspɪrɪˌtaɪz/", "truyền tinh thần; gọi hồn"),
    ("088751", "spiritistic", "adj", "/ˌspɪrɪˈtɪstɪk/", "thuộc thuyết thông linh gọi hồn"),
    ("088752", "spiritize", "verb", "/ˈspɪrɪˌtaɪz/", "truyền tinh thần; gọi hồn"),
    ("088753", "spiritlessness", "noun", "/ˈspɪrɪtləsnəs/", "sự uể oải thiếu sức sống; thờ ơ"),
    ("088754", "spiritoso", "adj", "/ˌspɪrɪˈtoʊsoʊ/", "sôi nổi đầy khí thế (âm nhạc)"),
    ("088755", "spiritous", "adj", "/ˈspɪrɪtəs/", "có cồn rượu; tinh khiết thanh cao"),
    ("088756", "spiritualisation", "noun", "/ˌspɪrɪtʃuəlaɪˈzeɪʃən/", "sự tinh thần hóa; sự nâng tầm tâm"[:35]),
    ("088757", "spiritualise", "verb", "/ˈspɪrɪtʃuəˌlaɪz/", "tinh thần hóa; hiểu theo nghĩa tâm"),
    ("088758", "spiritualization", "noun", "/ˌspɪrɪtʃuələˈzeɪʃən/", "sự tinh thần hóa"),
    ("088759", "spiritualness", "noun", "/ˈspɪrɪtʃuəlnəs/", "tính chất tinh thần; tâm linh"),
    ("088760", "spirituals", "noun", "/ˈspɪrɪtʃuəlz/", "thánh ca dân gian người Mỹ gốc Phi"),
    ("088761", "spiritualty", "noun", "/ˈspɪrɪtʃuəlti/", "tài sản giáo hội; hàng giáo phẩm"),
    ("088762", "spirituel", "adj", "/ˌspɪrɪtʃuˈɛl/", "hóm hỉnh tinh tế; thanh tao (nam)"),
    ("088763", "spirituelle", "adj", "/ˌspɪrɪtʃuˈɛl/", "duyên dáng tinh tế sắc sảo (nữ)"),
    ("088764", "spirituousness", "noun", "/ˈspɪrɪtʃuəsnəs/", "tính chất chứa cồn rượu mạnh"),
    ("088765", "spirivalve", "adj", "/ˈspaɪrɪˌvælv/", "có vỏ xoắn ốc (ốc sên)"),
    ("088766", "spirochaeta", "noun", "/ˌspaɪrəˈkiːtə/", "chi Xoắn khuẩn Spirochaeta"),
    ("088767", "spirochaetaceae", "noun", "/ˌspaɪrəkiːˈteɪsiːˌiː/", "họ Xoắn khuẩn Spirochaetaceae"),
    ("088768", "spirochaetal", "adj", "/ˌspaɪrəˈkiːtəl/", "do xoắn khuẩn gây ra"),
    ("088769", "spirochaetales", "noun", "/ˌspaɪrəkiːˈteɪliːz/", "bộ Xoắn khuẩn (Spirochaetales)"),
    ("088770", "spirochaete", "noun", "/ˈspaɪrəˌkiːt/", "xoắn khuẩn"),
    ("088771", "spirodela", "noun", "/ˌspaɪrəˈdiːlə/", "chi Bèo tấm lớn (Spirodela)"),
    ("088772", "spirogram", "noun", "/ˈspaɪrəˌɡræm/", "biểu đồ đo chức năng hô hấp"),
    ("088773", "spirographic", "adj", "/ˌspaɪrəˈɡræfɪk/", "thuộc phép ghi biểu đồ hô hấp"),
    ("088774", "spiroid", "adj", "/ˈspaɪrɔɪd/", "có hình dạng xoắn ốc"),
    ("088775", "spirometers", "noun", "/spaɪˈrɑːmɪtərz/", "phế dung kế; máy đo dung tích phổi"),
    ("088776", "spirula", "noun", "/ˈspaɪrjələ/", "mực mai xoắn biển sâu Spirula"),
    ("088777", "spirulidae", "noun", "/spaɪˈruːlɪˌdiː/", "họ Mực mai xoắn (Spirulidae)"),
    ("088778", "spiry", "adj", "/ˈspaɪri/", "nhọn vút như tháp chuông; xoắn ốc"),
    ("088779", "spitchcock", "noun", "/ˈspɪtʃˌkɑːk/", "món lươn xẻ dọc tẩm bột nướng"),
    ("088780", "spitdevil", "noun", "/ˈspɪtˌdɛvəl/", "pháo bông xoáy nhỏ phát tia lửa"),
    ("088781", "spited", "verb", "/ˈspaɪtɪd/", "đã chơi xỏ ác ý; làm bực mình"),
    ("088782", "spites", "verb", "/spaɪts/", "chơi ác; cố tình làm bực tức ai"),
    ("088783", "spiting", "verb", "/ˈspaɪtɪŋ/", "đang chơi xỏ ác ý; làm bực tức"),
    ("088784", "spitpoison", "noun", "/ˈspɪtˌpɔɪzən/", "kẻ ném đá giấu tay chuyên vu khống"),
    ("088785", "spits", "verb", "/spɪts/", "nhổ nước bọt; phun trào; mưa lất phất"[:35]),
    ("088786", "spitted", "verb", "/ˈspɪtɪd/", "đã xiên vào que nướng"),
    ("088787", "spittlebug", "noun", "/ˈspɪtəlˌbʌɡ/", "rầy ve bọt phun bọt trắng trên cây"),
    ("088788", "spivvery", "noun", "/ˈspɪvəri/", "trò buôn gian bán lận chợ đen"),
    ("088789", "spizella", "noun", "/spɪˈzɛlə/", "chi chim sẻ châu Mỹ Spizella"),
    ("088790", "splanchnology", "noun", "/ˌsplæŋkˈnɑːlədʒi/", "tạng học (giải phẫu học nội tạng)"),
    ("088791", "splanchnotomy", "noun", "/ˌsplæŋkˈnɑːtəmi/", "phẫu tích nội tạng; cắt dây tạng"),
    ("088792", "splashback", "noun", "/ˈsplæʃˌbæk/", "tấm ốp tường chắn nước văng bếp"),
    ("088793", "splashbacks", "noun", "/ˈsplæʃˌbæks/", "tấm ốp tường chắn nước văng"),
    ("088794", "splashboard", "noun", "/ˈsplæʃˌbɔːrd/", "tấm chắn bùn nước bắn (xe ngựa)"),
    ("088795", "splashers", "noun", "/ˈsplæʃərz/", "tấm chắn bùn bánh xe"),
    ("088796", "splashes", "verb", "/ˈsplæʃɪz/", "tạt nước bắn tung tóe; giật tít"),
    ("088797", "splashiness", "noun", "/ˈsplæʃinəs/", "sự phô trương sặc sỡ; sự lầy lội"),
    ("088798", "splatters", "verb", "/ˈsplætərz/", "văng tung tóe; bắn bết khắp nơi"),
    ("088799", "splayfoot", "adj", "/ˈspleɪˌfʊt/", "có bàn chân bẹt bè ra ngoài"),
    ("088800", "splayfooted", "adj", "/ˈspleɪˌfʊtɪd/", "có bàn chân bẹt bè ngang ra ngoài"),
    ("088801", "spleenful", "adj", "/ˈspliːnfəl/", "u uất cáu kỉnh; hậm hực bực bội"),
    ("088802", "spleenish", "adj", "/ˈspliːnɪʃ/", "hơi gắt gỏng bực bội; u uất"),
]

# Remove slices cleanly <= 35 chars
RECORDS[12] = ("088715", "spinnable", "adj", "/ˈspɪnəbəl/", "kéo sợi được; xoay chuyển dư luận")
RECORDS[38] = ("088741", "spiralled", "verb", "/ˈspaɪrəld/", "đã xoắn ốc; đã tăng vọt mất kiểm")
RECORDS[38] = ("088741", "spiralled", "verb", "/ˈspaɪrəld/", "đã xoắn ốc; đã tăng vọt dữ dội")
RECORDS[53] = ("088756", "spiritualisation", "noun", "/ˌspɪrɪtʃuəlaɪˈzeɪʃən/", "sự tinh thần hóa; sự nâng tâm hồn")
RECORDS[82] = ("088785", "spits", "verb", "/spɪts/", "nhổ nước bọt; xiên nướng; mưa phùn")

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b38_r08_raw_p3.json"))
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

json.dump(out, open("scratch/b38_r08_reviewed_p3.json", "w"), ensure_ascii=False, indent=2)
print("b38_r08_p3 saved OK")
