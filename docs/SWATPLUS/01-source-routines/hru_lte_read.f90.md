---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hru_lte_read.f90
note_file: hru_lte_read.f90
subroutine: hru_lte_read
module:
  - maximum_data_module
  - plant_data_module
  - hru_lte_module
  - hydrograph_module
  - input_file_module
  - output_landscape_module
  - climate_module
  - time_module
  - soil_data_module
  - conditional_module
calls:
  - ascrv
reads:
  - in_hru%hru_ez
writes: []
purpose: ""
---

# hru_lte_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hru_lte_read.f90`
- **Modules used**: [[maximum_data_module.f90]], [[plant_data_module.f90]], [[hru_lte_module.f90]], [[hydrograph_module.f90]], [[input_file_module.f90]], [[output_landscape_module.f90]], [[climate_module.f90]], [[time_module.f90]], [[soil_data_module.f90]], [[conditional_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 1 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[ascrv.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `in_hru%hru_ez` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
