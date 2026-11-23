import json

raw = json.load(open("scratch/b18_r10_raw_p5.json"))
assert len(raw) == 100

reviewed = [
    {"id": "lex.en.100k.089902", "hw": "kurchi", "pos": "noun", "ipa": "/ˈkɜːrtʃi/", "vi": "cây kurchi; vỏ kurchi"},
    {"id": "lex.en.100k.089903", "hw": "kurgan", "pos": "noun", "ipa": "/ˈkʊərɡɑːn/", "vi": "gò mộ kurgan; gò mộ cổ"},
    {"id": "lex.en.100k.089904", "hw": "kuri", "pos": "noun", "ipa": "/ˈkʊəri/", "vi": "chó kuri; giống chó Maori"},
    {"id": "lex.en.100k.089905", "hw": "kurrat", "pos": "noun", "ipa": "/kʊˈrɑːt/", "vi": "tỏi tây Ai Cập; rau kurrat"},
    {"id": "lex.en.100k.089906", "hw": "kurtosis", "pos": "noun", "ipa": "/kɜːrˈtoʊsɪs/", "vi": "độ nhọn; hệ số nhọn"},
    {"id": "lex.en.100k.089907", "hw": "kurux", "pos": "noun", "ipa": "/ˈkʊrʊk/", "vi": "tiếng Kurukh; người Kurukh"},
    {"id": "lex.en.100k.089908", "hw": "kusan", "pos": "noun", "ipa": "/ˈkuːsən/", "vi": "ngôn ngữ Kusan; thổ dân Kusan"},
    {"id": "lex.en.100k.089909", "hw": "kutya", "pos": "noun", "ipa": "/kʊˈtjɑː/", "vi": "món cháo kutia; cháo ngũ cốc"},
    {"id": "lex.en.100k.089910", "hw": "kuvasz", "pos": "noun", "ipa": "/ˈkuːvɑːs/", "vi": "chó Kuvasz; chó chăn cừu"},
    {"id": "lex.en.100k.089911", "hw": "kuvi", "pos": "noun", "ipa": "/ˈkuːvi/", "vi": "tiếng Kuvi; người Kuvi"},
    {"id": "lex.en.100k.089912", "hw": "kvas", "pos": "noun", "ipa": "/kvɑːs/", "vi": "rượu kvass; nước giải khát kvass"},
    {"id": "lex.en.100k.089913", "hw": "kvetched", "pos": "verb", "ipa": "/kvɛtʃt/", "vi": "đã cằn nhằn; đã phàn nàn"},
    {"id": "lex.en.100k.089914", "hw": "kvetches", "pos": "verb", "ipa": "/ˈkvɛtʃɪz/", "vi": "cằn nhằn; phàn nàn"},
    {"id": "lex.en.100k.089915", "hw": "kvetching", "pos": "verb", "ipa": "/ˈkvɛtʃɪŋ/", "vi": "đang cằn nhằn; thói phàn nàn"},
    {"id": "lex.en.100k.089916", "hw": "kwangchow", "pos": "noun", "ipa": "/ˌɡwɑːŋˈdʒoʊ/", "vi": "Quảng Châu"},
    {"id": "lex.en.100k.089917", "hw": "kweek", "pos": "noun", "ipa": "/kwiːk/", "vi": "cỏ chỉ; cỏ gà Nam Phi"},
    {"id": "lex.en.100k.089918", "hw": "kwela", "pos": "noun", "ipa": "/ˈkwɛlə/", "vi": "nhạc kwela; điệu nhảy kwela"},
    {"id": "lex.en.100k.089919", "hw": "kwell", "pos": "noun", "ipa": "/kwɛl/", "vi": "thuốc trị ghẻ Kwell"},
    {"id": "lex.en.100k.089920", "hw": "kyanization", "pos": "noun", "ipa": "/ˌkaɪənəˈzeɪʃən/", "vi": "sự ngâm hóa chất bảo quản gỗ"},
    {"id": "lex.en.100k.089921", "hw": "kyanize", "pos": "verb", "ipa": "/ˈkaɪənaɪz/", "vi": "ngâm bảo quản gỗ"},
    {"id": "lex.en.100k.089922", "hw": "kyaw", "pos": "noun", "ipa": "/kjaʊ/", "vi": "họ Kyaw"},
    {"id": "lex.en.100k.089923", "hw": "kye", "pos": "noun", "ipa": "/kaɪ/", "vi": "đàn bò; bò"},
    {"id": "lex.en.100k.089924", "hw": "kyle", "pos": "noun", "ipa": "/kaɪl/", "vi": "eo biển hẹp; eo biển Kyle"},
    {"id": "lex.en.100k.089925", "hw": "kylin", "pos": "noun", "ipa": "/ˈkiːlɪn/", "vi": "kỳ lân; con kỳ lân"},
    {"id": "lex.en.100k.089926", "hw": "kyloe", "pos": "noun", "ipa": "/ˈkaɪloʊ/", "vi": "bò vùng cao Scotland; bò kyloe"},
    {"id": "lex.en.100k.089927", "hw": "kymogram", "pos": "noun", "ipa": "/ˈkaɪməɡræm/", "vi": "đồ thị sóng; kymogram"},
    {"id": "lex.en.100k.089928", "hw": "kymograph", "pos": "noun", "ipa": "/ˈkaɪməɡræf/", "vi": "máy ghi sóng; kymograph"},
    {"id": "lex.en.100k.089929", "hw": "kymographic", "pos": "adj", "ipa": "/ˌkaɪməˈɡræfɪk/", "vi": "thuộc máy ghi sóng; ghi sóng"},
    {"id": "lex.en.100k.089930", "hw": "kyphos", "pos": "noun", "ipa": "/ˈkaɪfɒs/", "vi": "chứng gù lưng; lưng gù"},
    {"id": "lex.en.100k.089931", "hw": "kyphosidae", "pos": "noun", "ipa": "/kaɪˈfɒsɪdiː/", "vi": "họ cá chép biển; họ cá đù"},
    {"id": "lex.en.100k.089932", "hw": "kyphosus", "pos": "noun", "ipa": "/kaɪˈfoʊsəs/", "vi": "chi cá chép biển Kyphosus"},
    {"id": "lex.en.100k.089933", "hw": "kyphotic", "pos": "adj", "ipa": "/kaɪˈfɒtɪk/", "vi": "bị gù lưng; có dáng gù"},
    {"id": "lex.en.100k.089934", "hw": "kyyiv", "pos": "noun", "ipa": "/ˈkiːɪf/", "vi": "Kyiv; thủ đô Kyiv"},
    {"id": "lex.en.100k.089935", "hw": "labanotation", "pos": "noun", "ipa": "/ˌlɑːbənəʊˈteɪʃən/", "vi": "ký hiệu múa Laban; ghi hình múa"},
    {"id": "lex.en.100k.089936", "hw": "labarum", "pos": "noun", "ipa": "/ˈlæbərəm/", "vi": "cờ hiệu La Mã; cờ labarum"},
    {"id": "lex.en.100k.089937", "hw": "labefaction", "pos": "noun", "ipa": "/ˌlæbɪˈfækʃən/", "vi": "sự làm suy yếu; sự suy đồi"},
    {"id": "lex.en.100k.089938", "hw": "labeller", "pos": "noun", "ipa": "/ˈleɪbələr/", "vi": "máy dán nhãn; người dán nhãn"},
    {"id": "lex.en.100k.089939", "hw": "labellum", "pos": "noun", "ipa": "/ləˈbɛləm/", "vi": "cánh môi hoa lan; môi hoa"},
    {"id": "lex.en.100k.089940", "hw": "labia", "pos": "noun", "ipa": "/ˈleɪbiə/", "vi": "môi âm hộ; cặp môi sinh dục"},
    {"id": "lex.en.100k.089941", "hw": "labialise", "pos": "verb", "ipa": "/ˈleɪbiəlaɪz/", "vi": "môi hóa; phát âm tròn môi"},
    {"id": "lex.en.100k.089942", "hw": "labialization", "pos": "noun", "ipa": "/ˌleɪbiələˈzeɪʃən/", "vi": "sự môi hóa; hiện tượng tròn môi"},
    {"id": "lex.en.100k.089943", "hw": "labialize", "pos": "verb", "ipa": "/ˈleɪbiəlaɪz/", "vi": "môi hóa; phát âm môi hóa"},
    {"id": "lex.en.100k.089944", "hw": "labiate", "pos": "adj", "ipa": "/ˈleɪbiɪt/", "vi": "hình môi; thuộc họ hoa môi"},
    {"id": "lex.en.100k.089945", "hw": "lability", "pos": "noun", "ipa": "/ləˈbɪləti/", "vi": "tính không ổn định; tính bất định"},
    {"id": "lex.en.100k.089946", "hw": "labionasal", "pos": "adj", "ipa": "/ˌleɪbioʊˈneɪzəl/", "vi": "thuộc âm môi-mũi"},
    {"id": "lex.en.100k.089947", "hw": "labiovelar", "pos": "adj", "ipa": "/ˌleɪbioʊˈviːlər/", "vi": "thuộc âm môi-vòm mềm"},
    {"id": "lex.en.100k.089948", "hw": "lablink", "pos": "noun", "ipa": "/ˈlæblɪŋk/", "vi": "kết nối phòng thí nghiệm"},
    {"id": "lex.en.100k.089949", "hw": "laboratorial", "pos": "adj", "ipa": "/ləˌbɒrəˈtɔːriəl/", "vi": "thuộc phòng thí nghiệm"},
    {"id": "lex.en.100k.089950", "hw": "laboratorian", "pos": "noun", "ipa": "/ˌlæbrəˈtɔːriən/", "vi": "nhân viên xét nghiệm; kỹ thuật viên"},
    {"id": "lex.en.100k.089951", "hw": "laboratories", "pos": "noun", "ipa": "/ˈlæbrətɔːriz/", "vi": "các phòng thí nghiệm"},
    {"id": "lex.en.100k.089952", "hw": "laboriousness", "pos": "noun", "ipa": "/ləˈbɔːriəsnɪs/", "vi": "sự vất vả; sự cực nhọc"},
    {"id": "lex.en.100k.089953", "hw": "labors", "pos": "verb", "ipa": "/ˈleɪbərz/", "vi": "lao động; gắng sức"},
    {"id": "lex.en.100k.089954", "hw": "laborsaving", "pos": "adj", "ipa": "/ˈleɪbərˌseɪvɪŋ/", "vi": "tiết kiệm sức lao động"},
    {"id": "lex.en.100k.089955", "hw": "labourist", "pos": "noun", "ipa": "/ˈleɪbərɪst/", "vi": "đảng viên Công Đảng; phái lao động"},
    {"id": "lex.en.100k.089956", "hw": "labours", "pos": "verb", "ipa": "/ˈleɪbərz/", "vi": "lao động; gắng sức"},
    {"id": "lex.en.100k.089957", "hw": "laboursaving", "pos": "adj", "ipa": "/ˈleɪbəˌseɪvɪŋ/", "vi": "tiết kiệm sức lao động"},
    {"id": "lex.en.100k.089958", "hw": "labra", "pos": "noun", "ipa": "/ˈleɪbrə/", "vi": "viền môi sụn; các môi trên"},
    {"id": "lex.en.100k.089959", "hw": "labret", "pos": "noun", "ipa": "/ˈleɪbrɪt/", "vi": "khuyên môi; khuyên xỏ môi"},
    {"id": "lex.en.100k.089960", "hw": "labrid", "pos": "noun", "ipa": "/ˈlæbrɪd/", "vi": "cá bàng chài; cá rạn san hô"},
    {"id": "lex.en.100k.089961", "hw": "labridae", "pos": "noun", "ipa": "/ˈlæbrɪdiː/", "vi": "họ cá bàng chài"},
    {"id": "lex.en.100k.089962", "hw": "labrocyte", "pos": "noun", "ipa": "/ˈlæbrəsaɪt/", "vi": "dưỡng bào; tế bào mast"},
    {"id": "lex.en.100k.089963", "hw": "labroid", "pos": "adj", "ipa": "/ˈlæbrɔɪd/", "vi": "giống cá bàng chài"},
    {"id": "lex.en.100k.089964", "hw": "labrouste", "pos": "noun", "ipa": "/ləˈbruːst/", "vi": "kiến trúc sư Labrouste"},
    {"id": "lex.en.100k.089965", "hw": "labrum", "pos": "noun", "ipa": "/ˈleɪbrəm/", "vi": "viền sụn khớp; môi trên côn trùng"},
    {"id": "lex.en.100k.089966", "hw": "labrys", "pos": "noun", "ipa": "/ˈlæbrɪs/", "vi": "rìu hai lưỡi cổ đại; rìu Minoan"},
    {"id": "lex.en.100k.089967", "hw": "labyrinthic", "pos": "adj", "ipa": "/ˌlæbəˈrɪnθɪk/", "vi": "như mê cung; chằng chịt; rối rắm"},
    {"id": "lex.en.100k.089968", "hw": "labyrinthodont", "pos": "noun", "ipa": "/ˌlæbəˈrɪnθədɒnt/", "vi": "lưỡng cư răng mê lộ; hóa thạch cổ"},
    {"id": "lex.en.100k.089969", "hw": "labyrinthodonta", "pos": "noun", "ipa": "/ˌlæbəˌrɪnθəˈdɒntə/", "vi": "phân lớp lưỡng cư răng mê lộ"},
    {"id": "lex.en.100k.089970", "hw": "labyrinthodontia", "pos": "noun", "ipa": "/ˌlæbəˌrɪnθəˈdɒnʃiə/", "vi": "bộ lưỡng cư răng mê lộ"},
    {"id": "lex.en.100k.089971", "hw": "laccolith", "pos": "noun", "ipa": "/ˈlækəlɪθ/", "vi": "thể nấm macma; vòm đá xâm nhập"},
    {"id": "lex.en.100k.089972", "hw": "laccopetalum", "pos": "noun", "ipa": "/ˌlækəʊˈpɛtələm/", "vi": "chi thực vật Laccopetalum"},
    {"id": "lex.en.100k.089973", "hw": "lacebark", "pos": "noun", "ipa": "/ˈleɪsbɑːrk/", "vi": "cây vỏ lưới ren; vỏ cây ren"},
    {"id": "lex.en.100k.089974", "hw": "lacebug", "pos": "noun", "ipa": "/ˈleɪsbʌɡ/", "vi": "bọ cánh lưới; bọ ren"},
    {"id": "lex.en.100k.089975", "hw": "laceless", "pos": "adj", "ipa": "/ˈleɪslɪs/", "vi": "không dây buộc; không có ren"},
    {"id": "lex.en.100k.089976", "hw": "lacelike", "pos": "adj", "ipa": "/ˈleɪslaɪk/", "vi": "giống như ren; mảnh dẻ như ren"},
    {"id": "lex.en.100k.089977", "hw": "lacepod", "pos": "noun", "ipa": "/ˈleɪspɒd/", "vi": "cây quả vỏ ren"},
    {"id": "lex.en.100k.089978", "hw": "lacerable", "pos": "adj", "ipa": "/ˈlæsərəbəl/", "vi": "dễ bị xé rách; có thể rách"},
    {"id": "lex.en.100k.089979", "hw": "lacerates", "pos": "verb", "ipa": "/ˈlæsəreɪts/", "vi": "xé rách; làm tổn thương"},
    {"id": "lex.en.100k.089980", "hw": "lacerating", "pos": "adj", "ipa": "/ˈlæsəreɪtɪŋ/", "vi": "xé lòng; gây rách nát; buốt giá"},
    {"id": "lex.en.100k.089981", "hw": "lacertian", "pos": "noun", "ipa": "/ləˈsɜːrʃən/", "vi": "loài thằn lằn; giống thằn lằn"},
    {"id": "lex.en.100k.089982", "hw": "lacertid", "pos": "noun", "ipa": "/ləˈsɜːrtɪd/", "vi": "thằn lằn chính thực; họ thằn lằn"},
    {"id": "lex.en.100k.089983", "hw": "lacertidae", "pos": "noun", "ipa": "/ləˈsɜːrtɪdiː/", "vi": "họ thằn lằn chính thức"},
    {"id": "lex.en.100k.089984", "hw": "lacertilia", "pos": "noun", "ipa": "/ˌlæsərˈtɪliə/", "vi": "phân bộ thằn lằn"},
    {"id": "lex.en.100k.089985", "hw": "lacertilian", "pos": "adj", "ipa": "/ˌlæsərˈtɪliən/", "vi": "thuộc phân bộ thằn lằn"},
    {"id": "lex.en.100k.089986", "hw": "laces", "pos": "noun", "ipa": "/ˈleɪsɪz/", "vi": "dây giày; vải ren"},
    {"id": "lex.en.100k.089987", "hw": "lacewood", "pos": "noun", "ipa": "/ˈleɪswʊd/", "vi": "gỗ vân ren; gỗ lacewood"},
    {"id": "lex.en.100k.089988", "hw": "laceword", "pos": "noun", "ipa": "/ˈleɪswɜːrd/", "vi": "từ ngữ hoa mỹ"},
    {"id": "lex.en.100k.089989", "hw": "laches", "pos": "noun", "ipa": "/ˈlætʃɪz/", "vi": "sự chậm trễ tố tụng; trễ hạn kiện"},
    {"id": "lex.en.100k.089990", "hw": "lachnolaimus", "pos": "noun", "ipa": "/ˌlæknoʊˈleɪməs/ ", "vi": "chi cá mõm lợn Lachnolaimus"},
    {"id": "lex.en.100k.089991", "hw": "lachrymation", "pos": "noun", "ipa": "/ˌlækrɪˈmeɪʃən/", "vi": "sự chảy nước mắt; sự đổ lệ"},
    {"id": "lex.en.100k.089992", "hw": "lachrymator", "pos": "noun", "ipa": "/ˈlækrɪmeɪtər/", "vi": "chất làm cay mắt; hơi cay"},
    {"id": "lex.en.100k.089993", "hw": "lachrymatory", "pos": "adj", "ipa": "/ˈlækrɪmətɔːri/", "vi": "gây cay mắt; làm chảy nước mắt"},
    {"id": "lex.en.100k.089994", "hw": "laciniate", "pos": "adj", "ipa": "/ləˈsɪnieɪt/", "vi": "xẻ tua rua; có mép răng sâu"},
    {"id": "lex.en.100k.089995", "hw": "laciniation", "pos": "noun", "ipa": "/ləˌsɪniˈeɪʃən/", "vi": "dải tua rua; sự xẻ tua rua"},
    {"id": "lex.en.100k.089996", "hw": "lackadaisicalness", "pos": "noun", "ipa": "/ˌlækəˈdeɪzɪkəlnɪs/", "vi": "tính uể oải; sự thờ ơ vô cảm"},
    {"id": "lex.en.100k.089997", "hw": "lacked", "pos": "verb", "ipa": "/lækt/", "vi": "đã thiếu; từng không có"},
    {"id": "lex.en.100k.089998", "hw": "lacker", "pos": "noun", "ipa": "/ˈlækər/", "vi": "sơn mài; lớp sơn bóng"},
    {"id": "lex.en.100k.089999", "hw": "lackland", "pos": "noun", "ipa": "/ˈlæklænd/", "vi": "người không có đất; kẻ vô điền"},
    {"id": "lex.en.100k.090000", "hw": "lacklands", "pos": "noun", "ipa": "/ˈlæklændz/", "vi": "những người không có đất"},
    {"id": "lex.en.100k.090001", "hw": "lacks", "pos": "verb", "ipa": "/læks/", "vi": "thiếu; không có"}
]

assert len(reviewed) == 100
for i, (r, rev) in enumerate(zip(raw, reviewed)):
    assert r['id'] == rev['id'] and r['hw'] == rev['hw'], f"Mismatch at {i}: {r['id']} vs {rev['id']}"
    assert rev['vi'] and len(rev['vi']) <= 35, f"vi length > 35 at {i}: {rev['vi']}"
    assert rev['pos'] in ["noun", "verb", "adj", "adv", "intj", "prep", "pron", "conj", "det", "num"], f"pos invalid at {i}: {rev['pos']}"
    ipa = rev['ipa'].strip()
    assert ipa.startswith('/') and ipa.endswith('/') and ipa.count('/') == 2, f"ipa format invalid at {i}: {ipa}"
    rev['ipa'] = ipa
    rev['status'] = "reviewed"
    rev['cefr'] = r.get('cefr')
    rev['tier'] = r.get('tier')
    rev['notes'] = r.get('notes')

json.dump(reviewed, open("scratch/b18_r10_reviewed_p5.json", "w"), ensure_ascii=False, indent=2)
data = reviewed
print("Part 5 validated successfully!")
