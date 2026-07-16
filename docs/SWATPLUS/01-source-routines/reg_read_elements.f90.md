---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: reg_read_elements.f90
note_file: reg_read_elements.f90
subroutine: reg_read_elements
module:
  - input_file_module
  - maximum_data_module
  - calibration_data_module
  - landuse_data_module
  - hydrograph_module
  - hru_module
  - output_landscape_module
calls:
  - define_unit_elements
uses_variables:
  - calibration_data_module.f90#lsu_elem
  - calibration_data_module.f90#lsu_out
  - calibration_data_module.f90#lsu_reg
  - calibration_data_module.f90#reg_elem
  - calibration_data_module.f90#region
  - hru_module.f90#hru
  - hru_module.f90#ihru
  - hydrograph_module.f90#defunit_num
  - hydrograph_module.f90#elem_cnt
  - hydrograph_module.f90#sp_ob
  - input_file_module.f90#in_regs
  - landuse_data_module.f90#lum
  - landuse_data_module.f90#lum_grp
  - maximum_data_module.f90#db_mx
  - output_landscape_module.f90#rls_a
  - output_landscape_module.f90#rls_d
  - output_landscape_module.f90#rls_m
  - output_landscape_module.f90#rls_y
  - output_landscape_module.f90#rnb_a
  - output_landscape_module.f90#rnb_d
  - output_landscape_module.f90#rnb_m
  - output_landscape_module.f90#rnb_y
  - output_landscape_module.f90#rpw_a
  - output_landscape_module.f90#rpw_d
  - output_landscape_module.f90#rpw_m
  - output_landscape_module.f90#rpw_y
  - output_landscape_module.f90#rwb_a
  - output_landscape_module.f90#rwb_d
  - output_landscape_module.f90#rwb_m
  - output_landscape_module.f90#rwb_y
input_variables:
  - calibration_data_module.f90#lsu_reg
  - calibration_data_module.f90#reg_elem
  - landuse_data_module.f90#lum_grp
reads:
  - in_regs%def_reg
  - in_regs%ele_reg
writes: []
purpose: ""
---

# reg_read_elements

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `reg_read_elements.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[calibration_data_module.f90]]
  - [[landuse_data_module.f90]]
  - [[hydrograph_module.f90]]
  - [[hru_module.f90]]
  - [[output_landscape_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 2 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[define_unit_elements.f90]]

**Called by:**

(No static callers detected.)

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[calibration_data_module.f90#lsu_elem]] - `landscape_elements`
- [[calibration_data_module.f90#lsu_out]] - `landscape_units`
- [[calibration_data_module.f90#lsu_reg]] - `landscape_units`
- [[calibration_data_module.f90#reg_elem]] - `landscape_region_elements`
- [[calibration_data_module.f90#region]] - `cataloging_units`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#ihru]] - `integer`
- [[hydrograph_module.f90#defunit_num]] - `integer, dimension (:), allocatable`
- [[hydrograph_module.f90#elem_cnt]] - `integer, dimension (:), allocatable`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[input_file_module.f90#in_regs]] - `input_regions`
- [[landuse_data_module.f90#lum]] - `land_use_management`
- [[landuse_data_module.f90#lum_grp]] - `land_use_mgt_groups`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[output_landscape_module.f90#rls_a]] - `regional_output_losses`
- [[output_landscape_module.f90#rls_d]] - `regional_output_losses`
- [[output_landscape_module.f90#rls_m]] - `regional_output_losses`
- [[output_landscape_module.f90#rls_y]] - `regional_output_losses`
- [[output_landscape_module.f90#rnb_a]] - `regional_output_nutbal`
- [[output_landscape_module.f90#rnb_d]] - `regional_output_nutbal`
- [[output_landscape_module.f90#rnb_m]] - `regional_output_nutbal`
- [[output_landscape_module.f90#rnb_y]] - `regional_output_nutbal`
- [[output_landscape_module.f90#rpw_a]] - `regional_output_plantweather`
- [[output_landscape_module.f90#rpw_d]] - `regional_output_plantweather`
- [[output_landscape_module.f90#rpw_m]] - `regional_output_plantweather`
- [[output_landscape_module.f90#rpw_y]] - `regional_output_plantweather`
- [[output_landscape_module.f90#rwb_a]] - `regional_output_waterbal`
- [[output_landscape_module.f90#rwb_d]] - `regional_output_waterbal`
- [[output_landscape_module.f90#rwb_m]] - `regional_output_waterbal`
- [[output_landscape_module.f90#rwb_y]] - `regional_output_waterbal`

**Populated by file reads:**

- [[calibration_data_module.f90#lsu_reg]]
- [[calibration_data_module.f90#reg_elem]]
- [[landuse_data_module.f90#lum_grp]]

## File I/O
- **Reads**:
  - [[ls_reg.def]]
  - [[ls_reg.ele]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
