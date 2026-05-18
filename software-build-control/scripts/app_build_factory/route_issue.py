#!/usr/bin/env python3
"""Route app-build issues into deterministic workflow modes."""
from __future__ import annotations

import json
import os
import re
from pathlib import Path

ALLOWED_ROUTES = {"codex", "claude-review", "chatgpt-operator", "manual-only"}
READINESS_HOLD_VALUES = {"fail", "failed", "false", "hold", "not-ready", "not_ready", "blocked"}


def _from_labels(labels: list[str]) -> str | None:
    for label in labels:
        if label.startswith("route/"):
            candidate = label.split("/", 1)[1].strip()
            if candidate in ALLOWED_ROUTES:
                return candidate
            return "manual-only"
    return None


def _from_body(body: str) -> str | None:
    body = body or ""
    simple = re.search(r"(?im)^\s*route\s*:\s*([^\n\r#]+)\s*$", body)
    if simple:
        candidate = simple.group(1).strip().lower()
        return candidate if candidate in ALLOWED_ROUTES else "manual-only"

    form = re.search(r"(?ims)^\s*###\s*Initial route\s*$\s*([^\n\r]+)", body)
    if form:
        candidate = form.group(1).strip().lower()
        return candidate if candidate in ALLOWED_ROUTES else "manual-only"

    return None


def pick_route(labels: list[str], body: str) -> str:
    return _from_labels(labels) or _from_body(body) or "manual-only"


def readiness_failed() -> bool:
    """Return True when the workflow environment explicitly requests a HOLD state."""
    readiness = os.environ.get("VIF_TOOLCHAIN_READINESS", "ready").strip().lower()
    return readiness in READINESS_HOLD_VALUES


def _get_issue_number(event: dict) -> str:
    dispatch_number = event.get("inputs", {}).get("issue_number")
    if dispatch_number not in (None, ""):
        return str(dispatch_number)

    issue_number = event.get("issue", {}).get("number")
    if issue_number not in (None, ""):
        return str(issue_number)

    raise SystemExit("issue_number missing")


def main() -> None:
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    if not event_path:
        raise SystemExit("GITHUB_EVENT_PATH missing")

    event = json.loads(Path(event_path).read_text(encoding="utf-8"))
    issue = event.get("issue", {})
    labels = [x.get("name", "") for x in issue.get("labels", []) if isinstance(x, dict)]
    body = issue.get("body", "")

    issue_number = _get_issue_number(event)
    route = pick_route(labels, body)
    mode = "dry-run"
    readiness_decision = "PASS"

    if readiness_failed():
        route = "manual-only"
        mode = "hold"
        readiness_decision = "HOLD"

    out = Path(os.environ["GITHUB_OUTPUT"])
    with out.open("a", encoding="utf-8") as f:
        f.write(f"route={route}\n")
        f.write(f"mode={mode}\n")
        f.write(f"issue_number={issue_number}\n")
        f.write(f"readiness_decision={readiness_decision}\n")


if __name__ == "__main__":
    main()
