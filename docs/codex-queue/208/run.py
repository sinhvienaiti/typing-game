from pathlib import Path
import os, sys, subprocess, time, json, hashlib
ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / 'games/.wt-td-codex'
OUT = Path(__file__).resolve().parent

def inventory(name):
    files = [{'path': str(f.relative_to(WORK/'dist')), 'bytes': f.stat().st_size,
              'sha256': hashlib.sha256(f.read_bytes()).hexdigest()}
             for f in sorted((WORK/'dist').rglob('*')) if f.is_file()]
    result = {'fileCount': len(files), 'bytes': sum(f['bytes'] for f in files), 'files': files}
    (OUT/name).write_text(json.dumps(result, indent=2)+'\n')
    return result

def run(name, command, env=None, json_output=False):
    start = time.monotonic()
    merged = dict(os.environ, VITE_PORTAL_URL='')
    merged.update(env or {})
    result = subprocess.run(command, cwd=WORK, env=merged, capture_output=True, text=True)
    elapsed = round(time.monotonic()-start, 3)
    (OUT/(name+('.json' if json_output else '.log'))).write_text(result.stdout + ('' if json_output else result.stderr))
    meta = {'command': command, 'cwd': str(WORK), 'env': {'VITE_PORTAL_URL': merged['VITE_PORTAL_URL']}, 'exitCode': result.returncode, 'seconds': elapsed}
    (OUT/(name+'-run.json')).write_text(json.dumps(meta, indent=2)+'\n')
    print(json.dumps(meta), flush=True)
    return result

if __name__ == '__main__':
    label, *command = sys.argv[1:]
    run(label, command)
