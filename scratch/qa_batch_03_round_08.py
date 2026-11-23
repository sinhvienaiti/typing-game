import json

# Round 8 overrides (records 3500 to 4000, STT 3501 to 4000, IDs lex.en.100k.013501 to 014000)
OVERRIDES_B03_R08 = {
    # 3501-3550
    "lex.en.100k.013501": {"vi": "tên riêng Bernard"},  # bernard
    "lex.en.100k.013502": {"vi": "bằng cử nhân khoa học (BS)"},  # bs
    "lex.en.100k.013503": {"vi": "tên riêng Diana; công nương Diana"},  # diana
    "lex.en.100k.013504": {"vi": "tên riêng/họ Duncan"},  # duncan
    "lex.en.100k.013505": {"vi": "sóng FM (điều tần radio)"},  # fm
    "lex.en.100k.013506": {"vi": "tên riêng/họ Palmer"},  # palmer
    "lex.en.100k.013507": {"ipa": "/ˌpiː ˈɛs/", "vi": "tái bút (PS)"},  # ps
    "lex.en.100k.013508": {"ipa": "/ˌtiː ˈɛl/", "vi": "nguyên tố tali (Tl); tiếng Tagalog"},  # tl
    "lex.en.100k.013509": {"vi": "dung nham bazan aa; pin tiểu AA"},  # aa
    "lex.en.100k.013510": {"vi": "tên riêng/họ Bradley"},  # bradley
    "lex.en.100k.013511": {"vi": "thuộc triều vua Charles; tên riêng"},  # caroline
    "lex.en.100k.013513": {"vi": "nước Li-băng (Lebanon)"},  # lebanon
    "lex.en.100k.013514": {"vi": "thành phố Leeds (Anh)"},  # leeds
    "lex.en.100k.013515": {"vi": "tên riêng Leonard"},  # leonard
    "lex.en.100k.013516": {"vi": "thành phố Milwaukee (Mỹ)"},  # milwaukee
    "lex.en.100k.013517": {"vi": "khối quân sự Bắc Đại Tây Dương"},  # nato
    "lex.en.100k.013519": {"vi": "dòng họ Simpson; phim Simpsons"},  # simpson
    "lex.en.100k.013520": {"ipa": "/ˌtiː ˈɛks/", "vi": "tiểu bang Texas (viết tắt TX)"},  # tx
    "lex.en.100k.013521": {"vi": "nơi cư ngụ; chỗ ở nhà cửa"},  # abode
    "lex.en.100k.013522": {"vi": "chi cây thích (phong lá đỏ)"},  # acer
    "lex.en.100k.013523": {"vi": "hoóc-môn kích thích adrenaline"},  # adrenaline
    "lex.en.100k.013526": {"vi": "tên riêng/họ Arnold"},  # arnold
    "lex.en.100k.013527": {"vi": "thuộc về các vì sao; cõi tinh tú"},  # astral (purged single-word 'sao')
    "lex.en.100k.013532": {"vi": "tên họ Blair; cựu thủ tướng Blair"},  # blair
    "lex.en.100k.013533": {"vi": "sai lầm ngớ ngẩn; nước đi sai"},  # blunder
    "lex.en.100k.013534": {"pos": "noun", "vi": "tiền hối lộ; đút lót mua chuộc"},  # bribe
    "lex.en.100k.013538": {"vi": "thuộc người Celt; văn hóa Celt"},  # celtic
    "lex.en.100k.013539": {"vi": "người rượt đuổi; đồ uống kèm"},  # chaser
    "lex.en.100k.013540": {"vi": "sự trinh tiết; sự trong trắng"},  # chastity
    "lex.en.100k.013541": {"vi": "nguyên tố kim loại crôm (Cr)"},  # chromium
    "lex.en.100k.013543": {"vi": "con ngao; sò biển; tiền đô (lóng)"},  # clams (purged crawler 'tiền')
    "lex.en.100k.013545": {"pos": "noun", "vi": "vật có giá trị sưu tầm; sưu tập"},  # collectible
    "lex.en.100k.013548": {"vi": "sự nhượng bộ; thừa nhận thua"},  # conceding
    "lex.en.100k.013550": {"vi": "độ dẫn điện; tính dẫn nhiệt"},  # conductivity
    "lex.en.100k.013551": {"vi": "tuân thủ quy chuẩn; theo khuôn"},  # conform

    # 3551-3600
    "lex.en.100k.013553": {"vi": "lưỡi dao cày (máy cày đất)"},  # coulter
    "lex.en.100k.013554": {"vi": "thèm muốn tột cùng; khao khát"},  # crave
    "lex.en.100k.013555": {"vi": "phát điên loạn; cuồng trí"},  # crazed
    "lex.en.100k.013560": {"vi": "giải mã mật mã; đọc hiểu chữ xấu"},  # decipher
    "lex.en.100k.013565": {"vi": "chế độ ăn kiêng giảm cân"},  # dieting
    "lex.en.100k.013567": {"vi": "căn hộ thông tầng; truyền song công"},  # duplex
    "lex.en.100k.013570": {"vi": "hồ Eyre; tên riêng Eyre"},  # eyre
    "lex.en.100k.013572": {"pos": "noun", "vi": "đàn vĩ cầm; loay hoay nghịch vặt"},  # fiddle
    "lex.en.100k.013573": {"vi": "người hoàn thành chặng đua"},  # finisher
    "lex.en.100k.013574": {"vi": "cảnh hồi tưởng quá khứ (phim)"},  # flashback
    "lex.en.100k.013575": {"pos": "verb", "vi": "hưng thịnh phát triển; nét hoa mỹ"},  # flourish
    "lex.en.100k.013576": {"vi": "thiết bị tiện ích thông minh nhỏ"},  # gadget
    "lex.en.100k.013577": {"vi": "găng tay sắt giáp; thách đấu"},  # gauntlet
    "lex.en.100k.013580": {"vi": "môn bay lượn dù lượn; lướt êm"},  # gliding
    "lex.en.100k.013581": {"pos": "noun", "vi": "mảnh ghép mô; hối lộ tham nhũng"},  # graft (purged single-word 'ghép')
    "lex.en.100k.013582": {"vi": "tiếng chói tai; thanh song sắt"},  # grating
    "lex.en.100k.013583": {"vi": "thịt nướng vỉ; cuộc tra hỏi gắt"},  # grilling (purged single-word 'nướng')
    "lex.en.100k.013584": {"vi": "gà gô đen; càu nhàu phàn nàn"},  # grouse
    "lex.en.100k.013585": {"pos": "verb", "vi": "tiếng gầm gừ; tiếng sấm rền"},  # growl
    "lex.en.100k.013587": {"vi": "chiếc võng nằm thư giãn"},  # hammock (purged single-word 'võng')
    "lex.en.100k.013588": {"vi": "hậu cung nhiều thê thiếp"},  # harem
    "lex.en.100k.013590": {"vi": "nữ anh hùng; nữ nhân vật chính"},  # heroine
    "lex.en.100k.013591": {"vi": "thuộc Ấn Độ giáo (Hindu)"},  # hindu
    "lex.en.100k.013592": {"vi": "con hà mã (hippopotamus)"},  # hippo
    "lex.en.100k.013593": {"vi": "môn khúc côn cầu gậy Ireland"},  # hurling
    "lex.en.100k.013596": {"vi": "thuộc chủ nghĩa đế quốc"},  # imperialist
    "lex.en.100k.013597": {"vi": "thời gian ủ bệnh; ấp trứng"},  # incubation

    # 3601-3650
    "lex.en.100k.013601": {"vi": "trí tuệ; năng lực tư duy"},  # intellect
    "lex.en.100k.013603": {"vi": "trực giác; linh cảm mách bảo"},  # intuition
    "lex.en.100k.013604": {"vi": "Tổng thống Thomas Jefferson"},  # jefferson
    "lex.en.100k.013605": {"vi": "điềm gở; kẻ mang vận xui"},  # jinx
    "lex.en.100k.013608": {"vi": "đường sữa tự nhiên (lactose)"},  # lactose
    "lex.en.100k.013609": {"vi": "sơ suất nhỏ; khoảng thời gian trôi"},  # lapse
    "lex.en.100k.013610": {"vi": "cơ xô lưng (thể hình); vĩ độ"},  # lat
    "lex.en.100k.013614": {"vi": "chất bôi trơn; dầu nhớt bôi trơn"},  # lube
    "lex.en.100k.013616": {"vi": "thuộc Hội Tam điểm (Freemason)"},  # masonic
    "lex.en.100k.013617": {"vi": "người dẫn chương trình (MC); máy"},  # mc
    "lex.en.100k.013619": {"pos": "prep", "vi": "trừ đi; dấu trừ; âm dưới không"},  # minus
    "lex.en.100k.013620": {"vi": "động từ khiếm khuyết; điệu thức"},  # modal
    "lex.en.100k.013622": {"vi": "hoàn toàn không có gì (lóng)"},  # nada (purged single-word 'không')
    "lex.en.100k.013624": {"vi": "thập niên 90; tuổi chín mươi"},  # nineties
    "lex.en.100k.013625": {"vi": "có mũi (dài/nhọn); tò mò ngửi"},  # nosed
    "lex.en.100k.013627": {"vi": "thanh tra viên giải quyết khiếu nại"},  # ombudsman
    "lex.en.100k.013630": {"vi": "tuyến tụy (cơ quan nội tạng)"},  # pancreas
    "lex.en.100k.013632": {"vi": "tước hiệu tổng đốc Pasha"},  # pasha
    "lex.en.100k.013635": {"vi": "con chim công đực sặc sỡ"},  # peacock (purged single-word 'công')
    "lex.en.100k.013637": {"vi": "hốc hác tiều tụy; bị kẹp chặt"},  # pinched
    "lex.en.100k.013641": {"pos": "verb", "vi": "lao mình xuống nước; sụt giảm"},  # plunge
    "lex.en.100k.013645": {"vi": "động vật linh trưởng; giám mục"},  # primate
    "lex.en.100k.013648": {"vi": "tâm trí; tâm hồn; tinh thần"},  # psyche
    "lex.en.100k.013649": {"vi": "sưng húp; phồng căng to"},  # puffy
    "lex.en.100k.013650": {"vi": "chim cút; co rúm sợ hãi"},  # quail

    # 3651-3700
    "lex.en.100k.013651": {"vi": "sự la lối om sòm; chửi bới dài"},  # ranting
    "lex.en.100k.013652": {"pos": "verb", "vi": "tái sinh; phục hồi tái tạo"},  # regenerate
    "lex.en.100k.013654": {"vi": "sự hối hận ăn năn; day dứt"},  # remorse
    "lex.en.100k.013655": {"vi": "kiên cường; dẻo dai đàn hồi"},  # resilient
    "lex.en.100k.013656": {"vi": "quán rượu miền Tây; xe sedan"},  # saloon
    "lex.en.100k.013657": {"vi": "kịch bản phim điện ảnh"},  # screenplay
    "lex.en.100k.013659": {"vi": "ủy mị đa cảm; thiên về tình cảm"},  # sentimental
    "lex.en.100k.013660": {"vi": "đại thi hào William Shakespeare"},  # shakespeare
    "lex.en.100k.013663": {"vi": "tin sốc gây kinh ngạc; chuyện sốc"},  # shocker
    "lex.en.100k.013664": {"vi": "mỡ trừu làm bánh; sự rút ngắn"},  # shortening
    "lex.en.100k.013667": {"vi": "sũng nước ẩm ướt; nhão nhoét"},  # soggy
    "lex.en.100k.013671": {"vi": "mang tính suy đoán; đầu cơ"},  # speculative
    "lex.en.100k.013672": {"vi": "lá lách; sự bực dọc cáu kỉnh"},  # spleen
    "lex.en.100k.013674": {"vi": "cầu thang bộ; lối cầu thang"},  # stairway (purged crawler 'lan can')
    "lex.en.100k.013676": {"pos": "verb", "vi": "cúi gập người; bậc thềm trước nhà"},  # stoop
    "lex.en.100k.013678": {"vi": "đủ để đáp ứng yêu cầu"},  # suffice (purged single-word 'đủ')
    "lex.en.100k.013683": {"vi": "tẻ nhạt chán ngắt; dài dòng"},  # tedious
    "lex.en.100k.013684": {"vi": "ngành viễn thông; truyền thông xa"},  # telecommunication
    "lex.en.100k.013689": {"vi": "ba lần (từ cổ/trang trọng)"},  # thrice
    "lex.en.100k.013692": {"pos": "noun", "vi": "nhánh sông phụ lưu; triều cống"},  # tributary
    "lex.en.100k.013693": {"vi": "các cây kèn trumpet; kèn đồng"},  # trumpets (purged crawler 'cây nắp ấm')
    "lex.en.100k.013694": {"vi": "sự hỗn loạn rối ren; náo động"},  # turmoil
    "lex.en.100k.013698": {"vi": "không có thế chấp; không khóa"},  # unsecured
    "lex.en.100k.013700": {"vi": "rời bỏ; dọn ra khỏi; bỏ trống"},  # vacate

    # 3701-3750
    "lex.en.100k.013706": {"vi": "dày dạn gió sương; bị bào mòn"},  # weathered
    "lex.en.100k.013707": {"vi": "khu Westminster (Luân Đôn)"},  # westminster
    "lex.en.100k.013708": {"vi": "chút xíu; mảy may một tí"},  # whit
    "lex.en.100k.013711": {"vi": "ngày càng tồi tệ hơn; xấu đi"},  # worsening
    "lex.en.100k.013712": {"vi": "thành phố Adelaide (Úc)"},  # adelaide
    "lex.en.100k.013713": {"vi": "tên riêng Alfred; vua Alfred"},  # alfred
    "lex.en.100k.013714": {"vi": "thủ đô Brussels (Bỉ)"},  # brussels
    "lex.en.100k.013715": {"ipa": "/ˌsiː ˈɑːr/", "vi": "nguyên tố crôm (Cr); tỷ lệ tín dụng"},  # cr
    "lex.en.100k.013717": {"vi": "hệ điều hành Linux"},  # linux
    "lex.en.100k.013718": {"vi": "thuộc Địa Trung Hải"},  # mediterranean
    "lex.en.100k.013719": {"vi": "tiền tố tân-; phong cách mới"},  # neo
    "lex.en.100k.013720": {"vi": "vùng đất/nhà nước Palestine"},  # palestine
    "lex.en.100k.013721": {"vi": "tên riêng/họ Reid"},  # reid
    "lex.en.100k.013722": {"vi": "tên họ Reynolds"},  # reynolds
    "lex.en.100k.013723": {"vi": "tên họ Stevens"},  # stevens
    "lex.en.100k.013724": {"vi": "tổ phụ Abraham; tên riêng"},  # abraham
    "lex.en.100k.013725": {"vi": "tên riêng/họ Bryan"},  # bryan
    "lex.en.100k.013727": {"vi": "nhà tiên tri Mô-sê (Moses)"},  # moses
    "lex.en.100k.013728": {"vi": "thành phố Nashville (Mỹ)"},  # nashville
    "lex.en.100k.013730": {"vi": "thủ đô Ottawa (Canada)"},  # ottawa
    "lex.en.100k.013731": {"vi": "Đại học Stanford danh tiếng"},  # stanford
    "lex.en.100k.013733": {"vi": "thủ đô Viên (Vienna, Áo)"},  # vienna
    "lex.en.100k.013734": {"vi": "tên riêng/họ Brady"},  # brady
    "lex.en.100k.013735": {"vi": "thành phố Brisbane (Úc)"},  # brisbane
    "lex.en.100k.013736": {"vi": "tên riêng/họ Glenn"},  # glenn
    "lex.en.100k.013738": {"vi": "tên riêng Joel"},  # joel
    "lex.en.100k.013739": {"vi": "giấy phép lái xe; giấy phép"},  # licence
    "lex.en.100k.013740": {"ipa": "/ˌɛn ˈdʒeɪ/", "vi": "tiểu bang New Jersey (viết tắt NJ)"},  # nj
    "lex.en.100k.013742": {"vi": "sông Po (Ý); nguyên tố poloni"},  # po
    "lex.en.100k.013744": {"vi": "đạo luật RICO; đảo Puerto Rico"},  # rico
    "lex.en.100k.013745": {"vi": "từ viết tắt; chữ viết tắt"},  # abbreviation (purged crawler 'bài tóm tắt')
    "lex.en.100k.013748": {"vi": "sĩ quan phụ tá; chim già đẫy"},  # adjutant
    "lex.en.100k.013750": {"vi": "đẹp như thiên thần; thánh thiện"},  # angelic (purged single-word 'thiên thần')

    # 3751-3800
    "lex.en.100k.013753": {"vi": "thiết bị điện gia dụng gia đình"},  # appliance
    "lex.en.100k.013756": {"vi": "hạm đội tàu chiến hùng hậu"},  # armada
    "lex.en.100k.013759": {"vi": "khoang giếng trời; tâm nhĩ tim"},  # atrium
    "lex.en.100k.013760": {"vi": "mang tính tự truyện cuộc đời"},  # autobiographical
    "lex.en.100k.013761": {"vi": "nước Băng-la-đét (Bangladesh)"},  # bangladesh
    "lex.en.100k.013764": {"vi": "phim bom tấn; sách bán chạy kỷ lục"},  # blockbuster
    "lex.en.100k.013765": {"vi": "bảo vệ quán bar/hộp đêm"},  # bouncer
    "lex.en.100k.013766": {"vi": "bó hoa tươi; hương thơm rượu vang"},  # bouquet
    "lex.en.100k.013767": {"vi": "trong lành sảng khoái; nẹp giữ"},  # bracing
    "lex.en.100k.013769": {"vi": "gánh nặng chính; mũi chịu đòn"},  # brunt
    "lex.en.100k.013770": {"vi": "còi báo động; nút bấm chuông"},  # buzzer
    "lex.en.100k.013771": {"vi": "nhịp điệu câu; tiết tấu âm nhạc"},  # cadence
    "lex.en.100k.013772": {"vi": "vải len casơmia thượng hạng"},  # cashmere
    "lex.en.100k.013773": {"vi": "loài ngỗng tuyết; họ Trần"},  # chen
    "lex.en.100k.013774": {"vi": "ớt bột hun khói chipotle"},  # chipotle
    "lex.en.100k.013778": {"vi": "mật mã học; số không; nhân vật phụ"},  # cipher
    "lex.en.100k.013779": {"vi": "theo hoàn cảnh; chứng cứ gián tiếp"},  # circumstantial
    "lex.en.100k.013784": {"vi": "nhân viên hỗ trợ khách sạn"},  # concierge
    "lex.en.100k.013785": {"vi": "sự giam cầm; sự ở cữ sinh nở"},  # confinement
    "lex.en.100k.013787": {"pos": "verb", "vi": "gìn giữ bảo tồn; mứt quả nấu đông"},  # conserve
    "lex.en.100k.013788": {"vi": "công ty tư vấn; dịch vụ tư vấn"},  # consultancy
    "lex.en.100k.013789": {"vi": "người coi sóc bảo quản; quản thủ"},  # custodian
    "lex.en.100k.013790": {"vi": "nang u nang; bao nang vi sinh"},  # cyst
    "lex.en.100k.013791": {"vi": "tín hiệu tạch tạch (mã Morse)"},  # dah
    "lex.en.100k.013796": {"vi": "mẫu số chung (toán học)"},  # denominator
    "lex.en.100k.013799": {"pos": "verb", "vi": "vứt bỏ; loại bỏ; lá bài vứt đi"},  # discard

    # 3801-3850
    "lex.en.100k.013804": {"vi": "lên tàu khởi hành; bắt đầu"},  # embark (purged single-word 'lên tàu')
    "lex.en.100k.013808": {"vi": "lời bạt; phần kết tác phẩm"},  # epilogue
    "lex.en.100k.013811": {"vi": "sử dụng sức lực; tạo áp lực"},  # exert
    "lex.en.100k.013812": {"vi": "vở kịch hề hước; trò hề lố bịch"},  # farce
    "lex.en.100k.013813": {"pos": "noun", "vi": "thuộc loài mèo; con mèo"},  # feline (purged single-word 'mèo')
    "lex.en.100k.013814": {"vi": "hay thay đổi thất thường; phù phiếm"},  # fickle
    "lex.en.100k.013815": {"vi": "con đom đóm phát sáng"},  # firefly
    "lex.en.100k.013816": {"vi": "thành phố Florence (Ý)"},  # florence
    "lex.en.100k.013818": {"vi": "tìm kiếm thức ăn; thức ăn gia súc"},  # forage
    "lex.en.100k.013821": {"vi": "xứ Ga-li-lê (Galilee)"},  # galilee
    "lex.en.100k.013822": {"pos": "verb", "vi": "vật lộn đối mặt; móc câu bám"},  # grapple
    "lex.en.100k.013823": {"pos": "verb", "vi": "tiếng rên rỉ than vãn; rên"},  # groan (purged single-word 'rên')
    "lex.en.100k.013824": {"vi": "ấu trùng sâu bọ; thức ăn (lóng)"},  # grub
    "lex.en.100k.013826": {"vi": "bá quyền lãnh đạo; quyền thống trị"},  # hegemony
    "lex.en.100k.013827": {"vi": "gỗ mại châu (gỗ hickory)"},  # hickory
    "lex.en.100k.013828": {"vi": "bệnh nổi mề đay; tổ ong"},  # hives
    "lex.en.100k.013830": {"vi": "nữ chủ nhà; nữ tiếp viên"},  # hostess
    "lex.en.100k.013831": {"pos": "noun", "vi": "cơn hờn dỗi tức tối; thở hổn hển"},  # huff
    "lex.en.100k.013832": {"vi": "người đàn ông vạm vỡ cuốn hút"},  # hunk
    "lex.en.100k.013833": {"vi": "thôi miên; thuốc an thần gây ngủ"},  # hypnotic
    "lex.en.100k.013836": {"vi": "kích động xúi giục nổi loạn"},  # incite
    "lex.en.100k.013838": {"vi": "lồng ấp trẻ sơ sinh; vườn ươm DN"},  # incubator
    "lex.en.100k.013842": {"vi": "lởm chởm sắc nhọn; răng cưa"},  # jagged
    "lex.en.100k.013843": {"vi": "khoa học pháp lý; môn luật học"},  # jurisprudence
    "lex.en.100k.013847": {"vi": "món mì xếp lớp nướng (lasagna)"},  # lasagna
    "lex.en.100k.013848": {"vi": "đóng cửa xưởng ngăn công nhân"},  # lockout
    "lex.en.100k.013849": {"pos": "verb", "vi": "khung cửi dệt; hiện ra sừng sững"},  # loom

    # 3851-3900
    "lex.en.100k.013852": {"vi": "mi-li-mét (mm)"},  # millimeter
    "lex.en.100k.013853": {"vi": "hào nước quanh thành trì"},  # moat
    "lex.en.100k.013854": {"vi": "bùn lầy bẩn thỉu; dọn phân bùn"},  # muck
    "lex.en.100k.013856": {"vi": "tối tăm mờ mịt; u ám đáng ngờ"},  # murky (purged single-word 'đục')
    "lex.en.100k.013857": {"vi": "tóm gọn; bắt giữ quả tang"},  # nab
    "lex.en.100k.013863": {"ipa": "/əˈfɛns/", "vi": "sự xúc phạm; hành vi vi phạm"},  # offence
    "lex.en.100k.013864": {"vi": "điềm báo trước; điềm lành/dữ"},  # omen (purged single-word 'điềm')
    "lex.en.100k.013866": {"vi": "con rái cá (động vật)"},  # otter
    "lex.en.100k.013868": {"vi": "toàn cảnh bao quát; tầm nhìn rộng"},  # panorama
    "lex.en.100k.013869": {"vi": "kẻ chịu trận oan; tốt thế mạng"},  # patsy
    "lex.en.100k.013870": {"vi": "sự sám hối đền tội; việc phạt tạ"},  # penance
    "lex.en.100k.013872": {"vi": "chất oxy già peroxide; thuốc tẩy"},  # peroxide
    "lex.en.100k.013874": {"vi": "ngựa đốm khoang pinto; đậu pinto"},  # pinto
    "lex.en.100k.013876": {"vi": "phi lý vô lý đến nực cười"},  # preposterous
    "lex.en.100k.013881": {"vi": "bị bệnh dại; cuồng tín điên cuồng"},  # rabid (purged single-word 'dại')
    "lex.en.100k.013882": {"vi": "vật hiếm có; sự quý hiếm"},  # rarity
    "lex.en.100k.013884": {"vi": "tên riêng Rebecca; Rê-bê-ca"},  # rebecca
    "lex.en.100k.013885": {"vi": "sạc lại pin; nạp lại năng lượng"},  # recharge
    "lex.en.100k.013887": {"vi": "dân quê thô lỗ (miệt thị ở Mỹ)"},  # redneck
    "lex.en.100k.013889": {"vi": "nhắc lại nhiều lần; tái khẳng định"},  # reiterate
    "lex.en.100k.013891": {"vi": "oán giận phẫn uất; bực bội"},  # resent
    "lex.en.100k.013894": {"vi": "thuộc võng mạc mắt"},  # retinal
    "lex.en.100k.013896": {"pos": "verb", "vi": "tiếng ầm ầm rền vang; cuộc ẩu đả"},  # rumble
    "lex.en.100k.013898": {"vi": "cái tua-vít vặn ốc (screwdriver)"},  # screwdriver
    "lex.en.100k.013900": {"vi": "nóng bỏng sôi sục; xèo xèo"},  # sizzling

    # 3901-3950
    "lex.en.100k.013905": {"vi": "rộng rãi thoáng đãng"},  # spacious (purged single-word 'rộng')
    "lex.en.100k.013906": {"vi": "khắc khổ giản dị; dũng mãnh"},  # spartan
    "lex.en.100k.013908": {"vi": "sự giẫm đạp tháo chạy tán loạn"},  # stampede
    "lex.en.100k.013909": {"vi": "sự bế tắc đối đầu giằng co"},  # standoff
    "lex.en.100k.013914": {"vi": "vụ nổ siêu tân tinh (thiên văn)"},  # supernova
    "lex.en.100k.013915": {"vi": "mê tín dị đoan; mù quáng"},  # superstitious
    "lex.en.100k.013916": {"vi": "bản tóm tắt nội dung cốt truyện"},  # synopsis
    "lex.en.100k.013923": {"vi": "lớp gỗ dán bề mặt; vỏ bọc ngoài"},  # veneer
    "lex.en.100k.013924": {"vi": "độ nhớt quánh (chất lỏng)"},  # viscosity
    "lex.en.100k.013927": {"vi": "bánh xốp giòn; tấm wafer bán dẫn"},  # wafer
    "lex.en.100k.013928": {"vi": "phù thủy xuất chúng; bậc thầy giỏi"},  # wiz
    "lex.en.100k.013930": {"pos": "noun", "vi": "tiếng chó sủa gâu gâu; sợi ngang"},  # woof
    "lex.en.100k.013932": {"vi": "bò Tây Tạng (lông dài)"},  # yak
    "lex.en.100k.013933": {"vi": "tên riêng Adrian; hoàng đế La Mã"},  # adrian
    "lex.en.100k.013934": {"ipa": "/kɒl/", "vi": "đèo núi yên ngựa (địa lý)"},  # col
    "lex.en.100k.013938": {"vi": "tên riêng Frederick"},  # frederick
    "lex.en.100k.013942": {"vi": "tên riêng Pierre"},  # pierre
    "lex.en.100k.013943": {"vi": "Tổng thống Mỹ Ronald Reagan"},  # reagan
    "lex.en.100k.013944": {"pos": "num", "vi": "mười sáu (16)"},  # sixteen (pos fixed)
    "lex.en.100k.013945": {"vi": "tập đoàn ô tô Toyota; thành phố"},  # toyota
    "lex.en.100k.013946": {"vi": "tên riêng/họ Curtis"},  # curtis
    "lex.en.100k.013948": {"vi": "tháng Chín (viết tắt Sep)"},  # sep
    "lex.en.100k.013950": {"vi": "tên riêng/họ Andrews"},  # andrews

    # 3951-4000
    "lex.en.100k.013951": {"vi": "Đại học UC Berkeley; thành phố"},  # berkeley
    "lex.en.100k.013953": {"vi": "triều đại nhà Hán; người Hán"},  # han
    "lex.en.100k.013954": {"vi": "tổ phụ Isaac; tên Isaac"},  # isaac
    "lex.en.100k.013955": {"vi": "pao (đơn vị pound, viết tắt lb)"},  # lb
    "lex.en.100k.013956": {"vi": "thành phố Leicester (nước Anh)"},  # leicester
    "lex.en.100k.013957": {"vi": "nguyên tố kim loại niken (Ni)"},  # ni
    "lex.en.100k.013958": {"vi": "ông Nô-ê (con tàu Noah)"},  # noah
    "lex.en.100k.013959": {"vi": "ủy ban hành động chính trị (PAC)"},  # pac
    "lex.en.100k.013960": {"vi": "thành phố Perth (nước Úc)"},  # perth
    "lex.en.100k.013961": {"vi": "quỷ Sa-tăng (Satan)"},  # satan
    "lex.en.100k.013963": {"pos": "num", "vi": "sáu mươi (60)"},  # sixty (pos fixed)
    "lex.en.100k.013964": {"vi": "tên họ Sullivan"},  # sullivan
    "lex.en.100k.013966": {"vi": "thành phố Venice (nước Ý)"},  # venice
    "lex.en.100k.013975": {"pos": "verb", "vi": "phản tác dụng; nổ ngược động cơ"},  # backfire
    "lex.en.100k.013977": {"vi": "cây thủy dương; tên họ Bennet"},  # bennet
    "lex.en.100k.013978": {"vi": "nhà thờ thánh Bethel; nơi thánh"},  # bethel
    "lex.en.100k.013982": {"vi": "vốn hóa thị trường; sự viết hoa"},  # capitalization
    "lex.en.100k.013986": {"vi": "bánh mì kẹp phô mai thịt băm"},  # cheeseburger
    "lex.en.100k.013987": {"vi": "kèn clarinet (nhạc cụ hơi)"},  # clarinet
    "lex.en.100k.013988": {"pos": "verb", "vi": "móc cài khóa; siết chặt lấy"},  # clasp
    "lex.en.100k.013991": {"vi": "miễn phí tặng kèm; khen ngợi"},  # complimentary
    "lex.en.100k.013992": {"vi": "chứng táo bón (tiêu hóa)"},  # constipation
    "lex.en.100k.013994": {"pos": "noun", "vi": "hàng buôn lậu; hàng cấm nhập"},  # contraband (purged single-word 'lậu')
    "lex.en.100k.013995": {"vi": "có tính ăn mòn rỉ sét; gay gắt"},  # corrosive
    "lex.en.100k.013997": {"vi": "tính hèn nhát; sự nhát gan"},  # cowardice
    "lex.en.100k.013998": {"vi": "làm duyên e thẹn; lấp lửng kín"},  # coy
    "lex.en.100k.014000": {"vi": "máy nghiền đá quặng; người đè bẹp"},  # crusher
}

# Verify lengths <= 35
for k, v in OVERRIDES_B03_R08.items():
    if "vi" in v:
        assert len(v["vi"]) <= 35, f"Length > 35 for {k}: {v['vi']} ({len(v['vi'])})"

with open('content/english/qa-batches/batch-03.json', 'r', encoding='utf-8') as f:
    batch_data = json.load(f)

# Apply overrides to records in range 3500 to 4000
count = 0
for idx in range(3500, 4000):
    rec = batch_data['records'][idx]
    rid = rec['id']
    if rid in OVERRIDES_B03_R08:
        count += 1
        for field, val in OVERRIDES_B03_R08[rid].items():
            rec[field] = val
        rec['status'] = 'reviewed'

batch_data['reviewedCount'] = 4000

with open('content/english/qa-batches/batch-03.json', 'w', encoding='utf-8') as f:
    json.dump(batch_data, f, ensure_ascii=False, indent=2)

print(f"Successfully applied Batch 03 Round 8 ({count} overrides). Reviewed: {batch_data['reviewedCount']}/5000.")
