"""Firefly's conditional licence survives the existing render/release copy chain."""
import copy
import json
from pathlib import Path

import pytest

from build import ledger, licence_check, policy, release
from firefly import main
from firefly.tests.test_firefly import SID, hits


def test_firefly_render_release_licence(tmp_path):
    assert policy.classify('LicenseRef-Adobe-Firefly-owner') == 'allowed'
    inbox, out = tmp_path / 'inbox', tmp_path / 'out'
    hits(inbox / 'dragon-hold' / SID / 'owner.wav')
    assert main(['ingest', '--game', 'dragon-hold', '--id', SID, '--inbox', str(inbox),
                 '--out', str(out), '--run', 'licence']) == 0
    run = out / 'dragon-hold' / SID / 'licence'
    art, public = out / 'art-src/audio', out / 'public'
    release.release(run, None, art, public)
    assert licence_check.main(['--art-src', str(art), '--public', str(public)]) == 0
    recipe = json.loads((run / 'recipe.json').read_text())
    original_copy = Path(recipe['layers'][0]['source']['licenceText'])
    assert (art / 'licences/adobe-firefly-owner-2026-10-29.txt').read_bytes() == original_copy.read_bytes()
    rows = ledger.read_rows(art / 'licences.jsonl')
    for change, expected in [({'model': 'Partner Audio Model'}, 'adobe-model'),
                              ({'model': ''}, 'adobe-model'),
                              ({'raw_redistribution_allowed': True}, 'adobe-raw')]:
        bad = copy.deepcopy(rows)
        for row in bad:
            row.update(change)
        (art / 'licences.jsonl').write_text(''.join(json.dumps(r) + '\n' for r in bad))
        errors = licence_check.check(art, public)
        assert any(p.code == expected for p in errors)
    (art / 'licences.jsonl').write_text(''.join(json.dumps(r) + '\n' for r in rows))
    assert not [p for p in licence_check.check(art, public) if p.severity == 'error']


@pytest.mark.parametrize('model,allowed', [('Adobe Firefly Audio Model', True),
    ('Adobe Firefly Audio Model v2', True), ('Partner Adobe Firefly Audio Model', False),
    ('Adobe Firefly Audio ModelPartner', False), (None, False)])
def test_model_prefix(model, allowed, tmp_path):
    checker = licence_check.Checker(tmp_path, require_files=False)
    checker._check_row('test', {'key': 'test:source', 'licence': 'LicenseRef-Adobe-Firefly-owner',
                               'model': model, 'raw_redistribution_allowed': False}, [])
    assert (not checker.problems) == allowed
