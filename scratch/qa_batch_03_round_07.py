import json

# Round 7 overrides (records 3000 to 3500, STT 3001 to 3500, IDs lex.en.100k.013001 to 013500)
OVERRIDES_B03_R07 = {
    # 3001-3050
    "lex.en.100k.013001": {"vi": "được trát vữa; say bí tỉ"},  # plastered
    "lex.en.100k.013002": {"vi": "trường đại học bách khoa"},  # polytechnic
    "lex.en.100k.013003": {"vi": "người Anh (tiếng lóng Úc)"},  # pom
    "lex.en.100k.013005": {"vi": "mang tính khiêu dâm; đồi trụy"},  # pornographic
    "lex.en.100k.013006": {"pos": "noun", "vi": "tiền đề lập luận; tiền đề"},  # premise
    "lex.en.100k.013007": {"vi": "có đặc quyền; nhiều ưu đãi"},  # privileged
    "lex.en.100k.013008": {"ipa": "/prɒf/", "vi": "giáo sư (viết tắt prof)"},  # prof
    "lex.en.100k.013009": {"pos": "noun", "vi": "chân chống; đạo cụ sân khấu"},  # prop
    "lex.en.100k.013010": {"vi": "tiềm năng; triển vọng tương lai"},  # prospective
    "lex.en.100k.013012": {"vi": "bị tàn phá nặng nề; cướp phá"},  # ravaged
    "lex.en.100k.013015": {"vi": "đổi tên gọi; đặt lại tên"},  # rename
    "lex.en.100k.013016": {"vi": "kết xuất đồ họa; làm cho"},  # render
    "lex.en.100k.013017": {"vi": "bản vẽ kết xuất 3D; thể hiện"},  # rendering
    "lex.en.100k.013019": {"vi": "sự bồi thường thiệt hại; hoàn trả"},  # restitution
    "lex.en.100k.013020": {"vi": "việc chỉnh sửa; ôn tập lại"},  # revising
    "lex.en.100k.013021": {"vi": "thành phố Richmond"},  # richmond
    "lex.en.100k.013023": {"vi": "sự cứu rỗi linh hồn"},  # salvation
    "lex.en.100k.013025": {"vi": "lưới vây đánh cá; sông Seine"},  # seine
    "lex.en.100k.013026": {"vi": "khăn choàng vai; khăn choàng len"},  # shawl
    "lex.en.100k.013028": {"vi": "đồng xu shilling (tiền Anh)"},  # shilling
    "lex.en.100k.013029": {"pos": "noun", "vi": "khăn liệm; bao phủ che khuất"},  # shroud
    "lex.en.100k.013030": {"vi": "người trông trẻ; người ngồi mẫu"},  # sitter
    "lex.en.100k.013031": {"vi": "lỏng lẻo; uể oải ế ẩm"},  # slack
    "lex.en.100k.013032": {"vi": "sự phỏng đoán; đầu cơ tích trữ"},  # speculation
    "lex.en.100k.013033": {"vi": "tình trạng trì trệ; đình đốn"},  # stagnation
    "lex.en.100k.013034": {"vi": "sự trì hoãn câu giờ; chết máy"},  # stalling
    "lex.en.100k.013035": {"vi": "thổi bùng ngọn lửa; khơi dậy"},  # stoke
    "lex.en.100k.013036": {"vi": "dây đeo; quai da buộc"},  # strap
    "lex.en.100k.013038": {"vi": "tinh gọn hóa; làm khí động học"},  # streamline
    "lex.en.100k.013041": {"vi": "thuộc khu vực ngoại ô"},  # suburban
    "lex.en.100k.013042": {"vi": "sự kế thừa; chuỗi liên tiếp"},  # succession
    "lex.en.100k.013044": {"vi": "ga cuối tuyến; bến cuối"},  # terminus
    "lex.en.100k.013045": {"pos": "verb", "vi": "tan băng; làm tan chảy; làm dịu"},  # thaw
    "lex.en.100k.013047": {"vi": "gây chấn thương; sang chấn tâm lý"},  # traumatic
    "lex.en.100k.013048": {"vi": "giá đỡ ba chân (máy ảnh)"},  # tripod
    "lex.en.100k.013049": {"vi": "đường cao tốc có thu phí"},  # turnpike
    "lex.en.100k.013050": {"pos": "verb", "vi": "co giật cơ nhẹ; co giật"},  # twitch

    # 3051-3100
    "lex.en.100k.013051": {"vi": "không có người trông coi; bỏ mặc"},  # unattended
    "lex.en.100k.013054": {"vi": "đã tháo đạn; đã dỡ hàng xuống"},  # unloaded
    "lex.en.100k.013055": {"vi": "không đủ tư cách; tuyệt đối không"},  # unqualified
    "lex.en.100k.013057": {"vi": "chưa được ký tên; vô danh"},  # unsigned
    "lex.en.100k.013059": {"vi": "nhân viên đỗ xe; người phục vụ"},  # valet
    "lex.en.100k.013060": {"vi": "mối thù truyền kiếp; huyết thù"},  # vendetta
    "lex.en.100k.013061": {"vi": "bác sĩ thú y"},  # veterinarian
    "lex.en.100k.013063": {"vi": "thuộc thời đại nữ hoàng Victoria"},  # victorian
    "lex.en.100k.013064": {"pos": "noun", "vi": "màu tím hoa cà; hoa violet"},  # violet
    "lex.en.100k.013065": {"vi": "chim kền kền ăn xác thối"},  # vulture
    "lex.en.100k.013067": {"vi": "xúc xích Vienna; lạp xưởng"},  # wiener
    "lex.en.100k.013069": {"vi": "tên riêng Catherine"},  # catherine
    "lex.en.100k.013071": {"vi": "tiểu bang Connecticut; chụp CT"},  # ct
    "lex.en.100k.013073": {"vi": "hãng Warner Bros; người báo trước"},  # warner
    "lex.en.100k.013074": {"vi": "những cây cầu; tên họ Bridges"},  # bridges
    "lex.en.100k.013075": {"vi": "vùng Holland; nước Hà Lan"},  # holland
    "lex.en.100k.013076": {"vi": "nước Bồ Đào Nha"},  # portugal
    "lex.en.100k.013077": {"vi": "lực lượng SS Đức quốc xã; tàu SS"},  # ss
    "lex.en.100k.013078": {"vi": "tên riêng Carlos"},  # carlos
    "lex.en.100k.013079": {"vi": "bang Dakota; bộ tộc Dakota"},  # dakota
    "lex.en.100k.013080": {"ipa": "/ˌɛf ˈɛl/", "vi": "tiểu bang Florida (viết tắt FL)"},  # fl
    "lex.en.100k.013081": {"vi": "tiếng Pháp (FR); nguyên tố franxi"},  # fr
    "lex.en.100k.013082": {"vi": "người Karen; phụ nữ khó tính"},  # karen
    "lex.en.100k.013083": {"vi": "tên riêng Lucas"},  # lucas
    "lex.en.100k.013084": {"vi": "tên họ Rogers"},  # rogers
    "lex.en.100k.013085": {"vi": "tên riêng Todd"},  # todd
    "lex.en.100k.013086": {"pos": "num", "vi": "số La Mã VI (sáu)"},  # vi (pos fixed)
    "lex.en.100k.013087": {"ipa": "/ˌdʌbəl.juː ˈaɪ/", "vi": "tiểu bang Wisconsin (viết tắt WI)"},  # wi
    "lex.en.100k.013088": {"vi": "quen thuộc với; đã quen nếp"},  # accustomed
    "lex.en.100k.013091": {"vi": "sự tha hóa; cảm giác xa lánh"},  # alienation (purged single-word 'tha hoá')
    "lex.en.100k.013093": {"vi": "sức quyến rũ; sức lôi cuốn"},  # allure
    "lex.en.100k.013094": {"vi": "chứng biếng ăn tâm thần"},  # anorexia
    "lex.en.100k.013095": {"vi": "bệnh than (nhiễm khuẩn)"},  # anthrax
    "lex.en.100k.013096": {"vi": "người học việc; người học nghề"},  # apprentice
    "lex.en.100k.013100": {"vi": "quái vật chân to (Bigfoot)"},  # bigfoot

    # 3101-3150
    "lex.en.100k.013102": {"vi": "trò bài xì dách; dùi cui bọc da"},  # blackjack
    "lex.en.100k.013103": {"vi": "dòng nhạc đồng quê bluegrass"},  # bluegrass
    "lex.en.100k.013105": {"vi": "cúi chào cung kính; khúm núm"},  # bowing
    "lex.en.100k.013108": {"vi": "hai bên mông; vùng mông"},  # buttocks
    "lex.en.100k.013109": {"vi": "mua lại toàn bộ doanh nghiệp"},  # buyout
    "lex.en.100k.013110": {"vi": "đơn vị byte dữ liệu (8 bit)"},  # byte
    "lex.en.100k.013112": {"vi": "đơn vị carat (đo đá quý/vàng)"},  # carat
    "lex.en.100k.013113": {"vi": "chất bột đường (carbohydrate)"},  # carbohydrate
    "lex.en.100k.013115": {"vi": "lỗ sâu răng; khoang rỗng cơ thể"},  # cavity
    "lex.en.100k.013117": {"vi": "việc vặt việc nhà thường ngày"},  # chore
    "lex.en.100k.013118": {"pos": "verb", "vi": "trích dẫn dẫn chứng; biểu dương"},  # cite
    "lex.en.100k.013119": {"vi": "bè phái hẹp hòi; nhóm khép kín"},  # clique
    "lex.en.100k.013120": {"vi": "nanh vuốt; sự kìm kẹp kiểm soát"},  # clutches
    "lex.en.100k.013121": {"vi": "con gián"},  # cockroach
    "lex.en.100k.013124": {"vi": "tính liên tục; sự tiếp nối"},  # continuity
    "lex.en.100k.013127": {"vi": "có đường cong nảy nở; uốn lượn"},  # curvy
    "lex.en.100k.013128": {"vi": "có tính tuần hoàn; mạch vòng"},  # cyclic
    "lex.en.100k.013130": {"vi": "sự qua đời; sự sụp đổ chấm dứt"},  # demise
    "lex.en.100k.013131": {"vi": "sự nới lỏng quy chế quản lý"},  # deregulation
    "lex.en.100k.013135": {"vi": "đã được thuần hóa; thích ở nhà"},  # domesticated
    "lex.en.100k.013138": {"vi": "bền bỉ; dùng được lâu dài"},  # durable
    "lex.en.100k.013140": {"vi": "tiên dược; thuốc trường sinh"},  # elixir
    "lex.en.100k.013141": {"vi": "giai đoạn tàn cuộc; ván cờ cuối"},  # endgame
    "lex.en.100k.013143": {"vi": "dụ dỗ; cám dỗ lôi kéo"},  # entice
    "lex.en.100k.013145": {"vi": "sự giác ngộ bất ngờ; lễ hiển linh"},  # epiphany
    "lex.en.100k.013146": {"vi": "cái chết nhân đạo; an tử"},  # euthanasia
    "lex.en.100k.013147": {"vi": "cuộc di cư hàng loạt lánh nạn"},  # exodus
    "lex.en.100k.013151": {"vi": "củi đun; gỗ đốt lửa"},  # firewood
    "lex.en.100k.013153": {"pos": "verb", "vi": "búng nhẹ; bộ phim; lướt nhanh qua"},  # flick
    "lex.en.100k.013155": {"pos": "noun", "vi": "cầu chì; ngòi nổ; hàn gắn kết hợp"},  # fuse

    # 3151-3200
    "lex.en.100k.013157": {"vi": "quý ông lịch lãm; đàn ông"},  # gent
    "lex.en.100k.013159": {"vi": "chó săn thỏ greyhound"},  # greyhound
    "lex.en.100k.013161": {"vi": "xe ngựa cho thuê; đồ dùng chung"},  # hackney
    "lex.en.100k.013163": {"vi": "tên riêng/họ Harrison"},  # harrison
    "lex.en.100k.013165": {"vi": "tên họ Hughes"},  # hughes
    "lex.en.100k.013167": {"vi": "nạn dịch sâu bọ; sự phá hoại"},  # infestation
    "lex.en.100k.013168": {"vi": "mang tính cung cấp thông tin"},  # informational
    "lex.en.100k.013171": {"vi": "bất an thiếu tự tin; không an toàn"},  # insecure
    "lex.en.100k.013172": {"vi": "cuộc nổi dậy khởi nghĩa vũ trang"},  # insurrection
    "lex.en.100k.013176": {"vi": "khoảng cách chữ (kerning đồ họa)"},  # kern
    "lex.en.100k.013177": {"ipa": "/ˈkɪləɡræm/", "vi": "ki-lô-gam (kg)"},  # kg
    "lex.en.100k.013180": {"vi": "địa chủ Scotland"},  # laird
    "lex.en.100k.013181": {"vi": "đồng tiền Lev (Bulgaria)"},  # lev
    "lex.en.100k.013185": {"vi": "sự thao túng; sự khéo léo xử lý"},  # manipulation
    "lex.en.100k.013186": {"vi": "ở vùng biên; không đáng kể"},  # marginal
    "lex.en.100k.013189": {"vi": "giai đoạn mãn kinh phụ nữ"},  # menopause
    "lex.en.100k.013192": {"vi": "mol (đơn vị đo lượng chất)"},  # mol
    "lex.en.100k.013193": {"pos": "verb", "vi": "tiếng bò kêu ò ò; rống"},  # moo
    "lex.en.100k.013195": {"vi": "bị cắt xén biến dạng; tàn tật"},  # mutilated
    "lex.en.100k.013196": {"vi": "hành vi chặt xén tàn phá thân thể"},  # mutilation
    "lex.en.100k.013199": {"vi": "cục vàng tự nhiên; miếng gà viên"},  # nugget
    "lex.en.100k.013200": {"vi": "thuộc về ngành nghề công việc"},  # occupational

    # 3201-3250
    "lex.en.100k.013202": {"vi": "tác phẩm nghệ thuật đồ sộ"},  # opus
    "lex.en.100k.013203": {"ipa": "/ˈɔːrɡənaɪzd/", "vi": "có tổ chức bài bản; ngăn nắp"},  # organised
    "lex.en.100k.013204": {"vi": "thuộc về cơ cấu tổ chức"},  # organizational
    "lex.en.100k.013207": {"vi": "nông dân nghèo; bần nông"},  # peasant
    "lex.en.100k.013209": {"vi": "bị rỗ mặt; đã bỏ hạt quả"},  # pitted
    "lex.en.100k.013210": {"vi": "mảng bám răng; bia tưởng niệm"},  # plaque
    "lex.en.100k.013212": {"vi": "chính trị gia lọc lõi"},  # politico
    "lex.en.100k.013214": {"vi": "người thuyết giáo; mục sư"},  # preacher
    "lex.en.100k.013216": {"vi": "tỉnh (Nhật Bản/Pháp); hạt quản lý"},  # prefecture
    "lex.en.100k.013218": {"vi": "kiêu căng khoe khoang; tự phụ"},  # pretentious
    "lex.en.100k.013219": {"vi": "thủ tục chứng thực di chúc"},  # probate
    "lex.en.100k.013220": {"vi": "thu mua; kiếm được vật tư"},  # procure
    "lex.en.100k.013221": {"vi": "đẩy tới trước; thúc đẩy tiến lên"},  # propel
    "lex.en.100k.013222": {"vi": "bác sĩ chuyên khoa tâm thần"},  # psychiatrist
    "lex.en.100k.013223": {"vi": "sự thuần khiết; độ tinh khiết"},  # purity
    "lex.en.100k.013228": {"vi": "làm mới lại; nạp lại năng lượng"},  # refresh
    "lex.en.100k.013230": {"vi": "từ xa; một chút mảy may nào"},  # remotely
    "lex.en.100k.013231": {"vi": "nhựa cây; nhựa tổng hợp resin"},  # resin
    "lex.en.100k.013233": {"vi": "chuỗi hạt mân côi (Công giáo)"},  # rosary
    "lex.en.100k.013235": {"vi": "mẹo lừa; thủ đoạn đánh lừa"},  # ruse (purged single-word 'mẹo')
    "lex.en.100k.013236": {"vi": "tàn nhẫn; nhẫn tâm không nể ai"},  # ruthless
    "lex.en.100k.013238": {"pos": "noun", "vi": "nhựa cây; làm kiệt quệ dần"},  # sap
    "lex.en.100k.013240": {"vi": "vỏ bọc ngoài; bao kiếm dao"},  # sheath (purged single-word 'vỏ')
    "lex.en.100k.013241": {"vi": "sự giản dị; tính đơn giản"},  # simplicity
    "lex.en.100k.013242": {"vi": "con ốc sên; người chậm chạp"},  # snail (purged single-word 'ốc')
    "lex.en.100k.013245": {"vi": "mẫu vật xét nghiệm; mẫu thí nghiệm"},  # specimen
    "lex.en.100k.013249": {"vi": "ghim bấm; mặt hàng chủ lực"},  # staple
    "lex.en.100k.013250": {"vi": "mạn phải của tàu thuyền"},  # starboard
    "lex.en.100k.013251": {"vi": "bụi sao vũ trụ; vẻ hào nhoáng"},  # stardust
    "lex.en.100k.013253": {"pos": "verb", "vi": "dáng đi vênh váo; thanh chống"},  # strut
    "lex.en.100k.013255": {"pos": "verb", "vi": "dáng đi nghênh ngang; vênh váo"},  # swagger
    "lex.en.100k.013256": {"pos": "verb", "vi": "cuộn xoáy; lượn vòng xoáy"},  # swirl
    "lex.en.100k.013257": {"vi": "chữ cái Hy Lạp theta (θ)"},  # theta
    "lex.en.100k.013258": {"vi": "dép kẹp xỏ ngón; quần lọt khe"},  # thong
    "lex.en.100k.013260": {"vi": "con cáo; trạng thái một mình"},  # tod
    "lex.en.100k.013263": {"vi": "dải đất rộng; bộ máy cơ quan ruột"},  # tract
    "lex.en.100k.013265": {"vi": "vùng nhiệt đới nóng ẩm"},  # tropics
    "lex.en.100k.013266": {"vi": "chưa được lập bản đồ; vùng đất lạ"},  # uncharted
    "lex.en.100k.013272": {"vi": "tử tước (tước vị quý tộc)"},  # viscount
    "lex.en.100k.013276": {"vi": "người thực hành yoga chuyên sâu"},  # yogi
    "lex.en.100k.013277": {"vi": "chữ cái Z (phát âm Mỹ)"},  # zee
    "lex.en.100k.013278": {"vi": "nước Áo (Austria)"},  # austria
    "lex.en.100k.013279": {"vi": "tên riêng Lucy; hóa thạch Lucy"},  # lucy
    "lex.en.100k.013280": {"vi": "thành phố Montréal (Canada)"},  # montreal
    "lex.en.100k.013281": {"vi": "thành phố Newcastle (Anh)"},  # newcastle
    "lex.en.100k.013282": {"vi": "bằng tiến sĩ (PhD)"},  # phd
    "lex.en.100k.013284": {"vi": "tên riêng/họ Spencer"},  # spencer
    "lex.en.100k.013285": {"vi": "nước Chi-lê (Chile)"},  # chile
    "lex.en.100k.013286": {"vi": "thám tử Sherlock Holmes; họ"},  # holmes
    "lex.en.100k.013287": {"vi": "người Nigeria; thuộc Nigeria"},  # nigerian
    "lex.en.100k.013288": {"vi": "quận Queens (New York)"},  # queens
    "lex.en.100k.013290": {"vi": "tên riêng Dylan (Bob Dylan)"},  # dylan
    "lex.en.100k.013291": {"vi": "băng giá lạnh buốt; đóng băng"},  # freezing
    "lex.en.100k.013293": {"vi": "tiểu bang Montana (Mỹ)"},  # montana
    "lex.en.100k.013294": {"ipa": "/ˌɛn ˈsiː/", "vi": "tiểu bang North Carolina (NC)"},  # nc
    "lex.en.100k.013295": {"vi": "tên riêng/họ Owen"},  # owen
    "lex.en.100k.013296": {"vi": "tên riêng/họ Wallace"},  # wallace
    "lex.en.100k.013299": {"vi": "protein actin (cơ học sợi)"},  # actin

    # 3251-3300
    "lex.en.100k.013301": {"vi": "ngành nhân chủng học"},  # anthropology
    "lex.en.100k.013302": {"vi": "thủy cung; bể nuôi cá cảnh"},  # aquarium
    "lex.en.100k.013305": {"vi": "người điều hành bán đấu giá"},  # auctioneer
    "lex.en.100k.013306": {"vi": "tác quyền; quyền tác giả bài viết"},  # authorship
    "lex.en.100k.013307": {"vi": "ngăn ngừa thảm họa; né tránh"},  # avert
    "lex.en.100k.013309": {"pos": "noun", "vi": "bột nhão làm bánh; đập túi bụi"},  # batter
    "lex.en.100k.013310": {"vi": "thiết giáp hạm hải quân"},  # battleship
    "lex.en.100k.013311": {"vi": "lưỡi lê gắn đầu súng"},  # bayonet
    "lex.en.100k.013312": {"vi": "vùng lạch nước đầm lầy (Mỹ)"},  # bayou
    "lex.en.100k.013313": {"pos": "adv", "vi": "từ trước; trước thời điểm đó"},  # beforehand
    "lex.en.100k.013315": {"vi": "tin sét đánh chấn động; cú sốc"},  # bombshell
    "lex.en.100k.013316": {"vi": "tên họ Brooks; những con suối"},  # brooks
    "lex.en.100k.013317": {"vi": "lạc quan giá tăng (thị trường bò)"},  # bullish
    "lex.en.100k.013318": {"vi": "đơn vị năng lượng calo"},  # calorie
    "lex.en.100k.013319": {"vi": "ác tính; gây ung thư"},  # cancerous
    "lex.en.100k.013320": {"vi": "thuyền ca-nô chèo tay; xuồng"},  # canoe
    "lex.en.100k.013321": {"vi": "người xướng ca nhà thờ"},  # cantor
    "lex.en.100k.013323": {"vi": "trứng cá muối thượng hạng (caviar)"},  # caviar
    "lex.en.100k.013324": {"vi": "chủ tọa; chủ tịch hội đồng"},  # chairperson
    "lex.en.100k.013325": {"vi": "lạnh lẽo cóng; lạnh buốt"},  # chilly (purged crawler 'ớt cay' typo)
    "lex.en.100k.013326": {"pos": "verb", "vi": "chuông hòa âm; tiếng chuông điểm"},  # chime
    "lex.en.100k.013327": {"vi": "lách luật; tìm cách né tránh"},  # circumvent
    "lex.en.100k.013330": {"vi": "thành phố Columbus; nhà thám hiểm"},  # columbus
    "lex.en.100k.013335": {"pos": "noun", "vi": "tù nhân thụ án; tuyên án kết tội"},  # convict
    "lex.en.100k.013336": {"vi": "tràng hoa (thực vật học)"},  # corolla
    "lex.en.100k.013337": {"vi": "lượn sóng dập nếp; tôn lượn sóng"},  # corrugated
    "lex.en.100k.013338": {"vi": "nhồi nhét; học nhồi nhét thi cử"},  # cram (purged single-word 'nhồi; nhét')
    "lex.en.100k.013340": {"vi": "chim cu cu; kẻ ngớ ngẩn điên khùng"},  # cuckoo
    "lex.en.100k.013342": {"vi": "hoài nghi cay độc; yếm thế"},  # cynical
    "lex.en.100k.013343": {"vi": "cây dã hương; trạm bưu điện Ấn"},  # dak
    "lex.en.100k.013345": {"vi": "đào sâu nghiên cứu; tìm tòi kỹ"},  # delve
    "lex.en.100k.013347": {"vi": "nước Đan Mạch"},  # denmark
    "lex.en.100k.013348": {"vi": "suy giảm chất lượng; tệ đi dần"},  # deteriorate
    "lex.en.100k.013350": {"vi": "quẫn trí hoảng loạn; đau buồn sâu"},  # distraught
    "lex.en.100k.013352": {"pos": "noun", "vi": "mưa phùn lất phất; rưới nhẹ"},  # drizzle
    "lex.en.100k.013355": {"vi": "tên họ Edwards"},  # edwards
    "lex.en.100k.013360": {"vi": "quỹ ngân khố quốc gia"},  # exchequer
    "lex.en.100k.013361": {"vi": "hết hạn hợp đồng; qua đời"},  # expire
    "lex.en.100k.013362": {"vi": "sự may mắn ngẫu nhiên; may rủi"},  # fluke
    "lex.en.100k.013364": {"vi": "nghị lực kiên cường; lòng quả cảm"},  # fortitude
    "lex.en.100k.013366": {"vi": "người theo chủ nghĩa giáo điều"},  # fundamentalist
    "lex.en.100k.013367": {"vi": "con bạc; tay cá cược đỏ đen"},  # gambler
    "lex.en.100k.013368": {"vi": "kẻ khổng lồ; gã khổng lồ Goliath"},  # goliath
    "lex.en.100k.013369": {"pos": "verb", "vi": "tiếng ủn ỉn; càu nhàu trong họng"},  # grunt
    "lex.en.100k.013370": {"vi": "người Di-gan (Romani du mục)"},  # gypsy
    "lex.en.100k.013372": {"vi": "mờ mịt sương khói; mơ hồ lơ mơ"},  # hazy
    "lex.en.100k.013373": {"vi": "loài ong bắp cày to"},  # hornet
    "lex.en.100k.013375": {"vi": "nói quá cường điệu; hình hypebol"},  # hyperbolic
    "lex.en.100k.013376": {"vi": "thói đạo đức giả; hành vi giả tạo"},  # hypocrisy
    "lex.en.100k.013378": {"vi": "trở kháng dòng điện (vật lý)"},  # impedance
    "lex.en.100k.013379": {"pos": "noun", "vi": "con dốc nghiêng; có khuynh hướng"},  # incline
    "lex.en.100k.013380": {"vi": "không thể hiểu nổi; quá khó hiểu"},  # incomprehensible
    "lex.en.100k.013384": {"vi": "huy hiệu; phù hiệu cấp bậc"},  # insignia
    "lex.en.100k.013386": {"vi": "trực quan; mang tính trực giác"},  # intuitive
    "lex.en.100k.013387": {"vi": "cuộc thi đấu theo lời mời"},  # invitational
    "lex.en.100k.013388": {"vi": "giao thức IP (mạng); sở hữu trí tuệ"},  # ip (purged crawler 'tin học')
    "lex.en.100k.013390": {"vi": "chất đồng vị phóng xạ (vật lý)"},  # isotope
    "lex.en.100k.013391": {"vi": "tranh ghép hình; máy cưa lọng"},  # jigsaw
    "lex.en.100k.013392": {"vi": "cây bách xù; quả bách xù"},  # juniper
    "lex.en.100k.013393": {"vi": "cùng huyết thống; có họ hàng gần"},  # kindred
    "lex.en.100k.013394": {"vi": "tàu vũ trụ đổ bộ bề mặt"},  # lander
    "lex.en.100k.013395": {"vi": "mối liên lạc; sĩ quan liên lạc"},  # liaison
    "lex.en.100k.013396": {"vi": "kẹo que mút có cán cầm"},  # lollipop
    "lex.en.100k.013397": {"vi": "dao rựa phát cỏ lớn"},  # machete
    "lex.en.100k.013398": {"vi": "con chồn nâu; áo lông chồn mink"},  # mink
    "lex.en.100k.013400": {"vi": "bài chuyên khảo khoa học"},  # monograph

    # 3301-3350
    "lex.en.100k.013402": {"vi": "chất nhầy; niêm dịch cơ thể"},  # mucus
    "lex.en.100k.013403": {"vi": "quả dâu tằm; cây dâu tằm"},  # mulberry (purged single-word 'dâu')
    "lex.en.100k.013404": {"vi": "thần thoại học; truyện thần thoại"},  # mythology
    "lex.en.100k.013406": {"vi": "nhà tự nhiên học; tự nhiên"},  # naturalist
    "lex.en.100k.013407": {"vi": "tiểu bang Nevada (Mỹ)"},  # nevada
    "lex.en.100k.013408": {"vi": "phòng biên tập; tòa soạn báo"},  # newsroom
    "lex.en.100k.013409": {"vi": "tê liệt mất cảm giác; đờ đẫn"},  # numb (purged single-word 'tê')
    "lex.en.100k.013410": {"vi": "tuyển tập gộp; xe buýt lớn"},  # omnibus
    "lex.en.100k.013412": {"vi": "thành phố Orlando"},  # orlando
    "lex.en.100k.013415": {"vi": "sự đàn áp ngược đãi; bách hại"},  # persecution
    "lex.en.100k.013416": {"vi": "chim bồ câu"},  # pigeon
    "lex.en.100k.013419": {"vi": "lớp ván ép mỏng; bện sợi vải"},  # ply
    "lex.en.100k.013420": {"vi": "săn trộm thú rừng; chần trứng"},  # poaching
    "lex.en.100k.013424": {"vi": "sáng tác nhiều; mắn đẻ màu mỡ"},  # prolific
    "lex.en.100k.013428": {"vi": "hiệu phó phụ trách đào tạo"},  # provost
    "lex.en.100k.013429": {"ipa": "/piː ˈtiː/", "vi": "nguyên tố bạch kim (Pt); điểm số"},  # pt
    "lex.en.100k.013430": {"vi": "cú gạt bóng trên green (golf)"},  # putt
    "lex.en.100k.013432": {"pos": "noun", "vi": "mỏ khai thác đá; con mồi bị săn"},  # quarry
    "lex.en.100k.013435": {"vi": "chim săn mồi; khủng long raptor"},  # raptor
    "lex.en.100k.013436": {"vi": "bánh cóc cơ khí; siết một chiều"},  # ratchet
    "lex.en.100k.013438": {"pos": "adj", "vi": "nói mê sảng; cuồng nhiệt tán tụng"},  # raving
    "lex.en.100k.013439": {"vi": "gặt hái mùa màng; thu hoạch"},  # reap (purged single-word 'gặt')
    "lex.en.100k.013441": {"pos": "noun", "vi": "đền bù bồi thường; khắc phục"},  # redress
    "lex.en.100k.013443": {"vi": "khả năng phục hồi; sức chống chịu"},  # resilience
    "lex.en.100k.013445": {"vi": "người nhân hậu (người Samari)"},  # samaritan
    "lex.en.100k.013448": {"vi": "kèn sắc-xô-phôn (saxophone)"},  # sax
    "lex.en.100k.013449": {"vi": "kèn sắc-xô-phôn (saxophone)"},  # saxophone
    "lex.en.100k.013450": {"vi": "thâm niên công tác; bậc trên"},  # seniority
    "lex.en.100k.013452": {"vi": "tiền trợ cấp thôi việc; sự cắt đứt"},  # severance
    "lex.en.100k.013453": {"vi": "mài sắc nhọn; trau dồi kỹ năng"},  # sharpen (purged single-word 'mài; vót')
    "lex.en.100k.013454": {"vi": "động vật có vỏ (nghêu sò ốc)"},  # shellfish
    "lex.en.100k.013455": {"vi": "phép viết tốc ký; cách nói tắt"},  # shorthand
    "lex.en.100k.013456": {"vi": "mảnh đạn pháo găm; miểng bom"},  # shrapnel
    "lex.en.100k.013457": {"vi": "trận thắng giữ sạch lưới"},  # shutout
    "lex.en.100k.013458": {"vi": "cái liềm gặt lúa (nông cụ)"},  # sickle (purged single-word 'liềm')
    "lex.en.100k.013459": {"vi": "điểm kỳ dị vũ trụ; tính độc nhất"},  # singularity
    "lex.en.100k.013461": {"pos": "noun", "vi": "thuốc lào hít; hít ngửi; dập tắt"},  # snuff
    "lex.en.100k.013462": {"vi": "giao lưu hòa nhập xã hội"},  # socialize
    "lex.en.100k.013464": {"vi": "bản đặc tả kỹ thuật; quy cách"},  # specification
    "lex.en.100k.013467": {"vi": "khắc kỷ; người kiên định nhẫn nại"},  # stoic
    "lex.en.100k.013468": {"pos": "noun", "vi": "thợ may đo; may theo yêu cầu"},  # tailor
    "lex.en.100k.013469": {"vi": "vùng lãnh thổ Đài Loan"},  # taiwan
    "lex.en.100k.013471": {"pos": "verb", "vi": "đánh đập dữ dội; quẫy đạp mạnh"},  # thrash
    "lex.en.100k.013476": {"vi": "không chính thống; phá cách lập dị"},  # unorthodox
    "lex.en.100k.013478": {"vi": "chứng chóng mặt ảo giác độ cao"},  # vertigo
    "lex.en.100k.013481": {"vi": "bị góa vợ/góa chồng"},  # widowed (purged single-word 'góa')
    "lex.en.100k.013486": {"vi": "hạt Yorkshire (nước Anh)"},  # yorkshire
    "lex.en.100k.013488": {"vi": "thủ đô Amsterdam (Hà Lan)"},  # amsterdam
    "lex.en.100k.013489": {"vi": "tiếng Ả Rập; thuộc văn hóa Ả Rập"},  # arabic
    "lex.en.100k.013490": {"vi": "tên họ Bennett"},  # bennett
    "lex.en.100k.013491": {"vi": "thành phố Bristol (Anh)"},  # bristol
    "lex.en.100k.013492": {"vi": "hệ thống định vị toàn cầu (GPS)"},  # gps
    "lex.en.100k.013493": {"vi": "sông Hudson; vịnh Hudson"},  # hudson
    "lex.en.100k.013494": {"vi": "tên riêng/họ Lloyd"},  # lloyd
    "lex.en.100k.013495": {"vi": "dặm trên giờ (mph)"},  # mph
    "lex.en.100k.013496": {"vi": "thánh Nicholas; tên Nicholas"},  # nicholas
    "lex.en.100k.013497": {"vi": "tiếng Bồ Đào Nha; người Bồ"},  # portuguese
    "lex.en.100k.013498": {"vi": "tiền tố Sr (Senior - cha); stronti"},  # sr
    "lex.en.100k.013499": {"ipa": "/ˈeɪprəl/", "vi": "tháng Tư (viết tắt Apr)"},  # apr
    "lex.en.100k.013500": {"vi": "nguyên tố vàng (Au); nước Úc (AU)"},  # au
}

# Verify lengths <= 35
for k, v in OVERRIDES_B03_R07.items():
    if "vi" in v:
        assert len(v["vi"]) <= 35, f"Length > 35 for {k}: {v['vi']} ({len(v['vi'])})"

with open('content/english/qa-batches/batch-03.json', 'r', encoding='utf-8') as f:
    batch_data = json.load(f)

# Apply overrides to records in range 3000 to 3500
count = 0
for idx in range(3000, 3500):
    rec = batch_data['records'][idx]
    rid = rec['id']
    if rid in OVERRIDES_B03_R07:
        count += 1
        for field, val in OVERRIDES_B03_R07[rid].items():
            rec[field] = val
        rec['status'] = 'reviewed'

batch_data['reviewedCount'] = 3500

with open('content/english/qa-batches/batch-03.json', 'w', encoding='utf-8') as f:
    json.dump(batch_data, f, ensure_ascii=False, indent=2)

print(f"Successfully applied Batch 03 Round 7 ({count} overrides). Reviewed: {batch_data['reviewedCount']}/5000.")
