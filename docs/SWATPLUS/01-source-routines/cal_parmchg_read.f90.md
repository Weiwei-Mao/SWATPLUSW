---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cal_parmchg_read.f90
note_file: cal_parmchg_read.f90
subroutine: cal_parmchg_read
module:
  - input_file_module
  - maximum_data_module
  - calibration_data_module
  - hydrograph_module
  - gwflow_module
calls:
  - define_unit_elements
uses_variables:
  - calibration_data_module.f90#cal_parms
  - calibration_data_module.f90#cal_upd
  - gwflow_module.f90#ncell
  - hydrograph_module.f90#aqu
  - hydrograph_module.f90#defunit_num
  - hydrograph_module.f90#elem_cnt
  - hydrograph_module.f90#res
  - hydrograph_module.f90#sp_ob
  - input_file_module.f90#in_chg
  - maximum_data_module.f90#db_mx
input_variables:
  - calibration_data_module.f90#cal_upd
reads:
  - in_chg%cal_upd
writes: []
purpose: "this function computes new parameter value based on; user defined change"
---

# cal_parmchg_read

> [!info] Summary
> this function computes new parameter value based on; user defined change

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cal_parmchg_read.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[calibration_data_module.f90]]
  - [[hydrograph_module.f90]]
  - [[gwflow_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 1 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[define_unit_elements.f90]]

**Called by:**

- [[main.f90]]
- [[proc_cal.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[calibration_data_module.f90#cal_parms]] - `calibration_parameters`
- [[calibration_data_module.f90#cal_upd]] - `update_parameters`
- [[gwflow_module.f90#ncell]] - `integer`
- [[hydrograph_module.f90#aqu]] - `hyd_output`
- [[hydrograph_module.f90#defunit_num]] - `integer, dimension (:), allocatable`
- [[hydrograph_module.f90#elem_cnt]] - `integer, dimension (:), allocatable`
- [[hydrograph_module.f90#res]] - `hyd_output`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[input_file_module.f90#in_chg]] - `input_chg`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`

**Populated by file reads:**

- [[calibration_data_module.f90#cal_upd]]

## File I/O
- **Reads**:
  - [[calibration.cal]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
