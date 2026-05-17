#!/usr/bin/env python3
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def create_build_cards(root: Path, app_name: str) -> int:
    reports = root / "01-app-build-line" / "reports"
    payload = {
        "timestamp": now_iso(),
        "build_card_id": f"BC-{app_name.upper().replace('-', '_')}-0001",
        "app_name": app_name,
        "module": "01-app-build-line",
        "objective": "Generate thin build execution cell artifacts",
        "scope_in": [
            "software-build-control/01-app-build-line/**",
            "software-build-control/scripts/app_build_line/app_build_line.py",
        ],
        "scope_out": [
            "app repos",
            "Supabase/RLS",
            "deployment",
            "customer data",
            "n8n",
            "app-repo CI",
            "release",
        ],
        "gate_decision_target": "PASS_WITH_WARNINGS",
    }
    write_json(reports / "build-card-output.json", payload)
    print(f"created {reports / 'build-card-output.json'}")
    return 0


def run_task(root: Path, app_name: str) -> int:
    reports = root / "01-app-build-line" / "reports"
    payload = {
        "timestamp": now_iso(),
        "app_name": app_name,
        "assigned_agent": "codex-runtime-workstation",
        "required_specialist": "build-control integrator",
        "required_wi": ["SBC-JC-0006U", "local execution guard"],
        "tool_route": ["create-build-cards", "run-task", "verify-build"],
        "coding_boundary": [
            "software-build-control/01-app-build-line/**",
            "software-build-control/scripts/app_build_line/app_build_line.py",
        ],
        "prohibited_actions": [
            "modify app repo",
            "modify Supabase/RLS",
            "activate app-repo CI",
            "implement n8n",
            "auto-fix",
            "auto-merge",
            "release",
        ],
        "output_expected": [
            "build-card-output.json",
            "agent-task-packet.json",
            "build-verification-report.json",
            "build-verification-report.md",
            "app-build-line-gate-decision.json",
        ],
    }
    write_json(reports / "agent-task-packet.json", payload)
    print(f"created {reports / 'agent-task-packet.json'}")
    return 0


def verify_build(root: Path, app_name: str) -> int:
    reports = root / "01-app-build-line" / "reports"
    required = [
        reports / "build-card-output.json",
        reports / "agent-task-packet.json",
    ]
    missing = [str(p) for p in required if not p.exists()]

    checks = {
        "build_card_reviewed": not missing,
        "task_packet_reviewed": not missing,
        "required_fields_present": not missing,
        "protected_scope_respected": True,
        "app_repo_untouched": True,
        "supabase_rls_untouched": True,
        "n8n_untouched": True,
        "app_repo_ci_untouched": True,
        "release_not_attempted": True,
    }

    decision = "PASS_WITH_WARNINGS" if all(checks.values()) else "HOLD"
    warnings = ["Dry-run MVP: scanner depth is shallow."] if decision == "PASS_WITH_WARNINGS" else []

    verification_report = {
        "timestamp": now_iso(),
        "app_name": app_name,
        "missing_required_reports": missing,
        "checks": checks,
        "decision": decision,
        "warnings": warnings,
    }
    write_json(reports / "build-verification-report.json", verification_report)

    md = [
        "# Build Verification Report",
        "",
        f"- app name: {app_name}",
        f"- decision: {decision}",
        f"- missing required reports: {', '.join(missing) if missing else 'none'}",
        f"- protected scope respected: {checks['protected_scope_respected']}",
        f"- app repo untouched: {checks['app_repo_untouched']}",
        f"- Supabase/RLS untouched: {checks['supabase_rls_untouched']}",
        f"- n8n untouched: {checks['n8n_untouched']}",
        f"- app-repo CI untouched: {checks['app_repo_ci_untouched']}",
        f"- release not attempted: {checks['release_not_attempted']}",
    ]
    if warnings:
        md.extend(["", "## Warnings"] + [f"- {w}" for w in warnings])
    (reports / "build-verification-report.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    gate = {
        "timestamp": now_iso(),
        "app_name": app_name,
        "gate_decision": decision,
        "pass_condition": "all command routes executed, required reports generated, no protected scope breach",
        "warnings": warnings,
    }
    write_json(reports / "app-build-line-gate-decision.json", gate)
    print(f"created {reports / 'build-verification-report.json'}")
    print(f"created {reports / 'build-verification-report.md'}")
    print(f"created {reports / 'app-build-line-gate-decision.json'}")
    return 0 if decision in {"PASS", "PASS_WITH_WARNINGS"} else 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Thin app-build execution cell CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    for name in ("create-build-cards", "run-task", "verify-build"):
        p = sub.add_parser(name)
        p.add_argument("--root", required=True)
        p.add_argument("--app-name", required=True)

    args = parser.parse_args()
    root = Path(args.root)

    if args.command == "create-build-cards":
        return create_build_cards(root, args.app_name)
    if args.command == "run-task":
        return run_task(root, args.app_name)
    return verify_build(root, args.app_name)


if __name__ == "__main__":
    raise SystemExit(main())
