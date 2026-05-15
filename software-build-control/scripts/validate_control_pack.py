#!/usr/bin/env python3
import argparse,json
from pathlib import Path
from validation_common import severity_rollup
from check_required_artifacts import run as required
from check_template_fields import run as fields
from check_secret_risk import run as secrets
from check_large_files import run as large
from check_forbidden_patterns import run as forbidden
from check_evidence_completeness import run as evidence
CHECKS=[required,fields,secrets,large,forbidden,evidence]
NEXT={'PASS':'Proceed to controlled review/next approved gate.','PASS_WITH_WARNINGS':'Review warnings before app enforcement.','HOLD':'Resolve review findings before proceeding.','BLOCKED':'Stop: unsafe or critical evidence missing.'}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',default='.'); ap.add_argument('--mode',default='control-pack',choices=['control-pack','app-repo']); ap.add_argument('--control-path',default=None); ap.add_argument('--gate',default='baseline'); args=ap.parse_args(); root=Path(args.root)
    results=[c(root,args.mode,args.control_path) for c in CHECKS]
    overall, counts = severity_rollup(results)
    report={'overall_status':overall,'gate_decision':overall,'mode':args.mode,'root':str(root),'control_path':args.control_path,'counts_by_status':counts,'checks':results,'recommended_next_action':NEXT[overall]}
    report_root = root/args.control_path if args.mode=='app-repo' and args.control_path else root
    (report_root/'reports').mkdir(parents=True,exist_ok=True)
    (report_root/'reports/control-pack-validation.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    md=['# Control Pack Validation','',f'Mode: `{args.mode}`',f'Root: `{root}`',f'Control path: `{args.control_path or "."}`',f'Overall status: **{overall}**','',f'Recommended next action: {NEXT[overall]}','']
    for r in results: md.append(f"- {r['name']}: {r['status']} — {r.get('summary','')}")
    (report_root/'reports/control-pack-validation.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
    print(f'Control Pack Validation: {overall}')
    for r in results: print(f"- {r['name']}: {r['status']} — {r.get('summary','')}")
    print('Reports written: reports/control-pack-validation.json and reports/control-pack-validation.md')
    raise SystemExit(0 if overall in ['PASS','PASS_WITH_WARNINGS'] else 1)
if __name__=='__main__': main()
