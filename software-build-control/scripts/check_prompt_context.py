#!/usr/bin/env python3
from pathlib import Path
import argparse,json

PROMPT_FILES=[
'management-system/PROMPT_CONTROL_PROCEDURE.md',
'management-system/PROMPT_REGISTER.md',
'management-system/PROMPT_QUALITY_CHECKLIST.md',
'management-system/PROMPT_FAILURE_REGISTER.md',
'management-system/PROMPT_REVISION_CONTROL.md',
'management-system/FORBIDDEN_PROMPT_PATTERNS.md',
'management-system/APPROVED_PROMPT_LIBRARY.md',
'management-system/CONTEXT_PACK_STANDARD.md',
'management-system/SOURCE_OF_TRUTH_LOCK_PROCEDURE.md',
'management-system/NO_TRUNCATION_WORK_INSTRUCTION.md',
'management-system/TOOL_SPECIFIC_PROMPT_INSTRUCTIONS.md'
]

COMMON_TERMS=['Purpose','Scope','Inputs','Activities','Outputs','Owner/tool','Linked process','Linked gate','Records','PDCA','PASS/HOLD/BLOCKED','Update trigger']
QUALITY_TERMS=['objective','source basis','mode','scope in','scope out','prohibited changes','required inputs','required outputs','evidence required','verification method','rollback route','stop condition','tool routing','secret-safety','customer-data','no implementation without approved job card']
FAILURE_TERMS=['Failure ID','date','app/project','tool/model','prompt used or summary','failure type','drift observed','impact','root cause','correction','corrective action','linked lesson learned','effectiveness check']
FORBIDDEN_TERMS=['fix everything','make it work','complete the backend','build all features','clean up everything','improve the app','continue from previous chat','use all tools','release/publish','change schema/RLS','apply to all tenants','use customer data for testing']
CONTEXT_TERMS=['app identity','repo','branch/version','current commit','current job card','current gate','source-of-truth artefacts','latest evidence pack','known defects','current exclusions','tenant/environment context','rollback context','latest decision','unresolved gaps','no-truncation rule','archive/reference handling']
TOOL_TERMS=['ChatGPT architecture/review','Lovable plan-mode','Lovable build/repair','Codex repo-inspection','Codex patch','Claude/Claude Code','Gemini/local LLM','Copilot inline-assist','n8n prompt/automation']
JOB_CARD_TERMS=['no implementation prompt without approved job card','no build prompt without scope in/out','no repair prompt without defect evidence','no schema/RLS prompt without runtime/database gate','no release prompt without verification and rollback evidence','no tenant rollout prompt without tenant rollout register']

def read(root:Path,rel:str)->str:
    p=root/rel
    return p.read_text(encoding='utf-8',errors='ignore') if p.exists() else ''

def missing_terms(text:str,terms:list[str])->list[str]:
    low=text.lower()
    return [t for t in terms if t.lower() not in low]

def run_check(root:Path):
    findings=[]
    for rel in PROMPT_FILES:
        if not (root/rel).is_file():
            findings.append({'file':rel,'type':'missing_file','message':'Required prompt/context control file missing.'})
            continue
        text=read(root,rel)
        miss=missing_terms(text,COMMON_TERMS)
        if miss:
            findings.append({'file':rel,'type':'missing_common_terms','missing_terms':miss})
    targeted={
        'management-system/PROMPT_QUALITY_CHECKLIST.md':QUALITY_TERMS,
        'management-system/PROMPT_FAILURE_REGISTER.md':FAILURE_TERMS,
        'management-system/FORBIDDEN_PROMPT_PATTERNS.md':FORBIDDEN_TERMS,
        'management-system/CONTEXT_PACK_STANDARD.md':CONTEXT_TERMS,
        'management-system/TOOL_SPECIFIC_PROMPT_INSTRUCTIONS.md':TOOL_TERMS,
        'management-system/PROMPT_CONTROL_PROCEDURE.md':JOB_CARD_TERMS
    }
    for rel,terms in targeted.items():
        text=read(root,rel)
        miss=missing_terms(text,terms)
        if miss:
            findings.append({'file':rel,'type':'missing_targeted_terms','missing_terms':miss})
    return {
        'check':'prompt_context_controls',
        'status':'PASS' if not findings else 'BLOCKED',
        'summary':'11/11 prompt and context-control artefacts present with required control terms.' if not findings else f'{len(findings)} prompt/context issue(s).',
        'prompt_context_files_expected':len(PROMPT_FILES),
        'findings':findings
    }

def main():
    p=argparse.ArgumentParser(); p.add_argument('--root',default='.')
    a=p.parse_args(); r=run_check(Path(a.root)); print(json.dumps(r,indent=2))
    return 0 if r['status']=='PASS' else 2

if __name__=='__main__': raise SystemExit(main())
