import json

# Cognitive manual QA overrides for Batch 04 Round 01 (records 0 to 500, STT 1 to 500)
OVERRIDES_B04_R01 = {
    # 1 - 100
    "lex.en.100k.015001": {"vi": "thuộc về thần thoại; truyền thuyết"},  # mythological
    "lex.en.100k.015003": {"vi": "gian chính giữa giáo đường nhà thờ"},  # nave
    "lex.en.100k.015004": {"vi": "ngòi bút máy; ngòi viết nhọn"},  # nib
    "lex.en.100k.015006": {"vi": "bị xóa sạch hoàn toàn; phá hủy"},  # obliterated
    "lex.en.100k.015008": {"vi": "bỏ qua; lược bớt; không bao gồm"},  # omit (purged single-word 'lược')
    "lex.en.100k.015009": {"vi": "đang lao tới; đang đi ngược chiều"},  # oncoming
    "lex.en.100k.015010": {"vi": "quặng khoáng sản; đất đá quặng"},  # ore (purged single-word 'quặng')
    "lex.en.100k.015011": {"vi": "kỳ dị quái gở; kỳ quặc khác thường"},  # outlandish
    "lex.en.100k.015012": {"vi": "ở xa trung tâm; vùng ngoại vi"},  # outlying
    "lex.en.100k.015013": {"vi": "thuộc quá trình oxy hóa khử"},  # oxidative
    "lex.en.100k.015014": {"vi": "theo chủ nghĩa hòa bình; phản chiến"},  # pacifist
    "lex.en.100k.015015": {"vi": "diễn đạt lại ý; lời diễn giải lại"},  # paraphrase
    "lex.en.100k.015017": {"vi": "con chim bồ nông mỏ túi to"},  # pelican (purged single-word 'bồ nông')
    "lex.en.100k.015018": {"vi": "sở thích đặc biệt; thiên hướng mê"},  # penchant
    "lex.en.100k.015019": {"vi": "thuộc về Philippines; người Phi"},  # philippine
    "lex.en.100k.015020": {"vi": "điềm đạm điềm tĩnh; phẳng lặng"},  # placid
    "lex.en.100k.015021": {"vi": "thuộc về mặt phẳng; hai chiều"},  # planar (purged single-word 'phẳng')
    "lex.en.100k.015022": {"vi": "chế độ đa thê; tục nhiều vợ chồng"},  # polygamy
    "lex.en.100k.015023": {"vi": "kiểu buộc tóc đuôi ngựa cao"},  # ponytail
    "lex.en.100k.015024": {"vi": "cây bạch dương; cây gỗ dương"},  # poplar (purged single-word 'dương')
    "lex.en.100k.015025": {"vi": "thuộc chủ nghĩa hậu hiện đại"},  # postmodern
    "lex.en.100k.015026": {"vi": "đặc quyền riêng; quyền ưu tiên"},  # prerogative
    "lex.en.100k.015027": {"vi": "nguyên thủy ban sơ; từ sơ khai"},  # primordial
    "lex.en.100k.015028": {"vi": "thận trọng dè dặt; khôn ngoan"},  # prudential
    "lex.en.100k.015029": {"vi": "phương pháp phân tâm học (Freud)"},  # psychoanalysis
    "lex.en.100k.015030": {"vi": "thuộc vùng xương mu; lông mu"},  # pubic (purged single-word 'mu')
    "lex.en.100k.015031": {"vi": "chuyên viên quan hệ công chúng (PR)"},  # publicist (purged wrong 'nhà báo')
    "lex.en.100k.015032": {"vi": "một cách có chủ đích; quyết tâm"},  # purposefully
    "lex.en.100k.015033": {"pos": "noun", "vi": "bác sĩ lang băm; tiếng vịt kêu"},  # quack
    "lex.en.100k.015034": {"vi": "túc số biểu quyết; số tối thiểu"},  # quorum
    "lex.en.100k.015035": {"vi": "thằng nhóc nghịch ngợm; kẻ láu cá"},  # rascal
    "lex.en.100k.015037": {"vi": "áp bức hà khắc; kìm kẹp đàn áp"},  # repressive
    "lex.en.100k.015038": {"vi": "tháo vát nhanh trí; giàu sáng kiến"},  # resourceful
    "lex.en.100k.015039": {"vi": "vở diễn kịch tạp kỹ; ca vũ tạp kỹ"},  # revue (purged single-word 'tạp kỹ')
    "lex.en.100k.015040": {"vi": "sự nghiêm ngặt; tính chuẩn xác cao"},  # rigor
    "lex.en.100k.015041": {"vi": "người quăng thòng lọng bắt bò"},  # roper
    "lex.en.100k.015042": {"vi": "vải bao tải gai; việc bị đuổi việc"},  # sacking
    "lex.en.100k.015043": {"vi": "dùng để cúng tế; mang tính hiến tế"},  # sacrificial
    "lex.en.100k.015046": {"vi": "bị cháy xém khô cằn; cháy rụi"},  # scorched
    "lex.en.100k.015047": {"vi": "cẳng chân ống chân; bắp thịt cẳng"},  # shank
    "lex.en.100k.015048": {"vi": "nhà toán học Claude Shannon"},  # shannon
    "lex.en.100k.015049": {"vi": "được mài sắc bén; mài giũa sắc bén"},  # sharpened
    "lex.en.100k.015050": {"vi": "thanh bên cạnh lề; bài viết phụ"},  # sidebar
    "lex.en.100k.015051": {"vi": "chém bổ ác liệt; cắt giảm mạnh mẽ"},  # slashing
    "lex.en.100k.015052": {"vi": "xe trượt tuyết chó kéo; búa tạ lớn"},  # sledge
    "lex.en.100k.015053": {"vi": "giấc ngủ chợp mắt; báo lại chuông"},  # snooze
    "lex.en.100k.015054": {"vi": "lấp lánh lung linh; vui vẻ tươi vui"},  # sparkly
    "lex.en.100k.015055": {"vi": "sự mở rộng đô thị tràn lan bừa bãi"},  # sprawl
    "lex.en.100k.015056": {"vi": "kêu kẽo kẹt rin rít; giọng the thé"},  # squeaky
    "lex.en.100k.015057": {"vi": "sự tiêu chuẩn hóa; quy chuẩn hóa"},  # standardization
    "lex.en.100k.015058": {"vi": "tàu thủy chạy hơi nước động cơ"},  # steamship
    "lex.en.100k.015059": {"vi": "đau buốt nhói; châm chích chua cay"},  # stinging
    "lex.en.100k.015060": {"vi": "thủ đô Stockholm (Thụy Điển)"},  # stockholm
    "lex.en.100k.015061": {"vi": "ngột ngạt bức bối; bảo thủ hủ lậu"},  # stuffy
    "lex.en.100k.015062": {"vi": "phân nhóm nhánh nhỏ; tiểu nhóm"},  # subgroup
    "lex.en.100k.015063": {"vi": "sự triệu tập lệnh triệu hồi hầu tòa"},  # summoning
    "lex.en.100k.015064": {"vi": "hạt Sussex lịch sử (nước Anh)"},  # sussex
    "lex.en.100k.015066": {"vi": "ngôn ngữ Tamil; dân tộc Tamil Ấn"},  # tamil
    "lex.en.100k.015067": {"vi": "khoa học phân loại; phép phân loại"},  # taxonomy
    "lex.en.100k.015068": {"vi": "buổi phát sóng truyền hình vô tuyến"},  # telecast
    "lex.en.100k.015069": {"vi": "sự thuê mướn nhà; thời gian thuê"},  # tenancy
    "lex.en.100k.015071": {"vi": "cây cỏ xạ hương (thảo mộc thyme)"},  # thyme
    "lex.en.100k.015072": {"vi": "một cách miệt mài không biết mệt"},  # tirelessly
    "lex.en.100k.015073": {"vi": "nước cân bằng da toner; mực máy in"},  # toner (purged crawler typo 'nước hoà hồng')
    "lex.en.100k.015074": {"vi": "rẻ tiền rác rưởi; kém phẩm chất"},  # trashy (purged crawler 'cà khổ; cà gỉ')
    "lex.en.100k.015076": {"vi": "cứng rắn không thỏa hiệp nhượng bộ"},  # uncompromising
    "lex.en.100k.015077": {"vi": "bội bạc ngoại tình; thất hứa"},  # unfaithful
    "lex.en.100k.015078": {"vi": "báng bổ tội lỗi; dị hợm phi luân"},  # unholy
    "lex.en.100k.015079": {"vi": "thuộc vùng đồi núi cao cao nguyên"},  # upland
    "lex.en.100k.015080": {"vi": "băng ghi hình video; cuộn băng từ"},  # videotape
    "lex.en.100k.015082": {"vi": "từ điển Noah Webster; John Webster"},  # webster
    "lex.en.100k.015083": {"vi": "một cách cố tình; ngang bướng cố ý"},  # willfully
    "lex.en.100k.015084": {"vi": "áo giáp sắt; xe bọc thép thiết giáp"},  # armour
    "lex.en.100k.015085": {"vi": "nóng sôi sùng sục; cực kỳ sôi sục"},  # boiling
    "lex.en.100k.015086": {"vi": "thành phố Bradford (nước Anh)"},  # bradford
    "lex.en.100k.015087": {"vi": "quốc gia Congo; dòng sông Congo"},  # congo
    "lex.en.100k.015088": {"pos": "num", "vi": "số 80; tám mươi"},  # eighty
    "lex.en.100k.015090": {"vi": "vùng tranh chấp Kashmir (Ấn-Pak)"},  # kashmir
    "lex.en.100k.015091": {"vi": "John Knox; pháo đài vàng Fort Knox"},  # knox
    "lex.en.100k.015092": {"vi": "minh tinh Vivien Leigh; họ Leigh"},  # leigh
    "lex.en.100k.015093": {"vi": "môn toán học (tiếng Anh - Anh)"},  # maths
    "lex.en.100k.015094": {"vi": "nhà tiên tri Hồi giáo Mohammed"},  # mohammed
    "lex.en.100k.015095": {"ipa": "/ˌɛn ˈtiː/", "vi": "hệ thống Windows NT; Kinh Tân Ước"},  # nt
    "lex.en.100k.015096": {"ipa": "/rɑm/", "vi": "bộ nhớ chỉ đọc ROM (máy tính)"},  # rom
    "lex.en.100k.015097": {"vi": "thành phố cổ Canterbury (nước Anh)"},  # canterbury
    "lex.en.100k.015098": {"vi": "đất nước Croatia (Đông Nam Âu)"},  # croatia
    "lex.en.100k.015099": {"vi": "nhà bác học Albert Einstein"},  # einstein
    "lex.en.100k.015100": {"vi": "thành phố Istanbul (Thổ Nhĩ Kỳ)"},  # istanbul

    # 101 - 200
    "lex.en.100k.015101": {"vi": "họ Jacobs; nhà văn Harriet Jacobs"},  # jacobs
    "lex.en.100k.015102": {"vi": "đồ trang sức; vàng bạc nữ trang"},  # jewellery
    "lex.en.100k.015103": {"vi": "thủ đô Kingston (nước Jamaica)"},  # kingston
    "lex.en.100k.015104": {"vi": "thượng nghị sĩ Joseph McCarthy"},  # mccarthy
    "lex.en.100k.015105": {"vi": "chương trình y tế trợ cấp Medicaid"},  # medicaid
    "lex.en.100k.015106": {"ipa": "/ˌɛm aɪ ˈtiː/", "vi": "Học viện Kỹ thuật MIT (Hoa Kỳ)"},  # mit
    "lex.en.100k.015107": {"vi": "thành phố Newark (New Jersey)"},  # newark
    "lex.en.100k.015108": {"vi": "thủ đô Sofia (nước Bulgaria)"},  # sofia
    "lex.en.100k.015109": {"ipa": "/ˌɛks ˈɛks/", "vi": "số 20 La Mã (XX); thế kỷ 20"},  # xx
    "lex.en.100k.015110": {"ipa": "/ˌeɪ ˈkeɪ/", "vi": "tiểu bang Alaska (AK); súng AK-47"},  # ak
    "lex.en.100k.015111": {"vi": "kim loại nhôm (tiếng Anh - Anh)"},  # aluminium
    "lex.en.100k.015112": {"vi": "thành phố và nghĩa trang Arlington"},  # arlington
    "lex.en.100k.015113": {"vi": "chủ tịch Cuba Fidel Castro"},  # castro
    "lex.en.100k.015114": {"vi": "sông Dương Tử (Chang); họ Trương"},  # chang
    "lex.en.100k.015115": {"vi": "loài thỏ đá hoang dã hyrax coney"},  # das
    "lex.en.100k.015116": {"vi": "giải thưởng truyền hình Mỹ Emmy"},  # emmy
    "lex.en.100k.015117": {"vi": "quốc gia Ethiopia (Đông Phi)"},  # ethiopia
    "lex.en.100k.015118": {"ipa": "/ˈfleɪvɚ/", "vi": "mùi vị thơm ngon; hương vị đậm đà"},  # flavour
    "lex.en.100k.015119": {"vi": "nhà độc tài Francisco Franco (TBN)"},  # franco
    "lex.en.100k.015120": {"ipa": "/ˌeɪtʃ ˈkjuː/", "vi": "trụ sở chính công ty; bộ chỉ huy HQ"},  # hq
    "lex.en.100k.015121": {"ipa": "/ˌkeɪ ˈoʊ/", "vi": "đo ván hạ gục KO (quyền anh)"},  # ko
    "lex.en.100k.015122": {"vi": "nhà văn đoạt giải Nobel Thomas Mann"},  # mann
    "lex.en.100k.015123": {"ipa": "/ˌɛm ˈɛn/", "vi": "bang Minnesota; nguyên tố mangan"},  # mn
    "lex.en.100k.015124": {"vi": "Helmut Schmidt; Eric Schmidt"},  # schmidt
    "lex.en.100k.015125": {"vi": "thám tử đại tài Sherlock Holmes"},  # sherlock
    "lex.en.100k.015126": {"vi": "dòng sông Thames chảy qua Luân Đôn"},  # thames
    "lex.en.100k.015127": {"vi": "vương triều hoàng gia Windsor (Anh)"},  # windsor
    "lex.en.100k.015128": {"ipa": "/ˌɛks ɛks ˈɛks/", "vi": "số 30 La Mã (XXX); phim người lớn"},  # xxx
    "lex.en.100k.015129": {"vi": "quốc gia Zimbabwe (Nam Phi)"},  # zimbabwe
    "lex.en.100k.015130": {"vi": "Frederick Ashton; họ Ashton"},  # ashton
    "lex.en.100k.015131": {"vi": "con sông Clyde nổi tiếng (Scotland)"},  # clyde
    "lex.en.100k.015133": {"vi": "tài tử Matt Damon; họ Damon"},  # damon
    "lex.en.100k.015134": {"ipa": "/ˌdʒiː ˈaɪ/", "vi": "thuộc đường tiêu hóa dạ dày ruột"},  # gi
    "lex.en.100k.015135": {"vi": "quốc đảo Haiti nghèo khó (Caribe)"},  # haiti
    "lex.en.100k.015136": {"vi": "thuộc về Li-băng; người Li-băng"},  # lebanese
    "lex.en.100k.015137": {"ipa": "/ˌɛn ˈdʌbəl.juː/", "vi": "hướng tây bắc; khu vực tây bắc"},  # nw
    "lex.en.100k.015138": {"ipa": "/ˌpiː ˈiː/", "vi": "môn giáo dục thể chất PE (thể dục)"},  # pe
    "lex.en.100k.015139": {"vi": "quốc gia El Salvador; Salvador Dali"},  # salvador
    "lex.en.100k.015140": {"vi": "bảo tàng mỹ thuật Tate; họ Tate"},  # tate
    "lex.en.100k.015141": {"ipa": "/ˌjuː ˈtiː/", "vi": "bang Utah (Mỹ); nốt Đô nhạc cổ (ut)"},  # ut
    "lex.en.100k.015142": {"vi": "loài bướm Vanessa; tên nữ Vanessa"},  # vanessa
    "lex.en.100k.015143": {"pos": "num", "ipa": "/ˌviː aɪ aɪ ˈaɪ/", "vi": "số 8 La Mã (VIII); thứ tám"},  # viii
    "lex.en.100k.015144": {"vi": "Eli Whitney; bảo tàng Whitney"},  # whitney
    "lex.en.100k.015145": {"vi": "người mắc chứng bệnh bạch tạng"},  # albino
    "lex.en.100k.015147": {"vi": "phụ trợ hỗ trợ bổ sung; bên lề thêm"},  # ancillary
    "lex.en.100k.015148": {"vi": "có tác dụng gây mê; gây tê cục bộ"},  # anesthetic
    "lex.en.100k.015149": {"vi": "khoản tiền nợ đọng chưa thanh toán"},  # arrears
    "lex.en.100k.015150": {"vi": "rắn lục châu Âu; loài rắn độc nhỏ"},  # asp
    "lex.en.100k.015151": {"vi": "dấu sao hoa thị ghi chú (*)"},  # asterisk
    "lex.en.100k.015152": {"vi": "cây hoa đỗ quyên khoe sắc hồng rực"},  # azalea
    "lex.en.100k.015153": {"vi": "đơn bào vi khuẩn; một con vi khuẩn"},  # bacterium
    "lex.en.100k.015154": {"pos": "verb", "vi": "trao đổi hàng đổi hàng; đổi chác"},  # barter (purged single-word 'đổi')
    "lex.en.100k.015155": {"vi": "củ cải đường ngọt; củ dền đỏ"},  # beet
    "lex.en.100k.015156": {"vi": "mù quáng cố chấp; bảo thủ hẹp hòi"},  # bigoted
    "lex.en.100k.015157": {"vi": "quán ăn nhỏ bình dân kiểu Pháp"},  # bistro
    "lex.en.100k.015158": {"vi": "bị bịt kín mắt; mù quáng không thấy"},  # blindfolded
    "lex.en.100k.015159": {"vi": "mỏ vàng quặng giàu; món hời kếch xù"},  # bonanza
    "lex.en.100k.015160": {"vi": "vũ khí boomerang; tác dụng phản chủ"},  # boomerang
    "lex.en.100k.015161": {"vi": "bầu ngực phụ nữ; đáy lòng tâm can"},  # bosom
    "lex.en.100k.015162": {"vi": "sự mở mang đầu óc; mở rộng quy mô"},  # broadening
    "lex.en.100k.015163": {"vi": "nghệ thuật thư pháp chữ đẹp nắn nót"},  # calligraphy
    "lex.en.100k.015164": {"vi": "kẻ ăn thịt đồng loại dã man"},  # cannibal
    "lex.en.100k.015165": {"vi": "nghề mộc thợ gỗ gia công mộc"},  # carpentry
    "lex.en.100k.015166": {"vi": "mang tính ăn mừng kỷ niệm vui vẻ"},  # celebratory (purged single-word 'mừng')
    "lex.en.100k.015167": {"vi": "cây đục thợ mộc; chạm trổ gọt giũa"},  # chisel
    "lex.en.100k.015168": {"vi": "thuộc về nhận thức tư duy trí tuệ"},  # cognitive
    "lex.en.100k.015170": {"vi": "bản tổng hợp tóm lược; cẩm nang"},  # compendium
    "lex.en.100k.015171": {"vi": "có khả năng dẫn điện hoặc nhiệt"},  # conductive (purged single-word 'dẫn')
    "lex.en.100k.015172": {"vi": "thuộc về vùng vỏ não; lớp vỏ ngoài"},  # cortical
    "lex.en.100k.015173": {"vi": "bút sáp màu tô vẽ tranh cho trẻ em"},  # crayon
    "lex.en.100k.015174": {"vi": "sự hỏa táng thi hài; lễ hỏa táng"},  # cremation
    "lex.en.100k.015175": {"vi": "tình trạng chen chúc đông nghẹt thở"},  # crowding
    "lex.en.100k.015176": {"vi": "mẩu vụn bánh mì; một chút ít ỏi"},  # crumb
    "lex.en.100k.015178": {"vi": "thuộc chương trình giáo dục đào tạo"},  # curricular
    "lex.en.100k.015179": {"vi": "mỏm nhọn; ranh giới bước ngoặt"},  # cusp
    "lex.en.100k.015180": {"vi": "giấc mơ mộng ban ngày; viển vông"},  # daydream
    "lex.en.100k.015181": {"vi": "sự giải mã dữ liệu thông tin"},  # decoding
    "lex.en.100k.015184": {"vi": "trận đại hồng thủy; cơn ngập tràn"},  # deluge
    "lex.en.100k.015186": {"vi": "chấm dứt ngay; dừng hẳn hành vi xấu"},  # desist
    "lex.en.100k.015187": {"vi": "sự kích hoạt nổ; vụ nổ bom mìn"},  # detonation
    "lex.en.100k.015188": {"vi": "sự phân quyền địa phương; thoái hóa"},  # devolution
    "lex.en.100k.015190": {"vi": "tỏ ý gạt bỏ xua tay; coi khinh"},  # dismissive
    "lex.en.100k.015194": {"vi": "hành động cúi thụp đầu né tránh"},  # ducking
    "lex.en.100k.015195": {"vi": "tiếng vang vọng âm dội lại; lặp lại"},  # echo
    "lex.en.100k.015196": {"vi": "tiểu vương Hồi giáo; hoàng thân"},  # emir
    "lex.en.100k.015198": {"vi": "thuộc về hệ nội tiết tố cơ thể"},  # endocrine
    "lex.en.100k.015199": {"vi": "thuộc lớp mô biểu bì phủ da"},  # epithelial
    "lex.en.100k.015200": {"vi": "việc vặt chạy việc; công việc vặt"},  # errand

    # 201 - 300
    "lex.en.100k.015201": {"vi": "cực kỳ đau đớn buốt óc; khủng khiếp"},  # excruciating
    "lex.en.100k.015202": {"vi": "hân hoan phấn chấn; tươi tốt um tùm"},  # exuberant
    "lex.en.100k.015203": {"vi": "kỳ ảo huyền hoặc; viển vông lạ lùng"},  # fanciful
    "lex.en.100k.015204": {"vi": "cú ném bóng tốc độ cao (bóng chày)"},  # fastball
    "lex.en.100k.015206": {"vi": "nhiệt huyết sục sôi; lòng say mê"},  # fervor
    "lex.en.100k.015207": {"vi": "chói lọi sặc sỡ màu mè; phô trương"},  # flamboyant
    "lex.en.100k.015208": {"vi": "con chim hồng hạc chân dài cao vút"},  # flamingo
    "lex.en.100k.015209": {"vi": "lời nịnh bợ tâng bốc; sự tâng bốc"},  # flattery
    "lex.en.100k.015210": {"vi": "sự dại dột dốt nát; tính ngu xuẩn"},  # foolishness
    "lex.en.100k.015211": {"vi": "phun trào ồ ạt; khen ngợi thái quá"},  # gushing
    "lex.en.100k.015213": {"vi": "trạng thái ngủ đông; sự ngừng nghỉ"},  # hibernation
    "lex.en.100k.015214": {"vi": "tiếng xuỵt la ó; tiếng rắn rít"},  # hiss
    "lex.en.100k.015216": {"vi": "tiếng còi xe; tiếng ngỗng trời kêu"},  # honk
    "lex.en.100k.015217": {"vi": "khiến người ta khiêm nhường hạ mình"},  # humbling
    "lex.en.100k.015218": {"vi": "linh dương châu Phi Impala nhảy vọt"},  # impala
    "lex.en.100k.015220": {"vi": "tiến trình công nghiệp hóa đất nước"},  # industrialization
    "lex.en.100k.015221": {"vi": "một cách kỳ lạ không thể hiểu nổi"},  # inexplicably
    "lex.en.100k.015222": {"vi": "vô thưởng vô phạt; hoàn toàn vô hại"},  # innocuous
    "lex.en.100k.015224": {"vi": "sự hội nhập quốc tế; tích hợp"},  # integration
    "lex.en.100k.015225": {"vi": "ký hiệu chữ cái Hy Lạp Lambda (λ)"},  # lambda
    "lex.en.100k.015226": {"vi": "bản năng ham muốn tình dục (libido)"},  # libido
    "lex.en.100k.015227": {"vi": "nạn hành hình tập thể không xét xử"},  # lynching (purged single-word 'hành hình')
    "lex.en.100k.015228": {"vi": "con linh miêu tai túm lông hoang dã"},  # lynx
    "lex.en.100k.015229": {"vi": "bậc vĩ nhân Mahatma (Ấn Độ giáo)"},  # mahatma
    "lex.en.100k.015231": {"vi": "trụ cột nòng cốt; chỗ dựa vững chắc"},  # mainstay
    "lex.en.100k.015232": {"vi": "dịch vụ chăm sóc cắt tỉa móng tay"},  # manicure
    "lex.en.100k.015233": {"vi": "tượng ma-nơ-canh mặc quần áo mẫu"},  # mannequin
    "lex.en.100k.015235": {"vi": "điêu luyện bậc thầy; đầy bản lĩnh"},  # masterful
    "lex.en.100k.015236": {"vi": "ở mức tối đa; đạt giới hạn cao nhất"},  # maximal
    "lex.en.100k.015237": {"vi": "ít ỏi nghèo nàn gầy gò; đạm bạc"},  # meager
    "lex.en.100k.015238": {"vi": "giá trị công lao; ưu điểm điểm cộng"},  # merit
    "lex.en.100k.015239": {"vi": "tên tay sai hầu hạ; kẻ dưới trướng"},  # minion
    "lex.en.100k.015240": {"vi": "xe hơi gia đình đa dụng minivan"},  # minivan
    "lex.en.100k.015242": {"vi": "bị dùng sai mục đích; bị lạm quyền"},  # misused
    "lex.en.100k.015243": {"vi": "một cách khiêm tốn; dè dặt kín đáo"},  # modestly
    "lex.en.100k.015244": {"vi": "biệt danh; biệt hiệu thân mật"},  # moniker
    "lex.en.100k.015245": {"vi": "đơn điệu tẻ nhạt; đều đều buồn chán"},  # monotonous
    "lex.en.100k.015246": {"vi": "buổi bình minh sáng sớm sương mai"},  # morn
    "lex.en.100k.015247": {"vi": "không cần thiết; một cách vô ích"},  # needlessly
    "lex.en.100k.015248": {"vi": "theo phái bất bạo động; hòa bình"},  # nonviolent
    "lex.en.100k.015249": {"vi": "đáng chê trách phản đối; khó chịu"},  # objectionable
    "lex.en.100k.015250": {"vi": "trục lợi cơ hội chủ nghĩa; thừa cơ"},  # opportunistic
    "lex.en.100k.015251": {"vi": "khu đất công viên; bãi cỏ cây xanh"},  # parkland
    "lex.en.100k.015252": {"vi": "mang tính sư phạm; phương pháp dạy"},  # pedagogical
    "lex.en.100k.015253": {"vi": "bác sĩ chuyên khoa nhi chăm sóc trẻ"},  # pediatrician
    "lex.en.100k.015254": {"vi": "nhạy bén sắc sảo tinh tế; thấu suốt"},  # perceptive
    "lex.en.100k.015255": {"vi": "tính phân cực; sự đối lập hai cực"},  # polarity
    "lex.en.100k.015256": {"vi": "tự cao tự đại hợm hĩnh; phô trương"},  # pompous
    "lex.en.100k.015257": {"vi": "cú vồ chụp lấy; chộp lấy cơ hội"},  # pounce
    "lex.en.100k.015259": {"vi": "công khai tự nhận; khẳng định tin"},  # profess
    "lex.en.100k.015260": {"vi": "nằm úp sấp; có xu hướng dễ bị"},  # prone (purged single-word 'úp; sấp')
    "lex.en.100k.015261": {"vi": "nhô ra ngoài; lồi ra phía trước"},  # protruding
    "lex.en.100k.015262": {"vi": "thuộc miền quê tỉnh lẻ; thiển cận"},  # provincial
    "lex.en.100k.015264": {"vi": "hạt cơ bản quark (vật lý lượng tử)"},  # quark (purged single-word 'quắc')
    "lex.en.100k.015265": {"vi": "việc lấy lại bình tĩnh; giành lại"},  # regaining
    "lex.en.100k.015266": {"vi": "tập hợp lại lực lượng; chấn chỉnh"},  # regroup
    "lex.en.100k.015267": {"vi": "thuộc về cơ quan quản lý điều tiết"},  # regulatory
    "lex.en.100k.015268": {"vi": "tái tạo đổi mới toàn diện hình ảnh"},  # reinvent
    "lex.en.100k.015269": {"vi": "kho tiết mục biểu diễn nghệ thuật"},  # repertory
    "lex.en.100k.015270": {"vi": "khúc nhạc cầu hồn; thánh lễ cầu hồn"},  # requiem
    "lex.en.100k.015271": {"vi": "làm sống lại; hồi sinh từ cõi chết"},  # resurrect
    "lex.en.100k.015272": {"vi": "thuật hùng biện; lời lẽ sáo rỗng"},  # rhetoric
    "lex.en.100k.015273": {"vi": "người giống hệt đúc; kẻ mạo danh"},  # ringer
    "lex.en.100k.015274": {"vi": "vô cùng hấp dẫn lôi cuốn; ly kỳ"},  # riveting
    "lex.en.100k.015275": {"vi": "cổ áo xếp nếp; vòng lông quanh cổ"},  # ruff
    "lex.en.100k.015276": {"vi": "phần mông thịt thăn đùi gia súc bò"},  # rump
    "lex.en.100k.015277": {"vi": "váy sari truyền thống của phụ nữ Ấn"},  # sari
    "lex.en.100k.015278": {"vi": "gay gắt đay nghiến; đả kích cay độc"},  # scathing
    "lex.en.100k.015279": {"vi": "gan góc kiên cường; chắp vá vụn vặt"},  # scrappy
    "lex.en.100k.015280": {"vi": "thuộc thế tục; không theo tôn giáo"},  # secular
    "lex.en.100k.015281": {"vi": "ngoằn ngoèo uốn khúc; quanh co"},  # serpentine
    "lex.en.100k.015282": {"vi": "bước đi lê chân; hành động xáo bài"},  # shuffling
    "lex.en.100k.015283": {"vi": "cuộc giao tranh lẻ tẻ; đụng độ nhỏ"},  # skirmish
    "lex.en.100k.015284": {"vi": "vũng đầm lầy lội; da rắn lột xác"},  # slough
    "lex.en.100k.015285": {"vi": "khói bụi ô nhiễm sương mù quang hóa"},  # smog
    "lex.en.100k.015286": {"vi": "quá trình xã hội hóa; sự hòa nhập"},  # socialization
    "lex.en.100k.015287": {"vi": "kẻ thái nhân cách chống đối xã hội"},  # sociopath
    "lex.en.100k.015288": {"vi": "được làm cho đông cứng; cô kết lại"},  # solidified
    "lex.en.100k.015289": {"vi": "cột buồm phụ xà ngang; đấu khẩu vặt"},  # spar
    "lex.en.100k.015290": {"vi": "cất xếp gọn gàng ngăn nắp; giấu kín"},  # stow
    "lex.en.100k.015291": {"vi": "được cách điệu hóa; đậm nét ước lệ"},  # stylized
    "lex.en.100k.015292": {"vi": "chế ngự dập tắt; khuất phục kìm nén"},  # subdue
    "lex.en.100k.015293": {"vi": "cây lá mọng nước sen đá; ngon ngọt"},  # succulent
    "lex.en.100k.015294": {"vi": "người đàn ông cầu hôn; bên chào mua"},  # suitor
    "lex.en.100k.015295": {"vi": "môn võ đô vật Sumo (Nhật Bản)"},  # sumo
    "lex.en.100k.015299": {"vi": "đền tạm Do Thái; nhà nguyện Mormon"},  # tabernacle
    "lex.en.100k.015300": {"vi": "mang tính thao lược chiến thuật"},  # tactical

    # 301 - 400
    "lex.en.100k.015301": {"vi": "bùa hộ mệnh may mắn trừ tà khí ác"},  # talisman
    "lex.en.100k.015302": {"vi": "bé tí xíu tí hon; nhỏ xíu xiu"},  # teeny
    "lex.en.100k.015303": {"vi": "ghế ngang chèo thuyền; cản trở phá"},  # thwart
    "lex.en.100k.015304": {"vi": "bánh mì dẹt tráng mỏng Tortilla Mễ"},  # tortilla
    "lex.en.100k.015305": {"vi": "sự thanh bình tĩnh lặng; sự êm ả"},  # tranquility
    "lex.en.100k.015306": {"vi": "máy phát đáp tín hiệu tự động"},  # transponder
    "lex.en.100k.015307": {"vi": "nấm cục đen truffle đắt đỏ; kẹo mềm"},  # truffle
    "lex.en.100k.015308": {"vi": "biến động hỗn loạn; náo động ầm ĩ"},  # tumultuous
    "lex.en.100k.015309": {"vi": "dơ bẩn dơ dáy; nhơ nhuốc ô uế"},  # unclean
    "lex.en.100k.015312": {"vi": "rút phích cắm điện; ngắt kết nối"},  # unplug (purged single-word 'rút')
    "lex.en.100k.015313": {"vi": "không bị kiểm soát; ngoài vòng luật"},  # unregulated
    "lex.en.100k.015314": {"vi": "vô liêm sỉ; bất chấp mọi thủ đoạn"},  # unscrupulous
    "lex.en.100k.015315": {"vi": "kiên định vững vàng; không dao động"},  # unwavering
    "lex.en.100k.015316": {"vi": "một cách vô tình không hề hay biết"},  # unwittingly
    "lex.en.100k.015317": {"vi": "ở phía bụng dưới cơ thể sinh vật"},  # ventral
    "lex.en.100k.015318": {"vi": "xấp tiền cuộn tròn; nắm bông gòn"},  # wad
    "lex.en.100k.015319": {"vi": "ven mép lề đường quốc lộ; bờ đường"},  # wayside
    "lex.en.100k.015320": {"vi": "một cách kỳ dị quái gở khác thường"},  # weirdly
    "lex.en.100k.015321": {"vi": "nước váng sữa; bột đạm protein whey"},  # whey
    "lex.en.100k.015322": {"vi": "chấn thương cổ do va chạm giật mạnh"},  # whiplash
    "lex.en.100k.015323": {"vi": "tự phát chui; mèo rừng hoang dã"},  # wildcat
    "lex.en.100k.015324": {"vi": "nạn bài ngoại; nỗi ám ảnh bài ngoại"},  # xenophobia (purged crawler typo 'tinh')
    "lex.en.100k.015326": {"vi": "ngôn ngữ Ada; Hiệp hội Nha khoa ADA"},  # ada
    "lex.en.100k.015327": {"vi": "vương quốc Campuchia (Đông Nam Á)"},  # cambodia
    "lex.en.100k.015328": {"vi": "quốc đảo Síp (Địa Trung Hải)"},  # cyprus
    "lex.en.100k.015329": {"ipa": "/ˌaɪ ɛm ˈoʊ/", "vi": "theo quan điểm của tôi (IMO mạng)"},  # imo
    "lex.en.100k.015330": {"vi": "đại văn hào Mỹ Washington Irving"},  # irving
    "lex.en.100k.015331": {"vi": "nhà văn nữ cánh tả Erica Jong"},  # jong
    "lex.en.100k.015332": {"vi": "Calvin Klein; nhà toán học Klein"},  # klein
    "lex.en.100k.015333": {"ipa": "/ˌɛn ˈdiː/", "vi": "bang Bắc Dakota; kim loại neodim"},  # nd
    "lex.en.100k.015334": {"pos": "num", "vi": "số 90; chín mươi"},  # ninety
    "lex.en.100k.015335": {"ipa": "/ˌɑːr ˈɛn/", "vi": "y tá có chứng chỉ hành nghề (RN)"},  # rn
    "lex.en.100k.015336": {"vi": "thành phố Roma; người Digan (Roma)"},  # roma
    "lex.en.100k.015337": {"vi": "đất nước Serbia; Cộng hòa Serbia"},  # serbia
    "lex.en.100k.015338": {"ipa": "/ˌɛs ˈɛm/", "vi": "nguyên tố samari (Sm); công ty SM"},  # sm
    "lex.en.100k.015339": {"ipa": "/ˌtiː ˈbiː/", "vi": "bệnh lao phổi; dung lượng terabyte"},  # tb
    "lex.en.100k.015340": {"vi": "Mẹ Teresa thành Calcutta nhân ái"},  # teresa
    "lex.en.100k.015341": {"vi": "thủ tướng Theresa May; tên Theresa"},  # theresa
    "lex.en.100k.015342": {"ipa": "/ˌtiː ˈɛn/", "vi": "tiểu bang Tennessee nước Mỹ (TN)"},  # tn
    "lex.en.100k.015343": {"vi": "nhà soạn nhạc vĩ đại Richard Wagner"},  # wagner
    "lex.en.100k.015344": {"vi": "thành phố Auckland (New Zealand)"},  # auckland
    "lex.en.100k.015345": {"vi": "nhà văn trinh thám Agatha Christie"},  # christie
    "lex.en.100k.015346": {"ipa": "/ˌiː ˈsiː/", "vi": "Cộng đồng châu Âu EC; Ủy ban EC"},  # ec
    "lex.en.100k.015347": {"vi": "trận đánh lịch sử Hastings 1066"},  # hastings
    "lex.en.100k.015348": {"ipa": "/ˌaɪ ˈeɪ/", "vi": "bang Iowa (Mỹ); kiến trúc thông tin"},  # ia
    "lex.en.100k.015349": {"vi": "xe tải hạng nặng Mack; áo mưa mack"},  # mack
    "lex.en.100k.015350": {"vi": "nghề người mẫu; sự mô hình hóa số"},  # modelling (purged single-word 'mẫu')
    "lex.en.100k.015351": {"ipa": "/ˌpiː ˈdiː/", "vi": "sở cảnh sát (PD); kim loại paladi"},  # pd
    "lex.en.100k.015352": {"vi": "thành phố cổ Saint Petersburg (Nga)"},  # petersburg
    "lex.en.100k.015353": {"ipa": "/ˌɑːr ˈbiː/", "vi": "kim loại rubidi (Rb); cầu thủ RB"},  # rb
    "lex.en.100k.015354": {"vi": "thành phố săn phù thủy Salem (Mỹ)"},  # salem
    "lex.en.100k.015355": {"vi": "câu lạc bộ Santos; thành phố Santos"},  # santos
    "lex.en.100k.015356": {"ipa": "/ˌɛs ˈbiː/", "vi": "nguyên tố antimon (Sb); Super Bowl"},  # sb
    "lex.en.100k.015357": {"vi": "diễn viên Sidney Poitier; họ Sidney"},  # sidney
    "lex.en.100k.015358": {"vi": "tên nữ Stella; bia Stella Artois"},  # stella
    "lex.en.100k.015359": {"vi": "hướng nam (tiếng TBN); vùng Big Sur"},  # sur
    "lex.en.100k.015360": {"vi": "quốc gia Uruguay; dòng sông Uruguay"},  # uruguay
    "lex.en.100k.015361": {"ipa": "/ˌjuː tiː ˈsiː/", "vi": "Giờ Phối hợp Quốc tế chuẩn UTC"},  # utc
    "lex.en.100k.015362": {"vi": "nhà thần học Giám lý John Wesley"},  # wesley
    "lex.en.100k.015363": {"vi": "Thiền tông; trạng thái thiền tịnh"},  # zen
    "lex.en.100k.015364": {"vi": "hòn đảo thiên đường nghỉ dưỡng Bali"},  # bali
    "lex.en.100k.015365": {"vi": "thủ phủ công nghệ Bangalore (Ấn Độ)"},  # bangalore
    "lex.en.100k.015366": {"vi": "mạng internet băng thông rộng"},  # broadband
    "lex.en.100k.015367": {"vi": "Đại học danh tiếng Cornell (Mỹ)"},  # cornell
    "lex.en.100k.015368": {"ipa": "/ˈkaʊnsəlɚ/", "vi": "nghị viên hội đồng đô thị thành phố"},  # councillor
    "lex.en.100k.015369": {"ipa": "/ˈfʊtbɔːlɚ/", "vi": "cầu thủ bóng đá chuyên nghiệp"},  # footballer
    "lex.en.100k.015370": {"ipa": "/ˌeɪtʃ ˈɛs/", "vi": "trường cấp ba phổ thông (HS)"},  # hs
    "lex.en.100k.015371": {"vi": "máy nghe nhạc iPod của Apple"},  # ipod
    "lex.en.100k.015372": {"ipa": "/ˌaɪ ˈkjuː/", "vi": "chỉ số thông minh não bộ (IQ)"},  # iq
    "lex.en.100k.015373": {"pos": "num", "ipa": "/ˌaɪ ˈɛks/", "vi": "số 9 La Mã (IX); thứ chín"},  # ix
    "lex.en.100k.015374": {"vi": "người hàng xóm láng giềng kề bên"},  # neighbour
    "lex.en.100k.015375": {"vi": "hãng xe ô tô Nissan; tháng Nisan"},  # nissan
    "lex.en.100k.015376": {"vi": "thành phố cảng Plymouth (Anh & Mỹ)"},  # plymouth
    "lex.en.100k.015377": {"vi": "vùng đất lịch sử Punjab (Ấn - Pak)"},  # punjab
    "lex.en.100k.015378": {"vi": "hòn đảo Rhodes; tỷ phú Cecil Rhodes"},  # rhodes
    "lex.en.100k.015379": {"ipa": "/ˌɑːr ˈaɪ/", "vi": "tiểu bang Rhode Island Hoa Kỳ (RI)"},  # ri
    "lex.en.100k.015380": {"vi": "nhà lãnh đạo Liên Xô Joseph Stalin"},  # stalin
    "lex.en.100k.015381": {"vi": "lực lượng Hồi giáo Taliban (Afgh)"},  # taliban
    "lex.en.100k.015382": {"vi": "Thần sấm Thor dũng mãnh (Bắc Âu)"},  # thor
    "lex.en.100k.015383": {"vi": "tài tử Bruce Willis; tháp Willis"},  # willis
    "lex.en.100k.015384": {"ipa": "/ˌeɪ ˈzɛd/", "vi": "bang Arizona (Mỹ); từ A đến Z"},  # az
    "lex.en.100k.015385": {"vi": "vùng đất Bengal; loài mèo hổ Bengal"},  # bengal
    "lex.en.100k.015386": {"vi": "thi hào nước Anh Lord Byron"},  # byron
    "lex.en.100k.015387": {"ipa": "/ˌdiː ˈdiː/", "vi": "tiến sĩ thần học; lệnh sao lưu dd"},  # dd
    "lex.en.100k.015388": {"vi": "tên thơ của Ireland; tên nữ Erin"},  # erin
    "lex.en.100k.015389": {"vi": "thuộc Philippines; tiếng Filipino"},  # filipino
    "lex.en.100k.015390": {"vi": "thuộc về đảo Hawaii; thổ dân Hawaii"},  # hawaiian
    "lex.en.100k.015391": {"ipa": "/ˌaɪ ˈɑːr/", "vi": "tia hồng ngoại (IR); kim loại iridi"},  # ir
    "lex.en.100k.015392": {"vi": "hành tinh Sao Mộc; thần sấm Jupiter"},  # jupiter
    "lex.en.100k.015393": {"vi": "thiên tài Leonardo da Vinci"},  # leonardo
    "lex.en.100k.015394": {"vi": "Karl Marx; anh em diễn hài Marx"},  # marx
    "lex.en.100k.015395": {"vi": "axit ribonucleic ARN (sinh học)"},  # rna
    "lex.en.100k.015396": {"ipa": "/ˌɛs ˈdʌbəl.juː/", "vi": "hướng tây nam; viết tắt phần mềm SW"},  # sw
    "lex.en.100k.015397": {"pos": "num", "ipa": "/ˌɛks ˈɛl/", "vi": "số 40 La Mã (XL); cỡ áo quần XL"},  # xl
    "lex.en.100k.015398": {"vi": "nghĩa vụ giải trình; trách nhiệm"},  # accountability
    "lex.en.100k.015399": {"vi": "phán quyết tha bổng tuyên trắng án"},  # acquittal
    "lex.en.100k.015400": {"vi": "lòng vị tha nhân ái; đức hy sinh"},  # altruism

    # 401 - 500
    "lex.en.100k.015401": {"vi": "vị tha cao thượng; vì người khác"},  # altruistic
    "lex.en.100k.015402": {"vi": "cái đe thợ rèn; xương đe trong tai"},  # anvil (purged single-word 'đe')
    "lex.en.100k.015403": {"vi": "ngành nghề nuôi trồng thủy hải sản"},  # aquaculture
    "lex.en.100k.015404": {"vi": "vũ khí trang bị quân sự; khí tài"},  # armament
    "lex.en.100k.015405": {"vi": "về mặt thẩm mỹ; đậm chất nghệ thuật"},  # artistically
    "lex.en.100k.015406": {"vi": "bất đối xứng; lệch về một phía"},  # asymmetrical
    "lex.en.100k.015407": {"vi": "sự gia tăng tăng cường; độ bồi đắp"},  # augmentation
    "lex.en.100k.015408": {"vi": "tự hành độc lập; có quyền tự trị"},  # autonomous (purged single-word 'tự trị')
    "lex.en.100k.015410": {"vi": "thuộc thực vật học; vườn bách thảo"},  # botanic
    "lex.en.100k.015411": {"vi": "bao la vô biên; vô hạn không cùng"},  # boundless
    "lex.en.100k.015412": {"vi": "sự tẩy não; sự nhồi sọ tư tưởng"},  # brainwashing (purged single-word 'tẩy não')
    "lex.en.100k.015413": {"vi": "trâm cài áo đính đá; thoa cài tóc"},  # brooch (purged single-word 'trâm; thoa')
    "lex.en.100k.015414": {"vi": "dải cờ hoa trang trí; vải may cờ"},  # bunting
    "lex.en.100k.015415": {"vi": "bè lũ mưu phản bí mật; nhóm lợi ích"},  # cabal
    "lex.en.100k.015416": {"vi": "đội ngũ cán bộ nòng cốt khung sườn"},  # cadre
    "lex.en.100k.015417": {"vi": "đường đắp vượt đầm lầy; đê đắp cao"},  # causeway
    "lex.en.100k.015418": {"vi": "thống chế chỉ huy trăm quân La Mã"},  # centurion
    "lex.en.100k.015419": {"vi": "dao phay chặt thịt băm xương bản to"},  # cleaver
    "lex.en.100k.015420": {"vi": "cùi bắp ngô; giống ngựa lùn vạm vỡ"},  # cob
    "lex.en.100k.015422": {"vi": "tiền đúc kim loại; việc đặt từ mới"},  # coinage
    "lex.en.100k.015423": {"vi": "mặt hàng hóa thương phẩm buôn bán"},  # commodity
    "lex.en.100k.015424": {"vi": "sự tự mãn quá sớm; tâm lý chủ quan"},  # complacency
    "lex.en.100k.015426": {"vi": "tâm sự giãi bày; thổ lộ bí mật"},  # confide
    "lex.en.100k.015427": {"vi": "tụ họp quây quần; tập hợp đám đông"},  # congregate
    "lex.en.100k.015428": {"vi": "thuộc giáo đoàn tự trị; hội thánh"},  # congregational
    "lex.en.100k.015431": {"vi": "hoàn hảo tột bực; viên mãn trọn vẹn"},  # consummate
    "lex.en.100k.015432": {"vi": "sự mãn nguyện toại ý; lòng an yên"},  # contentment
    "lex.en.100k.015433": {"vi": "triệu tập cuộc họp; nhóm họp"},  # convene
    "lex.en.100k.015434": {"vi": "thi thể người chết; xác chết tử thi"},  # corpse
    "lex.en.100k.015435": {"vi": "thuộc về vũ trụ; tầm vóc vũ trụ lớn"},  # cosmic (purged single-word 'vũ trụ')
    "lex.en.100k.015436": {"vi": "chứng co rút cơ bắp (chuột rút)"},  # cramp
    "lex.en.100k.015437": {"vi": "chiếc nỏ bắn tên; cây nỏ săn bắn"},  # crossbow
    "lex.en.100k.015438": {"vi": "suy đồi sa đọa trụy lạc; suy thoái"},  # decadent
    "lex.en.100k.015439": {"vi": "mồi nhử bẫy lừa; kẻ làm mồi nhử"},  # decoy
    "lex.en.100k.015440": {"vi": "hoàn toàn không có khả năng tự vệ"},  # defenseless
    "lex.en.100k.015443": {"vi": "hiện tượng quang học nhiễu xạ sóng"},  # diffraction (purged single-word 'nhiễu xạ')
    "lex.en.100k.015444": {"vi": "đổ nát xập xệ hoang phế; tồi tàn"},  # dilapidated
    "lex.en.100k.015445": {"vi": "mổ xẻ giải phẫu; mổ xẻ phân tích kỹ"},  # dissect
    "lex.en.100k.015446": {"vi": "chuông bấm gọi cửa ở cổng vào"},  # doorbell
    "lex.en.100k.015447": {"vi": "máy hút nạo vét bùn sông; nạo vét"},  # dredge
    "lex.en.100k.015448": {"vi": "nước dãi chảy nhỏ ròng; thèm muốn"},  # drool
    "lex.en.100k.015449": {"vi": "chạy về hướng đông; theo hướng đông"},  # eastbound
    "lex.en.100k.015450": {"vi": "dám nghĩ dám làm; táo bạo linh hoạt"},  # enterprising
    "lex.en.100k.015453": {"vi": "nằm ở ngoài tế bào; dịch ngoại bào"},  # extracellular (purged single-word 'ngoại bào')
    "lex.en.100k.015454": {"vi": "nhiệt thành tha thiết; nồng cháy"},  # fervent
    "lex.en.100k.015455": {"vi": "thuộc nghĩa vụ ủy thác trung thực"},  # fiduciary
    "lex.en.100k.015456": {"vi": "kẻ dàn xếp ngầm; người sửa chữa"},  # fixer (purged crawler truncated string)
    "lex.en.100k.015457": {"vi": "chuyến đột kích ngắn; bước lấn sân"},  # foray
    "lex.en.100k.015458": {"vi": "độ tuổi bốn mươi; thập niên 1940"},  # forties
    "lex.en.100k.015459": {"vi": "thuộc phân số; chia từng phần nhỏ"},  # fractional
    "lex.en.100k.015460": {"vi": "tàu thủy chở hàng; máy bay chở hàng"},  # freighter
    "lex.en.100k.015461": {"vi": "tu sĩ dòng khất thực (Công giáo)"},  # friar
    "lex.en.100k.015462": {"vi": "lớp kem đường phủ mặt bánh ngọt"},  # frosting
    "lex.en.100k.015463": {"vi": "uổng công vô ích; không kết quả"},  # fruitless
    "lex.en.100k.015464": {"vi": "khó tính kỹ tính; quá mức cầu kỳ"},  # fussy
    "lex.en.100k.015465": {"vi": "rau thơm trang trí món ăn; khấu trừ"},  # garnish
    "lex.en.100k.015466": {"vi": "con linh dương đầu bò (châu Phi)"},  # gnu
    "lex.en.100k.015467": {"vi": "món ngon kẹo bánh; quà vặt hấp dẫn"},  # goody
    "lex.en.100k.015470": {"vi": "bước tiến triển; sự tiến bộ đáng kể"},  # headway
    "lex.en.100k.015471": {"vi": "tin đồn nghe lại; lời đồn thổi"},  # hearsay
    "lex.en.100k.015472": {"vi": "làm ấm lòng người; xúc động sâu sắc"},  # heartwarming
    "lex.en.100k.015473": {"vi": "nơi trú ẩn bí mật; sào huyệt trốn"},  # hideout
    "lex.en.100k.015474": {"vi": "những người theo văn hóa Hippie"},  # hippies
    "lex.en.100k.015475": {"vi": "thuộc về ảnh toàn ký ba chiều nổi"},  # holographic
    "lex.en.100k.015476": {"vi": "mộc mạc ấm cúng; ngoại hình kém sắc"},  # homely
    "lex.en.100k.015477": {"vi": "có đôi sừng nhọn hoắt trên đầu"},  # horned
    "lex.en.100k.015478": {"vi": "chuồng nuôi thỏ gỗ; tủ chạn có ngăn"},  # hutch
    "lex.en.100k.015480": {"vi": "thanh bình đẹp như tranh; thơ mộng"},  # idyllic
    "lex.en.100k.015482": {"vi": "hoàn toàn bất lực; chứng bất lực"},  # impotent
    "lex.en.100k.015484": {"vi": "chất gây cháy hỏa hoạn; kích động"},  # incendiary
    "lex.en.100k.015485": {"vi": "không thể phá hủy; kiên cố bất diệt"},  # indestructible
    "lex.en.100k.015486": {"vi": "không thể tha thứ; khó dung thứ nổi"},  # inexcusable
    "lex.en.100k.015488": {"vi": "một cách thông minh khôn ngoan"},  # intelligently
    "lex.en.100k.015489": {"vi": "ngắt quãng từng đợt; chập chờn"},  # intermittently
    "lex.en.100k.015491": {"vi": "cầu tàu cập bến; bờ kè đê chắn sóng"},  # jetty
    "lex.en.100k.015492": {"vi": "có màu vàng đất kaki; vải ka-ki bền"},  # khaki
    "lex.en.100k.015493": {"vi": "đồng kíp Lào; giấc ngủ chợp mắt"},  # kip
    "lex.en.100k.015494": {"vi": "gấu túi túi leo cây Koala châu Úc"},  # koala
    "lex.en.100k.015495": {"vi": "hòn đảo Kos Hy Lạp; dặm kos Ấn Độ"},  # kos
    "lex.en.100k.015496": {"vi": "mưa trút quất mạnh; dây thừng chằng"},  # lashing
    "lex.en.100k.015497": {"vi": "cặn bã lắng đọng đáy thùng rượu"},  # lees
    "lex.en.100k.015498": {"vi": "quân đoàn lê dương; đông đảo vô số"},  # legion
    "lex.en.100k.015499": {"vi": "thuộc về nghi lễ phụng vụ tôn giáo"},  # liturgical (purged single-word 'thuộc phụng vụ')
    "lex.en.100k.015500": {"vi": "dầu nhớt bôi trơn máy móc cơ khí"},  # lubricant (purged single-word 'dầu nhờn')
}

# Verify lengths <= 35
for k, v in OVERRIDES_B04_R01.items():
    if "vi" in v:
        assert len(v["vi"]) <= 35, f"Length > 35 for {k}: {v['vi']} ({len(v['vi'])})"

with open('content/english/qa-batches/batch-04.json', 'r', encoding='utf-8') as f:
    batch_data = json.load(f)

# Apply overrides to records in range 0 to 500
count = 0
for idx in range(0, 500):
    rec = batch_data['records'][idx]
    rid = rec['id']
    if rid in OVERRIDES_B04_R01:
        count += 1
        for field, val in OVERRIDES_B04_R01[rid].items():
            rec[field] = val
        rec['status'] = 'reviewed'

batch_data['reviewedCount'] = 500

with open('content/english/qa-batches/batch-04.json', 'w', encoding='utf-8') as f:
    json.dump(batch_data, f, ensure_ascii=False, indent=2)

print(f"Successfully applied Batch 04 Round 1 ({count} overrides). Reviewed: {batch_data['reviewedCount']}/5000.")
