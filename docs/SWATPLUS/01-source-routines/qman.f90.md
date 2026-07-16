---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: qman.f90
note_file: qman.f90
subroutine: qman
module: []
calls: []
uses_variables: []
input_variables: []
reads: []
writes: []
purpose: "this subroutine calculates flow rate or flow velocity using Manning\"s; equation. If x1 is set to 1, the velocity is calculated. If x1 is set to; cross-sectional area of flow, the flow rate is calculated."
---

# qman

> [!info] Summary
> this subroutine calculates flow rate or flow velocity using Manning"s; equation. If x1 is set to 1, the velocity is calculated. If x1 is set to; cross-sectional area of flow, the flow rate is calculated.

## Basic Information
- **Type**: `subroutine`
- **Source file**: `qman.f90`
- **Modules used**:
  - -
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
