#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json
from datetime import datetime, timezone
from pathlib import Path

CHECKS=[
    'check_required_artifacts.py',
    'check_template_fields.py',
    'check_process_architecture.py',
    'check_secret_risk.py',
    'check_large_files.py',
    'check_forbidden_patterns.py',
    'check_evidence_completeness.py'
]

def load(p):
    spec=importlib.util.spec_from_file_location(p.stem,p)
    m=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

def status(results):
    vals=[r.get('status','HOLD') for r in results]
    return 'BLOCKED' if 'BLOCKED' in vals else ('HOLD' if 'HOLD' in vals else 'PASS')

def write_md(report,path):
    lines=['# Control Pack Validation Report','',f"- Generated: `{report['generated_at']}`",f"- Mode: `{report['mode']}`",f"- Overall status: **{report['status']}**",'','| Check | Status | Summary |','|---|---|---|']
    for r in report['checks']:
        lines.append(f"| {r.get('check')} | {r.get('status')} | {str(r.get('summary','')).replace('|','/')} |")
    path.write_text('\n'.join(lines)+'\n',encoding='utf-8')

def run(root:Path,mode='control-pack'):
    root=root.resolve(); results=[]; sd=Path(__file__).resolve().parent
    for c in CHECKS:
        results.append(load(sd/c).run_check(root))
    report={
        'generated_at':datetime.now(timezone.utc).isoformat(),
        'root':str(root),
        'mode':mode,
        'status':status(results),
        'checks':results,
        'safe_automation_boundaries':{
            'read_only_source_inspection':True,
            'writes_reports_only':True,
            'external_services_called':False,
            'deploys':False,
            'auto_merge':False,
            'supabase_schema_or_rls_changes':False,
            'customer_data_access':False,
            'ci_activation':False,
            'n8n_implemented':False,
            'app_repo_modified':False
        }
    }
    rd=root/'reports'; rd.mkdir(parents=True,exist_ok=True)
    (rd/'control-pack-validation.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    write_md(report,rd/'control-pack-validation.md')
    return report

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--root',default='.')
    ap.add_argument('--mode',default='control-pack',choices=['control-pack','app-scan'])
    a=ap.parse_args(); r=run(Path(a.root),a.mode)
    print(f"Control Pack Validation: {r['status']}")
    for c in r['checks']:
        print(f"- {c.get('check')}: {c.get('status')} — {c.get('summary')}")
    print('Reports written:\n- reports/control-pack-validation.json\n- reports/control-pack-validation.md')
    return 0 if r['status']=='PASS' else 2

if __name__=='__main__': raise SystemExit(main())
