"""Build a static Firefly review gallery; importing this module performs no I/O."""
import argparse
import collections
import glob
import html
import json
import re
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit

REPO = Path(__file__).resolve().parents[2]
ROOT = REPO.parent
DEFAULT_SPRINT = REPO / 'games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05'
DEFAULT_OUT = ROOT / 'typing-game-review/owner-review/2026-11-05/tu-tien/firefly-gallery/index.html'
DEFAULT_LEAD = ('{jobs} việc video, {takes} bản, {stills} ảnh tĩnh. '
                'Rê chuột vào video để phát (mỗi lúc một video); bấm vào để xem to.')
SECTIONS = [
    ('ult', 'Tuyệt kỹ và cột trụ'),
    ('expansion', '30 kỹ năng mới (diện rộng, pháp tướng, thần thú, pháp bảo)'),
    ('crescent', 'Lưỡi liềm kiếm khí 14 hệ'),
    ('element', 'Vệt chém, dấu đất, vũ khí theo hệ'),
    ('dark', 'Ám màu A (đen, viền đỏ thẫm)'),
    ('material', 'Chất liệu và clip khác (bộ W2 sáng nay, Hỏa, cut-in)'),
    ('rejected', 'Đã loại'),
]


def merge_jobs(documents):
    """First job with an ID wins, including jobs held in a later queue."""
    jobs = {}
    for document in documents:
        if not isinstance(document, dict):
            continue
        for key in ('jobs', 'held'):
            for job in document.get(key, []):
                if isinstance(job, dict) and 'id' in job:
                    jobs.setdefault(job['id'], job)
    return jobs


def parse_lab_usage(manifests):
    """Manifest text, rather than its schema, determines which jobs are in lab."""
    usage = collections.defaultdict(set)
    for folder, raw in manifests.items():
        for job_id in re.findall(r'/video/([A-Za-z0-9-]+)/take', raw):
            usage[job_id].add(folder)
    return dict(usage)


def section_of(job_id, expansion):
    if job_id.endswith('-crescent-sym'):
        return 'crescent'
    if job_id in expansion:
        return 'expansion'
    if job_id.startswith(('i2v-ult-', 'i2v-pillar-')):
        return 'ult'
    if job_id.startswith('dark-'):
        return 'dark'
    if job_id.startswith('i2v-'):
        return 'element'
    return 'material'


def state_of(job_id, usage, notes, stone):
    if usage.get(job_id):
        return 'in', 'Trong lab: ' + ', '.join(sorted(usage[job_id]))
    if job_id in stone:
        return 'out', 'Đã gỡ: Firefly vẽ nền đá dính vào clip'
    if job_id in notes:
        return 'out', notes[job_id]
    return 'no', 'Chưa vào lab'


def group_cards(videos, rejected_videos, jobs, usage, originals, config):
    """Pure grouping and status logic over already collected URLs and metadata."""
    cards = {key: [] for key, _ in SECTIONS}
    expansion = {key for key, job in jobs.items()
                 if str(job.get('source', '')).startswith('Gemini design')}
    stone = set(config.get('stone', []))
    for job_id, takes in sorted(videos.items()):
        if not takes:
            continue
        state, tag = state_of(job_id, usage, config.get('notes', {}), stone)
        section = 'rejected' if state == 'out' else section_of(job_id, expansion)
        cards[section].append(dict(id=job_id, takes=list(takes), state=state, tag=tag,
                                  use=jobs.get(job_id, {}).get('use', ''),
                                  still=originals.get(job_id)))
    # Exact directory names only; no wildcard discovery of rejected batches.
    for directory, reason in config.get('rejectedDirs', {}).items():
        for job_id, takes in sorted(rejected_videos.get(directory, {}).items()):
            if takes:
                cards['rejected'].append(dict(id=job_id, takes=list(takes), state='out',
                                             tag=reason, use='', still=None))
    return cards


def summarize(cards, stills):
    return dict(counts={key: len(cards[key]) for key, _ in SECTIONS},
                takes=sum(len(card['takes']) for group in cards.values() for card in group),
                stills=len(stills),
                states=collections.Counter(card['state'] for group in cards.values() for card in group))


def load_notes(path):
    config = dict(title='Firefly · xem lại', h1='Ảnh và video Firefly', lead=DEFAULT_LEAD,
                  notes={}, stone=[], rejectedDirs={})
    if path:
        supplied = json.loads(Path(path).read_text(encoding='utf-8'))
        if not isinstance(supplied, dict):
            raise ValueError('notes phải là một JSON object')
        config.update(supplied)
    for key in ('title', 'h1', 'lead'):
        if not isinstance(config[key], str):
            raise ValueError(f'{key} phải là chuỗi')
    for key in ('notes', 'rejectedDirs'):
        if not isinstance(config[key], dict) or not all(
                isinstance(k, str) and isinstance(v, str) for k, v in config[key].items()):
            raise ValueError(f'{key} phải là object gồm các chuỗi')
    if not isinstance(config['stone'], list) or not all(isinstance(k, str) for k in config['stone']):
        raise ValueError('stone phải là danh sách ID')
    for name in config['rejectedDirs']:
        if name in ('', '.', '..') or '/' in name or '\\' in name:
            raise ValueError('rejectedDirs chỉ nhận tên thư mục con trực tiếp của sprint')
    return config


def file_url(path, root):
    # All generated media links must be reachable from the server root.
    return '/' + quote(Path(path).resolve().relative_to(root.resolve()).as_posix(), safe='/')


def read_jobs(pattern):
    documents = []
    pattern_path = Path(pattern)
    for filename in glob.glob(str(pattern_path if pattern_path.is_absolute() else REPO / pattern)):
        try:
            documents.append(json.loads(Path(filename).read_text(encoding='utf-8')))
        except (OSError, ValueError):
            continue
    return merge_jobs(documents)


def scan_videos(directory, root):
    if not directory.is_dir():
        return {}
    return {folder.name: [file_url(p, root) for p in sorted(folder.glob('*.mp4')) if p.is_file()]
            for folder in sorted(directory.iterdir()) if folder.is_dir()}


def still_of(job, sprint):
    for key in ('image', 'still'):
        value = job.get(key) or ''
        if not value:
            continue
        # Queue annotations can follow the still path in parentheses.
        if key == 'still':
            value = re.split(r'\s+\(', value, maxsplit=1)[0]
        parsed = urlsplit(value)
        local = Path(unquote(parsed.path))
        candidates = [sprint / 'stills/skills' / local.name]
        if not parsed.scheme and not parsed.netloc:
            candidates += [local] if local.is_absolute() else [sprint / local, REPO / local]
        for candidate in candidates:
            if candidate.is_file():
                return candidate
    return None


def collect_gallery(sprint, lab, jobs_pattern, root, config):
    jobs = read_jobs(jobs_pattern)
    manifests = {p.parent.name: p.read_text(encoding='utf-8')
                 for p in (lab / 'vfx').glob('*/manifest.json')}
    usage = parse_lab_usage(manifests)
    videos = scan_videos(sprint / 'video', root)
    rejected = {name: scan_videos(sprint / name, root) for name in config['rejectedDirs']}
    originals = {}
    for job_id in videos:
        still = still_of(jobs.get(job_id, {}), sprint)
        if still:
            originals[job_id] = file_url(still, root)
    stills = [file_url(p, root) for p in sorted((sprint / 'stills/skills').glob('*'))
              if p.is_file() and p.suffix in ('.png', '.jpg')]
    return group_cards(videos, rejected, jobs, usage, originals, config), stills


STYLE = '''
:root{--bg:#0e0f12;--card:#17191e;--line:#2a2d35;--text:#e8e6e1;--dim:#9a9890;--in:#4fbf8a;--no:#e0b44c;--out:#c8665a}
body{margin:0;background:var(--bg);color:var(--text);font:14px/1.45 -apple-system,system-ui,sans-serif}
nav{position:sticky;top:0;z-index:2;background:#0e0f12ee;border-bottom:1px solid var(--line);padding:10px 16px;display:flex;flex-wrap:wrap;gap:6px 14px;align-items:center}
nav a{color:var(--text);text-decoration:none;font-size:13px} nav b{color:var(--no);font-weight:600}
nav .f{margin-left:auto;display:flex;gap:6px} nav button{background:var(--card);color:var(--text);border:1px solid var(--line);border-radius:6px;padding:4px 10px;cursor:pointer} nav button.on{border-color:var(--no)}
main{padding:8px 16px 60px} h1{font-size:20px;margin:16px 0 4px} .lead{color:var(--dim);margin:0 0 8px}
h2{font-size:17px;margin:28px 0 10px;padding-top:8px} h2 small{color:var(--dim);font-weight:400}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(420px,1fr));gap:12px}
.card{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--no);border-radius:8px;padding:8px}
.card.in{border-left-color:var(--in)} .card.out{border-left-color:var(--out);opacity:.85}
.card header{display:flex;justify-content:space-between;gap:8px;align-items:baseline;margin-bottom:6px} code{font-size:12px;word-break:break-all}
.tag{font-size:12px;color:var(--dim);text-align:right} .in .tag{color:var(--in)} .out .tag{color:var(--out)}
.media{display:flex;gap:6px;overflow-x:auto} figure{margin:0;flex:0 0 auto;width:200px} figure video,figure img{width:200px;height:113px;object-fit:contain;background:#000;border-radius:4px;display:block;cursor:zoom-in}
figcaption{font-size:11px;color:var(--dim)} .card p{font-size:12px;color:var(--dim);margin:6px 0 0}
.thumbs{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:8px} .thumbs a{color:var(--dim);font-size:11px;text-decoration:none;word-break:break-all} .thumbs img{width:100%;height:110px;object-fit:contain;background:#000;border-radius:4px;display:block}
#big{position:fixed;inset:0;background:#000d;display:none;align-items:center;justify-content:center;z-index:5} #big video{max-width:94vw;max-height:90vh}
@media (max-width:480px){.grid{grid-template-columns:1fr} figure,figure video,figure img{width:150px}}
'''

SCRIPT = '''
// One video plays at a time; previews play only while hovered.
let cur=null;
const big=document.getElementById('big'),bv=big.querySelector('video');
document.querySelectorAll('.card video').forEach(v=>{
  v.dataset.src=v.getAttribute('src');
  v.addEventListener('mouseenter',()=>{
    if(big.style.display==='flex')return;
    if(cur&&cur!==v){cur.pause();cur.removeAttribute('src');cur.load();cur.src=cur.dataset.src}
    cur=v;v.play().catch(()=>{});
  });
  v.addEventListener('mouseleave',()=>v.pause());
});
document.addEventListener('click',ev=>{
  const v=ev.target.closest('.card video');
  if(v){if(cur)cur.pause();bv.src=v.src;big.style.display='flex';bv.play().catch(()=>{})}
  else if(ev.target===big){big.style.display='none';bv.pause();bv.removeAttribute('src');bv.load()}
});
document.querySelectorAll('nav button').forEach(b=>b.onclick=()=>{
  document.querySelectorAll('nav button').forEach(x=>x.classList.toggle('on',x===b));
  const f=b.dataset.f;
  document.querySelectorAll('.card').forEach(c=>c.style.display=(f==='all'||c.dataset.state===f)?'':'none');
});
'''


def render_html(cards, stills, config):
    e = html.escape
    totals = summarize(cards, stills)
    counts = totals['counts']
    lead = config['lead']
    for key, value in dict(jobs=sum(counts.values()), takes=totals['takes'], stills=len(stills)).items():
        lead = lead.replace('{' + key + '}', str(value))
    nav = ''.join(f'<a href="#{s}">{e(t)} <b>{counts[s]}</b></a>' for s, t in SECTIONS)
    nav += f'<a href="#stills">Ảnh tĩnh kỹ năng <b>{len(stills)}</b></a>'
    parts = []
    for section, title in SECTIONS:
        if not cards[section]:
            continue
        parts.append(f'<h2 id="{section}">{e(title)} <small>{counts[section]} việc</small></h2><div class="grid">')
        for card in cards[section]:
            videos = ''.join(f'<figure><video src="{e(v)}" muted loop playsinline preload="none"></video><figcaption>bản {i + 1}</figcaption></figure>'
                             for i, v in enumerate(card['takes']))
            still = (f'<figure class="still"><a href="{e(card["still"])}" target="_blank"><img src="{e(card["still"])}" loading="lazy"></a><figcaption>ảnh gốc</figcaption></figure>'
                     if card['still'] else '')
            parts.append(f'<article class="card {card["state"]}" data-state="{card["state"]}" data-id="{e(card["id"])}"><header><code>{e(card["id"])}</code><span class="tag">{e(card["tag"])}</span></header>'
                         f'<div class="media">{still}{videos}</div>' + (f'<p>{e(card["use"])}</p>' if card['use'] else '') + '</article>')
        parts.append('</div>')
    parts.append(f'<h2 id="stills">Ảnh tĩnh kỹ năng <small>{len(stills)} ảnh</small></h2><div class="thumbs">')
    for still in stills:
        name = unquote(still.rsplit('/', 1)[-1])
        parts.append(f'<a href="{e(still)}" target="_blank" title="{e(name)}"><img src="{e(still)}" loading="lazy"><span>{e(name)}</span></a>')
    parts.append('</div>')
    return f'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(config['title'])}</title><style>{STYLE}</style></head><body>
<nav>{nav}<span class="f"><button data-f="all" class="on">Tất cả</button><button data-f="in">Trong lab</button><button data-f="no">Chưa vào lab</button><button data-f="out">Đã loại</button></span></nav>
<main><h1>{e(config['h1'])}</h1><p class="lead">{e(lead)}</p>
{''.join(parts)}</main><div id="big"><video controls loop muted playsinline preload="none"></video></div>
<script>{SCRIPT}</script></body></html>'''


def main(argv=None):
    parser = argparse.ArgumentParser(description='Dựng trang xem lại ảnh và video Firefly.')
    parser.add_argument('--sprint', type=Path, default=DEFAULT_SPRINT)
    parser.add_argument('--lab', type=Path, help='Mặc định: thư mục cha của --sprint.')
    parser.add_argument('--jobs', default='docs/work/tasks/*.json', help='Glob tính từ gốc repo.')
    parser.add_argument('--root', type=Path, default=ROOT, help='Gốc htdocs để tính URL.')
    parser.add_argument('--out', type=Path, default=DEFAULT_OUT)
    parser.add_argument('--notes', type=Path, help='JSON chữ trên trang và các việc đã loại.')
    args = parser.parse_args(argv)
    try:
        config = load_notes(args.notes)
        cards, stills = collect_gallery(args.sprint, args.lab or args.sprint.parent,
                                       args.jobs, args.root, config)
        page = render_html(cards, stills, config)
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(page, encoding='utf-8')
    except (OSError, ValueError) as error:
        parser.error(str(error))
    totals = summarize(cards, stills)
    print(args.out, totals['counts'], 'takes', totals['takes'], 'stills', totals['stills'],
          'states', totals['states'])
    print('not in lab:', [c['id'] for group in cards.values() for c in group if c['state'] == 'no'])


if __name__ == '__main__':
    main()
