# Debug Inbox

Use this file while debugging SWAT+ step by step. Write raw observations here; they do not need to be polished.

Later, Codex can read this file and move stable knowledge into the right place:

- broad code structure -> `docs/model-structure.md`
- input/read/state/output paths -> `docs/input-output.md`
- detailed verified topic -> `docs/topics/*.md`
- unfinished session notes -> keep them in this debug inbox until they are ready to promote

## How To Write

Add new notes at the top of `## Current Debug Notes`.

Keep each step small. A good entry answers:

- Where am I? File, routine, line, breakpoint, or call stack.
- What input or object is active? Scenario, date, object type, index, file, or field.
- What did I see? Watched variables, values, branch taken, output file, or error.
- What do I think it means? Mark this as `verified`, `partial`, or `guess`.
- What is the next step? The next breakpoint, file, variable, or question.

## Current Debug Notes

### 2026-07-13 - Startup to `file.cio`

Status: partial
Scenario: `Osu_1hru`
Source revision: `cb442f7c05fc3bfc34349c446010f452d2737ca0`

#### Raw debugging notes moved from `docs/model-structure.md`

- `main.f90.in` lines 3-7: `use` modules.
- `main.f90.in` lines 9-25: declarations and external routine declarations.
- `main.f90.in` lines 27-37: write the startup banner to the console and `simulation.out`; `simulation.out` uses file unit `9003`.
- `main.f90.in` line 38: open `erosion.txt` with file unit `888`.
- `main.f90.in` line 40: call `proc_bsn`.
- `proc_bsn.f90` lines 2-10: module use, implicit setting, and external declarations.
- `proc_bsn.f90` line 12: call `readcio_read`.
- `readcio_read.f90` lines 2-16: module use and local variable declarations.
- `readcio_read.f90` lines 19-109: check, open, read, and close `file.cio`; `file.cio` uses file unit `107`.
- Stable `file.cio` understanding was promoted into `docs/topics/file-cio.md`.

### 2026-07-13 - <short topic>

Status: guess
Scenario: `Osu_1hru`
Source revision: `cb442f7c05fc3bfc34349c446010f452d2737ca0`

#### Step 1

- Location:
- Breakpoint or call stack:
- Active input/object:
- Watched values:
- Observation:
- Understanding:
- Next step:

#### Step 2

- Location:
- Breakpoint or call stack:
- Active input/object:
- Watched values:
- Observation:
- Understanding:
- Next step:

## Promotion Notes For Codex

When asked to clean this file:

1. Keep raw notes here unless the user asks to remove them.
2. Move only supported conclusions into reader-facing docs.
3. Preserve uncertainty labels. Do not promote a `guess` as verified.
4. If a trace is incomplete, create or update a `partial` topic note instead of overstating it.
5. Link back to this file or a journal note when the raw debugging path matters.
