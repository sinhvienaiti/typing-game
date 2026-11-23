import json

items = [
  {"id": "lex.en.200k.063103", "hw": "boardinghouses", "pos": "noun", "ipa": "/ˈbɔːrdɪŋˌhaʊzɪz/", "vi": "nhà trọ bình dân kèm ăn uống"},
  {"id": "lex.en.200k.063104", "hw": "bobtails", "pos": "noun", "ipa": "/ˈbɑːbteɪlz/", "vi": "động vật đuôi cụt; mèo giống cộc"},
  {"id": "lex.en.200k.063105", "hw": "bookmobiles", "pos": "noun", "ipa": "/ˈbʊkmoʊˌbiːlz/", "vi": "xe thư viện lưu động đến vùng xa"},
  {"id": "lex.en.200k.063106", "hw": "borages", "pos": "noun", "ipa": "/ˈbɔːrɪdʒɪz/", "vi": "cây thảo dược hoa xanh lưu ly"},
  {"id": "lex.en.200k.063107", "hw": "bowstrings", "pos": "noun", "ipa": "/ˈboʊstrɪŋz/", "vi": "dây cung căng bắn tên"},
  {"id": "lex.en.200k.063108", "hw": "busloads", "pos": "noun", "ipa": "/ˈbʌsloʊdz/", "vi": "lượng khách chở đầy một xe buýt"},
  {"id": "lex.en.200k.063109", "hw": "bustards", "pos": "noun", "ipa": "/ˈbʌstərdz/", "vi": "chim ô tác chân cao sống đồng cỏ"},
  {"id": "lex.en.200k.063110", "hw": "calumnies", "pos": "noun", "ipa": "/ˈkæləmniz/", "vi": "lời vu khống bôi nhọ danh dự"},
  {"id": "lex.en.200k.063111", "hw": "casalses", "pos": "noun", "ipa": "/kəˈsɑːlzɪz/", "vi": "nghệ sĩ đàn cello Pablo Casals"},
  {"id": "lex.en.200k.063112", "hw": "catenaries", "pos": "noun", "ipa": "/kəˈtɛnəriz/", "vi": "đường cong dây xích võng tự nhiên"},
  {"id": "lex.en.200k.063113", "hw": "chancier", "pos": "adj", "ipa": "/ˈtʃænsiər/", "vi": "may rủi mạo hiểm bấp bênh hơn"},
  {"id": "lex.en.200k.063114", "hw": "chanciest", "pos": "adj", "ipa": "/ˈtʃænsiɪst/", "vi": "may rủi mạo hiểm bấp bênh nhất"},
  {"id": "lex.en.200k.063115", "hw": "choroids", "pos": "noun", "ipa": "/ˈkɔːrɔɪdz/", "vi": "lớp màng mạch giàu máu trong mắt"},
  {"id": "lex.en.200k.063116", "hw": "conjunctives", "pos": "noun", "ipa": "/kənˈdʒʌŋktɪvz/", "vi": "liên từ nối câu trong ngữ pháp"},
  {"id": "lex.en.200k.063117", "hw": "craniotomies", "pos": "noun", "ipa": "/ˌkreɪniˈɑːtəmiz/", "vi": "phẫu thuật mở hộp sọ não y khoa"},
  {"id": "lex.en.200k.063118", "hw": "cygnets", "pos": "noun", "ipa": "/ˈsɪɡnɪts/", "vi": "chim thiên nga con mới nở"},
  {"id": "lex.en.200k.063119", "hw": "dagoes", "pos": "noun", "ipa": "/ˈdeɪɡoʊz/", "vi": "từ cũ chỉ người gốc Ý (miệt thị)"},
  {"id": "lex.en.200k.063120", "hw": "dagos", "pos": "noun", "ipa": "/ˈdeɪɡoʊz/", "vi": "từ cũ chỉ người gốc Ý (miệt thị)"},
  {"id": "lex.en.200k.063121", "hw": "dartboards", "pos": "noun", "ipa": "/ˈdɑːrtbɔːrdz/", "vi": "bảng bia tròn chơi ném phi tiêu"},
  {"id": "lex.en.200k.063122", "hw": "decoupages", "pos": "noun", "ipa": "/ˌdeɪkuːˈpɑːʒɪz/", "vi": "nghệ thuật trang trí cắt dán giấy"},
  {"id": "lex.en.200k.063123", "hw": "delormes", "pos": "noun", "ipa": "/dəˈlɔːrmz/", "vi": "kiến trúc sư Pháp Philibert Delorme"},
  {"id": "lex.en.200k.063124", "hw": "dingbats", "pos": "noun", "ipa": "/ˈdɪŋbæts/", "vi": "người khờ ngốc; ký tự biểu tượng"},
  {"id": "lex.en.200k.063125", "hw": "downshifts", "pos": "noun", "ipa": "/ˈdaʊnʃɪfts/", "vi": "sự về số thấp xe; sống chậm lại"},
  {"id": "lex.en.200k.063126", "hw": "ebonicses", "pos": "noun", "ipa": "/ɪˈbɑːnɪksɪz/", "vi": "tiếng Anh bản địa người Mỹ gốc Phi"},
  {"id": "lex.en.200k.063127", "hw": "ectoderms", "pos": "noun", "ipa": "/ˈɛktədɜːrmz/", "vi": "lớp ngoại bì phôi sinh da thần kinh"},
  {"id": "lex.en.200k.063128", "hw": "endosperms", "pos": "noun", "ipa": "/ˈɛndəspɜːrmz/", "vi": "mô nội nhũ nuôi dưỡng phôi hạt cây"},
  {"id": "lex.en.200k.063129", "hw": "enteroviruses", "pos": "noun", "ipa": "/ˌɛntəroʊˈvaɪrəsɪz/", "vi": "nhóm virus đường ruột enterovirus"},
  {"id": "lex.en.200k.063130", "hw": "exploiters", "pos": "noun", "ipa": "/ɪkˈsplɔɪtərz/", "vi": "kẻ bóc lột trục lợi sức lao động"},
  {"id": "lex.en.200k.063131", "hw": "eyefuls", "pos": "noun", "ipa": "/ˈaɪfʊlz/", "vi": "cảnh đẹp hút mắt; người quyến rũ"},
  {"id": "lex.en.200k.063132", "hw": "filched", "pos": "verb", "ipa": "/fɪltʃt/", "vi": "đã ăn cắp vặt; đã chôm đồ nhỏ"},
  {"id": "lex.en.200k.063133", "hw": "filches", "pos": "verb", "ipa": "/ˈfɪltʃɪz/", "vi": "ăn cắp vặt; lén lấy trộm đồ nhỏ"},
  {"id": "lex.en.200k.063134", "hw": "flautists", "pos": "noun", "ipa": "/ˈflɔːtɪsts/", "vi": "nghệ sĩ chuyên thổi sáo flute"},
  {"id": "lex.en.200k.063135", "hw": "fratricides", "pos": "noun", "ipa": "/ˈfrætrəsaɪdz/", "vi": "tội giết anh chị em ruột thịt"},
  {"id": "lex.en.200k.063136", "hw": "gipped", "pos": "verb", "ipa": "/dʒɪpt/", "vi": "đã lừa gạt tiền; đã bịp bợm (lóng)"},
  {"id": "lex.en.200k.063137", "hw": "gipping", "pos": "verb", "ipa": "/ˈdʒɪpɪŋ/", "vi": "đang lừa gạt bịp bợm tiền của"},
  {"id": "lex.en.200k.063138", "hw": "gips", "pos": "noun", "ipa": "/dʒɪps/", "vi": "trò lừa bịp gian lận; chứng gút gà"},
  {"id": "lex.en.200k.063139", "hw": "histocompatibilities", "pos": "noun", "ipa": "/ˌhɪstoʊkəmˌpætəˈbɪlətiz/", "vi": "tính tương hợp mô trong ghép tạng"},
  {"id": "lex.en.200k.063140", "hw": "humperdincks", "pos": "noun", "ipa": "/ˈhʊmpərdɪŋks/", "vi": "nhà soạn nhạc Đức Humperdinck"},
  {"id": "lex.en.200k.063141", "hw": "hypoglycaemias", "pos": "noun", "ipa": "/ˌhaɪpoʊɡlaɪˈsiːmiəz/", "vi": "tình trạng hạ đường huyết (Anh)"},
  {"id": "lex.en.200k.063142", "hw": "intensifiers", "pos": "noun", "ipa": "/ɪnˈtɛnsəˌfaɪərz/", "vi": "phó từ nhấn mạnh mức độ tính từ"},
  {"id": "lex.en.200k.063143", "hw": "irrelevancies", "pos": "noun", "ipa": "/ɪˈrɛləvənsiz/", "vi": "điều thừa thãi không liên quan"},
  {"id": "lex.en.200k.063144", "hw": "isoniazids", "pos": "noun", "ipa": "/ˌaɪsəˈnaɪəzɪdz/", "vi": "thuốc kháng sinh trị lao isoniazid"},
  {"id": "lex.en.200k.063145", "hw": "isotherms", "pos": "noun", "ipa": "/ˈaɪsəθɜːrmz/", "vi": "đường đẳng nhiệt trên bản đồ"},
  {"id": "lex.en.200k.063146", "hw": "jewesses", "pos": "noun", "ipa": "/ˈdʒuːəsɪz/", "vi": "phụ nữ Do Thái (từ cổ ít dùng)"},
  {"id": "lex.en.200k.063147", "hw": "kentuckians", "pos": "noun", "ipa": "/kənˈtʌkiənz/", "vi": "người dân bản địa bang Kentucky"},
  {"id": "lex.en.200k.063148", "hw": "khabarovsks", "pos": "noun", "ipa": "/xəˈbɑːrəfsks/", "vi": "thành phố Khabarovsk nước Nga"},
  {"id": "lex.en.200k.063149", "hw": "khis", "pos": "noun", "ipa": "/kaɪz/", "vi": "chữ cái Hy Lạp Chi (biến âm Khi)"},
  {"id": "lex.en.200k.063150", "hw": "kshatriyas", "pos": "noun", "ipa": "/kʃəˈtriːjəz/", "vi": "giai cấp võ sĩ quý tộc Ấn Độ"},
  {"id": "lex.en.200k.063151", "hw": "ladins", "pos": "noun", "ipa": "/ləˈdiːnz/", "vi": "tiếng Ladin vùng núi An-pơ Ý"},
  {"id": "lex.en.200k.063152", "hw": "laggards", "pos": "noun", "ipa": "/ˈlæɡərdz/", "vi": "kẻ chậm chân tụt hậu so với nhóm"},
  {"id": "lex.en.200k.063153", "hw": "lanker", "pos": "adj", "ipa": "/ˈlæŋkər/", "vi": "cao gầy hơn; thẳng rũ mượt hơn"},
  {"id": "lex.en.200k.063154", "hw": "lankest", "pos": "adj", "ipa": "/ˈlæŋkɪst/", "vi": "cao gầy nhất; thẳng rũ mượt nhất"},
  {"id": "lex.en.200k.063155", "hw": "mammalias", "pos": "noun", "ipa": "/məˈmeɪliəz/", "vi": "lớp động vật có vú Mammalia"},
  {"id": "lex.en.200k.063156", "hw": "mancunians", "pos": "noun", "ipa": "/mæŋˈkjuːniənz/", "vi": "người dân thành phố Manchester Anh"},
  {"id": "lex.en.200k.063157", "hw": "manicurists", "pos": "noun", "ipa": "/ˈmænɪˌkjʊrɪsts/", "vi": "thợ cắt tỉa sơn sửa móng tay"},
  {"id": "lex.en.200k.063158", "hw": "masonites", "pos": "noun", "ipa": "/ˈmeɪsəˌnaɪts/", "vi": "tấm ván gỗ ép sợi cứng Masonite"},
  {"id": "lex.en.200k.063159", "hw": "mauldins", "pos": "noun", "ipa": "/ˈmɔːldɪnz/", "vi": "họa sĩ biếm họa Mỹ Bill Mauldin"},
  {"id": "lex.en.200k.063160", "hw": "menanders", "pos": "noun", "ipa": "/mɪˈnændərz/", "vi": "nhà soạn hài kịch Hy Lạp Menander"},
  {"id": "lex.en.200k.063161", "hw": "microfloras", "pos": "noun", "ipa": "/ˌmaɪkroʊˈflɔːrəz/", "vi": "hệ vi sinh vật cộng sinh đường ruột"},
  {"id": "lex.en.200k.063162", "hw": "naifs", "pos": "noun", "ipa": "/naɪˈiːfs/", "vi": "người ngây thơ thật thà cả tin"},
  {"id": "lex.en.200k.063163", "hw": "neonates", "pos": "noun", "ipa": "/ˈniːəneɪts/", "vi": "trẻ sơ sinh dưới một tháng tuổi"},
  {"id": "lex.en.200k.063164", "hw": "nitroglycerines", "pos": "noun", "ipa": "/ˌnaɪtroʊˈɡlɪsərɪnz/", "vi": "chất nổ mạnh; thuốc giãn mạch tim"},
  {"id": "lex.en.200k.063165", "hw": "oblations", "pos": "noun", "ipa": "/əˈbleɪʃənz/", "vi": "lễ vật dâng hiến lên thần linh"},
  {"id": "lex.en.200k.063166", "hw": "orangeries", "pos": "noun", "ipa": "/ˈɔːrɪndʒəriz/", "vi": "nhà kính trồng cam chanh mùa đông"},
  {"id": "lex.en.200k.063167", "hw": "outmaneuvered", "pos": "verb", "ipa": "/ˌaʊtməˈnuːvərd/", "vi": "đã khéo léo vượt mặt giành ưu thế"},
  {"id": "lex.en.200k.063168", "hw": "outmaneuvering", "pos": "verb", "ipa": "/ˌaʊtməˈnuːvərɪŋ/", "vi": "đang dùng mưu lược giành thế thắng"},
  {"id": "lex.en.200k.063169", "hw": "outmaneuvers", "pos": "verb", "ipa": "/ˌaʊtməˈnuːvərz/", "vi": "vượt mặt bằng mưu lược khéo léo"},
  {"id": "lex.en.200k.063170", "hw": "pantheras", "pos": "noun", "ipa": "/pænˈθɛrəz/", "vi": "chi mèo lớn sư tử hổ báo Panthera"},
  {"id": "lex.en.200k.063171", "hw": "perfectives", "pos": "noun", "ipa": "/pərˈfɛktɪvz/", "vi": "thể hoàn thành trong ngữ pháp"},
  {"id": "lex.en.200k.063172", "hw": "photochemistries", "pos": "noun", "ipa": "/ˌfoʊtoʊˈkɛmɪstriz/", "vi": "ngành quang hóa học phản ứng sáng"},
  {"id": "lex.en.200k.063173", "hw": "polycarps", "pos": "noun", "ipa": "/ˈpɑːlɪkɑːrps/", "vi": "cây sinh sản nhiều mùa; thánh đồ"},
  {"id": "lex.en.200k.063174", "hw": "prokhorovs", "pos": "noun", "ipa": "/prəˈkɔːrəfs/", "vi": "nhà vật lý laser Nobel Prokhorov"},
  {"id": "lex.en.200k.063175", "hw": "proteinases", "pos": "noun", "ipa": "/ˈproʊtiːˌneɪsɪz/", "vi": "enzym phân giải chuỗi protein"},
  {"id": "lex.en.200k.063176", "hw": "ptahs", "pos": "noun", "ipa": "/ptɑːz/", "vi": "thần sáng tạo Memphis Ai Cập Ptah"},
  {"id": "lex.en.200k.063177", "hw": "pythiases", "pos": "noun", "ipa": "/ˈpɪθiəsɪz/", "vi": "nữ tiên tri đền Delphi Pythia"},
  {"id": "lex.en.200k.063178", "hw": "quahogs", "pos": "noun", "ipa": "/ˈkoʊhɑːɡz/", "vi": "nghêu vỏ dày Đại Tây Dương quahog"},
  {"id": "lex.en.200k.063179", "hw": "reasoners", "pos": "noun", "ipa": "/ˈriːzənərz/", "vi": "người suy luận logic sắc bén"},
  {"id": "lex.en.200k.063180", "hw": "reburials", "pos": "noun", "ipa": "/riːˈbɛriəlz/", "vi": "lễ cải táng chôn cất lại hài cốt"},
  {"id": "lex.en.200k.063181", "hw": "roseaus", "pos": "noun", "ipa": "/roʊˈzoʊz/", "vi": "thủ đô Roseau đảo Dominica"},
  {"id": "lex.en.200k.063182", "hw": "salonicas", "pos": "noun", "ipa": "/səˈlɑːnɪkəz/", "vi": "thành phố Thessaloniki của Hy Lạp"},
  {"id": "lex.en.200k.063183", "hw": "schumpeters", "pos": "noun", "ipa": "/ˈʃʊmpeɪtərz/", "vi": "nhà kinh tế học Joseph Schumpeter"},
  {"id": "lex.en.200k.063184", "hw": "seminarians", "pos": "noun", "ipa": "/ˌsɛməˈnɛriənz/", "vi": "chủng sinh đang học tại chủng viện"},
  {"id": "lex.en.200k.063185", "hw": "shipwrights", "pos": "noun", "ipa": "/ˈʃɪpraɪts/", "vi": "thợ đóng mới và sửa chữa tàu thuyền"},
  {"id": "lex.en.200k.063186", "hw": "sixpacks", "pos": "noun", "ipa": "/ˈsɪkspæks/", "vi": "lốc sáu lon nước; cơ bụng sáu múi"},
  {"id": "lex.en.200k.063187", "hw": "smallholdings", "pos": "noun", "ipa": "/ˈsmɔːlˌhoʊldɪŋz/", "vi": "trang trại tiểu nông quy mô hộ nhỏ"},
  {"id": "lex.en.200k.063188", "hw": "soissonses", "pos": "noun", "ipa": "/swɑːˈsɑːnz/", "vi": "thành phố cổ Soissons nước Pháp"},
  {"id": "lex.en.200k.063189", "hw": "sojas", "pos": "noun", "ipa": "/ˈsɔɪəz/", "vi": "cây đậu nành tương; nước tương đậu"},
  {"id": "lex.en.200k.063190", "hw": "squabs", "pos": "noun", "ipa": "/skwɑːbz/", "vi": "bồ câu non ra ràng; đệm ghế êm"},
  {"id": "lex.en.200k.063191", "hw": "straightedges", "pos": "noun", "ipa": "/ˈstreɪtˌɛdʒɪz/", "vi": "thước thẳng không chia vạch kẻ nét"},
  {"id": "lex.en.200k.063192", "hw": "sverdrups", "pos": "noun", "ipa": "/ˈsvɜːrdrəps/", "vi": "đơn vị lưu lượng hải lưu sverdrup"},
  {"id": "lex.en.200k.063193", "hw": "tatus", "pos": "noun", "ipa": "/ˈtɑːtuːz/", "vi": "thú có mai chín đai châu Mỹ (tatu)"},
  {"id": "lex.en.200k.063194", "hw": "thiopentals", "pos": "noun", "ipa": "/ˌθaɪoʊˈpɛntəlz/", "vi": "thuốc gây mê tĩnh mạch thiopental"},
  {"id": "lex.en.200k.063195", "hw": "tibialises", "pos": "noun", "ipa": "/ˌtɪbiˈeɪlɪsɪz/", "vi": "cơ chày vùng cẳng chân (giải phẫu)"},
  {"id": "lex.en.200k.063196", "hw": "tilliches", "pos": "noun", "ipa": "/ˈtɪlɪkɪz/", "vi": "nhà thần học Đức Mỹ Paul Tillich"},
  {"id": "lex.en.200k.063197", "hw": "topknots", "pos": "noun", "ipa": "/ˈtɑːpnɑːts/", "vi": "búi tóc trên đỉnh; chùm mào chim"},
  {"id": "lex.en.200k.063198", "hw": "trackballs", "pos": "noun", "ipa": "/ˈtrækbɔːlz/", "vi": "chuột bi xoay điều khiển con trỏ"},
  {"id": "lex.en.200k.063199", "hw": "trifoliums", "pos": "noun", "ipa": "/traɪˈfoʊliəmz/", "vi": "cây cỏ ba lá thuộc chi Trifolium"},
  {"id": "lex.en.200k.063200", "hw": "tweedled", "pos": "verb", "ipa": "/ˈtwiːdəld/", "vi": "đã hót líu lo; đã ngân nga nhẹ"},
  {"id": "lex.en.200k.063201", "hw": "tweedles", "pos": "verb", "ipa": "/ˈtwiːdəlz/", "vi": "hót líu lo; ngân nga sáo du dương"},
  {"id": "lex.en.200k.063202", "hw": "tweedling", "pos": "verb", "ipa": "/ˈtwiːdəlɪŋ/", "vi": "đang hót líu lo; đang chơi sáo nhẹ"}
]

with open('scratch/b33_r07_raw_p2.json') as f:
    raw = json.load(f)

assert len(items) == 100
assert len(raw) == 100

for i, (item, r) in enumerate(zip(items, raw)):
    assert item['id'] == r['id'], f"Mismatch id at {i}: {item['id']} vs {r['id']}"
    assert item['hw'] == r['hw'], f"Mismatch hw at {i}: {item['hw']} vs {r['hw']}"
    assert len(item['vi']) <= 35, f"vi length > 35 at {i} ({item['hw']}): {len(item['vi'])}"
    assert item['pos'] in ['noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'], f"Invalid pos at {i}: {item['pos']}"
    assert item['ipa'].startswith('/') and item['ipa'].endswith('/') and item['ipa'].count('/') == 2, f"Invalid ipa at {i}: {item['ipa']}"
    assert not item['ipa'][1:-1].startswith(' ') and not item['ipa'][1:-1].endswith(' '), f"Space in ipa at {i}: {item['ipa']}"
    r['pos'] = item['pos']
    r['ipa'] = item['ipa']
    r['vi'] = item['vi']
    r['status'] = 'reviewed'

with open('scratch/b33_r07_p2.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)
print("Saved scratch/b33_r07_p2.json OK")
