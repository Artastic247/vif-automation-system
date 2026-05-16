from pathlib import Path
BASE=Path('management-system/clause-09-performance-evaluation')
FILES='''MLA_ASSESSMENT_PROCEDURE.md MLA_ASSESSMENT_REGISTER.md MLA_EVIDENCE_MATRIX.md MLA_UPGRADE_DOWNGRADE_RULES.md MLA_AUTOMATION_PERMISSION_MATRIX.md MLA_AUDIT_REQUIREMENTS.md MLA_MATURITY_OVERSTATEMENT_CONTROL.md CLAUSE_09_PERFORMANCE_EVALUATION_OVERVIEW.md MONITORING_MEASUREMENT_ANALYSIS_EVALUATION.md INTERNAL_AUDIT_PROCEDURE.md AUDIT_PROGRAMME.md AUDIT_CRITERIA_REGISTER.md AUDIT_FINDINGS_REGISTER.md MANAGEMENT_REVIEW_INPUT_REGISTER.md PROCESS_AUDIT_CHECKLIST.md AGENT_AUDIT_CHECKLIST.md SKILL_WORK_INSTRUCTION_AUDIT_CHECKLIST.md PROCEDURE_AUDIT_CHECKLIST.md WORKFLOW_AUDIT_CHECKLIST.md PROMPT_AUDIT_CHECKLIST.md CONTEXT_PACK_AUDIT_CHECKLIST.md APP_PRODUCT_AUDIT_CHECKLIST.md AI_MODEL_TOOL_AUDIT_CHECKLIST.md AI_OUTPUT_AUDIT_CHECKLIST.md INFORMATION_SECURITY_DATA_AUDIT_CHECKLIST.md EVIDENCE_AUDIT_CHECKLIST.md RELEASE_AUDIT_CHECKLIST.md VALIDATOR_CHECK_AUDIT_CHECKLIST.md SUPPLIER_TOOL_PROVIDER_AUDIT_CHECKLIST.md N8N_READINESS_AUDIT_CHECKLIST.md GITHUB_CI_PILOT_AUDIT_RECORD.md'''.split()
HEADINGS=['Purpose','Scope','Owner/agent','Inputs','Activities/method','Outputs/records','Evidence required','MLA / maturity dependency','Linked process','Linked gate','PASS/HOLD/BLOCKED rules','Escalation','Update trigger']
REQ_PHRASES=['M0','M1','M2','M3','M4','M5','evidence','upgrade','downgrade','audit frequency','automation permission','maturity overstatement']
CI_PHRASES=['manual/read-only/control-system-only','app-repo CI','HOLD','expansion','auto-fix','BLOCKED','auto-merge','auto-release']
def has(t,s): return s.lower() in t.lower()
def run_check(root):
    root=Path(root); folder=root/BASE; findings=[]
    if not folder.is_dir():
        return {'check':'clause_09_performance_evaluation','status':'BLOCKED','summary':'Clause 9 folder missing.','findings':[{'path':str(BASE),'severity':'BLOCKED'}]}
    for f in FILES:
        p=folder/f
        if not p.is_file(): findings.append({'path':str(BASE/f),'severity':'BLOCKED','issue':'missing'}); continue
        txt=p.read_text(errors='ignore')
        if len(txt.strip())<250: findings.append({'path':str(BASE/f),'severity':'BLOCKED','issue':'placeholder'})
        for h in HEADINGS:
            if not has(txt,h): findings.append({'path':str(BASE/f),'severity':'HOLD','issue':'missing '+h})
        if not (has(txt,'Audit criteria') or has(txt,'Maturity criteria') or has(txt,'Assessment criteria') or has(txt,'Evidence criteria')):
            findings.append({'path':str(BASE/f),'severity':'HOLD','issue':'missing audit criteria/equivalent'})
        if not has(txt,'Management-review input'):
            findings.append({'path':str(BASE/f),'severity':'HOLD','issue':'missing management-review input'})
    mla='\n'.join((folder/f).read_text(errors='ignore') for f in FILES if f.startswith('MLA_') and (folder/f).exists())
    for x in REQ_PHRASES:
        if not has(mla,x): findings.append({'path':str(BASE),'severity':'HOLD','issue':'missing MLA phrase '+x})
    af=(folder/'AUDIT_FINDINGS_REGISTER.md').read_text(errors='ignore') if (folder/'AUDIT_FINDINGS_REGISTER.md').exists() else ''
    for x in ['NC','RCA','CAPA','trigger']:
        if not has(af,x): findings.append({'path':str(BASE/'AUDIT_FINDINGS_REGISTER.md'),'severity':'HOLD','issue':'missing '+x})
    n8n=(folder/'N8N_READINESS_AUDIT_CHECKLIST.md').read_text(errors='ignore') if (folder/'N8N_READINESS_AUDIT_CHECKLIST.md').exists() else ''
    if not (has(n8n,'n8n') and has(n8n,'HOLD')): findings.append({'path':str(BASE/'N8N_READINESS_AUDIT_CHECKLIST.md'),'severity':'HOLD','issue':'n8n HOLD not explicit'})
    ci=(folder/'GITHUB_CI_PILOT_AUDIT_RECORD.md').read_text(errors='ignore') if (folder/'GITHUB_CI_PILOT_AUDIT_RECORD.md').exists() else ''
    for x in CI_PHRASES:
        if not has(ci,x): findings.append({'path':str(BASE/'GITHUB_CI_PILOT_AUDIT_RECORD.md'),'severity':'HOLD','issue':'missing CI phrase '+x})
    status='BLOCKED' if any(f['severity']=='BLOCKED' for f in findings) else ('HOLD' if findings else 'PASS')
    return {'check':'clause_09_performance_evaluation','status':status,'summary':'Clause 9 / MLA artefacts validated.' if status=='PASS' else f'{len(findings)} Clause 9 findings.','findings':findings}
