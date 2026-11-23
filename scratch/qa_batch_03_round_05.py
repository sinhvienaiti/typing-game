import json

# Round 5 overrides (records 2000 to 2500, STT 2001 to 2500, IDs lex.en.100k.012001 to 012500)
OVERRIDES_B03_R05 = {
    # 2001-2050
    "lex.en.100k.012001": {"vi": "võ sĩ Muhammad Ali; tên Ali"},  # ali
    "lex.en.100k.012002": {"vi": "thiện chí; sự ủng hộ; ân huệ"},  # favour
    "lex.en.100k.012003": {"vi": "tên họ/thành phố Hamilton"},  # hamilton
    "lex.en.100k.012005": {"vi": "tên riêng Jonathan; giống táo"},  # jonathan
    "lex.en.100k.012006": {"vi": "tên riêng/họ Lawrence"},  # lawrence
    "lex.en.100k.012007": {"vi": "Tổng thống Lincoln; thành phố"},  # lincoln
    "lex.en.100k.012010": {"vi": "giải thưởng điện ảnh Oscar"},  # oscar
    "lex.en.100k.012011": {"vi": "thuộc vương quốc Ả Rập Xê Út"},  # saudi
    "lex.en.100k.012013": {"vi": "tỷ phú Bill Gates; các cánh cổng"},  # gates
    "lex.en.100k.012014": {"vi": "nhà leo núi Hillary; tên riêng"},  # hillary
    "lex.en.100k.012018": {"vi": "Nam Phi; Nam Úc (viết tắt SA)"},  # sa
    "lex.en.100k.012019": {"vi": "tháng Mười Hai (viết tắt Dec)"},  # dec
    "lex.en.100k.012021": {"pos": "num", "vi": "năm mươi (50)"},  # fifty (pos fixed)
    "lex.en.100k.012022": {"ipa": "/ˌɛm ˈpiː/", "vi": "nghị sĩ quốc hội; cảnh sát quân"},  # mp
    "lex.en.100k.012024": {"vi": "hướng đông nam; nguyên tố selen"},  # se
    "lex.en.100k.012027": {"vi": "Tổng thống Kennedy; họ Kennedy"},  # kennedy
    "lex.en.100k.012029": {"vi": "tên họ Moore"},  # moore
    "lex.en.100k.012030": {"vi": "Đảng Quốc xã; phát xít Đức"},  # nazi
    "lex.en.100k.012032": {"vi": "tên riêng Philip"},  # philip
    "lex.en.100k.012033": {"vi": "tên họ Thompson"},  # thompson
    "lex.en.100k.012035": {"vi": "chất mài mòn; thô lỗ cộc cằn"},  # abrasive
    "lex.en.100k.012036": {"vi": "nhạc đệm; món ăn phụ kèm theo"},  # accompaniment
    "lex.en.100k.012038": {"vi": "nhận nuôi (bố mẹ nuôi); dưỡng phụ"},  # adoptive (purged single-word 'nuôi')
    "lex.en.100k.012041": {"vi": "thuộc dòng dõi quý tộc"},  # aristocratic
    "lex.en.100k.012042": {"vi": "sự đình chiến; hiệp định hưu chiến"},  # armistice
    "lex.en.100k.012044": {"vi": "sự bảo trợ; sự đỡ đầu tài trợ"},  # auspices
    "lex.en.100k.012047": {"vi": "dịch mật; sự cáu gắt tức tối"},  # bile (purged single-word 'mật')
    "lex.en.100k.012049": {"vi": "âm vô thanh; thở nhẹ ra"},  # breathed
    "lex.en.100k.012050": {"vi": "muối cacbonat; sục khí ga"},  # carbonate
    "lex.en.100k.012051": {"vi": "thuộc chất xúc tác; gây xúc tác"},  # catalytic
    "lex.en.100k.012053": {"vi": "bánh phô mai (cheesecake)"},  # cheesecake
    "lex.en.100k.012057": {"vi": "liên minh bang; phe miền Nam Mỹ"},  # confederacy
    "lex.en.100k.012060": {"vi": "cũi trẻ em; giường bạt gấp"},  # cot
    "lex.en.100k.012061": {"vi": "kỷ Phấn Trắng (địa chất)"},  # cretaceous
    "lex.en.100k.012062": {"vi": "nồi nấu kim loại; chén nung"},  # crucible
    "lex.en.100k.012064": {"vi": "không gian mạng Internet"},  # cyberspace
    "lex.en.100k.012065": {"vi": "người máy sinh học (cyborg)"},  # cyborg
    "lex.en.100k.012066": {"pos": "verb", "vi": "màn ra mắt; lần đầu xuất hiện"},  # debut
    "lex.en.100k.012067": {"vi": "suy luận; suy đoán logic"},  # deduce
    "lex.en.100k.012071": {"vi": "nhà máy chưng cất rượu"},  # distillery
    "lex.en.100k.012072": {"pos": "verb", "vi": "hạ cấp; giảm mức đánh giá"},  # downgrade
    "lex.en.100k.012075": {"vi": "thập niên 80; tuổi tám mươi"},  # eighties
    "lex.en.100k.012081": {"vi": "phun trào núi lửa; bùng phát"},  # erupt
    "lex.en.100k.012082": {"vi": "thuộc gia đình; tính di truyền"},  # familial
    "lex.en.100k.012083": {"vi": "phân người/động vật; chất thải"},  # feces (purged crude 'cứt')
    "lex.en.100k.012084": {"vi": "phần sụn hệ thống (firmware)"},  # firmware
    "lex.en.100k.012085": {"vi": "ngành ngư nghiệp; nghề đánh cá"},  # fishery
    "lex.en.100k.012088": {"vi": "hậu vệ biên; hậu vệ quét bóng đá"},  # fullback
    "lex.en.100k.012089": {"vi": "thước đo; vật bảo đảm; đo lường"},  # gage
    "lex.en.100k.012090": {"vi": "thuyền buồm cổ; bếp trên tàu"},  # galley
    "lex.en.100k.012091": {"vi": "chóng mặt hoa mắt; phấn khích"},  # giddy
    "lex.en.100k.012092": {"vi": "được tôn vinh; được tán dương"},  # glorified
    "lex.en.100k.012095": {"vi": "bằng đồ thị; một cách sinh động"},  # graphically
    "lex.en.100k.012096": {"vi": "đấu vật giáp lá cà; vật lộn"},  # grappling
    "lex.en.100k.012098": {"pos": "verb", "vi": "nuốt ực một ngụm; hớp ngụm lớn"},  # gulp
    "lex.en.100k.012099": {"vi": "cây sơn tra; quả táo gai"},  # hawthorn (purged single-word 'sơn tra')
    "lex.en.100k.012100": {"vi": "hiếu khách; điều kiện thuận lợi"},  # hospitable

    # 2101-2150
    "lex.en.100k.012101": {"vi": "tiếng vo ve; tiếng ngâm nga hát"},  # humming
    "lex.en.100k.012103": {"vi": "ngâm mình; đắm chìm hoàn toàn"},  # immerse (purged single-word 'nhúng')
    "lex.en.100k.012107": {"vi": "vi phạm bản quyền; xâm phạm luật"},  # infringe
    "lex.en.100k.012109": {"vi": "đường ruột (nội tạng cơ thể)"},  # intestine (purged single-word 'ruột')
    "lex.en.100k.012111": {"vi": "ngôn ngữ đơn lập; mang tính cô lập"},  # isolating
    "lex.en.100k.012112": {"vi": "áo len; áo thi đấu thể thao"},  # jersey
    "lex.en.100k.012113": {"vi": "trò tung hứng nghệ thuật"},  # juggling
    "lex.en.100k.012114": {"vi": "khớp đốt ngón tay; móng heo"},  # knuckle
    "lex.en.100k.012115": {"pos": "noun", "vi": "người đoạt giải thưởng vinh dự"},  # laureate
    "lex.en.100k.012117": {"vi": "ban hành luật; làm luật lập pháp"},  # legislate
    "lex.en.100k.012119": {"vi": "dây cứu sinh; phao cứu mạng"},  # lifeline
    "lex.en.100k.012120": {"vi": "công nhân đường dây; cầu thủ biên"},  # lineman
    "lex.en.100k.012124": {"vi": "chứng suy dinh dưỡng"},  # malnutrition
    "lex.en.100k.012125": {"pos": "noun", "vi": "kẻ cuồng loạn; người điên cuồng"},  # maniac
    "lex.en.100k.012128": {"vi": "gốc metyl (hóa học hữu cơ)"},  # methyl
    "lex.en.100k.012129": {"vi": "vô tâm; ngớ ngẩn; không suy nghĩ"},  # mindless (purged single-word 'vô tri')
    "lex.en.100k.012130": {"vi": "khoa thần kinh học"},  # neurology
    "lex.en.100k.012131": {"pos": "verb", "vi": "huých nhẹ cùi chỏ; khích lệ"},  # nudge
    "lex.en.100k.012134": {"vi": "tràn ngập; đầy tràn ra ngoài"},  # overflowing
    "lex.en.100k.012137": {"vi": "phòng/tủ chứa thực phẩm khô"},  # pantry
    "lex.en.100k.012138": {"vi": "giấy da cừu (viết chữ)"},  # parchment
    "lex.en.100k.012140": {"vi": "chế độ phụ hệ; tính gia trưởng"},  # patriarchal
    "lex.en.100k.012141": {"vi": "người thanh toán; bên trả tiền"},  # payer
    "lex.en.100k.012142": {"vi": "hành vi đạo văn; ăn cắp ý tưởng"},  # plagiarism
    "lex.en.100k.012143": {"vi": "cây xén cành sát thân; tỉa cành"},  # pollard
    "lex.en.100k.012144": {"pos": "noun", "vi": "điều kiện tiên quyết; thiết yếu"},  # prerequisite
    "lex.en.100k.012146": {"vi": "phần mở đầu; lời tựa tác phẩm"},  # prologue
    "lex.en.100k.012147": {"vi": "tiền tố sơ khai; dạng nguyên thủy"},  # proto
    "lex.en.100k.012148": {"vi": "ngôi làng cổ người da đỏ Pueblo"},  # pueblo
    "lex.en.100k.012149": {"vi": "bục giảng trong nhà thờ"},  # pulpit
    "lex.en.100k.012150": {"vi": "báo sư tử Bắc Mỹ (puma)"},  # puma
    "lex.en.100k.012151": {"vi": "lỗ thủng săm lốp; vết đâm thủng"},  # puncture
    "lex.en.100k.012152": {"pos": "verb", "vi": "tỏa ra; phát nhiệt; phát xạ"},  # radiate
    "lex.en.100k.012153": {"vi": "người có tóc màu đỏ hung"},  # redhead
    "lex.en.100k.012155": {"vi": "cách biệt; xa cách; đã dời đi"},  # removed
    "lex.en.100k.012156": {"vi": "kẻ phản bội tổ chức; kẻ nổi loạn"},  # renegade
    "lex.en.100k.012159": {"vi": "kẻ sát nhân xé xác (ripper)"},  # ripper
    "lex.en.100k.012161": {"vi": "loài cá rudd (cá nước ngọt)"},  # rudd
    "lex.en.100k.012162": {"vi": "kẻ keo kiệt bủn xỉn (nhân vật)"},  # scrooge
    "lex.en.100k.012164": {"vi": "vải dệt thoi serge"},  # serge
    "lex.en.100k.012165": {"vi": "bài số bảy; bóng bầu dục 7 người"},  # sevens
    "lex.en.100k.012166": {"vi": "bình lắc pha chế; bình rắc gia vị"},  # shaker
    "lex.en.100k.012167": {"vi": "pháp sư saman giáo; thầy cúng"},  # shaman
    "lex.en.100k.012168": {"vi": "lá chắn bảo vệ; sự che chở chắn"},  # shielding
    "lex.en.100k.012169": {"vi": "hành vi trộm cắp tại cửa hàng"},  # shoplifting
    "lex.en.100k.012170": {"vi": "sơ sài; mờ ám đáng ngờ"},  # sketchy
    "lex.en.100k.012171": {"vi": "bùn đặc; chất cặn bã quánh"},  # sludge
    "lex.en.100k.012172": {"vi": "hàng buôn lậu; nhập lậu trái phép"},  # smuggled (purged single-word 'lậu')
    "lex.en.100k.012173": {"vi": "lượng tuyết rơi; trận tuyết"},  # snowfall
    "lex.en.100k.012175": {"vi": "độ mềm mại; tính dịu dàng"},  # softness
    "lex.en.100k.012176": {"vi": "thể thơ mười bốn câu (sonnet)"},  # sonnet
    "lex.en.100k.012177": {"vi": "đường đua xe tốc độ cao"},  # speedway
    "lex.en.100k.012179": {"pos": "verb", "vi": "bắn tia nước; phun phọt ra"},  # squirt
    "lex.en.100k.012181": {"vi": "cáng cứu thương; băng ca y tế"},  # stretcher
    "lex.en.100k.012185": {"vi": "lời mỉa mai; trêu ngươi chế giễu"},  # taunt
    "lex.en.100k.012186": {"vi": "có ren ốc vặn; được xâu chuỗi"},  # threaded
    "lex.en.100k.012187": {"vi": "hình thu nhỏ; móng ngón tay cái"},  # thumbnail
    "lex.en.100k.012188": {"vi": "ngăn kéo đựng tiền quầy thu ngân"},  # till
    "lex.en.100k.012189": {"vi": "màu sắc nhạt; nhuộm phớt nhẹ"},  # tint
    "lex.en.100k.012190": {"vi": "hành hạ dã man; sự tra tấn"},  # torturing
    "lex.en.100k.012191": {"vi": "Hội Tam Hoàng; bộ ba liên kết"},  # triad
    "lex.en.100k.012192": {"vi": "cắt tỉa gọn; chi tiết trang trí"},  # trimming
    "lex.en.100k.012194": {"vi": "gay go; đòi hỏi sự nhẫn nại"},  # trying
    "lex.en.100k.012199": {"vi": "đã cởi quần áo; không mặc gì"},  # undressed
    "lex.en.100k.012200": {"vi": "thiếu giáo dục; ít học thức"},  # uneducated

    # 2201-2250
    "lex.en.100k.012206": {"vi": "sự dũng cảm; lòng quả cảm"},  # valor
    "lex.en.100k.012207": {"vi": "tiếng bản địa; tiếng địa phương"},  # vernacular
    "lex.en.100k.012210": {"vi": "tranh màu nước; màu nước"},  # watercolor
    "lex.en.100k.012211": {"vi": "thoảng mùi; làn gió nhẹ thổi"},  # whiff
    "lex.en.100k.012212": {"vi": "sinh vật; người sống; đảo Wight"},  # wight
    "lex.en.100k.012213": {"pos": "verb", "vi": "héo rũ úa tàn; lụi tàn dần"},  # wilt
    "lex.en.100k.012214": {"vi": "người thợ; công nhân lao động"},  # workman (purged single-word 'thợ')
    "lex.en.100k.012217": {"ipa": "/ˌsɛntɪˈmiːtər/", "vi": "xen-ti-mét (cm)"},  # cm (added ipa)
    "lex.en.100k.012218": {"vi": "tập đoàn; công ty (viết tắt Corp)"},  # corp
    "lex.en.100k.012219": {"vi": "nữ thần Isis; tổ chức khủng bố"},  # isis
    "lex.en.100k.012221": {"vi": "sông Murray; tên họ Murray"},  # murray
    "lex.en.100k.012227": {"vi": "nhận ra; hiện thực hóa ý tưởng"},  # realise
    "lex.en.100k.012228": {"ipa": "/vɚˈdʒɪnjə/", "vi": "bang Virginia (viết tắt VA)"},  # va (added ipa)
    "lex.en.100k.012229": {"vi": "dòng điện xoay chiều; máy lạnh"},  # ac
    "lex.en.100k.012230": {"vi": "tên riêng/họ Adams"},  # adams
    "lex.en.100k.012232": {"vi": "chất DES (diethylstilbestrol)"},  # des
    "lex.en.100k.012235": {"vi": "tên họ Stewart"},  # stewart
    "lex.en.100k.012236": {"vi": "tên họ Wells; các giếng nước"},  # wells
    "lex.en.100k.012237": {"vi": "bảng chữ cái; điều cơ bản sơ đẳng"},  # abc
    "lex.en.100k.012240": {"vi": "sự ồn ào phiền hà; náo động"},  # ado
    "lex.en.100k.012242": {"vi": "thoáng khí; nhẹ bẫng ung dung"},  # airy
    "lex.en.100k.012243": {"vi": "tên riêng Albert"},  # albert
    "lex.en.100k.012244": {"vi": "thuộc về giải phẫu học cơ thể"},  # anatomical
    "lex.en.100k.012248": {"vi": "thuộc các thánh tông đồ"},  # apostolic
    "lex.en.100k.012253": {"vi": "công việc tồn đọng; hàng ứ đọng"},  # backlog
    "lex.en.100k.012255": {"pos": "prep", "vi": "ở dưới; thấp hơn; không xứng đáng"},  # beneath
    "lex.en.100k.012256": {"vi": "may đo riêng; theo đơn đặt hàng"},  # bespoke
    "lex.en.100k.012258": {"vi": "người cản trở; cầu thủ chặn bóng"},  # blocker
    "lex.en.100k.012259": {"vi": "sai lầm ngớ ngẩn; sự cương cứng"},  # boner
    "lex.en.100k.012261": {"vi": "bị làm hỏng; vụng về hỏng bét"},  # botched
    "lex.en.100k.012263": {"vi": "bánh brownie sô-cô-la; gia thần"},  # brownie
    "lex.en.100k.012264": {"vi": "số lượng lớn; hàng rời bán buôn"},  # bulk
    "lex.en.100k.012266": {"vi": "vết bỏng; tên họ Burns"},  # burns
    "lex.en.100k.012268": {"vi": "vòng quay ngựa gỗ; băng chuyền"},  # carousel
    "lex.en.100k.012269": {"vi": "hãng vận tải; người mang mầm bệnh"},  # carrier
    "lex.en.100k.012271": {"vi": "giống chó nhỏ Chihuahua; bang"},  # chihuahua
    "lex.en.100k.012272": {"vi": "bí mật; lén lút giấu giếm"},  # clandestine
    "lex.en.100k.012276": {"vi": "phân hữu cơ ủ mục; ủ phân"},  # compost
    "lex.en.100k.012277": {"pos": "noun", "vi": "chiêu lừa đảo; mặt bất lợi"},  # con
    "lex.en.100k.012278": {"vi": "giam giữ; hạn chế trong phạm vi"},  # confine (purged single-word 'nhốt')
    "lex.en.100k.012281": {"vi": "quân đoàn; đoàn thể chuyên môn"},  # corps
    "lex.en.100k.012282": {"vi": "đồng bào cùng nước; người nhà quê"},  # countryman
    "lex.en.100k.012283": {"vi": "độ bao phủ mạng; đưa tin báo chí"},  # coverage
    "lex.en.100k.012285": {"vi": "chiến binh thập tự; người đấu tranh"},  # crusader
    "lex.en.100k.012286": {"vi": "thần tình yêu Cupid; thần Ái Tình"},  # cupid
    "lex.en.100k.012287": {"vi": "độ cong; đường uốn cong"},  # curvature
    "lex.en.100k.012288": {"vi": "mức cắt giảm; thời hạn chót"},  # cutoff
    "lex.en.100k.012289": {"vi": "hoa bồ công anh"},  # dandelion
    "lex.en.100k.012291": {"vi": "hoãn lại; phục tùng theo ý"},  # defer
    "lex.en.100k.012294": {"vi": "bị biến dạng; méo mó dị dạng"},  # deformed (purged single-word 'méo mó')
    "lex.en.100k.012295": {"vi": "tạm giữ; câu lưu; giữ lại"},  # detain
    "lex.en.100k.012296": {"vi": "hệ thống chẩn đoán; phép chẩn đoán"},  # diagnostics
    "lex.en.100k.012297": {"vi": "giải trừ vũ khí; tước vũ khí"},  # disarm (purged crawler absurd 'tài binh')

    # 2251-2300
    "lex.en.100k.012302": {"vi": "khai sáng; soi sáng; giải thích rõ"},  # enlighten
    "lex.en.100k.012303": {"pos": "verb", "vi": "đòi hỏi phải có; dẫn đến hệ quả"},  # entail
    "lex.en.100k.012305": {"vi": "thuộc vùng xích đạo; xích đạo"},  # equatorial
    "lex.en.100k.012308": {"vi": "thập niên 50; độ tuổi năm mươi"},  # fifties
    "lex.en.100k.012309": {"vi": "mảnh vụn mỏng; bong tróc từng mảng"},  # flake
    "lex.en.100k.012310": {"vi": "cánh tà máy bay; vạt áo rủ"},  # flaps
    "lex.en.100k.012311": {"vi": "lông tơ; xơ vải; chuyện vụn vặt"},  # fluff
    "lex.en.100k.012314": {"vi": "thơm ngát; ngát hương thơm"},  # fragrant (purged single-word 'thơm')
    "lex.en.100k.012316": {"vi": "cơ quan sinh dục ngoài (y học)"},  # genitals
    "lex.en.100k.012317": {"vi": "nhà địa chất học"},  # geologist
    "lex.en.100k.012318": {"vi": "thần lùn giữ của; câu châm ngôn"},  # gnome
    "lex.en.100k.012321": {"vi": "khuôn viên đất; lý lẽ căn cứ"},  # grounds
    "lex.en.100k.012322": {"vi": "thần Hades; cõi âm phủ địa ngục"},  # hades
    "lex.en.100k.012324": {"vi": "Đại học Harvard danh tiếng"},  # harvard
    "lex.en.100k.012328": {"vi": "khiếm nhã; bất lịch sự thô tục"},  # indecent
    "lex.en.100k.012331": {"vi": "thuộc về ion; phong cách Ionic"},  # ionic
    "lex.en.100k.012333": {"vi": "tiếng leng keng; nhạc quảng cáo"},  # jingle
    "lex.en.100k.012334": {"vi": "nữ thần Kali; muối kali"},  # kali
    "lex.en.100k.012335": {"vi": "vật liệu bọc cách nhiệt; tụt hậu"},  # lagging
    "lex.en.100k.012338": {"vi": "tỏi tây; hành boa-rô"},  # leek
    "lex.en.100k.012340": {"vi": "vùng Levant; bỏ trốn quỵt nợ"},  # levant
    "lex.en.100k.012341": {"vi": "quyền cầm giữ; quyền lưu giữ"},  # lien
    "lex.en.100k.012342": {"vi": "điên rồ; mất trí (tiếng lóng)"},  # loco
    "lex.en.100k.012343": {"vi": "bị cướp phá; bị hôi của"},  # looted
    "lex.en.100k.012345": {"vi": "dịch bạch huyết (y học)"},  # lymph
    "lex.en.100k.012346": {"vi": "cây hoa mộc lan; ngọc lan"},  # magnolia
    "lex.en.100k.012347": {"vi": "tên riêng/họ Marshall"},  # marshall
    "lex.en.100k.012350": {"vi": "ghi nhớ; học thuộc lòng kỹ"},  # memorize
    "lex.en.100k.012351": {"vi": "thuộc kinh nguyệt phụ nữ"},  # menstrual
    "lex.en.100k.012353": {"vi": "tên họ Mitchell"},  # mitchell
    "lex.en.100k.012355": {"pos": "verb", "vi": "lầm bầm; nói lí nhí trong miệng"},  # mumble
    "lex.en.100k.012356": {"pos": "verb", "vi": "thì thầm; tiếng rì rầm; tiếng tim"},  # murmur
    "lex.en.100k.012358": {"vi": "có thể thương lượng; chuyển nhượng"},  # negotiable
    "lex.en.100k.012360": {"vi": "ám ảnh tâm trí; luôn bận tâm"},  # obsess
    "lex.en.100k.012363": {"vi": "đền thờ các vị thần; đền Pantheon"},  # pantheon
    "lex.en.100k.012366": {"pos": "verb", "vi": "cái cày; cày xới ruộng đất"},  # plow (purged single-word 'cày')
    "lex.en.100k.012367": {"vi": "nước Ba Lan"},  # poland
    "lex.en.100k.012368": {"vi": "sự lịch thiệp; phép lịch sự"},  # politeness
    "lex.en.100k.012369": {"vi": "thể chế nhà nước; chính thể"},  # polity
    "lex.en.100k.012371": {"pos": "adj", "vi": "thủ tướng; hàng đầu thứ nhất"},  # premier
    "lex.en.100k.012378": {"vi": "phản động; cực kỳ bảo thủ"},  # reactionary
    "lex.en.100k.012380": {"vi": "phục dựng; tái thiết xây lại"},  # reconstruct
    "lex.en.100k.012381": {"vi": "gỗ cự sam; cây hồng sam Bắc Mỹ"},  # redwood
    "lex.en.100k.012385": {"vi": "nhụy hoa nghệ tây (saffron)"},  # saffron
    "lex.en.100k.012386": {"vi": "ranh mãnh; tinh nghịch xấc xược"},  # sassy
    "lex.en.100k.012387": {"vi": "nam sinh; học sinh nam"},  # schoolboy
    "lex.en.100k.012389": {"vi": "sự phân khúc thị trường; phân đoạn"},  # segmentation
    "lex.en.100k.012391": {"vi": "người gửi thư/hàng; nơi gửi"},  # sender
    "lex.en.100k.012393": {"vi": "bị làm nhục; xấu hổ ê chề"},  # shamed
    "lex.en.100k.012395": {"vi": "thanh trượt giao diện; bánh kẹp"},  # slider
    "lex.en.100k.012396": {"vi": "thân tế bào soma; thần dược cổ"},  # soma
    "lex.en.100k.012398": {"vi": "tính cụ thể; độ đặc hiệu (y học)"},  # specificity
    "lex.en.100k.012399": {"vi": "nhuộm màu tế bào; vết ố bẩn"},  # staining
    "lex.en.100k.012400": {"vi": "bị rình rập; có cuống thân"},  # stalked

    # 2401-2500
    "lex.en.100k.012406": {"vi": "tiểu lục địa (Ấn Độ)"},  # subcontinent
    "lex.en.100k.012408": {"vi": "siêu cường quốc; cường quốc lớn"},  # superpower
    "lex.en.100k.012409": {"vi": "sự hiệp lực; tác động cộng hưởng"},  # synergy
    "lex.en.100k.012410": {"vi": "tật máy cơ; chứng co giật cơ nhẹ"},  # tic
    "lex.en.100k.012411": {"vi": "sự mệt mỏi; tình trạng kiệt sức"},  # tiredness
    "lex.en.100k.012412": {"vi": "cuốn sách lớn dày cộp; pho sách"},  # tome
    "lex.en.100k.012413": {"vi": "tấn (đơn vị khối lượng 1000kg)"},  # tonne
    "lex.en.100k.012414": {"vi": "sự cấy ghép mô/tạng (y học)"},  # transplantation
    "lex.en.100k.012415": {"pos": "verb", "vi": "chạy nước kiệu; đi bước ngắn"},  # trot
    "lex.en.100k.012420": {"vi": "lễ khánh thành; sự ra mắt hé lộ"},  # unveiling
    "lex.en.100k.012424": {"vi": "sử dụng vũ khí; nắm giữ quyền lực"},  # wield
    "lex.en.100k.012426": {"vi": "tên riêng Aaron"},  # aaron
    "lex.en.100k.012430": {"vi": "dòng họ Campbell; súp Campbell"},  # campbell
    "lex.en.100k.012432": {"vi": "DJ; người chỉnh nhạc đĩa"},  # dj
    "lex.en.100k.012433": {"vi": "tên riêng Jacob"},  # jacob
    "lex.en.100k.012434": {"vi": "chòm sao Sư Tử; tên riêng Leo"},  # leo
    "lex.en.100k.012435": {"vi": "tên riêng/họ Parker; bút Parker"},  # parker
    "lex.en.100k.012441": {"vi": "đã bị hủy bỏ; hủy hẹn"},  # cancelled
    "lex.en.100k.012442": {"vi": "tên riêng Christopher"},  # christopher
    "lex.en.100k.012443": {"vi": "tên họ Evans"},  # evans
    "lex.en.100k.012444": {"ipa": "/ˌdʒiː oʊ ˈpiː/", "vi": "Đảng Cộng hòa Mỹ (GOP)"},  # gop
    "lex.en.100k.012445": {"vi": "tên riêng Oliver"},  # oliver
    "lex.en.100k.012446": {"vi": "tên riêng/họ Perry"},  # perry
    "lex.en.100k.012447": {"vi": "tên riêng Ron; tiếng Ron"},  # ron
    "lex.en.100k.012449": {"vi": "Cơ quan Tình báo Mỹ (CIA)"},  # cia
    "lex.en.100k.012450": {"vi": "tên riêng/họ Douglas"},  # douglas
    "lex.en.100k.012453": {"vi": "Cơ quan Vũ trụ Mỹ (NASA)"},  # nasa
    "lex.en.100k.012456": {"vi": "tên họ Robinson"},  # robinson
    "lex.en.100k.012460": {"vi": "nốt nhạc Fa; Hiệp hội bóng đá Anh"},  # fa
    "lex.en.100k.012461": {"pos": "num", "vi": "bốn mươi (40)"},  # forty (pos fixed)
    "lex.en.100k.012462": {"vi": "nguồn nhân lực (HR); giờ đồng hồ"},  # hr
    "lex.en.100k.012464": {"vi": "bác sĩ y khoa (MD); bang Maryland"},  # md
    "lex.en.100k.012465": {"vi": "tên họ Wright; thợ chế tạo"},  # wright
    "lex.en.100k.012466": {"vi": "người ái mộ; người hâm mộ"},  # admirer
    "lex.en.100k.012471": {"pos": "adj", "vi": "nghiệp dư; không chuyên"},  # amateur
    "lex.en.100k.012472": {"vi": "giai thoại; mẩu chuyện ngắn thú vị"},  # anecdote
    "lex.en.100k.012477": {"vi": "gia tăng; tăng cường; bổ sung"},  # augment
    "lex.en.100k.012478": {"vi": "phía mặt sau; phần hông mông"},  # backside (purged crude 'đít')
    "lex.en.100k.012481": {"vi": "vụ nổ lốp xe; trận thắng áp đảo"},  # blowout
    "lex.en.100k.012487": {"pos": "noun", "vi": "hiến chương; điều lệ; thuê chuyến"},  # charter
    "lex.en.100k.012488": {"pos": "noun", "vi": "cơn ớn lạnh; thư giãn; lạnh buốt"},  # chill
    "lex.en.100k.012489": {"vi": "máng trượt xả rác; dù nhảy"},  # chute
    "lex.en.100k.012490": {"vi": "thủ thuật cắt bao quy đầu"},  # circumcision
    "lex.en.100k.012494": {"vi": "bộ máy đồng hồ; chạy trơn tru"},  # clockwork
    "lex.en.100k.012495": {"pos": "noun", "vi": "cục máu đông; đông tụ lại"},  # clot
    "lex.en.100k.012496": {"vi": "sự tuân thủ pháp lý/quy định"},  # compliance
    "lex.en.100k.012497": {"vi": "tuân thủ; tuân theo quy định"},  # comply
    "lex.en.100k.012499": {"vi": "bạn đời của nguyên thủ; phối ngẫu"},  # consort
}

# Verify lengths <= 35
for k, v in OVERRIDES_B03_R05.items():
    if "vi" in v:
        assert len(v["vi"]) <= 35, f"Length > 35 for {k}: {v['vi']} ({len(v['vi'])})"

with open('content/english/qa-batches/batch-03.json', 'r', encoding='utf-8') as f:
    batch_data = json.load(f)

# Apply overrides to records in range 2000 to 2500
count = 0
for idx in range(2000, 2500):
    rec = batch_data['records'][idx]
    rid = rec['id']
    if rid in OVERRIDES_B03_R05:
        count += 1
        for field, val in OVERRIDES_B03_R05[rid].items():
            rec[field] = val
        rec['status'] = 'reviewed'

batch_data['reviewedCount'] = 2500

with open('content/english/qa-batches/batch-03.json', 'w', encoding='utf-8') as f:
    json.dump(batch_data, f, ensure_ascii=False, indent=2)

print(f"Successfully applied Batch 03 Round 5 ({count} overrides). Reviewed: {batch_data['reviewedCount']}/5000.")
