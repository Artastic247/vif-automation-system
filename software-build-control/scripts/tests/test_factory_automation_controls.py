import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]


class FactoryAutomationControlTests(unittest.TestCase):
    def test_auto_pr_review_can_fail_status_on_hold(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            body_file = temp / "pr_body.md"
            changed_files_file = temp / "changed_files.txt"
            output_file = temp / "review.md"

            body_file.write_text(
                "\n".join(
                    [
                        "workflow_dispatch only",
                        "expected-file scope check",
                        "no auto-merge",
                        "human merge required",
                    ]
                ),
                encoding="utf-8",
            )
            changed_files_file.write_text(".github/workflows/main.yml\n", encoding="utf-8")

            result = subprocess.run(
                [
                    sys.executable,
                    str(REPO_ROOT / "software-build-control/scripts/auto_pr_review.py"),
                    "--repo",
                    "Artastic247/vif-automation-system",
                    "--pr-number",
                    "87",
                    "--head-branch",
                    "not-approved",
                    "--title",
                    "AUTO: Issue #87 - test hold",
                    "--body-file",
                    str(body_file),
                    "--changed-files-file",
                    str(changed_files_file),
                    "--output-file",
                    str(output_file),
                    "--fail-on-hold",
                ],
                cwd=REPO_ROOT,
                text=True,
                capture_output=True,
            )

            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            self.assertTrue(output_file.exists())
            self.assertIn("AUTO-002 Review Result: HOLD", output_file.read_text(encoding="utf-8"))

    def test_factory_memory_ingest_skips_already_processed_issue(self) -> None:
        workflow = (REPO_ROOT / ".github/workflows/factory-memory-ingest.yml").read_text(encoding="utf-8")

        processed_check = 'PROCESSED_LABEL=$(gh issue view "$ISSUE_NUMBER" --json labels'
        existing_pr_check = "EXISTING_PR_URL=$(gh pr list"
        self.assertIn(processed_check, workflow)
        self.assertIn("Factory memory ingest already marked issue", workflow)
        self.assertLess(workflow.index(processed_check), workflow.index(existing_pr_check))

    def test_factory_memory_ingest_searches_all_pr_states_for_processed_issue_evidence(self) -> None:
        workflow = (REPO_ROOT / ".github/workflows/factory-memory-ingest.yml").read_text(encoding="utf-8")

        processed_block_start = workflow.index("PROCESSED_PR_URL=$(gh pr list")
        processed_block = workflow[processed_block_start : processed_block_start + 240]
        self.assertIn("--state all", processed_block)

    def test_factory_memory_ingest_only_blocks_open_duplicate_prs_after_marker_removed(self) -> None:
        workflow = (REPO_ROOT / ".github/workflows/factory-memory-ingest.yml").read_text(encoding="utf-8")

        duplicate_block_start = workflow.index("EXISTING_PR_URL=$(gh pr list")
        duplicate_block = workflow[duplicate_block_start : duplicate_block_start + 240]
        self.assertIn("--state open", duplicate_block)

    def test_factory_auto_merge_has_clean_pr_fallback(self) -> None:
        workflow = (REPO_ROOT / ".github/workflows/factory-auto-merge.yml").read_text(encoding="utf-8")

        self.assertIn("MERGE_OUTPUT=$(mktemp)", workflow)
        self.assertIn("clean status", workflow)
        self.assertIn('gh pr merge "$PR_NUMBER" --squash --delete-branch --match-head-commit "$HEAD_SHA"', workflow)


if __name__ == "__main__":
    unittest.main()
