---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: plant_all_init.f90
note_file: plant_all_init.f90
subroutine: plant_all_init
module:
  - plant_module
  - plant_data_module
  - hru_module
  - hydrograph_module
  - maximum_data_module
calls:
  - plant_init
reads: []
writes: []
purpose: ""
---

# plant_all_init

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `plant_all_init.f90`
- **Modules used**: [[plant_module.f90]], [[plant_data_module.f90]], [[hru_module.f90]], [[hydrograph_module.f90]], [[maximum_data_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[plant_init.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
