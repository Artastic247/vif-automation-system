#!/usr/bin/env python3
import json
import os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "01-app-build-line" / "reports"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def main() -> int:
    verification = load_json(REPORTS / "build-verification-report.json")
    gate = load_json(REPORTS / "app-build-line-gate-decision.json")

    repo_slug = os.getenv("GITHUB_REPOSITORY", "<org>/<repo>")
    default_branch = os.getenv("DEFAULT_BRANCH", "main")

    snapshot = {
        "timestamp": now_iso(),
        "mode": "linked-dry-run",
        "control_links": {
            "open_app_build_issues": f"https://github.com/{repo_slug}/issues?q=is%3Aopen+label%3Aapp-build-line",
            "in_flight_app_build_prs": f"https://github.com/{repo_slug}/pulls?q=is%3Aopen+software-build-control",
            "failing_required_checks": f"https://github.com/{repo_slug}/pulls?q=is%3Aopen+status%3Afailure",
            "workflow_runs": f"https://github.com/{repo_slug}/actions/workflows/app-build-line-smoke.yml",
        },
        "auth_safeguards": {
            "openai_api_key_configured": bool(os.getenv("OPENAI_API_KEY")),
            "github_app_installed_for_automation": "manual-review-required",
            "branch_protection_main": "manual-review-required",
            "required_checks_configured": "manual-review-required",
        },
        "last_known_good_run": {
            "replay_key": gate.get("timestamp", "unknown"),
            "branch": default_branch,
            "pr": "manual-link-required",
            "evidence_artifact": "app-build-line-smoke-evidence",
            "app_name": verification.get("app_name", "unknown"),
            "gate_decision": gate.get("gate_decision", "unknown"),
        },
    }

    out = REPORTS / "operator-panel-snapshot.json"
    out.write_text(json.dumps(snapshot, indent=2) + "\n", encoding="utf-8")
    print(f"created {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
