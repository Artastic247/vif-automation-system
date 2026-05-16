#!/usr/bin/env python3
from pathlib import Path
import argparse,json
REQ={'templates/CURRENT_JOB_CARD.md':['Objective','Scope in','Scope out','Inputs','Outputs','Tools allowed','Tools prohibited','Verification','Rollback','Stop condition','Gate decision'],'templates/VERIFICATION_REGISTER.md':['Check ID','Linked job card','Expected result','Actual result','Evidence','Status','Reviewer'],'templates/TENANT_ROLLOUT_REGISTER.md':['Tenant','Tenant type','Data sensitivity','Feature exposure','Pilot allowed','Rollback method','Gate decision']}
def run_check(root:Path):
    findings=[]
    for rel,fields in REQ.items():
        p=root/rel; text=p.read_text(encoding='utf-8',errors='ignore') if p.exists() else ''
        miss=[f for f in fields if f.lower() not in text.lower()]
        if miss: findings.append({'file':rel,'missing_fields':miss})
    return {'check':'template_fields','status':'PASS' if not findings else 'BLOCKED','summary':'All required template fields present.' if not findings else f'{len(findings)} template issue(s).','findings':findings}
def main():
    p=argparse.ArgumentParser(); p.add_argument('--root',default='.'); a=p.parse_args(); r=run_check(Path(a.root)); print(json.dumps(r,indent=2)); return 0 if r['status']=='PASS' else 2
if __name__=='__main__': raise SystemExit(main())
