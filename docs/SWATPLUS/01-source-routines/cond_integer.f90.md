---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cond_integer.f90
note_file: cond_integer.f90
subroutine: cond_integer
module:
  - conditional_module
calls: []
uses_variables:
  - conditional_module.f90#d_tbl
input_variables: []
reads: []
writes: []
purpose: ""
---

# cond_integer

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cond_integer.f90`
- **Modules used**:
  - [[conditional_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[conditions.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[conditional_module.f90#d_tbl]] - `decision_table`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
