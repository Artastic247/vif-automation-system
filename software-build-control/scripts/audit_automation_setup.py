#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def run(root: Path) -> dict:
    findings = []

    required_files = [
        "github/workflows/app-build-line-smoke.yml",
        "management-system/HOOK_REGISTER.md",
        "scripts/check_prompt_context.py",
        "scripts/check_hook_controls.py",
        "01-app-build-line/reports/MLA_ASSESSMENT_SUMMARY.md",
        "01-app-build-line/reports/FULL_MATURITY_AND_IATF_APPLICATION_UPDATE.md",
        "reports/prompt-context-check.json",
        "reports/hook-controls-check.json",
        "reports/control-pack-validation.json",
    ]

    for rel in required_files:
        if not (root / rel).is_file():
            findings.append({"type": "missing_file", "file": rel})

    # Status checks
    try:
        prompt = load_json(root / "reports/prompt-context-check.json")
        if prompt.get("status") != "PASS":
            findings.append({"type": "status_mismatch", "file": "reports/prompt-context-check.json", "expected": "PASS", "actual": prompt.get("status")})
    except Exception as exc:
        findings.append({"type": "json_error", "file": "reports/prompt-context-check.json", "error": str(exc)})

    try:
        hook = load_json(root / "reports/hook-controls-check.json")
        if hook.get("status") != "PASS":
            findings.append({"type": "status_mismatch", "file": "reports/hook-controls-check.json", "expected": "PASS", "actual": hook.get("status")})
    except Exception as exc:
        findings.append({"type": "json_error", "file": "reports/hook-controls-check.json", "error": str(exc)})

    try:
        control = load_json(root / "reports/control-pack-validation.json")
        if control.get("status") != "PASS":
            findings.append({"type": "status_mismatch", "file": "reports/control-pack-validation.json", "expected": "PASS", "actual": control.get("status")})
    except Exception as exc:
        findings.append({"type": "json_error", "file": "reports/control-pack-validation.json", "error": str(exc)})

    return {
        "audit": "automation_setup_file_audit",
        "status": "PASS" if not findings else "HOLD",
        "summary": "Automation setup audit passed." if not findings else f"{len(findings)} finding(s) detected.",
        "findings": findings,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="software-build-control")
    parser.add_argument("--out", default="")
    args = parser.parse_args()

    result = run(Path(args.root))
    payload = json.dumps(result, indent=2)
    if args.out:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(payload + "\n", encoding="utf-8")
    print(payload)
    return 0 if result["status"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
