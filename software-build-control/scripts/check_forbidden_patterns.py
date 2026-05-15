#!/usr/bin/env python3
import re
from pathlib import Path
RULES=[('direct_supabase_ui',r'supabase\.',lambda p:'src/pages/' in str(p) or 'src/components/' in str(p)),('delete_call',r'\.delete\s*\(',lambda p:True),('delete_from',r'\bDELETE\s+FROM\b',lambda p:p.suffix.lower()=='.sql'),('verify_jwt_false',r'verify_jwt\s*=\s*false',lambda p:True),('hardcoded_tenant_id',r'(tenant|company)_id\s*[:=]\s*["\'][0-9a-fA-F-]{20,}',lambda p:True),('hardcoded_email_role',r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',lambda p:True)]
def run(root):
    root=Path(root); findings=[]; any_count=0
    for p in root.rglob('*'):
        if not p.is_file() or '.git' in p.parts: continue
        try: txt=p.read_text(errors='ignore')
        except Exception: continue
        if p.suffix in {'.ts','.tsx'}: any_count += len(re.findall(r'\bany\b',txt))
        for name,pat,scope in RULES:
            if scope(p) and re.search(pat,txt,re.I): findings.append({'file':str(p.relative_to(root)),'rule':name})
    if any_count>100: findings.append({'file':'<repo>','rule':'any_overuse_warning','count':any_count})
    return {'name':'forbidden_patterns','status':'PASS','findings':findings,'summary':'No forbidden-pattern findings detected.' if not findings else f'{len(findings)} forbidden-pattern findings detected.'}
if __name__=='__main__':
    import argparse,json; ap=argparse.ArgumentParser(); ap.add_argument('--root',default='.'); a=ap.parse_args(); r=run(a.root); print(json.dumps(r,indent=2)); raise SystemExit(0)
