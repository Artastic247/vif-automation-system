# Repo-local execution guard

This file is not the full factory doctrine. It is a local guard.

Rules:
- No build without approved job card.
- No PASS without evidence.
- No app code outside job-card scope.
- No secrets, customer data, Supabase/RLS/deployment changes unless specifically approved.
- Stop on missing source truth, failed verification, scope drift, or unsafe data exposure.
