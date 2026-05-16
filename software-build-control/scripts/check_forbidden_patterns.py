#!/usr/bin/env python3
from pathlib import Path
import argparse,json,os,re
SKIP={'.git','node_modules','dist','build','coverage','__pycache__','reports','templates','standards','app-registers'}
PAT=[('direct_supabase_call_in_ui',re.compile(r'\bsupabase\.(from|rpc|auth|storage)\s*\(',re.I)),('delete_method',re.compile(r'\.delete\s*\(')),('delete_from_migration',re.compile(r'\bDELETE\s+FROM\b',re.I)),('verify_jwt_false',re.compile(r'\bverify_jwt\s*=\s*false\b',re.I)),('hardcoded_email_role_logic',re.compile(r'[\w.%-]+@[\w.-]+\.[A-Za-z]{2,}'))]
def run_check(root:Path):
    findings=[]; fail=os.getenv('SBC_FAIL_FORBIDDEN_PATTERNS','false').lower() in {'1','true','yes'}
    for p in root.rglob('*'):
        if not p.is_file() or bool(set(p.relative_to(root).parts)&SKIP): continue
        rel=p.relative_to(root).as_posix()
        if p.suffix.lower() not in {'.ts','.tsx','.js','.jsx','.sql','.toml','.md','.json','.yml','.yaml'}: continue
        text=p.read_text(encoding='utf-8',errors='ignore')
        for n,line in enumerate(text.splitlines(),1):
            for typ,rx in PAT:
                if rx.search(line): findings.append({'type':typ,'file':rel,'line':n,'severity':'review','message':'Pattern requires human review.'})
    return {'check':'forbidden_patterns','status':'BLOCKED' if findings and fail else 'PASS','summary':'No forbidden-pattern findings detected.' if not findings else f'{len(findings)} finding(s) for review.','findings':findings,'fail_on_finding':fail}
def main():
    p=argparse.ArgumentParser(); p.add_argument('--root',default='.'); a=p.parse_args(); r=run_check(Path(a.root)); print(json.dumps(r,indent=2)); return 0 if r['status']=='PASS' else 2
if __name__=='__main__': raise SystemExit(main())
