#!/usr/bin/env python3
from pathlib import Path
import re

STATUSES = ["PASS", "PASS_WITH_WARNINGS", "HOLD", "BLOCKED"]
PLACEHOLDER_RE = re.compile(r"(?i)^(|tbd|todo|n/a|na|missing|unknown|placeholder|example|dummy|test|your_key_here|<placeholder>)$")

def rel(path, root):
    try:
        return str(Path(path).relative_to(root))
    except Exception:
        return str(path)

def read_text(path):
    try:
        return Path(path).read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""

def is_placeholder(value):
    return bool(PLACEHOLDER_RE.match(str(value).strip()))

def severity_rollup(results):
    order = {"PASS":0,"PASS_WITH_WARNINGS":1,"HOLD":2,"BLOCKED":3}
    worst = "PASS"
    counts = {k:0 for k in order}
    for result in results:
        status = result.get("status","PASS")
        counts[status] = counts.get(status,0) + 1
        if order.get(status,0) > order.get(worst,0):
            worst = status
    return worst, counts

def finding(file, severity, rule, message, context=""):
    return {"file":file,"severity":severity,"rule":rule,"message":message,"context":context}
