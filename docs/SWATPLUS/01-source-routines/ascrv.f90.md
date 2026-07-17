---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ascrv.f90
note_file: ascrv.f90
subroutine: ascrv
module: []
calls: []
uses_variables: []
input_variables: []
reads: []
writes: []
purpose: "this subroutine computes shape parameters x5 and x6 for the S curve; equation x = y/(y + exp(x5 + x6*y)) given 2 (x,y) points along the curve.; x5 is determined by solving the equation with x and y values measured"
---

# ascrv

> [!info] Summary
> this subroutine computes shape parameters x5 and x6 for the S curve; equation x = y/(y + exp(x5 + x6*y)) given 2 (x,y) points along the curve.; x5 is determined by solving the equation with x and y values measured

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ascrv.f90`
- **Modules used**:
  - (none)
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[caltsoft_hyd.f90]]
- [[curno.f90]]
- [[hru_lte_read.f90]]
- [[plantparm_init.f90]]
- [[topohyd_init.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
(No module-level variable references detected.)

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
