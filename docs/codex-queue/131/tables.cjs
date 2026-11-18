const fs=require('node:fs');const path=require('node:path');const cp=require('node:child_process');
const ts=require('../../../games/.wt-dh-codex/node_modules/typescript');
const root=path.resolve(__dirname,'../../../games/.wt-dh-codex');
const before=JSON.parse(fs.readFileSync(path.join(__dirname,'before.json'),'utf8'));
const allowed=/^src\/(ui|app|view|content)\//;
const vi=/[À-ÃÈ-ÊÌ-ÍÒ-ÕÙ-ÚÝà-ãè-êì-íò-õù-úýĂăĐđĨĩŨũƠơƯưẠ-ỹ]/;
const escape=s=>s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/\|/g,'&#124;').replace(/\r?\n/g,'<br>').replace(/`/g,'&#96;');
const cell=s=>'<code>'+escape(s)+'</code>';
function literals(file,text){const ast=ts.createSourceFile(file,text,ts.ScriptTarget.Latest,true);const a=[];function visit(n){if(ts.isStringLiteral(n)||ts.isNoSubstitutionTemplateLiteral(n)||ts.isTemplateExpression(n)){a.push({file,line:ast.getLineAndCharacterOfPosition(n.getStart(ast)).line+1,raw:n.getText(ast)});if(ts.isTemplateExpression(n))return;}ts.forEachChild(n,visit);}visit(ast);return a;}
const files=cp.execFileSync('git',['-C',root,'diff','--name-only'],{encoding:'utf8'}).trim().split('\n').filter(f=>f.endsWith('.ts'));
const changed=[];
for(const file of files){
 const old=literals(file,cp.execFileSync('git',['-C',root,'show','HEAD:'+file],{encoding:'utf8'}));
 const now=literals(file,fs.readFileSync(path.join(root,file),'utf8'));
 if(old.length!==now.length)throw Error(file+': literal count changed '+old.length+' to '+now.length);
 old.forEach((e,i)=>{if(e.raw!==now[i].raw)changed.push({...e,new:now[i].raw});});
}
const oldHtml=cp.execFileSync('git',['-C',root,'show','HEAD:index.html'],{encoding:'utf8'});
const nowHtml=fs.readFileSync(path.join(root,'index.html'),'utf8');
for(const pattern of [/lang="[^"]*"/,/<meta name="description" content="([^"]*)"/,/<title>([^<]*)/]){
 const a=oldHtml.match(pattern),b=nowHtml.match(pattern); const raw=a[1]??a[0],next=b[1]??b[0];
 changed.push({file:'index.html',line:oldHtml.slice(0,a.index).split('\n').length,raw,new:next});
}
const vocab=e=>e.file==='src/ui/ui-preview.ts'&&(e.line>=152&&e.line<=165||e.line===216);
const inventory=before.filter(e=>allowed.test(e.file)&&!vocab(e)&&e.raw.length<1500);
for(const e of changed.filter(e=>!e.file.startsWith('tests/')&&!vi.test(e.raw)&&e.file!=='index.html')) inventory.push(e);
inventory.push(...changed.filter(e=>e.file==='index.html'&&vi.test(e.raw)));
inventory.sort((a,b)=>a.file.localeCompare(b.file)||a.line-b.line);
fs.writeFileSync(path.join(__dirname,'strings-before.md'),'# Chuỗi trước khi đổi · Phiếu 131\n\nĐường dẫn tính từ `games/.wt-dh-codex`; số dòng theo HEAD nền. Quét literal và template bằng AST TypeScript, bỏ chú thích và nghĩa `vi`. Bổ sung các chữ Việt không dấu sau khi đọc các điểm hiển thị. Nhãn chẩn đoán view được ghi cùng để đối chiếu.\n\nTổng: **'+inventory.length+' chuỗi**.\n\n| file:dòng | chuỗi cũ |\n| --- | --- |\n'+inventory.map(e=>'| '+cell(e.file+':'+e.line)+' | '+cell(e.raw)+' |').join('\n')+'\n');
const visible=s=>(["\"", "\'", "`"].includes(s[0])?s.slice(1,-1):s).replace(/<[^>]*>/g,'').replace(/\\'/g,"'");
let large=0;
const rows=changed.map(e=>{
 const a=visible(e.raw),b=visible(e.new);let note=e.file.startsWith('tests/')?'Đồng bộ kỳ vọng/fixture.':'Dịch nhãn/chữ hiển thị.';
 if(e.file.startsWith('src/content/'))note='Chỉ đổi giá trị nameVi; giữ khóa và dữ liệu luật.';
 if(e.file==='index.html')note='Ngôn ngữ trang/tên game/mô tả.';
 if(b.length>a.length*1.2){large++;note+=' ⚑ Dài hơn 20% ('+a.length+' → '+b.length+' ký tự sau bỏ HTML); cần Claude duyệt theo ô thực tế.';}
 if(/Hoa Long|Bach Long/.test(e.new))note+=' Tên riêng phiên tự Latin.';
 if(e.raw.includes('${'))note+=' Giữ nội suy số/phím; chỉ đổi cách diễn đạt.';
 return '| '+cell(e.file+':'+e.line)+' | '+cell(e.raw)+' | '+cell(e.new)+' | '+note+' |';
});
fs.writeFileSync(path.join(__dirname,'strings.md'),'# Bảng duyệt chữ · Phiếu 131\n\nĐường dẫn tính từ `games/.wt-dh-codex`; số dòng theo HEAD nền, không dịch chuyển dòng mã. Mỗi template là một chuỗi, kể cả literal con trong biểu thức; không đếm trùng. Test mới quét chữ nằm trong `tests/english-ui.test.ts`, không có chuỗi cũ để đối chiếu.\n\nTổng **'+changed.length+' chuỗi đổi**, gồm **'+changed.filter(e=>!e.file.startsWith('tests/')).length+' chuỗi nguồn/trang** và **'+changed.filter(e=>e.file.startsWith('tests/')).length+' kỳ vọng/fixture test**. **'+large+' dòng** gắn cờ đo ký tự; đây là phép sàng lọc, không phải đo tràn chữ bằng trình duyệt. Các fragment ghép và tên đầy đủ có thể dài hơn nhưng không nằm trong nút/ô nhỏ.\n\n| file:dòng | chuỗi cũ | chuỗi mới | ghi chú |\n| --- | --- | --- | --- |\n'+rows.join('\n')+'\n');
fs.writeFileSync(path.join(__dirname,'changes.json'),JSON.stringify(changed,null,2)+'\n');
console.log(JSON.stringify({inventory:inventory.length,changed:changed.length,source:changed.filter(e=>!e.file.startsWith('tests/')).length,tests:changed.filter(e=>e.file.startsWith('tests/')).length,over20:large}));
