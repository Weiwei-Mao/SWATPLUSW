---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: rec_read_elements.f90
note_file: rec_read_elements.f90
subroutine: rec_read_elements
module:
  - input_file_module
  - maximum_data_module
  - calibration_data_module
  - hydrograph_module
calls:
  - define_unit_elements
uses_variables:
  - calibration_data_module.f90#pcu_cal
  - calibration_data_module.f90#pcu_elem
  - calibration_data_module.f90#pcu_out
  - calibration_data_module.f90#pcu_reg
  - hydrograph_module.f90#defunit_num
  - hydrograph_module.f90#elem_cnt
  - hydrograph_module.f90#ielem_ru
  - hydrograph_module.f90#recall
  - hydrograph_module.f90#sp_ob
  - hydrograph_module.f90#srec_a
  - hydrograph_module.f90#srec_d
  - hydrograph_module.f90#srec_m
  - hydrograph_module.f90#srec_y
  - input_file_module.f90#in_regs
  - maximum_data_module.f90#db_mx
input_variables:
  - calibration_data_module.f90#pcu_elem
  - calibration_data_module.f90#pcu_out
  - calibration_data_module.f90#pcu_reg
reads:
  - in_regs%def_psc
  - in_regs%def_psc_reg
  - in_regs%ele_psc
writes: []
purpose: ""
---

# rec_read_elements

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `rec_read_elements.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[calibration_data_module.f90]]
  - [[hydrograph_module.f90]]
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
- [[calibration_data_module.f90#pcu_cal]] - `cataloging_units`
- [[calibration_data_module.f90#pcu_elem]] - `landscape_elements`
- [[calibration_data_module.f90#pcu_out]] - `landscape_units`
- [[calibration_data_module.f90#pcu_reg]] - `landscape_units`
- [[hydrograph_module.f90#defunit_num]] - `integer, dimension (:), allocatable`
- [[hydrograph_module.f90#elem_cnt]] - `integer, dimension (:), allocatable`
- [[hydrograph_module.f90#ielem_ru]] - `integer, dimension(:), allocatable`
- [[hydrograph_module.f90#recall]] - `recall_hydrograph_inputs`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[hydrograph_module.f90#srec_a]] - `hyd_output`
- [[hydrograph_module.f90#srec_d]] - `hyd_output`
- [[hydrograph_module.f90#srec_m]] - `hyd_output`
- [[hydrograph_module.f90#srec_y]] - `hyd_output`
- [[input_file_module.f90#in_regs]] - `input_regions`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`

**Populated by file reads:**

- [[calibration_data_module.f90#pcu_elem]]
- [[calibration_data_module.f90#pcu_out]]
- [[calibration_data_module.f90#pcu_reg]]

## File I/O
- **Reads**:
  - [[rec_catunit.def]]
  - [[rec_reg.def]]
  - [[rec_catunit.ele]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
