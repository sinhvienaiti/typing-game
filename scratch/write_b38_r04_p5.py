import json

RECORDS = [
    ("086903", "siblings", "noun", "/ˈsɪblɪŋz/", "anh chị em ruột"),
    ("086904", "sibship", "noun", "/ˈsɪbˌʃɪp/", "nhóm anh chị em ruột cùng cha mẹ"),
    ("086905", "sibyllic", "adj", "/sɪˈbɪlɪk/", "thuộc nữ tiên tri; mang tính sấm"),
    ("086906", "sibyls", "noun", "/ˈsɪbəlz/", "nữ tiên tri cổ đại"),
    ("086907", "siccative", "noun", "/ˈsɪkətɪv/", "chất làm khô nhanh sơn"),
    ("086908", "sice", "noun", "/saɪs/", "mặt sáu nút trên quân xúc xắc"),
    ("086909", "sickbag", "noun", "/ˈsɪkˌbæɡ/", "túi nôn trên máy bay"),
    ("086910", "sicked", "verb", "/sɪkt/", "đã suỵt chó tấn công; đã nôn mửa"),
    ("086911", "sickened", "verb", "/ˈsɪkənd/", "đã làm phát ốm; đã làm kinh tởm"),
    ("086912", "sickeningness", "noun", "/ˈsɪkənɪŋnəs/", "sự gây buồn nôn; tính kinh tởm"),
    ("086913", "sickens", "verb", "/ˈsɪkənz/", "làm phát ốm; khiến ghê tởm"),
    ("086914", "sicker", "adj", "/ˈsɪkər/", "ốm nặng hơn; chắc chắn (Scotland)"),
    ("086915", "sickheadache", "noun", "/ˈsɪkˌhɛdˌeɪk/", "chứng đau nửa đầu kèm buồn nôn"),
    ("086916", "sicking", "verb", "/ˈsɪkɪŋ/", "đang suỵt chó đuổi; đang buồn nôn"),
    ("086917", "sickish", "adj", "/ˈsɪkɪʃ/", "hơi khó ở; hơi buồn nôn"),
    ("086918", "sicklepod", "noun", "/ˈsɪkəlˌpɑːd/", "cây muồng quả lưỡi liềm"),
    ("086919", "sickliness", "noun", "/ˈsɪklinəs/", "thể trạng ốm yếu; sự sến sẩm"),
    ("086920", "sicknesses", "noun", "/ˈsɪknəsɪz/", "căn bệnh; cơn ốm đau"),
    ("086921", "sicks", "verb", "/sɪks/", "suỵt chó xông vào cắn; làm phát ốm"[:35]),
    ("086922", "sidalcea", "noun", "/saɪˈdælsiə/", "chi cây cẩm quỳ đồng cỏ Bắc Mỹ"),
    ("086923", "sidebone", "noun", "/ˈsaɪdˌboʊn/", "bệnh vôi hóa sụn móng ngựa"),
    ("086924", "sideburns", "noun", "/ˈsaɪdˌbɜːrnz/", "tóc mai; râu quai nón hai bên"),
    ("086925", "sided", "verb", "/ˈsaɪdɪd/", "đã đứng về phe; đã ốp ván tường"),
    ("086926", "sidelined", "verb", "/ˈsaɪdˌlaɪnd/", "đã gạt ra ngoài lề; đã loại khỏi"),
    ("086927", "sidelines", "verb", "/ˈsaɪdˌlaɪnz/", "gạt ra ngoài lề; đẩy khỏi sân"),
    ("086928", "sideling", "adj", "/ˈsaɪdlɪŋ/", "nghiêng xiên; đi ngang dè chừng"),
    ("086929", "sidelining", "verb", "/ˈsaɪdˌlaɪnɪŋ/", "đang gạt ra ngoài lề"),
    ("086930", "sideman", "noun", "/ˈsaɪdˌmæn/", "nhạc công đệm trong ban nhạc"),
    ("086931", "sidepiece", "noun", "/ˈsaɪdˌpiːs/", "mảnh ghép bên hông; tình nhân phụ"),
    ("086932", "sideritis", "noun", "/ˌsɪdəˈraɪtɪs/", "chi trà thảo mộc vùng núi Sideritis"[:35]),
    ("086933", "sideroad", "noun", "/ˈsaɪdˌroʊd/", "đường nhánh; đường phụ rẽ ngang"),
    ("086934", "sideroblast", "noun", "/ˈsɪdərəˌblæst/", "nguyên hồng cầu chứa hạt sắt"),
    ("086935", "siderocyte", "noun", "/ˈsɪdərəˌsaɪt/", "hồng cầu chứa hạt sắt"),
    ("086936", "siderography", "noun", "/ˌsɪdəˈrɑːɡrəfi/", "kỹ thuật khắc bản in trên thép"),
    ("086937", "siderolite", "noun", "/ˈsɪdərəˌlaɪt/", "thiên thạch sắt đá"),
    ("086938", "sideropenia", "noun", "/ˌsɪdəroʊˈpiːniə/", "tình trạng thiếu sắt trong máu"),
    ("086939", "siderophilin", "noun", "/ˌsɪdəˈrɑːfəlɪn/", "protein vận chuyển sắt transferrin"[:35]),
    ("086940", "siderosis", "noun", "/ˌsɪdəˈroʊsɪs/", "bệnh nhiễm bụi sắt ở phổi hay mắt"[:35]),
    ("086941", "sides", "verb", "/saɪdz/", "đứng về phe; ốp ván vách tường"),
    ("086942", "sidesman", "noun", "/ˈsaɪdzmən/", "người hướng dẫn chỗ ngồi nhà thờ"),
    ("086943", "sidespin", "noun", "/ˈsaɪdˌspɪn/", "độ xoáy ngang của quả bóng"),
    ("086944", "sidesplitter", "noun", "/ˈsaɪdˌsplɪtər/", "câu chuyện cười vỡ bụng"),
    ("086945", "sidesplitting", "adj", "/ˈsaɪdˌsplɪtɪŋ/", "cực kỳ buồn cười; cười nghiêng ngả"),
    ("086946", "sidesplittingly", "adv", "/ˈsaɪdˌsplɪtɪŋli/", "buồn cười vỡ bụng"),
    ("086947", "sidestroke", "noun", "/ˈsaɪdˌstroʊk/", "kiểu bơi nghiêng một bên"),
    ("086948", "sidled", "verb", "/ˈsaɪdəld/", "đã rón rén đi ngang; lén tiến lại"[:35]),
    ("086949", "sidles", "verb", "/ˈsaɪdəlz/", "rón rén đi ngang; lén lút lại gần"),
    ("086950", "sidling", "verb", "/ˈsaɪdlɪŋ/", "đang rón rén đi ngang; lén tiến"),
    ("086951", "sidy", "adj", "/ˈsaɪdi/", "ra vẻ ta đây; huênh hoang làm bộ"),
    ("086952", "siemreap", "noun", "/siˈɛm riˈɛp/", "tỉnh Xiêm Riệp (Campuchia)"),
    ("086953", "sierras", "noun", "/siˈɛrəz/", "dãy núi răng cưa; cá thu Vua"),
    ("086954", "sievebone", "noun", "/ˈsiːvˌboʊn/", "xương sàng (hộp sọ)"),
    ("086955", "sieved", "verb", "/siːvd/", "đã rây qua lưới; đã sàng lọc"),
    ("086956", "sieves", "verb", "/siːvz/", "rây qua lưới; sàng lọc"),
    ("086957", "sieving", "verb", "/ˈsiːvɪŋ/", "đang rây qua lưới; đang sàng lọc"),
    ("086958", "sifted", "verb", "/ˈsɪftɪd/", "đã rây mịn; đã sàng lọc kỹ"),
    ("086959", "siftings", "noun", "/ˈsɪftɪŋz/", "phần cặn còn lại sau khi rây sàng"),
    ("086960", "sifts", "verb", "/sɪfts/", "rây mịn; sàng lọc kỹ càng"),
    ("086961", "sigeh", "noun", "/siːˈɡɛ/", "hôn nhân có thời hạn (Hồi giáo)"),
    ("086962", "sighed", "verb", "/saɪd/", "đã thở dài"),
    ("086963", "sighing", "verb", "/ˈsaɪɪŋ/", "đang thở dài"),
    ("086964", "sighs", "verb", "/saɪz/", "thở dài; rì rào (gió thổi)"),
    ("086965", "sighthole", "noun", "/ˈsaɪtˌhoʊl/", "lỗ ngắm; lỗ nhìn quan sát"),
    ("086966", "sightlessness", "noun", "/ˈsaɪtləsnəs/", "tình trạng mù lòa"),
    ("086967", "sightliness", "noun", "/ˈsaɪtlinəs/", "vẻ đẹp mắt; dáng vẻ dễ coi"),
    ("086968", "sightread", "verb", "/ˈsaɪtˌriːd/", "đọc thị tấu bản nhạc ngay lập tức"[:35]),
    ("086969", "sightreader", "noun", "/ˈsaɪtˌriːdər/", "người đọc thị tấu nhạc trực tiếp"),
    ("086970", "sightsing", "verb", "/ˈsaɪtˌsɪŋ/", "xướng âm đọc nốt nhạc ngay lập tức"[:35]),
    ("086971", "sightworthy", "adj", "/ˈsaɪtˌwɜːrði/", "đáng xem; ngoạn mục"),
    ("086972", "sigil", "noun", "/ˈsɪdʒəl/", "ấn ký huyền bí; con dấu niêm phong"),
    ("086973", "sigillate", "adj", "/ˈsɪdʒəˌleɪt/", "có đóng dấu ấn; trang trí khắc dấu"[:35]),
    ("086974", "sigillography", "noun", "/ˌsɪdʒəˈlɑːɡrəfi/", "ấn chương học (nghiên cứu con dấu)"),
    ("086975", "sigmate", "adj", "/ˈsɪɡmeɪt/", "uốn cong hình chữ S"),
    ("086976", "sigmation", "noun", "/sɪɡˈmeɪʃən/", "sự thêm phụ âm s (ngôn ngữ học)"),
    ("086977", "sigmodon", "noun", "/ˈsɪɡməˌdɑːn/", "chi chuột bông châu Mỹ Sigmodon"),
    ("086978", "sigmoidectomy", "noun", "/ˌsɪɡmɔɪˈdɛktəmi/", "phẫu thuật cắt đoạn đại tràng sigma"[:35]),
    ("086979", "sigmoidoscope", "noun", "/sɪɡˈmɔɪdəˌskoʊp/", "ống nội soi đại tràng sigma"),
    ("086980", "signable", "adj", "/ˈsaɪnəbəl/", "có thể ký tên xác nhận được"),
    ("086981", "signalement", "noun", "/sɪɡˈnælmənt/", "bản mô tả đặc điểm nhận dạng"),
    ("086982", "signalisation", "noun", "/ˌsɪɡnəlaɪˈzeɪʃən/", "hệ thống biển báo tín hiệu"),
    ("086983", "signalise", "verb", "/ˈsɪɡnəˌlaɪz/", "đánh dấu nổi bật; lắp đèn tín hiệu"[:35]),
    ("086984", "signalized", "verb", "/ˈsɪɡnəˌlaɪzd/", "đã lắp đặt đèn tín hiệu; đánh dấu"[:35]),
    ("086985", "signalizes", "verb", "/ˈsɪɡnəˌlaɪzɪz/", "lắp đèn tín hiệu; báo hiệu"),
    ("086986", "signalizing", "verb", "/ˈsɪɡnəˌlaɪzɪŋ/", "đang lắp đèn tín hiệu; báo hiệu"),
    ("086987", "signalled", "verb", "/ˈsɪɡnəld/", "đã ra hiệu; đã phát tín hiệu"),
    ("086988", "signalling", "verb", "/ˈsɪɡnəlɪŋ/", "đang ra hiệu; đang phát tín hiệu"),
    ("086989", "signalmen", "noun", "/ˈsɪɡnəlmən/", "nhân viên gác ghi tín hiệu đường sắt"[:35]),
    ("086990", "signalment", "noun", "/ˈsɪɡnəlmənt/", "bản mô tả đặc điểm nhận dạng"),
    ("086991", "signals", "verb", "/ˈsɪɡnəlz/", "ra hiệu; phát tín hiệu báo"),
    ("086992", "signifies", "verb", "/ˈsɪɡnəˌfaɪz/", "biểu thị; có nghĩa là; báo hiệu"),
    ("086993", "signifying", "verb", "/ˈsɪɡnəˌfaɪɪŋ/", "đang biểu thị; đang báo hiệu"),
    ("086994", "signiory", "noun", "/ˈsiːnjəri/", "lãnh địa lãnh chúa; chính quyền"),
    ("086995", "signless", "adj", "/ˈsaɪnləs/", "không có dấu hiệu; không triệu chứng"[:35]),
    ("086996", "signori", "noun", "/siːnˈjɔːri/", "quý ông; các ngài (tiếng Ý)"),
    ("086997", "signory", "noun", "/ˈsiːnjəri/", "lãnh địa phong kiến; quyền lãnh chúa"[:35]),
    ("086998", "signs", "verb", "/saɪnz/", "ký tên; làm dấu hiệu; ký hợp đồng"),
    ("086999", "signum", "noun", "/ˈsɪɡnəm/", "dấu hiệu; ký hiệu toán học (sgn)"),
    ("087000", "sihasapa", "noun", "/ˌsiːhɑːˈsɑːpə/", "bộ tộc người da đỏ Sihasapa"),
    ("087001", "silaged", "verb", "/ˈsaɪlɪdʒd/", "đã ủ chua làm thức ăn gia súc"),
    ("087002", "silages", "verb", "/ˈsaɪlɪdʒɪz/", "ủ chua làm thức ăn gia súc"),
]

# Replace all slices cleanly <= 35 chars
RECORDS[18] = ("086921", "sicks", "verb", "/sɪks/", "suỵt chó tấn công; làm phát ốm")
RECORDS[29] = ("086932", "sideritis", "noun", "/ˌsɪdəˈraɪtɪs/", "chi trà núi Sideritis")
RECORDS[36] = ("086939", "siderophilin", "noun", "/ˌsɪdəˈrɑːfəlɪn/", "protein tải sắt transferrin")
RECORDS[37] = ("086940", "siderosis", "noun", "/ˌsɪdəˈroʊsɪs/", "bệnh nhiễm bụi sắt phổi mắt")
RECORDS[45] = ("086948", "sidled", "verb", "/ˈsaɪdəld/", "đã rón rén đi ngang; lén lại gần")
RECORDS[65] = ("086968", "sightread", "verb", "/ˈsaɪtˌriːd/", "đọc thị tấu bản nhạc ngay")
RECORDS[67] = ("086970", "sightsing", "verb", "/ˈsaɪtˌsɪŋ/", "xướng âm ngay khi nhìn bản nhạc")
RECORDS[70] = ("086973", "sigillate", "adj", "/ˈsɪdʒəˌleɪt/", "có đóng dấu ấn; khắc họa tiết")
RECORDS[75] = ("086978", "sigmoidectomy", "noun", "/ˌsɪɡmɔɪˈdɛktəmi/", "phẫu thuật cắt đại tràng sigma")
RECORDS[80] = ("086983", "signalise", "verb", "/ˈsɪɡnəˌlaɪz/", "đánh dấu nổi bật; lắp đèn hiệu")
RECORDS[81] = ("086984", "signalized", "verb", "/ˈsɪɡnəˌlaɪzd/", "đã lắp đèn tín hiệu; đánh dấu")
RECORDS[86] = ("086989", "signalmen", "noun", "/ˈsɪɡnəlmən/", "nhân viên gác tín hiệu đường sắt")
RECORDS[92] = ("086995", "signless", "adj", "/ˈsaɪnləs/", "không có dấu hiệu; vô dấu")
RECORDS[94] = ("086997", "signory", "noun", "/ˈsiːnjəri/", "lãnh địa; quyền lãnh chúa")

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b38_r04_raw_p5.json"))
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

json.dump(out, open("scratch/b38_r04_reviewed_p5.json", "w"), ensure_ascii=False, indent=2)
print("b38_r04_p5 saved OK")
