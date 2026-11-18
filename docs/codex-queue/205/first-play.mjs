/** Run from parent: node --import ./games/.wt-ts-codex/node_modules/tsx/dist/loader.mjs docs/codex-queue/205/first-play.mjs */
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { crowdModelRequests, shipModelRequest } from '../../../games/.wt-ts-codex/src/view/models.ts';
import { boltModelRequests } from '../../../games/.wt-ts-codex/src/view/bolts.ts';
import { TRIAL_KIT, stageHeader, STANDARD_HEADER } from '../../../games/.wt-ts-codex/src/content/balance.ts';
import { CHAPTER_1 } from '../../../games/.wt-ts-codex/src/content/chapter-1.ts';
import { GUN_KEYS } from '../../../games/.wt-ts-codex/src/content/guns.ts';

const manifestPath = fileURLToPath(new URL('../../../games/.wt-ts-codex/public/assets/typing-survival/models/manifest.json', import.meta.url));
const raw = readFileSync(manifestPath);
const manifest = JSON.parse(raw);
const stage = CHAPTER_1.find((entry) => entry.id === 'c1-s1');
const guns = stageHeader(STANDARD_HEADER, stage, TRIAL_KIT.guns).kit.guns;
const budgetBytes = 4 * 1024 * 1024;
const cases = [];
for (const pilot of ['vanguard', 'draconis']) {
  for (const quality of ['high', 'medium']) {
    const ship = shipModelRequest(pilot, quality);
    const requests = [
      ...ship.ids.map((id) => ({ key: ship.kind + '/' + id, tier: ship.tier })),
      ...crowdModelRequests(quality).flatMap((request) => request.ids.map((id) => ({ key: 'enemies/' + id, tier: request.tier }))),
      ...boltModelRequests(quality, pilot === 'draconis', guns).flatMap((request) => request.spec.ids.map((id) => ({ key: 'skills/' + id, tier: request.tier }))),
    ];
    const files = [...new Map(requests.map(({ key, tier }) => {
      const file = manifest.models[key].tiers[tier];
      return [file.url, { key, tier, ...file }];
    })).values()];
    const modelBytes = files.reduce((sum, file) => sum + file.bytes, 0);
    const bytes = modelBytes + raw.length;
    cases.push({ pilot, quality, files, modelBytes, manifestBytes: raw.length, bytes, MiB: bytes / 1048576, MB: bytes / 1000000, overBudget: bytes > budgetBytes });
  }
}
console.log(JSON.stringify({ scope: 'Model requests at first load, including all crowd kinds and manifest; excludes JS, vocabulary, fonts and other media.', stage: stage.id, guns: guns.map((gun) => GUN_KEYS[gun]), budgetBytes, budgetDecimalBytes: 4000000, previousReportedMB: 9.06, cases }, null, 2));
