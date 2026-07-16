---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: cli_hmeas.f90
note_file: cli_hmeas.f90
subroutine: cli_hmeas
module:
  - input_file_module
  - climate_module
  - maximum_data_module
  - time_module
calls: []
uses_variables:
  - climate_module.f90#hmd
  - climate_module.f90#hmd_n
  - input_file_module.f90#in_cli
  - input_file_module.f90#in_path_hmd
  - maximum_data_module.f90#db_mx
  - time_module.f90#time
input_variables:
  - climate_module.f90#hmd
  - climate_module.f90#hmd_n
reads:
  - in_cli%hmd_cli
  - hmd(i
  - TRIM(ADJUSTL(in_path_hmd%hmd
writes: []
purpose: ""
---

# cli_hmeas

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `cli_hmeas.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[climate_module.f90]]
  - [[maximum_data_module.f90]]
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
- [[climate_module.f90#hmd]] - `climate_measured_data`
- [[climate_module.f90#hmd_n]] - `character(len=50), dimension(:), allocatable`
- [[input_file_module.f90#in_cli]] - `input_cli`
- [[input_file_module.f90#in_path_hmd]] - `input_path_hmd`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[time_module.f90#time]] - `time_current`

**Populated by file reads:**

- [[climate_module.f90#hmd]]
- [[climate_module.f90#hmd_n]]

## File I/O
- **Reads**:
  - [[hmd.cli]]
  - `hmd(i` _(variable; see [[file.cio]])_
  - `TRIM(ADJUSTL(in_path_hmd%hmd` _(variable; see [[file.cio]])_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
