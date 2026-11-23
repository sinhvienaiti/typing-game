# Batch 09 Round 7 Manual QA overrides (records 3000-3499, IDs 043002-043501)
import json

OVERRIDES_PART1 = {
    "lex.en.100k.043002": {
        "hw": "maguey",
        "pos": "noun",
        "vi": "cây thùa dệt sợi và ủ rượu",
        "ipa": "/məˈɡeɪ/"
    },
    "lex.en.100k.043003": {
        "hw": "majorette",
        "pos": "noun",
        "vi": "nữ múa gậy dẫn đầu đoàn diễu hành",
        "ipa": "/ˌmeɪdʒəˈrɛt/"
    },
    "lex.en.100k.043004": {
        "hw": "mammalogy",
        "pos": "noun",
        "vi": "ngành nghiên cứu động vật có vú",
        "ipa": "/məˈmælədʒi/"
    },
    "lex.en.100k.043005": {
        "hw": "mandragora",
        "pos": "noun",
        "vi": "cây khoai ma; chi khoai ma dược",
        "ipa": "/mænˈdræɡərə/"
    },
    "lex.en.100k.043006": {
        "hw": "mantilla",
        "pos": "noun",
        "vi": "khăn choàng ren trùm đầu",
        "ipa": "/mænˈtɪlə/"
    },
    "lex.en.100k.043007": {
        "hw": "meitner",
        "pos": "noun",
        "vi": "nhà vật lý hạt nhân Lise Meitner",
        "ipa": "/ˈmaɪtnɚ/"
    },
    "lex.en.100k.043008": {
        "hw": "melena",
        "pos": "noun",
        "vi": "chứng đi ngoài phân đen có máu",
        "ipa": "/məˈliːnə/"
    },
    "lex.en.100k.043009": {
        "hw": "mignonette",
        "pos": "noun",
        "vi": "cây mộc hương hoa thơm viền vườn",
        "ipa": "/ˌmɪnjəˈnɛt/"
    },
    "lex.en.100k.043010": {
        "hw": "milage",
        "pos": "noun",
        "vi": "tổng dặm đường; định mức số dặm",
        "ipa": "/ˈmaɪlɪdʒ/"
    },
    "lex.en.100k.043011": {
        "hw": "molder",
        "pos": "verb",
        "vi": "mục nát; phân hủy mục rữa",
        "ipa": "/ˈmoʊldɚ/"
    },
    "lex.en.100k.043012": {
        "hw": "morganite",
        "pos": "noun",
        "vi": "ngọc beryl hồng morganit",
        "ipa": "/ˈmɔːrɡənaɪt/"
    },
    "lex.en.100k.043013": {
        "hw": "morus",
        "pos": "noun",
        "vi": "chi cây dâu tằm Morus",
        "ipa": "/ˈmɔːrəs/"
    },
    "lex.en.100k.043014": {
        "hw": "myelinated",
        "pos": "adj",
        "vi": "có bao myelin bao bọc thần kinh",
        "ipa": "/ˈmaɪəlɪneɪtɪd/"
    },
    "lex.en.100k.043015": {
        "hw": "nandrolone",
        "pos": "noun",
        "vi": "hoóc-môn đồng hóa nandrolone",
        "ipa": "/ˈnændroʊloʊn/"
    },
    "lex.en.100k.043016": {
        "hw": "nightspot",
        "pos": "noun",
        "vi": "hộp đêm; quán bar giải trí đêm",
        "ipa": "/ˈnaɪtspɑːt/"
    },
    "lex.en.100k.043017": {
        "hw": "nontechnical",
        "pos": "adj",
        "vi": "phi kỹ thuật; không chuyên môn",
        "ipa": "/ˌnɑːntɛkˈnɪkəl/"
    },
    "lex.en.100k.043018": {
        "hw": "oleaginous",
        "pos": "adj",
        "vi": "nhờn bóng như dầu; nịnh hót giả tạo",
        "ipa": "/ˌoʊliˈædʒɪnəs/"
    },
    "lex.en.100k.043019": {
        "hw": "omiya",
        "pos": "noun",
        "vi": "thành phố Omiya tại Nhật Bản",
        "ipa": "/oʊˈmiːjə/"
    },
    "lex.en.100k.043020": {
        "hw": "organon",
        "pos": "noun",
        "vi": "hệ thống nguyên lý tư duy lập luận",
        "ipa": "/ˈɔːrɡənɑːn/"
    },
    "lex.en.100k.043021": {
        "hw": "orison",
        "pos": "noun",
        "vi": "lời cầu nguyện khẩn thiết",
        "ipa": "/ˈɔːrɪzən/"
    },
    "lex.en.100k.043022": {
        "hw": "overemphasize",
        "pos": "verb",
        "vi": "nhấn mạnh thái quá; thổi phồng",
        "ipa": "/ˌoʊvərˈɛmfəsaɪz/"
    },
    "lex.en.100k.043023": {
        "hw": "pablum",
        "pos": "noun",
        "vi": "cháo trẻ em; ý tưởng nhạt nhẽo sáo",
        "ipa": "/ˈpæbləm/"
    },
    "lex.en.100k.043024": {
        "hw": "panhandler",
        "pos": "noun",
        "vi": "người ăn xin trên đường phố",
        "ipa": "/ˈpænhændlɚ/"
    },
    "lex.en.100k.043025": {
        "hw": "papaw",
        "pos": "noun",
        "vi": "cây đu đủ; quả pawpaw Bắc Mỹ",
        "ipa": "/pɔːˈpɔː/"
    },
    "lex.en.100k.043026": {
        "hw": "pasang",
        "pos": "noun",
        "vi": "dê hoang dã Trung Đông",
        "ipa": "/ˈpɑːsæŋ/"
    },
    "lex.en.100k.043027": {
        "hw": "patency",
        "pos": "noun",
        "vi": "tình trạng thông suốt thông mạch",
        "ipa": "/ˈpeɪtənsi/"
    },
    "lex.en.100k.043028": {
        "hw": "personalty",
        "pos": "noun",
        "vi": "động sản cá nhân theo luật",
        "ipa": "/ˈpɝːsənəlti/"
    },
    "lex.en.100k.043029": {
        "hw": "perspicacity",
        "pos": "noun",
        "vi": "sự nhạy bén; óc nhìn sáng suốt",
        "ipa": "/ˌpɝːspɪˈkæsəti/"
    },
    "lex.en.100k.043030": {
        "hw": "pinnately",
        "pos": "adv",
        "vi": "theo hình dạng lông chim kép",
        "ipa": "/ˈpɪneɪtli/"
    },
    "lex.en.100k.043031": {
        "hw": "pinole",
        "pos": "noun",
        "vi": "bột ngô rang xay thảo mộc",
        "ipa": "/pɪˈnoʊli/"
    },
    "lex.en.100k.043032": {
        "hw": "pleader",
        "pos": "noun",
        "vi": "luật sư biện hộ; người van xin",
        "ipa": "/ˈpliːdɚ/"
    },
    "lex.en.100k.043033": {
        "hw": "plumeria",
        "pos": "noun",
        "vi": "hoa sứ; cây hoa đại nhiệt đới",
        "ipa": "/pluːˈmɛriə/"
    },
    "lex.en.100k.043034": {
        "hw": "polymerisation",
        "pos": "noun",
        "vi": "quá trình trùng hợp polyme",
        "ipa": "/ˌpɑːlɪmərəˈzeɪʃən/"
    },
    "lex.en.100k.043035": {
        "hw": "polyploidy",
        "pos": "noun",
        "vi": "hiện tượng đa bội thể di truyền",
        "ipa": "/ˈpɑːlɪplɔɪdi/"
    },
    "lex.en.100k.043036": {
        "hw": "precentor",
        "pos": "noun",
        "vi": "người xướng ca; người lĩnh xướng",
        "ipa": "/prɪˈsɛntɚ/"
    },
    "lex.en.100k.043037": {
        "hw": "pudendal",
        "pos": "adj",
        "vi": "thuộc vùng sinh dục ngoài",
        "ipa": "/pjuːˈdɛndəl/"
    },
    "lex.en.100k.043038": {
        "hw": "pule",
        "pos": "verb",
        "vi": "khóc thút thít yếu ớt; rên rỉ",
        "ipa": "/pjuːl/"
    },
    "lex.en.100k.043039": {
        "hw": "pyridoxal",
        "pos": "noun",
        "vi": "dạng vitamin B6 pyridoxal",
        "ipa": "/ˌpɪrɪˈdɑːksæl/"
    },
    "lex.en.100k.043040": {
        "hw": "rarebit",
        "pos": "noun",
        "vi": "món bánh mì nướng sốt phô mai",
        "ipa": "/ˈrɛərbɪt/"
    },
    "lex.en.100k.043041": {
        "hw": "ravenously",
        "pos": "adv",
        "vi": "một cách đói ngấu nghiến cồn cào",
        "ipa": "/ˈrævənəsli/"
    },
    "lex.en.100k.043042": {
        "hw": "reciter",
        "pos": "noun",
        "vi": "người ngâm thơ; người tụng đọc",
        "ipa": "/rɪˈsaɪtɚ/"
    },
    "lex.en.100k.043043": {
        "hw": "recondite",
        "pos": "adj",
        "vi": "uyên thâm khó hiểu; bí hiểm",
        "ipa": "/ˈrɛkəndaɪt/"
    },
    "lex.en.100k.043044": {
        "hw": "recurrently",
        "pos": "adv",
        "vi": "một cách tái diễn định kỳ",
        "ipa": "/rɪˈkɝːəntli/"
    },
    "lex.en.100k.043045": {
        "hw": "requite",
        "pos": "verb",
        "vi": "đền đáp công ơn; trả thù",
        "ipa": "/rɪˈkwaɪt/"
    },
    "lex.en.100k.043046": {
        "hw": "rickettsia",
        "pos": "noun",
        "vi": "vi khuẩn ký sinh Rickettsia",
        "ipa": "/rɪˈkɛtsiə/"
    },
    "lex.en.100k.043047": {
        "hw": "rugose",
        "pos": "adj",
        "vi": "nhăn nheo; có nếp gồ ghề ráp",
        "ipa": "/ˈruːɡoʊs/"
    },
    "lex.en.100k.043048": {
        "hw": "saluki",
        "pos": "noun",
        "vi": "giống chó săn nhanh nhẹn Saluki",
        "ipa": "/səˈluːki/"
    },
    "lex.en.100k.043049": {
        "hw": "sard",
        "pos": "noun",
        "vi": "ngọc mã não đỏ sẫm sard",
        "ipa": "/sɑːrd/"
    },
    "lex.en.100k.043050": {
        "hw": "sartor",
        "pos": "noun",
        "vi": "thợ may complet nam",
        "ipa": "/ˈsɑːrtɚ/"
    },
    "lex.en.100k.043051": {
        "hw": "satchmo",
        "pos": "noun",
        "vi": "biệt danh của Louis Armstrong",
        "ipa": "/ˈsætʃmoʊ/"
    },
    "lex.en.100k.043052": {
        "hw": "scriptorium",
        "pos": "noun",
        "vi": "phòng chép kinh thư tu viện xưa",
        "ipa": "/skrɪpˈtɔːriəm/"
    },
    "lex.en.100k.043053": {
        "hw": "seaborg",
        "pos": "noun",
        "vi": "nhà hóa học Glenn T. Seaborg",
        "ipa": "/ˈsiːbɔːrɡ/"
    },
    "lex.en.100k.043054": {
        "hw": "seigniorage",
        "pos": "noun",
        "vi": "thuế đúc tiền chênh lệch",
        "ipa": "/ˈseɪnjərɪdʒ/"
    },
    "lex.en.100k.043055": {
        "hw": "shivery",
        "pos": "adj",
        "vi": "run rẩy vì lạnh buốt sợ hãi",
        "ipa": "/ˈʃɪvəri/"
    },
    "lex.en.100k.043056": {
        "hw": "shorebird",
        "pos": "noun",
        "vi": "loài chim lội ven bờ biển bãi triều",
        "ipa": "/ˈʃɔːrbɝːd/"
    },
    "lex.en.100k.043057": {
        "hw": "skedaddle",
        "pos": "noun",
        "vi": "cuộc tháo chạy vội vã; sự tẩu thoát",
        "ipa": "/skɪˈdædəl/"
    },
    "lex.en.100k.043058": {
        "hw": "slighting",
        "pos": "adj",
        "vi": "khinh thường; miệt thị coi nhẹ",
        "ipa": "/ˈslaɪtɪŋ/"
    },
    "lex.en.100k.043059": {
        "hw": "smoothbore",
        "pos": "adj",
        "vi": "có nòng trơn không khương tuyến",
        "ipa": "/ˈsmuːðbɔːr/"
    },
    "lex.en.100k.043060": {
        "hw": "smoulder",
        "pos": "noun",
        "vi": "ngọn khói cháy âm ỉ không bốc lửa",
        "ipa": "/ˈsmoʊldɚ/"
    },
    "lex.en.100k.043061": {
        "hw": "souse",
        "pos": "noun",
        "vi": "kẻ bợm rượu; món thịt ngâm chua",
        "ipa": "/saʊs/"
    },
    "lex.en.100k.043062": {
        "hw": "soused",
        "pos": "adj",
        "vi": "say khướt mềm nhũn; được ngâm chua",
        "ipa": "/saʊst/"
    },
    "lex.en.100k.043063": {
        "hw": "sousse",
        "pos": "noun",
        "vi": "thành phố cảng Sousse của Tunisia",
        "ipa": "/suːs/"
    },
    "lex.en.100k.043064": {
        "hw": "spectrogram",
        "pos": "noun",
        "vi": "quang phổ đồ; ảnh biểu đồ phổ âm",
        "ipa": "/ˈspɛktrəɡræm/"
    },
    "lex.en.100k.043065": {
        "hw": "spoilsport",
        "pos": "noun",
        "vi": "kẻ phá bĩnh làm mất vui cuộc vui",
        "ipa": "/ˈspɔɪlspɔːrt/"
    },
    "lex.en.100k.043066": {
        "hw": "stob",
        "pos": "noun",
        "vi": "cọc gỗ nhỏ; gốc cây bị phạt cụt",
        "ipa": "/stɑːb/"
    },
    "lex.en.100k.043067": {
        "hw": "summerset",
        "pos": "noun",
        "vi": "cú nhào lộn xoay người tùng bê",
        "ipa": "/ˈsʌmɚsɛt/"
    },
    "lex.en.100k.043068": {
        "hw": "tallboy",
        "pos": "noun",
        "vi": "tủ ngăn kéo chân cao cổ điển",
        "ipa": "/ˈtɔːlbɔɪ/"
    },
    "lex.en.100k.043069": {
        "hw": "tereshkova",
        "pos": "noun",
        "vi": "phi hành gia Valentina Tereshkova",
        "ipa": "/ˌtɛrɪʃˈkoʊvə/"
    },
    "lex.en.100k.043070": {
        "hw": "thiocyanate",
        "pos": "noun",
        "vi": "hợp chất muối gốc thiocyanat",
        "ipa": "/ˌθaɪoʊˈsaɪəneɪt/"
    },
    "lex.en.100k.043071": {
        "hw": "tiredly",
        "pos": "adv",
        "vi": "một cách mệt mỏi rã rời kiệt sức",
        "ipa": "/ˈtaɪɚdli/"
    },
    "lex.en.100k.043072": {
        "hw": "torpid",
        "pos": "adj",
        "vi": "đờ đẫn; uể oải thiếu sinh khí",
        "ipa": "/ˈtɔːrpɪd/"
    },
    "lex.en.100k.043073": {
        "hw": "tricot",
        "pos": "noun",
        "vi": "loại vải dệt kim tricot co giãn",
        "ipa": "/ˈtriːkoʊ/"
    },
    "lex.en.100k.043074": {
        "hw": "trollop",
        "pos": "noun",
        "vi": "người phụ nữ nhếch nhác buông tuồng",
        "ipa": "/ˈtrɑːləp/"
    },
    "lex.en.100k.043075": {
        "hw": "undulation",
        "pos": "noun",
        "vi": "chuyển động uốn lượn hình sóng",
        "ipa": "/ˌʌndjəˈleɪʃən/"
    },
    "lex.en.100k.043076": {
        "hw": "unplaced",
        "pos": "adj",
        "vi": "không giành được thứ hạng có giải",
        "ipa": "/ʌnˈpleɪst/"
    },
    "lex.en.100k.043077": {
        "hw": "unpredicted",
        "pos": "adj",
        "vi": "không được báo trước; bất ngờ",
        "ipa": "/ˌʌnprɪˈdɪktɪd/"
    },
    "lex.en.100k.043078": {
        "hw": "vituperative",
        "pos": "adj",
        "vi": "chửi bới cay nghiệt; mắng nhiếc tồi",
        "ipa": "/vaɪˈtuːpərətɪv/"
    },
    "lex.en.100k.043079": {
        "hw": "vouchsafe",
        "pos": "verb",
        "vi": "hạ cố ban cho; chiếu cố ban ân",
        "ipa": "/vaʊtʃˈseɪf/"
    },
    "lex.en.100k.043080": {
        "hw": "weka",
        "pos": "noun",
        "vi": "chim không bay weka New Zealand",
        "ipa": "/ˈwɛkə/"
    },
    "lex.en.100k.043081": {
        "hw": "wigeon",
        "pos": "noun",
        "vi": "vịt trời đầu hung hoang dã wigeon",
        "ipa": "/ˈwɪdʒən/"
    },
    "lex.en.100k.043082": {
        "hw": "willebrand",
        "pos": "noun",
        "vi": "bác sĩ lập hội chứng Von Willebrand",
        "ipa": "/ˈvɪləbrɑːnt/"
    },
    "lex.en.100k.043083": {
        "hw": "adz",
        "pos": "noun",
        "vi": "cái rìu đẽo gỗ lưỡi ngang vòm",
        "ipa": "/ædz/"
    },
    "lex.en.100k.043084": {
        "hw": "aeronaut",
        "pos": "noun",
        "vi": "nhà thám hiểm khí cầu phi công",
        "ipa": "/ˈɛrənɔːt/"
    },
    "lex.en.100k.043085": {
        "hw": "aggrandisement",
        "pos": "noun",
        "vi": "sự mở rộng thế lực và quyền uy",
        "ipa": "/əˈɡrændɪzmənt/"
    },
    "lex.en.100k.043086": {
        "hw": "alee",
        "pos": "adv",
        "vi": "về hướng dưới gió khuất gió thuyền",
        "ipa": "/əˈliː/"
    },
    "lex.en.100k.043087": {
        "hw": "aliment",
        "pos": "noun",
        "vi": "chất bổ dưỡng; thức ăn nuôi sống",
        "ipa": "/ˈælɪmənt/"
    },
    "lex.en.100k.043088": {
        "hw": "alimentation",
        "pos": "noun",
        "vi": "sự nuôi dưỡng; việc tiếp dinh dưỡng",
        "ipa": "/ˌælɪmɛnˈteɪʃən/"
    },
    "lex.en.100k.043089": {
        "hw": "ammeter",
        "pos": "noun",
        "vi": "ampe kế đo cường độ dòng điện",
        "ipa": "/ˈæmˌmiːtɚ/"
    },
    "lex.en.100k.043090": {
        "hw": "amphipod",
        "pos": "noun",
        "vi": "loài giáp xác hai loại chân nhỏ",
        "ipa": "/ˈæmfəpɑːd/"
    },
    "lex.en.100k.043091": {
        "hw": "ananas",
        "pos": "noun",
        "vi": "chi cây dứa quả gai thơm Ananas",
        "ipa": "/əˈnænəs/"
    },
    "lex.en.100k.043092": {
        "hw": "apeldoorn",
        "pos": "noun",
        "vi": "thành phố Apeldoorn ở Hà Lan",
        "ipa": "/ˈɑːpəldoːrn/"
    },
    "lex.en.100k.043093": {
        "hw": "arenaria",
        "pos": "noun",
        "vi": "chi thảo mộc cỏ cát hoa trắng nhỏ",
        "ipa": "/ˌærɪˈnɛəriə/"
    },
    "lex.en.100k.043094": {
        "hw": "armourer",
        "pos": "noun",
        "vi": "thợ chế tạo áo giáp và sửa binh khí",
        "ipa": "/ˈɑːrmɚrɚ/"
    },
    "lex.en.100k.043095": {
        "hw": "aurally",
        "pos": "adv",
        "vi": "qua thính giác; bằng đường tai",
        "ipa": "/ˈɔːrəli/"
    },
    "lex.en.100k.043096": {
        "hw": "bagpiper",
        "pos": "noun",
        "vi": "người biểu diễn kèn túi Scotland",
        "ipa": "/ˈbæɡˌpaɪpɚ/"
    },
    "lex.en.100k.043097": {
        "hw": "balletic",
        "pos": "adj",
        "vi": "thanh thoát uyển chuyển như ba-lê",
        "ipa": "/bæˈlɛtɪk/"
    },
    "lex.en.100k.043098": {
        "hw": "barehanded",
        "pos": "adj",
        "vi": "tay không; không dùng găng tay",
        "ipa": "/ˌbɛrˈhændɪd/"
    },
    "lex.en.100k.043099": {
        "hw": "belike",
        "pos": "adv",
        "vi": "rất có thể; chắc hẳn là thế",
        "ipa": "/bɪˈlaɪk/"
    },
    "lex.en.100k.043100": {
        "hw": "berzelius",
        "pos": "noun",
        "vi": "nhà hóa học Jöns Jacob Berzelius",
        "ipa": "/bɝːˈziːliəs/"
    },
    "lex.en.100k.043101": {
        "hw": "bifurcate",
        "pos": "adj",
        "vi": "chia thành hai nhánh; chẽ đôi",
        "ipa": "/ˈbaɪfɚˌkeɪt/"
    }
}

OVERRIDES_PART2 = {
    "lex.en.100k.043102": {
        "hw": "blameworthy",
        "pos": "adj",
        "vi": "đáng khiển trách; đáng chê trách",
        "ipa": "/ˈbleɪmˌwɝːði/"
    },
    "lex.en.100k.043103": {
        "hw": "blixen",
        "pos": "noun",
        "vi": "nhà văn nữ Đan Mạch Karen Blixen",
        "ipa": "/ˈblɪksən/"
    },
    "lex.en.100k.043104": {
        "hw": "bontemps",
        "pos": "noun",
        "vi": "nhà văn Arna Bontemps phong trào",
        "ipa": "/bɔːnˈtɑːm/"
    },
    "lex.en.100k.043105": {
        "hw": "bounder",
        "pos": "noun",
        "vi": "kẻ đểu cáng thô lỗ; tên vô lại",
        "ipa": "/ˈbaʊndɚ/"
    },
    "lex.en.100k.043106": {
        "hw": "buckboard",
        "pos": "noun",
        "vi": "xe ngựa bốn bánh ván nhún",
        "ipa": "/ˈbʌkˌbɔːrd/"
    },
    "lex.en.100k.043107": {
        "hw": "carducci",
        "pos": "noun",
        "vi": "nhà thơ Ý Giosuè Carducci",
        "ipa": "/kɑːrˈduːtʃi/"
    },
    "lex.en.100k.043108": {
        "hw": "carnality",
        "pos": "noun",
        "vi": "dục vọng xác thịt; tính sắc dục",
        "ipa": "/kɑːrˈnæləti/"
    },
    "lex.en.100k.043109": {
        "hw": "cartage",
        "pos": "noun",
        "vi": "tiền cước chở xe; sự chở hàng xe",
        "ipa": "/ˈkɑːrtɪdʒ/"
    },
    "lex.en.100k.043110": {
        "hw": "catechin",
        "pos": "noun",
        "vi": "hợp chất chống oxy hóa catechin",
        "ipa": "/ˈkætətʃɪn/"
    },
    "lex.en.100k.043111": {
        "hw": "cavort",
        "pos": "verb",
        "vi": "nhảy nhót đùa nghịch nô nức",
        "ipa": "/kəˈvɔːrt/"
    },
    "lex.en.100k.043112": {
        "hw": "chasten",
        "pos": "verb",
        "vi": "uốn nắn trừng phạt để răn dạy",
        "ipa": "/ˈtʃeɪsən/"
    },
    "lex.en.100k.043113": {
        "hw": "cisc",
        "pos": "noun",
        "vi": "kiến trúc máy tính tập lệnh phức",
        "ipa": "/sɪsk/"
    },
    "lex.en.100k.043114": {
        "hw": "classifiable",
        "pos": "adj",
        "vi": "có thể phân loại sắp xếp được",
        "ipa": "/ˈklæsɪfaɪəbəl/"
    },
    "lex.en.100k.043115": {
        "hw": "cockatrice",
        "pos": "noun",
        "vi": "quái thú gà đuôi rắn thần thoại",
        "ipa": "/ˈkɑːkətrɪs/"
    },
    "lex.en.100k.043116": {
        "hw": "collectivized",
        "pos": "adj",
        "vi": "được tập thể hóa; đưa vào tổ hợp",
        "ipa": "/kəˈlɛktɪvaɪzd/"
    },
    "lex.en.100k.043117": {
        "hw": "compartmented",
        "pos": "adj",
        "vi": "được chia thành từng ô ngăn riêng",
        "ipa": "/kəmˈpɑːrtmɛntɪd/"
    },
    "lex.en.100k.043118": {
        "hw": "conjuncture",
        "pos": "noun",
        "vi": "kết hợp tình thế; thời cơ gay cấn",
        "ipa": "/kənˈdʒʌŋktʃɚ/"
    },
    "lex.en.100k.043119": {
        "hw": "convolvulus",
        "pos": "noun",
        "vi": "chi cây hoa bìm bìm dây leo",
        "ipa": "/kənˈvɑːlvjələs/"
    },
    "lex.en.100k.043120": {
        "hw": "cowpox",
        "pos": "noun",
        "vi": "bệnh đậu bò ở gia súc",
        "ipa": "/ˈkaʊpɑːks/"
    },
    "lex.en.100k.043121": {
        "hw": "crystalized",
        "pos": "adj",
        "vi": "kết tinh thành tinh thể; kết tinh",
        "ipa": "/ˈkrɪstəlaɪzd/"
    },
    "lex.en.100k.043122": {
        "hw": "cummerbund",
        "pos": "noun",
        "vi": "dải thắt lưng lụa nếp âu phục",
        "ipa": "/ˈkʌmɚbʌnd/"
    },
    "lex.en.100k.043123": {
        "hw": "cymbidium",
        "pos": "noun",
        "vi": "chi phong lan kiếm Cymbidium",
        "ipa": "/sɪmˈbɪdiəm/"
    },
    "lex.en.100k.043124": {
        "hw": "cytological",
        "pos": "adj",
        "vi": "thuộc lĩnh vực tế bào học",
        "ipa": "/ˌsaɪtəˈlɑːdʒɪkəl/"
    },
    "lex.en.100k.043125": {
        "hw": "dayspring",
        "pos": "noun",
        "vi": "bình minh ló rạng; khởi đầu mới",
        "ipa": "/ˈdeɪsprɪŋ/"
    },
    "lex.en.100k.043126": {
        "hw": "demoiselle",
        "pos": "noun",
        "vi": "thiếu nữ trẻ duyên dáng; chim hạc",
        "ipa": "/ˌdɛmwɑːˈzɛl/"
    },
    "lex.en.100k.043127": {
        "hw": "dependance",
        "pos": "noun",
        "vi": "sự lệ thuộc phụ thuộc",
        "ipa": "/dɪˈpɛndəns/"
    },
    "lex.en.100k.043128": {
        "hw": "depopulate",
        "pos": "verb",
        "vi": "làm suy giảm dân số nghiêm trọng",
        "ipa": "/diːˈpɑːpjəleɪt/"
    },
    "lex.en.100k.043129": {
        "hw": "destine",
        "pos": "verb",
        "vi": "định đoạt số phận; dành riêng cho",
        "ipa": "/ˈdɛstɪn/"
    },
    "lex.en.100k.043130": {
        "hw": "dichloromethane",
        "pos": "noun",
        "vi": "dung môi hóa học diclometan",
        "ipa": "/daɪˌklɔːroʊˈmɛθeɪn/"
    },
    "lex.en.100k.043131": {
        "hw": "didactics",
        "pos": "noun",
        "vi": "nghệ thuật sư phạm; khoa giáo học",
        "ipa": "/daɪˈdæktɪks/"
    },
    "lex.en.100k.043132": {
        "hw": "dirndl",
        "pos": "noun",
        "vi": "váy truyền thống vùng Alps áo chẽn",
        "ipa": "/ˈdɝːndəl/"
    },
    "lex.en.100k.043133": {
        "hw": "discoidal",
        "pos": "adj",
        "vi": "có hình dạng đĩa dẹt tròn",
        "ipa": "/dɪsˈkɔɪdəl/"
    },
    "lex.en.100k.043134": {
        "hw": "disfranchised",
        "pos": "adj",
        "vi": "bị tước quyền bầu cử công dân",
        "ipa": "/dɪsˈfræntʃaɪzd/"
    },
    "lex.en.100k.043135": {
        "hw": "distractedly",
        "pos": "adv",
        "vi": "một cách lơ đãng bồn chồn",
        "ipa": "/dɪˈstræktɪdli/"
    },
    "lex.en.100k.043136": {
        "hw": "dodecanese",
        "pos": "noun",
        "vi": "quần đảo Dodecanese của Hy Lạp",
        "ipa": "/doʊˌdɛkəˈniːz/"
    },
    "lex.en.100k.043137": {
        "hw": "doohickey",
        "pos": "noun",
        "vi": "món đồ lặt vặt; cái thứ linh tinh",
        "ipa": "/ˈduːˌhɪki/"
    },
    "lex.en.100k.043138": {
        "hw": "doorjamb",
        "pos": "noun",
        "vi": "thanh đứng khung cửa; trụ cửa sổ",
        "ipa": "/ˈdɔːrdʒæm/"
    },
    "lex.en.100k.043139": {
        "hw": "dubliner",
        "pos": "noun",
        "vi": "người dân thành phố Dublin",
        "ipa": "/ˈdʌblɪnɚ/"
    },
    "lex.en.100k.043140": {
        "hw": "ductless",
        "pos": "adj",
        "vi": "không có ống dẫn; thuộc nội tiết",
        "ipa": "/ˈdʌktləs/"
    },
    "lex.en.100k.043141": {
        "hw": "educationalist",
        "pos": "noun",
        "vi": "nhà nghiên cứu giáo dục sư phạm",
        "ipa": "/ˌɛdʒəˈkeɪʃənəlɪst/"
    },
    "lex.en.100k.043142": {
        "hw": "elamite",
        "pos": "noun",
        "vi": "người hoặc chữ Elam cổ đại",
        "ipa": "/ˈiːləmaɪt/"
    },
    "lex.en.100k.043143": {
        "hw": "embroil",
        "pos": "verb",
        "vi": "lôi kéo vào vòng tranh chấp rối ren",
        "ipa": "/ɛmˈbrɔɪl/"
    },
    "lex.en.100k.043144": {
        "hw": "encasement",
        "pos": "noun",
        "vi": "vỏ bọc ngoài; sự bọc hộp bảo vệ",
        "ipa": "/ɛnˈkeɪsmənt/"
    },
    "lex.en.100k.043145": {
        "hw": "enumerable",
        "pos": "adj",
        "vi": "có thể đếm được; liệt kê được",
        "ipa": "/ɪˈnuːmərəbəl/"
    },
    "lex.en.100k.043146": {
        "hw": "epona",
        "pos": "noun",
        "vi": "nữ thần bảo hộ loài ngựa Celtic",
        "ipa": "/ɪˈpoʊnə/"
    },
    "lex.en.100k.043147": {
        "hw": "equivocate",
        "pos": "verb",
        "vi": "nói nước đôi tránh nói sự thật",
        "ipa": "/ɪˈkwɪvəkeɪt/"
    },
    "lex.en.100k.043148": {
        "hw": "etd",
        "pos": "noun",
        "vi": "giờ khởi hành dự kiến phương tiện",
        "ipa": "/ˌiː.tiːˈdiː/"
    },
    "lex.en.100k.043149": {
        "hw": "evolutionism",
        "pos": "noun",
        "vi": "thuyết tiến hóa khoa học",
        "ipa": "/ˌɛvəˈluːʃənɪzəm/"
    },
    "lex.en.100k.043150": {
        "hw": "experimentalism",
        "pos": "noun",
        "vi": "chủ nghĩa thực nghiệm thực chứng",
        "ipa": "/ɪkˌspɛrɪˈmɛntəlɪzəm/"
    },
    "lex.en.100k.043151": {
        "hw": "fatiha",
        "pos": "noun",
        "vi": "kinh mở đầu Fatiha trong Kinh Quran",
        "ipa": "/ˈfɑːtiːhə/"
    },
    "lex.en.100k.043152": {
        "hw": "felicitate",
        "pos": "verb",
        "vi": "chúc mừng ân cần trịnh trọng",
        "ipa": "/fɪˈlɪsɪteɪt/"
    },
    "lex.en.100k.043153": {
        "hw": "firebrick",
        "pos": "noun",
        "vi": "viên gạch chịu nhiệt độ cao lò nung",
        "ipa": "/ˈfaɪərbrɪk/"
    },
    "lex.en.100k.043154": {
        "hw": "flowage",
        "pos": "noun",
        "vi": "dòng bùn nham thạch chảy tràn",
        "ipa": "/ˈfloʊɪdʒ/"
    },
    "lex.en.100k.043155": {
        "hw": "foldout",
        "pos": "noun",
        "vi": "trang gấp lớn mở rộng trong ấn phẩm",
        "ipa": "/ˈfoʊldaʊt/"
    },
    "lex.en.100k.043156": {
        "hw": "freyr",
        "pos": "noun",
        "vi": "thần mùa màng thịnh vượng Bắc Âu",
        "ipa": "/freɪr/"
    },
    "lex.en.100k.043157": {
        "hw": "frigga",
        "pos": "noun",
        "vi": "nữ thần Frigga vợ thần Odin",
        "ipa": "/ˈfrɪɡə/"
    },
    "lex.en.100k.043158": {
        "hw": "frump",
        "pos": "noun",
        "vi": "phụ nữ ăn mặc lôi thôi thiếu duyên",
        "ipa": "/frʌmp/"
    },
    "lex.en.100k.043159": {
        "hw": "gastropoda",
        "pos": "noun",
        "vi": "lớp Động vật chân bụng sên ốc",
        "ipa": "/ɡæsˈtrɑːpədə/"
    },
    "lex.en.100k.043160": {
        "hw": "geminate",
        "pos": "noun",
        "vi": "phụ âm đôi; phụ âm kéo dài âm thanh",
        "ipa": "/ˈdʒɛmənɪt/"
    },
    "lex.en.100k.043161": {
        "hw": "gesner",
        "pos": "noun",
        "vi": "nhà tự nhiên học Thụy Sĩ Gesner",
        "ipa": "/ˈɡɛsnɚ/"
    },
    "lex.en.100k.043162": {
        "hw": "glinka",
        "pos": "noun",
        "vi": "nhà soạn nhạc Mikhail Glinka",
        "ipa": "/ˈɡlɪŋkə/"
    },
    "lex.en.100k.043163": {
        "hw": "gracile",
        "pos": "adj",
        "vi": "thanh mảnh tao nhã mảnh dẻ",
        "ipa": "/ˈɡræsəl/"
    },
    "lex.en.100k.043164": {
        "hw": "grackle",
        "pos": "noun",
        "vi": "chim sáo đen đuôi thuyền Bắc Mỹ",
        "ipa": "/ˈɡrækəl/"
    },
    "lex.en.100k.043165": {
        "hw": "grindle",
        "pos": "noun",
        "vi": "cá vây cung nước ngọt Bắc Mỹ",
        "ipa": "/ˈɡrɪndəl/"
    },
    "lex.en.100k.043166": {
        "hw": "gruffly",
        "pos": "adv",
        "vi": "một cách gắt gỏng thô cộc khó chịu",
        "ipa": "/ˈɡrʌfli/"
    },
    "lex.en.100k.043167": {
        "hw": "hailstone",
        "pos": "noun",
        "vi": "cục mưa đá băng tuyết",
        "ipa": "/ˈheɪlstoʊn/"
    },
    "lex.en.100k.043168": {
        "hw": "hasidism",
        "pos": "noun",
        "vi": "phong trào Do Thái giáo Hasid",
        "ipa": "/ˈhæsɪdɪzəm/"
    },
    "lex.en.100k.043169": {
        "hw": "haversack",
        "pos": "noun",
        "vi": "ba lô dã ngoại đeo vai tiện lợi",
        "ipa": "/ˈhævɚsæk/"
    },
    "lex.en.100k.043170": {
        "hw": "hayseed",
        "pos": "noun",
        "vi": "hạt cỏ khô; kẻ quê mùa chất phác",
        "ipa": "/ˈheɪsiːd/"
    },
    "lex.en.100k.043171": {
        "hw": "heartlessly",
        "pos": "adv",
        "vi": "một cách nhẫn tâm vô tình máu lạnh",
        "ipa": "/ˈhɑːrtlɪsli/"
    },
    "lex.en.100k.043172": {
        "hw": "heartlessness",
        "pos": "noun",
        "vi": "sự nhẫn tâm lạnh lùng vô cảm",
        "ipa": "/ˈhɑːrtlɪsnəs/"
    },
    "lex.en.100k.043173": {
        "hw": "hryvnia",
        "pos": "noun",
        "vi": "đơn vị tiền tệ hryvnia Ukraina",
        "ipa": "/ˈhrɪvniə/"
    },
    "lex.en.100k.043174": {
        "hw": "hydroxyzine",
        "pos": "noun",
        "vi": "thuốc chống dị ứng an thần",
        "ipa": "/haɪˈdrɑːksɪziːn/"
    },
    "lex.en.100k.043175": {
        "hw": "hyperextension",
        "pos": "noun",
        "vi": "sự duỗi khớp cơ quá mức",
        "ipa": "/ˌhaɪpɚrɪkˈstɛnʃən/"
    },
    "lex.en.100k.043176": {
        "hw": "immiscible",
        "pos": "adj",
        "vi": "không hòa tan trộn lẫn vào nhau",
        "ipa": "/ɪˈmɪsəbəl/"
    },
    "lex.en.100k.043177": {
        "hw": "ineffectually",
        "pos": "adv",
        "vi": "một cách không hiệu quả bất lực",
        "ipa": "/ˌɪnɪˈfɛktʃuəli/"
    },
    "lex.en.100k.043178": {
        "hw": "intercalary",
        "pos": "adj",
        "vi": "nhuận xen kẽ; chèn vào giữa chu kỳ",
        "ipa": "/ɪnˈtɝːkəlɛri/"
    },
    "lex.en.100k.043179": {
        "hw": "interpose",
        "pos": "verb",
        "vi": "xen vào giữa; can thiệp nói chen",
        "ipa": "/ˌɪntɚˈpoʊz/"
    },
    "lex.en.100k.043180": {
        "hw": "jaywalk",
        "pos": "verb",
        "vi": "đi bộ băng qua đường ẩu trái phép",
        "ipa": "/ˈdʒeɪwɔːk/"
    },
    "lex.en.100k.043181": {
        "hw": "jennet",
        "pos": "noun",
        "vi": "con lừa cái; ngựa nhỏ Tây Ban Nha",
        "ipa": "/ˈdʒɛnɪt/"
    },
    "lex.en.100k.043182": {
        "hw": "kapok",
        "pos": "noun",
        "vi": "sợi bông gòn tự nhiên xơ mềm",
        "ipa": "/ˈkeɪpɑːk/"
    },
    "lex.en.100k.043183": {
        "hw": "kolam",
        "pos": "noun",
        "vi": "họa tiết rắc bột gạo may mắn Ấn Độ",
        "ipa": "/ˈkoʊlɑːm/"
    },
    "lex.en.100k.043184": {
        "hw": "kreisler",
        "pos": "noun",
        "vi": "nghệ sĩ vĩ cầm Fritz Kreisler",
        "ipa": "/ˈkraɪslɚ/"
    },
    "lex.en.100k.043185": {
        "hw": "kuznets",
        "pos": "noun",
        "vi": "nhà kinh tế học Simon Kuznets",
        "ipa": "/ˈkʌznɛts/"
    },
    "lex.en.100k.043186": {
        "hw": "lachrymose",
        "pos": "adj",
        "vi": "dễ rơi lệ sướt mướt; buồn thương",
        "ipa": "/ˈlækrɪmoʊs/"
    },
    "lex.en.100k.043187": {
        "hw": "largeness",
        "pos": "noun",
        "vi": "kích thước to lớn; lòng độ lượng",
        "ipa": "/ˈlɑːrdʒnəs/"
    },
    "lex.en.100k.043188": {
        "hw": "laryngoscope",
        "pos": "noun",
        "vi": "ống soi thanh quản trong y khoa",
        "ipa": "/ləˈrɪŋɡəskoʊp/"
    },
    "lex.en.100k.043189": {
        "hw": "levator",
        "pos": "noun",
        "vi": "cơ nâng nâng đỡ cơ quan cơ thể",
        "ipa": "/lɪˈveɪtɚ/"
    },
    "lex.en.100k.043190": {
        "hw": "libidinal",
        "pos": "adj",
        "vi": "thuộc bản năng dục vọng libido",
        "ipa": "/lɪˈbɪdɪnəl/"
    },
    "lex.en.100k.043191": {
        "hw": "limonite",
        "pos": "noun",
        "vi": "quặng sắt nâu limonit quặng mỏ",
        "ipa": "/ˈlaɪmənaɪt/"
    },
    "lex.en.100k.043192": {
        "hw": "linocut",
        "pos": "noun",
        "vi": "tranh khắc trên tấm vải sơn lót sàn",
        "ipa": "/ˈlaɪnoʊkʌt/"
    },
    "lex.en.100k.043193": {
        "hw": "lombardia",
        "pos": "noun",
        "vi": "vùng Lombardia trù phú miền bắc Ý",
        "ipa": "/lɑːmˈbɑːrdiə/"
    },
    "lex.en.100k.043194": {
        "hw": "madrasah",
        "pos": "noun",
        "vi": "trường giáo dục Hồi giáo madrasah",
        "ipa": "/məˈdrɑːsə/"
    },
    "lex.en.100k.043195": {
        "hw": "matcher",
        "pos": "noun",
        "vi": "người mai mối ghép đôi; bộ so khớp",
        "ipa": "/ˈmætʃɚ/"
    },
    "lex.en.100k.043196": {
        "hw": "meanly",
        "pos": "adv",
        "vi": "một cách bủn xỉn hèn mạt đê tiện",
        "ipa": "/ˈmiːnli/"
    },
    "lex.en.100k.043197": {
        "hw": "mechanistically",
        "pos": "adv",
        "vi": "theo quy luật máy móc cơ giới",
        "ipa": "/ˌmɛkəˈnɪstɪkli/"
    },
    "lex.en.100k.043198": {
        "hw": "menhaden",
        "pos": "noun",
        "vi": "loài cá mòi menhaden Đại Tây Dương",
        "ipa": "/mɛnˈheɪdən/"
    },
    "lex.en.100k.043199": {
        "hw": "mercuric",
        "pos": "adj",
        "vi": "chứa thủy ngân hóa trị hai",
        "ipa": "/mɚˈkjʊrɪk/"
    },
    "lex.en.100k.043200": {
        "hw": "mesenchyme",
        "pos": "noun",
        "vi": "mô liên kết trung mô phôi thai",
        "ipa": "/ˈmɛsəŋkaɪm/"
    },
    "lex.en.100k.043201": {
        "hw": "metonymy",
        "pos": "noun",
        "vi": "biện pháp tu từ hoán dụ",
        "ipa": "/məˈtɑːnəmi/"
    }
}

OVERRIDES_PART3 = {
    "lex.en.100k.043202": {
        "hw": "mucinous",
        "pos": "adj",
        "vi": "chứa chất nhầy; tiết chất nhầy",
        "ipa": "/ˈmjuːsɪnəs/"
    },
    "lex.en.100k.043203": {
        "hw": "mujahedeen",
        "pos": "noun",
        "vi": "chiến binh du kích Hồi giáo",
        "ipa": "/mʊˌdʒɑːhɪˈdiːn/"
    },
    "lex.en.100k.043204": {
        "hw": "multivalent",
        "pos": "adj",
        "vi": "đa hóa trị; nhiều giá trị liên kết",
        "ipa": "/ˌmʌltiˈveɪlənt/"
    },
    "lex.en.100k.043205": {
        "hw": "natriuretic",
        "pos": "adj",
        "vi": "kích thích bài tiết natri thận",
        "ipa": "/ˌneɪtrijəˈrɛtɪk/"
    },
    "lex.en.100k.043206": {
        "hw": "navaho",
        "pos": "noun",
        "vi": "người da đỏ bản địa Navajo",
        "ipa": "/ˈnævəhoʊ/"
    },
    "lex.en.100k.043207": {
        "hw": "naysayer",
        "pos": "noun",
        "vi": "người hay phản đối và bi quan",
        "ipa": "/ˈneɪseɪɚ/"
    },
    "lex.en.100k.043208": {
        "hw": "nbe",
        "pos": "noun",
        "vi": "hướng bắc lệch đông góc phụ",
        "ipa": "/ˌɛn.biːˈiː/"
    },
    "lex.en.100k.043209": {
        "hw": "neocolonialism",
        "pos": "noun",
        "vi": "chủ nghĩa thực dân mới áp đặt",
        "ipa": "/ˌniːoʊkəˈloʊniəlɪzəm/"
    },
    "lex.en.100k.043210": {
        "hw": "nernst",
        "pos": "noun",
        "vi": "nhà vật lý hóa Walther Nernst",
        "ipa": "/nɛrnst/"
    },
    "lex.en.100k.043211": {
        "hw": "nifedipine",
        "pos": "noun",
        "vi": "thuốc hạ huyết áp nifedipine",
        "ipa": "/naɪˈfɛdɪpiːn/"
    },
    "lex.en.100k.043212": {
        "hw": "nonprofessional",
        "pos": "adj",
        "vi": "phi chuyên nghiệp; nghiệp dư",
        "ipa": "/ˌnɑːnprəˈfɛʃənəl/"
    },
    "lex.en.100k.043213": {
        "hw": "oblanceolate",
        "pos": "adj",
        "vi": "có hình ngọn giáo ngược lá cây",
        "ipa": "/ɑːbˈlænsiəleɪt/"
    },
    "lex.en.100k.043214": {
        "hw": "occam",
        "pos": "noun",
        "vi": "triết gia William xứ Ockham",
        "ipa": "/ˈɑːkəm/"
    },
    "lex.en.100k.043215": {
        "hw": "outsole",
        "pos": "noun",
        "vi": "phần đế ngoài cùng của giày dép",
        "ipa": "/ˈaʊtsoʊl/"
    },
    "lex.en.100k.043216": {
        "hw": "overexploitation",
        "pos": "noun",
        "vi": "sự khai thác tài nguyên quá mức",
        "ipa": "/ˌoʊvɚˌɛksplɔɪˈteɪʃən/"
    },
    "lex.en.100k.043217": {
        "hw": "palpate",
        "pos": "verb",
        "vi": "sờ nắn chẩn đoán bằng tay trong y",
        "ipa": "/ˈpælpeɪt/"
    },
    "lex.en.100k.043218": {
        "hw": "paranasal",
        "pos": "adj",
        "vi": "nằm cạnh các xoang khoang mũi",
        "ipa": "/ˌpærəˈneɪzəl/"
    },
    "lex.en.100k.043219": {
        "hw": "passerine",
        "pos": "adj",
        "vi": "thuộc bộ chim Sẻ hót líu lo",
        "ipa": "/ˈpæsəraɪn/"
    },
    "lex.en.100k.043220": {
        "hw": "peafowl",
        "pos": "noun",
        "vi": "loài chim công đuôi xòe trĩ",
        "ipa": "/ˈpiːfaʊl/"
    },
    "lex.en.100k.043221": {
        "hw": "pectus",
        "pos": "noun",
        "vi": "lồng ngực; xương ức cơ thể",
        "ipa": "/ˈpɛktəs/"
    },
    "lex.en.100k.043222": {
        "hw": "phimosis",
        "pos": "noun",
        "vi": "chứng hẹp bao quy đầu sinh dục",
        "ipa": "/faɪˈmoʊsɪs/"
    },
    "lex.en.100k.043223": {
        "hw": "pigmy",
        "pos": "noun",
        "vi": "người lùn chủng Pygmy châu Phi",
        "ipa": "/ˈpɪɡmi/"
    },
    "lex.en.100k.043224": {
        "hw": "plaint",
        "pos": "noun",
        "vi": "lời than van than thở; đơn kiện",
        "ipa": "/pleɪnt/"
    },
    "lex.en.100k.043225": {
        "hw": "precociously",
        "pos": "adv",
        "vi": "sớm phát triển trước lứa tuổi",
        "ipa": "/prɪˈkoʊʃəsli/"
    },
    "lex.en.100k.043226": {
        "hw": "prepuce",
        "pos": "noun",
        "vi": "bao quy đầu cơ quan sinh dục",
        "ipa": "/ˈpriːpjuːs/"
    },
    "lex.en.100k.043227": {
        "hw": "proctologist",
        "pos": "noun",
        "vi": "bác sĩ chuyên khoa hậu môn",
        "ipa": "/prɑːkˈtɑːlədʒɪst/"
    },
    "lex.en.100k.043228": {
        "hw": "propanol",
        "pos": "noun",
        "vi": "rượu cồn công nghiệp propanol",
        "ipa": "/ˈproʊpənɔːl/"
    },
    "lex.en.100k.043229": {
        "hw": "propellor",
        "pos": "noun",
        "vi": "chân vịt tàu thủy; cánh quạt đẩy",
        "ipa": "/prəˈpɛlɚ/"
    },
    "lex.en.100k.043230": {
        "hw": "prophase",
        "pos": "noun",
        "vi": "kỳ đầu trong phân bào tế bào",
        "ipa": "/ˈproʊfeɪz/"
    },
    "lex.en.100k.043231": {
        "hw": "prosaically",
        "pos": "adv",
        "vi": "một cách tẻ nhạt nôm na bình dị",
        "ipa": "/proʊˈzeɪɪkli/"
    },
    "lex.en.100k.043232": {
        "hw": "providentially",
        "pos": "adv",
        "vi": "may mắn do trời run rủi",
        "ipa": "/ˌprɑːvəˈdɛnʃəli/"
    },
    "lex.en.100k.043233": {
        "hw": "psychokinesis",
        "pos": "noun",
        "vi": "khả năng dịch vật bằng ý nghĩ",
        "ipa": "/ˌsaɪkoʊkɪˈniːsɪs/"
    },
    "lex.en.100k.043234": {
        "hw": "radiogram",
        "pos": "noun",
        "vi": "bức điện tín vô tuyến truyền thanh",
        "ipa": "/ˈreɪdioʊɡræm/"
    },
    "lex.en.100k.043235": {
        "hw": "recuperative",
        "pos": "adj",
        "vi": "có tác dụng bồi bổ hồi phục sức",
        "ipa": "/rɪˈkuːpərətɪv/"
    },
    "lex.en.100k.043236": {
        "hw": "retrogressive",
        "pos": "adj",
        "vi": "thụt lùi thoái hóa đi xuống",
        "ipa": "/ˌrɛtrəˈɡrɛsɪv/"
    },
    "lex.en.100k.043237": {
        "hw": "roble",
        "pos": "noun",
        "vi": "cây sồi sồi nhiệt đới gỗ cứng",
        "ipa": "/ˈroʊbleɪ/"
    },
    "lex.en.100k.043238": {
        "hw": "roulade",
        "pos": "noun",
        "vi": "món thịt cuộn; bánh cuộn kem",
        "ipa": "/ruːˈlɑːd/"
    },
    "lex.en.100k.043239": {
        "hw": "rubia",
        "pos": "noun",
        "vi": "chi cây thiến thảo nhuộm đỏ Rubia",
        "ipa": "/ˈruːbiə/"
    },
    "lex.en.100k.043240": {
        "hw": "sacajawea",
        "pos": "noun",
        "vi": "nữ hướng đạo người Shoshone da đỏ",
        "ipa": "/ˌsækədʒəˈwiːə/"
    },
    "lex.en.100k.043241": {
        "hw": "sacerdotal",
        "pos": "adj",
        "vi": "thuộc chức tư tế linh mục",
        "ipa": "/ˌsæsɚˈdoʊtəl/"
    },
    "lex.en.100k.043242": {
        "hw": "salvadorean",
        "pos": "adj",
        "vi": "thuộc về đất nước El Salvador",
        "ipa": "/ˌsælvəˈdɔːriən/"
    },
    "lex.en.100k.043243": {
        "hw": "salver",
        "pos": "noun",
        "vi": "khay bưng chén đĩa bằng bạc",
        "ipa": "/ˈsælvɚ/"
    },
    "lex.en.100k.043244": {
        "hw": "sanctimony",
        "pos": "noun",
        "vi": "thái độ đạo đức giả sùng đạo",
        "ipa": "/ˈsæŋktəmoʊni/"
    },
    "lex.en.100k.043245": {
        "hw": "sanguinary",
        "pos": "adj",
        "vi": "đẫm máu hiếu sát; chém giết ác",
        "ipa": "/ˈsæŋɡwɪnɛri/"
    },
    "lex.en.100k.043246": {
        "hw": "schoolmistress",
        "pos": "noun",
        "vi": "nữ giáo viên hiệu trưởng bà giáo",
        "ipa": "/ˈskuːlˌmɪstrɪs/"
    },
    "lex.en.100k.043247": {
        "hw": "schoolwide",
        "pos": "adj",
        "vi": "áp dụng trên quy mô toàn trường",
        "ipa": "/ˈskuːlwaɪd/"
    },
    "lex.en.100k.043248": {
        "hw": "seasonable",
        "pos": "adj",
        "vi": "hợp mùa; đúng thời điểm thích hợp",
        "ipa": "/ˈsiːzənəbəl/"
    },
    "lex.en.100k.043249": {
        "hw": "semitrailer",
        "pos": "noun",
        "vi": "xe sơ-mi rơ-moóc kéo chở hàng",
        "ipa": "/ˈsɛmiˌtreɪlɚ/"
    },
    "lex.en.100k.043250": {
        "hw": "separability",
        "pos": "noun",
        "vi": "khả năng tách rời phân chia được",
        "ipa": "/ˌsɛpərəˈbɪləti/"
    },
    "lex.en.100k.043251": {
        "hw": "setswana",
        "pos": "noun",
        "vi": "tiếng Tswana ngôn ngữ Nam Phi",
        "ipa": "/sɛtˈswɑːnə/"
    },
    "lex.en.100k.043252": {
        "hw": "sextuple",
        "pos": "adj",
        "vi": "gấp sáu lần; gồm sáu phần bộ",
        "ipa": "/sɛksˈtuːpəl/"
    },
    "lex.en.100k.043253": {
        "hw": "siss",
        "pos": "verb",
        "vi": "phát ra tiếng xì xì rít dài",
        "ipa": "/sɪs/"
    },
    "lex.en.100k.043254": {
        "hw": "slipperiness",
        "pos": "noun",
        "vi": "độ trơn trượt; tính trơn láng",
        "ipa": "/ˈslɪpərinəs/"
    },
    "lex.en.100k.043255": {
        "hw": "slopped",
        "pos": "adj",
        "vi": "bị đổ tràn vung vãi; say khướt",
        "ipa": "/slɑːpt/"
    },
    "lex.en.100k.043256": {
        "hw": "snaky",
        "pos": "adj",
        "vi": "ngoằn ngoèo uốn lượn như rắn",
        "ipa": "/ˈsneɪki/"
    },
    "lex.en.100k.043257": {
        "hw": "solidago",
        "pos": "noun",
        "vi": "chi cúc hoàng anh hoa vàng rực",
        "ipa": "/ˌsɑːlɪˈdeɪɡoʊ/"
    },
    "lex.en.100k.043258": {
        "hw": "somnolent",
        "pos": "adj",
        "vi": "gây buồn ngủ; ngái ngủ đờ đẫn",
        "ipa": "/ˈsɑːmnələnt/"
    },
    "lex.en.100k.043259": {
        "hw": "soulfully",
        "pos": "adv",
        "vi": "một cách truyền cảm chan chứa tình",
        "ipa": "/ˈsoʊlfəli/"
    },
    "lex.en.100k.043260": {
        "hw": "spangle",
        "pos": "noun",
        "vi": "hạt cườm kim sa đính lấp lánh",
        "ipa": "/ˈspæŋɡəl/"
    },
    "lex.en.100k.043261": {
        "hw": "spiritism",
        "pos": "noun",
        "vi": "thuyết duy linh; hiện tượng gọi hồn",
        "ipa": "/ˈspɪrɪtɪzəm/"
    },
    "lex.en.100k.043262": {
        "hw": "squeamishness",
        "pos": "noun",
        "vi": "cảm giác dễ ghê tởm buồn nôn",
        "ipa": "/ˈskwiːmɪʃnəs/"
    },
    "lex.en.100k.043263": {
        "hw": "subconsciousness",
        "pos": "noun",
        "vi": "trạng thái tiềm thức tâm thần",
        "ipa": "/ˌsʌbˈkɑːnʃəsnəs/"
    },
    "lex.en.100k.043264": {
        "hw": "subvention",
        "pos": "noun",
        "vi": "khoản trợ cấp công quỹ tài trợ",
        "ipa": "/səbˈvɛnʃən/"
    },
    "lex.en.100k.043265": {
        "hw": "supraorbital",
        "pos": "adj",
        "vi": "nằm ngay phía trên ổ mắt",
        "ipa": "/ˌsuːprəˈɔːrbɪtəl/"
    },
    "lex.en.100k.043266": {
        "hw": "svedberg",
        "pos": "noun",
        "vi": "nhà hóa học Theodor Svedberg",
        "ipa": "/ˈsvɛdbɝːɡ/"
    },
    "lex.en.100k.043267": {
        "hw": "taenia",
        "pos": "noun",
        "vi": "loài sán xơ mít ký sinh đường ruột",
        "ipa": "/ˈtiːniə/"
    },
    "lex.en.100k.043268": {
        "hw": "taleban",
        "pos": "noun",
        "vi": "lực lượng Hồi giáo Taliban",
        "ipa": "/ˈtælɪbæn/"
    },
    "lex.en.100k.043269": {
        "hw": "terrasse",
        "pos": "verb",
        "vi": "xây bậc thềm; đắp đất giật cấp",
        "ipa": "/tɛˈrɑːs/"
    },
    "lex.en.100k.043270": {
        "hw": "thundercloud",
        "pos": "noun",
        "vi": "đám mây dông tích sấm sét đen ngòm",
        "ipa": "/ˈθʌndɚklaʊd/"
    },
    "lex.en.100k.043271": {
        "hw": "tinbergen",
        "pos": "noun",
        "vi": "nhà sinh vật học Nikolaas Tinbergen",
        "ipa": "/ˈtɪnbɝːɡən/"
    },
    "lex.en.100k.043272": {
        "hw": "transvestism",
        "pos": "noun",
        "vi": "thói quen mặc đồ khác giới tính",
        "ipa": "/trænzˈvɛstɪzəm/"
    },
    "lex.en.100k.043273": {
        "hw": "triploid",
        "pos": "adj",
        "vi": "có ba bộ nhiễm sắc thể tam bội",
        "ipa": "/ˈtrɪplɔɪd/"
    },
    "lex.en.100k.043274": {
        "hw": "tuberosity",
        "pos": "noun",
        "vi": "lồi củ xương; mấu gồ xương gân",
        "ipa": "/ˌtuːbəˈrɑːsəti/"
    },
    "lex.en.100k.043275": {
        "hw": "tupi",
        "pos": "noun",
        "vi": "thổ dân bản địa Tupi ở Brazil",
        "ipa": "/tuːˈpiː/"
    },
    "lex.en.100k.043276": {
        "hw": "turbaned",
        "pos": "adj",
        "vi": "quấn khăn đội đầu kiểu turban",
        "ipa": "/ˈtɝːbənd/"
    },
    "lex.en.100k.043277": {
        "hw": "typographer",
        "pos": "noun",
        "vi": "chuyên gia thiết kế sắp chữ in",
        "ipa": "/taɪˈpɑːɡrəfɚ/"
    },
    "lex.en.100k.043278": {
        "hw": "umbel",
        "pos": "noun",
        "vi": "cụm hoa xòe hình tán như chiếc dù",
        "ipa": "/ˈʌmbəl/"
    },
    "lex.en.100k.043279": {
        "hw": "uncolored",
        "pos": "adj",
        "vi": "không màu; mộc mạc không tô vẽ",
        "ipa": "/ʌnˈkʌlɚd/"
    },
    "lex.en.100k.043280": {
        "hw": "underpay",
        "pos": "verb",
        "vi": "trả thù lao thấp hơn công sức",
        "ipa": "/ˌʌndɚˈpeɪ/"
    },
    "lex.en.100k.043281": {
        "hw": "undyed",
        "pos": "adj",
        "vi": "mộc nguyên bản; chưa nhuộm màu",
        "ipa": "/ʌnˈdaɪd/"
    },
    "lex.en.100k.043282": {
        "hw": "unkept",
        "pos": "adj",
        "vi": "không được thực hiện; thất hứa",
        "ipa": "/ʌnˈkɛpt/"
    },
    "lex.en.100k.043283": {
        "hw": "unmerciful",
        "pos": "adj",
        "vi": "tàn nhẫn tuyệt đối không thương xót",
        "ipa": "/ʌnˈmɝːsɪfəl/"
    },
    "lex.en.100k.043284": {
        "hw": "unvarying",
        "pos": "adj",
        "vi": "đều đều bất biến không hề đổi",
        "ipa": "/ʌnˈvɛriɪŋ/"
    },
    "lex.en.100k.043285": {
        "hw": "unwaveringly",
        "pos": "adv",
        "vi": "một cách kiên định không lay chuyển",
        "ipa": "/ʌnˈweɪvərɪŋli/"
    },
    "lex.en.100k.043286": {
        "hw": "uprise",
        "pos": "verb",
        "vi": "nổi dậy đồng loạt; vươn lên cao",
        "ipa": "/ʌpˈraɪz/"
    },
    "lex.en.100k.043287": {
        "hw": "utu",
        "pos": "noun",
        "vi": "thần mặt trời Utu thời Lưỡng Hà",
        "ipa": "/ˈuːtuː/"
    },
    "lex.en.100k.043288": {
        "hw": "valetta",
        "pos": "noun",
        "vi": "thủ đô Valletta của đảo quốc Malta",
        "ipa": "/vəˈlɛtə/"
    },
    "lex.en.100k.043289": {
        "hw": "volvulus",
        "pos": "noun",
        "vi": "chứng xoắn nghẽn quai ruột cấp tính",
        "ipa": "/ˈvɑːlvjələs/"
    },
    "lex.en.100k.043290": {
        "hw": "wapiti",
        "pos": "noun",
        "vi": "loài nai tuyết Bắc Mỹ thân lớn",
        "ipa": "/ˈwɑːpɪti/"
    },
    "lex.en.100k.043291": {
        "hw": "weismann",
        "pos": "noun",
        "vi": "nhà sinh học August Weismann",
        "ipa": "/ˈvaɪsmən/"
    },
    "lex.en.100k.043292": {
        "hw": "wellpoint",
        "pos": "noun",
        "vi": "đầu mũi ống hút hạ mực nước ngầm",
        "ipa": "/ˈwɛlpɔɪnt/"
    },
    "lex.en.100k.043293": {
        "hw": "wiggler",
        "pos": "noun",
        "vi": "kẻ ngọ nguậy; bọ gậy ấu trùng muỗi",
        "ipa": "/ˈwɪɡlɚ/"
    },
    "lex.en.100k.043294": {
        "hw": "witting",
        "pos": "adj",
        "vi": "có chủ tâm cố ý; biết rõ việc làm",
        "ipa": "/ˈwɪtɪŋ/"
    },
    "lex.en.100k.043295": {
        "hw": "zombi",
        "pos": "noun",
        "vi": "xác sống ma quỷ tái sinh bí ẩn",
        "ipa": "/ˈzɑːmbi/"
    },
    "lex.en.100k.043296": {
        "hw": "abasement",
        "pos": "noun",
        "vi": "nỗi nhục nhã; sự hạ mình ê chề",
        "ipa": "/əˈbeɪsmənt/"
    },
    "lex.en.100k.043297": {
        "hw": "ablated",
        "pos": "adj",
        "vi": "bị nung mòn tan biến bề mặt",
        "ipa": "/æbˈleɪtɪd/"
    },
    "lex.en.100k.043298": {
        "hw": "abruptness",
        "pos": "noun",
        "vi": "sự đường đột; thái độ cộc cằn thô",
        "ipa": "/əˈbrʌptnəs/"
    },
    "lex.en.100k.043299": {
        "hw": "advisability",
        "pos": "noun",
        "vi": "tính nên làm; sự thích đáng hợp lý",
        "ipa": "/ədˌvaɪzəˈbɪləti/"
    },
    "lex.en.100k.043300": {
        "hw": "aesthetical",
        "pos": "adj",
        "vi": "mang tính thẩm mỹ mỹ cảm",
        "ipa": "/ɛsˈθɛtɪkəl/"
    },
    "lex.en.100k.043301": {
        "hw": "alleghenies",
        "pos": "noun",
        "vi": "dãy Allegheny miền đông nước Mỹ",
        "ipa": "/ˌæləˈɡeɪniz/"
    }
}

OVERRIDES_PART4 = {
    "lex.en.100k.043302": {
        "hw": "almsgiving",
        "pos": "noun",
        "vi": "việc bố thí chẩn bần cứu tế",
        "ipa": "/ˈɑːmzˌɡɪvɪŋ/"
    },
    "lex.en.100k.043303": {
        "hw": "amiability",
        "pos": "noun",
        "vi": "tính hòa nhã dễ mến thân thiện",
        "ipa": "/ˌeɪmiəˈbɪləti/"
    },
    "lex.en.100k.043304": {
        "hw": "animalia",
        "pos": "noun",
        "vi": "giới Động vật trong sinh học",
        "ipa": "/ˌænɪˈmeɪliə/"
    },
    "lex.en.100k.043305": {
        "hw": "anthelmintic",
        "pos": "adj",
        "vi": "có tính tẩy giun sán đường ruột",
        "ipa": "/ˌænθɛlˈmɪntɪk/"
    },
    "lex.en.100k.043306": {
        "hw": "antiarrhythmic",
        "pos": "noun",
        "vi": "thuốc chống loạn nhịp tim",
        "ipa": "/ˌæntiəˈrɪðmɪk/"
    },
    "lex.en.100k.043307": {
        "hw": "antiguan",
        "pos": "adj",
        "vi": "thuộc Antigua và Barbuda",
        "ipa": "/ænˈtiːɡwən/"
    },
    "lex.en.100k.043308": {
        "hw": "antipersonnel",
        "pos": "adj",
        "vi": "sát thương bộ binh con người",
        "ipa": "/ˌæntipɝːsəˈnɛl/"
    },
    "lex.en.100k.043309": {
        "hw": "antipodal",
        "pos": "adj",
        "vi": "đối cực; hoàn toàn trái ngược nhau",
        "ipa": "/ænˈtɪpədəl/"
    },
    "lex.en.100k.043310": {
        "hw": "apprehensively",
        "pos": "adv",
        "vi": "một cách đầy lo lắng e sợ",
        "ipa": "/ˌæprɪˈhɛnsɪvli/"
    },
    "lex.en.100k.043311": {
        "hw": "aquavit",
        "pos": "noun",
        "vi": "rượu trắng chưng cất Scandinavia",
        "ipa": "/ˈɑːkwəviːt/"
    },
    "lex.en.100k.043312": {
        "hw": "aquiline",
        "pos": "adj",
        "vi": "khoằm như mỏ chim đại bàng",
        "ipa": "/ˈækwɪlaɪn/"
    },
    "lex.en.100k.043313": {
        "hw": "aril",
        "pos": "noun",
        "vi": "áo hạt bọc ngoài hạt thực vật",
        "ipa": "/ˈærɪl/"
    },
    "lex.en.100k.043314": {
        "hw": "aureole",
        "pos": "noun",
        "vi": "hào quang quầng sáng quanh đầu",
        "ipa": "/ˈɔːriˌoʊl/"
    },
    "lex.en.100k.043315": {
        "hw": "avogadro",
        "pos": "noun",
        "vi": "nhà hóa học Amedeo Avogadro",
        "ipa": "/ˌævəˈɡɑːdroʊ/"
    },
    "lex.en.100k.043316": {
        "hw": "baboo",
        "pos": "noun",
        "vi": "ông thầy thông; người có học Ấn",
        "ipa": "/ˈbɑːbuː/"
    },
    "lex.en.100k.043317": {
        "hw": "basilicata",
        "pos": "noun",
        "vi": "vùng Basilicata ở miền nam Ý",
        "ipa": "/bəˌzɪlɪˈkɑːtə/"
    },
    "lex.en.100k.043318": {
        "hw": "bathos",
        "pos": "noun",
        "vi": "sự tụt cảm xúc sáo rỗng hụt hẫng",
        "ipa": "/ˈbeɪθɑːs/"
    },
    "lex.en.100k.043319": {
        "hw": "bayberry",
        "pos": "noun",
        "vi": "cây thanh mai; bụi cây sáp",
        "ipa": "/ˈbeɪˌbɛri/"
    },
    "lex.en.100k.043320": {
        "hw": "benthos",
        "pos": "noun",
        "vi": "quần xã sinh vật tầng đáy biển",
        "ipa": "/ˈbɛnθɑːs/"
    },
    "lex.en.100k.043321": {
        "hw": "benzocaine",
        "pos": "noun",
        "vi": "thuốc gây tê cục bộ benzocain",
        "ipa": "/ˈbɛnzoʊkeɪn/"
    },
    "lex.en.100k.043322": {
        "hw": "bifocal",
        "pos": "adj",
        "vi": "có hai tiêu cự tròng kính",
        "ipa": "/baɪˈfoʊkəl/"
    },
    "lex.en.100k.043323": {
        "hw": "binnacle",
        "pos": "noun",
        "vi": "hộp la bàn trên boong tàu thủy",
        "ipa": "/ˈbɪnəkəl/"
    },
    "lex.en.100k.043324": {
        "hw": "bobolink",
        "pos": "noun",
        "vi": "chim di cư bobolink châu Mỹ",
        "ipa": "/ˈbɑːbəˌlɪŋk/"
    },
    "lex.en.100k.043325": {
        "hw": "bombus",
        "pos": "noun",
        "vi": "chi ong nghệ thụ phấn Bombus",
        "ipa": "/ˈbɑːmbəs/"
    },
    "lex.en.100k.043326": {
        "hw": "brancusi",
        "pos": "noun",
        "vi": "nhà điêu khắc Constantin Brâncuși",
        "ipa": "/brɑːnˈkuːzi/"
    },
    "lex.en.100k.043327": {
        "hw": "brimful",
        "pos": "adj",
        "vi": "đầy ắp tràn trề tới tận mép",
        "ipa": "/ˈbrɪmˌfʊl/"
    },
    "lex.en.100k.043328": {
        "hw": "calcination",
        "pos": "noun",
        "vi": "sự nung khô ở nhiệt độ cao",
        "ipa": "/ˌkælsɪˈneɪʃən/"
    },
    "lex.en.100k.043329": {
        "hw": "candlewick",
        "pos": "noun",
        "vi": "tim nến; bấc nến sợi bông dày",
        "ipa": "/ˈkændəlˌwɪk/"
    },
    "lex.en.100k.043330": {
        "hw": "canetti",
        "pos": "noun",
        "vi": "nhà văn Elias Canetti giải Nobel",
        "ipa": "/kəˈnɛti/"
    },
    "lex.en.100k.043331": {
        "hw": "capek",
        "pos": "noun",
        "vi": "nhà văn Karel Čapek đẻ ra chữ Robot",
        "ipa": "/ˈtʃɑːpɛk/"
    },
    "lex.en.100k.043332": {
        "hw": "capitation",
        "pos": "noun",
        "vi": "thuế thân; thuế theo đầu người",
        "ipa": "/ˌkæpɪˈteɪʃən/"
    },
    "lex.en.100k.043333": {
        "hw": "caulked",
        "pos": "adj",
        "vi": "được trám kín khe hở chống thấm",
        "ipa": "/kɔːkt/"
    },
    "lex.en.100k.043334": {
        "hw": "celebrex",
        "pos": "noun",
        "vi": "thuốc giảm đau Celebrex",
        "ipa": "/ˈsɛləbrɛks/"
    },
    "lex.en.100k.043335": {
        "hw": "cervus",
        "pos": "noun",
        "vi": "chi hươu đỏ nai sừng tấm Cervus",
        "ipa": "/ˈsɝːvəs/"
    },
    "lex.en.100k.043336": {
        "hw": "chelated",
        "pos": "adj",
        "vi": "tạo phức càng cua chelat hóa",
        "ipa": "/ˈkiːleɪtɪd/"
    },
    "lex.en.100k.043337": {
        "hw": "chignon",
        "pos": "noun",
        "vi": "búi tóc cài sau gáy tao nhã",
        "ipa": "/ˈʃiːnjɑːn/"
    },
    "lex.en.100k.043338": {
        "hw": "chimerical",
        "pos": "adj",
        "vi": "huyễn tưởng hoang đường không tưởng",
        "ipa": "/kaɪˈmɛrɪkəl/"
    },
    "lex.en.100k.043339": {
        "hw": "christianize",
        "pos": "verb",
        "vi": "Cơ Đốc hóa; truyền đạo Ki-tô",
        "ipa": "/ˈkrɪstʃənaɪz/"
    },
    "lex.en.100k.043340": {
        "hw": "chuff",
        "pos": "verb",
        "vi": "thở phì phò; phụt hơi xình xịch",
        "ipa": "/tʃʌf/"
    },
    "lex.en.100k.043341": {
        "hw": "cilium",
        "pos": "noun",
        "vi": "lông mao tế bào; lông mi mí mắt",
        "ipa": "/ˈsɪliəm/"
    },
    "lex.en.100k.043342": {
        "hw": "collarless",
        "pos": "adj",
        "vi": "không có cổ áo; áo cổ tròn",
        "ipa": "/ˈkɑːlɚləs/"
    },
    "lex.en.100k.043343": {
        "hw": "collimation",
        "pos": "noun",
        "vi": "sự chuẩn trực gom chùm tia",
        "ipa": "/ˌkɑːlɪˈmeɪʃən/"
    },
    "lex.en.100k.043344": {
        "hw": "conferral",
        "pos": "noun",
        "vi": "sự phong tặng trao tước vị",
        "ipa": "/kənˈfɝːəl/"
    },
    "lex.en.100k.043345": {
        "hw": "convalesce",
        "pos": "verb",
        "vi": "tĩnh dưỡng hồi phục sau cơn ốm",
        "ipa": "/ˌkɑːnvəˈlɛs/"
    },
    "lex.en.100k.043346": {
        "hw": "costless",
        "pos": "adj",
        "vi": "miễn phí hoàn toàn; không tốn kém",
        "ipa": "/ˈkɔːstləs/"
    },
    "lex.en.100k.043347": {
        "hw": "countrywoman",
        "pos": "noun",
        "vi": "phụ nữ nông thôn; nữ đồng hương",
        "ipa": "/ˈkʌntriˌwʊmən/"
    },
    "lex.en.100k.043348": {
        "hw": "couperin",
        "pos": "noun",
        "vi": "nhà soạn nhạc François Couperin",
        "ipa": "/kuːpəˈræ̃/"
    },
    "lex.en.100k.043349": {
        "hw": "crimper",
        "pos": "noun",
        "vi": "kìm bấm cos; máy uốn gợn tóc",
        "ipa": "/ˈkrɪmpɚ/"
    },
    "lex.en.100k.043350": {
        "hw": "crosier",
        "pos": "noun",
        "vi": "gậy mục tử hình móc giám mục",
        "ipa": "/ˈkroʊʒɚ/"
    },
    "lex.en.100k.043351": {
        "hw": "cruet",
        "pos": "noun",
        "vi": "bình nhỏ đựng dầu giấm gia vị",
        "ipa": "/ˈkruːɪt/"
    },
    "lex.en.100k.043352": {
        "hw": "cycloid",
        "pos": "adj",
        "vi": "có hình đường cong xicloit lăn tròn",
        "ipa": "/ˈsaɪklɔɪd/"
    },
    "lex.en.100k.043353": {
        "hw": "dacoit",
        "pos": "noun",
        "vi": "tướng cướp có vũ trang Ấn Độ",
        "ipa": "/dəˈkɔɪt/"
    },
    "lex.en.100k.043354": {
        "hw": "diacritic",
        "pos": "adj",
        "vi": "dùng làm dấu phụ phân biệt âm",
        "ipa": "/ˌdaɪəˈkrɪtɪk/"
    },
    "lex.en.100k.043355": {
        "hw": "diazo",
        "pos": "adj",
        "vi": "chứa nhóm chức diazo hai nitơ",
        "ipa": "/daɪˈæzoʊ/"
    },
    "lex.en.100k.043356": {
        "hw": "dishcloth",
        "pos": "noun",
        "vi": "giẻ lau bát đĩa; khăn rửa chén",
        "ipa": "/ˈdɪʃklɔːθ/"
    },
    "lex.en.100k.043357": {
        "hw": "dolomitic",
        "pos": "adj",
        "vi": "chứa chất đá vôi dolomit",
        "ipa": "/ˌdoʊləˈmɪtɪk/"
    },
    "lex.en.100k.043358": {
        "hw": "duralumin",
        "pos": "noun",
        "vi": "hợp kim nhẹ duralumin máy bay",
        "ipa": "/djʊˈræljəmɪn/"
    },
    "lex.en.100k.043359": {
        "hw": "duse",
        "pos": "noun",
        "vi": "nữ minh tinh kịch Eleonora Duse",
        "ipa": "/ˈduːzeɪ/"
    },
    "lex.en.100k.043360": {
        "hw": "dustman",
        "pos": "noun",
        "vi": "công nhân thu gom dọn rác thải",
        "ipa": "/ˈdʌstmən/"
    },
    "lex.en.100k.043361": {
        "hw": "dybbuk",
        "pos": "noun",
        "vi": "ác linh chiếm đoạt thân xác người",
        "ipa": "/ˈdɪbək/"
    },
    "lex.en.100k.043362": {
        "hw": "effeminacy",
        "pos": "noun",
        "vi": "tính tình ẻo lả thiếu nam tính",
        "ipa": "/ɪˈfɛmɪnəsi/"
    },
    "lex.en.100k.043363": {
        "hw": "episodically",
        "pos": "adv",
        "vi": "theo từng đoạn ngắn đứt quãng",
        "ipa": "/ˌɛpɪˈsɑːdɪkli/"
    },
    "lex.en.100k.043364": {
        "hw": "erratum",
        "pos": "noun",
        "vi": "tờ đính chính lỗi in ấn sách báo",
        "ipa": "/ɛˈrɑːtəm/"
    },
    "lex.en.100k.043365": {
        "hw": "eurocentrism",
        "pos": "noun",
        "vi": "thuyết lấy châu Âu làm trung tâm",
        "ipa": "/ˌjʊroʊˈsɛntrɪzəm/"
    },
    "lex.en.100k.043366": {
        "hw": "fainthearted",
        "pos": "adj",
        "vi": "nhát gan mềm yếu thiếu can đảm",
        "ipa": "/ˌfeɪntˈhɑːrtɪd/"
    },
    "lex.en.100k.043367": {
        "hw": "faultlessly",
        "pos": "adv",
        "vi": "một cách hoàn hảo không tì vết",
        "ipa": "/ˈfɔːltləsli/"
    },
    "lex.en.100k.043368": {
        "hw": "fedayeen",
        "pos": "noun",
        "vi": "chiến binh cảm tử tự nguyện Ả Rập",
        "ipa": "/ˌfɛdəˈjiːn/"
    },
    "lex.en.100k.043369": {
        "hw": "fellah",
        "pos": "noun",
        "vi": "nông dân nghèo Ai Cập và Trung Đông",
        "ipa": "/ˈfɛlə/"
    },
    "lex.en.100k.043370": {
        "hw": "filthiness",
        "pos": "noun",
        "vi": "sự nhơ nhớp tục tĩu bẩn thỉu",
        "ipa": "/ˈfɪlθinəs/"
    },
    "lex.en.100k.043371": {
        "hw": "flatworm",
        "pos": "noun",
        "vi": "loài giun dẹp sán lá ký sinh",
        "ipa": "/ˈflætwɝːm/"
    },
    "lex.en.100k.043372": {
        "hw": "foreignness",
        "pos": "noun",
        "vi": "tính xa lạ ngoại quốc dị biệt",
        "ipa": "/ˈfɔːrənnəs/"
    },
    "lex.en.100k.043373": {
        "hw": "fujiyama",
        "pos": "noun",
        "vi": "ngọn núi Phú Sĩ của đất nước Nhật",
        "ipa": "/ˌfuːdʒiˈjɑːmə/"
    },
    "lex.en.100k.043374": {
        "hw": "genuflect",
        "pos": "verb",
        "vi": "quỳ một gối tôn kính cúi lạy",
        "ipa": "/ˈdʒɛnjəflɛkt/"
    },
    "lex.en.100k.043375": {
        "hw": "gristmill",
        "pos": "noun",
        "vi": "nhà máy xay bột ngũ cốc nước gió",
        "ipa": "/ˈɡrɪstmɪl/"
    },
    "lex.en.100k.043376": {
        "hw": "groundcover",
        "pos": "noun",
        "vi": "thảm thực vật bò phủ kín mặt đất",
        "ipa": "/ˈɡraʊndkʌvɚ/"
    },
    "lex.en.100k.043377": {
        "hw": "hagfish",
        "pos": "noun",
        "vi": "cá mút đá nhầy đáy biển sâu",
        "ipa": "/ˈhæɡfɪʃ/"
    },
    "lex.en.100k.043378": {
        "hw": "hairnet",
        "pos": "noun",
        "vi": "lưới bọc giữ búi tóc gọn gàng",
        "ipa": "/ˈhɛrnɛt/"
    },
    "lex.en.100k.043379": {
        "hw": "hitchings",
        "pos": "noun",
        "vi": "nhà hóa sinh George H. Hitchings",
        "ipa": "/ˈhɪtʃɪŋz/"
    },
    "lex.en.100k.043380": {
        "hw": "ideographic",
        "pos": "adj",
        "vi": "thuộc hệ chữ viết tượng hình biểu ý",
        "ipa": "/ˌaɪdioʊˈɡræfɪk/"
    },
    "lex.en.100k.043381": {
        "hw": "immunosuppressed",
        "pos": "adj",
        "vi": "bị suy giảm ức chế hệ miễn dịch",
        "ipa": "/ˌɪmjənoʊsəˈprɛst/"
    },
    "lex.en.100k.043382": {
        "hw": "imposture",
        "pos": "noun",
        "vi": "trò mạo danh lừa đảo tinh vi",
        "ipa": "/ɪmˈpɑːstʃɚ/"
    },
    "lex.en.100k.043383": {
        "hw": "insanitary",
        "pos": "adj",
        "vi": "mất vệ sinh ô nhiễm bẩn thỉu",
        "ipa": "/ɪnˈsænɪtɛri/"
    },
    "lex.en.100k.043384": {
        "hw": "insurgence",
        "pos": "noun",
        "vi": "hành vi nổi dậy chống chính quyền",
        "ipa": "/ɪnˈsɝːdʒəns/"
    },
    "lex.en.100k.043385": {
        "hw": "intermittency",
        "pos": "noun",
        "vi": "tính gián đoạn chập chờn ngắt quãng",
        "ipa": "/ˌɪntɚˈmɪtənsi/"
    },
    "lex.en.100k.043386": {
        "hw": "intubate",
        "pos": "verb",
        "vi": "đặt ống thở nội khí quản y tế",
        "ipa": "/ˈɪntuːbeɪt/"
    },
    "lex.en.100k.043387": {
        "hw": "ironmongery",
        "pos": "noun",
        "vi": "cửa hàng kinh doanh đồ sắt kim khí",
        "ipa": "/ˈaɪɚnmʌŋɡəri/"
    },
    "lex.en.100k.043388": {
        "hw": "juiciness",
        "pos": "noun",
        "vi": "độ mọng nước hấp dẫn ngon lành",
        "ipa": "/ˈdʒuːsinəs/"
    },
    "lex.en.100k.043389": {
        "hw": "justiciar",
        "pos": "noun",
        "vi": "quan tể tướng tư pháp nước Anh xưa",
        "ipa": "/dʒʌˈstɪʃiɚ/"
    },
    "lex.en.100k.043390": {
        "hw": "khaya",
        "pos": "noun",
        "vi": "chi cây xà cừ xoan Khaya",
        "ipa": "/ˈkeɪə/"
    },
    "lex.en.100k.043391": {
        "hw": "kuroshio",
        "pos": "noun",
        "vi": "dòng hải lưu Kuroshio Thái Bình",
        "ipa": "/ˌkʊroʊˈʃiːoʊ/"
    },
    "lex.en.100k.043392": {
        "hw": "lacerate",
        "pos": "adj",
        "vi": "bị xé rách toạc nham nhở mép",
        "ipa": "/ˈlæsəreɪt/"
    },
    "lex.en.100k.043393": {
        "hw": "lamivudine",
        "pos": "noun",
        "vi": "thuốc kháng virus lamivudine gan B",
        "ipa": "/ləˈmɪvjədiːn/"
    },
    "lex.en.100k.043394": {
        "hw": "lassitude",
        "pos": "noun",
        "vi": "trạng thái lừ đừ kiệt sức bơ phờ",
        "ipa": "/ˈlæsɪtuːd/"
    },
    "lex.en.100k.043395": {
        "hw": "likeliness",
        "pos": "noun",
        "vi": "khả năng diễn ra; tính chắc chắn",
        "ipa": "/ˈlaɪklinəs/"
    },
    "lex.en.100k.043396": {
        "hw": "macroscopically",
        "pos": "adv",
        "vi": "nhìn thấy bằng mắt thường vĩ mô",
        "ipa": "/ˌmækroʊˈskɑːpɪkli/"
    },
    "lex.en.100k.043397": {
        "hw": "maintenon",
        "pos": "noun",
        "vi": "phu nhân Madame de Maintenon",
        "ipa": "/mæ̃tˈnɔ̃/"
    },
    "lex.en.100k.043398": {
        "hw": "maladroit",
        "pos": "adj",
        "vi": "vụng về lóng ngóng trong cư xử",
        "ipa": "/ˌmæləˈdrɔɪt/"
    },
    "lex.en.100k.043399": {
        "hw": "malva",
        "pos": "noun",
        "vi": "chi cây cẩm quỳ hoa Malva tím",
        "ipa": "/ˈmælvə/"
    },
    "lex.en.100k.043400": {
        "hw": "marginality",
        "pos": "noun",
        "vi": "thực trạng bị gạt ra ngoài lề",
        "ipa": "/ˌmɑːrdʒɪˈnæləti/"
    },
    "lex.en.100k.043401": {
        "hw": "markova",
        "pos": "noun",
        "vi": "nghệ sĩ ba-lê Alicia Markova",
        "ipa": "/mɑːrˈkoʊvə/"
    }
}

OVERRIDES_PART5 = {
    "lex.en.100k.043402": {
        "hw": "meshwork",
        "pos": "noun",
        "vi": "mạng lưới đan xen; hệ lưới",
        "ipa": "/ˈmɛʃwɝːk/"
    },
    "lex.en.100k.043403": {
        "hw": "milhaud",
        "pos": "noun",
        "vi": "nhà soạn nhạc Pháp Darius Milhaud",
        "ipa": "/miˈjoʊ/"
    },
    "lex.en.100k.043404": {
        "hw": "ministration",
        "pos": "noun",
        "vi": "sự chăm sóc giúp đỡ; việc mục vụ",
        "ipa": "/ˌmɪnɪˈstreɪʃən/"
    },
    "lex.en.100k.043405": {
        "hw": "mishandle",
        "pos": "verb",
        "vi": "xử lý vụng về sai sót; đối xử tệ",
        "ipa": "/mɪsˈhændəl/"
    },
    "lex.en.100k.043406": {
        "hw": "mycotoxin",
        "pos": "noun",
        "vi": "độc tố do các loài vi nấm tiết ra",
        "ipa": "/ˌmaɪkoʊˈtɑːksɪn/"
    },
    "lex.en.100k.043407": {
        "hw": "numeration",
        "pos": "noun",
        "vi": "hệ thống đếm số; cách đánh số",
        "ipa": "/ˌnuːməˈreɪʃən/"
    },
    "lex.en.100k.043408": {
        "hw": "numismatist",
        "pos": "noun",
        "vi": "nhà nghiên cứu sưu tầm tiền cổ",
        "ipa": "/nuːˈmɪzmətɪst/"
    },
    "lex.en.100k.043409": {
        "hw": "overextend",
        "pos": "verb",
        "vi": "mở rộng quá mức; gắng sức kiệt quệ",
        "ipa": "/ˌoʊvɚrɪkˈstɛnd/"
    },
    "lex.en.100k.043410": {
        "hw": "overmuch",
        "pos": "adj",
        "vi": "quá nhiều quá mức cần thiết",
        "ipa": "/ˌoʊvɚˈmʌtʃ/"
    },
    "lex.en.100k.043411": {
        "hw": "pasto",
        "pos": "noun",
        "vi": "thành phố và núi lửa Pasto Colombia",
        "ipa": "/ˈpɑːstoʊ/"
    },
    "lex.en.100k.043412": {
        "hw": "pederast",
        "pos": "noun",
        "vi": "kẻ ấu dâm nam giới với bé trai",
        "ipa": "/ˈpɛdəræst/"
    },
    "lex.en.100k.043413": {
        "hw": "pekoe",
        "pos": "noun",
        "vi": "loại trà búp non pekoe thượng hạng",
        "ipa": "/ˈpiːkoʊ/"
    },
    "lex.en.100k.043414": {
        "hw": "peleus",
        "pos": "noun",
        "vi": "vua Peleus cha của dũng sĩ Achilles",
        "ipa": "/ˈpiːliəs/"
    },
    "lex.en.100k.043415": {
        "hw": "peridotite",
        "pos": "noun",
        "vi": "đá magma peridotit giàu olivin",
        "ipa": "/pəˈrɪdətaɪt/"
    },
    "lex.en.100k.043416": {
        "hw": "pervasively",
        "pos": "adv",
        "vi": "một cách lan tỏa tỏa khắp mọi nơi",
        "ipa": "/pɚˈveɪsɪvli/"
    },
    "lex.en.100k.043417": {
        "hw": "philadelphus",
        "pos": "noun",
        "vi": "chi cây hoa lài tây Philadelphus",
        "ipa": "/ˌfɪləˈdɛlfəs/"
    },
    "lex.en.100k.043418": {
        "hw": "phlogiston",
        "pos": "noun",
        "vi": "thuyết chất cháy phlogiston cổ đại",
        "ipa": "/flɑːˈdʒɪstən/"
    },
    "lex.en.100k.043419": {
        "hw": "photostat",
        "pos": "noun",
        "vi": "bản sao chụp tài liệu photostat",
        "ipa": "/ˈfoʊtəstæt/"
    },
    "lex.en.100k.043420": {
        "hw": "phrenic",
        "pos": "adj",
        "vi": "thuộc cơ hoành hô hấp",
        "ipa": "/ˈfrɛnɪk/"
    },
    "lex.en.100k.043421": {
        "hw": "phytochemical",
        "pos": "noun",
        "vi": "hợp chất hóa thực vật tự nhiên",
        "ipa": "/ˌfaɪtoʊˈkɛmɪkəl/"
    },
    "lex.en.100k.043422": {
        "hw": "pigman",
        "pos": "noun",
        "vi": "người chăn nuôi và chăm sóc lợn",
        "ipa": "/ˈpɪɡmən/"
    },
    "lex.en.100k.043423": {
        "hw": "platy",
        "pos": "noun",
        "vi": "loài cá mún cảnh platy nhiệt đới",
        "ipa": "/ˈpleɪti/"
    },
    "lex.en.100k.043424": {
        "hw": "plummy",
        "pos": "adj",
        "vi": "ngon ngọt; giọng sang trọng đài các",
        "ipa": "/ˈplʌmi/"
    },
    "lex.en.100k.043425": {
        "hw": "progestogen",
        "pos": "noun",
        "vi": "hoóc-môn thai kỳ nhóm progestogen",
        "ipa": "/proʊˈdʒɛstədʒən/"
    },
    "lex.en.100k.043426": {
        "hw": "propagandize",
        "pos": "verb",
        "vi": "tuyên truyền vận động quan điểm",
        "ipa": "/ˌprɑːpəˈɡændaɪz/"
    },
    "lex.en.100k.043427": {
        "hw": "provincialism",
        "pos": "noun",
        "vi": "óc địa phương; tính thiển cận",
        "ipa": "/prəˈvɪnʃəlɪzəm/"
    },
    "lex.en.100k.043428": {
        "hw": "pubescence",
        "pos": "noun",
        "vi": "giai đoạn dậy thì; lớp lông mịn lá",
        "ipa": "/pjuːˈbɛsəns/"
    },
    "lex.en.100k.043429": {
        "hw": "putamen",
        "pos": "noun",
        "vi": "nhân vỏ bèo putamen trong não",
        "ipa": "/pjuːˈteɪmən/"
    },
    "lex.en.100k.043430": {
        "hw": "reassertion",
        "pos": "noun",
        "vi": "sự tái khẳng định quả quyết",
        "ipa": "/ˌriːəˈsɝːʃən/"
    },
    "lex.en.100k.043431": {
        "hw": "reconcilable",
        "pos": "adj",
        "vi": "có thể hòa giải; có thể dung hòa",
        "ipa": "/ˌrɛkənˈsaɪləbəl/"
    },
    "lex.en.100k.043432": {
        "hw": "regnant",
        "pos": "adj",
        "vi": "đang trị vì chấp chính; thịnh hành",
        "ipa": "/ˈrɛɡnənt/"
    },
    "lex.en.100k.043433": {
        "hw": "reinforcer",
        "pos": "noun",
        "vi": "tác nhân củng cố kích thích hành vi",
        "ipa": "/ˌriːɪnˈfɔːrsɚ/"
    },
    "lex.en.100k.043434": {
        "hw": "relentlessness",
        "pos": "noun",
        "vi": "tính không ngừng; sự kiên quyết",
        "ipa": "/rɪˈlɛntləsnəs/"
    },
    "lex.en.100k.043435": {
        "hw": "riotously",
        "pos": "adv",
        "vi": "một cách náo loạn om sòm bừa bãi",
        "ipa": "/ˈraɪətəsli/"
    },
    "lex.en.100k.043436": {
        "hw": "saltbush",
        "pos": "noun",
        "vi": "loài cây bụi chịu mặn saltbush",
        "ipa": "/ˈsɔːltˌbʊʃ/"
    },
    "lex.en.100k.043437": {
        "hw": "screechy",
        "pos": "adj",
        "vi": "chói tai thé the đinh tai",
        "ipa": "/ˈskriːtʃi/"
    },
    "lex.en.100k.043438": {
        "hw": "seraglio",
        "pos": "noun",
        "vi": "hậu cung cung điện Thổ Nhĩ Kỳ",
        "ipa": "/sɪˈrɑːljoʊ/"
    },
    "lex.en.100k.043439": {
        "hw": "sheller",
        "pos": "noun",
        "vi": "máy bóc vỏ; công nhân tách vỏ hạt",
        "ipa": "/ˈʃɛlɚ/"
    },
    "lex.en.100k.043440": {
        "hw": "shirer",
        "pos": "noun",
        "vi": "nhà báo sử gia William L. Shirer",
        "ipa": "/ˈʃaɪrɚ/"
    },
    "lex.en.100k.043441": {
        "hw": "shirting",
        "pos": "noun",
        "vi": "vải dệt chuyên may áo sơ mi",
        "ipa": "/ˈʃɝːtɪŋ/"
    },
    "lex.en.100k.043442": {
        "hw": "shirtwaist",
        "pos": "noun",
        "vi": "áo sơ mi nữ kiểu cổ điển thanh lịch",
        "ipa": "/ˈʃɝːtweɪst/"
    },
    "lex.en.100k.043443": {
        "hw": "snick",
        "pos": "noun",
        "vi": "vết cứa khía nhỏ; tiếng lách cách",
        "ipa": "/snɪk/"
    },
    "lex.en.100k.043444": {
        "hw": "snifter",
        "pos": "noun",
        "vi": "ly bầu đáy rộng uống rượu mạnh",
        "ipa": "/ˈsnɪftɚ/"
    },
    "lex.en.100k.043445": {
        "hw": "soundman",
        "pos": "noun",
        "vi": "chuyên viên kỹ thuật âm thanh",
        "ipa": "/ˈsaʊndmæn/"
    },
    "lex.en.100k.043446": {
        "hw": "sporophyte",
        "pos": "noun",
        "vi": "thể bào tử lưỡng bội ở thực vật",
        "ipa": "/ˈspɔːrəfaɪt/"
    },
    "lex.en.100k.043447": {
        "hw": "sprog",
        "pos": "noun",
        "vi": "tân binh mới nhập ngũ; đứa trẻ con",
        "ipa": "/sprɑːɡ/"
    },
    "lex.en.100k.043448": {
        "hw": "stentorian",
        "pos": "adj",
        "vi": "oang oang vang dội sang sảng",
        "ipa": "/stɛnˈtɔːriən/"
    },
    "lex.en.100k.043449": {
        "hw": "stereoscope",
        "pos": "noun",
        "vi": "kính lập thể xem ảnh ba chiều",
        "ipa": "/ˈstɛriəskoʊp/"
    },
    "lex.en.100k.043450": {
        "hw": "submissively",
        "pos": "adv",
        "vi": "một cách ngoan ngoãn phục tùng",
        "ipa": "/səbˈmɪsɪvli/"
    },
    "lex.en.100k.043451": {
        "hw": "teleost",
        "pos": "noun",
        "vi": "loài cá xương thật có vây tia",
        "ipa": "/ˈtɛlioʊst/"
    },
    "lex.en.100k.043452": {
        "hw": "tetroxide",
        "pos": "noun",
        "vi": "oxit chứa bốn nguyên tử oxy",
        "ipa": "/tɛˈtrɑːksaɪd/"
    },
    "lex.en.100k.043453": {
        "hw": "ticktock",
        "pos": "noun",
        "vi": "tiếng tích tắc đồng hồ gõ nhịp",
        "ipa": "/ˈtɪktɑːk/"
    },
    "lex.en.100k.043454": {
        "hw": "tindale",
        "pos": "noun",
        "vi": "học giả William Tyndale dịch Kinh",
        "ipa": "/ˈtɪndəl/"
    },
    "lex.en.100k.043455": {
        "hw": "toolmaker",
        "pos": "noun",
        "vi": "thợ cơ khí chế tạo khuôn mẫu",
        "ipa": "/ˈtuːlˌmeɪkɚ/"
    },
    "lex.en.100k.043456": {
        "hw": "toothsome",
        "pos": "adj",
        "vi": "ngon miệng hấp dẫn vừa khẩu vị",
        "ipa": "/ˈtuːθsəm/"
    },
    "lex.en.100k.043457": {
        "hw": "torreon",
        "pos": "noun",
        "vi": "thành phố Torreón của Mexico",
        "ipa": "/tɔːreɪˈoʊn/"
    },
    "lex.en.100k.043458": {
        "hw": "towelling",
        "pos": "noun",
        "vi": "vải bông dày may khăn tắm bông",
        "ipa": "/ˈtaʊəlɪŋ/"
    },
    "lex.en.100k.043459": {
        "hw": "transmittable",
        "pos": "adj",
        "vi": "có thể truyền dẫn lây nhiễm được",
        "ipa": "/trænzˈmɪtəbəl/"
    },
    "lex.en.100k.043460": {
        "hw": "ulva",
        "pos": "noun",
        "vi": "chi rong diếp biển xanh Ulva",
        "ipa": "/ˈʌlvə/"
    },
    "lex.en.100k.043461": {
        "hw": "unconvincingly",
        "pos": "adv",
        "vi": "một cách thiếu tính thuyết phục",
        "ipa": "/ˌʌnkənˈvɪnsɪŋli/"
    },
    "lex.en.100k.043462": {
        "hw": "undistorted",
        "pos": "adj",
        "vi": "không bị biến dạng méo mó sai lệch",
        "ipa": "/ˌʌndɪˈstɔːrtɪd/"
    },
    "lex.en.100k.043463": {
        "hw": "undistributed",
        "pos": "adj",
        "vi": "chưa được phân bổ phân phối",
        "ipa": "/ˌʌndɪˈstrɪbjətɪd/"
    },
    "lex.en.100k.043464": {
        "hw": "unreached",
        "pos": "adj",
        "vi": "chưa đạt tới; hẻo lánh khó tới",
        "ipa": "/ʌnˈriːtʃt/"
    },
    "lex.en.100k.043465": {
        "hw": "untutored",
        "pos": "adj",
        "vi": "thiếu rèn luyện; tự nhiên mộc mạc",
        "ipa": "/ʌnˈtuːtɚd/"
    },
    "lex.en.100k.043466": {
        "hw": "urease",
        "pos": "noun",
        "vi": "men enzym thủy phân urê ureaza",
        "ipa": "/ˈjʊrieɪs/"
    },
    "lex.en.100k.043467": {
        "hw": "vacillation",
        "pos": "noun",
        "vi": "sự do dự ngập ngừng dao động",
        "ipa": "/ˌvæsəˈleɪʃən/"
    },
    "lex.en.100k.043468": {
        "hw": "vacuity",
        "pos": "noun",
        "vi": "sự trống rỗng; vẻ ngơ ngác vô cảm",
        "ipa": "/væˈkjuːəti/"
    },
    "lex.en.100k.043469": {
        "hw": "vandalise",
        "pos": "verb",
        "vi": "cố ý đập phá hủy hoại của công",
        "ipa": "/ˈvændəlaɪz/"
    },
    "lex.en.100k.043470": {
        "hw": "viceregal",
        "pos": "adj",
        "vi": "thuộc chức phó vương tổng trấn",
        "ipa": "/vaɪsˈriːɡəl/"
    },
    "lex.en.100k.043471": {
        "hw": "virtuously",
        "pos": "adv",
        "vi": "một cách trong sạch đức hạnh",
        "ipa": "/ˈvɝːtʃuəsli/"
    },
    "lex.en.100k.043472": {
        "hw": "walloping",
        "pos": "adj",
        "vi": "to tướng khổng lồ đáng kinh ngạc",
        "ipa": "/ˈwɑːləpɪŋ/"
    },
    "lex.en.100k.043473": {
        "hw": "wellborn",
        "pos": "adj",
        "vi": "xuất thân dòng dõi quý tộc cao quý",
        "ipa": "/ˈwɛlˌbɔːrn/"
    },
    "lex.en.100k.043474": {
        "hw": "acquirement",
        "pos": "noun",
        "vi": "kỹ năng thu nhận được qua rèn luyện",
        "ipa": "/əˈkwaɪərmənt/"
    },
    "lex.en.100k.043475": {
        "hw": "agrigento",
        "pos": "noun",
        "vi": "thành phố Agrigento vùng Sicilia Ý",
        "ipa": "/ˌæɡrɪˈdʒɛntoʊ/"
    },
    "lex.en.100k.043476": {
        "hw": "aldol",
        "pos": "noun",
        "vi": "hợp chất hữu cơ aldol ngưng tụ",
        "ipa": "/ˈældɔːl/"
    },
    "lex.en.100k.043477": {
        "hw": "ambulant",
        "pos": "adj",
        "vi": "có thể tự đi lại được không liệt",
        "ipa": "/ˈæmbjələnt/"
    },
    "lex.en.100k.043478": {
        "hw": "anneal",
        "pos": "verb",
        "vi": "ủ nhiệt ram kim loại cho bớt giòn",
        "ipa": "/əˈniːl/"
    },
    "lex.en.100k.043479": {
        "hw": "antabuse",
        "pos": "noun",
        "vi": "thuốc cai nghiện rượu Antabuse",
        "ipa": "/ˈæntəbjuːs/"
    },
    "lex.en.100k.043480": {
        "hw": "antidiabetic",
        "pos": "noun",
        "vi": "thuốc kiểm soát bệnh tiểu đường",
        "ipa": "/ˌæntidaɪəˈbɛtɪk/"
    },
    "lex.en.100k.043481": {
        "hw": "aplysia",
        "pos": "noun",
        "vi": "chi ốc sên biển thỏ biển Aplysia",
        "ipa": "/əˈplɪʒiə/"
    },
    "lex.en.100k.043482": {
        "hw": "ardea",
        "pos": "noun",
        "vi": "chi chim diệc lớn Ardea hoang dã",
        "ipa": "/ˈɑːrdiə/"
    },
    "lex.en.100k.043483": {
        "hw": "arikara",
        "pos": "noun",
        "vi": "bộ tộc Arikara bản địa Bắc Mỹ",
        "ipa": "/əˈrɪkərə/"
    },
    "lex.en.100k.043484": {
        "hw": "asphodel",
        "pos": "noun",
        "vi": "loài hoa bất tử thảo asphodel",
        "ipa": "/ˈæsfədɛl/"
    },
    "lex.en.100k.043485": {
        "hw": "auricle",
        "pos": "noun",
        "vi": "tâm nhĩ của tim; vành tai ngoài",
        "ipa": "/ˈɔːrɪkəl/"
    },
    "lex.en.100k.043486": {
        "hw": "auriga",
        "pos": "noun",
        "vi": "chòm sao Ngự Phu phương bắc",
        "ipa": "/ɔːˈraɪɡə/"
    },
    "lex.en.100k.043487": {
        "hw": "backstairs",
        "pos": "adj",
        "vi": "lén lút mờ ám; luồn lọt cửa sau",
        "ipa": "/ˈbækˌstɛrz/"
    },
    "lex.en.100k.043488": {
        "hw": "benzedrine",
        "pos": "noun",
        "vi": "thuốc kích thần kinh benzedrin",
        "ipa": "/ˈbɛnzɪdriːn/"
    },
    "lex.en.100k.043489": {
        "hw": "bionomics",
        "pos": "noun",
        "vi": "khoa sinh thái học môi trường sống",
        "ipa": "/ˌbaɪəˈnɑːmɪks/"
    },
    "lex.en.100k.043490": {
        "hw": "bivalent",
        "pos": "adj",
        "vi": "mang hóa trị hai trong hóa học",
        "ipa": "/baɪˈveɪlənt/"
    },
    "lex.en.100k.043491": {
        "hw": "blackcap",
        "pos": "noun",
        "vi": "loài chim chích đầu đen châu Âu",
        "ipa": "/ˈblækˌkæp/"
    },
    "lex.en.100k.043492": {
        "hw": "bobwhite",
        "pos": "noun",
        "vi": "loài chim cút bobwhite châu Mỹ",
        "ipa": "/bɑːbˈwaɪt/"
    },
    "lex.en.100k.043493": {
        "hw": "bromus",
        "pos": "noun",
        "vi": "chi cỏ Bromus thức ăn gia súc",
        "ipa": "/ˈbroʊməs/"
    },
    "lex.en.100k.043494": {
        "hw": "bronchus",
        "pos": "noun",
        "vi": "ống phế quản dẫn khí vào phổi",
        "ipa": "/ˈbrɑːŋkəs/"
    },
    "lex.en.100k.043495": {
        "hw": "caelum",
        "pos": "noun",
        "vi": "chòm sao Điêu Cụ phương nam",
        "ipa": "/ˈsiːləm/"
    },
    "lex.en.100k.043496": {
        "hw": "caesura",
        "pos": "noun",
        "vi": "chỗ ngắt nhịp giữa dòng câu thơ",
        "ipa": "/sɪˈzjʊrə/"
    },
    "lex.en.100k.043497": {
        "hw": "capercaillie",
        "pos": "noun",
        "vi": "loài gà gô rừng phương bắc lớn",
        "ipa": "/ˌkæpɚˈkeɪlji/"
    },
    "lex.en.100k.043498": {
        "hw": "caracara",
        "pos": "noun",
        "vi": "loài chim ưng caracara Trung Nam Mỹ",
        "ipa": "/ˌkærəˈkɑːrə/"
    },
    "lex.en.100k.043499": {
        "hw": "careerism",
        "pos": "noun",
        "vi": "chủ nghĩa hám danh thực dụng",
        "ipa": "/kəˈrɪrɪzəm/"
    },
    "lex.en.100k.043500": {
        "hw": "carsick",
        "pos": "adj",
        "vi": "say xe hơi; nôn nao khó chịu",
        "ipa": "/ˈkɑːrsɪk/"
    },
    "lex.en.100k.043501": {
        "hw": "cascara",
        "pos": "noun",
        "vi": "vỏ cây cascara nhuận tràng",
        "ipa": "/kæsˈkærə/"
    }
}

ALL_OVERRIDES = {}
ALL_OVERRIDES.update(OVERRIDES_PART1)
ALL_OVERRIDES.update(OVERRIDES_PART2)
ALL_OVERRIDES.update(OVERRIDES_PART3)
ALL_OVERRIDES.update(OVERRIDES_PART4)
ALL_OVERRIDES.update(OVERRIDES_PART5)

print(f"Total overrides loaded: {len(ALL_OVERRIDES)}")

# Validate all overrides
VALID_POS = {"noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det"}
errors = []

for rec_id, ov in ALL_OVERRIDES.items():
    if len(ov["vi"]) > 35:
        errors.append(f"{rec_id}: vi length {len(ov['vi'])} > 35: '{ov['vi']}'")
    if ov["pos"] not in VALID_POS:
        errors.append(f"{rec_id}: invalid pos '{ov['pos']}'")
    if not (ov["ipa"].startswith("/") and ov["ipa"].endswith("/")):
        errors.append(f"{rec_id}: invalid ipa: '{ov['ipa']}'")

if errors:
    print(f"Validation FAILED with {len(errors)} errors:")
    for err in errors[:20]:
        print(f"  {err}")
    raise SystemExit(1)

# Apply to batch-09.json
BATCH_FILE = "content/english/qa-batches/batch-09.json"
with open(BATCH_FILE, "r", encoding="utf-8") as f:
    batch_data = json.load(f)

records = batch_data["records"]
applied_count = 0

for i in range(3000, 3500):
    r = records[i]
    r_id = r["id"]
    if r_id in ALL_OVERRIDES:
        ov = ALL_OVERRIDES[r_id]
        if r["hw"].lower() != ov["hw"].lower():
            print(f"Mismatch at index {i}: record hw '{r['hw']}' vs override hw '{ov['hw']}'")
            raise SystemExit(1)
        r["pos"] = ov["pos"]
        r["vi"] = ov["vi"]
        r["ipa"] = ov["ipa"]
        applied_count += 1
    else:
        print(f"Missing override for record index {i}: {r_id} {r['hw']}")
        raise SystemExit(1)

print(f"Successfully applied {applied_count} overrides to records 3000-3499.")

# Update reviewedCount
batch_data["reviewedCount"] = 3500
batch_data["status"] = "in_progress"

with open(BATCH_FILE, "w", encoding="utf-8") as f:
    json.dump(batch_data, f, ensure_ascii=False, indent=2)

print("Batch 09 updated: reviewedCount is now 3500.")
