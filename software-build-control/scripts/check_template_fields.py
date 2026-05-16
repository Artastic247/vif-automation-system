#!/usr/bin/env python3
from pathlib import Path
import argparse,json

COMMON_MANAGEMENT_FIELDS=[
    'Purpose','Scope','Inputs','Activities/checklist','Outputs/records',
    'Owner/tool','Gate controlled','PASS/HOLD/BLOCKED rules','Update trigger'
]

PROCESS_FIELDS=['Process ID','Process name','Owner','Inputs','Activities','Outputs','Records','KPI','Risk','Controls','Gate','PDCA']

REQ={
    'templates/CURRENT_JOB_CARD.md':['Objective','Scope in','Scope out','Inputs','Outputs','Tools allowed','Tools prohibited','Verification','Rollback','Stop condition','Gate decision'],
    'templates/VERIFICATION_REGISTER.md':['Check ID','Linked job card','Expected result','Actual result','Evidence','Status','Reviewer'],
    'templates/TENANT_ROLLOUT_REGISTER.md':['Tenant','Tenant type','Data sensitivity','Feature exposure','Pilot allowed','Rollback method','Gate decision'],
    'management-system/CONTINGENCY_PLAN.md':COMMON_MANAGEMENT_FIELDS + ['trigger','risk','immediate containment','recovery route','rollback route','lesson learned'],
    'management-system/DESIGN_DEVELOPMENT_CONTROL.md':COMMON_MANAGEMENT_FIELDS + ['Intake','Context lock','Source-of-truth lock','Validation/UAT','Tenant rollout','Release','Support/maintenance'],
    'management-system/CHANGE_CONTROL_PROCEDURE.md':COMMON_MANAGEMENT_FIELDS,
    'management-system/APP_MAINTENANCE_PLAN.md':COMMON_MANAGEMENT_FIELDS,
    'management-system/PROCESS_MAP.md':COMMON_MANAGEMENT_FIELDS,
    'management-system/WORKFLOW_CATALOGUE.md':COMMON_MANAGEMENT_FIELDS,
    'management-system/APP_INTAKE_CHECKLIST.md':COMMON_MANAGEMENT_FIELDS + ['What app?','What problem?','Who are users?','What repo?','What branch/version?','What environment?','customer data','single-tenant','multi-tenant','What must not change?','What gate applies?'],
    'management-system/UI_INTERFACE_CONTROL.md':COMMON_MANAGEMENT_FIELDS + ['screen map','routes','tabs','tables/grids','modals','buttons/actions','badges','empty','loading','error','role-specific','responsive','accessibility'],
    'management-system/DATABASE_BACKEND_CONTROL.md':COMMON_MANAGEMENT_FIELDS + ['database design','migrations','RLS','tenant_id','user roles','protected actions','RPC','edge function','audit logs','dev/staging/prod','read/write proof'],
    'management-system/GATE_CHECKLISTS.md':COMMON_MANAGEMENT_FIELDS + ['intake','baseline','UI/screen','data table/grid','workflow','runtime/backend','database/RLS','job-card','verification','validation/UAT','tenant rollout','release','rollback','lessons-learned','automation-readiness'],
    'management-system/AGENT_REGISTER.md':COMMON_MANAGEMENT_FIELDS + ['Worker/agent name','allowed work','prohibited work','required input','required output','stop condition','escalation condition','VIF Orchestrator','Codex Repo Inspector','Lovable Builder','Supabase Backend Reviewer'],
    'management-system/SKILL_REGISTER.md':COMMON_MANAGEMENT_FIELDS + ['Trigger','when to use','when not to use','required inputs','method steps','quality checks','failure modes','gate controlled','context lock','scope lock','contingency review','release check'],
    'management-system/SKILL_TEMPLATE.md':COMMON_MANAGEMENT_FIELDS + ['Skill ID','trigger','when to use','when not to use','required inputs','method steps','output format','quality checks','failure modes','revision history'],
    'management-system/PROCESS_KNOWLEDGE_REGISTER.md':COMMON_MANAGEMENT_FIELDS + ['Process name','app/module affected','source of knowledge','current approved method','related templates','related skills','related agents','known failure modes','lessons learned','last review date','owner'],
    'management-system/PROCESS_ARCHITECTURE.md':COMMON_MANAGEMENT_FIELDS + ['MOP','COP','SOP','PDCA','process-led','document-led'],
    'management-system/PROCESS_REGISTER.md':COMMON_MANAGEMENT_FIELDS + PROCESS_FIELDS + ['MOP-01','COP-01','SOP-01'],
    'management-system/PROCESS_INTERACTION_MAP.md':COMMON_MANAGEMENT_FIELDS + ['MOP','COP','SOP','feedback','interfaces','Lessons learned'],
    'management-system/PDCA_PROCESS_MODEL.md':COMMON_MANAGEMENT_FIELDS + ['PLAN','DO','CHECK','ACT','MOP-01','COP-01','SOP-01'],
    'management-system/PROCESS_TURTLE_TEMPLATE.md':COMMON_MANAGEMENT_FIELDS + ['Inputs','Outputs','Owner','Resources/tools','Methods/skills','Measures/KPIs','Risks','Controls','Records/evidence','Interfaces','PLAN','DO','CHECK','ACT'],
    'management-system/PROCESS_OWNER_MATRIX.md':COMMON_MANAGEMENT_FIELDS + ['Process ID','Owner/agent','Backup/escalation','Authority','Gate controlled'],
    'management-system/PROCESS_KPI_REGISTER.md':COMMON_MANAGEMENT_FIELDS + ['KPI/performance measure','Evidence source','Review cadence','Escalation trigger'],
    'management-system/PROCESS_RISK_CONTROL_REGISTER.md':COMMON_MANAGEMENT_FIELDS + ['Key risk','Key controls','Detection/evidence','Related contingency','Gate impact'],
    'management-system/PROCESS_RECORDS_MATRIX.md':COMMON_MANAGEMENT_FIELDS + ['Required records/evidence','Record location/template','Review point','Retention/revision rule','Linked gate'],
    'management-system/PROCESS_GATE_MATRIX.md':COMMON_MANAGEMENT_FIELDS + ['Primary gate','Entry evidence','PASS condition','HOLD condition','BLOCKED condition','Required records']
}

def run_check(root:Path):
    findings=[]
    for rel,fields in REQ.items():
        p=root/rel
        text=p.read_text(encoding='utf-8',errors='ignore') if p.exists() else ''
        miss=[f for f in fields if f.lower() not in text.lower()]
        if miss:
            findings.append({'file':rel,'missing_fields':miss})
    return {
        'check':'template_fields',
        'status':'PASS' if not findings else 'BLOCKED',
        'summary':'All required template fields present, including process architecture and PDCA files.' if not findings else f'{len(findings)} template issue(s).',
        'findings':findings
    }

def main():
    p=argparse.ArgumentParser(); p.add_argument('--root',default='.')
    a=p.parse_args(); r=run_check(Path(a.root)); print(json.dumps(r,indent=2))
    return 0 if r['status']=='PASS' else 2

if __name__=='__main__': raise SystemExit(main())
