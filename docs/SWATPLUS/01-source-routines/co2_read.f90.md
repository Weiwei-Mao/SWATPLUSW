---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: co2_read.f90
note_file: co2_read.f90
subroutine: co2_read
module:
  - input_file_module
  - basin_module
  - time_module
  - climate_module
  - output_path_module
calls:
  - open_output_file
uses_variables:
  - basin_module.f90#bsn_prm
  - climate_module.f90#co2y
  - time_module.f90#time
input_variables: []
reads:
  - co2_yr.dat
writes:
  - co2.out
purpose: ""
---

# co2_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `co2_read.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[basin_module.f90]]
  - [[time_module.f90]]
  - [[climate_module.f90]]
  - [[output_path_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 1 | **Files written**: 1

## Call Relationships
**This routine calls:**

- [[output_path_module.f90#open_output_file]]

**Called by:**

- [[proc_bsn.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_prm]] - `basin_parms`
- [[climate_module.f90#co2y]] - `real, dimension(:), allocatable`
- [[time_module.f90#time]] - `time_current`

## File I/O
- **Writes**:
  - [[co2.out]]
- **Reads**:
  - [[co2_yr.dat]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
- Line 35, call [[output_path_module.f90#open_output_file]]
	- Open [[co2.out]]
- Line 40-64, Read from [[co2_yr.dat]] if available
- Line 68-75, Set variable *co2_y* from [[basin_module.f90#basin_parms]] %CO2
- Line 77-85, simulation after [[co2.out]]'s year, using the last value
- Line 87-104, simulation before  [[co2.out]]'s year, using the first value
- Line 106-111, wirte [[co2.out]]
- End
<!-- USER-NOTES-END -->
