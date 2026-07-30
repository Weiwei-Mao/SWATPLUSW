---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: lsu_read_elements.f90
note_file: lsu_read_elements.f90
subroutine: lsu_read_elements
module:
  - input_file_module
  - maximum_data_module
  - calibration_data_module
  - hydrograph_module
  - output_landscape_module
calls:
  - define_unit_elements
uses_variables:
  - calibration_data_module.f90#lsu_elem
  - calibration_data_module.f90#lsu_out
  - hydrograph_module.f90#defunit_num
  - hydrograph_module.f90#elem_cnt
  - input_file_module.f90#in_regs
  - maximum_data_module.f90#db_mx
  - output_landscape_module.f90#lsu_wb_d
  - output_landscape_module.f90#ruls_a
  - output_landscape_module.f90#ruls_d
  - output_landscape_module.f90#ruls_m
  - output_landscape_module.f90#ruls_y
  - output_landscape_module.f90#runb_a
  - output_landscape_module.f90#runb_d
  - output_landscape_module.f90#runb_m
  - output_landscape_module.f90#runb_y
  - output_landscape_module.f90#rupw_a
  - output_landscape_module.f90#rupw_d
  - output_landscape_module.f90#rupw_m
  - output_landscape_module.f90#rupw_y
  - output_landscape_module.f90#ruwb_a
  - output_landscape_module.f90#ruwb_d
  - output_landscape_module.f90#ruwb_m
  - output_landscape_module.f90#ruwb_y
input_variables:
  - calibration_data_module.f90#lsu_elem
  - calibration_data_module.f90#lsu_out
reads:
  - in_regs%def_lsu
  - in_regs%ele_lsu
writes: []
purpose: ""
---

# lsu_read_elements

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `lsu_read_elements.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[calibration_data_module.f90]]
  - [[hydrograph_module.f90]]
  - [[output_landscape_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 2 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[define_unit_elements.f90]]

**Called by:**

- [[main.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[calibration_data_module.f90#lsu_elem]] - `landscape_elements`
- [[calibration_data_module.f90#lsu_out]] - `landscape_units`
- [[hydrograph_module.f90#defunit_num]] - `integer, dimension (:), allocatable`
- [[hydrograph_module.f90#elem_cnt]] - `integer, dimension (:), allocatable`
- [[input_file_module.f90#in_regs]] - `input_regions`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[output_landscape_module.f90#lsu_wb_d]] - `output_waterbal`
- [[output_landscape_module.f90#ruls_a]] - `output_losses`
- [[output_landscape_module.f90#ruls_d]] - `output_losses`
- [[output_landscape_module.f90#ruls_m]] - `output_losses`
- [[output_landscape_module.f90#ruls_y]] - `output_losses`
- [[output_landscape_module.f90#runb_a]] - `output_nutbal`
- [[output_landscape_module.f90#runb_d]] - `output_nutbal`
- [[output_landscape_module.f90#runb_m]] - `output_nutbal`
- [[output_landscape_module.f90#runb_y]] - `output_nutbal`
- [[output_landscape_module.f90#rupw_a]] - `output_plantweather`
- [[output_landscape_module.f90#rupw_d]] - `output_plantweather`
- [[output_landscape_module.f90#rupw_m]] - `output_plantweather`
- [[output_landscape_module.f90#rupw_y]] - `output_plantweather`
- [[output_landscape_module.f90#ruwb_a]] - `output_waterbal`
- [[output_landscape_module.f90#ruwb_d]] - `output_waterbal`
- [[output_landscape_module.f90#ruwb_m]] - `output_waterbal`
- [[output_landscape_module.f90#ruwb_y]] - `output_waterbal`

**Populated by file reads:**

- [[calibration_data_module.f90#lsu_elem]]
- [[calibration_data_module.f90#lsu_out]]

## File I/O
- **Reads**:
  - [[ls_unit.def]]
  - [[ls_unit.ele]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.

- Read from [[input_file_module.f90#in_regs]] %def_lsu, [[ls_unit.def]]
- In the input file [[ls_unit.def]]
	- Line 2, mlsu, lsu numbers
	- Other lines
		- id
		- name
		- area
		- elem_tot
		- elements
- Line 99, read [[input_file_module.f90#in_regs]] %ele_lsu, [[ls_unit.ele]]
	- Read parameters
		- id
		- name
		- obj_type, hru/hru-lte, etc
		- obj_typ_number
		- fraction of element in basin
		- fraction of element in ru
		- fraction of element in calibration region
- End














<!-- USER-NOTES-END -->
