import json

items = [
  {"id": "lex.en.200k.059903", "hw": "phenyl salicylate", "pos": "phrase", "ipa": "/ˌfɛnəl səˈlɪsəleɪt/", "vi": "chất sát trùng phenyl salicylat"},
  {"id": "lex.en.200k.059904", "hw": "pinus virginiana", "pos": "phrase", "ipa": "/ˈpaɪnəs vərˌdʒɪniˈeɪnə/", "vi": "cây thông Virginia Bắc Mỹ"},
  {"id": "lex.en.200k.059905", "hw": "posterior meningeal artery", "pos": "phrase", "ipa": "/pɑːˈstɪəriər mɪˈnɪndʒiəl ˈɑːrtəri/", "vi": "động mạch màng não sau"},
  {"id": "lex.en.200k.059906", "hw": "redbrick university", "pos": "phrase", "ipa": "/ˌrɛdbrɪk juːnɪˈvɜːrsəti/", "vi": "đại học gạch đỏ lâu đời ở Anh"},
  {"id": "lex.en.200k.059907", "hw": "reniform leaf", "pos": "phrase", "ipa": "/ˈrɛnɪfɔːrm liːf/", "vi": "chiếc lá có hình quả thận"},
  {"id": "lex.en.200k.059908", "hw": "rete testis", "pos": "phrase", "ipa": "/ˈriːtiː ˈtɛstɪs/", "vi": "mạng lưới ống dẫn tinh hoàn"},
  {"id": "lex.en.200k.059909", "hw": "rough horsetail", "pos": "phrase", "ipa": "/rʌf ˈhɔːrsteɪl/", "vi": "cây cỏ tháp bút thân nhám"},
  {"id": "lex.en.200k.059910", "hw": "spotted barramundi", "pos": "phrase", "ipa": "/ˈspɑːtɪd ˌbærəˈmʌndi/", "vi": "loài cá chẽm đốm nước ngọt"},
  {"id": "lex.en.200k.059911", "hw": "striate area", "pos": "phrase", "ipa": "/ˈstraɪeɪt ˈɛəriə/", "vi": "vùng thị giác sơ cấp vỏ não"},
  {"id": "lex.en.200k.059912", "hw": "striate body", "pos": "phrase", "ipa": "/ˈstraɪeɪt ˈbɑːdi/", "vi": "thể vân nhân nền não bộ"},
  {"id": "lex.en.200k.059913", "hw": "subordinating conjunction", "pos": "phrase", "ipa": "/səˈbɔːrdɪneɪtɪŋ kənˈdʒʌŋkʃən/", "vi": "liên từ phụ thuộc câu"},
  {"id": "lex.en.200k.059914", "hw": "swamp horsetail", "pos": "phrase", "ipa": "/swɑːmp ˈhɔːrsteɪl/", "vi": "cây cỏ tháp bút đầm lầy"},
  {"id": "lex.en.200k.059915", "hw": "tattletale gray", "pos": "phrase", "ipa": "/ˈtætlteɪl ɡreɪ/", "vi": "màu xám bẩn ố của vải giặt"},
  {"id": "lex.en.200k.059916", "hw": "tattletale grey", "pos": "phrase", "ipa": "/ˈtætlteɪl ɡreɪ/", "vi": "màu vải giặt bị xám ố"},
  {"id": "lex.en.200k.059917", "hw": "theropod dinosaur", "pos": "phrase", "ipa": "/ˈθɛrəpɑːd ˈdaɪnəsɔːr/", "vi": "khủng long chân thú ăn thịt"},
  {"id": "lex.en.200k.059918", "hw": "trapezius muscle", "pos": "phrase", "ipa": "/trəˈpiːziəs ˈmʌsl/", "vi": "cơ hình thang vùng lưng gáy"},
  {"id": "lex.en.200k.059919", "hw": "virginia katherine mcmath", "pos": "phrase", "ipa": "/vərˈdʒɪnjə ˈkæθrɪn məkˈmæθ/", "vi": "nữ diễn viên Ginger Rogers"},
  {"id": "lex.en.200k.059920", "hw": "water horsetail", "pos": "phrase", "ipa": "/ˈwɔːtər ˈhɔːrsteɪl/", "vi": "cỏ tháp bút mọc dưới nước"},
  {"id": "lex.en.200k.059921", "hw": "wood horsetail", "pos": "phrase", "ipa": "/wʊd ˈhɔːrsteɪl/", "vi": "cây cỏ tháp bút mọc trong rừng"},
  {"id": "lex.en.200k.059922", "hw": "aalborgs", "pos": "noun", "ipa": "/ˈɔːlbɔːrɡz/", "vi": "thành phố cảng Aalborg ở Đan Mạch"},
  {"id": "lex.en.200k.059923", "hw": "adobos", "pos": "noun", "ipa": "/əˈdoʊboʊz/", "vi": "món thịt kho adobo Philippines"},
  {"id": "lex.en.200k.059924", "hw": "alcazars", "pos": "noun", "ipa": "/ælˈkæzərz/", "vi": "lâu đài pháo đài hoàng gia Alcazar"},
  {"id": "lex.en.200k.059925", "hw": "amaryllises", "pos": "noun", "ipa": "/ˌæmərˈɪlɪsɪz/", "vi": "hoa huệ tây; hoa loa kèn đỏ"},
  {"id": "lex.en.200k.059926", "hw": "ananiases", "pos": "noun", "ipa": "/ˌænəˈnaɪəsɪz/", "vi": "kẻ nói dối trơ trẽn; kẻ lừa đảo"},
  {"id": "lex.en.200k.059927", "hw": "angiograms", "pos": "noun", "ipa": "/ˈændʒioʊɡræmz/", "vi": "ảnh chụp x-quang mạch máu"},
  {"id": "lex.en.200k.059928", "hw": "antihypertensives", "pos": "noun", "ipa": "/ˌæntiˌhaɪpərˈtɛnsɪvz/", "vi": "thuốc hạ huyết áp điều trị tim"},
  {"id": "lex.en.200k.059929", "hw": "apuses", "pos": "noun", "ipa": "/ˈæpjəsɪz/", "vi": "chòm sao Thiên Yến vùng nam thiên"},
  {"id": "lex.en.200k.059930", "hw": "arases", "pos": "noun", "ipa": "/ˈærəzɪz/", "vi": "dòng sông Aras vùng Kavkaz"},
  {"id": "lex.en.200k.059931", "hw": "arnicas", "pos": "noun", "ipa": "/ˈɑːrnɪkəz/", "vi": "cây cúc arnica chiết xuất xoa bóp"},
  {"id": "lex.en.200k.059932", "hw": "ashurs", "pos": "noun", "ipa": "/ˈæʃʊərz/", "vi": "thần tối cao Ashur của Assyria"},
  {"id": "lex.en.200k.059933", "hw": "assemblywomen", "pos": "noun", "ipa": "/əˈsɛmbliwɪmɪn/", "vi": "các nữ dân biểu hội đồng lập pháp"},
  {"id": "lex.en.200k.059934", "hw": "beepers", "pos": "noun", "ipa": "/ˈbiːpərz/", "vi": "máy nhắn tin bíp; còi báo động"},
  {"id": "lex.en.200k.059935", "hw": "blackmailers", "pos": "noun", "ipa": "/ˈblækmeɪlərz/", "vi": "kẻ tống tiền; kẻ đe dọa tống tiền"},
  {"id": "lex.en.200k.059936", "hw": "braggarts", "pos": "noun", "ipa": "/ˈbræɡərts/", "vi": "kẻ khoác lác; người hay ba hoa"},
  {"id": "lex.en.200k.059937", "hw": "breccias", "pos": "noun", "ipa": "/ˈbrɛtʃiəz/", "vi": "đá dăm kết cấu địa chất"},
  {"id": "lex.en.200k.059938", "hw": "bywords", "pos": "noun", "ipa": "/ˈbaɪwɜːrdz/", "vi": "câu ngạn ngữ; ví dụ điển hình"},
  {"id": "lex.en.200k.059939", "hw": "caissons", "pos": "noun", "ipa": "/ˈkeɪsənz/", "vi": "thùng chìm thi công móng cầu"},
  {"id": "lex.en.200k.059940", "hw": "camases", "pos": "noun", "ipa": "/ˈkæməsɪz/", "vi": "cây hoa chuông camas củ ăn được"},
  {"id": "lex.en.200k.059941", "hw": "chandis", "pos": "noun", "ipa": "/ˈtʃʌndiz/", "vi": "nữ thần chiến binh hung dữ Chandi"},
  {"id": "lex.en.200k.059942", "hw": "chioses", "pos": "noun", "ipa": "/ˈkaɪɑːsɪz/", "vi": "hòn đảo Chios nổi tiếng Hy Lạp"},
  {"id": "lex.en.200k.059943", "hw": "commanderies", "pos": "noun", "ipa": "/kəˈmændəriz/", "vi": "quân doanh dòng hiệp sĩ dòng Đền"},
  {"id": "lex.en.200k.059944", "hw": "communalisms", "pos": "noun", "ipa": "/kəˈmjuːnəlɪzəmz/", "vi": "chủ nghĩa chia rẽ cộng đồng"},
  {"id": "lex.en.200k.059945", "hw": "convulsions", "pos": "noun", "ipa": "/kənˈvʌlʃənz/", "vi": "cơn co giật cơ; sự xáo động dữ dội"},
  {"id": "lex.en.200k.059946", "hw": "crawlspaces", "pos": "noun", "ipa": "/ˈkrɔːlspeɪsɪz/", "vi": "khoang hẹp thông gió dưới nền nhà"},
  {"id": "lex.en.200k.059947", "hw": "cutches", "pos": "noun", "ipa": "/ˈkʌtʃɪz/", "vi": "chất chát tanin chiết từ cây keo"},
  {"id": "lex.en.200k.059948", "hw": "cutlets", "pos": "noun", "ipa": "/ˈkʌtləts/", "vi": "miếng thịt sườn bao bột chiên xù"},
  {"id": "lex.en.200k.059949", "hw": "deadbolts", "pos": "noun", "ipa": "/ˈdɛdboʊlts/", "vi": "chốt khóa cửa an toàn chống trộm"},
  {"id": "lex.en.200k.059950", "hw": "determinatives", "pos": "noun", "ipa": "/dɪˈtɜːrmɪnətɪvz/", "vi": "ký hiệu hạn định chữ tượng hình"},
  {"id": "lex.en.200k.059951", "hw": "determiners", "pos": "noun", "ipa": "/dɪˈtɜːrmɪnərz/", "vi": "từ chỉ định; từ hạn định ngữ pháp"},
  {"id": "lex.en.200k.059952", "hw": "doxorubicins", "pos": "noun", "ipa": "/ˌdɑːksəˈruːbɪsɪnz/", "vi": "thuốc kháng sinh chống ung thư"},
  {"id": "lex.en.200k.059953", "hw": "echinaceas", "pos": "noun", "ipa": "/ˌɛkɪˈneɪʃiəz/", "vi": "cây cúc tím thảo dược trị cảm"},
  {"id": "lex.en.200k.059954", "hw": "egyptologies", "pos": "noun", "ipa": "/ˌiːdʒɪpˈtɑːlədʒiz/", "vi": "ngành nghiên cứu Ai Cập cổ đại"},
  {"id": "lex.en.200k.059955", "hw": "elastins", "pos": "noun", "ipa": "/ɪˈlæstɪnz/", "vi": "loại protein sợi tạo độ đàn hồi"},
  {"id": "lex.en.200k.059956", "hw": "endometria", "pos": "noun", "ipa": "/ˌɛndoʊˈmiːtriə/", "vi": "lớp niêm mạc lót trong tử cung"},
  {"id": "lex.en.200k.059957", "hw": "fatsoes", "pos": "noun", "ipa": "/ˈfætsoʊz/", "vi": "kẻ béo phì ục ịch thô kệch"},
  {"id": "lex.en.200k.059958", "hw": "fatsos", "pos": "noun", "ipa": "/ˈfætsoʊz/", "vi": "người béo tròn; kẻ mập mạp"},
  {"id": "lex.en.200k.059959", "hw": "foisted", "pos": "verb", "ipa": "/ˈfɔɪstɪd/", "vi": "đã gán ghép; đã lén nhét xấu vào"},
  {"id": "lex.en.200k.059960", "hw": "foisting", "pos": "verb", "ipa": "/ˈfɔɪstɪŋ/", "vi": "đang gán ghép; lén tuồn hàng dỏm"},
  {"id": "lex.en.200k.059961", "hw": "foists", "pos": "verb", "ipa": "/ˈfɔɪsts/", "vi": "gán ghép ép buộc; lén nhét vào"},
  {"id": "lex.en.200k.059962", "hw": "gammier", "pos": "adj", "ipa": "/ˈɡæmiər/", "vi": "khập khiễng hơn; đau nhức hơn"},
  {"id": "lex.en.200k.059963", "hw": "gammiest", "pos": "adj", "ipa": "/ˈɡæmiɪst/", "vi": "khập khiễng nhất; tàn phế nhất"},
  {"id": "lex.en.200k.059964", "hw": "getas", "pos": "noun", "ipa": "/ˈɡɛtəz/", "vi": "đôi guốc gỗ truyền thống Nhật Bản"},
  {"id": "lex.en.200k.059965", "hw": "giardias", "pos": "noun", "ipa": "/dʒiˈɑːrdiəz/", "vi": "trùng roi ký sinh gây tiêu chảy"},
  {"id": "lex.en.200k.059966", "hw": "hammurabis", "pos": "noun", "ipa": "/ˌhæmʊˈrɑːbiz/", "vi": "vua ban hành bộ luật Hammurabi"},
  {"id": "lex.en.200k.059967", "hw": "harassers", "pos": "noun", "ipa": "/həˈræsərz/", "vi": "kẻ quấy rối; người gây phiền toái"},
  {"id": "lex.en.200k.059968", "hw": "hexanes", "pos": "noun", "ipa": "/ˈhɛkseɪnz/", "vi": "dung môi hydrocarbon hexan"},
  {"id": "lex.en.200k.059969", "hw": "homebodies", "pos": "noun", "ipa": "/ˈhoʊmbɑːdiz/", "vi": "người chỉ thích quẩn quanh ở nhà"},
  {"id": "lex.en.200k.059970", "hw": "hussars", "pos": "noun", "ipa": "/hʊˈzɑːrz/", "vi": "kỵ binh nhẹ hussar châu Âu"},
  {"id": "lex.en.200k.059971", "hw": "institutionalizes", "pos": "verb", "ipa": "/ˌɪnstɪˈtuːʃənəlaɪzɪz/", "vi": "thể chế hóa; đưa vào dưỡng lão"},
  {"id": "lex.en.200k.059972", "hw": "institutionalizing", "pos": "verb", "ipa": "/ˌɪnstɪˈtuːʃənəlaɪzɪŋ/", "vi": "đang thể chế hóa; đưa vào viện"},
  {"id": "lex.en.200k.059973", "hw": "jaggeries", "pos": "noun", "ipa": "/ˈdʒæɡəriz/", "vi": "đường thốt nốt; đường mía thô"},
  {"id": "lex.en.200k.059974", "hw": "kennellies", "pos": "noun", "ipa": "/ˈkɛnəliz/", "vi": "nhà vật lý điện Arthur Kennelly"},
  {"id": "lex.en.200k.059975", "hw": "laffers", "pos": "noun", "ipa": "/ˈlæfərz/", "vi": "nhà kinh tế học Arthur Laffer"},
  {"id": "lex.en.200k.059976", "hw": "lagans", "pos": "noun", "ipa": "/ˈlæɡənz/", "vi": "hàng hóa buộc phao chìm dưới biển"},
  {"id": "lex.en.200k.059977", "hw": "lermontovs", "pos": "noun", "ipa": "/ˈlɛərməntɔːvz/", "vi": "nhà thơ lãng mạn Mikhail Lermontov"},
  {"id": "lex.en.200k.059978", "hw": "masterstrokes", "pos": "noun", "ipa": "/ˈmæstərstroʊks/", "vi": "nước cờ tài tình; đòn xuất chúng"},
  {"id": "lex.en.200k.059979", "hw": "mesons", "pos": "noun", "ipa": "/ˈmiːzɑːnz/", "vi": "hạt trung hòa meson vật lý"},
  {"id": "lex.en.200k.059980", "hw": "metacarpals", "pos": "noun", "ipa": "/ˌmɛtəˈkɑːrpəlz/", "vi": "các xương đốt bàn tay ở người"},
  {"id": "lex.en.200k.059981", "hw": "mexicalis", "pos": "noun", "ipa": "/ˌmɛksɪˈkæliz/", "vi": "thành phố biên giới Mexicali"},
  {"id": "lex.en.200k.059982", "hw": "mirabilises", "pos": "noun", "ipa": "/mɪˈræbəlɪsɪz/", "vi": "cây hoa phấn bông bốn giờ chiều"},
  {"id": "lex.en.200k.059983", "hw": "mommsens", "pos": "noun", "ipa": "/ˈmɑːmsənz/", "vi": "sử gia Nobel Theodor Mommsen"},
  {"id": "lex.en.200k.059984", "hw": "mycenaes", "pos": "noun", "ipa": "/maɪˈsiːniːz/", "vi": "thành bang Mycenae Hy Lạp cổ đại"},
  {"id": "lex.en.200k.059985", "hw": "mycoplasmas", "pos": "noun", "ipa": "/ˌmaɪkoʊˈplæzməz/", "vi": "vi khuẩn mycoplasma gây viêm phổi"},
  {"id": "lex.en.200k.059986", "hw": "nefertitis", "pos": "noun", "ipa": "/ˌnɛfərˈtiːtiz/", "vi": "hoàng hậu Nefertiti của Ai Cập"},
  {"id": "lex.en.200k.059987", "hw": "neoplasias", "pos": "noun", "ipa": "/ˌniːoʊˈpleɪʒiəz/", "vi": "sự tăng sinh khối u bất thường"},
  {"id": "lex.en.200k.059988", "hw": "neurofibromatoses", "pos": "noun", "ipa": "/ˌnjʊəroʊfaɪbroʊməˈtoʊsiːz/", "vi": "bệnh u sợi thần kinh di truyền"},
  {"id": "lex.en.200k.059989", "hw": "nitwits", "pos": "noun", "ipa": "/ˈnɪtwɪts/", "vi": "kẻ ngu xuẩn; đồ ngốc nghếch"},
  {"id": "lex.en.200k.059990", "hw": "oilseeds", "pos": "noun", "ipa": "/ˈɔɪlsiːdz/", "vi": "hạt lấy dầu; cây hạt có dầu"},
  {"id": "lex.en.200k.059991", "hw": "parenchymas", "pos": "noun", "ipa": "/pəˈrɛŋkɪməz/", "vi": "nhu mô cơ quan; mô mềm thực vật"},
  {"id": "lex.en.200k.059992", "hw": "perplexities", "pos": "noun", "ipa": "/pərˈplɛksətiz/", "vi": "sự bối rối; điều rắc rối phức tạp"},
  {"id": "lex.en.200k.059993", "hw": "photocopiers", "pos": "noun", "ipa": "/ˈfoʊtoʊkɑːpiərz/", "vi": "máy sao chụp tài liệu photocopy"},
  {"id": "lex.en.200k.059994", "hw": "polioviruses", "pos": "noun", "ipa": "/ˈpoʊlioʊvaɪrəsɪz/", "vi": "vi-rút gây bệnh sốt bại liệt"},
  {"id": "lex.en.200k.059995", "hw": "polyamides", "pos": "noun", "ipa": "/ˌpɑːliˈæmaɪdz/", "vi": "sợi nhựa tổng hợp polyamit"},
  {"id": "lex.en.200k.059996", "hw": "portended", "pos": "verb", "ipa": "/pɔːrˈtɛndɪd/", "vi": "đã báo trước điềm gở; đã cảnh báo"},
  {"id": "lex.en.200k.059997", "hw": "portending", "pos": "verb", "ipa": "/pɔːrˈtɛndɪŋ/", "vi": "đang báo trước điềm; cảnh báo"},
  {"id": "lex.en.200k.059998", "hw": "portends", "pos": "verb", "ipa": "/pɔːrˈtɛndz/", "vi": "báo trước điềm xấu; tiên triệu"},
  {"id": "lex.en.200k.059999", "hw": "pralines", "pos": "noun", "ipa": "/ˈpreɪliːnz/", "vi": "kẹo hạnh nhân caramen praline"},
  {"id": "lex.en.200k.060000", "hw": "prematurities", "pos": "noun", "ipa": "/ˌpriːməˈtjʊərətiz/", "vi": "sự sinh non; sự vội vã non yểu"},
  {"id": "lex.en.200k.060001", "hw": "proconsuls", "pos": "noun", "ipa": "/proʊˈkɑːnsəlz/", "vi": "quan tổng trấn thuộc địa La Mã"},
  {"id": "lex.en.200k.060002", "hw": "proofreaders", "pos": "noun", "ipa": "/ˈpruːfriːdərz/", "vi": "người duyệt sửa bản in xuất bản"}
]

with open('scratch/b32_r10_raw_p5.json') as f:
    raw = json.load(f)

assert len(items) == 100
assert len(raw) == 100

for i, (item, r) in enumerate(zip(items, raw)):
    assert item['id'] == r['id'], f"Mismatch id at {i}: {item['id']} vs {r['id']}"
    assert item['hw'] == r['hw'], f"Mismatch hw at {i}: {item['hw']} vs {r['hw']}"
    assert len(item['vi']) <= 35, f"vi length > 35 at {i} ({item['hw']}): {len(item['vi'])}"
    assert item['pos'] in ['noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'], f"Invalid pos at {i}: {item['pos']}"
    if ' ' not in item['hw']:
        assert item['ipa'].startswith('/') and item['ipa'].endswith('/') and item['ipa'].count('/') == 2, f"Invalid ipa at {i}: {item['ipa']}"
    r['pos'] = item['pos']
    r['ipa'] = item['ipa']
    r['vi'] = item['vi']
    r['status'] = 'reviewed'

with open('scratch/b32_r10_p5.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

print("Part 5 validated and written successfully.")
