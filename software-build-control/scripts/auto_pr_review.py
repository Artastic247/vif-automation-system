#!/usr/bin/env python3
"""AUTO-002 deterministic PR review station.

Reviews AUTO-generated PR metadata and changed-file scope, then writes a PASS/HOLD
review result as Markdown. This script intentionally uses only Python stdlib and
performs no external API calls.
"""
from __future__ import annotations

import argparse
import fnmatch
from pathlib import Path
from typing import Iterable, Sequence

AUTO_DOC_PATTERNS = (
    "software-build-control/management-system/**/*.md",
    "software-build-control/01-app-build-line/**/*.md",
)

PLUGIN_PACK_PATTERNS = (
    ".codex/**",
    ".codex-plugin/plugin.json",
)

AUTO_002_COVERAGE_PATTERNS = (
    ".github/workflows/auto-pr-review.yml",
    "software-build-control/scripts/auto_pr_review.py",
)

AUTO_003_FACTORY_MEMORY_PATTERNS = (
    ".codex/AGENTS.md",
    ".github/workflows/factory-memory-ingest.yml",
    "factory-memory/**",
    "software-build-control/scripts/auto_pr_review.py",
    "software-build-control/scripts/factory_memory_ingest.py",
)

AUTO_004_FACTORY_MEMORY_TRIGGER_PATTERNS = (
    ".codex/AGENTS.md",
    ".github/workflows/factory-memory-ingest.yml",
    "factory-memory/registers/FACTORY_MEMORY_REGISTER.md",
    "software-build-control/scripts/auto_pr_review.py",
)

AUTO_005_FACTORY_MEMORY_POLLER_PATTERNS = (
    ".codex/AGENTS.md",
    ".github/workflows/factory-memory-ingest.yml",
    "factory-memory/registers/FACTORY_MEMORY_REGISTER.md",
    "software-build-control/scripts/auto_pr_review.py",
)

AUTO_006_FACTORY_AUTOMATION_COMPLETION_PATTERNS = (
    ".codex/AGENTS.md",
    ".github/workflows/app-build-validate.yml",
    ".github/workflows/auto-doc-control-pr.yml",
    ".github/workflows/auto-pr-review.yml",
    ".github/workflows/control-pack-validate.yml",
    ".github/workflows/factory-auto-merge.yml",
    ".github/workflows/factory-memory-ingest.yml",
    ".github/workflows/main.yml",
    "factory-memory/registers/**",
    "software-build-control/management-system/clause-09-performance-evaluation/**",
    "software-build-control/scripts/auto_pr_review.py",
    "software-build-control/scripts/factory_auto_merge_guard.py",
    "software-build-control/scripts/tests/**",
)

FORBIDDEN_PATTERNS = (
    ".github/workflows/**",
    "software-build-control/reports/**",
    "**/reports/**",
    "*.json",
    "**/*.json",
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
    "software-build-control/scripts/**",
)

REQUIRED_TITLE_TOKENS = ("AUTO:", "Issue #")
REQUIRED_BODY_TOKENS = (
    "workflow_dispatch only",
    "expected-file scope check",
    "no auto-merge",
    "human merge required",
)


def read_lines(path: str) -> list[str]:
    p = Path(path)
    if not p.exists():
        return []
    lines: list[str] = []
    for line in p.read_text(encoding="utf-8-sig").splitlines():
        normalized = line.strip().lstrip("\ufeff")
        if normalized:
            lines.append(normalized)
    return lines


def read_text(path: str) -> str:
    p = Path(path)
    if not p.exists():
        return ""
    return p.read_text(encoding="utf-8")


def matches_any(path: str, patterns: Sequence[str]) -> bool:
    return any(fnmatch.fnmatch(path, pattern) for pattern in patterns)


def review_profile(head_branch: str) -> tuple[str, tuple[str, ...], str]:
    if head_branch.startswith("codex-plugin-"):
        return "Codex plugin pack", PLUGIN_PACK_PATTERNS, "Head branch uses codex-plugin- prefix"
    if head_branch.startswith("auto-issue-") and "auto-006" in head_branch and "factory-automation" in head_branch:
        return "AUTO-006 factory automation completion", AUTO_006_FACTORY_AUTOMATION_COMPLETION_PATTERNS, "Head branch uses controlled AUTO-006 factory-automation prefix"
    if head_branch.startswith("auto-issue-") and "auto-005" in head_branch and "factory-memory" in head_branch and "poller" in head_branch:
        return "AUTO-005 factory memory poller", AUTO_005_FACTORY_MEMORY_POLLER_PATTERNS, "Head branch uses controlled AUTO-005 factory-memory poller prefix"
    if head_branch.startswith("auto-issue-") and "auto-004" in head_branch and "factory-memory" in head_branch and "trigger" in head_branch:
        return "AUTO-004 factory memory trigger", AUTO_004_FACTORY_MEMORY_TRIGGER_PATTERNS, "Head branch uses controlled AUTO-004 factory-memory trigger prefix"
    if head_branch.startswith("auto-issue-") and "auto-003" in head_branch and "factory-memory" in head_branch:
        return "AUTO-003 factory memory pipeline", AUTO_003_FACTORY_MEMORY_PATTERNS, "Head branch uses controlled AUTO-003 factory-memory prefix"
    if head_branch.startswith("auto-issue-") and "auto-002" in head_branch and "coverage" in head_branch:
        return "AUTO-002 coverage repair", AUTO_002_COVERAGE_PATTERNS, "Head branch uses controlled AUTO-002 coverage prefix"
    if head_branch.startswith("auto-issue-"):
        return "AUTO documentation/control", AUTO_DOC_PATTERNS, "Head branch uses auto-issue- prefix"
    return "unsupported", (), "Head branch is not an approved AUTO-002 review branch"


def is_allowed_file(path: str, allowed_patterns: Sequence[str]) -> bool:
    return matches_any(path, allowed_patterns)


def is_forbidden_file(path: str, allowed_patterns: Sequence[str]) -> bool:
    # Controlled exceptions are allowed only when the active review profile names
    # those exact paths. Everything else still passes through the forbidden gate.
    if is_allowed_file(path, allowed_patterns):
        return False
    return matches_any(path, FORBIDDEN_PATTERNS)


def check_tokens(source: str, tokens: Iterable[str]) -> tuple[list[str], list[str]]:
    lower_source = source.lower()
    passed: list[str] = []
    failed: list[str] = []
    for token in tokens:
        if token.lower() in lower_source:
            passed.append(token)
        else:
            failed.append(token)
    return passed, failed


def build_review(args: argparse.Namespace) -> tuple[str, bool]:
    changed_files = read_lines(args.changed_files_file)
    pr_body = read_text(args.body_file)

    checks_passed: list[str] = []
    checks_failed: list[str] = []

    profile_name, allowed_patterns, branch_check = review_profile(args.head_branch)
    if allowed_patterns:
        checks_passed.append(branch_check)
        checks_passed.append(f"Review profile: {profile_name}")
    else:
        checks_failed.append(branch_check)

    if changed_files:
        checks_passed.append("Changed-file list is present")
    else:
        checks_failed.append("Changed-file list is empty")

    forbidden_files = [path for path in changed_files if is_forbidden_file(path, allowed_patterns)]
    out_of_scope_files = [path for path in changed_files if not is_allowed_file(path, allowed_patterns)]

    if forbidden_files:
        checks_failed.append("Forbidden files changed")
    else:
        checks_passed.append("No forbidden files changed")

    if out_of_scope_files:
        checks_failed.append(f"Files outside approved {profile_name} scope changed")
    else:
        checks_passed.append(f"All changed files are inside approved {profile_name} scope")

    title_passed, title_failed = check_tokens(args.title, REQUIRED_TITLE_TOKENS)
    checks_passed.extend([f"PR title contains '{token}'" for token in title_passed])
    checks_failed.extend([f"PR title missing '{token}'" for token in title_failed])

    body_passed, body_failed = check_tokens(pr_body, REQUIRED_BODY_TOKENS)
    checks_passed.extend([f"PR body contains '{token}'" for token in body_passed])
    checks_failed.extend([f"PR body missing '{token}'" for token in body_failed])

    passed = not checks_failed
    result = "PASS" if passed else "HOLD"
    recommendation = "Human may review for merge." if passed else "Do not merge until HOLD items are corrected."

    lines = [
        f"# AUTO-002 Review Result: {result}",
        "",
        f"Repository: `{args.repo}`",
        f"PR number: `#{args.pr_number}`",
        f"Head branch: `{args.head_branch}`",
        f"Review profile: `{profile_name}`",
        f"Title: `{args.title}`",
        "",
        "## Changed files",
        "",
    ]

    if changed_files:
        lines.extend([f"- `{path}`" for path in changed_files])
    else:
        lines.append("- `(none)`")

    lines.extend(["", "## Checks passed", ""])
    if checks_passed:
        lines.extend([f"- {item}" for item in checks_passed])
    else:
        lines.append("- `(none)`")

    lines.extend(["", "## Checks failed", ""])
    if checks_failed:
        lines.extend([f"- {item}" for item in checks_failed])
    else:
        lines.append("- `(none)`")

    if forbidden_files:
        lines.extend(["", "## Forbidden files", ""])
        lines.extend([f"- `{path}`" for path in forbidden_files])

    if out_of_scope_files:
        lines.extend(["", "## Out-of-scope files", ""])
        lines.extend([f"- `{path}`" for path in out_of_scope_files])

    lines.extend([
        "",
        "## Recommendation",
        "",
        recommendation,
        "",
        "## Authority boundary",
        "",
        "AUTO-002 may recommend PASS or HOLD. Human merge authority remains mandatory.",
    ])

    return "\n".join(lines) + "\n", passed


def main() -> int:
    parser = argparse.ArgumentParser(description="AUTO-002 deterministic PR review station")
    parser.add_argument("--repo", required=True)
    parser.add_argument("--pr-number", required=True)
    parser.add_argument("--head-branch", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--body-file", required=True)
    parser.add_argument("--changed-files-file", required=True)
    parser.add_argument("--output-file", required=True)
    parser.add_argument(
        "--fail-on-hold",
        action="store_true",
        help="Return exit code 1 when the deterministic review result is HOLD.",
    )
    args = parser.parse_args()

    review_markdown, passed = build_review(args)
    Path(args.output_file).write_text(review_markdown, encoding="utf-8")
    print(review_markdown)
    if args.fail_on_hold and not passed:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
