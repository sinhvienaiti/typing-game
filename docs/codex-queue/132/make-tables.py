from pathlib import Path
from collections import defaultdict
from difflib import SequenceMatcher
import json, re, html, subprocess, unicodedata

report = Path(__file__).resolve().parent
root = report.parents[2] / 'games/.wt-td-codex'
data = json.loads((report / 'inventory.json').read_text())
vi = re.compile('[ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯư\u1ea0-\u1ef9]')
broad = re.compile('[À-ỹđĐ]')
proper = re.compile('Mộc Tinh|Bà Cú Mực|Chấm|Phẩy|Gạch')
allowed = lambda f: f == 'index.html' or f.startswith(('src/ui/', 'src/app/', 'src/view/', 'src/content/'))
cell = lambda s: '`' + s.replace('`', '\\`').replace('|', '\\|').replace('\n', r'\n').replace('\r', r'\r') + '`'
location = lambda x: cell(x['file'] + ':' + str(x['line']))

def table(headers, rows):
    return '| ' + ' | '.join(headers) + ' |\n|' + '|'.join('---' for _ in headers) + '|\n' + ''.join('| ' + ' | '.join(row) + ' |\n' for row in rows)

before = sorted((x for x in data['baseline'] if allowed(x['file']) and vi.search(x['text'])), key=lambda x:(x['file'], x['line']))
text = '# Phiếu 132 · Chuỗi trước khi sửa\n\n'
text += f'Có **{len(before)} literal/mảnh template có chữ Việt** trong phạm vi được ghi. Dòng theo ảnh chụp nguồn trước lượt dịch (`literals-before.json`); CSS và HTML đối chiếu HEAD. Mỗi mảnh template là một dòng, không gồm biểu thức nội suy. Bỏ chú thích và chỗ đọc/hiện nghĩa từ `vi`. Tên riêng cũng được liệt kê để duyệt, nhưng giữ theo `NAMES_EN.md`.\n\n'
text += table(['file:dòng', 'chuỗi cũ'], [(location(x),cell(x['text'])) for x in before])
extras = [x for x in data['baseline'] if (x['file']=='src/app/sandbox.ts' and 'Kho' in x['text']) or (x['file']=='src/view/words/cards.ts' and x['text']=='Neo')]
text += '\n## Bổ sung sau đọc mã\n\nNhãn tiếng Việt không dấu không được bộ lọc dấu bắt; vẫn phải dịch. Các viết tắt tên thực thể cũ được ghi trong bảng cũ → mới.\n\n'
text += table(['file:dòng','chuỗi cũ'],[(location(x),cell(x['text'])) for x in extras])
main_before=[x for x in data['baseline'] if x['file']=='src/main.ts' and vi.search(x['text'])]
text += '\n## Ngoài phạm vi ghi\n\n`src/main.ts` có 16 literal UI tiếng Việt. Chỉ đọc và liệt kê; chưa được phép sửa.\n\n'+table(['file:dòng','chuỗi cũ'],[(location(x),cell(x['text'])) for x in main_before])
(report/'strings-before.md').write_text(text)

old, new = defaultdict(list), defaultdict(list)
for x in data['baseline']:old[x['file']].append(x)
for x in data['current']:new[x['file']].append(x)
changes=[]
for f in sorted(old.keys()|new.keys()):
    if not (allowed(f) or f.startswith('tests/')) or f=='tests/english-ui.test.ts':continue
    for op,i,j,k,l in SequenceMatcher(None,[x['text'] for x in old[f]],[x['text'] for x in new[f]],autojunk=False).get_opcodes():
        if op=='equal':continue
        if j-i==l-k:
            for a,b in zip(old[f][i:j],new[f][k:l]):
                changes.append(dict(file=f,line=a['line'],newLine=b['line'],text=a['text'],newText=b['text'],kind=a['kind']))
        elif f=='src/ui/profile.ts' and op=='insert':
            advice_old=[x for x in old['src/kit/balance/pace.ts'] if 110<=x['line']<=116 and vi.search(x['text'])]
            advice_new=[x for x in new[f][k:l] if ' ' in x['text']]
            assert len(advice_old)==len(advice_new)==7
            for a,b in zip(advice_old,advice_new):
                changes.append(dict(file=f,line=b['line'],newLine=b['line'],text=a['text'],newText=b['text'],kind=b['kind'],note=f"Lời khuyên cũ lấy từ {a['file']}:{a['line']}; bảng EN tại UI, không sửa kit."))
        else:raise RuntimeError((f,op,j-i,l-k))

# Regular-expression expectations are not TypeScript string literals.
for f in ['tests/td-hud.test.ts','tests/td-test-pass.test.ts']:
    a=subprocess.check_output(['git','-C',str(root),'show','HEAD:'+f],text=True).splitlines()
    b=(root/f).read_text().splitlines()
    assert len(a)==len(b)
    for n,(x,y) in enumerate(zip(a,b),1):
        if x!=y and ('toMatch(/' in x or 'exec(' in x or 'Number(/' in x) and '/' in y:
            if any(z in x for z in ['toMatch(/','exec(','Number(/']):
                changes.append(dict(file=f,line=n,newLine=n,text=x.strip(),newText=y.strip(),kind='RegexExpectation',note='Kỳ vọng regex theo chữ hiển thị; số và luật giữ nguyên.'))

(report/'changes.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2)+'\n')

def visible(s):
    return html.unescape(re.sub('<[^>]*>','',s)).strip()

def row(x):
    a,b=visible(x['text']),visible(x['newText'])
    note=x.get('note','')
    if x['file'].startswith('tests/'):
        note += ' Chỉ đổi kỳ vọng chuỗi.'
    if a and len(b)>len(a)*1.2:
        note += f' ⚑ {len(a)}→{len(b)} ký tự, +{(len(b)/len(a)-1)*100:.0f}%; còn vượt 20%, Claude duyệt/rút tiếp.'
    elif a:
        note += f' {len(a)}→{len(b)} ký tự (≤120%).'
    if proper.search(x['newText']):note += ' Giữ tên riêng theo NAMES_EN.md.'
    if 'Wordwoven' in x['newText']:note += ' Tên game bắt buộc.'
    if x['file'].endswith('slice-1a.ts'):note += ' Nhãn view; không đổi id hay dữ liệu sim.'
    if x['file'].endswith('title.ts') and x['line']==25:note += ' Đã rút gọn thành Profile.'
    if x['newText']=='Shatter':note += ' Rút gọn Break Shield để vừa thẻ.'
    return (cell(x['file']+':'+str(x['newLine'])),cell(x['text']),cell(x['newText']),note.strip())
source=[x for x in changes if not x['file'].startswith('tests/')]
tests=[x for x in changes if x['file'].startswith('tests/')]
expanded=[x for x in source if visible(x['text']) and len(visible(x['newText']))>len(visible(x['text']))*1.2]
text='# Phiếu 132 · Bảng duyệt cũ → mới\n\n'
text+=f'**{len(source)} chuỗi nguồn/trang và {len(tests)} chuỗi hoặc dòng kỳ vọng test**. `file:dòng` là vị trí hiện tại; mảnh template giữ phần chữ tĩnh, không đổi nội suy. Bảng gồm cả nhãn không dấu và lời khuyên từng đọc động từ kit.\n\n'
text+='Độ dài đếm Unicode đã hiển thị (bỏ thẻ HTML hoàn chỉnh, chưa đo pixel); mỗi mảnh nội suy được đếm riêng. ⚑ là mảnh còn dài quá 20%, chưa coi đạt cổng độ dài. Đã rút `Typing stats` thành `Profile`, `Break Shield` thành `Shatter`, và nhiều nhãn/toast; các từ ngắn như Build, Learn, Good, Sound cần Claude chốt cách viết trong ô thật. Tên Wordwoven là tên bắt buộc. Không có kiểm tràn chữ bằng trình duyệt trong phiếu này.\n\n'
text+=table(['file:dòng','chuỗi cũ','chuỗi mới','ghi chú'],[row(x) for x in source])
text+='\n## Kỳ vọng test\n\n'+table(['file:dòng','chuỗi cũ','chuỗi mới','ghi chú'],[row(x) for x in tests])
text+='\nTest mới `tests/english-ui.test.ts` dùng TypeScript AST để quét literal và mọi mảnh template, thêm chuỗi CSS và chữ/nhãn HTML. Không có test mới cho luật chơi.\n'
(report/'strings.md').write_text(text)

current_src=[x for x in data['current'] if x['file'].startswith('src/') or x['file']=='index.html']
remaining=[x for x in current_src if vi.search(unicodedata.normalize('NFC',x['text']))]
kit=[x for x in remaining if x['file'].startswith('src/kit/')]
names=[x for x in remaining if not x['file'].startswith('src/kit/') and not vi.search(unicodedata.normalize('NFC',proper.sub('',x['text'])))]
blocked=[x for x in remaining if x not in kit and x not in names]
text='# Phiếu 132 · Chuỗi còn lại\n\n'
text+=f'Quét lại bằng `node docs/codex-queue/132/inventory.mjs` từ repo cha. TypeScript AST bỏ chú thích, giải Unicode escape và tách mảnh template. Khoảng thô `[À-ỹđĐ]` còn bắt dấu × và ký tự ngoài tiếng Việt; lọc chữ Việt thật sau chuẩn hóa NFC. Kết quả: **{len(blocked)} literal UI chưa dịch ngoài phạm vi**, **{len(names)} literal/mảnh chứa tên riêng được giữ**, **{len(kit)} literal trong kit**; 0 literal tiếng Việt thường trong các thư mục được phép sửa.\n\n'
text+='## Chưa đạt: src/main.ts ngoài phạm vi ghi\n\nKhông thêm ngoại lệ cho file này vào test; test quét toàn `src/` phải đỏ cho tới khi chủ dự án cho phép dịch. Đã hỏi mở phạm vi, chưa có trả lời.\n\n'+table(['file:dòng','chuỗi còn lại'],[(location(x),cell(x['text'])) for x in blocked])
text+='\n## Tên riêng giữ theo quy ước\n\n`NAMES_EN.md` và AGENTS.md yêu cầu giữ tên nhân vật độc nhất: Mộc Tinh, Bà Cú Mực, Chấm, Phẩy, Gạch. Đây là ngoại lệ tên riêng, không phải nghĩa từ; nếu yêu cầu “chỉ còn nghĩa từ/kit/chú thích” hiểu tuyệt đối thì cần chủ dự án chốt lại. Phần câu quanh tên đã dịch.\n\n'+table(['file:dòng','chuỗi còn lại'],[(location(x),cell(x['text'])) for x in names])
text+='\n## Nghĩa từ vựng\n\nKhông có nghĩa tiếng Việt hardcode trong literal nguồn ngoài kit. Nghĩa được đọc động từ trường `vi`/gloss: `src/app/vocab.ts`, `src/app/learn.ts`, `src/typing/decks.ts`, `src/view/words/cards.ts`, `src/ui/hud.ts`, `src/ui/sheets.ts`. Không loại cả file nào trong số này khỏi test: nhãn UI của chúng vẫn bị quét. Dữ liệu từ vựng ở `public/vocabulary/` giữ nguyên và ngoài phạm vi sửa.\n'
text+='\n## Kit — chỉ liệt kê cho Claude\n\nBản chép kit không đổi. Bảy lời khuyên `ADVICE_VI` từng hiện ở hồ sơ được thay bằng bảng tiếng Anh cục bộ ở UI; kit vẫn giữ nguyên. Các chuỗi balance/bot là nhãn công cụ và dữ liệu; chuỗi trong `input/keys.ts` là tập ký tự xử lý IME, không phải nhãn người chơi.\n\n'+table(['file:dòng','chuỗi còn lại'],[(location(x),cell(x['text'])) for x in kit])
text+='\n## Chú thích\n\nCác chú thích cũ nhắc thuật ngữ tiếng Việt được giữ nguyên, không phải chữ người chơi đọc. Danh sách vị trí thu được từ trivia của AST:\n\n'+table(['file:dòng','chú thích'],[(location(x),cell(x['text'])) for x in data['comments']])
false=[x for x in current_src if broad.search(x['text']) and not vi.search(x['text'])]
text+='\n## Kết quả thô không phải tiếng Việt\n\n'+table(['file:dòng','literal'],[(location(x),cell(x['text'])) for x in false])
(report/'remaining.md').write_text(text)
raw=[]
for p in sorted((root/'src').rglob('*')):
    if p.is_file():
        for n,line in enumerate(p.read_text().splitlines(),1):
            if broad.search(line):raw.append(f'{p.relative_to(root)}:{n}: {line}')
for n,line in enumerate((root/'index.html').read_text().splitlines(),1):
    if broad.search(line):raw.append(f'index.html:{n}: {line}')
(report/'remaining-raw.txt').write_text('\n'.join(raw)+'\n')
summary=dict(before=len(before),sourceChanges=len(source),testChanges=len(tests),expandedFragments=len(expanded),blocked=len(blocked),properNames=len(names),kit=len(kit),comments=len(data['comments']))
(report/'inventory-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary))
