---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: header_water_allocation.f90
note_file: header_water_allocation.f90
subroutine: header_water_allocation
module:
  - maximum_data_module
  - water_allocation_module
  - basin_module
  - output_path_module
calls:
  - open_output_file
uses_variables:
  - basin_module.f90#bsn
  - basin_module.f90#pco
  - basin_module.f90#prog
  - maximum_data_module.f90#db_mx
  - water_allocation_module.f90#wallo_hdr
  - water_allocation_module.f90#wallo_hdr_units
input_variables: []
reads: []
writes:
  - water_allo_day.txt
  - water_allo_day.csv
  - water_allo_mon.txt
  - water_allo_mon.csv
  - water_allo_yr.txt
  - water_allo_yr.csv
  - water_allo_aa.txt
  - water_allo_aa.csv
purpose: ""
---

# header_water_allocation

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `header_water_allocation.f90`
- **Modules used**:
  - [[maximum_data_module.f90]]
  - [[water_allocation_module.f90]]
  - [[basin_module.f90]]
  - [[output_path_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 8

## Call Relationships
**This routine calls:**

- [[output_path_module.f90#open_output_file]]

**Called by:**

- [[proc_open.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn]] - `basin_inputs`
- [[basin_module.f90#pco]] - `basin_print_codes`
- [[basin_module.f90#prog]] - `character(len=80)`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[water_allocation_module.f90#wallo_hdr]] - `wallo_header`
- [[water_allocation_module.f90#wallo_hdr_units]] - `wallo_header_units`

## File I/O
- **Writes**:
  - [[water_allo_day.txt]]
  - [[water_allo_day.csv]]
  - [[water_allo_mon.txt]]
  - [[water_allo_mon.csv]]
  - [[water_allo_yr.txt]]
  - [[water_allo_yr.csv]]
  - [[water_allo_aa.txt]]
  - [[water_allo_aa.csv]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
