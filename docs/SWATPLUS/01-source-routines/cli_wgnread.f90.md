---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cli_wgnread.f90
note_file: cli_wgnread.f90
subroutine: cli_wgnread
module:
  - input_file_module
  - time_module
  - maximum_data_module
  - climate_module
calls:
  - gcycl
  - cli_initwgn
uses_variables:
  - climate_module.f90#frad
  - climate_module.f90#idg
  - climate_module.f90#rnd2
  - climate_module.f90#rnd3
  - climate_module.f90#rnd8
  - climate_module.f90#rnd9
  - climate_module.f90#rndseed
  - climate_module.f90#wgn
  - climate_module.f90#wgn_n
  - climate_module.f90#wgn_orig
  - climate_module.f90#wgn_pms
  - climate_module.f90#wgncur
  - climate_module.f90#wgnold
  - input_file_module.f90#in_cli
  - maximum_data_module.f90#db_mx
  - time_module.f90#time
input_variables:
  - climate_module.f90#wgn
  - climate_module.f90#wgn_n
reads:
  - in_cli%weat_wgn
writes: []
purpose: ""
---

# cli_wgnread

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cli_wgnread.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[time_module.f90]]
  - [[maximum_data_module.f90]]
  - [[climate_module.f90]]
- **Subroutine calls**: 2 | **Files read**: 1 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[gcycl.f90]]
- [[cli_initwgn.f90]]

**Called by:**

- [[proc_date_time.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[climate_module.f90#frad]] - `real, dimension (:,:), allocatable`
- [[climate_module.f90#idg]] - `integer, dimension (:), allocatable`
- [[climate_module.f90#rnd2]] - `real, dimension (:), allocatable`
- [[climate_module.f90#rnd3]] - `real, dimension (:), allocatable`
- [[climate_module.f90#rnd8]] - `real, dimension (:), allocatable`
- [[climate_module.f90#rnd9]] - `real, dimension (:), allocatable`
- [[climate_module.f90#rndseed]] - `integer, dimension (:,:), allocatable`
- [[climate_module.f90#wgn]] - `weather_generator_db`
- [[climate_module.f90#wgn_n]] - `character(len=50), dimension(:), allocatable`
- [[climate_module.f90#wgn_orig]] - `weather_generator_db`
- [[climate_module.f90#wgn_pms]] - `wgn_parms`
- [[climate_module.f90#wgncur]] - `real, dimension (:,:), allocatable`
- [[climate_module.f90#wgnold]] - `real, dimension (:,:), allocatable`
- [[input_file_module.f90#in_cli]] - `input_cli`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[time_module.f90#time]] - `time_current`

**Populated by file reads:**

- [[climate_module.f90#wgn]]
- [[climate_module.f90#wgn_n]]

## File I/O
- **Reads**:
  - [[weather-wgn.cli]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.

- Line 24, check [[input_file_module.f90#in_cli]] %weat_wgn, [[weather-wgn.cli]] exist or not
- If not, call [[gcycl.f90]], initializes the random number seeds
- Line 44, open the file [[weather-wgn.cli]]
- Line  45-58, numbers of each 12 rows, imax
- Line 60-82, allocations and initial variables
- Line 88, call [[gcycl.f90]]
- Iteration based on numbers of weather stations, each weather station has 14 lines
	- Line 1, name, lat, long, elev, rain_yrs(用于计算 rainhhmx(:) 值的记录最大 0.5 小时降雨量的年数)
	- Line 2, header
	- Line 3-14,
		- Each row is a month
		- Each column,
			- Tmax_ave, Tmin_ave, Tmax_sd, Tmin_sd, ...
	- Line 103, call [[cli_initwgn.f90]], initialize weather generator parameters
- END
<!-- USER-NOTES-END -->
