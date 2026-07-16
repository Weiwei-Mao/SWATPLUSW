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
uses_variables:
  - calibration_data_module.f90#plcal
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hydrograph_module.f90#defunit_num
  - hydrograph_module.f90#elem_cnt
  - hydrograph_module.f90#sp_ob
  - input_file_module.f90#in_chg
  - maximum_data_module.f90#db_mx
input_variables:
  - calibration_data_module.f90#plcal
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
- **Modules used**:
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[calibration_data_module.f90]]
  - [[hydrograph_module.f90]]
  - [[hru_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 1 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[define_unit_elements.f90]]

**Called by:**

- [[proc_cal.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[calibration_data_module.f90#plcal]] - `soft_data_calib_plant`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hydrograph_module.f90#defunit_num]] - `integer, dimension (:), allocatable`
- [[hydrograph_module.f90#elem_cnt]] - `integer, dimension (:), allocatable`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[input_file_module.f90#in_chg]] - `input_chg`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`

**Populated by file reads:**

- [[calibration_data_module.f90#plcal]]

## File I/O
- **Reads**:
  - [[plant_gro.sft]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
