#!/usr/bin/env python3
from pathlib import Path
CODE_EXT={'.ts','.tsx','.js','.jsx'}
SKIP_NAMES={'package-lock.json','pnpm-lock.yaml','yarn.lock'}
SKIP_PARTS={'node_modules','dist','build','reports'}
SKIP_SUFFIX={'.min.js','.min.css'}

def is_generated(path):
    s=str(path).lower()
    return 'supabase/types' in s or 'database.types' in s or 'generated' in s

def run(root, mode='control-pack', control_path=None, fail=False):
    root=Path(root); findings=[]
    for p in root.rglob('*'):
        if not p.is_file() or any(part in SKIP_PARTS for part in p.parts) or p.name in SKIP_NAMES or any(p.name.endswith(x) for x in SKIP_SUFFIX) or is_generated(p): continue
        try: lines=len(p.read_text(errors='ignore').splitlines())
        except Exception: continue
        if p.suffix in CODE_EXT and lines>800: findings.append({'file':str(p.relative_to(root)),'severity':'WARN','lines':lines,'issue':'code file exceeds 800 lines'})
        if p.suffix=='.md' and lines>1000 and 'archive' not in p.name.lower() and 'reference' not in p.name.lower(): findings.append({'file':str(p.relative_to(root)),'severity':'WARN','lines':lines,'issue':'control markdown unusually large'})
    return {'name':'large_files','status':'BLOCKED' if fail and findings else ('PASS_WITH_WARNINGS' if findings else 'PASS'),'findings':findings,'summary':'No large-file warnings detected.' if not findings else f'{len(findings)} large-file warnings detected.'}

if __name__=='__main__':
    import argparse,json; ap=argparse.ArgumentParser(); ap.add_argument('--root',default='.'); ap.add_argument('--mode',default='control-pack'); ap.add_argument('--control-path',default=None); ap.add_argument('--fail',action='store_true'); a=ap.parse_args(); r=run(a.root,a.mode,a.control_path,a.fail); print(json.dumps(r,indent=2)); raise SystemExit(0 if r['status']!='BLOCKED' else 1)
