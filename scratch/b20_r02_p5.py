import json

part5_data = [
  {"id": "lex.en.100k.095902", "hw": "nonelective", "pos": "adj", "ipa": "/ˌnɑnɪˈlɛktɪv/", "vi": "không qua bầu cử; bổ nhiệm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095903", "hw": "nonenterprising", "pos": "adj", "ipa": "/ˌnɑnˈɛntɚpraɪzɪŋ/", "vi": "thiếu dám nghĩ dám làm; thụ động", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095904", "hw": "nonenzymatic", "pos": "adj", "ipa": "/ˌnɑnˌɛnzaɪˈmætɪk/", "vi": "phi enzym; không dùng enzym", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095905", "hw": "nonequivalence", "pos": "noun", "ipa": "/ˌnɑnɪˈkwɪvələns/", "vi": "sự không tương đương; bất đẳng thế", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095906", "hw": "nonequivalent", "pos": "adj", "ipa": "/ˌnɑnɪˈkwɪvələnt/", "vi": "không tương đương; bất tương đương", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095907", "hw": "nonexplorative", "pos": "adj", "ipa": "/ˌnɑnɪkˈsplɔːrətɪv/", "vi": "không thăm dò; không khám phá", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095908", "hw": "nonexploratory", "pos": "adj", "ipa": "/ˌnɑnɪkˈsplɔːrətɔːri/", "vi": "không nhằm thám hiểm; không thăm dò", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095909", "hw": "nonexplosive", "pos": "adj", "ipa": "/ˌnɑnɪkˈsploʊsɪv/", "vi": "không gây nổ; không phát nổ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095910", "hw": "nonextant", "pos": "adj", "ipa": "/ˌnɑnɛkˈstænt/", "vi": "không còn tồn tại; đã thất truyền", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095911", "hw": "nonextensile", "pos": "adj", "ipa": "/ˌnɑnɪkˈstɛnsəl/", "vi": "không giãn nở; không kéo dài được", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095912", "hw": "nonfigurative", "pos": "adj", "ipa": "/ˌnɑnˈfɪɡjərətɪv/", "vi": "phi hình thể; trừu tượng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095913", "hw": "nonfissile", "pos": "adj", "ipa": "/ˌnɑnˈfɪsəl/", "vi": "không phân hạch; không tách lớp", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095914", "hw": "nonfissionable", "pos": "adj", "ipa": "/ˌnɑnˈfɪʃənəbəl/", "vi": "không thể phân hạch hạt nhân", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095915", "hw": "nonflavored", "pos": "adj", "ipa": "/ˌnɑnˈfleɪvɚd/", "vi": "không thêm hương vị; tự nhiên", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095916", "hw": "nonflavoured", "pos": "adj", "ipa": "/ˌnɑnˈfleɪvɚd/", "vi": "không thêm hương liệu; không vị", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095917", "hw": "nonflowering", "pos": "adj", "ipa": "/ˌnɑnˈflaʊərɪŋ/", "vi": "không hoa; không nở hoa", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095918", "hw": "nonglutinous", "pos": "adj", "ipa": "/ˌnɑnˈɡluːtənəs/", "vi": "không dính; không có chất nhớt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095919", "hw": "nongranular", "pos": "adj", "ipa": "/ˌnɑnˈɡrænjəlɚ/", "vi": "không dạng hạt; mịn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095920", "hw": "nongregarious", "pos": "adj", "ipa": "/ˌnɑnɡrɪˈɡɛriəs/", "vi": "sống đơn độc; không theo bầy đàn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095921", "hw": "nonhairy", "pos": "adj", "ipa": "/ˌnɑnˈhɛri/", "vi": "không có lông; nhẵn nhụi", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095922", "hw": "nonharmonic", "pos": "adj", "ipa": "/ˌnɑnhɑːrˈmɑːnɪk/", "vi": "phi điều hòa; không hòa âm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095923", "hw": "nonhereditary", "pos": "adj", "ipa": "/ˌnɑnhəˈrɛdəˌtɛri/", "vi": "không di truyền; không thế tập", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095924", "hw": "nonheritable", "pos": "adj", "ipa": "/ˌnɑnˈhɛrɪtəbəl/", "vi": "không thể di truyền; phi thừa kế", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095925", "hw": "nonhierarchic", "pos": "adj", "ipa": "/ˌnɑnˌhaɪəˈrɑːrkɪk/", "vi": "phi đẳng cấp; không phân thứ bậc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095926", "hw": "nonhierarchical", "pos": "adj", "ipa": "/ˌnɑnˌhaɪəˈrɑːrkɪkəl/", "vi": "phi phân cấp bậc; bình đẳng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095927", "hw": "nonillion", "pos": "num", "ipa": "/noʊˈnɪljən/", "vi": "một nonillion; 10 mũ 30 hoặc 54", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095928", "hw": "nonimitative", "pos": "adj", "ipa": "/ˌnɑnˈɪmɪteɪtɪv/", "vi": "không bắt chước; có tính nguyên bản", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095929", "hw": "nonimmune", "pos": "adj", "ipa": "/ˌnɑnɪˈmjuːn/", "vi": "không miễn dịch; không miễn nhiễm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095930", "hw": "nonindulgence", "pos": "noun", "ipa": "/ˌnɑnɪnˈdʌldʒəns/", "vi": "sự không nuông chiều; tính tiết chế", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095931", "hw": "nonindulgent", "pos": "adj", "ipa": "/ˌnɑnɪnˈdʌldʒənt/", "vi": "không nuông chiều; nghiêm khắc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095932", "hw": "nonindustrial", "pos": "adj", "ipa": "/ˌnɑnɪnˈdʌstriəl/", "vi": "phi công nghiệp; ngoài công nghiệp", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095933", "hw": "noninheritable", "pos": "adj", "ipa": "/ˌnɑnɪnˈhɛrɪtəbəl/", "vi": "không thể thừa kế; phi di truyền", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095934", "hw": "noninstitutional", "pos": "adj", "ipa": "/ˌnɑnˌɪnstɪˈtuːʃənəl/", "vi": "phi thể chế; ngoài cơ sở tập trung", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095935", "hw": "noninstitutionalised", "pos": "adj", "ipa": "/ˌnɑnˌɪnstɪˈtuːʃənəlaɪzd/", "vi": "sống ngoài trại; không bị biệt lập", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095936", "hw": "nonintegrated", "pos": "adj", "ipa": "/ˌnɑnˈɪntəˌɡreɪtɪd/", "vi": "không tích hợp; không hợp nhất", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095937", "hw": "nonintellectual", "pos": "adj", "ipa": "/ˌnɑnˌɪntəˈlɛktʃuəl/", "vi": "phi trí tuệ; không thuộc trí thức", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095938", "hw": "noninterchangeable", "pos": "adj", "ipa": "/ˌnɑnˌɪntɚˈtʃeɪndʒəbəl/", "vi": "không thể thay thế lẫn nhau", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095939", "hw": "nonintersecting", "pos": "adj", "ipa": "/ˌnɑnˌɪntɚˈsɛktɪŋ/", "vi": "không giao nhau; không cắt nhau", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095940", "hw": "nonionised", "pos": "adj", "ipa": "/ˌnɑnˈaɪənaɪzd/", "vi": "không bị ion hóa; phi ion", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095941", "hw": "nonionized", "pos": "adj", "ipa": "/ˌnɑnˈaɪənaɪzd/", "vi": "không bị ion hóa; dạng phân tử", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095942", "hw": "nonius", "pos": "noun", "ipa": "/ˈnoʊniəs/", "vi": "du xích; thước đo phụ nonius", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095943", "hw": "nonkosher", "pos": "adj", "ipa": "/ˌnɑnˈkoʊʃɚ/", "vi": "không kosher; trái luật Do Thái", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095944", "hw": "nonleaded", "pos": "adj", "ipa": "/ˌnɑnˈlɛdɪd/", "vi": "không chứa chì; không chì", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095945", "hw": "nonlegal", "pos": "adj", "ipa": "/ˌnɑnˈliːɡəl/", "vi": "phi pháp lý; ngoài phạm vi luật", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095946", "hw": "nonlexical", "pos": "adj", "ipa": "/ˌnɑnˈlɛksɪkəl/", "vi": "phi từ vựng; ngoài từ ngữ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095947", "hw": "nonlexically", "pos": "adv", "ipa": "/ˌnɑnˈlɛksɪkli/", "vi": "một cách phi từ vựng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095948", "hw": "nonlinguistic", "pos": "adj", "ipa": "/ˌnɑnlɪŋˈɡwɪstɪk/", "vi": "phi ngôn ngữ; ngoài ngôn từ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095949", "hw": "nonliterary", "pos": "adj", "ipa": "/ˌnɑnˈlɪtəˌrɛri/", "vi": "phi văn học; không mang tính văn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095950", "hw": "nonliterate", "pos": "adj", "ipa": "/ˌnɑnˈlɪtərət/", "vi": "chưa có chữ viết; chưa biết chữ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095951", "hw": "nonmandatory", "pos": "adj", "ipa": "/ˌnɑnˈmændəˌtɔːri/", "vi": "không bắt buộc; mang tính tùy chọn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095952", "hw": "nonmeaningful", "pos": "adj", "ipa": "/ˌnɑnˈmiːnɪŋfəl/", "vi": "không mang ý nghĩa; vô nghĩa lý", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095953", "hw": "nonmechanical", "pos": "adj", "ipa": "/ˌnɑnməˈkænɪkəl/", "vi": "phi cơ học; không dùng máy móc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095954", "hw": "nonmechanistic", "pos": "adj", "ipa": "/ˌnɑnˌmɛkəˈnɪstɪk/", "vi": "phi cơ giới; không máy móc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095955", "hw": "nonmedicinal", "pos": "adj", "ipa": "/ˌnɑnməˈdɪsənəl/", "vi": "không dùng làm thuốc; phi dược liệu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095956", "hw": "nonmetals", "pos": "noun", "ipa": "/ˌnɑnˈmɛtəlz/", "vi": "các phi kim; các nguyên tố phi kim", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095957", "hw": "nonmetamorphic", "pos": "adj", "ipa": "/ˌnɑnˌmɛtəˈmɔːrfɪk/", "vi": "không biến chất; phi biến chất", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095958", "hw": "nonmigratory", "pos": "adj", "ipa": "/ˌnɑnˈmaɪɡrətɔːri/", "vi": "không di cư; sống định cư", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095959", "hw": "nonmodern", "pos": "adj", "ipa": "/ˌnɑnˈmɑːdɚn/", "vi": "không hiện đại; phi tân thời", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095960", "hw": "nonmonotonic", "pos": "adj", "ipa": "/ˌnɑnˌmɑːnəˈtɑːnɪk/", "vi": "phi đơn điệu; không tăng giảm đều", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095961", "hw": "nonmoral", "pos": "adj", "ipa": "/ˌnɑnˈmɔːrəl/", "vi": "phi đạo đức; ngoài luân thường", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095962", "hw": "nonnatural", "pos": "adj", "ipa": "/ˌnɑnˈnætʃərəl/", "vi": "phi tự nhiên; siêu nhiên; nhân tạo", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095963", "hw": "nonnomadic", "pos": "adj", "ipa": "/ˌnɑnnoʊˈmædɪk/", "vi": "không du mục; sống định cư", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095964", "hw": "nonnormative", "pos": "adj", "ipa": "/ˌnɑnˈnɔːrmətɪv/", "vi": "phi chuẩn mực; không theo quy chuẩn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095965", "hw": "nonobjective", "pos": "adj", "ipa": "/ˌnɑnəbˈdʒɛktɪv/", "vi": "phi khách quan; trừu tượng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095966", "hw": "nonobligatory", "pos": "adj", "ipa": "/ˌnɑnəˈblɪɡətɔːri/", "vi": "không bắt buộc; hoàn toàn tùy ý", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095967", "hw": "nonobservance", "pos": "noun", "ipa": "/ˌnɑnəbˈzɜːrvəns/", "vi": "sự không tuân thủ; sự bất tuân", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095968", "hw": "nonobservant", "pos": "adj", "ipa": "/ˌnɑnəbˈzɜːrvənt/", "vi": "không tuân thủ luật giáo", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095969", "hw": "nonoccurrence", "pos": "noun", "ipa": "/ˌnɑnəˈkɜːrəns/", "vi": "sự không xảy ra; việc không có thực", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095970", "hw": "nonopening", "pos": "adj", "ipa": "/ˌnɑnˈoʊpənɪŋ/", "vi": "không mở được; cố định", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095971", "hw": "nonoscillatory", "pos": "adj", "ipa": "/ˌnɑnˈɑːsɪlətɔːri/", "vi": "không dao động; phi dao động", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095972", "hw": "nonparallel", "pos": "adj", "ipa": "/ˌnɑnˈpærəlɛl/", "vi": "không song song; giao cắt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095973", "hw": "nonparasitic", "pos": "adj", "ipa": "/ˌnɑnˌpærəˈsɪtɪk/", "vi": "không ký sinh; sống tự dưỡng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095974", "hw": "nonparticipant", "pos": "noun", "ipa": "/ˌnɑnpɑːrˈtɪsəpənt/", "vi": "người ngoài cuộc; kẻ không tham gia", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095975", "hw": "nonparticulate", "pos": "adj", "ipa": "/ˌnɑnpɑːrˈtɪkjələt/", "vi": "không chứa hạt; phi hạt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095976", "hw": "nonpartisanship", "pos": "noun", "ipa": "/ˌnɑnˈpɑːrtɪzənʃɪp/", "vi": "tính phi đảng phái; sự trung lập", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095977", "hw": "nonpartizan", "pos": "adj", "ipa": "/ˌnɑnˈpɑːrtɪzən/", "vi": "phi đảng phái; vô tư; trung lập", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095978", "hw": "nonpasserine", "pos": "adj", "ipa": "/ˌnɑnˈpæsəraɪn/", "vi": "không thuộc bộ sẻ; ngoài bộ sẻ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095979", "hw": "nonperiodic", "pos": "adj", "ipa": "/ˌnɑnˌpɪriˈɑːdɪk/", "vi": "không có chu kỳ; không định kỳ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095980", "hw": "nonpermeable", "pos": "adj", "ipa": "/ˌnɑnˈpɜːrmiəbəl/", "vi": "không thấm; không thấm qua được", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095981", "hw": "nonperson", "pos": "noun", "ipa": "/ˈnɑːnˌpɜːrsən/", "vi": "người vô danh; kẻ bị tước quyền", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095982", "hw": "nonpersonal", "pos": "adj", "ipa": "/ˌnɑnˈpɜːrsənəl/", "vi": "phi cá nhân; khách quan; chung", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095983", "hw": "nonphotosynthetic", "pos": "adj", "ipa": "/ˌnɑnˌfoʊtəsɪnˈθɛtɪk/", "vi": "không có khả năng quang hợp", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095984", "hw": "nonplus", "pos": "verb", "ipa": "/nɑːnˈplʌs/", "vi": "làm bối rối; làm chết lặng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095985", "hw": "nonpluses", "pos": "verb", "ipa": "/nɑːnˈplʌsɪz/", "vi": "làm sững sờ; làm bối rối", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095986", "hw": "nonplusing", "pos": "verb", "ipa": "/nɑːnˈplʌsɪŋ/", "vi": "làm sững sờ; gây bối rối", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095987", "hw": "nonplusses", "pos": "verb", "ipa": "/nɑːnˈplʌsɪz/", "vi": "làm lúng túng; khiến ngơ ngác", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095988", "hw": "nonplussing", "pos": "verb", "ipa": "/nɑːnˈplʌsɪŋ/", "vi": "gây hoang mang; làm bối rối", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095989", "hw": "nonpoisonous", "pos": "adj", "ipa": "/ˌnɑnˈpɔɪzənəs/", "vi": "không độc; không chứa chất độc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095990", "hw": "nonprehensile", "pos": "adj", "ipa": "/ˌnɑnprɪˈhɛnsəl/", "vi": "không cầm nắm được; không thể quắp", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095991", "hw": "nonprognosticative", "pos": "adj", "ipa": "/ˌnɑnprɑːɡˈnɑːstɪkətɪv/", "vi": "không có tính tiên lượng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095992", "hw": "nonprogressive", "pos": "adj", "ipa": "/ˌnɑnprəˈɡrɛsɪv/", "vi": "không tiến bộ; không tiến triển", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095993", "hw": "nonprotractile", "pos": "adj", "ipa": "/ˌnɑnproʊˈtræktəl/", "vi": "không thể thò ra kéo dài", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095994", "hw": "nonpsychoactive", "pos": "adj", "ipa": "/ˌnɑnˌsaɪkoʊˈæktɪv/", "vi": "phi hướng thần; không kích thần", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095995", "hw": "nonpurulent", "pos": "adj", "ipa": "/ˌnɑnˈpjʊrələnt/", "vi": "không làm mủ; không có mủ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095996", "hw": "nonracist", "pos": "adj", "ipa": "/ˌnɑnˈreɪsɪst/", "vi": "không kỳ thị sắc tộc; bình đẳng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095997", "hw": "nonrational", "pos": "adj", "ipa": "/ˌnɑnˈræʃənəl/", "vi": "phi lý tính; ngoài phạm trù lý trí", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095998", "hw": "nonreader", "pos": "noun", "ipa": "/ˈnɑːnˌriːdɚ/", "vi": "người không biết đọc; người mù chữ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.095999", "hw": "nonreciprocating", "pos": "adj", "ipa": "/ˌnɑnrɪˈsɪprəkeɪtɪŋ/", "vi": "không chuyển động qua lại", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096000", "hw": "nonrecreational", "pos": "adj", "ipa": "/ˌnɑnˌrɛkriˈeɪʃənəl/", "vi": "phi giải trí; phục vụ công việc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096001", "hw": "nonreflecting", "pos": "adj", "ipa": "/ˌnɑnrɪˈflɛktɪŋ/", "vi": "không phản chiếu ánh sáng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
]

assert len(part5_data) == 100, f"Expected 100 items, got {len(part5_data)}"

valid_pos = {"noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det"}

with open("scratch/b20_r02_raw_p5.json") as f:
    raw_p5 = json.load(f)

for i, (item, raw) in enumerate(zip(part5_data, raw_p5)):
    assert item["id"] == raw["id"], f"ID mismatch at {i}: {item['id']} vs {raw['id']}"
    assert item["hw"] == raw["hw"], f"HW mismatch at {i}: {item['hw']} vs {raw['hw']}"
    assert item["pos"] in valid_pos, f"Invalid POS at {i}: {item['pos']}"
    assert item["ipa"].startswith("/") and item["ipa"].endswith("/"), f"Invalid IPA slashes at {i}: {item['ipa']}"
    assert item["ipa"].count("/") == 2, f"IPA does not have exactly 2 slashes at {i}: {item['ipa']}"
    assert not item["ipa"].startswith("/ ") and not item["ipa"].endswith(" /"), f"IPA boundary spaces at {i}: {item['ipa']}"
    assert len(item["vi"]) <= 35, f"vi too long at {i} ({item['hw']}): {item['vi']} (len={len(item['vi'])})"
    assert len(item["vi"]) > 0, f"Empty vi at {i}"
    assert not any(art in item["vi"] for art in ["Số nhiều", "Xem ", "Dạng ", "Viết tắt", "Động từ chia", "%%"]), f"Crawler artifact in vi at {i}: {item['vi']}"
    assert item["status"] == "reviewed", f"Status not reviewed at {i}"

with open("scratch/b20_r02_p5.json", "w") as f:
    json.dump(part5_data, f, ensure_ascii=False, indent=2)

print("Batch 20 Round 2 Part 5 validated and saved successfully!")
