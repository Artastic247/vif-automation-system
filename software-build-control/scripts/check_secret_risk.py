#!/usr/bin/env python3
from pathlib import Path
import argparse,json,re
SKIP={'.git','node_modules','dist','build','coverage','__pycache__','reports'}
PAT=[('openai_api_key',re.compile(r'\bsk-(?:proj-)?[A-Za-z0-9_\-]{20,}\b')),('github_token',re.compile(r'\bgh[pousr]_[A-Za-z0-9_]{30,}\b')),('service_role',re.compile(r'\bSERVICE_ROLE(_KEY)?\s*[:=]\s*[^\s<>]+',re.I)),('credential_assignment',re.compile(r'\b(password|secret|token|private_key|api[_-]?key)\s*[:=]\s*[^\s<>]{8,}',re.I))]
PLACE=['placeholder','example','your_','redacted','changeme','<token>','<secret>','<api_key>']
def skip(p,root): return bool(set(p.relative_to(root).parts)&SKIP)
def run_check(root:Path):
    findings=[]
    for p in root.rglob('*'):
        if not p.is_file() or skip(p,root): continue
        rel=p.relative_to(root).as_posix()
        if p.name=='.env' or (p.name.startswith('.env.') and p.name!='.env.example'): findings.append({'type':'env_file','file':rel,'message':'.env or .env.* file detected.'})
        try: text=p.read_text(encoding='utf-8',errors='ignore')
        except Exception: continue
        for n,line in enumerate(text.splitlines(),1):
            low=line.lower()
            if any(x in low for x in PLACE): continue
            for typ,rx in PAT:
                if rx.search(line): findings.append({'type':typ,'file':rel,'line':n,'message':'Potential secret pattern detected.'})
    return {'check':'secret_risk','status':'PASS' if not findings else 'BLOCKED','summary':'No secret risks detected.' if not findings else f'{len(findings)} secret risk(s).','findings':findings}
def main():
    p=argparse.ArgumentParser(); p.add_argument('--root',default='.'); a=p.parse_args(); r=run_check(Path(a.root)); print(json.dumps(r,indent=2)); return 0 if r['status']=='PASS' else 2
if __name__=='__main__': raise SystemExit(main())
