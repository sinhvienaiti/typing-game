import json

items = [
    ("071803", "moorages", "noun", "/ˈmʊərɪdʒɪz/", "bến neo đậu tàu; phí neo đậu tàu"),
    ("071804", "ninepences", "noun", "/ˈnaɪnpənsɪz/", "đồng chín xu cũ của Anh"),
    ("071805", "nitrazepams", "noun", "/naɪˈtræzɪˌpæmz/", "thuốc an thần gây ngủ nitrazepam"),
    ("071806", "nitrobenzenes", "noun", "/ˌnaɪtroʊˈbɛnziːnz/", "hợp chất hữu cơ nitrobenzen"),
    ("071807", "onagers", "noun", "/ˈɒnədʒərz/", "lừa hoang châu Á; máy bắn đá cổ"),
    ("071808", "onanisms", "noun", "/ˈoʊnəˌnɪzəmz/", "hành vi tự kích dục (thuật ngữ cũ)"),
    ("071809", "outmatched", "verb", "/ˌaʊtˈmætʃt/", "đã áp đảo, vượt trội hơn hẳn"),
    ("071810", "outmatches", "verb", "/ˌaʊtˈmætʃɪz/", "áp đảo, tỏ ra vượt trội hơn hẳn"),
    ("071811", "outmatching", "verb", "/ˌaʊtˈmætʃɪŋ/", "đang áp đảo, vượt trội hơn hẳn"),
    ("071812", "overachieved", "verb", "/ˌoʊvərəˈtʃiːvd/", "đã đạt thành tích vượt mức kỳ vọng"),
    ("071813", "overachieves", "verb", "/ˌoʊvərəˈtʃiːvz/", "đạt thành tích vượt mức kỳ vọng"),
    ("071814", "overachieving", "verb", "/ˌoʊvərəˈtʃiːvɪŋ/", "đang đạt thành tích vượt kỳ vọng"),
    ("071815", "peptones", "noun", "/ˈpɛptoʊnz/", "hỗn hợp peptit thủy phân pepton"),
    ("071816", "percales", "noun", "/pərˈkeɪlz/", "vải cotton dệt trơn mịn percale"),
    ("071817", "perorations", "noun", "/ˌpɛrəˈreɪʃənz/", "đoạn kết hùng hồn của bài diễn văn"),
    ("071818", "pictors", "noun", "/ˈpɪktərz/", "chòm sao Hội Họa phương nam"),
    ("071819", "pigweeds", "noun", "/ˈpɪɡˌwiːdz/", "cỏ dền hoặc rau muối dại"),
    ("071820", "piperacillins", "noun", "/ˌpɪpərəˈsɪlɪnz/", "thuốc kháng sinh piperacillin"),
    ("071821", "plantigrades", "noun", "/ˈplæntɪˌɡreɪdz/", "động vật đi bằng cả gan bàn chân"),
    ("071822", "poolrooms", "noun", "/ˈpuːlˌruːmz/", "phòng chơi bi-a; sòng cá cược"),
    ("071823", "pyrographies", "noun", "/paɪˈrɒɡrəfiz/", "nghệ thuật bút lửa đốt hình gỗ"),
    ("071824", "ratholes", "noun", "/ˈrætˌhoʊlz/", "hang chuột; căn phòng tồi tàn"),
    ("071825", "resurged", "verb", "/rɪˈsɜːrdʒd/", "đã trỗi dậy hồi sinh trở lại"),
    ("071826", "resurges", "verb", "/rɪˈsɜːrdʒɪz/", "trỗi dậy hồi sinh trở lại"),
    ("071827", "resurging", "verb", "/rɪˈsɜːrdʒɪŋ/", "đang trỗi dậy hồi sinh trở lại"),
    ("071828", "revivified", "verb", "/rɪˈvɪvɪˌfaɪd/", "đã hồi sinh tiếp thêm sức sống"),
    ("071829", "revivifies", "verb", "/rɪˈvɪvɪˌfaɪz/", "hồi sinh làm sống lại đầy sức"),
    ("071830", "revivifying", "verb", "/rɪˈvɪvɪˌfaɪɪŋ/", "đang hồi sinh làm sống lại"),
    ("071831", "riesmans", "noun", "/ˈriːzmənz/", "nhà xã hội học Mỹ David Riesman"),
    ("071832", "ripsaws", "noun", "/ˈrɪpˌsɔːz/", "cưa xẻ dọc thớ gỗ"),
    ("071833", "rondels", "noun", "/ˈrɒndəlz/", "thể thơ rondel Pháp; hình tròn nhỏ"),
    ("071834", "sackbuts", "noun", "/ˈsækˌbʌts/", "kèn đồng cổ (tiền thân trombone)"),
    ("071835", "sanyasis", "noun", "/sənˈjɑːsiz/", "tu sĩ khổ hạnh Ấn Độ giáo"),
    ("071836", "scabiouses", "noun", "/ˈskeɪbiəsɪz/", "cây hoa nhím biển chi Scabiosa"),
    ("071837", "scullers", "noun", "/ˈskʌlərz/", "người chèo thuyền đôi hai mái"),
    ("071838", "seconals", "noun", "/ˈsɛkənɒlz/", "thuốc an thần gây ngủ Seconal"),
    ("071839", "sensualists", "noun", "/ˈsɛnʃuəlɪsts/", "người theo chủ nghĩa khoái lạc"),
    ("071840", "sesbanias", "noun", "/sɛsˈbeɪniəz/", "cây điền thanh thuộc chi Sesbania"),
    ("071841", "setarias", "noun", "/sɪˈtɛəriəz/", "cỏ đuôi chồn thuộc chi Setaria"),
    ("071842", "skulkers", "noun", "/ˈskʌlkərz/", "kẻ lẩn trốn né tránh công việc"),
    ("071843", "sniveled", "verb", "/ˈsnɪvəld/", "đã sụt sịt khóc thút thít"),
    ("071844", "snowploughs", "noun", "/ˈsnoʊˌplaʊz/", "xe ủi dọn tuyết trên đường (Anh)"),
    ("071845", "solfeges", "noun", "/sɒlˈfɛʒɪz/", "bài tập thanh nhạc xướng âm"),
    ("071846", "stereoscopies", "noun", "/ˌstɛriˈɒskəpiz/", "kỹ thuật nhìn ảnh nổi lập thể 3D"),
    ("071847", "superinfections", "noun", "/ˌsuːpərɪnˈfɛkʃənz/", "tình trạng bội nhiễm chồng thêm"),
    ("071848", "tailfins", "noun", "/ˈteɪlˌfɪnz/", "cánh đuôi ô tô cổ; vây đuôi cá"),
    ("071849", "tektites", "noun", "/ˈtɛktaɪts/", "thiên thạch thủy tinh tektit"),
    ("071850", "termagants", "noun", "/ˈtɜːrməɡənts/", "người đàn bà đanh đá hung dữ"),
    ("071851", "tunicates", "noun", "/ˈtjuːnɪkɪts/", "động vật có bao (hải tiêu biển)"),
    ("071852", "ukases", "noun", "/juːˈkeɪsɪz/", "sắc lệnh Nga hoàng; mệnh lệnh gắt"),
    ("071853", "venipunctures", "noun", "/ˈvɛnɪˌpʌŋktʃərz/", "thủ thuật chích lấy máu tĩnh mạch"),
    ("071854", "vicegerents", "noun", "/vaɪsˈdʒɛrənts/", "phó vương; người thừa ủy quyền"),
    ("071855", "villahermosas", "noun", "/ˌviːəɛərˈmoʊsəz/", "thành phố Villahermosa ở Mexico"),
    ("071856", "wannabees", "noun", "/ˈwɒnəbiz/", "người mơ mộng bắt chước nổi tiếng"),
    ("071857", "whiptails", "noun", "/ˈwɪpˌteɪlz/", "thằn lằn đuôi roi; cá đuôi roi"),
    ("071858", "wiremans", "noun", "/ˈwaɪərmənz/", "thợ lắp đặt đường dây điện (cũ)"),
    ("071859", "xylocaines", "noun", "/ˈzaɪləˌkeɪnz/", "thuốc gây tê cục bộ Xylocaine"),
    ("071860", "adiantums", "noun", "/ˌædiˈæntəmz/", "dương xỉ tóc thần nữ chi Adiantum"),
    ("071861", "aesculuses", "noun", "/ˈɛskjʊləsɪz/", "cây dẻ ngựa thuộc chi Aesculus"),
    ("071862", "allurements", "noun", "/əˈlʊərmənts/", "sức quyến rũ mê hoặc cám dỗ"),
    ("071863", "animalisms", "noun", "/ˈænɪməˌlɪzəmz/", "bản năng thú tính; thuyết động vật"),
    ("071864", "anorectics", "noun", "/ˌænəˈrɛktɪks/", "người biếng ăn; thuốc giảm thèm ăn"),
    ("071865", "anthemises", "noun", "/ˈænθəmɪsɪz/", "cây cúc La Mã thuộc chi Anthemis"),
    ("071866", "antirrhinums", "noun", "/ˌæntɪˈraɪnəmz/", "cây hoa mõm sói chi Antirrhinum"),
    ("071867", "araguaias", "noun", "/ˌɑːrəˈɡwaɪəz/", "sông Araguaia ở miền trung Brazil"),
    ("071868", "ascomyceteses", "noun", "/ˌæskoʊmaɪˈsiːtiːzɪz/", "ngành Nấm túi (Ascomycota)"),
    ("071869", "backcloths", "noun", "/ˈbækˌklɒθs/", "phông màn nền sân khấu (Anh)"),
    ("071870", "barnburners", "noun", "/ˈbɑːrnˌbɜːrnərz/", "người quá khích; trận cầu nảy lửa"),
    ("071871", "basidiomyceteses", "noun", "/bəˌsɪdioʊmaɪˈsiːtiːzɪz/", "lớp Nấm đảm (nấm mũ, nấm hương)"),
    ("071872", "bastinadoed", "verb", "/ˌbæstɪˈneɪdoʊd/", "đã đánh đòn vào gan bàn chân"),
    ("071873", "bastinadoes", "noun", "/ˌbæstɪˈneɪdoʊz/", "hình phạt đánh vào gan bàn chân"),
    ("071874", "bastinadoing", "verb", "/ˌbæstɪˈneɪdoʊɪŋ/", "đang đánh đòn vào gan bàn chân"),
    ("071875", "bastinados", "noun", "/ˌbæstɪˈneɪdoʊz/", "hình phạt đánh vào gan bàn chân"),
    ("071876", "benineses", "noun", "/bɛˈniːnz/", "người dân nước Cộng hòa Benin"),
    ("071877", "berceuses", "noun", "/bɛərˈsɜːrzɪz/", "bài hát ru êm dịu; khúc nhạc ru"),
    ("071878", "bivalvias", "noun", "/baɪˈvælviəz/", "lớp Thân mềm hai mảnh vỏ (sò vẹm)"),
    ("071879", "blackshirts", "noun", "/ˈblækˌʃɜːrts/", "đội quân áo đen phát xít Ý"),
    ("071880", "blendes", "noun", "/blɛndz/", "quặng kẽm sunfua (spalerit)"),
    ("071881", "cappellettis", "noun", "/ˌkæpəˈlɛtiz/", "mì nhân Ý hình mũ nhỏ cappelletti"),
    ("071882", "celosiae", "noun", "/sɪˈloʊʃiˌiː/", "chi Hoa mào gà (Celosia)"),
    ("071883", "chemisorptions", "noun", "/ˌkɛmɪˈzɔːrpʃənz/", "hiện tượng hấp phụ hóa học"),
    ("071884", "compromisers", "noun", "/ˈkɒmprəˌmaɪzərz/", "người sẵn sàng thỏa hiệp nhượng bộ"),
    ("071885", "convectors", "noun", "/kənˈvɛktərz/", "máy sưởi đối lưu tản nhiệt khí"),
    ("071886", "coprolites", "noun", "/ˈkɒprəˌlaɪts/", "phân hóa thạch của động vật cổ"),
    ("071887", "corvidaes", "noun", "/ˈkɔːrvɪˌdiːz/", "họ Quạ (quạ, ác là, giẻ cùi)"),
    ("071888", "cosmopolites", "noun", "/kɒzˈmɒpəˌlaɪts/", "công dân thế giới đi khắp năm châu"),
    ("071889", "coturnixes", "noun", "/kəˈtɜːrnɪksɪz/", "chim cút đồng chi Coturnix"),
    ("071890", "cryolites", "noun", "/ˈkraɪəˌlaɪts/", "khoáng vật criolit luyện nhôm"),
    ("071891", "curlicues", "noun", "/ˈkɜːrlɪˌkjuːz/", "nét uốn xoắn hoa văn trang trí"),
    ("071892", "cyanamides", "noun", "/saɪˈænəˌmaɪdz/", "hợp chất hóa học xyanamit"),
    ("071893", "defanged", "verb", "/diːˈfæŋd/", "đã nhổ răng nanh; làm mất nọc độc"),
    ("071894", "defanging", "verb", "/diːˈfæŋɪŋ/", "đang nhổ răng nanh; vô hiệu hóa"),
    ("071895", "defangs", "verb", "/diːˈfæŋz/", "nhổ răng nanh; làm hết nguy hiểm"),
    ("071896", "divorcements", "noun", "/dɪˈvɔːrsmənts/", "sự ly hôn ly dị; sự chia tách rời"),
    ("071897", "dobras", "noun", "/ˈdoʊbrəz/", "đồng tiền dobra (São Tomé)"),
    ("071898", "donatists", "noun", "/ˈdɒnətɪsts/", "tín đồ giáo phái Donatus Bắc Phi"),
    ("071899", "eastertides", "noun", "/ˈiːstərˌtaɪdz/", "mùa lễ Phục sinh (Ki-tô giáo)"),
    ("071900", "enkephalins", "noun", "/ɛnˈkɛfəlɪnz/", "peptit thần kinh enkephalin"),
    ("071901", "eparchies", "noun", "/ˈɛpɑːrkiz/", "tỉnh hành chính Hy Lạp; giáo phận"),
    ("071902", "epaulets", "noun", "/ˈɛpəˌlɛts/", "cầu vai áo quân phục đeo quân hàm"),
]

with open("scratch/b35_r04_raw_p4.json") as f:
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

with open("scratch/b35_r04_p4.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r04_p4.json OK")
