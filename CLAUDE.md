# DSA drill repo

Personal spaced-rep drill rig. Each `problems/pNN_<name>/` has `solution.py` (stub), `tests.py`, `prompt.md` (reference template), `__init__.py`.

## Problem numbering is pedagogical

`pNN_name` — two-digit numeric prefix. Leading `p` required (Python module names can't start with a digit).

**`NN` reflects drill order, not creation order.** Each problem should ideally only depend on patterns from earlier problems.

## When adding new problems

1. **During plan phase:** determine where each new problem fits in the existing progressive sequence. Don't just append at the end.
2. **After creating files:** reorder ALL existing problems as needed so the full set remains progressively sequenced. Use a two-phase rename (→ `tmp_*` → final) to avoid collisions. Clear `problems/__pycache__` after.
3. **Verify:** `.venv/bin/pytest problems/ --tb=no -q` — no collection errors, expected pass/fail counts.

## Conventions

- `__init__.py` required in every problem dir (pytest `tests.py` name-collision fix).
- `conftest.py` auto-wires `solution` fixture from sibling `solution.py`.
- **Brute-force verify every expected test value before writing files.** Stubs must fail cleanly for every case — redesign any that accidentally pass the `pass`-stub.
- Use `_scratch/` for throwaway verification scripts; delete when done.
- Python scripts in this project are in the exec allowlist (`~/.claude/settings.json`).
