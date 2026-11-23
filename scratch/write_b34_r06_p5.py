import json

items = [
    ("067903", "towellings", "noun", "/ˈtaʊəlɪŋz/", "vải dệt bông thô để may khăn lau"),
    ("067904", "ulvas", "noun", "/ˈʌlvəz/", "rong cải biển xanh thuộc chi Ulva"),
    ("067905", "ureases", "noun", "/jʊəˈriːeɪsɪz/", "enzym ureaza phân giải phân urê"),
    ("067906", "vacillations", "noun", "/ˌvæsəˈleɪʃənz/", "sự do dự lưỡng lự; sự dao động"),
    ("067907", "wallopings", "noun", "/ˈwɒləpɪŋz/", "trận đòn nhừ tử; thất bại thảm hại"),
    ("067908", "aleksandr nikolayevich scriabin", "phrase", "/ˌælɪɡˈzændər ˌnɪkəˈlaɪəvɪtʃ skriˈɑːbɪn/", "nhà soạn nhạc Nga A. N. Scriabin"),
    ("067909", "american feverfew", "phrase", "/əˈmɛrɪkən ˈfiːvərfjuː/", "cây cúc quinin hoang dã Bắc Mỹ"),
    ("067910", "aneroid barometer", "phrase", "/ˈænəˌrɔɪd bəˈrɒmɪtər/", "phong vũ biểu hộp kim loại khô"),
    ("067911", "betula pendula", "phrase", "/ˈbɛtjʊlə ˈpɛndjʊlə/", "cây bạch dương cành rủ châu Âu"),
    ("067912", "bodoni font", "phrase", "/boʊˈdoʊni fɒnt/", "kiểu chữ in có chân hiện đại Bodoni"),
    ("067913", "camelina sativa", "phrase", "/ˌkæməˈlaɪnə səˈtaɪvə/", "cây cải dầu camelina trồng lấy hạt"),
    ("067914", "chaim azriel weizmann", "phrase", "/ˈxaɪm ˌæzriəl ˈvaɪtsmən/", "Tổng thống đầu tiên Israel Weizmann"),
    ("067915", "comoro islands", "phrase", "/ˈkɒməroʊ ˈaɪləndz/", "quần đảo Comoros ở Ấn Độ Dương"),
    ("067916", "curcuma domestica", "phrase", "/ˈkɜːrkjʊmə dəˈmɛstɪkə/", "cây nghệ vàng trồng làm gia vị"),
    ("067917", "datura arborea", "phrase", "/dəˈtjuːrə ɑːrˈbɔːriə/", "cây cà độc dược hoa loa kèn thân gỗ"),
    ("067918", "el libertador", "phrase", "/ɛl ˌliːbɛərtɑːˈdɔːr/", "danh hiệu Người Giải phóng Bolívar"),
    ("067919", "eucalyptus globulus", "phrase", "/ˌjuːkəˈlɪptəs ˈɡlɒbjʊləs/", "cây bạch đàn xanh lá tinh dầu"),
    ("067920", "feodor mikhailovich dostoevsky", "phrase", "/ˈfjɔːdər mɪˈkaɪləvɪtʃ ˌdɒstəˈjɛfski/", "đại văn hào Nga Fyodor Dostoevsky"),
    ("067921", "fere phenomenon", "phrase", "/fɛər fɪˈnɒmɪnɒn/", "hiện tượng thay đổi điện trở da"),
    ("067922", "ficus carica", "phrase", "/ˈfaɪkəs ˈkɛərɪkə/", "cây vả tây trồng lấy quả ngọt"),
    ("067923", "ficus religiosa", "phrase", "/ˈfaɪkəs rɪˌlɪdʒiˈoʊsə/", "cây bồ đề thiêng liêng của Phật"),
    ("067924", "fraxinus latifolia", "phrase", "/ˈfræksɪnəs ˌlætɪˈfoʊliə/", "cây tần bì lá rộng vùng Oregon"),
    ("067925", "furring strip", "phrase", "/ˈfɜːrɪŋ strɪp/", "thanh nẹp gỗ lót phẳng ốp tường"),
    ("067926", "genus carcharias", "phrase", "/ˈdʒiːnəs kɑːrˈkɛəriəs/", "chi cá mập hổ cát Carcharias"),
    ("067927", "genus crotalaria", "phrase", "/ˈdʒiːnəs ˌkrɒtəˈlɛəriə/", "chi cây sục sạc Crotalaria"),
    ("067928", "genus galium", "phrase", "/ˈdʒiːnəs ˈɡeɪliəm/", "chi cây hoa sữa đông Galium"),
    ("067929", "genus hedera", "phrase", "/ˈdʒiːnəs ˈhɛdərə/", "chi dây thường xuân leo bám Hedera"),
    ("067930", "genus helleborus", "phrase", "/ˈdʒiːnəs ˌhɛlɪˈbɔːrəs/", "chi hoa giáng sinh Helleborus"),
    ("067931", "genus pyrethrum", "phrase", "/ˈdʒiːnəs paɪˈriːθrəm/", "chi hoa cúc trừ sâu Pyrethrum"),
    ("067932", "genus sagitta", "phrase", "/ˈdʒiːnəs səˈdʒɪtə/", "chi sâu mũi tên biển Sagitta"),
    ("067933", "genus simulium", "phrase", "/ˈdʒiːnəs sɪˈmjuːliəm/", "chi ruồi đen hút máu Simulium"),
    ("067934", "genus uria", "phrase", "/ˈdʒiːnəs ˈjʊəriə/", "chi chim biển Uria Bắc Cực"),
    ("067935", "gold panner", "phrase", "/ɡoʊld ˈpænər/", "người đãi cát tìm vàng thủ công"),
    ("067936", "gravida ii", "phrase", "/ˈɡrævɪdə tuː/", "sản phụ mang thai lần thứ hai"),
    ("067937", "gravida iii", "phrase", "/ˈɡrævɪdə θriː/", "sản phụ mang thai lần thứ ba"),
    ("067938", "greater whitethroat", "phrase", "/ˈɡreɪtər ˈwaɪtˌθroʊt/", "chim chích họng trắng lớn châu Âu"),
    ("067939", "helleborus niger", "phrase", "/ˌhɛlɪˈbɔːrəs ˈnaɪdʒər/", "hoa hồng Giáng sinh trắng nở đông"),
    ("067940", "hume blake cronyn", "phrase", "/hjuːm bleɪk ˈkroʊnɪn/", "nam diễn viên Hume Blake Cronyn"),
    ("067941", "hume cronyn", "phrase", "/hjuːm ˈkroʊnɪn/", "nam diễn viên Mỹ Hume Cronyn"),
    ("067942", "lake onega", "phrase", "/leɪk oʊˈnɛɡə/", "hồ nước ngọt lớn Onega ở Nga"),
    ("067943", "lateen sail", "phrase", "/ləˈtiːn seɪl/", "cánh buồm tam giác xéo truyền thống"),
    ("067944", "lesser whitethroat", "phrase", "/ˈlɛsər ˈwaɪtˌθroʊt/", "chim chích họng trắng nhỏ Á Âu"),
    ("067945", "musculus biceps femoris", "phrase", "/ˈmʌskjələs ˈbaɪsɛps ˈfɛmərɪs/", "cơ nhị đầu mặt sau xương đùi"),
    ("067946", "mytilus edulis", "phrase", "/ˈmɪtɪləs ˈɛdjʊlɪs/", "con vẹm xanh vỏ đen ăn được"),
    ("067947", "necrotizing enterocolitis", "phrase", "/ˈnɛkrəˌtaɪzɪŋ ˌɛntəroʊkoʊˈlaɪtɪs/", "bệnh viêm ruột hoại tử sơ sinh"),
    ("067948", "nolo contendere", "phrase", "/ˈnoʊloʊ kənˈtɛndəri/", "tuyên bố không tranh cãi bản án"),
    ("067949", "osmanthus americanus", "phrase", "/ɒzˈmænθəs əˌmɛrɪˈkeɪnəs/", "cây hoa mộc hương dại Mỹ"),
    ("067950", "paper toweling", "phrase", "/ˈpeɪpər ˈtaʊəlɪŋ/", "cuộn giấy thấm dùng lau tay bếp"),
    ("067951", "passionflower family", "phrase", "/ˈpæʃənˌflaʊər ˈfæməli/", "họ Lạc tiên dây leo chanh dây"),
    ("067952", "passionflower vine", "phrase", "/ˈpæʃənˌflaʊər vaɪn/", "dây leo hoa lạc tiên chanh dây"),
    ("067953", "photoconductive cell", "phrase", "/ˌfoʊtoʊkənˈdʌktɪv sɛl/", "cảm biến quang trở nhạy ánh sáng"),
    ("067954", "pier luigi nervi", "phrase", "/pjɛər luːˈiːdʒi ˈnɛərvi/", "kiến trúc sư kết cấu Ý Nervi"),
    ("067955", "potamogeton americanus", "phrase", "/ˌpɒtəmoʊˈdʒiːtɒn əˌmɛrɪˈkeɪnəs/", "cây rong mái chèo Bắc Mỹ"),
    ("067956", "pyriform lobe", "phrase", "/ˈpɪrɪfɔːrm loʊb/", "thùy vỏ não khứu giác hình quả lê"),
    ("067957", "rachet up", "phrase", "/ˈrætʃɪt ʌp/", "tăng dần từng nấc (biến thể)"),
    ("067958", "rattail cactus", "phrase", "/ˈrætˌteɪl ˈkæktəs/", "xương rồng thân rủ đuôi chuột"),
    ("067959", "red osier dogwood", "phrase", "/rɛd ˈoʊʒər ˈdɒɡwʊd/", "cây giác mộc cành đỏ Bắc Mỹ"),
    ("067960", "ribes sativum", "phrase", "/ˈraɪbiːz səˈtaɪvəm/", "cây lý chua đỏ trồng làm mứt"),
    ("067961", "ricinus communis", "phrase", "/ˈrɪsɪnəs ˈkɒmjʊnɪs/", "cây thầu dầu hạt ép lấy dầu"),
    ("067962", "rock gunnel", "phrase", "/rɒk ˈɡʌnəl/", "cá chạch đá thân dẹt ven bờ biển"),
    ("067963", "salvia divinorum", "phrase", "/ˈsælviə ˌdɪvɪˈnɔːrəm/", "cây xô thơm gây ảo giác Mexico"),
    ("067964", "semipermeable membrane", "phrase", "/ˌsɛmiˈpɜːrmiəbəl ˈmɛmbreɪn/", "màng bán thấm lọc chọn lọc phân tử"),
    ("067965", "sinoatrial node", "phrase", "/ˌsaɪnoʊˈeɪtriəl noʊd/", "nút xoang nhĩ tạo nhịp tim tự nhiên"),
    ("067966", "sphenoid fontanelle", "phrase", "/ˈsfiːnɔɪd ˌfɒntəˈnɛl/", "thóp bướm bên thái dương trẻ sơ"),
    ("067967", "styptic weed", "phrase", "/ˈstɪptɪk wiːd/", "cây muồng cốt khí; cỏ cầm máu"),
    ("067968", "tyan shan", "phrase", "/tiˈɑːn ʃɑːn/", "dãy núi cao Thiên Sơn ở Trung Á"),
    ("067969", "viscid mushroom", "phrase", "/ˈvɪsɪd ˈmʌʃruːm/", "nấm mũ nhớt mọc dưới rừng thông"),
    ("067970", "william schwenk gilbert", "phrase", "/ˈwɪljəm ʃwɛŋk ˈɡɪlbərt/", "nhà soạn kịch hài Anh W. Gilbert"),
    ("067971", "agrigentos", "noun", "/ˌɑːɡriˈdʒɛntoʊz/", "thành phố cổ Agrigento ở Sicily Ý"),
    ("067972", "aldols", "noun", "/ˈældɒlz/", "hợp chất hóa học hữu cơ aldol"),
    ("067973", "antabuses", "noun", "/ˈæntəˌbjuːsɪz/", "thuốc cai rượu gây sợ Antabuse"),
    ("067974", "antidiabetics", "noun", "/ˌæntidaɪəˈbɛtɪks/", "thuốc điều trị bệnh tiểu đường"),
    ("067975", "aplysiae", "noun", "/əˈplɪʒiː/", "chi ốc sên thỏ biển Aplysia"),
    ("067976", "ardeas", "noun", "/ˈɑːrdiəz/", "chi chim diệc lớn cổ dài Ardea"),
    ("067977", "arikaras", "noun", "/əˈrɪkərəz/", "bộ tộc bản địa Arikara Bắc Mỹ"),
    ("067978", "asphodels", "noun", "/ˈæsfəˌdɛlz/", "hoa bách hợp cánh sao asphodel"),
    ("067979", "aurigas", "noun", "/ɔːˈraɪɡəz/", "chòm sao Ngự Phu ở thiên cầu bắc"),
    ("067980", "benzedrines", "noun", "/ˈbɛnzəˌdriːnz/", "thuốc kích thích Benzedrine"),
    ("067981", "bionomicses", "noun", "/ˌbaɪəˈnɒmɪksɪz/", "sinh thái học môi trường sinh vật"),
    ("067982", "blackcaps", "noun", "/ˈblækˌkæps/", "chim chích mũ đen; quả mâm xôi đen"),
    ("067983", "bobwhites", "noun", "/ˈbɒbˌwaɪts/", "chim cút đồng cỏ bobwhite Bắc Mỹ"),
    ("067984", "bromuses", "noun", "/ˈbroʊməsɪz/", "cỏ bromus thuộc chi Bromus"),
    ("067985", "caelums", "noun", "/ˈsiːləmz/", "chòm sao Điêu Cụ Đục thiên cầu nam"),
    ("067986", "caesurae", "noun", "/sɪˈzjʊəriː/", "chỗ ngắt nhịp giữa dòng thơ nhạc"),
    ("067987", "caesuras", "noun", "/sɪˈzjʊərəz/", "nhịp ngừng ngắt quãng giữa câu thơ"),
    ("067988", "capercaillies", "noun", "/ˌkæpərˈkeɪliz/", "gà rừng lớn capercaillie châu Âu"),
    ("067989", "caracaras", "noun", "/ˌkærəˈkɑːrəz/", "chim ưng ăn xác caracara châu Mỹ"),
    ("067990", "cascaras", "noun", "/kæˈskɛərəz/", "vỏ cây cascara dùng làm thuốc xổ"),
    ("067991", "castaneas", "noun", "/kæˈsteɪniəz/", "cây dẻ ăn hạt thuộc chi Castanea"),
    ("067992", "ceramicists", "noun", "/səˈræmɪsɪsts/", "nghệ nhân chế tác đồ gốm sứ"),
    ("067993", "charolaises", "noun", "/ˌʃærəˈleɪz/", "giống bò thịt lông trắng Charolais"),
    ("067994", "clubbier", "adj", "/ˈklʌbiər/", "cởi mở giao du hợp hội nhóm hơn"),
    ("067995", "clubbiest", "adj", "/ˈklʌbiɪst/", "cởi mở giao du hợp hội nhóm nhất"),
    ("067996", "coffeas", "noun", "/ˈkɒfiəz/", "cây cà phê thuộc chi Coffea"),
    ("067997", "comraderies", "noun", "/ˌkɒmˈrɑːdəriz/", "tình đồng chí bạn bè gắn bó"),
    ("067998", "copts", "noun", "/kɒpts/", "người Cơ đốc giáo bản địa Copt Ai"),
    ("067999", "crudities", "noun", "/ˈkruːdɪtiz/", "lời thô lỗ tục tĩu; trạng thái thô"),
    ("068000", "dagestanis", "noun", "/ˌdɑːɡɪˈstɑːniz/", "người dân cộng hòa Dagestan Nga"),
    ("068001", "decapods", "noun", "/ˈdɛkəˌpɒdz/", "động vật giáp xác mười chân như tôm"),
    ("068002", "deportees", "noun", "/ˌdiːpɔːrˈtiːz/", "người bị trục xuất khỏi lãnh thổ"),
]

with open("scratch/b34_r06_raw_p5.json") as f:
    raw = json.load(f)

assert len(items) == 100
assert len(raw) == 100
allowed_pos = {"noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det", "phrase"}

out = []
for r, (rid, hw, pos, ipa, vi) in zip(raw, items):
    assert r["id"].endswith("." + rid), f"ID mismatch: {r['id']} != {rid}"
    assert r["hw"] == hw, f"HW mismatch: {r['hw']} != {hw}"
    assert pos in allowed_pos, f"Bad POS {pos} for {hw}"
    assert len(vi) <= 35, f"VI too long ({len(vi)}): {hw} -> {vi}"
    assert ipa.startswith("/") and ipa.endswith("/") and ipa.count("/") == 2, f"Bad IPA: {hw} -> {ipa}"
    inner = ipa[1:-1]
    assert inner and not inner.startswith(" ") and not inner.endswith(" "), f"Empty/space IPA: {hw} -> {ipa}"
    rec = dict(r)
    rec["pos"] = pos
    rec["ipa"] = ipa
    rec["vi"] = vi
    rec["status"] = "reviewed"
    out.append(rec)

with open("scratch/b34_r06_p5.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r06_p5.json OK")
