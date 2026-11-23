import json

items = [
    ("065903", "frederick childe hassam", "phrase", "/ˈfrɛdrɪk tʃaɪld ˈhæsəm/", "họa sĩ Mỹ Frederick Childe Hassam"),
    ("065904", "genus achillea", "phrase", "/ˈdʒiːnəs ˌækɪˈliːə/", "chi cây cúc vạn diệp Achillea"),
    ("065905", "genus agrostis", "phrase", "/ˈdʒiːnəs əˈɡrɒstɪs/", "chi cỏ mật; chi cỏ bông Agrostis"),
    ("065906", "genus aranea", "phrase", "/ˈdʒiːnəs əˈreɪniə/", "chi nhện chăng tơ Aranea"),
    ("065907", "genus artemia", "phrase", "/ˈdʒiːnəs ɑːrˈtiːmiə/", "chi giáp xác nước mặn Artemia"),
    ("065908", "genus atriplex", "phrase", "/ˈdʒiːnəs ˈætrɪplɛks/", "chi rau muối Atriplex"),
    ("065909", "genus carlina", "phrase", "/ˈdʒiːnəs kɑːrˈliːnə/", "chi cúc gai Carlina Địa Trung Hải"),
    ("065910", "genus crotalus", "phrase", "/ˈdʒiːnəs ˈkrɒtələs/", "chi rắn đuôi chuông Crotalus"),
    ("065911", "genus cucurbita", "phrase", "/ˈdʒiːnəs kjuːˈkɜːrbɪtə/", "chi bầu bí Cucurbita"),
    ("065912", "genus euryale", "phrase", "/ˈdʒiːnəs jʊˈraɪəli/", "chi khiếm thực; chi sao biển giỏ"),
    ("065913", "genus laurus", "phrase", "/ˈdʒiːnəs ˈlɔːrəs/", "chi cây nguyệt quế Laurus"),
    ("065914", "genus leptospira", "phrase", "/ˈdʒiːnəs ˌlɛptəˈspaɪrə/", "chi xoắn khuẩn Leptospira"),
    ("065915", "genus nymphaea", "phrase", "/ˈdʒiːnəs nɪmˈfiːə/", "chi hoa súng Nymphaea"),
    ("065916", "genus pothos", "phrase", "/ˈdʒiːnəs ˈpoʊθɒs/", "chi cây trầu bà Pothos"),
    ("065917", "genus pseudotsuga", "phrase", "/ˈdʒiːnəs ˌsuːdoʊˈtsuːɡə/", "chi cây linh sam Douglas"),
    ("065918", "genus sambucus", "phrase", "/ˈdʒiːnəs sæmˈbjuːkəs/", "chi cây cơm cháy Sambucus"),
    ("065919", "genus sciurus", "phrase", "/ˈdʒiːnəs saɪˈjʊərəs/", "chi sóc cây Sciurus"),
    ("065920", "genus sorbus", "phrase", "/ˈdʒiːnəs ˈsɔːrbəs/", "chi cây thanh lương trà Sorbus"),
    ("065921", "genus spodoptera", "phrase", "/ˈdʒiːnəs spoʊˈdɒptərə/", "chi bướm sâu keo Spodoptera"),
    ("065922", "golden pothos", "phrase", "/ˈɡoʊldən ˈpoʊθɒs/", "cây trầu bà lá vàng leo"),
    ("065923", "hawser bend", "phrase", "/ˈhɔːzər bɛnd/", "nút thắt nối hai dây thừng lớn"),
    ("065924", "homecourt advantage", "phrase", "/ˈhoʊmkɔːrt ədˈvæntɪdʒ/", "lợi thế thi đấu trên sân nhà"),
    ("065925", "impatiens capensis", "phrase", "/ɪmˈpeɪʃiɛnz kəˈpɛnsɪs/", "cây bóng nước hoa cam Bắc Mỹ"),
    ("065926", "iraqi mukhabarat", "phrase", "/ɪˈrɑːki muːˈkɑːbərɑːt/", "cơ quan tình báo Mukhabarat Iraq"),
    ("065927", "jarvik artificial heart", "phrase", "/ˈdʒɑːrvɪk ˌɑːrtɪˈfɪʃəl hɑːrt/", "tim nhân tạo cấy ghép Jarvik"),
    ("065928", "jarvik heart", "phrase", "/ˈdʒɑːrvɪk hɑːrt/", "thiết bị tim nhân tạo Jarvik"),
    ("065929", "karl linne", "phrase", "/kɑːrl lɪˈneɪ/", "nhà sinh vật học Carl Linnaeus"),
    ("065930", "lateral epicondyle", "phrase", "/ˈlætərəl ˌɛpɪˈkɒndaɪl/", "mỏm trên lồi cầu ngoài xương"),
    ("065931", "lichen ruber planus", "phrase", "/ˈlaɪkən ˈruːbər ˈpleɪnəs/", "bệnh liken phẳng ở da niêm mạc"),
    ("065932", "litchi chinensis", "phrase", "/ˈlaɪtʃi tʃaɪˈnɛnsɪs/", "cây vải thiều ăn quả"),
    ("065933", "lonicera canadensis", "phrase", "/ləˈnɪsərə ˌkænəˈdɛnsɪs/", "cây kim ngân hoa Canada"),
    ("065934", "lonicera japonica", "phrase", "/ləˈnɪsərə dʒəˈpɒnɪkə/", "cây kim ngân hoa Nhật Bản"),
    ("065935", "louis stanton auchincloss", "phrase", "/ˈluːɪs ˈstæntən ˈɔːkɪnklɒs/", "nhà văn Louis Stanton Auchincloss"),
    ("065936", "mentha aquatica", "phrase", "/ˈmɛnθə əˈkwætɪkə/", "cây bạc hà mọc nước"),
    ("065937", "modest petrovich mussorgsky", "phrase", "/ˈmɒdɪst pəˈtroʊvɪtʃ mʊˈsɔːrɡski/", "nhà soạn nhạc Nga Mussorgsky"),
    ("065938", "musculus trapezius", "phrase", "/ˈmʌskjələs trəˈpiːziəs/", "cơ thang ở vùng cổ vai lưng"),
    ("065939", "nicotiana rustica", "phrase", "/nɪˌkoʊʃiˈeɪnə ˈrʌstɪkə/", "cây thuốc lào lá đậm nicôtin"),
    ("065940", "nymphaea lotus", "phrase", "/nɪmˈfiːə ˈloʊtəs/", "hoa súng trắng sông Nile Ai Cập"),
    ("065941", "oyster agaric", "phrase", "/ˈɔɪstər ˈæɡərɪk/", "nấm sò; nấm bào ngư ăn được"),
    ("065942", "petty whin", "phrase", "/ˈpɛti wɪn/", "cây kim tước gai nhỏ châu Âu"),
    ("065943", "rana pipiens", "phrase", "/ˈrɑːnə ˈpɪpiənz/", "ếch da báo đồng cỏ Bắc Mỹ"),
    ("065944", "ribes nigrum", "phrase", "/ˈraɪbiːz ˈnaɪɡrəm/", "cây lý chua đen giàu vitamin"),
    ("065945", "royal agaric", "phrase", "/ˈrɔɪəl ˈæɡərɪk/", "nấm hoàng đế Amanita ăn được"),
    ("065946", "salmonella typhi", "phrase", "/ˌsælməˈnɛlə ˈtaɪfi/", "vi khuẩn gây bệnh thương hàn"),
    ("065947", "schizotypal personality", "phrase", "/ˌskɪtsəˈtaɪpəl ˌpɜːrsəˈnælɪti/", "rối loạn nhân cách dạng phân liệt"),
    ("065948", "siris tree", "phrase", "/ˈsɪrɪs triː/", "cây bồ kết tây; cây hợp hoan gỗ"),
    ("065949", "spectrographic analysis", "phrase", "/ˌspɛktrəˈɡræfɪk əˈnælɪsɪs/", "phép phân tích quang phổ học"),
    ("065950", "thuja occidentalis", "phrase", "/ˈθjuːdʒə ˌɒksɪdɛnˈteɪlɪs/", "cây trắc bách diệp phương Đông"),
    ("065951", "trematode worm", "phrase", "/ˈtrɛməˌtoʊd wɜːrm/", "giun sán lá ký sinh"),
    ("065952", "vin ordinaire", "phrase", "/væn ɔːrdiˈnɛər/", "rượu vang bình dân uống hàng ngày"),
    ("065953", "zeno of elea", "phrase", "/ˈziːnoʊ əv ˈɛliə/", "triết gia Hy Lạp Zeno xứ Elea"),
    ("065954", "abjurations", "noun", "/ˌæbdʒʊˈreɪʃənz/", "sự tuyên thệ từ bỏ đức tin"),
    ("065955", "accordionists", "noun", "/əˈkɔːrdiənɪsts/", "nghệ sĩ chơi đàn phong cầm"),
    ("065956", "alewives", "noun", "/ˈeɪlˌwaɪvz/", "cá trích sông Bắc Mỹ alewife"),
    ("065957", "alnuses", "noun", "/ˈælnəsɪz/", "cây tống quán sủ thuộc chi Alnus"),
    ("065958", "altaics", "noun", "/ælˈteɪɪks/", "ngữ hệ Altai; dân tộc vùng Altai"),
    ("065959", "antipastos", "noun", "/ˌæntiˈpæstoʊz/", "món khai vị nguội kiểu Ý"),
    ("065960", "arachnoids", "noun", "/əˈræknɔɪdz/", "màng nhện bao bọc não tủy"),
    ("065961", "avenas", "noun", "/əˈviːnəz/", "cây yến mạch thuộc chi Avena"),
    ("065962", "beerbohms", "noun", "/ˈbɪərˌboʊmz/", "họa sĩ biếm họa Max Beerbohm"),
    ("065963", "behaviourists", "noun", "/bɪˈheɪvjərɪsts/", "nhà tâm lý học hành vi"),
    ("065964", "bercies", "noun", "/bɛərˈsiz/", "nước xốt rượu vang trắng Bercy"),
    ("065965", "biltongs", "noun", "/ˈbɪlˌtɒŋz/", "thịt bò phơi khô tẩm gia vị Nam Phi"),
    ("065966", "bloodsuckers", "noun", "/ˈblʌdˌsʌkərz/", "con đỉa hút máu; kẻ bóc lột"),
    ("065967", "bluenoses", "noun", "/ˈbluːˌnoʊzɪz/", "người bảo thủ khắt khe; dân Nova"),
    ("065968", "bootlickers", "noun", "/ˈbuːtˌlɪkərz/", "kẻ xu nịnh bợ đỡ hèn hạ"),
    ("065969", "borodinos", "noun", "/ˌbɒrəˈdiːnoʊz/", "trận chiến Borodino năm 1812"),
    ("065970", "bronchos", "noun", "/ˈbrɒŋkoʊz/", "ngựa hoang bất kham miền Tây Mỹ"),
    ("065971", "buchners", "noun", "/ˈbʊknərz/", "nhà hóa học hoặc nhà văn Büchner"),
    ("065972", "byres", "noun", "/ˈbaɪərz/", "chuồng nuôi bò sữa"),
    ("065973", "ceca", "noun", "/ˈsiːkə/", "manh tràng ở đầu ruột già"),
    ("065974", "chamfered", "verb", "/ˈtʃæmfərd/", "đã vát mép; đã bào xiên cạnh"),
    ("065975", "chamfering", "verb", "/ˈtʃæmfərɪŋ/", "đang vát mép; việc bào xiên cạnh"),
    ("065976", "chamfers", "noun", "/ˈtʃæmfərz/", "mặt vát xiên cạnh gỗ kim loại"),
    ("065977", "champollions", "noun", "/ʃæmˈpɒliənz/", "nhà Ai Cập học Champollion"),
    ("065978", "chirked", "verb", "/tʃɜːrkt/", "đã kêu ríu rít; đã làm phấn chấn"),
    ("065979", "chirking", "verb", "/ˈtʃɜːrkɪŋ/", "đang kêu ríu rít; làm vui vẻ"),
    ("065980", "chirks", "verb", "/tʃɜːrks/", "kêu ríu rít; làm tinh thần vui vẻ"),
    ("065981", "ciliates", "noun", "/ˈsɪlieɪts/", "động vật nguyên sinh trùng lông"),
    ("065982", "corbels", "noun", "/ˈkɔːrbəlz/", "công-xôn đá đỡ dầm mái kiến trúc"),
    ("065983", "corms", "noun", "/kɔːrmz/", "thân hành; củ phình dưới đất"),
    ("065984", "corticosterones", "noun", "/ˌkɔːrtɪkəˈstɪəroʊnz/", "hoóc-môn vỏ thượng thận"),
    ("065985", "cosigners", "noun", "/ˈkoʊˌsaɪnərz/", "người đồng ký bảo lãnh khoản vay"),
    ("065986", "debilities", "noun", "/dɪˈbɪlɪtiz/", "tình trạng suy nhược ốm yếu"),
    ("065987", "depredations", "noun", "/ˌdɛprəˈdeɪʃənz/", "sự cướp bóc tàn phá nặng nề"),
    ("065988", "dianthuses", "noun", "/daɪˈænθəsɪz/", "hoa cẩm chướng thuộc chi Dianthus"),
    ("065989", "doglegged", "verb", "/ˈdɒɡˌlɛɡd/", "đã uốn cong thành góc gấp khúc"),
    ("065990", "doglegging", "verb", "/ˈdɒɡˌlɛɡɪŋ/", "đang bẻ ngoặt thành góc gấp khúc"),
    ("065991", "doglegs", "noun", "/ˈdɒɡˌlɛɡz/", "đoạn đường hoặc lỗ gôn gấp khúc"),
    ("065992", "eysencks", "noun", "/ˈaɪzɛŋks/", "nhà tâm lý học Hans Eysenck"),
    ("065993", "faguses", "noun", "/ˈfeɪɡəsɪz/", "cây dẻ gai thuộc chi Fagus"),
    ("065994", "fishponds", "noun", "/ˈfɪʃˌpɒndz/", "ao nuôi cá nước ngọt"),
    ("065995", "fluorocarbons", "noun", "/ˌflʊroʊˈkɑːrbənz/", "hợp chất hóa học fluorocarbon"),
    ("065996", "formosans", "noun", "/fɔːrˈmoʊsənz/", "người hoặc ngữ hệ Đài Loan cổ"),
    ("065997", "gambrels", "noun", "/ˈɡæmbrəlz/", "mái nhà hai dốc gãy khúc gambrel"),
    ("065998", "goatherds", "noun", "/ˈɡoʊtˌhɜːrdz/", "người chăn dắt đàn dê"),
    ("065999", "godchildren", "noun", "/ˈɡɒdˌtʃɪldrən/", "con đỡ đầu theo nghi thức rửa tội"),
    ("066000", "goteborgs", "noun", "/ˈjɜːtəˌbɔːrɡz/", "thành phố cảng Gothenburg Thụy Điển"),
    ("066001", "gromykos", "noun", "/ɡrəˈmiːkoʊz/", "nhà ngoại giao Liên Xô Gromyko"),
    ("066002", "guestrooms", "noun", "/ˈɡɛstˌruːmz/", "phòng ngủ dành cho khách ở nhà"),
]

with open("scratch/b34_r02_raw_p5.json") as f:
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

with open("scratch/b34_r02_p5.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r02_p5.json OK")
