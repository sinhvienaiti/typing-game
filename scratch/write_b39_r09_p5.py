import json

items = [
    ("094403", "tropomyosin", "noun", "/ˌtrɑpoʊˈmaɪəsɪn/", "protein cơ tropomyosin"),
    ("094404", "troponomy", "noun", "/trəˈpɑnəmi/", "ngữ nghĩa cách thức; địa danh học"),
    ("094405", "troponym", "noun", "/ˈtrɑpəˌnɪm/", "động từ chỉ cách thức hành động"),
    ("094406", "troponymy", "noun", "/trəˈpɑnəmi/", "quan hệ động từ chỉ cách thức"),
    ("094407", "tropophilous", "adj", "/trəˈpɑfələs/", "thích nghi khí hậu biến đổi mùa"),
    ("094408", "tropophyte", "noun", "/ˈtrɑpəˌfaɪt/", "thực vật thích nghi biến đổi mùa"),
    ("094409", "troppo", "adj", "/ˈtrɑpoʊ/", "rối loạn tâm thần do nắng nóng (Úc)"),
    ("094410", "trotline", "noun", "/ˈtrɑtˌlaɪn/", "dây câu giăng dài nhiều lưỡi câu"),
    ("094411", "trots", "verb", "/ˈtrɑts/", "chạy nước kiệu; đi bước nhỏ nhanh"),
    ("094412", "trotted", "verb", "/ˈtrɑtɪd/", "đã chạy nước kiệu; bước nhỏ nhanh"),
    ("094413", "trotters", "noun", "/ˈtrɑtɚz/", "ngựa chạy nước kiệu; móng giò lợn"),
    ("094414", "trotting", "verb", "/ˈtrɑtɪŋ/", "đang chạy nước kiệu; bước nhỏ nhanh"),
    ("094415", "trotyl", "noun", "/ˈtrɑtəl/", "thuốc nổ mạnh TNT (trotyl)"),
    ("094416", "troubler", "noun", "/ˈtrʌblɚ/", "kẻ gây rối; kẻ làm phiền muộn"),
    ("094417", "troubles", "verb", "/ˈtrʌbəlz/", "làm phiền; gây lo lắng rắc rối"),
    ("094418", "troubleshooted", "verb", "/ˈtrʌbəlˌʃutɪd/", "đã chẩn đoán và sửa chữa sự cố"),
    ("094419", "troubleshooters", "noun", "/ˈtrʌbəlˌʃutɚz/", "chuyên viên xử lý sự cố (số nhiều)"),
    ("094420", "troubleshooting", "noun", "/ˈtrʌbəlˌʃutɪŋ/", "quy trình tìm và sửa chữa sự cố"),
    ("094421", "troubleshoots", "verb", "/ˈtrʌbəlˌʃuts/", "chẩn đoán và khắc phục sự cố"),
    ("094422", "troublesomeness", "noun", "/ˈtrʌbəlsəmnəs/", "sự phiền toái; tính chất rắc rối"),
    ("094423", "troughing", "noun", "/ˈtrɔfɪŋ/", "hệ thống máng dẫn nước hoặc cáp"),
    ("094424", "trounced", "verb", "/ˈtraʊnst/", "đã đánh bại thảm hại; trừng trị"),
    ("094425", "trounces", "verb", "/ˈtraʊnsɪz/", "đánh bại áp đảo; trừng trị nặng"),
    ("094426", "trousering", "noun", "/ˈtraʊzɚɪŋ/", "vải dày chuyên dùng để may quần tây"),
    ("094427", "trousseaux", "noun", "/ˈtrusoʊz/", "của hồi môn áo váy cô dâu (số nhiều)"),
    ("094428", "trousses", "noun", "/ˈtrusɪz/", "áo giáp hông đùi; bao dao (số nhiều)"),
    ("094429", "troutlet", "noun", "/ˈtraʊtlɪt/", "cá hồi non kích thước nhỏ"),
    ("094430", "troutling", "noun", "/ˈtraʊtlɪŋ/", "cá hồi non kích thước nhỏ"),
    ("094431", "trouty", "adj", "/ˈtraʊti/", "có nhiều cá hồi; giống vị cá hồi"),
    ("094432", "trouvaille", "noun", "/truˈvaɪ/", "phát hiện tình cờ quý giá (từ Pháp)"),
    ("094433", "trover", "noun", "/ˈtroʊvɚ/", "vụ kiện đòi bồi thường chiếm giữ đồ"),
    ("094434", "trow", "verb", "/ˈtroʊ/", "nghĩ rằng; tin chắc rằng (từ cổ)"),
    ("094435", "trowed", "verb", "/ˈtroʊd/", "đã nghĩ rằng; đã tin rằng (từ cổ)"),
    ("094436", "trowelled", "verb", "/ˈtraʊəld/", "đã trát vữa bằng cái bay thợ hồ"),
    ("094437", "trowelling", "verb", "/ˈtraʊəlɪŋ/", "đang trát vữa bằng bay; xúc bằng bay"),
    ("094438", "trowels", "verb", "/ˈtraʊəlz/", "trát vữa bằng bay; xúc bằng bay"),
    ("094439", "trowing", "verb", "/ˈtroʊɪŋ/", "đang nghĩ rằng; đang tin tưởng (cổ)"),
    ("094440", "trows", "verb", "/ˈtroʊz/", "nghĩ rằng; tin tưởng (từ cổ)"),
    ("094441", "truanted", "verb", "/ˈtruəntɪd/", "đã trốn học; đã nghỉ học không phép"),
    ("094442", "truanting", "verb", "/ˈtruəntɪŋ/", "đang trốn học đi chơi"),
    ("094443", "truants", "verb", "/ˈtruənts/", "trốn học; cúp học đi chơi"),
    ("094444", "truceless", "adj", "/ˈtrusləs/", "không ngừng nghỉ; không đình chiến"),
    ("094445", "truckage", "noun", "/ˈtrʌkɪdʒ/", "cước vận chuyển hàng bằng xe tải"),
    ("094446", "trucked", "verb", "/ˈtrʌkt/", "đã chở bằng xe tải; trao đổi hàng"),
    ("094447", "truckful", "noun", "/ˈtrʌkˌfʊl/", "lượng hàng chất đầy một xe tải"),
    ("094448", "truckler", "noun", "/ˈtrʌklɚ/", "kẻ khúm núm nịnh hót xu thời"),
    ("094449", "truckling", "noun", "/ˈtrʌklɪŋ/", "thái độ khúm núm quỵ lụy cầu cạnh"),
    ("094450", "truckload", "noun", "/ˈtrʌkˌloʊd/", "một chuyến xe tải đầy; số lượng lớn"),
    ("094451", "truckman", "noun", "/ˈtrʌkmən/", "tài xế xe tải; người trồng rau chợ"),
    ("094452", "truckmaster", "noun", "/ˈtrʌkˌmæstɚ/", "sĩ quan phụ trách đổi hàng xưa"),
    ("094453", "truckmen", "noun", "/ˈtrʌkmən/", "tài xế xe tải; người trồng rau chợ"),
    ("094454", "trucks", "verb", "/ˈtrʌks/", "chuyên chở bằng xe tải; đổi chác"),
    ("094455", "truculency", "noun", "/ˈtrʌkjələnsi/", "tính hung hăng hiếu chiến tàn bạo"),
    ("094456", "trudged", "verb", "/ˈtrʌdʒd/", "đã lê bước nặng nhọc mệt mỏi"),
    ("094457", "trudgen", "noun", "/ˈtrʌdʒən/", "kiểu bơi trườn sấp chân ếch trudgen"),
    ("094458", "trudger", "noun", "/ˈtrʌdʒɚ/", "người lê bước đi bộ mệt nhọc"),
    ("094459", "trudges", "verb", "/ˈtrʌdʒɪz/", "lê bước đi nặng nhọc vất vả"),
    ("094460", "trudging", "verb", "/ˈtrʌdʒɪŋ/", "đang lê bước đi nặng nhọc vất vả"),
    ("094461", "trued", "verb", "/ˈtrud/", "đã cân chỉnh cho thật thẳng chuẩn"),
    ("094462", "truehearted", "adj", "/ˌtruˈhɑrtɪd/", "chân thành; thủy chung son sắt"),
    ("094463", "truepenny", "noun", "/ˈtruˌpɛni/", "người chính trực đáng tin (cổ)"),
    ("094464", "trues", "verb", "/ˈtruz/", "cân chỉnh đúng tâm thẳng chuẩn"),
    ("094465", "truffled", "adj", "/ˈtrʌfəld/", "có tẩm hoặc nhồi nấm cục truffle"),
    ("094466", "trug", "noun", "/ˈtrʌɡ/", "giỏ gỗ nông đựng hoa quả làm vườn"),
    ("094467", "truing", "verb", "/ˈtruɪŋ/", "đang cân chỉnh cho thật thẳng chuẩn"),
    ("094468", "truistic", "adj", "/truˈɪstɪk/", "hiển nhiên; mang tính chân lý sáo"),
    ("094469", "trull", "noun", "/ˈtrʌl/", "gái mại dâm; ả lẳng lơ (từ cổ)"),
    ("094470", "trumped", "verb", "/ˈtrʌmpt/", "đã đánh đè bằng quân át; vượt trội"),
    ("094471", "trumperies", "noun", "/ˈtrʌmpɚiz/", "đồ hào nhoáng vô giá trị (số nhiều)"),
    ("094472", "trumpeted", "verb", "/ˈtrʌmpətɪd/", "đã thổi kèn đồng; đã rêu rao ầm ĩ"),
    ("094473", "trumpetfish", "noun", "/ˈtrʌmpɪtˌfɪʃ/", "cá kèn mõm ống dài"),
    ("094474", "trumpeting", "verb", "/ˈtrʌmpətɪŋ/", "đang thổi kèn đồng; đang rêu rao"),
    ("094475", "trumpetwood", "noun", "/ˈtrʌmpɪtˌwʊd/", "cây thân rỗng cecropia Nam Mỹ"),
    ("094476", "trumpism", "noun", "/ˈtrʌmpɪzəm/", "chủ nghĩa chính trị của Donald Trump"),
    ("094477", "trumps", "verb", "/ˈtrʌmps/", "đánh át chủ bài; đánh bại vượt trội"),
    ("094478", "truncal", "adj", "/ˈtrʌŋkəl/", "thuộc thân mình hoặc thân chính"),
    ("094479", "truncates", "verb", "/ˈtrʌŋˌkeɪts/", "cắt cụt đầu đuôi; rút ngắn bớt"),
    ("094480", "truncating", "verb", "/ˈtrʌŋˌkeɪtɪŋ/", "đang cắt cụt; đang rút ngắn bớt"),
    ("094481", "truncocolumella", "noun", "/ˌtrʌŋkoʊˌkɑləˈmɛlə/", "chi nấm cục giả dưới đất"),
    ("094482", "trundled", "verb", "/ˈtrʌndəld/", "đã lăn bánh nặng nề; đẩy xe lăn"),
    ("094483", "trundler", "noun", "/ˈtrʌndlɚ/", "xe đẩy nhỏ; vận động viên ném bóng"),
    ("094484", "trundles", "verb", "/ˈtrʌndəlz/", "lăn bánh nặng nề; đẩy xe cút kít"),
    ("094485", "trundling", "verb", "/ˈtrʌndlɪŋ/", "đang lăn bánh nặng nề; đẩy xe"),
    ("094486", "trunked", "verb", "/ˈtrʌŋkt/", "đã kết nối đường trung kế (mạng)"),
    ("094487", "trunkfish", "noun", "/ˈtrʌŋkˌfɪʃ/", "cá hòm thân hộp giác"),
    ("094488", "trunkful", "noun", "/ˈtrʌŋkˌfʊl/", "lượng chứa đầy một rương hoặc cốp"),
    ("094489", "trunking", "verb", "/ˈtrʌŋkɪŋ/", "đang nối trung kế; máng đi dây điện"),
    ("094490", "trunklegs", "noun", "/ˈtrʌŋkˌlɛɡz/", "chân ngực của động vật giáp xác"),
    ("094491", "trunkless", "adj", "/ˈtrʌŋkləs/", "không có thân; không có vòi"),
    ("094492", "trunnel", "noun", "/ˈtrʌnəl/", "chốt gỗ cứng đóng mộng tàu thuyền"),
    ("094493", "trunnion", "noun", "/ˈtrʌnjən/", "ngõng trục xoay (nòng pháo, van)"),
    ("094494", "trusses", "verb", "/ˈtrʌsɪz/", "trói gô chặt; bó chặt; lắp giàn kèo"),
    ("094495", "trussing", "verb", "/ˈtrʌsɪŋ/", "đang trói gô; đang buộc chặt cánh gà"),
    ("094496", "trustable", "adj", "/ˈtrʌstəbəl/", "đáng tin cậy; có thể tin tưởng"),
    ("094497", "trustbuster", "noun", "/ˈtrʌstˌbʌstɚ/", "người phá thế độc quyền tập đoàn"),
    ("094498", "trustees", "noun", "/trʌsˈtiz/", "người ủy thác; ủy viên (số nhiều)"),
    ("094499", "trustfully", "adv", "/ˈtrʌstfəli/", "tin tưởng; tin cậy hoàn toàn"),
    ("094500", "trustfulness", "noun", "/ˈtrʌstfəlnəs/", "tính dễ tin người; lòng tin tưởng"),
    ("094501", "trustification", "noun", "/ˌtrʌstəfəˈkeɪʃən/", "sự sáp nhập thành tập đoàn độc quyền"),
    ("094502", "trustify", "verb", "/ˈtrʌstəˌfaɪ/", "tổ chức thành tập đoàn độc quyền"),
]

# Trim <=35:
items[23] = ("094426", "trousering", "noun", "/ˈtraʊzɚɪŋ/", "vải dày dùng để may quần tây")
items[24] = ("094427", "trousseaux", "noun", "/ˈtrusoʊz/", "tư trang hồi môn cô dâu (số nhiều)")
items[25] = ("094428", "trousses", "noun", "/ˈtrusɪz/", "giáp hông đùi; bao dao (số nhiều)")
items[30] = ("094433", "trover", "noun", "/ˈtroʊvɚ/", "vụ kiện đòi bồi thường đồ bị chiếm")
items[32] = ("094435", "trowed", "verb", "/ˈtroʊd/", "đã nghĩ rằng; đã tin rằng (cổ)")
items[34] = ("094437", "trowelling", "verb", "/ˈtraʊəlɪŋ/", "đang trát vữa bằng bay thợ hồ")
items[38] = ("094441", "truanted", "verb", "/ˈtruəntɪd/", "đã trốn học; nghỉ học không phép")
items[47] = ("094450", "truckload", "noun", "/ˈtrʌkˌloʊd/", "một chuyến xe tải đầy; lượng lớn")
items[54] = ("094457", "trudgen", "noun", "/ˈtrʌdʒən/", "kiểu bơi trườn sấp chân ếch")
items[68] = ("094471", "trumperies", "noun", "/ˈtrʌmpɚiz/", "đồ hào nhoáng rẻ tiền (số nhiều)")
items[71] = ("094474", "trumpeting", "verb", "/ˈtrʌmpətɪŋ/", "đang thổi kèn đồng; rêu rao ầm ĩ")
items[73] = ("094476", "trumpism", "noun", "/ˈtrʌmpɪzəm/", "chủ nghĩa chính trị Donald Trump")
items[80] = ("094483", "trundler", "noun", "/ˈtrʌndlɚ/", "xe đẩy nhỏ; cầu thủ ném bóng")
items[86] = ("094489", "trunking", "verb", "/ˈtrʌŋkɪŋ/", "đang nối trung kế; máng đi dây")
items[92] = ("094495", "trussing", "verb", "/ˈtrʌsɪŋ/", "đang trói gô; buộc chặt cánh gà")
items[98] = ("094501", "trustification", "noun", "/ˌtrʌstəfəˈkeɪʃən/", "sự lập tập đoàn độc quyền")

with open("scratch/b39_r09_p5.json", "w") as f:
    json.dump(items, f, ensure_ascii=False, indent=2)
print("Wrote p5:", len(items))
