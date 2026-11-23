import json

# Round 4 overrides (records 1500 to 2000, STT 1501 to 2000, IDs lex.en.100k.011501 to 012000)
OVERRIDES_B03_R04 = {
    # 1501-1550
    "lex.en.100k.011501": {"vi": "enzym kinase (hóa sinh)"},  # kinase
    "lex.en.100k.011502": {"vi": "kosher; đồ ăn hợp luật Do Thái"},  # kosher (<=35)
    "lex.en.100k.011503": {"vi": "chim chiền chiện; trò đùa vui"},  # lark
    "lex.en.100k.011504": {"vi": "tờ rơi quảng cáo; tờ truyền đơn"},  # leaflet
    "lex.en.100k.011505": {"vi": "hợp pháp hóa; luật hóa"},  # legalize
    "lex.en.100k.011506": {"vi": "nhà lập pháp; nghị sĩ quốc hội"},  # legislator
    "lex.en.100k.011507": {"vi": "bị đánh bại hoàn toàn; thua cuộc"},  # licked
    "lex.en.100k.011508": {"vi": "biết đọc biết viết; có học thức"},  # literate
    "lex.en.100k.011509": {"vi": "bản địa hóa; định vị khu vực"},  # localization
    "lex.en.100k.011510": {"vi": "nam tính cường tráng; đàn ông"},  # macho
    "lex.en.100k.011511": {"vi": "váy maxi dài; kiểu váy dài"},  # maxi
    "lex.en.100k.011514": {"vi": "cô bé ngổ ngáo; cô nương nhỏ"},  # missy
    "lex.en.100k.011516": {"vi": "độc thoại; bài độc thoại"},  # monologue
    "lex.en.100k.011517": {"vi": "khí monoxit; oxit đơn"},  # monoxide
    "lex.en.100k.011519": {"vi": "xe máy; xe mô tô hai bánh"},  # motorbike
    "lex.en.100k.011521": {"vi": "tự luyến; quá tự cao"},  # narcissistic
    "lex.en.100k.011523": {"vi": "phi tuyến tính; không thẳng"},  # nonlinear
    "lex.en.100k.011526": {"vi": "được phối khí; được dàn xếp kỹ"},  # orchestrated
    "lex.en.100k.011527": {"vi": "sự cố mất điện; cúp dịch vụ"},  # outage
    "lex.en.100k.011528": {"vi": "công nhân đóng gói hàng"},  # packer
    "lex.en.100k.011529": {"vi": "tấm pallet; bệ kê hàng hóa"},  # pallet
    "lex.en.100k.011530": {"vi": "ngò tây; rau mùi tây"},  # parsley
    "lex.en.100k.011533": {"pos": "verb", "vi": "nhổ lông; bứt; gảy đàn"},  # pluck
    "lex.en.100k.011534": {"vi": "thấm thía; đau xót; nhói lòng"},  # poignant
    "lex.en.100k.011535": {"vi": "bô vệ sinh trẻ em; gàn dở"},  # potty
    "lex.en.100k.011537": {"vi": "bấp bênh; không vững chắc"},  # precarious
    "lex.en.100k.011538": {"vi": "cái cớ; viện cớ; lý do thoái thác"},  # pretext (purged single-word 'cớ')
    "lex.en.100k.011540": {"vi": "vũng nước nhỏ; vũng bùn lầy"},  # puddle
    "lex.en.100k.011541": {"vi": "bến cảng; bến tàu bốc dỡ"},  # quay
    "lex.en.100k.011543": {"pos": "noun", "vi": "cuộc đột kích; sự cướp phá"},  # raiding
    "lex.en.100k.011545": {"vi": "được tái thiết; phục dựng lại"},  # reconstructed
    "lex.en.100k.011547": {"vi": "tải lại trang; nạp lại đạn"},  # reload
    "lex.en.100k.011548": {"vi": "vang vọng; gợi nhớ sâu sắc"},  # resonant
    "lex.en.100k.011550": {"pos": "verb", "vi": "thu hồi; bãi bỏ; hủy bỏ"},  # revoke (pos fixed)

    # 1551-1600
    "lex.en.100k.011554": {"vi": "sự ly khai; sự tách khỏi tổ chức"},  # secession
    "lex.en.100k.011556": {"vi": "có tính bước ngoặt; nền tảng"},  # seminal
    "lex.en.100k.011557": {"vi": "thập niên 70; tuổi bảy mươi"},  # seventies
    "lex.en.100k.011560": {"pos": "verb", "vi": "đun nhỏ lửa; sôi liu riu; âm ỉ"},  # simmer
    "lex.en.100k.011563": {"vi": "mẹ kế; dì ghẻ"},  # stepmother
    "lex.en.100k.011564": {"vi": "tinh gọn; hợp lý hóa quy trình"},  # streamlined
    "lex.en.100k.011566": {"vi": "bị chìm dưới nước; hõm sâu"},  # sunken
    "lex.en.100k.011567": {"vi": "nước Thụy Điển"},  # sweden
    "lex.en.100k.011569": {"vi": "nước Syria"},  # syria
    "lex.en.100k.011570": {"vi": "ống tiêm; xi-lanh y tế"},  # syringe
    "lex.en.100k.011572": {"vi": "có làn da rám nắng; thuộc da"},  # tanned
    "lex.en.100k.011573": {"vi": "kẻ hủy diệt; đoạn kết thúc gen"},  # terminator
    "lex.en.100k.011574": {"vi": "nhà lý thuyết; nhà lý luận"},  # theorist
    "lex.en.100k.011577": {"vi": "nằm ngang; đường cắt ngang"},  # transverse
    "lex.en.100k.011578": {"vi": "sự run rẩy; đang run sợ"},  # trembling
    "lex.en.100k.011579": {"vi": "cây đinh ba; mũi ba chĩa"},  # trident
    "lex.en.100k.011580": {"vi": "sự lấp lánh; ánh mắt lấp lánh"},  # twinkle
    "lex.en.100k.011582": {"vi": "chưa được giải thích; bí ẩn"},  # unexplained
    "lex.en.100k.011583": {"vi": "không lường trước được; bất ngờ"},  # unforeseen
    "lex.en.100k.011584": {"vi": "nỗi buồn tủi; sự bất hạnh"},  # unhappiness
    "lex.en.100k.011585": {"vi": "chưa chuẩn bị; bị động"},  # unprepared
    "lex.en.100k.011587": {"vi": "không thể tưởng tượng nổi"},  # unthinkable
    "lex.en.100k.011588": {"vi": "sự nâng đỡ tinh thần; nâng lên"},  # uplift
    "lex.en.100k.011589": {"vi": "sự biến mất; sự tan biến"},  # vanishing
    "lex.en.100k.011590": {"vi": "rau củ; người ăn chay"},  # veggie
    "lex.en.100k.011591": {"vi": "bị che mạng; che giấu kín đáo"},  # veiled
    "lex.en.100k.011593": {"vi": "hình dung trực quan; tưởng tượng"},  # visualize
    "lex.en.100k.011595": {"vi": "sự lúc lắc; sự ngọ nguậy"},  # wiggle
    "lex.en.100k.011599": {"pos": "noun", "vi": "Đại Tây Dương"},  # atlantic (pos fixed)
    "lex.en.100k.011600": {"vi": "thành phố Cambridge; ĐH Cambridge"},  # cambridge

    # 1601-1650
    "lex.en.100k.011601": {"vi": "hãng Disney; Walt Disney"},  # disney
    "lex.en.100k.011602": {"vi": "tên riêng Gary; thành phố Gary"},  # gary
    "lex.en.100k.011603": {"vi": "tên họ Ross"},  # ross
    "lex.en.100k.011604": {"vi": "thành phố Seattle"},  # seattle
    "lex.en.100k.011605": {"vi": "tên riêng/họ Allen"},  # allen
    "lex.en.100k.011607": {"vi": "tên riêng/họ Clark"},  # clark
    "lex.en.100k.011608": {"vi": "tháng Hai (viết tắt Feb)"},  # feb
    "lex.en.100k.011609": {"ipa": "/aɪ ˈviː/", "vi": "số La Mã IV (bốn)"},  # iv (added ipa)
    "lex.en.100k.011610": {"pos": "num", "vi": "ba mươi (30)"},  # thirty (pos fixed)
    "lex.en.100k.011611": {"vi": "thành phố Atlanta"},  # atlanta
    "lex.en.100k.011614": {"ipa": "/ˌkɪləˈmiːtər/", "vi": "ki-lô-mét (km)"},  # km (added ipa)
    "lex.en.100k.011615": {"vi": "tên riêng Matthew; Ma-thi-ơ"},  # matthew
    "lex.en.100k.011616": {"ipa": "/nɒv/", "vi": "tháng Mười Một (viết tắt)"},  # nov
    "lex.en.100k.011617": {"vi": "tên riêng Patrick; Thánh Patrick"},  # patrick
    "lex.en.100k.011618": {"vi": "tên riêng/họ Wayne"},  # wayne
    "lex.en.100k.011619": {"vi": "tên riêng/họ Anderson"},  # anderson
    "lex.en.100k.011620": {"vi": "thành phố Austin"},  # austin
    "lex.en.100k.011621": {"vi": "hành vi; cách ứng xử"},  # behaviour
    "lex.en.100k.011622": {"vi": "thành phố Melbourne"},  # melbourne
    "lex.en.100k.011623": {"vi": "tổ chức; cơ quan; sự tổ chức"},  # organisation
    "lex.en.100k.011624": {"vi": "tên riêng Walter"},  # walter
    "lex.en.100k.011629": {"vi": "mỗi người; mỗi cái; mỗi phần"},  # apiece (purged single-word 'mỗi')
    "lex.en.100k.011631": {"vi": "hình vòm; uốn cong hình vòm"},  # arched
    "lex.en.100k.011632": {"vi": "môn bắn cung; cung thuật"},  # archery
    "lex.en.100k.011633": {"vi": "thuộc động mạch; trục giao thông"},  # arterial
    "lex.en.100k.011634": {"vi": "đi lên; thăng tiến; trèo lên"},  # ascend (purged single-word 'lên')
    "lex.en.100k.011636": {"vi": "có thể đạt được; khả thi"},  # attainable
    "lex.en.100k.011637": {"vi": "thuộc thính giác; khả năng nghe"},  # auditory
    "lex.en.100k.011639": {"vi": "sự ác cảm; sự ghét bỏ"},  # aversion
    "lex.en.100k.011641": {"vi": "giống chó săn Beagle"},  # beagle
    "lex.en.100k.011642": {"vi": "hai năm một lần; cây hai năm tuổi"},  # biennial
    "lex.en.100k.011643": {"vi": "dân lái mô tô; nhóm đi xe máy"},  # bikers
    "lex.en.100k.011645": {"vi": "người vay tiền; người mượn"},  # borrower
    "lex.en.100k.011646": {"vi": "bím tóc; bện tóc; dải viền"},  # braid
    "lex.en.100k.011647": {"vi": "làm sáng lên; bừng sáng; rạng rỡ"},  # brighten
    "lex.en.100k.011648": {"vi": "chỗ phồng; chỗ phình ra; nhô lên"},  # bulge
    "lex.en.100k.011650": {"vi": "chứng nhận; cấp bằng; xác thực"},  # certify

    # 1651-1700
    "lex.en.100k.011651": {"vi": "bị mê hoặc; bị quyến rũ"},  # charmed
    "lex.en.100k.011655": {"vi": "nén ép; miếng gạc y tế đắp"},  # compress
    "lex.en.100k.011658": {"vi": "đan móc len; mũi móc len"},  # crochet (purged single-word 'móc')
    "lex.en.100k.011661": {"vi": "kẻ ngu ngốc; đồ đáng ghét (lóng)"},  # dickhead (sanitized)
    "lex.en.100k.011663": {"vi": "tùy ý; tùy quyền quyết định"},  # discretionary
    "lex.en.100k.011665": {"vi": "ký túc xá; phòng ngủ tập thể"},  # dormitory
    "lex.en.100k.011667": {"vi": "sự nhân bản; sự trùng lặp"},  # duplication
    "lex.en.100k.011669": {"vi": "danh dự (giáo sư về hưu)"},  # emeritus
    "lex.en.100k.011671": {"vi": "điều bí ẩn; người khó hiểu"},  # enigma
    "lex.en.100k.011672": {"vi": "sải đo nước biển; thấu hiểu"},  # fathom
    "lex.en.100k.011673": {"vi": "vợ chưa cưới; vị hôn thê"},  # fiancee
    "lex.en.100k.011674": {"vi": "hư cấu; tưởng tượng; giả tưởng"},  # fictitious
    "lex.en.100k.011675": {"vi": "nghĩa bóng; mang tính tượng trưng"},  # figurative
    "lex.en.100k.011676": {"vi": "trực tiếp; tận mắt thấy"},  # firsthand
    "lex.en.100k.011678": {"vi": "cây lanh; sợi lanh"},  # flax (purged single-word 'lanh')
    "lex.en.100k.011679": {"vi": "mềm rũ; đĩa mềm vi tính"},  # floppy
    "lex.en.100k.011680": {"vi": "hợp chất florua (hóa học)"},  # fluoride
    "lex.en.100k.011681": {"vi": "vỗ cánh; xao xuyến; đập loạn nhịp"},  # flutter
    "lex.en.100k.011682": {"vi": "tiền cảnh; vị trí nổi bật"},  # foreground
    "lex.en.100k.011683": {"vi": "tàu hộ tống; tàu khu trục nhỏ"},  # frigate
    "lex.en.100k.011685": {"vi": "thuộc về địa chất học"},  # geologic
    "lex.en.100k.011686": {"vi": "các sách Phúc Âm; chân lý"},  # gospels
    "lex.en.100k.011687": {"vi": "tham lam hám lợi; chộp lấy"},  # grasping
    "lex.en.100k.011690": {"vi": "cái bừa (nông cụ); cào xới"},  # harrow (purged single-word 'bừa')
    "lex.en.100k.011691": {"vi": "sự nở trứng; nét gạch bóng"},  # hatching
    "lex.en.100k.011692": {"vi": "hiệu trưởng trường học"},  # headmaster
    "lex.en.100k.011695": {"vi": "gấu áo; viền mép vải; hắng giọng"},  # hem
    "lex.en.100k.011697": {"pos": "verb", "vi": "không tặc; cướp quyền kiểm soát"},  # hijack
    "lex.en.100k.011698": {"vi": "cái cuốc (nông cụ); cuốc đất"},  # hoe (purged single-word 'cuốc')
    "lex.en.100k.011699": {"vi": "nhà nhân văn; thuộc nhân văn"},  # humanist

    # 1701-1750
    "lex.en.100k.011701": {"vi": "thuật thôi miên; sự thôi miên"},  # hypnosis
    "lex.en.100k.011704": {"vi": "trơ; thụ động; không phản ứng"},  # inert (purged single-word 'trơ')
    "lex.en.100k.011711": {"vi": "con sứa (sinh vật biển)"},  # jellyfish
    "lex.en.100k.011714": {"vi": "rửa trôi; chiết tách hòa tan"},  # leach
    "lex.en.100k.011715": {"vi": "người thuận tay trái; tả khuynh"},  # lefty
    "lex.en.100k.011716": {"vi": "sự thanh lý tài sản; giải thể"},  # liquidation
    "lex.en.100k.011720": {"vi": "sự huy động; sự động viên quân"},  # mobilization
    "lex.en.100k.011722": {"vi": "ông trùm; nhà tài phiệt lớn"},  # mogul
    "lex.en.100k.011728": {"vi": "phi hư cấu; văn học phi hư cấu"},  # nonfiction
    "lex.en.100k.011729": {"vi": "thường; thường hay (thơ ca)"},  # oft
    "lex.en.100k.011730": {"vi": "sự chính thống; giáo lý chuẩn"},  # orthodoxy
    "lex.en.100k.011731": {"vi": "phấn màu; gam màu pastel nhạt"},  # pastel
    "lex.en.100k.011733": {"vi": "khoản thanh toán cuối; hối lộ"},  # payoff
    "lex.en.100k.011736": {"vi": "đĩa bầu dục lớn; mâm thức ăn"},  # platter
    "lex.en.100k.011738": {"vi": "quận trưởng; huynh trưởng kỷ luật"},  # prefect
    "lex.en.100k.011740": {"vi": "sự tư nhân hóa doanh nghiệp"},  # privatization
    "lex.en.100k.011741": {"pos": "verb", "vi": "thúc giục; chọc nhẹ; cú hích"},  # prod
    "lex.en.100k.011742": {"vi": "thần đồng; tài năng xuất chúng"},  # prodigy
    "lex.en.100k.011743": {"pos": "noun", "vi": "vật phóng; đầu đạn; phi đạn"},  # projectile (pos fixed)
    "lex.en.100k.011745": {"vi": "chăn bông chần; may chần bông"},  # quilt
    "lex.en.100k.011746": {"vi": "chuyên viên môi giới nhà đất"},  # realtor
    "lex.en.100k.011754": {"vi": "vùng bờ biển nghỉ dưỡng Riviera"},  # riviera
    "lex.en.100k.011755": {"vi": "nữ sinh trung học; nữ sinh"},  # schoolgirl
    "lex.en.100k.011758": {"vi": "chất dẫn truyền thần kinh"},  # serotonin
    "lex.en.100k.011759": {"vi": "kẻ gian lận bài bạc; cờ bạc bịp"},  # sharper
    "lex.en.100k.011761": {"vi": "chậm chạp; uể oải; trì trệ"},  # sluggish
    "lex.en.100k.011762": {"vi": "khu ổ chuột nghèo nàn"},  # slum
    "lex.en.100k.011763": {"vi": "bệnh đậu mùa"},  # smallpox
    "lex.en.100k.011764": {"vi": "cạm bẫy; cái bẫy sập thú"},  # snare
    "lex.en.100k.011765": {"vi": "thuộc về xã hội học"},  # sociological
    "lex.en.100k.011766": {"vi": "thảm cỏ; lớp đất bề mặt có cỏ"},  # sod
    "lex.en.100k.011767": {"vi": "sự tinh tế; sự tinh vi sành điệu"},  # sophistication
    "lex.en.100k.011770": {"vi": "đậu nành; hạt đỗ tương"},  # soybean
    "lex.en.100k.011771": {"vi": "không nói nên lời; lặng người đi"},  # speechless
    "lex.en.100k.011772": {"vi": "sự làm hư hỏng; sự ôi thiu"},  # spoiling
    "lex.en.100k.011773": {"vi": "nữ phát ngôn viên"},  # spokeswoman
    "lex.en.100k.011775": {"vi": "phi thuyền không gian liên sao"},  # starship
    "lex.en.100k.011776": {"vi": "kho dự trữ; tích trữ dự trữ"},  # stockpile
    "lex.en.100k.011777": {"pos": "verb", "vi": "giậm chân mạnh; cú giậm chân"},  # stomp
    "lex.en.100k.011778": {"vi": "nhà chiến lược; chuyên gia kế sách"},  # strategist
    "lex.en.100k.011780": {"vi": "làm phép trừ; khấu trừ bớt"},  # subtract (purged single-word 'trừ')
    "lex.en.100k.011781": {"vi": "da lộn (chất liệu thuộc da)"},  # suede
    "lex.en.100k.011782": {"vi": "người theo chủ nghĩa thượng tôn"},  # supremacist
    "lex.en.100k.011784": {"vi": "màu xanh mòng két; vịt mòng két"},  # teal
    "lex.en.100k.011785": {"vi": "thứ ba là; điều thứ ba"},  # thirdly
    "lex.en.100k.011786": {"vi": "tẻ nhạt; gây mệt mỏi phiền phức"},  # tiresome
    "lex.en.100k.011787": {"vi": "rùa cạn; con rùa trên cạn"},  # tortoise
    "lex.en.100k.011790": {"vi": "truyền máu; sự truyền dịch y tế"},  # transfusion
    "lex.en.100k.011792": {"vi": "chảy nhỏ giọt; dòng chảy rỉ rỉ"},  # trickle
    "lex.en.100k.011794": {"vi": "vải tuýt (dạ len thô)"},  # tweed
    "lex.en.100k.011795": {"vi": "máy đánh chữ cổ điển"},  # typewriter
    "lex.en.100k.011798": {"vi": "không thể tưởng tượng nổi"},  # unimaginable
    "lex.en.100k.011800": {"vi": "không khôn ngoan; thiếu sáng suốt"},  # unwise

    # 1801-1850
    "lex.en.100k.011801": {"vi": "thuộc nội tạng; theo bản năng"},  # visceral
    "lex.en.100k.011802": {"vi": "người khao khát bắt chước"},  # wannabe
    "lex.en.100k.011805": {"pos": "verb", "vi": "ngáp ngủ; cái ngáp dài"},  # yawn (purged single-word 'ngáp')
    "lex.en.100k.011806": {"vi": "tiếng sủa ăng ẳng; tiếng la ngắn"},  # yelp
    "lex.en.100k.011808": {"vi": "tháng Mười (viết tắt Oct)"},  # oct
    "lex.en.100k.011809": {"vi": "thành phố Rio de Janeiro"},  # rio
    "lex.en.100k.011811": {"pos": "num", "vi": "mười hai (12)"},  # twelve (pos fixed)
    "lex.en.100k.011812": {"vi": "tên riêng Bruce"},  # bruce
    "lex.en.100k.011813": {"vi": "tháng Tám (viết tắt Aug)"},  # aug
    "lex.en.100k.011816": {"vi": "tên họ Parks; các công viên"},  # parks
    "lex.en.100k.011817": {"vi": "tên riêng/họ Russell"},  # russell
    "lex.en.100k.011818": {"vi": "niềm nở; sẵn lòng giúp đỡ"},  # accommodating
    "lex.en.100k.011821": {"vi": "sự tổng hợp; sự kết tụ khối"},  # aggregation
    "lex.en.100k.011823": {"vi": "tên riêng Anne"},  # anne
    "lex.en.100k.011825": {"vi": "nguyên tố asen; chất thạch tín"},  # arsenic
    "lex.en.100k.011827": {"vi": "buồn vui lẫn lộn; đắng ngọt"},  # bittersweet
    "lex.en.100k.011832": {"pos": "verb", "vi": "nhúc nhích; lay chuyển; dịch chuyển"},  # budge
    "lex.en.100k.011833": {"vi": "sự nhộn nhịp hối hả; tất bật"},  # bustle
    "lex.en.100k.011834": {"vi": "tiệm ca vũ; quán rượu ca nhạc"},  # cabaret
    "lex.en.100k.011837": {"vi": "về mặt hóa học; bằng hóa chất"},  # chemically
    "lex.en.100k.011838": {"pos": "verb", "vi": "làm tắc nghẽn; đôi guốc mộc"},  # clog
    "lex.en.100k.011839": {"vi": "nhân bản vô tính; tạo dòng gen"},  # cloning
    "lex.en.100k.011840": {"vi": "tầm ảnh hưởng; quyền lực; thế lực"},  # clout
    "lex.en.100k.011845": {"vi": "giới hạn; phạm vi ranh giới"},  # confines
    "lex.en.100k.011850": {"vi": "chất độc xyanua"},  # cyanide
    "lex.en.100k.011851": {"vi": "tiểu thư ra mắt giới thượng lưu"},  # deb
    "lex.en.100k.011859": {"vi": "quân cờ domino; hiệu ứng domino"},  # domino
    "lex.en.100k.011860": {"vi": "bị đánh thuốc mê; say thuốc"},  # drugged
    "lex.en.100k.011861": {"vi": "phân động vật; phân chuồng"},  # dung (purged single-word 'phân')
    "lex.en.100k.011862": {"vi": "con cá chình; con lươn biển"},  # eel
    "lex.en.100k.011863": {"vi": "nghệ thuật thêu may; đồ thêu"},  # embroidery
    "lex.en.100k.011864": {"vi": "sự di cư; sự di dân ra ngoài"},  # emigration
    "lex.en.100k.011867": {"vi": "cực kỳ tốt; tuyệt vời"},  # fantastically
    "lex.en.100k.011869": {"vi": "sự lưu loát; sự trôi chảy"},  # fluency
    "lex.en.100k.011870": {"vi": "sự phát huỳnh quang; huỳnh quang"},  # fluorescence
    "lex.en.100k.011872": {"pos": "noun", "vi": "sở trường; điểm mạnh nhất"},  # forte (pos fixed)
    "lex.en.100k.011873": {"vi": "túi da xách tay Gladstone"},  # gladstone
    "lex.en.100k.011876": {"vi": "phong cách Goth; người Goth"},  # goth
    "lex.en.100k.011878": {"vi": "tài liệu phát tay; đồ cứu tế"},  # handout
    "lex.en.100k.011879": {"vi": "móc treo quần áo; người treo"},  # hanger
    "lex.en.100k.011880": {"vi": "việc bán dạo; săn bằng chim ưng"},  # hawking
    "lex.en.100k.011881": {"pos": "verb", "vi": "tích trữ; kho tích trữ của cải"},  # hoard
    "lex.en.100k.011882": {"vi": "đám đông lúc nhúc; bầy đàn"},  # horde
    "lex.en.100k.011883": {"vi": "việc nội trợ; quản lý buồng phòng"},  # housekeeping
    "lex.en.100k.011886": {"vi": "vô phương cứu chữa; nan y"},  # incurable
    "lex.en.100k.011889": {"vi": "ngấm ngầm; âm ỉ hiểm độc"},  # insidious
    "lex.en.100k.011890": {"vi": "kết nối với nhau; liên kết mạng"},  # interconnected
    "lex.en.100k.011893": {"vi": "dầu hỏa thắp sáng; dầu hỏa"},  # kerosene
    "lex.en.100k.011894": {"vi": "bằng ren; viền ren mỏng manh"},  # lacy
    "lex.en.100k.011896": {"vi": "sự rò rỉ chất lỏng; thất thoát"},  # leakage
    "lex.en.100k.011897": {"vi": "thong thả; ung dung; nhàn nhã"},  # leisurely
    "lex.en.100k.011898": {"vi": "thuộc về hậu cần; tiếp vận"},  # logistical
    "lex.en.100k.011899": {"vi": "lỗ hổng pháp lý; kẽ hở quy định"},  # loophole
    "lex.en.100k.011900": {"vi": "trò chơi xổ số lô tô"},  # lotto

    # 1901-1950
    "lex.en.100k.011902": {"vi": "sai phạm chuyên môn; tắc trách"},  # malpractice
    "lex.en.100k.011903": {"vi": "tiếng xưng hô mẹ/bà; thưa bà"},  # mam
    "lex.en.100k.011905": {"vi": "cảnh sát liên bang; thống chế"},  # marshals
    "lex.en.100k.011906": {"vi": "sốt mayonnaise; xốt béo trứng"},  # mayonnaise
    "lex.en.100k.011907": {"vi": "du dương; có giai điệu êm ái"},  # melodic
    "lex.en.100k.011908": {"vi": "ngành vi sinh vật học"},  # microbiology
    "lex.en.100k.011912": {"vi": "chưa ngã ngũ; có thể tranh luận"},  # moot
    "lex.en.100k.011913": {"vi": "phép nhân; sự nhân lên gấp bội"},  # multiplication
    "lex.en.100k.011914": {"vi": "thịt cừu trưởng thành"},  # mutton
    "lex.en.100k.011915": {"vi": "tinh vân trong vũ trụ"},  # nebula
    "lex.en.100k.011916": {"vi": "vải lưới; hệ thống lưới vây"},  # netting
    "lex.en.100k.011917": {"vi": "con sa giông nhỏ (kỳ giông)"},  # newt
    "lex.en.100k.011918": {"vi": "nhà quý tộc; giới quý tộc"},  # nobleman
    "lex.en.100k.011919": {"vi": "chất bổ dưỡng; sự nuôi dưỡng"},  # nourishment
    "lex.en.100k.011920": {"vi": "đầu vòi phun; miệng ống phun"},  # nozzle
    "lex.en.100k.011922": {"vi": "tiệc truy hoan; cuộc trác táng"},  # orgy
    "lex.en.100k.011925": {"vi": "việc đi tiểu; đang đi tiểu"},  # peeing
    "lex.en.100k.011926": {"vi": "vỏ trái cây gọt ra; sự bong tróc"},  # peeling
    "lex.en.100k.011927": {"vi": "thuốc kháng sinh penicillin"},  # penicillin
    "lex.en.100k.011930": {"vi": "nguyên tố phóng xạ plutoni"},  # plutonium
    "lex.en.100k.011931": {"vi": "sự phân cực xã hội; phân cực"},  # polarization
    "lex.en.100k.011933": {"vi": "phương pháp tâm lý trị liệu"},  # psychotherapy
    "lex.en.100k.011935": {"vi": "bệnh dại (vi-rút dại)"},  # rabies (purged single-word 'dại')
    "lex.en.100k.011937": {"pos": "verb", "vi": "kể lại; thuật lại; kiểm phiếu lại"},  # recount
    "lex.en.100k.011940": {"vi": "làm đầy lại; cấp thêm đơn thuốc"},  # refill
    "lex.en.100k.011941": {"vi": "rất đều đặn; về mặt tôn giáo"},  # religiously
    "lex.en.100k.011943": {"vi": "tiền thù lao; tiền công trả"},  # remuneration
    "lex.en.100k.011945": {"pos": "adj", "vi": "cần thiết; điều kiện thiết yếu"},  # requisite
    "lex.en.100k.011947": {"pos": "verb", "vi": "tua lại băng; quay ngược lại"},  # rewind
    "lex.en.100k.011948": {"vi": "dải băng đeo qua vai; đai lưng"},  # sash
    "lex.en.100k.011949": {"vi": "hẻo lánh; biệt lập; yên tĩnh"},  # secluded
    "lex.en.100k.011951": {"vi": "vòng bán kết; trận bán kết"},  # semifinal
    "lex.en.100k.011952": {"vi": "giác quan; nghĩa lóng cần sa"},  # sens
    "lex.en.100k.011953": {"vi": "tránh xa; xa lánh; tẩy chay"},  # shun
    "lex.en.100k.011954": {"vi": "trợ thủ đắc lực; bạn đồng hành"},  # sidekick
    "lex.en.100k.011955": {"vi": "bộ đồ dùng bàn ăn bằng bạc"},  # silverware
    "lex.en.100k.011956": {"vi": "yếu đuối nhu nhược; ẻo lả"},  # sissy
    "lex.en.100k.011957": {"vi": "bị lệch; méo mó; thiên lệch"},  # skewed
    "lex.en.100k.011959": {"vi": "mảnh vỡ nhỏ sắc; lát cắt mỏng"},  # sliver

    # 1951-2000
    "lex.en.100k.011963": {"vi": "sự ngưng trệ; tình trạng bế tắc"},  # standstill (purged single-word 'dừng')
    "lex.en.100k.011965": {"pos": "noun", "vi": "chất kích thích; tính kích thích"},  # stimulant
    "lex.en.100k.011966": {"vi": "keo kiệt; bủn xỉn; hà tiện"},  # stingy
    "lex.en.100k.011967": {"vi": "bóp cổ; bóp nghẹt; kìm hãm"},  # strangle
    "lex.en.100k.011968": {"vi": "bị bóp nghẹt; bị nghẹn lại"},  # strangled
    "lex.en.100k.011974": {"vi": "giống chó săn sục nhỏ"},  # terrier
    "lex.en.100k.011975": {"vi": "chuyên viên kiểm thử; người thử"},  # tester
    "lex.en.100k.011976": {"vi": "thập niên 30; độ tuổi ba mươi"},  # thirties
    "lex.en.100k.011978": {"pos": "noun", "vi": "sự gợi nhớ quá khứ; người xưa cũ"},  # throwback
    "lex.en.100k.011980": {"vi": "đáng tin cậy; trung thành"},  # trusty
    "lex.en.100k.011982": {"vi": "nước Ukraina; Ukraine"},  # ukraine
    "lex.en.100k.011984": {"vi": "dễ hiểu là; hoàn toàn có thể hiểu"},  # understandably
    "lex.en.100k.011986": {"vi": "không tử tế; nhẫn tâm độc ác"},  # unkind
    "lex.en.100k.011987": {"vi": "sự dỡ hàng; bốc dỡ hàng hóa"},  # unloading
    "lex.en.100k.011988": {"vi": "không có nhãn hiệu; không dấu vết"},  # unmarked
    "lex.en.100k.011990": {"vi": "thiếu chuyên nghiệp; cẩu thả"},  # unprofessional
    "lex.en.100k.011991": {"vi": "chi phí bảo dưỡng; bảo trì"},  # upkeep
    "lex.en.100k.011992": {"vi": "bình đựng tro cốt; ấm pha trà"},  # urn
    "lex.en.100k.011993": {"pos": "verb", "vi": "rung lên; dao động; rung rinh"},  # vibrate (purged single-word 'rung')
    "lex.en.100k.011994": {"vi": "sự thức canh; lễ cầu nguyện đêm"},  # vigil
    "lex.en.100k.011995": {"vi": "sự phát âm; sự nói lên ý kiến"},  # voicing
    "lex.en.100k.011997": {"vi": "từ bỏ quyền lợi; miễn trừ"},  # waive
    "lex.en.100k.011999": {"vi": "tiền trúng thưởng; tiền thắng"},  # winnings
}

# Verify lengths <= 35
for k, v in OVERRIDES_B03_R04.items():
    if "vi" in v:
        assert len(v["vi"]) <= 35, f"Length > 35 for {k}: {v['vi']} ({len(v['vi'])})"

with open('content/english/qa-batches/batch-03.json', 'r', encoding='utf-8') as f:
    batch_data = json.load(f)

# Apply overrides to records in range 1500 to 2000
count = 0
for idx in range(1500, 2000):
    rec = batch_data['records'][idx]
    rid = rec['id']
    if rid in OVERRIDES_B03_R04:
        count += 1
        for field, val in OVERRIDES_B03_R04[rid].items():
            rec[field] = val
        rec['status'] = 'reviewed'

batch_data['reviewedCount'] = 2000

with open('content/english/qa-batches/batch-03.json', 'w', encoding='utf-8') as f:
    json.dump(batch_data, f, ensure_ascii=False, indent=2)

print(f"Successfully applied Batch 03 Round 4 ({count} overrides). Reviewed: {batch_data['reviewedCount']}/5000.")
