# scratch/b18_r02_p5.py
# Batch 18 Round 2 Part 5: records 900 - 999 (IDs 085902 - 086001)
import json

data = [
    {
        "id": "lex.en.100k.085902",
        "hw": "imamate",
        "pos": "noun",
        "ipa": "/ɪˈmɑːmət/",
        "vi": "chức vị imam; lãnh thổ imam",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085903",
        "hw": "imaret",
        "pos": "noun",
        "ipa": "/ɪˈmɑːrət/",
        "vi": "quán trọ tế bần Thổ Nhĩ Kỳ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085904",
        "hw": "imaum",
        "pos": "noun",
        "ipa": "/ɪˈmɑːm/",
        "vi": "giáo sĩ Hồi giáo; giáo trưởng imam",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085905",
        "hw": "imavate",
        "pos": "noun",
        "ipa": "/ˈɪməveɪt/",
        "vi": "muối imavat (hóa học)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085906",
        "hw": "imbark",
        "pos": "verb",
        "ipa": "/ɪmˈbɑːrk/",
        "vi": "lên tàu; bắt tay vào việc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085907",
        "hw": "imbauba",
        "pos": "noun",
        "ipa": "/ɪmˈbaʊbə/",
        "vi": "cây imbauba (thực vật)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085908",
        "hw": "imbecilely",
        "pos": "adv",
        "ipa": "/ˈɪmbəsɪlli/",
        "vi": "một cách ngốc nghếch; khờ khạo",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085909",
        "hw": "imbedding",
        "pos": "noun",
        "ipa": "/ɪmˈbɛdɪŋ/",
        "vi": "sự gắn chặt; sự nhúng sâu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085910",
        "hw": "imbiber",
        "pos": "noun",
        "ipa": "/ɪmˈbaɪbər/",
        "vi": "người uống rượu; người tiếp thu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085911",
        "hw": "imbibitional",
        "pos": "adj",
        "ipa": "/ˌɪmbɪˈbɪʃənəl/",
        "vi": "(thuộc) sự thấm hút nước",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085912",
        "hw": "imbitter",
        "pos": "verb",
        "ipa": "/ɪmˈbɪtər/",
        "vi": "làm cay đắng; làm chua xót",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085913",
        "hw": "imbody",
        "pos": "verb",
        "ipa": "/ɪmˈbɑːdi/",
        "vi": "hiện thân; bao gồm; thể hiện",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085914",
        "hw": "imbosom",
        "pos": "verb",
        "ipa": "/ɪmˈbʊzəm/",
        "vi": "ôm vào lòng; che chở yêu thương",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085915",
        "hw": "imbower",
        "pos": "verb",
        "ipa": "/ɪmˈbaʊər/",
        "vi": "che rợp bóng cây; vây quanh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085916",
        "hw": "imbrication",
        "pos": "noun",
        "ipa": "/ˌɪmbrɪˈkeɪʃən/",
        "vi": "sự xếp lợp vảy; gối mép lên nhau",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085917",
        "hw": "imbricative",
        "pos": "adj",
        "ipa": "/ˈɪmbrɪkətɪv/",
        "vi": "xếp lợp vảy; gối mép lên nhau",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085918",
        "hw": "imbrown",
        "pos": "verb",
        "ipa": "/ɪmˈbraʊn/",
        "vi": "làm sạm nâu; nhuộm nâu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085919",
        "hw": "imbrue",
        "pos": "verb",
        "ipa": "/ɪmˈbruː/",
        "vi": "vấy máu; làm thấm đẫm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085920",
        "hw": "imbruement",
        "pos": "noun",
        "ipa": "/ɪmˈbruːmənt/",
        "vi": "sự vấy máu; sự làm ướt đẫm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085921",
        "hw": "imbrute",
        "pos": "verb",
        "ipa": "/ɪmˈbruːt/",
        "vi": "hóa thành thú tính; làm tàn bạo",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085922",
        "hw": "imbrutement",
        "pos": "noun",
        "ipa": "/ɪmˈbruːtmənt/",
        "vi": "sự thú hóa; tính tàn bạo dã man",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085923",
        "hw": "imbued",
        "pos": "verb",
        "ipa": "/ɪmˈbjuːd/",
        "vi": "đã thấm nhuần; đã thấm đượm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085924",
        "hw": "imbuement",
        "pos": "noun",
        "ipa": "/ɪmˈbjuːmənt/",
        "vi": "sự thấm nhuần; sự tiêm nhiễm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085925",
        "hw": "imbues",
        "pos": "verb",
        "ipa": "/ɪmˈbjuːz/",
        "vi": "thấm nhuần; làm tràn ngập",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085926",
        "hw": "imbuing",
        "pos": "verb",
        "ipa": "/ɪmˈbjuːɪŋ/",
        "vi": "đang thấm nhuần; làm thấm đượm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085927",
        "hw": "imexplorable",
        "pos": "adj",
        "ipa": "/ˌɪmɪkˈsplɔːrəbəl/",
        "vi": "không thể khám phá; khôn dò",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085928",
        "hw": "imidazoles",
        "pos": "noun",
        "ipa": "/ˌɪmɪˈdæzoʊlz/",
        "vi": "các hợp chất imidazol (hóa học)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085929",
        "hw": "imidic",
        "pos": "adj",
        "ipa": "/ɪˈmɪdɪk/",
        "vi": "(thuộc) nhóm imit; gốc imit",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085930",
        "hw": "iminazole",
        "pos": "noun",
        "ipa": "/ɪˈmɪnəzoʊl/",
        "vi": "hợp chất iminazol (hóa học)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085931",
        "hw": "imitability",
        "pos": "noun",
        "ipa": "/ˌɪmɪtəˈbɪlɪti/",
        "vi": "khả năng có thể bắt chước",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085932",
        "hw": "imitable",
        "pos": "adj",
        "ipa": "/ˈɪmɪtəbəl/",
        "vi": "có thể bắt chước; noi theo được",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085933",
        "hw": "imitableness",
        "pos": "noun",
        "ipa": "/ˈɪmɪtəbəlnəs/",
        "vi": "tính có thể noi gương bắt chước",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085934",
        "hw": "imitated",
        "pos": "verb",
        "ipa": "/ˈɪmɪteɪtɪd/",
        "vi": "đã bắt chước; đã mô phỏng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085935",
        "hw": "imitates",
        "pos": "verb",
        "ipa": "/ˈɪmɪteɪts/",
        "vi": "bắt chước; mô phỏng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085936",
        "hw": "imitating",
        "pos": "verb",
        "ipa": "/ˈɪmɪteɪtɪŋ/",
        "vi": "đang bắt chước; đang mô phỏng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085937",
        "hw": "imitational",
        "pos": "adj",
        "ipa": "/ˌɪmɪˈteɪʃənəl/",
        "vi": "mang tính bắt chước; mô phỏng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085938",
        "hw": "imitatively",
        "pos": "adv",
        "ipa": "/ˈɪmɪtətɪvli/",
        "vi": "theo lối bắt chước; mô phỏng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085939",
        "hw": "imitativeness",
        "pos": "noun",
        "ipa": "/ˈɪmɪtətɪvnəs/",
        "vi": "tính hay bắt chước; tính mô phỏng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085940",
        "hw": "immaculacy",
        "pos": "noun",
        "ipa": "/ɪˈmækjələsi/",
        "vi": "sự tinh khiết; tính không tì vết",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085941",
        "hw": "immaculateness",
        "pos": "noun",
        "ipa": "/ɪˈmækjələtnəs/",
        "vi": "sự tinh khiết; vẻ không tì vết",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085942",
        "hw": "immanency",
        "pos": "noun",
        "ipa": "/ˈɪmənənsi/",
        "vi": "tính nội tại; sự gắn liền bên trong",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085943",
        "hw": "immanently",
        "pos": "adv",
        "ipa": "/ˈɪmənəntli/",
        "vi": "một cách nội tại; vốn có từ trong",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085944",
        "hw": "immaterialise",
        "pos": "verb",
        "ipa": "/ˌɪməˈtɪriəlaɪz/",
        "vi": "phi vật chất hóa; làm tan biến",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085945",
        "hw": "immaterialism",
        "pos": "noun",
        "ipa": "/ˌɪməˈtɪriəlɪzəm/",
        "vi": "thuyết phi vật chất (triết học)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085946",
        "hw": "immaterialist",
        "pos": "noun",
        "ipa": "/ˌɪməˈtɪriəlɪst/",
        "vi": "người theo thuyết phi vật chất",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085947",
        "hw": "immaterialize",
        "pos": "verb",
        "ipa": "/ˌɪməˈtɪriəlaɪz/",
        "vi": "phi vật chất hóa; làm tan biến",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085948",
        "hw": "immaterially",
        "pos": "adv",
        "ipa": "/ˌɪməˈtɪriəli/",
        "vi": "một cách không đáng kể; vô hình",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085949",
        "hw": "immaterialness",
        "pos": "noun",
        "ipa": "/ˌɪməˈtɪriəlnəs/",
        "vi": "tính phi vật chất; sự không can hệ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085950",
        "hw": "immatureness",
        "pos": "noun",
        "ipa": "/ˌɪmməˈtjʊərnəs/",
        "vi": "sự non nớt; tính chưa trưởng thành",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085951",
        "hw": "immeasurability",
        "pos": "noun",
        "ipa": "/ɪˌmɛʒərəˈbɪlɪti/",
        "vi": "tính khôn lường; sự vô hạn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085952",
        "hw": "immeasurableness",
        "pos": "noun",
        "ipa": "/ɪˈmɛʒərəbəlnəs/",
        "vi": "sự vô biên; tính không đo đếm được",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085953",
        "hw": "immediateness",
        "pos": "noun",
        "ipa": "/ɪˈmiːdiətnəs/",
        "vi": "tính tức thời; sự trực tiếp",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085954",
        "hw": "immediatism",
        "pos": "noun",
        "ipa": "/ɪˈmiːdiətɪzəm/",
        "vi": "chủ trương bãi nô ngay lập tức",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085955",
        "hw": "immediatist",
        "pos": "noun",
        "ipa": "/ɪˈmiːdiətɪst/",
        "vi": "người chủ trương bãi nô tức khắc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085956",
        "hw": "immedicable",
        "pos": "adj",
        "ipa": "/ɪˈmɛdɪkəbəl/",
        "vi": "vô phương cứu chữa; nan y",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085957",
        "hw": "immedicacble",
        "pos": "adj",
        "ipa": "/ɪˈmɛdɪkəbəl/",
        "vi": "vô phương cứu chữa; nan y",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085958",
        "hw": "immemorially",
        "pos": "adv",
        "ipa": "/ˌɪmməˈmɔːriəli/",
        "vi": "từ thời xa xưa; từ thuở ngút ngàn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085959",
        "hw": "immenseness",
        "pos": "noun",
        "ipa": "/ɪˈmɛnsnəs/",
        "vi": "sự bao la; tính vô cùng vô tận",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085960",
        "hw": "immensurability",
        "pos": "noun",
        "ipa": "/ɪˌmɛnʃərəˈbɪlɪti/",
        "vi": "tính không đo đếm được; vô lượng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085961",
        "hw": "immensurable",
        "pos": "adj",
        "ipa": "/ɪˈmɛnʃərəbəl/",
        "vi": "không thể đo lường; vô lượng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085962",
        "hw": "immensurableness",
        "pos": "noun",
        "ipa": "/ɪˈmɛnʃərəbəlnəs/",
        "vi": "tính vô lượng; sự khôn lường",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085963",
        "hw": "immerge",
        "pos": "verb",
        "ipa": "/ɪˈmɜːrdʒ/",
        "vi": "nhấn chìm; lặn biến vào bóng tối",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085964",
        "hw": "immergence",
        "pos": "noun",
        "ipa": "/ɪˈmɜːrdʒəns/",
        "vi": "sự chìm ngập; sự ẩn mình biến mất",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085965",
        "hw": "immersed",
        "pos": "verb",
        "ipa": "/ɪˈmɜːrst/",
        "vi": "đã nhúng ngập; đã đắm mình vào",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085966",
        "hw": "immerses",
        "pos": "verb",
        "ipa": "/ɪˈmɜːrsɪz/",
        "vi": "nhúng ngập; đắm chìm vào",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085967",
        "hw": "immersible",
        "pos": "adj",
        "ipa": "/ɪˈmɜːrsəbəl/",
        "vi": "có thể ngâm nước; chìm dưới nước",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085968",
        "hw": "immersing",
        "pos": "verb",
        "ipa": "/ɪˈmɜːrsɪŋ/",
        "vi": "đang nhúng ngập; đang đắm mình",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085969",
        "hw": "immesh",
        "pos": "verb",
        "ipa": "/ɪˈmɛʃ/",
        "vi": "bủa lưới; làm vướng vào bẫy",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085970",
        "hw": "immigrated",
        "pos": "verb",
        "ipa": "/ˈɪmɪɡreɪtɪd/",
        "vi": "đã nhập cư; đã chuyển đến định cư",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085971",
        "hw": "immigrates",
        "pos": "verb",
        "ipa": "/ˈɪmɪɡreɪts/",
        "vi": "nhập cư; vào định cư",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085972",
        "hw": "immigrating",
        "pos": "verb",
        "ipa": "/ˈɪmɪɡreɪtɪŋ/",
        "vi": "đang nhập cư; đang đến định cư",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085973",
        "hw": "imminency",
        "pos": "noun",
        "ipa": "/ˈɪmɪnənsi/",
        "vi": "sự cận kề; tính cấp bách",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085974",
        "hw": "imminentness",
        "pos": "noun",
        "ipa": "/ˈɪmɪnəntnəs/",
        "vi": "sự cận kề; điều sắp xảy đến",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085975",
        "hw": "immingle",
        "pos": "verb",
        "ipa": "/ɪˈmɪŋɡəl/",
        "vi": "hòa lẫn; trộn lẫn vào nhau",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085976",
        "hw": "immiscibility",
        "pos": "noun",
        "ipa": "/ˌɪmɪsəˈbɪlɪti/",
        "vi": "tính không hòa tan lẫn nhau",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085977",
        "hw": "immiscibly",
        "pos": "adv",
        "ipa": "/ɪˈmɪsəbli/",
        "vi": "không hòa lẫn vào nhau",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085978",
        "hw": "immitigability",
        "pos": "noun",
        "ipa": "/ɪˌmɪtɪɡəˈbɪlɪti/",
        "vi": "tính không thể xoa dịu; cay độc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085979",
        "hw": "immitigable",
        "pos": "adj",
        "ipa": "/ɪˈmɪtɪɡəbəl/",
        "vi": "không thể xoa dịu; khôn nguôi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085980",
        "hw": "immitigableness",
        "pos": "noun",
        "ipa": "/ɪˈmɪtɪɡəbəlnəs/",
        "vi": "tính không thể làm nguôi bớt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085981",
        "hw": "immitigably",
        "pos": "adv",
        "ipa": "/ɪˈmɪtɪɡəbli/",
        "vi": "một cách không thể xoa dịu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085982",
        "hw": "immittance",
        "pos": "noun",
        "ipa": "/ɪˈmɪtəns/",
        "vi": "trở kháng tổng quát (điện tử)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085983",
        "hw": "immix",
        "pos": "verb",
        "ipa": "/ɪˈmɪks/",
        "vi": "trộn lẫn; hòa quyện",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085984",
        "hw": "immixture",
        "pos": "noun",
        "ipa": "/ɪˈmɪkstʃər/",
        "vi": "sự pha trộn; hỗn hợp trộn lẫn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085985",
        "hw": "immobilised",
        "pos": "verb",
        "ipa": "/ɪˈmoʊbəlaɪzd/",
        "vi": "đã làm bất động; đã giữ cố định",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085986",
        "hw": "immobilises",
        "pos": "verb",
        "ipa": "/ɪˈmoʊbəlaɪzɪz/",
        "vi": "làm bất động; giữ cố định",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085987",
        "hw": "immobilising",
        "pos": "verb",
        "ipa": "/ɪˈmoʊbəlaɪzɪŋ/",
        "vi": "đang làm bất động; đang cố định",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085988",
        "hw": "immobilized",
        "pos": "verb",
        "ipa": "/ɪˈmoʊbəlaɪzd/",
        "vi": "đã làm bất động; đã giữ cố định",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085989",
        "hw": "immobilizer",
        "pos": "noun",
        "ipa": "/ɪˈmoʊbəlaɪzər/",
        "vi": "khóa chống trộm xe; nẹp cố định",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085990",
        "hw": "immobilizes",
        "pos": "verb",
        "ipa": "/ɪˈmoʊbəlaɪzɪz/",
        "vi": "làm bất động; giữ cố định",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085991",
        "hw": "immoderateness",
        "pos": "noun",
        "ipa": "/ɪˈmɑːdərɪtnəs/",
        "vi": "tính thái quá; sự thiếu chừng mực",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085992",
        "hw": "immoderation",
        "pos": "noun",
        "ipa": "/ˌɪmmɑːdəˈreɪʃən/",
        "vi": "sự thái quá; tính vô độ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085993",
        "hw": "immolated",
        "pos": "verb",
        "ipa": "/ˈɪməleɪtɪd/",
        "vi": "đã hiến tế; đã làm vật tế thần",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085994",
        "hw": "immolates",
        "pos": "verb",
        "ipa": "/ˈɪməleɪts/",
        "vi": "hiến tế; thiêu làm vật tế",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085995",
        "hw": "immolating",
        "pos": "verb",
        "ipa": "/ˈɪməleɪtɪŋ/",
        "vi": "đang hiến tế; đang thiêu sống",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085996",
        "hw": "immolator",
        "pos": "noun",
        "ipa": "/ˈɪməleɪtər/",
        "vi": "người làm lễ hiến tế",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085997",
        "hw": "immoralise",
        "pos": "verb",
        "ipa": "/ɪˈmɔːrəlaɪz/",
        "vi": "làm hư đốn; đồi bại hóa",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085998",
        "hw": "immoralism",
        "pos": "noun",
        "ipa": "/ɪˈmɔːrəlɪzəm/",
        "vi": "thuyết vô luân; thuyết bài đạo đức",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.085999",
        "hw": "immoralist",
        "pos": "noun",
        "ipa": "/ɪˈmɔːrəlɪst/",
        "vi": "người theo chủ nghĩa phi luân",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086000",
        "hw": "immoralize",
        "pos": "verb",
        "ipa": "/ɪˈmɔːrəlaɪz/",
        "vi": "làm hư đốn; làm tha hóa đạo đức",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086001",
        "hw": "immortalisation",
        "pos": "noun",
        "ipa": "/ɪˌmɔːrtəlaɪˈzeɪʃən/",
        "vi": "sự làm cho bất tử; sự lưu danh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    }
]

if __name__ == "__main__":
    assert len(data) == 100, f"Expected 100, got {len(data)}"
    with open("scratch/b18_r02_raw_p5.json") as f:
        raw = json.load(f)
    assert len(raw) == 100, f"Expected 100 raw, got {len(raw)}"
    for i in range(100):
        d = data[i]
        r = raw[i]
        assert d["id"] == r["id"], f"ID mismatch at {i}: {d['id']} vs {r['id']}"
        assert d["hw"] == r["hw"], f"HW mismatch at {i}: {d['hw']} vs {r['hw']}"
        assert d["cefr"] == r["cefr"], f"CEFR mismatch at {i}: {d['cefr']} vs {r['cefr']}"
        assert d["tier"] == r["tier"], f"TIER mismatch at {i}: {d['tier']} vs {r['tier']}"
        assert d["notes"] == r["notes"], f"NOTES mismatch at {i}: {d['notes']} vs {r['notes']}"
        assert d["status"] == "reviewed", f"Status not reviewed at {i}"
        assert d["ipa"].startswith("/") and d["ipa"].endswith("/") and d["ipa"].count("/") == 2, f"Bad IPA at {i}: {d['ipa']}"
        assert len(d["vi"]) <= 35, f"VI too long at {i} ({len(d['vi'])}): {d['vi']}"
        assert d["pos"] in ["noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det"], f"Invalid pos at {i}: {d['pos']}"
    print("ALL 100 RECORDS IN PART 5 VERIFIED SUCCESSFULLY!")
