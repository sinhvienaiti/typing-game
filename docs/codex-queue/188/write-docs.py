"""Kết xuất tài liệu phiếu 188 từ bằng chứng tại máy; chỉ ghi phạm vi được giao."""
from pathlib import Path
import json, hashlib, shutil, re

ROOT = Path.cwd()
OUT = ROOT / 'docs/codex-queue/188'
data = json.loads((OUT / 'inventory.json').read_text())
licenses = OUT / 'licenses'
licenses.mkdir(exist_ok=True)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def slug(name): return name.replace('@', '').replace('/', '--')
records = {}
for audit in data:
    for r in audit['records']:
        if r['kind'] != 'devDependency':
            records.setdefault(r['name'], r)
            for notice in r.get('notices', []):
                (licenses / (slug(r['name']) + '-' + Path(notice['path']).name)).write_text(notice['text'])

vite_path = ROOT / 'games/dragon-hold/node_modules/vite/LICENSE.md'
vite_core = vite_path.read_text().split('# Licenses of bundled dependencies')[0]
(licenses / 'vite-core-LICENSE.txt').write_text(vite_core)
mit_body = '''Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
mesh_license = 'MIT License\n\nCopyright (c) 2016-2022 Arseny Kapoulkine\n\n' + mit_body
ktx_license = 'The MIT License (MIT)\n\nCopyright (c) 2020 Don McCurdy\n\n' + mit_body
zstd_license = ktx_license + '''
***

BSD License

For Zstandard software
Copyright (c) 2016-present, Yann Collet, Facebook, Inc. All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

 * Redistributions of source code must retain the above copyright notice, this
 list of conditions and the following disclaimer.
 * Redistributions in binary form must reproduce the above copyright notice,
 this list of conditions and the following disclaimer in the documentation
 and/or other materials provided with the distribution.

 * Neither the name Facebook nor the names of its contributors may be used to
 endorse or promote products derived from this software without specific
 prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''
for name, text in [('meshoptimizer-0.18-LICENSE.txt', mesh_license), ('ktx-parse-upstream-LICENSE.txt', ktx_license), ('zstddec-upstream-LICENSE.txt', zstd_license)]:
    (licenses / name).write_text(text)

proof = {'buildEmbedded': [], 'vendored': [], 'distExisting': []}
for a in data:
    base = a['base']
    for f in a['vendorGraph']['files']:
        if '/libs/' in f:
            p = ROOT / f
            proof['vendored'].append({'base': base, 'path': f, 'container': 'three@0.170.0', 'sha256': sha(p), 'header': '\n'.join(p.read_text().splitlines()[:7]) if 'meshopt' in f else 'Không có nhãn semver trong bản nhúng.'})
    if base.startswith('games/'):
        vp = ROOT / base / 'node_modules/vite'
        v = json.loads((vp / 'package.json').read_text())
        assert v['version'] == '7.3.7' and v['license'] == 'MIT'
        config = vp / 'dist/node/chunks/config.js'
        t = config.read_text()
        proof['buildEmbedded'].append({'base': base, 'name': 'vite', 'version': v['version'], 'license': v['license'], 'packageJson': str((vp / 'package.json').relative_to(ROOT)), 'licensePath': str((vp / 'LICENSE.md').relative_to(ROOT)), 'licenseSha256': sha(vp / 'LICENSE.md'), 'source': str(config.relative_to(ROOT)), 'sourceSha256': sha(config), 'helperMarkers': {s: t.find(s) for s in ['function polyfill()', 'function preload(baseModule, deps, importerUrl)']}})
        dist = ROOT / base / 'dist'
        js = list((dist / 'assets').glob('*.js'))
        text = '\n'.join(f.read_text() for f in js)
        proof['distExisting'].append({'base': base, 'js': [{'path': str(f.relative_to(ROOT)), 'sha256': sha(f)} for f in js], 'modulepreload': 'modulepreload' in text, 'preloadHelper': 'vite:preloadError' in text, 'fullMitPermissionText': 'Permission is hereby granted' in text, 'copyrightMarker': 'Copyright' in text, 'noticeFiles': [str(f.relative_to(ROOT)) for f in dist.rglob('*') if f.is_file() and re.search('license|notice|credit', f.name, re.I)], 'publicCodeFiles': [str(f.relative_to(ROOT)) for f in (ROOT / base / 'public').rglob('*') if f.is_file() and f.suffix in ['.js','.mjs','.wasm','.html']]})
(OUT / 'embedded-evidence.json').write_text(json.dumps(proof, ensure_ascii=False, indent=2) + '\n')

titles = {'dragon-hold': 'Dragonhold', 'typing-defense': 'Wordwoven', 'typing-survival': 'Last Line', 'game-kit': 'Kit dùng chung'}
def license_for(name): return records[name]['notices'][0]['text']
def block(title, text, source):
    return f'## {title}\n\nNguồn: {source}. Giữ nguyên khối dưới đây khi phân phối.\n\n```text\n{text.rstrip()}\n```\n\n'
for a in data:
    game = a['base'].split('/')[-1]
    if game == 'game-kit': continue
    s = f'# Phiếu 188 · Credits cho {titles[game]}\n\nNgày kiểm: 29/10/2026. Phần giải thích dành cho người tích hợp; tên thành phần và nguyên văn giấy phép trong các khối là nội dung cho trang Credits tiếng Anh. MIT/OFL yêu cầu giữ thông báo khi phân phối; không bắt buộc đúng tên trang “Credits”. Chưa sửa UI hay gói phát hành trong phiếu này.\n\n'
    s += '**Cờ OFL-1.1:** các phông dưới đây nằm ngoài danh sách chủ dự án cho phép; đoạn ghi công không thay quyết định duyệt giấy phép.\n\n'
    for r in a['records']:
        if r['kind'] == 'devDependency': continue
        if r['name'] == 'three' and game == 'typing-defense': continue
        s += block(f"{r['name']} {r['version']} — {r['license']}", license_for(r['name']), '`' + r['notices'][0]['path'] + '`')
    if game != 'typing-defense':
        s += block('meshoptimizer 0.18 — MIT', '// Copyright (C) 2016-2022, by Arseny Kapoulkine (arseny.kapoulkine@gmail.com)\n\n' + mesh_license, '[LICENSE tại v0.18](https://raw.githubusercontent.com/zeux/meshoptimizer/v0.18/LICENSE.md) và header `three/examples/jsm/libs/meshopt_decoder.module.js` trên máy')
    s += block('Vite 7.3.7 — MIT', vite_core, f'`{a["base"]}/node_modules/vite/LICENSE.md`, phần Vite core; polyfill và helper preload vào bundle')
    if game == 'typing-defense':
        s += '## Dự phòng khi bắt đầu dùng three\n\n`three` 0.170.0 có trong dependencies/lockfile nhưng đồ thị từ `src/main.ts` hiện không nhập nó. Khối sau chỉ cần đưa vào khi bundle thực sự dùng three; chưa gán meshoptimizer hay a11y-dialog cho Wordwoven.\n\n'
        s += block('three 0.170.0 — MIT (chưa vào luồng chơi hiện tại)', license_for('three'), '`games/typing-defense/node_modules/three/LICENSE`')
    s += '## Khi đồng bộ kit mới\n\nNếu game nhập quick-settings của kit, phải thêm cả hai khối a11y-dialog và focusable-selectors từ [credits-game-kit.md](credits-game-kit.md); hiện package.json/lockfile và src/kit của game chưa có chúng. Không coi việc tạo tài liệu này là đã tích hợp Credits vào site.\n'
    (OUT / f'credits-{game}.md').write_text(s)

s = '# Phiếu 188 · Credits cho kit dùng chung\n\nKit không có trang chơi/build độc lập. Game lấy mô-đun nào thì giữ thông báo của mô-đun đó. Các khối sau sẵn để đưa vào trang Credits tiếng Anh; giải thích bằng tiếng Việt không phải nội dung UI.\n\n'
for name in ['a11y-dialog', 'focusable-selectors']:
    r = records[name]
    s += block(f'{name} {r["version"]} — MIT (quick-settings)', license_for(name), '`' + r['notices'][0]['path'] + '`')
s += 'focusable-selectors đã được đóng trực tiếp trong bản ESM a11y-dialog, vẫn phải giữ thông báo riêng của nó; không đếm thành hai bản runtime khi bundler dùng bản ESM này.\n\n'
s += block('three 0.170.0 — MIT (khi dùng mô-đun 3D)', license_for('three'), '`shared/game-kit/node_modules/three/LICENSE`; nằm ở devDependencies nhưng mô-đun kit nhập khi chơi')
s += block('meshoptimizer 0.18 — MIT (model-loader)', '// Copyright (C) 2016-2022, by Arseny Kapoulkine (arseny.kapoulkine@gmail.com)\n\n' + mesh_license, '[LICENSE tại v0.18](https://raw.githubusercontent.com/zeux/meshoptimizer/v0.18/LICENSE.md) và header file nhúng')
s += '## Nhánh KTX2 tùy chọn: chưa đi vào ba game\n\nHai thành phần sau được KTX2Loader nhập. Bản nhúng khóa theo three 0.170.0 và SHA-256 trong embedded-evidence.json; không có nhãn semver riêng để xác nhận trên máy. Cần xác minh nguồn phiên bản trước khi bật. Bên phục vụ còn phải chuẩn bị giấy phép/NOTICE cho đúng bản Basis Universal JS/WASM; không được coi hai khối sau là toàn bộ nghĩa vụ của Basis Universal.\n\n'
s += block('KTX-Parse — MIT (bản nhúng trong three 0.170.0)', ktx_license, '[LICENSE repo gốc](https://raw.githubusercontent.com/donmccurdy/KTX-Parse/main/LICENSE)')
s += block('zstddec / Zstandard — MIT AND BSD-3-Clause (bản nhúng trong three 0.170.0)', zstd_license, '[LICENSE repo gốc](https://raw.githubusercontent.com/donmccurdy/zstddec-wasm/main/LICENSE)')
(OUT / 'credits-game-kit.md').write_text(s)

header = '| Tên | Phiên bản | Loại | Nguồn | Giấy phép | Dùng ở đâu | Ghi công cần có | Người kiểm, ngày |\n|---|---|---|---|---|---|---|---|\n'
append = '''
## Phiếu 188 · Kiểm thư viện mã và phông trong gói chạy (29/10/2026)

Bổ sung, **giữ nguyên mọi dòng cũ**. Các dòng three.js và a11y-dialog cũ ghi “không bắt buộc” cần được hiểu lại: MIT buộc giữ thông báo bản quyền **và** văn bản cho phép khi phân phối mã; trang Credits là nơi ta chọn để cung cấp. Các dòng có phiên bản và kết quả kiểm dưới đây là đối chiếu hiện hành. OFL-1.1 bị gắn cờ vì nằm ngoài danh sách của phiếu/SHARED_SYSTEMS_BAR §5, không phải kết luận OFL cấm dùng thương mại.

Nguồn máy, SHA-256, dependency gián tiếp, cạnh import và toàn văn giấy phép: [hồ sơ 188](../codex-queue/188-report.md), [inventory.json](../codex-queue/188/inventory.json), [nguồn và cách đếm](../codex-queue/188/sources.md). Chưa tích hợp Credits vào game trong phiếu chỉ được ghi tài liệu này.
'''
for a in data:
    game = a['base'].split('/')[-1]
    append += f'\n### {titles[game]} (`{a["base"]}`)\n\n' + header
    credit = f'[Credits {titles[game]}](../codex-queue/188/credits-{game}.md)'
    for r in a['records']:
        if r['kind'] == 'devDependency': continue
        name = r['name']
        repo = r['repository']['url'].removeprefix('git+').removesuffix('.git')
        src = f'[{name}]({repo}); `{r["packageJson"]}` và `{r["notices"][0]["path"]}`'
        lic = r['license'] + (' — **CỜ: ngoài danh sách**' if r['license'] == 'OFL-1.1' else '')
        use = a['base']
        if game == 'typing-defense' and name == 'three': use += '; khai báo dependency, **chưa tới bundle qua entry hiện tại**'
        if r['kind'] == 'devDependency-runtime': use += '; devDependency nhưng được mô-đun 3D nhập khi chơi'
        if name == 'a11y-dialog': use += '; quick-settings; **ba game chưa đồng bộ mô-đun này**'
        if name == 'focusable-selectors': use += '; gián tiếp a11y-dialog, mã đã nhúng trong ESM; chưa vào ba game'
        notice = ('Có: giữ nguyên bản quyền + OFL-1.1; ' if r['license'] == 'OFL-1.1' else 'Có: giữ nguyên bản quyền + MIT; ') + credit
        append += f'| `{name}` | {r["version"]} | {"phông + CSS" if name.startswith("@fontsource/") else "mã"} | {src} | {lic} | {use} | {notice} | Codex, 29/10/2026 |\n'
    if game != 'typing-defense':
        append += f'| meshoptimizer (`meshopt_decoder.module.js`, nhúng trong three) | 0.18, đi kèm three 0.170.0 | mã JS/WASM nhúng, không phải dependency npm riêng | [LICENSE v0.18](https://raw.githubusercontent.com/zeux/meshoptimizer/v0.18/LICENSE.md); `{a["base"]}/node_modules/three/examples/jsm/libs/meshopt_decoder.module.js` | MIT | {a["base"]}; model-loader | Có: bản quyền Arseny Kapoulkine và MIT riêng; {credit} | Codex, 29/10/2026 |\n'
    if game != 'game-kit':
        append += f'| `vite` (helper chạy trong bản chơi) | 7.3.7 | devDependency có mã chèn vào bundle | [Vite](https://github.com/vitejs/vite); `{a["base"]}/node_modules/vite/package.json` và `LICENSE.md` | MIT (Vite core) | {a["base"]}; modulepreload polyfill + preload helper | Có: bản quyền VoidZero Inc. và Vite contributors + MIT; {credit} | Codex, 29/10/2026 |\n'
    else:
        append += f'| KTX-Parse (nhúng) | bản trong three 0.170.0; chưa xác minh semver riêng, có SHA-256 | mã nhúng, nhánh tùy chọn | [LICENSE gốc](https://raw.githubusercontent.com/donmccurdy/KTX-Parse/main/LICENSE); `shared/game-kit/node_modules/three/examples/jsm/libs/ktx-parse.module.js` | MIT; **cần xác minh nguồn phiên bản nhúng** | kit KTX2Loader; ba game chưa nhập | Có: Don McCurdy + MIT nếu bật KTX2; {credit} | Codex, 29/10/2026 |\n'
        append += f'| zstddec / Zstandard (nhúng JS/WASM) | bản trong three 0.170.0; chưa xác minh semver riêng, có SHA-256 | mã nhúng, nhánh tùy chọn | [LICENSE gốc](https://raw.githubusercontent.com/donmccurdy/zstddec-wasm/main/LICENSE); `shared/game-kit/node_modules/three/examples/jsm/libs/zstddec.module.js` | MIT AND BSD-3-Clause; **cần xác minh nguồn phiên bản nhúng** | kit KTX2Loader; ba game chưa nhập | Có: Don McCurdy, Yann Collet/Facebook + toàn văn MIT/BSD nếu bật KTX2; {credit} | Codex, 29/10/2026 |\n'
append += '\nKhông tính gói build/test thuần vào bản chơi; danh sách và phiên bản đã loại ở inventory.json. Kit không phát hành độc lập. Basis Universal transcoder chưa được ba game phục vụ: README trong gói three ghi Apache-2.0; phải khóa bản JS/WASM và giữ LICENSE/NOTICE tương ứng khi triển khai KTX2. Chưa tải hay sửa thành phần nào.\n'
target = ROOT / 'docs/games/THIRD_PARTY.md'
current = target.read_text()
marker = '\n## Phiếu 188 · Kiểm thư viện mã và phông trong gói chạy (29/10/2026)'
if marker in current:
    raise SystemExit('Đã có phần 188; không tự ghi đè lần hai.')
target.write_text(current + append)

summary = {
    'declaredDependencies': {'dragon-hold': {'total':4,'MIT':1,'OFL-1.1':3},'typing-defense':{'total':3,'MIT':1,'OFL-1.1':2},'typing-survival':{'total':3,'MIT':1,'OFL-1.1':2},'game-kit':{'total':2,'MIT':2,'OFL-1.1':0}},
    'kitDevDependencyUsedAtRuntime': {'three@0.170.0':'MIT'},
    'currentGameRuntimeIncludingEmbedded': {'dragon-hold':{'total':6,'MIT':3,'OFL-1.1':3},'typing-defense':{'total':3,'MIT':1,'OFL-1.1':2},'typing-survival':{'total':5,'MIT':3,'OFL-1.1':2}},
    'uniqueNpmRuntimePackagesIncludingKit':8,
    'uniqueNpmLicenses':{'MIT':3,'OFL-1.1':5},
    'uniqueComponentsIncludingBuildHelpersAndOptionalKitVendors':12,
    'uniqueComponentLicenseExpressions':{'MIT':6,'OFL-1.1':5,'MIT AND BSD-3-Clause':1},
    'policyFlags':[n+'@'+r['version'] for n,r in records.items() if r['license']=='OFL-1.1'],
    'policyFlagUsageCount':7,
    'unresolvedVendorSemver':['ktx-parse (three@0.170.0)','zstddec (three@0.170.0)'],
    'gplAgplLgplUnknownOrCustomNpmLicenses':[],
}
(OUT / 'counts.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False,indent=2))
