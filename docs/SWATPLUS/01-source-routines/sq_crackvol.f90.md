---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: sq_crackvol.f90
note_file: sq_crackvol.f90
subroutine: sq_crackvol
module:
  - hru_module
  - soil_module
calls: []
reads: []
writes: []
purpose: "this surboutine computes total crack volume for the soil profile and; modifies surface runoff to account for crack flow"
---

# sq_crackvol

> [!info] Summary
> this surboutine computes total crack volume for the soil profile and; modifies surface runoff to account for crack flow

## Basic Information
- **Type**: `subroutine`
- **Source file**: `sq_crackvol.f90`
- **Modules used**: [[hru_module.f90]], [[soil_module.f90]]
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
