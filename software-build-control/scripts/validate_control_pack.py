import argparse, importlib.util, json
from datetime import datetime, timezone
from pathlib import Path
CHECKS=['check_required_artifacts.py','check_template_fields.py','check_clause_09_performance_evaluation.py','check_secret_risk.py','check_large_files.py','check_forbidden_patterns.py','check_evidence_completeness.py']
def load(p):
    s=importlib.util.spec_from_file_location(p.stem,p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
def rollup(rs):
    vals=[r.get('status','HOLD') for r in rs]
    return 'BLOCKED' if 'BLOCKED' in vals else ('HOLD' if 'HOLD' in vals else ('PASS_WITH_WARNINGS' if 'PASS_WITH_WARNINGS' in vals else 'PASS'))
def write_md(r,p):
    lines=['# Control Pack Validation Report','',f"- Generated: `{r['generated_at']}`",f"- Mode: `{r['mode']}`",f"- Overall status: **{r['status']}**",'','| Check | Status | Summary |','|---|---|---|']
    [lines.append(f"| {c.get('check')} | {c.get('status')} | {str(c.get('summary','')).replace('|','/')} |") for c in r['checks']]
    p.write_text('\n'.join(lines)+'\n')
def run(root,mode='control-pack'):
    root=Path(root).resolve(); sd=Path(__file__).resolve().parent
    results=[load(sd/c).run_check(root) for c in CHECKS]
    report={'generated_at':datetime.now(timezone.utc).isoformat(),'root':str(root),'mode':mode,'status':rollup(results),'checks':results,'gate_controls':{'clause_09_mla_added':True,'github_ci_pilot':'manual/read-only/control-system-only','app_repo_ci':'HOLD','n8n':'HOLD','auto_fix':'BLOCKED','auto_merge':'BLOCKED','auto_release':'BLOCKED','app_onboarding':'HOLD','dos_fmea_repair':'HOLD'},'safe_automation_boundaries':{'read_only_source_inspection':True,'writes_reports_only':True,'external_services_called':False,'deploys':False,'auto_merge':False,'supabase_schema_or_rls_changes':False,'customer_data_access':False,'ci_activation':False,'n8n_implemented':False,'app_repo_modified':False}}
    (root/'reports').mkdir(exist_ok=True); (root/'reports/control-pack-validation.json').write_text(json.dumps(report,indent=2)); write_md(report,root/'reports/control-pack-validation.md'); return report
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',default='.'); ap.add_argument('--mode',default='control-pack'); a=ap.parse_args(); r=run(Path(a.root),a.mode)
    print('Control Pack Validation: '+r['status'])
    [print(f"- {c.get('check')}: {c.get('status')} — {c.get('summary')}") for c in r['checks']]
    print('Reports written:\n- reports/control-pack-validation.json\n- reports/control-pack-validation.md')
    return 0 if r['status'] in ['PASS','PASS_WITH_WARNINGS'] else 2
if __name__=='__main__': raise SystemExit(main())
