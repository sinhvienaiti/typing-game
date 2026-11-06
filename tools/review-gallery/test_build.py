"""Regression checks using only the standard library and temporary fixtures."""
import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path
from unittest.mock import patch

BUILD = Path(__file__).resolve().with_name('build.py')
spec = importlib.util.spec_from_file_location('review_gallery_build', BUILD)
gallery = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gallery)


class GalleryHTML(HTMLParser):
    def __init__(self, page):
        super().__init__()
        self.nav = []
        self.cards = []
        self.videos = []
        self.originals = []
        self.in_nav = False
        self.in_still = False
        self.feed(page)

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if tag == 'nav':
            self.in_nav = True
        if tag == 'a' and self.in_nav:
            self.nav.append(attrs['href'])
        if tag == 'article':
            self.cards.append((attrs['data-id'], attrs['data-state']))
        if tag == 'video' and 'src' in attrs:
            self.videos.append(attrs)
        if tag == 'figure':
            self.in_still = attrs.get('class') == 'still'
        if tag == 'img' and self.in_still:
            self.originals.append(attrs['src'])

    def handle_endtag(self, tag):
        if tag == 'nav':
            self.in_nav = False
        if tag == 'figure':
            self.in_still = False


class BuildTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='review-gallery-test-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.lab = self.root / 'repo/art-src/lab'
        self.sprint = self.lab / 'sprint with spaces'
        self.in_id = 'i2v-ult-in'
        self.stone_id = 'dark-stone'
        self.pending_id = 'mist-unused'
        self.write(self.sprint / f'video/{self.in_id}/take2.mp4')
        self.write(self.sprint / f'video/{self.in_id}/take1.mp4')
        self.write(self.sprint / f'video/{self.stone_id}/take1.mp4')
        self.write(self.sprint / f'video/{self.pending_id}/take1.mp4')
        self.write(self.sprint / 'video/empty/README.txt')
        self.write(self.sprint / 'video-rejected-dark-purple/old-dark/take1.mp4')
        self.write(self.sprint / 'video-rejected-khac/ignored/take1.mp4')
        self.image = self.write(self.sprint / 'stills/skills/in.png')
        self.still = self.write(self.sprint / 'stills/skills/pending-clean.jpg')
        self.write(self.sprint / 'stills/skills/not-an-image.txt')
        self.jobs_path = self.write(self.root / 'jobs.json', json.dumps({
            'jobs': [
                {'id': self.in_id, 'image': 'http://127.0.0.1:8864/still/in.png', 'use': '<đẹp>&'},
                {'id': self.stone_id, 'image': 'missing.png', 'still': 'stills/skills/missing.jpg'},
            ],
            'held': [{'id': self.pending_id, 'still': 'stills/skills/pending-clean.jpg (đã duyệt)'}],
        }))
        self.write(self.lab / 'vfx/zeta/manifest.json', json.dumps({
            'anySchema': f'/sprint/video/{self.in_id}/take1.mp4',
            'unrelated': f'/video/{self.pending_id}/preview.mp4',
        }))
        self.write(self.lab / 'vfx/alpha/manifest.json', f'/video/{self.in_id}/take2.mp4')
        self.notes_path = self.write(self.root / 'notes.json', json.dumps({
            'title': 'Đợt kiểm thử', 'h1': 'Ảnh & video',
            'lead': '{jobs} việc video, {takes} bản, {stills} ảnh tĩnh.',
            'notes': {}, 'stone': [self.stone_id],
            'rejectedDirs': {'video-rejected-dark-purple': 'Đã loại vì tím'},
        }, ensure_ascii=False))
        self.config = gallery.load_notes(self.notes_path)

    def write(self, path, text='fixture'):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding='utf-8')
        return path

    def collect(self, config=None):
        return gallery.collect_gallery(self.sprint, self.lab, str(self.jobs_path),
                                       self.root, self.config if config is None else config)

    def test_groups_counts_and_states(self):
        cards, stills = self.collect()
        totals = gallery.summarize(cards, stills)
        self.assertEqual(totals['counts'], dict(ult=1, expansion=0, crescent=0, element=0,
                                              dark=0, material=1, rejected=2))
        self.assertEqual(totals['takes'], 5)
        self.assertEqual(totals['stills'], 2)
        self.assertEqual(totals['states'], {'in': 1, 'out': 2, 'no': 1})
        by_id = {c['id']: c for group in cards.values() for c in group}
        self.assertEqual(by_id[self.in_id]['tag'], 'Trong lab: alpha, zeta')
        self.assertTrue(by_id[self.stone_id]['tag'].startswith('Đã gỡ:'))
        self.assertEqual(by_id[self.pending_id]['tag'], 'Chưa vào lab')
        self.assertEqual(by_id['old-dark']['tag'], 'Đã loại vì tím')
        self.assertNotIn('ignored', by_id)
        self.assertNotIn('empty', by_id)
        self.assertTrue(by_id[self.in_id]['takes'][0].endswith('/take1.mp4'))
        self.assertTrue(by_id[self.in_id]['still'].endswith('/in.png'))
        self.assertTrue(by_id[self.pending_id]['still'].endswith('/pending-clean.jpg'))
        self.assertIsNone(by_id[self.stone_id]['still'])

    def test_original_images_require_existing_files(self):
        for job in [dict(image=str(self.image)), dict(image='stills/skills/in.png'),
                    dict(still='stills/skills/in.png'), dict(still=str(self.image)),
                    dict(image='absent.png', still='stills/skills/in.png')]:
            with self.subTest(job=job):
                self.assertEqual(gallery.still_of(job, self.sprint), self.image)
        self.assertIsNone(gallery.still_of({'image': 'absent.png'}, self.sprint))
        self.assertIsNone(gallery.still_of({'still': 'stills/skills/absent.png'}, self.sprint))
        self.assertIsNone(gallery.still_of({}, self.sprint))

    def test_cli_outputs_portable_html_and_all_navigation(self):
        out = self.root / 'output/index.html'
        result = subprocess.run([
            sys.executable, '-B', str(BUILD), '--sprint', str(self.sprint),
            '--lab', str(self.lab), '--jobs', str(self.jobs_path), '--root', str(self.root),
            '--out', str(out), '--notes', str(self.notes_path),
        ], cwd=self.root, text=True, capture_output=True, check=True)
        page = out.read_text(encoding='utf-8')
        parsed = GalleryHTML(page)
        self.assertEqual(parsed.nav, ['#ult', '#expansion', '#crescent', '#element',
                                      '#dark', '#material', '#rejected', '#stills'])
        self.assertEqual(dict(parsed.cards), {self.in_id: 'in', self.stone_id: 'out',
                                             self.pending_id: 'no', 'old-dark': 'out'})
        self.assertEqual(len(parsed.videos), 5)
        self.assertEqual(len(parsed.originals), 2)
        self.assertTrue(all(v['preload'] == 'none' and 'autoplay' not in v for v in parsed.videos))
        self.assertIn('mouseenter', page)
        self.assertIn('4 việc video, 5 bản, 2 ảnh tĩnh.', page)
        self.assertIn('<title>Đợt kiểm thử</title>', page)
        self.assertIn('<h1>Ảnh &amp; video</h1>', page)
        self.assertIn('&lt;đẹp&gt;&amp;', page)
        self.assertIn('sprint%20with%20spaces', page)
        self.assertNotIn('/Volumes', page)
        self.assertNotIn(str(self.root), page)
        self.assertNotIn('ignored', page)
        self.assertNotIn('missing.png', page)
        self.assertIn('takes 5 stills 2', result.stdout)

    def test_cli_without_notes_infers_lab_from_custom_sprint(self):
        out = self.root / 'generic.html'
        subprocess.run([sys.executable, '-B', str(BUILD), '--sprint', str(self.sprint),
                        '--jobs', str(self.jobs_path), '--root', str(self.root), '--out', str(out)],
                       cwd=self.root, capture_output=True, check=True)
        parsed = GalleryHTML(out.read_text(encoding='utf-8'))
        self.assertEqual(dict(parsed.cards), {self.in_id: 'in', self.stone_id: 'no', self.pending_id: 'no'})
        self.assertEqual(self.config['title'], 'Đợt kiểm thử')

    def test_pure_classification_and_precedence(self):
        videos = {key: ['/take.mp4'] for key in ('new-crescent-sym', 'i2v-ult-new',
                  'i2v-ult-a', 'i2v-pillar-a', 'dark-a', 'i2v-a', 'material-a', 'noted')}
        videos['empty'] = []
        jobs = {key: {'source': 'Gemini design batch'} for key in ('new-crescent-sym', 'i2v-ult-new')}
        config = dict(stone=['i2v-ult-a'], notes={'i2v-ult-a': 'loại', 'noted': 'Anh đã loại'}, rejectedDirs={})
        inputs = (videos, jobs, config)
        before = copy.deepcopy(inputs)
        cards = gallery.group_cards(videos, {}, jobs, {'i2v-ult-a': {'lab'}}, {}, config)
        self.assertEqual(inputs, before)
        self.assertEqual({k: [c['id'] for c in v] for k, v in cards.items()}, {
            'ult': ['i2v-pillar-a', 'i2v-ult-a'], 'expansion': ['i2v-ult-new'],
            'crescent': ['new-crescent-sym'], 'element': ['i2v-a'], 'dark': ['dark-a'],
            'material': ['material-a'], 'rejected': ['noted'],
        })
        self.assertEqual(cards['ult'][1]['state'], 'in')
        self.assertEqual(cards['rejected'][0]['tag'], 'Anh đã loại')

    def test_merge_jobs_and_repo_relative_glob(self):
        self.assertEqual(gallery.merge_jobs([[], {'jobs': [None, {'id': 'a', 'use': 'first'}],
                          'held': [{'id': 'b'}]}, {'jobs': [{'id': 'a', 'use': 'second'}]}]),
                         {'a': {'id': 'a', 'use': 'first'}, 'b': {'id': 'b'}})
        with patch.object(gallery.glob, 'glob', return_value=[str(self.jobs_path)]) as paths:
            self.assertEqual(len(gallery.read_jobs('docs/work/tasks/*.json')), 3)
        paths.assert_called_once_with(str(gallery.REPO / 'docs/work/tasks/*.json'))

    def test_notes_directory_names_are_literal(self):
        config = dict(self.config, rejectedDirs={'video-rejected-*': 'literal'})
        cards, _ = self.collect(config)
        self.assertEqual([c['id'] for c in cards['rejected']], [self.stone_id])
        for name in ('../elsewhere', '/absolute', 'nested/dir', '..', 'nested\\dir'):
            with self.subTest(name=name):
                self.notes_path.write_text(json.dumps({'rejectedDirs': {name: 'bad'}}))
                with self.assertRaises(ValueError):
                    gallery.load_notes(self.notes_path)

    def test_empty_sprint_keeps_navigation(self):
        cards, stills = gallery.collect_gallery(self.root / 'empty', self.root / 'lab',
                                              str(self.root / 'no-jobs-*.json'), self.root,
                                              gallery.load_notes(None))
        self.assertEqual(sum(gallery.summarize(cards, stills)['counts'].values()), 0)
        self.assertEqual(len(GalleryHTML(gallery.render_html(cards, stills, self.config)).nav), 8)


if __name__ == '__main__':
    unittest.main()
