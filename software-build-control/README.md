# Software Build Control System

This repository contains the Software Build Control System foundation and safe automation MVP.

Purpose:
- prevent context drift
- prevent truncation
- control scope
- require job cards before build
- require verification evidence
- control tenant rollout
- prevent false PASS decisions
- support later automation

This package is foundation/control-system only. It must not contain app source code, Supabase secrets, customer data, production deployment files, or active app repair instructions.

Current gate: Remote baseline initialisation.

Automation status:
- validation scripts are safe and read-only except for report generation under reports/
- workflow files are templates only under software-build-control/github/workflows/
- workflows are not active until deliberately copied to .github/workflows/ under a separate approved job card

Do not apply this control pack to DOS FMEA or any app until the relevant job card is approved.
