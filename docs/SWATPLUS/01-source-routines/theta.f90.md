---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: theta.f90
note_file: theta.f90
subroutine: theta
module: []
calls: []
uses_variables: []
input_variables: []
reads: []
writes: []
purpose: "this function corrects rate constants for temperature; Equation is III-52 from QUAL2E"
---

# theta

> [!info] Summary
> this function corrects rate constants for temperature; Equation is III-52 from QUAL2E

## Basic Information
- **Type**: `subroutine`
- **Source file**: `theta.f90`
- **Modules used**:
  - (none)
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

(No static callers detected.)

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
