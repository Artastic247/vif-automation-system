# Lessons Learned Feedback Standard

## Purpose

This standard defines how evidence from build repositories feeds back into VIF so the factory improves instead of repeating the same manual prompt-and-fix loop.

## Principle

A build repo is allowed to teach the factory, but it must not become the factory. Reusable lessons return to VIF. Product-specific rules stay in the product repo.

## When to capture a lesson

Capture a lesson when one of the following occurs:

- The same prompt failure happens more than once.
- The same CI failure pattern appears in multiple tasks.
- An agent repeatedly changes unrelated files.
- Missing local repo controls cause rework.
- Acceptance criteria were too vague to verify.
- A useful verification command or checklist was discovered.
- A release gate allowed uncertainty to pass too far downstream.
- A protected or confidential logic boundary needed clarification.

## Lesson classification

| Class | Meaning | Destination |
| --- | --- | --- |
| Factory method | Improves VIF-wide agent/gate process | VIF factory-agent-system |
| Template update | Improves reusable repo deployment pack | VIF templates |
| Product rule | Applies only to one app/product | Build repo `AGENTS.md` or `BUILD_CONTROL.md` |
| Known issue | Persistent defect or environment blocker | Build repo `KNOWN_ISSUES.md` |
| Release control | Improves release checklist/gate | VIF and/or build repo release checklist |

## Minimum lesson record

Each lesson must include:

```text
Lesson ID:
Source repo:
Source issue/PR/log:
Date:
Observed failure or improvement:
Root cause:
Impact:
Reusable rule:
Destination file/template:
Action owner:
Status: Proposed / Accepted / Implemented / Rejected
```

## Feedback process

1. Identify the lesson from a real issue, PR, CI failure, or review finding.
2. Classify whether it is factory-wide or product-specific.
3. Update the correct file or raise a task to update it.
4. Do not mix confidential strategic logic into public or product-facing files.
5. Confirm the lesson is written as practical standard work, not abstract theory.
6. Use it in the next task card or repo control deployment.

## Factory-wide lesson example

```text
Lesson ID: VIF-LL-001
Source repo: fmea-app
Source PR: PR-115
Observed failure: Agent matched PFMEA and Control Plan rows by row identity instead of canonical operation identity.
Root cause: Task card did not specify operation identity as the correlation spine.
Impact: Alignment worked only when source row positions matched.
Reusable rule: Where process documents are aligned, canonical operation identity must be prioritised over row/source traceability.
Destination: VIF task-card guidance and relevant product AGENTS.md.
Status: Proposed
```

## Product-specific lesson example

```text
Lesson ID: APP-LL-001
Source repo: fmea-app
Observed failure: UI task attempted to change import alignment logic.
Root cause: Local repo instructions did not explicitly exclude alignment/matching logic for UI-only tasks.
Reusable rule: UI-only tasks must state that import/alignment/matching logic is excluded unless explicitly authorised.
Destination: fmea-app AGENTS.md
Status: Accepted
```

## Control rule

A lesson learned is not accepted because it sounds useful. It is accepted because it is linked to evidence and improves future execution without increasing unnecessary complexity.
