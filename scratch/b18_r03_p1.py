# scratch/b18_r03_p1.py
# Batch 18 Round 3 Part 1: records 1000 - 1099 (IDs 086002 - 086101)
import json

data = [
    {
        "id": "lex.en.100k.086002",
        "hw": "immortalised",
        "pos": "verb",
        "ipa": "/ɪˈmɔːrtəlaɪzd/",
        "vi": "đã làm cho bất tử; đã lưu danh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086003",
        "hw": "immortalises",
        "pos": "verb",
        "ipa": "/ɪˈmɔːrtəlaɪzɪz/",
        "vi": "làm cho bất tử; lưu danh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086004",
        "hw": "immortalising",
        "pos": "verb",
        "ipa": "/ɪˈmɔːrtəlaɪzɪŋ/",
        "vi": "đang làm cho bất tử; đang lưu danh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086005",
        "hw": "immortalization",
        "pos": "noun",
        "ipa": "/ɪˌmɔːrtələˈzeɪʃən/",
        "vi": "sự làm cho bất tử; sự lưu danh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086006",
        "hw": "immortalizes",
        "pos": "verb",
        "ipa": "/ɪˈmɔːrtəlaɪzɪz/",
        "vi": "làm cho bất tử; lưu danh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086007",
        "hw": "immortalizing",
        "pos": "verb",
        "ipa": "/ɪˈmɔːrtəlaɪzɪŋ/",
        "vi": "đang làm cho bất tử; đang lưu danh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086008",
        "hw": "immortally",
        "pos": "adv",
        "ipa": "/ɪˈmɔːrtəli/",
        "vi": "một cách bất tử; muôn đời",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086009",
        "hw": "immortals",
        "pos": "noun",
        "ipa": "/ɪˈmɔːrtəlz/",
        "vi": "những bậc bất tử; các vị thần",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086010",
        "hw": "immortile",
        "pos": "adj",
        "ipa": "/ɪˈmoʊtəl/",
        "vi": "không di động được; bất động",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086011",
        "hw": "immotile",
        "pos": "adj",
        "ipa": "/ɪˈmoʊtəl/",
        "vi": "bất động; không di động",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086012",
        "hw": "immotility",
        "pos": "noun",
        "ipa": "/ˌɪmoʊˈtɪləti/",
        "vi": "tính bất động; không di chuyển",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086013",
        "hw": "immovability",
        "pos": "noun",
        "ipa": "/ɪˌmuːvəˈbɪlɪti/",
        "vi": "tính bất động; tính kiên định",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086014",
        "hw": "immovableness",
        "pos": "noun",
        "ipa": "/ɪˈmuːvəbəlnəs/",
        "vi": "sự bất động; tính kiên định",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086015",
        "hw": "immunises",
        "pos": "verb",
        "ipa": "/ˈɪmjənaɪzɪz/",
        "vi": "tiêm chủng; miễn dịch hóa",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086016",
        "hw": "immunising",
        "pos": "verb",
        "ipa": "/ˈɪmjənaɪzɪŋ/",
        "vi": "đang gây miễn dịch; đang tiêm chủng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086017",
        "hw": "immunizer",
        "pos": "noun",
        "ipa": "/ˈɪmjənaɪzər/",
        "vi": "chất gây miễn dịch; người tiêm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086018",
        "hw": "immunizes",
        "pos": "verb",
        "ipa": "/ˈɪmjənaɪzɪz/",
        "vi": "tiêm chủng; gây miễn dịch",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086019",
        "hw": "immunizing",
        "pos": "verb",
        "ipa": "/ˈɪmjənaɪzɪŋ/",
        "vi": "đang gây miễn dịch; đang tiêm phòng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086020",
        "hw": "immunoadsorbent",
        "pos": "noun",
        "ipa": "/ˌɪmjənoʊædˈsɔːrbənt/",
        "vi": "chất hấp phụ miễn dịch",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086021",
        "hw": "immunocompetence",
        "pos": "noun",
        "ipa": "/ˌɪmjənoʊˈkɑːmpɪtəns/",
        "vi": "khả năng đáp ứng miễn dịch",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086022",
        "hw": "immunoelectrophoresis",
        "pos": "noun",
        "ipa": "/ˌɪmjənoʊɪˌlɛktroʊfəˈriːsɪs/",
        "vi": "phương pháp điện di miễn dịch",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086023",
        "hw": "immunohaematology",
        "pos": "noun",
        "ipa": "/ˌɪmjənoʊˌhiːməˈtɑːlədʒi/",
        "vi": "huyết học miễn dịch",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086024",
        "hw": "immunosuppressor",
        "pos": "noun",
        "ipa": "/ˌɪmjənoʊsəˈprɛsər/",
        "vi": "thuốc ức chế miễn dịch",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086025",
        "hw": "immunothromboses",
        "pos": "noun",
        "ipa": "/ˌɪmjənoʊθrɑːmˈboʊsiːz/",
        "vi": "các chứng huyết khối miễn dịch",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086026",
        "hw": "immure",
        "pos": "verb",
        "ipa": "/ɪˈmjʊər/",
        "vi": "giam cầm; nhốt kỹ trong tường",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086027",
        "hw": "immurement",
        "pos": "noun",
        "ipa": "/ɪˈmjʊərmənt/",
        "vi": "sự giam cầm; sự giam hãm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086028",
        "hw": "immusical",
        "pos": "adj",
        "ipa": "/ɪˈmjuːzɪkəl/",
        "vi": "không có nhạc điệu; chói tai",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086029",
        "hw": "immutableness",
        "pos": "noun",
        "ipa": "/ɪˈmjuːtəbəlnəs/",
        "vi": "tính bất biến; sự không đổi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086030",
        "hw": "impactful",
        "pos": "adj",
        "ipa": "/ɪmˈpæktfəl/",
        "vi": "có tác động mạnh; gây ấn tượng sâu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086031",
        "hw": "impacting",
        "pos": "verb",
        "ipa": "/ɪmˈpæktɪŋ/",
        "vi": "đang va chạm; đang tác động mạnh",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086032",
        "hw": "impactive",
        "pos": "adj",
        "ipa": "/ɪmˈpæktɪv/",
        "vi": "mang tính va chạm; tạo xung lực",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086033",
        "hw": "impacts",
        "pos": "verb",
        "ipa": "/ɪmˈpækts/",
        "vi": "tác động; ảnh hưởng mạnh mẽ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086034",
        "hw": "impairable",
        "pos": "adj",
        "ipa": "/ɪmˈpɛrəbəl/",
        "vi": "có thể bị tổn hại; dễ suy yếu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086035",
        "hw": "impairer",
        "pos": "noun",
        "ipa": "/ɪmˈpɛrər/",
        "vi": "kẻ làm tổn hại; thứ gây suy yếu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086036",
        "hw": "impairing",
        "pos": "verb",
        "ipa": "/ɪmˈpɛrɪŋ/",
        "vi": "đang làm suy yếu; đang làm tổn hại",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086037",
        "hw": "impairs",
        "pos": "verb",
        "ipa": "/ɪmˈpɛrz/",
        "vi": "làm suy yếu; làm hư hại",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086038",
        "hw": "impaler",
        "pos": "noun",
        "ipa": "/ɪmˈpeɪlər/",
        "vi": "kẻ đâm cọc; kẻ xiên chết",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086039",
        "hw": "impalpability",
        "pos": "noun",
        "ipa": "/ɪmˌpælpəˈbɪlɪti/",
        "vi": "tính vô hình; sự khó nắm bắt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086040",
        "hw": "impalpably",
        "pos": "adv",
        "ipa": "/ɪmˈpælpəbli/",
        "vi": "một cách mơ hồ; khó nắm bắt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086041",
        "hw": "impaludism",
        "pos": "noun",
        "ipa": "/ɪmˈpæljədɪzəm/",
        "vi": "chứng nhiễm độc sốt rét",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086042",
        "hw": "impanelled",
        "pos": "verb",
        "ipa": "/ɪmˈpænəld/",
        "vi": "đã chọn vào ban bồi thẩm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086043",
        "hw": "impanelling",
        "pos": "verb",
        "ipa": "/ɪmˈpænəlɪŋ/",
        "vi": "đang chọn vào ban bồi thẩm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086044",
        "hw": "impanelment",
        "pos": "noun",
        "ipa": "/ɪmˈpænəlmənt/",
        "vi": "sự lập danh sách bồi thẩm đoàn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086045",
        "hw": "impanels",
        "pos": "verb",
        "ipa": "/ɪmˈpænəlz/",
        "vi": "chọn vào ban bồi thẩm",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086046",
        "hw": "imparadise",
        "pos": "verb",
        "ipa": "/ɪmˈpærədaɪs/",
        "vi": "đưa lên cõi tiên; làm cực lạc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086047",
        "hw": "imparipinnate",
        "pos": "adj",
        "ipa": "/ɪmˌpærɪˈpɪneɪt/",
        "vi": "kép lông chim lẻ (lá cây)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086048",
        "hw": "imparisyllabic",
        "pos": "adj",
        "ipa": "/ɪmˌpærɪsɪˈlæbɪk/",
        "vi": "khác số âm tiết khi biến cách",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086049",
        "hw": "imparity",
        "pos": "noun",
        "ipa": "/ɪmˈpærɪti/",
        "vi": "sự bất bình đẳng; sự so le",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086050",
        "hw": "impark",
        "pos": "verb",
        "ipa": "/ɪmˈpɑːrk/",
        "vi": "rào bãi chăn thả; giữ thú rừng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086051",
        "hw": "imparkation",
        "pos": "noun",
        "ipa": "/ˌɪmpɑːrˈkeɪʃən/",
        "vi": "sự rào bãi chăn nuôi; bãi bảo tồn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086052",
        "hw": "impartable",
        "pos": "adj",
        "ipa": "/ɪmˈpɑːrtəbəl/",
        "vi": "có thể truyền đạt; có thể chia sẻ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086053",
        "hw": "imparted",
        "pos": "verb",
        "ipa": "/ɪmˈpɑːrtɪd/",
        "vi": "đã truyền đạt; đã truyền thụ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086054",
        "hw": "impartialness",
        "pos": "noun",
        "ipa": "/ɪmˈpɑːrʃəlnəs/",
        "vi": "tính chí công vô tư; sự vô tư",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086055",
        "hw": "impartibility",
        "pos": "noun",
        "ipa": "/ɪmˌpɑːrtəˈbɪlɪti/",
        "vi": "tính không thể chia cắt tài sản",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086056",
        "hw": "impartible",
        "pos": "adj",
        "ipa": "/ɪmˈpɑːrtəbəl/",
        "vi": "không thể chia cắt (thừa kế)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086057",
        "hw": "impartibly",
        "pos": "adv",
        "ipa": "/ɪmˈpɑːrtəbli/",
        "vi": "một cách không thể phân chia",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086058",
        "hw": "impartment",
        "pos": "noun",
        "ipa": "/ɪmˈpɑːrtmənt/",
        "vi": "sự truyền đạt; điều tiết lộ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086059",
        "hw": "imparts",
        "pos": "verb",
        "ipa": "/ɪmˈpɑːrts/",
        "vi": "truyền đạt; đem lại cho",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086060",
        "hw": "impassability",
        "pos": "noun",
        "ipa": "/ɪmˌpæsəˈbɪlɪti/",
        "vi": "tính không thể vượt qua",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086061",
        "hw": "impassableness",
        "pos": "noun",
        "ipa": "/ɪmˈpæsəbəlnəs/",
        "vi": "tình trạng tắc nghẽn; hiểm trở",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086062",
        "hw": "impassably",
        "pos": "adv",
        "ipa": "/ɪmˈpæsəbli/",
        "vi": "đến mức không thể đi qua",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086063",
        "hw": "impassibility",
        "pos": "noun",
        "ipa": "/ɪmˌpæsəˈbɪlɪti/",
        "vi": "tính miễn nhiễm đau đớn; tính trơ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086064",
        "hw": "impassible",
        "pos": "adj",
        "ipa": "/ɪmˈpæsəbəl/",
        "vi": "không cảm thấy đau; trơ trơ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086065",
        "hw": "impassibleness",
        "pos": "noun",
        "ipa": "/ɪmˈpæsəbəlnəs/",
        "vi": "sự vô cảm; tính trơ trước nỗi đau",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086066",
        "hw": "impassibly",
        "pos": "adv",
        "ipa": "/ɪmˈpæsəbli/",
        "vi": "một cách vô cảm; trơ trơ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086067",
        "hw": "impassion",
        "pos": "verb",
        "ipa": "/ɪmˈpæʃən/",
        "vi": "khơi gợi say mê; làm xúc động",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086068",
        "hw": "impassionedness",
        "pos": "noun",
        "ipa": "/ɪmˈpæʃəndnəs/",
        "vi": "sự nồng nhiệt; lòng say mê",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086069",
        "hw": "impassiveness",
        "pos": "noun",
        "ipa": "/ɪmˈpæsɪvnəs/",
        "vi": "sự điềm tĩnh; vẻ vô cảm lạnh lùng",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086070",
        "hw": "impastation",
        "pos": "noun",
        "ipa": "/ˌɪmpæˈsteɪʃən/",
        "vi": "kỹ thuật đắp màu vẽ dày",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086071",
        "hw": "impaste",
        "pos": "verb",
        "ipa": "/ɪmˈpeɪst/",
        "vi": "đắp sơn dầu dày cộm; nhào bột",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086072",
        "hw": "impastoed",
        "pos": "adj",
        "ipa": "/ɪmˈpæstoʊd/",
        "vi": "được đắp màu dày cộm (tranh vẽ)",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086073",
        "hw": "impatiens",
        "pos": "noun",
        "ipa": "/ɪmˈpeɪʃənz/",
        "vi": "cây bóng nước; hoa móng tay",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086074",
        "hw": "impatientness",
        "pos": "noun",
        "ipa": "/ɪmˈpeɪʃəntnəs/",
        "vi": "sự nôn nóng; tính thiếu kiên nhẫn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086075",
        "hw": "impawn",
        "pos": "verb",
        "ipa": "/ɪmˈpɔːn/",
        "vi": "cầm cố; thế chấp tài sản",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086076",
        "hw": "impeachability",
        "pos": "noun",
        "ipa": "/ɪmˌpiːtʃəˈbɪlɪti/",
        "vi": "khả năng có thể bị luận tội",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086077",
        "hw": "impeachable",
        "pos": "adj",
        "ipa": "/ɪmˈpiːtʃəbəl/",
        "vi": "đáng bị luận tội; đáng ngờ vực",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086078",
        "hw": "impeached",
        "pos": "verb",
        "ipa": "/ɪmˈpiːtʃt/",
        "vi": "đã luận tội; đã đàn hặc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086079",
        "hw": "impeacher",
        "pos": "noun",
        "ipa": "/ɪmˈpiːtʃər/",
        "vi": "người tố cáo; người luận tội",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086080",
        "hw": "impeaches",
        "pos": "verb",
        "ipa": "/ɪmˈpiːtʃɪz/",
        "vi": "luận tội; đàn hặc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086081",
        "hw": "impeaching",
        "pos": "verb",
        "ipa": "/ɪmˈpiːtʃɪŋ/",
        "vi": "đang luận tội; việc đàn hặc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086082",
        "hw": "impearl",
        "pos": "verb",
        "ipa": "/ɪmˈpɜːrl/",
        "vi": "kết thành ngọc; phủ sương như ngọc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086083",
        "hw": "impeccableness",
        "pos": "noun",
        "ipa": "/ɪmˈpɛkəbəlnəs/",
        "vi": "sự hoàn hảo; tính không tì vết",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086084",
        "hw": "impeccance",
        "pos": "noun",
        "ipa": "/ɪmˈpɛkəns/",
        "vi": "sự vô tội; sự không vướng tội lỗi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086085",
        "hw": "impeccancy",
        "pos": "noun",
        "ipa": "/ɪmˈpɛkənsi/",
        "vi": "tính vô tội; không vướng tội lỗi",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086086",
        "hw": "impeccant",
        "pos": "adj",
        "ipa": "/ɪmˈpɛkənt/",
        "vi": "vô tội; không vướng tì vết",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086087",
        "hw": "impecuniosity",
        "pos": "noun",
        "ipa": "/ˌɪmpɪˌkjuːniˈɑːsəti/",
        "vi": "cảnh bần hàn; tình trạng túng thiếu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086088",
        "hw": "impecuniously",
        "pos": "adv",
        "ipa": "/ˌɪmpɪˈkjuːniəsli/",
        "vi": "trong cảnh túng thiếu; nghèo khó",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086089",
        "hw": "impecuniousness",
        "pos": "noun",
        "ipa": "/ˌɪmpɪˈkjuːniəsnəs/",
        "vi": "cảnh túng quẫn; sự thiếu tiền bạc",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086090",
        "hw": "impeder",
        "pos": "noun",
        "ipa": "/ɪmˈpiːdər/",
        "vi": "kẻ ngáng đường; vật cản trở",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086091",
        "hw": "impedes",
        "pos": "verb",
        "ipa": "/ɪmˈpiːdz/",
        "vi": "cản trở; làm ngưng trệ",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086092",
        "hw": "impedient",
        "pos": "adj",
        "ipa": "/ɪmˈpiːdiənt/",
        "vi": "gây trở ngại; mang tính cản trở",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086093",
        "hw": "impedimental",
        "pos": "adj",
        "ipa": "/ɪmˌpɛdɪˈmɛntəl/",
        "vi": "mang tính cản trở; ngáng đường",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086094",
        "hw": "impedimentary",
        "pos": "adj",
        "ipa": "/ɪmˌpɛdɪˈmɛntəri/",
        "vi": "gây vướng víu; gây trở ngại",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086095",
        "hw": "impedingly",
        "pos": "adv",
        "ipa": "/ɪmˈpiːdɪŋli/",
        "vi": "một cách gây cản trở; vướng víu",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086096",
        "hw": "impeditive",
        "pos": "adj",
        "ipa": "/ɪmˈpɛdɪtɪv/",
        "vi": "có xu hướng cản trở; làm nghẽn",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086097",
        "hw": "impellent",
        "pos": "adj",
        "ipa": "/ɪmˈpɛlənt/",
        "vi": "thôi thúc; đẩy mạnh về phía trước",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086098",
        "hw": "impels",
        "pos": "verb",
        "ipa": "/ɪmˈpɛlz/",
        "vi": "thúc đẩy; thôi thúc mãnh liệt",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086099",
        "hw": "impend",
        "pos": "verb",
        "ipa": "/ɪmˈpɛnd/",
        "vi": "sắp xảy ra; lơ lửng đe dọa",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086100",
        "hw": "impended",
        "pos": "verb",
        "ipa": "/ɪmˈpɛndɪd/",
        "vi": "đã treo lơ lửng; đã chực xảy ra",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    },
    {
        "id": "lex.en.100k.086101",
        "hw": "impendence",
        "pos": "noun",
        "ipa": "/ɪmˈpɛndəns/",
        "vi": "sự lơ lửng; mối đe dọa cận kề",
        "cefr": "C2",
        "tier": "expanded",
        "status": "reviewed",
        "notes": ""
    }
]

if __name__ == "__main__":
    assert len(data) == 100, f"Expected 100, got {len(data)}"
    with open("scratch/b18_r03_raw_p1.json") as f:
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
    print("ALL 100 RECORDS IN ROUND 3 PART 1 VERIFIED SUCCESSFULLY!")
