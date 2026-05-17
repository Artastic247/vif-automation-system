#!/usr/bin/env python3
"""Route app-build events into deterministic workflow modes."""
from __future__ import annotations

import json
import os
import re
from pathlib import Path

ALLOWED_ROUTES = {"codex", "claude-review", "chatgpt-operator", "manual-only"}
ROUTE_LINE_RE = re.compile(r"(?im)^\s*route\s*:\s*(codex|claude-review|chatgpt-operator|manual-only)\s*$")
ISSUE_FORM_ROUTE_RE = re.compile(
    r"(?is)^\s*###\s*Initial\s+route\s*$\s*^(codex|claude-review|chatgpt-operator|manual-only)\s*$",
    re.MULTILINE,
)


def parse_route(labels: list[str], issue_body: str) -> str:
    for label in labels:
        if label.startswith("route/"):
            candidate = label.split("/", 1)[1].strip()
            if candidate in ALLOWED_ROUTES:
                return candidate

    m = ROUTE_LINE_RE.search(issue_body or "")
    if m:
        return m.group(1)

    m = ISSUE_FORM_ROUTE_RE.search(issue_body or "")
    if m:
        return m.group(1)

    return "manual-only"


def main() -> None:
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    event_name = os.environ.get("GITHUB_EVENT_NAME", "")
    if not event_path:
        raise SystemExit("GITHUB_EVENT_PATH missing")

    event = json.loads(Path(event_path).read_text(encoding="utf-8"))
    issue = event.get("issue", {})
    labels = [x.get("name", "") for x in issue.get("labels", []) if isinstance(x, dict)]
    issue_body = issue.get("body", "")

    issue_number = issue.get("number")
    if event_name == "workflow_dispatch":
        issue_number = (event.get("inputs") or {}).get("issue_number")

    if issue_number in (None, "", "None"):
        raise SystemExit("issue_number missing")

    route = parse_route(labels, issue_body)
    if route not in ALLOWED_ROUTES:
        route = "manual-only"
    mode = "dry-run"
    replay_key = f"issue-{issue_number}-r1"

    out = Path(os.environ["GITHUB_OUTPUT"])
    with out.open("a", encoding="utf-8") as f:
        f.write(f"route={route}\n")
        f.write(f"mode={mode}\n")
        f.write(f"issue_number={issue_number}\n")
        f.write(f"replay_key={replay_key}\n")


if __name__ == "__main__":
    main()
