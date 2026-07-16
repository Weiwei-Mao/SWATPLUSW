---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: dr_ru.f90
note_file: dr_ru.f90
subroutine: dr_ru
module:
  - hydrograph_module
  - hru_lte_module
  - ru_module
  - hru_module
calls: []
reads: []
writes: []
purpose: ""
---

# dr_ru

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `dr_ru.f90`
- **Modules used**: [[hydrograph_module.f90]], [[hru_lte_module.f90]], [[ru_module.f90]], [[hru_module.f90]]
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
