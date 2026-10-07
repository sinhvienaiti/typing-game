import assert from "node:assert/strict";
import { spawn } from "node:child_process";
import { createServer as createNetServer } from "node:net";
import { mkdtemp, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";

const root=resolve(fileURLToPath(new URL("..",import.meta.url)));const token="world-http-smoke";
async function freePort(){const probe=createNetServer();await new Promise((ok,fail)=>{probe.once("error",fail);probe.listen(0,"127.0.0.1",ok);});const address=probe.address();if(address===null||typeof address==="string")throw new Error("Could not allocate port");const port=address.port;await new Promise((ok,fail)=>probe.close((e)=>e?fail(e):ok()));return port;}
async function request(base,path,{method="GET",body,auth=true}={}){const response=await fetch(`${base}${path}`,{method,headers:{accept:"application/json",...(body===undefined?{}:{"content-type":"application/json"}),...(auth?{"x-typing-game-admin-token":token}:{})},...(body===undefined?{}:{body:JSON.stringify(body)})});const payload=await response.json().catch(()=>({}));assert.ok(response.ok,`${method} ${path} failed (${response.status}): ${JSON.stringify(payload)}`);return payload;}
async function waitForAdmin(base,child,stderr){for(let i=0;i<80;i+=1){if(child.exitCode!==null)throw new Error(`Admin exited (${child.exitCode}): ${stderr()}`);try{const response=await fetch(`${base}/api/admin/space-typing/state`,{headers:{"x-typing-game-admin-token":token}});if(response.ok)return;}catch{}await new Promise((r)=>setTimeout(r,50));}throw new Error(`Timed out: ${stderr()}`);}

test("B06.6 World HTTP Draft -> Validate -> Publish -> child gameplay preview -> Runtime -> Rollback smoke",async(t)=>{
  const dataDir=await mkdtemp(join(tmpdir(),"typing-game-world-http-"));const port=await freePort();const base=`http://127.0.0.1:${port}`;let serverStderr="";const child=spawn(process.execPath,["admin/server.mjs"],{cwd:root,env:{...process.env,TYPING_GAME_ADMIN_DATA_DIR:dataDir,TYPING_GAME_ADMIN_PORT:String(port),TYPING_GAME_ADMIN_TOKEN:token},stdio:["ignore","pipe","pipe"]});child.stderr.setEncoding("utf8");child.stderr.on("data",(c)=>{serverStderr+=c;});t.after(async()=>{if(child.exitCode===null)child.kill("SIGTERM");await new Promise((r)=>{if(child.exitCode!==null)return r();child.once("exit",r);setTimeout(r,1000).unref();});await rm(dataDir,{recursive:true,force:true});});
  await waitForAdmin(base,child,()=>serverStderr);const initial=await request(base,"/api/admin/space-typing/state");const seed=initial.active.revision;let runtime=await request(base,"/api/runtime/space-typing/worlds",{auth:false});assert.deepEqual(runtime.policy.worlds,{});
  const config=structuredClone(initial.active.config);config.content={...(config.content??{}),worlds:{configRevision:"worlds-http-smoke-v1",worlds:{"world-01":{enemyRoster:["rainbow-dart"]}}}};
  const preview=await request(base,"/api/admin/space-typing/worlds/preview",{method:"POST",body:{policy:config.content.worlds}});const before=preview.worlds.find((w)=>w.id==="world-01");assert.equal(before.sampleEnemyId,"rainbow-dart");assert.equal(before.galaxy,1);assert.equal(before.stageStart,1);assert.equal(before.stageEnd,20);
  const draft=await request(base,"/api/admin/space-typing/revisions",{method:"POST",body:{baseRevision:seed,config,message:"B06.6 World HTTP smoke"}});runtime=await request(base,"/api/runtime/space-typing/worlds",{auth:false});assert.deepEqual(runtime.policy.worlds,{},"Draft must not affect runtime");
  const validation=await request(base,"/api/admin/space-typing/validate-revision",{method:"POST",body:{revision:draft.revision}});assert.equal(validation.publishable,true);await request(base,"/api/admin/space-typing/publish",{method:"POST",body:{revision:draft.revision,expectedActiveRevision:seed}});
  runtime=await request(base,"/api/runtime/space-typing/worlds",{auth:false});assert.deepEqual(runtime.policy.worlds["world-01"].enemyRoster,["rainbow-dart"]);const consumed=await request(base,"/api/admin/space-typing/worlds/preview",{method:"POST",body:{policy:runtime.policy}});assert.equal(consumed.worlds.find((w)=>w.id==="world-01")?.sampleEnemyId,"rainbow-dart");
  await request(base,"/api/admin/space-typing/rollback",{method:"POST",body:{targetRevision:seed,expectedActiveRevision:draft.revision}});runtime=await request(base,"/api/runtime/space-typing/worlds",{auth:false});assert.deepEqual(runtime.policy.worlds,{});
});
