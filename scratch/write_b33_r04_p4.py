import json

items = [
  {"id": "lex.en.200k.061803", "hw": "suspensory bandage", "pos": "phrase", "ipa": "/səˈspɛnsəri ˈbændɪdʒ/", "vi": "băng treo nâng đỡ bộ phận cơ thể"},
  {"id": "lex.en.200k.061804", "hw": "systeme international", "pos": "phrase", "ipa": "/siˈstɛm ˌæntərnæsjoʊˈnɑːl/", "vi": "Hệ đo lường đơn vị quốc tế SI"},
  {"id": "lex.en.200k.061805", "hw": "trapezium bone", "pos": "phrase", "ipa": "/trəˈpiːziəm boʊn/", "vi": "xương thang ở hàng cổ tay ngoài"},
  {"id": "lex.en.200k.061806", "hw": "william crawford gorgas", "pos": "phrase", "ipa": "/ˈwɪljəm ˈkrɔːfərd ˈɡɔːrɡəs/", "vi": "bác sĩ quân y Mỹ William Gorgas"},
  {"id": "lex.en.200k.061807", "hw": "xenopus laevis", "pos": "phrase", "ipa": "/ˈzɛnəpəs ˈliːvɪs/", "vi": "ếch móng vuốt châu Phi thí nghiệm"},
  {"id": "lex.en.200k.061808", "hw": "zambian kwacha", "pos": "phrase", "ipa": "/ˈzæmbiən ˈkwɑːtʃə/", "vi": "đơn vị tiền tệ kwacha của Zambia"},
  {"id": "lex.en.200k.061809", "hw": "adars", "pos": "noun", "ipa": "/əˈdɑːrz/", "vi": "tháng thứ 6 lịch Do Thái Adar"},
  {"id": "lex.en.200k.061810", "hw": "adulteresses", "pos": "noun", "ipa": "/əˈdʌltərəsɪz/", "vi": "người đàn bà ngoại tình phản bội"},
  {"id": "lex.en.200k.061811", "hw": "ampoules", "pos": "noun", "ipa": "/ˈæmpuːlz/", "vi": "ống thủy tinh kín đựng thuốc tiêm"},
  {"id": "lex.en.200k.061812", "hw": "anesthetists", "pos": "noun", "ipa": "/əˈnɛsθətɪsts/", "vi": "bác sĩ hoặc điều dưỡng gây mê"},
  {"id": "lex.en.200k.061813", "hw": "anticlimaxes", "pos": "noun", "ipa": "/ˌæntiˈklaɪmæksɪz/", "vi": "sự tụt dốc hụt hẫng mất cao trào"},
  {"id": "lex.en.200k.061814", "hw": "antiphons", "pos": "noun", "ipa": "/ˈæntəfɑːnz/", "vi": "bài thánh ca đối đáp trong lễ"},
  {"id": "lex.en.200k.061815", "hw": "astartes", "pos": "noun", "ipa": "/əˈstɑːrtiz/", "vi": "nữ thần Phượng Hoàng Astarte cổ"},
  {"id": "lex.en.200k.061816", "hw": "astrobiologies", "pos": "noun", "ipa": "/ˌæstroʊbaɪˈɑːlədʒiz/", "vi": "ngành sinh vật học vũ trụ học"},
  {"id": "lex.en.200k.061817", "hw": "atresias", "pos": "noun", "ipa": "/əˈtriːʒəz/", "vi": "dị tật teo bít hẹp lỗ tự nhiên"},
  {"id": "lex.en.200k.061818", "hw": "bagatelles", "pos": "noun", "ipa": "/ˌbæɡəˈtɛlz/", "vi": "tiểu phẩm nhạc nhẹ; điều vặt vãnh"},
  {"id": "lex.en.200k.061819", "hw": "bairns", "pos": "noun", "ipa": "/bɛərnz/", "vi": "đứa trẻ; con cái (tiếng Scotland)"},
  {"id": "lex.en.200k.061820", "hw": "basters", "pos": "noun", "ipa": "/ˈbeɪstərz/", "vi": "ống rưới sốt thịt; người lược chỉ"},
  {"id": "lex.en.200k.061821", "hw": "beaverbrooks", "pos": "noun", "ipa": "/ˈbiːvərbrʊks/", "vi": "chủ báo chí chính khách Beaverbrook"},
  {"id": "lex.en.200k.061822", "hw": "bedas", "pos": "noun", "ipa": "/ˈbiːdəz/", "vi": "sử gia thánh nhân Anh Thánh Beda"},
  {"id": "lex.en.200k.061823", "hw": "breadboards", "pos": "noun", "ipa": "/ˈbrɛdbɔːrdz/", "vi": "thớt thái bánh mì; bảng thử mạch"},
  {"id": "lex.en.200k.061824", "hw": "broncs", "pos": "noun", "ipa": "/brɑːŋks/", "vi": "con ngựa hoang bất kham chưa thuần"},
  {"id": "lex.en.200k.061825", "hw": "burnishes", "pos": "noun", "ipa": "/ˈbɜːrnɪʃɪz/", "vi": "độ bóng láng mượt bề mặt kim loại"},
  {"id": "lex.en.200k.061826", "hw": "burnishing", "pos": "verb", "ipa": "/ˈbɜːrnɪʃɪŋ/", "vi": "đang đánh bóng chà láng kim loại"},
  {"id": "lex.en.200k.061827", "hw": "butterballs", "pos": "noun", "ipa": "/ˈbʌtərbɔːlz/", "vi": "người mũm mĩm tròn xoe; vịt đầu bò"},
  {"id": "lex.en.200k.061828", "hw": "cagliostros", "pos": "noun", "ipa": "/kɑːˈljɔːstroʊz/", "vi": "nhà giả kim phiêu lưu Cagliostro"},
  {"id": "lex.en.200k.061829", "hw": "camomiles", "pos": "noun", "ipa": "/ˈkæməmaɪlz/", "vi": "cây hoa cúc La Mã thảo mộc pha trà"},
  {"id": "lex.en.200k.061830", "hw": "catenae", "pos": "noun", "ipa": "/kəˈtiːniː/", "vi": "chuỗi trích dẫn; chuỗi đất nối tiếp"},
  {"id": "lex.en.200k.061831", "hw": "catenas", "pos": "noun", "ipa": "/kəˈtiːnəz/", "vi": "dãy liên kết các sự vật liên quan"},
  {"id": "lex.en.200k.061832", "hw": "caviled", "pos": "verb", "ipa": "/ˈkævəld/", "vi": "đã bắt bẻ vặt vãnh; bới móc lỗi"},
  {"id": "lex.en.200k.061833", "hw": "caviling", "pos": "verb", "ipa": "/ˈkævəlɪŋ/", "vi": "đang bắt bẻ nhỏ nhặt vụn vặt"},
  {"id": "lex.en.200k.061834", "hw": "chanters", "pos": "noun", "ipa": "/ˈtʃæntərz/", "vi": "ống thổi giai điệu kèn túi; ca sĩ"},
  {"id": "lex.en.200k.061835", "hw": "charis", "pos": "noun", "ipa": "/ˈtʃɑːriz/", "vi": "dòng sông Chari chảy vào hồ Tchad"},
  {"id": "lex.en.200k.061836", "hw": "charybdises", "pos": "noun", "ipa": "/kəˈrɪbdɪsɪz/", "vi": "xoáy nước quái vật biển Charybdis"},
  {"id": "lex.en.200k.061837", "hw": "choristers", "pos": "noun", "ipa": "/ˈkɔːrɪstərz/", "vi": "ca viên hát trong dàn hợp xướng"},
  {"id": "lex.en.200k.061838", "hw": "congeed", "pos": "verb", "ipa": "/ˈkɑːndʒiːd/", "vi": "đã cúi chào từ giã cáo lui"},
  {"id": "lex.en.200k.061839", "hw": "congeeing", "pos": "verb", "ipa": "/ˈkɑːndʒiːɪŋ/", "vi": "đang cúi chào cáo từ rời đi"},
  {"id": "lex.en.200k.061840", "hw": "congees", "pos": "noun", "ipa": "/ˈkɑːndʒiːz/", "vi": "món cháo gạo trắng nấu nhừ châu Á"},
  {"id": "lex.en.200k.061841", "hw": "cosses", "pos": "noun", "ipa": "/kɔːsɪz/", "vi": "đơn vị đo độ dài cổ ở Ấn Độ"},
  {"id": "lex.en.200k.061842", "hw": "cytomegaloviruses", "pos": "noun", "ipa": "/ˌsaɪtoʊˈmɛɡəloʊvaɪrəsɪz/", "vi": "vi-rút cự bào CMV gây nhiễm trùng"},
  {"id": "lex.en.200k.061843", "hw": "dagans", "pos": "noun", "ipa": "/ˈdeɪɡənz/", "vi": "thần lúa mạch nông nghiệp Dagan cổ"},
  {"id": "lex.en.200k.061844", "hw": "darters", "pos": "noun", "ipa": "/ˈdɑːrtərz/", "vi": "chim cổ rắn; cá nhỏ lao vọt nhanh"},
  {"id": "lex.en.200k.061845", "hw": "dawahs", "pos": "noun", "ipa": "/ˈdɑːwəz/", "vi": "hoạt động truyền bá đạo Hồi Dawah"},
  {"id": "lex.en.200k.061846", "hw": "desiccants", "pos": "noun", "ipa": "/ˈdɛsɪkənts/", "vi": "chất hút ẩm chống mốc giữ khô ráo"},
  {"id": "lex.en.200k.061847", "hw": "digesters", "pos": "noun", "ipa": "/daɪˈdʒɛstərz/", "vi": "bể phân hủy sinh học; nồi hầm áp"},
  {"id": "lex.en.200k.061848", "hw": "distils", "pos": "verb", "ipa": "/dɪˈstɪlz/", "vi": "chưng cất chất lỏng; chắt lọc ý"},
  {"id": "lex.en.200k.061849", "hw": "dphs", "pos": "noun", "ipa": "/diː piː eɪtʃɪz/", "vi": "học vị Tiến sĩ Y tế Công cộng DPH"},
  {"id": "lex.en.200k.061850", "hw": "drainpipes", "pos": "noun", "ipa": "/ˈdreɪnpaɪps/", "vi": "ống dẫn thoát nước mưa mái nhà"},
  {"id": "lex.en.200k.061851", "hw": "eelams", "pos": "noun", "ipa": "/ˈiːləmz/", "vi": "tên vùng đất người Tamil Sri Lanka"},
  {"id": "lex.en.200k.061852", "hw": "eggers", "pos": "noun", "ipa": "/ˈɛɡərz/", "vi": "loài bướm đêm lớn họ Lasiocampidae"},
  {"id": "lex.en.200k.061853", "hw": "eposes", "pos": "noun", "ipa": "/ˈɛpɑːsɪz/", "vi": "bộ sử thi anh hùng ca dân tộc"},
  {"id": "lex.en.200k.061854", "hw": "extraversions", "pos": "noun", "ipa": "/ˌɛkstrəˈvɜːrʒənz/", "vi": "tính hướng ngoại cởi mở giao du"},
  {"id": "lex.en.200k.061855", "hw": "foragers", "pos": "noun", "ipa": "/ˈfɔːrɪdʒərz/", "vi": "người hái lượm; loài thú đi kiếm ăn"},
  {"id": "lex.en.200k.061856", "hw": "friedans", "pos": "noun", "ipa": "/friːˈdænz/", "vi": "nhà nữ quyền Mỹ Betty Friedan"},
  {"id": "lex.en.200k.061857", "hw": "giacomettis", "pos": "noun", "ipa": "/ˌdʒɑːkəˈmɛtiz/", "vi": "nhà điêu khắc Alberto Giacometti"},
  {"id": "lex.en.200k.061858", "hw": "hachimans", "pos": "noun", "ipa": "/hɑːˈtʃiːmənz/", "vi": "thần chiến tranh Hachiman Nhật Bản"},
  {"id": "lex.en.200k.061859", "hw": "haematologies", "pos": "noun", "ipa": "/ˌhiːməˈtɑːlədʒiz/", "vi": "ngành y học chuyên khoa huyết học"},
  {"id": "lex.en.200k.061860", "hw": "hedonists", "pos": "noun", "ipa": "/ˈhiːdənɪsts/", "vi": "người theo chủ nghĩa khoái lạc"},
  {"id": "lex.en.200k.061861", "hw": "hemolyses", "pos": "noun", "ipa": "/hɪˈmɑːləsiːz/", "vi": "hiện tượng tan huyết vỡ hồng cầu"},
  {"id": "lex.en.200k.061862", "hw": "henhouses", "pos": "noun", "ipa": "/ˈhɛnhaʊzɪz/", "vi": "chuồng trại nuôi gà đẻ trứng"},
  {"id": "lex.en.200k.061863", "hw": "hokusais", "pos": "noun", "ipa": "/ˈhoʊkʊsaɪz/", "vi": "danh họa khắc gỗ Nhật Bản Hokusai"},
  {"id": "lex.en.200k.061864", "hw": "hookworms", "pos": "noun", "ipa": "/ˈhʊkwɜːrmz/", "vi": "loài giun móc ký sinh hút máu ruột"},
  {"id": "lex.en.200k.061865", "hw": "hyperventilated", "pos": "verb", "ipa": "/ˌhaɪpərˈvɛntəleɪtɪd/", "vi": "đã thở gấp tăng thông khí dồn dập"},
  {"id": "lex.en.200k.061866", "hw": "hyperventilates", "pos": "verb", "ipa": "/ˌhaɪpərˈvɛntəleɪts/", "vi": "thở gấp tăng thông khí quá mức"},
  {"id": "lex.en.200k.061867", "hw": "hyperventilating", "pos": "verb", "ipa": "/ˌhaɪpərˈvɛntəleɪtɪŋ/", "vi": "đang thở gấp dồn dập; thở hổn hển"},
  {"id": "lex.en.200k.061868", "hw": "inchons", "pos": "noun", "ipa": "/ˈɪntʃɑːnz/", "vi": "thành phố cảng Incheon Hàn Quốc"},
  {"id": "lex.en.200k.061869", "hw": "insolations", "pos": "noun", "ipa": "/ˌɪnsəˈleɪʃənz/", "vi": "lượng bức xạ nắng; chứng say nắng"},
  {"id": "lex.en.200k.061870", "hw": "interrelationships", "pos": "noun", "ipa": "/ˌɪntərrɪˈleɪʃənʃɪps/", "vi": "mối quan hệ tương hỗ qua lại"},
  {"id": "lex.en.200k.061871", "hw": "kaftans", "pos": "noun", "ipa": "/ˈkæftænz/", "vi": "áo choàng dài rộng kiểu kaftan"},
  {"id": "lex.en.200k.061872", "hw": "kiswahilis", "pos": "noun", "ipa": "/kiːswɑːˈhiːliz/", "vi": "ngôn ngữ Swahili phổ biến Đông Phi"},
  {"id": "lex.en.200k.061873", "hw": "kordofans", "pos": "noun", "ipa": "/ˌkɔːrdəˈfɑːnz/", "vi": "vùng cao nguyên Kordofan ở Sudan"},
  {"id": "lex.en.200k.061874", "hw": "krasners", "pos": "noun", "ipa": "/ˈkræsnərz/", "vi": "nữ họa sĩ trừu tượng Lee Krasner"},
  {"id": "lex.en.200k.061875", "hw": "lapidaries", "pos": "noun", "ipa": "/ˈlæpɪdɛriz/", "vi": "nghệ nhân cắt mài chế tác đá quý"},
  {"id": "lex.en.200k.061876", "hw": "legitimations", "pos": "noun", "ipa": "/lɪˌdʒɪtəˈmeɪʃənz/", "vi": "sự hợp pháp hóa; xác nhận hợp lệ"},
  {"id": "lex.en.200k.061877", "hw": "lemaitres", "pos": "noun", "ipa": "/ləˈmɛtrəz/", "vi": "nhà vật lý vũ trụ Georges Lemaître"},
  {"id": "lex.en.200k.061878", "hw": "lithologies", "pos": "noun", "ipa": "/lɪˈθɑːlədʒiz/", "vi": "ngành thạch học nghiên cứu đất đá"},
  {"id": "lex.en.200k.061879", "hw": "maleviches", "pos": "noun", "ipa": "/məˈlɛvɪtʃɪz/", "vi": "họa sĩ tiên phong Kazimir Malevich"},
  {"id": "lex.en.200k.061880", "hw": "mandelbrots", "pos": "noun", "ipa": "/ˈmændəlbɔːts/", "vi": "nhà toán học hình học Mandelbrot"},
  {"id": "lex.en.200k.061881", "hw": "mantegnas", "pos": "noun", "ipa": "/mɑːnˈtɛnjəz/", "vi": "họa sĩ Phục hưng Ý Andrea Mantegna"},
  {"id": "lex.en.200k.061882", "hw": "milords", "pos": "noun", "ipa": "/mɪˈlɔːrdz/", "vi": "tước hiệu thưa ngài quý tộc Anh"},
  {"id": "lex.en.200k.061883", "hw": "mineshafts", "pos": "noun", "ipa": "/ˈmaɪnʃæfts/", "vi": "giếng đứng thông xuống hầm mỏ sâu"},
  {"id": "lex.en.200k.061884", "hw": "misconstrued", "pos": "verb", "ipa": "/ˌmɪskənˈstruːd/", "vi": "đã hiểu lầm sai ý nghĩa câu nói"},
  {"id": "lex.en.200k.061885", "hw": "misconstrues", "pos": "verb", "ipa": "/ˌmɪskənˈstruːz/", "vi": "hiểu sai ý nghĩa; diễn giải nhầm"},
  {"id": "lex.en.200k.061886", "hw": "misconstruing", "pos": "verb", "ipa": "/ˌmɪskənˈstruːɪŋ/", "vi": "đang hiểu lầm sai ý; bóp méo nghĩa"},
  {"id": "lex.en.200k.061887", "hw": "mizzens", "pos": "noun", "ipa": "/ˈmɪznz/", "vi": "cột buồm sau cùng; lá buồm lái sau"},
  {"id": "lex.en.200k.061888", "hw": "mollified", "pos": "verb", "ipa": "/ˈmɑːləfaɪd/", "vi": "đã xoa dịu cơn giận; đã làm nguôi"},
  {"id": "lex.en.200k.061889", "hw": "mollifies", "pos": "verb", "ipa": "/ˈmɑːləfaɪz/", "vi": "xoa dịu cơn nóng giận; vỗ về"},
  {"id": "lex.en.200k.061890", "hw": "mollifying", "pos": "verb", "ipa": "/ˈmɑːləfaɪɪŋ/", "vi": "đang xoa dịu lắng xuống; làm mềm"},
  {"id": "lex.en.200k.061891", "hw": "monohydrates", "pos": "noun", "ipa": "/ˌmɑːnoʊˈhaɪdreɪts/", "vi": "tinh thể ngậm một phân tử nước"},
  {"id": "lex.en.200k.061892", "hw": "mutualisms", "pos": "noun", "ipa": "/ˈmjuːtʃuəlɪzəmz/", "vi": "mối quan hệ cộng sinh hỗ trợ nhau"},
  {"id": "lex.en.200k.061893", "hw": "myocarditides", "pos": "noun", "ipa": "/ˌmaɪoʊkɑːrˈdaɪtɪdiːz/", "vi": "các chứng bệnh viêm cơ tim cấp"},
  {"id": "lex.en.200k.061894", "hw": "nardos", "pos": "noun", "ipa": "/ˈnɑːrdoʊz/", "vi": "cây dương xỉ nước bốn lá nardoo Úc"},
  {"id": "lex.en.200k.061895", "hw": "ollas", "pos": "noun", "ipa": "/ˈoʊjəz/", "vi": "nồi gốm miệng rộng; món thịt hầm"},
  {"id": "lex.en.200k.061896", "hw": "ostravas", "pos": "noun", "ipa": "/ˈɔːstrəvəz/", "vi": "thành phố công nghiệp Ostrava Séc"},
  {"id": "lex.en.200k.061897", "hw": "panjabis", "pos": "noun", "ipa": "/pʌnˈdʒɑːbiz/", "vi": "người dân hoặc tiếng vùng Punjab Ấn"},
  {"id": "lex.en.200k.061898", "hw": "parmenideses", "pos": "noun", "ipa": "/pɑːrˈmɛnədiːzɪz/", "vi": "triết gia Hy Lạp cổ đại Parmenides"},
  {"id": "lex.en.200k.061899", "hw": "plasminogens", "pos": "noun", "ipa": "/plæzˈmɪnədʒənz/", "vi": "tiền chất enzyme tan máu đông"},
  {"id": "lex.en.200k.061900", "hw": "poulencs", "pos": "noun", "ipa": "/puːˈlæŋks/", "vi": "nhà soạn nhạc Pháp Francis Poulenc"},
  {"id": "lex.en.200k.061901", "hw": "prurituses", "pos": "noun", "ipa": "/prʊˈraɪtəsɪz/", "vi": "chứng ngứa ngáy ngoài da dữ dội"},
  {"id": "lex.en.200k.061902", "hw": "raskolnikovs", "pos": "noun", "ipa": "/rəˈskɔːlnɪkɔːvz/", "vi": "nhân vật chính Tội ác và Trừng phạt"}
]

with open('scratch/b33_r04_raw_p4.json') as f:
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

with open('scratch/b33_r04_p4.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

print("Batch 33 Round 4 Part 4 validated and written successfully.")
