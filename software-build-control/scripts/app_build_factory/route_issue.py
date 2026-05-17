#!/usr/bin/env python3
"""Route app-build issues into deterministic workflow modes."""
from __future__ import annotations

import json
import os
import re
from pathlib import Path


def pick_route(labels: list[str], body: str) -> str:
    for label in labels:
        if label.startswith("route/"):
            return label.split("/", 1)[1]
    m = re.search(r"(?im)^\s*route\s*:\s*(codex|claude-review|chatgpt-operator|manual-only)\s*$", body or "")
    if m:
        return m.group(1)
    return "manual-only"


def main() -> None:
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    if not event_path:
        raise SystemExit("GITHUB_EVENT_PATH missing")

    event = json.loads(Path(event_path).read_text(encoding="utf-8"))
    issue = event.get("issue", {})
    labels = [x.get("name", "") for x in issue.get("labels", []) if isinstance(x, dict)]
    body = issue.get("body", "")
    issue_number = issue.get("number")

    route = pick_route(labels, body)
    mode = "dry-run" if route in {"manual-only", "chatgpt-operator"} else "pr-write"

    out = Path(os.environ["GITHUB_OUTPUT"])
    with out.open("a", encoding="utf-8") as f:
        f.write(f"route={route}\n")
        f.write(f"mode={mode}\n")
        f.write(f"issue_number={issue_number}\n")


if __name__ == "__main__":
    main()
