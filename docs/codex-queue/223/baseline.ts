import {writeFileSync} from 'node:fs';
import {BOT_NAMES,M0_BOTS,BOTS} from '../../scripts/balance/bot';
writeFileSync('../../docs/codex-queue/223/bots-before.txt',JSON.stringify({BOT_NAMES,M0_BOTS,keys:Object.keys(BOTS)},null,2)+'\n');
