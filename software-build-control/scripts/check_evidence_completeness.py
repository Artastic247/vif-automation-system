#!/usr/bin/env python3
from pathlib import Path
import argparse,json
DIRS=['reports','management-system','maps','validation-profiles','external-scan-examples']
def run_check(root:Path):
    findings=[]
    for d in DIRS:
        if not (root/d).is_dir(): findings.append({'type':'missing_evidence_directory','file':d,'message':'Required evidence/control directory missing.'})
    if (root/'.github/workflows').exists(): findings.append({'type':'active_workflow_directory_present','file':'.github/workflows','message':'Workflows must remain inactive templates at this gate.'})
    return {'check':'evidence_completeness','status':'PASS' if not findings else 'BLOCKED','summary':'Evidence completeness checks passed.' if not findings else f'{len(findings)} blocking evidence issue(s).','findings':findings}
def main():
    p=argparse.ArgumentParser(); p.add_argument('--root',default='.'); a=p.parse_args(); r=run_check(Path(a.root)); print(json.dumps(r,indent=2)); return 0 if r['status']=='PASS' else 2
if __name__=='__main__': raise SystemExit(main())
