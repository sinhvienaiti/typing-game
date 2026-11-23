import json

OVERRIDES_ROUND_08 = {
    # 3501-3550
    "lex.en.100k.008504": {"vi": "đòi hỏi cao; nặng nhọc; mệt mỏi"},  # taxing
    "lex.en.100k.008508": {"vi": "thân trên; phần thân người"},  # torso
    "lex.en.100k.008509": {"vi": "độc hại; có độc; tiêu cực"},  # toxic
    "lex.en.100k.008510": {"vi": "đoạn giới thiệu phim; rơ-moóc xe"},  # trailer
    "lex.en.100k.008514": {"vi": "đường hầm"},  # tunnel
    "lex.en.100k.008516": {"pos": "verb", "vi": "cởi quần áo; cởi đồ"},  # undress
    "lex.en.100k.008517": {"vi": "phổ quát; toàn cầu; phổ biến"},  # universal (trimmed <=35)
    "lex.en.100k.008520": {"pos": "noun", "vi": "tiện ích; dịch vụ công ích"},  # utility
    "lex.en.100k.008523": {"vi": "cỏ dại; cỏ hoang"},  # weed
    "lex.en.100k.008525": {"vi": "phúc lợi xã hội; an sinh xã hội"},  # welfare
    "lex.en.100k.008527": {"vi": "sự tôn sùng; sự thờ phụng"},  # worship
    "lex.en.100k.008528": {"vi": "năng suất; sản lượng; lợi tức"},  # yield (noun)
    "lex.en.100k.008532": {"pos": "num", "vi": "số tám (8)"},  # eight
    "lex.en.100k.008534": {"ipa": "/tuː/"},  # ii (Roman numeral II)
    "lex.en.100k.008545": {"vi": "khúc độc ca opera; khúc aria"},  # aria
    "lex.en.100k.008549": {"vi": "rào cản; chướng ngại vật"},  # barrier
    "lex.en.100k.008550": {"vi": "chùm tia sáng; xà gồ dầm"},  # beam (noun)

    # 3551-3600
    "lex.en.100k.008551": {"pos": "noun", "vi": "ổ bi; vòng bi; phong thái"},  # bearing
    "lex.en.100k.008553": {"vi": "gian hàng; quầy hàng; buồng"},  # booth
    "lex.en.100k.008557": {"vi": "chồi non; nụ hoa"},  # bud (noun)
    "lex.en.100k.008558": {"vi": "bánh mì tròn; búi tóc; vòng ba"},  # buns (purged crude slur)
    "lex.en.100k.008560": {"vi": "quy chuẩn; nguyên tắc; quy điển"},  # canon (removed canyon 'hẻm núi')
    "lex.en.100k.008562": {"vi": "trần nhà; mức trần chi phí"},  # ceiling
    "lex.en.100k.008564": {"vi": "kẻ gian lận; trò bịp bợm"},  # cheat (noun)
    "lex.en.100k.008565": {"pos": "noun", "vi": "quả anh đào; màu đỏ anh đào"},  # cherry
    "lex.en.100k.008566": {"vi": "khe ngực; sự phân chia"},  # cleavage
    "lex.en.100k.008569": {"vi": "khối thịnh vượng chung"},  # commonwealth
    "lex.en.100k.008570": {"vi": "tham nhũng; đồi bại"},  # corrupt (adj)
    "lex.en.100k.008577": {"pos": "prep", "vi": "mặc dù; bất chấp"},  # despite
    "lex.en.100k.008580": {"vi": "tính kỷ luật; ngành học"},  # discipline
    "lex.en.100k.008586": {"vi": "sự tham gia; sự tương tác; đính hôn"},  # engagement
    "lex.en.100k.008587": {"vi": "doanh nghiệp; xí nghiệp"},  # enterprise
    "lex.en.100k.008592": {"vi": "vật trưng bày; triển lãm"},  # exhibit (noun)
    "lex.en.100k.008597": {"vi": "ngọn lửa; lời thóa mạ trên mạng"},  # flame

    # 3601-3650
    "lex.en.100k.008603": {"vi": "sự cầm nắm; sự kẹp chặt; tay cầm"},  # grip
    "lex.en.100k.008604": {"vi": "các lùm cây; rừng cây nhỏ"},  # groves
    "lex.en.100k.008605": {"vi": "phần cứng máy tính; thiết bị cứng"},  # hardware (purged archaic 'cương liệu')
    "lex.en.100k.008608": {"vi": "vụ cướp táo tợn; vụ trộm lớn"},  # heist
    "lex.en.100k.008610": {"vi": "rất vui nhộn; cực kỳ hài hước"},  # hilarious
    "lex.en.100k.008614": {"vi": "giống hệt nhau; đồng nhất"},  # identical
    "lex.en.100k.008615": {"pos": "verb", "vi": "triển khai; thực hiện; áp dụng"},  # implement
    "lex.en.100k.008619": {"vi": "ngay lập tức; tức thì"},  # instantly
    "lex.en.100k.008622": {"vi": "thuộc trí tuệ; mang tính trí thức"},  # intellectual
    "lex.en.100k.008626": {"vi": "vui tươi; hân hoan; ngập tràn vui"},  # joyful
    "lex.en.100k.008631": {"vi": "vết rò rỉ; sự rò rỉ thông tin"},  # leak (noun)
    "lex.en.100k.008632": {"vi": "pháp luật; luật ban hành; lập pháp"},  # legislation
    "lex.en.100k.008634": {"vi": "hệ thống chiếu sáng; ánh sáng"},  # lighting
    "lex.en.100k.008635": {"vi": "khổng lồ; to lớn đồ sộ"},  # mammoth (adj)
    "lex.en.100k.008638": {"vi": "tên lửa; phi đạn"},  # missile
    "lex.en.100k.008639": {"vi": "người điều phối; điều hành viên"},  # moderator
    "lex.en.100k.008641": {"pos": "noun", "vi": "quả ô-liu; màu xanh ô-liu"},  # olive
    "lex.en.100k.008644": {"vi": "sự cởi mở; tính minh bạch"},  # openness
    "lex.en.100k.008645": {"pos": "noun", "vi": "đối thủ; địch thủ; người chống đối"},  # opponent
    "lex.en.100k.008649": {"vi": "viên ngọc trai; hạt trân châu"},  # pearl (noun)

    # 3651-3700
    "lex.en.100k.008654": {"vi": "bác sĩ y khoa; thầy thuốc"},  # physician (purged archaic 'đốc-tờ')
    "lex.en.100k.008655": {"vi": "cây thông; gỗ thông"},  # pine (noun)
    "lex.en.100k.008657": {"vi": "đặc quyền; ưu đãi đặc biệt"},  # privilege
    "lex.en.100k.008659": {"vi": "việc lập trình máy tính"},  # programming
    "lex.en.100k.008666": {"vi": "hệ thống ra-đa; máy dò sóng"},  # radar
    "lex.en.100k.008669": {"vi": "sự công nhận; sự nhận diện"},  # recognition
    "lex.en.100k.008672": {"vi": "sơ yếu lý lịch; bản tóm tắt"},  # resume (noun)
    "lex.en.100k.008674": {"vi": "đoạn riff lặp lại (âm nhạc)"},  # riff
    "lex.en.100k.008678": {"vi": "vết trầy xước; tình thế khó khăn"},  # scrape
    "lex.en.100k.008681": {"vi": "kéo xén lông; ứng suất cắt"},  # shear
    "lex.en.100k.008686": {"pos": "verb", "vi": "đập vỡ nát; phá tan tành"},  # smash
    "lex.en.100k.008689": {"vi": "khoảng thời gian; sải nhịp; độ dài"},  # span
    "lex.en.100k.008690": {"vi": "bình xịt; tia nước xịt"},  # spray
    "lex.en.100k.008691": {"vi": "cổ phần; số tiền cược; cọc chống"},  # stake
    "lex.en.100k.008694": {"vi": "chất; vật chất; thực chất"},  # substance
    "lex.en.100k.008696": {"vi": "nhanh chóng; mau lẹ; chim yến"},  # swift
    "lex.en.100k.008697": {"pos": "verb", "vi": "giải quyết; đương đầu; chặn bóng"},  # tackle
    "lex.en.100k.008698": {"vi": "hình xăm"},  # tattoo
    "lex.en.100k.008699": {"pos": "noun", "vi": "giọng nam cao (tenor); chiều hướng"},  # tenor

    # 3701-3750
    "lex.en.100k.008701": {"vi": "phí cầu đường; số thương vong"},  # toll
    "lex.en.100k.008702": {"vi": "bản dịch; sự biên dịch"},  # translation
    "lex.en.100k.008704": {"vi": "cúp vô địch; chiến tích"},  # trophy
    "lex.en.100k.008709": {"vi": "bản nâng cấp; sự nâng cấp"},  # upgrade
    "lex.en.100k.008713": {"pos": "noun", "vi": "cựu chiến binh; người kỳ cựu"},  # veteran
    "lex.en.100k.008715": {"vi": "có tầm nhìn xa trông rộng; nhìn xa"},  # visionary
    "lex.en.100k.008716": {"vi": "cử tri; người bỏ phiếu"},  # voter
    "lex.en.100k.008717": {"vi": "giàu có; thịnh vượng"},  # wealthy
    "lex.en.100k.008719": {"vi": "quả phụ; người góa chồng"},  # widow
    "lex.en.100k.008723": {"vi": "nước Ca-na-đa (Canada)"},  # canada
    "lex.en.100k.008725": {"vi": "cấp tính; sắc bén; nghiêm trọng"},  # acute
    "lex.en.100k.008726": {"vi": "sự nghiện ngập; chứng nghiện"},  # addiction
    "lex.en.100k.008727": {"vi": "đầy đủ; thỏa đáng; tương xứng"},  # adequate
    "lex.en.100k.008728": {"vi": "sự nhận nuôi; sự thông qua áp dụng"},  # adoption
    "lex.en.100k.008730": {"vi": "luân phiên; xen kẽ; thay thế"},  # alternate
    "lex.en.100k.008731": {"vi": "chuyên viên phân tích"},  # analyst
    "lex.en.100k.008732": {"vi": "mỏ neo; biên tập viên chính"},  # anchor
    "lex.en.100k.008733": {"pos": "noun", "vi": "cổng vòm; vòm hình cung"},  # arch
    "lex.en.100k.008735": {"vi": "sự tham dự; số người tham dự"},  # attendance
    "lex.en.100k.008736": {"vi": "cuộc kiểm toán; sự kiểm tra sổ sách"},  # audit
    "lex.en.100k.008737": {"vi": "trục toạ độ; trục quay"},  # axis
    "lex.en.100k.008738": {"vi": "huy hiệu; thẻ nhân viên"},  # badge
    "lex.en.100k.008742": {"pos": "noun", "vi": "bu-lông ốc vít; tia sét; chốt cửa"},  # bolt
    "lex.en.100k.008743": {"vi": "sự tài ba xuất chúng; vẻ rực rỡ"},  # brilliance
    "lex.en.100k.008744": {"vi": "tiếng vo ve; sự xôn xao bàn tán"},  # buzz
    "lex.en.100k.008746": {"pos": "verb", "vi": "ngừng; chấm dứt; kết thúc"},  # cease
    "lex.en.100k.008747": {"vi": "thủ tướng; hiệu trưởng danh dự"},  # chancellor

    # 3751-3800
    "lex.en.100k.008754": {"vi": "sự liên minh; khối liên minh"},  # coalition
    "lex.en.100k.008759": {"vi": "bảng điều khiển; máy chơi game"},  # console
    "lex.en.100k.008760": {"vi": "chuyên gia tư vấn; cố vấn"},  # consultant
    "lex.en.100k.008761": {"vi": "sự tranh cãi; cuộc luận chiến"},  # controversy
    "lex.en.100k.008762": {"vi": "truyền thống; theo thông lệ"},  # conventional
    "lex.en.100k.008766": {"pos": "verb", "vi": "đương đầu; ứng phó; đối phó"},  # cope
    "lex.en.100k.008770": {"vi": "dấu gạch ngang; cú lao nhanh"},  # dash
    "lex.en.100k.008771": {"vi": "sáng chói mắt; lộng lẫy tuyệt đẹp"},  # dazzling
    "lex.en.100k.008772": {"vi": "sự thâm hụt; khoản thiếu hụt"},  # deficit
    "lex.en.100k.008774": {"vi": "dày đặc; đông đúc; đặc quánh"},  # dense
    "lex.en.100k.008779": {"vi": "nước sốt chấm; sự sụt giảm nhẹ"},  # dip
    "lex.en.100k.008781": {"vi": "bến tàu; ụ tàu; thanh dock (IT)"},  # dock (purged 'chút chít')
    "lex.en.100k.008782": {"vi": "ống thoát nước; cống rãnh"},  # drain
    "lex.en.100k.008784": {"vi": "được đắc cử (chưa nhậm chức)"},  # elect (adj)
    "lex.en.100k.008786": {"vi": "cái ôm; sự đón nhận nồng nhiệt"},  # embrace
    "lex.en.100k.008790": {"vi": "quá mức; thái quá; quá độ"},  # excessive (<=35)
    "lex.en.100k.008791": {"vi": "sự thi hành; sự thực thi dự án"},  # execution
    "lex.en.100k.008793": {"vi": "vải vóc; kết cấu; cấu trúc"},  # fabric
    "lex.en.100k.008798": {"pos": "noun", "vi": "lỗi phạm vi; cú đánh bóng ngoài"},  # foul
    "lex.en.100k.008799": {"vi": "người lập dị; kẻ quái đản"},  # freak (noun)

    # 3801-3850
    "lex.en.100k.008804": {"vi": "nhẹ nhàng; dịu dàng; êm ái"},  # gently
    "lex.en.100k.008805": {"vi": "thuộc sông băng; lạnh buốt giá"},  # glacial
    "lex.en.100k.008806": {"vi": "con dê"},  # goat
    "lex.en.100k.008807": {"vi": "rừng cây xanh tươi"},  # greenwood
    "lex.en.100k.008808": {"vi": "nỗi đau buồn sâu sắc; tang tóc"},  # grief
    "lex.en.100k.008812": {"vi": "khiêm tốn; nhún nhường; giản dị"},  # humble
    "lex.en.100k.008813": {"vi": "lai ghép; đa hợp; hỗn hợp"},  # hybrid
    "lex.en.100k.008815": {"vi": "hàng nhập khẩu; sự nhập khẩu"},  # import (noun)
    "lex.en.100k.008822": {"vi": "việc giặt ủi; đồ giặt; tiệm giặt"},  # laundry (fixed typo 'giặt giạ')
    "lex.en.100k.008823": {"vi": "bãi cỏ sân vườn"},  # lawn
    "lex.en.100k.008826": {"vi": "huyền thoại; mang tính truyền kỳ"},  # legendary
    "lex.en.100k.008827": {"vi": "hợp pháp; chính đáng; hợp lý"},  # legitimate
    "lex.en.100k.008833": {"vi": "châm ngôn; châm ngôn xử thế"},  # maxim
    "lex.en.100k.008835": {"vi": "hỗn hợp; sự pha trộn"},  # mixture
    "lex.en.100k.008836": {"vi": "khiêm tốn; vừa phải; nhã nhặn"},  # modest
    "lex.en.100k.008837": {"vi": "cây lau nhà; chổi lau sàn"},  # mop
    "lex.en.100k.008839": {"vi": "gọn gàng; ngăn nắp; tinh tươm"},  # neat
    "lex.en.100k.008841": {"vi": "sự khỏa thân; cảnh khỏa thân"},  # nudity
    "lex.en.100k.008842": {"vi": "hạt dinh dưỡng; đai ốc (bu-lông)"},  # nut
    "lex.en.100k.008844": {"vi": "quan điểm; triển vọng tương lai"},  # outlook
    "lex.en.100k.008845": {"vi": "tập giấy ghi chép; đệm bảo vệ"},  # pad
    "lex.en.100k.008846": {"vi": "đơn vị pascal (Pa); tiếng Pascal"},  # pascal
    "lex.en.100k.008850": {"vi": "hầu như; gần như; trên thực tế"},  # practically

    # 3851-3900
    "lex.en.100k.008852": {"vi": "chức tổng thống; nhiệm kỳ tổng thống"},  # presidency
    "lex.en.100k.008855": {"vi": "nhịp đập; mạch đập; xung"},  # pulse
    "lex.en.100k.008857": {"vi": "hòa nhau; không ai nợ ai"},  # quits
    "lex.en.100k.008858": {"vi": "sự hung hãn phá phách; cơn cuồng nộ"},  # rampage
    "lex.en.100k.008861": {"vi": "cây sậy; dăm kèn (nhạc cụ)"},  # reed
    "lex.en.100k.008864": {"pos": "noun", "vi": "đồ cho thuê; khoản tiền thuê"},  # rental
    "lex.en.100k.008866": {"vi": "sự rút lui; nơi tĩnh dưỡng"},  # retreat
    "lex.en.100k.008869": {"vi": "cánh buồm; chuyến đi thuyền buồm"},  # sail
    "lex.en.100k.008870": {"vi": "vải sa-tanh; lụa bóng"},  # satin
    "lex.en.100k.008871": {"vi": "sự tán xạ; sự rải rác"},  # scattering
    "lex.en.100k.008877": {"vi": "tiếng đóng sầm cửa; giải Grand Slam"},  # slam
    "lex.en.100k.008878": {"pos": "adj", "vi": "lén lút; bất ngờ không báo trước"},  # sneak
    "lex.en.100k.008880": {"vi": "chồng; ngăn xếp dữ liệu (IT)"},  # stack
    "lex.en.100k.008881": {"vi": "một cách nghiêm ngặt; chặt chẽ"},  # strictly
    "lex.en.100k.008884": {"vi": "sự đầu hàng; sự buông bỏ"},  # surrender
    "lex.en.100k.008885": {"vi": "sự giám sát; camera an ninh theo dõi"},  # surveillance
    "lex.en.100k.008888": {"vi": "dịu dàng; mềm; nhạy cảm đau"},  # tender
    "lex.en.100k.008890": {"vi": "luận văn tốt nghiệp; luận đề"},  # thesis (<=35)
    "lex.en.100k.008891": {"pos": "noun", "vi": "thuốc bổ; nước tonic tăng lực"},  # tonic
    "lex.en.100k.008892": {"vi": "sự tra tấn; sự chịu đựng khổ sở"},  # torture
    "lex.en.100k.008893": {"vi": "huấn luyện viên; giày thể thao"},  # trainer
    "lex.en.100k.008894": {"vi": "hộp số xe; sự truyền tải dữ liệu"},  # transmission
    "lex.en.100k.008895": {"vi": "thân cây; cốp xe ô tô; vòi voi"},  # trunk

    # 3901-3950
    "lex.en.100k.008901": {"vi": "cây roi da; người đốc thúc đảng"},  # whip
    "lex.en.100k.008902": {"vi": "chiều rộng; bề ngang"},  # width
    "lex.en.100k.008903": {"vi": "khăn ướt; cú lau chùi"},  # wipe
    "lex.en.100k.008905": {"vi": "dễ uốn nắn; dễ nhượng bộ"},  # yielding (<=35)
    "lex.en.100k.008910": {"pos": "pron", "vi": "không ai; không cái nào"},  # none
    "lex.en.100k.008911": {"vi": "nước Nga (Russia)"},  # russia
    "lex.en.100k.008915": {"vi": "ngoài ra; thêm vào đó"},  # additionally
    "lex.en.100k.008917": {"vi": "thuốc gây mê; sự gây mê tê"},  # anesthesia
    "lex.en.100k.008923": {"vi": "múa ba lê; vũ kịch ba-lê"},  # ballet
    "lex.en.100k.008924": {"vi": "sự phá sản; tình trạng vỡ nợ"},  # bankruptcy
    "lex.en.100k.008925": {"vi": "chuồng thóc; kho thóc; nhà kho"},  # barn
    "lex.en.100k.008927": {"vi": "có lợi; bổ ích; tốt cho sức khỏe"},  # beneficial (32 chars <=35)
    "lex.en.100k.008930": {"vi": "kỳ dị; quái gở; kỳ lạ"},  # bizarre
    "lex.en.100k.008931": {"vi": "áo sơ mi nữ; áo blouse"},  # blouse
    "lex.en.100k.008932": {"vi": "vụ đánh bom; sự ném bom"},  # bombing
    "lex.en.100k.008933": {"vi": "sự cố hỏng hóc; sự suy sụp"},  # breakdown
    "lex.en.100k.008934": {"vi": "chó mặt xệ; giống chó bulldog"},  # bulldog
    "lex.en.100k.008939": {"vi": "giáo sĩ; tu sĩ tôn giáo"},  # cleric
    "lex.en.100k.008940": {"vi": "hệ số (toán học/vật lý)"},  # coefficient
    "lex.en.100k.008941": {"vi": "đồng nghiệp trong cơ quan"},  # colleague
    "lex.en.100k.008942": {"vi": "sự phức tạp; độ phức tạp"},  # complexity
    "lex.en.100k.008944": {"vi": "chỉ huy lái tàu; lái tàu biển"},  # conn
    "lex.en.100k.008945": {"vi": "ý thức; sự tỉnh táo"},  # consciousness
    "lex.en.100k.008948": {"vi": "nhà tranh vùng quê; nhà nông thôn"},  # cottage
    "lex.en.100k.008949": {"vi": "báo sư tử núi; phụ nữ quyến rũ"},  # cougar (cougar animal & slang)
    "lex.en.100k.008950": {"vi": "giả mạo; tiền giả; hàng nhái"},  # counterfeit

    # 3951-4000
    "lex.en.100k.008953": {"vi": "ngành nha khoa; khoa răng hàm mặt"},  # dentistry
    "lex.en.100k.008954": {"vi": "nhân phẩm; lòng tự trọng"},  # dignity
    "lex.en.100k.008956": {"vi": "sự vứt bỏ; sự định đoạt; xử lý rác"},  # disposal
    "lex.en.100k.008958": {"vi": "quyên góp; quyên tặng; ủng hộ"},  # donate
    "lex.en.100k.008960": {"vi": "ngành điện tử; thiết bị điện tử"},  # electronics
    "lex.en.100k.008962": {"pos": "verb", "vi": "thuê làm việc; tuyển dụng"},  # employ
    "lex.en.100k.008964": {"vi": "dám nghĩ dám làm; tính khởi nghiệp"},  # entrepreneurial
    "lex.en.100k.008965": {"vi": "cà phê espresso đậm vị"},  # espresso
    "lex.en.100k.008970": {"vi": "sáo fife quân nhạc"},  # fife
    "lex.en.100k.008972": {"vi": "giận dữ; lôi đình; thịnh nộ"},  # furious (<=35)
    "lex.en.100k.008973": {"vi": "trò cờ bạc; nạn đánh bạc"},  # gambling (purged archaic 'đổ bác')
    "lex.en.100k.008975": {"vi": "tuyến bài tiết; hạch"},  # gland
    "lex.en.100k.008976": {"vi": "ánh sáng ấm áp; vẻ rạng rỡ"},  # glow
    "lex.en.100k.008977": {"vi": "sự thấu hiểu; tầm với; sự nắm bắt"},  # grasp
    "lex.en.100k.008980": {"vi": "cơn mưa đá; tràng hoan hô chào đón"},  # hail
    "lex.en.100k.008981": {"vi": "cỏ khô (cho gia súc)"},  # hay
    "lex.en.100k.008983": {"vi": "máy bay trực thăng"},  # helicopter
    "lex.en.100k.008984": {"vi": "rỗng ruột; trống rỗng"},  # hollow
    "lex.en.100k.008986": {"vi": "người Hung Nô cổ đại"},  # hun
    "lex.en.100k.008987": {"vi": "sự thiếu hiểu biết; sự thiếu thông tin"},  # ignorance
    "lex.en.100k.008988": {"vi": "thiếu hiểu biết; dốt nát"},  # ignorant
    "lex.en.100k.008989": {"vi": "người nhập cư"},  # immigrant
    "lex.en.100k.008990": {"vi": "trẻ sơ sinh (dưới 1 tuổi)"},  # infant
    "lex.en.100k.008991": {"vi": "lạm phát tiền tệ; sự thổi phồng"},  # inflation
    "lex.en.100k.008994": {"vi": "lời lăng mạ; sự sỉ nhục"},  # insult
    "lex.en.100k.008996": {"vi": "xương quai hàm"},  # jaw
    "lex.en.100k.008998": {"vi": "rau cải xoăn (kale)"},  # kale
    "lex.en.100k.008999": {"vi": "khập khiễng (lý do); què quặt"},  # lame
    "lex.en.100k.009000": {"vi": "ngọn giáo dài; cây thương hiệp sĩ"},  # lance
}

with open('content/english/qa-batches/batch-02.json', 'r', encoding='utf-8') as f:
    batch_data = json.load(f)

records = batch_data['records']

# Verify slice
target_records = records[3500:4000]
print(f"Applying overrides to records 3500-4000 ({len(target_records)} items)...")
applied_count = 0

for r in target_records:
    rid = r['id']
    if rid in OVERRIDES_ROUND_08:
        for k, v in OVERRIDES_ROUND_08[rid].items():
            r[k] = v
        applied_count += 1
    # Check length
    assert len(r['vi']) <= 35, f"Length violation at {rid}: {len(r['vi'])} chars: {r['vi']}"

print(f"Successfully verified and applied {applied_count} overrides!")

# Update reviewedCount to 4000
batch_data['reviewedCount'] = 4000

with open('content/english/qa-batches/batch-02.json', 'w', encoding='utf-8') as f:
    json.dump(batch_data, f, ensure_ascii=False, indent=2)

print("Round 8 applied and committed to batch-02.json! reviewedCount=4000.")
