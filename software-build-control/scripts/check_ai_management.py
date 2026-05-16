#!/usr/bin/env python3
from pathlib import Path
import argparse,json

AI_FILES=[
'management-system/AI_USE_POLICY.md',
'management-system/AI_SYSTEM_INVENTORY.md',
'management-system/AI_RISK_REGISTER.md',
'management-system/AI_IMPACT_ASSESSMENT.md',
'management-system/AI_OUTPUT_VERIFICATION_PROCEDURE.md',
'management-system/HUMAN_OVERSIGHT_MATRIX.md',
'management-system/AI_DATA_GOVERNANCE.md',
'management-system/AI_TOOL_PROVIDER_REVIEW.md',
'management-system/AI_LIFECYCLE_CONTROL.md',
'management-system/AI_BAD_OUTPUT_MONITORING_REGISTER.md',
'management-system/AI_MODEL_TOOL_CHANGE_CONTROL.md',
'management-system/AI_CREDIT_BURN_REGISTER.md',
'management-system/AI_TRACEABILITY_REGISTER.md'
]

COMMON_TERMS=[
'Purpose','Scope','Owner/tool','Inputs','Activities/fields','Outputs/records',
'Linked process','Linked gate','Human approval','Data boundary','PASS/HOLD/BLOCKED rules','PDCA','Update trigger'
]
POLICY_TERMS=['allowed ai uses','prohibited ai uses','no automatic release','no AI-generated PASS without evidence','no uncontrolled app-code changes','no invented emails']
INVENTORY_TERMS=['ChatGPT','Codex','Claude','Lovable','Gemini','Copilot','local LLMs','GitHub Actions','n8n','Supabase AI']
RISK_TERMS=['hallucination','false PASS','context loss','wrong repo','uncontrolled code change','unsafe schema/RLS','customer-data exposure','credit burn','standards/compliance overclaim']
LIFECYCLE_TERMS=['Request','Context pack','Tool route','Prompt approval','AI output','Human review','Verification evidence','Decision','Implementation if approved','Monitoring','Lessons learned']
TRACE_TERMS=['Job card','Prompt','Tool/model','AI output','Files/systems affected','Evidence','Human reviewer','Decision','Verification result','Linked lesson learned']

def read(root:Path,rel:str)->str:
    p=root/rel
    return p.read_text(encoding='utf-8',errors='ignore') if p.exists() else ''

def missing_terms(text:str,terms:list[str])->list[str]:
    low=text.lower()
    return [t for t in terms if t.lower() not in low]

def run_check(root:Path):
    findings=[]
    for rel in AI_FILES:
        p=root/rel
        if not p.is_file():
            findings.append({'file':rel,'type':'missing_file','message':'Required AI management file missing.'})
            continue
        text=read(root,rel)
        miss=missing_terms(text,COMMON_TERMS)
        if miss:
            findings.append({'file':rel,'type':'missing_common_terms','missing_terms':miss})
    targeted={
        'management-system/AI_USE_POLICY.md':POLICY_TERMS,
        'management-system/AI_SYSTEM_INVENTORY.md':INVENTORY_TERMS,
        'management-system/AI_RISK_REGISTER.md':RISK_TERMS,
        'management-system/AI_LIFECYCLE_CONTROL.md':LIFECYCLE_TERMS,
        'management-system/AI_TRACEABILITY_REGISTER.md':TRACE_TERMS
    }
    for rel,terms in targeted.items():
        text=read(root,rel)
        miss=missing_terms(text,terms)
        if miss:
            findings.append({'file':rel,'type':'missing_targeted_terms','missing_terms':miss})
    return {
        'check':'ai_management_controls',
        'status':'PASS' if not findings else 'BLOCKED',
        'summary':'13/13 AI management artefacts present with required control terms.' if not findings else f'{len(findings)} AI management issue(s).',
        'ai_files_expected':len(AI_FILES),
        'findings':findings
    }

def main():
    p=argparse.ArgumentParser(); p.add_argument('--root',default='.')
    a=p.parse_args(); r=run_check(Path(a.root)); print(json.dumps(r,indent=2))
    return 0 if r['status']=='PASS' else 2

if __name__=='__main__': raise SystemExit(main())
