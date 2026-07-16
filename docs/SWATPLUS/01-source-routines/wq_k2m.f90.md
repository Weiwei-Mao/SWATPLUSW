---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: wq_k2m.f90
note_file: wq_k2m.f90
subroutine: wq_k2m
module:
  - utils
calls: []
reads: []
writes: []
purpose: "This function solves a semi-analytic solution for the QUAL2E equations (cfr Befekadu Woldegiorgis)."
---

# wq_k2m

> [!info] Summary
> This function solves a semi-analytic solution for the QUAL2E equations (cfr Befekadu Woldegiorgis).

## Basic Information
- **Type**: `subroutine`
- **Source file**: `wq_k2m.f90`
- **Modules used**: [[utils.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
