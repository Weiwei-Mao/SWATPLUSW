---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cli_pmeas.f90
note_file: cli_pmeas.f90
subroutine: cli_pmeas
module:
  - climate_module
  - maximum_data_module
  - basin_module
  - input_file_module
  - time_module
calls: []
uses_variables:
  - climate_module.f90#pcp
  - climate_module.f90#pcp_n
  - input_file_module.f90#in_cli
  - input_file_module.f90#in_path_pcp
  - maximum_data_module.f90#db_mx
  - time_module.f90#time
input_variables:
  - climate_module.f90#pcp
  - climate_module.f90#pcp_n
reads:
  - in_cli%pcp_cli
  - pcp(i
  - TRIM(ADJUSTL(in_path_pcp%pcp
writes: []
purpose: ""
---

# cli_pmeas

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cli_pmeas.f90`
- **Modules used**:
  - [[climate_module.f90]]
  - [[maximum_data_module.f90]]
  - [[basin_module.f90]]
  - [[input_file_module.f90]]
  - [[time_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 3 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_date_time.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[climate_module.f90#pcp]] - `climate_measured_data`
- [[climate_module.f90#pcp_n]] - `character(len=50), dimension(:), allocatable`
- [[input_file_module.f90#in_cli]] - `input_cli`
- [[input_file_module.f90#in_path_pcp]] - `input_path_pcp`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[time_module.f90#time]] - `time_current`

**Populated by file reads:**

- [[climate_module.f90#pcp]]
- [[climate_module.f90#pcp_n]]

## File I/O
- **Reads**:
  - [[pcp.cli]]
  - `pcp(i` _(variable; see [[file.cio]])_
  - `TRIM(ADJUSTL(in_path_pcp%pcp` _(variable; see [[file.cio]])_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.

- Line 32, check [[input_file_module.f90#in_cli]] %pcp_cli, precipitation
	- if it does not exist, return
	- Else, read the file [[pcp.cli]]
		- Line 38-47, count lines, imax
		- Line 52-60, read the data, actually, it is file name of precipitation file
		- Line 62-85, open the file, and read the data into [[climate_module.f90#pcp]]
		  This is first part, read number of year, tstep, lat, lon, and elev of the station
		  **tstep** shown in the weather input file, actually, they are **Julian day of year**, not any steps.
		- Line 87-150, read the precipitation data
		  The data are stored in [[climate_module.f90#pcp]] %ts
- End
<!-- USER-NOTES-END -->
