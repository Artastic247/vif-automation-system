#!/usr/bin/env python3
import argparse,json
from pathlib import Path
from check_required_artifacts import run as required
from check_template_fields import run as fields
from check_secret_risk import run as secrets
from check_large_files import run as large
from check_forbidden_patterns import run as forbidden
CHECKS=[required,fields,secrets,large,forbidden]
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',default='.'); args=ap.parse_args(); root=Path(args.root)
    results=[c(root) for c in CHECKS]
    overall='PASS'
    if any(r['status']=='BLOCKED' for r in results): overall='BLOCKED'
    elif any(r['status']=='HOLD' for r in results): overall='HOLD'
    report={'overall_status':overall,'checks':results}
    (root/'reports').mkdir(exist_ok=True)
    (root/'reports/control-pack-validation.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    md=['# Control Pack Validation','',f'Overall status: **{overall}**','']
    for r in results: md.append(f"- {r['name']}: {r['status']} — {r.get('summary','')}")
    (root/'reports/control-pack-validation.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
    print(f'Control Pack Validation: {overall}')
    for r in results: print(f"- {r['name']}: {r['status']} — {r.get('summary','')}")
    print('Reports written: reports/control-pack-validation.json and reports/control-pack-validation.md')
    raise SystemExit(0 if overall=='PASS' else 1)
if __name__=='__main__': main()
