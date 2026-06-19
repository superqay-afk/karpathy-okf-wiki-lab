# Errors

Command failures and integration errors.

---

## ERR-20260619-001 init-skill-metadata

Logged: 2026-06-19T00:00:00+08:00
Priority: low
Status: resolved
Area: skills

### Symptom
`init_skill.py` created skill directories but rejected short UI descriptions.

### Root Cause
`agents/openai.yaml` `short_description` must be 25-64 characters.

### Fix
Added valid `agents/openai.yaml` files and reran `quick_validate.py`.
