#!/usr/bin/env python3
import re
from pathlib import Path

KEY_PATTERNS=[('openai_key',r'sk-[A-Za-z0-9_-]{20,}'),('github_token',r'gh[pousr]_[A-Za-z0-9_]{20,}'),('jwt_like_key',r'eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}'),('private_key_block',r'-----BEGIN (RSA |EC |OPENSSH |)PRIVATE KEY-----')]
ASSIGN_RE=re.compile(r'(?i)(password|secret|token|private_key|service_role|api_key)\s*[:=]\s*["\']([^"\']+)["\']')
PLACEHOLDER=re.compile(r'(?i)^(your_|<|example|dummy|test|placeholder|changeme|xxx|\$\{)')
ALLOW_NAMES={'.env.example'}
SKIP_PARTS={'.git','node_modules','dist','build'}

def run(root, mode='control-pack', control_path=None):
    root=Path(root); findings=[]
    for p in root.rglob('*'):
        if not p.is_file() or any(part in SKIP_PARTS for part in p.parts): continue
        if p.name.startswith('.env') and p.name not in ALLOW_NAMES:
            findings.append({'file':str(p.relative_to(root)),'severity':'BLOCKED','rule':'env_file','message':'Environment file present.'}); continue
        txt=p.read_text(errors='ignore')
        for name,pat in KEY_PATTERNS:
            if re.search(pat,txt): findings.append({'file':str(p.relative_to(root)),'severity':'BLOCKED','rule':name,'message':'Real-looking secret pattern detected.'})
        for m in ASSIGN_RE.finditer(txt):
            value=m.group(2).strip()
            if not PLACEHOLDER.match(value) and len(value) >= 12:
                findings.append({'file':str(p.relative_to(root)),'severity':'BLOCKED','rule':'credential_assignment','message':'Credential-like assignment with non-placeholder value.'})
    return {'name':'secret_risk','status':'PASS' if not findings else 'BLOCKED','findings':findings,'summary':'No secret risks detected.' if not findings else f'{len(findings)} secret risks detected.'}

if __name__=='__main__':
    import argparse,json; ap=argparse.ArgumentParser(); ap.add_argument('--root',default='.'); ap.add_argument('--mode',default='control-pack'); ap.add_argument('--control-path',default=None); a=ap.parse_args(); r=run(a.root,a.mode,a.control_path); print(json.dumps(r,indent=2)); raise SystemExit(0 if r['status']=='PASS' else 1)
