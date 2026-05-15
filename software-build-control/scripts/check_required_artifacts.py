#!/usr/bin/env python3
from pathlib import Path

BASE_FILES = ['README.md','templates/APP_CONTEXT.md','templates/SCREEN_MAP.md','templates/DATA_TABLE_SPEC.md','templates/WORKFLOW_MAP.md','templates/RUNTIME_MAP.md','templates/CHANGE_BACKLOG.md','templates/CURRENT_JOB_CARD.md','templates/VERIFICATION_REGISTER.md','templates/RELEASE_REGISTER.md','templates/TENANT_ROLLOUT_REGISTER.md','templates/CUSTOMER_CHANGE_REGISTER.md','templates/CODING_PATTERN_REGISTER.md','templates/SYSTEM_FLAGS_REGISTER.md','templates/TOOL_ROUTING_MATRIX.md','templates/LESSONS_LEARNED.md','standards/AGENTS.md','standards/GATE_MODEL.md','standards/TOOL_ROUTING_MATRIX.md','standards/DO_NOT_REPEAT_RULES.md','github/ISSUE_TEMPLATE/defect.yml','github/ISSUE_TEMPLATE/change-request.yml','github/ISSUE_TEMPLATE/job-card.yml','github/pull_request_template.md']
MGMT_FILES = ['management-system/SYSTEM_CONTEXT_ANALYSIS.md','management-system/LEADERSHIP_GOVERNANCE.md','management-system/RISK_OPPORTUNITY_REGISTER.md','management-system/OBJECTIVES_REGISTER.md','management-system/COMPETENCE_MATRIX.md','management-system/TOOL_REGISTER.md','management-system/PROMPT_REGISTER.md','management-system/PROMPT_QUALITY_STANDARD.md','management-system/CONTEXT_PACK_STANDARD.md','management-system/AGENT_REGISTER.md','management-system/SKILL_REGISTER.md','management-system/SKILL_TEMPLATE.md','management-system/STANDARDS_REGISTER.md','management-system/STANDARDS_APPLICABILITY_MATRIX.md','management-system/DESIGN_DEVELOPMENT_CONTROL.md','management-system/CHANGE_CONTROL_PROCEDURE.md','management-system/APP_MAINTENANCE_PLAN.md','management-system/INCIDENT_REGISTER.md','management-system/PROBLEM_SOLVING_REGISTER.md','management-system/RCA_CORRECTIVE_ACTION.md','management-system/INTERNAL_AUDIT_REGISTER.md','management-system/GATE_REVIEW_REGISTER.md','management-system/KPI_REGISTER.md','management-system/MANAGEMENT_REVIEW_REGISTER.md']
MAP_FILES = ['maps/PROCESS_MAP.md','maps/TURTLE_DIAGRAM.md','maps/PDCA_REGISTER.md','maps/WORKFLOW_CATALOGUE.md','maps/INTERFACE_MAP.md','maps/SYSTEM_ARCHITECTURE_MAP.md','maps/DATA_FLOW_MAP.md','maps/TENANT_ISOLATION_MAP.md','maps/ENVIRONMENT_MAP.md','maps/DEPLOYMENT_MAP.md','maps/SCREEN_LAYOUT_MAP.md','maps/ENTITY_RELATIONSHIP_MAP.md','maps/STATE_MACHINE_MAP.md','maps/CHANGE_IMPACT_MAP.md']
SCRIPT_FILES = ['scripts/validate_control_pack.py','scripts/check_required_artifacts.py','scripts/check_template_fields.py','scripts/check_secret_risk.py','scripts/check_large_files.py','scripts/check_forbidden_patterns.py','scripts/check_evidence_completeness.py','scripts/validation_common.py']
BASE_DIRS = ['templates','scripts','reports','github','standards','app-registers','management-system','maps']

def run(root, mode='control-pack', control_path=None):
    root = Path(root)
    control_root = root / control_path if mode == 'app-repo' and control_path else root
    required = BASE_FILES + MGMT_FILES + MAP_FILES + SCRIPT_FILES
    missing = [p for p in required if not (control_root / p).is_file()]
    missing += [p+'/' for p in BASE_DIRS if not (control_root / p).is_dir()]
    status = 'PASS' if not missing else 'BLOCKED'
    return {'name':'required_artifacts','status':status,'mode':mode,'missing':missing,'summary':f'{len(required)-sum(1 for f in required if f in missing)}/{len(required)} required files present; {len(BASE_DIRS)-sum(1 for d in BASE_DIRS if d+"/" in missing)}/{len(BASE_DIRS)} required directories present.'}

if __name__ == '__main__':
    import argparse,json; ap=argparse.ArgumentParser(); ap.add_argument('--root',default='.'); ap.add_argument('--mode',default='control-pack'); ap.add_argument('--control-path',default=None); a=ap.parse_args(); r=run(a.root,a.mode,a.control_path); print(json.dumps(r,indent=2)); raise SystemExit(0 if r['status']=='PASS' else 1)
