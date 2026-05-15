#!/usr/bin/env python3
from pathlib import Path
REQUIRED_FILES=['README.md','templates/APP_CONTEXT.md','templates/SCREEN_MAP.md','templates/DATA_TABLE_SPEC.md','templates/WORKFLOW_MAP.md','templates/RUNTIME_MAP.md','templates/CHANGE_BACKLOG.md','templates/CURRENT_JOB_CARD.md','templates/VERIFICATION_REGISTER.md','templates/RELEASE_REGISTER.md','templates/TENANT_ROLLOUT_REGISTER.md','templates/CUSTOMER_CHANGE_REGISTER.md','templates/CODING_PATTERN_REGISTER.md','templates/SYSTEM_FLAGS_REGISTER.md','templates/TOOL_ROUTING_MATRIX.md','templates/LESSONS_LEARNED.md','standards/AGENTS.md','standards/GATE_MODEL.md','standards/TOOL_ROUTING_MATRIX.md','standards/DO_NOT_REPEAT_RULES.md','github/ISSUE_TEMPLATE/defect.yml','github/ISSUE_TEMPLATE/change-request.yml','github/ISSUE_TEMPLATE/job-card.yml','github/pull_request_template.md']
REQUIRED_DIRS=['templates','scripts','reports','github','standards','app-registers']
def run(root):
    root=Path(root); missing=[]
    for p in REQUIRED_FILES:
        if not (root/p).is_file(): missing.append(p)
    for p in REQUIRED_DIRS:
        if not (root/p).is_dir(): missing.append(p+'/')
    return {'name':'required_artifacts','status':'PASS' if not missing else 'BLOCKED','missing':missing,'summary':f'{len(REQUIRED_FILES)-sum(1 for f in REQUIRED_FILES if f in missing)}/{len(REQUIRED_FILES)} required files present; {len(REQUIRED_DIRS)-sum(1 for d in REQUIRED_DIRS if d+"/" in missing)}/{len(REQUIRED_DIRS)} required directories present.'}
if __name__=='__main__':
    import argparse,json; ap=argparse.ArgumentParser(); ap.add_argument('--root',default='.'); a=ap.parse_args(); r=run(a.root); print(json.dumps(r,indent=2)); raise SystemExit(0 if r['status']=='PASS' else 1)
