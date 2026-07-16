---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cond_integer_c.f90
note_file: cond_integer_c.f90
subroutine: cond_integer_c
module:
  - reservoir_conditions_module
calls: []
uses_variables:
  - reservoir_conditions_module.f90#hit
input_variables: []
reads: []
writes: []
purpose: ""
---

# cond_integer_c

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cond_integer_c.f90`
- **Modules used**:
  - [[reservoir_conditions_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[res_rel_conds.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[reservoir_conditions_module.f90#hit]] - `character(1)`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
