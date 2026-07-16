---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hru_lte_control.f90
note_file: hru_lte_control.f90
subroutine: hru_lte_control
module:
  - hru_lte_module
  - hydrograph_module
  - output_landscape_module
  - basin_module
  - climate_module
  - time_module
  - plant_data_module
  - conditional_module
calls:
  - conditions
  - actions
reads: []
writes: []
purpose: ""
---

# hru_lte_control

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hru_lte_control.f90`
- **Modules used**: [[hru_lte_module.f90]], [[hydrograph_module.f90]], [[output_landscape_module.f90]], [[basin_module.f90]], [[climate_module.f90]], [[time_module.f90]], [[plant_data_module.f90]], [[conditional_module.f90]]
- **Subroutine calls**: 2 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[conditions.f90]]
- [[actions.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
