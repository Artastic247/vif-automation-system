#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

REQUIRED_SECTIONS = [
    "## Purpose",
    "## Scope",
    "## Inputs",
    "## Activities",
    "## Outputs/records",
    "## Hook inventory",
    "## Audit criteria",
    "## Linked gate",
    "## Update trigger",
]

REQUIRED_COLUMNS = [
    "Hook ID",
    "Hook name",
    "Owner role",
    "Trigger point",
    "Purpose",
    "Test cadence",
    "Last test date",
    "Next test due",
    "Rollback route",
    "Break-glass condition",
    "Current status",
    "Evidence ref",
]


def run(root: Path) -> dict:
    rel = "management-system/HOOK_REGISTER.md"
    path = root / rel
    findings: list[dict] = []

    if not path.is_file():
        findings.append({"file": rel, "type": "missing_file", "message": "Hook register file is required."})
    else:
        text = path.read_text(encoding="utf-8", errors="ignore")
        missing_sections = [s for s in REQUIRED_SECTIONS if s not in text]
        if missing_sections:
            findings.append({"file": rel, "type": "missing_sections", "missing": missing_sections})

        header_line = next((line for line in text.splitlines() if line.strip().startswith("| Hook ID |")), "")
        missing_columns = [c for c in REQUIRED_COLUMNS if c not in header_line]
        if missing_columns:
            findings.append({"file": rel, "type": "missing_columns", "missing": missing_columns})

        inventory_rows = [line for line in text.splitlines() if line.strip().startswith("| HK-")]
        if len(inventory_rows) < 3:
            findings.append({
                "file": rel,
                "type": "insufficient_inventory_rows",
                "message": "At least 3 managed hooks must be registered.",
                "count": len(inventory_rows),
            })

    return {
        "check": "hook_controls",
        "status": "PASS" if not findings else "BLOCKED",
        "summary": "Hook register and lifecycle controls are present." if not findings else f"{len(findings)} hook control issue(s).",
        "findings": findings,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    args = parser.parse_args()

    result = run(Path(args.root))
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
