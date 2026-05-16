from pathlib import Path
HEADINGS=['Purpose','Scope','Owner/agent','Inputs','Activities/method','Outputs/records','Evidence required','MLA / maturity dependency','Linked process','Linked gate','PASS/HOLD/BLOCKED rules','Escalation','Update trigger']
def run_check(root):
    root=Path(root); findings=[]
    for p in (root/'management-system/clause-09-performance-evaluation').glob('*.md'):
        txt=p.read_text(errors='ignore')
        for h in HEADINGS:
            if h.lower() not in txt.lower(): findings.append({'path':str(p.relative_to(root)),'severity':'HOLD','issue':f'missing {h}'})
    return {'check':'template_fields','status':'PASS' if not findings else 'HOLD','summary':'Clause 9 required headings present.' if not findings else f'{len(findings)} heading findings.','findings':findings}
