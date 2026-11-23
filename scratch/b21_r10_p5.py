import json

# Manual word-by-word cognitive review for Batch 21 Round 10 Part 5 (records 4900-4999, IDs 200k.004902 to 200k.005001)
reviewed_entries = [
    # 4900: magic number
    {"ipa": "/ˈmædʒɪk ˈnʌmbər/", "vi": "con số ma thuật trong hạt nhân", "pos": "phrase"},
    # 4901: major scale
    {"ipa": "/ˈmeɪdʒər skeɪl/", "vi": "gam trưởng; thang âm trưởng âm nhạc", "pos": "phrase"},
    # 4902: master race
    {"ipa": "/ˈmæstər reɪs/", "vi": "chủng tộc thượng đẳng Đức Quốc Xã", "pos": "phrase"},
    # 4903: medicine man
    {"ipa": "/ˈmɛdsn mæn/", "vi": "thầy mo chữa bệnh bộ tộc da đỏ", "pos": "phrase"},
    # 4904: miles per hour
    {"ipa": "/maɪlz pər ˈaʊər/", "vi": "dặm trên giờ; đơn vị tốc độ mph", "pos": "phrase"},
    # 4905: military mission
    {"ipa": "/ˈmɪlətɛri ˈmɪʃən/", "vi": "phái đoàn quân sự; sứ mệnh quân sự", "pos": "phrase"},
    # 4906: mix up
    {"ipa": "/mɪks ʌp/", "vi": "làm lộn xộn; nhầm lẫn tai hại", "pos": "phrase"},
    # 4907: moon on
    {"ipa": "/muːn ɑːn/", "vi": "mơ màng thẫn thờ; tơ tưởng tương tư", "pos": "phrase"},
    # 4908: mountain man
    {"ipa": "/ˈmaʊntn mæn/", "vi": "người bẫy thú rừng miền sơn cước", "pos": "phrase"},
    # 4909: national weather service
    {"ipa": "/ˈnæʃnəl ˈwɛðər ˈsɜːrvɪs/", "vi": "Cơ quan Thời tiết Quốc gia Hoa Kỳ", "pos": "phrase"},
    # 4910: natural resources
    {"ipa": "/ˈnætʃrəl ˈriːsɔːrsɪz/", "vi": "tài nguyên thiên nhiên của quốc gia", "pos": "phrase"},
    # 4911: natural spring
    {"ipa": "/ˈnætʃrəl sprɪŋ/", "vi": "mạch nước ngầm; dòng suối tự nhiên", "pos": "phrase"},
    # 4912: off guard
    {"ipa": "/ɔːf ɡɑːrd/", "vi": "lơ là mất cảnh giác; bị bất ngờ", "pos": "phrase"},
    # 4913: off his guard
    {"ipa": "/ɔːf hɪz ɡɑːrd/", "vi": "mất cảnh giác; sơ hở không phòng bị", "pos": "phrase"},
    # 4914: off your guard
    {"ipa": "/ɔːf jɔːr ɡɑːrd/", "vi": "bạn lơ là sơ hở; mất cảnh giác", "pos": "phrase"},
    # 4915: one hundred
    {"ipa": "/wʌn ˈhʌndrəd/", "vi": "một trăm; con số tròn 100", "pos": "phrase"},
    # 4916: one hundred one
    {"ipa": "/wʌn ˈhʌndrəd wʌn/", "vi": "một trăm lẻ một; kiến thức sơ cấp", "pos": "phrase"},
    # 4917: phone jack
    {"ipa": "/foʊn dʒæk/", "vi": "ổ cắm dây điện thoại; giắc cắm line", "pos": "phrase"},
    # 4918: popular opinion
    {"ipa": "/ˈpɑːpjələr əˈpɪnjən/", "vi": "dư luận xã hội; quan điểm số đông", "pos": "phrase"},
    # 4919: positive charge
    {"ipa": "/ˈpɑːzətɪv tʃɑːrdʒ/", "vi": "điện tích dương trong vật lý", "pos": "phrase"},
    # 4920: potential drop
    {"ipa": "/pəˈtɛnʃl drɑːp/", "vi": "độ sụt điện áp; giảm áp mạch điện", "pos": "phrase"},
    # 4921: quarter day
    {"ipa": "/ˈkwɔːrtər deɪ/", "vi": "ngày kết toán theo quý trong năm", "pos": "phrase"},
    # 4922: radio link
    {"ipa": "/ˈreɪdioʊ lɪŋk/", "vi": "đường truyền vô tuyến viễn thông", "pos": "phrase"},
    # 4923: rain out
    {"ipa": "/reɪn aʊt/", "vi": "hoãn trận đấu vì trời mưa to", "pos": "phrase"},
    # 4924: regular army
    {"ipa": "/ˈrɛɡjələr ˈɑːrmi/", "vi": "quân đội chính quy thường trực", "pos": "phrase"},
    # 4925: round trip
    {"ipa": "/raʊnd trɪp/", "vi": "chuyến đi khứ hồi; vé khứ hồi", "pos": "phrase"},
    # 4926: royal road
    {"ipa": "/ˈrɔɪəl roʊd/", "vi": "con đường êm thắm; lối đi dễ dàng", "pos": "phrase"},
    # 4927: sex activity
    {"ipa": "/sɛks ækˈtɪvəti/", "vi": "hoạt động quan hệ tình dục sinh lý", "pos": "phrase"},
    # 4928: shoot down
    {"ipa": "/ʃuːt daʊn/", "vi": "bắn hạ máy bay; bác bỏ thẳng thừng", "pos": "phrase"},
    # 4929: shop boy
    {"ipa": "/ʃɑːp bɔɪ/", "vi": "cậu bé phụ việc trong cửa hàng", "pos": "phrase"},
    # 4930: short selling
    {"ipa": "/ʃɔːrt ˈsɛlɪŋ/", "vi": "nghiệp vụ bán khống chứng khoán", "pos": "phrase"},
    # 4931: shot glass
    {"ipa": "/ʃɑːt ɡlæs/", "vi": "ly thủy tinh uống rượu mạnh shot", "pos": "phrase"},
    # 4932: song of songs
    {"ipa": "/sɔːŋ ʌv sɔːŋz/", "vi": "sách Nhã Ca trong bộ Kinh Thánh", "pos": "phrase"},
    # 4933: special agent
    {"ipa": "/ˈspɛʃl ˈeɪdʒənt/", "vi": "đặc vụ điều tra viên liên bang FBI", "pos": "phrase"},
    # 4934: spirit level
    {"ipa": "/ˈspɪrɪt ˈlɛvl/", "vi": "thước thủy chuẩn ống bọt nước", "pos": "phrase"},
    # 4935: street smart
    {"ipa": "/striːt smɑːrt/", "vi": "sự khôn ngoan từng trải đường đời", "pos": "phrase"},
    # 4936: sun river
    {"ipa": "/sʌn ˈrɪvər/", "vi": "sông Sun River tại bang Montana Mỹ", "pos": "phrase"},
    # 4937: surface fire
    {"ipa": "/ˈsɜːrfɪs faɪər/", "vi": "đám cháy bề mặt thảm rừng cỏ khô", "pos": "phrase"},
    # 4938: sweet cup
    {"ipa": "/swiːt kʌp/", "vi": "quả lạc tiên ngọt Passiflora", "pos": "phrase"},
    # 4939: take orders
    {"ipa": "/teɪk ˈɔːrdərz/", "vi": "nhận mệnh lệnh; nhận đơn đặt hàng", "pos": "phrase"},
    # 4940: take sides with
    {"ipa": "/teɪk saɪdz wɪð/", "vi": "đứng về phe; thiên vị ủng hộ ai", "pos": "phrase"},
    # 4941: technology administration
    {"ipa": "/tɛkˈnɑːlədʒi ədˌmɪnɪˈstreɪʃən/", "vi": "Cơ quan Quản lý Công nghệ Quốc gia", "pos": "phrase"},
    # 4942: television news
    {"ipa": "/ˈtɛləvɪʒən nuːz/", "vi": "chương trình tin tức truyền hình", "pos": "phrase"},
    # 4943: third estate
    {"ipa": "/θɜːrd ɪˈsteɪt/", "vi": "đẳng cấp thứ ba; tầng lớp bình dân", "pos": "phrase"},
    # 4944: to the limit
    {"ipa": "/tuː ðə ˈlɪmɪt/", "vi": "đến tận giới hạn cùng cực tối đa", "pos": "phrase"},
    # 4945: total heat
    {"ipa": "/ˈtoʊtl hiːt/", "vi": "nhiệt hàm toàn phần; entanpi", "pos": "phrase"},
    # 4946: touch football
    {"ipa": "/tʌtʃ ˈfʊtbɔːl/", "vi": "môn bóng bầu dục chạm không húc", "pos": "phrase"},
    # 4947: tv camera
    {"ipa": "/ˌtiːˈviː ˈkæmrə/", "vi": "máy quay phim đài truyền hình", "pos": "phrase"},
    # 4948: variety show
    {"ipa": "/vəˈraɪəti ʃoʊ/", "vi": "chương trình đại nhạc hội tạp kỹ", "pos": "phrase"},
    # 4949: warm up
    {"ipa": "/wɔːrm ʌp/", "vi": "khởi động làm nóng người; hâm nóng", "pos": "phrase"},
    # 4950: word square
    {"ipa": "/wɜːrd skwɛr/", "vi": "trò chơi ô chữ hình vuông đối xứng", "pos": "phrase"},
    # 4951: word structure
    {"ipa": "/wɜːrd ˈstrʌktʃər/", "vi": "cấu trúc hình thái học của từ vựng", "pos": "phrase"},
    # 4952: work clothes
    {"ipa": "/wɜːrk kloʊðz/", "vi": "quần áo bảo hộ lao động nhà xưởng", "pos": "phrase"},
    # 4953: sawed
    {"ipa": "/sɔːd/", "vi": "đã cưa xẻ gỗ; đã dùng lưỡi cưa", "pos": "verb"},
    # 4954: sawing
    {"ipa": "/ˈsɔːɪŋ/", "vi": "đang cưa xẻ gỗ; động tác kéo cưa", "pos": "verb"},
    # 4955: sawn
    {"ipa": "/sɔːn/", "vi": "được cưa xẻ ra; dạng bị cưa đứt", "pos": "verb"},
    # 4956: saws
    {"ipa": "/sɔːz/", "vi": "những chiếc cưa; các câu ngạn ngữ", "pos": "noun"},
    # 4957: specials
    {"ipa": "/ˈspɛʃlz/", "vi": "các món đặc sản; các đợt giảm giá", "pos": "noun"},
    # 4958: futures
    {"ipa": "/ˈfjuːtʃərz/", "vi": "các hợp đồng tương lai; tiền đồ", "pos": "noun"},
    # 4959: millions
    {"ipa": "/ˈmɪljənz/", "vi": "hàng triệu; vô số người dân chúng", "pos": "noun"},
    # 4960: stayed
    {"ipa": "/steɪd/", "vi": "đã lưu lại trú lại; đã hoãn lại", "pos": "verb"},
    # 4961: active voice
    {"ipa": "/ˈæktɪv vɔɪs/", "vi": "thể chủ động trong ngữ pháp câu", "pos": "phrase"},
    # 4962: air bag
    {"ipa": "/ɛr bæɡ/", "vi": "túi khí an toàn trên xe ô tô", "pos": "phrase"},
    # 4963: baby rose
    {"ipa": "/ˈbeɪbi roʊz/", "vi": "hoa hồng leo tường nhỏ xinh bông", "pos": "phrase"},
    # 4964: balance of power
    {"ipa": "/ˈbæləns ʌv ˈpaʊər/", "vi": "cán cân quyền lực địa chính trị", "pos": "phrase"},
    # 4965: bay state
    {"ipa": "/beɪ steɪt/", "vi": "bang Vịnh Massachusetts nước Mỹ", "pos": "phrase"},
    # 4966: beer can
    {"ipa": "/bɪr kæn/", "vi": "vỏ lon bia bằng kim loại nhôm", "pos": "phrase"},
    # 4967: birthday party
    {"ipa": "/ˈbɜːrθdeɪ ˈpɑːrti/", "vi": "bữa tiệc sinh nhật mừng tuổi mới", "pos": "phrase"},
    # 4968: blood disease
    {"ipa": "/blʌd dɪˈziːz/", "vi": "bệnh lý về máu; rối loạn huyết học", "pos": "phrase"},
    # 4969: blue peter
    {"ipa": "/bluː ˈpiːtər/", "vi": "cờ hiệu xanh báo tàu sắp nhổ neo", "pos": "phrase"},
    # 4970: body bag
    {"ipa": "/ˈbɑːdi bæɡ/", "vi": "túi bọc tử thi; bao đựng thi thể", "pos": "phrase"},
    # 4971: breaking away
    {"ipa": "/ˈbreɪkɪŋ əˈweɪ/", "vi": "sự bứt phá ly khai; thoát ly nhóm", "pos": "phrase"},
    # 4972: capital of canada
    {"ipa": "/ˈkæpɪtl ʌv ˈkænədə/", "vi": "thủ đô Ottawa của đất nước Canada", "pos": "phrase"},
    # 4973: carry forward
    {"ipa": "/ˈkæri ˈfɔːrwərd/", "vi": "kết chuyển sang kỳ sau sổ kế toán", "pos": "phrase"},
    # 4974: cat food
    {"ipa": "/kæt fuːd/", "vi": "thức ăn dành cho mèo; hạt cho mèo", "pos": "phrase"},
    # 4975: coffee break
    {"ipa": "/ˈkɔːfi breɪk/", "vi": "giờ nghỉ giải lao uống cà phê", "pos": "phrase"},
    # 4976: color code
    {"ipa": "/ˈkʌlər koʊd/", "vi": "mã màu quy ước phân loại dữ liệu", "pos": "phrase"},
    # 4977: commercial paper
    {"ipa": "/kəˈmɜːrʃl ˈpeɪpər/", "vi": "thương phiếu ngắn hạn phát hành", "pos": "phrase"},
    # 4978: computer network
    {"ipa": "/kəmˈpjuːtər ˈnɛtwɜːrk/", "vi": "mạng máy vi tính kết nối dữ liệu", "pos": "phrase"},
    # 4979: computer store
    {"ipa": "/kəmˈpjuːtər stɔːr/", "vi": "cửa hàng bán máy vi tính phụ kiện", "pos": "phrase"},
    # 4980: contract offer
    {"ipa": "/ˈkɑːntrækt ˈɔːfər/", "vi": "đề nghị giao kết hợp đồng kinh tế", "pos": "phrase"},
    # 4981: control function
    {"ipa": "/kənˈtroʊl ˈfʌŋkʃən/", "vi": "chức năng điều khiển kiểm soát", "pos": "phrase"},
    # 4982: crowd out
    {"ipa": "/kraʊd aʊt/", "vi": "chèn ép đẩy lùi; hiệu ứng lấn át", "pos": "phrase"},
    # 4983: david smith
    {"ipa": "/ˈdeɪvɪd smɪθ/", "vi": "nhà điêu khắc David Smith nước Mỹ", "pos": "phrase"},
    # 4984: dead heat
    {"ipa": "/dɛd hiːt/", "vi": "cuộc đua hòa điểm; về đích cùng lúc", "pos": "phrase"},
    # 4985: death camp
    {"ipa": "/dɛθ kæmp/", "vi": "trại hủy diệt tử thần diệt chủng", "pos": "phrase"},
    # 4986: doctor of science
    {"ipa": "/ˈdɑːktər ʌv ˈsaɪəns/", "vi": "học vị tiến sĩ khoa học tự nhiên", "pos": "phrase"},
    # 4987: double quick
    {"ipa": "/ˈdʌbl kwɪk/", "vi": "bước đều chạy nhanh gấp đôi", "pos": "phrase"},
    # 4988: draw near
    {"ipa": "/drɔː nɪr/", "vi": "tiến sát lại gần; ngày càng cận kề", "pos": "phrase"},
    # 4989: east coast
    {"ipa": "/iːst koʊst/", "vi": "vùng Bờ Đông nước Mỹ duyên hải", "pos": "phrase"},
    # 4990: election commission
    {"ipa": "/ɪˈlɛkʃən kəˈmɪʃən/", "vi": "hội đồng bầu cử quốc gia độc lập", "pos": "phrase"},
    # 4991: english channel
    {"ipa": "/ˈɪŋɡlɪʃ ˈtʃænl/", "vi": "eo biển Manche nối Anh và Pháp", "pos": "phrase"},
    # 4992: evening star
    {"ipa": "/ˈiːvnɪŋ stɑːr/", "vi": "ngôi sao Hôm; sao Kim lúc hoàng hôn", "pos": "phrase"},
    # 4993: executive director
    {"ipa": "/ɪɡˈzɛkjətɪv dəˈrɛktər/", "vi": "giám đốc điều hành tổng quản lý", "pos": "phrase"},
    # 4994: eye movement
    {"ipa": "/aɪ ˈmuːvmənt/", "vi": "cử động nhãn cầu của đôi mắt", "pos": "phrase"},
    # 4995: facts of life
    {"ipa": "/fækts ʌv laɪf/", "vi": "thực tế đời sống; chuyện sinh sản", "pos": "phrase"},
    # 4996: file name
    {"ipa": "/faɪl neɪm/", "vi": "tên của tập tin lưu trên máy tính", "pos": "phrase"},
    # 4997: file system
    {"ipa": "/faɪl ˈsɪstəm/", "vi": "hệ thống quản lý tập tin ổ đĩa", "pos": "phrase"},
    # 4998: financial organization
    {"ipa": "/faɪˈnænʃl ˌɔːrɡənəˈzeɪʃən/", "vi": "tổ chức tài chính; định chế tiền tệ", "pos": "phrase"},
    # 4999: fine structure
    {"ipa": "/faɪn ˈstrʌktʃər/", "vi": "cấu trúc vi mô tinh tế quang phổ", "pos": "phrase"}
]

with open("scratch/b21_r10_raw_p5.json", "r", encoding="utf-8") as f:
    raw_data = json.load(f)

assert len(raw_data) == 100
assert len(reviewed_entries) == 100

output = []
for i, item in enumerate(raw_data):
    rev = reviewed_entries[i]
    assert len(rev["vi"]) <= 35, f"Too long: {item['hw']} -> {rev['vi']} ({len(rev['vi'])} chars)"
    assert rev["ipa"].startswith("/") and rev["ipa"].endswith("/"), f"Bad IPA: {item['hw']} -> {rev['ipa']}"
    assert rev["ipa"].count("/") == 2, f"Bad slash count: {item['hw']} -> {rev['ipa']}"
    assert rev["pos"] in ["noun", "verb", "adj", "adv", "intj", "prep", "conj", "pron", "det", "num", "phrase"]

    entry = {
        "id": item["id"],
        "hw": item["hw"],
        "pos": rev["pos"],
        "ipa": rev["ipa"],
        "vi": rev["vi"],
        "cefr": item["cefr"],
        "tier": item["tier"],
        "status": "reviewed",
        "notes": item["notes"]
    }
    output.append(entry)

with open("scratch/b21_r10_p5.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"Successfully processed {len(output)} entries for Round 10 Part 5.")
