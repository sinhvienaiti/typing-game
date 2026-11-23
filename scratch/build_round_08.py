import json

with open('scratch/test_round_08.py') as f:
    # part 1
    p1_code = f.read()

# Let's import part1, part2, part3, part4, part5
import sys
sys.path.insert(0, 'scratch')
from test_round_08 import part1
from test_round_08_p2 import part2
from test_round_08_p3 import part3
from test_round_08_p4 import part4
from test_round_08_p5 import part5

# Apply Part 1 fixes
part1['lex.en.100k.043518']['vi'] = 'người học đòi; kẻ làm việc tài tử'
part1['lex.en.100k.043545']['vi'] = 'trẻ bụi đời lang thang đường phố'
part1['lex.en.100k.043551']['vi'] = 'họa sĩ Childe Hassam Mỹ'
part1['lex.en.100k.043552']['vi'] = 'thái độ kiêu căng ngạo mạn'
part1['lex.en.100k.043555']['vi'] = 'các tiên nữ canh vườn táo vàng'
part1['lex.en.100k.043563']['vi'] = 'dòng máu bất tử của thần linh'
part1['lex.en.100k.043567']['vi'] = 'chim choi choi killdeer châu Mỹ'
part1['lex.en.100k.043568']['vi'] = 'sự hiệp thông trong Ki-tô giáo'
part1['lex.en.100k.043585']['vi'] = 'hỗn hợp nhựa dầu tự nhiên'
part1['lex.en.100k.043595']['vi'] = 'một cách hờn dỗi cáu kỉnh'

# Apply Part 2 fixes
part2['lex.en.100k.043642']['vi'] = 'tự nhiên không bởi nguyên nhân nào'
part2['lex.en.100k.043675']['vi'] = 'người phân tích giám định quặng'
part2['lex.en.100k.043688']['vi'] = 'tổng đài điện thoại cơ quan'
part2['lex.en.100k.043692']['vi'] = 'nói chuyện phiếm; buôn chuyện'
part2['lex.en.100k.043697']['vi'] = 'có quan hệ cận huyết thống'

# Apply Part 3 fixes
part3['lex.en.100k.043709']['vi'] = 'sự khử muối; việc lọc nước biển'
part3['lex.en.100k.043719']['vi'] = 'quả hạch có nhân cứng bên trong'
part3['lex.en.100k.043750']['vi'] = 'tính không thể đảo ngược hoàn lại'
part3['lex.en.100k.043760']['vi'] = 'phô mai mềm mùi nồng Limburger'
part3['lex.en.100k.043771']['vi'] = 'đảng viên phái Menshevik ở Nga'
part3['lex.en.100k.043776']['vi'] = 'công nghệ đa xử lý dữ liệu'
part3['lex.en.100k.043791']['vi'] = 'người tuần tra; nhân viên tuần tra'
part3['lex.en.100k.043795']['vi'] = 'lá bột mỏng nướng bánh Hy Lạp'
part3['lex.en.100k.043796']['vi'] = 'thuộc ký tự chữ viết tượng hình'
part3['lex.en.100k.043801']['vi'] = 'khoa phục hình làm răng giả thẩm mỹ'

# Apply Part 4 fixes
part4['lex.en.100k.043814']['vi'] = 'thầy lang truyền thống người Zulu'
part4['lex.en.100k.043837']['vi'] = 'thuốc trị tiểu đường sulfonylurea'
part4['lex.en.100k.043855']['vi'] = 'vô song không ai có thể vượt qua'
part4['lex.en.100k.043861']['vi'] = 'làm bằng sáp; tái nhợt như sáp'
part4['lex.en.100k.043897']['vi'] = 'vùng bắt chéo dây thần kinh'

# Apply Part 5 fixes
part5['lex.en.100k.043903']['vi'] = 'hoạt động phản gián tình báo'
part5['lex.en.100k.043904']['vi'] = 'bản văn kiện viết bằng mật mã'
part5['lex.en.100k.043923']['vi'] = 'phong tước quý tộc; tôn vinh'
part5['lex.en.100k.043930']['vi'] = 'chứng lãnh cảm; sự lạnh lùng'
part5['lex.en.100k.043939']['vi'] = 'từ đồng âm; phức điệu chủ âm'
part5['lex.en.100k.043964']['vi'] = 'có song đứng chia ô cửa sổ'
part5['lex.en.100k.043968']['vi'] = 'quan chức giàu có phô trương'
part5['lex.en.100k.043973']['vi'] = 'ghi chép bằng nốt nhạc ký âm'
part5['lex.en.100k.043975']['vi'] = 'hào hứng thái quá; quá nồng nhiệt'
part5['lex.en.100k.043976']['vi'] = 'thuộc loài cừu; nhút nhát như cừu'
part5['lex.en.100k.043978']['vi'] = 'lạnh buốt giá; có sương giá'
part5['lex.en.100k.043982']['vi'] = 'rối loạn chuyển hóa bẩm sinh PKU'
part5['lex.en.100k.043984']['vi'] = 'nguyên sinh chất tế bào'
part5['lex.en.100k.043987']['vi'] = 'tính khả thi trong thực tiễn'

code = '''# Batch 09 Round 8 Manual QA overrides (records 3500-3999, IDs 043502-044001)
import json

OVERRIDES_PART1 = ''' + json.dumps(part1, ensure_ascii=False, indent=4) + '''

OVERRIDES_PART2 = ''' + json.dumps(part2, ensure_ascii=False, indent=4) + '''

OVERRIDES_PART3 = ''' + json.dumps(part3, ensure_ascii=False, indent=4) + '''

OVERRIDES_PART4 = ''' + json.dumps(part4, ensure_ascii=False, indent=4) + '''

OVERRIDES_PART5 = ''' + json.dumps(part5, ensure_ascii=False, indent=4) + '''

ALL_OVERRIDES = {}
ALL_OVERRIDES.update(OVERRIDES_PART1)
ALL_OVERRIDES.update(OVERRIDES_PART2)
ALL_OVERRIDES.update(OVERRIDES_PART3)
ALL_OVERRIDES.update(OVERRIDES_PART4)
ALL_OVERRIDES.update(OVERRIDES_PART5)

print(f\"Total overrides loaded: {len(ALL_OVERRIDES)}\")

# Validate all overrides
VALID_POS = {\"noun\", \"verb\", \"adj\", \"adv\", \"num\", \"intj\", \"prep\", \"pron\", \"conj\", \"det\"}
errors = []

for rec_id, ov in ALL_OVERRIDES.items():
    if len(ov[\"vi\"]) > 35:
        errors.append(f\"{rec_id}: vi length {len(ov['vi'])} > 35: '{ov['vi']}'\")
    if ov[\"pos\"] not in VALID_POS:
        errors.append(f\"{rec_id}: invalid pos '{ov['pos']}'\")
    if not (ov[\"ipa\"].startswith(\"/\") and ov[\"ipa\"].endswith(\"/\")):
        errors.append(f\"{rec_id}: invalid ipa: '{ov['ipa']}'\")

if errors:
    print(f\"Validation FAILED with {len(errors)} errors:\")
    for err in errors[:20]:
        print(f\"  {err}\")
    raise SystemExit(1)

# Apply to batch-09.json
BATCH_FILE = \"content/english/qa-batches/batch-09.json\"
with open(BATCH_FILE, \"r\", encoding=\"utf-8\") as f:
    batch_data = json.load(f)

records = batch_data[\"records\"]
applied_count = 0

for i in range(3500, 4000):
    r = records[i]
    r_id = r[\"id\"]
    if r_id in ALL_OVERRIDES:
        ov = ALL_OVERRIDES[r_id]
        if r[\"hw\"].lower() != ov[\"hw\"].lower():
            print(f\"Mismatch at index {i}: record hw '{r['hw']}' vs override hw '{ov['hw']}'\")
            raise SystemExit(1)
        r[\"pos\"] = ov[\"pos\"]
        r[\"vi\"] = ov[\"vi\"]
        r[\"ipa\"] = ov[\"ipa\"]
        applied_count += 1
    else:
        print(f\"Missing override for record index {i}: {r_id} {r['hw']}\")
        raise SystemExit(1)

print(f\"Successfully applied {applied_count} overrides to records 3500-3999.\")

# Update reviewedCount
batch_data[\"reviewedCount\"] = 4000
batch_data[\"status\"] = \"in_progress\"

with open(BATCH_FILE, \"w\", encoding=\"utf-8\") as f:
    json.dump(batch_data, f, ensure_ascii=False, indent=2)

print(\"Batch 09 updated: reviewedCount is now 4000.\")
'''

with open('scratch/qa_batch_09_round_08.py', 'w', encoding='utf-8') as f:
    f.write(code)

print('Successfully generated scratch/qa_batch_09_round_08.py')
