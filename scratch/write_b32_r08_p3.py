import json

items = [
  {"id": "lex.en.200k.058702", "hw": "jarrells", "pos": "noun", "ipa": "/dʒˈærəlz/", "vi": "nhà thơ Randall Jarrell"},
  {"id": "lex.en.200k.058703", "hw": "juleps", "pos": "noun", "ipa": "/dʒˈuləps/", "vi": "rượu cocktail bạc hà julep"},
  {"id": "lex.en.200k.058704", "hw": "khadis", "pos": "noun", "ipa": "/kˈɑːdiz/", "vi": "vải sợi dệt tay khadi"},
  {"id": "lex.en.200k.058705", "hw": "kookaburras", "pos": "noun", "ipa": "/kˈʊkəbˌɜːrəz/", "vi": "chim bói cá kookaburra Úc"},
  {"id": "lex.en.200k.058706", "hw": "kosciuskos", "pos": "noun", "ipa": "/kˌɑːziˈʌskoʊz/", "vi": "tướng Tadeusz Kościuszko"},
  {"id": "lex.en.200k.058707", "hw": "kurtas", "pos": "noun", "ipa": "/kˈʊrtəz/", "vi": "áo dài truyền thống kurta"},
  {"id": "lex.en.200k.058708", "hw": "lionfishes", "pos": "noun", "ipa": "/lˈaɪənfˌɪʃɪz/", "vi": "cá sư tử biển; cá mao tiên"},
  {"id": "lex.en.200k.058709", "hw": "malthuses", "pos": "noun", "ipa": "/mˈæmθəsɪz/", "vi": "nhà kinh tế học Malthus"},
  {"id": "lex.en.200k.058710", "hw": "methuselahs", "pos": "noun", "ipa": "/mɪθˈuːzələz/", "vi": "người đại thọ; chai rượu 6 lít"},
  {"id": "lex.en.200k.058711", "hw": "mickles", "pos": "noun", "ipa": "/mˈɪkəlz/", "vi": "món nhỏ tích tụ; số lượng lớn"},
  {"id": "lex.en.200k.058712", "hw": "misdemeanours", "pos": "noun", "ipa": "/ˌmɪsdəmˈiːnɚz/", "vi": "tội ít nghiêm trọng; vi phạm nhẹ"},
  {"id": "lex.en.200k.058713", "hw": "nacelles", "pos": "noun", "ipa": "/nəsˈɛlz/", "vi": "vỏ động cơ máy bay; buồng lái"},
  {"id": "lex.en.200k.058714", "hw": "namurs", "pos": "noun", "ipa": "/nɑːmˈjʊərz/", "vi": "thành phố Namur của Bỉ"},
  {"id": "lex.en.200k.058715", "hw": "norges", "pos": "noun", "ipa": "/nˈɔːrɡeɪz/", "vi": "nước Na Uy"},
  {"id": "lex.en.200k.058716", "hw": "outdoorsmans", "pos": "noun", "ipa": "/ˈaʊtdɔːrzmənz/", "vi": "người mê hoạt động ngoài trời"},
  {"id": "lex.en.200k.058717", "hw": "paperboys", "pos": "noun", "ipa": "/pˈeɪpɚbˌɔjz/", "vi": "cậu bé giao báo dạo"},
  {"id": "lex.en.200k.058718", "hw": "pastorates", "pos": "noun", "ipa": "/pˈæstərɪts/", "vi": "chức vị mục sư; nhiệm kỳ mục vụ"},
  {"id": "lex.en.200k.058719", "hw": "pepla", "pos": "noun", "ipa": "/pˈɛplə/", "vi": "vạt áo xòe; tầng vải peplum"},
  {"id": "lex.en.200k.058720", "hw": "peplums", "pos": "noun", "ipa": "/pˈɛpləmz/", "vi": "vạt áo peplum xòe ngang hông"},
  {"id": "lex.en.200k.058721", "hw": "periodontitises", "pos": "noun", "ipa": "/ˌpɛrioʊdɑːntˈaɪtɪsɪz/", "vi": "bệnh viêm nha chu quanh răng"},
  {"id": "lex.en.200k.058722", "hw": "petrarches", "pos": "noun", "ipa": "/pɛtrˈɑːrkɪz/", "vi": "nhà thơ Petrarca"},
  {"id": "lex.en.200k.058723", "hw": "petrels", "pos": "noun", "ipa": "/pˈɛtrəlz/", "vi": "chim hải âu báo bão"},
  {"id": "lex.en.200k.058724", "hw": "psalmists", "pos": "noun", "ipa": "/sˈɑːmɪsts/", "vi": "tác giả thánh thi; người hát vịnh"},
  {"id": "lex.en.200k.058725", "hw": "pyridines", "pos": "noun", "ipa": "/pˈɪrədiːnz/", "vi": "hợp chất hữu cơ pyridine"},
  {"id": "lex.en.200k.058726", "hw": "pyrrhuses", "pos": "noun", "ipa": "/pˈɪrəsɪz/", "vi": "vua Pyrrhus xứ Epirus"},
  {"id": "lex.en.200k.058727", "hw": "recommits", "pos": "verb", "ipa": "/rɪkˈɑmɪts/", "vi": "giao lại xem xét; cam kết lại"},
  {"id": "lex.en.200k.058728", "hw": "recommitted", "pos": "verb", "ipa": "/rˌikəmˈɪtɪd/", "vi": "đã cam kết lại; giao lại"},
  {"id": "lex.en.200k.058729", "hw": "recommitting", "pos": "verb", "ipa": "/ˌriːkəmˈɪtɪŋ/", "vi": "đang cam kết lại; giao lại hồ sơ"},
  {"id": "lex.en.200k.058730", "hw": "sachets", "pos": "noun", "ipa": "/sæʃˈeɪz/", "vi": "gói nhỏ tiện dụng; túi hương liệu"},
  {"id": "lex.en.200k.058731", "hw": "savitars", "pos": "noun", "ipa": "/sˈævətɑːrz/", "vi": "thần mặt trời Savitr"},
  {"id": "lex.en.200k.058732", "hw": "scrappers", "pos": "noun", "ipa": "/skrˈæpɚz/", "vi": "người hiếu chiến; thợ ve chai"},
  {"id": "lex.en.200k.058733", "hw": "slovenlier", "pos": "adj", "ipa": "/slˈʌvənliɚ/", "vi": "luộm thuộm hơn; bừa bãi hơn"},
  {"id": "lex.en.200k.058734", "hw": "slovenliest", "pos": "adj", "ipa": "/slˈʌvənliɪst/", "vi": "luộm thuộm nhất; nhếch nhác nhất"},
  {"id": "lex.en.200k.058735", "hw": "sonograms", "pos": "noun", "ipa": "/sˈɔnəɡrˌæmz/", "vi": "hình ảnh chụp siêu âm y khoa"},
  {"id": "lex.en.200k.058736", "hw": "spalls", "pos": "noun", "ipa": "/spˈɔːlz/", "vi": "mảnh vụn đá; mạt đá vỡ"},
  {"id": "lex.en.200k.058737", "hw": "stomas", "pos": "noun", "ipa": "/stˈoʊməz/", "vi": "lỗ khí khổng lá; lỗ mở thông ruột"},
  {"id": "lex.en.200k.058738", "hw": "subscripts", "pos": "noun", "ipa": "/sˈʌbskrɪpts/", "vi": "chỉ số dưới; ký tự viết thụt xuống"},
  {"id": "lex.en.200k.058739", "hw": "taprooms", "pos": "noun", "ipa": "/tˈæpruːmz/", "vi": "quán phục vụ bia tươi; quán rượu"},
  {"id": "lex.en.200k.058740", "hw": "telomerases", "pos": "noun", "ipa": "/təlˈɑːməreɪsɪz/", "vi": "men enzym telomerase"},
  {"id": "lex.en.200k.058741", "hw": "thanatoses", "pos": "noun", "ipa": "/θˈænətoʊsɪz/", "vi": "thần chết Thanatos; bản năng chết"},
  {"id": "lex.en.200k.058742", "hw": "theists", "pos": "noun", "ipa": "/θˈiːɪsts/", "vi": "người theo thuyết hữu thần"},
  {"id": "lex.en.200k.058743", "hw": "thermopylaes", "pos": "noun", "ipa": "/θərmˈɑːpɪliːz/", "vi": "trận Thermopylae; đèo núi hiểm"},
  {"id": "lex.en.200k.058744", "hw": "thumbprints", "pos": "noun", "ipa": "/θˈʌmprɪnts/", "vi": "dấu vân tay ngón cái"},
  {"id": "lex.en.200k.058745", "hw": "tojos", "pos": "noun", "ipa": "/tˈoʊdʒoʊz/", "vi": "thủ tướng Hideki Tojo"},
  {"id": "lex.en.200k.058746", "hw": "toped", "pos": "verb", "ipa": "/tˈoʊpt/", "vi": "đã uống rượu say sưa"},
  {"id": "lex.en.200k.058747", "hw": "topes", "pos": "noun", "ipa": "/tˈoʊps/", "vi": "bảo tháp xá lợi Phật giáo; tháp"},
  {"id": "lex.en.200k.058748", "hw": "typesets", "pos": "verb", "ipa": "/tˈaɪpsɛts/", "vi": "sắp chữ in; xếp chữ dòng sách"},
  {"id": "lex.en.200k.058749", "hw": "victimisations", "pos": "noun", "ipa": "/vˌɪktɪmɪzˈeɪʃənz/", "vi": "sự trừng phạt oan; hành vi trù dập"},
  {"id": "lex.en.200k.058750", "hw": "waratahs", "pos": "noun", "ipa": "/wˈɔːrətɑːz/", "vi": "hoa bụi đỏ waratah nước Úc"},
  {"id": "lex.en.200k.058751", "hw": "washingtonians", "pos": "noun", "ipa": "/wˌɑʃɪŋtˈoʊniənz/", "vi": "người dân vùng Washington"},
  {"id": "lex.en.200k.058752", "hw": "watchwords", "pos": "noun", "ipa": "/wˈɑtʃwˌɜːrdz/", "vi": "khẩu hiệu hành động; mật hiệu"},
  {"id": "lex.en.200k.058753", "hw": "wracked", "pos": "verb", "ipa": "/rˈækt/", "vi": "bị dày vò thể xác; bị tàn phá"},
  {"id": "lex.en.200k.058754", "hw": "wracking", "pos": "verb", "ipa": "/rˈækɪŋ/", "vi": "đang dày vò; làm tổn hại tàn phá"},
  {"id": "lex.en.200k.058755", "hw": "wracks", "pos": "noun", "ipa": "/rˈæks/", "vi": "đám rong biển dạt bờ; xác đổ nát"},
  {"id": "lex.en.200k.058756", "hw": "xenopuses", "pos": "noun", "ipa": "/zˈɛnəpəsɪz/", "vi": "loài ếch có vuốt châu Phi xenopus"},
  {"id": "lex.en.200k.058757", "hw": "aliquot part", "pos": "phrase", "ipa": "/ˈælɪkwɑːt pɑːrt/", "vi": "ước số đúng; phần nguyên chia hết"},
  {"id": "lex.en.200k.058758", "hw": "amanita caesarea", "pos": "phrase", "ipa": "/ˌæməˈnaɪtə sɪˈzɛriə/", "vi": "loài nấm hoàng đế Caesar"},
  {"id": "lex.en.200k.058759", "hw": "american dewberry", "pos": "phrase", "ipa": "/əˈmɛrɪkən ˈduːbɛri/", "vi": "loài dâu mâm xôi dại Bắc Mỹ"},
  {"id": "lex.en.200k.058760", "hw": "antimony potassium tartrate", "pos": "phrase", "ipa": "/ˈæntɪmoʊni pəˈtæsiəm ˈtɑːrtreɪt/", "vi": "chất kali antimon tartrat"},
  {"id": "lex.en.200k.058761", "hw": "archean eon", "pos": "phrase", "ipa": "/ɑːrˈkiːən ˈiːɑːn/", "vi": "liên đại Thái Cổ"},
  {"id": "lex.en.200k.058762", "hw": "bernard hinault", "pos": "phrase", "ipa": "/bərˈnɑːrd iːˈnoʊ/", "vi": "tay đua xe đạp Bernard Hinault"},
  {"id": "lex.en.200k.058763", "hw": "blat out", "pos": "phrase", "ipa": "/blæt aʊt/", "vi": "thốt ra bừa bãi; buột mồm nói"},
  {"id": "lex.en.200k.058764", "hw": "book of haggai", "pos": "phrase", "ipa": "/bʊk əv ˈhæɡeɪaɪ/", "vi": "sách tiên tri Ha-gai"},
  {"id": "lex.en.200k.058765", "hw": "bustard quail", "pos": "phrase", "ipa": "/ˈbʌstərd kweɪl/", "vi": "loài chim cút ô tác"},
  {"id": "lex.en.200k.058766", "hw": "carbolic acid", "pos": "phrase", "ipa": "/kɑːrˈbɑːlɪk ˈæsɪd/", "vi": "axit cacbolic; chất phenol"},
  {"id": "lex.en.200k.058767", "hw": "chenin blanc", "pos": "phrase", "ipa": "/ˌʃɛnɪn ˈblɑːŋk/", "vi": "giống nho trắng Chenin Blanc"},
  {"id": "lex.en.200k.058768", "hw": "coloratura soprano", "pos": "phrase", "ipa": "/ˌkʌlərəˈtʊərə səˈprɑːnoʊ/", "vi": "giọng nữ cao màu sắc hoa mỹ"},
  {"id": "lex.en.200k.058769", "hw": "cotton stainer", "pos": "phrase", "ipa": "/ˈkɑːtn ˈsteɪnər/", "vi": "loài bọ xít hại bông vải"},
  {"id": "lex.en.200k.058770", "hw": "crosscut saw", "pos": "phrase", "ipa": "/ˈkrɔːskʌt sɔː/", "vi": "cưa tay cưa ngang thớ gỗ"},
  {"id": "lex.en.200k.058771", "hw": "darning needle", "pos": "phrase", "ipa": "/ˈdɑːrnɪŋ ˈniːdl/", "vi": "kim khâu vá mạng; chuồn chuồn"},
  {"id": "lex.en.200k.058772", "hw": "dementia praecox", "pos": "phrase", "ipa": "/dɪˈmɛnʃiə ˈpriːkɑːks/", "vi": "chứng tâm thần phân liệt sớm"},
  {"id": "lex.en.200k.058773", "hw": "dewberry bush", "pos": "phrase", "ipa": "/ˈduːbɛri bʊʃ/", "vi": "bụi cây mâm xôi gai bò"},
  {"id": "lex.en.200k.058774", "hw": "downy manzanita", "pos": "phrase", "ipa": "/ˈdaʊni ˌmænzəˈniːtə/", "vi": "cây bụi mộc tặc lông manzanita"},
  {"id": "lex.en.200k.058775", "hw": "european dewberry", "pos": "phrase", "ipa": "/ˌjʊərəˈpiːən ˈduːbɛri/", "vi": "dâu mâm xôi xanh châu Âu"},
  {"id": "lex.en.200k.058776", "hw": "foxtail millet", "pos": "phrase", "ipa": "/ˈfɑːksteɪl ˈmɪlɪt/", "vi": "cây kê đuôi chồn"},
  {"id": "lex.en.200k.058777", "hw": "francois villon", "pos": "phrase", "ipa": "/frɑːnˈswɑː viːˈjɔːn/", "vi": "nhà thơ François Villon"},
  {"id": "lex.en.200k.058778", "hw": "genus amia", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈeɪmiə/", "vi": "chi cá vây cung Amia"},
  {"id": "lex.en.200k.058779", "hw": "genus forsythia", "pos": "phrase", "ipa": "/ˈdʒiːnəs fɔːrˈsɪθiə/", "vi": "chi hoa mai Mỹ liên kiều"},
  {"id": "lex.en.200k.058780", "hw": "genus phylloxera", "pos": "phrase", "ipa": "/ˈdʒiːnəs fɪˈlɑːksərə/", "vi": "chi rệp hại rễ nho Phylloxera"},
  {"id": "lex.en.200k.058781", "hw": "genus rhus", "pos": "phrase", "ipa": "/ˈdʒiːnəs rʊs/", "vi": "chi cây sơn đào Rhus"},
  {"id": "lex.en.200k.058782", "hw": "giuseppe sarto", "pos": "phrase", "ipa": "/dʒuːˈzɛppeɪ ˈsɑːrtoʊ/", "vi": "Giáo hoàng Piô X Giuseppe Sarto"},
  {"id": "lex.en.200k.058783", "hw": "grape phylloxera", "pos": "phrase", "ipa": "/ɡreɪp fɪˈlɑːksərə/", "vi": "rệp rễ ăn hại cây nho"},
  {"id": "lex.en.200k.058784", "hw": "hanky panky", "pos": "phrase", "ipa": "/ˈhæŋki ˈpæŋki/", "vi": "trò gian trá; hành vi mờ ám"},
  {"id": "lex.en.200k.058785", "hw": "henri pitot", "pos": "phrase", "ipa": "/ɑːnˈriː piːˈtoʊ/", "vi": "kỹ sư Henri Pitot sáng chế ống đo"},
  {"id": "lex.en.200k.058786", "hw": "hominy grits", "pos": "phrase", "ipa": "/ˈhɑːməni ɡrɪts/", "vi": "món cháo ngô tấm ninh nhừ"},
  {"id": "lex.en.200k.058787", "hw": "joao pessoa", "pos": "phrase", "ipa": "/ʒwˈaʊ pəˈsoʊə/", "vi": "thành phố cảng João Pessoa"},
  {"id": "lex.en.200k.058788", "hw": "john amos comenius", "pos": "phrase", "ipa": "/dʒɑːn ˈeɪməs kəˈmiːniəs/", "vi": "nhà sư phạm Jan Amos Comenius"},
  {"id": "lex.en.200k.058789", "hw": "kauri gum", "pos": "phrase", "ipa": "/ˈkaʊri ɡʌm/", "vi": "nhựa hóa thạch cây kauri"},
  {"id": "lex.en.200k.058790", "hw": "kauri pine", "pos": "phrase", "ipa": "/ˈkaʊri paɪn/", "vi": "cây thông kauri cổ thụ"},
  {"id": "lex.en.200k.058791", "hw": "magnolia virginiana", "pos": "phrase", "ipa": "/mæɡˈnoʊliə vərˌdʒɪniˈeɪnə/", "vi": "cây hoa mộc lan Virginia"},
  {"id": "lex.en.200k.058792", "hw": "maned sheep", "pos": "phrase", "ipa": "/meɪnd ʃiːp/", "vi": "loài cừu bờm Bắc Phi"},
  {"id": "lex.en.200k.058793", "hw": "maned wolf", "pos": "phrase", "ipa": "/meɪnd wʊlf/", "vi": "loài sói bờm Nam Mỹ"},
  {"id": "lex.en.200k.058794", "hw": "martello tower", "pos": "phrase", "ipa": "/mɑːrˈtɛloʊ ˈtaʊər/", "vi": "tháp pháo phòng thủ Martello"},
  {"id": "lex.en.200k.058795", "hw": "maud gonne", "pos": "phrase", "ipa": "/mɔːd ɡɑːn/", "vi": "nhà hoạt động Maud Gonne"},
  {"id": "lex.en.200k.058796", "hw": "medical extern", "pos": "phrase", "ipa": "/ˈmɛdɪkəl ɛkˈstɜːrn/", "vi": "sinh viên y thực tập ngoại trú"},
  {"id": "lex.en.200k.058797", "hw": "nag hammadi", "pos": "phrase", "ipa": "/nɑːɡ hɑːˈmɑːdi/", "vi": "thị trấn cổ Nag Hammadi Ai Cập"},
  {"id": "lex.en.200k.058798", "hw": "nag hammadi library", "pos": "phrase", "ipa": "/nɑːɡ hɑːˈmɑːdi ˈlaɪbrəri/", "vi": "thư tịch cổ Nag Hammadi"},
  {"id": "lex.en.200k.058799", "hw": "negative chemotaxis", "pos": "phrase", "ipa": "/ˈnɛɡətɪv ˌkiːmoʊˈtæksɪs/", "vi": "hướng hóa âm; sự né tránh chất"},
  {"id": "lex.en.200k.058800", "hw": "niccolo paganini", "pos": "phrase", "ipa": "/ˌniːkəˈloʊ ˌpæɡəˈniːni/", "vi": "nghệ sĩ vĩ cầm Niccolò Paganini"},
  {"id": "lex.en.200k.058801", "hw": "nonsmoking car", "pos": "phrase", "ipa": "/nɑːnˈsmoʊkɪŋ kɑːr/", "vi": "toa xe cấm hút thuốc lá"}
]

with open('scratch/b32_r08_raw_p3.json') as f:
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

with open('scratch/b32_r08_p3.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

print("Part 3 validated and written successfully.")
