---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: basin_prm_default.f90
note_file: basin_prm_default.f90
subroutine: basin_prm_default
module:
  - basin_module
  - hru_module
  - utils
calls: []
reads: []
writes: []
purpose: ""
---

# basin_prm_default

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `basin_prm_default.f90`
- **Modules used**: [[basin_module.f90]], [[hru_module.f90]], [[utils.f90]]
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
