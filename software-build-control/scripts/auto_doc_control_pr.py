#!/usr/bin/env python3
import argparse
import os
import sys
from pathlib import Path

ALLOWED_SCOPES = [
    Path("software-build-control/management-system"),
    Path("software-build-control/01-app-build-line"),
]
EVIDENCE_DIR = Path("artifacts")
EVIDENCE_FILE = EVIDENCE_DIR / "auto-doc-control-summary.md"
EVIDENCE_NOTE_MARKER = "AUTO-001 evidence note:"


def parse_multi_line(value: str):
    if value is None:
        return []
    return [line.strip() for line in value.splitlines() if line.strip()]


def normalize_expected_files(raw_lines):
    paths = []
    for raw in raw_lines:
        path = raw.strip()
        if not path:
            continue
        if Path(path).is_absolute():
            raise ValueError(f"Expected file path must be relative: {path}")
        if ".." in Path(path).parts:
            raise ValueError(f"Expected file path must not contain parent directory traversal: {path}")
        paths.append(Path(path))
    if not paths:
        raise ValueError("No expected files were provided.")
    return paths


def validate_path(path: Path):
    text_path = str(path.as_posix())
    if path.suffix.lower() != ".md":
        raise ValueError(f"Unsupported file type for expected file: {text_path}")
    if any(part == "reports" for part in path.parts):
        raise ValueError(f"Expected file path must not include generated reports folders: {text_path}")
    if path.suffix.lower() == ".json":
        raise ValueError(f"JSON evidence output is forbidden: {text_path}")
    if not any(path == scope or scope in path.parents for scope in ALLOWED_SCOPES):
        raise ValueError(
            f"Expected file path is outside approved scope: {text_path}."
            f" Allowed scopes: {[str(s) + '/**/*.md' for s in ALLOWED_SCOPES]}"
        )


def append_evidence_note(file_path: Path, instruction_text: str):
    if file_path.exists():
        content = file_path.read_text(encoding="utf-8")
    else:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        content = ""

    if EVIDENCE_NOTE_MARKER in content:
        return False

    note_lines = [
        "",
        "> AUTO-001 evidence note: updated by automation execution loop.",
        "> This file was modified as part of a controlled doc control update.",
    ]
    if instruction_text:
        instruction_summary = instruction_text.strip().splitlines()[0]
        if instruction_summary:
            note_lines.append(f"> Instruction summary: {instruction_summary}")
    content = content.rstrip() + "\n" + "\n".join(note_lines) + "\n"
    file_path.write_text(content, encoding="utf-8")
    return True


def ensure_task_class_supported(task_class: str):
    if task_class != "doc_control_update":
        raise ValueError(f"Unsupported task class: {task_class}")


def main():
    parser = argparse.ArgumentParser(description="AUTO-001 documentation control PR executor")
    parser.add_argument("--issue-number", required=True)
    parser.add_argument("--task-class", required=True)
    parser.add_argument("--short-task-name", required=True)
    parser.add_argument("--expected-files-file", required=True)
    parser.add_argument("--instruction-text-file", required=True)
    args = parser.parse_args()

    expected_raw = Path(args.expected_files_file).read_text(encoding="utf-8")
    instruction_text = Path(args.instruction_text_file).read_text(encoding="utf-8")

    expected_files = normalize_expected_files(parse_multi_line(expected_raw))
    for expected_file in expected_files:
        validate_path(expected_file)

    ensure_task_class_supported(args.task_class)

    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)

    updated = []
    skipped = []
    for expected_file in expected_files:
        changed = append_evidence_note(expected_file, instruction_text)
        if changed:
            updated.append(str(expected_file.as_posix()))
        else:
            skipped.append(str(expected_file.as_posix()))

    summary_lines = [
        "# AUTO-001 Automation Summary",
        "",
        f"Issue number: {args.issue_number}",
        f"Task class: {args.task_class}",
        f"Short task name: {args.short_task_name}",
        "",
        "## Instruction text",
        "",
        instruction_text.strip() if instruction_text.strip() else "(none)",
        "",
        "## Expected files",
        "",
    ]
    for expected_file in expected_files:
        summary_lines.append(f"- {expected_file.as_posix()}")
    summary_lines.extend([
        "",
        "## Updated files",
        "",
    ])
    for file_path in updated:
        summary_lines.append(f"- {file_path}")
    if skipped:
        summary_lines.extend([
            "",
            "## Files already contained evidence note",
            "",
        ])
        for file_path in skipped:
            summary_lines.append(f"- {file_path}")
    summary_lines.extend([
        "",
        "## Notes",
        "",
        "- The executor only supports initial task class 'doc_control_update'.",
        "- Generated reports and JSON evidence outputs are rejected.",
        "- This tool does not perform LLM-based rewriting.",
    ])

    EVIDENCE_FILE.write_text("\n".join(summary_lines) + "\n", encoding="utf-8")
    print(f"Summary written to {EVIDENCE_FILE}")

    if not updated and not skipped:
        raise RuntimeError("Executor did not process any expected files.")

    sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
