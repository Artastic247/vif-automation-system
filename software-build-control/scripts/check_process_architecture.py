#!/usr/bin/env python3
from pathlib import Path
import argparse,json

PROCESS_IDS=[
'MOP-01','MOP-02','MOP-03','MOP-04','MOP-05','MOP-06','MOP-07',
'COP-01','COP-02','COP-03','COP-04','COP-05','COP-06','COP-07','COP-08','COP-09','COP-10','COP-11','COP-12','COP-13','COP-14','COP-15','COP-16',
'SOP-01','SOP-02','SOP-03','SOP-04','SOP-05','SOP-06','SOP-07','SOP-08','SOP-09','SOP-10','SOP-11','SOP-12'
]

FILES=[
'management-system/PROCESS_ARCHITECTURE.md',
'management-system/PROCESS_REGISTER.md',
'management-system/PROCESS_INTERACTION_MAP.md',
'management-system/PDCA_PROCESS_MODEL.md',
'management-system/PROCESS_TURTLE_TEMPLATE.md',
'management-system/PROCESS_OWNER_MATRIX.md',
'management-system/PROCESS_KPI_REGISTER.md',
'management-system/PROCESS_RISK_CONTROL_REGISTER.md',
'management-system/PROCESS_RECORDS_MATRIX.md',
'management-system/PROCESS_GATE_MATRIX.md'
]

REQUIRED_REGISTER_TERMS=['Process ID','Owner/agent','Inputs','Activities','Outputs','Records/evidence','KPI','Key risk','Key controls','Linked gate','PDCA status']
REQUIRED_PDCA_TERMS=['PLAN','DO','CHECK','ACT']
REQUIRED_TURTLE_TERMS=['Inputs','Outputs','Owner','Resources/tools','Methods/skills','Measures/KPIs','Risks','Controls','Records/evidence','Interfaces','PLAN','DO','CHECK','ACT']

def read(root:Path,rel:str)->str:
    p=root/rel
    return p.read_text(encoding='utf-8',errors='ignore') if p.exists() else ''

def missing_terms(text:str,terms:list[str])->list[str]:
    low=text.lower()
    return [t for t in terms if t.lower() not in low]

def run_check(root:Path):
    findings=[]
    for rel in FILES:
        if not (root/rel).is_file():
            findings.append({'file':rel,'type':'missing_file','message':'Required process architecture file missing.'})
    register=read(root,'management-system/PROCESS_REGISTER.md')
    pdca=read(root,'management-system/PDCA_PROCESS_MODEL.md')
    turtle=read(root,'management-system/PROCESS_TURTLE_TEMPLATE.md')
    for pid in PROCESS_IDS:
        if pid not in register:
            findings.append({'file':'management-system/PROCESS_REGISTER.md','type':'missing_process_id','process_id':pid})
        if pid not in pdca:
            findings.append({'file':'management-system/PDCA_PROCESS_MODEL.md','type':'missing_pdca_process_id','process_id':pid})
    for term in missing_terms(register,REQUIRED_REGISTER_TERMS):
        findings.append({'file':'management-system/PROCESS_REGISTER.md','type':'missing_register_term','term':term})
    for term in missing_terms(pdca,REQUIRED_PDCA_TERMS):
        findings.append({'file':'management-system/PDCA_PROCESS_MODEL.md','type':'missing_pdca_term','term':term})
    for term in missing_terms(turtle,REQUIRED_TURTLE_TERMS):
        findings.append({'file':'management-system/PROCESS_TURTLE_TEMPLATE.md','type':'missing_turtle_term','term':term})
    return {
        'check':'process_architecture',
        'status':'PASS' if not findings else 'BLOCKED',
        'summary':'35/35 processes present with explicit process architecture and PDCA checks.' if not findings else f'{len(findings)} process architecture issue(s).',
        'process_count_expected':len(PROCESS_IDS),
        'findings':findings
    }

def main():
    p=argparse.ArgumentParser(); p.add_argument('--root',default='.')
    a=p.parse_args(); r=run_check(Path(a.root)); print(json.dumps(r,indent=2))
    return 0 if r['status']=='PASS' else 2

if __name__=='__main__': raise SystemExit(main())
