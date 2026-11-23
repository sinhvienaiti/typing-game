import json

RECORDS = [
    ("084603", "salesmanships", "noun", "/ˈseɪlzmənˌʃɪps/", "kỹ năng bán hàng; tài chào hàng"),
    ("084604", "salesmen", "noun", "/ˈseɪlzmən/", "nam nhân viên bán hàng"),
    ("084605", "salespeople", "noun", "/ˈseɪlzˌpiːpəl/", "nhân viên bán hàng"),
    ("084606", "saleswomen", "noun", "/ˈseɪlzˌwɪmən/", "nữ nhân viên bán hàng"),
    ("084607", "salicaceae", "noun", "/ˌsælɪˈkeɪsiːˌiː/", "họ Liễu (Salicaceae)"),
    ("084608", "salicaceous", "adj", "/ˌsælɪˈkeɪʃəs/", "thuộc họ Liễu"),
    ("084609", "salicales", "noun", "/ˌsælɪˈkeɪliːz/", "bộ Liễu (Salicales)"),
    ("084610", "salicin", "noun", "/ˈsælɪsɪn/", "hoạt chất giảm đau salicin"),
    ("084611", "salicylic", "adj", "/ˌsælɪˈsɪlɪk/", "thuộc axit salicylic"),
    ("084612", "salientia", "noun", "/ˌseɪliˈɛnʃə/", "bộ Không đuôi (ếch nhái)"),
    ("084613", "salientian", "adj", "/ˌseɪliˈɛnʃən/", "thuộc bộ Ếch nhái"),
    ("084614", "saliferous", "adj", "/səˈlɪfərəs/", "chứa muối; có mỏ muối"),
    ("084615", "salification", "noun", "/ˌsælɪfɪˈkeɪʃən/", "sự tạo thành muối"),
    ("084616", "salify", "verb", "/ˈsælɪˌfaɪ/", "hóa muối; tạo thành muối"),
    ("084617", "salii", "noun", "/ˈseɪliˌaɪ/", "tu sĩ nhảy múa thờ thần Mars"),
    ("084618", "salinate", "verb", "/ˈsælɪˌneɪt/", "ướp muối; làm mặn nước"),
    ("084619", "salinization", "noun", "/ˌsælɪnəˈzeɪʃən/", "sự nhiễm mặn; sự mặn hóa đất"),
    ("084620", "salinometer", "noun", "/ˌsælɪˈnɑːmɪtər/", "máy đo độ mặn"),
    ("084621", "salinometers", "noun", "/ˌsælɪˈnɑːmɪtərz/", "máy đo độ mặn"),
    ("084622", "salival", "adj", "/səˈlaɪvəl/", "thuộc nước bọt"),
    ("084623", "salivant", "adj", "/ˈsælɪvənt/", "kích thích tiết nước bọt"),
    ("084624", "salivated", "verb", "/ˈsælɪˌveɪtɪd/", "đã tiết nước bọt; đã thèm nhỏ dãi"),
    ("084625", "salivates", "verb", "/ˈsælɪˌveɪts/", "tiết nước bọt; thèm nhỏ dãi"),
    ("084626", "salivating", "verb", "/ˈsælɪˌveɪtɪŋ/", "đang tiết nước bọt; thèm nhỏ dãi"),
    ("084627", "salivous", "adj", "/səˈlaɪvəs/", "thuộc nước bọt; giống nước bọt"),
    ("084628", "salle", "noun", "/sɑːl/", "đại sảnh; phòng lớn (tiếng Pháp)"),
    ("084629", "sallenders", "noun", "/ˈsælɪndərz/", "bệnh ghẻ chàm khủy chân sau ngựa"),
    ("084630", "saller", "noun", "/ˈsɔːlər/", "chiếu nghỉ cầu thang"),
    ("084631", "sallied", "verb", "/ˈsælid/", "đã xông ra đánh; đã đi dạo"),
    ("084632", "sallies", "verb", "/ˈsæliz/", "xông ra đánh; lên đường"),
    ("084633", "sallowish", "adj", "/ˈsæloʊɪʃ/", "hơi vàng vọt; hơi xanh xao"),
    ("084634", "sallowness", "noun", "/ˈsæloʊnəs/", "nước da vàng vọt; vẻ xanh xao"),
    ("084635", "sallowy", "adj", "/ˈsæloʊi/", "nhiều cây liễu bụi"),
    ("084636", "sallying", "verb", "/ˈsæliɪŋ/", "đang xông ra đánh; đang lên đường"),
    ("084637", "salmacis", "noun", "/ˈsælməsɪs/", "tiên nữ Salmacis (thần thoại)"),
    ("084638", "salmonet", "noun", "/ˌsæməˈnɛt/", "cá hồi non; cá phèn đỏ"),
    ("084639", "salmwood", "noun", "/ˈsɑːmˌwʊd/", "gỗ sồi Tây Ban Nha vùng nhiệt đới"),
    ("084640", "salol", "noun", "/ˈsælɔːl/", "chất sát khuẩn phenyl salicylat"),
    ("084641", "salomone", "noun", "/ˌsɑːloʊˈmoʊni/", "tên họ Ý Salomone"),
    ("084642", "salomones", "noun", "/ˌsɑːloʊˈmoʊniz/", "gia đình họ Salomone"),
    ("084643", "saloop", "noun", "/səˈluːp/", "trà thảo mộc xá xị truyền thống"),
    ("084644", "salpichroa", "noun", "/ˌsælpɪˈkroʊə/", "chi cây họ Cà Salpichroa"),
    ("084645", "salpicon", "noun", "/ˈsælpɪkɑːn/", "nhân thịt rau củ băm nhỏ sốt kem"),
    ("084646", "salpidae", "noun", "/ˈsælpɪˌdiː/", "họ Động vật có bao Salpidae"),
    ("084647", "salpiglossis", "noun", "/ˌsælpɪˈɡlɑːsɪs/", "hoa loa kèn nhung Salpiglossis"),
    ("084648", "salpinctes", "noun", "/sælˈpɪŋktiːz/", "chi chim tiêu liêu đá Bắc Mỹ"),
    ("084649", "salpingian", "adj", "/sælˈpɪndʒiən/", "thuộc vòi trứng hoặc vòi nhĩ"),
    ("084650", "salpingitis", "noun", "/ˌsælpɪnˈdʒaɪtɪs/", "viêm vòi trứng; viêm vòi nhĩ"),
    ("084651", "salpinx", "noun", "/ˈsælpɪŋks/", "vòi trứng; vòi nhĩ; kèn đồng cổ"),
    ("084652", "salsilla", "noun", "/sælˈsɪlə/", "cây khoai mỡ leo Nam Mỹ"),
    ("084653", "saltant", "adj", "/ˈsæltənt/", "nhảy vọt; biến dị nhảy bậc"),
    ("084654", "saltate", "verb", "/ˈsælˌteɪt/", "nhảy bật từng bước; di chuyển nhảy"),
    ("084655", "saltatorial", "adj", "/ˌsæltəˈtɔːriəl/", "thích nghi để nhảy vọt"),
    ("084656", "saltatory", "adj", "/ˈsæltəˌtɔːri/", "nhảy cóc; tiến từng bước nhảy"),
    ("084657", "saltcellar", "noun", "/ˈsɔːltˌsɛlər/", "lọ đựng muối ăn; hũ muối"),
    ("084658", "saltern", "noun", "/ˈsɔːltərn/", "ruộng làm muối; xưởng sản xuất muối"[:35]),
    ("084659", "saltigrade", "adj", "/ˈsæltɪˌɡreɪd/", "có chân nhảy săn mồi (nhện)"),
    ("084660", "saltimbanco", "noun", "/ˌsæltɪmˈbæŋkoʊ/", "lang băm diễn trò bán thuốc dạo"),
    ("084661", "saltish", "adj", "/ˈsɔːltɪʃ/", "hơi mặn; lờ lợ mặn"),
    ("084662", "saltlike", "adj", "/ˈsɔːltˌlaɪk/", "giống muối; có tính chất như muối"),
    ("084663", "saltness", "noun", "/ˈsɔːltnəs/", "độ mặn; vị mặn"),
    ("084664", "saltpan", "noun", "/ˈsɔːltˌpæn/", "ruộng muối; chảo muối tự nhiên"),
    ("084665", "salts", "verb", "/sɔːlts/", "rắc muối; ướp muối; rải muối"),
    ("084666", "saltus", "noun", "/ˈsæltəs/", "bước nhảy gián đoạn (lôgic học)"),
    ("084667", "saltwort", "noun", "/ˈsɔːltˌwɜːrt/", "cây muối mọc vùng đất mặn"),
    ("084668", "salubriousness", "noun", "/səˈluːbriəsnəs/", "tính trong lành; tính bổ ích"),
    ("084669", "salutariness", "noun", "/ˈsæljəˌtɛrinəs/", "tính bổ ích; tác dụng lành mạnh"),
    ("084670", "salutatory", "noun", "/səˈluːtəˌtɔːri/", "diễn văn chào mừng lễ tốt nghiệp"),
    ("084671", "saluted", "verb", "/səˈluːtɪd/", "đã chào; đã giơ tay chào"),
    ("084672", "saluter", "noun", "/səˈluːtər/", "người giơ tay chào"),
    ("084673", "salutes", "verb", "/səˈluːts/", "chào; giơ tay chào điều lệnh"),
    ("084674", "salutiferous", "adj", "/ˌsæljəˈtɪfərəs/", "có lợi cho sức khỏe; bổ dưỡng"),
    ("084675", "saluting", "verb", "/səˈluːtɪŋ/", "đang chào; đang giơ tay chào"),
    ("084676", "salvable", "adj", "/ˈsælvəbəl/", "có thể cứu vãn; trục vớt được"),
    ("084677", "salvadoraceae", "noun", "/ˌsælvədəˈreɪsiːˌiː/", "họ thực vật Salvadoraceae"),
    ("084678", "salvaged", "verb", "/ˈsælvɪdʒd/", "đã cứu hộ; đã tận dụng lại"),
    ("084679", "salvages", "verb", "/ˈsælvɪdʒɪz/", "cứu hộ; trục vớt; vớt vát lại"),
    ("084680", "salvaging", "verb", "/ˈsælvɪdʒɪŋ/", "đang cứu hộ; đang tận dụng lại"),
    ("084681", "salvationism", "noun", "/sælˈveɪʃəˌnɪzəm/", "chủ trương của Đội quân Cứu thế"),
    ("084682", "salvationist", "noun", "/sælˈveɪʃənɪst/", "thành viên Đội quân Cứu thế"),
    ("084683", "salved", "verb", "/sɑːvd/", "đã bôi thuốc mỡ; đã xoa dịu"),
    ("084684", "salverform", "adj", "/ˈsælvərˌfɔːrm/", "hình mâm dẹt trên ống hẹp (hoa)"),
    ("084685", "salves", "verb", "/sɑːvz/", "bôi thuốc mỡ; xoa dịu lương tâm"),
    ("084686", "salviniaceae", "noun", "/sælˌvɪniˈeɪsiːˌiː/", "họ Bèo ong (Salviniaceae)"),
    ("084687", "samanala", "noun", "/ˌsɑːməˈnɑːlə/", "đỉnh núi Samanala (Sri Lanka)"),
    ("084688", "samarcand", "noun", "/ˌsæmərˈkænd/", "thành phố Samarkand"),
    ("084689", "samariform", "adj", "/səˈmɛrɪˌfɔːrm/", "có dạng quả có cánh"),
    ("084690", "samarskite", "noun", "/səˈmɑːrskaɪt/", "khoáng vật phóng xạ samarskit"),
    ("084691", "sambaed", "verb", "/ˈsɑːmbəd/", "đã nhảy điệu samba"),
    ("084692", "sambaing", "verb", "/ˈsɑːmbəɪŋ/", "đang nhảy điệu samba"),
    ("084693", "sambas", "verb", "/ˈsɑːmbəz/", "nhảy điệu samba"),
    ("084694", "sambo", "noun", "/ˈsæmboʊ/", "từ miệt thị chủng tộc (lịch sử)"),
    ("084695", "sambur", "noun", "/ˈsæmbər/", "nai đen sambar"),
    ("084696", "samekh", "noun", "/ˈsɑːmɛx/", "chữ cái Do Thái Samekh"),
    ("084697", "samel", "adj", "/ˈsæməl/", "nung chưa chín kỹ (gạch)"),
    ("084698", "samely", "adv", "/ˈseɪmli/", "đều đều đơn điệu; không đổi"),
    ("084699", "samey", "adj", "/ˈseɪmi/", "đơn điệu; nhàm chán giống hệt nhau"[:35]),
    ("084700", "samgha", "noun", "/ˈsʌŋɡə/", "Tăng đoàn Phật giáo"),
    ("084701", "samiel", "noun", "/ˈsæmjəl/", "gió nóng khô sa mạc Ả Rập"),
    ("084702", "samisen", "noun", "/ˈsæmɪˌsɛn/", "đàn ba dây shamisen Nhật Bản"),
]

# Clean 084658 and 084699 without slices
RECORDS[55] = ("084658", "saltern", "noun", "/ˈsɔːltərn/", "ruộng muối; xưởng làm muối")
RECORDS[96] = ("084699", "samey", "adj", "/ˈseɪmi/", "đơn điệu; nhàm chán như nhau")

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b37_r10_raw_p2.json"))
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

json.dump(out, open("scratch/b37_r10_reviewed_p2.json", "w"), ensure_ascii=False, indent=2)
print("b37_r10_p2 saved OK")
