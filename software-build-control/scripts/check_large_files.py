#!/usr/bin/env python3
from pathlib import Path
CODE_EXT={'.ts','.tsx','.js','.jsx'}
def run(root,fail=False):
    root=Path(root); findings=[]
    for p in root.rglob('*'):
        if not p.is_file() or '.git' in p.parts: continue
        try: lines=len(p.read_text(errors='ignore').splitlines())
        except Exception: continue
        if p.suffix in CODE_EXT and lines>800: findings.append({'file':str(p.relative_to(root)),'lines':lines,'issue':'code file exceeds 800 lines'})
        if p.suffix=='.md' and lines>1000 and 'archive' not in p.name.lower() and 'reference' not in p.name.lower(): findings.append({'file':str(p.relative_to(root)),'lines':lines,'issue':'control markdown unusually large'})
    return {'name':'large_files','status':'BLOCKED' if fail and findings else 'PASS','findings':findings,'summary':'No large-file warnings detected.' if not findings else f'{len(findings)} large-file warnings detected.'}
if __name__=='__main__':
    import argparse,json; ap=argparse.ArgumentParser(); ap.add_argument('--root',default='.'); ap.add_argument('--fail',action='store_true'); a=ap.parse_args(); r=run(a.root,a.fail); print(json.dumps(r,indent=2)); raise SystemExit(0 if r['status']=='PASS' else 1)
