---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: unit_hyd_ru_hru.f90
note_file: unit_hyd_ru_hru.f90
subroutine: unit_hyd_ru_hru
module:
  - hru_module
  - ru_module
  - hydrograph_module
  - time_module
calls:
  - unit_hyd
reads: []
writes: []
purpose: ""
---

# unit_hyd_ru_hru

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `unit_hyd_ru_hru.f90`
- **Modules used**: [[hru_module.f90]], [[ru_module.f90]], [[hydrograph_module.f90]], [[time_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[unit_hyd.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
