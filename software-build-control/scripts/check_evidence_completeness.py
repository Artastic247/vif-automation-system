#!/usr/bin/env python3
from pathlib import Path
REQUIRED = {
 'templates/CURRENT_JOB_CARD.md':['Objective','Scope in','Scope out','Inputs','Outputs','Tools allowed','Tools prohibited','Verification','Rollback','Stop condition','Gate decision'],
 'templates/VERIFICATION_REGISTER.md':['Check ID','Linked job card','Expected result','Actual result','Evidence','Status','Reviewer'],
 'templates/RELEASE_REGISTER.md':['Rollback','Decision','Approver'],
 'templates/TENANT_ROLLOUT_REGISTER.md':['Tenant','Tenant type','Data sensitivity','Pilot allowed','Rollback method','Gate decision'],
 'templates/APP_CONTEXT.md':['App name','Purpose','Repo','Branch','Environment','Tenants']
}

def useful(txt):
    stripped=''.join(line.strip() for line in txt.splitlines() if line.strip() and not line.strip().startswith('|---'))
    return len(stripped) > 120

def run(root, mode='control-pack', control_path=None, gate='baseline'):
    root=Path(root); control_root=root/control_path if mode=='app-repo' and control_path else root
    findings=[]
    for file, fields in REQUIRED.items():
        p=control_root/file
        if not p.exists(): findings.append({'file':file,'severity':'BLOCKED','rule':'missing_evidence_artifact'}); continue
        txt=p.read_text(errors='ignore')
        missing=[f for f in fields if f.lower() not in txt.lower()]
        if missing: findings.append({'file':file,'severity':'HOLD','rule':'missing_evidence_fields','fields':missing})
        if mode=='app-repo' and not useful(txt): findings.append({'file':file,'severity':'HOLD','rule':'placeholder_or_empty_evidence'})
    if any(f['severity']=='BLOCKED' for f in findings): status='BLOCKED'
    elif findings: status='HOLD'
    else: status='PASS'
    return {'name':'evidence_completeness','status':status,'findings':findings,'summary':'Evidence artefacts are present and sufficiently populated for the selected mode/gate.' if not findings else f'{len(findings)} evidence completeness findings.'}

if __name__=='__main__':
    import argparse,json; ap=argparse.ArgumentParser(); ap.add_argument('--root',default='.'); ap.add_argument('--mode',default='control-pack'); ap.add_argument('--control-path',default=None); ap.add_argument('--gate',default='baseline'); a=ap.parse_args(); r=run(a.root,a.mode,a.control_path,a.gate); print(json.dumps(r,indent=2)); raise SystemExit(0 if r['status']=='PASS' else 1)
