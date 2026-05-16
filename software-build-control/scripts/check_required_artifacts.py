#!/usr/bin/env python3
from pathlib import Path
import argparse,json

FILES=[
'README.md',
'templates/APP_CONTEXT.md','templates/SCREEN_MAP.md','templates/DATA_TABLE_SPEC.md','templates/WORKFLOW_MAP.md','templates/RUNTIME_MAP.md','templates/CHANGE_BACKLOG.md','templates/CURRENT_JOB_CARD.md','templates/VERIFICATION_REGISTER.md','templates/RELEASE_REGISTER.md','templates/TENANT_ROLLOUT_REGISTER.md','templates/CUSTOMER_CHANGE_REGISTER.md','templates/CODING_PATTERN_REGISTER.md','templates/SYSTEM_FLAGS_REGISTER.md','templates/TOOL_ROUTING_MATRIX.md','templates/LESSONS_LEARNED.md',
'standards/AGENTS.md','standards/GATE_MODEL.md','standards/TOOL_ROUTING_MATRIX.md','standards/DO_NOT_REPEAT_RULES.md',
'github/ISSUE_TEMPLATE/defect.yml','github/ISSUE_TEMPLATE/change-request.yml','github/ISSUE_TEMPLATE/job-card.yml','github/pull_request_template.md',
'management-system/CONTINGENCY_PLAN.md','management-system/DESIGN_DEVELOPMENT_CONTROL.md','management-system/CHANGE_CONTROL_PROCEDURE.md','management-system/APP_MAINTENANCE_PLAN.md','management-system/PROCESS_MAP.md','management-system/WORKFLOW_CATALOGUE.md','management-system/APP_INTAKE_CHECKLIST.md','management-system/UI_INTERFACE_CONTROL.md','management-system/DATABASE_BACKEND_CONTROL.md','management-system/GATE_CHECKLISTS.md','management-system/AGENT_REGISTER.md','management-system/SKILL_REGISTER.md','management-system/SKILL_TEMPLATE.md','management-system/PROCESS_KNOWLEDGE_REGISTER.md',
'management-system/PROCESS_ARCHITECTURE.md','management-system/PROCESS_REGISTER.md','management-system/PROCESS_INTERACTION_MAP.md','management-system/PDCA_PROCESS_MODEL.md','management-system/PROCESS_TURTLE_TEMPLATE.md','management-system/PROCESS_OWNER_MATRIX.md','management-system/PROCESS_KPI_REGISTER.md','management-system/PROCESS_RISK_CONTROL_REGISTER.md','management-system/PROCESS_RECORDS_MATRIX.md','management-system/PROCESS_GATE_MATRIX.md',
'scripts/check_process_architecture.py'
]
FILES=list(dict.fromkeys(FILES))
DIRS=['templates','scripts','standards','management-system','maps','validation-profiles','external-scan-examples','reports','github','app-registers','github/ISSUE_TEMPLATE','github/workflows']

def run_check(root:Path):
    mf=[x for x in FILES if not (root/x).is_file()]
    md=[x for x in DIRS if not (root/x).is_dir()]
    return {
        'check':'required_artifacts',
        'status':'PASS' if not mf and not md else 'BLOCKED',
        'summary':f'{len(FILES)-len(mf)}/{len(FILES)} required files present; {len(DIRS)-len(md)}/{len(DIRS)} required directories present.',
        'missing_files':mf,
        'missing_directories':md
    }

def main():
    p=argparse.ArgumentParser(); p.add_argument('--root',default='.')
    a=p.parse_args(); r=run_check(Path(a.root)); print(json.dumps(r,indent=2))
    return 0 if r['status']=='PASS' else 2

if __name__=='__main__': raise SystemExit(main())
