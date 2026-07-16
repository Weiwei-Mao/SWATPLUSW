---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pl_read_regions_cal.f90
note_file: pl_read_regions_cal.f90
subroutine: pl_read_regions_cal
module:
  - input_file_module
  - maximum_data_module
  - calibration_data_module
  - hydrograph_module
  - hru_module
calls:
  - define_unit_elements
reads:
  - in_chg%plant_gro_sft
writes: []
purpose: ""
---

# pl_read_regions_cal

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pl_read_regions_cal.f90`
- **Modules used**: [[input_file_module.f90]], [[maximum_data_module.f90]], [[calibration_data_module.f90]], [[hydrograph_module.f90]], [[hru_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 1 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[define_unit_elements.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `in_chg%plant_gro_sft` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
