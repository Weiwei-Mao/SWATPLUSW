---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: nuts.f90
note_file: nuts.f90
subroutine: nuts
module: []
calls: []
uses_variables: []
input_variables: []
reads: []
writes: []
purpose: "this function calculates the plant stress factor caused by limited; supply of nitrogen or phosphorus"
---

# nuts

> [!info] Summary
> this function calculates the plant stress factor caused by limited; supply of nitrogen or phosphorus

## Basic Information
- **Type**: `subroutine`
- **Source file**: `nuts.f90`
- **Modules used**:
  - (none)
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[pl_nup.f90]]
- [[pl_pup.f90]]

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
