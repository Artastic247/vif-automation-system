#!/usr/bin/env python3
from pathlib import Path
import argparse,json,re

SKIP_DIRS={'.git','node_modules','dist','build','coverage','__pycache__','reports'}
EMAIL_RE=re.compile(r'\b[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}\b')
SECURITY_TERMS=['role','permission','admin','super_admin','auth','user','tenant','access','owner','security']
PLACEHOLDER_DOMAINS=('example.com','example.org','example.net','example.test')
SNAGG_DOMAIN='@'+'snagg.org'
KHAN_CONTACT='khan.angus'+SNAGG_DOMAIN
CONTROL_REFERENCE_FILES={
    'README.md',
    'management-system/IDENTITY_CONTACT_DATA_CONTROL.md',
    'management-system/APPROVED_CONTACT_REGISTER.md',
    'management-system/PROMPT_QUALITY_CHECKLIST.md',
    'management-system/CONTEXT_PACK_STANDARD.md',
    'management-system/TOOL_SPECIFIC_PROMPT_INSTRUCTIONS.md',
    'scripts/check_identity_contact_data.py',
    'scripts/check_template_fields.py'
}

def skip(path:Path,root:Path)->bool:
    return bool(set(path.relative_to(root).parts)&SKIP_DIRS)

def load_register(root:Path):
    p=root/'management-system/APPROVED_CONTACT_REGISTER.md'
    approved={}; raw=''
    if p.exists():
        raw=p.read_text(encoding='utf-8',errors='ignore')
        for email in EMAIL_RE.findall(raw):
            lower=email.lower()
            line=next((ln for ln in raw.splitlines() if email in ln),'')
            status='UNKNOWN'
            for candidate in ['Approved placeholder','Approved','HOLD','Retired','Blocked','Draft']:
                if candidate.lower() in line.lower():
                    status=candidate.upper().replace(' ','_')
                    break
            approved[lower]={'line':line,'status':status}
    return approved,raw

def classify(email,rel,line,approved):
    lower=email.lower()
    line_lower=line.lower()
    is_placeholder=lower.endswith(PLACEHOLDER_DOMAINS)
    in_register=lower in approved
    in_control_reference=rel in CONTROL_REFERENCE_FILES
    is_snagg=lower.endswith(SNAGG_DOMAIN)
    near_security=any(term in line_lower for term in SECURITY_TERMS)

    if is_placeholder:
        return 'PASS','Placeholder/example email.'
    if near_security and not in_control_reference:
        return 'BLOCKED','Email appears near role/security/access terms outside approved control/reference files.'
    if in_register:
        status=approved[lower].get('status','UNKNOWN')
        if status=='BLOCKED':
            return 'BLOCKED','Contact is registered as blocked.'
        if status=='HOLD':
            if in_control_reference:
                return 'PASS_WITH_WARNINGS','Contact is intentionally controlled as HOLD in policy/register/reference text; not approved for active use.'
            return 'HOLD','Contact is registered as HOLD and requires project-specific approval before active use.'
        return 'PASS',f'Contact register match with status {status}.'
    if is_snagg:
        if in_control_reference:
            return 'PASS_WITH_WARNINGS','SNAGG email appears only as controlled policy/reference text; register approval required before active use.'
        return 'HOLD','SNAGG email is not approved in the contact register.'
    if in_control_reference:
        return 'PASS_WITH_WARNINGS','Real/unknown email appears only in controlled reference text; review before active use.'
    return 'HOLD','Unknown real email in generated/control files.'

def run_check(root:Path):
    root=root.resolve()
    approved,_=load_register(root)
    findings=[]; counts={'PASS':0,'PASS_WITH_WARNINGS':0,'HOLD':0,'BLOCKED':0}
    for p in root.rglob('*'):
        if not p.is_file() or skip(p,root):
            continue
        rel=p.relative_to(root).as_posix()
        try:
            text=p.read_text(encoding='utf-8',errors='ignore')
        except Exception:
            continue
        for lineno,line in enumerate(text.splitlines(),1):
            for email in EMAIL_RE.findall(line):
                classification,message=classify(email,rel,line,approved)
                counts[classification]=counts.get(classification,0)+1
                findings.append({
                    'file':rel,
                    'line':lineno,
                    'email':email,
                    'classification':classification,
                    'message':message
                })
    status='BLOCKED' if counts.get('BLOCKED',0)>0 else ('HOLD' if counts.get('HOLD',0)>0 else 'PASS')
    return {
        'check':'identity_contact_data',
        'status':status,
        'summary':f"{len(findings)} email/contact occurrence(s) found; PASS={counts.get('PASS',0)}, WARN={counts.get('PASS_WITH_WARNINGS',0)}, HOLD={counts.get('HOLD',0)}, BLOCKED={counts.get('BLOCKED',0)}.",
        'counts':counts,
        'findings':findings
    }

def main():
    p=argparse.ArgumentParser(); p.add_argument('--root',default='.')
    a=p.parse_args(); r=run_check(Path(a.root)); print(json.dumps(r,indent=2))
    return 0 if r['status']=='PASS' else 2

if __name__=='__main__': raise SystemExit(main())
