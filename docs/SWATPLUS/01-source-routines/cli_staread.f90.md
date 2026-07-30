---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cli_staread.f90
note_file: cli_staread.f90
subroutine: cli_staread
module:
  - input_file_module
  - maximum_data_module
  - climate_module
  - time_module
  - hydrograph_module
calls:
  - search
uses_variables:
  - climate_module.f90#atmo_n
  - climate_module.f90#atmodep
  - climate_module.f90#hmd_n
  - climate_module.f90#pcp
  - climate_module.f90#pcp_n
  - climate_module.f90#petm_n
  - climate_module.f90#slr_n
  - climate_module.f90#tmp_n
  - climate_module.f90#wgn
  - climate_module.f90#wgn_n
  - climate_module.f90#wnd_n
  - climate_module.f90#wst
  - climate_module.f90#wst_n
  - hydrograph_module.f90#iwst
  - hydrograph_module.f90#ts
  - input_file_module.f90#in_cli
  - maximum_data_module.f90#db_mx
  - time_module.f90#time
input_variables:
  - climate_module.f90#wst
reads:
  - in_cli%weat_sta
writes: []
purpose: ""
---

# cli_staread

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cli_staread.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[maximum_data_module.f90]]
  - [[climate_module.f90]]
  - [[time_module.f90]]
  - [[hydrograph_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 1 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[search.f90]]

**Called by:**

- [[proc_read.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[climate_module.f90#atmo_n]] - `character(len=50), dimension(:), allocatable`
- [[climate_module.f90#atmodep]] - `atmospheric_deposition`
- [[climate_module.f90#hmd_n]] - `character(len=50), dimension(:), allocatable`
- [[climate_module.f90#pcp]] - `climate_measured_data`
- [[climate_module.f90#pcp_n]] - `character(len=50), dimension(:), allocatable`
- [[climate_module.f90#petm_n]] - `character(len=50), dimension(:), allocatable`
- [[climate_module.f90#slr_n]] - `character(len=50), dimension(:), allocatable`
- [[climate_module.f90#tmp_n]] - `character(len=50), dimension(:), allocatable`
- [[climate_module.f90#wgn]] - `weather_generator_db`
- [[climate_module.f90#wgn_n]] - `character(len=50), dimension(:), allocatable`
- [[climate_module.f90#wnd_n]] - `character(len=50), dimension(:), allocatable`
- [[climate_module.f90#wst]] - `weather_station`
- [[climate_module.f90#wst_n]] - `character(len=50), dimension(:), allocatable`
- [[hydrograph_module.f90#iwst]] - `integer`
- [[hydrograph_module.f90#ts]] - `timestep`
- [[input_file_module.f90#in_cli]] - `input_cli`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[time_module.f90#time]] - `time_current`

**Populated by file reads:**

- [[climate_module.f90#wst]]

## File I/O
- **Reads**:
  - [[weather-sta.cli]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.

- Line 27, check [[input_file_module.f90#in_cli]], %wea_sta, [[weather-sta.cli]] exist or not
- Line 34-44, read file and count imax
- Line 46-57, allocation
- Line 68, read [[climate_module.f90#wst]], name and wco_c
	- weather station name
	- weather genrator name
	- gage name for rainfall/temp/solar radiation/humidity/wind/ET/atmodep
- Line 71, based on the name of weather station, search the number
- Then check the files exist or not
- End
<!-- USER-NOTES-END -->
