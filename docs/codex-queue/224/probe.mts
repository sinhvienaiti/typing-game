// Chạy bằng pnpm exec tsx trong tree/tmp; không mở server hoặc trình duyệt.
import { readFileSync, mkdirSync, rmSync, writeFileSync, symlinkSync } from 'node:fs';
import { resolve, join } from 'node:path';
import { pathToFileURL } from 'node:url';
import { build } from 'vite';
import config, { replacePortalOrigin } from '../vite.config.ts';
import { portalHome } from '../src/app/portal.ts';

const root = process.cwd();
const scratch = resolve('tmp/audit-vite');
mkdirSync(scratch, { recursive: true });
const results: Record<string, unknown> = {};
const values = [undefined, '', '   ', ' https://portal.example/path ', 'https://portal.ex ample/', 'https://portal.example/a b', 'https://por\ttal.example/', 'https://portal.example/\nbook', 'https://user@portal.example/', 'https://:pass@portal.example/', 'https://@portal.example/', 'https://:@portal.example/', 'javascript:alert(1)', 'data:text/html,x', 'file:///portal', 'ftp://portal.example/', 'ws://portal.example/', '/portal', '//portal.example/', 'http://portal.example:8080/path?q=1#book', 'https:portal.example'];
results.portal = values.map(value => {
  try { return { value: value ?? '(undefined)', result: portalHome(value) }; }
  catch (error) { return { value, error: String(error) }; }
});
const declaration = 'export const PARENT_ORIGIN = "old";';
results.declarations = ['', declaration, declaration + '\n' + declaration, declaration + '\r\n'].map(code => {
  try { return { code, result: replacePortalOrigin(code, '') }; }
  catch (error) { return { code, error: String(error) }; }
});
const cfg: any = await (config as any)({ mode: 'production', command: 'build' });
const plugin = cfg.plugins.find((p: any) => p.name === 'wordwoven-portal-origin');
const contract = join(root, 'src/kit/learning/contract.ts');
results.transformIds = [contract, contract+'?v=123', contract+'?import', contract.toUpperCase(), contract.replace('/tree/', '/alias-tree/')].map(id => {
  try { return { id, result: plugin.transform.call({error(message: string) { throw new Error(message); }}, declaration, id) }; }
  catch (error) { return { id, error: String(error) }; }
});
results.pluginHooks = Object.keys(plugin);
async function bundle(name: string, specifier: string, extra: object = {}) {
  const input = join(scratch, name+'.ts');
  writeFileSync(input, `export { PARENT_ORIGIN } from ${JSON.stringify(specifier)};`);
  try {
    const result: any = await build({ configFile: join(root,'vite.config.ts'), logLevel:'silent', ...extra,
      build: { outDir:join(scratch,name+'-out'),copyPublicDir:false,minify:false,
        rollupOptions:{input,preserveEntrySignatures:'strict',output:{manualChunks:()=>undefined}} } });
    const chunks=result.output.filter((o: any)=>o.type==='chunk');
    return { success:true, code:chunks.map((o: any)=>o.code).join('\n'), localHost:chunks.some((o: any)=>o.code.includes('typing-game.local')) };
  } catch (error) { return { success:false,error:String(error) }; }
}
try {
  results.realBuilds = {
    canonical: await bundle('canonical',contract),
    queryV: await bundle('query-v',contract+'?v=123'),
    queryImport: await bundle('query-import',contract+'?import'),
  };
  const alias=join(scratch,'alias-root');symlinkSync(root,alias,'dir');
  (results.realBuilds as any).symlinkConfig=await bundle('symlink-config',contract,{configFile:join(alias,'vite.config.ts')});
  // Đồ thị không đưa contract qua transform: plugin không có buildEnd guard.
  const unused=join(scratch,'unused.ts');writeFileSync(unused,'console.log("unused");');
  try {
    await build({configFile:join(root,'vite.config.ts'),logLevel:'silent',build:{outDir:join(scratch,'unused-out'),copyPublicDir:false,rollupOptions:{input:unused}}});
    results.unseenContractBuild={success:true};
  } catch(error) { results.unseenContractBuild={success:false,error:String(error)}; }
  results.devPlugin=(await (config as any)({mode:'development',command:'serve'})).plugins.map((p: any)=>p.name);
  // .env.production được tạo/xóa chỉ trong bản chép, không bao giờ ở worktree.
  const envFile=join(root,'.env.production');
  writeFileSync(envFile,'VITE_PORTAL_URL=https://env-file.example/path\n');
  try {
    results.envFile=await bundle('env-file',contract);
    process.env.VITE_PORTAL_URL='';
    results.envOverride=await bundle('env-override',contract);
  } finally { delete process.env.VITE_PORTAL_URL; rmSync(envFile); }
  console.log('AUDIT_JSON='+JSON.stringify(results));
} finally { rmSync(scratch,{recursive:true,force:true}); }
