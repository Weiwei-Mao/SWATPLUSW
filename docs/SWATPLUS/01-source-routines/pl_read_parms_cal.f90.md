---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pl_read_parms_cal.f90
note_file: pl_read_parms_cal.f90
subroutine: pl_read_parms_cal
module:
  - maximum_data_module
  - calibration_data_module
  - hydrograph_module
  - hru_module
  - input_file_module
  - plant_module
calls:
  - define_unit_elements
uses_variables:
  - calibration_data_module.f90#pl_prms
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hru_module.f90#ipl
  - hydrograph_module.f90#defunit_num
  - hydrograph_module.f90#elem_cnt
  - hydrograph_module.f90#sp_ob
  - input_file_module.f90#in_chg
  - maximum_data_module.f90#db_mx
  - plant_module.f90#pcom
input_variables:
  - calibration_data_module.f90#pl_prms
reads:
  - in_chg%plant_parms_sft
writes: []
purpose: ""
---

# pl_read_parms_cal

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pl_read_parms_cal.f90`
- **Modules used**:
  - [[maximum_data_module.f90]]
  - [[calibration_data_module.f90]]
  - [[hydrograph_module.f90]]
  - [[hru_module.f90]]
  - [[input_file_module.f90]]
  - [[plant_module.f90]]
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
- [[calibration_data_module.f90#pl_prms]] - `pl_parm_region`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hru_module.f90#ipl]] - `integer`
- [[hydrograph_module.f90#defunit_num]] - `integer, dimension (:), allocatable`
- [[hydrograph_module.f90#elem_cnt]] - `integer, dimension (:), allocatable`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[input_file_module.f90#in_chg]] - `input_chg`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[plant_module.f90#pcom]] - `plant_community`

**Populated by file reads:**

- [[calibration_data_module.f90#pl_prms]]

## File I/O
- **Reads**:
  - [[plant_parms.sft]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
