import test from 'node:test';
import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { inspectGlb, parseGlb } from '../../map-factory/registry/scan-assets.mjs';
import { CONFIG, scoreFace, scoreShape, scoreName, tokenize, unaccent, parseImageName,
  parseIndex, parseEnglishNames, rankCandidates, greedyMatch, parseAnswers, evaluate,
  markdown, parseOptions, validateOutput } from '../match.mjs';

test('face: sát mục tiêu đạt điểm tối đa; dùng ngưỡng chung 3000', () => {
  assert.equal(scoreFace(5700, 6000).score, CONFIG.faceReward);
  const small = scoreFace(2850, 2000);
  assert.equal(small.effectiveLimit, 3000);
  assert.equal(small.rawRatio, 1.425);
  assert.equal(small.score, CONFIG.faceReward);
});

test('face: hai biên được tính trong bậc; ngoài bậc bị trừ mạnh', () => {
  assert.equal(scoreFace(5500, 10000).inBand, true);
  assert.equal(scoreFace(10200, 10000).inBand, true);
  assert.ok(scoreFace(5499, 10000).score < -CONFIG.facePenalty);
  assert.ok(scoreFace(10201, 10000).score < -CONFIG.facePenalty);
  assert.throws(() => scoreFace(0, 4000));
});

test('face: bậc gần thực tế mạnh hơn bậc quá cao', () => {
  assert.ok(scoreFace(5700, 6000).score > scoreFace(5700, 10000).score);
  assert.ok(scoreFace(5700, 4000).score < 0);
});

test('hình: khoảng cách log đối xứng, giảm theo độ lệch', () => {
  assert.equal(scoreShape(2, 2).score, CONFIG.shapeWeight);
  assert.equal(scoreShape(2, 1).score, scoreShape(1, 2).score);
  assert.ok(scoreShape(1.1, 1).score > scoreShape(2, 1).score);
  assert.equal(scoreShape(2, 1).logRatio, Math.log(2));
  for (const value of [null, 0, NaN, Infinity]) assert.deepEqual(scoreShape(value, 1), { score: 0, logRatio: null, missing: true });
});

test('chữ: bỏ dấu Việt, số bản tải trùng và từ rỗng', () => {
  assert.equal(unaccent('Đá Thác Bạc'), 'da thac bac');
  assert.deepEqual(tokenize('stylized+wolf+3d+model (1).glb'), ['wolf']);
  assert.deepEqual(tokenize('wolf wolf wolf'), ['wolf']);
});

test('chữ: đồng nghĩa hai chiều và vật liệu yếu hơn danh từ', () => {
  assert.equal(scoreName('wolf.glb', 'Sói').score, CONFIG.nameWeight);
  assert.equal(scoreName('soi.glb', 'wolf').score, CONFIG.nameWeight);
  assert.equal(scoreName('bandana.glb', 'Băng đô').score, CONFIG.nameWeight);
  assert.equal(scoreName('goggles.glb', 'Kính').score, CONFIG.nameWeight);
  assert.equal(scoreName('purple.glb', 'violet').score, CONFIG.nameWeight);
  assert.equal(scoreName('yellow.glb', 'vàng').score, CONFIG.nameWeight);
  assert.equal(scoreName('boar.glb', 'piggy').score, 0);
  assert.deepEqual(tokenize('pinecone'), ['pine', 'cone']);
  for (const [english, vi] of [['bridge', 'cầu'], ['bamboo', 'tre'], ['feather', 'lông'],
    ['scaffold', 'giàn'], ['axe', 'rìu'], ['hat', 'nón'], ['cliff', 'vách'], ['waterfall', 'thác']]) {
    assert.equal(scoreName(english, vi).score, CONFIG.nameWeight);
  }
  assert.ok(scoreName('wooden+bridge.glb', 'bridge').score > scoreName('wooden+bridge.glb', 'wood').score);
  assert.equal(scoreName('3d+model.glb', 'wolf').score, 0);
  assert.equal(scoreName('wolf.glb', 'bridge').score, 0);
});

test('tên ảnh: gom góc và biến thể theo model, giữ nguyên id', () => {
  assert.deepEqual(parseImageName('loigoi_fire-feather_front.alpha.png'), { id: 'loigoi_fire-feather', game: 'loigoi', view: 'front', variant: 'alpha' });
  assert.equal(parseImageName('loigoi_fire-feather.flat.png').id, 'loigoi_fire-feather');
  assert.equal(parseImageName('rong_wolf_left.png').view, 'left');
  assert.equal(parseImageName('loigoi_tre_back.png').id, 'loigoi_tre');
  assert.equal(parseImageName('INDEX.md'), null);
});

test('INDEX: đọc danh sách đợt 1, bảng đợt 2 và multiview wildcard', () => {
  const labels = parseIndex('- `rong_wolf`: Sói Mục · Rồng Giữ Ải\n| `face 2000 - x/loigoi_seed.flat.png` | Hạt xanh | ghi chú |\n| `face 6000 - x/loigoi_tre_*.png` | Tướng Tre | |');
  assert.equal(labels.get('rong_wolf'), 'Sói Mục');
  assert.equal(labels.get('loigoi_seed'), 'Hạt xanh');
  assert.equal(labels.get('loigoi_tre'), 'Tướng Tre');
});

test('NAMES_EN: chỉ nối id chính xác trong từng game', () => {
  const names = parseEnglishNames('## Rồng (`games/dragon-hold`)\n| `shield` | Khiên | Thorn Shield |\n## Lời (`games/typing-defense`)\n| `shield` | Khiên | Bronze Shield |\n| `hero` | Tre | — |\n| `NPC_KIND.villager` | Dân | Villager |');
  assert.equal(names.get('rong_shield'), 'Thorn Shield');
  assert.equal(names.get('loigoi_shield'), 'Bronze Shield');
  assert.equal(names.has('loigoi_hero'), false);
  assert.equal(names.size, 2);
});

test('xếp hạng: cộng đúng ba thành phần và có dùng nhãn Việt/tên Anh', () => {
  const candidates = [
    { id: 'rong_other', faceLimit: 6000, ratio: 1, label: 'Cầu', image: 'a.png' },
    { id: 'rong_unknown', faceLimit: 6000, ratio: 1, englishName: 'Bridge', image: 'b.png' },
    { id: 'rong_wolf', faceLimit: 6000, ratio: 1, image: 'c.png' },
  ];
  const ranked = rankCandidates({ file: 'bridge.glb', triangles: 5700, ratio: 1 }, candidates);
  assert.equal(ranked[0].id, 'rong_other');
  assert.equal(ranked[1].name.score, CONFIG.nameWeight);
  for (const row of ranked) assert.equal(row.score, row.face.score + row.shape.score + row.name.score);
  assert.equal(candidates[0].score, undefined);
});

const row = (file, pairs) => ({ file, ranking: pairs.map(([id, score]) => ({ id, score })) });
test('ghép một-một: ma trận cố định, cặp điểm cao nhất trước', () => {
  const rows = [row('a', [['x', 9], ['y', 8], ['z', 2]]), row('b', [['x', 10], ['y', 4], ['z', 3]]), row('c', [['y', 7], ['z', 6], ['x', 1]])];
  const before = JSON.stringify(rows);
  assert.deepEqual(greedyMatch(rows).map(c => c.id), ['y', 'x', 'z']);
  assert.equal(JSON.stringify(rows), before);
});

test('ghép: duyệt toàn bộ ứng viên, không chỉ top-3; thiếu model thì null', () => {
  const rows = [row('a', [['x', 100]]), row('b', [['y', 99]]), row('c', [['z', 98]]),
    row('d', [['x', 4], ['y', 3], ['z', 2], ['w', 1]]), row('e', [['x', 0]]), row('f', [])];
  assert.deepEqual(greedyMatch(rows).map(c => c?.id ?? null), ['x', 'y', 'z', 'w', null, null]);
});

test('ghép: hòa điểm xử lý ổn định theo tên file rồi id', () => {
  const rows = [row('b', [['y', 5], ['x', 5]]), row('a', [['y', 5], ['x', 5]])];
  assert.deepEqual(greedyMatch(rows).map(c => c.id), ['y', 'x']);
  assert.deepEqual(greedyMatch([]), []);
});

function makeGlb(json, bin = Buffer.from([0, 0, 0, 0])) {
  const text = Buffer.from(JSON.stringify(json));
  const jsonBytes = Buffer.alloc(Math.ceil(text.length / 4) * 4, 32);
  text.copy(jsonBytes);
  const header = Buffer.alloc(20);
  header.writeUInt32LE(0x46546c67, 0); header.writeUInt32LE(2, 4);
  header.writeUInt32LE(28 + jsonBytes.length + bin.length, 8);
  header.writeUInt32LE(jsonBytes.length, 12); header.writeUInt32LE(0x4e4f534a, 16);
  const binHeader = Buffer.alloc(8);
  binHeader.writeUInt32LE(bin.length, 0); binHeader.writeUInt32LE(0x004e4942, 4);
  return Buffer.concat([header, jsonBytes, binHeader, bin]);
}

test('GLB trong RAM: đọc header, JSON/BIN, cảnh 0, nhân instance và biến đổi bounds', () => {
  const bytes = makeGlb({ asset: { version: '2.0' }, scene: 1, scenes: [{ nodes: [0, 1] }, { nodes: [2] }],
    nodes: [{ mesh: 0 }, { mesh: 0, translation: [4, 0, 0], scale: [2, 1, 1] }, { mesh: 0 }],
    meshes: [{ primitives: [{ attributes: { POSITION: 0 }, indices: 1 }] }],
    accessors: [{ count: 3, componentType: 5126, min: [0, 0, 0], max: [1, 2, 3] }, { count: 6 }] });
  const hash = createHash('md5').update(bytes).digest('hex');
  assert.deepEqual(parseGlb(bytes).bin, Buffer.from([0, 0, 0, 0]));
  const info = inspectGlb(bytes);
  assert.equal(info.triangles, 4);
  assert.equal(info.meshInstances, 2);
  assert.deepEqual(info.bounds.size, [6, 2, 3]);
  assert.equal(Math.max(info.bounds.size[0], info.bounds.size[2]) / info.bounds.size[1], 3);
  assert.equal(createHash('md5').update(bytes).digest('hex'), hash);
  const corrupt = Buffer.from(bytes); corrupt.writeUInt32LE(1, 8);
  assert.throws(() => inspectGlb(corrupt), /Độ dài/);
});

test('đánh giá: tính cả bản trùng; không coi mục CLI là file .glb', () => {
  const answers = parseAnswers('| Game | `loigoi_hat` | face 2000 | `hat.glb` | 2800 | x |\n| Game | `loigoi_hat` | face 2000 | `hat (1).glb` | 2790 | x |\n| Game | `loigoi_club` | face 2000 | `(Tripo CLI test)` | 2780 | x |');
  const result = { rows: [{ file: 'hat.glb', triangles: 2800, top3: [{ id: 'loigoi_hat' }], assigned: { id: 'loigoi_hat' } },
    { file: 'hat (1).glb', triangles: 2790, top3: [{ id: 'loigoi_else' }, { id: 'loigoi_hat' }], assigned: { id: 'loigoi_else' } }] };
  const metrics = evaluate(result, answers);
  assert.equal(answers.length, 2);
  assert.equal(metrics.total, 2);
  assert.equal(metrics.top1, 1); assert.equal(metrics.top3, 2); assert.equal(metrics.assigned, 1);
  assert.equal(metrics.details.every(d => d.trianglesMatch), true);
  assert.deepEqual(metrics.missingFiles, []);
});

test('CLI: cờ bắt buộc, giá trị thiếu, cờ lạ và lặp', () => {
  assert.deepEqual(parseOptions(['--upload', 'u', '--glb', 'g', '--out', 'r.json']), { upload: 'u', glb: 'g', out: 'r.json' });
  for (const args of [[], ['--upload'], ['--upload', '--out'], ['--url', 'x'], ['--upload', 'a', '--upload', 'b']]) {
    assert.throws(() => parseOptions(args));
  }
});

test('đầu ra: chặn ghi vào media và ghi đè; không tạo file trong test', async () => {
  await assert.rejects(validateOutput('tools/tripo-match/README.md', 'tools/tripo-match/test'), /\.json/);
  await assert.rejects(validateOutput('tools/tripo-match/test/result.json', 'tools/tripo-match/test'), /cây media/);
  await assert.rejects(validateOutput('package.json', 'tools/tripo-match/test'), /đã tồn tại/);
});

test('Markdown/JSON: trường hợp 0 GLB, roundtrip JSON và escape dấu bảng', () => {
  const result = { rows: [], candidates: [], warnings: [], mediaIntegrity: { filesChecked: 0 } };
  assert.match(markdown(result), /^0 GLB/);
  assert.deepEqual(JSON.parse(JSON.stringify(result)), result);
  result.rows.push({ file: 'a|b.glb', triangles: null, ratio: null, top3: [], assigned: null, error: 'lỗi\nđọc' });
  assert.match(markdown(result), /a\\\|b\.glb/);
  assert.match(markdown(result), /LỖI: lỗi đọc/);
});
