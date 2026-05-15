#!/usr/bin/env python3
import re
from pathlib import Path
UI_PATHS=['src/pages/','src/components/','src/ui/','src/views/']
SERVICE_OK=['src/services/','src/data/','src/repositories/','src/integrations/','src/lib/']
TEST_DEMO=['test','tests','__tests__','demo','seed','training']
UUID_RE=re.compile(r'[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}')
SEC_WORD=re.compile(r'(?i)(tenant_id|user_id|company_id|role|permission|admin|super_admin|email|auth|owner)')
EMAIL_RE=re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}')

def cls(path):
    s=str(path).replace('\\','/')
    if any(x in s.lower() for x in TEST_DEMO): return 'test/demo acceptable usage if clearly isolated'
    if any(x in s for x in UI_PATHS): return 'UI direct backend access'
    if any(x in s for x in SERVICE_OK): return 'likely service/repository-layer acceptable usage'
    return 'requires human review'

def run(root, mode='control-pack', control_path=None):
    root=Path(root); findings=[]; any_count=0
    for p in root.rglob('*'):
        if not p.is_file() or any(part in {'.git','node_modules','dist','build','reports'} for part in p.parts): continue
        txt=p.read_text(errors='ignore')
        rp=str(p.relative_to(root)).replace('\\','/')
        lower=txt.lower(); context=cls(rp)
        if any(token in txt for token in ['supabase.','supabase.auth.','supabase.from(','supabase.functions.invoke','createClient(']) or ('@supabase/supabase-js' in txt):
            if context == 'UI direct backend access': findings.append({'file':rp,'severity':'HOLD','rule':'direct_supabase_ui','classification':context})
            elif 'supabase.auth.' in txt: findings.append({'file':rp,'severity':'HOLD','rule':'auth_access_review','classification':context})
        if '.delete(' in txt: findings.append({'file':rp,'severity':'HOLD','rule':'delete_call_review','classification':context})
        if p.suffix.lower()=='.sql' and re.search(r'\bDELETE\s+FROM\b',txt,re.I): findings.append({'file':rp,'severity':'HOLD','rule':'delete_from_migration','classification':'requires impact/rollback review'})
        if re.search(r'verify_jwt\s*=\s*false',txt,re.I): findings.append({'file':rp,'severity':'HOLD','rule':'verify_jwt_false','classification':'edge-function security review required'})
        if UUID_RE.search(txt) and SEC_WORD.search(txt): findings.append({'file':rp,'severity':'HOLD','rule':'hardcoded_security_uuid','classification':context})
        if EMAIL_RE.search(txt) and SEC_WORD.search(txt): findings.append({'file':rp,'severity':'HOLD','rule':'hardcoded_email_role_context','classification':context})
        if p.suffix in {'.ts','.tsx'}: any_count += len(re.findall(r'\bany\b',txt))
    if any_count>100: findings.append({'file':'<repo>','severity':'WARN','rule':'any_overuse_warning','count':any_count})
    has_hold=any(f.get('severity')=='HOLD' for f in findings); has_warn=any(f.get('severity')=='WARN' for f in findings)
    status='HOLD' if has_hold else ('PASS_WITH_WARNINGS' if has_warn else 'PASS')
    return {'name':'forbidden_patterns','status':status,'findings':findings,'summary':'No forbidden-pattern findings detected.' if not findings else f'{len(findings)} forbidden-pattern findings detected.'}

if __name__=='__main__':
    import argparse,json; ap=argparse.ArgumentParser(); ap.add_argument('--root',default='.'); ap.add_argument('--mode',default='control-pack'); ap.add_argument('--control-path',default=None); a=ap.parse_args(); r=run(a.root,a.mode,a.control_path); print(json.dumps(r,indent=2)); raise SystemExit(0)
