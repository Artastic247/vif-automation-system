#!/usr/bin/env python3
from pathlib import Path
REQUIRED={'templates/CURRENT_JOB_CARD.md':['Objective','Scope in','Scope out','Inputs','Outputs','Tools allowed','Tools prohibited','Verification','Rollback','Stop condition','Gate decision'],'templates/VERIFICATION_REGISTER.md':['Check ID','Linked job card','Expected result','Actual result','Evidence','Status','Reviewer'],'templates/TENANT_ROLLOUT_REGISTER.md':['Tenant','Tenant type','Data sensitivity','Feature exposure','Pilot allowed','Rollback method','Gate decision']}
def run(root):
    root=Path(root); gaps=[]
    for file,fields in REQUIRED.items():
        txt=(root/file).read_text(errors='ignore') if (root/file).exists() else ''
        for f in fields:
            if f.lower() not in txt.lower(): gaps.append({'file':file,'field':f})
    return {'name':'template_fields','status':'PASS' if not gaps else 'HOLD','findings':gaps,'summary':'All required template fields present.' if not gaps else f'{len(gaps)} missing fields.'}
if __name__=='__main__':
    import argparse,json; ap=argparse.ArgumentParser(); ap.add_argument('--root',default='.'); a=ap.parse_args(); r=run(a.root); print(json.dumps(r,indent=2)); raise SystemExit(0 if r['status']=='PASS' else 1)
