---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: res_read_elements.f90
note_file: res_read_elements.f90
subroutine: res_read_elements
module:
  - input_file_module
  - maximum_data_module
  - calibration_data_module
  - hydrograph_module
  - reservoir_module
calls:
  - define_unit_elements
uses_variables:
  - calibration_data_module.f90#rcu_cal
  - calibration_data_module.f90#rcu_elem
  - calibration_data_module.f90#rcu_out
  - calibration_data_module.f90#rcu_reg
  - hydrograph_module.f90#defunit_num
  - hydrograph_module.f90#elem_cnt
  - hydrograph_module.f90#res
  - hydrograph_module.f90#sp_ob
  - input_file_module.f90#in_regs
  - maximum_data_module.f90#db_mx
input_variables:
  - calibration_data_module.f90#rcu_cal
  - calibration_data_module.f90#rcu_elem
  - calibration_data_module.f90#rcu_out
reads:
  - in_regs%def_res
  - in_regs%def_res_reg
  - in_regs%ele_res
writes: []
purpose: ""
---

# res_read_elements

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `res_read_elements.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[calibration_data_module.f90]]
  - [[hydrograph_module.f90]]
  - [[reservoir_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 3 | **Files written**: 0

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
- [[calibration_data_module.f90#rcu_cal]] - `cataloging_units`
- [[calibration_data_module.f90#rcu_elem]] - `landscape_elements`
- [[calibration_data_module.f90#rcu_out]] - `landscape_units`
- [[calibration_data_module.f90#rcu_reg]] - `landscape_units`
- [[hydrograph_module.f90#defunit_num]] - `integer, dimension (:), allocatable`
- [[hydrograph_module.f90#elem_cnt]] - `integer, dimension (:), allocatable`
- [[hydrograph_module.f90#res]] - `hyd_output`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[input_file_module.f90#in_regs]] - `input_regions`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`

**Populated by file reads:**

- [[calibration_data_module.f90#rcu_cal]]
- [[calibration_data_module.f90#rcu_elem]]
- [[calibration_data_module.f90#rcu_out]]

## File I/O
- **Reads**:
  - [[res_catunit.def]]
  - [[res_reg.def]]
  - [[res_catunit.ele]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
