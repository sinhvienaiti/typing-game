from pathlib import Path
import os,subprocess,json,time,sys
OUT=Path(__file__).resolve().parent
WT=OUT.parents[2]/'games/.wt-td-codex'
def run(name,args,portal=None):
    env=os.environ.copy();env.pop('VITE_PORTAL_URL',None)
    if portal is not None: env['VITE_PORTAL_URL']=portal
    env['pnpm_config_verify_deps_before_run']='false'
    start=time.monotonic()
    with (OUT/(name+'.log')).open('wb') as log:
        result=subprocess.run(args,cwd=WT,env=env,stdout=log,stderr=subprocess.STDOUT)
    record={'command':args,'cwd':str(WT),'portal':portal,'exit':result.returncode,'seconds':round(time.monotonic()-start,3)}
    (OUT/(name+'-run.json')).write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record),flush=True)
    print('\n'.join((OUT/(name+'.log')).read_text(errors='replace').splitlines()[-14:]),flush=True)
    return result.returncode
if __name__=='__main__':
    sys.exit(run(sys.argv[1],sys.argv[2:]))
