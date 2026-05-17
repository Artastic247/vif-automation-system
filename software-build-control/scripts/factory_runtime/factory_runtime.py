from pathlib import Path
import argparse
import json
from datetime import datetime, timezone
from typing import Dict, List


REQUIRED_DIRS = [
    "management-system/audit-programme",
    "management-system/standards-control",
    "management-system/validator-calibration",
    "management-system/process-turtles",
    "management-system/agent-assignment",
    "management-system/work-instructions",
    "management-system/app-development-operating-model",
    "management-system/clause-09-performance-evaluation",
    "management-system/clause-10-improvement",
]


def write_json(path: Path, data: Dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")


def scan_markdown(root: Path) -> Dict[str, List[str]]:
    prompts: List[str] = []
    workflows: List[str] = []
    wi_count = 0

    for p in root.rglob("*.md"):
        try:
            rel = str(p.relative_to(root))
        except Exception:
            rel = str(p)

        name_lower = p.name.lower()
        rel_lower = rel.lower()

        if name_lower.startswith("wi_"):
            wi_count += 1

        # prompt-like files: filename or path contains 'prompt'
        if "prompt" in name_lower or "prompt" in rel_lower:
            title = ""
            try:
                with p.open("r", encoding="utf-8") as fh:
                    first = fh.readline().strip()
                    title = first if first else ""
            except Exception:
                title = ""
            prompts.append(rel)

        # workflow-like files: filename or path contains 'workflow' or 'workflows'
        if "workflow" in name_lower or "workflows" in rel_lower:
            workflows.append(rel)

    return {"prompts": prompts, "workflows": workflows, "wi_count": wi_count}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True, help="Root path to scan (e.g. software-build-control)")
    args = parser.parse_args()

    root = Path(args.root)
    out = root / "reports" / "factory-runtime"

    findings = []
    for rel in REQUIRED_DIRS:
        if not (root / rel).exists():
            findings.append({
                "severity": "BLOCKED",
                "code": "missing_required_directory",
                "path": rel,
                "message": f"Required directory missing: {rel}",
            })

    files = [str(p) for p in root.rglob("*") if p.is_file()]

    md_scan = scan_markdown(root)
    prompt_items = md_scan["prompts"]
    workflow_items = md_scan["workflows"]
    wi_count = md_scan["wi_count"]

    # Gate logic
    if findings:
        gate = "BLOCKED"
    elif wi_count < 30:
        gate = "HOLD"
    else:
        gate = "PASS_WITH_WARNINGS"

    registry = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "root": str(root),
        "total_files": len(files),
        "total_markdown_files": sum(1 for p in root.rglob("*.md") if p.is_file()),
        "wi_count": wi_count,
        "prompt_count": len(prompt_items),
        "workflow_count": len(workflow_items),
        "files": files,
    }

    audit_report = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "finding_count": len(findings),
        "findings": findings,
    }

    gate_decision = {
        "decision": gate,
        "reason": (
            "MVP runtime executed. Full scanner depth still pending."
            if gate == "PASS_WITH_WARNINGS"
            else "See findings or WI count for HOLD/BLOCKED reasons."
        ),
        "blocked_count": sum(1 for f in findings if f["severity"] == "BLOCKED"),
        "hold_count": 1 if (not findings and wi_count < 30) else 0,
        "warning_count": 1 if (not findings and wi_count >= 30 and gate == "PASS_WITH_WARNINGS") else 0,
    }

    write_json(out / "factory-object-registry.json", registry)
    write_json(out / "factory-audit-report.json", audit_report)
    write_json(out / "factory-gate-decision.json", gate_decision)

    # Prompt inventory
    prompt_items_list = []
    for rel in prompt_items:
        prompt_items_list.append({"path": rel})
    write_json(out / "prompt-inventory.json", {"status": "OK", "items": prompt_items_list})

    # Workflow inventory
    workflow_items_list = []
    for rel in workflow_items:
        workflow_items_list.append({"path": rel})
    write_json(out / "workflow-inventory.json", {"status": "OK", "items": workflow_items_list})

    # Placeholders for future scanners
    write_json(out / "process-inventory.json", {"status": "MVP_PLACEHOLDER", "items": []})
    write_json(out / "agent-skill-map.json", {"status": "MVP_PLACEHOLDER", "items": []})

    (out / "factory-audit-report.md").write_text(
        "# VIF Factory Runtime Audit Report\n\n"
        f"Gate decision: **{gate}**\n\n"
        f"Findings: {len(findings)}; WI count: {wi_count}; Prompts: {len(prompt_items)}; Workflows: {len(workflow_items)}\n",
        encoding="utf-8",
    )

    print(f"Factory runtime completed. Gate decision: {gate}")
    print(f"Reports written to: {out}")


if __name__ == "__main__":
    main()
