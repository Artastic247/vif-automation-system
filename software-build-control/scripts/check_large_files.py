#!/usr/bin/env python3
from pathlib import Path
import argparse,json,os
SKIP={'.git','node_modules','dist','build','coverage','__pycache__','reports'}
def run_check(root:Path):
    warns=[]; fail=os.getenv('SBC_FAIL_LARGE_FILES','false').lower() in {'1','true','yes'}
    for p in root.rglob('*'):
        if not p.is_file() or bool(set(p.relative_to(root).parts)&SKIP): continue
        rel=p.relative_to(root).as_posix(); size=p.stat().st_size
        if size>250000: warns.append({'type':'file_size','file':rel,'message':'File exceeds size threshold.'})
        if p.suffix in {'.ts','.tsx','.js','.jsx','.md','.py'}:
            try: lines=sum(1 for _ in p.open(encoding='utf-8',errors='ignore'))
            except Exception: lines=0
            if p.suffix in {'.ts','.tsx','.js','.jsx'} and lines>800: warns.append({'type':'large_code_file','file':rel,'lines':lines})
            if p.suffix=='.md' and lines>1500 and 'archive' not in rel.lower(): warns.append({'type':'large_markdown_file','file':rel,'lines':lines})
    return {'check':'large_files','status':'BLOCKED' if warns and fail else 'PASS','summary':'No large-file warnings detected.' if not warns else f'{len(warns)} warning(s).','warnings':warns}
def main():
    p=argparse.ArgumentParser(); p.add_argument('--root',default='.'); a=p.parse_args(); r=run_check(Path(a.root)); print(json.dumps(r,indent=2)); return 0 if r['status']=='PASS' else 2
if __name__=='__main__': raise SystemExit(main())
