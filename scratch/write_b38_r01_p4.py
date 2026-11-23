import json

RECORDS = [
    ("085303", "schnorrer", "noun", "/ˈʃnɔːrər/", "kẻ ăn bám; kẻ chực chờ xin xỏ"),
    ("085304", "schnozzle", "noun", "/ˈʃnɑːzəl/", "cái mũi to (tiếng lóng)"),
    ("085305", "schnozzles", "noun", "/ˈʃnɑːzəlz/", "cái mũi to (tiếng lóng)"),
    ("085306", "scholars", "noun", "/ˈskɑːlərz/", "học giả; người nhận học bổng"),
    ("085307", "scholarships", "noun", "/ˈskɑːlərˌʃɪps/", "học bổng; học vấn uyên bác"),
    ("085308", "schomburgkia", "noun", "/ʃɑːmˈbɜːrkiə/", "chi phong lan Schomburgkia"),
    ("085309", "schonbein", "noun", "/ˈʃɜːrnˌbaɪn/", "nhà hóa học Christian Schönbein"),
    ("085310", "schoolable", "adj", "/ˈskuːləbəl/", "đến tuổi đi học; có thể dạy được"),
    ("085311", "schoolboyish", "adj", "/ˈskuːlˌbɔɪɪʃ/", "trẻ con; ngây ngô như nam sinh"),
    ("085312", "schooled", "verb", "/skuːld/", "đã dạy dỗ; đã rèn luyện kỹ"),
    ("085313", "schoolfellow", "noun", "/ˈskuːlˌfɛloʊ/", "bạn học cũ; bạn cùng trường"),
    ("085314", "schoolgirlish", "adj", "/ˈskuːlˌɡɜːrlɪʃ/", "ngây thơ nhí nhảnh như nữ sinh"),
    ("085315", "schoolhouses", "noun", "/ˈskuːlˌhaʊzɪz/", "ngôi trường nhỏ; nhà trường"),
    ("085316", "schoolings", "noun", "/ˈskuːlɪŋz/", "việc học hành; sự huấn luyện"),
    ("085317", "schoolman", "noun", "/ˈskuːlmən/", "nhà triết học kinh viện"),
    ("085318", "schoolmasterly", "adj", "/ˈskuːlˌmæstərli/", "vẻ nghiêm nghị như thầy đồ"),
    ("085319", "schoolmasters", "noun", "/ˈskuːlˌmæstərz/", "hiệu trưởng nam; thầy giáo cũ"),
    ("085320", "schools", "verb", "/skuːlz/", "dạy dỗ; huấn luyện; bơi thành đàn"),
    ("085321", "schoolteacherly", "adj", "/ˈskuːlˌtiːtʃərli/", "khuôn phép kiểu giáo viên"),
    ("085322", "schooltime", "noun", "/ˈskuːlˌtaɪm/", "giờ học ở trường; thời đi học"),
    ("085323", "schorl", "noun", "/ʃɔːrl/", "khoáng vật tourmalin đen (schorl)"),
    ("085324", "schrod", "noun", "/ʃrɑːd/", "cá tuyết non; cá haddock non"),
    ("085325", "schtickl", "noun", "/ˈʃtɪkəl/", "một chút xíu; đoạn nhỏ"),
    ("085326", "schtik", "noun", "/ʃtɪk/", "mánh hài quen; trò diễn đặc trưng"),
    ("085327", "schtikl", "noun", "/ˈʃtɪkəl/", "một chút xíu; đoạn nhỏ"),
    ("085328", "schwanpan", "noun", "/ˈʃwɑːnˌpæn/", "bàn tính gảy Trung Hoa"),
    ("085329", "schwarzschild", "noun", "/ˈʃvɑːrtsˌʃɪlt/", "nhà vật lý thiên văn Schwarzschild"),
    ("085330", "sciadopityaceae", "noun", "/ˌsaɪədəˌpɪtiˈeɪsiːˌiː/", "họ Thông dù Nhật Bản"),
    ("085331", "sciadopitys", "noun", "/ˌsaɪəˈdɑːpɪtɪs/", "cây thông dù Nhật Bản"),
    ("085332", "sciaena", "noun", "/saɪˈiːnə/", "chi cá đù Sciaena"),
    ("085333", "sciaenid", "noun", "/saɪˈiːnɪd/", "cá họ Cá đù"),
    ("085334", "sciaenidae", "noun", "/saɪˈiːnɪˌdiː/", "họ Cá đù (Sciaenidae)"),
    ("085335", "sciaenops", "noun", "/saɪˈiːnɑːps/", "chi cá đù đỏ Đại Tây Dương"),
    ("085336", "sciagram", "noun", "/ˈsaɪəˌɡræm/", "phim chụp X-quang; mặt cắt đứng"),
    ("085337", "sciagrammatic", "adj", "/ˌsaɪəɡrəˈmætɪk/", "thuộc ảnh chụp X-quang"),
    ("085338", "sciagraph", "noun", "/ˈsaɪəˌɡræf/", "mặt cắt đứng; phim chụp X-quang"),
    ("085339", "sciagraphic", "adj", "/ˌsaɪəˈɡræfɪk/", "thuộc thuật vẽ bóng; X-quang"),
    ("085340", "sciagraphy", "noun", "/saɪˈɑːɡrəfi/", "thuật vẽ bóng đổ; phép chụp X-quang"[:35]),
    ("085341", "sciamachy", "noun", "/saɪˈæməki/", "cuộc đánh bóng; trận chiến tưởng tượng"[:35]),
    ("085342", "sciantific", "adj", "/ˌsaɪənˈtɪfɪk/", "thuộc khoa học"),
    ("085343", "sciarid", "noun", "/ˈsaɪərɪd/", "ruồi nấm nhỏ"),
    ("085344", "sciaridae", "noun", "/saɪˈærɪˌdiː/", "họ Ruồi nấm (Sciaridae)"),
    ("085345", "sciences", "noun", "/ˈsaɪənsɪz/", "ngành khoa học"),
    ("085346", "scient", "adj", "/ˈsaɪənt/", "am hiểu; thông thạo"),
    ("085347", "sciential", "adj", "/saɪˈɛnʃəl/", "thuộc khoa học; giàu tri thức"),
    ("085348", "scientism", "noun", "/ˈsaɪənˌtɪzəm/", "chủ nghĩa duy khoa học"),
    ("085349", "scientistic", "adj", "/ˌsaɪənˈtɪstɪk/", "theo chủ nghĩa duy khoa học"),
    ("085350", "scientists", "noun", "/ˈsaɪəntɪsts/", "nhà khoa học"),
    ("085351", "scilicet", "adv", "/ˈsɪlɪsɛt/", "nghĩa là; tức là (luật pháp)"),
    ("085352", "scimiter", "noun", "/ˈsɪmɪtər/", "thanh đao cong Trung Đông"),
    ("085353", "scincella", "noun", "/sɪnˈsɛlə/", "chi thằn lằn bóng đất Scincella"),
    ("085354", "scincid", "noun", "/ˈsɪnsɪd/", "thằn lằn bóng họ Scincidae"),
    ("085355", "scincidae", "noun", "/ˈsɪnsɪˌdiː/", "họ Thằn lằn bóng (Scincidae)"),
    ("085356", "scincus", "noun", "/ˈsɪŋkəs/", "chi thằn lằn cát Scincus"),
    ("085357", "scindapsus", "noun", "/sɪnˈdæpsəs/", "chi cây trầu bà bạc Scindapsus"),
    ("085358", "scintillant", "adj", "/ˈsɪntələnt/", "lấp lánh; sáng chói sắc sảo"),
    ("085359", "scintillated", "verb", "/ˈsɪntəˌleɪtɪd/", "đã lấp lánh; đã tỏa sáng"),
    ("085360", "scintillates", "verb", "/ˈsɪntəˌleɪts/", "lấp lánh; tỏa sáng rực rỡ"),
    ("085361", "scintillator", "noun", "/ˈsɪntəˌleɪtər/", "chất nhấp nháy phát quang"),
    ("085362", "scintillometer", "noun", "/ˌsɪntəˈlɑːmɪtər/", "máy đo phóng xạ nhấp nháy"),
    ("085363", "scintiscanner", "noun", "/ˈsɪntɪˌskænər/", "máy quét xạ hình đồng vị"),
    ("085364", "sciograph", "noun", "/ˈsaɪəˌɡræf/", "hình cắt đứng công trình"),
    ("085365", "sciography", "noun", "/saɪˈɑːɡrəfi/", "kỹ thuật vẽ bóng đổ kiến trúc"),
    ("085366", "sciolism", "noun", "/ˈsaɪəˌlɪzəm/", "sự hiểu biết nông cạn hời hợt"),
    ("085367", "sciolist", "noun", "/ˈsaɪəlɪst/", "kẻ dốt hay khoe chữ; học giả rởm"),
    ("085368", "sciolistic", "adj", "/ˌsaɪəˈlɪstɪk/", "nông cạn; hời hợt khoe mẽ"),
    ("085369", "sciomachy", "noun", "/saɪˈɑːməki/", "cuộc chiến với cái bóng tưởng tượng"[:35]),
    ("085370", "scionphilous", "adj", "/ˌsaɪəˈnɑːfɪləs/", "ưa bóng râm"),
    ("085371", "scionphyll", "noun", "/ˈsaɪənˌfɪl/", "cây có lá ưa bóng"),
    ("085372", "scionphyte", "noun", "/ˈsaɪənˌfaɪt/", "thực vật ưa bóng râm"),
    ("085373", "scirrhous", "adj", "/ˈsɪrəs/", "xơ cứng (khối u ung thư)"),
    ("085374", "scirrhus", "noun", "/ˈsɪrəs/", "khối ung thư xơ cứng"),
    ("085375", "scirroco", "noun", "/səˈrɑːkoʊ/", "gió nóng ẩm Địa Trung Hải"),
    ("085376", "scissel", "noun", "/ˈsɪsəl/", "vụn kim loại dư khi đúc tiền"),
    ("085377", "scissile", "adj", "/ˈsɪsəl/", "có thể tách cắt dễ dàng"),
    ("085378", "scissored", "verb", "/ˈsɪzərd/", "đã cắt bằng kéo; đã kẹp chân"),
    ("085379", "scissoring", "verb", "/ˈsɪzərɪŋ/", "đang cắt bằng kéo; đang kẹp"),
    ("085380", "scissortail", "noun", "/ˈsɪzərˌteɪl/", "chim đớp ruồi đuôi kéo"),
    ("085381", "scissura", "noun", "/sɪˈʒʊrə/", "rãnh nứt; khe hở giải phẫu"),
    ("085382", "scissure", "noun", "/ˈsɪʒər/", "khe nứt hẹp; sự chia cắt"),
    ("085383", "sciuridae", "noun", "/saɪˈjʊrɪˌdiː/", "họ Sóc (Sciuridae)"),
    ("085384", "sciurine", "noun", "/ˈsaɪjəˌraɪn/", "loài thuộc họ Sóc"),
    ("085385", "sciuroid", "adj", "/saɪˈjʊrɔɪd/", "giống sóc; giống đuôi sóc"),
    ("085386", "sciuromorpha", "noun", "/saɪˌjʊrəˈmɔːrfə/", "phân bộ Dạng sóc"),
    ("085387", "sclaff", "noun", "/sklæf/", "cú đánh golf cày xuống cỏ"),
    ("085388", "sclav", "adj", "/slɑːv/", "thuộc dân tộc Slav"),
    ("085389", "sclavonic", "adj", "/sləˈvɑːnɪk/", "thuộc ngôn ngữ Slav"),
    ("085390", "scleral", "adj", "/ˈsklɪrəl/", "thuộc củng mạc mắt"),
    ("085391", "scleranthus", "noun", "/skləˈrænθəs/", "chi cỏ Scleranthus"),
    ("085392", "scleredema", "noun", "/ˌsklɪrɪˈdiːmə/", "bệnh phù cứng da"),
    ("085393", "sclereid", "noun", "/ˈsklɛriɪd/", "tế bào đá (mô cứng thực vật)"),
    ("085394", "sclerenchyma", "noun", "/skləˈrɛŋkɪmə/", "mô cứng thực vật"),
    ("085395", "scleriasis", "noun", "/skləˈraɪəsɪs/", "chứng xơ cứng mô"),
    ("085396", "sclerid", "noun", "/ˈsklɛrɪd/", "tế bào đá (mô cứng thực vật)"),
    ("085397", "sclerification", "noun", "/ˌsklɛrɪfɪˈkeɪʃən/", "quá trình hóa cứng thành gỗ"),
    ("085398", "scleritis", "noun", "/skləˈraɪtɪs/", "viêm củng mạc mắt"),
    ("085399", "scleritization", "noun", "/ˌsklɛrɪtaɪˈzeɪʃən/", "sự hóa cứng kitin (côn trùng)"),
    ("085400", "scleroblast", "noun", "/ˈsklɪrəˌblæst/", "tế bào tạo gai xương bọt biển"),
    ("085401", "sclerocarp", "noun", "/ˈsklɪrəˌkɑːrp/", "lớp vỏ quả cứng"),
    ("085402", "sclerodermataceae", "noun", "/ˌsklɪroʊdɜːrməˈteɪsiːˌiː/", "họ Nấm trứng đất"),
]

# Clean 085340, 085341, 085369 without slices
RECORDS[37] = ("085340", "sciagraphy", "noun", "/saɪˈɑːɡrəfi/", "thuật vẽ bóng; chụp X-quang")
RECORDS[38] = ("085341", "sciamachy", "noun", "/saɪˈæməki/", "cuộc chiến với cái bóng ảo")
RECORDS[66] = ("085369", "sciomachy", "noun", "/saɪˈɑːməki/", "cuộc chiến với cái bóng ảo")

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b38_r01_raw_p4.json"))
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

json.dump(out, open("scratch/b38_r01_reviewed_p4.json", "w"), ensure_ascii=False, indent=2)
print("b38_r01_p4 saved OK")
