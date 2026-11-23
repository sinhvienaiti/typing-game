import json

items = [
  {"id": "lex.en.200k.062003", "hw": "otic ganglion", "pos": "phrase", "ipa": "/ˈoʊtɪk ˈɡæŋɡliən/", "vi": "hạch thần kinh tai phó giao cảm"},
  {"id": "lex.en.200k.062004", "hw": "parol evidence rule", "pos": "phrase", "ipa": "/pəˈroʊl ˈɛvɪdəns ruːl/", "vi": "quy tắc cấm chứng cứ miệng ngoài"},
  {"id": "lex.en.200k.062005", "hw": "pennyroyal oil", "pos": "phrase", "ipa": "/ˈpɛnirɔɪəl ɔɪl/", "vi": "tinh dầu bạc hà hăng đuổi muỗi"},
  {"id": "lex.en.200k.062006", "hw": "pomelo tree", "pos": "phrase", "ipa": "/ˈpɑːməloʊ triː/", "vi": "cây bưởi ăn quả thuộc họ Cam chanh"},
  {"id": "lex.en.200k.062007", "hw": "potato peelings", "pos": "phrase", "ipa": "/pəˈteɪtoʊ ˈpiːlɪŋz/", "vi": "vỏ củ khoai tây gọt bỏ đi"},
  {"id": "lex.en.200k.062008", "hw": "pterygoid plexus", "pos": "phrase", "ipa": "/ˈtɛrɪɡɔɪd ˈplɛksəs/", "vi": "đám rối tĩnh mạch chân bướm hàm"},
  {"id": "lex.en.200k.062009", "hw": "purple orchis", "pos": "phrase", "ipa": "/ˈpɜːrpl ˈɔːrkɪs/", "vi": "cây hoa phong lan đất sắc tím"},
  {"id": "lex.en.200k.062010", "hw": "ranunculus occidentalis", "pos": "phrase", "ipa": "/rəˈnʌŋkjʊləs ˌɑːksɪdɛnˈteɪlɪs/", "vi": "cây mao lương hoa vàng miền tây Mỹ"},
  {"id": "lex.en.200k.062011", "hw": "rectus lateralis", "pos": "phrase", "ipa": "/ˈrɛktəs ˌlætəˈreɪlɪs/", "vi": "cơ thẳng ngoài xoay nhãn cầu mắt"},
  {"id": "lex.en.200k.062012", "hw": "ribonucleic acid", "pos": "phrase", "ipa": "/ˌraɪboʊnjuːˈkliːɪk ˈæsɪd/", "vi": "axit ribonucleic ARN vật chất gen"},
  {"id": "lex.en.200k.062013", "hw": "senecio vulgaris", "pos": "phrase", "ipa": "/sɪˈniːʃioʊ vʌlˈɡɛərɪs/", "vi": "cây cỏ cúc bạc dại hoa vàng nhỏ"},
  {"id": "lex.en.200k.062014", "hw": "sorbent material", "pos": "phrase", "ipa": "/ˈsɔːrbənt məˈtɪriəl/", "vi": "vật liệu thấm hút; chất hấp phụ"},
  {"id": "lex.en.200k.062015", "hw": "spurge nettle", "pos": "phrase", "ipa": "/spɜːrdʒ ˈnɛtl/", "vi": "cây tầm ma gai ngứa rát châu Mỹ"},
  {"id": "lex.en.200k.062016", "hw": "superficial epigastric vein", "pos": "phrase", "ipa": "/ˌsuːpərˈfɪʃl ˌɛpɪˈɡæstrɪk veɪn/", "vi": "tĩnh mạch thượng vị nông dưới da"},
  {"id": "lex.en.200k.062017", "hw": "superior epigastric veins", "pos": "phrase", "ipa": "/suːˈpɪriər ˌɛpɪˈɡæstrɪk veɪnz/", "vi": "tĩnh mạch thượng vị trên ổ bụng"},
  {"id": "lex.en.200k.062018", "hw": "true glottis", "pos": "phrase", "ipa": "/truː ˈɡlɑːtɪs/", "vi": "khe thanh môn thật giữa hai dây âm"},
  {"id": "lex.en.200k.062019", "hw": "tub gurnard", "pos": "phrase", "ipa": "/tʌb ˈɡɜːrnərd/", "vi": "cá chào mào biển vây ngực xanh óng"},
  {"id": "lex.en.200k.062020", "hw": "valproic acid", "pos": "phrase", "ipa": "/vælˈproʊɪk ˈæsɪd/", "vi": "axit valproic thuốc trị động kinh"},
  {"id": "lex.en.200k.062021", "hw": "vervain family", "pos": "phrase", "ipa": "/ˈvɜːrveɪn ˈfæməli/", "vi": "họ thực vật Cỏ roi ngựa Mã tiên"},
  {"id": "lex.en.200k.062022", "hw": "vervain sage", "pos": "phrase", "ipa": "/ˈvɜːrveɪn seɪdʒ/", "vi": "cây xô thơm hoa tím dại châu Âu"},
  {"id": "lex.en.200k.062023", "hw": "volute spring", "pos": "phrase", "ipa": "/vəˈluːt sprɪŋ/", "vi": "lò xo lá cuộn hình nón xoắn ốc"},
  {"id": "lex.en.200k.062024", "hw": "vulpes vulpes", "pos": "phrase", "ipa": "/ˈvʌlpiz ˈvʌlpiz/", "vi": "loài cáo đỏ Bắc bán cầu thông minh"},
  {"id": "lex.en.200k.062025", "hw": "wassily kandinsky", "pos": "phrase", "ipa": "/ˈvɑːsɪli kænˈdɪnski/", "vi": "họa sĩ tiên phong Wassily Kandinsky"},
  {"id": "lex.en.200k.062026", "hw": "water chickweed", "pos": "phrase", "ipa": "/ˈwɔːtər ˈtʃɪkwiːd/", "vi": "cỏ tinh thảo nước mọc ven bờ suối"},
  {"id": "lex.en.200k.062027", "hw": "will keith kellog", "pos": "phrase", "ipa": "/wɪl kiːθ ˈkɛlɑːɡ/", "vi": "nhà sáng lập ngũ cốc Will Kellogg"},
  {"id": "lex.en.200k.062028", "hw": "winter aconite", "pos": "phrase", "ipa": "/ˈwɪntər ˈækənaɪt/", "vi": "cây hoa ô đầu vàng nở cuối đông"},
  {"id": "lex.en.200k.062029", "hw": "yellow gurnard", "pos": "phrase", "ipa": "/ˈjɛloʊ ˈɡɜːrnərd/", "vi": "cá chào mào biển ánh vàng châu Âu"},
  {"id": "lex.en.200k.062030", "hw": "abruzzis", "pos": "noun", "ipa": "/əˈbruːtsiz/", "vi": "vùng núi Abruzzi miền trung nước Ý"},
  {"id": "lex.en.200k.062031", "hw": "amyls", "pos": "noun", "ipa": "/ˈæmɪlz/", "vi": "nhóm gốc hữu cơ hóa học amyl C5H11"},
  {"id": "lex.en.200k.062032", "hw": "aragonites", "pos": "noun", "ipa": "/ˈærəɡənaɪts/", "vi": "khoáng vật tinh thể đá aragonit"},
  {"id": "lex.en.200k.062033", "hw": "avestas", "pos": "noun", "ipa": "/əˈvɛstəz/", "vi": "bộ kinh thánh cổ Avesta Hỏa giáo"},
  {"id": "lex.en.200k.062034", "hw": "azithromycins", "pos": "noun", "ipa": "/əˌzɪθrəˈmaɪsɪnz/", "vi": "kháng sinh nhóm macrolide phổ rộng"},
  {"id": "lex.en.200k.062035", "hw": "belisariuses", "pos": "noun", "ipa": "/ˌbɛlɪˈsɛriəsɪz/", "vi": "danh tướng Đông La Mã Belisarius"},
  {"id": "lex.en.200k.062036", "hw": "biggins", "pos": "noun", "ipa": "/ˈbɪɡɪnz/", "vi": "mũ trùm trẻ em; ấm pha cà phê nhỏ"},
  {"id": "lex.en.200k.062037", "hw": "blackguards", "pos": "noun", "ipa": "/ˈblæɡərdz/", "vi": "kẻ vô lại đê tiện; gã khốn nạn"},
  {"id": "lex.en.200k.062038", "hw": "blushers", "pos": "noun", "ipa": "/ˈblʌʃərz/", "vi": "nấm đỏ blusher; người dễ đỏ mặt"},
  {"id": "lex.en.200k.062039", "hw": "bonheurs", "pos": "noun", "ipa": "/bɔːnˈhɜːrz/", "vi": "niềm hạnh phúc; họa sĩ Rosa Bonheur"},
  {"id": "lex.en.200k.062040", "hw": "bookbinders", "pos": "noun", "ipa": "/ˈbʊkbaɪndərz/", "vi": "người thợ đóng gáy sách thủ công"},
  {"id": "lex.en.200k.062041", "hw": "bubers", "pos": "noun", "ipa": "/ˈbuːbərz/", "vi": "triết gia tôn giáo Martin Buber"},
  {"id": "lex.en.200k.062042", "hw": "bunters", "pos": "noun", "ipa": "/ˈbʌntərz/", "vi": "cầu thủ đẩy bóng ngắn bóng chày"},
  {"id": "lex.en.200k.062043", "hw": "busboys", "pos": "noun", "ipa": "/ˈbʌsbɔɪz/", "vi": "nhân viên phụ bàn dọn dẹp nhà hàng"},
  {"id": "lex.en.200k.062044", "hw": "caducei", "pos": "noun", "ipa": "/kəˈduːsiːaɪ/", "vi": "quyền trượng hai rắn thần Hermes"},
  {"id": "lex.en.200k.062045", "hw": "capstans", "pos": "noun", "ipa": "/ˈkæpstənz/", "vi": "tời đứng cuộn dây neo; trục cuốn"},
  {"id": "lex.en.200k.062046", "hw": "censers", "pos": "noun", "ipa": "/ˈsɛnsərz/", "vi": "lư xông trầm hương nghi lễ tôn giáo"},
  {"id": "lex.en.200k.062047", "hw": "cesspits", "pos": "noun", "ipa": "/ˈsɛspɪts/", "vi": "hố chứa chất thải; nơi ô uế tệ nạn"},
  {"id": "lex.en.200k.062048", "hw": "coagulants", "pos": "noun", "ipa": "/koʊˈæɡjələnts/", "vi": "chất gây đông tụ keo tụ chất lỏng"},
  {"id": "lex.en.200k.062049", "hw": "consumptives", "pos": "noun", "ipa": "/kənˈsʌmptɪvz/", "vi": "người mắc bệnh lao phổi ho ra máu"},
  {"id": "lex.en.200k.062050", "hw": "conveyers", "pos": "noun", "ipa": "/kənˈveɪərz/", "vi": "băng chuyền hàng; người truyền đạt"},
  {"id": "lex.en.200k.062051", "hw": "crackerjacks", "pos": "noun", "ipa": "/ˈkrækərdʒæks/", "vi": "tay cừ khôi xuất sắc; bắp rang bơ"},
  {"id": "lex.en.200k.062052", "hw": "criminalisations", "pos": "noun", "ipa": "/ˌkrɪmɪnəlaɪˈzeɪʃənz/", "vi": "sự hình sự hóa hành vi vi phạm"},
  {"id": "lex.en.200k.062053", "hw": "deciles", "pos": "noun", "ipa": "/ˈdɛsaɪlz/", "vi": "giá trị thập phân vị trong thống kê"},
  {"id": "lex.en.200k.062054", "hw": "demogorgons", "pos": "noun", "ipa": "/ˌdiːməˈɡɔːrɡənz/", "vi": "ác thần âm phủ kinh dị Demogorgon"},
  {"id": "lex.en.200k.062055", "hw": "devourers", "pos": "noun", "ipa": "/dɪˈvaʊərərz/", "vi": "kẻ ngấu nghiến; người đọc ngốn sách"},
  {"id": "lex.en.200k.062056", "hw": "diskettes", "pos": "noun", "ipa": "/dɪˈskɛts/", "vi": "đĩa mềm lưu dữ liệu máy tính cũ"},
  {"id": "lex.en.200k.062057", "hw": "doctorows", "pos": "noun", "ipa": "/ˈdɑːktəroʊz/", "vi": "nhà văn lịch sử Mỹ E. L. Doctorow"},
  {"id": "lex.en.200k.062058", "hw": "doorframes", "pos": "noun", "ipa": "/ˈdɔːrfreɪmz/", "vi": "khung bao cố định cánh cửa ra vào"},
  {"id": "lex.en.200k.062059", "hw": "doublers", "pos": "noun", "ipa": "/ˈdʌblərz/", "vi": "mạch nhân đôi điện áp; thợ bện đôi"},
  {"id": "lex.en.200k.062060", "hw": "dredgers", "pos": "noun", "ipa": "/ˈdrɛdʒərz/", "vi": "tàu hút nạo vét lòng sông; hộp rắc"},
  {"id": "lex.en.200k.062061", "hw": "egyptologists", "pos": "noun", "ipa": "/ˌiːdʒɪpˈtɑːlədʒɪsts/", "vi": "nhà Ai Cập học chuyên văn minh cổ"},
  {"id": "lex.en.200k.062062", "hw": "endives", "pos": "noun", "ipa": "/ˈɛndaɪvz/", "vi": "cây rau diếp xoăn đắng làm xà lách"},
  {"id": "lex.en.200k.062063", "hw": "entranceways", "pos": "noun", "ipa": "/ˈɛntrənsweɪz/", "vi": "lối hành lang cổng bước vào tòa nhà"},
  {"id": "lex.en.200k.062064", "hw": "fluoresceins", "pos": "noun", "ipa": "/ˌflʊərˈɛsiːnz/", "vi": "thuốc nhuộm phát quang fluorescein"},
  {"id": "lex.en.200k.062065", "hw": "friulis", "pos": "noun", "ipa": "/friˈuːliz/", "vi": "vùng đất và tiếng Friuli ở nước Ý"},
  {"id": "lex.en.200k.062066", "hw": "galeae", "pos": "noun", "ipa": "/ˈɡeɪliːiː/", "vi": "mũ sắt La Mã; cấu trúc hình mũ"},
  {"id": "lex.en.200k.062067", "hw": "galeas", "pos": "noun", "ipa": "/ˈɡeɪliəz/", "vi": "các mũ trụ giáp đầu lính La Mã cổ"},
  {"id": "lex.en.200k.062068", "hw": "gamelans", "pos": "noun", "ipa": "/ˈɡæməlænz/", "vi": "dàn nhạc gõ dân gian gamelan Indo"},
  {"id": "lex.en.200k.062069", "hw": "garands", "pos": "noun", "ipa": "/ɡəˈrændz/", "vi": "súng trường bán tự động M1 Garand"},
  {"id": "lex.en.200k.062070", "hw": "gargantuas", "pos": "noun", "ipa": "/ɡɑːrˈɡæntʃuəz/", "vi": "người khổng lồ phàm ăn Gargantua"},
  {"id": "lex.en.200k.062071", "hw": "gentamicins", "pos": "noun", "ipa": "/ˌdʒɛntəˈmaɪsɪnz/", "vi": "thuốc kháng sinh mạnh gentamicin"},
  {"id": "lex.en.200k.062072", "hw": "gerunds", "pos": "noun", "ipa": "/ˈdʒɛrəndz/", "vi": "danh động từ (V-ing) trong ngữ pháp"},
  {"id": "lex.en.200k.062073", "hw": "ghrelins", "pos": "noun", "ipa": "/ˈɡrɛlɪnz/", "vi": "hoóc-môn kích thích cảm giác đói"},
  {"id": "lex.en.200k.062074", "hw": "gypped", "pos": "verb", "ipa": "/dʒɪpt/", "vi": "đã lừa bịp tiền; đã quỵt lừa gạt"},
  {"id": "lex.en.200k.062075", "hw": "gypping", "pos": "verb", "ipa": "/ˈdʒɪpɪŋ/", "vi": "đang lừa gạt tiền bạc; gian lận"},
  {"id": "lex.en.200k.062076", "hw": "habakkuks", "pos": "noun", "ipa": "/həˈbækəks/", "vi": "tiên tri Ha-ba-cúc trong Cựu Ước"},
  {"id": "lex.en.200k.062077", "hw": "hyperbolas", "pos": "noun", "ipa": "/haɪˈpɜːrbələz/", "vi": "đường cong hai nhánh hypecbol toán"},
  {"id": "lex.en.200k.062078", "hw": "iowans", "pos": "noun", "ipa": "/ˈaɪəwənz/", "vi": "cư dân sống tại tiểu bang Iowa Mỹ"},
  {"id": "lex.en.200k.062079", "hw": "klansmans", "pos": "noun", "ipa": "/ˈklænzmənz/", "vi": "thành viên tổ chức Ku Klux Klan"},
  {"id": "lex.en.200k.062080", "hw": "lambskins", "pos": "noun", "ipa": "/ˈlæmskɪnz/", "vi": "tấm da lông cừu non mềm mại thuộc"},
  {"id": "lex.en.200k.062081", "hw": "lethes", "pos": "noun", "ipa": "/ˈliːθiz/", "vi": "con sông lãng quên Lethe cõi âm ti"},
  {"id": "lex.en.200k.062082", "hw": "looters", "pos": "noun", "ipa": "/ˈluːtərz/", "vi": "kẻ hôi của cướp phá lúc hỗn loạn"},
  {"id": "lex.en.200k.062083", "hw": "lories", "pos": "noun", "ipa": "/ˈlɔːriz/", "vi": "loài chim vẹt mật lory sặc sỡ"},
  {"id": "lex.en.200k.062084", "hw": "luculluses", "pos": "noun", "ipa": "/luːˈkʌləsɪz/", "vi": "tướng La Mã sành ăn xa hoa Lucullus"},
  {"id": "lex.en.200k.062085", "hw": "madwomen", "pos": "noun", "ipa": "/ˈmædwɪmɪn/", "vi": "người phụ nữ điên loạn mất trí"},
  {"id": "lex.en.200k.062086", "hw": "massenets", "pos": "noun", "ipa": "/ˌmæsəˈneɪz/", "vi": "nhà soạn nhạc opera Jules Massenet"},
  {"id": "lex.en.200k.062087", "hw": "merovingians", "pos": "noun", "ipa": "/ˌmɛrəˈvɪndʒiənz/", "vi": "vương triều cổ Meroving nước Pháp"},
  {"id": "lex.en.200k.062088", "hw": "mindoros", "pos": "noun", "ipa": "/mɪnˈdɔːroʊz/", "vi": "hòn đảo lớn Mindoro ở Philippines"},
  {"id": "lex.en.200k.062089", "hw": "mithridateses", "pos": "noun", "ipa": "/ˌmɪθrɪˈdeɪtiːzɪz/", "vi": "quốc vương Pontus cổ Mithridates"},
  {"id": "lex.en.200k.062090", "hw": "modellers", "pos": "noun", "ipa": "/ˈmɑːdlərz/", "vi": "người làm mô hình nặn tượng mẫu"},
  {"id": "lex.en.200k.062091", "hw": "molehills", "pos": "noun", "ipa": "/ˈmoʊlhɪlz/", "vi": "đụn đất nhỏ do chuột chũi đùn lên"},
  {"id": "lex.en.200k.062092", "hw": "mucins", "pos": "noun", "ipa": "/ˈmjuːsɪnz/", "vi": "chất nhầy protein bảo vệ niêm mạc"},
  {"id": "lex.en.200k.062093", "hw": "necropsies", "pos": "noun", "ipa": "/ˈnɛkrɑːpsiz/", "vi": "cuộc mổ khám nghiệm tử thi xác thú"},
  {"id": "lex.en.200k.062094", "hw": "nesters", "pos": "noun", "ipa": "/ˈnɛstərz/", "vi": "loài chim làm tổ; người di dân mới"},
  {"id": "lex.en.200k.062095", "hw": "nursemaids", "pos": "noun", "ipa": "/ˈnɜːrsmeɪdz/", "vi": "cô bảo mẫu giữ trẻ; cô vú nuôi trẻ"},
  {"id": "lex.en.200k.062096", "hw": "overpressures", "pos": "noun", "ipa": "/ˌoʊvərˈprɛʃərz/", "vi": "áp suất vượt ngưỡng; sóng xung kích"},
  {"id": "lex.en.200k.062097", "hw": "pkus", "pos": "noun", "ipa": "/piː keɪ juːz/", "vi": "bệnh phenylketon niệu PKU bẩm sinh"},
  {"id": "lex.en.200k.062098", "hw": "plotinuses", "pos": "noun", "ipa": "/ploʊˈtaɪnəsɪz/", "vi": "triết gia Tân Platon Plotinus"},
  {"id": "lex.en.200k.062099", "hw": "potentiations", "pos": "noun", "ipa": "/pəˌtɛnʃiˈeɪʃənz/", "vi": "sự tăng cường hiệu lực cộng hưởng"},
  {"id": "lex.en.200k.062100", "hw": "primulas", "pos": "noun", "ipa": "/ˈprɪmjʊləz/", "vi": "cây hoa anh thảo sắc màu sặc sỡ"},
  {"id": "lex.en.200k.062101", "hw": "proposers", "pos": "noun", "ipa": "/prəˈpoʊzərz/", "vi": "người đề xuất; người ngỏ lời cưới"},
  {"id": "lex.en.200k.062102", "hw": "proteinurias", "pos": "noun", "ipa": "/ˌproʊtiːˈnjʊəriəz/", "vi": "tình trạng đạm protein niệu thận"}
]

with open('scratch/b33_r05_raw_p1.json') as f:
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

with open('scratch/b33_r05_p1.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

print("Batch 33 Round 5 Part 1 validated and written successfully.")
