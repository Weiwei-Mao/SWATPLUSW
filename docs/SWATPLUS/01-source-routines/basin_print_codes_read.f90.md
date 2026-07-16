---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: basin_print_codes_read.f90
note_file: basin_print_codes_read.f90
subroutine: basin_print_codes_read
module:
  - input_file_module
  - basin_module
  - time_module
calls: []
uses_variables:
  - basin_module.f90#pco
  - input_file_module.f90#in_sim
  - time_module.f90#time
input_variables:
  - basin_module.f90#pco
reads:
  - in_sim%prt
writes: []
purpose: ""
---

# basin_print_codes_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `basin_print_codes_read.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[basin_module.f90]]
  - [[time_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_bsn.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#pco]] - `basin_print_codes`
- [[input_file_module.f90#in_sim]] - `input_sim`
- [[time_module.f90#time]] - `time_current`

**Populated by file reads:**

- [[basin_module.f90#pco]]

## File I/O
- **Reads**:
  - [[print.prt]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.

- Line 17-783, Read input file [[print.prt]], from variable *[[input_file_module.f90#in_sim]]* to get the file name
	- File line 3, 6 parameters
		- nyskip, number of year at the beginning of the simulation to not print output
		- day_start: Julian day to start printing output, for daily only
		- yrc_start, calendar year to start printing output
		- day_end, Julian day to stop printing output, for daily only
		- yrc_end, calendar year to stop printing output
		- interval, print interval within the period
	- For line 5
		- aa_int_cnt, Number of print intervals for average annual output
	- For line 7
		- csvout, csv format
		- dbout, DB format
		- cdfout, NetCDF format
	- For line 9
		- crop_yld, yearly and average annual crop yield
		- mgtout, management output
		- hydcon, hydrograph connection output
		- fdcout, flow duration curve output
	- Then the lines are:
		- basin_wb, water balance
		- basin_nb, nutrient balance
		- basin_ls, losses
		- basin_pw, plant weather
		- basin_aqu,
		- basin_res,
		- basin_cha,
		- basin_sd_cha
		- basin_psc
		- ...
- Line 785-790, reset input data of line 3
	- if <= 0, set to default time or date from [[time_module.f90#time]]
- End
<!-- USER-NOTES-END -->
