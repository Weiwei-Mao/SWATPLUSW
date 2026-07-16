---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: ch_read_elements.f90
note_file: ch_read_elements.f90
subroutine: ch_read_elements
module:
  - input_file_module
  - maximum_data_module
  - calibration_data_module
  - hydrograph_module
  - sd_channel_module
calls:
  - define_unit_elements
uses_variables:
  - calibration_data_module.f90#ccu_cal
  - calibration_data_module.f90#ccu_elem
  - calibration_data_module.f90#ccu_out
  - calibration_data_module.f90#ccu_reg
  - hydrograph_module.f90#defunit_num
  - hydrograph_module.f90#elem_cnt
  - hydrograph_module.f90#res
  - hydrograph_module.f90#sp_ob
  - input_file_module.f90#in_regs
  - maximum_data_module.f90#db_mx
  - sd_channel_module.f90#schsd_a
  - sd_channel_module.f90#schsd_d
  - sd_channel_module.f90#schsd_m
  - sd_channel_module.f90#schsd_y
input_variables:
  - calibration_data_module.f90#ccu_elem
  - calibration_data_module.f90#ccu_out
  - calibration_data_module.f90#ccu_reg
reads:
  - in_regs%def_cha
  - in_regs%def_cha_reg
  - element.ccu
writes: []
purpose: ""
---

# ch_read_elements

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `ch_read_elements.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[calibration_data_module.f90]]
  - [[hydrograph_module.f90]]
  - [[sd_channel_module.f90]]
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
- [[calibration_data_module.f90#ccu_cal]] - `cataloging_units`
- [[calibration_data_module.f90#ccu_elem]] - `landscape_elements`
- [[calibration_data_module.f90#ccu_out]] - `landscape_units`
- [[calibration_data_module.f90#ccu_reg]] - `landscape_units`
- [[hydrograph_module.f90#defunit_num]] - `integer, dimension (:), allocatable`
- [[hydrograph_module.f90#elem_cnt]] - `integer, dimension (:), allocatable`
- [[hydrograph_module.f90#res]] - `hyd_output`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[input_file_module.f90#in_regs]] - `input_regions`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[sd_channel_module.f90#schsd_a]] - `sd_ch_output`
- [[sd_channel_module.f90#schsd_d]] - `sd_ch_output`
- [[sd_channel_module.f90#schsd_m]] - `sd_ch_output`
- [[sd_channel_module.f90#schsd_y]] - `sd_ch_output`

**Populated by file reads:**

- [[calibration_data_module.f90#ccu_elem]]
- [[calibration_data_module.f90#ccu_out]]
- [[calibration_data_module.f90#ccu_reg]]

## File I/O
- **Reads**:
  - [[ch_catunit.def]]
  - [[ch_reg.def]]
  - [[element.ccu]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
