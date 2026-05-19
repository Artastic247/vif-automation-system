#!/usr/bin/env python3
"""Guard VIF factory auto-merge eligibility.

This script is intentionally deterministic. It allows auto-merge only for
factory-created memory-ingest PRs whose changed files are generated
factory-memory outputs and whose PR discussion already contains AUTO-002 PASS.
"""
from __future__ import annotations

import argparse
import fnmatch
from pathlib import Path
from typing import Iterable, Sequence

ALLOWED_MEMORY_OUTPUT_PATTERNS = (
    "factory-memory/chats/inbox/*.md",
    "factory-memory/chats/summaries/*.md",
    "factory-memory/decisions/*.md",
    "factory-memory/lessons-learned/*.md",
    "factory-memory/skills/*.md",
)

FORBIDDEN_PATTERNS = (
    ".codex/**",
    ".github/**",
    "software-build-control/**",
    "factory-memory/registers/**",
    "factory-memory/instructions/**",
    "factory-memory/agents/**",
    "factory-memory/plugins/**",
    "factory-memory/deployments/**",
    "supabase/**",
    "**/supabase/**",
    "deployment/**",
    "deploy/**",
    "**/deployment/**",
    "**/deploy/**",
    "apps/**",
    "app/**",
    "**/customer-data/**",
    "**/customer_data/**",
)

AUTO_002_PASS_TOKEN = "AUTO-002 Review Result: PASS"
AUTO_002_HOLD_TOKEN = "AUTO-002 Review Result: HOLD"


def read_lines(path: str) -> list[str]:
    p = Path(path)
    if not p.exists():
        return []
    return [line.strip() for line in p.read_text(encoding="utf-8").splitlines() if line.strip()]


def read_text(path: str) -> str:
    p = Path(path)
    if not p.exists():
        return ""
    return p.read_text(encoding="utf-8")


def matches_any(path: str, patterns: Sequence[str]) -> bool:
    return any(fnmatch.fnmatch(path, pattern) for pattern in patterns)


def add_all(lines: list[str], prefix: str, values: Iterable[str]) -> None:
    for value in values:
        lines.append(f"- {prefix}: `{value}`")


def build_report(args: argparse.Namespace) -> tuple[str, int]:
    changed_files = read_lines(args.changed_files_file)
    comments = read_text(args.comments_file)
    hard_failures: list[str] = []
    pending: list[str] = []
    passed: list[str] = []

    title = args.title.strip()
    head_branch = args.head_branch.strip()
    is_draft = args.is_draft.strip().lower() == "true"

    if is_draft:
        hard_failures.append("PR is still draft")
    else:
        passed.append("PR is not draft")

    if title.startswith("AUTO: Issue #") and "Factory memory ingest" in title:
        passed.append("PR title matches factory-memory ingest route")
    else:
        hard_failures.append("PR title is not a factory-memory ingest title")

    if head_branch.startswith("auto-issue-") and "auto-003-factory-memory" in head_branch:
        passed.append("Head branch matches AUTO-003 factory-memory route")
    else:
        hard_failures.append("Head branch is not an AUTO-003 factory-memory branch")

    if changed_files:
        passed.append("Changed-file list is present")
    else:
        hard_failures.append("Changed-file list is empty")

    forbidden_files = [path for path in changed_files if matches_any(path, FORBIDDEN_PATTERNS)]
    out_of_scope_files = [path for path in changed_files if not matches_any(path, ALLOWED_MEMORY_OUTPUT_PATTERNS)]

    if forbidden_files:
        hard_failures.append("Protected or control files changed")
    else:
        passed.append("No protected or control files changed")

    if out_of_scope_files:
        hard_failures.append("Files outside generated factory-memory output scope changed")
    else:
        passed.append("All changed files are generated factory-memory outputs")

    if AUTO_002_HOLD_TOKEN in comments:
        hard_failures.append("AUTO-002 HOLD is present in PR discussion")
    elif AUTO_002_PASS_TOKEN in comments:
        passed.append("AUTO-002 PASS is present in PR discussion")
    else:
        pending.append("AUTO-002 PASS is not present yet")

    if hard_failures:
        result = "HOLD"
        exit_code = 1
        recommendation = "Do not request auto-merge. Remove the factory-auto-merge label or repair the PR."
    elif pending:
        result = "PENDING"
        exit_code = 2
        recommendation = "Leave the PR open. The auto-merge guard can retry after AUTO-002 posts PASS."
    else:
        result = "PASS"
        exit_code = 0
        recommendation = "Request GitHub auto-merge for this generated memory PR."

    lines = [
        f"# Factory Auto-Merge Guard: {result}",
        "",
        f"PR number: `#{args.pr_number}`",
        f"Head branch: `{head_branch}`",
        f"Title: `{title}`",
        "",
        "## Changed files",
        "",
    ]

    if changed_files:
        lines.extend([f"- `{path}`" for path in changed_files])
    else:
        lines.append("- `(none)`")

    lines.extend(["", "## Checks passed", ""])
    lines.extend([f"- {item}" for item in passed] if passed else ["- `(none)`"])

    lines.extend(["", "## Pending", ""])
    lines.extend([f"- {item}" for item in pending] if pending else ["- `(none)`"])

    lines.extend(["", "## Checks failed", ""])
    lines.extend([f"- {item}" for item in hard_failures] if hard_failures else ["- `(none)`"])

    if forbidden_files:
        lines.extend(["", "## Forbidden files", ""])
        add_all(lines, "forbidden", forbidden_files)

    if out_of_scope_files:
        lines.extend(["", "## Out-of-scope files", ""])
        add_all(lines, "out-of-scope", out_of_scope_files)

    lines.extend([
        "",
        "## Recommendation",
        "",
        recommendation,
        "",
        "## Authority boundary",
        "",
        "This guard may request auto-merge only for generated factory-memory output PRs. Workflow, script, register, deployment, Supabase/RLS, app, and customer-data changes remain human-gated.",
    ])

    return "\n".join(lines) + "\n", exit_code


def main() -> int:
    parser = argparse.ArgumentParser(description="Guard VIF factory auto-merge eligibility")
    parser.add_argument("--pr-number", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--head-branch", required=True)
    parser.add_argument("--is-draft", required=True)
    parser.add_argument("--changed-files-file", required=True)
    parser.add_argument("--comments-file", required=True)
    parser.add_argument("--output-file", required=True)
    args = parser.parse_args()

    report, exit_code = build_report(args)
    Path(args.output_file).write_text(report, encoding="utf-8")
    print(report)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
