#!/usr/bin/env python3
import re
from pathlib import Path
PATTERNS=[r'sk-[A-Za-z0-9_-]{20,}',r'gh[pousr]_[A-Za-z0-9_]{20,}',r'eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}',r'(?i)(password|secret|token|private_key)\s*=']
ALLOW_NAMES={'.env.example'}
def run(root):
    root=Path(root); findings=[]
    for p in root.rglob('*'):
        if not p.is_file() or '.git' in p.parts: continue
        if p.name.startswith('.env') and p.name not in ALLOW_NAMES:
            findings.append({'file':str(p.relative_to(root)),'issue':'env file present'}); continue
        try: txt=p.read_text(errors='ignore')
        except Exception: continue
        for pat in PATTERNS:
            if re.search(pat,txt): findings.append({'file':str(p.relative_to(root)),'issue':'possible secret pattern','pattern':pat})
    return {'name':'secret_risk','status':'PASS' if not findings else 'BLOCKED','findings':findings,'summary':'No secret risks detected.' if not findings else f'{len(findings)} secret risks detected.'}
if __name__=='__main__':
    import argparse,json; ap=argparse.ArgumentParser(); ap.add_argument('--root',default='.'); a=ap.parse_args(); r=run(a.root); print(json.dumps(r,indent=2)); raise SystemExit(0 if r['status']=='PASS' else 1)
