---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cli_tmeas.f90
note_file: cli_tmeas.f90
subroutine: cli_tmeas
module:
  - input_file_module
  - climate_module
  - maximum_data_module
  - time_module
calls:
  - xmon
uses_variables:
  - climate_module.f90#tmp
  - climate_module.f90#tmp_n
  - input_file_module.f90#in_cli
  - input_file_module.f90#in_path_tmp
  - maximum_data_module.f90#db_mx
  - time_module.f90#ndays
  - time_module.f90#ndays_leap
  - time_module.f90#ndays_noleap
  - time_module.f90#time
input_variables:
  - climate_module.f90#tmp
  - climate_module.f90#tmp_n
reads:
  - in_cli%tmp_cli
  - tmp(i
  - TRIM(ADJUSTL(in_path_tmp%tmp
writes: []
purpose: ""
---

# cli_tmeas

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cli_tmeas.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[climate_module.f90]]
  - [[maximum_data_module.f90]]
  - [[time_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 3 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[xmon.f90]]

**Called by:**

- [[proc_date_time.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[climate_module.f90#tmp]] - `climate_measured_data`
- [[climate_module.f90#tmp_n]] - `character(len=50), dimension(:), allocatable`
- [[input_file_module.f90#in_cli]] - `input_cli`
- [[input_file_module.f90#in_path_tmp]] - `input_path_tmp`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[time_module.f90#ndays]] - `integer, dimension (13)`
- [[time_module.f90#ndays_leap]] - `integer, dimension (13)`
- [[time_module.f90#ndays_noleap]] - `integer, dimension (13)`
- [[time_module.f90#time]] - `time_current`

**Populated by file reads:**

- [[climate_module.f90#tmp]]
- [[climate_module.f90#tmp_n]]

## File I/O
- **Reads**:
  - [[tmp.cli]]
  - `tmp(i` _(variable; see [[file.cio]])_
  - `TRIM(ADJUSTL(in_path_tmp%tmp` _(variable; see [[file.cio]])_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.

Same as [[cli_pmeas.f90]]

Two values in one line, maximum T, and minimum T

<!-- USER-NOTES-END -->
