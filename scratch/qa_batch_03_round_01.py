import json

OVERRIDES_B03_R01 = {
    # 001-050
    "lex.en.100k.010002": {"vi": "dụng cụ làm nhẵn; máy chà nhám"},  # smoother
    "lex.en.100k.010003": {"pos": "verb", "vi": "ngâm nước; nhúng ướt sũng"},  # soak
    "lex.en.100k.010004": {"vi": "môn bóng quần (squash); bí ngồi"},  # squash
    "lex.en.100k.010006": {"vi": "mũi khâu; vết khâu phẫu thuật"},  # stitch
    "lex.en.100k.010011": {"vi": "sự cất cánh máy bay; trò nhại"},  # takeoff
    "lex.en.100k.010016": {"vi": "người dịch; biên dịch viên"},  # translator (fixed typo 'dịch gỉa')
    "lex.en.100k.010018": {"vi": "tầm thường; không đáng kể; nhỏ nhặt"},  # trivial
    "lex.en.100k.010021": {"vi": "không mong muốn; gây bất lợi"},  # undesirable
    "lex.en.100k.010023": {"vi": "không được ưa chuộng; ít phổ biến"},  # unpopular
    "lex.en.100k.010024": {"vi": "tình trạng bất ổn chính trị/xã hội"},  # unrest
    "lex.en.100k.010027": {"vi": "giấm ăn"},  # vinegar
    "lex.en.100k.010028": {"vi": "bị cong vênh; lệch lạc tư tưởng"},  # warped
    "lex.en.100k.010031": {"vi": "vụ cháy rừng; ngọn lửa lan nhanh"},  # wildfire (fixed 'chất cháy')
    "lex.en.100k.010032": {"vi": "hệ điều hành Windows; các cửa sổ"},  # windows
    "lex.en.100k.010034": {"pos": "num", "vi": "số một trăm (100)"},  # hundred
    "lex.en.100k.010035": {"vi": "tệ nạn; thói xấu; ê-tô kẹp"},  # vice
    "lex.en.100k.010037": {"vi": "lao động; nhân công; công đoàn"},  # labour
    "lex.en.100k.010039": {"vi": "các ngân hàng; bờ sông dốc"},  # banks (purged specific person Joseph Banks)
    "lex.en.100k.010041": {"vi": "sự tuân thủ nguyên tắc; bám dính"},  # adherence
    "lex.en.100k.010044": {"vi": "hãng máy bay Airbus; xe buýt bay"},  # airbus
    "lex.en.100k.010045": {"vi": "đáng kinh ngạc; tuyệt vời thay"},  # amazingly
    "lex.en.100k.010049": {"vi": "xấp xỉ; tương đối; gần đúng"},  # approximate (purged slang 'xêm xêm')
    "lex.en.100k.010051": {"vi": "lắp ráp linh kiện; tập hợp lại"},  # assemble

    # 051-100
    "lex.en.100k.010053": {"vi": "sự xác thực danh tính (IT)"},  # authentication
    "lex.en.100k.010056": {"vi": "rượu whisky Bourbon; triều Bourbon"},  # bourbon
    "lex.en.100k.010057": {"vi": "uốn cong; cúi đầu"},  # bowed
    "lex.en.100k.010058": {"vi": "lòng dũng cảm; sự can đảm"},  # bravery
    "lex.en.100k.010059": {"vi": "đài truyền hình; phát thanh viên"},  # broadcaster
    "lex.en.100k.010060": {"vi": "sự xem lướt; duyệt xem qua"},  # browse
    "lex.en.100k.010062": {"vi": "nhà một tầng kiểu bungalow"},  # bungalow
    "lex.en.100k.010064": {"vi": "tận dụng cơ hội; viết hoa"},  # capitalize
    "lex.en.100k.010065": {"vi": "đoàn lữ hành; xe nhà lưu động"},  # caravan
    "lex.en.100k.010070": {"vi": "hoàn cảnh; tình huống cụ thể"},  # circumstance
    "lex.en.100k.010071": {"vi": "tiếng vỗ tay; tiếng sét đánh"},  # clap
    "lex.en.100k.010072": {"vi": "sự nhận thức; khả năng tri nhận"},  # cognition
    "lex.en.100k.010074": {"vi": "quãng đường đi làm hàng ngày"},  # commute
    "lex.en.100k.010081": {"vi": "có dạng hình trụ tròn"},  # cylindrical
    "lex.en.100k.010085": {"vi": "làm gián đoạn; làm đảo lộn"},  # disrupt
    "lex.en.100k.010086": {"vi": "nhà phân phối hàng hóa; bộ chia"},  # distributor
    "lex.en.100k.010088": {"vi": "chú cún con; kiểu doggy"},  # doggy
    "lex.en.100k.010089": {"vi": "tiền trợ cấp thất nghiệp (dole)"},  # dole
    "lex.en.100k.010090": {"vi": "ký túc xá sinh viên"},  # dorm
    "lex.en.100k.010092": {"pos": "adj", "vi": "trùng lặp; giống hệt nhau"},  # duplicate
    "lex.en.100k.010095": {"vi": "phôi thai; mầm mống sơ khai"},  # embryo
    "lex.en.100k.010099": {"vi": "sự loại trừ; điều khoản loại trừ"},  # exclusion

    # 101-150
    "lex.en.100k.010104": {"vi": "mối tình thoảng qua; cú ném mạnh"},  # fling
    "lex.en.100k.010107": {"vi": "có thể thấy trước; dự đoán được"},  # foreseeable
    "lex.en.100k.010108": {"vi": "ghê gớm; đáng gờm; dữ dội"},  # formidable
    "lex.en.100k.010109": {"vi": "kẹo mềm fudge; né tránh sự thật"},  # fudge
    "lex.en.100k.010113": {"vi": "sự khuyết tật; thế bất lợi"},  # handicap
    "lex.en.100k.010115": {"vi": "Điện hạ; Hoàng thân"},  # highness
    "lex.en.100k.010118": {"vi": "sự chiếu sáng; sự soi sáng"},  # illumination (fixed 'bôi lên' error)
    "lex.en.100k.010120": {"vi": "không chính xác; sai lệch"},  # inaccurate
    "lex.en.100k.010127": {"vi": "truyền cảm hứng; đầy cảm hứng"},  # inspirational
    "lex.en.100k.010130": {"vi": "gây khó chịu; gây ngứa ngáy"},  # irritating
    "lex.en.100k.010134": {"vi": "con báo đốm (leopard)"},  # leopard
    "lex.en.100k.010136": {"vi": "xe limousine sang trọng"},  # limo
    "lex.en.100k.010138": {"vi": "đơn vị độ rọi lux (lx)"},  # lux
    "lex.en.100k.010139": {"vi": "cây chùy gai; bình xịt hơi cay"},  # mace (fixed wrong 'hạt macca')
    "lex.en.100k.010140": {"vi": "bờm sư tử; bờm ngựa"},  # mane
    "lex.en.100k.010141": {"vi": "quả xoài; trái xoài"},  # mango
    "lex.en.100k.010143": {"vi": "nghề xay xát; sự phay cơ khí"},  # milling
    "lex.en.100k.010146": {"vi": "ánh trăng; làm việc ngoài giờ"},  # moonlight
    "lex.en.100k.010150": {"vi": "xúc phạm; làm mếch lòng"},  # offend
    "lex.en.100k.010152": {"vi": "nghịch lý; điều trớ trêu"},  # paradox
    "lex.en.100k.010153": {"vi": "phòng tiếp khách; tiệm dịch vụ"},  # parlor
    "lex.en.100k.010154": {"vi": "vỉa hè; lối đi bộ lát gạch"},  # pavement

    # 151-200
    "lex.en.100k.010155": {"pos": "noun", "vi": "quả mận; vị trí béo bở"},  # plum
    "lex.en.100k.010158": {"vi": "đắt đỏ; giá cao"},  # pricey
    "lex.en.100k.010161": {"vi": "giẻ lau; tờ báo lá cải"},  # rag
    "lex.en.100k.010166": {"vi": "dư thừa; nhân viên dôi dư"},  # redundant
    "lex.en.100k.010171": {"vi": "xương sườn; gọng sườn"},  # rib
    "lex.en.100k.010175": {"vi": "nước sốt salsa; điệu nhảy salsa"},  # salsa
    "lex.en.100k.010176": {"vi": "xe tay ga; xe trượt scooter"},  # scooter
    "lex.en.100k.010177": {"vi": "xứ Scotland"},  # scotland
    "lex.en.100k.010178": {"vi": "nhà điêu khắc; nghệ nhân tạc"},  # sculptor
    "lex.en.100k.010186": {"vi": "số lượng lớn; hàng loạt"},  # slew
    "lex.en.100k.010191": {"vi": "ghế đẩu; phân thải (y tế)"},  # stool
    "lex.en.100k.010192": {"pos": "noun", "vi": "eo biển; tình thế khó khăn"},  # strait
    "lex.en.100k.010194": {"vi": "đề cương môn học; giáo trình"},  # syllabus
    "lex.en.100k.010197": {"vi": "con cóc"},  # toad

    # 201-250
    "lex.en.100k.010202": {"vi": "sự đánh giá quá thấp; ước tính ít"},  # underestimate
    "lex.en.100k.010206": {"vi": "sự thống nhất; sự hợp nhất"},  # unification
    "lex.en.100k.010208": {"vi": "vùng phía bắc bang; ngoại ô xa"},  # upstate
    "lex.en.100k.010212": {"vi": "quả óc chó; hạt óc chó; gỗ óc chó"},  # walnut
    "lex.en.100k.010218": {"vi": "bấc đèn; tim nến"},  # wick
    "lex.en.100k.010222": {"vi": "ngon miệng; ngon tuyệt"},  # yummy
    "lex.en.100k.010224": {"vi": "bang California (CA); viết tắt Ca"},  # ca
    "lex.en.100k.010227": {"vi": "họ Williams; tên riêng Williams"},  # williams
    "lex.en.100k.010234": {"vi": "họ Taylor; tên riêng Taylor"},  # taylor
    "lex.en.100k.010235": {"pos": "num", "vi": "số hai mươi (20)"},  # twenty
    "lex.en.100k.010239": {"vi": "sự cáo buộc; lời buộc tội"},  # accusation
    "lex.en.100k.010242": {"vi": "mơ hồ; nhập nhằng; đa nghĩa"},  # ambiguous
    "lex.en.100k.010246": {"vi": "tảng băng trôi (iceberg)"},  # berg
    "lex.en.100k.010251": {"pos": "verb", "vi": "khoe khoang; khoác lác"},  # brag
    "lex.en.100k.010254": {"pos": "noun", "vi": "xe đẩy em bé; lỗi phần mềm (IT)"},  # buggy
    "lex.en.100k.010255": {"vi": "khu khởi động ném bóng chày"},  # bullpen
    "lex.en.100k.010256": {"vi": "bộ máy quan liêu; chế độ quan liêu"},  # bureaucracy
    "lex.en.100k.010258": {"vi": "thuộc loài chó; răng nanh"},  # canine
    "lex.en.100k.010261": {"vi": "bắt tai; lôi cuốn; dễ nhớ"},  # catchy
    "lex.en.100k.010264": {"vi": "hóa trị liệu ung thư"},  # chemotherapy
    "lex.en.100k.010267": {"vi": "tiện nghi sinh hoạt; sự an ủi"},  # comforts
    "lex.en.100k.010269": {"vi": "thừa nhận thua cuộc; nhượng bộ"},  # concede
    "lex.en.100k.010273": {"vi": "tàu hộ tống nhỏ; xe Corvette"},  # corvette
    "lex.en.100k.010278": {"vi": "thoái hóa; suy đồi; biến chất"},  # degenerate
    "lex.en.100k.010280": {"vi": "hạ xuống; đi xuống; bắt nguồn từ"},  # descend
    "lex.en.100k.010284": {"vi": "khung cửa ra vào; ngưỡng cửa"},  # doorway
    "lex.en.100k.010286": {"vi": "sự sụp đổ quyền lực; sự suy vong"},  # downfall
    "lex.en.100k.010291": {"vi": "trang bị dụng cụ; cung cấp thiết bị"},  # equip
    "lex.en.100k.010294": {"vi": "sơ tán; di tản; rút khẩn cấp"},  # evacuate
    "lex.en.100k.010295": {"vi": "điếu thuốc lá (Anh); việc vất vả"},  # fag
    "lex.en.100k.010299": {"pos": "noun", "vi": "nắp đậy; cánh tà; sự bối rối"},  # flap

    # 301-350
    "lex.en.100k.010306": {"vi": "cuộc trốn chạy; kỳ nghỉ ngắn ngày"},  # getaway
    "lex.en.100k.010307": {"vi": "quà tặng miễn phí; điều sơ hở"},  # giveaway
    "lex.en.100k.010314": {"vi": "đau lòng; xé lòng; đau đớn"},  # heartbreaking
    "lex.en.100k.010318": {"vi": "sự yên ắng; sự tĩnh lặng"},  # hush
    "lex.en.100k.010323": {"vi": "thừa kế; thừa hưởng tài sản"},  # inherit
    "lex.en.100k.010324": {"vi": "bẩm sinh; thiên bẩm"},  # innate
    "lex.en.100k.010331": {"vi": "dây dắt thú cưng; sự kiểm soát"},  # leash (purged 'số ba')
    "lex.en.100k.010336": {"vi": "sang trọng; xa hoa; lộng lẫy"},  # luxurious
    "lex.en.100k.010337": {"vi": "ác tính (u/bệnh); hiểm độc"},  # malignant
    "lex.en.100k.010338": {"vi": "mẹ; má; tuyến vú"},  # mamma
    "lex.en.100k.010339": {"vi": "chuốt mi mắt (mascara)"},  # mascara
    "lex.en.100k.010340": {"vi": "bệnh sởi"},  # measles
    "lex.en.100k.010342": {"vi": "nhu mì; ngoan ngoãn; cam chịu"},  # meek
    "lex.en.100k.010348": {"vi": "nghệ thuật dựng phim; tranh ghép"},  # montage
    "lex.en.100k.010352": {"vi": "sự vâng lời; sự tuân lệnh"},  # obedience
    "lex.en.100k.010353": {"vi": "tối ưu hóa; tinh chỉnh hiệu năng"},  # optimize (purged 'lạc quan')
    "lex.en.100k.010355": {"vi": "người ngoài cuộc; kẻ lép vế"},  # outsider
    "lex.en.100k.010357": {"vi": "điểm ngắm cảnh trên cao; bỏ qua"},  # overlook
    "lex.en.100k.010358": {"vi": "con bò đực thiến"},  # ox
    "lex.en.100k.010362": {"vi": "bàn chân động vật có móng vuốt"},  # paw
    "lex.en.100k.010365": {"vi": "kiên trì; cố chấp; tiếp tục có"},  # persist
    "lex.en.100k.010368": {"vi": "sự phát lại (âm thanh/video)"},  # playback
    "lex.en.100k.010373": {"vi": "lập trình viên máy tính"},  # programmer
    "lex.en.100k.010374": {"vi": "ngăn cấm; cấm đoán bằng luật"},  # prohibit
    "lex.en.100k.010382": {"vi": "sự chế nhạo; lời giễu cợt"},  # ridicule
    "lex.en.100k.010385": {"vi": "hệ thống vệ sinh dịch tễ"},  # sanitation
    "lex.en.100k.010387": {"vi": "sự phân biệt đối xử giới tính"},  # sexism
    "lex.en.100k.010389": {"vi": "đơn vị đo độ dẫn điện siemens"},  # siemens
    "lex.en.100k.010391": {"vi": "cái xẻng xúc đất; quân bích"},  # spade (purged wrong 'xuồng')
    "lex.en.100k.010394": {"vi": "thuốc xtê-rô-ít (steroid)"},  # steroid
    "lex.en.100k.010397": {"vi": "khu quy hoạch dân cư; phân khu"},  # subdivision

    # 401-500
    "lex.en.100k.010404": {"vi": "bệnh lao phổi; bệnh lao"},  # tuberculosis
    "lex.en.100k.010409": {"pos": "noun", "vi": "người hướng dẫn chỗ ngồi"},  # usher
    "lex.en.100k.010410": {"vi": "sự rung động; dao động rung"},  # vibration
    "lex.en.100k.010415": {"pos": "noun", "vi": "mối hàn; sự hàn kim loại"},  # weld
    "lex.en.100k.010418": {"pos": "num", "vi": "số một nghìn (1.000)"},  # thousand
    "lex.en.100k.010419": {"ipa": "/θriː/"},  # iii
    "lex.en.100k.010421": {"vi": "tên riêng Daniel; tiên tri Daniel"},  # daniel
    "lex.en.100k.010428": {"vi": "khả năng tiếp cận; trợ năng (IT)"},  # accessibility
    "lex.en.100k.010432": {"vi": "lời cáo buộc; sự quy kết"},  # allegation
    "lex.en.100k.010433": {"vi": "cá sấu mõm ngắn Mỹ (alligator)"},  # alligator
    "lex.en.100k.010437": {"vi": "thơm ngát; có mùi thơm dễ chịu"},  # aromatic
    "lex.en.100k.010441": {"vi": "bản nhạc ballad trữ tình"},  # ballad
    "lex.en.100k.010442": {"vi": "ngạnh sắt; lời châm chọc sâu cay"},  # barb
    "lex.en.100k.010445": {"vi": "thống đốc thời Ottoman (Bey)"},  # bey
    "lex.en.100k.010446": {"vi": "bìa còng kẹp tài liệu; chất dính"},  # binder
    "lex.en.100k.010447": {"vi": "sinh thiết mô tế bào (y khoa)"},  # biopsy
    "lex.en.100k.010448": {"vi": "chứng mù lòa; sự mù quáng"},  # blindness
    "lex.en.100k.010457": {"vi": "vụng về; lóng ngóng"},  # clumsy
    "lex.en.100k.010458": {"vi": "trùng hợp; xảy ra cùng lúc"},  # coincide
    "lex.en.100k.010462": {"vi": "khả năng thấu hiểu; sự lĩnh hội"},  # comprehension
    "lex.en.100k.010465": {"vi": "ngược lại; điều tương phản"},  # converse
    "lex.en.100k.010468": {"vi": "con cá sấu"},  # crocodile (fixed single character 'sấu')
    "lex.en.100k.010471": {"vi": "dày đặc; đông đúc (mật độ)"},  # densely
    "lex.en.100k.010472": {"vi": "sự tuyệt vọng; nỗi cùng quẫn"},  # desperation
    "lex.en.100k.010474": {"vi": "ngắt kết nối; bất đồng nhận thức"},  # disconnect
    "lex.en.100k.010475": {"pos": "verb", "vi": "phân biệt đối xử; kỳ thị"},  # discriminate
    "lex.en.100k.010479": {"vi": "sự chuyển hướng; yếu tố phân tâm"},  # diversion
    "lex.en.100k.010483": {"vi": "tiếng reo Eureka (tìm ra rồi!)"},  # eureka
    "lex.en.100k.010484": {"vi": "giám đốc điều hành (executive)"},  # exec
    "lex.en.100k.010485": {"vi": "tình trạng kiệt sức; sự cạn kiệt"},  # exhaustion
    "lex.en.100k.010488": {"vi": "các cánh đồng; lĩnh vực hoạt động"},  # fields
    "lex.en.100k.010490": {"vi": "sự rèn đúc; hành vi làm giả mạo"},  # forging
    "lex.en.100k.010492": {"vi": "người làm vườn; thợ làm vườn"},  # gardener
    "lex.en.100k.010493": {"vi": "sự u ám; cảnh tối tăm buồn bã"},  # gloom
    "lex.en.100k.010494": {"vi": "máy xay cà phê; máy mài góc"},  # grinder
    "lex.en.100k.010497": {"vi": "viết bằng tay; chữ viết tay"},  # handwritten
    "lex.en.100k.010499": {"vi": "cây gai dầu (lấy sợi/dầu)"},  # hemp
}

# Verify lengths <= 35
for k, v in OVERRIDES_B03_R01.items():
    if "vi" in v:
        assert len(v["vi"]) <= 35, f"Length > 35 for {k}: {v['vi']} ({len(v['vi'])})"

with open('content/english/qa-batches/batch-03.json', 'r', encoding='utf-8') as f:
    batch_data = json.load(f)

records = batch_data['records']
target_records = records[0:500]

applied_count = 0
for r in target_records:
    rid = r['id']
    if rid in OVERRIDES_B03_R01:
        for k, v in OVERRIDES_B03_R01[rid].items():
            r[k] = v
        applied_count += 1
    assert len(r['vi']) <= 35, f"Target record length > 35: {rid} {r['vi']}"

# Update reviewedCount for Batch 03 to 500 (Round 1 completed)
batch_data['reviewedCount'] = 500
batch_data['status'] = 'in_progress'

with open('content/english/qa-batches/batch-03.json', 'w', encoding='utf-8') as f:
    json.dump(batch_data, f, ensure_ascii=False, indent=2)

print(f"Successfully applied Batch 03 Round 1 ({applied_count} overrides). Reviewed: 500/5000.")
