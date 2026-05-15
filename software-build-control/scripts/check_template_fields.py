#!/usr/bin/env python3
from pathlib import Path

COMMON = ['Purpose','When to use','Owner/tool','Inputs','Outputs/records','Gate controlled','Update trigger']
REQUIRED = {
 'templates/CURRENT_JOB_CARD.md':['Objective','Scope in','Scope out','Inputs','Outputs','Tools allowed','Tools prohibited','Verification','Rollback','Stop condition','Gate decision'],
 'templates/VERIFICATION_REGISTER.md':['Check ID','Linked job card','Expected result','Actual result','Evidence','Status','Reviewer'],
 'templates/TENANT_ROLLOUT_REGISTER.md':['Tenant','Tenant type','Data sensitivity','Feature exposure','Pilot allowed','Rollback method','Gate decision'],
 'management-system/DESIGN_DEVELOPMENT_CONTROL.md':['Request','Context check','Impact assessment','Design/update plan','Risk review','Job card','Build/modification','Verification','Validation/UAT','Tenant rollout decision','Release','Lessons learned'],
 'management-system/CHANGE_CONTROL_PROCEDURE.md':['internal change','customer change','defect repair','urgent fix','schema/backend/RLS change','release rollback'],
 'management-system/PROMPT_QUALITY_STANDARD.md':['objective','scope in','scope out','prohibited changes','verification','rollback','stop condition','gate decision'],
 'management-system/CONTEXT_PACK_STANDARD.md':['app context','current branch/version','current job card','latest evidence','tenant/environment context','rollback context'],
 'management-system/SKILL_TEMPLATE.md':['skill ID','trigger','purpose','when to use','when not to use','required inputs','method steps','output format','quality checks','failure modes','gate controlled','revision history']
}

def run(root, mode='control-pack', control_path=None):
    root = Path(root); control_root = root / control_path if mode == 'app-repo' and control_path else root
    gaps=[]
    for file, fields in REQUIRED.items():
        txt=(control_root/file).read_text(errors='ignore') if (control_root/file).exists() else ''
        for f in fields:
            if f.lower() not in txt.lower(): gaps.append({'file':file,'field':f})
    for folder in ['management-system','maps']:
        base=control_root/folder
        if base.exists():
            for p in base.glob('*.md'):
                txt=p.read_text(errors='ignore').lower()
                for f in COMMON:
                    if f.lower() not in txt: gaps.append({'file':str(p.relative_to(control_root)),'field':f})
    return {'name':'template_fields','status':'PASS' if not gaps else 'HOLD','findings':gaps,'summary':'All required template fields present.' if not gaps else f'{len(gaps)} missing fields.'}

if __name__=='__main__':
    import argparse,json; ap=argparse.ArgumentParser(); ap.add_argument('--root',default='.'); ap.add_argument('--mode',default='control-pack'); ap.add_argument('--control-path',default=None); a=ap.parse_args(); r=run(a.root,a.mode,a.control_path); print(json.dumps(r,indent=2)); raise SystemExit(0 if r['status']=='PASS' else 1)
